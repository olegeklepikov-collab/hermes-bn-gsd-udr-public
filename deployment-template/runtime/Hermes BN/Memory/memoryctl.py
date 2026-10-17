"""Local owner commands. Not exposed as agent tools or arbitrary SQL."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import sys
import yaml

M=Path(__file__).resolve().parent;B=M.parent;CONFIG=M/'settings.json'
def reseal():
    for path in [B/'GSD/operator/settings.json',B/'data/profiles/bn-gsd-only/settings.json']:
        d=json.loads(path.read_text());d['local_adapter_sha256'][str(CONFIG)]=hashlib.sha256(CONFIG.read_bytes()).hexdigest();path.write_text(json.dumps(d,ensure_ascii=False,indent=2));path.chmod(0o600)

def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='action',required=True)
    q=sub.add_parser('register-project');q.add_argument('name');q.add_argument('path');q.add_argument('--languages',default='python')
    q=sub.add_parser('snapshot');q.add_argument('destination')
    q=sub.add_parser('verify-snapshot');q.add_argument('path')
    q=sub.add_parser('rebuild');q.add_argument('backend',choices=['agentmemory','graphiti','zvec']);q.add_argument('--max-batches',type=int,default=30);q.add_argument('--resume',action='store_true')
    sub.add_parser('status');sub.add_parser('sync')
    a=p.parse_args();cfg=json.loads(CONFIG.read_text());sys.path.insert(0,cfg['package_root']);from bn_memory.broker import Broker
    broker=Broker(cfg);sid='bn-memory-local-owner';broker.store.bind(sid)
    if a.action=='register-project':
        root=Path(a.path)
        if not re.fullmatch('[a-z][a-z0-9-]{0,63}',a.name) or not root.is_absolute() or root.is_symlink() or not root.is_dir():raise ValueError('valid_project_name_and_directory_required')
        root=root.resolve();cfg['projects'][a.name]=str(root);cfg.setdefault('project_languages',{})[str(root)]=a.languages.split(',');CONFIG.write_text(json.dumps(cfg,ensure_ascii=False,indent=2));CONFIG.chmod(0o600);reseal()
        serena=root/'.serena/project.yml';serena.parent.mkdir(exist_ok=True)
        d=yaml.safe_load(serena.read_text()) if serena.exists() else {'project_name':a.name,'encoding':'utf-8'}
        d['language_servers']=a.languages.split(',');d['read_only']=True;d['ignored_paths']=list(dict.fromkeys([*d.get('ignored_paths',[]),'**/.env*','**/auth.json','**/mcp-tokens.json','**/.git/**','**/node_modules/**']))
        serena.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False));print(json.dumps({'registered':a.name,'path':str(root),'languages':d['language_servers'],'restart_bn_gateway_required':True}))
    elif a.action=='snapshot':print(json.dumps(broker.store.snapshot(a.destination)))
    elif a.action=='verify-snapshot':
        import sqlite3
        dest=Path(a.path).resolve();c=sqlite3.connect('file:'+str(dest)+'?mode=ro',uri=True)
        check=c.execute('PRAGMA integrity_check').fetchone()[0];bad=c.execute('PRAGMA foreign_key_check').fetchall();count=c.execute('SELECT count(*) FROM current').fetchone()[0];c.close()
        if check!='ok' or bad:raise RuntimeError('snapshot_integrity_failed')
        print(json.dumps({'integrity':check,'foreign_key_errors':len(bad),'records':count,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
    elif a.action=='rebuild':
        if not 1<=a.max_batches<=100:raise ValueError('bounded_rebuild_required')
        with broker.store.db() as c:
            if not a.resume:c.execute('UPDATE outbox SET status=\'pending\' WHERE backend=? AND EXISTS (SELECT 1 FROM current u WHERE u.id=outbox.id AND u.revision=outbox.revision)',(a.backend,))
            owners=[x['sid'] for x in c.execute('SELECT sid FROM sessions WHERE readonly=0')]
        results=[]
        for owner in owners:
            while len(results)<a.max_batches:
                r=broker.sync(owner,10)
                if not r['results']:break
                results.append(r)
                if r['status']!='complete':break
        with broker.store.db() as c:left=c.execute('SELECT count(*) FROM outbox o JOIN current u ON o.id=u.id AND o.revision=u.revision WHERE o.backend=? AND o.status!=\'indexed\'',(a.backend,)).fetchone()[0]
        print(json.dumps({'backend':a.backend,'batches':len(results),'pending':left,'complete':left==0,'results':results},ensure_ascii=False))
    elif a.action=='sync':print(json.dumps(broker.sync(sid,10),ensure_ascii=False))
    else:print(json.dumps(broker.store.status(sid),ensure_ascii=False))

if __name__=='__main__':main()
