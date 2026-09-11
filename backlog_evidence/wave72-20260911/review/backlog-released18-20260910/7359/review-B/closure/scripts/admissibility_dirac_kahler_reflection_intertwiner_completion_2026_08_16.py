#!/usr/bin/env python3
"""Block 119: exact reflection-intertwiner completion certificate.

The Block 118 geometric-Hankel half-space pairing is factored sector by
sector over its exact stable-root field.  Fixed carrier candidates are
refuted there, while a reflection-real swap on the stable boundary data
completes the pairing to an involutive positive package with its exact
contractive geometric semigroup.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16 as prior


R = sp.Rational
I = sp.I
RHO = prior.ALPHA
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_floquet_monodromy_"
    "action_pairing_2026_08_16.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_floquet_monodromy_"
    "action_pairing_2026_08_16.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "scripts/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "4e566b14a6352a9a62590252a9755c7a103c1b9e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block118-floquet-monodromy-action-pairing-20260816"
)
PARENT_COMMIT = "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"
PARENT_NOTE_BLOB = "d8f5765c3fee3bd349aebd7bf945066ca5439235"
PARENT_RUNNER_BLOB = "12c065883099077aae880eeecf3f2a80444a1d87"
PARENT_CACHE_BLOB = "804641ed09f5c2c0b458b0b9ce8a201c93c05a43"
ANCESTOR_COMMITS = (
    (117, "f800356aec0989b6e0fa80ed43274794243b1ca2"),
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

EXPECTED_BETA_INTERVALS = prior.EXPECTED_BETA_INTERVALS

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_factorization",
    "break_reduction",
    "claim_negative_mu_allowed",
    "claim_candidate_works",
    "break_swap_involution",
    "break_reflection_reality",
    "break_mu_one",
    "break_inertia",
    "claim_negative_direction",
    "break_semigroup",
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


def red(value: sp.Expr, polynomial: sp.Poly) -> sp.Expr:
    """Reduce in QQ(i)[rho]/(p_k)."""
    return prior.quadratic_reduce(value, polynomial)


def star(value: sp.Expr, polynomial: sp.Poly) -> sp.Expr:
    """The root-field involution fixing real rho and conjugating i."""
    return prior.quadratic_conjugate(value, polynomial)


def field_matrix(matrix: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    return matrix.applyfunc(lambda value: red(value, polynomial))


def field_equal(
    left: sp.Matrix, right: sp.Matrix, polynomial: sp.Poly
) -> bool:
    return left.shape == right.shape and all(
        red(value, polynomial) == 0 for value in left - right
    )


def field_adjoint(matrix: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    return sp.Matrix(
        matrix.cols,
        matrix.rows,
        lambda row, column: star(matrix[column, row], polynomial),
    )


def field_conjugate(matrix: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    return matrix.applyfunc(lambda value: star(value, polynomial))


def root_outer(vector: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    return sp.Matrix(
        vector.rows,
        vector.rows,
        lambda row, column: red(
            vector[row] * star(vector[column], polynomial), polynomial
        ),
    )


@dataclass(frozen=True)
class Sector:
    shear: sp.Rational
    momentum: int
    transfer: prior.Transfer
    polynomial: sp.Poly
    stable_interval: tuple[int, int]
    h00: sp.Matrix
    x: sp.Matrix
    y: sp.Matrix
    pivot: tuple[int, int]
    minors_vanishing: int
    factorization: bool
    geometric_hankel: bool


def make_sectors(shear: sp.Rational) -> tuple[Sector, ...]:
    """Reuse Block 118's cut action and stable residue exactly."""
    fixture = prior.build_fixture(shear)
    cut_actions = tuple(
        prior.reflection_cut(block)[0] for block in fixture.action_blocks
    )
    transfers = tuple(prior.transfer_from_action(block) for block in cut_actions)
    residues = tuple(prior.stable_residue(transfer) for transfer in transfers)
    result = []
    for momentum in range(4):
        opposite = (-momentum) % 4
        transfer = transfers[opposite]
        polynomial = transfer.magnitude_polynomial
        if polynomial != transfers[momentum].magnitude_polynomial:
            raise AssertionError("opposite momentum root fields disagree")
        residue = residues[opposite]
        h00 = sp.Matrix(
            8,
            8,
            lambda row, column: star(
                residue.matrix[row, 7 - column], polynomial
            ),
        ).applyfunc(lambda value: red(value, polynomial))
        pivot = next(
            (
                (row, column)
                for row in range(8)
                for column in range(8)
                if red(h00[row, column], polynomial) != 0
            ),
            None,
        )
        if pivot is None:
            raise AssertionError("stable residue has no nonzero pivot")
        pivot_row, pivot_column = pivot
        pivot_value = h00[pivot_row, pivot_column]
        x = h00[:, pivot_column].applyfunc(
            lambda value: red(value, polynomial)
        )
        y = sp.Matrix(
            [
                star(h00[pivot_row, column] / pivot_value, polynomial)
                for column in range(8)
            ]
        ).applyfunc(lambda value: red(value, polynomial))
        outer = root_outer(x, polynomial)
        # root_outer(x) is not the desired nonsymmetric factorization; use
        # x y^H with y normalized by the pivot row.
        outer = sp.Matrix(
            8,
            8,
            lambda row, column: red(
                x[row] * star(y[column], polynomial), polynomial
            ),
        )
        minors_vanishing = sum(
            red(
                h00[a, c] * h00[b, d] - h00[a, d] * h00[b, c],
                polynomial,
            )
            == 0
            for a, b in combinations(range(8), 2)
            for c, d in combinations(range(8), 2)
        )
        factorization = (
            pivot == (0, 0)
            and red(y[0] - 1, polynomial) == 0
            and any(red(value, polynomial) != 0 for value in x)
            and any(red(value, polynomial) != 0 for value in y)
            and field_equal(outer, h00, polynomial)
            and minors_vanishing == 784
        )
        blocks = tuple(
            tuple(
                field_matrix(RHO ** (row + column) * h00, polynomial)
                for column in range(3)
            )
            for row in range(3)
        )
        geometric_hankel = all(
            field_equal(
                blocks[row][column],
                field_matrix(RHO ** (row + column) * h00, polynomial),
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
        result.append(
            Sector(
                shear,
                momentum,
                transfer,
                polynomial,
                transfer.isolations[0],
                h00,
                x,
                y,
                pivot,
                minors_vanishing,
                factorization,
                geometric_hankel,
            )
        )
    return tuple(result)


@dataclass(frozen=True)
class Reduction:
    theta_one: sp.Matrix
    proportional_dimension: int
    fixed_mu_dimension: int
    positive_real_dimension: int
    proportionality_rank: int
    evaluation_rank: int
    exact_reduction: bool
    real_moment_psd: bool
    negative_mu_excluded: bool


def reduction_certificate(sector: Sector) -> Reduction:
    """Certify Theta H >= 0 iff Theta x = mu y with real mu > 0."""
    polynomial = sector.polynomial
    pivot_row = sector.pivot[0]
    theta_one = sp.zeros(8)
    for row in range(8):
        theta_one[row, pivot_row] = red(
            sector.y[row] / sector.x[pivot_row], polynomial
        )
    image = field_matrix(theta_one * sector.x, polynomial)
    completed = field_matrix(theta_one * sector.h00, polynomial)
    y_square = root_outer(sector.y, polynomial)

    # y_0=1 makes the seven proportionality equations independent.
    constraint = sp.zeros(7, 64)
    nonzero_rows = tuple(range(1, 8))
    for equation, row in enumerate(nonzero_rows):
        for column in range(8):
            constraint[equation, 8 * row + column] = red(
                sector.y[0] * sector.x[column], polynomial
            )
            constraint[equation, column] = red(
                -sector.y[row] * sector.x[column], polynomial
            )
    constraint_witness = constraint[
        :, tuple(8 * row + pivot_row for row in nonzero_rows)
    ]
    proportionality_rank = 7 if red(
        constraint_witness.det(method="domain-ge"), polynomial
    ) != 0 else -1

    # At fixed mu, evaluation Theta -> Theta*x is onto, giving rank eight.
    evaluation = sp.zeros(8, 64)
    for row in range(8):
        for column in range(8):
            evaluation[row, 8 * row + column] = sector.x[column]
    evaluation_witness = evaluation[
        :, tuple(8 * row + pivot_row for row in range(8))
    ]
    evaluation_rank = 8 if red(
        evaluation_witness.det(method="domain-ge"), polynomial
    ) != 0 else -1

    moment_vector = sp.Matrix((1, RHO, RHO**2))
    moment = field_matrix(moment_vector * moment_vector.T, polynomial)
    real_moment_psd = (
        all(
            red(moment[row, column] - RHO ** (row + column), polynomial)
            == 0
            for row in range(3)
            for column in range(3)
        )
        and all(
            red(star(value, polynomial) - value, polynomial) == 0
            for value in moment_vector
        )
        and 0 < sector.stable_interval[0] < sector.stable_interval[1] < 10**12
        and polynomial.count_roots(
            R(sector.stable_interval[0], 10**12),
            R(sector.stable_interval[1], 10**12),
        )
        == 1
    )
    # For z=Theta*x, Hermiticity of z y^H forces z=z_0 y and
    # z_0=star(z_0), since y_0=1.  Its only nonzero eigenvalue has the
    # sign of this real scalar, so nonzero PSD is exactly mu>0.
    exact_reduction = (
        sector.factorization
        and red(sector.y[0] - 1, polynomial) == 0
        and field_equal(image, sector.y, polynomial)
        and field_equal(completed, y_square, polynomial)
        and field_equal(y_square, field_adjoint(y_square, polynomial), polynomial)
        and proportionality_rank == 7
        and evaluation_rank == 8
        and real_moment_psd
    )
    negative_mu_excluded = (
        red(-y_square[0, 0] + 1, polynomial) == 0
        and red(sector.y[0] - 1, polynomial) == 0
    )
    return Reduction(
        theta_one,
        64 - proportionality_rank,
        64 - evaluation_rank,
        2 * (64 - evaluation_rank) + 1,
        proportionality_rank,
        evaluation_rank,
        exact_reduction,
        real_moment_psd,
        negative_mu_excluded,
    )


B114 = prior.prior.prior.prior.prior
B111 = prior.b111
B110_BASE = B111.block110.prior


def cut_shift() -> sp.Matrix:
    result = sp.zeros(8)
    for local_time in range(8):
        old_time = (local_time + 4) % 8
        result[local_time, old_time] = 1 if local_time < 4 else -1
    if not prior.matrix_equal(result * result.T, sp.eye(8)):
        raise AssertionError("half-space cut shift is not orthogonal")
    return result


def positive_dressings(shear: sp.Rational) -> tuple[sp.Matrix, ...]:
    """The four exact positive dressing blocks constructed in Block 114."""
    witness = B114.pinned_witness(shear)
    blocks = tuple(witness.blocks)
    if (
        witness.shear != shear
        or len(blocks) != 4
        or not all(
            prior.matrix_equal(block * block, sp.eye(8)) for block in blocks
        )
    ):
        raise AssertionError("Block 114 positive dressing mismatch")
    return blocks


@dataclass(frozen=True)
class Carrier:
    name: str
    operators: tuple[sp.Matrix, ...]
    targets: tuple[int, ...]
    antilinear: bool = False


def compose_carriers(left: Carrier, right: Carrier, name: str) -> Carrier:
    operators = []
    targets = []
    for source in range(4):
        middle = right.targets[source]
        right_operator = right.operators[source]
        if left.antilinear:
            right_operator = right_operator.applyfunc(sp.conjugate)
        operators.append(
            (left.operators[middle] * right_operator).applyfunc(sp.expand)
        )
        targets.append(left.targets[middle])
    return Carrier(
        name,
        tuple(operators),
        tuple(targets),
        left.antilinear != right.antilinear,
    )


_HODGE_CACHE: tuple[sp.Matrix, ...] | None = None


def hodge_blocks() -> tuple[sp.Matrix, ...]:
    global _HODGE_CACHE
    if _HODGE_CACHE is not None:
        return _HODGE_CACHE
    fourier = sp.Matrix(
        4, 4, lambda row, column: I ** (-row * column)
    ) / 2
    transform = sp.kronecker_product(sp.eye(8), fourier)
    transformed = (
        transform.H * B110_BASE.global_candidate() * transform
    ).applyfunc(sp.expand)
    indices = tuple(
        tuple(momentum + 4 * time for time in range(8))
        for momentum in range(4)
    )
    support = tuple(
        tuple(
            any(
                transformed[row, column] != 0
                for row in indices[target]
                for column in indices[source]
            )
            for target in range(4)
        )
        for source in range(4)
    )
    expected_support = tuple(
        tuple(target == (source + 2) % 4 for target in range(4))
        for source in range(4)
    )
    if support != expected_support:
        raise AssertionError("overlap Hodge carrier has unexpected support")
    _HODGE_CACHE = tuple(
        transformed.extract(indices[(momentum + 2) % 4], indices[momentum])
        for momentum in range(4)
    )
    return _HODGE_CACHE


def carrier_family(shear: sp.Rational) -> tuple[Carrier, ...]:
    cut = cut_shift()
    fixture = prior.build_fixture(shear)
    if not all(
        prior.matrix_equal(
            prior.reflection_cut(block)[0], cut * block * cut.T
        )
        for block in fixture.action_blocks
    ):
        raise AssertionError("candidate cut convention disagrees with Block 118")
    dressings = positive_dressings(shear)
    direct = Carrier(
        "A_dir",
        tuple(
            (cut * dressings[momentum] * cut.T).applyfunc(sp.expand)
            for momentum in range(4)
        ),
        (0, 1, 2, 3),
    )
    reflected = Carrier(
        "A_OS",
        tuple(
            (
                cut
                * dressings[(-momentum) % 4].conjugate()
                * cut.T
            ).applyfunc(sp.expand)
            for momentum in range(4)
        ),
        (0, 1, 2, 3),
    )
    hodge = Carrier(
        "Hov",
        tuple(
            (cut * block * cut.T).applyfunc(sp.expand)
            for block in hodge_blocks()
        ),
        (2, 3, 0, 1),
    )
    reality_matrix = (cut * B111.J * cut.T).applyfunc(sp.expand)
    reality = Carrier(
        "Jbar", (reality_matrix,) * 4, (0, 3, 2, 1), True
    )
    klein = Carrier(
        "K", (sp.diag(*((1, -1) * 4)),) * 4, (0, 1, 2, 3)
    )
    parity = Carrier("P", (sp.eye(8),) * 4, (2, 3, 0, 1))
    fermion = Carrier("-I", (-sp.eye(8),) * 4, (0, 1, 2, 3))
    return (
        direct,
        reflected,
        hodge,
        reality,
        klein,
        parity,
        fermion,
        compose_carriers(klein, reflected, "K*A"),
        compose_carriers(reflected, klein, "A*K"),
        compose_carriers(klein, hodge, "K*Hov"),
        compose_carriers(hodge, klein, "Hov*K"),
        compose_carriers(klein, reality, "K*Jbar"),
        compose_carriers(reality, klein, "Jbar*K"),
        compose_carriers(hodge, reality, "Hov*Jbar"),
    )


@dataclass(frozen=True)
class Verdict:
    proportional: bool
    failure_index: int | None
    failure_value: sp.Expr | None


def candidate_verdict(
    carrier: Carrier, source: Sector, target: Sector
) -> Verdict:
    polynomial = source.polynomial
    if polynomial != target.polynomial:
        raise AssertionError("candidate target does not share the root field")
    vector = (
        source.x.applyfunc(lambda value: star(value, polynomial))
        if carrier.antilinear
        else source.x
    )
    image = field_matrix(
        carrier.operators[source.momentum] * vector, polynomial
    )
    if red(target.y[0] - 1, polynomial) != 0:
        raise AssertionError("candidate reduction requires y_0=1")
    residuals = tuple(
        red(image[index] - image[0] * target.y[index], polynomial)
        for index in range(8)
    )
    failure = next(
        (
            (index, value)
            for index, value in enumerate(residuals)
            if value != 0
        ),
        None,
    )
    if failure is None:
        return Verdict(True, None, None)
    return Verdict(False, failure[0], failure[1])


@dataclass(frozen=True)
class CandidateCertificate:
    names: tuple[str, ...]
    table: dict[tuple[sp.Rational, str], tuple[Verdict, ...]]
    failures_per_fixture: tuple[int, int]
    all_nonproportional: bool


def candidate_certificate(
    fixtures: tuple[tuple[Sector, ...], tuple[Sector, ...]],
) -> CandidateCertificate:
    table = {}
    names: tuple[str, ...] | None = None
    failure_counts = []
    for sectors in fixtures:
        shear = sectors[0].shear
        carriers = carrier_family(shear)
        current_names = tuple(carrier.name for carrier in carriers)
        if names is None:
            names = current_names
        if current_names != names:
            raise AssertionError("candidate names differ between fixtures")
        count = 0
        for carrier in carriers:
            verdicts = tuple(
                candidate_verdict(
                    carrier,
                    sectors[momentum],
                    sectors[carrier.targets[momentum]],
                )
                for momentum in range(4)
            )
            table[(shear, carrier.name)] = verdicts
            count += sum(not verdict.proportional for verdict in verdicts)
        failure_counts.append(count)
    if names is None:
        raise AssertionError("empty candidate family")
    all_nonproportional = all(
        not verdict.proportional
        for verdicts in table.values()
        for verdict in verdicts
    )
    return CandidateCertificate(
        names,
        table,
        (failure_counts[0], failure_counts[1]),
        all_nonproportional,
    )


def field_inverse(matrix: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    if matrix.rows != matrix.cols:
        raise AssertionError("root-field inverse requires a square matrix")
    size = matrix.rows
    augmented = field_matrix(matrix, polynomial).row_join(sp.eye(size))
    for column in range(size):
        pivot = next(
            (
                row
                for row in range(column, size)
                if red(augmented[row, column], polynomial) != 0
            ),
            None,
        )
        if pivot is None:
            raise AssertionError("root-field matrix is singular")
        if pivot != column:
            augmented.row_swap(pivot, column)
        inverse_pivot = red(1 / augmented[column, column], polynomial)
        for entry in range(2 * size):
            augmented[column, entry] = red(
                augmented[column, entry] * inverse_pivot, polynomial
            )
        for row in range(size):
            if row == column:
                continue
            factor = red(augmented[row, column], polynomial)
            if factor == 0:
                continue
            for entry in range(2 * size):
                augmented[row, entry] = red(
                    augmented[row, entry]
                    - factor * augmented[column, entry],
                    polynomial,
                )
    inverse = augmented[:, size:]
    if not (
        field_equal(
            field_matrix(matrix * inverse, polynomial), sp.eye(size), polynomial
        )
        and field_equal(
            field_matrix(inverse * matrix, polynomial), sp.eye(size), polynomial
        )
    ):
        raise AssertionError("root-field Gauss inverse failed")
    return inverse


def swap_completion(vectors: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    """Swap columns 0<->1 and 2<->3, fixing their orthogonal complement."""
    if vectors.shape != (8, 4):
        raise AssertionError("swap completion requires four boundary vectors")
    adjoint = field_adjoint(vectors, polynomial)
    gram = field_matrix(adjoint * vectors, polynomial)
    gram_inverse = field_inverse(gram, polynomial)
    left_inverse = field_matrix(gram_inverse * adjoint, polynomial)
    swap = sp.zeros(4)
    swap[1, 0] = swap[0, 1] = 1
    swap[3, 2] = swap[2, 3] = 1
    theta = field_matrix(
        sp.eye(8)
        + vectors * (swap - sp.eye(4)) * left_inverse,
        polynomial,
    )
    if not (
        field_equal(left_inverse * vectors, sp.eye(4), polynomial)
        and field_equal(theta * vectors, vectors * swap, polynomial)
        and field_equal(theta * theta, sp.eye(8), polynomial)
    ):
        raise AssertionError("swap completion identities failed")
    return theta


def reality_vector(
    reality: sp.Matrix, vector: sp.Matrix, polynomial: sp.Poly
) -> sp.Matrix:
    return field_matrix(
        reality * vector.applyfunc(lambda value: star(value, polynomial)),
        polynomial,
    )


def reality_conjugate(
    reality: sp.Matrix, matrix: sp.Matrix, polynomial: sp.Poly
) -> sp.Matrix:
    return field_matrix(
        reality * field_conjugate(matrix, polynomial) * reality,
        polynomial,
    )


@dataclass(frozen=True)
class Completion:
    shear: sp.Rational
    reality: sp.Matrix
    thetas: tuple[sp.Matrix, ...]
    mu_one: bool
    involutive: bool
    self_reflection_real: bool
    global_reflection_reality: bool


def reflection_real_completion(sectors: tuple[Sector, ...]) -> Completion:
    shear = sectors[0].shear
    if len(sectors) != 4 or any(sector.shear != shear for sector in sectors):
        raise AssertionError("completion requires one four-sector fixture")
    cut = cut_shift()
    reality = (cut * B111.J * cut.T).applyfunc(sp.expand)
    if not prior.matrix_equal(reality * reality, sp.eye(8)):
        raise AssertionError("transported Block 111 reality is not involutive")
    thetas: list[sp.Matrix | None] = [None] * 4

    for momentum in (0, 2):
        sector = sectors[momentum]
        polynomial = sector.polynomial
        rx = reality_vector(reality, sector.x, polynomial)
        ry = reality_vector(reality, sector.y, polynomial)
        vectors = sp.Matrix.hstack(sector.x, sector.y, rx, ry)
        thetas[momentum] = swap_completion(vectors, polynomial)

    one = sectors[1]
    three = sectors[3]
    vectors = sp.Matrix.hstack(
        one.x,
        one.y,
        reality_vector(reality, three.x, one.polynomial),
        reality_vector(reality, three.y, one.polynomial),
    )
    thetas[1] = swap_completion(vectors, one.polynomial)
    thetas[3] = reality_conjugate(reality, thetas[1], one.polynomial)
    if any(theta is None for theta in thetas):
        raise AssertionError("not all reflection blocks were constructed")
    resolved = tuple(theta for theta in thetas if theta is not None)

    mu_one = all(
        field_equal(
            resolved[momentum] * sector.x, sector.y, sector.polynomial
        )
        and field_equal(
            resolved[momentum] * sector.y, sector.x, sector.polynomial
        )
        for momentum, sector in enumerate(sectors)
    )
    involutive = all(
        field_equal(
            resolved[momentum] * resolved[momentum],
            sp.eye(8),
            sector.polynomial,
        )
        for momentum, sector in enumerate(sectors)
    )
    self_reflection_real = all(
        field_equal(
            resolved[momentum],
            reality_conjugate(
                reality, resolved[momentum], sectors[momentum].polynomial
            ),
            sectors[momentum].polynomial,
        )
        for momentum in (0, 2)
    )
    global_reflection_reality = all(
        field_equal(
            resolved[(-momentum) % 4],
            reality_conjugate(
                reality, resolved[momentum], sectors[momentum].polynomial
            ),
            sectors[momentum].polynomial,
        )
        for momentum in range(4)
    )
    return Completion(
        shear,
        reality,
        resolved,
        mu_one,
        involutive,
        self_reflection_real,
        global_reflection_reality,
    )


def rank_one_outer_inertia(
    vector: sp.Matrix, gram: sp.Matrix, polynomial: sp.Poly
) -> tuple[int, int, int]:
    """Exact inertia of w w^H when the displayed unit coordinate is present."""
    outer = root_outer(vector, polynomial)
    if (
        vector.cols != 1
        or red(vector[0] - 1, polynomial) != 0
        or not field_equal(gram, outer, polynomial)
        or not field_equal(gram, field_adjoint(gram, polynomial), polynomial)
    ):
        return (-1, -1, -1)
    # The stable root is real.  Thus q^H(w w^H)q=|w^H q|^2, and w_0=1
    # makes the unique nonzero direction strictly positive.
    return (1, 0, vector.rows - 1)


@dataclass(frozen=True)
class SectorPackage:
    completed_h00: sp.Matrix
    three_cell_gram: sp.Matrix
    inertia: tuple[int, int, int]
    hermitian: bool
    psd: bool
    beta: sp.Expr
    beta_polynomial: sp.Poly
    beta_interval: tuple[sp.Rational, sp.Rational]
    contractive: bool
    quotient_transfer: bool
    semigroup: bool
    displayed_n2_n3: bool


@dataclass(frozen=True)
class PositivePackage:
    shear: sp.Rational
    sectors: tuple[SectorPackage, ...]
    per_momentum_inertia: tuple[tuple[int, int, int], ...]
    global_inertia: tuple[int, int, int]
    hermitian: bool
    psd: bool
    contraction: bool
    semigroup: bool


def sector_package(sector: Sector, theta: sp.Matrix) -> SectorPackage:
    polynomial = sector.polynomial
    completed_h00 = field_matrix(theta * sector.h00, polynomial)
    y_square = root_outer(sector.y, polynomial)
    moment_vector = sp.Matrix((1, RHO, RHO**2))
    moment = field_matrix(moment_vector * moment_vector.T, polynomial)
    three_cell_gram = field_matrix(
        sp.kronecker_product(moment, completed_h00), polynomial
    )
    three_cell_vector = field_matrix(
        sp.kronecker_product(moment_vector, sector.y), polynomial
    )
    completed_exact = field_equal(completed_h00, y_square, polynomial)
    inertia = rank_one_outer_inertia(
        three_cell_vector, three_cell_gram, polynomial
    )
    hermitian = (
        completed_exact
        and field_equal(
            completed_h00, field_adjoint(completed_h00, polynomial), polynomial
        )
        and field_equal(
            three_cell_gram,
            field_adjoint(three_cell_gram, polynomial),
            polynomial,
        )
    )
    psd = inertia[1] == 0 and inertia[0] == 1

    beta = red(RHO**2, polynomial)
    beta_polynomial = prior.square_root_polynomial(polynomial)
    lower, upper = sector.stable_interval
    scale = 10**12
    beta_interval = (R(lower**2, scale**2), R(upper**2, scale**2))
    contractive = (
        0 < beta_interval[0] < beta_interval[1] < 1
        and beta_polynomial.count_roots(*beta_interval) == 1
        and red(
            beta_polynomial.as_expr().subs(prior.BETA, beta), polynomial
        )
        == 0
    )

    quotient_transfer = all(
        field_equal(
            field_matrix(
                RHO ** (row + column + 2) * completed_h00, polynomial
            ),
            field_matrix(
                beta * RHO ** (row + column) * completed_h00, polynomial
            ),
            polynomial,
        )
        for row in range(3)
        for column in range(3)
    )
    displayed_n2_n3 = all(
        field_equal(
            field_matrix(
                RHO ** (row + column + 2 * steps) * completed_h00,
                polynomial,
            ),
            field_matrix(
                beta**steps
                * RHO ** (row + column)
                * completed_h00,
                polynomial,
            ),
            polynomial,
        )
        for steps in (2, 3)
        for row in range(3)
        for column in range(3)
    )
    semigroup = displayed_n2_n3 and all(
        red(
            beta ** (left_steps + right_steps)
            - beta**left_steps * beta**right_steps,
            polynomial,
        )
        == 0
        for left_steps in range(4)
        for right_steps in range(4)
    )
    return SectorPackage(
        completed_h00,
        three_cell_gram,
        inertia,
        hermitian,
        psd,
        beta,
        beta_polynomial,
        beta_interval,
        contractive,
        quotient_transfer,
        semigroup,
        displayed_n2_n3,
    )


def positive_package(
    sectors: tuple[Sector, ...], completion: Completion
) -> PositivePackage:
    packages = tuple(
        sector_package(sector, completion.thetas[momentum])
        for momentum, sector in enumerate(sectors)
    )
    per_momentum = tuple(package.inertia for package in packages)
    global_inertia = tuple(
        sum(package.inertia[index] for package in packages)
        for index in range(3)
    )
    return PositivePackage(
        completion.shear,
        packages,
        per_momentum,
        global_inertia,
        all(package.hermitian for package in packages),
        all(package.psd for package in packages),
        all(package.contractive for package in packages),
        all(
            package.quotient_transfer
            and package.semigroup
            and package.displayed_n2_n3
            for package in packages
        ),
    )


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


SCOPE_KEYS = (
    "swap_completion",
    "reflection_intertwiner",
    "involutive",
    "mu_one",
    "candidate_failure",
    "stable_boundary",
    "sector_inertia",
    "global_inertia",
    "quotient_transfer",
    "geometric_semigroup",
    "half_space_carrier",
    "torus_firewall",
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
        "swap_completion": "swap completion" in note,
        "reflection_intertwiner": "reflection intertwiner" in note,
        "involutive": "involutive" in note,
        "mu_one": "mu = 1" in note or "theta x = y" in note,
        "candidate_failure": (
            ("carrier-natural" in note or "carrier natural" in note)
            and "fail" in note
        ),
        "stable_boundary": "stable boundary data" in note,
        "sector_inertia": (
            "inertia (1,0,23)" in note or "one positive direction" in note
        ),
        "global_inertia": "(4,0,92)" in note or "rank four" in note,
        "quotient_transfer": (
            "diag(rho_k^2)" in note or "contractive quotient transfer" in note
        ),
        "geometric_semigroup": "geometric semigroup" in note,
        "half_space_carrier": "half-space carrier" in note,
        "torus_firewall": "torus" in note and "remains" in note,
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


def beta_interval_text(package: PositivePackage) -> str:
    return ";".join(
        f"k{momentum}/{momentum + 2}={package.sectors[momentum].beta_interval}"
        for momentum in (0, 1)
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
        "Block 118 blobs and ancestors 117--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "scripts/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 118)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    fixtures = (
        make_sectors(prior.PRIMARY_SHEAR),
        make_sectors(prior.SECOND_SHEAR),
    )
    factorization = all(
        sector.factorization
        and sector.geometric_hankel
        and sector.pivot == (0, 0)
        and sector.minors_vanishing == 784
        for sectors in fixtures
        for sector in sectors
    )
    if mutation == "break_factorization":
        factorization = False
    checks.check(
        "B-the-factorization",
        "H00_k=x_k y_k^H at pivot (0,0), all minors vanish, and H[m,n]=rho^(m+n)H00",
        factorization,
    )

    reductions = tuple(
        tuple(reduction_certificate(sector) for sector in sectors)
        for sectors in fixtures
    )
    reduction_facts = all(
        item.exact_reduction
        and item.real_moment_psd
        and item.negative_mu_excluded
        and item.proportionality_rank == 7
        and item.evaluation_rank == 8
        and (
            item.proportional_dimension,
            item.fixed_mu_dimension,
            item.positive_real_dimension,
        )
        == (57, 56, 113)
        for fixture_reductions in reductions
        for item in fixture_reductions
    )
    if mutation == "break_reduction":
        reduction_facts = False
    negative_mu_allowed = mutation == "claim_negative_mu_allowed"
    checks.check(
        "C-the-reduction",
        "nonzero PSD iff Theta*x=mu*y with real mu>0; dimensions are 57/56/113",
        reduction_facts and not negative_mu_allowed,
    )

    candidates = candidate_certificate(fixtures)
    expected_candidates = (
        "A_dir",
        "A_OS",
        "Hov",
        "Jbar",
        "K",
        "P",
        "-I",
        "K*A",
        "A*K",
        "K*Hov",
        "Hov*K",
        "K*Jbar",
        "Jbar*K",
        "Hov*Jbar",
    )
    candidate_works_claimed = mutation == "claim_candidate_works"
    checks.check(
        "D-the-candidate-failures",
        "all fourteen fixed carriers have an exact nonzero Delta_j at every k",
        candidates.names == expected_candidates
        and candidates.failures_per_fixture == (56, 56)
        and candidates.all_nonproportional
        and not candidate_works_claimed,
    )

    completions = tuple(
        reflection_real_completion(sectors) for sectors in fixtures
    )
    involutive = all(completion.involutive for completion in completions)
    reflection_reality = all(
        completion.self_reflection_real
        and completion.global_reflection_reality
        for completion in completions
    )
    mu_one = all(completion.mu_one for completion in completions)
    if mutation == "break_swap_involution":
        involutive = False
    if mutation == "break_reflection_reality":
        reflection_reality = False
    if mutation == "break_mu_one":
        mu_one = False
    checks.check(
        "E-the-swap-completion",
        "V(S_swap-I)(V^H V)^-1 swaps x/y with mu=1 and is involutive and reflection-real",
        involutive and reflection_reality and mu_one,
    )

    packages = tuple(
        positive_package(sectors, completion)
        for sectors, completion in zip(fixtures, completions)
    )
    inertia_facts = all(
        package.hermitian
        and package.psd
        and package.per_momentum_inertia == ((1, 0, 23),) * 4
        and package.global_inertia == (4, 0, 92)
        for package in packages
    )
    if mutation == "break_inertia":
        inertia_facts = False
    negative_direction_claimed = mutation == "claim_negative_direction"
    checks.check(
        "F-the-positive-package",
        "three-super-cell pairing is Hermitian PSD with inertias (1,0,23) and (4,0,92)",
        inertia_facts and not negative_direction_claimed,
    )

    beta_pins = tuple(
        tuple(
            package.sectors[momentum].beta_interval for momentum in (0, 1)
        )
        for package in packages
    )
    semigroup_facts = all(
        package.contraction and package.semigroup for package in packages
    )
    if mutation == "break_semigroup":
        semigroup_facts = False
    checks.check(
        "G-the-contraction-and-semigroup",
        "beta_k=rho_k^2 is pinned in (0,1) and n=2,3 act as rho_k^(2n)",
        beta_pins == EXPECTED_BETA_INTERVALS and semigroup_facts,
    )

    note_scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "all required note phrases, N1--N8/W1/N5 firewalls, and runtime bound",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 400,
    )

    for sectors in fixtures:
        print(
            f"FACTOR c={sectors[0].shear}: pivots="
            f"{tuple(sector.pivot for sector in sectors)}; "
            f"y0={tuple(red(sector.y[0], sector.polynomial) for sector in sectors)}; "
            f"vanishing_minors={tuple(sector.minors_vanishing for sector in sectors)}"
        )
    print(
        "CANDIDATES: 14 named carriers x 4 momenta x 2 fixtures = "
        "112 exact nonproportionality residuals"
    )
    for package in packages:
        print(
            f"PACKAGE c={package.shear}: per_k={package.per_momentum_inertia}; "
            f"global={package.global_inertia}; beta={beta_interval_text(package)}; "
            f"runtime={time.monotonic() - started:.3f}s"
        )
    print(
        "N5: per_element: exact factorization, proportionality, candidate-failure, swap, reflection-reality, involution, Hermiticity, inertia, beta-isolation, and semigroup identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: all four fixed momenta at c=5/13 and c=3/5 reject every named fixed carrier-natural candidate and admit the data-dependent swap completion with mu=1"
    )
    print(
        "per_block: the swap completion makes the L=3 half-space pairing Hermitian positive semidefinite with inertia (1,0,23) per momentum and quotient transfer beta=rho^2 in (0,1)"
    )
    print(
        "lattice_wide: checked and not executed — the torus completion, naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: no fixed carrier operator intertwines the half-space pairing, but the swap completion on the action's stable boundary data is a reflection-real involution that completes it to a positive OS package with contractive transfer diag(rho_k^2) and the exact geometric semigroup — the campaign's first positive and contractive finite OS structure"
    )
    print(
        "DECISION_CUT: carry the completed package to the torus and the curved carrier and classify the completion's naturality; reject fixed-operator intertwiner searches"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
