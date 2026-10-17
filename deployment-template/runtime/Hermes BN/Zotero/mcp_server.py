import asyncio, base64, json
from pathlib import Path
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from mcp import types
from api import OPERATIONS, call

async def list_tools(context, params):
    return types.ListToolsResult(tools=[types.Tool(name=n, description=o['description'], input_schema=o['input_schema']) for n,o in OPERATIONS.items()])

async def call_tool(context, params):
    result = await asyncio.to_thread(call, params.name, params.arguments or {})
    body = json.dumps(result, ensure_ascii=False)
    if len(body) > 180000:
        import uuid
        output = Path(__file__).parent/'checks'/('response-'+uuid.uuid4().hex+'.json')
        output.write_text(body); output.chmod(0o600)
        body = json.dumps({'ok':result.get('ok'), 'operation':params.name, 'complete_result_file':str(output),
                           'reading_level':'Response saved to a local file; read it before claiming content reading'},ensure_ascii=False)
    content = [types.TextContent(type='text',text=body)]
    if result.get('ok') and result.get('image_path'):
        content.append(types.ImageContent(type='image',mime_type='image/png',data=base64.b64encode(Path(result['image_path']).read_bytes()).decode()))
    return types.CallToolResult(content=content, is_error=not result.get('ok',True))

async def main():
    server = Server('Hermes BN Zotero',version='1.0.0',
        instructions='Official Zotero 10 local API, pinned independent instance on AgentRuntime2. Search and metadata do not establish full article reading. Track indexed coverage, returned page/text slices, original PDF versus notes, DOI and date discrepancies. Creates and patches are restricted to the personal library; expected_version is local to this server. Inspect partial write failures. No permanent deletion, publication, group writes or silent cloud/provider fallback.',
        on_list_tools=list_tools,on_call_tool=call_tool)
    async with stdio_server() as streams:
        await server.run(streams[0],streams[1],server.create_initialization_options())

if __name__ == '__main__': asyncio.run(main())
