"""One broker for all BN modules; local authority survives derived-service outages."""
import fcntl
import json
import os
import subprocess
import signal
import time
from pathlib import Path
from bn_memory.store import Store,canonical,sha,SENSITIVE
from bn_memory.workers import http

class Broker:
    def __init__(self,config):
        self.config=config;self.store=Store(config['state_root'],config)

    def worker(self,backend,operation,payload=None):
        executable=self.config['graph_python'] if backend=='graphiti' else self.config['zvec_python'] if backend=='zvec' else self.config['python']
        req={'config':self.config,'backend':backend,'operation':operation,'payload':payload or {}}
        process=subprocess.Popen([executable,str(Path(__file__).with_name('workers.py'))],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=True)
        try:stdout,_=process.communicate(canonical(req),timeout=35 if backend in {'serena','mirage'} else 12)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid,signal.SIGKILL);process.communicate();raise RuntimeError('bounded_backend_timeout')
        finally:
            try:os.killpg(process.pid,signal.SIGTERM)
            except ProcessLookupError:pass
        try:value=json.loads(stdout)
        except ValueError:raise RuntimeError('backend_result_invalid')
        if process.returncode:raise RuntimeError(value.get('code','backend_failed'))
        return value

    def embedding(self,text,input_type):
        if SENSITIVE.search(text):raise ValueError('secret_not_embedding')
        key='VECTOR-'+sha(input_type+':'+text)
        with self.store.db() as c:
            c.execute('BEGIN IMMEDIATE')
            old=c.execute('SELECT vector FROM vectors WHERE id=? AND model=\'voyage-4-large\'',(key,)).fetchone()
            if old:return json.loads(old[0])
            day=time.strftime('%Y-%m-%d',time.gmtime());used=c.execute('SELECT bytes FROM budget WHERE day=?',(day,)).fetchone()
            count=len(text.encode())+256
            if (used[0] if used else 0)+count>self.config['embedding_daily_bytes']:raise RuntimeError('embedding_daily_budget_exhausted')
            c.execute('INSERT INTO budget VALUES(?,?) ON CONFLICT(day) DO UPDATE SET bytes=bytes+excluded.bytes',(day,count))
        r=http(self.config['embedding_url'],{'model':'voyage-4-large','input':[text],'output_dimension':1024,'output_dtype':'float','input_type':input_type,'truncation':False},self.config['voyage_key_file'],timeout=12)
        vector=r['data'][0]['embedding']
        if len(vector)!=1024:raise RuntimeError('embedding_dimension_mismatch')
        with self.store.db() as c:c.execute('INSERT OR IGNORE INTO vectors VALUES(?,1,\'voyage-4-large\',?)',(key,canonical(vector)))
        return vector

    def sync(self,sid,limit=3):
        self.store.writable(sid)
        if type(limit) is not int or not 1<=limit<=10:raise ValueError('sync_limit_invalid')
        lock=Path(self.config['state_root'])/'derived.lock';out=[]
        with lock.open('a') as f:
            try:fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
            except BlockingIOError:return {'status':'busy','results':[]}
            with self.store.db() as c:
                scopes=self.store.scopes(self.store.binding(sid))
                rows=c.execute('SELECT r.*,o.backend FROM outbox o JOIN current u ON o.id=u.id AND o.revision=u.revision JOIN records r ON r.id=o.id AND r.revision=o.revision WHERE o.status!=\'indexed\' AND r.scope IN (?,?,?) LIMIT ?',(*scopes,limit)).fetchall()
            for entry in rows:
                row=dict(entry)
                if row['scope'] not in self.store.scopes(self.store.binding(sid)):continue
                backend=row['backend']
                with self.store.db() as c:
                    old=c.execute('SELECT receipt FROM outbox WHERE id=? AND backend=? AND receipt IS NOT NULL ORDER BY revision DESC LIMIT 1',(row['id'],backend)).fetchone()
                previous=json.loads(old[0]) if old else {}
                payload={'record':row,'previous':previous}
                try:
                    if backend=='zvec' and row['status']=='recorded':payload['vector']=self.embedding(row['content'],'document')
                    result=self.worker(backend,'sync',payload);status='indexed'
                except Exception as exc:result={**previous,'status':'unavailable','code':type(exc).__name__};status='pending'
                with self.store.db() as c:c.execute('UPDATE outbox SET status=?,receipt=? WHERE id=? AND revision=? AND backend=?',(status,canonical(result),row['id'],row['revision'],backend))
                out.append({'id':row['id'],'revision':row['revision'],'backend':backend,**result})
        return {'status':'complete' if all(x.get('status')!='unavailable' for x in out) else 'degraded','results':out}

    def recall(self,sid,args):
        query=args['query'];result=self.store.local_search(sid,query,args.get('limit',5),args.get('offset',0));result['derived']={}
        if args.get('mode','local')=='hybrid':
            scopes=self.store.scopes(self.store.binding(sid));ids={x['id'] for x in result['records']}
            for backend in ['agentmemory','graphiti','zvec']:
                try:
                    payload={'query':query,'scopes':scopes}
                    if backend=='zvec':payload['vector']=self.embedding(query,'query')
                    found=self.worker(backend,'search',payload);valid=[]
                    for item in found.get('records',[]):
                        try:row=self.store.read(sid,item['id'])
                        except (PermissionError,KeyError):continue
                        if row['revision']!=item['revision'] or row['content_hash']!=item['content_hash']:continue
                        valid.append(item)
                        if row['id'] not in ids and len(result['records'])<args.get('limit',5):result['records'].append(row);ids.add(row['id'])
                    result['derived'][backend]={'status':'queried','matches':valid}
                except Exception as exc:result['derived'][backend]={'status':'unavailable','code':type(exc).__name__}
        result['evidence_status']='unreviewed';return result

    def files(self,sid,args):
        root,target=self.store.safe_file(sid,args['path']);action=args.get('action','read')
        if action=='ls':
            if not target.is_dir():raise ValueError('directory_required')
            entries=[]
            for p in sorted(target.iterdir()):
                try:self.store.safe_file(sid,str(p.relative_to(root)))
                except PermissionError:continue
                entries.append(p.name)
            return {'entries':entries[:100],'has_more':len(entries)>100,'backend':'scoped_filesystem'}
        if not target.is_file() or target.stat().st_size>65536:raise ValueError('split_file_required')
        original=target.read_bytes();text=original.decode('utf-8')
        if SENSITIVE.search(text):raise ValueError('private_file_not_context')
        start=args.get('offset',0);limit=args.get('limit',8192)
        if type(start) is not int or start<0 or type(limit) is not int or not 1<=limit<=8192:raise ValueError('page_invalid')
        result=self.worker('mirage','read',{'project_root':str(root),'tool':'read','arguments':{'path':'/project/'+str(target.relative_to(root))}})
        if target.read_bytes()!=original:raise RuntimeError('source_changed_during_read')
        result.update({'path':str(target.relative_to(root)),'source_sha256':sha(text),'text':text[start:start+limit],'offset':start,'next_offset':start+limit if start+limit<len(text) else None,'has_more':start+limit<len(text),'reading_level':'exact_local_text_page'})
        # Backend native return may repeat the whole file; return only the explicit page.
        result.pop('content',None);return result

    def code(self,sid,args):
        root,target=self.store.safe_file(sid,args['path']);action=args['action']
        if action not in {'overview','symbol','references'}:raise ValueError('code_action_invalid')
        if not target.is_file() or target.stat().st_size>1048576:raise ValueError('bounded_code_file_required')
        text=target.read_text()
        if SENSITIVE.search(text):raise ValueError('private_code_not_context')
        relative=str(target.relative_to(root))
        if action=='overview':name='get_symbols_overview';arguments={'relative_path':relative,'depth':1,'max_answer_chars':12000}
        elif action=='symbol':name='find_symbol';arguments={'relative_path':relative,'name_path_pattern':args['symbol'],'include_body':True,'max_answer_chars':12000}
        else:name='find_referencing_symbols';arguments={'relative_path':relative,'name_path':args['symbol'],'max_answer_chars':12000}
        result=self.worker('serena','read',{'project_root':str(root),'tool':name,'arguments':arguments})
        if SENSITIVE.search(canonical(result)):raise ValueError('private_code_result_not_context')
        def paths(value):
            if isinstance(value,dict):
                for key,item in value.items():
                    if key=='relative_path' and isinstance(item,str):yield item
                    elif isinstance(key,str) and key.endswith(('.py','.r','.R','.ts','.js','.sh','.md')):yield key
                    yield from paths(item)
            elif isinstance(value,list):
                for item in value:yield from paths(item)
        for content in result.get('content',[]):
            try:value=json.loads(content)
            except ValueError:continue
            for relative_source in paths(value):self.store.safe_file(sid,relative_source)
        if sha(target.read_text())!=sha(text):raise RuntimeError('code_changed_during_read')
        if len(canonical(result).encode())>16384:raise ValueError('narrow_symbol_query_required')
        return {**result,'source_sha256':sha(text),'path':relative,'reading_level':'native_symbol_lookup'}

    def dispatch(self,sid,name,args):
        runtime=args.pop('_runtime',None)
        if name.startswith('knowledge_'):
            from bn_memory.knowledge import Knowledge
            knowledge=Knowledge(self)
            if name=='knowledge_ingest':return knowledge.ingest(sid,args,runtime)
            if name=='knowledge_query':return knowledge.query(sid,args,runtime)
            if name=='knowledge_manage':return knowledge.manage(sid,args,runtime)
        if name=='memory_recall':
            result=self.recall(sid,args)
            if args.get('mode')=='hybrid' and self.config.get('cognee_enabled'):
                try:
                    from bn_memory.knowledge import Knowledge
                    result['knowledge_context']=Knowledge(self).query(sid,{'query':args['query'],'limit':3,'mode':'hybrid'},runtime)
                except Exception as exc:result['knowledge_context']={'status':'unavailable','code':type(exc).__name__}
            return result
        if name=='memory_record':
            if args.get('source_ref','').startswith('local:'):
                _,original=self.store.safe_file(sid,args['source_ref'][6:])
                raw=original.read_text()
                if SENSITIVE.search(raw):raise ValueError('private_source_not_memory')
                if args['kind']=='source' and args['content'] not in raw:raise ValueError('source_quote_not_exact')
                args={**args,'source_ref':args['source_ref']+'#sha256='+sha(raw)}
            r=self.store.record(sid,args);return {**r,'indexes':self.sync(sid,3)}
        if name=='memory_read':return self.store.read(sid,args['id'],args.get('revision'))
        if name=='memory_retract':
            r=self.store.retract(sid,args['id'],args['expected_revision']);return {**r,'indexes':self.sync(sid,3)}
        if name=='memory_sync':return self.sync(sid,args.get('limit',3))
        if name=='memory_scope':return self.store.select_project(sid,args['project'])
        if name=='memory_status':return self.store.status(sid)
        if name=='memory_files':return self.files(sid,args)
        if name=='memory_code':return self.code(sid,args)
        raise ValueError('unknown_memory_tool')
