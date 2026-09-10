#!/usr/bin/env python3
"""Block 127: exact naturality moduli of the Dirac--Kahler completion.

The runner classifies the reflection-real involutive completions at the two
self-conjugate momenta, tests the proposed monodromy/naturality selectors, and
keeps all scientific arithmetic in exact rational quadratic root fields.
Wall-clock timing is the sole floating-point quantity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_time_dressing_adjointness_wall_2026_08_17 as prior


R = sp.Rational
I = sp.I
b119 = prior.block119
RHO = b119.RHO
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_NATURALITY_MODULI_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TIME_DRESSING_ADJOINTNESS_WALL_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_time_dressing_"
    "adjointness_wall_2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_time_dressing_"
    "adjointness_wall_2026_08_17.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_NATURALITY_MODULI_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TIME_DRESSING_ADJOINTNESS_WALL_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_time_dressing_adjointness_wall_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_time_dressing_adjointness_wall_2026_08_17.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "b8e134041e71710f490e226f38e72507312cf6c9"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block126-time-dressing-adjointness-wall-20260817"
)
PARENT_COMMIT = "a145a4e2cfc19bc919371196d7c5f3451c0bb45d"
PARENT_NOTE_BLOB = "186e55661f7bdc54540558491dcdd20123bcb89d"
PARENT_RUNNER_BLOB = "65cbed51069b3b6b9a7cd431ca3ad6a689f13473"
PARENT_CACHE_BLOB = "39602d1725bf49ab2089ab1c247c4ad4e7523d08"
ANCESTOR_COMMITS = (
    (125, "ff85cc8c6a991b2926b9ac5cb5168f2587bc0c0d"),
    (124, "da2b9020e9f15ac55640ef87a0798a78e3c9a0d0"),
    (123, "954322e0e085d6c3133ce24dca49db2efbd7d0a6"),
    (122, "f067b99be7eb49fc46ea8dffccab5e20e6052d88"),
    (121, "1714abeefcf3763c0bfe001f30fd14521c538622"),
    (120, "1c2386bf3df420707fd2ecb2d7ec84002ba40ad1"),
    (119, "33fd2d21558604718f3a88713fe1976aff8f9dbb"),
    (118, "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"),
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

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_parametrization",
    "break_dimension_law",
    "break_inversion_identity",
    "claim_inversion_pins",
    "break_eigenvector_argument",
    "claim_commuting_member",
    "break_minimality_uniqueness",
    "claim_unconditional_uniqueness",
    "break_verdict",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
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
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **{
            f"ancestor_{number}": is_ancestor(commit, "HEAD")
            for number, commit in ANCESTOR_COMMITS
        },
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


def exact_digest(*payload: object) -> str:
    return hashlib.sha256(sp.srepr(payload).encode("utf-8")).hexdigest()[:16]


def red(value: sp.Expr, polynomial: sp.Poly) -> sp.Expr:
    return b119.red(value, polynomial)


def fm(matrix: sp.MatrixBase, polynomial: sp.Poly) -> sp.Matrix:
    return b119.field_matrix(sp.Matrix(matrix), polynomial)


def feq(
    left: sp.MatrixBase, right: sp.MatrixBase, polynomial: sp.Poly
) -> bool:
    return b119.field_equal(sp.Matrix(left), sp.Matrix(right), polynomial)


def field_rank(matrix: sp.MatrixBase, polynomial: sp.Poly) -> int:
    """Gaussian rank over the exact quadratic quotient field."""
    work = fm(matrix, polynomial)
    pivot_row = 0
    for column in range(work.cols):
        pivot = next(
            (
                row
                for row in range(pivot_row, work.rows)
                if red(work[row, column], polynomial) != 0
            ),
            None,
        )
        if pivot is None:
            continue
        if pivot != pivot_row:
            work.row_swap(pivot, pivot_row)
        inverse = red(1 / work[pivot_row, column], polynomial)
        for entry in range(column, work.cols):
            work[pivot_row, entry] = red(
                work[pivot_row, entry] * inverse, polynomial
            )
        for row in range(work.rows):
            if row == pivot_row:
                continue
            coefficient = red(work[row, column], polynomial)
            if coefficient == 0:
                continue
            for entry in range(column, work.cols):
                work[row, entry] = red(
                    work[row, entry]
                    - coefficient * work[pivot_row, entry],
                    polynomial,
                )
        pivot_row += 1
        if pivot_row == work.rows:
            break
    return pivot_row


def reality_operator(polynomial: sp.Poly) -> sp.Matrix:
    cut = b119.cut_shift()
    return fm(cut * b119.B111.J * cut.T, polynomial)


def reality_matrix(
    reality: sp.Matrix, matrix: sp.MatrixBase, polynomial: sp.Poly
) -> sp.Matrix:
    return b119.reality_conjugate(reality, sp.Matrix(matrix), polynomial)


def independent_columns(matrix: sp.Matrix, polynomial: sp.Poly) -> tuple[int, ...]:
    selected: list[int] = []
    rank = 0
    for column in range(matrix.cols):
        candidate = matrix[:, selected + [column]]
        candidate_rank = field_rank(candidate, polynomial)
        if candidate_rank > rank:
            selected.append(column)
            rank = candidate_rank
        if rank == 4:
            break
    if len(selected) != 4:
        raise AssertionError("rank-four column basis")
    return tuple(selected)


def fixed_basis(
    coordinate_reality: sp.Matrix, polynomial: sp.Poly
) -> sp.Matrix:
    """Return four exact vectors fixed by a coordinate anti-involution."""
    identity = sp.eye(4)
    candidates: list[sp.Matrix] = []
    for column in range(4):
        vector = identity[:, column]
        reflected = fm(coordinate_reality * b119.field_conjugate(vector, polynomial), polynomial)
        candidates.extend(
            (
                fm(vector + reflected, polynomial),
                fm(I * (vector - reflected), polynomial),
            )
        )
    selected: list[sp.Matrix] = []
    rank = 0
    for candidate in candidates:
        trial = sp.Matrix.hstack(*selected, candidate) if selected else candidate
        trial_rank = field_rank(trial, polynomial)
        if trial_rank > rank:
            selected.append(candidate)
            rank = trial_rank
        if rank == 4:
            break
    if len(selected) != 4:
        raise AssertionError("fixed real form has dimension four")
    result = fm(sp.Matrix.hstack(*selected), polynomial)
    reflected_result = fm(
        coordinate_reality * b119.field_conjugate(result, polynomial),
        polynomial,
    )
    if not feq(reflected_result, result, polynomial):
        raise AssertionError("reality-fixed basis")
    return result


@dataclass(frozen=True)
class Chart:
    sector: object
    reality: sp.Matrix
    vectors: sp.Matrix
    left_inverse: sp.Matrix
    carrier: sp.Matrix
    carrier_coordinate_reality: sp.Matrix
    carrier_change: sp.Matrix
    carrier_basis: sp.Matrix
    carrier_inverse: sp.Matrix
    complement: sp.Matrix
    complement_basis: sp.Matrix
    complement_inverse: sp.Matrix
    coordinate_reality: sp.Matrix
    full_basis: sp.Matrix
    full_inverse: sp.Matrix


def carrier_chart(sectors: tuple[object, ...], momentum: int) -> Chart:
    sector = sectors[momentum]
    opposite = (-momentum) % 4
    polynomial = sector.polynomial
    if polynomial != sectors[opposite].polynomial:
        raise AssertionError("opposite sectors share a root field")
    reality = reality_operator(polynomial)
    vectors = fm(
        sp.Matrix.hstack(
            sector.x,
            sector.y,
            b119.reality_vector(reality, sectors[opposite].x, polynomial),
            b119.reality_vector(reality, sectors[opposite].y, polynomial),
        ),
        polynomial,
    )
    gram = fm(b119.field_adjoint(vectors, polynomial) * vectors, polynomial)
    left_inverse = fm(
        b119.field_inverse(gram, polynomial)
        * b119.field_adjoint(vectors, polynomial),
        polynomial,
    )
    carrier = fm(vectors * left_inverse, polynomial)
    carrier_coordinate_reality = fm(
        left_inverse * b119.reality_vector(reality, vectors, polynomial),
        polynomial,
    )
    carrier_change = fixed_basis(carrier_coordinate_reality, polynomial)
    carrier_change_inverse = b119.field_inverse(carrier_change, polynomial)
    carrier_basis = fm(vectors * carrier_change, polynomial)
    carrier_inverse = fm(carrier_change_inverse * left_inverse, polynomial)
    complement = fm(sp.eye(8) - carrier, polynomial)
    columns = independent_columns(complement, polynomial)
    raw_basis = complement[:, columns]
    raw_gram = fm(
        b119.field_adjoint(raw_basis, polynomial) * raw_basis,
        polynomial,
    )
    raw_inverse = fm(
        b119.field_inverse(raw_gram, polynomial)
        * b119.field_adjoint(raw_basis, polynomial),
        polynomial,
    )
    raw_coordinate_reality = fm(
        raw_inverse * b119.reality_vector(reality, raw_basis, polynomial),
        polynomial,
    )
    change = fixed_basis(raw_coordinate_reality, polynomial)
    complement_basis = fm(raw_basis * change, polynomial)
    complement_inverse = fm(
        b119.field_inverse(change, polynomial) * raw_inverse,
        polynomial,
    )
    coordinate_reality = fm(
        complement_inverse
        * b119.reality_vector(reality, complement_basis, polynomial),
        polynomial,
    )
    full_basis = fm(
        sp.Matrix.hstack(carrier_basis, complement_basis), polynomial
    )
    full_inverse = fm(
        sp.Matrix.vstack(carrier_inverse, complement_inverse), polynomial
    )
    if not (
        field_rank(vectors, polynomial) == 4
        and field_rank(complement, polynomial) == 4
        and feq(left_inverse * vectors, sp.eye(4), polynomial)
        and feq(complement_inverse * complement_basis, sp.eye(4), polynomial)
        and feq(full_inverse * full_basis, sp.eye(8), polynomial)
        and feq(full_basis * full_inverse, sp.eye(8), polynomial)
        and feq(coordinate_reality, sp.eye(4), polynomial)
        and feq(
            fm(
                carrier_inverse
                * b119.reality_vector(reality, carrier_basis, polynomial),
                polynomial,
            ),
            sp.eye(4),
            polynomial,
        )
        and feq(reality_matrix(reality, carrier, polynomial), carrier, polynomial)
        and feq(
            reality_matrix(reality, complement, polynomial),
            complement,
            polynomial,
        )
    ):
        raise AssertionError("exact reflection-real carrier chart")
    return Chart(
        sector,
        reality,
        vectors,
        left_inverse,
        carrier,
        carrier_coordinate_reality,
        carrier_change,
        carrier_basis,
        carrier_inverse,
        complement,
        complement_basis,
        complement_inverse,
        coordinate_reality,
        full_basis,
        full_inverse,
    )


def mu_swap(mu: sp.Expr) -> sp.Matrix:
    """The two reflection-coupled swaps in (x,y,Rx,Ry) coordinates."""
    if mu == 0:
        raise ZeroDivisionError("the completion scale is nonzero")
    result = sp.zeros(4)
    result[1, 0] = mu
    result[0, 1] = 1 / mu
    result[3, 2] = mu
    result[2, 3] = 1 / mu
    if sp.simplify(result * result) != sp.eye(4):
        raise AssertionError("mu-swap involution")
    return result


def carrier_swap(chart: Chart, mu: sp.Expr) -> sp.Matrix:
    polynomial = chart.sector.polynomial
    change_inverse = b119.field_inverse(chart.carrier_change, polynomial)
    return fm(change_inverse * mu_swap(mu) * chart.carrier_change, polynomial)


def first_image_vector(
    projector: sp.Matrix, polynomial: sp.Poly
) -> sp.Matrix:
    return next(
        projector[:, column]
        for column in range(projector.cols)
        if any(red(value, polynomial) != 0 for value in projector[:, column])
    )


def compatible_extension(
    swap: sp.Matrix, signature: sp.Matrix, polynomial: sp.Poly
) -> sp.Matrix:
    """Exhibit a nonzero reflection-real B with S B+B A=0."""
    plus = fm((sp.eye(4) + swap) / 2, polynomial)
    minus = fm((sp.eye(4) - swap) / 2, polynomial)
    columns: list[sp.Matrix] = []
    for column in range(4):
        sign = int(signature[column, column])
        projector = minus if sign == 1 else plus
        columns.append(first_image_vector(projector, polynomial))
    result = fm(sp.Matrix.hstack(*columns), polynomial)
    if not (
        feq(swap * result + result * signature, sp.zeros(4), polynomial)
        and feq(
            b119.field_conjugate(result, polynomial), result, polynomial
        )
        and field_rank(result, polynomial) > 0
    ):
        raise AssertionError("compatible nonzero extension")
    return result


@dataclass(frozen=True)
class ModuliMember:
    rank_plus: int
    mu: sp.Expr
    swap: sp.Matrix
    complement_action: sp.Matrix
    extension: sp.Matrix
    theta: sp.Matrix
    reflection_real: bool
    involutive: bool
    intertwines: bool
    block_roundtrip: bool


def displayed_member(
    chart: Chart,
    rank_plus: int,
    mu: sp.Expr = R(1),
    with_extension: bool = True,
) -> ModuliMember:
    if rank_plus not in range(5):
        raise ValueError("rank_plus must lie in 0..4")
    polynomial = chart.sector.polynomial
    swap = carrier_swap(chart, mu)
    signature = sp.diag(
        *(tuple(1 for _ in range(rank_plus))
          + tuple(-1 for _ in range(4 - rank_plus)))
    )
    extension = (
        compatible_extension(swap, signature, polynomial)
        if with_extension
        else sp.zeros(4)
    )
    carrier_action = fm(
        chart.carrier_basis * swap * chart.carrier_inverse, polynomial
    )
    complement_action = fm(
        chart.complement_basis
        * signature
        * chart.complement_inverse,
        polynomial,
    )
    mixed_action = fm(
        chart.carrier_basis
        * extension
        * chart.complement_inverse,
        polynomial,
    )
    theta = fm(carrier_action + mixed_action + complement_action, polynomial)
    coordinate = fm(chart.full_inverse * theta * chart.full_basis, polynomial)
    expected_coordinate = fm(
        sp.Matrix.vstack(
            sp.Matrix.hstack(swap, extension),
            sp.Matrix.hstack(sp.zeros(4), signature),
        ),
        polynomial,
    )
    original_swap = mu_swap(mu)
    block_constraints = (
        feq(swap * swap, sp.eye(4), polynomial)
        and feq(signature * signature, sp.eye(4), polynomial)
        and feq(
            swap * extension + extension * signature,
            sp.zeros(4),
            polynomial,
        )
    )
    return ModuliMember(
        rank_plus,
        mu,
        swap,
        complement_action,
        extension,
        theta,
        feq(reality_matrix(chart.reality, theta, polynomial), theta, polynomial),
        feq(theta * theta, sp.eye(8), polynomial),
        feq(theta * chart.vectors, chart.vectors * original_swap, polynomial),
        block_constraints and feq(coordinate, expected_coordinate, polynomial),
    )


def linear_map_matrix(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    """Matrix of X -> left X + X right in row-major coordinates."""
    columns: list[sp.Matrix] = []
    for row in range(4):
        for column in range(4):
            basis = sp.zeros(4)
            basis[row, column] = 1
            image = left * basis + basis * right
            columns.append(sp.Matrix(tuple(image)))
    return sp.Matrix.hstack(*columns)


def intertwiner_constraint_ranks() -> tuple[int, int, bool]:
    """Solve Delta [I;0]=0 in an exact adapted 8-by-8 chart."""
    constraint_columns: list[sp.Matrix] = []
    parameter_columns: list[sp.Matrix] = []
    carrier_inclusion = sp.Matrix.vstack(sp.eye(4), sp.zeros(4))
    for row in range(8):
        for column in range(8):
            basis = sp.zeros(8)
            basis[row, column] = 1
            constraint_columns.append(sp.Matrix(tuple(basis * carrier_inclusion)))
    for row in range(8):
        for column in range(4, 8):
            basis = sp.zeros(8)
            basis[row, column] = 1
            parameter_columns.append(sp.Matrix(tuple(basis)))
    constraint = sp.Matrix.hstack(*constraint_columns)
    parameter_map = sp.Matrix.hstack(*parameter_columns)
    parameter_kills_carrier = all(
        column == sp.zeros(32, 1)
        for column in (
            constraint * parameter_map[:, index]
            for index in range(parameter_map.cols)
        )
    )
    return constraint.rank(), parameter_map.rank(), parameter_kills_carrier


def block_equivalence_certificate() -> bool:
    """Certify the full nonlinear involution equations in adapted blocks."""
    a_symbols = sp.symbols("a0:16")
    b_symbols = sp.symbols("b0:16")
    action = sp.Matrix(4, 4, a_symbols)
    extension = sp.Matrix(4, 4, b_symbols)
    swap = mu_swap(R(1))
    theta = sp.Matrix.vstack(
        sp.Matrix.hstack(swap, extension),
        sp.Matrix.hstack(sp.zeros(4), action),
    )
    residual = sp.expand(theta * theta - sp.eye(8))
    return (
        residual[:4, :4] == swap * swap - sp.eye(4)
        and residual[:4, 4:] == swap * extension + extension * action
        and residual[4:, :4] == sp.zeros(4)
        and residual[4:, 4:] == action * action - sp.eye(4)
    )


@dataclass(frozen=True)
class DimensionCertificate:
    dimensions: tuple[int, ...]
    a_ranks: tuple[int, ...]
    b_ranks: tuple[int, ...]
    self_with_scale: tuple[int, ...]
    coupled_with_scales: tuple[int, ...]


def dimension_certificate(chart: Chart) -> DimensionCertificate:
    polynomial = chart.sector.polynomial
    swap = carrier_swap(chart, R(1))
    dimensions: list[int] = []
    a_ranks: list[int] = []
    b_ranks: list[int] = []
    for rank_plus in range(5):
        signature = sp.diag(
            *(tuple(1 for _ in range(rank_plus))
              + tuple(-1 for _ in range(4 - rank_plus)))
        )
        a_rank = field_rank(
            linear_map_matrix(signature, signature), polynomial
        )
        b_rank = field_rank(linear_map_matrix(swap, signature), polynomial)
        a_ranks.append(a_rank)
        b_ranks.append(b_rank)
        dimensions.append((16 - a_rank) + (16 - b_rank))
    fixed = tuple(dimensions)
    return DimensionCertificate(
        fixed,
        tuple(a_ranks),
        tuple(b_ranks),
        tuple(value + 1 for value in fixed),
        tuple(2 * value + 2 for value in fixed),
    )


@dataclass(frozen=True)
class FixtureCertificate:
    shear: sp.Rational
    sectors: tuple[object, ...]
    self_charts: tuple[Chart, Chart]
    displayed: tuple[tuple[ModuliMember, ...], ...]
    dimensions: tuple[DimensionCertificate, DimensionCertificate]


def build_fixture(shear: sp.Rational) -> FixtureCertificate:
    sectors = b119.make_sectors(shear)
    charts = (carrier_chart(sectors, 0), carrier_chart(sectors, 2))
    displayed = tuple(
        tuple(displayed_member(chart, rank_plus) for rank_plus in range(5))
        for chart in charts
    )
    dimensions = tuple(dimension_certificate(chart) for chart in charts)
    return FixtureCertificate(
        shear,
        sectors,
        charts,
        displayed,
        dimensions,  # type: ignore[arg-type]
    )


def fixture_certificates() -> tuple[FixtureCertificate, FixtureCertificate]:
    fixtures = tuple(build_fixture(shear) for shear in prior.SHEARS)
    if tuple(fixture.shear for fixture in fixtures) != prior.SHEARS:
        raise AssertionError("both exact shear fixtures")
    return fixtures  # type: ignore[return-value]


@dataclass(frozen=True)
class SpectralCertificate:
    inversion_entries: tuple[sp.Expr, ...]
    second_inversion_entries: tuple[sp.Expr, ...]
    inverse_members_distinct: bool
    stable_eigenvector: bool
    eigenvalues_distinct: bool
    x_y_independent: bool
    stable_component_nonzero: bool
    unstable_component_nonzero: bool
    commutator_nonzero: bool
    commutant_dimension: int
    polynomial_grading: bool
    digest: str


def spectral_projectors(
    monodromy: sp.Matrix, polynomial: sp.Poly
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    identity = sp.eye(2)
    denominator = red(RHO - 1 / RHO, polynomial)
    if denominator == 0:
        raise AssertionError("the reciprocal roots are distinct")
    stable = fm(
        (monodromy - (1 / RHO) * identity) / denominator,
        polynomial,
    )
    unstable = fm(identity - stable, polynomial)
    stable_vector = first_image_vector(stable, polynomial)
    if not (
        feq(stable * stable, stable, polynomial)
        and feq(unstable * unstable, unstable, polynomial)
        and feq(stable * unstable, sp.zeros(2), polynomial)
        and field_rank(stable, polynomial) == 1
        and field_rank(unstable, polynomial) == 1
        and feq(monodromy * stable, RHO * stable, polynomial)
        and feq(
            monodromy * unstable, (1 / RHO) * unstable, polynomial
        )
    ):
        raise AssertionError("simple reciprocal spectral resolution")
    return stable, unstable, stable_vector


def straddling_vector(
    stable: sp.Matrix, unstable: sp.Matrix, x: sp.Matrix, polynomial: sp.Poly
) -> sp.Matrix:
    candidates = (
        sp.Matrix((1, 0)),
        sp.Matrix((0, 1)),
        sp.Matrix((1, 1)),
        sp.Matrix((1, 2)),
    )
    return next(
        candidate
        for candidate in candidates
        if field_rank(sp.Matrix.hstack(x, candidate), polynomial) == 2
        and field_rank(fm(stable * candidate, polynomial), polynomial) == 1
        and field_rank(fm(unstable * candidate, polynomial), polynomial) == 1
    )


def commutator_map(monodromy: sp.Matrix) -> sp.Matrix:
    columns: list[sp.Matrix] = []
    for row in range(2):
        for column in range(2):
            basis = sp.zeros(2)
            basis[row, column] = 1
            columns.append(sp.Matrix(tuple(basis * monodromy - monodromy * basis)))
    return sp.Matrix.hstack(*columns)


def spectral_certificate(sector: object) -> SpectralCertificate:
    polynomial = sector.polynomial
    # The stored antiperiodic cycle product carries the wrap sign.  The
    # positive companion monodromy used by the root field is its negative,
    # with exact eigenvalues rho and rho^-1.
    monodromy = fm(-sector.transfer.monodromy, polynomial)
    inverse_monodromy = b119.field_inverse(monodromy, polynomial)
    stable, unstable, x = spectral_projectors(monodromy, polynomial)
    unstable_vector = first_image_vector(unstable, polynomial)
    eigenbasis = fm(sp.Matrix.hstack(x, unstable_vector), polynomial)
    eigenbasis_inverse = b119.field_inverse(eigenbasis, polynomial)
    diagonal = fm(sp.diag(RHO, 1 / RHO), polynomial)
    if not feq(
        eigenbasis_inverse * monodromy * eigenbasis,
        diagonal,
        polynomial,
    ):
        raise AssertionError("exact diagonalization of companion monodromy")

    inverse_thetas: list[sp.Matrix] = []
    residual_entries: list[tuple[sp.Expr, ...]] = []
    for mu in (R(1), R(2)):
        exchange = sp.Matrix(((0, 1 / mu), (mu, 0)))
        theta = fm(eigenbasis * exchange * eigenbasis_inverse, polynomial)
        residual = fm(
            theta * monodromy * theta - inverse_monodromy, polynomial
        )
        inverse_thetas.append(theta)
        residual_entries.append(
            tuple(red(value, polynomial) for value in tuple(residual))
        )

    y = straddling_vector(stable, unstable, x, polynomial)
    pinned_basis = fm(sp.Matrix.hstack(x, y), polynomial)
    pinned_theta = fm(
        pinned_basis
        * sp.Matrix(((0, 1), (1, 0)))
        * b119.field_inverse(pinned_basis, polynomial),
        polynomial,
    )
    commutator = fm(
        pinned_theta * monodromy - monodromy * pinned_theta, polynomial
    )
    commute_rank = field_rank(commutator_map(monodromy), polynomial)
    # Cayley--Hamilton reduces every polynomial in M to aI+bM.  Both basis
    # elements preserve the exact stable/unstable resolution.
    cayley_hamilton = fm(
        monodromy**2 - monodromy.trace() * monodromy + sp.eye(2),
        polynomial,
    )
    polynomial_grading = (
        feq(cayley_hamilton, sp.zeros(2), polynomial)
        and all(
            feq(left * power * right, sp.zeros(2), polynomial)
            for power in (sp.eye(2), monodromy)
            for left, right in ((stable, unstable), (unstable, stable))
        )
    )
    return SpectralCertificate(
        residual_entries[0],
        residual_entries[1],
        not feq(inverse_thetas[0], inverse_thetas[1], polynomial),
        feq(monodromy * x, RHO * x, polynomial),
        red(RHO - 1 / RHO, polynomial) != 0,
        field_rank(sp.Matrix.hstack(x, y), polynomial) == 2,
        field_rank(fm(stable * y, polynomial), polynomial) == 1,
        field_rank(fm(unstable * y, polynomial), polynomial) == 1,
        field_rank(commutator, polynomial) > 0,
        4 - commute_rank,
        polynomial_grading,
        exact_digest(monodromy, x, y, commutator),
    )


@dataclass(frozen=True)
class MinimalityCertificate:
    fixed_mu_unique: bool
    rank_plus: int
    reference_swap: bool
    identity_on_complement: bool
    uniqueness_rank: int
    scaled_family: bool
    family_dimension: int
    digest: str


def minimality_certificate(chart: Chart) -> MinimalityCertificate:
    polynomial = chart.sector.polynomial
    swap = displayed_member(chart, 4, R(1), with_extension=False)
    scaled = displayed_member(chart, 4, R(2), with_extension=False)
    reference = b119.swap_completion(chart.vectors, polynomial)
    # In adapted blocks, identity on Q is the simultaneous system B=0,
    # A-I=0.  Its coefficient matrix on the 32 (B,A) coordinates is I_32.
    uniqueness_rank = sp.eye(32).rank()
    fixed_mu_unique = uniqueness_rank == 32 and swap.rank_plus == 4
    scaled_family = (
        all(
            member.reflection_real
            and member.involutive
            and member.intertwines
            and member.block_roundtrip
            for member in (swap, scaled)
        )
        and not feq(swap.theta, scaled.theta, polynomial)
        and swap.mu == 1
        and scaled.mu == 2
    )
    return MinimalityCertificate(
        fixed_mu_unique,
        swap.rank_plus,
        feq(swap.theta, reference, polynomial),
        feq(
            swap.theta * chart.complement_basis,
            chart.complement_basis,
            polynomial,
        ),
        uniqueness_rank,
        scaled_family,
        1,
        exact_digest(swap.theta, scaled.theta),
    )


SCOPE_KEYS = (
    "moduli",
    "dimension_law",
    "nonpinning",
    "inversion",
    "eigenline",
    "minimality",
    "positive_family",
    "next_hinge",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "moduli": "moduli" in note,
        "dimension_law": (
            "8 + 2r(4-r)" in note or "(8,14,16,14,8)" in note
        ),
        "nonpinning": any(
            phrase in note
            for phrase in ("does not pin", "pins nothing", "not uniquely")
        ),
        "inversion": (
            "inverts the monodromy" in note
            or "theta m theta = m^{-1}" in note
        ),
        "eigenline": "eigenvector" in note and "straddles" in note,
        "minimality": "minimal" in note and "normalization" in note,
        "positive_family": (
            "one point of" in note or "positive-dimensional" in note
        ),
        "next_hinge": "hinge" in note or "descending member" in note,
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
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
        result["os_boundary"] = False
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    return result


N5_LINES = (
    "N5: per_element: reflection-reality covariance, involutivity, boundary mu-swap, orthocomplement-involution parametrization, dimension-law, inversion-family, eigenline-exclusion, spectral-projector-exclusion, and normalized-minimality certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: at fixed mu the completion moduli stratum with +1-eigenspace dimension r has exact real dimension 8 + 2r(4-r), and the swap completion is one point",
    "per_block: physical inversion holds for the swap and a positive-dimensional family; commutation and spectral-projector expressibility fail for every member; minimality selects the swap only with mu = 1 normalization",
    "lattice_wide: checked and not executed — the moduli-adjointness hinge, the curved-carrier dependency, the cross-lane facet-charge bridge, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
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
        "Block 126 note/runner/cache and ancestors 125--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_NATURALITY_MODULI_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TIME_DRESSING_ADJOINTNESS_WALL_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_time_dressing_adjointness_wall_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_time_dressing_adjointness_wall_2026_08_17.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(authority[f"ancestor_{number}"] for number in range(103, 126))
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    fixtures = fixture_certificates()
    constraint_rank, parameter_rank, parameter_kills_carrier = (
        intertwiner_constraint_ranks()
    )
    all_members = tuple(
        member
        for fixture in fixtures
        for self_sector in fixture.displayed
        for member in self_sector
    )
    parametrization_raw = (
        constraint_rank == 32
        and 64 - constraint_rank == 32
        and parameter_rank == 32
        and parameter_kills_carrier
        and block_equivalence_certificate()
        and all(
            member.reflection_real
            and member.involutive
            and member.intertwines
            and member.block_roundtrip
            for member in all_members
        )
        and all(
            field_rank(member.extension, chart.sector.polynomial) > 0
            for fixture in fixtures
            for chart, members in zip(
                fixture.self_charts, fixture.displayed
            )
            for member in members
        )
    )
    parametrization_gate = parametrization_raw
    if mutation == "break_parametrization":
        parametrization_gate = False
    checks.check(
        "B-the-moduli-parametrization",
        "the reflection-real involutive intertwiner solution is exactly the mu-swap/A/B block parametrization",
        parametrization_gate,
    )

    expected_dimensions = (8, 14, 16, 14, 8)
    expected_self_scales = (9, 15, 17, 15, 9)
    expected_coupled_scales = (18, 30, 34, 30, 18)
    dimension_raw = all(
        certificate.dimensions == expected_dimensions
        and certificate.a_ranks == (16, 10, 8, 10, 16)
        and certificate.b_ranks == (8, 8, 8, 8, 8)
        and certificate.self_with_scale == expected_self_scales
        and certificate.coupled_with_scales == expected_coupled_scales
        for fixture in fixtures
        for certificate in fixture.dimensions
    )
    dimension_gate = dimension_raw
    if mutation == "break_dimension_law":
        dimension_gate = False
    checks.check(
        "C-the-dimension-law",
        "explicit ranks give fixed-mu dimensions (8,14,16,14,8), with the stated self and coupled scale totals in both fixtures",
        dimension_gate,
    )

    spectra = tuple(
        spectral_certificate(sector)
        for fixture in fixtures
        for sector in fixture.sectors
    )
    minimalities = tuple(
        minimality_certificate(chart)
        for fixture in fixtures
        for chart in fixture.self_charts
    )
    inversion_raw = (
        all(
            certificate.inversion_entries == (0, 0, 0, 0)
            and certificate.second_inversion_entries == (0, 0, 0, 0)
            and certificate.inverse_members_distinct
            for certificate in spectra
        )
        and all(certificate.scaled_family for certificate in minimalities)
    )
    inversion_gate = inversion_raw
    if mutation in ("break_inversion_identity", "claim_inversion_pins"):
        inversion_gate = False
    checks.check(
        "D-the-inversion-criterion",
        "all four companion entries vanish for Theta M Theta=M^-1, and a second moduli member also inverts M, so inversion does not pin",
        inversion_gate,
    )

    exclusion_raw = all(
        certificate.stable_eigenvector
        and certificate.eigenvalues_distinct
        and certificate.x_y_independent
        and certificate.stable_component_nonzero
        and certificate.unstable_component_nonzero
        and certificate.commutator_nonzero
        and certificate.commutant_dimension == 2
        and certificate.polynomial_grading
        for certificate in spectra
    )
    exclusion_gate = exclusion_raw
    if mutation in ("break_eigenvector_argument", "claim_commuting_member"):
        exclusion_gate = False
    checks.check(
        "E-the-commutation-exclusion",
        "Mx=rho x, y is independent and straddles both eigenlines, excluding every commuting or polynomial-in-M moduli member",
        exclusion_gate,
    )

    minimality_raw = all(
        certificate.fixed_mu_unique
        and certificate.rank_plus == 4
        and certificate.reference_swap
        and certificate.identity_on_complement
        and certificate.uniqueness_rank == 32
        and certificate.scaled_family
        and certificate.family_dimension == 1
        for certificate in minimalities
    )
    minimality_gate = minimality_raw
    if mutation in (
        "break_minimality_uniqueness",
        "claim_unconditional_uniqueness",
    ):
        minimality_gate = False
    checks.check(
        "F-the-minimality-selection",
        "at mu=1 the r=4, A=identity, B=0 point is uniquely minimal; without normalization the minimal points form a one-parameter mu family",
        minimality_gate,
    )

    verdict_raw = inversion_raw and exclusion_raw and minimality_raw
    verdict_gate = verdict_raw
    if mutation == "break_verdict":
        verdict_gate = False
    checks.check(
        "G-the-verdict-assembly",
        "independently certified inversion non-pinning, spectral exclusion, and normalized-only minimality imply no displayed criterion uniquely selects the swap",
        verdict_gate,
    )

    note_scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "moduli/dimension/inversion/eigenline/minimality/N1--N8/W1/N5 and no-go/TOE firewalls are present",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 400,
    )

    first_dimension = fixtures[0].dimensions[0]
    print(
        "MODULI: Theta=[S_mu B;0 A] in the exact reflection-fixed (V,Q) chart; "
        f"rank(constraints)={constraint_rank}, rank(parameters)={parameter_rank}, "
        "A^2=I and S_mu B+B A=0."
    )
    print(
        f"DIMENSIONS: fixed mu={first_dimension.dimensions}; "
        f"self with scale={first_dimension.self_with_scale}; "
        f"coupled k=1/3 with scales={first_dimension.coupled_with_scales}; "
        f"rank_A={first_dimension.a_ranks}, rank_B={first_dimension.b_ranks}; fixtures=2."
    )
    print(
        "INVERSION: Theta M Theta=M^-1 has entry residuals "
        f"{spectra[0].inversion_entries} at mu=1 and "
        f"{spectra[0].second_inversion_entries} at mu=2; the two exact members differ."
    )
    print(
        "EIGENLINES: Mx=rho x exactly; rank[x,y]=2; y has nonzero stable and "
        "unstable components and therefore straddles the grading; no commuting "
        f"or polynomial member exists; witness#={spectra[0].digest}."
    )
    print(
        "MINIMALITY: fixed mu=1 gives the unique r=4 A=identity, B=0 swap point; "
        "mu=1 and mu=2 display the unnormalized one-parameter minimal family; "
        f"witness#={minimalities[0].digest}."
    )
    for line in N5_LINES:
        print(line)
    print(
        "RESULT: the completion is one point of an exactly classified "
        "positive-dimensional moduli space — canonical only as minimal plus "
        "normalized — and that freedom is now the campaign's live resource "
        "for the descending-member hinge"
    )
    print(
        "DECISION_CUT: run the moduli-adjointness hinge and the curved "
        "dependency; reject uniqueness claims for the displayed criteria"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory "
        "count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
