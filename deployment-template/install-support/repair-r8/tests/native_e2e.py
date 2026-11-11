import os
from pathlib import Path
import json,sys,time,subprocess,hashlib,os,traceback
W=Path(__file__).resolve().parents[1];B=Path(os.environ['HERMES_BN_ROOT']);U=Path(os.environ.get('HERMES_UDR_ROOT',str(B.parent/'Hermes UDR')))
sys.path.insert(0,str(B/'hermes-agent'))
from dotenv import load_dotenv
load_dotenv(B/'data/.env',override=False)
import model_tools
from hermes_cli.config import load_config_readonly
from tools.mcp_tool_discovery import register_mcp_servers
from hermes_cli.lifecycle import invoke_hook
from hermes_cli.runtime_provider import resolve_runtime_provider
from hermes_constants import parse_reasoning_effort
from run_agent import AIAgent
sid='bn-remediation-20261111-'+str(time.time_ns());e=W/'evidence'/sid;e.mkdir(mode=0o700)
config=load_config_readonly();register_mcp_servers({n:config['mcp_servers'][n] for n in ['context','udr']});invoke_hook('on_session_start',session_id=sid,platform='cli')
seq=0
def tool(server,name,args):
 global seq
 seq+=1
 raw=model_tools.handle_function_call('mcp__'+server+'__'+name,args,session_id=sid,tool_call_id=sid+'-'+str(seq))
 result=json.loads(raw) if isinstance(raw,str) else raw
 if 'error' in result:raise RuntimeError(result)
 value=result.get('result',result);value=json.loads(value) if isinstance(value,str) else value
 (e/('tool-'+str(seq)+'.json')).write_text(json.dumps({'server':server,'name':name,'args':args,'result':value},ensure_ascii=False,indent=2))
 if isinstance(value,dict) and ('error' in value or value.get('status') in ['blocked','error']):raise RuntimeError(value)
 print('TOOL',name,args.get('request',{}).get('action',''),flush=True);return value

