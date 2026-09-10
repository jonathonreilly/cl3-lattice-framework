#!/usr/bin/env python3
"""Block 109: global dressing, involution, and positivity boundary.

On the exact Block 108 antiperiodic reflection torus, the full globally
supported translation-covariant dressing space is feasible.  It contains a
window-invisible dressed-reflection involution and a separate positive fiber.
Within the exact anti-diagonal class, however, involution leaves only the two
indefinite branches ``+A*`` and ``-A*``.  This is a bounded classification,
not a transporter impossibility or an ADM/history completion.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_involution_seam_dressing_locality_"
    "2026_08_15.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_involution_seam_dressing_"
    "locality_2026_08_15.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_involution_seam_dressing_locality_2026_08_15.py",
    "logs/runner-cache/admissibility_dirac_kahler_involution_seam_dressing_locality_2026_08_15.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "b8d9f4c40125e45415d6dd240a7ef806e773a278"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block108-involution-seam-dressing-20260815"
)
PARENT_COMMIT = "8afe8dff5ccf531208238af0aaaec1f547d73874"
PARENT_NOTE_BLOB = "21128ab10b32d4f99190ce7107ef9fb790a05781"
PARENT_RUNNER_BLOB = "57c7a81317b455912571a703a3933043248ce70f"
PARENT_CACHE_BLOB = "e0bc41e3d44d67a22dc327acd2c0d8ce77c83d30"
ANCESTOR_107 = "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"
ANCESTOR_106 = "22d6d90ec2279e5868c9c825149b2a20beea3797"
ANCESTOR_105 = "d06066c2b908aaca0779625d831dfb10620cf34d"
ANCESTOR_104 = "7fe07db6c03fad1191893c942f708c5cb9a54c43"
ANCESTOR_103 = "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"


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


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        "ancestor_107": is_ancestor(ANCESTOR_107, "HEAD"),
        "ancestor_106": is_ancestor(ANCESTOR_106, "HEAD"),
        "ancestor_105": is_ancestor(ANCESTOR_105, "HEAD"),
        "ancestor_104": is_ancestor(ANCESTOR_104, "HEAD"),
        "ancestor_103": is_ancestor(ANCESTOR_103, "HEAD"),
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


I = sp.I
LX = 4
TT = 4
SIZE = 2 * TT * LX
WINDOW_TIMES = (-2, -1, 0, 1)
POSITIVE_TIMES = (0, 1, 2, 3)
OFFSETS = ((0, 0), (0, 1), (1, 0), (1, 1))


def parity(integer: int) -> sp.Integer:
    """Return the staggered sign without unsafe negative exponentiation."""
    return sp.Integer(-1 if integer % 2 else 1)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.expand(entry) == 0 for entry in left - right)


def exact_rank(matrix: sp.Matrix) -> int:
    return DomainMatrix.from_Matrix(matrix).rank()


def max_abs_entry(matrix: sp.Matrix) -> sp.Expr:
    return max((sp.Abs(sp.factor(value)) for value in matrix), default=sp.Integer(0))


def h_site(shear: sp.Expr, volume: sp.Expr) -> sp.Matrix:
    metric = sp.Matrix([[1, shear], [shear, 1]])
    return sp.diag(volume, volume * metric.inv(), 1 / volume)


def torus_objects(
    mass: sp.Expr,
    field_c: dict[int, sp.Expr],
    volume: sp.Expr,
    half_time: int,
    boundary_sign: int,
    spatial_extent: int = LX,
) -> tuple[sp.Matrix, sp.Matrix, object]:
    """Build the exact Dirac--Kahler Q, reflection P, and torus site map."""
    size = 2 * half_time * spatial_extent

    def site_index(time_value: int, space: int) -> int:
        return ((time_value + half_time) % (2 * half_time)) * spatial_extent + (
            space % spatial_extent
        )

    def temporal_hop_sign(target_time_raw: int) -> sp.Integer:
        return sp.Integer(
            boundary_sign
            if target_time_raw >= half_time or target_time_raw < -half_time
            else 1
        )

    staggered = sp.zeros(size, size)
    for time_value in range(-half_time, half_time):
        for space in range(spatial_extent):
            index = site_index(time_value, space)
            staggered[index, index] += mass
            staggered[index, site_index(time_value + 1, space)] += (
                sp.Rational(1, 2) * temporal_hop_sign(time_value + 1)
            )
            staggered[index, site_index(time_value - 1, space)] += (
                -sp.Rational(1, 2) * temporal_hop_sign(time_value - 1)
            )
            staggered[index, site_index(time_value, space + 1)] += (
                parity(time_value) * sp.Rational(1, 2)
            )
            staggered[index, site_index(time_value, space - 1)] += (
                -parity(time_value) * sp.Rational(1, 2)
            )

    degrees = {
        site_index(time_value, space): (time_value % 2) + (space % 2)
        for time_value in range(-half_time, half_time)
        for space in range(spatial_extent)
    }
    kernel = staggered - mass * sp.eye(size)
    raising_kernel = sp.zeros(size, size)
    for row in range(size):
        for column in range(size):
            if kernel[row, column] != 0 and degrees[row] == degrees[column] + 1:
                raising_kernel[row, column] = kernel[row, column]
    differential = -I * raising_kernel

    hodge = sp.zeros(size, size)
    for anchor_time in range(-half_time, half_time):
        for anchor_space in range(spatial_extent):
            block = h_site(field_c[anchor_time], volume)
            for row_offset, (row_time, row_space) in enumerate(OFFSETS):
                for column_offset, (column_time, column_space) in enumerate(OFFSETS):
                    if block[row_offset, column_offset] == 0:
                        continue
                    hodge[
                        site_index(anchor_time + row_time, anchor_space + row_space),
                        site_index(
                            anchor_time + column_time, anchor_space + column_space
                        ),
                    ] += block[row_offset, column_offset] / 4

    operator = mass * hodge + I * (
        hodge * differential + differential.H * hodge
    )
    reflection = sp.zeros(size, size)
    for time_value in range(-half_time, half_time):
        for space in range(spatial_extent):
            reflection[
                site_index(-1 - time_value, space), site_index(time_value, space)
            ] = 1
    return operator, reflection, site_index


def step_profile(half_time: int, shear: sp.Expr) -> dict[int, sp.Expr]:
    return {
        time_value: (
            sp.Integer(0)
            if time_value in (-1, half_time - 1)
            else (shear if time_value >= 0 else -shear)
        )
        for time_value in range(-half_time, half_time)
    }


def spatial_factors() -> tuple[sp.Matrix, ...]:
    cyclic_shift = sp.zeros(LX, LX)
    for space in range(LX):
        cyclic_shift[(space + 1) % LX, space] = 1
    return (
        sp.eye(LX),
        sp.diag(*(parity(space) for space in range(LX))),
        cyclic_shift + cyclic_shift.T,
        cyclic_shift - cyclic_shift.T,
    )


@dataclass(frozen=True)
class Fixture:
    shear: sp.Rational
    propagator: sp.Matrix
    reflection: sp.Matrix
    site_index: object
    window: tuple[int, ...]
    positive: tuple[int, ...]
    reflected: tuple[int, ...]
    raw_gram: sp.Matrix


def history_gram(
    propagator: sp.Matrix,
    positive: tuple[int, ...] | list[int],
    reflected: tuple[int, ...] | list[int],
) -> sp.Matrix:
    return sp.Matrix(
        len(positive),
        len(reflected),
        lambda row, column: sp.conjugate(
            propagator[positive[row], reflected[column]]
        ),
    )


def fixture_data(shear: sp.Rational) -> Fixture:
    operator, reflection, site_index = torus_objects(
        sp.Rational(9, 20),
        step_profile(TT, shear),
        sp.Integer(1),
        TT,
        -1,
    )
    propagator = operator.inv(method="DM")
    window = tuple(
        site_index(time_value, space)
        for time_value in WINDOW_TIMES
        for space in range(LX)
    )
    positive = tuple(
        site_index(time_value, space)
        for time_value in POSITIVE_TIMES
        for space in range(LX)
    )
    reflected = tuple(
        site_index(-1 - time_value, space)
        for time_value in POSITIVE_TIMES
        for space in range(LX)
    )
    raw_gram = history_gram(propagator, positive, reflected)
    return Fixture(
        shear,
        propagator,
        reflection,
        site_index,
        window,
        positive,
        reflected,
        raw_gram,
    )


def parameter_index(
    slice_i: int, slice_j: int, factor_index: int, imaginary: int
) -> int:
    """Factor/block/real-imag order on all eight torus slices."""
    return 2 * (4 * (8 * slice_i + slice_j) + factor_index) + imaginary


def global_labels() -> tuple[tuple[int, int, int, str], ...]:
    return tuple(
        (slice_i, slice_j, factor_index, part)
        for slice_i in range(8)
        for slice_j in range(8)
        for factor_index in range(4)
        for part in ("re", "im")
    )


def reality_permutation_certificate(mutation: str) -> dict[str, object]:
    labels = global_labels()
    label_to_index = {label: index for index, label in enumerate(labels)}
    targets: list[int] = []
    signs: list[int] = []
    for slice_i, slice_j, factor_index, part in labels:
        targets.append(
            label_to_index[(7 - slice_i, 7 - slice_j, factor_index, part)]
        )
        signs.append(-1 if part == "im" else 1)
    if mutation == "break_reality_permutation":
        targets[0] = 0
    involutive = all(
        targets[targets[index]] == index
        and signs[index] * signs[targets[index]] == 1
        for index in range(512)
    )
    fixed_points = tuple(
        index for index, target in enumerate(targets) if index == target
    )
    return {
        "basis_count": len(labels),
        "signed_basis_map": len(set(targets)) == 512
        and all(abs(sign) == 1 for sign in signs),
        "involutive": involutive,
        "fixed_points": fixed_points,
        "cycle_count": len(labels) // 2,
    }


def reality_system() -> tuple[sp.Matrix, sp.Matrix]:
    """Return reality equations and a 256-column exact kernel basis."""
    rows: list[list[int]] = []
    transform_columns: list[list[int]] = []
    seen: set[tuple[int, int]] = set()
    for slice_i in range(8):
        for slice_j in range(8):
            reflected_i, reflected_j = 7 - slice_i, 7 - slice_j
            for factor_index in range(4):
                real_row = [0] * 512
                imaginary_row = [0] * 512
                real_row[parameter_index(slice_i, slice_j, factor_index, 0)] += 1
                real_row[
                    parameter_index(reflected_i, reflected_j, factor_index, 0)
                ] -= 1
                imaginary_row[
                    parameter_index(slice_i, slice_j, factor_index, 1)
                ] += 1
                imaginary_row[
                    parameter_index(reflected_i, reflected_j, factor_index, 1)
                ] += 1
                rows.extend((real_row, imaginary_row))
            if (slice_i, slice_j) in seen:
                continue
            seen.add((slice_i, slice_j))
            seen.add((reflected_i, reflected_j))
            for factor_index in range(4):
                for imaginary, reflected_sign in ((0, 1), (1, -1)):
                    column = [0] * 512
                    column[
                        parameter_index(slice_i, slice_j, factor_index, imaginary)
                    ] = 1
                    column[
                        parameter_index(
                            reflected_i, reflected_j, factor_index, imaginary
                        )
                    ] = reflected_sign
                    transform_columns.append(column)
    reality = sp.Matrix(rows)
    transform = sp.Matrix(
        512, 256, lambda row, column: transform_columns[column][row]
    )
    return reality, transform


def global_hermiticity_matrix(fixture: Fixture) -> sp.Matrix:
    """The 16^2 real equations for K_A=K_A^H in 512 real coordinates.

    The convention is the Block 108 left placement
    ``K_A[r,s]=conjugate((A G)[positive[r], reflected[s]])``.
    """
    if not all(sp.im(value) == 0 for value in fixture.propagator):
        raise AssertionError("the exact fixture propagator must be real")
    factors = spatial_factors()
    base_rows: dict[tuple[int, int, int, int], tuple[sp.Expr, ...]] = {}
    for positive_row in range(16):
        slice_i = 4 + positive_row // 4
        space_i = positive_row % 4
        for slice_j in range(8):
            for factor_index, factor in enumerate(factors):
                values = []
                for reflected_column in range(16):
                    value = sum(
                        factor[space_i, space_j]
                        * fixture.propagator[
                            4 * slice_j + space_j,
                            fixture.reflected[reflected_column],
                        ]
                        for space_j in range(4)
                    )
                    values.append(sp.cancel(value))
                base_rows[(slice_i, slice_j, factor_index, positive_row)] = tuple(
                    values
                )

    rows: list[list[sp.Expr]] = []
    for row in range(16):
        diagonal_equation = [sp.Integer(0)] * 512
        slice_i = 4 + row // 4
        for slice_j in range(8):
            for factor_index in range(4):
                coordinate = parameter_index(slice_i, slice_j, factor_index, 1)
                diagonal_equation[coordinate] = -base_rows[
                    (slice_i, slice_j, factor_index, row)
                ][row]
        rows.append(diagonal_equation)

        for column in range(row + 1, 16):
            real_equation = [sp.Integer(0)] * 512
            imaginary_equation = [sp.Integer(0)] * 512
            row_slice = 4 + row // 4
            column_slice = 4 + column // 4
            for slice_j in range(8):
                for factor_index in range(4):
                    row_base = base_rows[
                        (row_slice, slice_j, factor_index, row)
                    ][column]
                    column_base = base_rows[
                        (column_slice, slice_j, factor_index, column)
                    ][row]
                    real_equation[
                        parameter_index(row_slice, slice_j, factor_index, 0)
                    ] += row_base
                    real_equation[
                        parameter_index(column_slice, slice_j, factor_index, 0)
                    ] -= column_base
                    imaginary_equation[
                        parameter_index(row_slice, slice_j, factor_index, 1)
                    ] -= row_base
                    imaginary_equation[
                        parameter_index(column_slice, slice_j, factor_index, 1)
                    ] -= column_base
            rows.extend((real_equation, imaginary_equation))
    return sp.Matrix(rows)


@dataclass(frozen=True)
class GlobalLinearCertificate:
    hermiticity: sp.Matrix
    hermiticity_rank_on_reality: int
    joint_rank: int
    dimension: int


def global_linear_certificate(
    fixture: Fixture, transform: sp.Matrix
) -> GlobalLinearCertificate:
    hermiticity = global_hermiticity_matrix(fixture)
    reduced = hermiticity * transform
    reduced_rank = exact_rank(reduced)
    return GlobalLinearCertificate(
        hermiticity,
        reduced_rank,
        256 + reduced_rank,
        256 - reduced_rank,
    )


def coordinates_to_matrix(coordinates: sp.Matrix) -> sp.Matrix:
    if coordinates.shape != (512, 1):
        raise ValueError("global coordinate vector must be 512x1")
    factors = spatial_factors()
    result = sp.zeros(SIZE, SIZE)
    for slice_i in range(8):
        for slice_j in range(8):
            block = sp.zeros(4, 4)
            for factor_index, factor in enumerate(factors):
                coefficient = (
                    coordinates[parameter_index(slice_i, slice_j, factor_index, 0)]
                    + I
                    * coordinates[
                        parameter_index(slice_i, slice_j, factor_index, 1)
                    ]
                )
                if coefficient != 0:
                    block += coefficient * factor
            result[
                4 * slice_i : 4 * (slice_i + 1),
                4 * slice_j : 4 * (slice_j + 1),
            ] = block
    return result


ASTAR_SIGNS = (1, -1, 1, -1, -1, 1, -1, 1)
UNDRESSED_DEFECT = sp.Rational(
    2100468154772736499016437760573154473873400000,
    61391349876435377016600254323619839508354485363,
)
PRIMARY_NEGATIVE_MINOR = sp.Rational(
    -33333963283450197824471164187210075293672388640,
    61391349876435377016600254323619839508354485363,
)
SECOND_NEGATIVE_MINOR = sp.Rational(
    -30292616102306685544040740640984160,
    68872508036021339265532585819028911,
)


def global_candidate(signs: tuple[int, ...] = ASTAR_SIGNS) -> sp.Matrix:
    """Exact anti-diagonal dressed-reflection involution A*."""
    dressing = sp.zeros(SIZE, SIZE)
    spatial_parity = spatial_factors()[1]
    for slice_i, sign in enumerate(signs):
        slice_j = 7 - slice_i
        dressing[
            4 * slice_i : 4 * (slice_i + 1),
            4 * slice_j : 4 * (slice_j + 1),
        ] = sign * spatial_parity
    return dressing


def astar_ambient_coordinates(signs: tuple[int, ...] = ASTAR_SIGNS) -> sp.Matrix:
    coordinates = sp.zeros(512, 1)
    for slice_i, sign in enumerate(signs):
        coordinates[parameter_index(slice_i, 7 - slice_i, 1, 0)] = sign
    return coordinates


def dressed_gram(dressing: sp.Matrix, fixture: Fixture) -> sp.Matrix:
    return history_gram(
        dressing * fixture.propagator,
        fixture.positive,
        fixture.reflected,
    )


def leading_minors(matrix: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.factor(matrix[:size, :size].det(method="domain-ge"))
        for size in range(1, matrix.rows + 1)
    )


def inertia_from_nonzero_leading_minors(
    minors: tuple[sp.Expr, ...]
) -> tuple[int, int, int]:
    previous = sp.Integer(1)
    positive = 0
    negative = 0
    for minor in minors:
        if minor == 0:
            raise AssertionError("leading-minor inertia certificate is singular")
        pivot = sp.factor(minor / previous)
        positive += int(bool(pivot > 0))
        negative += int(bool(pivot < 0))
        previous = minor
    return positive, negative, 0


def leading_sign_changes(minors: tuple[sp.Expr, ...]) -> int:
    signs = [1] + [1 if minor > 0 else -1 for minor in minors]
    return sum(left != right for left, right in zip(signs, signs[1:]))


@dataclass(frozen=True)
class AstarCertificate:
    matrix: sp.Matrix
    gram: sp.Matrix
    leading: tuple[sp.Expr, ...]
    inertia: tuple[int, int, int]
    selected_reality: bool
    selected_hermiticity: bool
    selected_involution: bool
    sign_symmetry: bool
    sign_products: bool
    expected_inertia: tuple[int, int, int]


def astar_certificate(fixture: Fixture, mutation: str) -> AstarCertificate:
    canonical = global_candidate()
    gram = dressed_gram(canonical, fixture)
    leading = leading_minors(gram)
    inertia = inertia_from_nonzero_leading_minors(leading)

    selected_signs = list(ASTAR_SIGNS)
    if mutation == "break_astar_signs":
        selected_signs[0] *= -1
    selected = global_candidate(tuple(selected_signs))
    selected_gram = dressed_gram(selected, fixture)
    expected_inertia = (
        (16, 0, 0) if mutation == "claim_astar_positive" else (8, 8, 0)
    )
    return AstarCertificate(
        canonical,
        gram,
        leading,
        inertia,
        matrix_equal(
            fixture.reflection * selected.conjugate() * fixture.reflection,
            selected,
        ),
        matrix_equal(selected_gram, selected_gram.H),
        matrix_equal(selected * selected, sp.eye(SIZE)),
        all(selected_signs[index] == selected_signs[7 - index] for index in range(8)),
        all(
            selected_signs[index] * selected_signs[7 - index] == 1
            for index in range(8)
        ),
        expected_inertia,
    )


def anti_diagonal_embedding() -> sp.Matrix:
    embedding = sp.zeros(512, 64)
    for slice_i in range(8):
        slice_j = 7 - slice_i
        for factor_index in range(4):
            for imaginary in (0, 1):
                local = 8 * slice_i + 2 * factor_index + imaginary
                embedding[
                    parameter_index(slice_i, slice_j, factor_index, imaginary),
                    local,
                ] = 1
    return embedding


def matrix_block(matrix: sp.Matrix, slice_i: int, slice_j: int) -> sp.Matrix:
    return matrix[
        4 * slice_i : 4 * (slice_i + 1),
        4 * slice_j : 4 * (slice_j + 1),
    ]


def monic_nonzero_entries(
    matrix: sp.Matrix, variable: sp.Symbol
) -> tuple[sp.Expr, ...]:
    polynomials: dict[str, sp.Expr] = {}
    for entry in matrix:
        expanded = sp.expand(entry)
        if expanded == 0:
            continue
        monic = sp.Poly(expanded, variable, domain=sp.QQ).monic().as_expr()
        polynomials[sp.srepr(monic)] = monic
    return tuple(polynomials.values())


def involution_groebner_certificate(
    generator: sp.Matrix,
) -> tuple[tuple[sp.Expr, ...], tuple[tuple[sp.Expr], ...], bool]:
    lam = sp.Symbol("lambda", real=True)
    pair_bases: list[sp.Expr] = []
    every_pair_reduces = True
    for slice_i in range(4):
        slice_j = 7 - slice_i
        left = matrix_block(lam * generator, slice_i, slice_j)
        right = matrix_block(lam * generator, slice_j, slice_i)
        equations = monic_nonzero_entries(
            (left * right - sp.eye(4)).col_join(right * left - sp.eye(4)),
            lam,
        )
        pair_groebner = sp.groebner(equations, lam, order="lex", domain=sp.QQ)
        basis = tuple(poly.monic().as_expr() for poly in pair_groebner.polys)
        every_pair_reduces &= basis == (lam**2 - 1,)
        pair_bases.extend(basis)
    total = sp.groebner(pair_bases, lam, order="lex", domain=sp.QQ)
    total_basis = tuple(poly.monic().as_expr() for poly in total.polys)
    solutions = tuple(sp.solve_poly_system(total_basis, lam))
    return total_basis, solutions, every_pair_reduces and total.is_zero_dimensional


@dataclass(frozen=True)
class AntiDiagonalCertificate:
    reality_rank: int
    primary_h_rank: int
    second_h_rank: int
    primary_joint_rank: int
    second_joint_rank: int
    generator_member_both: bool
    parametrization_exact: bool
    groebner_basis: tuple[sp.Expr, ...]
    expected_groebner_basis: tuple[sp.Expr, ...]
    solutions: tuple[tuple[sp.Expr], ...]
    pair_reduction: bool
    primary_minus_inertia: tuple[int, int, int]
    second_plus_inertia: tuple[int, int, int]
    second_minus_inertia: tuple[int, int, int]
    pinned_negative_minors: bool
    both_branches_indefinite: bool
    expected_disjoint: bool


def anti_diagonal_certificate(
    primary: Fixture,
    second: Fixture,
    reality: sp.Matrix,
    primary_linear: GlobalLinearCertificate,
    second_linear: GlobalLinearCertificate,
    astar: AstarCertificate,
    mutation: str,
) -> AntiDiagonalCertificate:
    embedding = anti_diagonal_embedding()
    restricted_reality = reality * embedding
    primary_h = primary_linear.hermiticity * embedding
    second_h = second_linear.hermiticity * embedding
    primary_joint = restricted_reality.col_join(primary_h)
    second_joint = restricted_reality.col_join(second_h)
    local_generator = sp.zeros(64, 1)
    for slice_i, sign in enumerate(ASTAR_SIGNS):
        local_generator[8 * slice_i + 2] = sign
    ambient_generator = embedding * local_generator
    generator = coordinates_to_matrix(ambient_generator)
    total_basis, solutions, pair_reduction = involution_groebner_certificate(
        generator
    )
    expected_basis = (
        (sp.Symbol("lambda", real=True) ** 2 + 1,)
        if mutation == "break_groebner_reduction"
        else (sp.Symbol("lambda", real=True) ** 2 - 1,)
    )

    primary_minus_leading = tuple(
        (-1) ** size * minor for size, minor in enumerate(astar.leading, start=1)
    )
    primary_minus_inertia = inertia_from_nonzero_leading_minors(
        primary_minus_leading
    )
    second_plus_gram = dressed_gram(generator, second)
    second_plus_leading = leading_minors(second_plus_gram)
    second_plus_inertia = inertia_from_nonzero_leading_minors(second_plus_leading)
    second_minus_leading = tuple(
        (-1) ** size * minor
        for size, minor in enumerate(second_plus_leading, start=1)
    )
    second_minus_inertia = inertia_from_nonzero_leading_minors(
        second_minus_leading
    )
    both_indefinite = all(
        inertia == (8, 8, 0)
        for inertia in (
            astar.inertia,
            primary_minus_inertia,
            second_plus_inertia,
            second_minus_inertia,
        )
    )
    pinned_negative = (
        astar.gram[0, 0] == PRIMARY_NEGATIVE_MINOR
        and any(
            second_plus_gram[index, index] == SECOND_NEGATIVE_MINOR
            for index in range(16)
        )
        and any(-astar.gram[index, index] < 0 for index in range(16))
        and any(-second_plus_gram[index, index] < 0 for index in range(16))
    )
    return AntiDiagonalCertificate(
        exact_rank(restricted_reality),
        exact_rank(primary_h),
        exact_rank(second_h),
        exact_rank(primary_joint),
        exact_rank(second_joint),
        matrix_equal(primary_joint * local_generator, sp.zeros(primary_joint.rows, 1))
        and matrix_equal(
            second_joint * local_generator, sp.zeros(second_joint.rows, 1)
        ),
        matrix_equal(generator, global_candidate()),
        total_basis,
        expected_basis,
        solutions,
        pair_reduction,
        primary_minus_inertia,
        second_plus_inertia,
        second_minus_inertia,
        pinned_negative,
        both_indefinite,
        mutation != "claim_antidiagonal_positive",
    )


def undressed_certificate(fixture: Fixture, mutation: str) -> dict[str, object]:
    identity = sp.eye(SIZE)
    gram = dressed_gram(identity, fixture)
    excluded = not matrix_equal(gram, gram.H)
    expected_excluded = mutation != "claim_undressed_included"
    return {
        "reality": matrix_equal(
            fixture.reflection * identity.conjugate() * fixture.reflection,
            identity,
        ),
        "excluded": excluded,
        "expected_excluded": expected_excluded,
        "defect": sp.factor(max_abs_entry(gram - gram.H)),
    }


# Exact real coefficients of the pinned K_A=I16 representative.  The order is
# output-positive-slice/source-slice/spatial-factor; each coefficient's paired
# imaginary coordinate is pinned to zero, giving a 256-real-coordinate vector.
POSITIVE_FIBER_REAL_COEFFICIENTS = (
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(-601, 1152),
    sp.Rational(0, 1),
    sp.Rational(13, 512),
    sp.Rational(-13, 512),
    sp.Rational(601, 1280),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(601, 1152),
    sp.Rational(601, 1152),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(-65, 1152),
    sp.Rational(65, 1152),
    sp.Rational(-313, 576),
    sp.Rational(0, 1),
    sp.Rational(13, 512),
    sp.Rational(-13, 512),
    sp.Rational(313, 640),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(-21, 32),
    sp.Rational(601, 1152),
    sp.Rational(0, 1),
    sp.Rational(13, 512),
    sp.Rational(13, 512),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(65, 2304),
    sp.Rational(65, 2304),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(-313, 576),
    sp.Rational(0, 1),
    sp.Rational(13, 512),
    sp.Rational(-13, 512),
    sp.Rational(313, 640),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(313, 576),
    sp.Rational(313, 576),
    sp.Rational(0, 1),
    sp.Rational(13, 512),
    sp.Rational(13, 512),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(436809039108148887533657557, 804232781120185338452680960),
    sp.Rational(0, 1),
    sp.Rational(
        -274883293329205100057146567350659375,
        11729321357571487073092949075073000096,
    ),
    sp.Rational(
        -33553212886792720271322184503961802111,
        50472385359755030117824566557535388992,
    ),
    sp.Rational(313, 576),
    sp.Rational(0, 1),
    sp.Rational(13, 512),
    sp.Rational(13, 512),
    sp.Rational(250275225864092239893875, 20105819528004633461317024),
    sp.Rational(0, 1),
    sp.Rational(46696418743926259989987865, 482539668672111203071608576),
    sp.Rational(23270527433258866903237225, 1447619006016333609214825728),
    sp.Rational(540061969291618982716173449, 723809503008166804607412864),
    sp.Rational(0, 1),
    sp.Rational(2314083242220299018095675, 40211639056009266922634048),
    sp.Rational(2314083242220299018095675, 40211639056009266922634048),
    sp.Rational(-25026612019895715356918807, 25132274410005791826646280),
    sp.Rational(0, 1),
    sp.Rational(
        -1093045962325603246948958346437854715,
        11729321357571487073092949075073000096,
    ),
    sp.Rational(
        19286823944372851229685807615056984221,
        25236192679877515058912283278767694496,
    ),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
    sp.Rational(0, 1),
)
POSITIVE_FIBER_PARAMETER_VECTOR = tuple(
    coordinate
    for real_coordinate in POSITIVE_FIBER_REAL_COEFFICIENTS
    for coordinate in (real_coordinate, sp.Integer(0))
)


def positive_fiber_mapping(fixture: Fixture) -> tuple[sp.Matrix, sp.Matrix]:
    factors = spatial_factors()
    mapping = sp.zeros(64, 32)
    right_hand_side = sp.zeros(64, 4)
    for space in range(4):
        for column, reflected_index in enumerate(fixture.reflected):
            row = 16 * space + column
            for output_slice in range(4):
                right_hand_side[row, output_slice] = int(
                    4 * output_slice + space == column
                )
            for slice_j in range(8):
                for factor_index, factor in enumerate(factors):
                    mapping[row, 4 * slice_j + factor_index] = sum(
                        factor[space, source_space]
                        * fixture.propagator[
                            4 * slice_j + source_space, reflected_index
                        ]
                        for source_space in range(4)
                    )
    return mapping, right_hand_side


@dataclass(frozen=True)
class PositiveFiberCertificate:
    mapping_rank: int
    rank: int
    augmented_rank: int
    dimension: int
    expected_dimension: int
    parameter_count: int
    reality: bool
    representative_exact: bool
    square_defect_rank: int


def positive_fiber_certificate(
    fixture: Fixture, mutation: str
) -> PositiveFiberCertificate:
    mapping, right_hand_side = positive_fiber_mapping(fixture)
    mapping_rank = exact_rank(mapping)
    local_augmented_rank = exact_rank(mapping.row_join(right_hand_side))
    full_rank = 8 * mapping_rank
    full_augmented_rank = (
        full_rank if local_augmented_rank == mapping_rank else full_rank + 1
    )
    coefficients = list(POSITIVE_FIBER_REAL_COEFFICIENTS)
    if mutation == "break_fiber_representative":
        coefficients[0] += 1

    factors = spatial_factors()
    positive_half = sp.zeros(SIZE, SIZE)
    offset = 0
    for output_slice in range(4):
        slice_i = 4 + output_slice
        for slice_j in range(8):
            block = sp.zeros(4, 4)
            for factor in factors:
                block += coefficients[offset] * factor
                offset += 1
            positive_half[
                4 * slice_i : 4 * (slice_i + 1),
                4 * slice_j : 4 * (slice_j + 1),
            ] = block
    matrix = (
        positive_half
        + fixture.reflection * positive_half.conjugate() * fixture.reflection
    )
    gram = dressed_gram(matrix, fixture)
    return PositiveFiberCertificate(
        mapping_rank,
        full_rank,
        full_augmented_rank,
        256 - full_rank,
        36 if mutation == "claim_fiber_dim_36" else 72,
        len(POSITIVE_FIBER_PARAMETER_VECTOR),
        matrix_equal(
            fixture.reflection * matrix.conjugate() * fixture.reflection,
            matrix,
        ),
        matrix_equal(gram, sp.eye(16)),
        exact_rank(matrix * matrix - sp.eye(SIZE)),
    )


def block107_homogeneous_window_system(fixture: Fixture) -> sp.Matrix:
    raw = history_gram(
        fixture.propagator, fixture.positive[:8], fixture.reflected[:8]
    )
    basis: list[sp.Matrix] = []
    for slice_i in range(2):
        for slice_j in range(2):
            for factor in spatial_factors():
                for scalar in (sp.Integer(1), I):
                    item = sp.zeros(8, 8)
                    item[
                        4 * slice_i : 4 * (slice_i + 1),
                        4 * slice_j : 4 * (slice_j + 1),
                    ] = scalar * factor
                    basis.append(item)

    rows: list[list[sp.Expr]] = []
    for row in range(8):
        diagonal_row: list[sp.Expr] = []
        for item in basis:
            _, imaginary = sp.expand_complex((item * raw)[row, row]).as_real_imag()
            diagonal_row.append(sp.expand(imaginary))
        rows.append(diagonal_row)
        for column in range(row + 1, 8):
            real_row: list[sp.Expr] = []
            imaginary_row: list[sp.Expr] = []
            for item in basis:
                product = item * raw
                difference = sp.expand(
                    product[row, column] - sp.conjugate(product[column, row])
                )
                real, imaginary = sp.expand_complex(difference).as_real_imag()
                real_row.append(sp.expand(real))
                imaginary_row.append(sp.expand(imaginary))
            rows.extend((real_row, imaginary_row))
    return sp.Matrix(rows)


def window_invisibility_certificate(
    fixture: Fixture, dressing: sp.Matrix, mutation: str
) -> dict[str, object]:
    central_indices = fixture.positive[:8]
    central_block = dressing.extract(central_indices, central_indices)
    central_zero = matrix_equal(central_block, sp.zeros(8, 8))
    homogeneous = block107_homogeneous_window_system(fixture)
    zero_coordinates = sp.zeros(32, 1)
    claimed_zero = False if mutation == "claim_window_visible" else central_zero
    return {
        "central_zero": claimed_zero,
        "homogeneous_rank": exact_rank(homogeneous),
        "homogeneous_dimension": 32 - exact_rank(homogeneous),
        "zero_member": matrix_equal(
            homogeneous * zero_coordinates, sp.zeros(homogeneous.rows, 1)
        ),
    }


def support_certificate(mutation: str) -> dict[str, object]:
    signs = list(ASTAR_SIGNS)
    dressing = global_candidate()
    if mutation == "break_astar_support":
        dressing[0:4, 28:32] = sp.zeros(4, 4)
        signs[0] = 0
    occupied = tuple(
        (slice_i, slice_j)
        for slice_i in range(8)
        for slice_j in range(8)
        if not matrix_equal(
            matrix_block(dressing, slice_i, slice_j), sp.zeros(4, 4)
        )
    )
    magnitudes = {
        sp.Abs(entry) for entry in dressing if sp.expand(entry) != 0
    }
    spatial_parity = spatial_factors()[1]
    parity_blocks = all(
        matrix_equal(
            matrix_block(dressing, slice_i, 7 - slice_i),
            signs[slice_i] * spatial_parity,
        )
        for slice_i in range(8)
    )
    return {
        "occupied": occupied,
        "row_slices": {slice_i for slice_i, _ in occupied},
        "column_slices": {slice_j for _, slice_j in occupied},
        "magnitudes": magnitudes,
        "parity_blocks": parity_blocks,
    }


SCOPE_KEYS = (
    "global_feasibility",
    "involution",
    "indefinite",
    "positive_fiber",
    "window_invisible",
    "joint_variety",
    "transporter_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity",
    "adm",
    "n1_n8",
    "walls",
    "n5_resolution",
)


def scope_certificate(mutation: str) -> dict[str, bool]:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return {key: False for key in SCOPE_KEYS}
    note = " ".join(raw_note.lower().split())
    result = {
        "global_feasibility": "global feasibility" in note,
        "involution": "exact involution" in note or "dressed reflection" in note,
        "indefinite": "inertia (8,8,0)" in note or "exactly indefinite" in note,
        "positive_fiber": "positive fiber" in note,
        "window_invisible": (
            "window-invisible" in note or "invisible to the central window" in note
        ),
        "joint_variety": (
            "joint variety" in note or "involution and positivity" in note
        ),
        "transporter_boundary": "not a transporter impossibility" in note,
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero"
        in note,
        "gravity": "gravity constraint quotient remains unexecuted" in note,
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "walls": "w1" in note,
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
    }
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_adm_link_derived":
        result["adm"] = False
    if mutation == "claim_curved_os_closed":
        result["transporter_boundary"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_obligation_retirement":
        result["zero_retirement"] = False
    return result


MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_reality_permutation",
    "claim_wrong_global_dim",
    "claim_undressed_included",
    "break_astar_signs",
    "claim_astar_positive",
    "break_groebner_reduction",
    "claim_antidiagonal_positive",
    "claim_fiber_dim_36",
    "break_fiber_representative",
    "claim_window_visible",
    "break_astar_support",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_adm_link_derived",
    "claim_curved_os_closed",
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
        "A-authority-and-Block108-parent",
        "current axioms, registries, ancestry, and the Block108 parent triple are content-bound",
        authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["ancestor_107"]
        and authority["ancestor_106"]
        and authority["ancestor_105"]
        and authority["ancestor_104"]
        and authority["ancestor_103"]
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    primary = fixture_data(sp.Rational(5, 13))
    second = fixture_data(sp.Rational(3, 5))
    permutation = reality_permutation_certificate(mutation)
    reality, transform = reality_system()
    primary_linear = global_linear_certificate(primary, transform)
    second_linear = global_linear_certificate(second, transform)
    expected_dimension = 66 if mutation == "claim_wrong_global_dim" else 132
    checks.check(
        "B-global-feasibility",
        "the fixed-point-free reality permutation gives rank 256 and both fixtures give rank 380",
        permutation["basis_count"] == 512
        and permutation["signed_basis_map"]
        and permutation["involutive"]
        and permutation["fixed_points"] == ()
        and permutation["cycle_count"] == 256
        and matrix_equal(reality * transform, sp.zeros(512, 256))
        and exact_rank(transform) == 256
        and primary_linear.hermiticity_rank_on_reality == 124
        and second_linear.hermiticity_rank_on_reality == 124
        and primary_linear.joint_rank == second_linear.joint_rank == 380
        and primary_linear.dimension
        == second_linear.dimension
        == expected_dimension,
        f"reality/H/joint/dim=256/124/380/{primary_linear.dimension} at c=5/13 and c=3/5",
    )

    undressed = undressed_certificate(primary, mutation)
    checks.check(
        "C-undressed-exclusion",
        "A=I obeys reality but its pinned Block108 defect excludes it from the joint space",
        undressed["reality"]
        and undressed["excluded"] == undressed["expected_excluded"]
        and undressed["defect"] == UNDRESSED_DEFECT,
    )

    astar = astar_certificate(primary, mutation)
    checks.check(
        "D-exact-involution-A-star",
        "A* is an exact real dressed reflection with Hermitian Gram and inertia (8,8,0)",
        astar.selected_reality
        and astar.selected_hermiticity
        and astar.selected_involution
        and astar.sign_symmetry
        and astar.sign_products
        and len(astar.leading) == 16
        and all(minor != 0 for minor in astar.leading)
        and astar.inertia == astar.expected_inertia
        and leading_sign_changes(astar.leading) == 8
        and astar.leading[0] == PRIMARY_NEGATIVE_MINOR,
        f"Delta1={astar.leading[0]}; inertia={astar.inertia}; sign changes=8",
    )

    anti = anti_diagonal_certificate(
        primary,
        second,
        reality,
        primary_linear,
        second_linear,
        astar,
        mutation,
    )
    checks.check(
        "E-anti-diagonal-classification",
        "the 64-real anti-diagonal class is lambda A* with variety {+A*,-A*}, both indefinite",
        anti.reality_rank == 32
        and anti.primary_h_rank == anti.second_h_rank == 31
        and anti.primary_joint_rank == anti.second_joint_rank == 63
        and anti.generator_member_both
        and anti.parametrization_exact
        and anti.groebner_basis == anti.expected_groebner_basis
        and anti.solutions == ((sp.Integer(-1),), (sp.Integer(1),))
        and anti.pair_reduction
        and anti.pinned_negative_minors
        and anti.both_branches_indefinite
        and anti.expected_disjoint,
        f"rank/dim=63/1; Groebner={anti.groebner_basis}; both fixtures and branches have inertia (8,8,0)",
    )

    fiber = positive_fiber_certificate(primary, mutation)
    checks.check(
        "F-positive-fiber",
        "K_A=I16 has exact rank 184 and a 72-dimensional real fiber with a pinned non-involution",
        fiber.mapping_rank == 23
        and fiber.rank == fiber.augmented_rank == 184
        and fiber.dimension == fiber.expected_dimension
        and fiber.parameter_count == 256
        and fiber.reality
        and fiber.representative_exact
        and fiber.square_defect_rank == 32,
        f"rank[M]=rank[M|b]=184; dim={fiber.dimension}; rank(A^2-I)={fiber.square_defect_rank}",
    )

    window = window_invisibility_certificate(primary, astar.matrix, mutation)
    checks.check(
        "G-window-invisibility",
        "A* has zero central {0,1} window block, the zero Block107 homogeneous solution",
        window["central_zero"]
        and window["homogeneous_rank"] == 24
        and window["homogeneous_dimension"] == 8
        and window["zero_member"],
    )

    support = support_certificate(mutation)
    checks.check(
        "H-structure-and-support",
        "A* occupies all eight anti-diagonal slice-blocks at magnitude one with x-parity structure",
        support["occupied"] == tuple((index, 7 - index) for index in range(8))
        and support["row_slices"] == set(range(8))
        and support["column_slices"] == set(range(8))
        and support["magnitudes"] == {sp.Integer(1)}
        and support["parity_blocks"],
    )

    scope = scope_certificate(mutation)
    checks.check(
        "I-scope",
        "the note preserves the bounded joint-variety, N1--N8, W1, N5, ADM, gravity, audit, and TOE walls",
        all(scope.values()),
    )

    print(
        "EXACT_WITNESSES: "
        f"undressed_defect={undressed['defect']}; primary_Delta1={astar.leading[0]}; "
        f"second_K88={SECOND_NEGATIVE_MINOR}"
    )
    print(
        f"AXIOM_AUTHORITY: origin/main={authority['main']} axiom={CURRENT_AXIOM_BLOB} "
        f"registry={CURRENT_REGISTRY_BLOB}; Block108 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: exact feasibility, involution, classification, fiber, and invisibility identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: both shear fixtures certify the same dimensions, variety, and inertia"
    )
    print(
        "per_block: the exact involution occupies every slice at magnitude one while its central window block vanishes"
    )
    print(
        "lattice_wide: checked and not executed — the joint involution-positivity variety on the full 132-dimensional space, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the global dressing space is richly feasible and contains an exact window-invisible dressed-reflection involution and a positive fiber, but on the anti-diagonal class involution and positivity are exactly disjoint"
    )
    print(
        "DECISION_CUT: advance the joint variety on the full global space and the modular selection; reject undressed, seam-local, and anti-diagonal-only routes"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
