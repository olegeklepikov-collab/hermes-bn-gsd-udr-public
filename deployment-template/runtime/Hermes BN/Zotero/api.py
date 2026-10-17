"""Hermes BN adapter to the official Zotero 10 local API; no database writes."""
from pathlib import Path
import hashlib, html, json, mimetypes, re, sys, uuid
from urllib.parse import urlencode, urlsplit, unquote
import httpx

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'deps'))
IDENTITY = ROOT / 'config/identity.json'
AUTH = ROOT / 'config/authorization.json'
EXPORT_FORMATS = ['bibtex','biblatex','bookmarks','coins','csljson','csv','mods','refer',
                  'rdf_bibliontology','rdf_dc','rdf_zotero','ris','tei','wikipedia']
KEY = re.compile(r'^[A-Z0-9]{8}$')

class ZoteroError(Exception):
    def __init__(self, message, status=None):
        super().__init__(message)
        self.status = status

def config():
    return json.loads(IDENTITY.read_text())

def object_key(key):
    if not isinstance(key, str) or not KEY.fullmatch(key):
        raise ValueError('Expected an eight-character Zotero object key')
    return key

def library(args):
    kind = args.get('library_type', 'user')
    ident = args.get('library_id', 0)
    if kind not in ('user', 'group') or not isinstance(ident, int) or ident < 0:
        raise ValueError('Invalid library scope')
    if kind == 'user' and ident != 0:
        raise ValueError('The pinned local personal library uses users/0')
    return f"{'users' if kind == 'user' else 'groups'}/{ident}"

def request(path, method='GET', params=None, data=None, form=None, headers=None):
    c = config()
    if method != 'GET' and not path.startswith('users/0/'):
        raise ValueError('Writes are limited to the personal library of the pinned instance')
    base = c['base_url']
    h = {'Zotero-API-Version':'3', 'Zotero-Server-ID':c['server_id']}
    if method != 'GET':
        if not AUTH.exists():
            raise ZoteroError('Persistent local write authorization has not been granted', 401)
        auth = json.loads(AUTH.read_text())
        if not auth.get('remember') or auth.get('server_id') != c['server_id']:
            raise ZoteroError('Authorization does not match the pinned instance', 412)
        h['Zotero-API-Key'] = auth['key']
    h.update(headers or {})
    with httpx.Client(timeout=60, follow_redirects=False, trust_env=False) as client:
        r = client.request(method, base + path, params=params, json=data, data=form, headers=h)
    sid = r.headers.get('Zotero-Server-ID')
    if sid and sid != c['server_id']:
        raise ZoteroError('Zotero instance changed; stop and reauthorize the intended library', 412)
    if r.status_code >= 400:
        raise ZoteroError(r.text[:2500], r.status_code)
    info = {'http_status':r.status_code, 'library_version':r.headers.get('Last-Modified-Version'),
            'total_results':r.headers.get('Total-Results')}
    if r.status_code == 302:
        return {'location':r.headers.get('Location'), **info}
    if not r.content:
        return {'ok':True, **info}
    if 'json' in r.headers.get('Content-Type',''):
        value = r.json()
        if isinstance(value, dict) and 'failed' in value:
            info['ok'] = not bool(value['failed'])
            info['partial_failure'] = bool(value['failed'])
        return {'data':value, **info}
    return {'text':r.text, **info}

def read_item(args, key=None):
    return request(library(args) + '/items/' + object_key(key or args['key']))

def batch_create(args, kind, objects):
    if not isinstance(objects, list) or not 1 <= len(objects) <= 50:
        raise ValueError('Supply one to fifty objects')
    for value in objects:
        if not isinstance(value, dict) or 'key' in value or 'version' in value:
            raise ValueError('Create accepts new objects without keys or versions; use patch for updates')
        if kind == 'items' and value.get('inPublications'):
            raise ValueError('Publishing is outside this connection')
    token = args.get('write_token') or uuid.uuid4().hex
    if not re.fullmatch(r'[A-Za-z0-9]{1,32}', token):
        raise ValueError('Invalid write token')
    result = request(library(args) + '/' + kind, 'POST', data=objects,
                     headers={'Zotero-Write-Token':token})
    result['write_token'] = token
    result['retry_policy'] = 'Do not repeat a changed request with this token. Inspect per-entry results.'
    return result

