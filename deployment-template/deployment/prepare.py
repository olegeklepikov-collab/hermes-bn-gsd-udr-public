#!/usr/bin/env python3
"""Prepare a fresh local installation; never starts services or signs into accounts."""
from pathlib import Path
import argparse,os,sys,json,subprocess,platform,shutil
B=Path(__file__).resolve().parents[1];R=B/'runtime/Hermes BN';RR=B/'runtime/hermes-bn-r';S=B/'deployment/prepared.json'
p=argparse.ArgumentParser();p.add_argument('--contact-email',default='');p.add_argument('--r-runtime',required=True,help='New empty R software directory, preferably a short absolute path');p.add_argument('--init-local-databases',action='store_true');a=p.parse_args()
if platform.system()!='Darwin' or platform.machine()!='arm64':raise SystemExit('Bundled executables require macOS arm64; rebuild from supplied source and dependency locks on other platforms.')
if S.exists():raise SystemExit('Already prepared; do not relocate an installation after preparation. Extract a fresh copy instead.')
if not (R/'data/config.yaml').is_file():raise SystemExit('Missing fresh configuration')
rr=Path(a.r_runtime).expanduser().absolute()
if rr.exists():raise SystemExit('R destination must not already exist')
if any(c.isspace() for c in str(rr)):raise SystemExit('Choose an R software path without whitespace; native R rejects a spaced temporary directory.')
if len(str(rr/'env').encode())>49:raise SystemExit('Choose a shorter R directory: the absolute path ending in /env must be at most 49 UTF-8 bytes for these binary packages.')
rr.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(RR),rr)
# Relocate the conda binary/text prefixes using its supported null-padding rules.
sys.path.insert(0,str(B/'deployment'));from conda_pack.prefixes import update_prefix
for rec in json.loads((B/'deployment/r-prefix-records.json').read_text()):
 q=rr/'env'/rec['path']
 if q.is_file() and not q.is_symlink():update_prefix(str(q),str(rr/'env'),rec['placeholder'],rec['mode'])
for relative in json.loads((B/'deployment/r-library-prefix-records.json').read_text()):
 q=rr/relative
 if q.is_file():update_prefix(str(q),str(rr),'/__hbn_r_________________________________________','binary')
renv=os.environ.copy();renv.update(R_HOME=str(rr/'env/lib/R'),R_LIBS_USER=str(rr/'library'))
subprocess.run([str(rr/'env/bin/Rscript'),'--vanilla',str(B/'deployment/relocate-r-metadata.R'),str(rr/'library'),'__HERMES_BN_R_RUNTIME__',str(rr)],env=renv,check=True)
substitutions={'__HERMES_BN_ROOT__':str(R),'__HERMES_BN_R_RUNTIME__':str(rr),'__USER_HOME__':str(Path.home()),'__CONTACT_EMAIL__':a.contact_email}
# Change only text. Compiled libraries were handled above, not by variable-length byte edits.
for root in [R,rr]:
 for base,ds,fs in os.walk(root,followlinks=False):
  ds[:]=[d for d in ds if d not in ['.git','__pycache__']]
  for n in fs:
   q=Path(base)/n
   if q.is_symlink():
    target=os.readlink(q);new=target
    for k,v in substitutions.items():new=new.replace(k,v)
    if new!=target:q.unlink();q.symlink_to(new)
    continue
   if not q.is_file():continue
   with q.open('rb') as f:head=f.read(8192)
   if b'\x00' in head:continue
   try:s=q.read_text()
   except (UnicodeError,OSError):continue
   old=s
   for k,v in substitutions.items():s=s.replace(k,v)
   if s!=old:
    tmp=q.with_name(q.name+'.prepare-tmp');tmp.write_text(s);shutil.copymode(q,tmp);os.replace(tmp,q)
# Symlinks to R are relative to the original neutral tree; re-point them to the selected directory.
for name,target in [('runtime',rr/'env'),('packages',rr/'library'),('runtime-temp',rr/'tmp')]:
 q=R/'R'/name
 if q.is_symlink():q.unlink()
 if q.exists():raise SystemExit('Unexpected R link target')
 q.symlink_to(target)
