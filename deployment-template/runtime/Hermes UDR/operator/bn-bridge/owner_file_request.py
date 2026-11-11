"""Read an owner's original file-output request from native session history."""
from datetime import datetime
from pathlib import Path
import hashlib
import re
import sqlite3


def requested_markdown(text):
    text = re.sub(r'```.*?```|<untrusted_tool_result\b.*?</untrusted_tool_result>', '', text, flags=re.S)
    lines = [line for line in text.splitlines() if not line.lstrip().startswith('>')]
    clean = '\n'.join(lines)
    if re.search(r'(?im)^\s*(?:не\s+(?:отправляй|присылай|передавай|доставляй)|отменяю\s+(?:отправку|передачу)|не\s+(?:разрешаю|подтверждаю))\b', clean):
        return 'denied'
    for line in lines:
        if re.search(r'(?i)^\s*(?:форма|формат)\s*:', line) and re.search(r'(?i)(?:\bmd\b|\.md\b|markdown)', line):
            return 'requested'
        if re.search(r'(?i)^\s*(?:пришли|отправь|предоставь|выдай|передай|доставь)\b', line) and re.search(r'(?i)файл|отч[её]т|документ|markdown|\.md\b', line):
            return 'requested'
    return None


def from_history(home, request_sid, identity, created_at, filename, current_sid=None):
    if Path(filename).suffix.lower() != '.md':
        return None
    started = datetime.fromisoformat(created_at).timestamp()
    database = Path(home) / 'state.db'
    with sqlite3.connect(database.as_uri() + '?mode=ro', uri=True) as db:
        session = db.execute('SELECT source,user_id,chat_id,chat_type FROM sessions WHERE id=?', (request_sid,)).fetchone()
        if not session or session[0] != 'telegram' or session[3] != 'dm' or str(session[1]) != str(identity['user_id']) or str(session[2]) != str(identity['chat_id']):
            return None
        anchor = db.execute("SELECT id,timestamp FROM messages WHERE session_id=? AND role='user' AND timestamp<=? ORDER BY timestamp DESC,id DESC LIMIT 1", (request_sid, started)).fetchone()
        if anchor is None:
            return None
        rows = list(db.execute("SELECT id,content,timestamp,session_id FROM messages WHERE session_id=? AND role='user' AND timestamp>=? ORDER BY timestamp,id", (request_sid, anchor[1])))
        if current_sid and current_sid != request_sid:
            rows.extend(db.execute("SELECT id,content,timestamp,session_id FROM messages WHERE session_id=? AND role='user' ORDER BY timestamp,id", (current_sid,)))
    proof = None
    for message_id, content, timestamp, message_sid in rows:
        if not isinstance(content, str):
            continue
        decision = requested_markdown(content)
        if decision == 'denied':
            proof = None
        elif decision == 'requested':
            proof = {'kind': 'native_owner_file_request', 'request_session_id': message_sid,
                     'message_id': message_id, 'message_sha256': hashlib.sha256(content.encode()).hexdigest(),
                     'created_at': created_at, 'format': 'md'}
    return proof
