"""Native owner approval creates an exact, signed grant for an existing artifact."""
import hashlib
import hmac
import json
from pathlib import Path
import re
import sqlite3
import time


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def owners(value):
    text = str(value or '').strip()
    values = json.loads(text) if text.startswith('[') else re.split(r'[,\s]+', text)
    if not isinstance(values, list) or any(not str(v).isdecimal() for v in values):
        raise PermissionError('numeric_owner_allowlist_required')
    return set(map(str, values))


def transport_home(bn_root, profile):
    if profile in {None, '', 'default', 'main'}:
        return bn_root / 'data'
    if not re.fullmatch(r'[a-zA-Z0-9_-]{1,64}', profile):
        raise PermissionError('invalid_delivery_transport_profile')
    return bn_root / 'data/profiles' / profile


def owner_identity(bn_root, home, sid, session_value):
    if session_value('HERMES_SESSION_PLATFORM') != 'telegram' or session_value('HERMES_SESSION_CHAT_TYPE') != 'dm':
        raise PermissionError('live_private_telegram_owner_context_required')
    user, chat = session_value('HERMES_SESSION_USER_ID'), session_value('HERMES_SESSION_CHAT_ID')
    if not user.isdecimal() or user != chat:
        raise PermissionError('private_owner_destination_required')
    with sqlite3.connect('file:' + str(home / 'state.db') + '?mode=ro', uri=True) as connection:
        row = connection.execute('SELECT chat_id,transport_profile,session_key FROM sessions WHERE id=?', (sid,)).fetchone()
    if not row or str(row[0]) != chat or row[2] != session_value('HERMES_SESSION_KEY'):
        raise PermissionError('native_delivery_session_identity_mismatch')
    destination = transport_home(bn_root, row[1]).resolve()
    from dotenv import dotenv_values
    allowed = dotenv_values(destination / '.env').get('TELEGRAM_ALLOWED_USERS', '')
    if user not in owners(allowed):
        raise PermissionError('configured_owner_delivery_required')
    return {'chat_id': int(chat), 'user_id': int(user), 'transport_home': str(destination)}


def authorize_native(host, args, sid):
    from gateway.session_context import get_session_env
    from hermes_constants import get_hermes_home
    from tools.approval import request_tool_approval
    home = get_hermes_home().resolve()
    bn = host.root.parent / 'Hermes BN'
    identity = owner_identity(bn, home, sid, get_session_env)
    if not args.get('artifact_id'):
        raise PermissionError('adopt_file_before_requesting_owner_delivery')
    quote = host.rpc('prepare_delivery', sid, **args)
    reason = ('Передать вам в этот личный Telegram-чат файл «' + quote['filename'] + '», ' +
              str(quote['bytes']) + ' байт, SHA-256 ' + args['expected_sha256'] +
              '. Передаются точные сохранённые байты; выводы исследования этим не принимаются.')
    key = hashlib.sha256(canonical({'sid': sid, **args, **identity})).hexdigest()
    approval = request_tool_approval('bn_deliver_report', reason, rule_key='bn-owner-file:' + key)
    if approval.get('approved') is not True:
        return {'status': 'delivery_not_approved', 'message': approval.get('message', 'Ожидается разрешение владельца.'),
                'file_sent': False}
    body = {'sid': sid, **args, **identity, 'expires_at': time.time() + 90,
            'authorization_source': 'owner-authorized:native-Hermes-tool-approval:' + key}
    secret = host.key.read_bytes()
    envelope = {'body': body, 'mac': hmac.new(secret, canonical(body), hashlib.sha256).hexdigest()}
    issued = host.rpc('authorize_delivery', sid, approval=envelope)
    return {'status': 'delivery_authorized', 'grant_id': issued['grant_id']}


def prepare(sid, run_id, artifact_id, expected_sha256):
    from prepared_file import registered
    _, _, item, raw = registered(sid, run_id, artifact_id, expected_sha256)
    return {'filename': item['filename'], 'bytes': len(raw), 'sha256': expected_sha256,
            'artifact_id': artifact_id, 'delivery_authorized': False}


def issue(sid, approval):
    import backend as backend
    body = approval['body']
    key = (backend.ROOT / 'state/authority/bn-bridge.key').read_bytes()
    expected = hmac.new(key, canonical(body), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(approval['mac'], expected):
        raise PermissionError('native_delivery_approval_authentication_failed')
    if body['sid'] != sid or not time.time() < body['expires_at'] <= time.time() + 95:
        raise PermissionError('native_delivery_approval_identity_or_expiry_mismatch')
    if body['user_id'] != body['chat_id'] or not body['authorization_source'].startswith('owner-authorized:native-Hermes-tool-approval:'):
        raise PermissionError('native_owner_delivery_approval_required')
    bn = backend.ROOT.parent / 'Hermes BN'
    home = Path(body['transport_home']).resolve()
    homes = [bn / 'data', *[p for p in (bn / 'data/profiles').iterdir() if p.is_dir()]]
    if home not in [p.resolve() for p in homes]:
        raise PermissionError('configured_delivery_transport_required')
    from dotenv import dotenv_values
    env = dotenv_values(home / '.env')
    if str(body['user_id']) not in owners(env.get('TELEGRAM_ALLOWED_USERS', '')):
        raise PermissionError('configured_owner_delivery_required')
    quote = prepare(sid, body['run_id'], body['artifact_id'], body['expected_sha256'])
    import asyncio
    from telegram import Bot
    token = env.get('TELEGRAM_BOT_TOKEN') or env.get('HERMES_TELEGRAM_BOT_TOKEN')
    if not token:
        raise PermissionError('bot_credential_unavailable')
    async def identity():
        async with Bot(token) as bot:
            return (await bot.get_me()).username
    bot_name = asyncio.run(identity())
    grant = {'sid': sid, 'run_id': body['run_id'], 'sha256': body['expected_sha256'],
             'artifact_id': body['artifact_id'], 'filename': quote['filename'], 'chat_id': body['chat_id'],
             'bot_name': bot_name, 'transport_home': str(home), 'expires_at': time.time() + 300,
             'authorization_source': body['authorization_source']}
    grant_id = hashlib.sha256(canonical({k: v for k, v in grant.items() if k != 'expires_at'})).hexdigest()[:32]
    folder = backend.HERE / 'owner-grants'
    folder.mkdir(mode=0o700, exist_ok=True)
    from report_delivery import write_receipt
    write_receipt(folder / (grant_id + '.json'), {'body': grant, 'mac': hmac.new(key, canonical(grant), hashlib.sha256).hexdigest()})
    return {'grant_id': grant_id, 'filename': grant['filename'], 'sha256': grant['sha256']}
