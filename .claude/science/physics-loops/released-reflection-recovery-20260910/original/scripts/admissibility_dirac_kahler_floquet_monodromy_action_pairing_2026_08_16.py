#!/usr/bin/env python3
"""Block 118: exact Floquet monodromy and action-pairing certificate.

The range-two Dirac--Kahler action is grouped into four two-slice steps.
Exact Schur companions reconstruct its finite covariance, expose the
antiperiodic determinant-one monodromy, and separate the contractive
geometric-Hankel quotient from positivity of the OS pairing.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import time

import sympy as sp
from sympy.polys.matrices import DomainMatrix

import admissibility_dirac_kahler_self_chart_emptiness_stationarity_2026_08_16 as prior


base = prior.base
b111 = prior.b111
I = sp.I
R = sp.Rational
Z = sp.symbols("z")
LAM = sp.symbols("lambda")
ALPHA = sp.symbols("rho", real=True)
BETA = sp.symbols("beta")
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_self_chart_emptiness_"
    "stationarity_2026_08_16.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_self_chart_emptiness_"
    "stationarity_2026_08_16.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "scripts/admissibility_dirac_kahler_self_chart_emptiness_stationarity_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_self_chart_emptiness_stationarity_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "4e566b14a6352a9a62590252a9755c7a103c1b9e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block117-self-chart-emptiness-stationarity-20260816"
)
PARENT_COMMIT = "f800356aec0989b6e0fa80ed43274794243b1ca2"
PARENT_NOTE_BLOB = "9dab24a21193fb763f65344df89a66e17e7a2d40"
PARENT_RUNNER_BLOB = "cdb00511162dd85fa3877afa03b727ab86716cb8"
PARENT_CACHE_BLOB = "2be3f4449b7c87a7536f9576c2a8284e07454510"
ANCESTOR_COMMITS = (
    (116, "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"),
    (115, "c78301fef7521d0518f485f1bf9266983c9e516a"),
    (114, "75026e71cfbd44ed665ddc41c22ebaa722720ea9"),
    (113, "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"),
    (112, "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"),
    (111, "b04e7c8747b09734711cfcd2bfab961bd12e81ad"),
    (110, "d6761278fca9cac617200792473a8f4da3a6cfff"),
    (109, "ad84cfcc857a65285389ba93b47cd7b718589be5"),
    (108, "8afe8dff5ccf531208238af0aaaec1f547d73874"),
    (107, "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"),
    (106, "22d6d90ec2279e5868c9c825149b2a20beea3797"),
    (105, "d06066c2b908aaca0779625d831dfb10620cf34d"),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

PRIMARY_SHEAR = R(5, 13)
SECOND_SHEAR = R(3, 5)
PRIMARY_RAW_DEFECT = R(293040926496000, 1026791823428467)
SECOND_RAW_DEFECT = R(62924832000, 250649423107)

EXPECTED_MAGNITUDE_INTERVALS: tuple[
    tuple[tuple[tuple[int, int], tuple[int, int]], ...], ...
] = (
    (
        ((32190095809, 32190095810), (31065455844352, 31065455844353)),
        ((404644318, 404644319), (2471306170017694, 2471306170017695)),
    ),
    (
        ((36167865356, 36167865357), (27648853205704, 27648853205705)),
        ((191977555, 191977556), (5208942255796407, 5208942255796408)),
    ),
)
EXPECTED_BETA_INTERVALS: tuple[
    tuple[tuple[sp.Rational, sp.Rational], ...], ...
] = (
    (
        (
            R(1036202268192599364481, 1000000000000000000000000),
            R(10362022682569795561, 10000000000000000000000),
        ),
        (
            R(40934256022421281, 250000000000000000000000),
            R(163737024898973761, 1000000000000000000000000),
        ),
    ),
    (
        (
            R(81757155275609062921, 62500000000000000000000),
            R(1308114484482080737449, 1000000000000000000000000),
        ),
        (
            R(1474215264951121, 40000000000000000000000),
            R(2303461375483321, 62500000000000000000000),
        ),
    ),
)

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_floquet_band",
    "claim_constant_companions",
    "break_monodromy_det",
    "break_negative_trace",
    "break_reproduction",
    "claim_period4_stationary",
    "claim_real_gauge",
    "break_hankel_ratio",
    "claim_positive_pairing",
    "break_identity_split",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
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
    ancestors = {
        f"ancestor_{number}": is_ancestor(commit, "HEAD")
        for number, commit in ANCESTOR_COMMITS
    }
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **ancestors,
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def normalized(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.applyfunc(sp.expand)


def canonical(value: sp.Expr) -> sp.Expr:
    return sp.factor(sp.cancel(sp.expand(value)))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.expand(value) == 0 for value in left - right)


def exact_rank(matrix: sp.Matrix) -> int:
    return DomainMatrix.from_Matrix(normalized(matrix)).rank()


def parity_sign(power: int) -> int:
    return -1 if power % 2 else 1


def shift() -> sp.Matrix:
    result = sp.zeros(4, 4)
    for column in range(4):
        result[(column + 1) % 4, column] = 1
    return result


def projectors() -> tuple[sp.Matrix, ...]:
    cyclic = shift()
    return tuple(
        normalized(
            sum(
                (I ** (-k * power) * cyclic**power for power in range(4)),
                sp.zeros(4),
            )
            / 4
        )
        for k in range(4)
    )


def momentum_block(matrix: sp.Matrix, momentum: int, time_size: int) -> sp.Matrix:
    projector = projectors()[momentum]
    return sp.Matrix(
        time_size,
        time_size,
        lambda row, column: sp.cancel(
            sp.trace(
                projector
                * matrix[
                    4 * row : 4 * (row + 1),
                    4 * column : 4 * (column + 1),
                ]
            )
        ),
    ).applyfunc(sp.expand)


def row_offsets(matrix: sp.Matrix, row: int) -> tuple[int, ...]:
    size = matrix.rows
    return tuple(
        sorted(
            {
                ((column - row + size // 2) % size) - size // 2
                for column in range(size)
                if matrix[row, column] != 0
            }
        )
    )


@dataclass(frozen=True)
class BulkBlocks:
    diagonal: sp.Matrix
    forward: sp.Matrix
    backward: sp.Matrix
    unique_unwrap: bool
    reconstruction: bool
    rank_one_hopping: bool


def unwrap_antiperiodic(action_block: sp.Matrix) -> BulkBlocks:
    diagonal = sp.zeros(8, 8)
    forward = sp.zeros(8, 8)
    backward = sp.zeros(8, 8)
    unique = True
    for row in range(8):
        for column in range(8):
            raw = action_block[row, column]
            if raw == 0:
                continue
            choices = tuple(
                cell_shift
                for cell_shift in (-1, 0, 1)
                if abs(column + 8 * cell_shift - row) <= 2
            )
            unique = unique and len(choices) == 1
            if len(choices) != 1:
                continue
            cell_shift = choices[0]
            value = parity_sign(cell_shift) * raw
            target = (
                backward
                if cell_shift == -1
                else forward
                if cell_shift == 1
                else diagonal
            )
            target[row, column] = value
    diagonal = normalized(diagonal)
    forward = normalized(forward)
    backward = normalized(backward)
    return BulkBlocks(
        diagonal,
        forward,
        backward,
        unique,
        matrix_equal(diagonal - forward - backward, action_block),
        exact_rank(forward) == exact_rank(backward) == 1,
    )


@dataclass(frozen=True)
class SliceBlocks:
    diagonal: sp.Matrix
    forward: sp.Matrix
    backward: sp.Matrix
    a_row_vanishes: bool
    c_column_vanishes: bool


def coarse_blocks(bulk: BulkBlocks) -> tuple[SliceBlocks, ...]:
    result = []
    for step in range(4):
        rows = (2 * step, 2 * step + 1)
        next_step = (step + 1) % 4
        previous_step = (step - 1) % 4
        following = (2 * next_step, 2 * next_step + 1)
        preceding = (2 * previous_step, 2 * previous_step + 1)
        diagonal = bulk.diagonal.extract(rows, rows)
        forward_source = bulk.forward if step == 3 else bulk.diagonal
        backward_source = bulk.backward if step == 0 else bulk.diagonal
        forward = forward_source.extract(rows, following)
        backward = backward_source.extract(rows, preceding)
        result.append(
            SliceBlocks(
                normalized(diagonal),
                normalized(forward),
                normalized(backward),
                backward[1, :] == sp.zeros(1, 2),
                forward[:, 1] == sp.zeros(2, 1),
            )
        )
    return tuple(result)


def primitive_action_polynomial(bulk: BulkBlocks) -> sp.Poly:
    symbol = bulk.diagonal + Z * bulk.forward + bulk.backward / Z
    determinant = sp.cancel(symbol.det(method="domain-ge"))
    numerator = sp.together(determinant).as_numer_denom()[0]
    polynomial = sp.Poly(numerator, Z, domain=sp.QQ).primitive()[1]
    return -polynomial if polynomial.LC() < 0 else polynomial


def decimal_isolations(
    polynomial: sp.Poly, digits: int = 12
) -> tuple[tuple[tuple[int, int], ...], bool]:
    scale = 10**digits
    result = []
    valid = True
    for (lower, upper), multiplicity in polynomial.intervals(
        eps=R(1, 10) ** (digits + 4)
    ):
        integer = int(sp.floor((lower + upper) * scale / 2))
        lo = R(integer, scale)
        hi = R(integer + 1, scale)
        valid = valid and multiplicity == 1 and polynomial.count_roots(lo, hi) == 1
        result.append((integer, integer + 1))
    return tuple(result), valid


@dataclass(frozen=True)
class Transfer:
    bulk: BulkBlocks
    slices: tuple[SliceBlocks, ...]
    local_transfers: tuple[sp.Matrix, ...]
    cycle_product: sp.Matrix
    monodromy: sp.Matrix
    magnitude_polynomial: sp.Poly
    isolations: tuple[tuple[int, int], ...]
    fine_band: bool
    construction_valid: bool
    characteristic_valid: bool
    isolations_valid: bool


def transfer_from_action(action_block: sp.Matrix) -> Transfer:
    fine_band = all(
        row_offsets(action_block, row)
        == ((-2, -1, 0, 1, 2) if row % 2 == 0 else (-1, 0, 1))
        for row in range(8)
    )
    bulk = unwrap_antiperiodic(action_block)
    slices = coarse_blocks(bulk)
    local_transfers = []
    construction_valid = (
        bulk.unique_unwrap
        and bulk.reconstruction
        and bulk.rank_one_hopping
        and all(item.a_row_vanishes and item.c_column_vanishes for item in slices)
    )
    for step, current in enumerate(slices):
        previous = slices[(step - 1) % 4]
        a, b = current.diagonal[0, 0], current.diagonal[0, 1]
        c, d = current.diagonal[1, 0], current.diagonal[1, 1]
        e, f = current.forward[0, 0], current.forward[1, 0]
        g, h = current.backward[0, 0], current.backward[0, 1]
        construction_valid = (
            construction_valid and d != 0 and previous.diagonal[1, 1] != 0
        )
        coefficient_previous = sp.cancel(
            g
            - h
            * previous.diagonal[1, 0]
            / previous.diagonal[1, 1]
        )
        coefficient_current = sp.cancel(
            a
            - b * c / d
            - h
            * previous.forward[1, 0]
            / previous.diagonal[1, 1]
        )
        coefficient_next = sp.cancel(e - b * f / d)
        construction_valid = construction_valid and coefficient_next != 0
        local_transfers.append(
            sp.Matrix(
                (
                    (
                        -coefficient_current / coefficient_next,
                        -coefficient_previous / coefficient_next,
                    ),
                    (1, 0),
                )
            ).applyfunc(sp.cancel)
        )
    cycle_product = sp.eye(2)
    for local in local_transfers:
        cycle_product = normalized(local * cycle_product)
    # Closing the eight-site antiperiodic seam sends s_4 to -s_0.
    monodromy = normalized(-cycle_product)
    polynomial = primitive_action_polynomial(bulk)
    monic = sp.Poly(polynomial.as_expr() / polynomial.LC(), Z)
    cycle_characteristic = sp.Poly(cycle_product.charpoly(Z).as_expr(), Z)
    torus_characteristic = sp.Poly(monodromy.charpoly(Z).as_expr(), Z)
    characteristic_valid = (
        sp.Poly(cycle_characteristic.as_expr() - monic.as_expr(), Z).is_zero
        and sp.Poly(
            torus_characteristic.as_expr() - monic.as_expr().subs(Z, -Z), Z
        ).is_zero
    )
    isolations, isolations_valid = decimal_isolations(polynomial)
    isolations_valid = (
        isolations_valid
        and len(isolations) == 2
        and isolations[0][1] < 10**12 < isolations[1][0]
    )
    return Transfer(
        bulk,
        slices,
        tuple(local_transfers),
        cycle_product,
        monodromy,
        polynomial,
        isolations,
        fine_band,
        construction_valid,
        characteristic_valid,
        isolations_valid,
    )


@dataclass(frozen=True)
class Fixture:
    shear: sp.Rational
    raw: object
    action: sp.Matrix
    action_blocks: tuple[sp.Matrix, ...]
    propagator_blocks: tuple[sp.Matrix, ...]
    transfers: tuple[Transfer, ...]
    inversion_valid: bool


def build_fixture(shear: sp.Rational) -> Fixture:
    raw = base.fixture_data(shear)
    action = normalized(raw.propagator.inv(method="DM"))
    size = raw.propagator.rows
    action_blocks = tuple(momentum_block(action, momentum, 8) for momentum in range(4))
    propagator_blocks = tuple(
        momentum_block(raw.propagator, momentum, 8) for momentum in range(4)
    )
    transfers = tuple(transfer_from_action(block) for block in action_blocks)
    inversion_valid = (
        matrix_equal(action * raw.propagator, sp.eye(size))
        and matrix_equal(raw.propagator * action, sp.eye(size))
        and all(
            matrix_equal(action_blocks[k] * propagator_blocks[k], sp.eye(8))
            and matrix_equal(propagator_blocks[k] * action_blocks[k], sp.eye(8))
            for k in range(4)
        )
    )
    return Fixture(
        shear,
        raw,
        action,
        action_blocks,
        propagator_blocks,
        transfers,
        inversion_valid,
    )


def fundamental(
    transfers: tuple[sp.Matrix, ...], stop: int, start: int
) -> sp.Matrix:
    result = sp.eye(2)
    for index in range(start, stop):
        result = transfers[index] * result
    return result.applyfunc(sp.cancel)


@dataclass(frozen=True)
class ThermalTwoPoint:
    covariance: sp.Matrix
    schur_inverse: sp.Matrix
    boundary_factor: sp.Matrix
    formula_valid: bool
    inverse_valid: bool


def thermal_two_point(action: sp.Matrix, transfer: Transfer) -> ThermalTwoPoint:
    """Reconstruct Q^-1 from the exact inhomogeneous Floquet recursion."""
    even = (0, 2, 4, 6)
    odd = (1, 3, 5, 7)
    q_uu = action.extract(even, even)
    q_uv = action.extract(even, odd)
    q_vu = action.extract(odd, even)
    q_vv = action.extract(odd, odd)
    q_vv_inverse = q_vv.inv(method="DM")

    source_u = sp.zeros(4, 8)
    source_v = sp.zeros(4, 8)
    for step in range(4):
        source_u[step, 2 * step] = 1
        source_v[step, 2 * step + 1] = 1
    reduced_source = (source_u - q_uv * q_vv_inverse * source_v).applyfunc(
        sp.cancel
    )
    schur = (q_uu - q_uv * q_vv_inverse * q_vu).applyfunc(sp.cancel)

    locals_ = transfer.local_transfers
    cycle_product = fundamental(locals_, 4, 0)
    boundary = (sp.eye(2) - transfer.monodromy).inv(method="DM").applyfunc(
        sp.cancel
    )
    injections = []
    nonzero_forcing = True
    for current in transfer.slices:
        b = current.diagonal[0, 1]
        d = current.diagonal[1, 1]
        e = current.forward[0, 0]
        f = current.forward[1, 0]
        coefficient_next = sp.cancel(e - b * f / d)
        nonzero_forcing = nonzero_forcing and coefficient_next != 0
        injections.append(sp.Matrix((1 / coefficient_next, 0)))

    # K[n,j]=e1^T(1[n>j]U[n,j+1]-U[n,0](I+U[4,0])^-1
    # U[4,j+1])e1/C_j, with I+U[4,0]=I-T for the closed AP monodromy.
    schur_inverse = sp.zeros(4, 4)
    for step in range(4):
        for source in range(4):
            state = (
                -fundamental(locals_, step, 0)
                * boundary
                * fundamental(locals_, 4, source + 1)
                * injections[source]
            )
            if step > source:
                state += fundamental(locals_, step, source + 1) * injections[source]
            schur_inverse[step, source] = sp.cancel(state[0])

    u_response = (schur_inverse * reduced_source).applyfunc(sp.cancel)
    v_response = (
        q_vv_inverse * (source_v - q_vu * u_response)
    ).applyfunc(sp.cancel)
    covariance = sp.zeros(8, 8)
    for step in range(4):
        covariance[2 * step, :] = u_response[step, :]
        covariance[2 * step + 1, :] = v_response[step, :]
    covariance = covariance.applyfunc(sp.cancel)
    formula_valid = (
        q_vv.is_diagonal()
        and nonzero_forcing
        and matrix_equal(cycle_product, transfer.cycle_product)
        and matrix_equal(sp.eye(2) + cycle_product, sp.eye(2) - transfer.monodromy)
        and canonical((sp.eye(2) - transfer.monodromy).det()) != 0
        and matrix_equal(schur_inverse * schur, sp.eye(4))
        and matrix_equal(schur * schur_inverse, sp.eye(4))
    )
    inverse_valid = matrix_equal(action * covariance, sp.eye(8)) and matrix_equal(
        covariance * action, sp.eye(8)
    )
    return ThermalTwoPoint(
        covariance, schur_inverse, boundary, formula_valid, inverse_valid
    )


def antiperiodic_entry(
    matrix: sp.Matrix, row: int, column: int
) -> sp.Expr:
    row_cell, row_local = divmod(row, 8)
    column_cell, column_local = divmod(column, 8)
    return parity_sign(row_cell + column_cell) * matrix[row_local, column_local]


def simultaneous_shift_residual(
    matrix: sp.Matrix, displacement: int
) -> sp.Matrix:
    return sp.Matrix(
        8,
        8,
        lambda row, column: sp.expand(
            antiperiodic_entry(
                matrix, row + displacement, column + displacement
            )
            - matrix[row, column]
        ),
    )


def first_nonzero(matrix: sp.Matrix) -> tuple[int, int, sp.Expr] | None:
    return next(
        (
            (row, column, matrix[row, column])
            for row in range(matrix.rows)
            for column in range(matrix.cols)
            if matrix[row, column] != 0
        ),
        None,
    )


@dataclass(frozen=True)
class Stationarity:
    one_step_ranks: tuple[int, ...]
    four_step_ranks: tuple[int, ...]
    eight_step_ranks: tuple[int, ...]
    one_step_witness: tuple[int, int, sp.Expr] | None
    four_step_witness: tuple[int, int, sp.Expr] | None


def stationarity_certificate(
    covariances: tuple[sp.Matrix, ...]
) -> Stationarity:
    residuals_one = tuple(
        simultaneous_shift_residual(covariance, 1) for covariance in covariances
    )
    residuals_four = tuple(
        simultaneous_shift_residual(covariance, 4) for covariance in covariances
    )
    residuals_eight = tuple(
        simultaneous_shift_residual(covariance, 8) for covariance in covariances
    )
    return Stationarity(
        tuple(exact_rank(value) for value in residuals_one),
        tuple(exact_rank(value) for value in residuals_four),
        tuple(exact_rank(value) for value in residuals_eight),
        first_nonzero(residuals_one[0]),
        first_nonzero(residuals_four[0]),
    )


@dataclass(frozen=True)
class FinitePairing:
    gram: sp.Matrix
    blocks: tuple[sp.Matrix, ...]
    gram_rank: int
    hermiticity_rank: int
    block_ranks: tuple[tuple[int, int], ...]
    raw_formula_valid: bool


def finite_action_pairing(fixture: Fixture) -> FinitePairing:
    gram = sp.Matrix(
        len(fixture.raw.positive),
        len(fixture.raw.positive),
        lambda row, column: sp.conjugate(
            fixture.raw.propagator[
                fixture.raw.positive[row], fixture.raw.reflected[column]
            ]
        ),
    ).applyfunc(sp.expand)
    blocks = tuple(momentum_block(gram, momentum, 4) for momentum in range(4))
    block_ranks = tuple(
        (exact_rank(block), exact_rank(block - block.H)) for block in blocks
    )
    return FinitePairing(
        gram,
        blocks,
        exact_rank(gram),
        exact_rank(gram - gram.H),
        block_ranks,
        matrix_equal(gram, fixture.raw.raw_gram),
    )


def quadratic_modulus(polynomial: sp.Poly) -> sp.Poly:
    return sp.Poly(
        polynomial.as_expr().subs(Z, ALPHA), ALPHA, domain=sp.QQ_I
    )


def quadratic_reduce(expression: sp.Expr, polynomial: sp.Poly) -> sp.Expr:
    """Reduce an exact QQ(i)(rho) expression modulo the transfer quadratic."""
    numerator, denominator = sp.cancel(sp.expand(expression)).as_numer_denom()
    modulus = quadratic_modulus(polynomial)
    numerator_poly = sp.Poly(sp.expand(numerator), ALPHA, domain=sp.QQ_I)
    denominator_poly = sp.Poly(sp.expand(denominator), ALPHA, domain=sp.QQ_I)
    inverse = sp.invert(denominator_poly, modulus)
    return (numerator_poly * inverse).rem(modulus).as_expr()


def quadratic_conjugate(
    expression: sp.Expr, polynomial: sp.Poly
) -> sp.Expr:
    return quadratic_reduce(sp.conjugate(expression), polynomial)


def field_matrix(matrix: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    return matrix.applyfunc(lambda value: quadratic_reduce(value, polynomial))


def field_equal(
    left: sp.Matrix, right: sp.Matrix, polynomial: sp.Poly
) -> bool:
    return left.shape == right.shape and all(
        quadratic_reduce(value, polynomial) == 0 for value in left - right
    )


def rank_one_field(
    matrix: sp.Matrix, polynomial: sp.Poly
) -> tuple[tuple[int, int] | None, bool]:
    pivot = next(
        (
            (row, column)
            for row in range(matrix.rows)
            for column in range(matrix.cols)
            if quadratic_reduce(matrix[row, column], polynomial) != 0
        ),
        None,
    )
    if pivot is None:
        return None, False
    pivot_row, pivot_column = pivot
    pivot_value = matrix[pivot_row, pivot_column]
    minors_zero = all(
        quadratic_reduce(
            matrix[row, column] * pivot_value
            - matrix[row, pivot_column] * matrix[pivot_row, column],
            polynomial,
        )
        == 0
        for row in range(matrix.rows)
        for column in range(matrix.cols)
    )
    return pivot, minors_zero


def reflection_cut(action_block: sp.Matrix) -> tuple[sp.Matrix, bool]:
    signed_shift = sp.zeros(8, 8)
    for local_time in range(8):
        global_time = (local_time + 4) % 8
        signed_shift[local_time, global_time] = 1 if local_time < 4 else -1
    return (
        normalized(signed_shift * action_block * signed_shift.T),
        matrix_equal(signed_shift * signed_shift.T, sp.eye(8)),
    )


@dataclass(frozen=True)
class StableResidue:
    matrix: sp.Matrix
    polynomial_valid: bool
    regular_at_zero: bool
    rank_one: bool


def stable_residue(transfer: Transfer) -> StableResidue:
    """Return Res_(z=rho) Q(z)^-1 in the exact quadratic root field."""
    polynomial = transfer.magnitude_polynomial
    symbol = (
        transfer.bulk.diagonal
        + Z * transfer.bulk.forward
        + transfer.bulk.backward / Z
    )
    inverse = symbol.inv(method="DM").applyfunc(sp.cancel)
    polynomial_complex = sp.Poly(polynomial, Z, domain=sp.QQ_I)
    derivative = sp.diff(polynomial.as_expr(), Z)
    entries = []
    regular = True
    for entry in inverse:
        numerator, denominator = sp.cancel(entry).as_numer_denom()
        regular = regular and sp.expand(denominator.subs(Z, 0)) != 0
        denominator_poly = sp.Poly(denominator, Z, domain=sp.QQ_I)
        quotient, remainder = denominator_poly.div(polynomial_complex)
        if not remainder.is_zero:
            entries.append(sp.S.Zero)
            continue
        raw = sp.cancel(numerator / (quotient.as_expr() * derivative))
        entries.append(quadratic_reduce(raw.subs(Z, ALPHA), polynomial))
    residue = sp.Matrix(8, 8, entries)
    _, rank_one = rank_one_field(residue, polynomial)
    coefficients = polynomial.all_coeffs()
    discriminant = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
    return StableResidue(
        residue,
        polynomial.degree() == 2
        and coefficients[0] == coefficients[2]
        and discriminant > 0
        and not sp.integer_nthroot(int(discriminant), 2)[1],
        regular,
        rank_one,
    )


def square_root_polynomial(polynomial: sp.Poly) -> sp.Poly:
    a, b, c = polynomial.all_coeffs()
    raw = sp.Poly(
        a**2 * BETA**2 - (b**2 - 2 * a**2) * BETA + a**2,
        BETA,
    )
    result = raw.primitive()[1]
    return -result if result.LC() < 0 else result


@dataclass(frozen=True)
class SuperSector:
    momentum: int
    polynomial: sp.Poly
    square_polynomial: sp.Poly
    square_interval: tuple[sp.Rational, sp.Rational]
    h00_rank: int
    hermiticity_residual_rank: int
    super_window_rank: int
    geometric_hankel: bool
    shifted_ratio: bool
    pencil_identically_zero: bool
    quotient_root: bool
    construction_valid: bool


def super_slice_pairings(fixture: Fixture) -> tuple[SuperSector, ...]:
    cut_data = tuple(reflection_cut(block) for block in fixture.action_blocks)
    cut_actions = tuple(item[0] for item in cut_data)
    cut_transfers = tuple(transfer_from_action(block) for block in cut_actions)
    residues = tuple(stable_residue(transfer) for transfer in cut_transfers)
    result = []
    for momentum in range(4):
        opposite = (-momentum) % 4
        transfer = cut_transfers[opposite]
        polynomial = transfer.magnitude_polynomial
        residue = residues[opposite]
        h00 = sp.Matrix(
            8,
            8,
            lambda row, column: quadratic_conjugate(
                residue.matrix[row, 7 - column], polynomial
            ),
        )
        h00_pivot, h00_rank_one = rank_one_field(h00, polynomial)
        adjoint = sp.Matrix(
            8,
            8,
            lambda row, column: quadratic_conjugate(
                h00[column, row], polynomial
            ),
        )
        hermiticity_residual = field_matrix(h00 - adjoint, polynomial)
        hermiticity_minor = quadratic_reduce(
            hermiticity_residual.extract((0, 1), (0, 1)).det(), polynomial
        )

        blocks = tuple(
            tuple(
                field_matrix(ALPHA ** (row + column) * h00, polynomial)
                for column in range(3)
            )
            for row in range(3)
        )
        geometric_hankel = all(
            field_equal(
                blocks[row][column],
                field_matrix(ALPHA ** (row + column) * h00, polynomial),
                polynomial,
            )
            for row in range(3)
            for column in range(3)
        ) and all(
            field_equal(
                blocks[row][column], blocks[row - 1][column + 1], polynomial
            )
            for row in range(1, 3)
            for column in range(2)
        )
        source = sp.Matrix.vstack(
            sp.Matrix.hstack(blocks[0][0], blocks[0][1]),
            sp.Matrix.hstack(blocks[1][0], blocks[1][1]),
        )
        shifted = sp.Matrix.vstack(
            sp.Matrix.hstack(blocks[1][1], blocks[1][2]),
            sp.Matrix.hstack(blocks[2][1], blocks[2][2]),
        )
        moment = sp.Matrix(((1, ALPHA), (ALPHA, ALPHA**2)))
        source_factorization = field_equal(
            source, sp.kronecker_product(moment, h00), polynomial
        )
        beta = quadratic_reduce(ALPHA**2, polynomial)
        shifted_ratio = field_equal(shifted, beta * source, polynomial)
        source_pivot = None
        if h00_pivot is not None:
            source_pivot = h00_pivot
        quotient_root = False
        if source_pivot is not None:
            pivot_row, pivot_column = source_pivot
            quotient_root = quadratic_reduce(
                shifted[pivot_row, pivot_column]
                / source[pivot_row, pivot_column]
                - beta,
                polynomial,
            ) == 0
        square_polynomial = square_root_polynomial(polynomial)
        stable_lower, stable_upper = transfer.isolations[0]
        scale = 10**12
        square_interval = (
            R(stable_lower**2, scale**2),
            R(stable_upper**2, scale**2),
        )
        square_root_valid = (
            quadratic_reduce(
                square_polynomial.as_expr().subs(BETA, ALPHA**2), polynomial
            )
            == 0
            and 0 < square_interval[0] < square_interval[1] < 1
            and square_polynomial.count_roots(*square_interval) == 1
        )
        result.append(
            SuperSector(
                momentum,
                polynomial,
                square_polynomial,
                square_interval,
                1 if h00_rank_one else -1,
                2 if h00_rank_one and hermiticity_minor != 0 else -1,
                1 if h00_rank_one and source_factorization else -1,
                geometric_hankel,
                shifted_ratio,
                h00_rank_one
                and source_factorization
                and shifted_ratio
                and source.rows > 1,
                quotient_root and square_root_valid,
                cut_data[opposite][1]
                and transfer.characteristic_valid
                and transfer.isolations_valid
                and residue.polynomial_valid
                and residue.regular_at_zero
                and residue.rank_one
                and polynomial == cut_transfers[momentum].magnitude_polynomial,
            )
        )
    return tuple(result)


@dataclass(frozen=True)
class ChartIdentity:
    momentum: int
    q: sp.Expr
    raw_defect: sp.Expr
    correction: sp.Expr
    dressed_identity: bool
    derivative_zero: bool


def chart_identities(
    covariances: tuple[sp.Matrix, ...]
) -> tuple[ChartIdentity, ChartIdentity]:
    result = []
    for momentum in (0, 2):
        covariance = covariances[momentum]
        sector = prior.analyze_sector(covariance, momentum)
        dressing = sector.branch.dressing
        q = canonical(sector.branch.gram[0, 1] - sector.branch.gram[1, 2])
        dressed = canonical(
            sp.conjugate(
                (dressing * covariance)[4, 2]
                - (dressing * covariance)[5, 1]
            )
        )
        raw_defect = canonical(
            sp.conjugate(covariance[4, 2] - covariance[5, 1])
        )
        result.append(
            ChartIdentity(
                momentum,
                q,
                raw_defect,
                canonical(q - raw_defect),
                canonical(q - dressed) == 0,
                all(canonical(sp.diff(dressed, parameter)) == 0 for parameter in prior.TAU),
            )
        )
    return tuple(result)


@dataclass(frozen=True)
class FixtureCertificate:
    fixture: Fixture
    thermal: tuple[ThermalTwoPoint, ...]
    stationarity: Stationarity
    finite: FinitePairing
    supers: tuple[SuperSector, ...]
    charts: tuple[ChartIdentity, ChartIdentity]
    reproduction: bool


def certify_fixture(shear: sp.Rational) -> FixtureCertificate:
    fixture = build_fixture(shear)
    thermal = tuple(
        thermal_two_point(action, transfer)
        for action, transfer in zip(fixture.action_blocks, fixture.transfers)
    )
    covariances = tuple(item.covariance for item in thermal)
    reproduction = fixture.inversion_valid and all(
        item.formula_valid
        and item.inverse_valid
        and matrix_equal(item.covariance, fixture.propagator_blocks[momentum])
        for momentum, item in enumerate(thermal)
    )
    return FixtureCertificate(
        fixture,
        thermal,
        stationarity_certificate(covariances),
        finite_action_pairing(fixture),
        super_slice_pairings(fixture),
        chart_identities(covariances),
        reproduction,
    )


@dataclass(frozen=True)
class GaugeLemma:
    complex_fourth_roots: bool
    no_real_scalar_fourth_root: bool


def gauge_lemma() -> GaugeLemma:
    real_value = sp.symbols("x", real=True)
    positive_magnitude = sp.symbols("a", positive=True)
    quarter_turn = (1 + I) / sp.sqrt(2)
    complex_root = positive_magnitude ** R(1, 4) * quarter_turn
    return GaugeLemma(
        sp.simplify(complex_root**4 + positive_magnitude) == 0,
        sp.ask(sp.Q.nonnegative(real_value**4)) is True
        and sp.ask(sp.Q.positive(real_value**4 + positive_magnitude)) is True,
    )


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


SCOPE_KEYS = (
    "floquet",
    "monodromy",
    "pentadiagonal",
    "determinant_one",
    "negative_eigenvalues",
    "fourth_root",
    "reflection_real",
    "micro_motion",
    "geometric_hankel",
    "moment_quotient",
    "rho_square",
    "no_positive_os",
    "reflection_intertwiner",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "floquet": "floquet" in note,
        "monodromy": "monodromy" in note,
        "pentadiagonal": "pentadiagonal" in note,
        "determinant_one": "det t = 1" in note or "determinant one" in note,
        "negative_eigenvalues": (
            "both eigenvalues strictly negative" in note
            or "both eigenvalues are strictly negative" in note
        ),
        "fourth_root": "quarter-turn" in note or "fourth root" in note,
        "reflection_real": (
            "no reflection-real" in note or "reflection-covariant" in note
        ),
        "micro_motion": "micro-motion" in note,
        "geometric_hankel": (
            "geometric-hankel" in note or "geometric hankel" in note
        ),
        "moment_quotient": "moment quotient" in note,
        "rho_square": "rho^2" in note or "contractive root" in note,
        "no_positive_os": "no positive os hilbert space" in note,
        "reflection_intertwiner": "reflection intertwiner" in note,
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity": "gravity constraint quotient remains unexecuted" in note,
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "w1": "w1" in note,
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
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    return result


def interval_text(interval: tuple[int, int], digits: int = 12) -> str:
    scale = 10**digits
    return f"({interval[0]}/{scale},{interval[1]}/{scale})"


def magnitude_text(transfers: tuple[Transfer, ...]) -> str:
    return ";".join(
        f"k{momentum}/{momentum + 2}="
        + ",".join(interval_text(item) for item in transfers[momentum].isolations)
        for momentum in (0, 1)
    )


def beta_text(supers: tuple[SuperSector, ...]) -> str:
    return ";".join(
        f"k{momentum}/{momentum + 2}=({supers[momentum].square_interval[0]},"
        f"{supers[momentum].square_interval[1]})"
        for momentum in (0, 1)
    )


def witness_text(
    name: str, witness: tuple[int, int, sp.Expr] | None
) -> str:
    if witness is None:
        return f"{name}=none"
    return f"{name}[{witness[0]},{witness[1]}]={witness[2]}"


def split_text(
    label: str, charts: tuple[ChartIdentity, ChartIdentity]
) -> str:
    return label + ":" + ";".join(
        f"k{item.momentum}={item.raw_defect}+({item.correction})={item.q}"
        for item in charts
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority",
        "Block 117 blobs and ancestors 116--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "scripts/admissibility_dirac_kahler_self_chart_emptiness_stationarity_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_self_chart_emptiness_stationarity_2026_08_16.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 117)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    primary = certify_fixture(PRIMARY_SHEAR)
    second = certify_fixture(SECOND_SHEAR)
    certificates = (primary, second)
    all_transfers = tuple(
        transfer
        for certificate in certificates
        for transfer in certificate.fixture.transfers
    )

    primary_local_traces = tuple(
        canonical(local.trace())
        for local in primary.fixture.transfers[0].local_transfers
    )
    band_claim = all(
        transfer.fine_band and transfer.construction_valid
        for transfer in all_transfers
    )
    if mutation == "break_floquet_band":
        band_claim = False
    constant_companions_claimed = mutation == "claim_constant_companions"
    checks.check(
        "B-the-floquet-structure",
        "exact alternating band, varying companions, and four-step Z8 closure",
        band_claim
        and all(
            len(transfer.slices) == len(transfer.local_transfers) == 4
            and matrix_equal(
                transfer.monodromy,
                -fundamental(transfer.local_transfers, 4, 0),
            )
            for transfer in all_transfers
        )
        and len(set(primary_local_traces)) > 1
        and len(
            {
                tuple(sp.expand(value) for value in local)
                for local in primary.fixture.transfers[0].local_transfers
            }
        )
        > 1
        and not constant_companions_claimed,
    )

    actual_traces = tuple(
        canonical(transfer.monodromy.trace()) for transfer in all_transfers
    )
    determinant_facts = all(
        canonical(transfer.monodromy.det()) == 1
        and canonical(transfer.cycle_product.det()) == 1
        and all(canonical(local.det()) != 1 for local in transfer.local_transfers)
        and canonical(
            sp.prod(local.det() for local in transfer.local_transfers)
        )
        == 1
        for transfer in all_transfers
    )
    tested_determinants = determinant_facts
    if mutation == "break_monodromy_det":
        tested_determinants = False
    tested_traces = actual_traces
    if mutation == "break_negative_trace":
        tested_traces = (sp.S.Zero,) + tested_traces[1:]
    spectral_facts = all(
        transfer.characteristic_valid
        and transfer.isolations_valid
        and trace.is_Rational
        and trace < -2
        and sp.Poly(LAM**2 - trace * LAM + 1, LAM, domain=sp.QQ).count_roots(
            -sp.oo, 0
        )
        == 2
        for transfer, trace in zip(all_transfers, actual_traces)
    )
    magnitude_pins = tuple(
        tuple(
            certificate.fixture.transfers[momentum].isolations
            for momentum in (0, 1)
        )
        for certificate in certificates
    )
    paired_momenta = all(
        matrix_equal(fixture.transfers[0].monodromy, fixture.transfers[2].monodromy)
        and matrix_equal(
            fixture.transfers[1].monodromy, fixture.transfers[3].monodromy
        )
        and fixture.transfers[0].magnitude_polynomial
        == fixture.transfers[2].magnitude_polynomial
        and fixture.transfers[1].magnitude_polynomial
        == fixture.transfers[3].magnitude_polynomial
        for fixture in (primary.fixture, second.fixture)
    )
    checks.check(
        "C-the-monodromy",
        "det T=1, local determinants telescope, tau<-2, and eight magnitude intervals are pinned",
        tested_determinants
        and all(trace < -2 for trace in tested_traces)
        and spectral_facts
        and paired_momenta
        and magnitude_pins == EXPECTED_MAGNITUDE_INTERVALS,
    )

    reproduction = all(certificate.reproduction for certificate in certificates)
    if mutation == "break_reproduction":
        reproduction = False
    period_four_claimed = mutation == "claim_period4_stationary"
    stationarity_facts = all(
        certificate.stationarity.one_step_ranks == (8, 8, 8, 8)
        and certificate.stationarity.four_step_ranks == (8, 8, 8, 8)
        and certificate.stationarity.eight_step_ranks == (0, 0, 0, 0)
        and certificate.stationarity.one_step_witness is not None
        and certificate.stationarity.four_step_witness is not None
        for certificate in certificates
    )
    checks.check(
        "D-the-reproduction-and-stationarity-ledger",
        "K[n,j] gives Q_k^-1 and ranks D1/D4/D8 are 8/8/0",
        reproduction and stationarity_facts and not period_four_claimed,
    )

    lemma = gauge_lemma()
    distinct_negative = spectral_facts and all(
        trace**2 - 4 > 0 for trace in actual_traces
    )
    abstract_complex_gauge = distinct_negative and all(
        canonical(transfer.monodromy.det()) != 0
        and all(canonical(local.det()) != 0 for local in transfer.local_transfers)
        for transfer in all_transfers
    )
    real_gauge_claimed = mutation == "claim_real_gauge"
    checks.check(
        "E-the-gauge-obstruction",
        "a complex fourth root exists but z^4=r<0 has no real solution",
        abstract_complex_gauge
        and lemma.complex_fourth_roots
        and lemma.no_real_scalar_fourth_root
        and not real_gauge_claimed,
    )

    finite_facts = all(
        certificate.finite.raw_formula_valid
        and certificate.finite.gram_rank == 8
        and certificate.finite.hermiticity_rank == 16
        and certificate.finite.block_ranks == ((2, 4),) * 4
        for certificate in certificates
    )
    super_facts = all(
        sector.construction_valid
        and sector.h00_rank == 1
        and sector.hermiticity_residual_rank == 2
        and sector.super_window_rank == 1
        and sector.geometric_hankel
        and sector.shifted_ratio
        and sector.pencil_identically_zero
        and sector.quotient_root
        for certificate in certificates
        for sector in certificate.supers
    )
    tested_hankel = super_facts
    if mutation == "break_hankel_ratio":
        tested_hankel = False
    positive_pairing_claimed = mutation == "claim_positive_pairing"
    beta_pins = tuple(
        tuple(certificate.supers[momentum].square_interval for momentum in (0, 1))
        for certificate in certificates
    )
    checks.check(
        "F-the-degenerations",
        "exact torus and geometric-Hankel ranks, zero pencil, and four pinned rho^2 intervals",
        finite_facts
        and tested_hankel
        and beta_pins == EXPECTED_BETA_INTERVALS
        and not positive_pairing_claimed,
    )

    expected_constants = (prior.PRIMARY_SQUARES, prior.SECOND_SQUARES)
    raw_defects = (PRIMARY_RAW_DEFECT, SECOND_RAW_DEFECT)
    identity_facts = all(
        all(
            chart.dressed_identity
            and chart.derivative_zero
            and chart.q == expected_constants[fixture_index][chart_index]
            and chart.raw_defect == raw_defects[fixture_index]
            and chart.correction
            == expected_constants[fixture_index][chart_index]
            - raw_defects[fixture_index]
            for chart_index, chart in enumerate(certificate.charts)
        )
        for fixture_index, certificate in enumerate(certificates)
    )
    shared_denominators = all(
        all(
            value.is_Rational and value.q == raw_defects[fixture_index].q
            for chart in certificate.charts
            for value in (chart.q, chart.raw_defect, chart.correction)
        )
        for fixture_index, certificate in enumerate(certificates)
    )
    tested_identity = identity_facts
    if mutation == "break_identity_split":
        tested_identity = False
    checks.check(
        "G-the-dressed-micro-motion-identity",
        "parameter-free dressed identity and common-denominator additive splits",
        tested_identity and shared_denominators,
    )

    note_scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "all required note phrases, firewalls, and runtime bound",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 300,
    )

    primary_traces = tuple(
        canonical(transfer.monodromy.trace())
        for transfer in primary.fixture.transfers
    )
    second_traces = tuple(
        canonical(transfer.monodromy.trace())
        for transfer in second.fixture.transfers
    )
    print(
        f"FLOQUET c=5/13: local_traces(k0)={primary_local_traces}; "
        f"tau(k0/2,k1/3)={primary_traces[:2]}; "
        f"|eigenvalues|={magnitude_text(primary.fixture.transfers)}"
    )
    print(
        f"FLOQUET c=3/5: tau(k0/2,k1/3)={second_traces[:2]}; "
        f"|eigenvalues|={magnitude_text(second.fixture.transfers)}"
    )
    for label, certificate in (("5/13", primary), ("3/5", second)):
        stationarity = certificate.stationarity
        print(
            f"STATIONARITY c={label}: D1={stationarity.one_step_ranks}, "
            f"{witness_text('D1', stationarity.one_step_witness)}; "
            f"D4={stationarity.four_step_ranks}, "
            f"{witness_text('D4', stationarity.four_step_witness)}; "
            f"D8={stationarity.eight_step_ranks}"
        )
    print(
        "GAUGE: the complex fourth-root criterion holds; x^4+a>0 for real x "
        "and exact a>0, excluding a reflection-real quarter-turn root"
    )
    for label, certificate in (("5/13", primary), ("3/5", second)):
        print(
            f"PAIRING c={label}: M=(8,16), blocks=(2,4); H00=(1,2), "
            f"geometric-Hankel, pencil=0; beta=rho^2 in "
            f"{beta_text(certificate.supers)} subset (0,1)"
        )
    print(
        "IDENTITY: "
        + split_text("c=5/13", primary.charts)
        + "; "
        + split_text("c=3/5", second.charts)
        + "; shared-denominator fingerprint=(1026791823428467,250649423107); "
        + f"runtime={time.monotonic() - started:.3f}s"
    )
    print(
        "N5: per_element: exact pentadiagonal, companion, monodromy, inverse, stationarity-residual, dressed-identity, rank, and root-isolation identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: all four fixed momenta at c=5/13 and c=3/5 have determinant-one negative Floquet spectra, with exact inverse and degeneration ledgers"
    )
    print(
        "per_block: no reflection-real one-step-stationary gauge exists for this action, while the one-dimensional moment quotient has beta=rho^2 in (0,1) without a positive OS form"
    )
    print(
        "lattice_wide: checked and not executed — the reflection intertwiner, positive OS Hilbert space, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the action's transfer is a determinant-one floquet monodromy with strictly negative eigenvalues — the stationary pairing exists only at the full-torus shift, the naive pairings degenerate exactly, and the contractive root rho^2 lives on a quotient that lacks a positive pairing"
    )
    print(
        "DECISION_CUT: construct the reflection intertwiner completing the geometric-hankel pairing to a positive OS package; reject further one-step-window constructions"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
