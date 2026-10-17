#!/usr/bin/env python3
"""Apply a verified upgrade only to a fresh, restored copy, never to live BN/UDR."""
from pathlib import Path
import argparse,ctypes,hashlib,json,os,platform,shutil,stat,unicodedata
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        while block:=f.read(4*1024*1024):h.update(block)
    return h.hexdigest()
def local(root,relative):
    p=Path(relative)
    if p.is_absolute() or '..' in p.parts or not p.parts:raise ValueError('Unsafe relative path')
    target=root/p
    parent=target.parent
    while parent!=root:
        if parent.is_symlink():raise ValueError('Symlink ancestor refused: '+relative)
        parent=parent.parent
    return target
def metadata(path,row,full):
    s=path.lstat()
    if stat.S_IMODE(s.st_mode)!=row['mode']:return False
    kind=row['type']
    if kind=='file':good=stat.S_ISREG(s.st_mode) and s.st_size==row['size'] and sha(path)==row['sha256']
    elif kind=='directory':good=stat.S_ISDIR(s.st_mode)
    else:good=stat.S_ISLNK(s.st_mode) and os.readlink(path)==row['target']
    if good and full:
        from mac_metadata import hashes
        actual_attrs=hashes(path);expected_attrs=dict(row.get('xattrs',{}))
        actual_attrs.pop('com.apple.provenance',None);expected_attrs.pop('com.apple.provenance',None)
        good=actual_attrs==expected_attrs
    return good
def main():
    p=argparse.ArgumentParser();p.add_argument('--base-root',type=Path,required=True);p.add_argument('--update-root',type=Path,required=True);p.add_argument('--verify-only',action='store_true');a=p.parse_args()
    root=a.base_root.resolve();update=a.update_root.resolve();m=json.loads((update/'UPDATE.json').read_text());full=m['mode']=='full'
    if m['format']!='hermes-bn-recovery-delta/1':raise ValueError('Unsupported update format')
    if m['mode'] not in {'full','new-user'}:raise ValueError('Unsupported recovery mode')
    if full and platform.system()!='Darwin':raise ValueError('Full macOS metadata restore requires macOS')
    if m.get('platform')=='macos-arm64' and (platform.system()!='Darwin' or platform.machine()!='arm64'):raise ValueError('This runtime update is qualified only for macOS arm64')
    live=Path('/Volumes/AgentRuntime2/active-runtime')
    if root==live or any(root==live/n or root.is_relative_to(live/n) for n in ['Hermes BN','Hermes UDR']):raise ValueError('Live runtime destination refused; restore to a separate copy')
    if root.is_symlink() or update.is_relative_to(root):raise ValueError('Separate regular staging roots required')
    expected=update/'FINAL-MANIFEST.jsonl'
    if sha(expected)!=m['final_manifest_sha256']:raise ValueError('Final manifest integrity failed')
    if not a.verify_only:
        if (root/'RESTORE-APPLIED.json').exists():raise ValueError('Already applied; use --verify-only')
        if sha(root/'MANIFEST.jsonl')!=m['base_manifest_sha256']:raise ValueError('Wrong or altered base manifest')
        for row in m['changes']:
            source=local(update/'payload',row['path'])
            if not metadata(source,row,full):raise ValueError('Payload integrity failed: '+row['path'])
        removals=sorted(set(m['deleted']+m['replace_roots']),key=lambda s:len(Path(s).parts),reverse=True)
        for relative in removals:
            target=local(root,relative)
            if target.is_symlink() or target.is_file():target.unlink()
            elif target.is_dir():shutil.rmtree(target)
        lib=ctypes.CDLL('/usr/lib/libSystem.B.dylib',use_errno=True) if platform.system()=='Darwin' else None
        if lib:lib.copyfile.argtypes=[ctypes.c_char_p,ctypes.c_char_p,ctypes.c_void_p,ctypes.c_uint32]
        rows=sorted(m['changes'],key=lambda r:(r['type']!='directory',len(Path(r['path']).parts)))
        directories=[]
        for row in rows:
            source=local(update/'payload',row['path']);target=local(root,row['path']);target.parent.mkdir(parents=True,exist_ok=True)
            if row['type']=='directory':
                if target.is_symlink() or target.is_file():target.unlink()
                target.mkdir(exist_ok=True);directories.append((source,target,row));continue
            if target.is_symlink() or target.is_file():target.unlink()
            elif target.is_dir():shutil.rmtree(target)
            if row['type']=='symlink':
                target.symlink_to(row['target'])
                if full and lib:
                    if lib.copyfile(os.fsencode(source),os.fsencode(target),None,7|(1<<18)|(1<<19)):raise OSError(ctypes.get_errno(),str(target))
                else:shutil.copystat(source,target,follow_symlinks=False)
            elif full and lib:
                # One native complete copy preserves data and xattrs together.
                if lib.copyfile(os.fsencode(source),os.fsencode(target),None,15|(1<<24)):raise OSError(ctypes.get_errno(),str(target))
            else:
                shutil.copyfile(source,target);target.chmod(row['mode'])
        for source,target,row in reversed(directories):
            if full and lib:
                if lib.copyfile(os.fsencode(source),os.fsencode(target),None,7):raise OSError(ctypes.get_errno(),str(target))
            target.chmod(row['mode'])
        shutil.copyfile(expected,root/'MANIFEST.jsonl')
        (root/'MANIFEST.sha256').write_text(m['final_manifest_sha256']+'  MANIFEST.jsonl\n')
    checked=0;missing=[];expected_paths=set()
    for line in expected.open():
        row=json.loads(line);path=local(root,row['path'])
        expected_paths.add(unicodedata.normalize('NFC',row['path']))
        try:good=metadata(path,row,full)
        except (OSError,ValueError):good=False
        if not good:missing.append(row['path'])
        checked+=1
    actual=set()
    for base,ds,fs in os.walk(root,followlinks=False):
        for name in ds+fs:actual.add(unicodedata.normalize('NFC',str((Path(base)/name).relative_to(root))))
    generated={'MANIFEST.jsonl','MANIFEST.sha256','MANIFEST-summary.json','RESTORE-APPLIED.json'}
    unexpected=sorted(actual-expected_paths-generated)
    receipt={'format':'hermes-bn-update-application/1','mode':m['mode'],'verified_entries':checked,'mismatches':missing,'unexpected_paths':unexpected,'final_manifest_sha256':m['final_manifest_sha256'],'services_started':False,'credentials_used':False}
    (root/'RESTORE-APPLIED.json').write_text(json.dumps(receipt,indent=2))
    if missing or unexpected:raise ValueError('Restoration differs; receipt retained')
    print(json.dumps(receipt))
if __name__=='__main__':main()
