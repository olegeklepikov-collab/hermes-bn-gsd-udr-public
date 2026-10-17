"""Temporary loopback-only, one-use credential input; no keys in chat or logs."""
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs
import json,os,secrets,threading,time
ROOT=Path(__file__).resolve().parents[1]
CSRF=secrets.token_urlsafe(32)
PAGE='''<!doctype html><html lang="ru"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>OpenAlex — Hermes BN</title>
<style>body{font:18px/1.6 system-ui;margin:3rem auto;padding:0 1.5rem;max-width:44rem;color:#1d2532}label{display:block;font-weight:600;margin-top:2rem}input{box-sizing:border-box;width:100%;font:inherit;padding:.7rem;margin:.5rem 0 1rem;border:1px solid #7b8798;border-radius:5px}button{font:inherit;padding:.7rem 1.4rem;background:#174c8d;color:white;border:0;border-radius:5px;cursor:pointer}small{color:#46546a}code{overflow-wrap:anywhere}</style>
<h1>OpenAlex → Hermes BN</h1><p>Вставьте существующий личный ключ OpenAlex. Он будет сохранён только на AgentRuntime2 для запросов Hermes BN к OpenAlex.</p><p><small>Ключ также даёт вход в аккаунт OpenAlex. Не отправляйте его в чат и не создавайте замену: нужен уже имеющийся ключ.</small></p>
<form method="post" action="/save"><input type="hidden" name="csrf" value="CSRF_VALUE"><label for="api-key">Личный ключ OpenAlex</label><input type="password" id="api-key" name="api_key" required autocomplete="off" spellcheck="false" autocapitalize="none" minlength="6" maxlength="512"><button type="submit">Сохранить в Hermes BN</button></form>
<p><small>Файл: <code>__HERMES_BN_ROOT__/OpenAlex/credentials.json</code>. Доступ к нему будет только у владельца учётной записи компьютера. Подписка и пополнение баланса не оформляются.</small></p></html>'''.replace('CSRF_VALUE',CSRF)
class Handler(BaseHTTPRequestHandler):
 def log_message(self,*args):pass
 def reply(self,status,body,cookie=False):
  self.send_response(status);self.send_header('Content-Type','text/html; charset=utf-8');self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.send_header('Content-Security-Policy',"default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'")
  if cookie:self.send_header('Set-Cookie','bn_setup='+CSRF+'; HttpOnly; SameSite=Strict; Path=/')
  self.end_headers();self.wfile.write(body.encode())
 def do_GET(self):
  if self.path!='/':return self.reply(404,'Страница не найдена')
  if (ROOT/'credentials.json').exists():return self.reply(200,'<meta charset="utf-8"><h1>Ключ уже сохранён</h1><p>Можно закрыть вкладку.</p>')
  self.reply(200,PAGE,True)
 def do_POST(self):
  if self.path!='/save':return self.reply(404,'Страница не найдена')
  if (ROOT/'credentials.json').exists():return self.reply(200,'<meta charset="utf-8"><h1>Ключ уже сохранён</h1><p>Можно закрыть вкладку.</p>')
  host=self.headers.get('Host','');origin=self.headers.get('Origin','')
  if host!=f'127.0.0.1:{self.server.server_port}' or origin!=f'http://{host}' or ('bn_setup='+CSRF) not in self.headers.get('Cookie',''):return self.reply(403,'Доступ запрещён')
  length=int(self.headers.get('Content-Length','0'))
  if not 1<=length<=8192:return self.reply(400,'Недопустимый размер формы')
  form=parse_qs(self.rfile.read(length).decode());token=form.get('api_key',[''])[0].strip()
  if form.get('csrf',[''])[0]!=CSRF:return self.reply(403,'Доступ запрещён')
  if not 6<=len(token)<=512 or any(ord(c)<33 or ord(c)>126 for c in token):return self.reply(400,'<meta charset="utf-8">Ключ содержит пробелы или недопустимые символы. Вернитесь и вставьте только ключ.')
  path=ROOT/'credentials.json';fd=os.open(path,os.O_CREAT|os.O_WRONLY|os.O_EXCL,0o600)
  with os.fdopen(fd,'w') as f:json.dump({'api_key':token},f)
  status={'saved':True,'path':str(path),'saved_epoch':time.time()};(ROOT/'config/key-entry-status.json').write_text(json.dumps(status));(ROOT/'config/key-entry-status.json').chmod(0o600)
  self.reply(200,'<meta charset="utf-8"><title>OpenAlex — ключ сохранён</title><h1>Ключ сохранён в Hermes BN</h1><p>Можно закрыть вкладку и сообщить агенту: «Ключ сохранён».</p>')
  threading.Thread(target=self.server.shutdown,daemon=True).start()
server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
status={'url':f'http://127.0.0.1:{server.server_port}/','pid':os.getpid(),'loopback_only':True}
(ROOT/'config/key-entry-flow.json').write_text(json.dumps(status));(ROOT/'config/key-entry-flow.json').chmod(0o600)
print(json.dumps(status),flush=True)
timer=threading.Timer(3600,server.shutdown);timer.daemon=True;timer.start()
try:server.serve_forever()
finally:timer.cancel();server.server_close()