def patch(args, kind, changes=None):
    version = args['expected_version']
    if not isinstance(version, int) or version < 0:
        raise ValueError('expected_version must be the last read local object version')
    changes = changes if changes is not None else args['changes']
    if any(k in changes for k in ('key','version','inPublications')):
        raise ValueError('Key, version and publication status cannot be patched here')
    return request(library(args) + '/' + kind + '/' + object_key(args['key']), 'PATCH',
                   data=changes, headers={'If-Unmodified-Since-Version':str(version)})

def attachment_path(args):
    item = read_item(args)['data']['data']
    if item.get('itemType') != 'attachment':
        raise ValueError('An attachment key is required')
    result = request(library(args) + '/items/' + object_key(args['key']) + '/file/view/url')
    url = result.get('text','').strip()
    # Zotero returns JSON {url: file://...} in some versions.
    if 'data' in result:
        value = result['data']
        url = value.get('url','') if isinstance(value,dict) else value
    parsed = urlsplit(url)
    if parsed.scheme != 'file' or parsed.netloc not in ('', 'localhost'):
        raise ValueError('Zotero did not return a local attachment file')
    path = Path(unquote(parsed.path)).resolve(strict=True)
    if not path.is_relative_to(Path(config()['data']).resolve()):
        raise ValueError('Attachment file is outside this independent Zotero data directory')
    return path, item

def output_file(name, text=None, binary=None):
    if Path(name).name != name or name in ('.','..'):
        raise ValueError('Output name must be a bare filename')
    directory = Path(config()['output_root'])
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / name
    # Refuse accidental replacement of a prior report/export.
    if target.exists():
        raise ValueError('Output already exists; choose a new name')
    with target.open('xb') as f:
        f.write(binary if binary is not None else text.encode('utf-8'))
    target.chmod(0o600)
    return str(target)

