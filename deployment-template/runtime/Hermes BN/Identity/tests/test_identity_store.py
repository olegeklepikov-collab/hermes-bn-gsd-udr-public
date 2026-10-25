import importlib.util
import json
from pathlib import Path
import stat
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "identity_store.py"
spec = importlib.util.spec_from_file_location("identity_store", MODULE)
identity = importlib.util.module_from_spec(spec)
spec.loader.exec_module(identity)


class IdentityStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "identity"
        self.root.mkdir(mode=0o700)
        self.native = self.base / "SOUL.md"
        self.payload = "# Учебная идентичность\r\nТолько тест.\n".encode()
        self.native.write_bytes(self.payload)
        config = {"schema_version": 1, "agent_id": "test-agent", "instance_id": "test-instance",
                  "profile_bindings": {"main": str(self.native)}}
        identity.save_new(self.root / "policy.json", identity.encoded(config))
        self.store = identity.Store(self.root)

    def capture(self):
        return self.store.capture("Синтетическая проверка")

    def test_exact_bytes_and_native_untouched(self):
        before = self.native.stat().st_mtime_ns
        pointer = self.capture()
        folder, manifest = self.store.load()
        self.assertEqual((folder / "main/SOUL.md").read_bytes(), self.payload)
        self.assertEqual(self.native.stat().st_mtime_ns, before)
        self.assertEqual(self.native.read_bytes(), self.payload)
        self.assertTrue(self.store.verify()["ok"])
        self.assertEqual(manifest["revision"], pointer["revision"])
        self.assertEqual(set(manifest["deep_identity"].values()), {None})

    def test_drift_is_reported_without_overwrite(self):
        self.capture()
        self.native.write_text("Новое содержание владельца")
        result = self.store.verify()
        self.assertFalse(result["ok"])
        self.assertTrue(result["archive_valid"])
        self.assertEqual(self.native.read_text(), "Новое содержание владельца")

    def test_history_retains_old_content_and_parent(self):
        first = self.capture()
        self.native.write_text("Новая учебная редакция")
        self.capture()
        _, current = self.store.load()
        old, _ = self.store.load(first["revision"])
        self.assertEqual(current["previous"], first)
        self.assertEqual((old / "main/SOUL.md").read_bytes(), self.payload)

    def test_archive_content_tamper_rejected(self):
        self.capture()
        folder, _ = self.store.load()
        (folder / "main/SOUL.md").write_text("Изменённый архив")
        with self.assertRaisesRegex(ValueError, "soul_hash_mismatch"):
            self.store.verify()

    def test_manifest_tamper_rejected(self):
        self.capture()
        folder, _ = self.store.load()
        with (folder / "manifest.json").open("ab") as handle:
            handle.write(b" ")
        with self.assertRaisesRegex(ValueError, "manifest_hash_mismatch"):
            self.store.load()

    def test_historical_manifest_hash_is_checked(self):
        first = self.capture()
        folder, _ = self.store.load()
        self.native.write_text("Следующая редакция")
        self.capture()
        with (folder / "manifest.json").open("ab") as handle:
            handle.write(b" ")
        with self.assertRaisesRegex(ValueError, "manifest_hash_mismatch"):
            self.store.load(first["revision"])

    def test_unregistered_revision_is_rejected(self):
        self.capture()
        with self.assertRaisesRegex(ValueError, "revision_not_in_observed_history"):
            self.store.load("not-registered")

    def test_export_exact_exclusive_and_not_active(self):
        revision = self.capture()["revision"]
        target = self.base / "review-copy.md"
        result = self.store.export(revision, "main", target)
        self.assertEqual(target.read_bytes(), self.payload)
        self.assertFalse(result["activated"])
        self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o600)
        with self.assertRaises(FileExistsError):
            self.store.export(revision, "main", target)
        with self.assertRaisesRegex(ValueError, "native_write_forbidden"):
            self.store.export(revision, "main", self.native)
        with self.assertRaisesRegex(ValueError, "store_write_forbidden"):
            self.store.export(revision, "main", self.root / "other.md")

    def test_symlink_native_is_rejected(self):
        other = self.base / "other.md"
        other.write_text("Тест")
        self.native.unlink()
        self.native.symlink_to(other)
        with self.assertRaises(OSError):
            self.capture()
        self.assertIsNone(self.store.observed())

    def test_invalid_revision_and_unknown_profile_rejected(self):
        revision = self.capture()["revision"]
        with self.assertRaisesRegex(ValueError, "invalid_revision"):
            self.store.load("../elsewhere")
        with self.assertRaisesRegex(ValueError, "unknown_profile"):
            self.store.export(revision, "unknown", self.base / "out.md")

    def test_failed_capture_does_not_advance_pointer(self):
        before = self.capture()
        self.native.write_bytes(b"\xff")
        with self.assertRaises(UnicodeDecodeError):
            self.capture()
        self.assertEqual(self.store.observed(), before)
        self.assertEqual(len(list((self.root / "versions").iterdir())), 1)

    def test_private_edition_permissions(self):
        self.capture()
        folder, _ = self.store.load()
        for path in [folder, folder / "main"]:
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o700)
        for path in [folder / "manifest.json", folder / "main/SOUL.md", self.root / "observed.json"]:
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)


if __name__ == "__main__":
    unittest.main(verbosity=2)
