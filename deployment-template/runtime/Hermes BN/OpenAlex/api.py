"""Read-only official OpenAlex API and bounded local research files."""
from pathlib import Path
from datetime import datetime,timezone
import csv,fcntl,hashlib,io,json,os,re,sys,time,uuid
from urllib.parse import quote,urlsplit,urlencode
from zoneinfo import ZoneInfo
import xml.etree.ElementTree as ET
import httpx
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parent
BASE='https://api.openalex.org'
ENTITIES=['works','authors','sources','institutions','publishers','funders','awards','locations','raw-affiliation-strings',
 'topics','subfields','fields','domains','keywords','sdgs','study-designs','work-types','source-types','institution-types',
 'countries','continents','languages','licenses','indexes','source-lists','collections']

def now():return datetime.now(ZoneInfo('__TIMEZONE__')).isoformat()
def atomic(path,value):
 p=path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp');p.write_text(json.dumps(value,ensure_ascii=False));p.chmod(0o600);p.replace(path)
def credential():
 p=ROOT/'credentials.json'
 if not p.exists():return None
 if p.stat().st_mode & 0o077:raise ValueError('credentials.json must have permissions 0600')
 return json.loads(p.read_text())['api_key']
def clean(value,key=None):
 if isinstance(value,dict):return {k:('[redacted]' if k.lower() in ('api_key','access_token','refresh_token') and isinstance(v,str) else clean(v,key)) for k,v in value.items()}
 if isinstance(value,list):return [clean(v,key) for v in value]
 if isinstance(value,str) and key:return value.replace(key,'[redacted]')
 return value
class APIError(Exception):
 def __init__(self,message,status=None,diagnostic_file=None):super().__init__(message);self.status=status;self.diagnostic_file=diagnostic_file

def budget_cap(settings,key=True):
 cap=settings['local_daily_budget_usd']
 if settings.get('setup_mode',True):cap=min(cap,settings.get('setup_budget_usd',.15))
 return cap if key else min(cap,.08)

