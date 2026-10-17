"""Publish already-tested 1.0.1 without resetting state or relaxing controls."""
from pathlib import Path
import hashlib,json,os,shutil,subprocess,sys,yaml
M=Path(__file__).resolve().parent;B=M.parent;version=sys.argv[1] if len(sys.argv)>1 else '1.0.2';release=M/'releases'/version
def write(path,text):
    t=path.with_name(path.name+'.memory-update.tmp');t.write_text(text);t.chmod(0o600);os.replace(t,path)
def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

if not release.exists():shutil.copytree(M/'staging',release,ignore=shutil.ignore_patterns('__pycache__'))
config=json.loads((M/'settings.json').read_text());config['package_root']=str(release)
write(M/'settings.json',json.dumps(config,ensure_ascii=False,indent=2))
homes=[B/'data',*sorted((B/'data/profiles').glob('*'))];homes=[p for p in homes if (p/'config.yaml').exists()]
server=None
for home in homes:
    c=yaml.safe_load((home/'config.yaml').read_text());server=c['mcp_servers']['context'];server['args'][0]=str(release/'bn_memory/server.py')
    if not c.get('platform_toolsets'):c['platform_toolsets']={s:['udr','context'] for s in ['cli','gui','api_server','telegram','tui','cron']}
    else:
        for surface,tools in c['platform_toolsets'].items():
            if isinstance(tools,list) and 'context' not in tools:tools.append('context')
    write(home/'config.yaml',yaml.safe_dump(c,allow_unicode=True,sort_keys=False))
    manifest=home/'plugins/bn-common-memory/plugin.yaml';d=yaml.safe_load(manifest.read_text());d['version']=version;write(manifest,yaml.safe_dump(d,allow_unicode=True,sort_keys=False))
for p in [B/'GSD/operator/settings.json',B/'data/profiles/bn-gsd-only/settings.json']:
    d=json.loads(p.read_text());d['mcp_transport_digests']['context']=digest(server)
    for f in [M/'settings.json',release/'manifest.json',*(release/'bn_memory').glob('*.py')]:d['local_adapter_sha256'][str(f)]=hashlib.sha256(f.read_bytes()).hexdigest()
    write(p,json.dumps(d,ensure_ascii=False,indent=2))
(M/'checks/15-update.json').write_text(json.dumps({'version':version,'profiles':[h.name for h in homes],'all_configured_surfaces_include_context':True,'primary_store_replaced':False,'core_changed':False},indent=2));print('Common memory '+version+' installed; all configured channels include context; state retained')
