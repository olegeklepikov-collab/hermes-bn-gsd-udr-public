import tempfile
import os
from pathlib import Path
import importlib.util,json,shutil,sys,hashlib,subprocess,os,time
W=Path(__file__).resolve().parents[1];B=Path(os.environ['HERMES_BN_ROOT']);settings=json.loads((B/'Memory/settings.json').read_text());P=Path(settings['package_root']);stage=W/'evidence/parser-stage'
if not stage.exists():shutil.copytree(P,stage,ignore=shutil.ignore_patterns('__pycache__'))
for name in ['parser_host.py','document_worker.py']:shutil.copy2(W/'code'/name,stage/'bn_memory'/name)
# Keep the admitted runtime/binary identity; only this independent parser package changes.
def load():
 spec=importlib.util.spec_from_file_location('parser_stage_host',stage/'bn_memory/parser_host.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
h=load();work=Path(os.environ.get('HERMES_REPAIR_TEST_DIR',tempfile.gettempdir()))/'bn-ocr-check'/str(time.time_ns());work.mkdir(parents=True,exist_ok=False);source=work/'scan.pdf'
font=Path('/System/Library/Fonts/Supplemental/Arial Unicode.ttf')
if not font.exists():font=Path('/System/Library/Fonts/Supplemental/Arial.ttf')
program='''import pymupdf,sys
src=pymupdf.open();p=src.new_page();p.insert_font(fontname="test",fontfile=sys.argv[2]);p.insert_text((40,80),"OCR TEST BEFORE 20 AFTER 30",fontname="test",fontsize=22);p.insert_text((40,130),"ПРОВЕРКА ДО 20 ПОСЛЕ 30",fontname="test",fontsize=22)
raw=p.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False).tobytes("png")
doc=pymupdf.open()
for _ in range(2):doc.new_page().insert_image(p.rect,stream=raw)
doc.save(sys.argv[1])
'''
if not source.exists():subprocess.run([settings['document_python'],'-I','-c',program,str(source),str(font)],check=True)
results=[]
def run(label,omit=False):
 original=h.profile
 if omit:
  def old_profile(*a,**kw):return original(*a,**kw).replace('(iokit-user-client-class "H11ANEInDirectPathClient")','')
  h.profile=old_profile
 try:
  folder=work/label
  r=h.run_step({'path':str(source),'format':'pdf','output':str(folder)},settings['document_python'],{'max_units':1})
  partial=r['status']=='partial'
  while r['status']=='partial':r=h.run_step({'path':str(source),'format':'pdf','output':str(folder)},settings['document_python'],{'max_units':1})
  text='\n'.join(p.read_text() for p in Path(r['output_directory']).glob('[0-9]*.txt'))
  result={'label':label,'status':r['status'],'ocr_status':r.get('ocr_status'),'english':'BEFORE 20 AFTER 30' in text,'russian':'ДО 20 ПОСЛЕ 30' in text,'partial_step_observed':partial,'sandbox':r.get('sandbox_enforced'),'network_allowed':r.get('network_allowed'),'credentials_inherited':r.get('credentials_inherited')}
  if not omit:
   assert result['english'] and result['russian'],result
   assert r['ocr_status']['status']=='complete' and r['ocr_status']['succeeded_units']==2 and r['ocr_status']['completed_units']==r['ocr_status']['required_units'],result
   cached=h.run_step({'path':str(source),'format':'pdf','output':str(folder)},settings['document_python']);assert cached['cached_parser_result'] and not cached['new_executor_launched']
   result['repeat_reused_receipt']=True
  results.append(result)
 finally:h.profile=original
run('without-h11',True)
run('with-h11')
run('without-h11-after',True)
# Simulate a real OCR process failure, keeping the sandbox and pinned binary enforcement.
fail=stage/'vision-ocr';saved=fail.read_bytes();mode=fail.stat().st_mode;pinpath=stage/'parser-runtime.json';pin=pinpath.read_bytes()
try:
 # A native executable which exits nonzero is admitted only in this test package.
 fail.write_bytes(Path('/usr/bin/false').read_bytes());fail.chmod(0o700)
 d=json.loads(pin);d['ocr_binary_hash']=h.filehash(fail);pinpath.write_text(json.dumps(d))
 r=h.run_step({'path':str(source),'format':'pdf','output':str(work/'failing-ocr')},settings['document_python'])
 assert r['ocr_status']['status']=='incomplete' and r['ocr_status']['failed_units']==r['ocr_status']['required_units'],r
 results.append({'label':'failed-ocr-explicit','status':r['status'],'ocr_status':r['ocr_status'],'failure_not_claimed_success':True})
finally:fail.write_bytes(saved);fail.chmod(mode);pinpath.write_bytes(pin)
# OCR summary handles duplicate text fragments, empty recognition and unavailable units.
f=work/'summary.jsonl';f.write_text('\n'.join(json.dumps(x) for x in [
 {'locator':{'page':1,'fragment':0},'ocr_required':True,'ocr':{'status':'extracted'}},
 {'locator':{'page':1,'fragment':1},'ocr_required':True,'ocr':{'status':'extracted'}},
 {'locator':{'page':2},'ocr_required':True,'ocr':{'status':'empty'}},
 {'locator':{'page':3},'ocr_required':True},
 {'locator':{'page':4},'ocr_required':False}])+'\n')
r=h.ocr_summary(f);assert r['required_units']==3 and r['succeeded_units']==1 and r['empty_units']==1 and r['unknown_units']==1
results.append({'label':'summary-boundaries','passed':True})
proof={'passed':True,'cases':results,'model_calls':0,'live_package_changed':False}
(W/'evidence/OCR.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(json.dumps(proof,ensure_ascii=False),flush=True)
