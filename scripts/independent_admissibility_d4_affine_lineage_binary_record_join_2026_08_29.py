#!/usr/bin/env python3
"""Independent diagonal check of the corrected Eta Block-03 operator claim."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import re
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
PRIMARY = ROOT / "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py"
PRIMARY_CACHE = ROOT / "logs/runner-cache/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt",
)
ACTIVE = {5, 6, 9, 10, 17, 18, 20, 23, 24, 27, 29, 30,
          33, 34, 36, 39, 40, 43, 45, 46, 53, 54, 57, 58}


def cache_bound() -> bool:
    text = PRIMARY_CACHE.read_text(encoding="utf-8")
    expected = hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
    match = re.search(r"^runner_sha256:\s*([0-9a-f]{64})$", text, re.M)
    return bool(match and match.group(1) == expected and "status: ok" in text
                and "TOTAL: PASS=5 FAIL=0" in text)


def main() -> int:
    u = sp.symbols("u", real=True)
    high, low = sp.sqrt((1 + u) / 2), sp.sqrt((1 - u) / 2)
    root_plus = sp.diag(high, low)
    opposite = sp.diag((1 - u) / 2, (1 + u) / 2)
    cross = sp.simplify(root_plus * opposite * root_plus)
    expected = (1 - u**2) * sp.eye(2) / 4
    diagonal_ok = all(sp.simplify(v) == 0 for v in (cross - expected))

    spectra = {
        q: ((1 + q) / 2, (1 - q) / 2)
        for q in (sp.Integer(1), sp.Rational(1, 2))
    }
    bound = Fraction(2193749493000038667200, 177556693536960624997803)
    checks = (
        ("A_primary_identity", cache_bound(), "primary cache is bound to the current primary source"),
        ("B_independent_diagonal_calculus", diagonal_ok,
         "direct diagonal roots give (1-u^2)I/4 without importing primary definitions"),
        ("C_spectral_inequivalence", spectra[sp.Integer(1)] != spectra[sp.Rational(1, 2)],
         f"sharp and half-sharp spectra differ: {spectra}"),
        ("D_domain_and_bound", len(ACTIVE) == 24 and bound < Fraction(1, 71),
         "the supplied final rational is exactly below the supplied gap; this check does not reconstruct the resolvents"),
    )
    passed = sum(ok for _, ok, _ in checks)
    for name, ok, message in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {message}")
    print("INDEPENDENT: active=24; diagonal_root=true; parent_cubic_recomputed=false.")
    print("MUTATION_CREDIT: none claimed; no mutation sweep executed.")
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
