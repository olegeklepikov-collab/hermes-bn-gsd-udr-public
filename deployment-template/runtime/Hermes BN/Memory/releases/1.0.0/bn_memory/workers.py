"""Pinned native backends. No autonomous model, arbitrary query or shell execution."""
import asyncio
import contextlib
import hashlib
import json
import os
import sys
import urllib.request
from pathlib import Path

def hashtext(text):return hashlib.sha256(text.encode()).hexdigest()

def http(url,body=None,token=None,timeout=8):
    headers={'Content-Type':'application/json'}
    if token:headers['Authorization']='Bearer '+Path(token).read_text().strip()
    req=urllib.request.Request(url,data=json.dumps(body).encode() if body is not None else None,headers=headers)
    with urllib.request.urlopen(req,timeout=timeout) as response:return json.load(response)

def agentmemory(config,operation,payload):
    base=config['agentmemory_url']
    if operation=='health':return http(base+'/agentmemory/health')
    if operation=='search':
        results=[]
        for scope in payload['scopes']:
            group='bn-memory-'+hashtext(scope)[:24]
            r=http(base+'/agentmemory/search',{'query':payload['query'],'project':group,'agentId':group,'limit':5,'format':'full'})
            for row in r.get('results',[]):
                item=row.get('observation',row);content=item.get('content') or item.get('narrative','')
                try:v=json.loads(content)
                except (ValueError,TypeError):continue
                if v.get('scope')==scope and v.get('id','').startswith('MEM-'):results.append(v)
        return {'records':results,'backend':'agentmemory'}
    row=payload['record'];group='bn-memory-'+hashtext(row['scope'])[:24]
    previous=payload.get('previous',{})
    if previous.get('memory_id'):
        http(base+'/agentmemory/forget',{'memoryId':previous['memory_id']})
    if row['status']=='retracted':return {'status':'deleted','backend':'agentmemory'}
    content=json.dumps({k:row[k] for k in ['id','revision','scope','content','content_hash','source']},ensure_ascii=False)
    r=http(base+'/agentmemory/remember',{'content':content,'project':group,'agentId':group,'concepts':json.loads(row['concepts'])})
    memory=r.get('memory',{})
    if memory.get('content')!=content or memory.get('agentId')!=group or memory.get('project')!=group:raise RuntimeError('agentmemory_readback_mismatch')
    return {'status':'indexed','backend':'agentmemory','memory_id':memory['id'],'content_hash':row['content_hash'],'revision':row['revision'],'readback_verified':True}

async def graphiti_async(config,operation,payload):
    from graphiti_core.driver.neo4j_driver import Neo4jDriver
    d=Neo4jDriver(uri=config['neo4j_uri'],user=config['neo4j_user'],password=Path(config['neo4j_password_file']).read_text().strip(),database='neo4j')
    def rows(value):return [dict(x) for x in value.records]
    try:
        await d.health_check()
        if operation=='health':return {'status':'healthy','backend':'graphiti_core.Neo4jDriver','mode':'typed_provenance_graph'}
        if operation=='search':
            r=await d.execute_query('MATCH (m:BNMemory) WHERE m.scope IN $scopes AND m.active=true '
                'AND (toLower(m.content) CONTAINS toLower($query) OR EXISTS { MATCH (m)-[:MENTIONS]->(t:BNMemoryTopic) WHERE toLower(t.name) CONTAINS toLower($query) }) '
                'OPTIONAL MATCH (m)-[:MENTIONS]->(t:BNMemoryTopic) RETURN m.id AS id,m.revision AS revision,m.content_hash AS content_hash,m.scope AS scope,collect(t.name) AS concepts ORDER BY m.id LIMIT 10',params=payload)
            return {'records':rows(r),'backend':'graphiti/neo4j'}
        row=payload['record'];key=hashtext(row['scope']+':'+row['id']);params={k:row[k] for k in ['id','revision','scope','content','content_hash','source']};params['key']=key
        await d.execute_query('MERGE (m:BNMemory {key:$key}) SET m.id=$id,m.revision=$revision,m.scope=$scope,m.content=$content,m.content_hash=$content_hash,m.source=$source,m.active=$active',params={**params,'active':row['status']=='recorded'})
        await d.execute_query('MATCH (m:BNMemory {key:$key})-[r:MENTIONS]->() DELETE r',params={'key':key})
        if row['status']=='recorded':
            for concept in json.loads(row['concepts']):
                await d.execute_query('MATCH (m:BNMemory {key:$key}) MERGE (t:BNMemoryTopic {key:$topic_key}) SET t.name=$name,t.scope=$scope MERGE (m)-[r:MENTIONS]->(t) SET r.revision=$revision,r.provenance=$source',params={**params,'topic_key':hashtext(row['scope']+':'+concept),'name':concept})
        r=await d.execute_query('MATCH (m:BNMemory {key:$key}) RETURN m.revision AS revision,m.content_hash AS content_hash,m.active AS active',params={'key':key});verified=rows(r)
        if not verified or verified[0]['content_hash']!=row['content_hash'] or verified[0]['revision']!=row['revision']:raise RuntimeError('graph_readback_mismatch')
        return {'status':'indexed' if row['status']=='recorded' else 'deleted','backend':'graphiti/neo4j','revision':row['revision'],'content_hash':row['content_hash'],'readback_verified':True,'inferred_relations':False}
    finally:await d.close()