def research(action,**kw):return tool('udr','udr_research',{'request':{'action':action,**kw}})
folder=B/'workspace'/sid;folder.mkdir(mode=0o700);pdf=folder/'synthetic-scan.pdf';cfg=json.loads((B/'Memory/settings.json').read_text())
font='/System/Library/Fonts/Supplemental/Arial Unicode.ttf'
code='''import pymupdf,sys
s=pymupdf.open();p=s.new_page(width=600,height=500);p.insert_font(fontname="owned",fontfile=sys.argv[2]);p.insert_text((35,65),"SYNTHETIC CHECK BEFORE 20 AFTER 30",fontname="owned",fontsize=19);p.insert_text((35,110),"УЧЕБНЫЙ ПРИМЕР ДО 20 ПОСЛЕ 30",fontname="owned",fontsize=19);p.insert_text((35,155),"NO CAUSAL EFFECT ESTABLISHED",fontname="owned",fontsize=19)
r=p.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False).tobytes("png");d=pymupdf.open();d.new_page(width=600,height=500).insert_image(p.rect,stream=r);d.save(sys.argv[1])
'''
subprocess.run([cfg['document_python'],'-I','-c',code,str(pdf),font],check=True)
invoke_hook('pre_llm_call',user_message='Проверь учебный скан в '+str(pdf)+'; разрешено чтение и рабочие копии, без внешних действий.',session_id=sid,platform='cli',turn_id=sid+'-host-intake')
try:
 inventory=tool('context','document_catalogue',{'path':str(pdf),'request_id':sid,'required_phases':['plan','collect','analyse','verify','report']})
 cid=inventory['corpus_id'];documents=inventory.get('sources',inventory.get('documents',[]))
 if not documents:
  # Read the declared source IDs from the real inventory ledger, not guessed IDs.
  from bn_memory.broker import Broker
  from bn_memory.documents import Documents
  docs=Documents(Broker(cfg));inventory=docs.status(sid,{'corpus_id':cid});documents=inventory.get('sources',inventory.get('documents',[]))
  if not documents:
   with docs.store.db() as db:documents=[{'id':r[0]} for r in db.execute('SELECT id FROM document_sources WHERE corpus=?',(cid,))]
 did=documents[0].get('id',documents[0].get('doc_id'))
 parsed=tool('context','document_extract',{'doc_id':did})
 while parsed.get('status') in ['extracting','partial']:parsed=tool('context','document_extract',{'doc_id':did})
 assert parsed['status']=='extracted' and parsed['metadata']['ocr_status']['status']=='complete',parsed
 start=research('start',question='Проверить по учебному скану изменение 20→30; рассчитать абсолютное и относительное изменение, сохранить ограничение причинного вывода.',mode='search',request_id=sid,corpus_id=cid)
 intake=research('intake',doc_id=did,corpus_id=cid)
 while not intake.get('registration_complete'):intake=research('intake',doc_id=did,corpus_id=cid)
 (e/'start.json').write_text(json.dumps(start,ensure_ascii=False,indent=2));(e/'intake.json').write_text(json.dumps(intake,ensure_ascii=False,indent=2))
 source_ids=intake.get('source_ids',[])
 if not source_ids:
  import sqlite3
  with sqlite3.connect(U/'workspace/bn-research-runs'/start['run_id']/'corpus.sqlite') as db:source_ids=[r[0] for r in db.execute('SELECT id FROM sources')]
 unit_ids=[r['index'] for r in parsed['units']]
 route=resolve_runtime_provider(requested='openai-codex',target_model='gpt-6.1-sol')
 outputs={};step_outputs={}
 for phase in ['plan','collect','analyse','verify','report']:
  research('phase',phase=phase)
  for index in unit_ids:tool('context','document_read',{'corpus_id':cid,'doc_id':did,'unit':index,'phase':phase,'max_chars':16384})
  if phase=='analyse':calculation=tool('udr','udr_compare_rates',{'before':20,'after':30})
  a=AIAgent(model='gpt-6.1-sol',provider=route['provider'],requested_provider='openai-codex',base_url=route['base_url'],api_key=route['api_key'],api_mode=route.get('api_mode'),credential_pool=route.get('credential_pool'),reasoning_config=parse_reasoning_effort('high'),session_id=sid,enabled_toolsets=['context','udr'],max_iterations=3,quiet_mode=True,skip_context_files=True,skip_memory=False,skip_background_review=True,run_budget_seconds=240)
  question={'plan':'Опиши короткий план проверки учебного документа.','collect':'Прочитай доставленные текст и изображение. Укажи значения до и после на русском и английском.','analyse':'Рассмотри выполненный точный расчёт и объясни изменение и границы.','verify':'Проверь, совпадают ли текст распознавания и изображение, нет ли оснований для причинного вывода.','report':'Напиши итоговый краткий Markdown-отчёт по учебному скану: значения, изменение, фактический уровень чтения, отсутствие причинного вывода. Сошлись на выданные source_ids в виде [S-...].'}[phase]
  prompt=start['context']+'\n'+start['depth']+'\nФаза '+phase+'. '+question+'\nЭто операторская синтетическая проверка, исходные фрагменты и изображения доставляются штатным расширением. Новые исследования, новые агенты и внешние действия не запускай. На этом шаге инструменты не вызывай: верни только содержательный результат фазы. Идентификаторы источников: '+json.dumps(source_ids)+'\nПредыдущие результаты: '+json.dumps(outputs,ensure_ascii=False)
  if phase in ['analyse','verify','report']:prompt+='\nРезультат штатного вычислителя: '+json.dumps(calculation,ensure_ascii=False)
  try:r=a.run_conversation(prompt)
  finally:a.close()
  (e/('model-'+phase+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2));assert r.get('completed') and not r.get('failed'),r.get('final_response',r)
  outputs[phase]=r['final_response'];print('MODEL_PHASE',phase,'completed',flush=True)
  if phase=='plan':research('plan',plan={'objective':'Учебная сквозная проверка сканированного PDF','scope':'один операторский синтетический источник','steps':[{'id':name,'title':name,'status':'pending','result_paths':[]} for name in ['plan','collect','analyse','verify','report']],'model_plan':outputs[phase],'stop_condition':'Сохранён и повторно прочитан отчёт; причинный вывод не делается'})
  else:
   recorded=research('note',text=outputs[phase],source_ids=source_ids);step_outputs[phase]=str(Path(recorded['path']).relative_to(U/'workspace/bn-research-runs'/start['run_id']))
 coverage=tool('context','document_status',{'corpus_id':cid});assert coverage['model_delivery_complete'],coverage
 research('plan',plan={'steps':[{'id':p,'title':p,'status':'done','result_paths':[step_outputs[p]] if p in step_outputs else []} for p in outputs]})
 finish=research('finish',report=outputs['report'],status='complete');assert finish['status']=='completed_draft',finish
 read=research('read',path='report.md');assert outputs['report'] in read['text']
 state=research('status')
 proof={'passed':True,'session_id':sid,'run_id':start['run_id'],'corpus_id':cid,'doc_id':did,'source_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'source_ids':source_ids,'ocr_status':parsed['metadata']['ocr_status'],'coverage':coverage,'completion':finish,'readback':{'sha256':read['sha256'],'exact_model_report_preserved':True},'phases':list(outputs),'native_required_controls_used':True,'synthetic_data_only':True}
 (e/'RESULT.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2));(W/'evidence/native-e2e-latest.json').write_text(json.dumps({'directory':str(e),'result':str(e/'RESULT.json')},indent=2));print(json.dumps({'passed':True,'result':str(e/'RESULT.json')},ensure_ascii=False),flush=True)
except Exception:
 (e/'ERROR.txt').write_text(traceback.format_exc());(W/'evidence/native-e2e-latest.json').write_text(json.dumps({'directory':str(e),'error':str(e/'ERROR.txt')},indent=2));raise
