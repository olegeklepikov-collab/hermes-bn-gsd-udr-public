"""Native owner source requests grant task-scoped reading, never source writes."""
from pathlib import Path
import hashlib
import json
import re
import sqlite3
import time

PRIVATE = {'.env', '.ssh', '.aws', '.gnupg', 'auth.json', 'credentials.json',
           'mcp-tokens', 'mcp-tokens.json', 'authority', '.git', 'node_modules'}
READ_REQUEST = re.compile(r'(?i)исслед|анализ|проч[иь]|читать|чтени|изуч|провер|посмотр|обработ|разбер|откр|read|analy[sz]|inspect|audit|review|open')
QUOTED_PATH = re.compile(r"[\"'`«“](/[^\"'`»”\r\n]+)[\"'`»”]")
BARE_PATH = re.compile(r'(?m)(?:^|\s)(/(?:Users|Volumes|home|tmp|private)/[^\s<>"\x27`]+)')


def enabled(config):
    return config.get('source_access', {}).get('enabled', False) is True


def resolve_path(raw, config):
    path = Path(raw).expanduser()
    if '..' in path.parts:
        raise PermissionError('source_parent_traversal_denied')
    aliases = config.get('source_access', {}).get('path_aliases', {})
    if path.is_absolute() and not path.exists():
        for old, new in sorted(aliases.items(), key=lambda x: len(x[0]), reverse=True):
            if path.is_relative_to(Path(old)):
                mapped = Path(new) / path.relative_to(Path(old))
                if mapped.exists():
                    return mapped
    return path


def checked_source(raw, config):
    path = resolve_path(raw, config)
    if not path.is_absolute():
        raise ValueError('absolute_source_path_required')
    if any(part.lower() in PRIVATE or part.lower().startswith('.env') for part in path.parts):
        raise PermissionError('private_source_path_denied')
    if path.suffix.lower() in {'.key', '.pem', '.p12', '.pfx'}:
        raise PermissionError('private_source_path_denied')
    for part in [path, *path.parents]:
        if part.is_symlink():
            raise PermissionError('symlink_source_denied')
    if not path.exists():
        raise FileNotFoundError('source_path_not_found:' + str(path))
    if not (path.is_dir() or path.is_file()):
        raise ValueError('regular_source_required')
    return path.resolve()


def requested_paths(message):
    if isinstance(message, list):
        message = '\n'.join(item.get('text', '') for item in message
                            if isinstance(item, dict) and item.get('type') in {'text', 'input_text'})
    if not isinstance(message, str) or not READ_REQUEST.search(message):
        return []
    # Fenced documents and labelled tool results are data, not an owner path request.
    text = re.sub(r'```.*?```|<untrusted_tool_result\b.*?</untrusted_tool_result>', '', message, flags=re.S)
    if re.search(r'(?i)\bне\s+(?:читай|читать|открывай|исследуй|анализируй)', text):
        return []
    quoted = QUOTED_PATH.findall(text)
    without_quotes = QUOTED_PATH.sub('', text)
    return list(dict.fromkeys([*quoted, *(p.rstrip('.,;:!?)]}') for p in BARE_PATH.findall(without_quotes))]))


