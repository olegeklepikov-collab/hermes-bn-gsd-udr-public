import getpass,json,re,os
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"credentials.env"
key=getpass.getpass("Ключ API Semantic Scholar (ввод скрыт): ").strip()
if not key or re.search(r"[\s\x00-\x1f\x7f]",key):raise SystemExit("Нужен непустой ключ без пробелов и управляющих символов.")
fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_TRUNC,0o600)
os.fchmod(fd,0o600)
with os.fdopen(fd,"w") as f:f.write("SEMANTIC_SCHOLAR_API_KEY="+json.dumps(key)+"\n")
p.chmod(0o600)
print("Ключ сохранён для Hermes BN. Значение не выводится.")
