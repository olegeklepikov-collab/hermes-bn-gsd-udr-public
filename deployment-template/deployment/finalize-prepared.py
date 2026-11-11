#!/usr/bin/env python3
"""Seal only a newly prepared neutral installation after all path substitutions."""
from pathlib import Path
import hashlib,json,sys,operator,subprocess,shutil
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'runtime/Hermes BN';U=ROOT/'runtime/Hermes UDR'
def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def filehash(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def require_profile_controls(home):
    names=['bn-common-memory']+(['bn-gsd'] if home.name!='bn-udr-only' else [])+(['bn-udr-host'] if home.name!='bn-gsd-only' else [])
    controls=home/'execution-controls.json'
    policy=json.loads(controls.read_text()) if controls.exists() else {'version':1,'required':{},'timeout_seconds':60}
    if policy.get('version')!=1 or not isinstance(policy.get('required'),dict):raise ValueError('Invalid profile execution policy')
    for kind in ['tool','tool_result','llm','auxiliary']:
        policy['required'][kind]=list(dict.fromkeys(policy['required'].get(kind,[])+names))
    controls.write_text(json.dumps(policy,indent=2));controls.chmod(0o600)
def main():
    for name in ['prepared.json','UDR-prepared.json','Memory-prepared.json','Parser-prepared.json']:
        if not (ROOT/'deployment'/name).is_file():raise ValueError('Finish all fresh preparation steps first')
    if (B/'data/auth.json').exists() or (U/'profile/auth.json').exists():raise ValueError('Fresh preparation must precede account authorization')
    import yaml
    for home in [B/'data',B/'data/profiles/bn-gsd-only',B/'data/profiles/bn-udr-only']:
        if not (home/'config.yaml').is_file():continue
        data=yaml.safe_load((home/'config.yaml').read_text())
        def unresolved(value):
            if isinstance(value,str):return '__HERMES_BN_ROOT__' in value or '__HERMES_UDR_ROOT__' in value
            if isinstance(value,dict):return any(unresolved(v) for v in value.values())
            if isinstance(value,list):return any(unresolved(v) for v in value)
            return False
        if unresolved(data):raise ValueError('Unresolved instance root in prepared profile: '+str(home))
    memory=json.loads((B/'Memory/settings.json').read_text());package=Path(memory['package_root'])
    if package.name!='1.4.2':raise ValueError('Expected selected Memory1.4.2; old template must not activate a stale package')
    manifest=package/'manifest.json';values=json.loads(manifest.read_text())
    for name in values:values[name]=filehash(package/name)
    manifest.write_text(json.dumps(values,indent=2))
    bridge=U/'operator/bn-bridge';bm=bridge/'source-manifest.json';values=json.loads(bm.read_text())
    for name in values:values[name]=filehash(bridge/name)
    bm.write_text(json.dumps(values,indent=2))
    gsd=Path(yaml.safe_load((B/'data/config.yaml').read_text())['plugins']['entries']['bn-gsd']['settings']['package_root']);cm=gsd/'release/core-manifest.json';values=json.loads(cm.read_text())
    corepaths=set()
    for name in values['files']:
        path=B/'hermes-agent'/name;values['files'][name]=filehash(path);corepaths.add(str(path))
    cm.write_text(json.dumps(values,indent=2))
    for fresh_home in [B/'data',B/'data/profiles/bn-gsd-only',B/'data/profiles/bn-udr-only']:
        path=fresh_home/'config.yaml'
        if not path.is_file():continue
        config=yaml.safe_load(path.read_text());config.setdefault('compression',{})['enabled']=True
        config.setdefault('agent',{})['reasoning_effort']='high';config['execution_controls_required']=True
        path.write_text(yaml.safe_dump(config,allow_unicode=True,sort_keys=False));path.chmod(0o600)
        require_profile_controls(fresh_home)
    changed=[]
    for home in [B/'data',B/'data/profiles/bn-gsd-only',B/'data/profiles/bn-udr-only']:
        config=home/'config.yaml'
        if not config.exists():continue
        cfg=yaml.safe_load(config.read_text());entry=cfg.get('plugins',{}).get('entries',{}).get('bn-gsd')
        if not entry:continue
        entry['settings'].update(package_root=str(gsd),core_manifest=str(cm))
        edge=home/'plugins/bn-gsd';edge.mkdir(parents=True,exist_ok=True)
        for name in ['__init__.py','plugin.yaml']:shutil.copy2(gsd/'plugin'/name,edge/name)
        config.write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False));config.chmod(0o600)
        path=Path(entry['settings']['settings_file'])
        if not path.exists():
            # A neutral alternate profile is a template until its independent
            # authority/state are initialized; never copy the producer's state.
            rr=Path(json.loads((ROOT/'deployment/prepared.json').read_text())['r_runtime'])
            subprocess.run([str(B/'hermes-agent/venv/bin/python'),str(gsd/'configure_profile.py'),
                '--home',str(home),'--core',str(B/'hermes-agent'),'--bundle',str(B/'GSD/vendor/1.1.0'),
                '--operator',str(home),'--state',str(home/'state'),'--workspace',str(B/'workspace'),
                '--runtime-root',str(B),'--r-runtime',str(rr),'--core-manifest',str(cm),'--apply'],check=True)
        config_file=home/'config.yaml';fresh=yaml.safe_load(config_file.read_text());fresh.setdefault('compression',{})['enabled']=True;fresh.setdefault('agent',{})['reasoning_effort']='high';fresh['plugins']['disabled']=[n for n in fresh['plugins'].get('disabled',[]) if n!='bn-gsd'];config_file.write_text(yaml.safe_dump(fresh,allow_unicode=True,sort_keys=False));cfg=fresh
        require_profile_controls(home)
        s=json.loads(path.read_text())
        if s.get('limits',{}).get('budget_mode')!='observe':raise ValueError('Unexpected fresh resource policy')
        s['mcp_transport_digests']={name:digest(value) for name,value in cfg.get('mcp_servers',{}).items()}
        s['local_adapter_sha256']={name:value for name,value in s.get('local_adapter_sha256',{}).items() if name not in corepaths}
        include_udr=bool(cfg.get('plugins',{}).get('entries',{}).get('bn-udr-host',{}).get('enabled',False))
        def optional_udr(name):
            return Path(name).is_relative_to(bridge) or name in {str(U/'state/adapters/beads-runtime.json'),str(U/'software/bin/bd')} or '/plugins/bn-udr-host/' in name
        if not include_udr:s['local_adapter_sha256']={n:v for n,v in s['local_adapter_sha256'].items() if not optional_udr(n)}
        for root in [gsd,package]+([bridge] if include_udr else []):
            for p in root.rglob('*'):
                if p.is_file() and not p.is_symlink() and '__pycache__' not in p.parts and (p.suffix in {'.py','.json','.yaml','.patch','.txt'} or p.name in {'rpc','serve'}):
                    # State and prior acceptance never become authority in a fresh profile.
                    if root==bridge and any(x in p.parts for x in ['evidence','checkpoint-final','owner-grants','rollback','staging-home','profile']):continue
                    s['local_adapter_sha256'][str(p)]=filehash(p)
        s['local_adapter_sha256'][str(edge/'__init__.py')]=filehash(edge/'__init__.py')
        s['local_adapter_sha256'][str(B/'R/serena-bin/R')]=filehash(B/'R/serena-bin/R')
        for p in [B/'Memory/settings.json',cm]+([bm,U/'state/adapters/beads-runtime.json'] if include_udr else []):
            s['local_adapter_sha256'][str(p)]=filehash(p)
        path.write_text(json.dumps(s,indent=2));path.chmod(0o600);changed.append(home.name)
    proof={'fresh_policy_sealed':True,'profiles':changed,'services_started':False,'accounts_authorized':False,'model_calls':0,'old_owner_state_imported':False}
    (ROOT/'deployment/FINALIZED.json').write_text(json.dumps(proof,indent=2));print(json.dumps(proof))
if __name__=='__main__':main()
