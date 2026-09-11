#!/usr/bin/env python3
"""Corrected finite shear, mirror, transport, and evidence-scope checks."""

from __future__ import annotations

import ast
import hashlib
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11 as fixture


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py",
    "scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
INPUT_SHA256 = {
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_MIRROR_INTERFERENCE_BOUNDED_THEOREM_NOTE_2026-08-23.md': '6279ab719634de14e2be2eedfd29054c72697096f710278233002a0322bd076d',
    'scripts/admissibility_dirac_kahler_released7359_a_fixtures_2026_09_11.py': '7b91bfd85d98bada7f64196665722cc08267812fd2c5344dab8b342f236129b6',
    'scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py': '594e7032f453fec4c6791067a147d1544636ddce9567a87a3449352b5546d5f5',
    'scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py': '8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2',
    'docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md': '9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py': '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37',
}
AUDIT_TIMEOUT_SEC = 150

R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
CHECKS: list[tuple[str, bool, str]] = []
EXPECTED_AMBIENT = {"8x4": 64, "12x4": 96}
EXPECTED_PINNED = {"8x4": 32, "12x4": 64}
EXPECTED_COMMUTATOR = {"8x4": (16, 64, 72), "12x4": (32, 96, 112)}
EXPECTED_TRANSPOSE = {"8x4": (16, 64, 72), "12x4": (24, 104, 116)}
EXPECTED_SX_CENSUS = {
    "8x4": {(1, 0): 8, (1, 2): 8},
    "12x4": {(1, 0): 16, (1, 2): 16},
}
EXPECTED_ST_CENSUS = {
    "8x4": {(0, 1): 16, (1, 0): 32, (2, 1): 16},
    "12x4": {(0, 1): 16, (1, 0): 48, (2, 1): 32},
}


def check(name: str, condition: bool, detail: str) -> None:
    CHECKS.append((name, bool(condition), detail))


def mirror_profiles() -> dict[str, fixture.base.Bench]:
    benches: dict[str, fixture.base.Bench] = {}
    for tag, cover_t, lx in fixture.COVER_EXTENTS:
        bench = fixture.base.Bench(f"released7359-a-mirror-{tag}", cover_t, lx)
        benches[tag] = bench

        flat = fixture.carrier_field(bench, lambda _t, _x: ZERO, lambda _t, _x: ONE)
        flat_hodge = fixture.hodge_from(bench, flat)
        check(
            f"{tag} flat mirror control",
            (
                flat_hodge == sp.eye(bench.N)
                and fixture.matrix_zero(fixture.commutator_defect(bench, flat_hodge))
                and fixture.matrix_zero(fixture.transpose_defect(bench, flat_hodge))
            ),
            "zero shear and unit volume pass both finite tests",
        )

        volume = fixture.carrier_field(
            bench,
            lambda _t, _x: ZERO,
            lambda _t, x: fixture.VOLUME_PROFILE[x % 4],
        )
        volume_hodge = fixture.hodge_from(bench, volume)
        diagonal = tuple(sp.expand(volume_hodge[index, index]) for index in range(4))
        check(
            f"{tag} non-flat volume control",
            (
                diagonal == fixture.VOLUME_DIAGONAL
                and all(
                    volume_hodge[row, column] == 0
                    for row in range(bench.N)
                    for column in range(bench.N)
                    if row != column
                )
                and all(volume_hodge[index, index] == fixture.VOLUME_DIAGONAL[index % 4] for index in range(bench.N))
                and fixture.matrix_zero(fixture.commutator_defect(bench, volume_hodge))
                and fixture.matrix_zero(fixture.transpose_defect(bench, volume_hodge))
            ),
            f"repeating_diagonal={diagonal}",
        )

        ambient = fixture.carrier_field(
            bench, lambda _t, _x: fixture.AMBIENT_SIGMA, lambda _t, _x: ONE
        )
        ambient_hodge = fixture.hodge_from(bench, ambient)
        ambient_defect = fixture.commutator_defect(bench, ambient_hodge)
        pinned = fixture.carrier_field(
            bench,
            lambda time, _x: ZERO if time in fixture.PINNED_LEVELS else fixture.AMBIENT_SIGMA,
            lambda _t, _x: ONE,
        )
        pinned_defect = fixture.commutator_defect(bench, fixture.hodge_from(bench, pinned))
        check(
            f"{tag} tested shear profiles",
            (
                fixture.nnz(ambient_defect) == EXPECTED_AMBIENT[tag]
                and fixture.nnz(pinned_defect) == EXPECTED_PINNED[tag]
                and fixture.value_set(ambient_defect) == {R(-15, 64), R(15, 64)}
                and fixture.value_set(pinned_defect) == {R(-15, 64), R(15, 64)}
            ),
            f"ambient={fixture.nnz(ambient_defect)}, pinned={fixture.nnz(pinned_defect)}",
        )

        moduli = {}
        for time, space in bench.fx.CELLS:
            moduli[bench.fx.NU[(time, space)]] = ONE
            moduli[bench.fx.MU[(time, space)]] = ONE
            moduli[bench.fx.A[(time, space)]] = ONE
            moduli[bench.fx.B[(time, space)]] = R(-15, 16) if time == 0 else ZERO
        pure_b = fixture.commutator_defect(bench, fixture.hodge_from_moduli(bench, moduli))
        one_level = fixture.carrier_field(
            bench,
            lambda time, _x: fixture.AMBIENT_SIGMA if time == 0 else ZERO,
            lambda _t, _x: ONE,
        )
        physical = fixture.commutator_defect(bench, fixture.hodge_from(bench, one_level))
        check(
            f"{tag} single-level accounting",
            fixture.nnz(pure_b) == 16 and fixture.nnz(physical) == 24,
            f"pure_b={fixture.nnz(pure_b)}, physical_profile={fixture.nnz(physical)}",
        )
    return benches


