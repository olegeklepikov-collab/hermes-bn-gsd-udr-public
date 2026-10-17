import asyncio,base64,json,uuid
from pathlib import Path
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from mcp import types
from api import call,OPERATIONS
ROOT=Path(__file__).resolve().parent
async def list_tools(context,params):
 return types.ListToolsResult(tools=[types.Tool(name=n,description=o['description'],input_schema=o['input_schema']) for n,o in OPERATIONS.items()])
async def call_tool(context,params):
 result=await asyncio.to_thread(call,params.name,params.arguments or {});body=json.dumps(result,ensure_ascii=False)
 limit=1400 if result.get('ok') is False else 180000
 if len(body)>limit:
  p=ROOT/'checks'/('tool-result-'+uuid.uuid4().hex+'.json');p.write_text(body);p.chmod(0o600)
  body=json.dumps({'ok':result.get('ok',True),'operation':params.name,'http_status':result.get('http_status'),'complete_result_file':str(p),'reading_level':'Only response location returned; read saved data before claiming reading'},ensure_ascii=False)
 content=[types.TextContent(type='text',text=body)]
 if result.get('ok') and result.get('image_path'):content.append(types.ImageContent(type='image',mime_type='image/png',data=base64.b64encode(Path(result['image_path']).read_bytes()).decode()))
 return types.CallToolResult(content=content,is_error=result.get('ok') is False)
async def main():
 server=Server('Hermes BN OpenAlex API and Content',version='1.0.0',instructions='Official OpenAlex API and content on AgentRuntime2, complementing the official OpenAlex MCP. Read-only account access; no curation, cloud writes or alerts. Credentials never returned. Respect free daily and local setup budgets; no prepaid usage. Metadata, reconstructed abstracts, original PDFs and machine-parsed GROBID TEI are distinct reading levels. Preserve corpus, dates, paging and missingness. Citation counts and FWCI do not establish quality or citation stance. Downloading is not reading. Inspect specified original PDF pages for complex tables. No automatic retry/provider fallback.',on_list_tools=list_tools,on_call_tool=call_tool)
 async with stdio_server() as streams:await server.run(streams[0],streams[1],server.create_initialization_options())
if __name__=='__main__':asyncio.run(main())
