"""Restore only adapter/configuration changes. Keep research evidence and private stores."""
from pathlib import Path
import hashlib,json,shutil,subprocess
HERE=Path(__file__).resolve().parent;BN=Path('__HERMES_BN_ROOT__')
rows=json.loads((HERE/'rollback/manifest.json').read_text())
for row in rows:
 if hashlib.sha256((HERE/'rollback'/row['backup']).read_bytes()).hexdigest()!=row['sha256']:raise RuntimeError('Rollback checkpoint hash mismatch')
subprocess.run([str(BN/'bin/hermes-bn-telegram'),'stop'],check=True)
for row in rows:
 target=Path(row['path']);shutil.copy2(HERE/'rollback'/row['backup'],target);target.chmod(0o600)
# Retain the installed files as a recoverable local snapshot, outside native discovery.
stage=HERE/'disabled-after-rollback';stage.mkdir(mode=0o700,exist_ok=False)
for p in [BN/'data/plugins/bn-udr-host',BN/'data/profiles/bn-gsd-only',BN/'data/profiles/bn-udr-only',BN/'data/skills/bn-udr-host-work']:
 if p.exists():shutil.move(str(p),str(stage/p.name))
subprocess.run([str(BN/'bin/hermes-bn-telegram'),'start'],check=True)
print('Prior BN configuration restored; UDR, research drafts and prior conversations preserved')
