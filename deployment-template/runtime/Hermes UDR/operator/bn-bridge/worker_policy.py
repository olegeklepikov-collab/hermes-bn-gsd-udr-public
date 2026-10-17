"""Explicit read-only worker surface; effectful paths fail closed."""
READ_TOOLS={'mcp__context__document_read','mcp__context__document_status','mcp__context__document_describe','web_search','web_extract','tool_search','tool_describe','mcp__udr__udr_research','mcp__udr__udr_workspace','mcp__udr__udr_compare_rates'}
READ_OPERATIONS={
 'exa':['web_search_exa','web_search_advanced_exa','web_fetch_exa'],
 'tavily':['tavily_search','tavily_extract','tavily_map'],
 'keenable':['search_web_pages','fetch_page_content'],
 'parallel_search':['web_search'],
 'firecrawl':['firecrawl_search','firecrawl_scrape','firecrawl_map','firecrawl_research_search_papers','firecrawl_research_inspect_paper','firecrawl_research_related_papers','firecrawl_research_read_paper'],
 'consensus':['search'],
 'scite':['search_literature','citation_graph','read_fulltext','search_patents','search_clinical_trials','get_clinical_trial'],
 'undermind':['get_paper_info','search_papers','find_papers_by_author','lookup_papers_by_metadata','read_pdfs'],
 'alphaxiv':['discover_papers','get_paper_content','answer_pdf_queries'],
 'openalex':['search_works','get_work','resolve_references','list_citations','search_entities','get_entity'],
 'pubmed':['pubmed_search','pubmed_fetch','pubmed_summary','pmc_read','pmc_table','pmc_metadata'],
 'crossref':['works_search','work_get','bibliographic_match','work_references','work_relations']}
for server,operations in READ_OPERATIONS.items():READ_TOOLS.update('mcp__'+server+'__'+op for op in operations)
def domain_contains(domain,allowed):
 return domain in allowed or any(domain.endswith('.'+d) for d in allowed)

def urls_within(urls,domains):
 from urllib.parse import urlsplit
 if isinstance(urls,str):urls=[urls]
 if not isinstance(urls,list) or not urls:return False
 for url in urls:
  if not isinstance(url,str):return False
  parsed=urlsplit(url)
  if parsed.scheme not in {'http','https'} or parsed.username or not domain_contains((parsed.hostname or '').lower(),domains):return False
 return True

def worker_allows(name,args,read_paths=None,source_domains=()):
 if not isinstance(args,dict):return False
 if name=='mcp__firecrawl__firecrawl_scrape' and args.get('actions'):return False
 if name=='tool_call':
  calls=args.get('calls');return isinstance(calls,list) and len(calls)==1 and isinstance(calls[0],dict) and worker_allows(calls[0].get('name'),calls[0].get('arguments',{}),read_paths,source_domains)
 if name not in READ_TOOLS:return False
 if name=='mcp__udr__udr_workspace':
  return read_paths is None or args.get('request',{}).get('path') in read_paths
 if name=='mcp__udr__udr_research':
  request=args.get('request',{});return request.get('action')=='status' or (request.get('action')=='read' and (read_paths is None or request.get('path') in read_paths))
 if source_domains:
  domains=[d.lower() for d in source_domains]
  fetch_keys={'web_extract':'urls','mcp__exa__web_fetch_exa':'urls','mcp__tavily__tavily_extract':'urls','mcp__keenable__fetch_page_content':'url','mcp__firecrawl__firecrawl_scrape':'url','mcp__firecrawl__firecrawl_map':'url','mcp__tavily__tavily_map':'url'}
  if name in fetch_keys:return urls_within(args.get(fetch_keys[name]),domains)
  filters={'mcp__exa__web_search_advanced_exa':'includeDomains','mcp__tavily__tavily_search':'include_domains'}
  if name in filters:
   values=args.get(filters[name]);return isinstance(values,list) and bool(values) and all(isinstance(d,str) and domain_contains(d.lower(),domains) for d in values) and args.get('include_domains_mode','restrict')=='restrict'
  if name=='mcp__keenable__search_web_pages':return isinstance(args.get('site'),str) and domain_contains(args['site'].lower(),domains)
  if name in {'tool_search','tool_describe','mcp__context__document_read','mcp__context__document_status','mcp__context__document_describe'}:return True
  return False # No hard domain parameter in this interface; choose a supported one.
 return True