def ensure_schema(store):
    if not enabled(store.config):
        return
    with store.db() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS source_read_grants(
            id TEXT PRIMARY KEY, task TEXT NOT NULL, root TEXT NOT NULL, requested_path TEXT NOT NULL,
            sid TEXT NOT NULL, actor TEXT NOT NULL, turn_id TEXT NOT NULL, origin TEXT NOT NULL,
            created REAL NOT NULL, UNIQUE(task,root))''')


def native_owner(config, sid, platform, sender_id):
    for database in config.get('native_session_databases', []):
        path = Path(database)
        if not path.is_file():
            continue
        with sqlite3.connect(path.as_uri() + '?mode=ro', uri=True) as db:
            row = db.execute('SELECT source,user_id,chat_id,chat_type FROM sessions WHERE id=?', (sid,)).fetchone()
        if row is None:
            continue
        if platform == 'telegram' and row[0] == platform and row[3] == 'dm':
            owners = set(map(str, config.get('source_access', {}).get('telegram_owner_ids', [])))
            if str(sender_id) in owners and str(row[1]) == str(sender_id) == str(row[2]):
                return 'telegram:' + str(sender_id)
        if platform == 'cli' and row[0] == 'cli' and config.get('source_access', {}).get('local_cli_owner', False):
            return 'native-local-cli'
        return None
    return None


def grant(store, sid, requested_path, actor, turn_id, origin='native-owner-request'):
    binding = store.writable(sid)
    path = checked_source(requested_path, store.config)
    # This function is native-only; no schema, model tool, or MCP operation exposes it.
    identity = hashlib.sha256((binding['task'] + '\0' + str(path)).encode()).hexdigest()
    with store.db() as db:
        db.execute('INSERT OR IGNORE INTO source_read_grants VALUES(?,?,?,?,?,?,?,?,?)',
                   (identity, binding['task'], str(path), requested_path, sid, actor, turn_id, origin, time.time()))
    return {'path': str(path), 'requested_path': requested_path, 'access': 'read', 'scope': 'current_task',
            'authorization': 'native_owner_request', 'grant_id': identity}


def authorize_turn(store, sid, message, platform, sender_id, turn_id):
    if not enabled(store.config) or store.binding(sid)['readonly']:
        return []
    actor = native_owner(store.config, sid, platform, sender_id)
    if not actor:
        return []
    results = []
    for raw in requested_paths(message):
        try:
            results.append(grant(store, sid, raw, actor, turn_id))
        except (ValueError, PermissionError, FileNotFoundError) as exc:
            results.append({'requested_path': raw, 'status': 'unavailable', 'reason': str(exc)})
    return results


def grants(store, sid):
    if not enabled(store.config):
        return []
    binding = store.binding(sid)
    if binding['readonly']:
        return []
    with store.db() as db:
        exists = db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='source_read_grants'").fetchone()
        if not exists:
            return []
        rows = db.execute('SELECT root,requested_path,origin FROM source_read_grants WHERE task=? ORDER BY root',
                          (binding['task'],)).fetchall()
    return [{'path': r[0], 'requested_path': r[1], 'access': 'read', 'origin': r[2]} for r in rows]


def source_roots(config, sid):
    """Read the same grant journal in the native GSD parent without opening it to the terminal."""
    if not enabled(config) or not sid:
        return []
    path = Path(config['state_root']) / 'memory.sqlite'
    with sqlite3.connect(path.as_uri() + '?mode=ro', uri=True) as db:
        binding = db.execute('SELECT task,readonly FROM sessions WHERE sid=?', (sid,)).fetchone()
        if not binding or binding[1]:
            return []
        if not db.execute("SELECT 1 FROM sqlite_master WHERE name='source_read_grants' AND type='table'").fetchone():
            return []
        roots=[]
        for row in db.execute('SELECT root FROM source_read_grants WHERE task=?', (binding[0],)):
            try:roots.append(checked_source(row[0],config))
            except (PermissionError,FileNotFoundError,ValueError):continue
        return roots


def diagnostic_snapshot(config):
    """Publish only non-secret installation facts for the isolated read-only CLI."""
    if not enabled(config):
        return
    from hermes_constants import get_hermes_home
    from hermes_cli.config import load_config_readonly
    home = get_hermes_home().resolve()
    value = load_config_readonly()
    entries = value.get('plugins', {}).get('entries', {})
    plugins = {name: {'name': name, 'enabled': entry.get('enabled', True)} for name, entry in entries.items()}
    snapshot = {'home': str(home), 'mode': 'read_only_diagnostics', 'plugins': plugins,
                'memory_version': '1.4.1', 'generated_at': time.time()}
    root = Path(config['source_access']['diagnostic_snapshots'])
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    destination = root / (hashlib.sha256(str(home).encode()).hexdigest() + '.json')
    temporary = destination.with_suffix('.tmp')
    temporary.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n')
    temporary.chmod(0o600)
    temporary.replace(destination)
