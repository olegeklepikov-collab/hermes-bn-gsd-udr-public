"""Apply reversible native plugin/configuration changes; no credentials or core edits."""
from pathlib import Path
import argparse,datetime,hashlib,json,shutil
import yaml
p=argparse.ArgumentParser();p.add_argument('--root',required=True);a=p.parse_args();B=Path(a.root).resolve();source=Path(__file__).resolve().parent
homes=[B/'data',B/'data/profiles/bn-gsd-only',B/'data/profiles/bn-udr-only']
checkpoint=B/'WorkStatus/operator'/datetime.datetime.now(datetime.timezone.utc).strftime('checkpoint-%Y%m%dT%H%M%SZ');checkpoint.mkdir(parents=True,mode=0o700)
saved=[]
for n,home in enumerate(homes):
 cfg_path=home/'config.yaml';cfg=yaml.safe_load(cfg_path.read_text());q=checkpoint/(str(n)+'-config.yaml');shutil.copy2(cfg_path,q);q.chmod(0o600);saved.append({'path':str(cfg_path),'copy':q.name})
 dst=home/'plugins/bn-work-status';dst.mkdir(parents=True,exist_ok=True)
 for name in ['__init__.py','plugin.yaml']:shutil.copy2(source/name,dst/name)
 plugins=cfg.setdefault('plugins',{});enabled=plugins.setdefault('enabled',[])
 if 'bn-work-status' not in enabled:enabled.append('bn-work-status')
 plugins.setdefault('entries',{})['bn-work-status']={'enabled':True};plugins['load_timeout_seconds']=max(30,plugins.get('load_timeout_seconds',30))
 display=cfg.setdefault('display',{});display.update(interim_assistant_messages=True,show_commentary=True)
 telegram=display.setdefault('platforms',{}).setdefault('telegram',{});telegram.update(tool_progress='off',interim_assistant_messages=True,show_commentary=True,show_reasoning=False,thinking_progress=False)
 cfg_path.write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False));cfg_path.chmod(0o600)
for n,path in enumerate([B/'GSD/operator/settings.json',B/'data/profiles/bn-gsd-only/settings.json']):
 q=checkpoint/(str(n)+'-gsd-settings.json');shutil.copy2(path,q);q.chmod(0o600);saved.append({'path':str(path),'copy':q.name});cfg=json.loads(path.read_text())
 for home in homes:
  target=home/'plugins/bn-work-status/__init__.py';cfg['local_adapter_sha256'][str(target)]=hashlib.sha256(target.read_bytes()).hexdigest()
 path.write_text(json.dumps(cfg,ensure_ascii=False,indent=2));path.chmod(0o600)
(checkpoint/'manifest.json').write_text(json.dumps(saved,indent=2))
print(json.dumps({'installed':'bn-work-status 1.0.2','profiles':[h.name for h in homes],'checkpoint':str(checkpoint),'core_changed':False,'services_started':False}))