def request(path,params=None,method='GET',body=None,estimate=0.0001,cache=True,binary=False):
 key=credential();url=path if path.startswith('https:') else BASE+path;parsed=urlsplit(url)
 if parsed.scheme!='https' or parsed.hostname not in ('api.openalex.org','content.openalex.org'):raise ValueError('Only official OpenAlex API/content hosts are permitted')
 if parsed.query:raise ValueError('Pass query parameters separately; credentials must never appear in a URL')
 if method!='GET' and not (parsed.hostname=='api.openalex.org' and parsed.path in ('/','/query','/text','/text/topics','/text/keywords')):raise ValueError('Writes to accounts and scientific records are not enabled')
 p=dict(params or {})
 if any(k.lower() in ('api_key','authorization','mailto') for k in p):raise ValueError('Credentials are loaded only from the independent private file')
 settings=json.loads((ROOT/'config/settings.json').read_text());partition=hashlib.sha256((key or 'anonymous').encode()).hexdigest()[:16]
 cache_key=hashlib.sha256(json.dumps([url,p,body,method,partition],sort_keys=True).encode()).hexdigest();cached=ROOT/'cache'/(cache_key+'.json')
 state_path=ROOT/'config/transport.json';day=datetime.now(timezone.utc).date().isoformat()
 with (ROOT/'config/request.lock').open('a+') as f:
  fcntl.flock(f,fcntl.LOCK_EX)
  if cache and not binary and cached.exists():
   saved=json.loads(cached.read_text())
   if time.time()-saved['epoch']<settings['cache_seconds']:return {**saved['result'],'cache_hit':True}
  state=json.loads(state_path.read_text()) if state_path.exists() else {}
  if state.get('day')!=day or state.get('partition')!=partition:state={'day':day,'partition':partition,'local_spent_usd':0}
  if state.get('blocked_until',0)>time.time():raise APIError('OpenAlex requested a pause; no request sent',429)
  if estimate and state.get('free_remaining_usd') is None and key:raise APIError('Check service_status first to establish the remaining free daily budget')
  cap=budget_cap(settings,bool(key))
  if estimate+state.get('local_spent_usd',0)>cap+1e-9:raise APIError('Local daily budget reached; no prepaid usage is authorized',429)
  if estimate>state.get('free_remaining_usd',0.1)+1e-9:raise APIError('Free daily budget insufficient; prepaid balance will not be used',429)
  delay=settings['minimum_interval_seconds']-(time.time()-state.get('last_finished',0))
  if delay>0:time.sleep(delay)
  headers={'User-Agent':'HermesBN-OpenAlex/1.0','Accept':'application/octet-stream' if binary else 'application/json'}
  if key:headers['Authorization']='Bearer '+key
  with httpx.Client(timeout=httpx.Timeout(60,connect=10),follow_redirects=False) as client:r=client.request(method,url,params=p,json=body,headers=headers)
  limits={k:v for k,v in r.headers.items() if k.startswith('x-ratelimit') or k=='retry-after'}
  cost=float(r.headers.get('x-ratelimit-cost-usd',r.headers.get('x-ratelimit-credits-used','0')))
  if 'x-ratelimit-cost-usd' not in r.headers:cost/=10000
  state['local_spent_usd']=round(state.get('local_spent_usd',0)+cost,8);state['last_finished']=time.time()
  if 'x-ratelimit-remaining-usd' in r.headers:state['free_remaining_usd']=float(r.headers['x-ratelimit-remaining-usd'])
  if r.status_code==429:
   try:pause=float(r.headers.get('retry-after','10'))
   except ValueError:pause=10
   state['blocked_until']=time.time()+max(pause,1)
  atomic(state_path,state)
  safe_url=url+('?' + urlencode(p) if p else '')
  if r.status_code>=400:
   diagnostic=ROOT/'checks'/('upstream-error-'+uuid.uuid4().hex+'.json');text=clean(r.text,key)
   atomic(diagnostic,{'status':r.status_code,'source_url':safe_url,'headers':limits,'body':text})
   try:
    error=r.json();brief=error.get('message',error.get('error',error));brief=json.dumps(brief,ensure_ascii=False) if not isinstance(brief,str) else brief
   except ValueError:brief=text
   raise APIError(clean(brief,key)[:600],r.status_code,str(diagnostic))
  result={'http_status':r.status_code,'source_url':safe_url,'retrieved_at':now(),'cache_hit':False,'api_key_used':bool(key),'cost_usd':cost,'response_limits':limits}
  if binary:return {**result,'bytes':r.content,'content_type':r.headers.get('content-type'),'redirect':r.headers.get('location')}
  if 300<=r.status_code<400:raise APIError('Unexpected redirect; no credentials forwarded',r.status_code)
  data=clean(r.json(),key)
  if parsed.path=='/rate-limit':
   budget=data.get('rate_limit',{});state['free_remaining_usd']=budget.get('daily_remaining_usd');atomic(state_path,state)
  result['data']=data
  if cache:atomic(cached,{'epoch':time.time(),'result':result})
  return result

def identifier(value):
 value=value.strip()
 if re.search(r'[\x00-\x20\x7f]',value) or '?' in value or '#' in value or len(value)>1200:raise ValueError('Invalid identifier')
 if value.startswith('https://openalex.org/'):value=value.removeprefix('https://openalex.org/')
 if value.startswith(('http://','https://')):
  if urlsplit(value).hostname not in ('doi.org','dx.doi.org','orcid.org','ror.org','pubmed.ncbi.nlm.nih.gov','www.ncbi.nlm.nih.gov'):raise ValueError('Unknown external identifier namespace')
 elif not re.fullmatch(r'(?:[WAISPF TG]\d+|col_[A-Za-z0-9_-]+|(?:doi|pmid|pmcid|orcid|ror|issn|mag):.+|10\.\d{4,9}/.+|[A-Za-z0-9_.-]+)',value):raise ValueError('Invalid identifier')
 return quote(value,safe='/:')
