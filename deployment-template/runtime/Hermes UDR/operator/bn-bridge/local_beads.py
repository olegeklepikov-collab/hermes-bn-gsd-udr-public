"""Local compatibility layer; the signed Foundation SDK stays unchanged."""
from pathlib import Path
import hashlib,json,os,subprocess,fcntl
from hermes_foundation_bridge.beads_adapter import BeadsAdapter
from hermes_foundation_bridge.canonical import canonical_bytes
from hermes_foundation_bridge.errors import BridgeError

class LocalBeadsAdapter(BeadsAdapter):
    def __init__(self,root,lock_path=None):
        super().__init__(root)
        self.runtime_lock=Path(lock_path) if lock_path else Path(__file__).resolve().parents[2]/'state/adapters/beads-runtime.json'
    def _run(self,arguments,*,actor='foundation-bridge'):
        lock=json.loads(self.runtime_lock.read_text())
        executable=Path(lock['executable'])
        if not executable.is_absolute() or executable.is_symlink() or not executable.is_file():
            raise PermissionError('absolute_owned_beads_executable_required')
        if hashlib.sha256(executable.read_bytes()).hexdigest()!=lock['sha256']:
            raise PermissionError('beads_executable_integrity_failed')
        if not (self.root/'.beads').is_dir():raise PermissionError('owned_beads_workspace_required')
        environment=dict(os.environ,BEADS_ACTOR=actor,BEADS_DIR=str(self.root/'.beads'),DOLT_ROOT_PATH=lock['dolt_root'],BD_DISABLE_METRICS='1',BD_DISABLE_EVENT_FLUSH='1',DO_NOT_TRACK='1')
        p=subprocess.run([str(executable),'-C',str(self.root),*arguments,'--json'],env=environment,capture_output=True,text=True,encoding='utf-8',timeout=45)
        if p.returncode:
            # Retain errors locally without copying confidential process environments.
            raise BridgeError('owned_beads_cli_failed','runtime.beads','Owned Beads command failed; effect must be reconciled')
        return json.loads(p.stdout)
    def health(self,request):
        result=super().health(request)
        lock=json.loads(self.runtime_lock.read_text())
        return {'contract':'HermesBNBeadsRuntimeHealth/1','status':result['status'],'sdk_receipt':result,'runtime_version':lock['version'],'runtime_executable':lock['executable'],
            'runtime_sha256':lock['sha256'],'supplier_baseline_version':'1.1.0','signed_SDK_modified':False}
    def _stable_result(self,kind,request,perform):
        fingerprint=hashlib.sha256(canonical_bytes(request)).hexdigest()
        identity=request.get('operation_key') or fingerprint
        key=hashlib.sha256((kind+':'+identity).encode()).hexdigest()
        directory=self.foundation/'local-beads-receipts';directory.mkdir(mode=0o700,exist_ok=True)
        path=directory/(key+'.json')
        with (directory/(key+'.lock')).open('a') as f:
            fcntl.flock(f,fcntl.LOCK_EX)
            if path.exists():
                cached=json.loads(path.read_text())
                if cached['fingerprint']!=fingerprint:raise ValueError('beads_operation_key_input_conflict')
                if cached['state']!='succeeded':raise PermissionError('beads_prior_outcome_requires_reconciliation')
                result=cached['result']
                if result.get('issue_id'):self.get({'schema_version':1,'issue_id':result['issue_id']})
                return result
            def save(value):
                temporary=path.with_suffix('.tmp');temporary.write_bytes(canonical_bytes(value));temporary.chmod(0o600);temporary.replace(path)
            save({'fingerprint':fingerprint,'state':'pending'})
            result=perform(request)
            if result.get('status') not in {'created','claimed','closed'}:
                save({'fingerprint':fingerprint,'state':'unknown','result':result})
                raise PermissionError('beads_historical_or_unknown_outcome_not_replayed')
            save({'fingerprint':fingerprint,'state':'succeeded','result':result})
            return result
    def create(self,request):return self._stable_result('create',request,super().create)
    def claim(self,request):return self._stable_result('claim',request,super().claim)
    def close(self,request):return self._stable_result('close',request,super().close)
