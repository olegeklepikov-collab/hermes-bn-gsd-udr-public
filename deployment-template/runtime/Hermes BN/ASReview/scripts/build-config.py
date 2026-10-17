from pathlib import Path
from dataclasses import asdict
import json,copy
from asreview.models import get_ai_config
z=Path(__file__).resolve().parents[1]
models={}
for name in ['elas_u4','elas_u3','elas_l2','elas_h3']:
 m=get_ai_config(name);models[name]={'description':m['label'],'value':asdict(m['value']),'source':'official ASReview 3.0.8'}
for name,changes,description in [
 ('logistic_tfidf',{'classifier':'logistic','classifier_param':{}},'Логистическая регрессия и словесные признаки для сравнения'),
 ('forest_tfidf',{'classifier':'rf','classifier_param':{'n_estimators':100,'n_jobs':1}},'Случайный лес для сравнения на локальных данных'),
 ('mixed_random',{'querier':'max_random'},'Максимальный приоритет с 5% случайных записей'),
 ('mixed_uncertainty',{'querier':'max_uncertainty'},'Максимальный приоритет с 5% неопределённых записей'),
 ('uncertainty_tfidf',{'querier':'uncertainty'},'Проверка пограничных записей'),
 ('char_svm',{'feature_extractor_param':{'analyzer':'char_wb','ngram_range':[3,5],'min_df':1,'max_features':100000,'sublinear_tf':True}},'Символьные признаки для русскоязычных данных и вариаций написания'),
 ('random',{'classifier':None,'classifier_param':{},'balancer':None,'querier':'random','feature_extractor':None},'Случайный контрольный порядок'),
 ('top_down',{'classifier':None,'classifier_param':{},'balancer':None,'querier':'top_down','feature_extractor':None},'Исходный порядок для контрольной проверки')]:
 m=copy.deepcopy(models['elas_u4']['value']);m.update(changes);models[name]={'description':description,'value':m,'source':'Hermes BN configuration using official ASReview components'}
# Dense models use snapshots pinned after the initial download; no global model cache.
f=z/'config/model-snapshots.json'
if f.exists():
 snapshots=json.loads(f.read_text())
 for n,repo in [('elas_l2','intfloat/multilingual-e5-large'),('elas_h3','mixedbread-ai/mxbai-embed-large-v1')]:
  if repo in snapshots:models[n]['value']['feature_extractor_param'].update(model_name=snapshots[repo]['path'],device='cpu',verbose=False)
(z/'config/models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2))
import sys;sys.path.insert(0,str(z));from api import OPS
catalog={n:{k:v for k,v in d.items() if k!='fn'} for n,d in OPS.items()}
(z/'config/tool-catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2))
profiles={
 'installation':{'name':'service_status','arguments':{}},
 'models':{'name':'model_catalog','arguments':{}},
 'projects':{'name':'list_projects','arguments':{}},
 'synthetic_connection_test':{'name':'create_demo','arguments':{'project_id':'bn-connection-demo'}},
}
for model in models:
 profiles['review_'+model]={'name':'create_project','arguments':{'mode':'oracle','model':model,'seed':42},'required':['project_id','file']}
 profiles['validation_'+model]={'name':'create_project','arguments':{'mode':'validate','model':model,'seed':42},'required':['project_id','file']}
 profiles['simulation_'+model]={'name':'simulate','arguments':{'model':model,'seed':42,'stop':'all'},'required':['project_id','file']}
for fmt in ['csv','tsv','json','xlsx','ris']:
 for selection in ['all','relevant','irrelevant','unseen']:
  profiles['export_'+fmt+'_'+selection]={'name':'export_dataset','arguments':{'format':fmt,'filter':selection,'include_duplicates':True},'required':['project_id']}
for stop in ['last_relevant','n_labelled','consecutive_irrelevant']:
 profiles['simulation_stop_'+stop]={'name':'simulate','arguments':{'model':'elas_u4','seed':42,'stop':stop,'stop_value':100},'required':['project_id','file']}
for n,a in [('unseen_random_audit',{'size':20,'seed':42}),('unseen_larger_audit',{'size':100,'seed':42})]:profiles[n]={'name':'sample_audit','arguments':a,'required':['project_id']}
(z/'config/profiles.json').write_text(json.dumps(profiles,ensure_ascii=False,indent=2));print('models',len(models),'tools',len(catalog),'profiles',len(profiles))
