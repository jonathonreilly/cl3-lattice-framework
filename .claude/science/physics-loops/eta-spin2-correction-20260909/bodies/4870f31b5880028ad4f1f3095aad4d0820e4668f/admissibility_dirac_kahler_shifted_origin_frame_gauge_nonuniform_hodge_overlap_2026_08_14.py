#!/usr/bin/env python3
"""Block 105: shifted-origin frame gauge and overlap-Hodge repair.

This runner tests the exact one-site staggered shift action on the Block 104
Dirac--Kahler carrier, proves the fixed-origin/nonuniform-Hodge obstruction,
and executes a positive translation-covariant overlapping-cell Hodge repair
on an exact 4x4 fine torus.  A common global nilpotent differential, the
actual ADM/history link, reflection positivity, and TOE closure remain open.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_"
    "HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_"
    "LORENTZ_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_wick_phase_fine_site_staggered_os_"
    "lorentz_boundary_2026_08_14.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_wick_phase_fine_site_"
    "staggered_os_lorentz_boundary_2026_08_14.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_LORENTZ_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_wick_phase_fine_site_staggered_os_lorentz_boundary_2026_08_14.py",
    "logs/runner-cache/admissibility_dirac_kahler_wick_phase_fine_site_staggered_os_lorentz_boundary_2026_08_14.txt",
)

CURRENT_MAIN = "43ba5587944ffe0f43df10864c8348a99c17517b"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_COMMIT = "7fe07db6c03fad1191893c942f708c5cb9a54c43"
PARENT_NOTE_BLOB = "3622f91ca2fc505fbb441c4b474450b0c9fb28c3"
PARENT_RUNNER_BLOB = "d0b26299319b7d861510f124c65d44143b1e1a32"
PARENT_CACHE_BLOB = "8bd3c6fbe15c96c1cdeb8b26d74e70ddc2d62529"

I = sp.I
ID2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.diag(1, -1)
ID4 = sp.eye(4)
ZERO4 = sp.zeros(4)
EX = sp.Matrix(
    [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
)
ET = sp.Matrix(
    [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, -1, 0, 0]]
)
N0 = sp.diag(0, 1, 1, 2)
A_XX = sp.diag(sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2))
A_TT = sp.diag(sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2), -sp.Rational(1, 2))
A_XT = sp.zeros(4)
A_XT[1, 2] = A_XT[2, 1] = -1

LENGTH = 4
FINE_SIZE = LENGTH * LENGTH
COARSE_EXTENT = LENGTH // 2
CELL_COUNT = COARSE_EXTENT * COARSE_EXTENT
BASE_SHEARS = (
    (sp.Rational(3, 5), sp.Rational(4, 5)),
    (sp.Rational(5, 13), sp.Rational(12, 13)),
    (sp.Rational(8, 17), sp.Rational(15, 17)),
    (sp.Rational(7, 25), sp.Rational(24, 25)),
)
OVERLAP_SHEARS = (
    (sp.Integer(0), sp.Integer(1)),
    (sp.Rational(3, 5), sp.Rational(4, 5)),
    (sp.Rational(5, 13), sp.Rational(12, 13)),
    (sp.Rational(8, 17), sp.Rational(15, 17)),
    (sp.Rational(7, 25), sp.Rational(24, 25)),
    (sp.Rational(20, 29), sp.Rational(21, 29)),
    (sp.Rational(12, 37), sp.Rational(35, 37)),
    (sp.Rational(9, 41), sp.Rational(40, 41)),
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 190 else detail[:187] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
    ).returncode == 0


def kron(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(left, right)


def phase_unitary() -> sp.Matrix:
    phases = []
    for subset in range(4):
        degree = subset.bit_count()
        koszul = (-1) ** (degree * (degree - 1) // 2)
        phases.append((-I) ** degree * koszul)
    return sp.diag(*phases)


def shift_lifts() -> tuple[sp.Matrix, sp.Matrix]:
    return kron(Y, ID2), kron(Z, Y)


def physical_tangents() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    return A_XX, A_XT, A_TT


def vectorize(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(matrix.rows * matrix.cols, 1, list(matrix))


def column_basis(matrix: sp.Matrix) -> sp.Matrix:
    pivots = matrix.rref()[1]
    if not pivots:
        return sp.zeros(matrix.rows, 0)
    return matrix[:, list(pivots)]


def subspace_intersection(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    null = left.row_join(-right).nullspace()
    if not null:
        return sp.zeros(left.rows, 0)
    images = [left * item[: left.cols, :] for item in null]
    return column_basis(sp.Matrix.hstack(*images))


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    expected_parent = "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_COMMIT),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def shift_group_certificate(mutation: str) -> dict[str, bool]:
    rt, rx = shift_lifts()
    raw_rt = kron(X, Z)
    raw_rx = kron(ID2, X)
    phase = phase_unitary()
    generic = sp.Matrix(4, 4, sp.symbols("z0:16"))
    projective = (
        rt.H == rt
        and rx.H == rx
        and rt**2 == ID4
        and rx**2 == ID4
        and rt * rx == -rx * rt
        and rt * rx * rt * rx == -ID4
    )
    lift_match = sp.simplify(phase.H * raw_rt * phase - rt) == ZERO4 and sp.simplify(
        phase.H * raw_rx * phase - rx
    ) == ZERO4
    ad_commute = sp.simplify(
        rt * (rx * generic * rx) * rt - rx * (rt * generic * rt) * rx
    ) == ZERO4
    if mutation == "force_linear_shift_group":
        projective = False
    if mutation == "break_adjoint_action":
        ad_commute = False
    return {
        "projective": projective,
        "lift_match": lift_match,
        "ad_commute": ad_commute,
    }


def fixed_frame_certificate(mutation: str) -> dict[str, object]:
    rt, rx = shift_lifts()
    a02 = sp.simplify(rx * A_XT * rx)
    expected_a02 = sp.zeros(4)
    expected_a02[0, 3] = expected_a02[3, 0] = -1
    commutator_ranks = {
        "Axx": ((rx * A_XX - A_XX * rx).rank(), (rt * A_XX - A_XX * rt).rank()),
        "Axt": ((rx * A_XT - A_XT * rx).rank(), (rt * A_XT - A_XT * rt).rank()),
        "Att": ((rx * A_TT - A_TT * rx).rank(), (rt * A_TT - A_TT * rt).rank()),
    }
    orbit = sp.Matrix.hstack(*(vectorize(item) for item in (A_XX, A_XT, A_TT, a02)))
    physical = orbit[:, :3]
    span_escape = physical.rank() == 3 and orbit.rank() == 4 and a02 == expected_a02

    constraints = []
    for lift in (rt, rx):
        constraints.append(
            sp.Matrix.hstack(
                *(vectorize(lift * item - item * lift) for item in physical_tangents())
            )
        )
    invariant_rank = constraints[0].col_join(constraints[1]).rank()
    reynolds = []
    group = (ID4, rt, rx, rt * rx)
    for tangent in physical_tangents():
        reynolds.append(sp.simplify(sum((r * tangent * r.H for r in group), ZERO4) / 4))

    nvars = sp.symbols("n0:4")
    diagonal_grade = sp.diag(*nvars)
    raw_rt = kron(X, Z)
    raw_rx = kron(ID2, X)
    expressions = list(raw_rt * diagonal_grade - diagonal_grade * raw_rt)
    expressions += list(raw_rx * diagonal_grade - diagonal_grade * raw_rx)
    grade_matrix, _ = sp.linear_eq_to_matrix(expressions, nvars)
    transitive_grade = grade_matrix.rank() == 3 and grade_matrix * sp.ones(4, 1) == sp.zeros(
        grade_matrix.rows, 1
    )
    degree_boundary = (
        N0 * A_XT - A_XT * N0 == ZERO4
        and (N0 * a02 - a02 * N0).rank() == 2
    )

    if mutation == "claim_fixed_frame_covariant":
        invariant_rank = 0
    if mutation == "drop_degree_changing_orbit":
        span_escape = False
    if mutation == "invent_translation_invariant_grading":
        transitive_grade = False
    return {
        "commutator_ranks": commutator_ranks,
        "span_escape": span_escape,
        "invariant_rank": invariant_rank,
        "reynolds": all(item == ZERO4 for item in reynolds),
        "transitive_grade": transitive_grade,
        "degree_boundary": degree_boundary,
    }


def frame_covariance_certificate(mutation: str) -> dict[str, bool]:
    sx, st, mass, hxx, hxt, htt = sp.symbols(
        "sx st mass hxx hxt htt", real=True
    )
    differential = I * (sx * EX + st * ET)
    hodge = ID4 + hxx * A_XX + hxt * A_XT + htt * A_TT
    action = sp.simplify(
        mass * hodge + I * (hodge * differential + differential.H * hodge)
    )
    rt, rx = shift_lifts()
    exact = True
    nilpotent = differential**2 == ZERO4
    degree = sp.simplify(N0 * differential - differential * N0 - differential) == ZERO4
    hodge_degree = sp.simplify(N0 * hodge - hodge * N0) == ZERO4
    for ot, ox in ((0, 0), (1, 0), (0, 1), (1, 1)):
        lift = (rt**ot) * (rx**ox)
        shifted_n = sp.simplify(lift.H * N0 * lift)
        shifted_d = sp.simplify(lift.H * differential * lift)
        shifted_h = sp.simplify(lift.H * hodge * lift)
        if mutation == "freeze_degree_under_shift" and (ot, ox) == (0, 1):
            shifted_n = N0
        if mutation == "freeze_hodge_under_shift" and (ot, ox) == (1, 0):
            shifted_h = hodge
        shifted_q = sp.simplify(
            mass * shifted_h
            + I * (shifted_h * shifted_d + shifted_d.H * shifted_h)
        )
        exact &= (
            shifted_d**2 == ZERO4
            and sp.simplify(shifted_n * shifted_d - shifted_d * shifted_n - shifted_d)
            == ZERO4
            and sp.simplify(shifted_n * shifted_h - shifted_h * shifted_n) == ZERO4
            and sp.simplify(shifted_q - lift.H * action * lift) == ZERO4
        )
    return {
        "base_nilpotent": nilpotent,
        "base_degree": degree,
        "base_hodge_degree": hodge_degree,
        "exact": exact,
    }


def fine_index(time: int, space: int) -> int:
    return (time % LENGTH) * LENGTH + (space % LENGTH)


def chart_matrix(origin: tuple[int, int]) -> sp.Matrix:
    matrix = sp.zeros(FINE_SIZE)
    row = 0
    for coarse_t in range(COARSE_EXTENT):
        for coarse_x in range(COARSE_EXTENT):
            for offset_t in range(2):
                for offset_x in range(2):
                    time = 2 * coarse_t + offset_t + origin[0]
                    space = 2 * coarse_x + offset_x + origin[1]
                    matrix[row, fine_index(time, space)] = 1
                    row += 1
    return matrix


def anchor_embedding(time: int, space: int) -> sp.Matrix:
    matrix = sp.zeros(FINE_SIZE, 4)
    for column, (dt, dx) in enumerate(((0, 0), (0, 1), (1, 0), (1, 1))):
        matrix[fine_index(time + dt, space + dx), column] = 1
    return matrix


def shear_hodge(shear: sp.Rational, volume: sp.Rational) -> sp.Matrix:
    metric = sp.Matrix([[1, shear], [shear, 1]])
    return sp.diag(volume, volume * metric.inv(), 1 / volume)


def onsite_hodge() -> sp.Matrix:
    result = sp.zeros(FINE_SIZE)
    for coarse_t in range(COARSE_EXTENT):
        for coarse_x in range(COARSE_EXTENT):
            shear, volume = BASE_SHEARS[2 * coarse_t + coarse_x]
            embedding = anchor_embedding(2 * coarse_t, 2 * coarse_x)
            result += embedding * shear_hodge(shear, volume) * embedding.T
    return sp.simplify(result)


def overlap_field() -> dict[tuple[int, int], tuple[sp.Rational, sp.Rational]]:
    return {
        (time, space): OVERLAP_SHEARS[(3 * time + space) % 8]
        for time in range(LENGTH)
        for space in range(LENGTH)
    }


def overlap_hodge(
    field: dict[tuple[int, int], tuple[sp.Rational, sp.Rational]]
) -> sp.Matrix:
    result = sp.zeros(FINE_SIZE)
    for (time, space), (shear, volume) in field.items():
        embedding = anchor_embedding(time, space)
        result += embedding * shear_hodge(shear, volume) * embedding.T / 4
    return sp.simplify(result)


def translation_matrix(displacement: tuple[int, int]) -> sp.Matrix:
    matrix = sp.zeros(FINE_SIZE)
    for time in range(LENGTH):
        for space in range(LENGTH):
            source = fine_index(time, space)
            target = fine_index(time + displacement[0], space + displacement[1])
            matrix[target, source] = 1
    return matrix


def shifted_field(
    field: dict[tuple[int, int], tuple[sp.Rational, sp.Rational]],
    displacement: tuple[int, int],
) -> dict[tuple[int, int], tuple[sp.Rational, sp.Rational]]:
    return {
        (time, space): field[
            ((time - displacement[0]) % LENGTH, (space - displacement[1]) % LENGTH)
        ]
        for time in range(LENGTH)
        for space in range(LENGTH)
    }


def block_diagonal_part(matrix: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(FINE_SIZE)
    for cell in range(CELL_COUNT):
        start = 4 * cell
        result[start : start + 4, start : start + 4] = matrix[
            start : start + 4, start : start + 4
        ]
    return result


def chart_tangent_basis(origin: tuple[int, int]) -> sp.Matrix:
    chart = chart_matrix(origin)
    columns = []
    for cell in range(CELL_COUNT):
        for tangent in physical_tangents():
            local = sp.zeros(FINE_SIZE)
            start = 4 * cell
            local[start : start + 4, start : start + 4] = tangent
            columns.append(vectorize(chart.T * local * chart))
    return sp.Matrix.hstack(*columns)


def overlap_certificate(mutation: str) -> dict[str, object]:
    origins = ((0, 0), (0, 1), (1, 0), (1, 1))
    onsite = onsite_hodge()
    onsite_cross_ranks = []
    transported_degree_ranks = []
    reset_degree_ranks = []
    degree_difference_ranks = []
    block_grade = sp.kronecker_product(sp.eye(CELL_COUNT), N0)
    base_chart = chart_matrix((0, 0))
    fine_grade = base_chart.T * block_grade * base_chart
    for origin in origins:
        chart = chart_matrix(origin)
        charted = chart * onsite * chart.T
        onsite_cross_ranks.append((charted - block_diagonal_part(charted)).rank())
        transported_grade = chart * fine_grade * chart.T
        transported_degree_ranks.append(
            (transported_grade * charted - charted * transported_grade).rank()
        )
        reset_degree_ranks.append(
            (block_grade * charted - charted * block_grade).rank()
        )
        degree_difference_ranks.append((transported_grade - block_grade).rank())

    tangent_spaces = [chart_tangent_basis(origin) for origin in origins]
    intersection = tangent_spaces[0]
    intersection_dimensions = [intersection.rank()]
    for space in tangent_spaces[1:]:
        intersection = subspace_intersection(intersection, space)
        intersection_dimensions.append(intersection.rank())
    parity_x = sp.diag(
        *((-1) ** (index % LENGTH) for index in range(FINE_SIZE))
    )
    parity_t = sp.diag(
        *((-1) ** (index // LENGTH) for index in range(FINE_SIZE))
    )
    parity_span = sp.Matrix.hstack(vectorize(parity_x), vectorize(parity_t))
    intersection_exact = (
        [space.rank() for space in tangent_spaces] == [12, 12, 12, 12]
        and intersection_dimensions == [12, 4, 2, 2]
        and intersection.row_join(parity_span).rank() == 2
    )

    field = overlap_field()
    overlap = overlap_hodge(field)
    flat = overlap_hodge(
        {(time, space): (sp.Integer(0), sp.Integer(1)) for time, space in field}
    )
    leading_minors = [sp.factor(overlap[:size, :size].det()) for size in range(1, 17)]
    positive = overlap == overlap.T and overlap.rank() == 16 and all(
        bool(item > 0) for item in leading_minors
    )
    covariance = True
    for displacement in ((1, 0), (0, 1), (1, 1)):
        translation = translation_matrix(displacement)
        covariance &= sp.simplify(
            translation * overlap * translation.T
            - overlap_hodge(shifted_field(field, displacement))
        ) == sp.zeros(FINE_SIZE)

    phase = sp.kronecker_product(sp.eye(CELL_COUNT), phase_unitary().H)
    charts = {origin: phase * chart_matrix(origin) for origin in origins}
    cocycle = True
    for first in origins:
        for second in origins:
            for third in origins:
                u21 = charts[second] * charts[first].H
                u32 = charts[third] * charts[second].H
                u31 = charts[third] * charts[first].H
                cocycle &= sp.simplify(u32 * u21 - u31) == sp.zeros(FINE_SIZE)

    overlap_cross_ranks = []
    for origin in origins:
        charted = chart_matrix(origin) * overlap * chart_matrix(origin).T
        overlap_cross_ranks.append((charted - block_diagonal_part(charted)).rank())

    local_support = True
    for row in range(FINE_SIZE):
        rt, rx = divmod(row, LENGTH)
        for column in range(FINE_SIZE):
            if row == column or overlap[row, column] == 0:
                continue
            ct, cx = divmod(column, LENGTH)
            dt = min((rt - ct) % LENGTH, (ct - rt) % LENGTH)
            dx = min((rx - cx) % LENGTH, (cx - rx) % LENGTH)
            local_support &= dt <= 1 and dx <= 1

    if mutation == "claim_onsite_all_charts":
        onsite_cross_ranks = [0, 0, 0, 0]
    if mutation == "drop_overlap_link":
        overlap_cross_ranks = [0, 0, 0, 0]
    if mutation == "break_overlap_cocycle":
        cocycle = False
    if mutation == "erase_nonuniform_provenance":
        covariance = False
    if mutation == "break_overlap_positivity":
        positive = False
    return {
        "onsite_cross_ranks": onsite_cross_ranks,
        "transported_degree_ranks": transported_degree_ranks,
        "reset_degree_ranks": reset_degree_ranks,
        "degree_difference_ranks": degree_difference_ranks,
        "intersection_exact": intersection_exact,
        "intersection_dimensions": intersection_dimensions,
        "positive": positive,
        "flat": flat == sp.eye(FINE_SIZE),
        "covariance": covariance,
        "cocycle": cocycle,
        "overlap_cross_ranks": overlap_cross_ranks,
        "local_support": local_support,
        "one_mode_per_site": overlap.rows == FINE_SIZE,
    }


def descent_boundary_certificate(mutation: str) -> dict[str, object]:
    field = overlap_field()
    overlap = overlap_hodge(field)
    block_grade = sp.kronecker_product(sp.eye(CELL_COUNT), N0)
    grade_ranks = []
    for origin in ((0, 0), (0, 1), (1, 0), (1, 1)):
        chart = chart_matrix(origin)
        fine_grade = chart.T * block_grade * chart
        grade_ranks.append((fine_grade * overlap - overlap * fine_grade).rank())

    sx, st = sp.symbols("sx st", real=True)
    differential = I * (sx * EX + st * ET)
    rt, rx = shift_lifts()
    group = (ID4, rt, rx, rt * rx)
    average_grade = sp.simplify(
        sum((lift.H * N0 * lift for lift in group), ZERO4) / 4
    )
    average_d = sp.simplify(
        sum((lift.H * differential * lift for lift in group), ZERO4) / 4
    )
    average_square = sp.simplify(
        average_d**2 - (sx**2 + st**2) * ID4 / 4
    ) == ZERO4
    average_determinant = sp.factor(average_d.det()) == (sx**2 + st**2) ** 2 / 16
    character_determinants = []
    character_ranks = []
    for weights in (
        (1, -1, 1, -1),
        (1, 1, -1, -1),
        (1, -1, -1, 1),
    ):
        projected_d = sp.simplify(
            sum(
                (
                    weight * lift.H * differential * lift
                    for weight, lift in zip(weights, group, strict=True)
                ),
                ZERO4,
            )
            / 4
        )
        character_determinants.append(sp.factor(projected_d.det()))
        character_ranks.append(projected_d.rank())
    character_boundary = (
        character_determinants == [st**4 / 16, sx**4 / 16, 0]
        and character_ranks == [4, 4, 0]
    )
    if mutation == "pretend_overlap_preserves_degree":
        grade_ranks = [0, 0, 0, 0]
    if mutation == "average_d_as_nilpotent":
        average_square = False
    if mutation == "character_average_as_complex":
        character_boundary = False
    return {
        "grade_ranks": grade_ranks,
        "average_grade": average_grade == ID4,
        "average_square": average_square,
        "average_determinant": average_determinant,
        "character_boundary": character_boundary,
        "character_determinants": character_determinants,
        "character_ranks": character_ranks,
    }


def constant_metric_certificate(mutation: str) -> dict[str, object]:
    a, b, c, sx, st, mass, volume = sp.symbols(
        "a b c sx st mass volume", real=True, nonzero=True
    )
    determinant = a * b - c**2
    metric = sp.Matrix([[a, c], [c, b]])
    hodge = sp.diag(volume, volume * metric.inv(), volume / determinant)
    differential = I * (sx * EX + st * ET)
    matter = sp.simplify(hodge * differential + differential.H * hodge)
    normalized = sp.simplify(hodge.inv() * matter)
    radius2 = sp.factor(
        (sp.Matrix([[sx, st]]) * metric.inv() * sp.Matrix([sx, st]))[0]
    )
    scalar_square = sp.simplify(normalized**2 - radius2 * ID4) == ZERO4
    characteristic = sp.trace(normalized) == 0 and sp.factor(
        normalized.det() - radius2**2
    ) == 0
    h_self_adjoint = sp.simplify(normalized.H * hodge - hodge * normalized) == ZERO4
    hodge_determinant = sp.factor(hodge.det() - volume**4 / determinant**2) == 0

    pullback = sp.diag(1, 1, -1, -1)
    reflection = sp.simplify(
        pullback * hodge * pullback - hodge.subs(c, -c)
    ) == ZERO4
    reflection_odd = sp.simplify(hodge.diff(c).subs(c, 0)) != ZERO4

    fixtures_positive = True
    for shear, fixture_volume in OVERLAP_SHEARS:
        fixture_h = shear_hodge(shear, fixture_volume)
        fixture_d = differential.subs({sx: sp.Rational(3, 5), st: sp.Rational(4, 5)})
        fixture_m = sp.simplify(
            fixture_h * fixture_d + fixture_d.H * fixture_h
        )
        fixture_q = sp.Rational(2, 7) * fixture_h + I * fixture_m
        fixtures_positive &= bool(sp.factor(fixture_q.det()) > 0)

    if mutation == "drop_hodge_inverse":
        scalar_square = False
    if mutation == "hold_shift_even_under_reflection":
        reflection = False
    return {
        "scalar_square": scalar_square,
        "characteristic": characteristic,
        "h_self_adjoint": h_self_adjoint,
        "hodge_determinant": hodge_determinant,
        "reflection": reflection,
        "reflection_odd": reflection_odd,
        "fixtures_positive": fixtures_positive,
    }


def scope_certificate(mutation: str) -> dict[str, bool]:
    raw_note = NOTE_PATH.read_text(encoding="utf-8")
    note = " ".join(raw_note.lower().split())
    w1_packet = raw_note.split("#### W1 attacks", 1)[1].split(
        "#### W2 attacks", 1
    )[0]
    w2_packet = raw_note.split("#### W2 attacks", 1)[1].split(
        "### N2", 1
    )[0]
    result = {
        "fixed_origin": "fixed blocking origin is not admissible as physical structure" in note,
        "repair": "overlap hodge is a candidate carrier repair" in note,
        "not_full_repair": "overlap hodge alone is not a full dirac-kahler repair" in note,
        "global_d": "common global nilpotent differential remains unexecuted" in note,
        "adm": "actual adm/history transporter remains unexecuted" in note,
        "os": "reflection positivity remains unexecuted" in note,
        "frame_vector": "vector lift still needs a spin/z2 choice" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "n1_normalized_routes": (
            w1_packet.count("**ATTEMPTED**") >= 5
            and w2_packet.count("**ATTEMPTED**") >= 5
            and "primary object/formulation, mechanism/invariant" in note
        ),
        "n1_authority_partition": (
            raw_note.count("current-cycle evidence") >= 8
            and raw_note.count("content-bound unaudited") >= 4
            and "does **not** prove the new matrix ranks" in note
        ),
        "n2_pairwise": (
            "closing first automatically closes second?" in note
            and "closing second automatically closes first?" in note
            and "| `(w1,w2)` | no | no | yes |" in note
        ),
        "n3_hidden_scan": (
            "the required phrase scan found no uses" in note
            and "no hit promotes a hidden condition" in note
        ),
        "n4_line_anchors": all(
            anchor in note
            for anchor in (
                "2026-08-14.md:214-248",
                "2026-08-14.md:582-586",
                "2026-08-14.md:361-364",
                "2026-08-14.md:593-599",
            )
        ),
        "n5_resolution_packet": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
        "n6_registry_scan": (
            "docs/audit/data/axiom_premise_nodes.json" in note
            and "frame gauge is a convention" in note
            and "no axiom amendment is justified" in note
        ),
        "n7_concrete_steelman": (
            "d_ext=e_g d l_g" in note
            and "l_g e_g=i" in note
            and "uniform finite-range support" in note
            and "exact `q_e` action pullback" in note
        ),
        "n8_cross_cycle": (
            "all 89 `no_go_ledger.md` files were searched" in note
            and "2026-08-14.md:593-603" in note
            and "2026-08-14.md:575-583" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero" in note,
    }
    if mutation == "claim_adm_os_closed":
        result["adm"] = False
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    if mutation == "drop_n1_route_markers":
        result["n1_normalized_routes"] = False
    if mutation == "blur_n1_authority_partition":
        result["n1_authority_partition"] = False
    if mutation == "drop_n2_pairwise_table":
        result["n2_pairwise"] = False
    if mutation == "hide_n3_condition":
        result["n3_hidden_scan"] = False
    if mutation == "mismatch_n4_residual":
        result["n4_line_anchors"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution_packet"] = False
    if mutation == "skip_n6_registry_scan":
        result["n6_registry_scan"] = False
    if mutation == "weaken_n7_steelman":
        result["n7_concrete_steelman"] = False
    if mutation == "skip_n8_echo":
        result["n8_cross_cycle"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_obligation_retirement":
        result["zero_retirement"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "stale_parent_authority",
            "force_linear_shift_group",
            "break_adjoint_action",
            "claim_fixed_frame_covariant",
            "drop_degree_changing_orbit",
            "invent_translation_invariant_grading",
            "freeze_degree_under_shift",
            "freeze_hodge_under_shift",
            "claim_onsite_all_charts",
            "drop_overlap_link",
            "break_overlap_cocycle",
            "erase_nonuniform_provenance",
            "break_overlap_positivity",
            "pretend_overlap_preserves_degree",
            "average_d_as_nilpotent",
            "character_average_as_complex",
            "drop_hodge_inverse",
            "hold_shift_even_under_reflection",
            "claim_adm_os_closed",
            "weaken_no_go_packet",
            "drop_n1_route_markers",
            "blur_n1_authority_partition",
            "drop_n2_pairwise_table",
            "hide_n3_condition",
            "mismatch_n4_residual",
            "drop_n5_resolution",
            "skip_n6_registry_scan",
            "weaken_n7_steelman",
            "skip_n8_echo",
            "claim_axiom_amendment",
            "claim_toe_progress",
            "claim_obligation_retirement",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-authority-and-Block104-parent",
        "current axioms and the exact same-action Block104 parent triple are content-bound",
        authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
        f"origin/main={str(authority['main'])[:10]}; parent={str(authority['parent'])[:10]}",
    )

    shift = shift_group_certificate(mutation)
    checks.check(
        "B-projective-one-site-lifts-and-honest-adjoint-action",
        "the exact staggered one-site lifts anticommute while their operator conjugations form Z2 squared",
        all(shift.values()),
        "Rt=Y tensor I, Rx=Z tensor Y; RxRt=-RtRx but Ad_Rx Ad_Rt=Ad_Rt Ad_Rx",
    )

    fixed = fixed_frame_certificate(mutation)
    checks.check(
        "C-fixed-origin-physical-Hodge-and-grading-obstruction",
        "no nonzero physical Hodge tangent is fixed and the shear orbit exits the fixed degree-preserving span",
        fixed["commutator_ranks"]
        == {"Axx": (4, 0), "Axt": (4, 4), "Att": (0, 4)}
        and fixed["span_escape"]
        and fixed["invariant_rank"] == 3
        and fixed["reynolds"]
        and fixed["transitive_grade"]
        and fixed["degree_boundary"],
        "the Axt orbit adds A02; every fixed-frame Reynolds average vanishes",
    )

    frame = frame_covariance_certificate(mutation)
    checks.check(
        "D-covariant-frame-degree-differential-Hodge-and-action",
        "co-transforming N, d, and H gives exact nilpotent degree and same-action covariance in all four frames",
        all(frame.values()),
        "N_o=R_o^dag N0 R_o, d_o=R_o^dag d0 R_o, H_o=R_o^dag H0 R_o",
    )

    overlap = overlap_certificate(mutation)
    checks.check(
        "E-nonuniform-onsite-overlap-boundary",
        "a single onsite shear Hodge is not block-onsite in shifted charts and the four physical tangent spaces share no shear",
        overlap["onsite_cross_ranks"] == [0, 8, 8, 8]
        and overlap["transported_degree_ranks"] == [0, 0, 0, 0]
        and overlap["reset_degree_ranks"] == [0, 8, 8, 0]
        and overlap["degree_difference_ranks"] == [0, 16, 16, 8]
        and overlap["intersection_exact"],
        f"tangent-space intersection dimensions={overlap['intersection_dimensions']}",
    )
    checks.check(
        "F-positive-translation-covariant-overlap-Hodge-repair",
        "averaging over all anchors gives a positive flat-normalized bounded-local one-mode Hodge with exact cocycle covariance",
        overlap["positive"]
        and overlap["flat"]
        and overlap["covariance"]
        and overlap["cocycle"]
        and overlap["overlap_cross_ranks"] == [16, 16, 16, 12]
        and overlap["local_support"]
        and overlap["one_mode_per_site"],
        "4x4 exact rational witness; cross-block residual ranks 16/16/16/12",
    )

    descent = descent_boundary_certificate(mutation)
    checks.check(
        "G-overlap-degree-and-naive-differential-averaging-boundary",
        "the positive overlap Hodge breaks every canonical grading and naive frame averaging destroys nilpotence",
        descent["grade_ranks"] == [8, 8, 8, 8]
        and descent["average_grade"]
        and descent["average_square"]
        and descent["average_determinant"]
        and descent["character_boundary"],
        "Nbar=I; trivial dbar is invertible; character ranks are 4/4/0",
    )

    metric = constant_metric_certificate(mutation)
    checks.check(
        "H-constant-positive-metric-Clifford-and-reflection-parity",
        "the H-normalized matter operator has the metric Clifford shell and the ADM shear is time-reflection odd",
        all(metric.values()),
        "(H^-1 M)^2=(s^T g^-1 s)I; P_t H(c) P_t=H(-c)",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "I-scope-no-go-discipline-and-TOE-firewall",
        "N1-N8 preserve the common-d, Ward, ADM, OS, gravity, audit, axiom, and TOE obligations",
        all(scope.values()),
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['main']} axiom={CURRENT_AXIOM_BLOB}; Block104 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: exact projective shift lifts, Hodge tangents, metric Clifford identity, and reflection parity are checked"
    )
    print(
        "per_site: one fine Grassmann mode is retained at each of the 16 torus sites; no anchor copy is added"
    )
    print(
        "per_mode: the zero-coarse-momentum shear orbit adds the degree-changing A02 direction; fixed physical tangent invariants are zero"
    )
    print(
        "per_block: onsite nonuniform shear has shifted-chart cross rank 8; overlap repair cross ranks are 16/16/16/12"
    )
    print(
        "lattice_wide: checked and not executed — a uniformly finite-range signed-shift common d/Ward action, ADM/history common link, OS positivity, joint gravity, Records, selection, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: fixed-origin curved shear is not translation-closed; an all-anchor positive overlap Hodge restores exact passive and active translation covariance without extra site modes"
    )
    print(
        "DECISION_CUT: advance only the overlap/frame-gauge carrier to the common-d and ADM reflection-link test; reject a physical fixed blocking origin"
    )
    print(
        "TOE: zero obligation retirement, zero retained-positive end-to-end theories, and no percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
