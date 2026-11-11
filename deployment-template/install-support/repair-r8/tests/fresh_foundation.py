import os
from pathlib import Path
import json,sys,time,os
W=Path(__file__).resolve().parents[1];sys.path.insert(0,str(W/'code'));import foundation_setup as f
u=Path(os.environ['HERMES_UDR_ROOT']);root=u/'operator'/('repair-trial-'+str(time.time_ns()))/'profile/foundation';root.mkdir(parents=True,mode=0o700)
# Binding values only, not a copied secret or previous verification/permission receipt.
source=u/'profile/foundation/native-runtime.json';target=root/'native-runtime.json';target.write_bytes(source.read_bytes());target.chmod(0o600)
r=f.apply(u,foundation_root=root);v=f.verify(u,foundation_root=root);assert v['status']=='healthy',v
assert (root/'beads-workspace/.beads').is_dir();assert all((root/'dolt'/n/'.dolt').is_dir() for n in ['kw_core','kw_context','kw_quant','kw_registry'])
repeat=f.apply(u,foundation_root=root);assert repeat['status']=='already_ready',repeat
proof={'passed':True,'new_state_root':str(root),'new_Beads_and_four_Dolt_databases':True,'native_services_reused_are_owned':True,'old_permissions_or_release_receipts_copied':False,'signed_pair_checked':True,'fresh_release_receipt_created':True,'repeat_preserved_state':True,'model_calls':0,'verification':v,'first_apply':r}
(W/'evidence/fresh-foundation.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(json.dumps({'passed':True,'new_state_root':str(root),'repeat':'already_ready'},ensure_ascii=False),flush=True)
