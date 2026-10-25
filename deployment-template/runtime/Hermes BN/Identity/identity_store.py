#!/usr/bin/env python3
"""Owner-side identity archive. Never writes Hermes profile files or calls models."""
import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import tempfile
import uuid

VERSION = "0.1.0"
RESERVED = ("continuity", "foundations", "epistemic_stance", "values_and_boundaries",
            "dispositions", "relationships", "expression")
SAFE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_-]{0,95}$")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_regular(path):
    # O_NOFOLLOW also rejects a last-component symlink introduced after lstat.
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, "rb") as handle:
        if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
            raise ValueError("expected_regular_file")
        return handle.read()


def save_new(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


class Store:
    def __init__(self, root):
        self.root = Path(root).resolve(strict=True)
        self.config = json.loads(read_regular(self.root / "policy.json"))
        if self.config["schema_version"] != 1:
            raise ValueError("unsupported_schema_version")
        self.bindings = self.config["profile_bindings"]
        for name, path in self.bindings.items():
            if not SAFE.fullmatch(name) or not Path(path).is_absolute():
                raise ValueError("invalid_profile_binding")

    @contextlib.contextmanager
    def locked(self):
        fd = os.open(self.root / ".lock", os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            yield
        finally:
            os.close(fd)

    def observed(self):
        path = self.root / "observed.json"
        return json.loads(read_regular(path)) if path.exists() else None

    def load(self, revision=None):
        pointer = self.observed()
        if revision is None:
            if not pointer:
                raise ValueError("no_observed_revision")
            revision = pointer["revision"]
        if not isinstance(revision, str) or not SAFE.fullmatch(revision):
            raise ValueError("invalid_revision")
        seen = set()
        while pointer:
            current = pointer["revision"]
            if current in seen or not isinstance(current, str) or not SAFE.fullmatch(current):
                raise ValueError("invalid_revision_chain")
            seen.add(current)
            folder = self.root / "versions" / current
            if folder.resolve() != folder:
                raise ValueError("revision_symlink_forbidden")
            raw = read_regular(folder / "manifest.json")
            if digest(raw) != pointer["manifest_sha256"]:
                raise ValueError("manifest_hash_mismatch")
            manifest = json.loads(raw)
            if manifest["revision"] != current:
                raise ValueError("revision_pointer_mismatch")
            if current == revision:
                break
            pointer = manifest["previous"]
        else:
            raise ValueError("revision_not_in_observed_history")
        if (manifest["schema_version"] != 1 or manifest["revision"] != revision
                or manifest["agent_id"] != self.config["agent_id"]
                or manifest["instance_id"] != self.config["instance_id"]):
            raise ValueError("edition_identity_mismatch")
        if manifest["deep_identity"] != dict.fromkeys(RESERVED):
            raise ValueError("deep_content_not_supported_in_foundation_release")
        if set(manifest["profiles"]) != set(self.bindings):
            raise ValueError("edition_profiles_mismatch")
        for name, item in manifest["profiles"].items():
            expected = f"{name}/SOUL.md"
            if item["file"] != expected or item["native_path"] != self.bindings[name]:
                raise ValueError("edition_path_mismatch")
            if (folder / name).resolve() != folder / name:
                raise ValueError("profile_symlink_forbidden")
            data = read_regular(folder / expected)
            if digest(data) != item["sha256"] or len(data) != item["bytes"]:
                raise ValueError("soul_hash_mismatch")
        return folder, manifest

    def capture(self, reason):
        if not reason.strip():
            raise ValueError("reason_required")
        with self.locked():
            previous = self.observed()
            if previous:
                self.load()
            sources = {}
            for name, native in self.bindings.items():
                data = read_regular(native)
                if not data.decode("utf-8").strip():
                    raise ValueError("empty_soul")
                sources[name] = data
            versions = self.root / "versions"
            versions.mkdir(exist_ok=True, mode=0o700)
            revision = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ-") + uuid.uuid4().hex[:12]
            staging = Path(tempfile.mkdtemp(prefix=".capture-", dir=versions))
            try:
                profiles = {}
                for name, data in sources.items():
                    (staging / name).mkdir(mode=0o700)
                    save_new(staging / name / "SOUL.md", data)
                    profiles[name] = {"file": f"{name}/SOUL.md", "native_path": self.bindings[name],
                                      "sha256": digest(data), "bytes": len(data)}
                # Reject mixed observations caused by a concurrent native-file edit.
                if any(read_regular(self.bindings[n]) != d for n, d in sources.items()):
                    raise ValueError("native_changed_during_capture")
                manifest = {"schema_version": 1, "store_version": VERSION, "revision": revision,
                            "agent_id": self.config["agent_id"], "instance_id": self.config["instance_id"],
                            "previous": previous, "observed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                            "reason": reason, "status": "observed_not_activated",
                            "content_authority": "existing_native_soul",
                            "deep_identity": dict.fromkeys(RESERVED), "profiles": profiles}
                raw = encoded(manifest)
                save_new(staging / "manifest.json", raw)
                staging.rename(versions / revision)
                pointer = {"revision": revision, "manifest_sha256": digest(raw)}
                pending = self.root / (".observed-" + uuid.uuid4().hex)
                save_new(pending, encoded(pointer))
                os.replace(pending, self.root / "observed.json")
                return pointer
            finally:
                if staging.exists():
                    shutil.rmtree(staging)

    def verify(self, revision=None):
        with self.locked():
            _, manifest = self.load(revision)
            profiles = {}
            for name, item in manifest["profiles"].items():
                try:
                    current = read_regular(item["native_path"])
                    profiles[name] = {"archive_sha256": item["sha256"], "native_sha256": digest(current),
                                      "matches_native": digest(current) == item["sha256"]}
                except OSError as exc:
                    profiles[name] = {"matches_native": False, "error": type(exc).__name__}
            return {"ok": all(p["matches_native"] for p in profiles.values()), "archive_valid": True,
                    "revision": manifest["revision"], "deep_identity_defined": False, "profiles": profiles}

    def export(self, revision, profile, output):
        with self.locked():
            folder, manifest = self.load(revision)
            if profile not in manifest["profiles"]:
                raise ValueError("unknown_profile")
            target = Path(output).absolute()
            resolved = target.resolve()
            if resolved in {Path(p).resolve() for p in self.bindings.values()}:
                raise ValueError("native_write_forbidden")
            if resolved.is_relative_to(self.root):
                raise ValueError("store_write_forbidden")
            save_new(target, read_regular(folder / manifest["profiles"][profile]["file"]))
            return {"exported": str(target), "sha256": manifest["profiles"][profile]["sha256"],
                    "activated": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    sub = parser.add_subparsers(dest="command", required=True)
    capture = sub.add_parser("capture")
    capture.add_argument("--reason", required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("--revision")
    export = sub.add_parser("export")
    export.add_argument("--revision", required=True)
    export.add_argument("--profile", required=True)
    export.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        store = Store(args.root)
        if args.command == "capture":
            result = store.capture(args.reason)
        elif args.command == "verify":
            result = store.verify(args.revision)
        else:
            result = store.export(args.revision, args.profile, args.output)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result.get("ok", True) else 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
