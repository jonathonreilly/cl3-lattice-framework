#!/usr/bin/env python3
"""Block 106: exact local dual and descended Dirac--Kahler patch complex.

The exact all-anchor analysis isometry gives a strictly patch-local left dual,
a nilpotent descended differential, the overlap-Hodge same-action pullback,
and signed-shift covariance on the 4x4 fine torus.  With ``C = H_patch`` the
weighted identities require no square roots.  For ``C = H_patch^(1/2)`` this
is literally ``E_g = H^(1/2) A``, ``L_g = A.T H^(-1/2)``, and
``L_g E_g = I``; conjugation preserves every identity, so the weighted
statement follows exactly.  The actual ADM/history transporter, reflection
positivity, gravity constraint quotient, and TOE closure remain unexecuted.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_"
    "HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "logs/runner-cache/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "43ba5587944ffe0f43df10864c8348a99c17517b"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_COMMIT = "d06066c2b908aaca0779625d831dfb10620cf34d"
PARENT_NOTE_BLOB = "5eff91757e38f3f2ea7dc2a2c50788636cc2e3a5"
PARENT_RUNNER_BLOB = "4870f31b5880028ad4f1f3095aad4d0820e4668f"
PARENT_CACHE_BLOB = "5139965f5d7d62801820163fd05717e375abe111"
GRANDPARENT_104 = "7fe07db6c03fad1191893c942f708c5cb9a54c43"
GRANDPARENT_103 = "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"


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
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


I = sp.I
ID2 = sp.eye(2)
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.diag(1, -1)
N0 = sp.diag(0, 1, 1, 2)
LENGTH = 4
FINE_SIZE = LENGTH * LENGTH
PATCH_SIZE = 4 * FINE_SIZE
COARSE_EXTENT = LENGTH // 2
OFFSETS = ((0, 0), (0, 1), (1, 0), (1, 1))
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


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.expand(entry) == 0 for entry in left - right)


def fine_index(time: int, space: int) -> int:
    return (time % LENGTH) * LENGTH + (space % LENGTH)


def wrap_l1(first: tuple[int, int], second: tuple[int, int]) -> int:
    distance = 0
    for left, right in zip(first, second, strict=True):
        forward = (left - right) % LENGTH
        backward = (right - left) % LENGTH
        distance += min(forward, backward)
    return distance


def translation_matrix(displacement: tuple[int, int]) -> sp.Matrix:
    entries: dict[tuple[int, int], sp.Expr] = {}
    for time in range(LENGTH):
        for space in range(LENGTH):
            source = fine_index(time, space)
            target = fine_index(time + displacement[0], space + displacement[1])
            entries[target, source] = sp.Integer(1)
    return sp.MutableSparseMatrix(FINE_SIZE, FINE_SIZE, entries)


def projection_for_grade(degrees: tuple[int, ...], grade: int) -> sp.Matrix:
    return sp.diag(*(sp.Integer(value == grade) for value in degrees))


def analysis_isometry(scale: sp.Expr = sp.Rational(1, 2)) -> sp.Matrix:
    entries: dict[tuple[int, int], sp.Expr] = {}
    for anchor_t in range(LENGTH):
        for anchor_x in range(LENGTH):
            anchor = fine_index(anchor_t, anchor_x)
            for offset_index, (offset_t, offset_x) in enumerate(OFFSETS):
                row = 4 * anchor + offset_index
                column = fine_index(anchor_t + offset_t, anchor_x + offset_x)
                entries[row, column] = scale
    return sp.MutableSparseMatrix(PATCH_SIZE, FINE_SIZE, entries)


def chart_matrix(origin: tuple[int, int]) -> sp.Matrix:
    entries: dict[tuple[int, int], sp.Expr] = {}
    row = 0
    for coarse_t in range(COARSE_EXTENT):
        for coarse_x in range(COARSE_EXTENT):
            for offset_t in range(2):
                for offset_x in range(2):
                    time = 2 * coarse_t + offset_t + origin[0]
                    space = 2 * coarse_x + offset_x + origin[1]
                    entries[row, fine_index(time, space)] = sp.Integer(1)
                    row += 1
    return sp.MutableSparseMatrix(FINE_SIZE, FINE_SIZE, entries)


def core_objects(mass: sp.Symbol) -> dict[str, object]:
    temporal = translation_matrix((1, 0))
    spatial = translation_matrix((0, 1))
    eta_x = sp.diag(*((-1) ** (index // LENGTH) for index in range(FINE_SIZE)))
    # Forward-minus-backward central difference, the Block 104 h(Q) orientation.
    kernel = (temporal.T - temporal) / 2 + eta_x * (spatial.T - spatial) / 2
    degrees = tuple(
        (index // LENGTH) % 2 + (index % LENGTH) % 2
        for index in range(FINE_SIZE)
    )
    number = sp.diag(*degrees)
    projections = tuple(projection_for_grade(degrees, grade) for grade in range(3))
    d_kernel = projections[1] * kernel * projections[0] + projections[2] * kernel * projections[1]
    differential = -I * d_kernel
    staggered = mass * sp.eye(FINE_SIZE) + kernel
    analysis = analysis_isometry()
    descent = analysis * differential * analysis.T
    descended_number = analysis * number * analysis.T
    patch_number = sp.kronecker_product(sp.eye(FINE_SIZE), N0)
    return {
        "Tt": temporal,
        "Tx": spatial,
        "K": kernel,
        "degrees": degrees,
        "N_glob": number,
        "projections": projections,
        "d_K": d_kernel,
        "d_glob": differential,
        "D_stag": staggered,
        "A": analysis,
        "L": analysis.T,
        "Pproj": analysis * analysis.T,
        "d_ext": descent,
        "N_ext": descended_number,
        "N_patch": patch_number,
    }


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
        "grandparent_104_ancestor": is_ancestor(GRANDPARENT_104, "HEAD"),
        "grandparent_103_ancestor": is_ancestor(GRANDPARENT_103, "HEAD"),
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def index_order_raising(kernel: sp.Matrix) -> sp.Matrix:
    entries: dict[tuple[int, int], sp.Expr] = {}
    for row in range(kernel.rows):
        for column in range(row):
            if kernel[row, column] != 0:
                entries[row, column] = kernel[row, column]
    return sp.MutableSparseMatrix(kernel.rows, kernel.cols, entries)


def coarse_dft() -> sp.Matrix:
    entries: dict[tuple[int, int], sp.Expr] = {}
    for momentum_t in range(COARSE_EXTENT):
        for momentum_x in range(COARSE_EXTENT):
            momentum = 2 * momentum_t + momentum_x
            for cell_t in range(COARSE_EXTENT):
                for cell_x in range(COARSE_EXTENT):
                    cell = 2 * cell_t + cell_x
                    phase = (-1) ** (momentum_t * cell_t + momentum_x * cell_x)
                    for component in range(4):
                        entries[4 * momentum + component, 4 * cell + component] = sp.Rational(
                            phase, 2
                        )
    return sp.MutableSparseMatrix(FINE_SIZE, FINE_SIZE, entries)


def one_direction_symbol(momentum: int) -> sp.Matrix:
    phase_minus = sp.exp(-I * sp.pi * momentum)
    phase_plus = sp.exp(I * sp.pi * momentum)
    return sp.Matrix(
        [
            [0, (1 - phase_minus) / 2],
            [(phase_plus - 1) / 2, 0],
        ]
    )


def staggered_symbol(momentum_t: int, momentum_x: int) -> sp.Matrix:
    temporal = sp.kronecker_product(one_direction_symbol(momentum_t), ID2)
    spatial = sp.kronecker_product(Z, one_direction_symbol(momentum_x))
    return temporal + spatial


def half_phase(momentum_half: sp.Rational) -> sp.Matrix:
    negative = sp.expand_complex(sp.exp(-I * sp.pi * momentum_half / 2))
    positive = sp.expand_complex(sp.exp(I * sp.pi * momentum_half / 2))
    return sp.diag(negative, positive)


def momentum_gate(kernel: sp.Matrix, mutation: str) -> bool:
    blocking = chart_matrix((0, 0))
    fourier = coarse_dft()
    blocked = fourier * blocking * kernel * blocking.T * fourier.H
    diagonal = True
    symbols: dict[tuple[int, int], sp.Matrix] = {}
    for momentum_t in range(COARSE_EXTENT):
        for momentum_x in range(COARSE_EXTENT):
            momentum = 2 * momentum_t + momentum_x
            expected = staggered_symbol(momentum_t, momentum_x)
            symbols[momentum_t, momentum_x] = expected
            for other in range(COARSE_EXTENT * COARSE_EXTENT):
                block = blocked[
                    4 * momentum : 4 * momentum + 4,
                    4 * other : 4 * other + 4,
                ]
                diagonal &= matrix_equal(block, expected if other == momentum else sp.zeros(4))

    gamma_t = sp.kronecker_product(Y, Z)
    gamma_x = sp.kronecker_product(ID2, Y)
    phase_fix = sp.diag(1, -I, -I, 1)
    fine_site_equivalence = True
    for (momentum_t, momentum_x), symbol in symbols.items():
        phase = sp.kronecker_product(
            half_phase(sp.Rational(momentum_t, 2)),
            half_phase(sp.Rational(momentum_x, 2)),
        )
        unitary = phase if mutation == "break_symbol_gate" else phase * phase_fix
        target = I * (
            sp.sin(sp.pi * momentum_t / 2) * gamma_t
            + sp.sin(sp.pi * momentum_x / 2) * gamma_x
        )
        fine_site_equivalence &= matrix_equal(unitary.H * symbol * unitary, target)
    return diagonal and fine_site_equivalence


def staggered_certificate(
    mass: sp.Symbol, core: dict[str, object], mutation: str
) -> dict[str, bool]:
    temporal = core["Tt"]
    spatial = core["Tx"]
    if mutation == "break_staggered_sign":
        eta_x = sp.eye(FINE_SIZE)
        kernel = (temporal.T - temporal) / 2 + eta_x * (spatial.T - spatial) / 2
    else:
        kernel = core["K"]

    projections = core["projections"]
    if mutation == "break_raising_extraction":
        d_kernel = index_order_raising(kernel)
    else:
        d_kernel = projections[1] * kernel * projections[0] + projections[2] * kernel * projections[1]
    differential = d_kernel if mutation == "drop_wick_phase" else -I * d_kernel
    staggered = mass * sp.eye(FINE_SIZE) + kernel
    number = core["N_glob"]

    range_one = True
    for row in range(FINE_SIZE):
        row_site = divmod(row, LENGTH)
        for column in range(FINE_SIZE):
            if differential[row, column] == 0:
                continue
            range_one &= wrap_l1(row_site, divmod(column, LENGTH)) == 1

    b1 = (
        matrix_equal(kernel, d_kernel - d_kernel.T)
        and matrix_equal(d_kernel**2, sp.zeros(FINE_SIZE))
        and matrix_equal(differential**2, sp.zeros(FINE_SIZE))
        and matrix_equal(number * differential - differential * number, differential)
        and matrix_equal(
            staggered,
            mass * sp.eye(FINE_SIZE) + I * (differential + differential.H),
        )
        and range_one
    )
    hermitian_matter = -I * (staggered - mass * sp.eye(FINE_SIZE))
    b2 = matrix_equal(hermitian_matter, hermitian_matter.H) and matrix_equal(
        hermitian_matter, differential + differential.H
    )
    b3 = momentum_gate(kernel, mutation)
    return {"B1": b1, "B2": b2, "B3": b3}


def patch_local_dual_certificate(mutation: str) -> dict[str, object]:
    scale = sp.Integer(1) if mutation == "break_isometry_normalization" else sp.Rational(1, 2)
    analysis = analysis_isometry(scale)
    local_dual = analysis.T
    if mutation == "break_patch_locality":
        local_dual = local_dual.copy()
        local_dual[0, 4 * fine_index(2, 2)] = sp.Rational(1, 2)
    projector = analysis * analysis.T
    supported_values = all(entry in (0, sp.Rational(1, 2)) for entry in analysis)
    four_rows_per_site = all(
        sum(int(analysis[row, column] != 0) for row in range(PATCH_SIZE)) == 4
        for column in range(FINE_SIZE)
    )
    strictly_local = True
    for fine_site in range(FINE_SIZE):
        for patch_row in range(PATCH_SIZE):
            if local_dual[fine_site, patch_row] == 0:
                continue
            anchor = patch_row // 4
            offset_t, offset_x = OFFSETS[patch_row % 4]
            anchor_t, anchor_x = divmod(anchor, LENGTH)
            strictly_local &= fine_site == fine_index(
                anchor_t + offset_t, anchor_x + offset_x
            )
    return {
        "isometry": matrix_equal(analysis.T * analysis, sp.eye(FINE_SIZE)),
        "projector": matrix_equal(projector**2, projector),
        "projector_rank": projector.rank(),
        "supported_values": supported_values,
        "four_rows_per_site": four_rows_per_site,
        "dual_identity": matrix_equal(local_dual * analysis, sp.eye(FINE_SIZE)),
        "strictly_local": strictly_local,
    }


def patch_block_range(matrix: sp.Matrix) -> tuple[bool, int]:
    in_range = True
    maximum = 0
    for row_anchor in range(FINE_SIZE):
        row_site = divmod(row_anchor, LENGTH)
        for column_anchor in range(FINE_SIZE):
            block = matrix[
                4 * row_anchor : 4 * row_anchor + 4,
                4 * column_anchor : 4 * column_anchor + 4,
            ]
            if matrix_equal(block, sp.zeros(4)):
                continue
            distance = wrap_l1(row_site, divmod(column_anchor, LENGTH))
            maximum = max(maximum, distance)
            in_range &= distance <= 3
    return in_range, maximum


def descended_certificate(
    core: dict[str, object], mutation: str
) -> dict[str, object]:
    differential = core["d_ext"].copy()
    if mutation == "break_descent_intertwiner":
        differential[0, 4 * fine_index(2, 2)] += 1
    if mutation == "smuggle_geometry_into_dext":
        field = overlap_field()
        differential = patch_hodge(field) * differential * patch_hodge_inverse(field)
    # Geometry-freedom is checked on the entries: the descended differential
    # takes only the field-independent values 0 and +-i/8.
    allowed_entries = (sp.Integer(0), I / 8, -I / 8)
    geometry_free = all(
        sp.expand(entry) in allowed_entries for entry in differential
    )
    analysis = core["A"]
    global_differential = core["d_glob"]
    descended_number = core["N_ext"]
    in_range, maximum = patch_block_range(differential)
    return {
        "nilpotent": matrix_equal(differential**2, sp.zeros(PATCH_SIZE)),
        "graded": matrix_equal(
            descended_number * differential - differential * descended_number,
            differential,
        ),
        "intertwiner": matrix_equal(
            differential * analysis, analysis * global_differential
        ),
        "compression": matrix_equal(
            analysis.T * differential * analysis, global_differential
        ),
        "number_intertwiner": matrix_equal(
            descended_number * analysis, analysis * core["N_glob"]
        ),
        "in_range": in_range,
        "maximum_range": maximum,
        "geometry_free": geometry_free,
    }


def anchor_embedding(time: int, space: int) -> sp.Matrix:
    entries = {
        (fine_index(time + offset_t, space + offset_x), column): sp.Integer(1)
        for column, (offset_t, offset_x) in enumerate(OFFSETS)
    }
    return sp.MutableSparseMatrix(FINE_SIZE, 4, entries)


def shear_hodge(shear: sp.Expr, volume: sp.Expr) -> sp.Matrix:
    metric = sp.Matrix([[1, shear], [shear, 1]])
    return sp.diag(volume, volume * metric.inv(), 1 / volume)


def overlap_field() -> dict[tuple[int, int], tuple[sp.Expr, sp.Expr]]:
    return {
        (time, space): OVERLAP_SHEARS[(3 * time + space) % 8]
        for time in range(LENGTH)
        for space in range(LENGTH)
    }


def shifted_field(
    field: dict[tuple[int, int], tuple[sp.Expr, sp.Expr]],
    displacement: tuple[int, int],
) -> dict[tuple[int, int], tuple[sp.Expr, sp.Expr]]:
    return {
        (time, space): field[
            ((time - displacement[0]) % LENGTH, (space - displacement[1]) % LENGTH)
        ]
        for time in range(LENGTH)
        for space in range(LENGTH)
    }


def flipped_field(
    field: dict[tuple[int, int], tuple[sp.Expr, sp.Expr]]
) -> dict[tuple[int, int], tuple[sp.Expr, sp.Expr]]:
    return {site: (-shear, volume) for site, (shear, volume) in field.items()}


def patch_hodge(
    field: dict[tuple[int, int], tuple[sp.Expr, sp.Expr]]
) -> sp.Matrix:
    result = sp.MutableSparseMatrix(PATCH_SIZE, PATCH_SIZE, {})
    for (time, space), (shear, volume) in field.items():
        anchor = fine_index(time, space)
        block = shear_hodge(shear, volume)
        result[4 * anchor : 4 * anchor + 4, 4 * anchor : 4 * anchor + 4] = block
    return result


def patch_hodge_inverse(
    field: dict[tuple[int, int], tuple[sp.Expr, sp.Expr]]
) -> sp.Matrix:
    result = sp.MutableSparseMatrix(PATCH_SIZE, PATCH_SIZE, {})
    for (time, space), (shear, volume) in field.items():
        anchor = fine_index(time, space)
        block = shear_hodge(shear, volume).inv()
        result[4 * anchor : 4 * anchor + 4, 4 * anchor : 4 * anchor + 4] = block
    return result


def overlap_hodge(
    field: dict[tuple[int, int], tuple[sp.Expr, sp.Expr]],
    normalization: sp.Expr = sp.Rational(1, 4),
) -> sp.Matrix:
    result = sp.zeros(FINE_SIZE)
    for (time, space), (shear, volume) in field.items():
        embedding = anchor_embedding(time, space)
        result += normalization * embedding * shear_hodge(shear, volume) * embedding.T
    return result


def geometry_certificate(
    analysis: sp.Matrix,
    hodge_patch: sp.Matrix,
    field: dict[tuple[int, int], tuple[sp.Expr, sp.Expr]],
    mutation: str,
) -> dict[str, object]:
    normalization = sp.Integer(1) if mutation == "break_overlap_pullback" else sp.Rational(1, 4)
    hodge_overlap = overlap_hodge(field, normalization)
    anchor_onsite = True
    for row_anchor in range(FINE_SIZE):
        for column_anchor in range(FINE_SIZE):
            if row_anchor == column_anchor:
                continue
            anchor_onsite &= matrix_equal(
                hodge_patch[
                    4 * row_anchor : 4 * row_anchor + 4,
                    4 * column_anchor : 4 * column_anchor + 4,
                ],
                sp.zeros(4),
            )
    leading_minors = [
        sp.factor(hodge_overlap[:size, :size].det())
        for size in range(1, FINE_SIZE + 1)
    ]
    return {
        "pullback": matrix_equal(analysis.T * hodge_patch * analysis, hodge_overlap),
        "anchor_onsite": anchor_onsite,
        "positive_leading_minors": all(bool(minor > 0) for minor in leading_minors),
    }


def action_pullback_certificate(
    mass: sp.Symbol,
    core: dict[str, object],
    hodge_patch: sp.Matrix,
    hodge_overlap: sp.Matrix,
    mutation: str,
) -> dict[str, bool]:
    sign = -1 if mutation == "break_action_pullback" else 1
    differential = core["d_ext"]
    global_differential = core["d_glob"]
    analysis = core["A"]
    patch_action = mass * hodge_patch + sign * I * (
        hodge_patch * differential + differential.H * hodge_patch
    )
    overlap_action = mass * hodge_overlap + I * (
        hodge_overlap * global_differential
        + global_differential.H * hodge_overlap
    )
    flat_patch_action = mass * sp.eye(PATCH_SIZE) + I * (
        differential + differential.H
    )
    return {
        "curved": matrix_equal(analysis.T * patch_action * analysis, overlap_action),
        "flat": matrix_equal(
            analysis.T * flat_patch_action * analysis, core["D_stag"]
        ),
    }


def weighted_certificate(
    core: dict[str, object],
    field: dict[tuple[int, int], tuple[sp.Expr, sp.Expr]],
    hodge_patch: sp.Matrix,
    mutation: str,
) -> dict[str, bool]:
    inverse = patch_hodge_inverse(field)
    analysis = core["A"]
    left_factor = analysis.T * (hodge_patch.T if mutation == "break_weighted_conjugation" else inverse)
    weighted_embedding = hodge_patch * analysis
    weighted_differential = hodge_patch * core["d_ext"] * inverse
    weighted_number = hodge_patch * core["N_ext"] * inverse
    return {
        "inverse": matrix_equal(hodge_patch * inverse, sp.eye(PATCH_SIZE)),
        "dual": matrix_equal(left_factor * weighted_embedding, sp.eye(FINE_SIZE)),
        "nilpotent": matrix_equal(weighted_differential**2, sp.zeros(PATCH_SIZE)),
        "graded": matrix_equal(
            weighted_number * weighted_differential
            - weighted_differential * weighted_number,
            weighted_differential,
        ),
        "intertwiner": matrix_equal(
            weighted_differential * weighted_embedding,
            weighted_embedding * core["d_glob"],
        ),
    }


def patch_lift(displacement: tuple[int, int], sign) -> sp.Matrix:
    entries: dict[tuple[int, int], sp.Expr] = {}
    for target_t in range(LENGTH):
        for target_x in range(LENGTH):
            target_anchor = fine_index(target_t, target_x)
            source_anchor = fine_index(
                target_t - displacement[0], target_x - displacement[1]
            )
            for offset_index, (offset_t, offset_x) in enumerate(OFFSETS):
                target_site_t = (target_t + offset_t) % LENGTH
                target_site_x = (target_x + offset_x) % LENGTH
                entries[
                    4 * target_anchor + offset_index,
                    4 * source_anchor + offset_index,
                ] = sign(target_site_t, target_site_x)
    return sp.MutableSparseMatrix(PATCH_SIZE, PATCH_SIZE, entries)


def monomial_signed(matrix: sp.Matrix) -> bool:
    values = {sp.Integer(-1), sp.Integer(0), sp.Integer(1)}
    return (
        all(entry in values for entry in matrix)
        and all(
            sum(int(matrix[row, column] != 0) for row in range(matrix.rows)) == 1
            for column in range(matrix.cols)
        )
        and all(
            sum(int(matrix[row, column] != 0) for column in range(matrix.cols)) == 1
            for row in range(matrix.rows)
        )
    )


def diagonal_sign_field(matrix: sp.Matrix) -> bool:
    return all(
        matrix[row, column] == 0 if row != column else matrix[row, row] in (-1, 1)
        for row in range(matrix.rows)
        for column in range(matrix.cols)
    )


def signed_shift_certificate(
    mass: sp.Symbol,
    core: dict[str, object],
    field: dict[tuple[int, int], tuple[sp.Expr, sp.Expr]],
    hodge_patch: sp.Matrix,
    mutation: str,
) -> dict[str, object]:
    temporal = core["Tt"]
    spatial = core["Tx"]
    temporal_sign = sp.diag(*((-1) ** (index % LENGTH) for index in range(FINE_SIZE)))
    signed_temporal = temporal_sign * temporal
    signed_spatial = spatial

    plain_temporal_lift = patch_lift((1, 0), lambda _time, _space: sp.Integer(1))
    plain_spatial_lift = patch_lift((0, 1), lambda _time, _space: sp.Integer(1))
    signed_temporal_lift = patch_lift(
        (1, 0), lambda _time, space: sp.Integer((-1) ** space)
    )
    signed_spatial_lift = patch_lift(
        (0, 1), lambda _time, _space: sp.Integer(1)
    )
    if mutation == "drop_signed_lift_intertwiner":
        signed_temporal_lift = plain_temporal_lift

    analysis = core["A"]
    differential = core["d_ext"]
    flat_action = mass * sp.eye(PATCH_SIZE) + I * (
        differential + differential.H
    )
    flat_invariance = all(
        matrix_equal(lift * flat_action * lift.H, flat_action)
        for lift in (signed_temporal_lift, signed_spatial_lift)
    )

    plain_geometry = (
        matrix_equal(
            plain_temporal_lift * hodge_patch * plain_temporal_lift.H,
            patch_hodge(shifted_field(field, (1, 0))),
        )
        and matrix_equal(
            plain_spatial_lift * hodge_patch * plain_spatial_lift.H,
            patch_hodge(shifted_field(field, (0, 1))),
        )
    )
    spatial_geometry = matrix_equal(
        signed_spatial_lift * hodge_patch * signed_spatial_lift.H,
        patch_hodge(shifted_field(field, (0, 1))),
    )
    flipped_temporal_geometry = patch_hodge(
        shifted_field(flipped_field(field), (1, 0))
    )
    temporal_geometry = signed_temporal_lift * hodge_patch * signed_temporal_lift.H
    shear_parity = matrix_equal(temporal_geometry, flipped_temporal_geometry)
    unflipped_residual = temporal_geometry - patch_hodge(
        shifted_field(field, (1, 0))
    )
    unflipped_rank = unflipped_residual.rank()
    expected_unflipped_rank = (
        0 if mutation == "claim_signed_geometry_covariant_unflipped" else 28
    )

    shear, volume = sp.symbols("q v", real=True, nonzero=True)
    parity = (
        sp.eye(4)
        if mutation == "break_shear_parity_identity"
        else sp.diag(1, -1, 1, -1)
    )
    block_parity = matrix_equal(
        parity * shear_hodge(shear, volume) * parity,
        shear_hodge(-shear, volume),
    )

    temporal_connection = signed_temporal_lift * plain_temporal_lift.T
    spatial_connection = signed_spatial_lift * plain_spatial_lift.T
    return {
        "commuting_action": matrix_equal(
            signed_temporal * core["D_stag"], core["D_stag"] * signed_temporal
        )
        and matrix_equal(
            signed_spatial * core["D_stag"], core["D_stag"] * signed_spatial
        ),
        "projective": matrix_equal(
            signed_temporal * signed_spatial,
            -signed_spatial * signed_temporal,
        ),
        "two_step": matrix_equal(signed_temporal**2, temporal**2)
        and matrix_equal(signed_spatial**2, spatial**2)
        and not matrix_equal(temporal**2, sp.eye(FINE_SIZE))
        and not matrix_equal(spatial**2, sp.eye(FINE_SIZE)),
        "monomial": monomial_signed(signed_temporal) and monomial_signed(signed_spatial),
        "lift_intertwiner": matrix_equal(
            signed_temporal_lift * analysis, analysis * signed_temporal
        )
        and matrix_equal(signed_spatial_lift * analysis, analysis * signed_spatial),
        "lift_orthogonal": matrix_equal(
            signed_temporal_lift * signed_temporal_lift.T, sp.eye(PATCH_SIZE)
        )
        and matrix_equal(
            signed_spatial_lift * signed_spatial_lift.T, sp.eye(PATCH_SIZE)
        ),
        "flat_invariance": flat_invariance,
        "plain_geometry": plain_geometry,
        "spatial_geometry": spatial_geometry,
        "shear_parity": shear_parity,
        "unflipped_rank": unflipped_rank,
        "unflipped_rank_expected": unflipped_rank == expected_unflipped_rank,
        "block_parity": block_parity,
        "connection": diagonal_sign_field(temporal_connection)
        and diagonal_sign_field(spatial_connection),
    }


SCOPE_KEYS = (
    "weighted_dual",
    "uniform_range",
    "same_action",
    "n5_resolution",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "adm",
    "os",
    "gravity",
    "n1_n8",
    "walls",
)


def scope_certificate(mutation: str) -> dict[str, bool]:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return {key: False for key in SCOPE_KEYS}
    note = " ".join(raw_note.lower().split())
    result = {
        "weighted_dual": "l_g e_g = i" in note,
        "uniform_range": "uniform finite-range" in note,
        "same_action": "same-action pullback" in note,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero" in note,
        "adm": "actual adm/history transporter remains unexecuted" in note,
        "os": "reflection positivity remains unexecuted" in note,
        "gravity": "gravity constraint quotient remains unexecuted" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "walls": "w1" in note and "w2" in note,
    }
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_adm_os_closed":
        result["adm"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_obligation_retirement":
        result["zero_retirement"] = False
    return result


def grade_boundary_certificate(
    core: dict[str, object], mutation: str
) -> dict[str, object]:
    defect = (
        core["N_patch"] * core["d_ext"]
        - core["d_ext"] * core["N_patch"]
        - core["d_ext"]
    )
    defect_rank = defect.rank()
    expected_rank = 0 if mutation == "claim_canonical_grade_compatible" else 12
    co_transforming_boundary = not matrix_equal(
        core["N_patch"] * core["A"], core["A"] * core["N_glob"]
    )
    scope = scope_certificate(mutation)
    return {
        "defect_rank": defect_rank,
        "rank_expected": defect_rank == expected_rank,
        "co_transforming_boundary": co_transforming_boundary,
        "scope": all(scope.values()),
    }


MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_staggered_sign",
    "break_raising_extraction",
    "drop_wick_phase",
    "break_symbol_gate",
    "break_isometry_normalization",
    "break_patch_locality",
    "break_descent_intertwiner",
    "smuggle_geometry_into_dext",
    "break_overlap_pullback",
    "break_action_pullback",
    "break_weighted_conjugation",
    "drop_signed_lift_intertwiner",
    "claim_signed_geometry_covariant_unflipped",
    "break_shear_parity_identity",
    "claim_canonical_grade_compatible",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_adm_os_closed",
    "claim_axiom_amendment",
    "claim_toe_progress",
    "claim_obligation_retirement",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-authority-and-Block105-parent",
        "current axioms, registries, ancestry, and the Block105 parent triple are content-bound",
        authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["grandparent_104_ancestor"]
        and authority["grandparent_103_ancestor"]
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
        f"registry origin/main={authority['registry']}; worktree={authority['worktree_registry']}",
    )

    mass = sp.symbols("m", real=True, positive=True)
    core = core_objects(mass)
    staggered = staggered_certificate(mass, core, mutation)
    checks.check(
        "B-exact-staggered-differential-and-same-action",
        "the exact real raising complex, Wick phase, Hermitian matter operator, and Block104 symbol agree",
        all(staggered.values()),
        "B1 nilpotence/grade/range, B2 Hermiticity, and B3 all four coarse momenta",
    )

    dual = patch_local_dual_certificate(mutation)
    checks.check(
        "C-exact-patch-isometry-and-local-dual",
        "the all-anchor analysis has a rank-16 projector and a strictly patch-local exact dual",
        dual["isometry"]
        and dual["projector"]
        and dual["projector_rank"] == 16
        and dual["supported_values"]
        and dual["four_rows_per_site"]
        and dual["dual_identity"]
        and dual["strictly_local"],
        "A entries are 0 or 1/2; each fine site occurs in exactly four patch rows",
    )

    descended = descended_certificate(core, mutation)
    checks.check(
        "D-descended-complex-exact",
        "the geometry-free descended complex is nilpotent, graded, intertwined, compressed, and range three",
        descended["nilpotent"]
        and descended["graded"]
        and descended["intertwiner"]
        and descended["compression"]
        and descended["number_intertwiner"]
        and descended["in_range"]
        and descended["maximum_range"] == 3
        and descended["geometry_free"],
        f"maximum wrap-L1 anchor-block distance={descended['maximum_range']}",
    )

    field = overlap_field()
    hodge_patch = patch_hodge(field)
    hodge_overlap = overlap_hodge(field)
    geometry = geometry_certificate(core["A"], hodge_patch, field, mutation)
    checks.check(
        "E-onsite-patch-geometry-is-overlap-Hodge",
        "anchor-onsite patch geometry pulls back to the independently recomputed positive overlap Hodge",
        all(geometry.values()),
        "all sixteen exact leading principal minors are positive",
    )

    pullback = action_pullback_certificate(
        mass, core, hodge_patch, hodge_overlap, mutation
    )
    checks.check(
        "F-same-action-pullback",
        "the curved overlap-Hodge action and the flat staggered action are exact pullbacks",
        all(pullback.values()),
        "symbolic positive mass; no fitted normalization",
    )

    weighted = weighted_certificate(core, field, hodge_patch, mutation)
    checks.check(
        "G-weighted-conjugate-corollary",
        "blockwise Hodge conjugation preserves the exact dual, nilpotence, grade, and intertwiner",
        all(weighted.values()),
        "C=H_patch exactly; C=H_patch^(1/2) gives the literal E_g/L_g reading",
    )

    shifts = signed_shift_certificate(mass, core, field, hodge_patch, mutation)
    checks.check(
        "H-signed-shift-lifts-and-shear-parity",
        "signed lifts intertwine the staggered action and move temporal shear by the exact parity flip",
        shifts["commuting_action"]
        and shifts["projective"]
        and shifts["two_step"]
        and shifts["monomial"]
        and shifts["lift_intertwiner"]
        and shifts["lift_orthogonal"]
        and shifts["flat_invariance"]
        and shifts["plain_geometry"]
        and shifts["spatial_geometry"]
        and shifts["shear_parity"]
        and shifts["unflipped_rank_expected"]
        and shifts["block_parity"]
        and shifts["connection"],
        f"Ut^2=Tt^2 and Ux^2=Tx^2 are two-step plain coarse translations, NOT identity; unflipped rank={shifts['unflipped_rank']}",
    )

    boundary = grade_boundary_certificate(core, mutation)
    checks.check(
        "I-canonical-grade-boundary-and-scope",
        "the rank-12 canonical-grade defect is closed by descended grade; co-transforming degree remains a boundary",
        boundary["rank_expected"]
        and boundary["co_transforming_boundary"]
        and boundary["scope"],
        f"canonical-grade defect rank={boundary['defect_rank']}; note scope guarded against absence",
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['main']} axiom={CURRENT_AXIOM_BLOB}; Block105 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: exact dual, descent, grading, pullback, lift, and shear-parity identities are checked symbolically in the mass"
    )
    print(
        "per_site: every fine site lies in exactly four patches and keeps one physical Grassmann mode; no anchor copy is added"
    )
    print(
        "per_mode: the blocked staggered symbol matches Block 104 momentum-by-momentum, including both zero and pi coarse lines"
    )
    print(
        "per_block: d_ext has anchor-block range three, H_patch is exactly anchor-onsite, and the signed/plain lift mismatch is a displayed sign field"
    )
    print(
        "lattice_wide: checked and not executed — the ADM/history transporter, reflection positivity/OS on the patch carrier, joint gravity, the gravity constraint quotient, Records, selection, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the all-anchor patch carrier admits an exact patch-local dual and nilpotent graded descent whose pullback is the overlap-Hodge action; the dense-inverse obstruction is bypassed"
    )
    print(
        "DECISION_CUT: advance the descended patch complex to the ADM/history reflection-link test; reject dense-inverse descent routes"
    )
    print(
        "TOE: zero obligation retirement, zero retained-positive end-to-end theories, and no percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
