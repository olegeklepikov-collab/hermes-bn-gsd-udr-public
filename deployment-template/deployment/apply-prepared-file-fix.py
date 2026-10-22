#!/usr/bin/env python3
"""Qualified offline update of the UDR host, preserving account and research state."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import tempfile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe(path, root):
    if not path.is_relative_to(root):
        raise ValueError('Destination outside the selected root')
    current = path
    while current != root.parent:
        if current.is_symlink():
            raise ValueError('Symlink destination refused: '+str(current))
        current = current.parent


def atomic(path, data, mode):
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix='.prepared-file-fix-', dir=path.parent)
    try:
        with os.fdopen(descriptor, 'wb') as stream:
            os.fchmod(stream.fileno(), mode)
            stream.write(data);stream.flush();os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def main():
    parser=argparse.ArgumentParser(description='UDR 0.3.1: проверка, установка и откат без замены пользовательских состояний')
    parser.add_argument('--bn-root',type=Path,required=True)
    parser.add_argument('--udr-root',type=Path,required=True)
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--check',action='store_true')
    mode.add_argument('--rollback',action='store_true')
    args=parser.parse_args();bn=args.bn_root.resolve(strict=True);udr=args.udr_root.resolve(strict=True)
    if bn.parent!=udr.parent or bn.name!='Hermes BN' or udr.name!='Hermes UDR':
        raise ValueError('Qualified sibling Hermes BN / Hermes UDR layout required')
    backup=bn/'operator/prepared-files-0.3.1/rollback'
    safe(backup,bn)
    if not args.check:
        for home in [bn/'data',*(bn/'data/profiles').glob('*')]:
            if (home/'gateway.pid').exists():
                raise ValueError('Stop the owning gateway first; gateway.pid is present')
    if args.rollback:
        journal=json.loads((backup/'journal.json').read_text())
        for row in journal:
            path=Path(row['path']);safe(path,bn if path.is_relative_to(bn) else udr)
            if not path.is_file() or sha(path.read_bytes())!=row['after_sha256']:
                raise ValueError('A later change prevents automatic rollback: '+str(path))
            if row['existed'] and sha((backup/row['backup']).read_bytes())!=row['before_sha256']:
                raise ValueError('Damaged rollback copy')
        for row in reversed(journal):
            path=Path(row['path'])
            if row['existed']:atomic(path,(backup/row['backup']).read_bytes(),row['mode'])
            else:path.unlink()
        print('Previous host code and exact admissions restored; states and receipts retained')
        return
    source=Path(__file__).with_name('prepared-files')
    qualified=json.loads((source/'qualification.json').read_text());bridge=udr/'operator/bn-bridge';changes={}
    for name,expected in qualified['after'].items():
        raw=(source/'bridge'/name).read_bytes()
        if sha(raw)!=expected:raise ValueError('Damaged update source: '+name)
        path=bridge/name;safe(path,udr)
        before=sha(path.read_bytes()) if path.exists() else None
        if before not in {qualified['before'].get(name),expected}:
            raise ValueError('Unqualified host source: '+name)
        changes[path]=raw
    for folder in [bn/'data/plugins/bn-udr-host',bn/'data/profiles/bn-udr-only/plugins/bn-udr-host']:
        if not folder.exists():continue
        for name in ('__init__.py','plugin.yaml'):
            path=folder/name;safe(path,bn);key='plugin/'+name
            allowed=set(qualified.get('before_native_plugin',{}).get(name,[qualified['before'][key]]))|{qualified['after'][key]}
            if sha(path.read_bytes()) not in allowed:
                raise ValueError('Unqualified native plugin copy: '+str(path))
            changes[path]=changes[bridge/key]
    skill=bn/'data/skills/bn-udr-host-work/SKILL.md';safe(skill,bn)
    text=skill.read_text();addition=(source/'skill-addendum.md').read_text()
    changes[skill]=(text if addition.strip() in text else text.rstrip()+addition).encode()
    manifest=bridge/'source-manifest.json';safe(manifest,udr);mapping=json.loads(manifest.read_text())
    for name,expected in mapping.items():
        path=bridge/name
        if sha(path.read_bytes())!=expected:raise ValueError('Existing source admission is invalid: '+name)
    mapping.setdefault('prepared_file.py','')
    mapping.setdefault(os.path.relpath(skill,bridge),'')
    changes[manifest]=(json.dumps({name:sha(changes.get((bridge/name).resolve(),(bridge/name).read_bytes() if (bridge/name).exists() else b'')) for name in mapping},ensure_ascii=False,indent=2)+'\n').encode()
    settings=bn/'GSD/operator/settings.json'
    if settings.exists():
        safe(settings,bn);value=json.loads(settings.read_text());admissions=value['local_adapter_sha256']
        for name,expected in admissions.items():
            if sha(Path(name).read_bytes())!=expected:raise ValueError('Existing GSD admission is invalid: '+name)
        for path,raw in changes.items():
            if str(path) in admissions or path in {manifest,bridge/'prepared_file.py',skill}:
                admissions[str(path)]=sha(raw)
        changes[settings]=(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
    pending={path:raw for path,raw in changes.items() if not path.exists() or path.read_bytes()!=raw}
    if args.check:
        print(json.dumps({'compatible':True,'installed':not pending,'changed_files':len(pending),'authority_imported':False}))
        return
    if not pending:
        print('UDR 0.3.1 already installed and admitted; no changes')
        return
    backup.mkdir(parents=True,mode=0o700,exist_ok=False);rows=[]
    for index,(path,raw) in enumerate(pending.items()):
        existed=path.exists();old=path.read_bytes() if existed else b'';name=f'{index:03d}.bin'
        if existed:atomic(backup/name,old,0o600)
        rows.append({'path':str(path),'existed':existed,'backup':name,'before_sha256':sha(old),
            'after_sha256':sha(raw),'mode':(path.stat().st_mode&0o777) if existed else 0o644})
    atomic(backup/'journal.json',json.dumps(rows,indent=2).encode(),0o600)
    try:
        for row in rows:atomic(Path(row['path']),pending[Path(row['path'])],row['mode'])
    except BaseException:
        for row in reversed(rows):
            path=Path(row['path'])
            if row['existed']:atomic(path,(backup/row['backup']).read_bytes(),row['mode'])
            else:path.unlink(missing_ok=True)
        raise
    print('UDR host 0.3.1 installed; exact admissions updated; states and limits preserved; gateway not started')


if __name__=='__main__':main()
