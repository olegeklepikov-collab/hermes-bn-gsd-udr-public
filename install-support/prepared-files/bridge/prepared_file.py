"""Host-only preservation of an existing workspace artifact; never accepts claims."""
from pathlib import Path
import hashlib
import os
import re
import stat
import tempfile

MAX_BYTES = 64 * 1024 * 1024  # Pinned Foundation ArtifactService boundary, not a truncation.


def exact_source(workspace, source_path, expected_sha256):
    """Read one allowed regular file through no-follow directory descriptors."""
    if not re.fullmatch(r"[a-f0-9]{64}", expected_sha256):
        raise ValueError("exact_artifact_sha256_required")
    workspace = Path(workspace)
    if workspace.is_symlink() or not workspace.is_dir():
        raise PermissionError("regular_workspace_required")
    source = Path(source_path)
    if ".." in source.parts:
        raise PermissionError("workspace_source_required")
    if source.is_absolute():
        try:
            source = source.relative_to(workspace)
        except ValueError as exc:
            raise PermissionError("workspace_source_required") from exc
    parts = source.parts
    if len(parts) < 3 or parts[0] != "research" or any(p.startswith(".") for p in parts):
        raise PermissionError("public_research_file_required")
    filename = parts[-1]
    if len(filename) > 240 or any(ord(c) < 32 for c in filename):
        raise ValueError("safe_artifact_filename_required")
    directory = os.open(workspace, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for part in parts[:-1]:
            following = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory)
            os.close(directory)
            directory = following
        descriptor = os.open(filename, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory)
        try:
            before = os.fstat(descriptor)
            if not stat.S_ISREG(before.st_mode) or before.st_size > MAX_BYTES:
                raise ValueError("bounded_regular_artifact_required")
            chunks, total = [], 0
            while block := os.read(descriptor, 1024 * 1024):
                total += len(block)
                if total > MAX_BYTES:
                    raise ValueError("artifact_size_exceeded_no_truncation")
                chunks.append(block)
            after = os.fstat(descriptor)
            fields = ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")
            if any(getattr(before, key) != getattr(after, key) for key in fields):
                raise PermissionError("artifact_changed_during_read")
        finally:
            os.close(descriptor)
    finally:
        os.close(directory)
    raw = b"".join(chunks)
    if not raw or hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise PermissionError("artifact_source_hash_mismatch")
    return raw, str(source), filename


def _owner(sid, run_id):
    import backend as b
    body = b.saved(sid)
    if (not body or body.get("native_child") or body.get("managed_worker")
            or body.get("run_id") != run_id or body.get("phase") not in {"running", "draft"}):
        raise PermissionError("own_root_research_required")
    session, artifacts = b.session(body)
    session.check()
    return body, session, artifacts


def _read_registered(body, session, artifacts, artifact_id, expected_sha256):
    import backend as b
    if not re.fullmatch(r"BNAF-[a-f0-9]{32}", artifact_id):
        raise PermissionError("prepared_artifact_reference_required")
    stored = session.state.get({"schema_version": 1, "database": "kw_core",
        "project_id": body["project"], "object_id": artifact_id})
    item = stored.get("object", {})
    if (stored.get("status") != "found" or item.get("contract") != "PreparedDeliverableV1"
            or item.get("run_id") != body["run_id"] or item.get("project_id") != body["project"]
            or item.get("work_contract_ref") != body["work_ref"] or item.get("sha256") != expected_sha256):
        raise PermissionError("prepared_artifact_scope_or_version_mismatch")
    path = artifacts.originals / expected_sha256
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, "rb") as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_BYTES:
            raise PermissionError("canonical_artifact_invalid")
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) != item["bytes"] or b.digest(raw) != expected_sha256:
        raise PermissionError("canonical_artifact_bytes_mismatch")
    return item, raw


def registered(sid, run_id, artifact_id, expected_sha256):
    body, session, artifacts = _owner(sid, run_id)
    item, raw = _read_registered(body, session, artifacts, artifact_id, expected_sha256)
    return body, session, item, raw


def adopt(sid, run_id, source_path, expected_sha256):
    import backend as b
    body, session, artifacts = _owner(sid, run_id)
    raw, relative, filename = exact_source(b.ROOT.parent / "Hermes BN/workspace", source_path, expected_sha256)
    identity = {"project_id": body["project"], "run_id": run_id,
                "source_relative_path": relative, "sha256": expected_sha256}
    artifact_id = "BNAF-" + b.digest(b.canonical(identity))[:32]
    query = {"schema_version": 1, "database": "kw_core", "project_id": body["project"], "object_id": artifact_id}
    existing = session.state.get(query)
    if existing.get("status") == "found":
        item, saved_raw = _read_registered(body, session, artifacts, artifact_id, expected_sha256)
        if saved_raw != raw:
            raise PermissionError("prepared_artifact_bytes_changed")
        return {**item, "idempotent": True}
    acquisition = "BNAQ-" + b.digest(b.canonical(identity))[:32]
    # Only the host writes quarantine. No model-supplied destination or canonical path.
    descriptor, temporary = tempfile.mkstemp(prefix="bn-prepared-", dir=artifacts.quarantine)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        receipt = artifacts.ingest({"schema_version": 1, "acquisition_id": acquisition,
            "relative_path": Path(temporary).name, "media_type": "text/markdown" if filename.lower().endswith(".md") else "application/octet-stream",
            "max_bytes": MAX_BYTES})
    finally:
        Path(temporary).unlink(missing_ok=True)
    if receipt.get("status") != "accepted" or receipt.get("content_hash") != expected_sha256:
        raise PermissionError("prepared_artifact_intake_failed")
    item = {"schema_version": 1, "contract": "PreparedDeliverableV1", "status": "prepared",
        "artifact_id": artifact_id, "foundation_artifact_id": receipt["artifact_id"],
        **identity, "work_contract_ref": body["work_ref"], "origin_session_id": sid,
        "filename": filename, "bytes": len(raw), "sha256": expected_sha256,
        "intake_receipt": receipt, "byte_identity_verified": True,
        "claims_accepted": False, "delivery_authorized": False,
        "research_completed": False, "content_rewritten": False}
    session.check()
    b.put(session.state, item, body["project"], artifact_id, body["host_run"])
    _read_registered(body, session, artifacts, artifact_id, expected_sha256)
    return {**item, "idempotent": False}
