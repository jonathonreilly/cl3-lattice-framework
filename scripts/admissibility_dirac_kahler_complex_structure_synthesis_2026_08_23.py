#!/usr/bin/env python3
"""Corrected finite complex-structure and determinant-realification checks."""

from __future__ import annotations

import ast
import hashlib
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11 as fixture


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_BOUNDED_THEOREM_NOTE_2026-08-23.md"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py",
    "scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_BOUNDED_THEOREM_NOTE_2026-08-23.md': 'b7fe086354536f2d456c710c160066a410f523e71f2e103f264077dea4b8ef14',
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


def check(name: str, condition: bool, detail: str) -> None:
    CHECKS.append((name, bool(condition), detail))


def exact_complex_cell() -> None:
    bench, pinned, action = fixture.constant_wide_fixture()
    translation = fixture.chart_translation(bench)
    embedding = fixture.orbit_embedding(bench, 0, 0)
    restriction = sp.expand(embedding.T * action * embedding)
    expected = R(3193, 2240) * sp.eye(3)
    f_one = fixture.chart_character(bench, 0, 0, 1)
    f_two = fixture.chart_character(bench, 0, 0, 2)
    beta_one = fixture.exact_scalar((f_one.H * action * f_one)[0])
    beta_two = fixture.exact_scalar((f_two.H * action * f_two)[0])
    antilinear = (
        fixture.exact_scalar((f_one.T * action * f_one)[0]),
        fixture.exact_scalar((f_two.T * action * f_two)[0]),
    )
    check(
        "12x6 finite orbit and complex characters",
        (
            pinned == (0, 1)
            and action.shape == (36, 36)
            and translation ** 3 == sp.eye(36)
            and fixture.matrix_zero(translation * embedding - embedding * fixture.P3)
            and restriction == expected
            and fixture.matrix_zero(f_two - f_one.conjugate())
            and beta_one == beta_two == R(3193, 2240)
            and antilinear == (0, 0)
        ),
        f"restriction={restriction}, betas=({beta_one},{beta_two}), antilinear={antilinear}",
    )

    determinant = sp.expand(restriction.det())
    realified_determinant = sp.expand(fixture.realify(restriction).det())
    norm_squared = sp.expand(determinant * sp.conjugate(determinant))
    gaussian_pair = sp.pi ** 6 / norm_squared
    check(
        "realification has the positive determinant power",
        realified_determinant == norm_squared and determinant != 0,
        f"det_R={realified_determinant}, |det_C|^2={norm_squared}",
    )
    check(
        "paired Gaussian uses reciprocal realified determinant",
        sp.simplify(gaussian_pair - sp.pi ** 6 / realified_determinant) == 0,
        "Z(Q)Z(Q^dagger)=pi^(2N)/det Real(Q) for N=3",
    )

    j_complex = sp.Matrix([[0, -1], [1, 0]])
    check(
        "supplied complex structure",
        j_complex ** 2 == -sp.eye(2) and j_complex.T * j_complex == sp.eye(2),
        f"J^2={j_complex ** 2}",
    )


def supplied_counting_comparison() -> None:
    one_complex_r = fixture.supplied_slot_ratio(1)
    two_real_r = fixture.supplied_slot_ratio(2)
    values = (
        one_complex_r,
        fixture.supplied_q_from_ratio(one_complex_r),
        two_real_r,
        fixture.supplied_q_from_ratio(two_real_r),
    )
    check(
        "supplied slot comparison",
        values == (R(1, 2), R(2, 3), sp.Integer(1), sp.Integer(1)),
        f"(r1,q1,r2,q2)={values}; this map is supplied, not derived",
    )


def source_scope() -> None:
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
            and "role assignment remains an interpretation" in note
            and "do not derive a unique physical slot count" in note
        ),
        f"float_literals={len(floats)}, inputs_bound={actual == INPUT_SHA256}",
    )


def main() -> int:
    exact_complex_cell()
    supplied_counting_comparison()
    source_scope()
    for name, passed, detail in CHECKS:
        print(f"{'PASS' if passed else 'FAIL'}: {name} :: {detail}")
    print("per_element: determinant realification and the reciprocal Gaussian normalization are distinguished exactly")
    print("per_site: one supplied 12x6 orbit has the displayed scalar sesquilinear restriction")
    print("per_mode: the one-complex-slot arithmetic is a supplied comparison, not a physical derivation")
    print("per_block: the historical role reading remains interpretive and no holonomy arm is executed here")
    print("lattice_wide: no probability law, carrier selector, all-lattice theorem, premise, axiom, audit, or TOE conclusion follows")
    passed = sum(ok for _, ok, _ in CHECKS)
    total = len(CHECKS)
    print(f"TOTAL: {passed}/{total} {'PASS' if passed == total else 'FAIL'}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
