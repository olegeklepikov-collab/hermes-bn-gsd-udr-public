"""Bounded native startup dependencies, then the repository's unchanged service launcher."""
import json
import socket
import sys
import time
import subprocess
import signal
import os
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import urlopen

spec_path=Path(sys.argv[1]).resolve(strict=True)
spec=json.loads(spec_path.read_text())
deadline=time.monotonic()+45
for dep in spec.get('dependencies',[]):
    while True:
        try:
            if dep['kind']=='tcp':
                if dep['host']!='127.0.0.1':raise ValueError('local_dependency_required')
                with socket.create_connection((dep['host'],int(dep['port'])),timeout=1):pass
            else:
                url=dep['url'];parsed=urlsplit(url)
                if parsed.scheme!='http' or parsed.hostname!='127.0.0.1':raise ValueError('local_dependency_required')
                with urlopen(url,timeout=2) as response:
                    if dep.get('json_status'):
                        if json.load(response).get('status')!=dep['json_status']:raise OSError('not_ready')
            break
        except (OSError,TimeoutError):
            if time.monotonic()>=deadline:raise SystemExit('Required native dependency not ready within 45s')
            time.sleep(0.2)
env=os.environ.copy()
if spec.get('env_file'):
    from dotenv import dotenv_values
    env.update({k:v for k,v in dotenv_values(spec['env_file']).items() if v is not None})
env.update(spec.get('env',{}))
process=subprocess.Popen(spec['argv'],cwd=spec['cwd'],env=env,start_new_session=True)
stopping=False
stop_at=None
def stop(_signum,_frame):
    global stopping,stop_at
    if stopping:return
    stopping=True
    stop_at=time.monotonic()
    try:os.killpg(process.pid,signal.SIGTERM)
    except ProcessLookupError:return
signal.signal(signal.SIGTERM,stop)
signal.signal(signal.SIGINT,stop)
while process.poll() is None:
    if stopping and time.monotonic()-stop_at>=20:
        os.killpg(process.pid,signal.SIGKILL)
        break
    time.sleep(0.1)
raise SystemExit(process.wait())
