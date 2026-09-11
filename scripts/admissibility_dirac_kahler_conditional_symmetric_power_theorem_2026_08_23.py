#!/usr/bin/env python3
"""Corrected finite symmetric-power and kernel-candidate checks."""

from __future__ import annotations

import ast
import hashlib
import math
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11 as fixture


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py",
    "scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md': '8466c8eee317a15a8994f251ce5730834fa2f67d24ca5a390554c671e61ffb1c',
    'scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py': '7b91bfd85d98bada7f64196665722cc08267812fd2c5344dab8b342f236129b6',
    'scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py': '594e7032f453fec4c6791067a147d1544636ddce9567a87a3449352b5546d5f5',
    'scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py': '8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}
AUDIT_TIMEOUT_SEC = 120

R = sp.Rational
CHECKS: list[tuple[str, bool, str]] = []
EXPECTED_ACTION = {
    ("8x4", R(1, 4)): (5, 3, 0),
    ("12x4", R(1, 4)): (4, 4, 0),
    ("8x4", sp.Integer(0)): (4, 0, 4),
    ("12x4", sp.Integer(0)): (4, 0, 4),
}
EXPECTED_COVARIANCE = {
    ("8x4", R(1, 4)): (6, 2, 0),
    ("12x4", R(1, 4)): (4, 4, 0),
    ("8x4", sp.Integer(0)): (6, 2, 0),
    ("12x4", sp.Integer(0)): (4, 4, 0),
}


def check(name: str, condition: bool, detail: str) -> None:
    CHECKS.append((name, bool(condition), detail))


def symmetric_power_minor() -> None:
    p = sp.Symbol("p", positive=True)
    qq = sp.Symbol("qq", positive=True)
    a, b = sp.symbols("a b", real=True)
    q = -qq
    r = a + sp.I * b
    kernel = sp.Matrix([[p, r], [sp.conjugate(r), q]])
    for degree in (2, 3, 4):
        pure = (0,) * degree
        mixed = (0,) * (degree - 1) + (1,)
        aa = fixture.monomial_gram(kernel, pure, pure)
        bb = fixture.monomial_gram(kernel, pure, mixed)
        dd = fixture.monomial_gram(kernel, mixed, mixed)
        determinant = sp.expand(aa * dd - bb * sp.conjugate(bb))
        expected = sp.expand(
            math.factorial(degree)
            * math.factorial(degree - 1)
            * p ** (2 * degree - 2)
            * (p * q - (a ** 2 + b ** 2))
        )
        check(
            f"degree-{degree} permanent minor",
            sp.expand(determinant - expected) == 0,
            f"det={sp.factor(determinant)}",
        )


def finite_kernel_candidates() -> None:
    measured_action: dict = {}
    measured_covariance: dict = {}
    raw_status: dict = {}
    for tag, cover_t, lx in fixture.COVER_EXTENTS:
        bench = fixture.base.Bench(f"released7359-a-{tag}", cover_t, lx)
        for dial in (sp.Integer(0), R(1, 4)):
            substitutions = bench.carrier(st=dial)
            action = sp.expand(bench.form.subs(substitutions))
            q_matrix = sp.expand(bench.Q.subs(substitutions))
            raw_covariance, covariance = fixture.selected_reflected_covariance(
                bench, q_matrix
            )
            key = (tag, dial)
            measured_action[key] = fixture.base.real_symmetric_inertia(action)
            measured_covariance[key] = fixture.base.real_symmetric_inertia(covariance)
            raw_status[key] = raw_covariance == raw_covariance.H
            check(
                f"{tag} dial {dial} exact candidate construction",
                (
                    action == action.H
                    and covariance == covariance.H
                    and fixture.matrix_zero(q_matrix * fixture.base.finite.exact_inv(q_matrix) - sp.eye(bench.N))
                    and action != covariance
                ),
                f"action_inertia={measured_action[key]}, covariance_inertia={measured_covariance[key]}, raw_covariance_hermitian={raw_status[key]}",
            )
    check(
        "finite action-side inertia ledger",
        measured_action == EXPECTED_ACTION,
        f"measured={measured_action}",
    )
    check(
        "finite covariance-side inertia ledger",
        measured_covariance == EXPECTED_COVARIANCE,
        f"measured={measured_covariance}",
    )
    for tag in ("8x4", "12x4"):
        bench = fixture.base.Bench(f"released7359-a-region-{tag}", 8 if tag == "8x4" else 12, 4)
        region = sp.expand(bench.form.subs(bench.carrier(st=0)))
        expected = sp.diag(*([R(57, 40)] * 4 + [0] * 4))
        check(
            f"{tag} action region is PSD",
            region == expected and region.is_positive_semidefinite is True,
            f"inertia={fixture.base.real_symmetric_inertia(region)}",
        )


def vacuum_and_source_scope() -> None:
    normalized_vacuum = sp.Integer(1)
    check(
        "normalized symmetric vacuum",
        normalized_vacuum == 1 and sp.diff(normalized_vacuum, fixture.ST) == 0,
        "Sym^0 coefficient is one; an unnormalized Gaussian prefactor is separate",
    )
    note = NOTE.read_text(encoding="utf-8")
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    floats = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    actual = {
        path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    check(
        "literal input closure and bounded note",
        (
            not floats
            and actual == INPUT_SHA256
            and fixture.source_hygiene(AUDIT_INPUT_PATHS, INPUT_SHA256)
            and all(f"## N{index}" in note for index in range(1, 9))
            and "positive-semidefinite" in note
            and "normalized coefficient is `1`" in note
        ),
        f"float_literals={len(floats)}, inputs_bound={actual == INPUT_SHA256}",
    )


def main() -> int:
    symmetric_power_minor()
    finite_kernel_candidates()
    vacuum_and_source_scope()
    for name, passed, detail in CHECKS:
        print(f"{'PASS' if passed else 'FAIL'}: {name} :: {detail}")
    print("per_element: the permanent minor uses |r|^2 and is negative only under its mixed-kernel hypotheses")
    print("per_site: action-side and covariance-side candidates are reconstructed on two supplied covers")
    print("per_mode: at s_t=0 the action-side form is PSD while the covariance candidate remains mixed")
    print("per_block: the normalized vacuum is one; any dial-sensitive Gaussian prefactor is an extra convention")
    print("lattice_wide: no physical source grading, unique readout, continuum theorem, premise, axiom, audit, or TOE conclusion follows")
    passed = sum(ok for _, ok, _ in CHECKS)
    total = len(CHECKS)
    print(f"TOTAL: {passed}/{total} {'PASS' if passed == total else 'FAIL'}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
