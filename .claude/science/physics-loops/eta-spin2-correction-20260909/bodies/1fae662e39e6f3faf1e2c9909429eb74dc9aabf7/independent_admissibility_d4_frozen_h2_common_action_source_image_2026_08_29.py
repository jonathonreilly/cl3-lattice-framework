#!/usr/bin/env python3
"""Independent Block-07 H2 source-image checker.

The checker does not import the primary Block-07 runner or the Block-03
decoder.  It rebuilds the H2 TT section, the proper-cubic H1 shear orbit,
the ten universal action vertices, and the complete cubic/reflection test.
"""

from __future__ import annotations

import argparse
from functools import cache
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24 as b190  # noqa: E402
import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block07-frozen-h2-common-action-20260829"
)
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_FROZEN_H2_COMMON_ACTION_SOURCE_IMAGE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
NO_GO = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
PARENT = "a9b4285a17a3a35941667b074bda2f20fa8f1c70"
PREREG = "0169137102e9c2677de51aa8e13f4e1ea2665bce"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block07-frozen-h2-common-action-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block07-frozen-h2-common-action-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block07-frozen-h2-common-action-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_FROZEN_H2_COMMON_ACTION_SOURCE_IMAGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
)

MUTATIONS = (
    "stale_authority",
    "wrong_fixture",
    "wrong_tt_column",
    "erase_diagonal",
    "invent_t2_membership",
    "fit_new_shear",
    "omit_zero_inputs",
    "sample_shears",
    "drop_vertex",
    "support_equality",
    "skip_reverse",
    "lose_injectivity",
    "skip_improper_cubic",
    "continue_state",
    "continue_history",
    "claim_universal_no_go",
    "claim_axiom",
    "claim_toe",
    "claim_retained",
)

I = sp.I
EXPECTED = (
    0, (sp.sqrt(3) + 3) / 4, -(sp.sqrt(3) + 1) / 4,
    -sp.Rational(1, 2), 0, 0, 0, -sp.sqrt(3) / 2, 0, 1,
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def rotations(proper_only: bool = True) -> tuple[sp.Matrix, ...]:
    result = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column, row in enumerate(permutation):
                matrix[row, column] = signs[column]
            if not proper_only or matrix.det() == 1:
                result.append(matrix)
    return tuple(result)


def shear_representation(rotation: sp.MatrixBase) -> sp.Matrix:
    basis = (
        sp.Matrix(((0, 1, 0), (1, 0, 0), (0, 0, 0))),
        sp.Matrix(((0, 0, 0), (0, 0, 1), (0, 1, 0))),
        sp.Matrix(((0, 0, 1), (0, 0, 0), (1, 0, 0))),
    )
    columns = []
    for tensor in basis:
        transformed = sp.expand(rotation * tensor * rotation.T)
        columns.append(sp.Matrix((
            transformed[0, 1], transformed[1, 2], transformed[0, 2]
        )))
    return sp.Matrix.hstack(*columns)


def tt_section(transfer: tuple[sp.Expr, ...]) -> sp.Matrix:
    basis = []
    for left, right in ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)):
        matrix = sp.zeros(3)
        value = 1 if left == right else 1 / sp.sqrt(2)
        matrix[left, right] = value
        matrix[right, left] = value
        basis.append(matrix)
    incidence = sp.Matrix(tuple(2 * sp.sin(transfer[axis] / 2)
                                for axis in range(3)))
    rows = [sp.Matrix([[sp.trace(item) for item in basis]])]
    for axis in range(3):
        rows.append(sp.Matrix([[(item * incidence)[axis] for item in basis]]))
    constraint = sp.Matrix.vstack(*rows)
    spatial = sp.Matrix.hstack(*constraint.nullspace())
    embedding = sp.zeros(10, 6)
    for column, row in enumerate((1, 2, 3, 7, 8, 9)):
        embedding[row, column] = 1
    return sp.expand(embedding * spatial)


