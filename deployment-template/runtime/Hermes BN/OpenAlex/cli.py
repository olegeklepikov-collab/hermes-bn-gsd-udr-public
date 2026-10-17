import argparse,asyncio,json,sys
from pathlib import Path
from api import call,OPERATIONS
ROOT=Path(__file__).resolve().parent;R=ROOT.parent
ALLOWED={'search_works','get_work','resolve_references','list_citations','search_entities','get_entity','group_works','analyze_works','find_keywords','keyword_search','read_docs','check_oql','calculate_works'}
async def mcp_run(command,name,args):
 sys.path.insert(0,str(R/'hermes-agent'))
 from tools.mcp_tool_config import _load_mcp_config
 from tools.mcp_oauth_manager import get_manager
 from mcp import ClientSession
 from mcp.client.streamable_http import streamable_http_client
 import httpx2
 cfg=_load_mcp_config()['openalex'];auth=get_manager().get_or_build_provider('openalex',cfg['url'],cfg.get('oauth'))
 if not auth:raise ValueError('Complete the separate OpenAlex MCP sign-in')
 async with httpx2.AsyncClient(auth=auth,timeout=180) as http:
  async with streamable_http_client(cfg['url'],http_client=http) as streams:
   async with ClientSession(streams[0],streams[1],read_timeout_seconds=180) as s:
    initialized=await s.initialize();catalog=await s.list_tools()
    if command=='mcp-catalog':
     await s.send_ping();return {'initialize':initialized.model_dump(mode='json',by_alias=True),'tools':catalog.model_dump(mode='json',by_alias=True),'ping':'passed'}
    tools={t.name:t for t in catalog.tools}
    if name not in ALLOWED or name not in tools:raise ValueError('MCP method is not in the selected research set')
    from jsonschema import Draft202012Validator
    Draft202012Validator(tools[name].input_schema).validate(args)
    result=await s.call_tool(name,args);return result.model_dump(mode='json',by_alias=True)
def main():
 p=argparse.ArgumentParser(prog='openalex-bn');p.add_argument('command',choices=['status','catalog','profiles','call','mcp-call','mcp-catalog']);p.add_argument('--name');p.add_argument('--profile');p.add_argument('--params',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
 try:
  profiles=json.loads((ROOT/'config/profiles.json').read_text());args=json.loads(a.params.read_text()) if a.params else {}
  if a.profile:
   preset=profiles[a.profile];a.name=preset['name'];a.command='mcp-call' if preset.get('transport')=='official-mcp' else 'call';args={**preset.get('arguments',{}),**args}
  if a.command=='profiles':result=profiles
  elif a.command=='catalog':result=OPERATIONS
  elif a.command=='status':result=call('service_status')
  elif a.command in ('mcp-call','mcp-catalog'):result=asyncio.run(mcp_run(a.command,a.name,args))
  else:result=call(a.name,args)
  text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
  if a.output:
   a.output.parent.mkdir(parents=True,exist_ok=True)
   with a.output.open('x') as f:f.write(text)
   a.output.chmod(0o600);print(a.output)
  else:print(text,end='')
  if result.get('ok') is False or result.get('isError'):sys.exit(2)
 except Exception as e:
  while isinstance(e,BaseExceptionGroup) and e.exceptions:e=e.exceptions[0]
  print(json.dumps({'ok':False,'error_type':type(e).__name__,'error':'OpenAlex call failed; check access, parameters, free budget and service availability'},ensure_ascii=False),file=sys.stderr);sys.exit(2)
if __name__=='__main__':main()
