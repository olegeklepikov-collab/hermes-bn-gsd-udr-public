"""Owner-operated selection through the documented gateway profile routing."""
from pathlib import Path
import json,subprocess,sys,yaml
BN=Path('__HERMES_BN_ROOT__');here=Path(__file__).resolve().parent
mode=sys.argv[1] if len(sys.argv)>1 else 'status'
path=BN/'data/config.yaml';cfg=yaml.safe_load(path.read_text());routes=cfg.setdefault('gateway',{}).setdefault('profile_routes',[])
if mode=='status':
 print(json.dumps([r for r in routes if r.get('name')=='BN-module-mode'],ensure_ascii=False));raise SystemExit()
if mode not in {'combined','gsd','udr'}:raise SystemExit('Modes: status, combined, gsd, udr')
# Never drop a required controller from a profile. Route the next task to a separately qualified profile.
routes[:]=[r for r in routes if r.get('name')!='BN-module-mode']
if mode!='combined':
 routes.append({'name':'BN-module-mode','platform':'telegram','bot_profile':'default','user_id':'0','chat_id':'0','profile':'bn-'+mode+'-only'})
tmp=path.with_suffix('.yaml.mode-new');tmp.write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False));tmp.chmod(0o600);tmp.replace(path)
subprocess.run([str(BN/'bin/hermes-bn-telegram'),'restart'],check=True)
print('Selected',mode,'for new owner Telegram tasks; existing records preserved. Send /new before starting unrelated work.')
