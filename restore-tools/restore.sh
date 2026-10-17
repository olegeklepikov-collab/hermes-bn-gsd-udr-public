#!/bin/bash
set -euo pipefail
umask 077
tool_root=$(cd "$(dirname "$0")" && pwd)
if [[ $(uname -s) != Darwin || $(uname -m) != arm64 ]]; then
  printf 'Эти средства предназначены для macOS arm64. На другой платформе установите age, zstd и libarchive для неё.\n' >&2
  exit 2
fi
if [[ $# -ne 2 && $# -ne 3 ]]; then
  printf 'Обезличенная копия: restore.sh АРХИВ.tar.zst НОВЫЙ_КАТАЛОГ\nПолная копия: restore.sh АРХИВ.tar.zst.age НОВЫЙ_КАТАЛОГ ФАЙЛ_КЛЮЧА.agekey\n' >&2
  exit 2
fi
archive=$1
destination=$2
[[ -f "$archive" ]] || { printf 'Архив не найден.\n' >&2; exit 2; }
[[ ! -e "$destination" ]] || { printf 'Каталог назначения уже существует. Выберите новый.\n' >&2; exit 2; }
mkdir -m 700 -p "$destination"
if [[ "$archive" == *.age ]]; then
  [[ $# -eq 3 && -f "$3" ]] || { printf 'Нужен отдельный файл ключа.\n' >&2; exit 2; }
  "$tool_root/age" -d -i "$3" "$archive" | "$tool_root/zstd" -d -q -c | /usr/bin/bsdtar --no-same-owner -xpf - -C "$destination"
else
  "$tool_root/zstd" -d -q -c "$archive" | /usr/bin/bsdtar --no-same-owner -xpf - -C "$destination"
fi
printf 'Распаковано в отдельный каталог. Сначала выполните verify.py и прочитайте README.md. Программы и службы не запускались.\n'
