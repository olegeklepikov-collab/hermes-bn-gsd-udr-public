#!/usr/bin/env python3
"""Admit the bundled deterministic parser in a newly prepared macOS arm64 copy; no credentials/network."""
from pathlib import Path
import json,hashlib,platform,subprocess,sys,os
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'runtime/Hermes BN'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while data:=f.read(4*1024*1024):h.update(data)
 return h.hexdigest()
def main():
 if platform.system()!='Darwin' or platform.machine()!='arm64' or not Path('/usr/bin/sandbox-exec').is_file():raise RuntimeError('Required macOS arm64 isolation is unavailable; dependent parsing remains closed')
 cfg=json.loads((B/'Memory/settings.json').read_text());P=Path(cfg['package_root']);python=Path(cfg['document_python']);ocr=P/'vision-ocr'
 if P.name!='1.3.0':raise RuntimeError('Memory 1.3.0 must be selected')
 if not ocr.is_file():raise RuntimeError('Bundled native OCR is missing; do not substitute an unverified executable')
 roots=json.loads(subprocess.check_output([str(python),'-I','-B','-c','import sys,json;print(json.dumps([sys.prefix,sys.base_prefix]))'],text=True))
 if any(not Path(r).resolve().is_relative_to(B.resolve()) for r in roots):raise RuntimeError('Document interpreter must belong to this new instance')
 lock={'version':1,'python':str(python),'python_roots':roots,'python_binary_hash':sha(python.resolve()),'ocr_binary_hash':sha(ocr),'platform':'macos-arm64','os_isolation':'sandbox-exec','profile_id':'parser'}
 p=P/'parser-runtime.json';p.write_text(json.dumps(lock,indent=2));p.chmod(0o600)
 m=P/'manifest.json';values=json.loads(m.read_text());values={name:sha(P/name) for name in values};m.write_text(json.dumps(values,indent=2));m.chmod(0o600)
 proof={'parser_runtime_admitted':True,'Memory':'1.3.0','network_calls':0,'old_owner_authority_imported':False,'execution_test_required':True};(ROOT/'deployment/Parser-prepared.json').write_text(json.dumps(proof,indent=2));print(json.dumps(proof))
if __name__=='__main__':main()
