"""Prepare a fresh owner instance from already-installed pinned BN/UDR dependencies."""
from pathlib import Path
import argparse,json,os,sys

def main():
    p=argparse.ArgumentParser();p.add_argument('--bn-root',required=True);p.add_argument('--udr-root',required=True);a=p.parse_args()
    B=Path(a.bn_root).resolve();U=Path(a.udr_root).resolve();M=B/'Memory'
    if (M/'settings.json').exists():raise FileExistsError('existing_memory_configuration_not_overwritten')
    for directory in ['state','documents','checks','checkpoint']:(M/directory).mkdir(parents=True,exist_ok=True,mode=0o700)
    native=json.loads((U/'profile/foundation/native-runtime.json').read_text());cfg={k:v for k,v in native.items() if k in ['agentmemory_url','neo4j_uri','neo4j_user','neo4j_password_file']}
    cfg.update({'default_project':'bn-main','projects':{'bn-main':str(B/'workspace')},'state_root':str(M/'state'),'package_root':str(M/'staging'),'python':str(B/'hermes-agent/venv/bin/python'),'graph_python':str(U/'software/foundation-graph/bin/python'),'zvec_python':str(U/'software/zvec/bin/python'),'serena_command':str(U/'software/serena/bin/serena'),'mirage_command':str(U/'software/mirage/.venv/bin/mirage'),'code_path':str(U/'software/bin')+':/opt/homebrew/bin:/usr/bin:/bin','host_key':str(M/'state/host.key'),'context_bytes':6000,'embedding_url':'https://api.voyageai.com/v1/embeddings','voyage_key_file':str(U/'state/authority/voyage.key'),'embedding_daily_bytes':1000000})
    for field in ['python','graph_python','zvec_python','serena_command','mirage_command','voyage_key_file','neo4j_password_file']:
        if not Path(cfg[field]).is_file():raise FileNotFoundError('required_existing_component:'+field)
    if (M/'state/host.key').exists():raise FileExistsError('existing_host_key_not_overwritten')
    fd=os.open(cfg['host_key'],os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
    try:os.write(fd,os.urandom(32))
    finally:os.close(fd)
    config=M/'settings.json';config.write_text(json.dumps(cfg,ensure_ascii=False,indent=2));config.chmod(0o600)
    sys.path.insert(0,str(M/'staging'));from bn_memory.store import Store
    Store(M/'state',cfg).initialize();print('Fresh memory prepared; new host key created; no account copied. Run activate.py with the BN gateway stopped.')

if __name__=='__main__':main()