def upload(args):
    path = Path(args['path']).resolve(strict=True)
    roots = [Path(x).resolve() for x in config()['import_roots']]
    if not path.is_file() or not any(path.is_relative_to(r) for r in roots):
        raise ValueError('Copy the authorized file to Zotero/inbox or Hermes data/workspace first')
    if path.stat().st_size > 100 * 1024**2:
        raise ValueError('This adapter limits a file to 100 MB; Zotero itself allows up to 4 GB')
    object_key(args['parent_key'])
    parent = read_item(args, args['parent_key'])['data']['data']
    if parent.get('itemType') in ('note','annotation','attachment'):
        raise ValueError('The parent must be a bibliographic record')
    content_type = args.get('content_type') or mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    item = {'itemType':'attachment','parentItem':args['parent_key'],'linkMode':'imported_file',
            'title':args.get('title') or path.name,'contentType':content_type,'filename':path.name,
            'tags':[]}
    creation = batch_create(args,'items',[item])
    if creation.get('ok') is False:
        return creation
    key = creation['data']['successful']['0']['key']
    endpoint = library(args) + '/items/' + key + '/file'
    payload = path.read_bytes()
    md5 = hashlib.md5(payload).hexdigest()
    conditions = {'If-None-Match':'*'}
    auth = request(endpoint,'POST',form={'md5':md5,'filename':path.name,'filesize':str(len(payload)),
            'mtime':str(path.stat().st_mtime_ns//1_000_000),'contentType':content_type},headers=conditions)
    details = auth['data']
    if not details.get('exists'):
        parsed = urlsplit(details['url']); base = urlsplit(config()['base_url'])
        if (parsed.scheme,parsed.hostname,parsed.port) != (base.scheme,base.hostname,base.port) or not re.fullmatch(r'/api/local/uploads/[A-Za-z0-9]{32}',parsed.path):
            raise ZoteroError('Unexpected upload destination; incomplete attachment '+key)
        with httpx.Client(timeout=120,trust_env=False,follow_redirects=False) as client:
            r = client.post(details['url'],content=payload,headers={'Content-Type':details.get('contentType',content_type)})
        if r.status_code >= 400:
            raise ZoteroError('File upload failed; incomplete attachment '+key,r.status_code)
        request(endpoint,'POST',form={'upload':details['uploadKey']},headers=conditions)
    return {'ok':True,'attachment_key':key,'parent_key':args['parent_key'],'bytes':len(payload),
            'sha256':hashlib.sha256(payload).hexdigest(),'stored_in_zotero':True,
            'reading_level':'File imported; no reading or fulltext indexing is implied',
            'item':read_item(args,key)['data']}

def execute(name, args):
    scope = library(args)
    if name == 'service_status':
        root = request('')
        count = request('users/0/items',params={'limit':1})
        c = config()
        return {'ok':True,'mode':'official_local_api','app_version':c['app_version'],
                'server_id':c['server_id'],'profile':c['profile'],'data_directory':c['data'],
                'account_username':c.get('account_username'),'account_bound':c.get('sync_account_bound',False),
                'write_key_saved':AUTH.exists(),'writes_personal_library_only':True,
                'items':count['total_results'],'cloud_access':'Native Zotero sync; no cloud API key',
                'delete_policy':'Permanent deletion and publishing are not exposed',**root}
    if name == 'schema':
        endpoint = args.get('kind','schema')
        allowed = ('schema','itemTypes','itemFields','creatorFields','itemTypeFields','itemTypeCreatorTypes')
        if endpoint not in allowed:
            raise ValueError('Unknown schema kind')
        return request(endpoint,params={'itemType':args['item_type']} if 'item_type' in args else None)
    if name == 'item_template':
        t = args['item_type']
        if not re.fullmatch(r'[A-Za-z]{1,40}',t): raise ValueError('Invalid item type')
        if t == 'annotation':
            data = json.loads((ROOT/'config/annotation-template-web.json').read_text())
        elif t == 'attachment':
            data = json.loads((ROOT/'config/attachment-template-web.json').read_text())
        elif t == 'note':
            data = {'itemType':'note','note':'','tags':[],'collections':[],'relations':{}}
        else:
            fields = request('itemTypeFields',params={'itemType':t})['data']
            data = {'itemType':t,**{f['field']:'' for f in fields},'creators':[],'tags':[],'collections':[],'relations':{}}
        return {'template':data,'source':'Local type fields; special attachment/annotation structures cached from official public Web API templates','library_read':False}
    if name == 'groups': return request('users/0/groups')
    if name == 'query_items':
        params = {k:args[k] for k in ('q','qmode','sort','direction','start','limit','itemType','tag','includeTrashed') if k in args}
        params.setdefault('limit',25)
        if not 1 <= params['limit'] <= 100 or params.get('start',0) < 0: raise ValueError('Invalid page range')
        if 'keys' in args: params['itemKey'] = ','.join(object_key(k) for k in args['keys'])
        if 'collection_key' in args: path = f"{scope}/collections/{object_key(args['collection_key'])}/items"
        elif 'search_key' in args: path = f"{scope}/searches/{object_key(args['search_key'])}/items"
        else: path = scope + '/items' + ('/trash' if args.get('trash') else '')
        if args.get('top'): path += '/top'
        result = request(path,params=params)
        result['reading_level'] = 'Metadata and included notes/annotations; matched full text is not returned by this search'
        return result
    if name == 'get_item': return read_item(args)
    if name == 'item_children': return request(scope+'/items/'+object_key(args['key'])+'/children',params={'limit':args.get('limit',100)})
    if name == 'collections':
        path = scope+'/collections'
        if args.get('key'): path += '/'+object_key(args['key'])+('/collections' if args.get('children') else '')
        elif args.get('top'): path += '/top'
        return request(path,params={'limit':args.get('limit',100)})
    if name == 'tags':
        path = scope+'/tags'
        if args.get('collection_key'): path = scope+'/collections/'+object_key(args['collection_key'])+'/items/tags'
        return request(path,params={k:args[k] for k in ('q','qmode','limit','start') if k in args})
    if name == 'saved_searches':
        return request(scope+'/searches'+('/'+object_key(args['key']) if args.get('key') else ''))
    if name == 'fulltext_versions':
        return request(scope+'/fulltext',params={'since':args.get('since',0)})
    if name == 'read_fulltext':
        result = request(scope+'/items/'+object_key(args['key'])+'/fulltext')
        value = result['data']; body = value.pop('content','')
        start = args.get('start',0); length = args.get('length',6000)
        if not isinstance(start,int) or start < 0 or not isinstance(length,int) or not 1 <= length <= 30000: raise ValueError('Invalid text slice')
        return {**result,'data':{**value,'content':body[start:start+length]},'start':start,
                'returned_characters':len(body[start:start+length]),'indexed_content_characters':len(body),
                'has_more':start+length < len(body),'reading_level':'Only returned indexed text; indexing coverage is given separately'}
    if name == 'attachment_info':
        path,item = attachment_path(args)
        return {'path':str(path),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                'item':item,'reading_level':'File metadata; content not read'}
    if name in ('read_pdf_pages','render_pdf_page'):
        import pymupdf
        path,item = attachment_path(args)
        with pymupdf.open(path) as document:
            if document.needs_pass: raise ValueError('The PDF requires a password')
            if name == 'render_pdf_page':
                page = args['page']
                if not isinstance(page,int) or not 1 <= page <= len(document): raise ValueError('Invalid page')
                image = document[page-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).tobytes('png')
                return {'page':page,'pages_total':len(document),'image_path':output_file(args.get('output_name') or f"{args['key']}-page-{page}-{uuid.uuid4().hex[:8]}.png",binary=image),'reading_level':'Rendered specified page; inspect the image before claiming visual reading'}
            pages = args['pages']
            if not isinstance(pages,list) or not 1 <= len(pages) <= 10 or any(not isinstance(p,int) or not 1 <= p <= len(document) for p in pages): raise ValueError('Supply one to ten one-based PDF page numbers')
            limit = args.get('max_characters_per_page',12000)
            if not 1 <= limit <= 30000: raise ValueError('Invalid character limit')
            entries = []
            for p in pages:
                body = document[p-1].get_text(sort=True)
                entries.append({'page':p,'text':body[:limit],'characters_total':len(body),'has_more':len(body)>limit})
            return {'pages_total':len(document),'pages':entries,'source':'Local original PDF, PyMuPDF text extraction',
                    'reading_level':'Only returned page text; scanned text requires separate OCR; article not presumed fully read'}
    if name == 'export_items':
        fmt = args['format']
        if fmt not in EXPORT_FORMATS+['bib']: raise ValueError('Unsupported export format')
        params = {'format':fmt,'itemKey':','.join(object_key(k) for k in args['keys'])}
        if fmt == 'bib':
            style = args.get('style','apa')
            if not re.fullmatch(r'[a-z0-9-]{1,150}',style): raise ValueError('Use an official Zotero style identifier')
            params.update(style=style,locale=args.get('locale','en-US'),linkwrap=1)
        result = request(scope+'/items',params=params)
        if args.get('output_name'):
            body = result.get('text') or json.dumps(result.get('data'),ensure_ascii=False,indent=2)
            result['output_path'] = output_file(args['output_name'],text=body)
        result['reading_level'] = 'Bibliographic export; scientific claims and full text not verified'
        return result
    if name == 'create_items': return batch_create(args,'items',args['items'])
    if name == 'patch_item': return patch(args,'items')
    if name == 'create_collections': return batch_create(args,'collections',args['collections'])
    if name == 'patch_collection': return patch(args,'collections')
    if name == 'create_saved_searches': return batch_create(args,'searches',args['searches'])
    if name == 'patch_saved_search': return patch(args,'searches')
    if name == 'create_note':
        note = {'itemType':'note','note':args['html'],'tags':[{'tag':t} for t in args.get('tags',[])]}
        if args.get('parent_key'): note['parentItem'] = object_key(args['parent_key'])
        else: note['collections'] = [object_key(k) for k in args.get('collections',[])]
        return batch_create(args,'items',[note])
    if name == 'attach_file': return upload(args)
    if name == 'create_annotation':
        path,item = attachment_path({**args,'key':args['attachment_key']})
        if item.get('contentType') != 'application/pdf': raise ValueError('A stored PDF attachment is required')
        import pymupdf
        with pymupdf.open(path) as doc:
            p = args['page']
            if not isinstance(p,int) or not 1 <= p <= len(doc): raise ValueError('Invalid page')
        rects = args['rects']
        if not isinstance(rects,list) or not rects or any(not isinstance(r,list) or len(r)!=4 or any(not isinstance(v,(int,float)) for v in r) or r[2]<=r[0] or r[3]<=r[1] for r in rects): raise ValueError('Expected nonempty PDF rectangles [x1,y1,x2,y2] in Zotero bottom-left coordinates')
        annotation = {'itemType':'annotation','parentItem':args['attachment_key'],'annotationType':'highlight',
            'annotationText':args['text'],'annotationComment':args.get('comment',''),
            'annotationColor':args.get('color','#ffd400'),'annotationPageLabel':args.get('page_label',str(p)),
            'annotationSortIndex':f'{p-1:05d}|000000|00000',
            'annotationPosition':json.dumps({'pageIndex':p-1,'rects':rects},separators=(',',':')),'tags':[{'tag':t} for t in args.get('tags',[])]}
        return batch_create(args,'items',[annotation])
    if name == 'trash_item': return patch(args,'items',{'deleted':1})
    if name == 'restore_item': return patch(args,'items',{'deleted':0})
    if name == 'index_fulltext':
        path,item = attachment_path(args)
        if item.get('contentType') == 'application/pdf':
            import pymupdf
            with pymupdf.open(path) as document:
                if document.needs_pass: raise ValueError('Encrypted PDF')
                content = '\n'.join(p.get_text(sort=True) for p in document)
                payload = {'content':content,'indexedPages':len(document),'totalPages':len(document)}
                if not content.strip(): raise ValueError('No extractable PDF text; OCR is required')
        else:
            raise ValueError('This controlled indexer supports text PDFs only. The official local API rejected text/plain fulltext writes; the attachment itself is preserved.')
        result = request(scope+'/items/'+object_key(args['key'])+'/fulltext','PUT',data=payload)
        result.update(indexed_characters=len(content),coverage= {k:v for k,v in payload.items() if k!='content'},
                      reading_level='Machine text indexing; does not mean the agent read the content')
        return result
    raise ValueError('Unknown operation: '+str(name))

def call(name, args=None):
    try:
        result = execute(name,args or {})
        return {'ok':True,'provider':'Zotero local API','operation':name,**result}
    except Exception as e:
        return {'ok':False,'provider':'Zotero local API','operation':name,'error':str(e),
                'http_status':getattr(e,'status',None),'retry_policy':'Stop on 401, 412, 428 or partial write; no silent provider or instance fallback'}

def specification(description, props=None, required=None, write=False):
    base = {'library_type':{'type':'string','enum':['user','group'],'default':'user'},
            'library_id':{'type':'integer','minimum':0,'default':0}}
    base.update(props or {})
    return {'description':description,'write':write,'input_schema':{'type':'object','properties':base,'required':required or [],'additionalProperties':False}}

S = lambda: {'type':'string'}
I = lambda: {'type':'integer','minimum':0}
A = lambda: {'type':'array','items':{'type':'string'}}
O = lambda: {'type':'object'}
K = {'key':S()}
V = {**K,'expected_version':I()}
PATCH = {**V,'changes':O()}
OPERATIONS = {
 'service_status':specification('Check the pinned Zotero instance, paths, account binding, item count and saved write authorization.'),
 'schema':specification('Get the actual local schema, item fields, creator fields and item-specific field/type lists.',{'kind':S(),'item_type':S()}),
 'item_template':specification('Return an empty item structure using official field lists and cached public templates.',{'item_type':S()},['item_type']),
 'groups':specification('Read available group libraries; group writes are disabled.'),
 'query_items':specification('Search metadata or indexed full text (qmode=everything). Returns records, not matched full text. Supports collection, saved search, tags, item types, trash and pagination.',{'q':S(),'qmode':{'type':'string','enum':['titleCreatorYear','everything']},'sort':S(),'direction':{'type':'string','enum':['asc','desc']},'start':I(),'limit':I(),'itemType':S(),'tag':S(),'includeTrashed':{'type':'integer','enum':[0,1]},'keys':A(),'collection_key':S(),'search_key':S(),'trash':{'type':'boolean'},'top':{'type':'boolean'}}),
 'get_item':specification('Read one item, note, attachment or annotation and its local optimistic version.',K,['key']),
 'item_children':specification('Read child notes, attachments and PDF annotations.',{**K,'limit':I()},['key']),
 'collections':specification('Read collections and their hierarchy.',{**K,'top':{'type':'boolean'},'children':{'type':'boolean'},'limit':I()}),
 'tags':specification('Read/search library or collection tags.',{'q':S(),'qmode':S(),'limit':I(),'start':I(),'collection_key':S()}),
 'saved_searches':specification('Read native saved search names and conditions; execute through query_items(search_key).',K),
 'fulltext_versions':specification('Read locally indexed attachment keys and versions since a local version.',{'since':I()}),
 'read_fulltext':specification('Read a bounded slice of the indexed attachment text; report actual coverage and unread remainder.',{**K,'start':I(),'length':I()},['key']),
 'attachment_info':specification('Resolve a stored local attachment within this independent Zotero library; return hash and size.',K,['key']),
 'read_pdf_pages':specification('Extract original text from specified one-based PDF pages, at most ten. Does not perform OCR.',{**K,'pages':{'type':'array','items':{'type':'integer','minimum':1}},'max_characters_per_page':I()},['key','pages']),
 'render_pdf_page':specification('Render one original PDF page to PNG in Zotero/exports; inspect it for tables, figures and layout.',{**K,'page':{'type':'integer','minimum':1},'output_name':S()},['key','page']),
 'export_items':specification('Export references in 14 translator formats or CSL bibliography HTML. Uses official Zotero styles; does not verify scientific conclusions.',{'keys':A(),'format':{'type':'string','enum':EXPORT_FORMATS+['bib']},'style':S(),'locale':S(),'output_name':S()},['keys','format']),
 'create_items':specification('Create bibliographic records using official item fields. Inspect all per-entry failed results. Use a write token for a known retry.',{'items':{'type':'array','items':O()},'write_token':S()},['items'],True),
 'patch_item':specification('Patch selected fields using the last read local expected_version; array fields replace the whole array.',PATCH,['key','expected_version','changes'],True),
 'create_collections':specification('Create collections with name and optional parentCollection; memberships do not move attachment files.',{'collections':{'type':'array','items':O()},'write_token':S()},['collections'],True),
 'patch_collection':specification('Rename or reparent a collection with an optimistic version.',PATCH,['key','expected_version','changes'],True),
 'create_saved_searches':specification('Create native saved searches with name and condition/operator/value objects.',{'searches':{'type':'array','items':O()},'write_token':S()},['searches'],True),
 'patch_saved_search':specification('Update native saved search fields with an optimistic version.',PATCH,['key','expected_version','changes'],True),
 'create_note':specification('Create an HTML research note. State sources, pages actually read, evidence and limitations.',{'html':S(),'parent_key':S(),'collections':A(),'tags':A(),'write_token':S()},['html'],True),
 'attach_file':specification('Import an authorized local file from Zotero/inbox or Hermes data/workspace as a stored child attachment. Three-phase upload, hash verification, no overwritten files.',{'path':S(),'parent_key':S(),'title':S(),'content_type':S(),'write_token':S()},['path','parent_key'],True),
 'create_annotation':specification('Create a native PDF highlight on a specified page with verified text and bottom-left PDF rectangle coordinates.',{'attachment_key':S(),'page':{'type':'integer','minimum':1},'rects':{'type':'array','items':{'type':'array','items':{'type':'number'},'minItems':4,'maxItems':4}},'text':S(),'comment':S(),'color':S(),'page_label':S(),'tags':A(),'write_token':S()},['attachment_key','page','rects','text'],True),
 'index_fulltext':specification('Index actual extracted PDF text locally for qmode=everything; machine indexing is not agent reading. Rejects PDFs without text and unsupported plain-text attachment writes.',K,['key'],True),
 'trash_item':specification('Move an explicitly disposable or user-approved item to recoverable Zotero Trash. Requires the last read local version.',V,['key','expected_version'],True),
 'restore_item':specification('Restore a trashed item using the last read local version.',V,['key','expected_version'],True),
}
