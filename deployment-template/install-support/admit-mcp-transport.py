#!/usr/bin/env python3
"""Owner-only admission of one existing MCP transport; no tool-policy expansion or agent execution."""
import argparse, hashlib, json, os, tempfile
from datetime import datetime, timezone
from pathlib import Path
import yaml

def sha(raw): return hashlib.sha256(raw).hexdigest()
def digest(value): return sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())
def main():
    p=argparse.ArgumentParser(description='План или точечное принятие уже известного MCP-подключения оператором.')
    p.add_argument('--home',type=Path,required=True);p.add_argument('--server',required=True)
    p.add_argument('--apply',action='store_true');p.add_argument('--expected-config-sha256');p.add_argument('--expected-settings-sha256')
    a=p.parse_args();home=a.home.expanduser().resolve();cfgpath=home/'config.yaml'
    if cfgpath.is_symlink():raise ValueError('Refuse symlink config')
    raw=cfgpath.read_bytes();cfg=yaml.safe_load(raw) or {};entry=cfg.get('plugins',{}).get('entries',{}).get('bn-gsd',{})
    server=cfg.get('mcp_servers',{}).get(a.server)
    if not isinstance(server,dict) or not server.get('enabled',True):raise ValueError('Server must already be configured and enabled')
    if not entry.get('enabled',False):
        if a.apply:raise ValueError('No active GSD admission in this profile; no change made')
        print(json.dumps({'required':False,'reason':'no_active_gsd_controller','config_sha256':sha(raw)},ensure_ascii=False));return
    settingspath=Path(entry['settings']['settings_file']).expanduser()
    if not settingspath.is_absolute() or settingspath.is_symlink():raise ValueError('Use an absolute regular settings file')
    prior=settingspath.read_bytes();settings=json.loads(prior);policy_path=Path(settings['tool_policy'])
    if sha(policy_path.read_bytes())!=settings['tool_policy_sha256']:raise ValueError('Tool policy integrity failed')
    policy=json.loads(policy_path.read_bytes())
    if policy.get('version')!=1:raise ValueError('Unsupported tool policy version')
    methods=sorted(k for k,v in policy['entries'].items() if v.get('server')==a.server)
    if not methods:raise ValueError('Unknown server: requires separately reviewed tool-policy integration')
    for name,value in settings.get('local_adapter_sha256',{}).items():
        if sha(Path(name).read_bytes())!=value:raise ValueError('Existing local adapter integrity failed; transport admission cannot repair code')
    old=settings.get('mcp_transport_digests',{}).get(a.server);new=digest(server)
    plan={'server':a.server,'home':str(home),'config_sha256':sha(raw),'settings_sha256':sha(prior),
          'old_transport_sha256':old,'new_transport_sha256':new,'change_required':old!=new,
          'known_policy_methods':methods,'method_policy_changed':False,'credentials_changed':False}
    if a.apply:
        if a.expected_config_sha256!=sha(raw) or a.expected_settings_sha256!=sha(prior):raise ValueError('Explicit plan hashes required; configuration changed or plan not accepted')
        if old==new:plan['applied']=False;plan['no_op']=True
        else:
            if cfgpath.read_bytes()!=raw or settingspath.read_bytes()!=prior:raise ValueError('Concurrent change; repeat plan')
            receipts=settingspath.parent/'transport-admissions'
            if receipts.is_symlink():raise ValueError('Refuse symlink receipt directory')
            receipts.mkdir(mode=0o700,exist_ok=True);receipts.chmod(0o700)
            stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            backup=receipts/(stamp+'.settings.before.json')
            with backup.open('xb') as f:os.chmod(backup,0o600);f.write(prior);f.flush();os.fsync(f.fileno())
            settings.setdefault('mcp_transport_digests',{})[a.server]=new
            updated=json.dumps(settings,ensure_ascii=False,indent=2).encode()+b'\n'
            fd,tmp=tempfile.mkstemp(prefix='.transport-',dir=settingspath.parent)
            try:
                with os.fdopen(fd,'wb') as f:os.fchmod(f.fileno(),0o600);f.write(updated);f.flush();os.fsync(f.fileno())
                if cfgpath.read_bytes()!=raw or settingspath.read_bytes()!=prior:raise ValueError('Concurrent change; no admission applied')
                os.replace(tmp,settingspath)
            finally:
                if os.path.exists(tmp):os.unlink(tmp)
            plan.update(applied=True,backup=str(backup),result_settings_sha256=sha(updated))
            receipt=receipts/(stamp+'.receipt.json')
            with receipt.open('x') as f:os.chmod(receipt,0o600);json.dump(plan,f,ensure_ascii=False,indent=2)
    print(json.dumps(plan,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
