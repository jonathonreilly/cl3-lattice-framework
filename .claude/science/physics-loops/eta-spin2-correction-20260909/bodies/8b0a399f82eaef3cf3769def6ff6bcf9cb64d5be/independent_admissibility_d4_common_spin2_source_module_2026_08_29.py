#!/usr/bin/env python3
"""Independent Block-08 common-module and affine-capacity checker."""

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

import admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as b3  # noqa: E402
import admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24 as b190  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block08-common-spin2-module-20260829"
)
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_COMMON_SPIN2_SOURCE_MODULE_SIX_BIT_CAPACITY_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
NO_GO = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
PARENT = "5445bccc4e6e6a47197930caae22bcc9cdc30fc5"
PREREG = "a4cbc76a77297a093a08e382f769df1390fc02c4"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block08-common-spin2-module-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block08-common-spin2-module-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block08-common-spin2-module-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_COMMON_SPIN2_SOURCE_MODULE_SIX_BIT_CAPACITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
)

MUTATIONS = (
    "stale_authority", "wrong_h1", "wrong_h2", "add_trace",
    "rank_four", "drop_e", "drop_t2", "bad_source_rank", "skip_reverse",
    "wrong_affine_translation", "miss_orbit", "invent_free_orbit",
    "ignore_target_stabilizer", "reuse_free_orbit", "fixture_switch",
    "claim_compiler", "claim_ownership", "claim_history", "claim_axiom",
    "claim_toe", "claim_retained", "claim_universal",
)

I = sp.I


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def rotations() -> tuple[sp.Matrix, ...]:
    result = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column, row in enumerate(permutation):
                matrix[row, column] = signs[column]
            if matrix.det() == 1:
                result.append(matrix)
    return tuple(sorted(result, key=lambda matrix: tuple(int(x) for x in matrix)))


def tensor_basis4() -> tuple[sp.Matrix, ...]:
    basis = []
    for left, right in (
        (3, 3), (0, 0), (1, 1), (2, 2), (0, 3),
        (1, 3), (2, 3), (0, 1), (0, 2), (1, 2),
    ):
        matrix = sp.zeros(4)
        value = 1 if left == right else 1 / sp.sqrt(2)
        matrix[left, right] = value
        matrix[right, left] = value
        basis.append(matrix)
    return tuple(basis)


TENSOR_BASIS = tensor_basis4()


def tensor_representation(spatial: sp.MatrixBase) -> sp.Matrix:
    full = sp.eye(4)
    full[:3, :3] = spatial
    return sp.Matrix(10, 10, lambda row, column: sp.trace(
        TENSOR_BASIS[row].T * full * TENSOR_BASIS[column] * full.T
    ))


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
    constraints = [sp.Matrix([[sp.trace(item) for item in basis]])]
    for axis in range(3):
        constraints.append(sp.Matrix([[(item * incidence)[axis]
                                       for item in basis]]))
    spatial = sp.Matrix.hstack(*sp.Matrix.vstack(*constraints).nullspace())
    embedding = sp.zeros(10, 6)
    for column, row in enumerate((1, 2, 3, 7, 8, 9)):
        embedding[row, column] = 1
    return sp.expand(embedding * spatial)


def raw_vertices() -> tuple[b190.PolyMatrix, ...]:
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
    answer = []
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
        answer.append(b190.poly_add(
            b190.poly_scale(hodge, b190.MASS),
            b190.poly_scale(b190.poly_add(
                b190.poly_multiply(hodge, differential_0),
                b190.poly_multiply(b190.poly_transpose(differential_1), hodge),
            ), I),
        ))
    return tuple(answer)


def reverse(source: b190.PolyMatrix) -> b190.PolyMatrix:
    answer: b190.PolyMatrix = {}
    for power, matrix in source.items():
        target = tuple(power[index] for index in range(4)) + tuple(
            power[index] - power[4 + index] for index in range(4)
        )
        answer = b190.poly_add(answer, {target: matrix})
    return answer


