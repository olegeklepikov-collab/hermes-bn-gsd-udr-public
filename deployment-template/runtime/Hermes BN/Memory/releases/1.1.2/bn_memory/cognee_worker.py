"""Pinned Cognee SDK only; native model/embedding provider must be supplied by the host."""
import asyncio
import dataclasses
import json
import os
import sys
from pathlib import Path

def plain(value):
    if hasattr(value,'model_dump'):return value.model_dump(mode='json')
    if hasattr(value,'to_dict'):return value.to_dict()
    if dataclasses.is_dataclass(value):return dataclasses.asdict(value)
    if isinstance(value,dict):return {str(k):plain(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [plain(x) for x in value]
    return value

async def run(req):
    cfg=req['config'];root=Path(cfg['cognee_root']);runtime=req.get('runtime') or {};state=root/'state/engine'
    state.mkdir(parents=True,exist_ok=True)
    if req['operation']=='parse_pdf':
        from pypdf import PdfReader
        reader=PdfReader(req['payload']['path'])
        if len(reader.pages)>100:raise ValueError('partition_pdf_required')
        return {'text':'\n\n'.join('PAGE '+str(i+1)+'\n'+(p.extract_text() or '') for i,p in enumerate(reader.pages)),'pages':len(reader.pages),'original_already_preserved':True}
    env={'COGNEE_LOGS_DIR':str(root/'state/logs'),'COGNEE_REPOS_DIR':str(root/'state/repos'),'COGNEE_TRACING_ENABLED':'false','TELEMETRY_DISABLED':'true','COGNEE_SKIP_CONNECTION_TEST':'true','ENABLE_BACKEND_ACCESS_CONTROL':'false','AUTO_FEEDBACK':'false','ALLOW_CYPHER_QUERY':'false','LLM_PROVIDER':'custom','LLM_MODEL':'openai/gpt-6.1-sol','LLM_MAX_COMPLETION_TOKENS':'4096','LLM_STRUCTURED_OUTPUT_FRAMEWORK':'litellm_native','EMBEDDING_PROVIDER':'openai_compatible','EMBEDDING_MODEL':'voyage-4-large','EMBEDDING_DIMENSIONS':'1024','EMBEDDING_MAX_COMPLETION_TOKENS':'4096','EMBEDDING_BATCH_SIZE':'16','NO_PROXY':'127.0.0.1,localhost','GRAPH_DATABASE_PROVIDER':'ladybug','VECTOR_DB_PROVIDER':'lancedb','DB_PROVIDER':'sqlite','XDG_CACHE_HOME':str(root/'state/cache'),'HF_HOME':str(root/'state/cache/huggingface'),'IMPROVE_STAGES_DISABLED':'build_truth_subspace'}
    if runtime:
        env.update({'LLM_ENDPOINT':runtime['url'],'LLM_API_KEY':runtime['token'],'EMBEDDING_ENDPOINT':runtime['url'],'EMBEDDING_API_KEY':runtime['token']})
    else:
        env.update({'LLM_ENDPOINT':'http://127.0.0.1:1/v1','LLM_API_KEY':'unavailable','EMBEDDING_ENDPOINT':'http://127.0.0.1:1/v1','EMBEDDING_API_KEY':'unavailable'})
    os.environ.update(env)
    if req['operation']=='lesson':os.environ['AUTO_FEEDBACK']='true'
    os.environ.update({'SYSTEM_ROOT_DIRECTORY':str(state/'system'),'DATA_ROOT_DIRECTORY':str(state/'data'),'CACHE_ROOT_DIRECTORY':str(state/'cache')})
    import cognee
    from importlib.metadata import version
    if version('cognee')!='1.6.3':raise RuntimeError('cognee_version_not_accepted')
    cognee.config.system_root_directory(str(state/'system'));cognee.config.data_root_directory(str(state/'data'))
    from cognee.base_config import get_base_config
    get_base_config().cache_root_directory=str(state/'cache')
    operation=req['operation'];payload=req.get('payload',{})
    if operation=='health':return {'version':version('cognee'),'native':True,'stores':['sqlite','lancedb','ladybug'],'model_executor':'Hermes native leaf','embedding':'voyage-4-large:1024'}
    if not runtime:raise PermissionError('native_runtime_provider_required')
    import urllib.request
    def phase(purpose):
        request=urllib.request.Request(runtime['url']+'/phase',data=json.dumps({'embedding_purpose':purpose}).encode(),headers={'Authorization':'Bearer '+runtime['token'],'Content-Type':'application/json'})
        with urllib.request.urlopen(request,timeout=5) as response:response.read()
    if operation=='resolve_ids':
        datasets=await cognee.datasets.list_datasets();target=next((x for x in datasets if x.name==payload['dataset']),None)
        if target is None:return {'data_ids':[]}
        rows=await cognee.datasets.list_data(target.id);ids=[]
        for row in rows:
            meta=getattr(row,'external_metadata',None)
            if isinstance(meta,str):
                try:meta=json.loads(meta)
                except ValueError:meta=None
            if isinstance(meta,dict) and meta.get('bn_doc_id')==payload['doc_id'] or getattr(row,'label',None)==payload['doc_id']:ids.append(str(row.id))
        return {'data_ids':ids}
    if operation=='ingest':
        from cognee.tasks.ingestion.data_item import DataItem
        from cognee.modules.ontology.rdf_xml.RDFLibOntologyResolver import RDFLibOntologyResolver
        config={'ontology_config':{'ontology_resolver':RDFLibOntologyResolver(ontology_file=str(root/'operator/knowledge-work.owl')),'ontology_mode':'annotate'}}
        if payload['metadata'].get('content_type')=='code':
            directory=root/'state/code-inputs'/payload['doc_id'];directory.mkdir(parents=True,exist_ok=True)
            filename=payload['metadata']['filename'];path=directory/filename;path.write_text(payload['text']);path.chmod(0o600)
            result=await cognee.remember(str(directory),dataset_name=payload['dataset'],content_type='code',index_vectors=True,self_improvement=False,run_in_background=False)
        else:
            item=DataItem(data=payload['text'],label=payload['doc_id'],external_metadata=payload['metadata'],literal_text=True)
            result=await cognee.remember(item,dataset_name=payload['dataset'],chunk_size=1024,self_improvement=False,run_in_background=False,config=config,summary_method='from_extraction')
        return {'operation':'remember','result':plain(result),'evidence_status':'unreviewed'}
    if operation=='query':
        phase('query')
        from cognee.modules.search.types.SearchType import SearchType
        modes={'chunks':SearchType.CHUNKS,'hybrid':SearchType.HYBRID_COMPLETION,'graph':SearchType.GRAPH_COMPLETION,'temporal':SearchType.TEMPORAL,'summaries':SearchType.SUMMARIES}
        result=await cognee.recall(payload['query'],query_type=modes[payload.get('mode','hybrid')],datasets=payload['datasets'],top_k=payload.get('limit',5),only_context=True,auto_route=False,retriever_specific_config={'chunks_top_k':5,'entities_top_k':5,'facts_top_k':5,'max_edges_per_entity':3,'include_external_metadata':True,'external_metadata_keys':['bn_doc_id','source_sha256','source_ref','extent']})
        passages=await cognee.recall(payload['query'],query_type=SearchType.HYBRID_COMPLETION,datasets=payload['datasets'],only_context=True,auto_route=False,retriever_specific_config={'chunks_top_k':5,'entities_top_k':0,'facts_top_k':0,'include_external_metadata':True,'external_metadata_keys':['bn_doc_id','source_sha256','source_ref','extent']})
        return {'operation':'recall','results':plain(result),'passages':plain(passages),'only_context':True,'evidence_status':'unreviewed'}
    if operation=='enrich':
        result=await cognee.improve(dataset=payload['dataset'],build_global_context_index=True,build_truth_subspace=False,run_in_background=False)
        return {'operation':'improve','result':plain(result),'evidence_status':'unreviewed'}
    if operation=='lesson':
        # Session guidance is explicitly supplied from the primary ledger, not a copied transcript.
        session_id=payload['session_id']
        await cognee.remember(payload['text'],dataset_name=payload['dataset'],session_id=session_id,self_improvement=False)
        from cognee.infrastructure.session.get_session_manager import get_session_manager
        manager=get_session_manager()
        # A normal gated session turn records guidance; final answer stays local to this finite operation.
        phase('query');await cognee.recall(payload['text'],datasets=[payload['dataset']],session_id=session_id,query_type=__import__('cognee').SearchType.HYBRID_COMPLETION,only_context=False);phase('document')
        result=await cognee.session.distill_session(session_id,dataset=payload['dataset'])
        return {'operation':'distill_session','result':plain(result),'evidence_status':'unreviewed'}
    if operation=='forget':
        from uuid import UUID
        result=await cognee.forget(dataset=payload['dataset'],data_id=UUID(payload['data_id']) if payload.get('data_id') else None)
        return {'operation':'forget','result':plain(result)}
    raise ValueError('cognee_operation_not_admitted')

def main():
    req=json.load(sys.stdin)
    try:
        result=asyncio.run(run(req));print(json.dumps(plain(result),ensure_ascii=False,default=str))
    except Exception as exc:
        print(json.dumps({'status':'unavailable','code':type(exc).__name__+':'+str(exc)[:220]}));sys.exit(2)
if __name__=='__main__':main()
