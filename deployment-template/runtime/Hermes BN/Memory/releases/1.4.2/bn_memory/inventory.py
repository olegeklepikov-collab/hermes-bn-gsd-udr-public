"""Durable finite inventory steps; a large folder is never silently truncated."""
from pathlib import Path
import os
import time


def prepare(store, cid, target):
    with store.db() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS document_inventory(
            corpus TEXT NOT NULL,path TEXT NOT NULL,state TEXT NOT NULL,
            PRIMARY KEY(corpus,path))''')
        db.execute('CREATE INDEX IF NOT EXISTS document_inventory_pending ON document_inventory(corpus,state,path)')
        db.execute('INSERT OR IGNORE INTO document_inventory VALUES(?,?,?)', (cid, str(target), 'pending'))


def page(store, cid, maximum=256, seconds=30):
    deadline = time.monotonic() + seconds
    paths, errors = [], []
    while len(paths) < maximum and time.monotonic() < deadline:
        with store.db() as db:
            rows = db.execute("SELECT path FROM document_inventory WHERE corpus=? AND state='pending' ORDER BY path LIMIT ?",
                              (cid, maximum)).fetchall()
        candidates = [Path(row[0]) for row in rows if Path(row[0]) not in paths]
        if not candidates:
            break
        for path in candidates:
            if len(paths) >= maximum or time.monotonic() >= deadline:
                break
            if path.is_dir() and not path.is_symlink():
                try:
                    with os.scandir(path) as entries:
                        children = [(cid, entry.path, 'pending') for entry in entries]
                    with store.db() as db:
                        db.executemany('INSERT OR IGNORE INTO document_inventory VALUES(?,?,?)', children)
                        db.execute("UPDATE document_inventory SET state='enumerated' WHERE corpus=? AND path=?", (cid, str(path)))
                except OSError as exc:
                    errors.append(exc)
                    with store.db() as db:
                        db.execute("UPDATE document_inventory SET state='failed' WHERE corpus=? AND path=?", (cid, str(path)))
            else:
                paths.append(path)
    return paths, errors


def done(store, cid, path):
    with store.db() as db:
        db.execute("UPDATE document_inventory SET state='done' WHERE corpus=? AND path=?", (cid, str(path)))


def remaining(store, cid):
    with store.db() as db:
        return db.execute("SELECT count(*) FROM document_inventory WHERE corpus=? AND state='pending'", (cid,)).fetchone()[0]
