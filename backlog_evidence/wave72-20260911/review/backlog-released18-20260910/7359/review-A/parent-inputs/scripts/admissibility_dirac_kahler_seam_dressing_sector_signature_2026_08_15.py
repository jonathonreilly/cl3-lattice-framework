#!/usr/bin/env python3
"""Block 110: seam-dressing sector signature and sparse even boundary.

On the exact Block 109 antiperiodic reflection torus, spatial-shift
conjugation splits the 132-dimensional joint dressing space into a
128-dimensional even sector and a four-dimensional odd sector.  Every odd
sector Gram anticommutes with the spatial shift, so its spectrum is exactly
negation-symmetric and its signature is zero.  This is a sector theorem and
a bounded sparse-even no-go, not a transporter impossibility or a solution
of the full even-sector involution variety.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess

import sympy as sp

import admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15 as prior


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_"
    "2026_08_15.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_global_dressing_involution_"
    "positivity_2026_08_15.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py",
    "logs/runner-cache/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "795e851254e689a66fa9e3fe619823835d4d8661"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block109-global-dressing-involution-positivity-20260815"
)
PARENT_COMMIT = "ad84cfcc857a65285389ba93b47cd7b718589be5"
PARENT_NOTE_BLOB = "3ed51ad603b3c4dc9a0e9eb3c98e343b49c3b9ea"
PARENT_RUNNER_BLOB = "4facf35d1f8d91fa05d4df7c6e1fdc7b8047f048"
PARENT_CACHE_BLOB = "a9e0a6e045cb34221aa1fdb876a93ab571f856ce"
ANCESTOR_108 = "8afe8dff5ccf531208238af0aaaec1f547d73874"
ANCESTOR_107 = "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"
ANCESTOR_106 = "22d6d90ec2279e5868c9c825149b2a20beea3797"
ANCESTOR_105 = "d06066c2b908aaca0779625d831dfb10620cf34d"
ANCESTOR_104 = "7fe07db6c03fad1191893c942f708c5cb9a54c43"
ANCESTOR_103 = "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"


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
        "ancestor_108": is_ancestor(ANCESTOR_108, "HEAD"),
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
EVEN_FACTORS = (0, 2, 3)
ODD_FACTORS = (1,)
ALL_SLICE_BLOCKS = tuple(
    (slice_i, slice_j) for slice_i in range(8) for slice_j in range(8)
)


def spatial_shift() -> sp.Matrix:
    factors = prior.spatial_factors()
    return (factors[2] + factors[3]) / 2


def carrier_shifts() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    cyclic = spatial_shift()
    return (
        cyclic,
        sp.kronecker_product(sp.eye(8), cyclic),
        sp.kronecker_product(sp.eye(4), cyclic),
    )


def support_embedding(
    support: tuple[tuple[int, int], ...],
    factor_indices: tuple[int, ...],
) -> sp.Matrix:
    """Embed a selected slice/factor support in the 512 real coordinates."""
    embedding = sp.zeros(512, 2 * len(support) * len(factor_indices))
    local = 0
    for slice_i, slice_j in support:
        for factor_index in factor_indices:
            for imaginary in (0, 1):
                embedding[
                    prior.parameter_index(
                        slice_i, slice_j, factor_index, imaginary
                    ),
                    local,
                ] = 1
                local += 1
    return embedding


def restricted_joint_rank(
    reality: sp.Matrix,
    hermiticity: sp.Matrix,
    embedding: sp.Matrix,
) -> int:
    restricted = (reality * embedding).col_join(hermiticity * embedding)
    return prior.exact_rank(restricted)


@dataclass(frozen=True)
class SectorCertificate:
    conjugation: tuple[bool, ...]
    even_coordinates: int
    odd_coordinates: int
    primary_even_rank: int
    second_even_rank: int
    primary_odd_rank: int
    second_odd_rank: int
    expected_even_dimension: int

    @property
    def primary_even_dimension(self) -> int:
        return self.even_coordinates - self.primary_even_rank

    @property
    def second_even_dimension(self) -> int:
        return self.even_coordinates - self.second_even_rank

    @property
    def primary_odd_dimension(self) -> int:
        return self.odd_coordinates - self.primary_odd_rank

    @property
    def second_odd_dimension(self) -> int:
        return self.odd_coordinates - self.second_odd_rank


def sector_certificate(
    reality: sp.Matrix,
    primary_hermiticity: sp.Matrix,
    second_hermiticity: sp.Matrix,
    mutation: str,
) -> SectorCertificate:
    cyclic = spatial_shift()
    factors = prior.spatial_factors()
    actual_signs = (1, -1, 1, 1)
    expected_signs = (
        (1, -1, 1, -1)
        if mutation == "break_conjugation_table"
        else actual_signs
    )
    conjugation = tuple(
        prior.matrix_equal(
            cyclic * factor * cyclic.inv(),
            sign * factor,
        )
        for factor, sign in zip(factors, expected_signs)
    )

    even_embedding = support_embedding(ALL_SLICE_BLOCKS, EVEN_FACTORS)
    odd_embedding = support_embedding(ALL_SLICE_BLOCKS, ODD_FACTORS)
    return SectorCertificate(
        conjugation,
        even_embedding.cols,
        odd_embedding.cols,
        restricted_joint_rank(reality, primary_hermiticity, even_embedding),
        restricted_joint_rank(reality, second_hermiticity, even_embedding),
        restricted_joint_rank(reality, primary_hermiticity, odd_embedding),
        restricted_joint_rank(reality, second_hermiticity, odd_embedding),
        127 if mutation == "claim_wrong_even_dim" else 128,
    )


def selector(indices: tuple[int, ...]) -> sp.Matrix:
    result = sp.zeros(prior.SIZE, len(indices))
    for column, index in enumerate(indices):
        result[index, column] = 1
    return result


def matrix_with_blocks(
    entries: tuple[tuple[int, int, int, sp.Rational], ...]
) -> sp.Matrix:
    factors = prior.spatial_factors()
    result = sp.zeros(prior.SIZE, prior.SIZE)
    for slice_i, slice_j, factor_index, coefficient in entries:
        result[
            4 * slice_i : 4 * (slice_i + 1),
            4 * slice_j : 4 * (slice_j + 1),
        ] += coefficient * factors[factor_index]
    return result


def pinned_rational_test_elements() -> tuple[sp.Matrix, ...]:
    return (
        matrix_with_blocks(((0, 3, 0, sp.Rational(2, 3)),)),
        matrix_with_blocks(((5, 2, 1, sp.Rational(-7, 5)),)),
        matrix_with_blocks(
            (
                (1, 6, 2, sp.Rational(3, 4)),
                (7, 0, 3, sp.Rational(-2, 7)),
            )
        ),
    )


@dataclass(frozen=True)
class SignatureCertificate:
    carrier_commutation: bool
    reflection_commutation: bool
    index_preservation: bool
    rational_covariance_tests: tuple[bool, ...]
    real_linearity: bool
    odd_action: bool
    astar_is_odd: bool
    endpoint_identity: bool
    odd_charpoly_coefficients_zero: bool
    endpoint_inertia: tuple[int, int, int]
    expected_signature: int


def signature_certificate(
    primary: prior.Fixture,
    second: prior.Fixture,
    mutation: str,
) -> SignatureCertificate:
    cyclic, carrier_shift, positive_shift = carrier_shifts()
    fixtures = (primary, second)
    carrier_commutation = all(
        prior.matrix_equal(
            carrier_shift * fixture.propagator,
            fixture.propagator * carrier_shift,
        )
        for fixture in fixtures
    )
    reflection_commutation = all(
        prior.matrix_equal(
            carrier_shift * fixture.reflection,
            fixture.reflection * carrier_shift,
        )
        for fixture in fixtures
    )
    index_preservation = all(
        prior.matrix_equal(
            carrier_shift * selector(fixture.positive),
            selector(fixture.positive) * positive_shift,
        )
        and prior.matrix_equal(
            carrier_shift * selector(fixture.reflected),
            selector(fixture.reflected) * positive_shift,
        )
        for fixture in fixtures
    )

    tests = pinned_rational_test_elements()
    covariance_tests = tuple(
        prior.matrix_equal(
            positive_shift
            * prior.dressed_gram(test, primary)
            * positive_shift.inv(),
            prior.dressed_gram(
                carrier_shift * test * carrier_shift.inv(), primary
            ),
        )
        for test in tests
    )
    real_linearity = (
        prior.matrix_equal(
            prior.dressed_gram(tests[0] + tests[1], primary),
            prior.dressed_gram(tests[0], primary)
            + prior.dressed_gram(tests[1], primary),
        )
        and prior.matrix_equal(
            prior.dressed_gram(sp.Rational(11, 13) * tests[2], primary),
            sp.Rational(11, 13) * prior.dressed_gram(tests[2], primary),
        )
        and prior.matrix_equal(
            prior.dressed_gram(sp.zeros(prior.SIZE), primary),
            sp.zeros(16),
        )
    )
    if mutation == "break_linearity_identity":
        real_linearity = False

    spatial_parity = prior.spatial_factors()[1]
    odd_action = prior.matrix_equal(
        cyclic * spatial_parity * cyclic.inv(), -spatial_parity
    )
    astar = prior.global_candidate()
    astar_is_odd = prior.matrix_equal(
        carrier_shift * astar * carrier_shift.inv(), -astar
    )
    endpoint_gram = prior.dressed_gram(astar, primary)
    endpoint_identity = prior.matrix_equal(
        positive_shift * endpoint_gram * positive_shift.inv(), -endpoint_gram
    )
    polynomial = endpoint_gram.charpoly().as_poly()
    odd_coefficients_zero = all(
        polynomial.nth(degree) == 0 for degree in range(1, 17, 2)
    )
    leading = prior.leading_minors(endpoint_gram)
    endpoint_inertia = prior.inertia_from_nonzero_leading_minors(leading)
    return SignatureCertificate(
        carrier_commutation,
        reflection_commutation,
        index_preservation,
        covariance_tests,
        real_linearity,
        odd_action,
        astar_is_odd,
        endpoint_identity,
        odd_coefficients_zero,
        endpoint_inertia,
        16 if mutation == "claim_odd_sector_positive" else 0,
    )


@dataclass(frozen=True)
class AnticommutantCertificate:
    equation_rank: int
    dimension: int
    expected_dimension: int
    expected_kernel: bool
    shift_basis_identification: bool
    unitary: bool
    second_power_not_identity: bool
    fourth_power_identity: bool
    parity_mechanism: bool


def anticommutant_certificate(
    endpoint_gram: sp.Matrix,
    mutation: str,
) -> AnticommutantCertificate:
    cyclic, _, positive_shift = carrier_shifts()
    basis: list[sp.Matrix] = []
    for slice_index in range(4):
        for power in range(4):
            item = sp.zeros(16, 16)
            item[
                4 * slice_index : 4 * (slice_index + 1),
                4 * slice_index : 4 * (slice_index + 1),
            ] = cyclic**power
            basis.append(item)

    columns = [
        sp.Matrix(list(item * endpoint_gram + endpoint_gram * item))
        for item in basis
    ]
    equations = sp.Matrix.hstack(*columns)
    equation_rank = prior.exact_rank(equations)
    odd_shift_coordinates = sp.zeros(16, 2)
    for slice_index in range(4):
        odd_shift_coordinates[4 * slice_index + 1, 0] = 1
        odd_shift_coordinates[4 * slice_index + 3, 1] = 1
    expected_kernel = (
        prior.matrix_equal(
            equations * odd_shift_coordinates,
            sp.zeros(equations.rows, 2),
        )
        and prior.exact_rank(odd_shift_coordinates) == 2
    )
    first_shift = sum(
        (
            odd_shift_coordinates[index, 0] * item
            for index, item in enumerate(basis)
        ),
        sp.zeros(16),
    )
    third_shift = sum(
        (
            odd_shift_coordinates[index, 1] * item
            for index, item in enumerate(basis)
        ),
        sp.zeros(16),
    )
    claimed_second_power = (
        prior.matrix_equal(positive_shift**2, sp.eye(16))
        if mutation == "break_shift_order"
        else not prior.matrix_equal(positive_shift**2, sp.eye(16))
    )
    spatial_parity = prior.spatial_factors()[1]
    return AnticommutantCertificate(
        equation_rank,
        16 - equation_rank,
        3 if mutation == "claim_anticommutant_dim_wrong" else 2,
        expected_kernel,
        prior.matrix_equal(first_shift, positive_shift)
        and prior.matrix_equal(third_shift, positive_shift**3),
        prior.matrix_equal(positive_shift.H * positive_shift, sp.eye(16)),
        claimed_second_power,
        prior.matrix_equal(positive_shift**4, sp.eye(16)),
        prior.matrix_equal(
            spatial_parity * cyclic, -cyclic * spatial_parity
        ),
    )


SPARSE_SUPPORTS = (
    ("F-1", ((1, 3), (6, 4))),
    ("F-2", ((1, 3), (6, 4), (0, 3), (7, 4))),
    ("F+1", ((3, 0), (4, 7))),
    ("F+2", ((3, 0), (4, 7), (1, 2), (6, 5))),
)
PERMUTATION_32107654 = (3, 2, 1, 0, 7, 6, 5, 4)


@dataclass(frozen=True)
class SparseFamilyResult:
    name: str
    coordinates: int
    primary_rank: int
    second_rank: int


@dataclass(frozen=True)
class SparseCertificate:
    families: tuple[SparseFamilyResult, ...]
    expected_empty: bool
    permutation_coordinates: int
    primary_permutation_rank: int
    second_permutation_rank: int
    primary_groebner_basis: tuple[sp.Expr, ...]
    second_groebner_basis: tuple[sp.Expr, ...]
    expected_groebner_basis: tuple[sp.Expr, ...]


def one_parameter_involution_groebner(
    joint: sp.Matrix,
    embedding: sp.Matrix,
) -> tuple[sp.Expr, ...]:
    kernel = joint.nullspace()
    if len(kernel) != 1:
        return ()
    generator_coordinates = kernel[0]
    if not prior.matrix_equal(
        joint * generator_coordinates, sp.zeros(joint.rows, 1)
    ):
        return ()
    generator = prior.coordinates_to_matrix(embedding * generator_coordinates)
    lam = sp.Symbol("lambda", real=True)
    equations = tuple(
        sp.expand(entry)
        for entry in (lam * generator) ** 2 - sp.eye(prior.SIZE)
        if sp.expand(entry) != 0
    )
    groebner = sp.groebner(
        equations,
        lam,
        extension=I,
        order="lex",
    )
    return tuple(polynomial.monic().as_expr() for polynomial in groebner.polys)


def sparse_certificate(
    reality: sp.Matrix,
    primary_hermiticity: sp.Matrix,
    second_hermiticity: sp.Matrix,
    mutation: str,
) -> SparseCertificate:
    families: list[SparseFamilyResult] = []
    for name, support in SPARSE_SUPPORTS:
        embedding = support_embedding(support, EVEN_FACTORS)
        families.append(
            SparseFamilyResult(
                name,
                embedding.cols,
                restricted_joint_rank(
                    reality, primary_hermiticity, embedding
                ),
                restricted_joint_rank(
                    reality, second_hermiticity, embedding
                ),
            )
        )

    permutation_support = tuple(enumerate(PERMUTATION_32107654))
    permutation_embedding = support_embedding(
        permutation_support, EVEN_FACTORS
    )
    primary_joint = (reality * permutation_embedding).col_join(
        primary_hermiticity * permutation_embedding
    )
    second_joint = (reality * permutation_embedding).col_join(
        second_hermiticity * permutation_embedding
    )
    expected_groebner = (
        (sp.Symbol("lambda", real=True) ** 2 - 1,)
        if mutation == "break_groebner_one"
        else (sp.Integer(1),)
    )
    return SparseCertificate(
        tuple(families),
        mutation != "claim_sparse_family_solvable",
        permutation_embedding.cols,
        prior.exact_rank(primary_joint),
        prior.exact_rank(second_joint),
        one_parameter_involution_groebner(
            primary_joint, permutation_embedding
        ),
        one_parameter_involution_groebner(
            second_joint, permutation_embedding
        ),
        expected_groebner,
    )


def positive_fiber_representative(fixture: prior.Fixture) -> sp.Matrix:
    factors = prior.spatial_factors()
    positive_half = sp.zeros(prior.SIZE, prior.SIZE)
    offset = 0
    for output_slice in range(4):
        slice_i = 4 + output_slice
        for slice_j in range(8):
            block = sp.zeros(4, 4)
            for factor in factors:
                block += prior.POSITIVE_FIBER_REAL_COEFFICIENTS[offset] * factor
                offset += 1
            positive_half[
                4 * slice_i : 4 * (slice_i + 1),
                4 * slice_j : 4 * (slice_j + 1),
            ] = block
    if offset != len(prior.POSITIVE_FIBER_REAL_COEFFICIENTS):
        raise AssertionError("pinned positive-fiber coordinate count changed")
    return (
        positive_half
        + fixture.reflection
        * positive_half.conjugate()
        * fixture.reflection
    )


@dataclass(frozen=True)
class InheritanceCertificate:
    fiber_reality: bool
    fiber_gram_identity: bool
    off_sector_fixed: bool
    off_sector_negated: bool
    expected_off_sector_negated: bool
    identity_reality: bool
    identity_excluded: bool
    identity_defect: sp.Expr


def inheritance_certificate(
    fixture: prior.Fixture,
    mutation: str,
) -> InheritanceCertificate:
    _, _, positive_shift = carrier_shifts()
    representative = positive_fiber_representative(fixture)
    gram = prior.dressed_gram(representative, fixture)
    shifted_gram = positive_shift * gram * positive_shift.inv()
    undressed = prior.undressed_certificate(fixture, "")
    return InheritanceCertificate(
        prior.matrix_equal(
            fixture.reflection
            * representative.conjugate()
            * fixture.reflection,
            representative,
        ),
        prior.matrix_equal(gram, sp.eye(16)),
        prior.matrix_equal(shifted_gram, gram),
        prior.matrix_equal(shifted_gram, -gram),
        mutation == "claim_obstruction_generic",
        bool(undressed["reality"]),
        bool(undressed["excluded"]),
        sp.factor(undressed["defect"]),
    )


def is_momentum_diagonal(matrix: sp.Matrix, slice_count: int) -> bool:
    return all(
        sp.expand(matrix[4 * row_slice + row_momentum,
                         4 * column_slice + column_momentum]) == 0
        for row_slice in range(slice_count)
        for column_slice in range(slice_count)
        for row_momentum in range(4)
        for column_momentum in range(4)
        if row_momentum != column_momentum
    )


@dataclass(frozen=True)
class MomentumCertificate:
    dft_unitary: bool
    eigenvalues: tuple[tuple[sp.Expr, ...], ...]
    expected_eigenvalues: tuple[tuple[sp.Expr, ...], ...]
    even_test_diagonal: bool
    propagators_diagonal: bool
    reflections_diagonal: bool
    four_momentum_blocks: bool


def momentum_certificate(
    primary: prior.Fixture,
    second: prior.Fixture,
    mutation: str,
) -> MomentumCertificate:
    dft = sp.Matrix(
        4,
        4,
        lambda space, momentum: I ** (-space * momentum) / 2,
    )
    factors = prior.spatial_factors()
    even_structures = tuple(factors[index] for index in EVEN_FACTORS)
    transformed_structures = tuple(
        sp.simplify(dft.H * structure * dft)
        for structure in even_structures
    )
    eigenvalues = tuple(
        tuple(sp.simplify(value) for value in transformed.diagonal())
        for transformed in transformed_structures
    )
    expected_s3 = (
        (sp.Integer(0), -2 * I, sp.Integer(0), 2 * I)
        if mutation == "break_dft_eigenvalues"
        else (sp.Integer(0), 2 * I, sp.Integer(0), -2 * I)
    )
    expected_eigenvalues = (
        tuple(sp.Integer(1) for _ in range(4)),
        (sp.Integer(2), sp.Integer(0), sp.Integer(-2), sp.Integer(0)),
        expected_s3,
    )

    slice_tests = (
        sp.Matrix(8, 8, lambda row, column: sp.Rational(row + 2 * column + 1, 17)),
        sp.Matrix(8, 8, lambda row, column: sp.Rational(3 * row - column + 2, 19)),
        sp.Matrix(8, 8, lambda row, column: sp.Rational(row - 4 * column - 3, 23)),
    )
    generic_even = sum(
        (
            sp.kronecker_product(slice_matrix, structure)
            for slice_matrix, structure in zip(slice_tests, even_structures)
        ),
        sp.zeros(prior.SIZE),
    )
    carrier_fourier = sp.kronecker_product(sp.eye(8), dft)
    transformed_even = sp.simplify(
        carrier_fourier.H * generic_even * carrier_fourier
    )
    fixtures = (primary, second)
    transformed_propagators = tuple(
        sp.simplify(
            carrier_fourier.H * fixture.propagator * carrier_fourier
        )
        for fixture in fixtures
    )
    transformed_reflections = tuple(
        sp.simplify(
            carrier_fourier.H * fixture.reflection * carrier_fourier
        )
        for fixture in fixtures
    )
    return MomentumCertificate(
        prior.matrix_equal(dft.H * dft, sp.eye(4)),
        eigenvalues,
        expected_eigenvalues,
        is_momentum_diagonal(transformed_even, 8),
        all(is_momentum_diagonal(matrix, 8) for matrix in transformed_propagators),
        all(is_momentum_diagonal(matrix, 8) for matrix in transformed_reflections),
        len(eigenvalues[0]) == 4,
    )


SCOPE_KEYS = (
    "sector",
    "signature_zero",
    "odd_sector",
    "even_sector",
    "negation_symmetric",
    "momentum",
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
        "sector": "sector" in note,
        "signature_zero": (
            "signature is exactly zero" in note or "signature zero" in note
        ),
        "odd_sector": "odd sector" in note,
        "even_sector": "even sector" in note,
        "negation_symmetric": "negation-symmetric" in note,
        "momentum": "momentum" in note or "fourier" in note,
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
    "break_conjugation_table",
    "claim_wrong_even_dim",
    "break_linearity_identity",
    "claim_odd_sector_positive",
    "claim_anticommutant_dim_wrong",
    "break_shift_order",
    "claim_sparse_family_solvable",
    "break_groebner_one",
    "claim_obstruction_generic",
    "break_dft_eigenvalues",
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
        "A-authority-and-Block109-parent",
        "current axioms, registries, ancestry, and the Block109 parent triple are content-bound",
        authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["ancestor_108"]
        and authority["ancestor_107"]
        and authority["ancestor_106"]
        and authority["ancestor_105"]
        and authority["ancestor_104"]
        and authority["ancestor_103"]
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    primary = prior.fixture_data(sp.Rational(5, 13))
    second = prior.fixture_data(sp.Rational(3, 5))
    reality, transform = prior.reality_system()
    primary_hermiticity = prior.global_hermiticity_matrix(primary)
    second_hermiticity = prior.global_hermiticity_matrix(second)

    sector = sector_certificate(
        reality, primary_hermiticity, second_hermiticity, mutation
    )
    checks.check(
        "B-sector-split",
        "C-conjugation splits the 132-dimensional joint space into even dimension 128 and odd dimension 4",
        all(sector.conjugation)
        and prior.matrix_equal(reality * transform, sp.zeros(512, 256))
        and prior.exact_rank(transform) == 256
        and sector.even_coordinates == 384
        and sector.odd_coordinates == 128
        and sector.primary_even_rank == sector.second_even_rank == 256
        and sector.primary_odd_rank == sector.second_odd_rank == 124
        and sector.primary_even_dimension
        == sector.second_even_dimension
        == sector.expected_even_dimension
        and sector.primary_odd_dimension
        == sector.second_odd_dimension
        == 4
        and sector.primary_even_dimension + sector.primary_odd_dimension == 132
        and sector.second_even_dimension + sector.second_odd_dimension == 132,
    )

    signature = signature_certificate(primary, second, mutation)
    checks.check(
        "C-odd-sector-signature-theorem",
        "shift covariance makes every odd-sector Gram negation-symmetric with signature exactly zero",
        signature.carrier_commutation
        and signature.reflection_commutation
        and signature.index_preservation
        and len(signature.rational_covariance_tests) == 3
        and all(signature.rational_covariance_tests)
        and signature.real_linearity
        and signature.odd_action
        and signature.astar_is_odd
        and signature.endpoint_identity
        and signature.odd_charpoly_coefficients_zero
        and signature.endpoint_inertia == (8, 8, 0)
        and signature.endpoint_inertia[0] - signature.endpoint_inertia[1]
        == signature.expected_signature,
    )

    endpoint_gram = prior.dressed_gram(prior.global_candidate(), primary)
    anticommutant = anticommutant_certificate(endpoint_gram, mutation)
    checks.check(
        "D-anticommutant-structure",
        "the 16-dimensional slice-diagonal anticommutant is exactly span{I4 tensor C,I4 tensor C^3}",
        anticommutant.equation_rank == 14
        and anticommutant.dimension == anticommutant.expected_dimension
        and anticommutant.expected_kernel
        and anticommutant.shift_basis_identification
        and anticommutant.unitary
        and anticommutant.second_power_not_identity
        and anticommutant.fourth_power_identity
        and anticommutant.parity_mechanism,
    )

    sparse = sparse_certificate(
        reality, primary_hermiticity, second_hermiticity, mutation
    )
    actual_sparse_empty = all(
        family.primary_rank == family.second_rank == family.coordinates
        for family in sparse.families
    )
    checks.check(
        "E-even-sector-sparse-emptiness",
        "F-1/F-2/F+1/F+2 are exactly empty and p=32107654 has nullity one with Groebner basis {1}",
        tuple(
            (
                family.name,
                family.coordinates,
                family.primary_rank,
                family.second_rank,
            )
            for family in sparse.families
        )
        == (
            ("F-1", 12, 12, 12),
            ("F-2", 24, 24, 24),
            ("F+1", 12, 12, 12),
            ("F+2", 24, 24, 24),
        )
        and actual_sparse_empty == sparse.expected_empty
        and sparse.permutation_coordinates == 48
        and sparse.primary_permutation_rank
        == sparse.second_permutation_rank
        == 47
        and sparse.primary_groebner_basis
        == sparse.second_groebner_basis
        == sparse.expected_groebner_basis,
    )

    inheritance = inheritance_certificate(primary, mutation)
    checks.check(
        "F-scope-inheritance",
        "the shift obstruction is odd-sector-only while K=I16 and the Block108 A=I exclusion remain exact",
        inheritance.fiber_reality
        and inheritance.fiber_gram_identity
        and inheritance.off_sector_fixed
        and inheritance.off_sector_negated
        == inheritance.expected_off_sector_negated
        and inheritance.identity_reality
        and inheritance.identity_excluded
        and inheritance.identity_defect == prior.UNDRESSED_DEFECT,
    )

    momentum = momentum_certificate(primary, second, mutation)
    checks.check(
        "G-momentum-factorization",
        "the even structures and translation-invariant fixture data split exactly into four momentum blocks",
        momentum.dft_unitary
        and momentum.eigenvalues == momentum.expected_eigenvalues
        and momentum.even_test_diagonal
        and momentum.propagators_diagonal
        and momentum.reflections_diagonal
        and momentum.four_momentum_blocks,
    )

    scope = scope_certificate(mutation)
    checks.check(
        "H-scope",
        "the note preserves the sector theorem, sparse boundary, N1--N8, W1, N5, ADM, gravity, audit, and TOE walls",
        all(scope.values()),
    )

    print(
        "EXACT_WITNESSES: even/odd ranks=256/124; anticommutant rank/dim=14/2; "
        "p=32107654 rank/nullity=47/1; Groebner={1}; inertia(A*)=(8,8,0)"
    )
    print(
        f"AXIOM_AUTHORITY: origin/main={authority['main']} axiom={CURRENT_AXIOM_BLOB} "
        f"registry={CURRENT_REGISTRY_BLOB}; Block109 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: exact grading, Gram covariance, signature, anticommutant, characteristic-polynomial, sparse-rank, and Groebner identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: both shear fixtures certify the same sector dimensions, signature theorem, sparse obstructions, and momentum factorization"
    )
    print(
        "per_block: the odd x-parity structure reverses sign while the identity and symmetric/antisymmetric shifts are preserved and Fourier diagonal"
    )
    print(
        "lattice_wide: checked and not executed — the even-sector involution variety, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: signature zero is a sector theorem — every odd-sector dressing is exactly signature-pinned, so seam positivity must come from the even sector, whose displayed sparse truncations are exactly empty"
    )
    print(
        "DECISION_CUT: advance the momentum-factorized even-sector involution variety; reject odd-sector and sparse-truncation routes"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