def single(entity,value,select=None):
 if entity not in ENTITIES:raise ValueError('Unknown entity endpoint')
 if value.startswith('https://openalex.org/'+entity+'/'):value=value.removeprefix('https://openalex.org/'+entity+'/')
 if entity=='works' and re.match(r'^10\.\d{4,9}/',value):value='https://doi.org/'+value
 p={'select':','.join(select)} if select else None
 external=value.startswith(('https://doi.org/','http://doi.org/','https://orcid.org/','https://ror.org/','doi:','pmid:','pmcid:','orcid:','ror:','issn:','10.'))
 return request('/'+entity+'/'+identifier(value),p,estimate=.0001 if external else 0)
def params(args):
 p={k:args[k] for k in ('page','per_page','cursor','sample','seed','sort','group_by','corpus') if k in args};p.setdefault('per_page',10)
 if args.get('filters'):p['filter']=','.join(args['filters'])
 if args.get('select'):p['select']=','.join(args['select'])
 for field,value in args.get('searches',{}).items():
  if field not in ('search','search.exact','search.title','search.title.exact','search.title_and_abstract','search.title_and_abstract.exact','search.title_abstract_keywords','search.title_abstract_keywords.exact','search.semantic'):raise ValueError('Unknown search parameter')
  p[field]=value
 if 'search.semantic' in p and len(args['searches'])>1:raise ValueError('Semantic search cannot be combined with other search modes')
 if args.get('rerank'):p['rerank']='true'
 if 'cursor' in p and 'page' in p:raise ValueError('Choose cursor or basic page')
 if p.get('page',1)*p['per_page']>10000:raise ValueError('Use cursor beyond 10000 results')
 if p.get('group_by') and 'page' in p:raise ValueError('Grouped responses require cursor paging')
 return p
def listing(entity,args):
 p=params(args)
 if entity!='works' and 'corpus' in p:raise ValueError('corpus applies only to works')
 estimate=.001 if any(k.startswith('search') for k in p) or any('.search' in f.split(':',1)[0] for f in args.get('filters',[])) else .0001
 if args.get('rerank'):estimate+=.001
 result=request('/'+entity,p,estimate=estimate,cache='cursor' not in p and 'sample' not in p)
 result['reading_level']='Returned metadata and indexed abstracts only; a match in fulltext search does not mean fulltext reading'
 result['coverage']='OpenAlex index, not all worldwide research; preserve corpus, filters, dates and meta.next_cursor'
 return result
def work(value):return single('works',value)
def file_name(value):
 if Path(value).name!=value or value in ('.','..'):raise ValueError('Use a bare filename')
 return value
def content_path(value):
 p=Path(value).resolve(strict=True)
 if not p.is_file() or not p.is_relative_to((ROOT/'inbox').resolve()):raise ValueError('Content must be an imported file in OpenAlex/inbox')
 return p