for sub in ['projects/default','exports','checks']:(R/'R'/sub).mkdir(parents=True,exist_ok=True)
# New library has no cloud account or inherited authorization; sync is off.
(R/'Zotero/profile/user.js').write_text('\n'.join([
'user_pref("extensions.zotero.useDataDir", true);',
'user_pref("extensions.zotero.dataDir", '+json.dumps(str(R/'Zotero/data'))+');',
'user_pref("extensions.zotero.httpServer.enabled", true);',
'user_pref("extensions.zotero.httpServer.port", 23119);',
'user_pref("extensions.zotero.httpServer.localAPI.enabled", true);',
'user_pref("extensions.zotero.sync.autoSync", false);',
'user_pref("extensions.zotero.integration.skipInstallation", true);'])+'\n')
if a.contact_email:
 q=R/'Crossref/config/settings.json';d=json.loads(q.read_text());d['email_authorized']=True;q.write_text(json.dumps(d,ensure_ascii=False,indent=2))
# The bundle remains disabled until the user configures their own provider and tools.
if a.init_local_databases:
 env=os.environ.copy();env.update(HERMES_HOME=str(R/'data'),BEADS_DIR=str(R/'Beads/workspace/.beads'),BEADS_ACTOR='Hermes BN',BD_DISABLE_METRICS='1',BD_DISABLE_EVENT_FLUSH='1',BD_NON_INTERACTIVE='1',DOLT_ROOT_PATH=str(R/'Beads/local-state'),DO_NOT_TRACK='1')
 subprocess.run([str(R/'Beads/bin/bd'),'init','--prefix','hbn','--stealth','--non-interactive','--skip-agents','--skip-hooks'],cwd=R/'Beads/workspace',env=env,check=True)
 bead=R/'Beads/workspace/.beads'
 if (R/'Beads/formulas').exists():shutil.copytree(R/'Beads/formulas',bead/'formulas',dirs_exist_ok=True)
 shutil.copy2(R/'Beads/PRIME.md',bead/'PRIME.md')
 db=R/'Dolt/databases/knowledgework';db.mkdir()
 de=os.environ.copy();de.update(DOLT_ROOT_PATH=str(R/'Dolt/local-state'),DOLT_AUTHOR_NAME='Hermes BN',DOLT_AUTHOR_EMAIL='local@localhost')
 subprocess.run([str(R/'Dolt/bin/dolt'),'init','--name','Hermes BN','--email','local@localhost'],cwd=db,env=de,check=True)
 ddl="CREATE TABLE research_sources (dataset_id VARCHAR(80) PRIMARY KEY, source_file TEXT NOT NULL, source_sha256 CHAR(64) NOT NULL, imported_at DATETIME(6) NOT NULL, row_count BIGINT NOT NULL, source_format VARCHAR(20) NOT NULL, note TEXT); CREATE TABLE research_records (dataset_id VARCHAR(80) NOT NULL, record_id BIGINT NOT NULL, payload JSON NOT NULL, PRIMARY KEY(dataset_id,record_id), FOREIGN KEY(dataset_id) REFERENCES research_sources(dataset_id)); CALL DOLT_ADD('.'); CALL DOLT_COMMIT('-m','Initialize independent research tables');"
 subprocess.run([str(R/'Dolt/bin/dolt'),'sql','-q',ddl],cwd=db,env=de,check=True)
subprocess.run([sys.executable,str(B/'deployment/activate-gsd.py'),str(rr)],check=True)
S.write_text(json.dumps({'prepared':True,'local_databases_initialized':a.init_local_databases,'services_started':False,'accounts_authorized':False,'root':str(R),'r_runtime':str(rr)},ensure_ascii=False,indent=2));S.chmod(0o600)
print('Fresh installation prepared; no services were started and no remote requests were made.')