def transport_profiles(benches: dict[str, fixture.base.Bench]) -> None:
    for tag, bench in benches.items():
        pinned = fixture.carrier_field(
            bench,
            lambda time, _x: ZERO if time in fixture.PINNED_LEVELS else fixture.AMBIENT_SIGMA,
            lambda _t, _x: ONE,
        )
        symbolic = fixture.connection_from(bench, pinned)

        def at(sx, st):
            return sp.expand(symbolic.subs({fixture.SX: sx, fixture.ST: st}))

        sx_value = fixture.AMBIENT_SIGMA
        st_value = R(1, 2)
        unit_sx = fixture.commutator_defect(bench, at(sx_value, ZERO))
        unit_st = fixture.commutator_defect(bench, at(ZERO, st_value))
        combined = fixture.commutator_defect(bench, at(sx_value, st_value))
        transpose = tuple(
            fixture.nnz(fixture.transpose_defect(bench, at(sx, st)))
            for sx, st in (
                (sx_value, ZERO),
                (ZERO, st_value),
                (sx_value, st_value),
            )
        )
        commutator = (
            fixture.nnz(unit_sx), fixture.nnz(unit_st), fixture.nnz(combined)
        )
        check(
            f"{tag} exact transport family",
            (
                fixture.matrix_zero(combined - unit_sx - unit_st)
                and fixture.hop_census(bench, unit_sx) == EXPECTED_SX_CENSUS[tag]
                and fixture.hop_census(bench, unit_st) == EXPECTED_ST_CENSUS[tag]
                and commutator == EXPECTED_COMMUTATOR[tag]
                and transpose == EXPECTED_TRANSPOSE[tag]
            ),
            f"commutator={commutator}, transpose={transpose}",
        )

        action_zero = fixture.action_from(bench, pinned, st=ZERO)
        action_quarter = fixture.action_from(bench, pinned, st=R(1, 4))
        herm_zero = sp.expand((action_zero + action_zero.H) / 2)
        herm_quarter = sp.expand((action_quarter + action_quarter.H) / 2)
        det_zero = fixture.base.finite.dm_det(action_zero)
        det_quarter = fixture.base.finite.dm_det(action_quarter)
        check(
            f"{tag} finite candidate-family contrast",
            (
                herm_zero == herm_quarter
                and det_zero != 0
                and det_quarter != 0
                and sp.expand(det_zero * sp.conjugate(det_zero))
                != sp.expand(det_quarter * sp.conjugate(det_quarter))
                and sp.Integer(1) == sp.Integer(1)
            ),
            "1/det Herm(Q) and a constant are dial-blind; determinant modulus changes",
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
        "literal input closure and historical-interference fence",
        (
            not floats
            and actual == INPUT_SHA256
            and fixture.source_hygiene(AUDIT_INPUT_PATHS, INPUT_SHA256)
            and all(f"## N{index}" in note for index in range(1, 9))
            and "did **not** execute the advertised point `(1/3,1/4)`" in note
            and "preserved as historical cache evidence" in " ".join(note.split())
        ),
        f"float_literals={len(floats)}, inputs_bound={actual == INPUT_SHA256}",
    )


def main() -> int:
    benches = mirror_profiles()
    transport_profiles(benches)
    source_scope()
    for name, passed, detail in CHECKS:
        print(f"{'PASS' if passed else 'FAIL'}: {name} :: {detail}")
    print("per_element: rQr=Q^T is the antiunitary condition; the commutator test is retained only as a comparison")
    print("per_site: flat and one non-flat volume profile pass, while the separately tested shear profiles fail")
    print("per_mode: transport support counts are exact for two finite extents and differ across them")
    print("per_block: candidate function families do not select a unique readout; interference brackets remain historical")
    print("lattice_wide: no carrier classification, OS no-go, physical interference theorem, premise, axiom, audit, or TOE conclusion follows")
    passed = sum(ok for _, ok, _ in CHECKS)
    total = len(CHECKS)
    print(f"TOTAL: {passed}/{total} {'PASS' if passed == total else 'FAIL'}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
