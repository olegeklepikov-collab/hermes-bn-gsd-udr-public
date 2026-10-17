"""Scope official Beads/Dolt MCP servers to the independent Hermes BN stores."""
import asyncio,json,sys,copy,uuid,re
from pathlib import Path
from contextlib import AsyncExitStack
import sqlglot
from sqlglot import exp
from mcp import ClientSession,StdioServerParameters,types
from mcp.client.stdio import stdio_client
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from jsonschema import Draft202012Validator
R=Path('__HERMES_BN_ROOT__')
BEADS={'ready','list','show','create','claim','update','close','reopen','dep','comment','comments','note','stats','blocked'}
DOLT={'select_version','show_tables','show_create_table','describe_table','create_table','alter_table','query','exec','list_dolt_branches','select_active_branch','create_dolt_branch_from_head','create_dolt_branch','move_dolt_branch','stage_table_for_dolt_commit','stage_all_tables_for_dolt_commit','unstage_table','unstage_all_tables','create_dolt_commit','list_dolt_commits','list_dolt_diff_changes_in_working_set','list_dolt_diff_changes_by_table_name','list_dolt_diff_changes_in_date_range','get_dolt_merge_status','merge_dolt_branch','merge_dolt_branch_no_fast_forward','list_dolt_remotes','run_dolt_tests','add_dolt_test','remove_dolt_test'}
def checked_sql(text,kind='read',limit=None):
 if len(text)>30000:raise ValueError('SQL exceeds 30000 characters')
 snapshot=bool(re.search(r'(?i)\bAS\s+OF\s+',text))
 normalized=text
 if snapshot:
  if '--' in text or '/*' in text:raise ValueError('Use a snapshot query without SQL comments')
  normalized=re.sub(r"(?i)\bAS\s+OF\s+'[A-Za-z0-9_./~^:+ -]+'",'',text)
 statements=sqlglot.parse(normalized,read='mysql')
 if len(statements)!=1 or statements[0] is None:raise ValueError('Exactly one SQL statement required')
 tree=statements[0]
 if kind=='read' and not isinstance(tree,(exp.Select,exp.Union,exp.Intersect,exp.Except)):raise ValueError('Only SELECT queries are enabled')
 if kind=='write' and not isinstance(tree,(exp.Insert,exp.Update,exp.Delete)):raise ValueError('exec accepts only INSERT, UPDATE or DELETE; use selected schema/version methods for other operations')
 if kind=='create' and not (isinstance(tree,exp.Create) and tree.args.get('kind')=='TABLE'):raise ValueError('Only CREATE TABLE is enabled')
 if kind=='alter' and not isinstance(tree,exp.Alter):raise ValueError('Only ALTER TABLE is enabled')
 if tree.find(exp.Into):raise ValueError('SQL file output is disabled; use the local export helper')
 for f in tree.find_all(exp.Anonymous):
  name=f.name.lower()
  if name in ['load_file','sys_eval','sys_exec','sleep','benchmark'] or (name.startswith('dolt_') and name not in ['dolt_hashof','dolt_hashof_table','dolt_version','dolt_merge_base','dolt_diff','dolt_history','dolt_schema_diff','dolt_log','dolt_status']):raise ValueError('Function not enabled for this SQL interface')
 for table in tree.find_all(exp.Table):
  if table.catalog or (table.db and table.db not in ['knowledgework','information_schema']):raise ValueError('Cross-database access is disabled')
  if kind!='read' and table.db=='information_schema':raise ValueError('System metadata writes disabled')
 if kind=='read' and limit:
  old=tree.args.get('limit');n=None
  if old:
   try:n=int(old.expression.name)
   except (ValueError,AttributeError):raise ValueError('Use a literal LIMIT')
  if snapshot:
   if n is not None and n>limit:raise ValueError('Snapshot LIMIT exceeds 500; use export_query for larger results')
   return text.rstrip().rstrip(';')+(f' LIMIT {limit}' if n is None else '')
  if n is None or n>limit:tree=tree.limit(limit)
 return text if snapshot else tree.sql(dialect='mysql')
