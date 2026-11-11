"""Read-only BN installation inspection; never starts package management or tools."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import sys


def main():
    parser = argparse.ArgumentParser(description='Hermes BN: диагностика текущего профиля без изменения установки.')
    parser.add_argument('--snapshot-dir', required=True)
    parser.add_argument('--version', action='store_true')
    parser.add_argument('command', nargs='?', choices=['plugins', 'status'])
    parser.add_argument('action', nargs='?', choices=['list', 'ls', 'show', 'info'])
    parser.add_argument('name', nargs='?')
    args = parser.parse_args()
    raw = os.environ.get('HERMES_HOME', '').strip()
    if not raw:
        parser.error('HERMES_HOME отсутствует: профиль BN не определён')
    home = str(Path(raw).resolve())
    path = Path(args.snapshot_dir) / (hashlib.sha256(home.encode()).hexdigest() + '.json')
    if not path.is_file():
        parser.error('нет нативного снимка диагностики этого профиля; требуется перезапуск его компонентов BN')
    value = json.loads(path.read_text())
    if value['home'] != home:
        parser.error('снимок относится к другому профилю')
    if args.version:
        result = {'product': 'Hermes BN', 'memory_version': value['memory_version'], 'home': home}
    elif args.command == 'plugins' and args.action in {'show', 'info'}:
        if args.name not in value['plugins']:
            parser.error('расширение отсутствует в текущем профиле: ' + str(args.name))
        result = value['plugins'][args.name]
    elif args.command == 'plugins' and args.action in {'list', 'ls'}:
        result = {'home': home, 'plugins': list(value['plugins'].values())}
    elif args.command == 'status':
        result = value
    else:
        parser.print_help()
        return
    print(json.dumps({'diagnostic_mode': 'read_only', **result}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
