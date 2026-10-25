"""Native lifecycle + mandatory enforcement. No forked model controller."""
import copy
import hashlib
import hmac
import json
import sys
import time
import threading
import contextvars
_document_attempt=contextvars.ContextVar('bn_document_attempt',default=None)
from pathlib import Path

def strings(v):
    if isinstance(v,str):yield v
    elif isinstance(v,dict):
        for x in v.values():yield from strings(x)
    elif isinstance(v,list):
        for x in v:yield from strings(x)

class Host:
    def __init__(self,config_path):
        self.config=json.loads(Path(config_path).read_text());root=Path(self.config['package_root']);manifest=json.loads((root/'manifest.json').read_text())
        for name,digest in manifest.items():
            if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest:raise RuntimeError('common_memory_code_integrity_failed')
        sys.path.insert(0,str(root))
        from bn_memory.broker import Broker
        self.broker=Broker(self.config);self.store=self.broker.store
        self.sync_stop=threading.Event();self.sync_lock=threading.Lock();self.sync_thread=None

    @staticmethod
    def approved_effort(model):
        from hermes_cli.config import load_config_readonly
        from hermes_constants import resolve_reasoning_config
        effort=(resolve_reasoning_config(load_config_readonly(),model) or {}).get('effort')
        if effort not in {'low','medium','high','xhigh'}:raise PermissionError('configured_reasoning_effort_required')
        return effort

    def schedule_sync(self,sid):
        if self.store.binding(sid)['readonly'] or self.sync_stop.is_set():return
        with self.sync_lock:
            if self.sync_thread and self.sync_thread.is_alive():return
            from agent.memory_provider import spawn_context_thread
            def drain():
                try:
                    self.broker.stop_event=self.sync_stop
                    while not self.sync_stop.is_set():
                        result=self.broker.sync_all(10)
                        sources=self.broker.sources()
                        if sources:
                            if not hasattr(self,'_sources_discovered'):
                                sources.discover();self._sources_discovered=True
                            progress=sources.sync(32)
                        else:progress={}
                        if not result.get('results') and not progress.get('processed') and not progress.get('indexed') and not progress.get('blocked'):break
                except Exception:
                    import logging
                    logging.getLogger(__name__).warning('Scoped index catch-up failed; primary memory retained',exc_info=True)
            if hasattr(self,'_sources_discovered'):del self._sources_discovered
            self.sync_thread=spawn_context_thread(drain,name='bn-memory-index-sync')
            self.sync_thread.start()

    def close(self):
        self.sync_stop.set()
        if self.sync_thread:self.sync_thread.join(timeout=15)

    def document_store(self):
        from bn_memory.documents import Documents
        return Documents(self.broker)

    def document_role(self,sid):
        from hermes_cli.config import load_config_readonly
        cfg=load_config_readonly();entry=(cfg.get('plugins',{}).get('entries',{}).get('bn-gsd') or {})
        path=entry.get('settings',{}).get('settings_file')
        if path:
            from bn_gsd.bridge import Bridge
            value=Bridge(path).call('lookup',{'sid':sid})
            if value.get('job'):return value['job'].get('role')
        udr=(cfg.get('plugins',{}).get('entries',{}).get('bn-udr-host') or {})
        root=udr.get('settings',{}).get('udr_root')
        if root:
            import subprocess
            result=subprocess.run([str(Path(root)/'operator/bn-bridge/rpc')],input=json.dumps({'operation':'document_phase','sid':sid}),text=True,capture_output=True,timeout=45)
            if result.returncode:raise PermissionError('document_phase_authority_unavailable')
            return json.loads(result.stdout).get('phase')
        return None

    def before_turn(self,user_message='',session_id='',parent_session_id='',platform='',turn_id='',**kw):
        from bn_memory.store import SENSITIVE
        self.store.bind(session_id,parent_session_id,subagent=platform=='subagent')
        query=user_message if isinstance(user_message,str) else json.dumps(user_message,ensure_ascii=False)
        query='' if SENSITIVE.search(query) else query[:1024]
        context=self.broker.context(session_id,query,turn_id or hashlib.sha256(query.encode()).hexdigest())
        self.schedule_sync(session_id)
        return {'context':context+'\nFor document corpora or large attachments, load skill_view document-corpus-completeness. Inventory every file; extraction is not reading. Use addressed document_read and document_status; split large corpora with document_partition, retain typed products and reconcile cross-partition contradictions. Required phase gaps forbid full completion.'}

    def child_start(self,parent_session_id='',child_session_id='',**kw):return self.store.bind(child_session_id,parent_session_id,subagent=True)

    def tool_request(self,tool_name,args,session_id='',**kw):
        if not tool_name.startswith('mcp__context__'):return None
        from bn_memory.store import canonical
        clean={k:v for k,v in args.items() if k not in {'_host','_runtime'}};expiry=time.time()+90;name=tool_name.removeprefix('mcp__context__')
        signature=hmac.new(Path(self.config['host_key']).read_bytes(),canonical({'tool':name,'args':clean,'sid':session_id,'expires':expiry}).encode(),hashlib.sha256).hexdigest()
        return {'args':{**clean,'_host':{'sid':session_id,'expires':expiry,'signature':signature}},'source':'bn-common-memory'}

    def tool_execution(self,tool_name,args,next_call,session_id='',tool_call_id='',**kw):
        if tool_name=='read_file':
            from bn_memory.read_adapter import needs_route,execute
            if needs_route(args):return execute(self,args,session_id,tool_call_id,kw)
        name=tool_name.removeprefix('mcp__context__')
        needed=self.config.get('cognee_enabled') and tool_name.startswith('mcp__context__') and (name in {'knowledge_ingest','knowledge_query','knowledge_manage'} or name=='memory_recall' and args.get('mode','hybrid')=='hybrid')
        if not needed:return next_call(args)
        from bn_memory.cognee_native import NativeProvider
        allow=name=='knowledge_ingest' or name=='knowledge_manage' and args.get('action') in {'enrich','lesson','reindex'} or name=='knowledge_query' and args.get('mode')=='temporal'
        with NativeProvider(self.ctx,self.broker,session_id,allow_models=allow,call_id=tool_call_id) as provider:
            from bn_memory.store import canonical
            clean={k:v for k,v in args.items() if k not in {'_host','_runtime'}}
            clean['_runtime']={'url':provider.url,'token':provider.token}
            expiry=time.time()+90
            signature=hmac.new(Path(self.config['host_key']).read_bytes(),canonical({'tool':name,'args':clean,'sid':session_id,'expires':expiry}).encode(),hashlib.sha256).hexdigest()
            return next_call({**clean,'_host':{'sid':session_id,'expires':expiry,'signature':signature}})

    def tool_control(self,payload,session_id='',**kw):
        from hermes_cli.execution_control import ExecutionDecision
        name=payload['tool_name']
        if name=='read_file':
            try:
                from bn_memory.read_adapter import needs_route,SAFE_ROUTE
                if needs_route(payload.get('args',{})):
                    return ExecutionDecision(bool(SAFE_ROUTE.get()),'Document conversion requires the mandatory safe read adapter; unsafe native/hosted fallback is forbidden')
            except Exception as exc:return ExecutionDecision(False,'Document routing control failed: '+type(exc).__name__)
        if name in {'mcp__exa__web_search_exa','mcp__exa__web_search_advanced_exa'}:
            import re
            args=payload.get('args',{});sites=re.findall(r'(?i)\bsite:([a-z0-9.-]+)',args.get('query',''))
            if sites:
                domains=args.get('includeDomains')
                if name.endswith('__web_search_exa') or not isinstance(domains,list) or not domains or not all(isinstance(d,str) and any(d.lower()==site.lower() or d.lower().endswith('.'+site.lower()) for site in sites) for d in domains):
                    return ExecutionDecision(False,'A site-scoped Exa search requires web_search_advanced_exa with matching includeDomains; query text is not a domain filter')
        if not name.startswith('mcp__context__'):return ExecutionDecision(True)
        try:
            binding=self.store.binding(session_id)
            if binding['readonly'] and name.removeprefix('mcp__context__') not in {'memory_recall','memory_read','memory_status','memory_files','memory_code','knowledge_query','knowledge_manage','document_read','document_status','document_describe'}:raise PermissionError('child_memory_is_read_only')
            if binding['readonly'] and name.endswith('knowledge_manage') and payload['args'].get('action') not in {'status','read_source','read_context'}:raise PermissionError('child_knowledge_is_read_only')
            if binding['readonly'] and name.endswith('knowledge_query') and payload['args'].get('mode')=='temporal':raise PermissionError('temporal_model_step_requires_parent')
            if name.endswith('knowledge_manage') and payload['args'].get('action')=='lesson' and not self.config.get('cognee_lesson_enabled',False):raise PermissionError('cognee_lesson_pipeline_not_accepted')
            # Verify at the trusted boundary as well as inside the server.
            from bn_memory.store import canonical
            args=dict(payload['args']);host=args.pop('_host',{});expected=hmac.new(Path(self.config['host_key']).read_bytes(),canonical({'tool':name.removeprefix('mcp__context__'),'args':args,'sid':session_id,'expires':host.get('expires')}).encode(),hashlib.sha256).hexdigest()
            if host.get('sid')!=session_id or not hmac.compare_digest(expected,host.get('signature','')):raise PermissionError('native_memory_signature_required')
            return ExecutionDecision(True)
        except Exception as exc:return ExecutionDecision(False,str(exc))

    def request(self,request,session_id='',platform='',**kw):
        if not session_id:return None
        b=self.store.binding(session_id)
        if platform=='subagent' and not b['readonly']:raise PermissionError('child_context_inheritance_missing')
        result=copy.deepcopy(request)
        # Preserve the active profile's approved effort after recovery ladders.
        if result.get('model')=='gpt-6.1-sol' and 'input' in result:
            result['reasoning']={**(result.get('reasoning') or {}),'effort':self.approved_effort(result['model'])}
            result['max_output_tokens']=min(result.get('max_output_tokens') or 128000,128000)
        rows=result.get('messages',result.get('input',[]));row=next((x for x in reversed(rows) if x.get('role')=='user'),None)
        if row is None:raise RuntimeError('native_context_envelope_required')
        context=b['context']
        if not context:
            query='\n'.join(strings(row.get('content','')))[:1024]
            context=self.broker.context(session_id,query,'request-fallback')
        if context not in '\n'.join(strings(result)):
            if isinstance(row.get('content'),str):row['content']+='\n'+context
            elif isinstance(row.get('content'),list):row['content'].append({'type':'input_text' if 'input' in result else 'text','text':context})
            else:raise RuntimeError('native_context_envelope_required')
        for pending in self.document_store().pending(session_id):
            present=pending['context'] in '\n'.join(strings(result))
            content=row.get('content')
            if isinstance(content,str):row['content']=[{'type':'input_text' if 'input' in result else 'text','text':content}]
            if not isinstance(row['content'],list):raise RuntimeError('native_document_envelope_required')
            if not present:row['content'].append({'type':'input_text' if 'input' in result else 'text','text':pending['context']})
            if pending['image']:
                import base64
                image=Path(pending['image']).read_bytes()
                if hashlib.sha256(image).hexdigest()!=pending['image_hash']:raise PermissionError('document_visual_integrity_failed')
                encoded='data:image/png;base64,'+base64.b64encode(image).decode()
                if encoded not in list(strings(result)):
                    row['content'].append({'type':'input_image','image_url':encoded,'detail':'high'} if 'input' in result else {'type':'image_url','image_url':{'url':encoded,'detail':'high'}})
        return {'request':result,'source':'bn-common-memory','reason':'scoped whole-record memory context'}

    def execution(self,request,next_call,**kw):
        r=self.request(request,**kw);info={};token=_document_attempt.set(info)
        try:
            response=next_call(r['request'] if r else request)
        except BaseException:
            if info.get('reference'):self.document_store().confirm_response(kw.get('session_id',''),info['reference'],True)
            raise
        else:
            if info.get('reference'):self.document_store().confirm_response(kw.get('session_id',''),info['reference'],False)
            return response
        finally:_document_attempt.reset(token)

    def model_control(self,payload,session_id='',platform='',execution_kind='',**kw):
        from hermes_cli.execution_control import ExecutionDecision
        if not session_id:
            return ExecutionDecision(execution_kind=='auxiliary','Native memory session required')
        try:
            b=self.store.binding(session_id)
            request=payload['request']
            if request.get('model')=='gpt-6.1-sol' and 'input' in request and (request.get('reasoning') or {}).get('effort')!=self.approved_effort(request['model']):
                raise PermissionError('configured_reasoning_effort_not_delivered')
            if request.get('model')=='gpt-6.1-sol' and 'input' in request and (type(request.get('max_output_tokens')) is not int or not 0<request['max_output_tokens']<=128000):
                raise PermissionError('bounded_provider_output_required')
            if platform=='subagent' and not b['readonly']:raise PermissionError('child_context_inheritance_missing')
            if not b['context'] or b['context'] not in '\n'.join(strings(payload['request'])):raise PermissionError('required_memory_context_not_delivered')
            with self.store.db() as c:c.execute('INSERT INTO audit(event,sid_hash,at) VALUES(?,?,?)',('context_delivered',hashlib.sha256(session_id.encode()).hexdigest(),time.time()))
            api_id=kw.get('api_request_id')
            docs=self.document_store()
            if docs.in_flight(session_id):raise PermissionError('document_delivery_already_in_flight')
            if docs.pending(session_id):
                if not api_id:raise PermissionError('document_delivery_request_id_required')
                from bn_memory.store import canonical,sha
                info=_document_attempt.get()
                if info is None:raise PermissionError('document_model_executor_required')
                retry=kw.get('retry_count',0)
                if type(retry) is not int or retry<0:raise PermissionError('document_native_attempt_number_required')
                reference=api_id+'.attempt-'+str(retry)+'.payload-'+sha(canonical({k:v for k,v in request.items() if k not in {'timeout','http_client'}}))
                docs.schedule_delivery(session_id,request,reference,self.document_role(session_id))
                info['reference']=reference
                return ExecutionDecision(True,on_abort=lambda reason:docs.confirm_response(session_id,reference,True))
            return ExecutionDecision(True)
        except Exception as exc:return ExecutionDecision(False,str(exc))

    def result_control(self,payload,session_id='',tool_call_id='',**kw):
        from hermes_cli.execution_control import ExecutionDecision
        # Successful UDR notes join the same task's memory as unreviewed notes.
        if payload['tool_name']=='mcp__udr__udr_research':
            args=payload['args'].get('request',{});value=payload.get('result')
            if args.get('action')=='note' and isinstance(args.get('text'),str) and not self.store.binding(session_id)['readonly']:
                rendered='\n'.join(strings(value))
                if '"isError": true' not in rendered and '"status":"blocked"' not in rendered:
                    try:self.store.record(session_id,{'content':args['text'],'source_ref':'udr-note:'+','.join(args.get('source_ids',[])),'kind':'note','request_id':'udr-'+hashlib.sha256((tool_call_id+args['text']).encode()).hexdigest()[:24],'scope':'task'})
                    except ValueError:pass  # Oversize/private notes remain in their canonical UDR store.
        return ExecutionDecision(True)

def register(ctx):
    host=Host(ctx.get_config('config_file'))
    host.ctx=ctx
    ctx.on_unload(host.close)
    ctx.register_hook('pre_llm_call',host.before_turn)
    ctx.register_hook('subagent_start',host.child_start)
    ctx.register_middleware('tool_request',host.tool_request)
    ctx.register_middleware('tool_execution',host.tool_execution)
    ctx.register_middleware('llm_request',host.request)
    ctx.register_middleware('llm_execution',host.execution)
    ctx.register_execution_control('tool',host.tool_control)
    ctx.register_execution_control('tool_result',host.result_control)
    ctx.register_execution_control('llm',host.model_control)
    ctx.register_execution_control('auxiliary',host.model_control)
