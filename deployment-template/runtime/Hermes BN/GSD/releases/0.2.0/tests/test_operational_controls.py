from test_host_contracts import host
import time, pytest
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))


def test_exact_tool_grant_is_shared_scoped_revocable_and_non_replayable(host):
    args={'sid':'root','name':'mcp__example__publish','arguments':{'text':'synthetic'},'ttl':300,'reason':'Synthetic test'}
    grant=host('issue_tool_grant',args)
    from bn_gsd.codec import digest
    request={'sid':'root','name':args['name'],'args_digest':digest(args['arguments']),'call_id':'call1','boundary':'execution_middleware'}
    host('authorize_tool_grant',{**request,'args_digest':'0'*64},ok=False)
    host('authorize_tool_grant',request)
    host('authorize_tool_grant',{**request,'boundary':'registry'})
    host('authorize_tool_grant',request,ok=False)
    host('evidence_event',{'sid':'root','event':{'tool_call_id':'call1','result_sha256':'synthetic'}})
    host('authorize_tool_grant',{**request,'call_id':'call2'},ok=False)
    other=host('issue_tool_grant',{**args,'arguments':{'text':'other'}})
    host('revoke_grant',{'grant_id':other['grant_id'],'reason':'Revoked'})
    host('authorize_tool_grant',{**request,'args_digest':digest({'text':'other'}),'call_id':'call3'},ok=False)


def test_migration_inspection_uses_real_source_without_reset(host,tmp_path):
    before=host('family_status',{'sid':'root'})['resource']
    plan=host('operator_migrate',{'backup_path':str(tmp_path/'migration.sqlite'),'apply':False})
    assert plan['runs']==[] and plan['counter_reset'] is False
    after=host('family_status',{'sid':'root'})['resource']
    assert before==after


def test_missing_external_executor_never_commits(host):
    host('operator_external_commit',{'job_id':'absent','run_id':'absent','payload':{},'request_id':'x','review_reason':'Synthetic'},ok=False)