async def main(kind):
 root=R/('Beads' if kind=='beads' else 'Dolt');allowed=BEADS if kind=='beads' else DOLT
 native=R/'bin'/('beads-bn-mcp' if kind=='beads' else 'dolt-bn-official-mcp')
 async with AsyncExitStack() as stack:
  streams=await stack.enter_async_context(stdio_client(StdioServerParameters(command=str(native))))
  client=await stack.enter_async_context(ClientSession(streams[0],streams[1],read_timeout_seconds=180))
  await client.initialize();catalog=await client.list_tools();selected={t.name:t for t in catalog.tools if t.name in allowed};assert set(selected)==allowed
  lock=asyncio.Lock()
  async def list_tools(context,params):return types.ListToolsResult(tools=list(selected.values()))
  async def call_tool(context,params):
   effective=None
   try:
    name=params.name;a=copy.deepcopy(params.arguments or {})
    if name not in selected:raise ValueError('Method is outside selected scope')
    Draft202012Validator(selected[name].input_schema).validate(a)
    if kind=='beads':
     if a.get('workspace_root') is not None and Path(a['workspace_root']).resolve()!=(R/'Beads/workspace').resolve():raise ValueError('Only Hermes BN Beads workspace is enabled')
     a['workspace_root']=str(R/'Beads/workspace')
    else:
     if 'working_database'in a and a['working_database']!='knowledgework':raise ValueError('Only knowledgework database is enabled')
     if a.get('force'):raise ValueError('Force replacement is disabled')
     if name=='move_dolt_branch' and a.get('old_name')=='main':raise ValueError('Renaming the main branch is outside the selected workflow')
     if 'query'in a:
      typ='read' if name in ['query','add_dolt_test'] else 'create' if name=='create_table' else 'alter' if name=='alter_table' else 'write'
      effective=checked_sql(a['query'],typ,500 if name=='query' else None);a['query']=effective
    if kind=='beads':
     async with lock:result=await client.call_tool(name,a)
    else:result=await client.call_tool(name,a)
    if kind=='beads' and not result.is_error:
     # Upstream Beads 1.3.1 sometimes returns a CLI failure as text with isError=false.
     soft=[]
     for content in result.content:
      if content.type!='text':continue
      try:value=json.loads(content.text)
      except json.JSONDecodeError:value=content.text
      if isinstance(value,dict) and set(value)=={'result'}:value=value['result']
      if isinstance(value,str) and value.lstrip().startswith(('Error:','ERROR:')):soft.append(value)
     if soft:return types.CallToolResult(content=[types.TextContent(type='text',text=json.dumps({'ok':False,'upstream_soft_error_normalized':True,'error':'\n'.join(soft)},ensure_ascii=False))],is_error=True)
    if effective is not None:
     result.content.insert(0,types.TextContent(type='text',text=json.dumps({'official_server':'dolthub/dolt-mcp v0.3.8','effective_sql':effective,'query_row_limit':500 if name=='query' else None},ensure_ascii=False)))
    length=sum(len(c.text) for c in result.content if c.type=='text')
    if length>100000:
     p=root/'exports'/('mcp-result-'+uuid.uuid4().hex+'.json');p.write_text(json.dumps(result.model_dump(mode='json',by_alias=True),ensure_ascii=False));p.chmod(0o600)
     return types.CallToolResult(content=[types.TextContent(type='text',text=json.dumps({'ok':not result.is_error,'complete_result_file':str(p),'reading_level':'Only result location returned; read saved data before claiming inspection'}))],is_error=result.is_error)
    return result
   except Exception as e:
    return types.CallToolResult(content=[types.TextContent(type='text',text=json.dumps({'ok':False,'error_type':type(e).__name__,'error':str(e)[:1400]},ensure_ascii=False))],is_error=True)
  server=Server('Hermes BN scoped official '+kind,version='1.0.0',instructions='Official upstream tools scoped to independent Hermes BN storage on AgentRuntime2. Beads tracks task state and provenance, not scientific truth. Dolt versions tables, not external PDF files. Use explicit working branches; preserve original files and source hashes. A SQL commit differs from a Dolt version commit. No account creation, remote publishing, hard resets, database drops or force branch replacement. SQL query output is limited to 500 rows, with effective SQL shown. Original upstream code is unchanged.',on_list_tools=list_tools,on_call_tool=call_tool)
  async with stdio_server() as streams:await server.run(streams[0],streams[1],server.create_initialization_options())
if __name__=='__main__':asyncio.run(main(sys.argv[1]))
