import argparse,asyncio,json,sys
from pathlib import Path
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from workspace_api import OPS,ROOT,call
async def native(server,name,args):
 cmd=ROOT.parent/'bin'/('beads-bn-scoped-mcp' if server=='beads' else 'dolt-bn-mcp')
 async with stdio_client(StdioServerParameters(command=str(cmd))) as streams:
  async with ClientSession(streams[0],streams[1],read_timeout_seconds=180) as c:
   await c.initialize();res=await c.call_tool(name,args);return res.model_dump(mode='json',by_alias=True)
p=argparse.ArgumentParser();p.add_argument('command',choices=['status','catalog','profiles','call']);p.add_argument('--name');p.add_argument('--profile');p.add_argument('--params',type=Path);p.add_argument('--output',type=Path);a=p.parse_args();args=json.loads(a.params.read_text()) if a.params else {}
if a.command=='catalog':res={n:{k:v for k,v in op.items() if k!='fn'} for n,op in OPS.items()}
elif a.command=='profiles':res=json.loads((ROOT/'config/profiles.json').read_text())
elif a.profile:
 cfg=json.loads((ROOT/'config/profiles.json').read_text())[a.profile];args={**cfg['arguments'],**args};missing=set(cfg.get('required',[]))-set(args)
 if missing:res={'ok':False,'error':'Missing profile parameters: '+', '.join(sorted(missing))}
 elif cfg['server']=='beads-dolt':res=call(cfg['method'],args)
 else:res=asyncio.run(native(cfg['server'],cfg['method'],args))
else:res=call('service_status' if a.command=='status' else a.name,args)
s=json.dumps(res,ensure_ascii=False,indent=2,default=str)+'\n'
if a.output:
 with a.output.open('x') as f:f.write(s)
 a.output.chmod(0o600);print(a.output)
else:print(s,end='')
if res.get('ok') is False or res.get('isError'):sys.exit(2)
