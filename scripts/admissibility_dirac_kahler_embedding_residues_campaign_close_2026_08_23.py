#!/usr/bin/env python3
"""Corrected finite orbit, metric, orientation, and multiplicity checks."""

from __future__ import annotations

import ast
import hashlib
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11 as fixture


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_DIRAC_KAHLER_EMBEDDING_RESIDUES_CAMPAIGN_CLOSE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_EMBEDDING_RESIDUES_CAMPAIGN_CLOSE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py",
    "scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_EMBEDDING_RESIDUES_CAMPAIGN_CLOSE_BOUNDED_THEOREM_NOTE_2026-08-23.md': '9b58bba35323c78dcfb1d717f767cc020e298771e86a4753876aec23cd642f51',
    'scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py': '7b91bfd85d98bada7f64196665722cc08267812fd2c5344dab8b342f236129b6',
    'scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py': '594e7032f453fec4c6791067a147d1544636ddce9567a87a3449352b5546d5f5',
    'scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py': '8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}
AUDIT_TIMEOUT_SEC = 90

R = sp.Rational
CHECKS: list[tuple[str, bool, str]] = []
EXPECTED_LEVELS = {
    0: R(3193, 2240),
    1: R(43, 35),
    2: R(3193, 2240),
    3: R(1817, 1120),
    4: R(1817, 1120),
    5: R(1817, 1120),
}
OPEN_OBLIGATIONS = (
    "multiplicity selector, quotient, or proved fiber theorem",
    "injective unital star-algebra carrier map",
    "non-vacuous physical observable preservation",
    "record-write identification",
    "ambient higher-weight treatment",
    "nondegenerate metric-ratio comparison",
)


def check(name: str, condition: bool, detail: str) -> None:
    CHECKS.append((name, bool(condition), detail))


def orbit_and_orientation() -> tuple[fixture.base.Bench, sp.Matrix, dict]:
    bench, pinned, action = fixture.constant_wide_fixture()
    translation = fixture.chart_translation(bench)
    embedding = fixture.orbit_embedding(bench, 0, 0)
    restriction = sp.expand(embedding.T * action * embedding)
    f_one = fixture.chart_character(bench, 0, 0, 1)
    f_two = fixture.chart_character(bench, 0, 0, 2)
    results = {
        "restriction": restriction,
        "beta_one": fixture.exact_scalar((f_one.H * action * f_one)[0]),
        "beta_two": fixture.exact_scalar((f_two.H * action * f_two)[0]),
        "anti_one": fixture.exact_scalar((f_one.T * action * f_one)[0]),
        "anti_two": fixture.exact_scalar((f_two.T * action * f_two)[0]),
    }
    check(
        "finite three-cycle orbit",
        (
            pinned == (0, 1)
            and translation ** 3 == sp.eye(bench.N)
            and fixture.matrix_zero(translation * embedding - embedding * fixture.P3)
            and sp.expand(embedding.T * translation * embedding) == fixture.P3
        ),
        "U E=E P3 on the chosen three-site orbit",
    )
    check(
        "conjugate-character scalar indifference",
        (
            fixture.matrix_zero(f_two - f_one.conjugate())
            and fixture.matrix_zero((translation * f_one - fixture.OMEGA * f_one).applyfunc(fixture.exact_scalar))
            and fixture.matrix_zero((translation * f_two - fixture.OMEGA ** 2 * f_two).applyfunc(fixture.exact_scalar))
            and results["beta_one"] == results["beta_two"] == R(3193, 2240)
            and results["anti_one"] == results["anti_two"] == 0
            and restriction == R(3193, 2240) * sp.eye(3)
        ),
        f"betas=({results['beta_one']},{results['beta_two']}), restriction={restriction}",
    )
    return bench, action, results


