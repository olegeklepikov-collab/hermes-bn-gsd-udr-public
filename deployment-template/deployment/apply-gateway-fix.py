#!/usr/bin/env python3
"""Apply the qualified Hermes 0.22.2 command fix without replacing user state."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile

BEFORE = "f399c90076668e8745e19b640fdcd9a467bd07cc1217a33b38aca00cd38191c1"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic(path, data):
    mode = path.stat().st_mode & 0o777
    descriptor, name = tempfile.mkstemp(prefix=".gateway-fix-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(name, mode)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main():
    parser = argparse.ArgumentParser(description="Исправление команд Hermes 0.22.2; состояния и доступы сохраняются")
    parser.add_argument("--bn-root", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--rollback", action="store_true")
    args = parser.parse_args()
    root = args.bn_root.resolve(strict=True)
    target = root / "hermes-agent/gateway/run_inbound.py"
    manifest = root / "GSD/releases/0.2.13-hermes-0.22.2-r3/release/core-manifest.json"
    settings_paths = [path for path in (root / "GSD/operator/settings.json",
        root / "data/profiles/bn-gsd-only/settings.json") if path.is_file()]
    source = Path(__file__).with_name("gateway-fix") / "run_inbound.py"
    qualification = json.loads(source.with_name("qualification.json").read_text())
    after = qualification["gateway_file_sha256"]
    if sha(source) != after:
        raise ValueError("Повреждён источник исправления")
    if any(path.is_symlink() for path in (target, manifest)):
        raise ValueError("Файлы назначения должны быть обычными файлами")
    current = sha(target)
    if current not in (BEFORE, after):
        raise ValueError("Неизвестная редакция Hermes: автоматическая перезапись запрещена")
    data = json.loads(manifest.read_text())
    if data["hermes_commit"] != qualification["hermes_commit"]:
        raise ValueError("Другая основа Hermes требует отдельной проверки")
    for name, digest in data["files"].items():
        path = (root / "hermes-agent" / name).resolve(strict=True)
        if not path.is_relative_to(root / "hermes-agent"):
            raise ValueError("Небезопасный путь манифеста")
        if name != "gateway/run_inbound.py" and sha(path) != digest:
            raise ValueError("Не совпал доверенный файл: " + name)
    if args.check:
        digest = sha(manifest)
        admissions = all(value.get(str(manifest), digest) == digest for value in
                         (json.loads(path.read_text()).get("local_adapter_sha256", {}) for path in settings_paths))
        print(json.dumps({"compatible": True, "installed": current == after,
                          "core_manifest_sealed": data["files"].get("gateway/run_inbound.py") == after,
                          "profile_admissions_valid": admissions}))
        return
    # Offline application only. An existing pidfile is conservatively a live owner
    # until the operator has stopped the gateway by its own service interface.
    for home in (root / "data", root / "data/profiles/bn-gsd-only", root / "data/profiles/bn-udr-only"):
        if (home / "gateway.pid").exists():
            raise ValueError("Сначала штатно остановите шлюз; найден gateway.pid: " + str(home))
    backup = root / "operator/gateway-command-fix-r5/rollback"
    if args.rollback:
        if current != after or not backup.is_dir():
            raise ValueError("Нет подходящего сохранённого отката")
        if sha(backup / "run_inbound.py") != BEFORE:
            raise ValueError("Повреждён исходник отката")
        atomic(target, (backup / "run_inbound.py").read_bytes())
        atomic(manifest, (backup / "core-manifest.json").read_bytes())
        for index, path in enumerate(settings_paths):
            atomic(path, (backup / f"settings-{index}.json").read_bytes())
        print("Исходник и доверенный манифест восстановлены; шлюз не запускался")
        return
    if current == after and data["files"].get("gateway/run_inbound.py") == after:
        digest = sha(manifest)
        if any(json.loads(path.read_text()).get("local_adapter_sha256", {}).get(str(manifest), digest) != digest
               for path in settings_paths):
            raise ValueError("Исправление неполное: не совпал допуск манифеста профиля")
        print("Исправление уже установлено и включено в доверенный манифест")
        return
    backup.mkdir(parents=True, exist_ok=False)
    shutil.copy2(target, backup / "run_inbound.py")
    shutil.copy2(manifest, backup / "core-manifest.json")
    for index, path in enumerate(settings_paths):
        shutil.copy2(path, backup / f"settings-{index}.json")
    data["files"]["gateway/run_inbound.py"] = after
    try:
        atomic(target, source.read_bytes())
        atomic(manifest, (json.dumps(data, indent=2) + "\n").encode())
        digest = sha(manifest)
        for path in settings_paths:
            settings = json.loads(path.read_text())
            admissions = settings.get("local_adapter_sha256", {})
            if str(manifest) in admissions:
                admissions[str(manifest)] = digest
                atomic(path, (json.dumps(settings, ensure_ascii=False, indent=2) + "\n").encode())
    except BaseException:
        atomic(target, (backup / "run_inbound.py").read_bytes())
        atomic(manifest, (backup / "core-manifest.json").read_bytes())
        for index, path in enumerate(settings_paths):
            atomic(path, (backup / f"settings-{index}.json").read_bytes())
        raise
    print("Исправление установлено; состояния, ограничения и доступы сохранены; шлюз не запускался")


if __name__ == "__main__":
    main()
