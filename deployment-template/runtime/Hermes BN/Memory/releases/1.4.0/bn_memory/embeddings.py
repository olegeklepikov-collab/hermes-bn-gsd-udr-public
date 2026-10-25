"""One cache-aware Voyage batch path; accounting is independent of source authority."""
import fcntl
import json
import math
import time
from pathlib import Path
from bn_memory.store import canonical,sha,SENSITIVE
from bn_memory.workers import http

class Embeddings:
    def __init__(self,store,config,request=http):self.store=store;self.config=config;self.request=request

    @staticmethod
    def vector(value):
        if not isinstance(value,list) or len(value)!=1024 or any(type(x) not in (float,int) or not math.isfinite(x) for x in value):
            raise ValueError('embedding_vector_invalid')
        if not any(value):raise ValueError('embedding_zero_vector')
        return value

    def many(self,texts,purpose):
        if purpose not in {'query','document'} or not isinstance(texts,list) or not texts:raise ValueError('embedding_input_invalid')
        if any(not isinstance(t,str) or not t or SENSITIVE.search(t) for t in texts):raise ValueError('secret_or_empty_not_embedding')
        keys={sha(purpose+':'+t):t for t in texts};vectors={};hits=0
        with self.store.db() as db:
            db.execute('CREATE TABLE IF NOT EXISTS embedding_usage(at REAL,purpose TEXT,requests INTEGER,texts INTEGER,cache_hits INTEGER,tokens INTEGER,bytes INTEGER,seconds REAL,status TEXT)')
        with (Path(self.config['state_root'])/'embedding.lock').open('a') as lock:
            # Query latency must not depend on a background document batch.
            if purpose=='document':fcntl.flock(lock,fcntl.LOCK_EX)
            with self.store.db() as db:
                for k in keys:
                    row=db.execute("SELECT vector FROM vectors WHERE id=? AND model='voyage-4-large'",('VECTOR-'+k,)).fetchone()
                    if row:vectors[k]=self.vector(json.loads(row[0]));hits+=1
            missing=[k for k in keys if k not in vectors];batches=[];batch=[];size=0
            for k in missing:
                amount=len(keys[k].encode())+256
                if batch and (len(batch)>=32 or size+amount>96000):batches.append(batch);batch=[];size=0
                batch.append(k);size+=amount
            if batch:batches.append(batch)
            for batch in batches:
                amount=sum(len(keys[k].encode())+256 for k in batch);day=time.strftime('%Y-%m-%d',time.gmtime())
                with self.store.db() as db:
                    db.execute('BEGIN IMMEDIATE');row=db.execute('SELECT bytes FROM budget WHERE day=?',(day,)).fetchone()
                    cap=self.config.get('embedding_daily_bytes')
                    if cap is not None and (row[0] if row else 0)+amount>cap:raise RuntimeError('embedding_daily_budget_exhausted')
                    db.execute('INSERT INTO budget VALUES(?,?) ON CONFLICT(day) DO UPDATE SET bytes=bytes+excluded.bytes',(day,amount))
                started=time.monotonic()
                try:
                    result=self.request(self.config['embedding_url'],{'model':'voyage-4-large','input':[keys[k] for k in batch],
                        'output_dimension':1024,'output_dtype':'float','input_type':purpose,'truncation':False},self.config['voyage_key_file'],timeout=12)
                    data=result['data'];indexed={v['index']:self.vector(v['embedding']) for v in data}
                    if set(indexed)!=set(range(len(batch))) or len(data)!=len(batch):raise ValueError('embedding_batch_mismatch')
                    with self.store.db() as db:
                        for i,k in enumerate(batch):
                            vectors[k]=indexed[i];db.execute("INSERT OR IGNORE INTO vectors VALUES(?,1,'voyage-4-large',?)",('VECTOR-'+k,canonical(vectors[k])))
                        db.execute('INSERT INTO embedding_usage VALUES(?,?,?,?,?,?,?,?,?)',(time.time(),purpose,1,len(batch),0,result.get('usage',{}).get('total_tokens'),amount,time.monotonic()-started,'complete'))
                except Exception:
                    with self.store.db() as db:db.execute('INSERT INTO embedding_usage VALUES(?,?,?,?,?,?,?,?,?)',(time.time(),purpose,1,len(batch),0,None,amount,time.monotonic()-started,'failed'))
                    raise
            if hits:
                with self.store.db() as db:db.execute('INSERT INTO embedding_usage VALUES(?,?,?,?,?,?,?,?,?)',(time.time(),purpose,0,len(keys),hits,0,0,0,'cache'))
        return [vectors[sha(purpose+':'+t)] for t in texts]
