"""Bounded pure arithmetic and exact, paged local text; no model or nested loop."""
from pathlib import Path
from decimal import Decimal, localcontext
import hashlib, math

def compare_rates(before, after):
    for value in (before,after):
        if type(value) not in (int,float) or not 0<=value<=10**15 or not math.isfinite(value):
            raise ValueError('finite_nonnegative_number_at_most_1e15_required')
    with localcontext() as c:
        c.prec=50
        b,a=Decimal(str(before)),Decimal(str(after))
        difference=a-b
        return {'before':str(b),'after':str(a),'absolute_change':str(difference),
            'relative_change_percent':str(difference/b*100) if b else None,
            'relative_change_defined':bool(b),'method':'(after-before)/before*100; decimal arithmetic',
            'causality_established':False,'external_effect_performed':False}

def read_page(root,relative,offset=0,max_chars=4096):
    root=Path(root).resolve()
    if not isinstance(relative,str) or not relative or Path(relative).is_absolute() or '..' in Path(relative).parts:
        raise ValueError('scoped_relative_file_required')
    if Path(relative).parts[0] in {'teams','authority','runtime'} or any(part.startswith('.') for part in Path(relative).parts):
        raise ValueError('operator_bookkeeping_is_not_a_source; use public status')
    p=root/relative
    if p.is_symlink() or not p.resolve().is_relative_to(root) or not p.is_file():
        raise ValueError('scoped_regular_file_required')
    if type(offset) is not int or type(max_chars) is not int or offset<0 or not 1<=max_chars<=4096:
        raise ValueError('invalid_page_bounds')
    raw=p.read_bytes();text=raw.decode('utf-8',errors='strict')
    if offset>len(text):raise ValueError('offset_outside_document')
    fragment=text[offset:offset+max_chars];end=offset+len(fragment)
    return {'path':relative,'text':fragment,'sha256':hashlib.sha256(raw).hexdigest(),
        'fragment_sha256':hashlib.sha256(fragment.encode('utf-8')).hexdigest(),
        'offset':offset,'end_offset':end,'next_offset':end if end<len(text) else None,
        'complete':end==len(text),'whole_document_in_this_page':offset==0 and end==len(text),
        'total_characters':len(text),'total_bytes':len(raw),'offset_unit':'Unicode code points',
        'reading_level':'exact_preserved_text_page','coverage_claim':'This page only; aggregate contiguous pages to establish complete reading'}


def report_from_file(root,request):
    """Exact input adapter for the existing SDK report string; never publishes."""
    if 'report' in request:raise ValueError('choose_report_text_or_file')
    expected=request.get('report_sha256')
    if not isinstance(expected,str) or len(expected)!=64 or any(c not in '0123456789abcdef' for c in expected):raise ValueError('exact_report_sha256_required')
    page=read_page(root,request['report_path'],0,1)
    if page['sha256']!=expected:raise ValueError('report_source_version_changed')
    if page['total_bytes']>8*1024*1024:raise ValueError('split_report_into_addressed_documents_before_finish')
    raw=(Path(root)/request['report_path']).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected:raise ValueError('report_source_version_changed')
    result={k:v for k,v in request.items() if k not in {'report_path','report_sha256'}}
    result['report']=raw.decode('utf-8',errors='strict')
    return result