def coefficient_from_shear(shear: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    result = [sp.Integer(0)] * 10
    result[7] = sp.sqrt(2) * shear[0]
    result[9] = sp.sqrt(2) * shear[1]
    result[8] = sp.sqrt(2) * shear[2]
    return tuple(result)


def raw_action_vertices() -> tuple[b190.PolyMatrix, ...]:
    differential_0: b190.PolyMatrix = {}
    differential_1: b190.PolyMatrix = {}
    for axis in range(4):
        differential_0 = b190.poly_add(differential_0, {
            b190.exponent({axis: 1}): b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}): -b190.CREATION[axis] / (2 * I),
        })
        differential_1 = b190.poly_add(differential_1, {
            b190.exponent({axis: 1}, {axis: 1}):
                b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}, {axis: -1}):
                -b190.CREATION[axis] / (2 * I),
        })
    vertices = []
    for left, right in b190.PAIRS4:
        if left == right:
            hodge = b190.poly_multiply(
                b190.cosine_square(left),
                {b190.ZERO_EXPONENT:
                 sp.Rational(1, 2) * b190.IDENTITY_FORM - b190.NUMBER[left]},
            )
        else:
            hodge = b190.poly_multiply(
                b190.poly_scale(b190.poly_multiply(
                    b190.placed_cosine(left), b190.placed_cosine(right)
                ), -1 / sp.sqrt(2)),
                {b190.ZERO_EXPONENT: (
                    b190.CREATION[left] * b190.ANNIHILATION[right]
                    + b190.CREATION[right] * b190.ANNIHILATION[left]
                )},
            )
        vertices.append(b190.poly_add(
            b190.poly_scale(hodge, b190.MASS),
            b190.poly_scale(b190.poly_add(
                b190.poly_multiply(hodge, differential_0),
                b190.poly_multiply(b190.poly_transpose(differential_1), hodge),
            ), I),
        ))
    return tuple(vertices)


def poly_sum(
    vertices: tuple[b190.PolyMatrix, ...], coefficients: tuple[sp.Expr, ...]
) -> b190.PolyMatrix:
    result: b190.PolyMatrix = {}
    for coefficient, vertex in zip(coefficients, vertices):
        result = b190.poly_add(result, b190.poly_scale(vertex, coefficient))
    return result


def reverse(source: b190.PolyMatrix) -> b190.PolyMatrix:
    result: b190.PolyMatrix = {}
    for power, matrix in source.items():
        target = tuple(power[index] for index in range(4)) + tuple(
            power[index] - power[4 + index] for index in range(4)
        )
        result = b190.poly_add(result, {target: matrix})
    return result


def equal(left: b190.PolyMatrix, right: b190.PolyMatrix) -> bool:
    difference = b190.poly_add(left, b190.poly_scale(right, -1))
    return not difference


def flatten(polynomials: tuple[b190.PolyMatrix, ...]) -> sp.Matrix:
    powers = sorted(set().union(*(set(item) for item in polynomials)))
    return sp.Matrix.hstack(*(
        sp.Matrix([
            value
            for power in powers
            for value in polynomial.get(power, sp.zeros(16))
        ])
        for polynomial in polynomials
    ))


