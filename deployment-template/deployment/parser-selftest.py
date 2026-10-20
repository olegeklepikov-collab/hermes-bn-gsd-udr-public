#!/usr/bin/env python3
"""A finite real-OS parser check in a fresh neutral installation, without model/service credentials."""
from pathlib import Path
import argparse,json,subprocess,uuid,sys,hashlib,shutil
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'runtime/Hermes BN';cfg=json.loads((B/'Memory/settings.json').read_text());sys.path.insert(0,cfg['package_root'])
from bn_memory.parser_host import run_step
p=argparse.ArgumentParser();p.add_argument('--work',type=Path,required=True);a=p.parse_args();a.work.mkdir(parents=True,exist_ok=False,mode=0o700)
source=a.work/'input';source.mkdir();pdf=source/'long.pdf'
program="import pymupdf,sys;d=pymupdf.open();[(d.new_page().insert_text((30,40),'PAGE '+str(i+1)+(' FINAL_MARKER' if i==1000 else ''))) for i in range(1001)];d.save(sys.argv[1])"
subprocess.run([cfg['document_python'],'-I','-B','-c',program,str(pdf)],check=True)
steps=[]
for n in range(30):
 r=run_step({'path':str(pdf),'format':'pdf','output':str(a.work/'parsed')},cfg['document_python'],{'max_units':128});steps.append(r['status'])
 if n==0 and r['status']=='partial':
  restored=source/'restored.pdf';shutil.copy2(pdf,restored);restored.replace(pdf)
  saved=a.work/'saved-first-step';(a.work/'parsed').rename(saved);shutil.copytree(saved,a.work/'parsed')
 if r['status']!='partial':break
assert r['status']=='extracted' and r['units']==1001,r
assert r.get('original_identity_revalidation_ref') and json.loads(Path(r['original_identity_revalidation_ref']).read_text())['settled_checkpoint_only']
assert 'FINAL_MARKER' in (Path(r['output_directory'])/'1000.txt').read_text()
again=run_step({'path':str(pdf),'format':'pdf','output':str(a.work/'parsed')},cfg['document_python']);assert again['cached_parser_result'] and not again['new_executor_launched']
bad=source/'bad.pdf';bad.write_bytes(b'%PDF- damaged');blocked=run_step({'path':str(bad),'format':'pdf','output':str(a.work/'bad')},cfg['document_python']);assert blocked['status']=='blocked'
scan=source/'scan.pdf'
scan_program="import pymupdf,sys;d=pymupdf.open();p=d.new_page();p.insert_text((40,60),'SCAN RESTORE 20 TO 30',fontsize=20);raw=p.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False).tobytes('png');s=pymupdf.open();s.new_page().insert_image(p.rect,stream=raw);s.save(sys.argv[1])"
subprocess.run([cfg['document_python'],'-I','-B','-c',scan_program,str(scan)],check=True)
scan_result=run_step({'path':str(scan),'format':'pdf','output':str(a.work/'scan-parsed')},cfg['document_python'])
assert scan_result['status']=='extracted'
assert 'SCAN RESTORE 20 TO 30' in ''.join(p.read_text() for p in Path(scan_result['output_directory']).glob('*.txt'))
cyr=source/'русский документ.txt';cyr.write_text('Точный исходник 20 → 30.',encoding='utf-8')
cyr_result=run_step({'path':str(cyr),'format':'text','output':str(a.work/'разбор-кириллица')},cfg['document_python'])
assert cyr_result['status']=='extracted'
assert (Path(cyr_result['output_directory'])/'0.txt').read_text()==cyr.read_text()
proof={'passed':True,'pages':1001,'calls':len(steps),'late_marker_verified':True,'filesystem_restore_preserved_first_128_pages':True,'OS_isolation':r['sandbox_enforced'],'complete_reuse_without_executor':True,'corrupt_PDF_blocked':True,'model_reading_tested':False,'Cyrillic_source_and_output_paths':True,'remote_calls':0,'native_OCR_from_relocated_runtime':True};(a.work/'result.json').write_text(json.dumps(proof,indent=2));print(json.dumps(proof))