def zvec(config,operation,payload):
    import zvec as zv
    root=Path(config['state_root'])/'zvec';root.mkdir(exist_ok=True)
    if operation=='health':return {'status':'healthy','version':zv.__version__,'model':'voyage-4-large','dimensions':1024}
    scopes=payload.get('scopes') or [payload['record']['scope']];results=[]
    for scope in scopes:
        path=root/hashtext(scope)[:24]
        if not path.exists():
            if operation=='search':continue
            schema=zv.CollectionSchema(name='bn_memory',vectors=[zv.VectorSchema('embedding',zv.DataType.VECTOR_FP32,1024)],fields=[zv.FieldSchema('record_id',zv.DataType.STRING),zv.FieldSchema('revision',zv.DataType.INT64),zv.FieldSchema('content_hash',zv.DataType.STRING)])
            collection=zv.create_and_open(str(path),schema)
        else:collection=zv.open(str(path))
        try:
            if operation=='search':
                for doc in collection.query(zv.VectorQuery(field_name='embedding',vector=payload['vector']),topk=10):
                    results.append({'id':doc.fields['record_id'],'revision':doc.fields['revision'],'content_hash':doc.fields['content_hash'],'scope':scope,'score':doc.score})
            else:
                row=payload['record'];docid=row['id']
                if row['status']=='retracted':collection.delete(docid)
                else:
                    statuses=collection.upsert([zv.Doc(id=docid,fields={'record_id':row['id'],'revision':row['revision'],'content_hash':row['content_hash']},vectors={'embedding':payload['vector']})])
                    fetched=collection.fetch(docid).get(docid)
                    if fetched is None or fetched.fields.get('content_hash')!=row['content_hash'] or fetched.fields.get('revision')!=row['revision']:raise RuntimeError('zvec_readback_failed')
                collection.flush()
        finally:collection.close()
    return {'records':results,'backend':'zvec','status':'queried' if operation=='search' else 'indexed','dimensions':1024,'readback_verified':operation!='search'}

async def mcp_read(config,operation,payload):
    from mcp import ClientSession,StdioServerParameters
    from mcp.client.stdio import stdio_client
    root=payload['project_root'];state=Path(config['state_root']);env=dict(os.environ)
    env['SERENA_HOME']=str(state/'serena');env['PATH']=config['code_path']
    if operation=='serena':
        command=config['serena_command'];args=['start-mcp-server','--transport','stdio','--project',root,'--mode','planning','--add-mode','no-memories','--enable-web-dashboard','false'];name=payload['tool'];arguments=payload['arguments']
    else:
        import yaml
        workspace=state/('mirage-'+hashtext(root)[:16]+'.yaml')
        workspace.write_text(yaml.safe_dump({'mode':'READ','runtimes':['vfs'],'mounts':{'/project':{'resource':'disk','mode':'READ','config':{'root':root}}}}));workspace.chmod(0o600)
        command=config['mirage_command'];args=['mcp',str(workspace)];name=payload['tool'];arguments=payload['arguments']
    with open(os.devnull,'w') as log:
        async with stdio_client(StdioServerParameters(command=command,args=args,env=env),errlog=log) as (read,write):
            async with ClientSession(read,write) as session:
                await session.initialize();tool_list=await session.list_tools();tools={t.name:getattr(t,'input_schema',None) or getattr(t,'inputSchema',{}) for t in tool_list.tools}
                if name=='__describe__':return {'tools':tools}
                if name not in tools:raise ValueError('read_tool_unavailable')
                if operation=='mirage' and 'path' in arguments:
                    # Preserve exact source version; returned text is checked by the broker.
                    schema=tools[name];pathkey='path' if 'path' in schema.get('properties',{}) else 'virtual_path'
                    arguments={pathkey:arguments['path']}
                result=await session.call_tool(name,arguments)
                if getattr(result,'is_error',False) or getattr(result,'isError',False):raise RuntimeError('native_read_tool_error:'+str([getattr(c,'text','') for c in result.content])[:300])
                return {'backend':operation,'tool':name,'content':[c.text for c in result.content if getattr(c,'type','')=='text']}

def main():
    req=json.load(sys.stdin);config=req['config'];backend=req['backend'];operation=req['operation'];payload=req.get('payload',{})
    if backend=='agentmemory':result=agentmemory(config,operation,payload)
    elif backend=='graphiti':result=asyncio.run(graphiti_async(config,operation,payload))
    elif backend=='zvec':result=zvec(config,operation,payload)
    elif backend in {'serena','mirage'}:result=asyncio.run(mcp_read(config,backend,payload))
    else:raise ValueError('backend_not_allowed')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':
    try:main()
    except Exception as exc:
        def detail(e):
            return ' | '.join(detail(x) for x in e.exceptions) if isinstance(e,BaseExceptionGroup) else type(e).__name__+':'+str(e)[:200]
        print(json.dumps({'status':'unavailable','code':detail(exc)}));sys.exit(2)
