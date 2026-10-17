"""Own local R MCP client; no language-model API or cloud credentials."""
import asyncio, base64, json, os
from pathlib import Path
import jsonschema

P = Path(__file__).resolve().parent
COMMAND = str(P / 'bin/mcp-server-bn')

def load(path):
    return json.loads(Path(path).read_text())

def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'w') as out:
        json.dump(value, out, ensure_ascii=False, indent=2)
        out.write('\n')
    path.chmod(0o600)

async def request(command, name=None, arguments=None):
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    parameters = StdioServerParameters(command=COMMAND, args=[])
    async with stdio_client(parameters) as streams:
        async with ClientSession(streams[0], streams[1], read_timeout_seconds=600) as session:
            init = await session.initialize()
            listing = await session.list_tools()
            tools = {tool.name: tool for tool in listing.tools}
            if command == 'catalog':
                await session.send_ping()
                return {'initialize':init.model_dump(mode='json', by_alias=True),
                        'tools':listing.model_dump(mode='json', by_alias=True),
                        'ping':'passed', 'mode':'local', 'api_key_used':False}
            calls = arguments if command == 'batch' else [{'name':name, 'arguments':arguments or {}}]
            if not isinstance(calls, list) or not 1 <= len(calls) <= 20:
                raise ValueError('От 1 до 20 явных операций за запуск.')
            for call in calls:
                if call['name'] not in tools:
                    raise ValueError('Метод отсутствует в текущем каталоге R.')
                jsonschema.Draft202012Validator(tools[call['name']].input_schema).validate(call.get('arguments', {}))
            results=[]
            for call in calls:
                result = await session.call_tool(call['name'], arguments=call.get('arguments', {}))
                results.append({**call, 'result':result.model_dump(mode='json', by_alias=True)})
                if command == 'batch':
                    save(P/'checks/last-batch-progress.json', {'calls':results,'same_R_process':True})
                if result.is_error:
                    break
            if command == 'call':
                return results[0]['result']
            return {'ok':len(results)==len(calls) and not any(x['result'].get('isError') for x in results),
                    'calls':results,'same_R_process':True,'api_key_used':False}

def save_images(result, target):
    directory=Path(target).resolve()
    if not directory.is_relative_to((P/'exports').resolve()):
        raise ValueError('Изображения клиента сохраняются только в R/exports.')
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    calls=result.get('calls',[{'result':result}])
    paths=[]
    for call_index, call in enumerate(calls,1):
        for image_index, block in enumerate(call['result'].get('content',[]),1):
            if block.get('type')!='image':
                continue
            extension={'image/png':'.png','image/jpeg':'.jpg'}.get(block.get('mimeType'))
            if extension is None:
                raise ValueError('Неизвестный формат изображения R.')
            path=directory/f'call-{call_index}-image-{image_index}{extension}'
            path.write_bytes(base64.b64decode(block['data'], validate=True))
            path.chmod(0o600)
            paths.append(str(path))
    return paths