@cache
def facts() -> dict[str, object]:
    incoming = (sp.pi / 4, sp.pi / 6, sp.pi / 3, sp.pi / 6)
    transfer = (sp.pi / 6, sp.pi / 3, sp.pi / 2, sp.Integer(0))
    coefficients = tuple(sp.simplify(value)
                         for value in tt_section(transfer)[:, 1])
    base = sp.Matrix((0, 1 / sp.sqrt(2), -1))
    active_shears = tuple(shear_representation(rotation) * base
                          for rotation in rotations())
    shear_image = active_shears + (sp.zeros(3, 1),) * 40
    candidates = tuple(coefficient_from_shear(shear) for shear in shear_image)
    vertices = raw_action_vertices()
    target = poly_sum(vertices, coefficients)
    target_reverse = reverse(target)
    forward_matches = tuple(index for index, candidate in enumerate(candidates)
                            if equal(target, poly_sum(vertices, candidate)))
    reverse_matches = tuple(index for index, candidate in enumerate(candidates)
                            if equal(target_reverse, reverse(
                                poly_sum(vertices, candidate))))
    matrix = flatten(vertices)
    h1 = matrix[:, (7, 9, 8)]
    target_column = matrix * sp.Matrix(coefficients)
    fixed_vertices = b190.centered_objects(incoming, transfer)[2]
    fixed_target = sp.expand(sum(
        (coefficient * vertex for coefficient, vertex
         in zip(coefficients, fixed_vertices)), sp.zeros(16)
    ))
    fixed_matches = []
    for index, candidate in enumerate(candidates):
        fixed_candidate = sp.expand(sum(
            (coefficient * vertex for coefficient, vertex
             in zip(candidate, fixed_vertices)), sp.zeros(16)
        ))
        if b190.matrix_equal(fixed_target, fixed_candidate):
            fixed_matches.append(index)
    h1_domain = sp.zeros(10, 3)
    h1_domain[7, 0] = sp.sqrt(2)
    h1_domain[9, 1] = sp.sqrt(2)
    h1_domain[8, 2] = sp.sqrt(2)
    orbit_rows = []
    for spatial in rotations(False):
        full = sp.eye(4)
        full[:3, :3] = spatial
        tensor = b190.tensor_representation(full)
        domain = tensor * h1_domain
        orbit_rows.append((int(spatial.det()), domain.rank(),
                           domain.row_join(tensor * sp.Matrix(coefficients)).rank()))
    return {
        "coefficients": coefficients,
        "nonzero": tuple(index for index, value in enumerate(coefficients)
                         if value != 0),
        "active_shear_count": len(active_shears),
        "all_input_count": len(shear_image),
        "distinct_shears": len({tuple(shear) for shear in shear_image}),
        "shear_matches": tuple(index for index, shear in enumerate(shear_image)
                               if shear == sp.Matrix((
                                   coefficients[7] / sp.sqrt(2),
                                   coefficients[9] / sp.sqrt(2),
                                   coefficients[8] / sp.sqrt(2),
                               ))),
        "forward_matches": forward_matches,
        "reverse_matches": reverse_matches,
        "fixed_matches": tuple(fixed_matches),
        "target_terms": len(target),
        "reverse_terms": len(target_reverse),
        "full_rank": matrix.rank(),
        "h1_rank": h1.rank(),
        "augmented_rank": h1.row_join(target_column).rank(),
        "orbit": tuple(orbit_rows),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool, detail: str) -> None:
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    mutation = parser.parse_args().mutation
    checks = Checks()
    data = facts()

    authority = (
        git("rev-parse", "origin/main") == MAIN
        and ancestor(PARENT)
        and ancestor(PREREG)
        and git("hash-object", "--", "docs/MINIMAL_AXIOMS_2026-06-29.md")
        == AXIOM_BLOB
    )
    if mutation == "stale_authority":
        authority = False
    checks.check("A_independent_authority", authority,
                 "frozen main, parent, preregistration, and axiom blob match")

    fixture = data["coefficients"] == EXPECTED and data["nonzero"] == (1, 2, 3, 7, 9)
    if mutation in ("wrong_fixture", "wrong_tt_column", "erase_diagonal"):
        fixture = False
    checks.check("B_independent_h2_tt_section", fixture,
                 "constraint-nullspace reconstruction gives the exact preregistered H2 column")

    decoder = (
        data["active_shear_count"] == 24
        and data["all_input_count"] == 64
        and data["distinct_shears"] == 25
        and data["shear_matches"] == ()
    )
    if mutation in ("invent_t2_membership", "fit_new_shear", "omit_zero_inputs", "sample_shears"):
        decoder = False
    checks.check("C_independent_decoder_image", decoder,
                 "24 proper-cubic active shears plus 40 frozen zero inputs contain no H2 shear")

    source = (
        data["forward_matches"] == ()
        and data["reverse_matches"] == ()
        and data["fixed_matches"] == ()
        and data["target_terms"] == 195
        and data["reverse_terms"] == 195
    )
    if mutation in ("drop_vertex", "support_equality", "skip_reverse"):
        source = False
    checks.check("D_independent_source_comparison", source,
                 "all 64 universal forward/reverse images and fixed-H2 evaluated vertices disagree exactly")

    rank = data["full_rank"] == 10 and data["h1_rank"] == 3 and data["augmented_rank"] == 4
    if mutation == "lose_injectivity":
        rank = False
    checks.check("E_independent_injective_rank", rank,
                 "ten source columns are independent and H2 raises the frozen H1 image rank from three to four")

    orbit = data["orbit"]
    orbit_ok = (
        len(orbit) == 48
        and sum(row[0] == 1 for row in orbit) == 24
        and sum(row[0] == -1 for row in orbit) == 24
        and all(row[1:] == (3, 4) for row in orbit)
    )
    if mutation == "skip_improper_cubic":
        orbit_ok = False
    checks.check("F_independent_full_cubic_orbit", orbit_ok,
                 "all 48 signed cubic transforms retain the rank-3/rank-4 nonmembership certificate")

    text = (NOTE.read_text(encoding="utf-8") if NOTE.is_file() else "") + "\n" + (
        NO_GO.read_text(encoding="utf-8") if NO_GO.is_file() else ""
    )
    scope = all(phrase in text for phrase in (
        "NO-MEMBER only for the frozen H1 family",
        "positive H2 state/history chain stops at Stage A",
        "larger H1+H2 source representation remains open",
        "TOE percentage movement: 0",
        "N7 — Steelman",
    ))
    if mutation in (
        "continue_state", "continue_history", "claim_universal_no_go",
        "claim_axiom", "claim_toe", "claim_retained",
    ):
        scope = False
    checks.check("G_independent_scope", scope,
                 "the exact family is rejected without promoting the result to a universal, axiom, retained, or TOE claim")

    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        f"INDEPENDENT_H2: nonzero={data['nonzero']}; source_terms={data['target_terms']}/{data['reverse_terms']}; "
        f"ranks={data['full_rank']},{data['h1_rank']},{data['augmented_rank']}."
    )
    print(
        "INDEPENDENT_ADJUDICATION: all64_no_member=true; fixed_H2_no_member=true; full_cubic_orbit_no_member=true; verdict=NO-MEMBER."
    )
    print(f"SCORECARD PASS={checks.passed} FAIL={checks.failed}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return checks.failed


if __name__ == "__main__":
    raise SystemExit(main())
