#!/usr/bin/env python3
"""Public edition 2026-10-17: unauthenticated HTTPS download; immutable payload hashes retained."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,re
from urllib.parse import quote
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        while True:
            b=f.read(8*1024*1024)
            if not b:break
            h.update(b)
    return h.hexdigest()
def main():
    p=argparse.ArgumentParser(description='Собрать полный комплект: неизменная основа и проверенное обновление.')
    p.add_argument('--manifest',type=Path,default=Path(__file__).with_name('recovery-set.json'));p.add_argument('--parts-dir',type=Path,default=Path('parts'));p.add_argument('--output-dir',type=Path,default=Path('recovery-archives'));p.add_argument('--download',action='store_true');a=p.parse_args()
    m=json.loads(a.manifest.read_text())
    if m['format']!='hermes-bn-recovery-set/2' or [x['role'] for x in m['archives']]!=['base','update']:raise ValueError('Нужен согласованный комплект основы и обновления')
    if a.download and not shutil.which('curl'):raise ValueError('Требуется curl; в macOS он находится в /usr/bin/curl')
    a.output_dir.mkdir(parents=True,exist_ok=True)
    for item in m['archives']:
        archive=item['archive'];target=a.output_dir/archive['name'];folder=a.parts_dir/item['role'];folder.mkdir(parents=True,exist_ok=True)
        if Path(archive['name']).name!=archive['name']:raise ValueError('Неверное имя архива')
        if target.exists():
            if target.stat().st_size==archive['bytes'] and sha(target)==archive['sha256']:print('Уже проверен:',target.name);continue
            raise ValueError('Существующий файл не совпал; перезапись запрещена')
        total=0
        for i,part in enumerate(item['parts'],1):
            if part['index']!=i or part['offset']!=total or Path(part['name']).name!=part['name']:raise ValueError('Неверный порядок частей')
            total+=part['bytes'];path=folder/part['name']
            if not path.exists() and a.download:
                if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',item['repository']):raise ValueError('Неверный адрес репозитория')
                url='https://github.com/'+item['repository']+'/releases/download/'+quote(item['tag'],safe='')+'/'+quote(part['name'],safe='')
                pending=path.with_name(path.name+'.download-partial')
                if pending.exists():raise ValueError('Есть незавершённая загрузка: '+str(pending))
                print('Загрузка без авторизации: '+part['name'],flush=True)
                try:
                    subprocess.run(['curl','--fail','--location','--silent','--show-error','--retry','3','--proto','=https','--output',str(pending),url],check=True)
                    if pending.stat().st_size!=part['bytes'] or sha(pending)!=part['sha256']:raise ValueError('Загруженная часть не совпала с манифестом')
                    pending.rename(path)
                except BaseException:
                    if pending.exists():pending.unlink()
                    raise
            if not path.is_file() or path.stat().st_size!=part['bytes'] or sha(path)!=part['sha256']:raise ValueError('Отсутствует или повреждена часть: '+part['name'])
            print(item['role']+': проверена часть '+str(i)+'/'+str(len(item['parts'])),flush=True)
        if total!=archive['bytes']:raise ValueError('Размер комплекта частей неверен')
        temporary=target.with_name(target.name+'.partial')
        if temporary.exists():raise ValueError('Есть прежний незавершённый файл; выберите новую папку результата')
        with temporary.open('xb') as f:
            for part in item['parts']:
                with (folder/part['name']).open('rb') as src:shutil.copyfileobj(src,f,8*1024*1024)
            f.flush();os.fsync(f.fileno())
        if sha(temporary)!=archive['sha256']:raise ValueError('Итоговый SHA256 не совпал')
        temporary.rename(target);print('Архив проверен:',target.name)
    print('Полный комплект собран: основа + обновление. Следуйте INSTALL-macOS-Apple-Silicon.md; службы автоматически не запускаются.')
if __name__=='__main__':main()
