import asyncio
import hashlib
import hmac
import json
import sys
import time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool,TextContent,ListToolsResult,CallToolResult
from bn_memory.schemas import SCHEMAS
from bn_memory.broker import Broker
from bn_memory.store import canonical

CONFIG=json.loads(Path(sys.argv[1]).read_text());BROKER=Broker(CONFIG)

async def list_tools(context,params):
    return ListToolsResult(tools=[Tool(name=n,description=d,input_schema={'type':'object','properties':{**p,'_host':{'type':'object','description':'Доверенная привязка Hermes; модель не формирует.'},'_runtime':{'type':'object','description':'Конечный нативный исполнитель; заполняет только расширение Hermes.'}},'required':r,'additionalProperties':False}) for n,(d,p,r) in SCHEMAS.items()])

async def call_tool(context,params):
    try:
        args=dict(params.arguments);host=args.pop('_host',{});signed={'tool':params.name,'args':args,'sid':host.get('sid'),'expires':host.get('expires')}
        expected=hmac.new(Path(CONFIG['host_key']).read_bytes(),canonical(signed).encode(),hashlib.sha256).hexdigest()
        if not isinstance(host.get('sid'),str) or not hmac.compare_digest(expected,host.get('signature','')) or not time.time()<=host.get('expires',0)<=time.time()+120:raise PermissionError('native_memory_signature_required')
        value=await asyncio.to_thread(BROKER.dispatch,host['sid'],params.name,args)
        return CallToolResult(content=[TextContent(type='text',text=canonical(value))])
    except Exception as exc:
        return CallToolResult(is_error=True,content=[TextContent(type='text',text=canonical({'status':'blocked','code':type(exc).__name__+':'+str(exc)[:140]}))])

server=Server('hermes-bn-common-memory',version='1.1.1',on_list_tools=list_tools,on_call_tool=call_tool)
async def main():
    async with stdio_server() as (read,write):await server.run(read,write,server.create_initialization_options())
if __name__=='__main__':asyncio.run(main())
