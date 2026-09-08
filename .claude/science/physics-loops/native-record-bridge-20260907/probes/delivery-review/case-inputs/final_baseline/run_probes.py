"""Reproduce the bounded research probes without modifying the tracked packet."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

AUDIT_TIMEOUT_SEC = 180


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, help="Optional directory for fresh raw outputs")
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    manifest = json.loads((packet / "FROZEN_PROBE_SHA256.json").read_text())
    for relative, expected in manifest.items():
        actual = hashlib.sha256((packet / relative).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"Frozen input changed: {relative}")
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
    jobs = [
        ("native-instrument/probe.py", "checks", 71),
        ("native-instrument-cold-review/check.py", "checks", 29),
        ("record-relay-review/check.py", "TOTAL", 15),
        ("probability-family/check.py", "assertions", 27),
        ("probability-family-cold-review/independent_portable.py", None, None),
        ("action-measure/check.py", "pass_count", 27),
        ("action-measure/check_reservoir.py", "pass_count", 17),
    ]
    env = dict(os.environ)
    # Every probe uses executable mathematical assertions. Never inherit -O.
    env.pop("PYTHONOPTIMIZE", None)
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
        env[key] = "1"
    rows = []
    with tempfile.TemporaryDirectory(prefix="native-record-probes-") as temporary:
        work = Path(temporary) / "probes"
        shutil.copytree(packet / "probes", work)
        for relative, count_key, expected_count in jobs:
            result = subprocess.run(
                [sys.executable, "-B", str(work / relative)],
                cwd=work, env=env, capture_output=True, text=True,
                timeout=AUDIT_TIMEOUT_SEC,
            )
            if args.output_dir:
                stem = relative.replace("/", "__").removesuffix(".py")
                (args.output_dir / (stem + ".stdout.json")).write_text(result.stdout)
                (args.output_dir / (stem + ".stderr.txt")).write_text(result.stderr)
            if result.returncode:
                raise RuntimeError(f"{relative} exited {result.returncode}: {result.stderr}")
            payload = json.loads(result.stdout)
            if count_key and payload[count_key] != expected_count:
                raise RuntimeError(f"Unexpected executed assertion count for {relative}")
            if payload.get("failed", 0) != 0:
                raise RuntimeError(f"Reported failed assertions in {relative}")
            if isinstance(payload.get("checks"), dict) and not all(value is True for value in payload["checks"].values()):
                raise RuntimeError(f"Reported false mathematical predicate in {relative}")
            if relative == "probability-family/check.py":
                # The independent checker below consumes this fresh result.
                (work / "probability-family/result.json").write_text(result.stdout)
            if relative.endswith("independent_portable.py"):
                if payload.get("status") != "PASS" or payload["all_probability_rows_checked"] != 1458:
                    raise RuntimeError("Independent probability census did not complete")
            rows.append({
                "probe": relative, "exit_code": result.returncode,
                "executed_assertions": payload[count_key] if count_key else None,
                "scope": "Bounded finite checks; analytical proofs and assumptions are separate",
            })
    # Verify that subprocess execution did not alter the tracked inputs.
    for relative, expected in manifest.items():
        if hashlib.sha256((packet / relative).read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"Tracked input changed during reproduction: {relative}")
    summary = {
        "status": "PASS", "probe_programs": len(rows),
        "executed_named_assertions": sum(row["executed_assertions"] or 0 for row in rows),
        "additional_independent_probability_rows": 1458,
        "canonical_audit_cache": False, "audit_verdict": None,
        "rows": rows,
    }
    if args.output_dir:
        (args.output_dir / "SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
