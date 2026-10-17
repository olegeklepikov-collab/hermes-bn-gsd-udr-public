#!/usr/bin/env python3
"""Stage a requested upstream revision; refuse conflicts and never switch the active runtime."""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys

PACKAGE = Path(__file__).resolve().parent


def run(argv, cwd=None, env=None):
    return subprocess.run(argv, cwd=cwd, env=env, check=True, text=True, capture_output=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True, help="Local official Hermes checkout")
    p.add_argument("--ref", required=True, help="Explicit branch/tag/commit; never guessed")
    p.add_argument("--destination", required=True)
    p.add_argument("--uv", required=True); p.add_argument("--python", required=True)
    p.add_argument("--baseline-overlay", help="Explicit separately audited pre-existing user changes")
    a = p.parse_args(); source = Path(a.source).resolve(); destination = Path(a.destination).resolve()
    if destination.exists():
        raise ValueError("Destination exists; stages are immutable and never overwritten")
    sha = run(["git", "rev-parse", "--verify", "--end-of-options", a.ref + "^{commit}"], source).stdout.strip()
    if len(sha) != 40:
        raise ValueError("Expected an immutable Git commit")
    run(["git", "clone", "--no-checkout", "--no-hardlinks", str(source), str(destination)])
    run(["git", "checkout", "--detach", sha], destination)
    patch = PACKAGE / "release/hermes-native-controls.patch"
    run(["git", "apply", "--check", str(patch)], destination)
    run(["git", "apply", str(patch)], destination)
    if a.baseline_overlay:
        overlay = Path(a.baseline_overlay).resolve(strict=True)
        run(["git", "apply", "--check", str(overlay)], destination)
        run(["git", "apply", str(overlay)], destination)
    # Frozen upstream dependencies in a fresh environment. No active venv/config/token writes.
    run([a.uv, "sync", "--frozen", "--extra", "dev", "--python", a.python], destination)
    checks = json.loads((PACKAGE / "release/core-test-files.json").read_text())
    if a.baseline_overlay and (destination / "tests/tools/test_tool_discovery_batch_contract.py").exists():
        checks.append("tests/tools/test_tool_discovery_batch_contract.py")
    run(["bash", "scripts/run_tests.sh", *checks, "--tb=short"], destination)
    from runtime_guard import verify
    template = json.loads((PACKAGE / "release/core-manifest.json").read_text())
    import hashlib
    template.update(hermes_commit=sha, files={name: hashlib.sha256((destination / name).read_bytes()).hexdigest()
                    for name in template["files"]})
    manifest = destination / "bn-gsd-compatibility.json"
    manifest.write_text(json.dumps(template, indent=2))
    verify(destination, manifest)
    # Native behavior tests still need a fresh profile and actual provider/gateway acceptance.
    report = {"stage": str(destination), "commit": sha, "patch_applied": True,
              "frozen_dependencies": True, "core_contract_tests_passed": True,
              "live_provider_gateway_acceptance": "required_before_activation", "active_runtime_changed": False}
    report["baseline_overlay_applied"] = bool(a.baseline_overlay)
    (destination / "bn-gsd-stage-result.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