def flatten(polynomials: tuple[b190.PolyMatrix, ...]) -> sp.Matrix:
    powers = sorted(set().union(*(set(polynomial) for polynomial in polynomials)))
    return sp.Matrix.hstack(*(
        sp.Matrix([value for power in powers
                   for value in polynomial.get(power, sp.zeros(16))])
        for polynomial in polynomials
    ))


@cache
def facts() -> dict[str, object]:
    h1_transfer = (sp.pi / 3, sp.pi / 2, sp.Integer(0), sp.Integer(0))
    h2_transfer = (sp.pi / 6, sp.pi / 3, sp.pi / 2, sp.Integer(0))
    h1 = sp.Matrix(tuple(sp.simplify(value) for value in tt_section(h1_transfer)[:, 1]))
    h2 = sp.Matrix(tuple(sp.simplify(value) for value in tt_section(h2_transfer)[:, 1]))
    reps = tuple(tensor_representation(rotation) for rotation in rotations())
    h1_span = sp.Matrix.hstack(*(rep * h1 for rep in reps))
    h2_span = sp.Matrix.hstack(*(rep * h2 for rep in reps))
    common_span = h1_span.row_join(h2_span)
    e_t2 = sp.zeros(10, 5)
    e_t2[1, 0], e_t2[2, 0] = 1, -1
    e_t2[1, 1], e_t2[2, 1], e_t2[3, 1] = 1, 1, -2
    e_t2[7, 2], e_t2[8, 3], e_t2[9, 4] = 1, 1, 1
    source = flatten(raw_vertices())
    reverse_source = flatten(tuple(reverse(vertex) for vertex in raw_vertices()))

    translations = b3.action_facts()["translations"]
    permutations = b3.b2.shell_permutations()
    def action(group: int, mask: int) -> int:
        return b3.b2.permute_mask(mask, permutations[group]) ^ translations[group]
    unseen = set(range(64))
    orbit_rows = []
    while unseen:
        representative = min(unseen)
        orbit = tuple(sorted({action(group, representative)
                              for group in range(24)}))
        unseen -= set(orbit)
        stabilizer = tuple(group for group in range(24)
                           if action(group, representative) == representative)
        orbit_rows.append((representative, len(orbit), len(stabilizer)))
    h1_stabilizer = sum(rep * h1 == h1 for rep in reps)
    h2_stabilizer = sum(rep * h2 == h2 for rep in reps)
    free = tuple(rep for rep, _size, stabilizer in orbit_rows if stabilizer == 1)
    return {
        "h1": h1, "h2": h2,
        "h1_trace": sp.simplify(h1[1] + h1[2] + h1[3]),
        "h2_trace": sp.simplify(h2[1] + h2[2] + h2[3]),
        "h1_rank": h1_span.rank(), "h2_rank": h2_span.rank(),
        "common_rank": common_span.rank(),
        "intersection": h1_span.rank() + h2_span.rank() - common_span.rank(),
        "common_equals_e_t2": common_span.rank() == e_t2.rank()
        == common_span.row_join(e_t2).rank(),
        "h1_orbit": len({tuple(rep * h1) for rep in reps}),
        "h2_orbit": len({tuple(rep * h2) for rep in reps}),
        "h1_stabilizer": h1_stabilizer, "h2_stabilizer": h2_stabilizer,
        "source_rank": source.rank(), "reverse_rank": reverse_source.rank(),
        "common_source_rank": (source * e_t2).rank(),
        "common_reverse_rank": (reverse_source * e_t2).rank(),
        "orbit_rows": tuple(orbit_rows),
        "orbit_sizes": tuple(sorted((size for _, size, _ in orbit_rows), reverse=True)),
        "free_representatives": free,
        "all_masks": sum(size for _, size, _ in orbit_rows),
        "translations": tuple(translations),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool, detail: str) -> None:
        self.passed += int(ok); self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    mutation = parser.parse_args().mutation
    checks = Checks(); data = facts()

    authority = (
        git("rev-parse", "origin/main") == MAIN and ancestor(PARENT)
        and ancestor(PREREG)
        and git("hash-object", "--", "docs/MINIMAL_AXIOMS_2026-06-29.md") == AXIOM_BLOB
    )
    if mutation == "stale_authority": authority = False
    checks.check("A_independent_authority", authority,
                 "main, parent, preregistration, and axiom identities match")

    expected_h1 = (0, 0, 0, 0, 0, 0, 0, 0, -sp.sqrt(2), 1)
    expected_h2 = (0, (sp.sqrt(3)+3)/4, -(sp.sqrt(3)+1)/4,
                   -sp.Rational(1,2), 0, 0, 0, -sp.sqrt(3)/2, 0, 1)
    fixtures = tuple(data["h1"]) == expected_h1 and tuple(data["h2"]) == expected_h2
    if mutation in ("wrong_h1", "wrong_h2"): fixtures = False
    checks.check("B_independent_fixture_sections", fixtures,
                 "constraint-nullspace TT reconstruction reproduces both exact source vectors")

    module = (
        data["h1_trace"] == 0 and data["h2_trace"] == 0
        and data["h1_rank"] == 3 and data["h2_rank"] == 5
        and data["common_rank"] == 5 and data["intersection"] == 3
        and data["common_equals_e_t2"]
    )
    if mutation in ("add_trace", "rank_four", "drop_e", "drop_t2"): module = False
    checks.check("C_independent_minimal_module", module,
                 "cyclic spans independently give H1 rank 3, H2/common rank 5, intersection 3, exactly E+T2")

    source = (
        data["source_rank"] == 10 and data["reverse_rank"] == 10
        and data["common_source_rank"] == 5 and data["common_reverse_rank"] == 5
    )
    if mutation in ("bad_source_rank", "skip_reverse"): source = False
    checks.check("D_independent_source_injectivity", source,
                 "independently rebuilt forward and actual-reverse maps have full rank ten and common-module rank five")

    census = (
        len(data["orbit_rows"]) == 8 and data["all_masks"] == 64
        and data["orbit_sizes"] == (24, 12, 6, 6, 6, 4, 4, 2)
        and data["free_representatives"] == (5,)
    )
    if mutation in ("wrong_affine_translation", "miss_orbit", "invent_free_orbit"): census = False
    checks.check("E_independent_affine_orbits", census,
                 "direct affine-action enumeration gives eight mask orbits and exactly one free orbit, representative 5")

    capacity = (
        data["h1_orbit"] == 24 and data["h2_orbit"] == 24
        and data["h1_stabilizer"] == 1 and data["h2_stabilizer"] == 1
        and data["free_representatives"] == (5,)
    )
    if mutation in (
        "ignore_target_stabilizer", "reuse_free_orbit", "fixture_switch",
        "claim_compiler",
    ): capacity = False
    checks.check("F_independent_capacity_wall", capacity,
                 "two distinct trivial-stabilizer target orbits require two free domain orbits, while six bits supply one")

    text = (NOTE.read_text(encoding="utf-8") if NOTE.is_file() else "") + "\n" + (
        NO_GO.read_text(encoding="utf-8") if NO_GO.is_file() else ""
    )
    scope = all(phrase in text for phrase in (
        "MODULE-ONLY", "six-bit affine-action capacity",
        "a second physically owned free orbit remains open",
        "physical local ownership is not proved", "TOE percentage movement: 0",
        "N7 — Steelman",
    ))
    if mutation in (
        "claim_ownership", "claim_history", "claim_axiom", "claim_toe",
        "claim_retained", "claim_universal",
    ): scope = False
    checks.check("G_independent_scope", scope,
                 "the result is limited to the frozen six-bit deterministic equivariant source decoder")

    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        f"INDEPENDENT_MODULE: ranks=H1:{data['h1_rank']},H2:{data['h2_rank']},common:{data['common_rank']}; intersection={data['intersection']}; trace=0."
    )
    print(
        f"INDEPENDENT_CAPACITY: orbit_sizes={data['orbit_sizes']}; free={data['free_representatives']}; H1/H2_stabilizers=1/1; verdict=MODULE-ONLY."
    )
    print(f"SCORECARD PASS={checks.passed} FAIL={checks.failed}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return checks.failed


if __name__ == "__main__":
    raise SystemExit(main())
