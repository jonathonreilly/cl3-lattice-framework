#!/usr/bin/env python3
"""Block 115: exact transfer-spectrum and selection-gap certificate.

The committed Block 114 positive dressed-reflection witness is reconstructed
from its literal QQ(i) pins.  Its positive-span Gram is re-certified positive
definite, then resolved into exact two-slice transfer pencils at every spatial
momentum.  The action commutant is cut inside the exact reflection-real,
Gram-Hermitian joint space to test whether the action selects the witness.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path
import subprocess
import time

import sympy as sp
from sympy.polys.matrices import DomainMatrix

import admissibility_dirac_kahler_positive_dressed_reflection_2026_08_15 as prior


base = prior.base
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_GAP_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVE_DRESSED_REFLECTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_positive_dressed_reflection_"
    "2026_08_15.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_positive_dressed_"
    "reflection_2026_08_15.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_GAP_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_POSITIVE_DRESSED_REFLECTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_positive_dressed_reflection_2026_08_15.py",
    "logs/runner-cache/admissibility_dirac_kahler_positive_dressed_reflection_2026_08_15.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "4e566b14a6352a9a62590252a9755c7a103c1b9e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block114-positive-dressed-reflection-20260815"
)
PARENT_COMMIT = "75026e71cfbd44ed665ddc41c22ebaa722720ea9"
PARENT_NOTE_BLOB = "bcd81575da68286121a8ba6dc4ef9e6bddecb374"
PARENT_RUNNER_BLOB = "8570426930649d7300319bff2553b9a00bd41a28"
PARENT_CACHE_BLOB = "85081c90bd6f4e07a7f6170c1713f5d9c700a972"
ANCESTOR_113 = "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"
ANCESTOR_112 = "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"
ANCESTOR_111 = "b04e7c8747b09734711cfcd2bfab961bd12e81ad"
ANCESTOR_110 = "d6761278fca9cac617200792473a8f4da3a6cfff"
ANCESTOR_109 = "ad84cfcc857a65285389ba93b47cd7b718589be5"
ANCESTOR_108 = "8afe8dff5ccf531208238af0aaaec1f547d73874"
ANCESTOR_107 = "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"
ANCESTOR_106 = "22d6d90ec2279e5868c9c825149b2a20beea3797"
ANCESTOR_105 = "d06066c2b908aaca0779625d831dfb10620cf34d"
ANCESTOR_104 = "7fe07db6c03fad1191893c942f708c5cb9a54c43"
ANCESTOR_103 = "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"

PRIMARY_SHEAR = sp.Rational(5, 13)
SECOND_SHEAR = sp.Rational(3, 5)
IDENTITY_32 = sp.eye(32)
F2_COEFFICIENT_PIN = (
    5175261142208185330195747399956023340238344517047759,
    -6033804201790765437297938355001793292322654475638139,
    536815344990418589208178945880770658322516674278000,
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
        for number, commit in (
            (113, ANCESTOR_113),
            (112, ANCESTOR_112),
            (111, ANCESTOR_111),
            (110, ANCESTOR_110),
            (109, ANCESTOR_109),
            (108, ANCESTOR_108),
            (107, ANCESTOR_107),
            (106, ANCESTOR_106),
            (105, ANCESTOR_105),
            (104, ANCESTOR_104),
            (103, ANCESTOR_103),
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


def canonical(value: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.expand(value))


def normalized(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.applyfunc(sp.expand)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        canonical(entry) == 0 for entry in left - right
    )


def exact_rank(matrix: sp.Matrix) -> int:
    domain_matrix = DomainMatrix.from_Matrix(normalized(matrix), fmt="sparse")
    return len(domain_matrix.rref(method="GJ")[1])


def positive_leading_minors(
    matrix: sp.Matrix,
) -> tuple[tuple[sp.Expr, ...], tuple[int, ...]]:
    minors = prior.bareiss_leading_minors(matrix)
    signs = tuple(
        prior.qqi_sign(sp.QQ_I.from_sympy(canonical(value))) for value in minors
    )
    return minors, signs


def gram_momentum_blocks(matrix: sp.Matrix) -> tuple[sp.Matrix, ...]:
    """Invert Block 114's spatial Fourier convention on a 16-by-16 Gram.

    Rows and columns are ordered as four positive time slices times four
    spatial sites.  Block k is therefore 4-by-4 and retains only slice labels.
    """
    if matrix.shape != (16, 16):
        raise ValueError("a 16-by-16 positive-span Gram is required")
    return tuple(
        sp.Matrix(
            4,
            4,
            lambda source_slice, target_slice: canonical(
                sum(
                    I ** (-momentum * displacement)
                    * matrix[4 * source_slice, 4 * target_slice + displacement]
                    for displacement in range(4)
                )
            ),
        )
        for momentum in range(4)
    )


def assemble_gram_from_momentum(blocks: tuple[sp.Matrix, ...]) -> sp.Matrix:
    if len(blocks) != 4 or any(block.shape != (4, 4) for block in blocks):
        raise ValueError("four 4-by-4 Gram momentum blocks are required")
    return sp.Matrix(
        16,
        16,
        lambda row, column: canonical(
            sum(
                I ** (momentum * ((column % 4) - (row % 4)))
                * blocks[momentum][row // 4, column // 4]
                for momentum in range(4)
            )
            / 4
        ),
    )


def hermitian_pd_two_by_two(matrix: sp.Matrix) -> bool:
    return (
        matrix.shape == (2, 2)
        and matrix_equal(matrix, matrix.H)
        and canonical(matrix[0, 0]) > 0
        and canonical(matrix.det(method="domain-ge")) > 0
    )


def primitive_transfer_factor(
    source: sp.Matrix,
    shifted: sp.Matrix,
    variable: sp.Symbol,
) -> sp.Poly:
    pencil = variable * source - shifted
    expression = sp.expand(
        pencil[0, 0] * pencil[1, 1] - pencil[0, 1] * pencil[1, 0]
    )
    rational_coefficients: list[sp.Expr] = []
    for coefficient in sp.Poly(expression, variable).all_coeffs():
        real, imaginary = sp.expand(coefficient).as_real_imag()
        if imaginary != 0:
            raise ArithmeticError("transfer pencil coefficient is not rational")
        rational_coefficients.append(real)
    rational = sp.Poly.from_list(
        rational_coefficients,
        gens=variable,
        domain=sp.QQ,
    )
    _, integral = rational.clear_denoms(convert=True)
    primitive = integral.primitive()[1]
    return -primitive if primitive.LC() < 0 else primitive


@dataclass(frozen=True)
class TransferData:
    blocks: tuple[sp.Matrix, ...]
    sources: tuple[sp.Matrix, ...]
    shifted: tuple[sp.Matrix, ...]
    factors: tuple[sp.Poly, ...]
    discriminants: tuple[sp.Expr, ...]
    coefficient_certificates: tuple[bool, ...]
    values_at_one: tuple[sp.Expr, ...]
    splits: tuple[tuple[int, int], ...]


def transfer_certificate(gram: sp.Matrix) -> TransferData:
    variable = sp.symbols("lambda", real=True)
    blocks = gram_momentum_blocks(gram)
    sources = tuple(
        block.extract((0, 1), (0, 1)) for block in blocks
    )
    shifted = tuple(
        block.extract((1, 2), (1, 2)) for block in blocks
    )
    factors = tuple(
        primitive_transfer_factor(source, target, variable)
        for source, target in zip(sources, shifted)
    )
    discriminants = []
    coefficient_certificates = []
    values_at_one = []
    splits = []
    for factor in factors:
        coefficients = factor.all_coeffs()
        if len(coefficients) != 3:
            discriminants.append(sp.S.Zero)
            coefficient_certificates.append(False)
            values_at_one.append(factor.eval(1))
            splits.append((0, 0))
            continue
        a, b, c = coefficients
        discriminant = sp.expand(b * b - 4 * a * c)
        value_at_one = factor.eval(1)
        coefficient_certificate = bool(
            factor.degree() == 2
            and a > 0
            and b < 0
            and c > 0
            and discriminant > 0
        )
        discriminants.append(discriminant)
        coefficient_certificates.append(coefficient_certificate)
        values_at_one.append(value_at_one)
        # With a>0, b<0, c>0 and Delta>0, both roots are real positive.
        # A negative value at lambda=1 then puts exactly one root on each side.
        splits.append(
            (1, 1) if coefficient_certificate and value_at_one < 0 else (0, 0)
        )
    return TransferData(
        blocks,
        sources,
        shifted,
        factors,
        tuple(discriminants),
        tuple(coefficient_certificates),
        tuple(values_at_one),
        tuple(splits),
    )


def polynomial_digest(poly: sp.Poly) -> str:
    payload = ",".join(str(value) for value in poly.all_coeffs())
    return hashlib.sha256(payload.encode()).hexdigest()[:16]


def action_for_fixture(fixture) -> sp.Matrix:
    action = normalized(fixture.propagator.inv(method="DM"))
    if not matrix_equal(action * fixture.propagator, IDENTITY_32):
        raise ArithmeticError("exact action inverse reconstruction failed")
    return action


def commutator_rank(operator: sp.Matrix, action: sp.Matrix) -> int:
    return exact_rank(operator * action - action * operator)


def spatial_half_shift() -> sp.Matrix:
    shift = sp.Matrix(
        base.LX,
        base.LX,
        lambda row, column: int(row == (column + 1) % base.LX),
    )
    return sp.kronecker_product(sp.eye(base.SIZE // base.LX), shift**2)


def rref_nullspace(matrix: sp.Matrix) -> tuple[sp.Matrix, int]:
    domain_matrix = DomainMatrix.from_Matrix(matrix, fmt="sparse").convert_to(sp.QQ)
    reduced, pivots = domain_matrix.rref(method="GJ")
    reduced_matrix = reduced.to_Matrix()
    pivot_rows = {pivot: row for row, pivot in enumerate(pivots)}
    free_columns = tuple(
        column for column in range(matrix.cols) if column not in pivot_rows
    )
    nullspace = sp.Matrix(
        len(free_columns),
        matrix.cols,
        lambda row, column: (
            sp.S.One
            if column == free_columns[row]
            else (
                -reduced_matrix[pivot_rows[column], free_columns[row]]
                if column in pivot_rows
                else sp.S.Zero
            )
        ),
    )
    return nullspace, len(pivots)


@dataclass(frozen=True)
class CommutantData:
    ambient_dimension: int
    hermiticity_rank: int
    joint_dimension: int
    commutator_rank: int
    commutant_dimension: int
    combined_rank: int
    nullspace_residual_zero: bool


def joint_commutant_certificate(fixture, action: sp.Matrix) -> CommutantData:
    reality_rows, reality_transform = base.reality_system()
    linear = base.global_linear_certificate(fixture, reality_transform)
    joint_system = linear.hermiticity * reality_transform
    nullspace, hermiticity_rank = rref_nullspace(joint_system)
    nullspace_residual_zero = matrix_equal(
        joint_system * nullspace.T,
        sp.zeros(joint_system.rows, nullspace.rows),
    )
    ambient_coordinates = reality_transform * nullspace.T

    entries: dict[tuple[int, int], sp.Expr] = {}
    square_size = base.SIZE * base.SIZE
    for column in range(ambient_coordinates.cols):
        candidate = base.coordinates_to_matrix(ambient_coordinates[:, column])
        commutator = normalized(candidate * action - action * candidate)
        for row, value in enumerate(commutator):
            if value == 0:
                continue
            real, imaginary = value.as_real_imag()
            if real != 0:
                entries[(row, column)] = real
            if imaginary != 0:
                entries[(square_size + row, column)] = imaginary
    commutator_system = sp.MutableSparseMatrix(
        2 * square_size,
        ambient_coordinates.cols,
        entries,
    )
    restricted_rank = exact_rank(commutator_system)
    joint_dimension = nullspace.rows
    return CommutantData(
        reality_transform.cols,
        hermiticity_rank,
        joint_dimension,
        restricted_rank,
        joint_dimension - restricted_rank,
        hermiticity_rank + restricted_rank,
        bool(
            reality_rows.shape == (512, 512)
            and reality_transform.shape == (512, 256)
            and linear.hermiticity.shape == (256, 512)
            and linear.hermiticity_rank_on_reality == hermiticity_rank
            and linear.joint_rank == 256 + hermiticity_rank
            and linear.dimension == joint_dimension
            and nullspace_residual_zero
        ),
    )


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


SCOPE_KEYS = (
    "hilbert_space",
    "noncontractive",
    "four_four",
    "momentum_uniform",
    "commutant_zero",
    "rank_twenty_eight",
    "selection_gap",
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
        "hilbert_space": "hilbert space" in note,
        "noncontractive": (
            "positive but not contractive" in note
            or "uniformly non-contractive" in note
        ),
        "four_four": "(4, 4)" in note or "four below and four above" in note,
        "momentum_uniform": (
            "momentum-aligned" in note or "momentum-uniform" in note
        ),
        "commutant_zero": (
            "commutant" in note
            and ("dimension zero" in note or "exactly zero" in note)
        ),
        "rank_twenty_eight": (
            "rank 28" in note or "rank twenty-eight" in note
        ),
        "selection_gap": "selection gap" in note,
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
    if mutation == "claim_os_package_assembled":
        result["os_boundary"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    return result


MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_gram_pd",
    "break_window_hermiticity",
    "break_quadratic_certificate",
    "claim_contractive",
    "break_f2_pin",
    "mismatch_second_fixture",
    "claim_commutant_nonzero",
    "break_commutator_rank",
    "claim_witness_action_diagonal",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_os_package_assembled",
    "claim_axiom_amendment",
    "claim_toe_progress",
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
        "Block 114 parent note/runner/cache and ancestors 113--103 are exact content-bound authorities",
        AUDIT_TIMEOUT_SEC == 600
        and len(AUDIT_INPUT_PATHS) == 6
        and AUDIT_INPUT_PATHS[0]
        == "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_GAP_BOUNDED_THEOREM_NOTE_2026-08-15.md"
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(authority[f"ancestor_{number}"] for number in range(103, 114))
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    primary_fixture = base.fixture_data(PRIMARY_SHEAR)
    primary = prior.pinned_witness(PRIMARY_SHEAR)
    primary_gram = prior.left_dressed_gram(primary.operator, primary_fixture)
    tested_gram = primary_gram.copy()
    if mutation == "break_gram_pd":
        tested_gram[0, 0] = -tested_gram[0, 0]
    primary_minors, tested_minor_signs = positive_leading_minors(tested_gram)
    checks.check(
        "B-hilbert-space",
        "the Block 114 K+ is exactly Hermitian with sixteen positive leading minors, so its positive-span Hilbert space exists",
        primary.operator.shape == (32, 32)
        and primary_gram.shape == (16, 16)
        and matrix_equal(primary_gram, primary_gram.H)
        and matrix_equal(
            primary_gram,
            base.dressed_gram(primary.operator, primary_fixture),
        )
        and len(primary_minors) == 16
        and all(sign > 0 for sign in tested_minor_signs),
    )

    primary_transfer = transfer_certificate(primary_gram)
    tested_sources = list(primary_transfer.sources)
    if mutation == "break_window_hermiticity":
        broken_source = tested_sources[0].copy()
        broken_source[0, 1] += 1
        tested_sources[0] = broken_source
    checks.check(
        "C-transfer-windows",
        "the 16x16 K+ is spatial-Fourier resolved into four 4x4 K_k indexed by slice; source=K_k[{0,1},{0,1}] and shifted=K_k[{1,2},{1,2}] are Hermitian-PD 2x2 windows for every k",
        matrix_equal(
            assemble_gram_from_momentum(primary_transfer.blocks),
            primary_gram,
        )
        and all(matrix_equal(block, block.H) for block in primary_transfer.blocks)
        and all(hermitian_pd_two_by_two(source) for source in tested_sources)
        and all(
            hermitian_pd_two_by_two(shifted)
            for shifted in primary_transfer.shifted
        ),
    )

    tested_coefficients = list(primary_transfer.coefficient_certificates)
    if mutation == "break_quadratic_certificate":
        tested_coefficients[0] = False
    tested_f2 = tuple(primary_transfer.factors[2].all_coeffs())
    if mutation == "break_f2_pin":
        tested_f2 = (tested_f2[0] + 1,) + tested_f2[1:]
    claimed_contractive = mutation == "claim_contractive"
    checks.check(
        "D-transfer-spectrum",
        "all four primitive f_k have a>0,b<0,c>0,disc>0 and f_k(1)<0; the eight positive real roots split momentum-uniformly as [(1,1)x4], hence K+ transfer is positive but uniformly non-contractive",
        len(primary_transfer.factors) == 4
        and all(factor.degree() == 2 for factor in primary_transfer.factors)
        and all(tested_coefficients)
        and all(discriminant > 0 for discriminant in primary_transfer.discriminants)
        and all(value < 0 for value in primary_transfer.values_at_one)
        and primary_transfer.splits == ((1, 1),) * 4
        and sum(split[0] for split in primary_transfer.splits) == 4
        and sum(split[1] for split in primary_transfer.splits) == 4
        and not claimed_contractive
        and tuple(primary_transfer.factors[2].all_coeffs())
        == F2_COEFFICIENT_PIN
        and tested_f2 == F2_COEFFICIENT_PIN,
    )

    second_fixture = base.fixture_data(SECOND_SHEAR)
    second = prior.pinned_witness(SECOND_SHEAR)
    second_gram = prior.left_dressed_gram(second.operator, second_fixture)
    second_transfer = transfer_certificate(second_gram)
    expected_second_splits = (
        ((1, 1), (1, 1), (1, 1), (2, 0))
        if mutation == "mismatch_second_fixture"
        else ((1, 1),) * 4
    )
    checks.check(
        "E-second-fixture",
        "at c=3/5 all exact Hermitian-PD windows again give real positive quadratic roots, four f_k(1)<0, and the same momentum-uniform (4,4) split",
        matrix_equal(second_gram, second_gram.H)
        and all(
            hermitian_pd_two_by_two(source)
            for source in second_transfer.sources
        )
        and all(
            hermitian_pd_two_by_two(shifted)
            for shifted in second_transfer.shifted
        )
        and all(second_transfer.coefficient_certificates)
        and all(value < 0 for value in second_transfer.values_at_one)
        and second_transfer.splits == expected_second_splits
        and sum(split[0] for split in second_transfer.splits) == 4
        and sum(split[1] for split in second_transfer.splits) == 4,
    )

    primary_action = action_for_fixture(primary_fixture)
    second_action = action_for_fixture(second_fixture)
    commutant = joint_commutant_certificate(primary_fixture, primary_action)
    tested_commutant_dimension = commutant.commutant_dimension
    if mutation == "claim_commutant_nonzero":
        tested_commutant_dimension = 1
    checks.check(
        "F-commutant-zero",
        "the commutator has rank 132 on the 132-dimensional joint space, leaving dimension zero; equivalently reality+Hermiticity+commutation has rank 256/256",
        commutant.ambient_dimension == 256
        and commutant.hermiticity_rank == 124
        and commutant.joint_dimension == 132
        and commutant.commutator_rank == 132
        and tested_commutant_dimension == 0
        and commutant.combined_rank == 256
        and commutant.nullspace_residual_zero,
    )

    primary_commutator_rank = commutator_rank(primary.operator, primary_action)
    second_commutator_rank = commutator_rank(second.operator, second_action)
    tested_primary_commutator_rank = primary_commutator_rank
    if mutation == "break_commutator_rank":
        tested_primary_commutator_rank = 27
    claimed_action_diagonal = mutation == "claim_witness_action_diagonal"
    natural = spatial_half_shift()
    natural_gram = prior.left_dressed_gram(natural, primary_fixture)
    natural_residual_rank = exact_rank(natural_gram - natural_gram.H)
    checks.check(
        "G-selection-gap",
        "rank([A+,Q])=28 at both fixtures, while I_slices tensor X^2 commutes with Q but has Gram-Hermiticity residual rank 16: the natural candidates fail complementarily",
        tested_primary_commutator_rank == 28
        and second_commutator_rank == 28
        and not claimed_action_diagonal
        and matrix_equal(natural * natural, IDENTITY_32)
        and commutator_rank(natural, primary_action) == 0
        and natural_residual_rank == 16,
    )

    scope = scope_certificate(normalized_note(), mutation)
    checks.check(
        "H-scope",
        "the note preserves the Hilbert/non-contraction/selection boundaries, N1--N8, W1, five N5 resolutions, ADM, gravity, axiom, and TOE firewalls",
        set(scope) == set(SCOPE_KEYS) and all(scope.values()),
    )

    factor_ids = tuple(polynomial_digest(factor) for factor in primary_transfer.factors)
    print(
        "PRIMARY_TRANSFER: "
        f"factor_ids={factor_ids}; f2_coefficients={tuple(primary_transfer.factors[2].all_coeffs())}; "
        f"split={primary_transfer.splits}"
    )
    print(
        "SECOND_TRANSFER: "
        f"c=3/5 split={second_transfer.splits}; all four exact f_k(1)<0"
    )
    print(
        "COMMUTANT: "
        f"joint_dim={commutant.joint_dimension}; restricted_rank={commutant.commutator_rank}; "
        f"dimension={commutant.commutant_dimension}; combined_rank={commutant.combined_rank}/256"
    )
    print(
        "SELECTION_GAP: "
        f"rank([A+,Q])=({primary_commutator_rank},{second_commutator_rank}); "
        f"rank(K_x2-K_x2^H)={natural_residual_rank}"
    )
    print(f"RUNTIME_SECONDS: {time.monotonic() - started:.3f}")
    print(
        "N5: per_element: exact window, quadratic-certificate, commutant-rank, and commutator identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: every momentum factor carries exactly one transfer root below one and one above one at both fixtures"
    )
    print(
        "per_block: the commutant cut of the joint space is exactly zero-dimensional and the positive witness has commutator rank twenty-eight"
    )
    print(
        "lattice_wide: checked and not executed — a transfer-contractive point of the positive variety, the transfer-window normalization question, the modular selection, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the positive pairing carries a Hilbert space whose one-slice transfer is positive but uniformly non-contractive, and the action's commutant selects nothing — the OS package and the selection are one shared open gate"
    )
    print(
        "DECISION_CUT: advance the transfer-contractive search on the positive variety and the modular selection; reject blockwise repairs and commutant selection"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
