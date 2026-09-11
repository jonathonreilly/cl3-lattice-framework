#!/usr/bin/env python3
"""Block 111: momentum-factorized positivity frontier.

On the exact Block 110 antiperiodic reflection torus, the spatially
circulant left-dressing class factorizes into four momentum sectors.  Exact
involutions reach inertias (15,1,0) and (14,2,0), and an explicit self-sector
determinant changes sign.  Thus no fixed determinant or index obstruction
survives on this class.  The remaining paired-sector parity question is
germ-local at the displayed charts, not a transporter impossibility or a
global positivity theorem.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import subprocess

import sympy as sp

import admissibility_dirac_kahler_seam_dressing_sector_signature_2026_08_15 as block110


base = block110.prior
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_seam_dressing_sector_signature_"
    "2026_08_15.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_seam_dressing_sector_"
    "signature_2026_08_15.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_FACTORIZED_POSITIVITY_FRONTIER_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_seam_dressing_sector_signature_2026_08_15.py",
    "logs/runner-cache/admissibility_dirac_kahler_seam_dressing_sector_signature_2026_08_15.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "795e851254e689a66fa9e3fe619823835d4d8661"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block110-sector-signature-theorem-20260815"
)
PARENT_COMMIT = "d6761278fca9cac617200792473a8f4da3a6cfff"
PARENT_NOTE_BLOB = "8401946b778d8d41b0a553d0844f59e616c22e9f"
PARENT_RUNNER_BLOB = "853b86ecd81dfaedd6a84b8cc251d7913c54b6cf"
PARENT_CACHE_BLOB = "57fe4458326634d26f003bdc5ffee4866d8de439"
ANCESTOR_109 = "ad84cfcc857a65285389ba93b47cd7b718589be5"
ANCESTOR_108 = "8afe8dff5ccf531208238af0aaaec1f547d73874"
ANCESTOR_107 = "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"
ANCESTOR_106 = "22d6d90ec2279e5868c9c825149b2a20beea3797"
ANCESTOR_105 = "d06066c2b908aaca0779625d831dfb10620cf34d"
ANCESTOR_104 = "7fe07db6c03fad1191893c942f708c5cb9a54c43"
ANCESTOR_103 = "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"

I = sp.I
MASS = sp.Rational(9, 20)
PRIMARY_SHEAR = sp.Rational(5, 13)
SECOND_SHEAR = sp.Rational(3, 5)
ALL_SLICE_BLOCKS = tuple(
    (row, column) for row in range(8) for column in range(8)
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition) -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
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
        name: is_ancestor(commit, "HEAD")
        for name, commit in (
            ("ancestor_109", ANCESTOR_109),
            ("ancestor_108", ANCESTOR_108),
            ("ancestor_107", ANCESTOR_107),
            ("ancestor_106", ANCESTOR_106),
            ("ancestor_105", ANCESTOR_105),
            ("ancestor_104", ANCESTOR_104),
            ("ancestor_103", ANCESTOR_103),
        )
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


J = sp.zeros(8, 8)
E = sp.zeros(4, 8)
F = sp.zeros(4, 8)
for _row in range(8):
    J[_row, 7 - _row] = 1
for _row in range(4):
    E[_row, 4 + _row] = 1
    F[_row, 3 - _row] = 1


def spatial_shift() -> sp.Matrix:
    return (base.spatial_factors()[2] + base.spatial_factors()[3]) / 2


def projectors() -> tuple[sp.Matrix, ...]:
    cyclic = spatial_shift()
    return tuple(
        sp.simplify(
            sum(
                (I ** (-k * power) * cyclic**power for power in range(4)),
                sp.zeros(4),
            )
            / 4
        )
        for k in range(4)
    )


def momentum_block(matrix: sp.Matrix, k: int) -> sp.Matrix:
    projector = projectors()[k]
    return sp.Matrix(
        8,
        8,
        lambda row, column: sp.cancel(
            sp.trace(
                projector
                * matrix[
                    4 * row : 4 * (row + 1),
                    4 * column : 4 * (column + 1),
                ]
            )
        ),
    )


def assemble(blocks: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sum(
        (
            sp.kronecker_product(blocks[k], projectors()[k])
            for k in range(4)
        ),
        sp.zeros(base.SIZE),
    )


def gram_blocks(
    blocks: tuple[sp.Matrix, ...], propagator_blocks: tuple[sp.Matrix, ...]
) -> tuple[sp.Matrix, ...]:
    left_blocks = tuple(
        sp.simplify(E * blocks[k] * propagator_blocks[k] * F.T)
        for k in range(4)
    )
    return tuple(left_blocks[-k % 4].conjugate() for k in range(4))


def assemble_gram(blocks: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sum(
        (sp.kronecker_product(blocks[k], projectors()[k]) for k in range(4)),
        sp.zeros(16),
    )


def generic_real_basis() -> tuple[sp.Matrix, ...]:
    result: list[sp.Matrix] = []
    for row in range(8):
        for column in range(8):
            for scalar in (sp.Integer(1), I):
                item = sp.zeros(8, 8)
                item[row, column] = scalar
                result.append(item)
    return tuple(result)


def self_real_basis() -> tuple[sp.Matrix, ...]:
    result: list[sp.Matrix] = []
    for row in range(4, 8):
        for column in range(8):
            for scalar in (sp.Integer(1), I):
                lower = sp.zeros(8, 8)
                lower[row, column] = scalar
                result.append(lower + J * lower.conjugate() * J)
    return tuple(result)


def real_imag_entries(matrix: sp.Matrix) -> list[sp.Expr]:
    result: list[sp.Expr] = []
    for value in matrix:
        real, imaginary = sp.expand_complex(value).as_real_imag()
        result.extend((sp.expand(real), sp.expand(imaginary)))
    return result


def hermitian_residual(matrix: sp.Matrix) -> sp.Matrix:
    result: list[sp.Expr] = []
    for row in range(4):
        result.append(sp.expand_complex(matrix[row, row]).as_real_imag()[1])
        for column in range(row + 1, 4):
            difference = sp.expand_complex(
                matrix[row, column] - sp.conjugate(matrix[column, row])
            )
            real, imaginary = difference.as_real_imag()
            result.extend((sp.expand(real), sp.expand(imaginary)))
    return sp.Matrix(result)


def restriction(
    basis: tuple[sp.Matrix, ...],
    propagators: tuple[sp.Matrix, ...],
    paired: bool = False,
) -> sp.Matrix:
    columns: list[list[sp.Expr]] = []
    for item in basis:
        values: list[sp.Expr] = []
        for index, propagator in enumerate(propagators):
            use = J * item.conjugate() * J if paired and index == 1 else item
            values.extend(hermitian_residual(E * use * propagator * F.T))
        columns.append(values)
    return sp.Matrix(
        16 * len(propagators),
        len(basis),
        lambda row, column: columns[column][row],
    )


def nullspace_columns(matrix: sp.Matrix) -> sp.Matrix:
    columns = matrix.nullspace()
    return sp.Matrix.hstack(*columns) if columns else sp.zeros(matrix.cols, 0)


def exact_inertia(matrix: sp.Matrix) -> tuple[int, int, int]:
    if not base.matrix_equal(matrix, matrix.H):
        return (-1, -1, -1)
    minors = tuple(
        sp.factor(matrix[:size, :size].det(method="domain-ge"))
        for size in range(1, matrix.rows + 1)
    )
    if any(value == 0 for value in minors):
        return (-1, -1, -1)
    return base.inertia_from_nonzero_leading_minors(minors)


def direct_inertia(matrix: sp.Matrix) -> tuple[tuple[int, int, int], tuple[sp.Expr, ...]]:
    minors = tuple(sp.factor(value) for value in base.leading_minors(matrix))
    if any(value == 0 for value in minors):
        return (-1, -1, -1), minors
    return base.inertia_from_nonzero_leading_minors(minors), minors


def self_direct_system(propagator: sp.Matrix) -> sp.Matrix:
    columns: list[list[sp.Expr]] = []
    for item in generic_real_basis():
        reality = item - J * item.conjugate() * J
        values = real_imag_entries(reality)
        values.extend(hermitian_residual(E * item * propagator * F.T))
        columns.append(values)
    return sp.Matrix(
        144,
        128,
        lambda row, column: columns[column][row],
    )


def paired_direct_system(
    first_propagator: sp.Matrix, third_propagator: sp.Matrix
) -> sp.Matrix:
    generic = generic_real_basis()
    columns: list[list[sp.Expr]] = []
    zero = sp.zeros(8)
    for sector in range(2):
        for item in generic:
            first = item if sector == 0 else zero
            third = item if sector == 1 else zero
            reality = third - J * first.conjugate() * J
            values = real_imag_entries(reality)
            values.extend(hermitian_residual(E * first * first_propagator * F.T))
            values.extend(hermitian_residual(E * third * third_propagator * F.T))
            columns.append(values)
    return sp.Matrix(
        160,
        256,
        lambda row, column: columns[column][row],
    )


@dataclass(frozen=True)
class LinearMomentumData:
    propagator_conjugacy: bool
    self_ranks: tuple[int, int]
    pair_rank: int
    dimensions: tuple[int, int, int]
    direct_ranks: tuple[int, int, int]
    direct_dimension: int


def linear_momentum_data(fixture, compute_direct: bool = True) -> LinearMomentumData:
    propagators = tuple(momentum_block(fixture.propagator, k) for k in range(4))
    self_basis = self_real_basis()
    generic_basis = generic_real_basis()
    self_ranks = (
        base.exact_rank(restriction(self_basis, (propagators[0],))),
        base.exact_rank(restriction(self_basis, (propagators[2],))),
    )
    pair_rank = base.exact_rank(
        restriction(generic_basis, (propagators[1], propagators[3]), paired=True)
    )
    dimensions = (
        64 - self_ranks[0],
        128 - pair_rank,
        64 - self_ranks[1],
    )
    direct_ranks = (
        (
            base.exact_rank(self_direct_system(propagators[0])),
            base.exact_rank(paired_direct_system(propagators[1], propagators[3])),
            base.exact_rank(self_direct_system(propagators[2])),
        )
        if compute_direct
        else ()
    )
    return LinearMomentumData(
        all(
            base.matrix_equal(
                propagators[-k % 4], propagators[k].conjugate()
            )
            for k in range(4)
        ),
        self_ranks,
        pair_rank,
        dimensions,
        direct_ranks,
        512 - sum(direct_ranks) if compute_direct else -1,
    )


@dataclass(frozen=True)
class MomentumFactorizationCertificate:
    projector_ranks: tuple[int, ...]
    projector_eigenvalues: bool
    projector_resolution: bool
    projector_conjugation: bool
    primary: LinearMomentumData
    second: LinearMomentumData
    expected_dimensions: tuple[int, int, int]
    involution_decoupling: bool
    gram_decomposition: bool
    block_hermiticity: bool
    sector_inertia: tuple[tuple[int, int, int], ...]
    additive_inertia: tuple[int, int, int]


def momentum_factorization_certificate(
    primary_linear: LinearMomentumData,
    second_linear: LinearMomentumData,
    pinned_witness: "FixtureWitness",
    mutation: str,
) -> MomentumFactorizationCertificate:
    cyclic = spatial_shift()
    pis = projectors()
    conjugate_indices = (
        (0, 1, 2, 3)
        if mutation == "break_projector_conjugation"
        else (0, 3, 2, 1)
    )
    expected_dimensions = (
        (48, 95, 49)
        if mutation == "claim_wrong_sector_dims"
        else (48, 96, 48)
    )
    squared = tuple(block * block for block in pinned_witness.blocks)
    assembled_square = pinned_witness.dressing * pinned_witness.dressing
    sector_inertia = tuple(exact_inertia(block) for block in pinned_witness.kblocks)
    additive = (
        sum(value[0] for value in sector_inertia),
        sum(value[1] for value in sector_inertia),
        sum(value[2] for value in sector_inertia),
    )
    return MomentumFactorizationCertificate(
        tuple(base.exact_rank(projector) for projector in pis),
        all(
            base.matrix_equal(cyclic * pis[k], I**k * pis[k])
            for k in range(4)
        ),
        base.matrix_equal(sum(pis, sp.zeros(4)), sp.eye(4))
        and all(
            base.matrix_equal(
                pis[j] * pis[k], pis[k] if j == k else sp.zeros(4)
            )
            for j in range(4)
            for k in range(4)
        ),
        all(
            base.matrix_equal(pis[k].conjugate(), pis[conjugate_indices[k]])
            for k in range(4)
        ),
        primary_linear,
        second_linear,
        expected_dimensions,
        base.matrix_equal(assembled_square, assemble(squared)),
        base.matrix_equal(
            pinned_witness.gram, assemble_gram(pinned_witness.kblocks)
        ),
        all(base.matrix_equal(block, block.H) for block in pinned_witness.kblocks),
        sector_inertia,
        additive,
    )


def support_embedding(factor_indices: tuple[int, ...]) -> sp.Matrix:
    embedding = sp.zeros(512, 2 * len(ALL_SLICE_BLOCKS) * len(factor_indices))
    local = 0
    for slice_i, slice_j in ALL_SLICE_BLOCKS:
        for factor_index in factor_indices:
            for imaginary in (0, 1):
                embedding[
                    base.parameter_index(slice_i, slice_j, factor_index, imaginary),
                    local,
                ] = 1
                local += 1
    return embedding


@dataclass(frozen=True)
class ClassDecompositionCertificate:
    primary_dimensions: tuple[int, int, int]
    second_dimensions: tuple[int, int, int]
    factor_rank: int
    extended_factor_rank: int
    expected_extended_rank: int
    disjoint_coordinates: bool
    primary_full_dimension: int
    second_full_dimension: int
    expected_direct_sum: int


def class_decomposition_certificate(
    reality: sp.Matrix,
    reality_transform: sp.Matrix,
    primary_hermiticity: sp.Matrix,
    second_hermiticity: sp.Matrix,
    mutation: str,
) -> ClassDecompositionCertificate:
    circ = support_embedding((0, 2, 3))
    s1 = support_embedding((1,))

    def dimensions(hermiticity: sp.Matrix) -> tuple[int, int, int]:
        joint = reality.col_join(hermiticity)
        circ_rank = base.exact_rank(joint * circ)
        s1_rank = base.exact_rank(joint * s1)
        return (
            circ.cols - circ_rank,
            s1.cols - s1_rank,
            reality_transform.cols
            - base.exact_rank(hermiticity * reality_transform),
        )

    factors = base.spatial_factors()
    factor_columns = [sp.Matrix(list(item)) for item in factors]
    cyclic_squared = spatial_shift() ** 2
    extended = factor_columns + [sp.Matrix(list(cyclic_squared))]
    expected_extended_rank = 4 if mutation == "break_c2_independence" else 5
    expected_direct_sum = 131 if mutation == "claim_mixed_only_directions" else 132
    primary_dimensions = dimensions(primary_hermiticity)
    second_dimensions = dimensions(second_hermiticity)
    return ClassDecompositionCertificate(
        primary_dimensions,
        second_dimensions,
        base.exact_rank(sp.Matrix.hstack(*factor_columns)),
        base.exact_rank(sp.Matrix.hstack(*extended)),
        expected_extended_rank,
        base.matrix_equal(circ.T * s1, sp.zeros(circ.cols, s1.cols)),
        primary_dimensions[2],
        second_dimensions[2],
        expected_direct_sum,
    )


def tau_real_change() -> sp.Matrix:
    columns: list[sp.Matrix] = []
    for index in range(4):
        first = sp.zeros(8, 1)
        first[index] = first[7 - index] = 1
        columns.append(first)
        second = sp.zeros(8, 1)
        second[index] = I
        second[7 - index] = -I
        columns.append(second)
    return sp.Matrix.hstack(*columns)


@dataclass(frozen=True)
class SelfFamily:
    candidate: sp.Matrix
    variables: tuple[sp.Symbol, ...]
    source_free_order: tuple[str, ...]
    system_rank: int
    parameter_count: int
    frame_reality: bool
    family_reality: bool
    family_involution: bool
    gram_hermiticity: bool
    determinant: sp.Expr

    def at(self, values: tuple[int, int, int]) -> sp.Matrix:
        return sp.simplify(self.candidate.subs(dict(zip(self.variables, values))))


def self_triangular_family(propagator: sp.Matrix) -> SelfFamily:
    change = tau_real_change()
    inverse = change.inv()
    plus = (1, 6, 7)
    minus = (0, 2, 3, 4, 5)
    diagonal = sp.diag(*(1 if index in plus else -1 for index in range(8)))
    seed = change * diagonal * inverse
    directions: list[sp.Matrix] = []
    for row in plus:
        for column in minus:
            elementary = sp.zeros(8, 8)
            elementary[row, column] = 1
            directions.append(change * elementary * inverse)
    columns = [
        hermitian_residual(E * item * propagator * F.T) for item in directions
    ]
    system = sp.Matrix(16, 15, lambda row, column: columns[column][row])
    rhs = -hermitian_residual(E * seed * propagator * F.T)
    coordinates, parameters = system.gauss_jordan_solve(rhs)
    free = sorted(
        set().union(*(entry.free_symbols for entry in coordinates)), key=str
    )
    variables = sp.symbols("tau0:3", real=True)
    coordinates = coordinates.xreplace(dict(zip(free, variables)))
    negative = seed + sum(
        (coordinates[index] * item for index, item in enumerate(directions)),
        sp.zeros(8),
    )
    candidate = sp.simplify(-negative)
    gram = sp.simplify(E * candidate * propagator * F.T)
    determinant = sp.factor(gram.det(method="domain-ge"))
    return SelfFamily(
        candidate,
        variables,
        tuple(str(symbol) for symbol in free),
        base.exact_rank(system),
        parameters.rows,
        base.matrix_equal(J * change.conjugate(), change),
        base.matrix_equal(J * candidate.conjugate() * J, candidate),
        base.matrix_equal(candidate * candidate, sp.eye(8)),
        base.matrix_equal(gram, gram.H),
        determinant,
    )


PRIMARY_R = (
    (1, 0), (0, -2), (0, -2), (0, 0), (0, 0), (0, 0), (0, 0), (-1, 1),
    (-1, 0), (1, 2), (0, 2), (0, 0), (-1, 2), (-1, 0), (0, 0), (2, -1),
    (0, 0), (1, 0), (1, 0), (0, 0), (0, 0), (0, 0), (1, 0), (1, -1),
    (1, -1), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0),
    (2, 0), (1, 0), (0, 0), (1, 1), (0, 2), (-1, 0), (0, 0), (1, 0),
    (0, 0), (-1, 1), (0, 0), (0, 0), (-1, -2), (2, -1), (-1, -1), (-3, 1),
    (-1, -1), (0, -4), (0, -2), (0, 0), (3, 1), (-1, 3), (3, 0), (2, -4),
    (0, 0), (-1, 1), (-1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0),
)

SECOND_R = (
    (1, 0), (1, -1), (-1, -1), (3, 1), (0, 0), (0, 0), (1, -2), (1, -1),
    (0, 0), (1, 0), (0, 0), (-2, 0), (0, 0), (0, 0), (-1, 1), (0, 0),
    (0, 0), (1, 0), (0, -1), (0, 2), (0, 0), (0, 0), (1, 0), (1, 0),
    (0, 0), (0, -1), (-1, 1), (2, 1), (0, 0), (0, 0), (0, 0), (0, -1),
    (1, 0), (0, 0), (2, 0), (1, -1), (1, 0), (0, 0), (1, 0), (-1, 1),
    (0, 1), (1, 0), (1, 1), (1, 3), (0, 1), (1, 0), (1, 2), (-1, 0),
    (1, 0), (0, 0), (2, 0), (2, 0), (1, 0), (0, 0), (2, 0), (-1, 1),
    (0, 0), (2, 1), (0, -2), (-2, 4), (0, 0), (0, 0), (2, 1), (2, 1),
)


@dataclass(frozen=True)
class PairChart:
    first: sp.Matrix
    third: sp.Matrix
    system_rank: int
    first_involution: bool
    third_involution: bool
    conjugate_reality: bool
    gram_hermiticity: bool


def pair_candidate(
    first_propagator: sp.Matrix,
    third_propagator: sp.Matrix,
    raw_change: tuple[tuple[int, int], ...],
) -> PairChart:
    change = sp.Matrix(
        8,
        8,
        [real + I * imaginary for real, imaginary in raw_change],
    )
    inverse = change.inv()
    diagonal = sp.diag(1, 1, 1, 1, -1, -1, -1, -1)
    seed = change * diagonal * inverse
    directions: list[sp.Matrix] = []
    for row in range(4):
        for column in range(4, 8):
            for scalar in (sp.Integer(1), I):
                elementary = sp.zeros(8, 8)
                elementary[row, column] = scalar
                directions.append(change * elementary * inverse)
    rhs: list[sp.Expr] = []
    columns: list[list[sp.Matrix]] = [[], []]
    for position, propagator in enumerate((first_propagator, third_propagator)):
        use_seed = seed if position == 0 else J * seed.conjugate() * J
        rhs.extend(-hermitian_residual(E * use_seed * propagator * F.T))
        for item in directions:
            use = item if position == 0 else J * item.conjugate() * J
            columns[position].append(
                hermitian_residual(E * use * propagator * F.T)
            )
    system = sp.Matrix(
        32,
        32,
        lambda row, column: columns[row // 16][column][row % 16],
    )
    coordinates = system.inv(method="DM") * sp.Matrix(rhs)
    first = sp.simplify(
        seed
        + sum(
            (
                coordinates[index] * item
                for index, item in enumerate(directions)
            ),
            sp.zeros(8),
        )
    )
    third = sp.simplify(J * first.conjugate() * J)
    first_gram = sp.simplify(E * first * first_propagator * F.T)
    third_gram = sp.simplify(E * third * third_propagator * F.T)
    return PairChart(
        first,
        third,
        base.exact_rank(system),
        base.matrix_equal(first * first, sp.eye(8)),
        base.matrix_equal(third * third, sp.eye(8)),
        base.matrix_equal(third, J * first.conjugate() * J),
        base.matrix_equal(first_gram, first_gram.H)
        and base.matrix_equal(third_gram, third_gram.H),
    )


@dataclass(frozen=True)
class FixtureWitness:
    shear: sp.Rational
    fixture: object
    propagator_blocks: tuple[sp.Matrix, ...]
    self_zero: SelfFamily
    self_two: SelfFamily
    pair: PairChart
    blocks: tuple[sp.Matrix, ...]
    dressing: sp.Matrix
    kblocks: tuple[sp.Matrix, ...]
    gram: sp.Matrix
    sector_inertias: tuple[tuple[int, int, int], ...]
    inertia: tuple[int, int, int]
    determinant: sp.Expr
    involution: bool
    reality: bool
    hermiticity: bool
    decomposition: bool


def fixture_witness(
    shear: sp.Rational,
    raw_change: tuple[tuple[int, int], ...],
) -> FixtureWitness:
    fixture = base.fixture_data(shear)
    propagators = tuple(momentum_block(fixture.propagator, k) for k in range(4))
    self_zero = self_triangular_family(propagators[0])
    self_two = self_triangular_family(propagators[2])
    pair = pair_candidate(propagators[1], propagators[3], raw_change)
    file_tau = (-6, -6, -6)
    blocks = (
        self_zero.at(file_tau),
        pair.first,
        self_two.at(file_tau),
        pair.third,
    )
    dressing = assemble(blocks)
    kblocks = gram_blocks(blocks, propagators)
    gram = base.dressed_gram(dressing, fixture)
    sector_inertias = tuple(exact_inertia(block) for block in kblocks)
    inertia = (
        sum(value[0] for value in sector_inertias),
        sum(value[1] for value in sector_inertias),
        sum(value[2] for value in sector_inertias),
    )
    return FixtureWitness(
        shear,
        fixture,
        propagators,
        self_zero,
        self_two,
        pair,
        blocks,
        dressing,
        kblocks,
        gram,
        sector_inertias,
        inertia,
        sp.factor(gram.det(method="domain-ge")),
        base.matrix_equal(dressing * dressing, sp.eye(base.SIZE)),
        base.matrix_equal(
            fixture.reflection * dressing.conjugate() * fixture.reflection,
            dressing,
        ),
        base.matrix_equal(gram, gram.H),
        base.matrix_equal(gram, assemble_gram(kblocks)),
    )


@dataclass(frozen=True)
class NearPositiveCertificate:
    primary: FixtureWitness
    second: FixtureWitness
    expected_primary_inertia: tuple[int, int, int]


def near_positive_certificate(
    primary: FixtureWitness,
    second: FixtureWitness,
    mutation: str,
) -> NearPositiveCertificate:
    expected = (16, 0, 0) if mutation == "claim_file_point_positive" else (15, 1, 0)
    return NearPositiveCertificate(primary, second, expected)


TARGET_WITNESS_DETERMINANT = sp.Rational(
    -952483819446288555393408748681387763238904565727822844475274893721600000000000,
    50541872451803201688403110994090831298117817049759327949912224801699937566860497,
)


@dataclass(frozen=True)
class AffineDeterminantFactor:
    determinant: sp.Expr
    positive_coefficient: sp.Rational
    affine: sp.Expr
    exact_factorization: bool
    affine_tau_zero_two_only: bool
    sign_tunable: bool


def affine_determinant_factor(family: SelfFamily) -> AffineDeterminantFactor:
    polynomial = sp.Poly(-family.determinant, *family.variables, domain=sp.QQ)
    content, primitive = polynomial.primitive()
    if content < 0:
        content = -content
        primitive = -primitive
    affine = sp.factor(primitive.as_expr())
    allowed_monomials = {(0, 0, 0), (1, 0, 0), (0, 0, 1)}
    affine_shape = (
        polynomial.total_degree() == 1
        and set(polynomial.monoms()).issubset(allowed_monomials)
        and any(
            polynomial.coeff_monomial(monomial) != 0
            for monomial in ((1, 0, 0), (0, 0, 1))
        )
    )
    coefficients = [
        sp.expand(affine).coeff(variable) for variable in family.variables
    ]
    active = next(
        (index for index in (0, 2) if coefficients[index] != 0),
        None,
    )
    sign_tunable = False
    if active is not None:
        zero_values = {variable: 0 for variable in family.variables}
        constant = sp.expand(affine).subs(zero_values)
        crossing = -constant / coefficients[active]
        below = dict(zero_values)
        above = dict(zero_values)
        below[family.variables[active]] = crossing - 1
        above[family.variables[active]] = crossing + 1
        sign_tunable = bool(
            sp.expand(affine.subs(below) * affine.subs(above)) < 0
        )
    return AffineDeterminantFactor(
        family.determinant,
        content,
        affine,
        sp.expand(family.determinant + content * affine) == 0,
        affine_shape,
        sign_tunable,
    )


@dataclass(frozen=True)
class AssemblyCheck:
    signs: tuple[int, int, int]
    involution: bool
    reality: bool
    hermiticity: bool
    decomposition: bool
    sector_inertia: tuple[int, int, int]
    direct_inertia: tuple[int, int, int]
    leading_minor_count: int
    determinant: sp.Expr


@dataclass(frozen=True)
class DeterminantRefutationCertificate:
    witness: sp.Matrix
    witness_involution: bool
    witness_reality: bool
    witness_hermiticity: bool
    witness_inertia: tuple[int, int, int]
    witness_determinant: sp.Expr
    expected_witness_determinant: sp.Expr
    assemblies: tuple[AssemblyCheck, ...]
    expected_positive_indices: tuple[int, ...]
    zero_factor: AffineDeterminantFactor
    two_factor: AffineDeterminantFactor
    file_to_witness_sign_flip: bool


def determinant_refutation_certificate(
    primary: FixtureWitness,
    mutation: str,
) -> DeterminantRefutationCertificate:
    witness_tau = (1, -6, -6)
    witness = primary.self_zero.at(witness_tau)
    witness_x = sp.simplify(
        E * witness * primary.propagator_blocks[0] * F.T
    )
    witness_y = witness_x.conjugate()
    witness_determinant = sp.factor(witness_x.det(method="domain-ge"))
    expected_witness = (
        -TARGET_WITNESS_DETERMINANT
        if mutation == "break_witness_determinant"
        else TARGET_WITNESS_DETERMINANT
    )
    assemblies: list[AssemblyCheck] = []
    for sign_zero, sign_pair, sign_two in product((-1, 1), repeat=3):
        signs = (sign_zero, sign_pair, sign_two)
        blocks = (
            sign_zero * witness,
            sign_pair * primary.blocks[1],
            sign_two * primary.blocks[2],
            sign_pair * primary.blocks[3],
        )
        dressing = assemble(blocks)
        kblocks = gram_blocks(blocks, primary.propagator_blocks)
        gram = base.dressed_gram(dressing, primary.fixture)
        parts = tuple(exact_inertia(block) for block in kblocks)
        sector_inertia = (
            sum(value[0] for value in parts),
            sum(value[1] for value in parts),
            sum(value[2] for value in parts),
        )
        full_inertia, minors = direct_inertia(gram)
        assemblies.append(
            AssemblyCheck(
                signs,
                base.matrix_equal(dressing * dressing, sp.eye(base.SIZE)),
                base.matrix_equal(
                    primary.fixture.reflection
                    * dressing.conjugate()
                    * primary.fixture.reflection,
                    dressing,
                ),
                base.matrix_equal(gram, gram.H),
                base.matrix_equal(gram, assemble_gram(kblocks)),
                sector_inertia,
                full_inertia,
                len(minors),
                minors[-1],
            )
        )
    expected_indices = (
        (1, 3, 5, 7, 9, 11, 13, 15)
        if mutation == "claim_fixed_parity"
        else (2, 4, 6, 8, 8, 10, 12, 14)
    )
    zero_factor = affine_determinant_factor(primary.self_zero)
    two_factor = affine_determinant_factor(primary.self_two)
    file_x = sp.simplify(
        E * primary.blocks[0] * primary.propagator_blocks[0] * F.T
    )
    return DeterminantRefutationCertificate(
        witness,
        base.matrix_equal(witness * witness, sp.eye(8)),
        base.matrix_equal(J * witness.conjugate() * J, witness),
        base.matrix_equal(witness_x, witness_x.H),
        exact_inertia(witness_y),
        witness_determinant,
        expected_witness,
        tuple(assemblies),
        expected_indices,
        zero_factor,
        two_factor,
        bool(sp.factor(file_x.det(method="domain-ge")) > 0)
        and bool(witness_determinant < 0),
    )


@dataclass(frozen=True)
class PairedParityCertificate:
    primary_paired_positive: int
    second_paired_positive: int
    germ_local_only: bool


def paired_parity_certificate(
    primary: FixtureWitness,
    second: FixtureWitness,
    mutation: str,
) -> PairedParityCertificate:
    return PairedParityCertificate(
        primary.sector_inertias[1][0] + primary.sector_inertias[3][0],
        second.sector_inertias[1][0] + second.sector_inertias[3][0],
        mutation != "claim_parity_proven_global",
    )


def pure_imaginary_equal_basis(
    propagator_blocks: tuple[sp.Matrix, ...],
) -> tuple[tuple[sp.Matrix, ...], int, bool]:
    basis = self_real_basis()
    hermiticity = restriction(
        basis,
        (propagator_blocks[1], propagator_blocks[3]),
    )
    real_part = sp.Matrix(
        64,
        64,
        lambda row, column: sp.expand_complex(
            basis[column][row]
        ).as_real_imag()[0],
    )
    system = hermiticity.col_join(real_part)
    kernel = nullspace_columns(system)
    result: list[sp.Matrix] = []
    for column in range(kernel.cols):
        candidate = sum(
            (
                kernel[index, column] * item
                for index, item in enumerate(basis)
            ),
            sp.zeros(8),
        )
        result.append(sp.simplify(-I * candidate))
    real_basis = tuple(result)
    all_real = all(
        all(sp.expand_complex(value).as_real_imag()[1] == 0 for value in item)
        for item in real_basis
    )
    return real_basis, base.exact_rank(system), all_real


def residual_rank(
    basis: tuple[sp.Matrix, ...],
    residual,
) -> int:
    columns = [sp.Matrix(list(residual(item))) for item in basis]
    if not columns:
        return 0
    return base.exact_rank(sp.Matrix.hstack(*columns))


def slice_shift() -> sp.Matrix:
    result = sp.zeros(8, 8)
    for column in range(8):
        result[(column + 1) % 8, column] = 1
    return result


@dataclass(frozen=True)
class EvenClosureCertificate:
    ambient_rank: int
    ambient_dimension: int
    real_basis: bool
    structured_dimensions: tuple[int, int, int]
    expected_dimensions: tuple[int, int, int]


def even_closure_certificate(
    primary: FixtureWitness,
    mutation: str,
) -> EvenClosureCertificate:
    basis, ambient_rank, all_real = pure_imaginary_equal_basis(
        primary.propagator_blocks
    )
    cyclic = slice_shift()

    def anti_diagonal_residual(matrix: sp.Matrix) -> sp.Matrix:
        return sp.Matrix(
            [
                matrix[row, column]
                for row in range(8)
                for column in range(8)
                if row + column != 7
            ]
        )

    structured_ranks = (
        residual_rank(basis, lambda matrix: matrix.T + matrix),
        residual_rank(basis, lambda matrix: matrix * cyclic - cyclic * matrix),
        residual_rank(basis, anti_diagonal_residual),
    )
    dimensions = tuple(len(basis) - rank for rank in structured_ranks)
    expected = (1, 0, 0) if mutation == "claim_subfamily_solvable" else (0, 0, 0)
    return EvenClosureCertificate(
        ambient_rank,
        len(basis),
        all_real,
        dimensions,
        expected,
    )


MIXTURE_DIFFERENCE_00 = sp.Rational(
    66667926566900395648942328374420150587344777280,
    61391349876435377016600254323619839508354485363,
)


@dataclass(frozen=True)
class MixtureCertificate:
    astar_identification: bool
    ac_circulant: bool
    ac_reality: bool
    ac_identity_gram: bool
    gram_linearity: bool
    ac_even: bool
    astar_odd: bool
    difference_identity: bool
    sum_identity: bool
    difference_entry: sp.Expr
    sum_entry: sp.Expr
    expected_difference_entry: sp.Expr
    neither_grading_sign: bool


def mixture_certificate(
    primary: FixtureWitness,
    mutation: str,
) -> MixtureCertificate:
    cyclic = spatial_shift()
    carrier_shift = sp.kronecker_product(sp.eye(8), cyclic)
    positive_shift = sp.kronecker_product(sp.eye(4), cyclic)
    raw_fiber = block110.positive_fiber_representative(primary.fixture)
    ac = sp.simplify(
        (raw_fiber + carrier_shift * raw_fiber * carrier_shift.inv()) / 2
    )
    signs = (1, -1, 1, -1, -1, 1, -1, 1)
    slice_adiagonal = sp.zeros(8, 8)
    for row, value in enumerate(signs):
        slice_adiagonal[row, 7 - row] = value
    constructed_astar = sp.kronecker_product(
        slice_adiagonal,
        base.spatial_factors()[1],
    )
    expected_astar = (
        -base.global_candidate()
        if mutation == "break_astar_identification"
        else base.global_candidate()
    )
    astar = base.global_candidate()
    mixture = ac + astar
    kac = base.dressed_gram(ac, primary.fixture)
    kastar = base.dressed_gram(astar, primary.fixture)
    kmix = base.dressed_gram(mixture, primary.fixture)
    transformed = positive_shift * kmix * positive_shift.inv()
    difference = sp.simplify(transformed - kmix)
    total = sp.simplify(transformed + kmix)
    expected_entry = (
        -MIXTURE_DIFFERENCE_00
        if mutation == "break_grading_split"
        else MIXTURE_DIFFERENCE_00
    )
    return MixtureCertificate(
        base.matrix_equal(constructed_astar, expected_astar),
        base.matrix_equal(
            carrier_shift * ac * carrier_shift.inv(), ac
        ),
        base.matrix_equal(
            primary.fixture.reflection * ac.conjugate() * primary.fixture.reflection,
            ac,
        ),
        base.matrix_equal(kac, sp.eye(16)),
        base.matrix_equal(kmix, kac + kastar),
        base.matrix_equal(
            positive_shift * kac * positive_shift.inv(), kac
        ),
        base.matrix_equal(
            positive_shift * kastar * positive_shift.inv(), -kastar
        ),
        base.matrix_equal(difference, -2 * kastar),
        base.matrix_equal(total, 2 * sp.eye(16)),
        sp.factor(difference[0, 0]),
        sp.factor(total[0, 0]),
        expected_entry,
        not base.matrix_equal(transformed, kmix)
        and not base.matrix_equal(transformed, -kmix),
    )


SCOPE_KEYS = (
    "momentum_factorization",
    "determinant_refutation",
    "near_positive",
    "even_frontier",
    "paired_parity",
    "germ_local",
    "direct_sum",
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
        "momentum_factorization": (
            "momentum factorization" in note
            or "factorizes over spatial momenta" in note
        ),
        "determinant_refutation": (
            "determinant obstruction is refuted" in note
            or "no fixed index parity" in note
        ),
        "near_positive": "(15,1,0)" in note,
        "even_frontier": "(14,2,0)" in note,
        "paired_parity": "paired-sector parity" in note,
        "germ_local": "germ-local" in note,
        "direct_sum": "direct sum" in note,
        "transporter_boundary": "not a transporter impossibility" in note,
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
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
    "break_projector_conjugation",
    "claim_wrong_sector_dims",
    "break_c2_independence",
    "claim_mixed_only_directions",
    "claim_file_point_positive",
    "break_witness_determinant",
    "claim_fixed_parity",
    "claim_parity_proven_global",
    "claim_subfamily_solvable",
    "break_astar_identification",
    "break_grading_split",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_adm_link_derived",
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
        "A-authority-and-Block110-parent",
        "current axioms, registries, ancestry, and the Block110 parent triple are content-bound",
        authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(authority[f"ancestor_{number}"] for number in range(103, 110))
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    primary = fixture_witness(PRIMARY_SHEAR, PRIMARY_R)
    second = fixture_witness(SECOND_SHEAR, SECOND_R)
    primary_linear = linear_momentum_data(primary.fixture)
    second_linear = linear_momentum_data(second.fixture, compute_direct=False)
    momentum = momentum_factorization_certificate(
        primary_linear,
        second_linear,
        primary,
        mutation,
    )
    checks.check(
        "B-momentum-factorization",
        "the 256-complex-parameter circulant class factorizes as 48+96+48=192 and inertia adds",
        momentum.projector_ranks == (1, 1, 1, 1)
        and momentum.projector_eigenvalues
        and momentum.projector_resolution
        and momentum.projector_conjugation
        and momentum.primary.propagator_conjugacy
        and momentum.second.propagator_conjugacy
        and momentum.primary.self_ranks == momentum.second.self_ranks == (16, 16)
        and momentum.primary.pair_rank == momentum.second.pair_rank == 32
        and momentum.primary.dimensions
        == momentum.second.dimensions
        == momentum.expected_dimensions
        and sum(momentum.primary.dimensions) == 192
        and momentum.primary.direct_ranks == (80, 160, 80)
        and momentum.primary.direct_dimension == 192
        and momentum.involution_decoupling
        and momentum.gram_decomposition
        and momentum.block_hermiticity
        and momentum.additive_inertia == primary.inertia,
    )

    reality, transform = base.reality_system()
    primary_hermiticity = base.global_hermiticity_matrix(primary.fixture)
    second_hermiticity = base.global_hermiticity_matrix(second.fixture)
    decomposition = class_decomposition_certificate(
        reality,
        transform,
        primary_hermiticity,
        second_hermiticity,
        mutation,
    )
    checks.check(
        "C-class-decomposition",
        "the Block109 joint space is exactly the direct sum V_circ(128)+V_S1(4), with C^2 independent",
        base.matrix_equal(reality * transform, sp.zeros(512, 256))
        and base.exact_rank(transform) == 256
        and decomposition.primary_dimensions
        == decomposition.second_dimensions
        == (128, 4, 132)
        and decomposition.factor_rank == 4
        and decomposition.extended_factor_rank
        == decomposition.expected_extended_rank
        and decomposition.disjoint_coordinates
        and decomposition.primary_full_dimension
        == decomposition.second_full_dimension
        == decomposition.expected_direct_sum
        and decomposition.primary_dimensions[0]
        + decomposition.primary_dimensions[1]
        == decomposition.primary_dimensions[2],
    )

    near = near_positive_certificate(primary, second, mutation)
    all_self_families = (
        primary.self_zero,
        primary.self_two,
        second.self_zero,
        second.self_two,
    )
    all_pairs = (primary.pair, second.pair)
    primary_block_det_product = sp.factor(
        sp.prod(block.det(method="domain-ge") for block in primary.kblocks)
    )
    second_block_det_product = sp.factor(
        sp.prod(block.det(method="domain-ge") for block in second.kblocks)
    )
    checks.check(
        "D-near-positive-certificate",
        "both exact all-plus file points are involutions with Hermitian Gram, inertia (15,1,0), and negative determinant",
        MASS == sp.Rational(9, 20)
        and primary.shear == sp.Rational(5, 13)
        and second.shear == sp.Rational(3, 5)
        and all(
            family.system_rank == 12
            and family.parameter_count == 3
            and family.source_free_order == ("tau0", "tau1", "tau2")
            and family.frame_reality
            and family.family_reality
            and family.family_involution
            and family.gram_hermiticity
            for family in all_self_families
        )
        and all(
            pair.system_rank == 32
            and pair.first_involution
            and pair.third_involution
            and pair.conjugate_reality
            and pair.gram_hermiticity
            for pair in all_pairs
        )
        and all(
            witness.involution
            and witness.reality
            and witness.hermiticity
            and witness.decomposition
            for witness in (primary, second)
        )
        and primary.inertia == near.expected_primary_inertia
        and second.inertia == (15, 1, 0)
        and primary.determinant == primary_block_det_product
        and second.determinant == second_block_det_product
        and primary.determinant < 0
        and second.determinant < 0,
    )

    refutation = determinant_refutation_certificate(primary, mutation)
    obtained_indices = tuple(
        sorted(assembly.direct_inertia[0] for assembly in refutation.assemblies)
    )
    determinant_factors = (refutation.zero_factor, refutation.two_factor)
    checks.check(
        "E-determinant-refutation",
        "the tau=(1,-6,-6) block refutes fixed determinant and index parity; eight assemblies reach (14,2,0)",
        refutation.witness_involution
        and refutation.witness_reality
        and refutation.witness_hermiticity
        and refutation.witness_inertia == (3, 1, 0)
        and refutation.witness_determinant
        == refutation.expected_witness_determinant
        and len(refutation.assemblies) == 8
        and all(
            assembly.involution
            and assembly.reality
            and assembly.hermiticity
            and assembly.decomposition
            and assembly.sector_inertia == assembly.direct_inertia
            and assembly.leading_minor_count == 16
            and assembly.determinant > 0
            for assembly in refutation.assemblies
        )
        and obtained_indices == refutation.expected_positive_indices
        and max(
            (assembly.direct_inertia for assembly in refutation.assemblies),
            key=lambda value: value[0],
        )
        == (14, 2, 0)
        and primary.inertia[0] % 2 == 1
        and all(assembly.direct_inertia[0] % 2 == 0 for assembly in refutation.assemblies)
        and all(
            factor.positive_coefficient > 0
            and factor.exact_factorization
            and factor.affine_tau_zero_two_only
            and factor.sign_tunable
            for factor in determinant_factors
        )
        and refutation.file_to_witness_sign_flip,
    )

    parity = paired_parity_certificate(primary, second, mutation)
    checks.check(
        "F-paired-sector-parity-boundary",
        "paired-sector parity is odd here: a GERM-LOCAL observation, NOT a proven global invariant; the global decision is open",
        parity.primary_paired_positive % 2 == 1
        and parity.second_paired_positive % 2 == 1
        and parity.germ_local_only,
    )

    closures = even_closure_certificate(primary, mutation)
    checks.check(
        "G-even-subclass-closures",
        "inside the 16-dimensional B^2=-I reduction, skew/normal, slice-circulant, and anti-diagonal families are empty",
        closures.ambient_rank == 48
        and closures.ambient_dimension == 16
        and closures.real_basis
        and closures.structured_dimensions == closures.expected_dimensions,
    )

    mixture = mixture_certificate(primary, mutation)
    checks.check(
        "H-mixture-nonpinning",
        "M tensor S1 is A*, while the K=I circulant mixture is pinned by neither grading sign",
        mixture.astar_identification
        and mixture.ac_circulant
        and mixture.ac_reality
        and mixture.ac_identity_gram
        and mixture.gram_linearity
        and mixture.ac_even
        and mixture.astar_odd
        and mixture.difference_identity
        and mixture.sum_identity
        and mixture.difference_entry == mixture.expected_difference_entry
        and mixture.sum_entry == 2
        and mixture.neither_grading_sign,
    )

    scope = scope_certificate(mutation)
    checks.check(
        "I-scope",
        "the note preserves the momentum frontier, direct sum, N1--N8, W1, N5, ADM, gravity, audit, and TOE walls",
        all(scope.values()),
    )

    print(
        f"EXACT_WITNESSES: file det(c=5/13)={primary.determinant}; "
        f"tau witness det={refutation.witness_determinant}; mixture[0,0]={mixture.difference_entry}"
    )
    print(
        f"AXIOM_AUTHORITY: origin/main={authority['main']} axiom={CURRENT_AXIOM_BLOB} "
        f"registry={CURRENT_REGISTRY_BLOB}; Block110 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: exact momentum-projector, dimension-additivity, involution, determinant, inertia, parity, emptiness, and grading-split identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: the self-conjugate k=0 and k=2 branches and the conjugate k=1,3 pair factorize exactly and assemble blockwise"
    )
    print(
        "per_block: all eight sign assemblies and the determinant-changing k=0 branch witness are checked exactly, while the paired-sector parity decision remains global"
    )
    print(
        "lattice_wide: checked and not executed — the global paired-sector parity decision, mixed circulant-plus-A-star dressing variety, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the momentum-factorized positivity frontier is one parity decision away — no fixed determinant or index obstruction survives on the circulant involution class, whose best displayed inertias are (15,1,0) and (14,2,0)"
    )
    print(
        "DECISION_CUT: advance the global paired-sector parity decision and the mixed variety; reject fixed-parity readings of the near-miss chart"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
