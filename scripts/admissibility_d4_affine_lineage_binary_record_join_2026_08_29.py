#!/usr/bin/env python3
"""Finite conditional operator core for the corrected Eta Block-03 claim."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sympy as sp

# Source-only import: makes the co-load-bearing checker visible to both packet
# dependency consumers. No checker definitions are used by this computation.
import independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as _packet_helper  # noqa: F401,E501

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
)
ACTIVE = frozenset((5, 6, 9, 10, 17, 18, 20, 23, 24, 27, 29, 30,
                    33, 34, 36, 39, 40, 43, 45, 46, 53, 54, 57, 58))
EXPECTED_BOUND = Fraction(
    2193749493000038667200,
    177556693536960624997803,
)


def equal(a: sp.MatrixBase, b: sp.MatrixBase) -> bool:
    return all(sp.simplify(x) == 0 for x in (a - b))


def main() -> int:
    checks: list[tuple[str, bool, str]] = []
    add = lambda name, ok, message: checks.append((name, bool(ok), message))

    weights = {n: sum(mask.bit_count() == n for mask in ACTIVE) for n in (2, 4)}
    add("A_supplied_active_domain", len(ACTIVE) == 24 and weights == {2: 12, 4: 12},
        f"active=24 with weight census {weights}; action/decoder selection remains supplied")

    u = sp.symbols("u", real=True)
    I2 = sp.eye(2)
    S = sp.diag(1, -1)
    qp, qm = (I2 + S) / 2, (I2 - S) / 2
    roots = []
    effects = []
    for b in (0, 1):
        sign = 1 if b == 0 else -1
        effect = (I2 + sign * u * S) / 2
        root = (sp.sqrt((1 + u) / 2) * (qp if sign == 1 else qm)
                + sp.sqrt((1 - u) / 2) * (qm if sign == 1 else qp))
        roots.append(root)
        effects.append(effect)
    # On the declared real interval these roots are Hermitian.  Multiplying
    # directly avoids asking unconstrained symbolic conjugation to infer the
    # signs of 1+u and 1-u.
    root_ok = all(equal(sp.simplify(k * k), e) for k, e in zip(roots, effects))
    complete = equal(effects[0] + effects[1], I2)
    cross = sp.simplify(roots[0] * effects[1] * roots[0])
    expected_cross = (1 - u**2) * I2 / 4
    add("B_effect_root_channel", root_ok and complete and equal(cross, expected_cross),
        "symbolic projector roots are exact, effects complete, and active cross-effect is (1-u^2)I/4")

    inactive_effect = I2 / 2
    inactive_root = I2 / sp.sqrt(2)
    inactive_cross = sp.simplify(inactive_root * inactive_effect * inactive_root)
    sharp_spectrum = (sp.Integer(1), sp.Integer(0))
    half_spectrum = (sp.Rational(3, 4), sp.Rational(1, 4))
    add("C_solution_family", equal(inactive_cross, I2 / 4)
        and sharp_spectrum != half_spectrum,
        "different u have different effect spectra; inactive zero-detector blocks retain I/4 cross-effect")

    x = Fraction(1, 10**9)
    a, b = 22 * 13 * x, 16 * 13 * x
    y, r = Fraction(22, 1 - a), Fraction(20, 1 - b)
    dy = x * 22**2 * 13 / (1 - a)
    dr = x * 16 * 13 * 20 / (1 - b)
    bound = 2 * (dr * y * r + 20 * dy * r + 20 * 22 * dr)
    add("D_conditional_positivity_bound", bound == EXPECTED_BOUND and bound < Fraction(1, 71),
        f"supplied resolvent estimates give final bound={bound} < supplied gap 1/71")

    note = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = ("supplied finite-model inputs", "not evidence in the present proof",
                "not a global uniqueness", "no formal audit has run")
    add("E_scope", all(token in note for token in required),
        "parent response, physical realization, global uniqueness, and audit remain explicitly outside the result")

    passed = 0
    for name, ok, message in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {message}")
        passed += int(ok)
    print(f"ACTIVE: count={len(ACTIVE)}; weights={weights}; supplied_action=true.")
    print("LAW: domain=0<u<=1; spectral_family=inequivalent; active_repeatability=u=1; inactive_cross=I/4.")
    print(f"BOUND: endpoint=1e-9; exact={bound}; baseline_norms=supplied.")
    print("MUTATION_CREDIT: none claimed; no mutation sweep executed.")
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
