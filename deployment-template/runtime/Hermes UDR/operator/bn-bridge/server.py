"""Three MCP tools; Hermes BN remains the only research model executor."""
import asyncio
import threading
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ListToolsResult, CallToolResult
import backend

SCHEMAS = {
    'udr_research': ('Управляемое исследование UDR. Сначала start(question,mode,request_id), затем plan, source(url,title,text,extent), note(text,source_ids), fetch(url), method, finish(report,status) or finish(report_path,report_sha256,status). read(path) читает сохранённое; stop сохраняет прерванную работу. Полный профиль возвращается при старте. Модель не принимает выводы и не разрешает передачу.',
        {'request': {'type': 'object', 'properties': {
            'action': {'enum': ['start','status','plan','source','document','note','fetch','parse','intake','method','compare','build_report','workspace','finish','adopt_file','read','stop','list','resume','phase']},
            'source_path':{'type':'string','description':'adopt_file: existing regular file under BN workspace/research/<project>; scoped relative or exact absolute BN path. No symlinks or parent traversal. The host preserves all bytes; no delivery authority is created.'},
            'expected_sha256':{'type':'string','pattern':'^[a-f0-9]{64}$'},
            'run_id':{'type':'string'}, 'retrieval_id':{'type':'string','pattern':'^[a-f0-9]{32}$'}, 'doc_id':{'type':'string'}, 'corpus_id':{'type':'string'},'phase':{'enum':['plan','collect','analyse','verify','report']},
            'question':{'type':'string'}, 'mode':{'enum':['search','research','deep','ultra','academic']},
            'request_id':{'type':'string'}, 'plan':{'type':'object','description':'Substantive roadmap object, never a string; use applicable planning_fields returned by start.'},
            'url':{'type':'string'}, 'title':{'type':'string'}, 'text':{'type':'string'},
            'extent':{'enum':['full_text','excerpt','abstract','metadata']},
            'source_ids':{'type':'array','items':{'type':'string'}},
            'report':{'type':'string','description':'Complete report text with [S-...] citations, never a JSON object or a promise.'},
            'report_path':{'type':'string','description':'Alternative to report: existing scoped UDR-workspace text path; use with exact report_sha256. Existing SDK receives all verified bytes as report, without model recopy.'},
            'report_sha256':{'type':'string','pattern':'^[a-f0-9]{64}$'},
            'status':{'enum':['complete','partial']}, 'path':{'type':'string'}, 'index':{'type':'integer','minimum':0}
            ,'method_action':{'enum':['catalogue','guide','describe','run']}, 'method':{'type':'string'},'input':{'type':'object'},
            'workspace_action':{'enum':['status','dispatch','complete_step','record','capabilities','handoff']}
        }, 'required': ['action'], 'additionalProperties': True}}),
    'udr_workspace': ('Read an exact bounded page from this UDR workspace. Continue via next_offset until complete; retain full byte SHA and fragment SHA. Not an assertion of whole-file reading.', {'request': {'type':'object','properties': {'path':{'type':'string'},'offset':{'type':'integer','minimum':0},'max_chars':{'type':'integer','minimum':1,'maximum':4096}},'required':['path'],'additionalProperties':False}}),
    'udr_compare_rates': ('Pure bounded decimal comparison. No commands, network or file writes. Zero baseline has no relative percentage; no causal inference.', {'before':{'type':'number','minimum':0,'maximum':1000000000000000},'after':{'type':'number','minimum':0,'maximum':1000000000000000}}),
    'udr_recall': ('Контекст текущего проекта: AgentMemory, Graphiti и Zvec. Сведения остаются кандидатами; не подтверждают научные выводы.', {'query': {'type': 'string'}}),
    'udr_status': ('Фактическое состояние UDR и текущей исследовательской работы. Не выдаёт разрешение на производственную активацию.', {})
}

async def list_tools(context, params):
    return ListToolsResult(tools=[Tool(name=n, description=description, input_schema={'type': 'object',
        'properties': {**props, '_host': {'type': 'object', 'description': 'Заполняется доверенным расширением Hermes; модель это поле не формирует.'}},
        'required': list(props), 'additionalProperties': False}) for n, (description, props) in SCHEMAS.items()])

async def call_tool(context, params):
    cancel=None;cancel_var=None;cancel_token=None
    try:
        request=params.arguments.get('request',{})
        if params.name=='udr_research' and request.get('action') in {'fetch','parse','intake'}:
            settings=json.loads((backend.ROOT.parent/'Hermes BN/Memory/settings.json').read_text())
            __import__('sys').path.insert(0,settings['package_root'])
            from bn_memory.parser_host import CANCEL_EVENT
            cancel=threading.Event();cancel_var=CANCEL_EVENT;cancel_token=cancel_var.set(cancel)
        result = await asyncio.to_thread(backend.dispatch, params.name, params.arguments)
        return CallToolResult(content=[TextContent(type='text', text=json.dumps(result, ensure_ascii=False))])
    except asyncio.CancelledError:
        if cancel is not None:cancel.set()
        raise
    except Exception as exc:
        # Expected refusals are structured; no confidential inputs in a traceback.
        return CallToolResult(is_error=True, content=[TextContent(type='text', text=json.dumps(
            {'status':'blocked','error':type(exc).__name__,'code':getattr(exc,'code',str(exc))},ensure_ascii=False))])

    finally:
        if cancel_token is not None:cancel_var.reset(cancel_token)

server = Server('hermes-bn-udr', version='0.3.2', on_list_tools=list_tools, on_call_tool=call_tool)

async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())

if __name__ == '__main__':
    asyncio.run(main())
