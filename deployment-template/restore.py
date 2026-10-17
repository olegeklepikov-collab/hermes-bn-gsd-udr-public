#!/usr/bin/env python3
"""Fetch and reconstruct BOTH immutable archives of a complete recovery set."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess
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
    if a.download and not shutil.which('gh'):raise ValueError('Установите GitHub CLI и войдите своим аккаунтом с доступом')
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
            if not path.exists() and a.download:subprocess.run(['gh','release','download',item['tag'],'--repo',item['repository'],'--pattern',part['name'],'--dir',str(folder)],check=True)
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
    print('Полный комплект собран: основа + обновление. Следуйте CURRENT-SETUP.md; службы автоматически не запускаются.')
if __name__=='__main__':main()
