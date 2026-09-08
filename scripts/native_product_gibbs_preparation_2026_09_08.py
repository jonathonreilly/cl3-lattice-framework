"""Finite native preparation evidence; full proof and supplied inputs are in the note."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/NATIVE_PRODUCT_GIBBS_PREPARATION_NOTE_2026-09-08.md",
    "docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/NATIVE_EDGE_RECORD_LOCAL_CYCLE_TRANSPORT_AND_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/native_product_gibbs_dimer_2026_09_08.py",
    "scripts/native_product_gibbs_path_2026_09_08.py",
    "scripts/native_product_gibbs_encoded_2026_09_08.py",
)
from pathlib import Path
import contextlib, io, json, os, resource, runpy, time
for resource_variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[resource_variable] = "1"
start = time.monotonic()
root = Path(__file__).resolve().parents[1]
parts = {}
for name in ("dimer", "path", "encoded"):
    with contextlib.redirect_stdout(io.StringIO()):
        data = runpy.run_path(str(root / "scripts" / f"native_product_gibbs_{name}_2026_09_08.py"))
    parts[name] = data["result"]
    if parts[name]["status"] != "PASS" or not all(parts[name]["checks"].values()):
        raise RuntimeError(f"Incomplete {name} evidence")
seconds = time.monotonic() - start
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_mib = rss / (1024 ** 2 if os.uname().sysname == "Darwin" else 1024)
if seconds > AUDIT_TIMEOUT_SEC or rss_mib > 384:
    raise RuntimeError(f"Resource contract failed: {seconds}s, {rss_mib}MiB")
result = {"status": "PASS", "classification": "conditional-support", "parts": parts,
          "executed_assertions": sum(len(x["checks"]) for x in parts.values()),
          "elapsed_seconds": seconds, "peak_rss_mib": rss_mib,
          "scope": "Finite operator evidence for the declared construction. General path proof is analytic; preparation, controls, beta, h and Born events are supplied."}
(root / "outputs" / "native_product_gibbs_preparation_2026_09_08.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
