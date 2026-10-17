"""Native lifecycle + mandatory enforcement. No forked model controller."""
import copy
import hashlib
import hmac
import json
import sys
import time
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

    def before_turn(self,user_message='',session_id='',parent_session_id='',platform='',turn_id='',**kw):
        from bn_memory.store import SENSITIVE
        self.store.bind(session_id,parent_session_id,subagent=platform=='subagent')
        query=user_message if isinstance(user_message,str) else json.dumps(user_message,ensure_ascii=False)
        query='' if SENSITIVE.search(query) else query[:1024]
        context=self.store.context(session_id,query,turn_id or hashlib.sha256(query.encode()).hexdigest())
        return {'context':context}

    def child_start(self,parent_session_id='',child_session_id='',**kw):return self.store.bind(child_session_id,parent_session_id,subagent=True)

    def tool_request(self,tool_name,args,session_id='',**kw):
        if not tool_name.startswith('mcp__context__'):return None
        from bn_memory.store import canonical
        clean={k:v for k,v in args.items() if k not in {'_host','_runtime'}};expiry=time.time()+90;name=tool_name.removeprefix('mcp__context__')
        signature=hmac.new(Path(self.config['host_key']).read_bytes(),canonical({'tool':name,'args':clean,'sid':session_id,'expires':expiry}).encode(),hashlib.sha256).hexdigest()
        return {'args':{**clean,'_host':{'sid':session_id,'expires':expiry,'signature':signature}},'source':'bn-common-memory'}

    def tool_execution(self,tool_name,args,next_call,session_id='',tool_call_id='',**kw):
        name=tool_name.removeprefix('mcp__context__')
        needed=self.config.get('cognee_enabled') and tool_name.startswith('mcp__context__') and (name in {'knowledge_ingest','knowledge_query','knowledge_manage'} or name=='memory_recall' and args.get('mode')=='hybrid')
        if not needed:return next_call(args)
        from bn_memory.cognee_native import NativeProvider
        allow=name=='knowledge_ingest' or name=='knowledge_manage' and args.get('action') in {'enrich','lesson'} or name=='knowledge_query' and args.get('mode')=='temporal'
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
        if not name.startswith('mcp__context__'):return ExecutionDecision(True)
        try:
            binding=self.store.binding(session_id)
            if binding['readonly'] and name.removeprefix('mcp__context__') not in {'memory_recall','memory_read','memory_status','memory_files','memory_code','knowledge_query','knowledge_manage'}:raise PermissionError('child_memory_is_read_only')
            if binding['readonly'] and name.endswith('knowledge_manage') and payload['args'].get('action') not in {'status','read_source','read_context'}:raise PermissionError('child_knowledge_is_read_only')
            if binding['readonly'] and name.endswith('knowledge_query') and payload['args'].get('mode')=='temporal':raise PermissionError('temporal_model_step_requires_parent')
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
        result=copy.deepcopy(request);rows=result.get('messages',result.get('input',[]));row=next((x for x in reversed(rows) if x.get('role')=='user'),None)
        if row is None:raise RuntimeError('native_context_envelope_required')
        context=b['context']
        if not context:
            query='\n'.join(strings(row.get('content','')))[:1024]
            context=self.store.context(session_id,query,'request-fallback')
        if context not in '\n'.join(strings(result)):
            if isinstance(row.get('content'),str):row['content']+='\n'+context
            elif isinstance(row.get('content'),list):row['content'].append({'type':'input_text' if 'input' in result else 'text','text':context})
            else:raise RuntimeError('native_context_envelope_required')
        return {'request':result,'source':'bn-common-memory','reason':'scoped whole-record memory context'}

    def execution(self,request,next_call,**kw):
        r=self.request(request,**kw);return next_call(r['request'] if r else request)

    def model_control(self,payload,session_id='',platform='',execution_kind='',**kw):
        from hermes_cli.execution_control import ExecutionDecision
        if not session_id:
            return ExecutionDecision(execution_kind=='auxiliary','Native memory session required')
        try:
            b=self.store.binding(session_id)
            if platform=='subagent' and not b['readonly']:raise PermissionError('child_context_inheritance_missing')
            if not b['context'] or b['context'] not in '\n'.join(strings(payload['request'])):raise PermissionError('required_memory_context_not_delivered')
            with self.store.db() as c:c.execute('INSERT INTO audit(event,sid_hash,at) VALUES(?,?,?)',('context_delivered',hashlib.sha256(session_id.encode()).hexdigest(),time.time()))
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