def download(args):
 if not credential():raise ValueError('Content downloads require the separately saved API key')
 result=work(args['id']);record=result['data'];wid=record['id'].split('/')[-1]
 fmt=args['format'];field='grobid_xml' if fmt=='tei' else 'pdf';extension='.grobid-xml' if fmt=='tei' else '.pdf'
 if not record.get('has_content',{}).get(field):raise APIError('Requested cached content is not available',404)
 dest=ROOT/'inbox'/(wid+extension)
 if dest.exists():return {'path':str(dest),'work_id':wid,'already_downloaded':True,'reading_level':'Previously saved file; no new reading'}
 fetched=request('https://content.openalex.org/works/'+wid+extension,estimate=.01,cache=False,binary=True)
 raw=fetched.pop('bytes');redirect=fetched.pop('redirect')
 if redirect:
  u=urlsplit(redirect)
  if u.scheme!='https' or not (u.hostname or '').endswith('.r2.cloudflarestorage.com'):raise APIError('Unrecognized content storage redirect; credentials were not forwarded')
  with httpx.Client(timeout=90,follow_redirects=False) as c:r=c.get(redirect)
  if r.status_code!=200:raise APIError('Content storage download failed',r.status_code)
  raw=r.content
 if len(raw)>50*1024**2:raise ValueError('Content exceeds the controlled 50 MB limit')
 if fmt=='pdf' and not raw.startswith(b'%PDF'):raise ValueError('OpenAlex did not return a PDF')
 if fmt=='tei':
  if raw.startswith(b'\x1f\x8b'):
   import gzip;raw=gzip.decompress(raw)
  root=ET.fromstring(raw)
  if root.tag.rsplit('}',1)[-1]!='TEI':raise ValueError('Content is not TEI XML')
 with dest.open('xb') as f:f.write(raw)
 dest.chmod(0o600)
 provenance={'work_id':wid,'doi':record.get('doi'),'format':fmt,'source_url':fetched['source_url'],'retrieved_at':fetched['retrieved_at'],'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'best_oa_location':record.get('best_oa_location'),'reading_level':'File downloaded; article not yet read','cost_usd':fetched['cost_usd']}
 atomic(dest.with_suffix(dest.suffix+'.provenance.json'),provenance)
 return {**fetched,**provenance,'path':str(dest)}
def node_text(node):return ' '.join(' '.join(node.itertext()).split())

def execute(name,args):
 if name=='service_status':
  if not credential():return {'mode':'public_without_key','api_key_used':False,'mcp_oauth':'separate authorization','fulltext_downloads':'key_required'}
  r=request('/rate-limit',estimate=0,cache=False);r.update(mode='personal_key',local_daily_budget_usd=budget_cap(json.loads((ROOT/'config/settings.json').read_text())),prepaid_usage_enabled=False,account_writes_enabled=False);return r
 if name=='list_entities':return listing(args['entity'],{k:v for k,v in args.items() if k!='entity'})
 if name=='get_entity':return {**single(args['entity'],args['id'],args.get('select')),'reading_level':'Metadata/abstract if present, not full article text'}
 if name=='batch_entities':
  query={'filters':['ids.openalex:'+'|'.join(args['ids'])],'per_page':len(args['ids'])}
  if args.get('select'):query['select']=list(dict.fromkeys(['id']+args['select']))
  if args['entity']=='works':query['corpus']='all'
  result=listing(args['entity'],query);returned=[x['id'] for x in result['data'].get('results',[])];short=lambda x:x.removeprefix('https://openalex.org/').upper()
  result.update(requested_ids=args['ids'],returned_ids=returned,missing_ids=[x for x in args['ids'] if short(x) not in {short(y) for y in returned}],lookup_corpus='all' if args['entity']=='works' else None)
  return result
 if name=='group_entities':return listing(args['entity'],{k:v for k,v in args.items() if k!='entity'})
 if name=='semantic_search':
  if any(f.startswith(('cited_by_count:','last_known_institutions.country_code:','country_code:')) for f in args.get('filters',[])):raise ValueError('These filters are not supported by semantic search')
  return listing('works',{'searches':{'search.semantic':args['query']},'filters':args.get('filters',[]),'per_page':args.get('limit',5),'select':args.get('select',['id','title','doi','publication_year','relevance_score'])})
 if name=='autocomplete':return request('/autocomplete/'+args['entity'],{'q':args['query']},estimate=.0001)
 if name in ('read_abstract','work_links','work_metrics','citations'):
  r=work(args['id']);d=r.pop('data');r['work_id']=d['id'];r['doi']=d.get('doi')
  if name=='read_abstract':
   index=d.get('abstract_inverted_index')
   if not index:return {**r,'abstract_available':False,'reading_level':'Metadata only; no abstract supplied'}
   words={}
   for word,positions in index.items():
    for pos in positions:
     if not isinstance(pos,int) or not 0<=pos<100000 or pos in words:raise ValueError('Invalid/ambiguous abstract index')
     words[pos]=word
   text=' '.join(words.get(i,'[missing indexed word]') for i in range(max(words)+1));start=args.get('start',0);length=args.get('length',6000)
   return {**r,'abstract_available':True,'text':text[start:start+length],'start':start,'total_characters':len(text),'has_more':start+length<len(text),'reading_level':'Only returned reconstructed indexed abstract; no full article text'}
  if name=='work_links':return {**r,**{k:d.get(k) for k in ['open_access','primary_location','best_oa_location','locations','has_content','content_urls','is_retracted']},'reading_level':'Version/license/link metadata; content not downloaded or read'}
  if name=='work_metrics':return {**r,**{k:d.get(k) for k in ['cited_by_count','counts_by_year','fwci','citation_normalized_percentile','cited_by_percentile_year','publication_year','is_retracted']},'coverage':'Metrics from this index; not scientific validity or citation stance'}
  direction=args.get('direction','incoming');wid=d['id'].split('/')[-1]
  fields=args.get('select',['id','doi','display_name','publication_year','type','cited_by_count','primary_location'])
  if direction=='incoming':return {**listing('works',{'filters':['cites:'+wid],'per_page':args.get('limit',5),'select':fields,**({'cursor':args['cursor']} if args.get('cursor') else {})}),'direction':'incoming','target_work':wid,'reported_cited_by_count':d.get('cited_by_count'),'fields_returned':fields}
  ids=d.get('referenced_works' if direction=='outgoing' else 'related_works',[]);start=args.get('start',0);selected=ids[start:start+args.get('limit',5)]
  if not selected:return {**r,'direction':direction,'ids':[],'total_ids':len(ids),'has_more':False}
  return {**listing('works',{'filters':['ids.openalex:'+'|'.join(x.split('/')[-1] for x in selected)],'per_page':len(selected),'corpus':'all','select':fields}),'direction':direction,'total_ids':len(ids),'selected_ids':selected,'start':start,'has_more':start+len(selected)<len(ids),'lookup_corpus':'all','fields_returned':fields,'coverage':'Matched indexed references/relatedness, not all printed references or semantic support'}
 if name=='translate_query':return request('/query',method='POST',body={args['format']:args['query']},estimate=0,cache=False)
 if name=='execute_query':
  query={args['format']:args['query']};check=request('/query',method='POST',body=query,estimate=0,cache=False)['data']
  if not check.get('validation',{}).get('valid'):raise ValueError('OQL/OQO validation failed')
  cost=check.get('check',{}).get('cost',{})
  if not cost and ('calculate' in check.get('oqo',{}) or 'search in' in check.get('oql','').lower()):raise ValueError('No price preview for this complex query; execution stopped')
  estimate=cost.get('usd',cost.get('cost_usd',.001)) if isinstance(cost,dict) else float(cost)/10000
  if estimate>0.03:raise ValueError('Query exceeds the controlled per-call budget; inspect translate_query first')
  body={**query,**{k:args[k] for k in ('page','per_page','cursor','sort','select','rerank') if k in args}}
  return request('/',method='POST',body=body,estimate=max(estimate,.0001),cache=False)
 if name=='classify_text':
  if not 20<=len(args['title'])+len(args.get('abstract',''))<=2000:raise ValueError('Combined title and abstract must contain 20 to 2000 characters')
  return request('/text'+('/'+args['kind'] if args.get('kind') in ('topics','keywords') else ''),method='POST',body={'title':args['title'],**({'abstract':args['abstract']} if args.get('abstract') else {})},estimate=.01,cache=False)
 if name=='download_content':return download(args)
 if name in ('content_structure','read_content'):
  path=content_path(args['path']);root=ET.parse(path).getroot();ns={'t':'http://www.tei-c.org/ns/1.0'}
  nodes=root.findall('.//t:text/t:body//t:div',ns);tables=root.findall('.//t:table',ns);abstracts=root.findall('.//t:abstract',ns)
  if name=='content_structure':return {'source_file':str(path),'source':'GROBID TEI parsed from a PDF, not original publisher XML','sections':[{'index':i,'title':node_text(n.find('t:head',ns)) if n.find('t:head',ns) is not None else '', 'characters':len(node_text(n))} for i,n in enumerate(nodes)],'tables':[{'index':i,'characters':len(node_text(n))} for i,n in enumerate(tables)],'abstracts':len(abstracts),'reading_level':'Structure only'}
  candidates={'section':nodes,'table':tables,'abstract':abstracts}[args['kind']];index=args.get('index',0)
  if not 0<=index<len(candidates):raise ValueError('Requested content section does not exist')
  table_rows=[[{'text':node_text(cell),'attributes':cell.attrib} for cell in row.findall('t:cell',ns)] for row in candidates[index].findall('t:row',ns)] if args['kind']=='table' else None
  text='\n'.join('\t'.join(cell['text'] for cell in row) for row in table_rows) if table_rows else node_text(candidates[index]);start=args.get('start',0);length=args.get('length',6000)
  return {'source_file':str(path),'kind':args['kind'],'index':index,'text':text[start:start+length],'table_rows':table_rows if start==0 and length>=len(text) else None,'table_rows_total':len(table_rows) if table_rows else None,'total_characters':len(text),'has_more':start+length<len(text),'reading_level':'Returned part of machine-extracted TEI; verify complex tables against original PDF'}
 if name in ('read_pdf_pages','render_pdf_page'):
  sys.path.insert(0,str(ROOT/'deps'));import pymupdf
  path=content_path(args['path'])
  with pymupdf.open(path) as doc:
   pages=args.get('pages',[args.get('page',1)])
   if any(not 1<=p<=len(doc) for p in pages):raise ValueError('PDF page out of range')
   if name=='render_pdf_page':
    p=ROOT/'exports'/(path.stem+'-page-'+str(pages[0])+'-'+uuid.uuid4().hex[:8]+'.png');doc[pages[0]-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(p);p.chmod(0o600)
    return {'image_path':str(p),'page':pages[0],'pages_total':len(doc),'source_file':str(path),'reading_level':'Specified original PDF page rendered; inspect image before claiming visual reading'}
   limit=args.get('max_characters_per_page',10000);entries=[]
   for p in pages:
    text=doc[p-1].get_text(sort=True);entries.append({'page':p,'text':text[:limit],'characters_total':len(text),'has_more':len(text)>limit})
   return {'pages':entries,'pages_total':len(doc),'source_file':str(path),'reading_level':'Only returned extracted page text; OCR not performed; full article not presumed read'}
 if name=='export_results':
  result=listing(args['entity'],args.get('query',{}));data=result['data'];rows=data.get('results') or data.get('group_by',[]);fmt=args['format'];path=ROOT/'exports'/file_name(args['output_name'])
  if fmt=='json':body=json.dumps(result,ensure_ascii=False,indent=2)
  elif fmt=='jsonl':body='\n'.join(json.dumps(x,ensure_ascii=False) for x in rows)+'\n'
  else:
   stream=io.StringIO();fields=args.get('fields') or (['key','key_display_name','count'] if data.get('group_by') else ['id','display_name','doi','publication_year','cited_by_count']);writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader()
   for row in rows:
    values={k:json.dumps(row[k],ensure_ascii=False) if isinstance(row.get(k),(list,dict)) else row.get(k,'') for k in fields}
    writer.writerow({k:"'"+v if isinstance(v,str) and v.startswith(('=','+','-','@')) else v for k,v in values.items()})
   body=stream.getvalue()
  with path.open('x') as f:f.write(body)
  path.chmod(0o600);return {'output_path':str(path),'records':len(rows),'total_matching':data.get('meta',{}).get('count'),'next_cursor':data.get('meta',{}).get('next_cursor'),'source_url':result['source_url'],'reading_level':'Exported returned page of metadata, not full result set or full texts'}
 if name=='save_query':
  check=request('/query',method='POST',body={args['format']:args['query']},estimate=0,cache=False)
  if not check['data'].get('validation',{}).get('valid'):raise ValueError('Invalid query')
  path=ROOT/'exports'/file_name(args['output_name']);data={'saved_at':now(),'query':check['data'],'purpose':args.get('purpose',''),'provider':'OpenAlex','cloud_alert_created':False}
  with path.open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2)
  path.chmod(0o600);return {'output_path':str(path),'cloud_write':False,'query':check['data']}
 raise ValueError('Unknown OpenAlex API operation')

def spec(description,props=None,required=None):return {'description':description,'input_schema':{'type':'object','properties':props or {},'required':required or [],'additionalProperties':False}}
S={'type':'string','minLength':1};ENTITY={'type':'string','enum':ENTITIES};ID={'id':S};ARRAY={'type':'array','items':S,'minItems':1,'maxItems':100}
QUERY={'filters':{'type':'array','items':S},'searches':{'type':'object','additionalProperties':S},'per_page':{'type':'integer','minimum':1,'maximum':100},'page':{'type':'integer','minimum':1},'cursor':S,'select':ARRAY,'sort':S,'sample':{'type':'integer','minimum':1,'maximum':10000},'seed':{'type':'integer'},'group_by':S,'corpus':{'type':'string','enum':['core','expansion','all']},'rerank':{'type':'boolean'}}
Q={'format':{'type':'string','enum':['oql','oqo']},'query':{'anyOf':[S,{'type':'object'}]}}
PATH={'path':S}
OPERATIONS={
 'service_status':spec('Проверить личный ключ, бесплатный остаток, тариф и собственные ограничения; ключ скрывается.'),
 'list_entities':spec('Полный официальный API поиска и фильтров по 26 активным типам сущностей. Полный текст поиска не равен чтению статьи.',{'entity':ENTITY,**QUERY},['entity']),
 'get_entity':spec('Полные метаданные по OpenAlex ID или DOI/PMID/PMCID/ORCID/ROR/ISSN, с исходными полями.',{'entity':ENTITY,**ID,'select':ARRAY},['entity','id']),
 'batch_entities':spec('До 100 однотипных OpenAlex ID через OR; вернуть покрытие и отсутствующие записи без выдумывания.',{'entity':ENTITY,'ids':ARRAY,'select':ARRAY},['entity','ids']),
 'group_entities':spec('Группировки и числа по полю; фиксировать корпус, пропуски, перекрытие групп и страницы.',{'entity':ENTITY,**QUERY},['entity','group_by']),
 'semantic_search':spec('Поиск работ по смыслу: до 50 результатов, запрос до 2000 знаков; не оценка научной достоверности.',{'query':{'type':'string','minLength':1,'maxLength':2000},'filters':{'type':'array','items':S},'limit':{'type':'integer','minimum':1,'maximum':50},'select':ARRAY},['query']),
 'autocomplete':spec('Подсказки имён сущностей и идентификаторов; совпадение имени не подтверждает личность.',{'entity':{'type':'string','enum':['works','authors','sources','institutions','publishers','funders','topics','keywords']},'query':S},['entity','query']),
 'read_abstract':spec('Восстановить порядок слов индексированной аннотации и прочитать ограниченный фрагмент.',{**ID,'start':{'type':'integer','minimum':0},'length':{'type':'integer','minimum':1,'maximum':30000}},['id']),
 'work_links':spec('OA, версии, лицензии, источники и доступность PDF/TEI. Не скачивает и не читает тексты.',ID,['id']),
 'work_metrics':spec('Счётчики, динамика, FWCI и процентили OpenAlex; не качество или поддержка научного вывода.',ID,['id']),
 'citations':spec('Входящие цитирования, внесённые исходящие ссылки или похожие работы; по умолчанию краткие записи, дополнительные поля через select. Контексты цитирования не предоставляются.',{**ID,'direction':{'type':'string','enum':['incoming','outgoing','related']},'limit':{'type':'integer','minimum':1,'maximum':100},'start':{'type':'integer','minimum':0},'cursor':S,'select':ARRAY},['id']),
 'translate_query':spec('Проверить и перевести OQL/OQO бесплатно, без исполнения; сохранить цену и предупреждения.',Q,['format','query']),
 'execute_query':spec('Выполнить проверенный OQL/OQO с вложенной логикой, группировками и расчётами, в пределах бесплатного бюджета.',{**Q,**{k:QUERY[k] for k in ['page','per_page','cursor','sort','select','rerank']}},['format','query']),
 'classify_text':spec('Классифицировать предоставленный публичный/согласованный текст по темам и ключевым словам; текущая модель октября 2026. Закрытый текст не передавать автоматически.',{'title':{'type':'string','minLength':1,'maxLength':2000},'abstract':{'type':'string','maxLength':1999},'kind':{'type':'string','enum':['topics','keywords','both']}},['title']),
 'download_content':spec('Один доступный оригинальный PDF или GROBID TEI из OpenAlex; личный ключ, контроль расходов, 50 МБ, без передачи ключа хранилищу.',{**ID,'format':{'type':'string','enum':['pdf','tei']}},['id','format']),
 'content_structure':spec('Структура местного GROBID TEI: разделы и таблицы. Это машинное извлечение, не издательский XML.',PATH,['path']),
 'read_content':spec('Прочитать ограниченный раздел, аннотацию или таблицу TEI; сложные таблицы сверять по PDF.',{**PATH,'kind':{'type':'string','enum':['section','table','abstract']},'index':{'type':'integer','minimum':0},'start':{'type':'integer','minimum':0},'length':{'type':'integer','minimum':1,'maximum':30000}},['path','kind']),
 'read_pdf_pages':spec('Прочитать текст указанных страниц оригинального PDF с 1, не более 10; распознавания сканов нет.',{**PATH,'pages':{'type':'array','items':{'type':'integer','minimum':1},'minItems':1,'maxItems':10},'max_characters_per_page':{'type':'integer','minimum':1,'maximum':30000}},['path','pages']),
 'render_pdf_page':spec('Изображение страницы исходного PDF для проверки таблиц и рисунков.',{**PATH,'page':{'type':'integer','minimum':1}},['path','page']),
 'export_results':spec('Сохранить полученную страницу метаданных/групп в JSON, JSONL или CSV; не объявлять полной выгрузкой.',{'entity':ENTITY,'query':{'type':'object','properties':QUERY,'additionalProperties':False},'format':{'type':'string','enum':['json','jsonl','csv']},'output_name':S,'fields':ARRAY},['entity','format','output_name']),
 'save_query':spec('Сохранить проверенный OQL/OQO и его происхождение местным файлом на AgentRuntime2; не создаёт почтовых уведомлений.',{**Q,'output_name':S,'purpose':{'type':'string'}},['format','query','output_name']),
}
def call(name,args=None):
 try:
  if name not in OPERATIONS:raise ValueError('Unknown operation')
  Draft202012Validator(OPERATIONS[name]['input_schema']).validate(args or {})
  return {'ok':True,'provider':'OpenAlex API','operation':name,**execute(name,args or {})}
 except Exception as e:return {'ok':False,'provider':'OpenAlex API','operation':name,'http_status':getattr(e,'status',None),'diagnostic_file':getattr(e,'diagnostic_file',None),'error':getattr(e,'message',str(e))[:800],'retry_policy':'No automatic retries, no paid balance, no provider substitution'}
