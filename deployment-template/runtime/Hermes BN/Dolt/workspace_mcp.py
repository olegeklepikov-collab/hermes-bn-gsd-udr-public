import asyncio,json,uuid
from pathlib import Path
from mcp import types
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from workspace_api import OPS,ROOT,call
async def list_tools(context,params):return types.ListToolsResult(tools=[types.Tool(name=n,description=o['description'],input_schema=o['input_schema']) for n,o in OPS.items()])
async def call_tool(context,params):
 result=await asyncio.to_thread(call,params.name,params.arguments or {});body=json.dumps(result,ensure_ascii=False,default=str)
 if len(body)>80000:
  p=ROOT/'exports'/('workspace-result-'+uuid.uuid4().hex+'.json');p.write_text(body);p.chmod(0o600);body=json.dumps({'ok':result['ok'],'complete_result_file':str(p),'reading_level':'Read the saved result before claiming inspection'})
 return types.CallToolResult(content=[types.TextContent(type='text',text=body)],is_error=not result['ok'])
async def main():
 server=Server('Hermes BN Beads and Dolt workspace',version='1.0.0',instructions='Complements official Beads and Dolt MCP tools with provenance, original-file imports, local exports and full database backups. Tasks, persistent memories and research data are different objects. A task closure or version commit does not prove scientific validity. Preserve source bytes, hashes, branch and commit, missingness, criteria and reading level. Create working branches before imports. Backups are on the same disk and do not include external original files unless separately copied. Restore only into new copies. No network accounts, remote publications, credential disclosure or destructive cleanup.',on_list_tools=list_tools,on_call_tool=call_tool)
 async with stdio_server() as streams:await server.run(streams[0],streams[1],server.create_initialization_options())
if __name__=='__main__':asyncio.run(main())