def metric_preservation(restriction: sp.Matrix) -> None:
    identity = sp.eye(3)
    scale = 2 * identity
    check(
        "commutation differs from metric preservation",
        (
            fixture.matrix_zero(scale * restriction - restriction * scale)
            and scale.det() != 0
            and sp.expand(scale.H * restriction * scale) != restriction
            and sp.expand(fixture.P3.H * restriction * fixture.P3) == restriction
            and sp.expand(fixture.P3.H * fixture.P3) == identity
        ),
        "2I is invertible and commutes with cI but is not an R-isometry; P3 is unitary",
    )
    singular = sp.zeros(3)
    singular[0, 1] = 1
    check(
        "historical matrix witness is not a basis change",
        singular.det() == 0 and fixture.matrix_zero(singular * restriction - restriction * singular),
        f"rank(e0 e1^T)={singular.rank()}",
    )


def multiplicity(bench: fixture.base.Bench, action: sp.Matrix) -> None:
    copies = tuple((time, parity) for time in range(bench.T) for parity in (0, 1))
    vectors = {
        copy: fixture.chart_character(bench, copy[0], copy[1], 1)
        for copy in copies
    }
    ledger = {
        copy: fixture.exact_scalar((vector.H * action * vector)[0])
        for copy, vector in vectors.items()
    }
    level_ledger = {time: ledger[(time, 0)] for time in range(bench.T)}
    parity_independent = all(
        ledger[(time, 0)] == ledger[(time, 1)] for time in range(bench.T)
    )
    basis = sp.Matrix.hstack(*(vectors[copy] for copy in copies))
    gram = sp.Matrix(
        len(copies),
        len(copies),
        lambda row, column: fixture.exact_scalar(
            (vectors[copies[row]].H * action * vectors[copies[column]])[0]
        ),
    )
    offdiagonal = sum(
        row != column and gram[row, column] != 0
        for row in range(len(copies))
        for column in range(len(copies))
    )
    one_r = fixture.supplied_slot_ratio(1)
    all_r = fixture.supplied_slot_ratio(len(copies))
    check(
        "twelve-copy finite ledger",
        (
            len(copies) == 12
            and parity_independent
            and level_ledger == EXPECTED_LEVELS
            and fixture.matrix_zero(basis.H * basis - sp.eye(12))
            and offdiagonal == 36
        ),
        f"levels={level_ledger}, offdiagonal_gram_entries={offdiagonal}",
    )
    check(
        "supplied additive count leaves multiplicity open",
        (
            one_r == R(1, 2)
            and fixture.supplied_q_from_ratio(one_r) == R(2, 3)
            and all_r == 6
            and fixture.supplied_q_from_ratio(all_r) == R(13, 3)
        ),
        "one selected copy and all twelve copies give different supplied arithmetic",
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
        "literal input closure and pending-fiber fence",
        (
            not floats
            and actual == INPUT_SHA256
            and fixture.source_hygiene(AUDIT_INPUT_PATHS, INPUT_SHA256)
            and len(OPEN_OBLIGATIONS) == 6
            and all(f"## N{index}" in note for index in range(1, 9))
            and "remains explicitly **pending**" in note
            and "scalar-observable indifference" in note
        ),
        f"float_literals={len(floats)}, inputs_bound={actual == INPUT_SHA256}, open_obligations={len(OPEN_OBLIGATIONS)}",
    )


def main() -> int:
    bench, action, results = orbit_and_orientation()
    metric_preservation(results["restriction"])
    multiplicity(bench, action)
    source_scope()
    for name, passed, detail in CHECKS:
        print(f"{'PASS' if passed else 'FAIL'}: {name} :: {detail}")
    print("per_element: a scalar orbit metric commutes with every matrix but is preserved only by unitary basis changes")
    print("per_site: one chosen three-site orbit carries an exact C3 module map")
    print("per_mode: conjugate characters have different translation eigenvalues and equal values only for the tested scalar restriction")
    print("per_block: multiplicity, six bridge supplies, and the historical fiber-response interpretation remain open")
    print("lattice_wide: no physical carrier equivalence, orientation elimination, campaign-close theorem, premise, axiom, audit, or TOE conclusion follows")
    passed = sum(ok for _, ok, _ in CHECKS)
    total = len(CHECKS)
    print(f"TOTAL: {passed}/{total} {'PASS' if passed == total else 'FAIL'}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
