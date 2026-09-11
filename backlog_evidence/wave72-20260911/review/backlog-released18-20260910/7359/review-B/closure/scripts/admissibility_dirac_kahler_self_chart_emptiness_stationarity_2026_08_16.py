#!/usr/bin/env python3
"""Block 117: exact self-chart emptiness and stationarity certificate.

The Block 111 self branches are reconstructed from exact QQ(i) data at the
Block 116 authority tip.  A symbolic three-slice window identity reduces the
transfer determinant at one to minus a squared window non-stationarity.  The
two self sectors and a second exact fixture then decide the displayed
contractive regions without floating-point input.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_chart_invariant_contractivity_obstruction_2026_08_15 as prior


b111 = prior.paired_source.prior
base = prior.base
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_"
    "OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_chart_invariant_contractivity_"
    "obstruction_2026_08_15.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_chart_invariant_"
    "contractivity_obstruction_2026_08_15.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_chart_invariant_contractivity_obstruction_2026_08_15.py",
    "logs/runner-cache/admissibility_dirac_kahler_chart_invariant_contractivity_obstruction_2026_08_15.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "4e566b14a6352a9a62590252a9755c7a103c1b9e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block116-chart-invariant-contractivity-obstruction-20260815"
)
PARENT_COMMIT = "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"
PARENT_NOTE_BLOB = "b3838b43d1e16dbd497faa8f613cb3d89be1abc1"
PARENT_RUNNER_BLOB = "0e5604358a3d1ff1ca7cadf1f58f40f00de4fa6b"
PARENT_CACHE_BLOB = "669e5bddb8aeb019ca96e05b89637afa5ef70b2c"
ANCESTOR_COMMITS = (
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

PRIMARY_SHEAR = sp.Rational(5, 13)
SECOND_SHEAR = sp.Rational(3, 5)
TAU = sp.symbols("tau0:3", real=True)
LAMBDA = sp.symbols("lambda", real=True)
FILE_POINT = (-6, -6, -6)
PARAMETER_POINTS = (
    FILE_POINT,
    (0, 0, 0),
    (1, -2, 3),
    (7, -11, 13),
)
REVERSE_ZERO_POINTS = tuple(range(-3, 4))
PRIMARY_SQUARES = (
    sp.Rational(355348797912000, 1026791823428467),
    sp.Rational(228512035080000, 1026791823428467),
)
SECOND_SQUARES = (
    sp.Rational(86496072000, 250649423107),
    sp.Rational(35364504000, 250649423107),
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


def canonical(value: sp.Expr) -> sp.Expr:
    return sp.factor(sp.cancel(sp.expand(value)))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return prior.matrix_equal(left, right)


def exact_rank(matrix: sp.Matrix) -> int:
    return prior.exact_rank(matrix)


MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_window_identity",
    "break_middle_diagonal",
    "break_square_constant",
    "claim_parameter_dependent",
    "claim_contractive_point",
    "break_sign_pattern",
    "break_degree_argument",
    "mismatch_second_fixture",
    "claim_stationary_already",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_axiom_amendment",
    "claim_toe_progress",
)


CHANGE = b111.tau_real_change()
CHANGE_INVERSE = CHANGE.inv()


@dataclass(frozen=True)
class WindowIdentityData:
    factor: sp.Poly
    right_hand_side: sp.Expr
    residual: sp.Expr


def symbolic_window_identity() -> WindowIdentityData:
    y00, y11, y22 = sp.symbols("y00 y11 y22", real=True)
    x01, q01, x02, q02, x12, q12 = sp.symbols(
        "x01 q01 x02 q02 x12 q12", real=True
    )
    y01 = x01 + I * q01
    y02 = x02 + I * q02
    y12 = x12 + I * q12
    hermitian = sp.Matrix(
        (
            (y00, y01, y02),
            (sp.conjugate(y01), y11, y12),
            (sp.conjugate(y02), sp.conjugate(y12), y22),
        )
    )
    source = hermitian.extract((0, 1), (0, 1))
    shifted = hermitian.extract((1, 2), (1, 2))
    factor = sp.Poly(sp.expand((LAMBDA * source - shifted).det()), LAMBDA)
    nonstationarity = hermitian[0, 1] - hermitian[1, 2]
    right_hand_side = canonical(
        (hermitian[0, 0] - hermitian[1, 1])
        * (hermitian[1, 1] - hermitian[2, 2])
        - nonstationarity * sp.conjugate(nonstationarity)
    )
    residual = canonical(factor.eval(1) - right_hand_side)
    return WindowIdentityData(factor, right_hand_side, residual)


@dataclass(frozen=True)
class Branch:
    dressing: sp.Matrix
    gram: sp.Matrix
    system_shape: tuple[int, int]
    system_rank: int
    free_count: int
    solve_residual_zero: bool
    involution: bool
    reality: bool
    hermiticity: bool


def self_branch(
    propagator: sp.Matrix, *, reverse: bool = False, overall_sign: int = -1
) -> Branch:
    """Reconstruct both exact triangular orientations of the self cell."""
    plus = (1, 6, 7)
    minus = (0, 2, 3, 4, 5)
    diagonal = sp.diag(*(1 if index in plus else -1 for index in range(8)))
    origin = CHANGE * diagonal * CHANGE_INVERSE
    rows, columns = (minus, plus) if reverse else (plus, minus)
    directions: list[sp.Matrix] = []
    for row in rows:
        for column in columns:
            elementary = sp.zeros(8, 8)
            elementary[row, column] = 1
            directions.append(CHANGE * elementary * CHANGE_INVERSE)

    system = sp.Matrix.hstack(
        *(
            b111.hermitian_residual(b111.E * item * propagator * b111.F.T)
            for item in directions
        )
    )
    rhs = -b111.hermitian_residual(b111.E * origin * propagator * b111.F.T)
    coordinates, parameters = system.gauss_jordan_solve(rhs)
    free = sorted(
        set().union(*(entry.free_symbols for entry in coordinates)), key=str
    )
    coordinates = coordinates.subs(dict(zip(free, TAU)))
    triangular = origin + sum(
        (
            coordinates[index] * direction
            for index, direction in enumerate(directions)
        ),
        sp.zeros(8),
    )
    dressing = (overall_sign * triangular).applyfunc(sp.expand)
    gram = (
        b111.E * dressing * propagator * b111.F.T
    ).conjugate().applyfunc(sp.factor)
    return Branch(
        dressing=dressing,
        gram=gram,
        system_shape=system.shape,
        system_rank=exact_rank(system),
        free_count=len(free),
        solve_residual_zero=matrix_equal(system * coordinates, rhs),
        involution=matrix_equal(dressing**2, sp.eye(8)),
        reality=matrix_equal(
            b111.J * dressing.conjugate() * b111.J, dressing
        ),
        hermiticity=matrix_equal(gram, gram.H),
    )


def leading_minors(matrix: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(
        canonical(matrix[:size, :size].det(method="domain-ge"))
        for size in range(1, 5)
    )


def transfer_factor(matrix: sp.Matrix) -> sp.Poly:
    source = matrix.extract((0, 1), (0, 1))
    shifted = matrix.extract((1, 2), (1, 2))
    return sp.Poly(canonical((LAMBDA * source - shifted).det()), LAMBDA)


def point_substitution(point: tuple[int, int, int]) -> dict[sp.Symbol, int]:
    return dict(zip(TAU, point))


def sign_profile(
    minors: tuple[sp.Expr, ...], point: tuple[int, int, int]
) -> tuple[int, ...]:
    substitution = point_substitution(point)
    return tuple(int(sp.sign(minor.subs(substitution))) for minor in minors)


@dataclass(frozen=True)
class Sector:
    momentum: int
    branch: Branch
    minors: tuple[sp.Expr, ...]
    factor: sp.Poly
    coefficients: tuple[sp.Expr, sp.Expr, sp.Expr]
    f_one: sp.Expr
    nonstationarity: sp.Expr
    nonstationarity_square: sp.Expr
    equal_middle: bool
    window_reduction: bool
    leading_coefficient_is_second_minor: bool
    cancellation_identity: bool
    constant_in_parameters: bool
    leading_coefficient_varies: bool
    positive_constant_term: bool
    discriminant_identity: bool
    parameter_values: tuple[sp.Expr, ...]
    point_profiles: tuple[tuple[int, ...], ...]


def analyze_sector(propagator: sp.Matrix, momentum: int) -> Sector:
    branch = self_branch(propagator)
    minors = leading_minors(branch.gram)
    factor = transfer_factor(branch.gram)
    a, b, c = tuple(canonical(item) for item in factor.all_coeffs())
    f_one = canonical(factor.eval(1))
    nonstationarity = canonical(branch.gram[0, 1] - branch.gram[1, 2])
    nonstationarity_square = canonical(
        nonstationarity * sp.conjugate(nonstationarity)
    )
    discriminant_form = canonical(
        (a - c) ** 2 - 2 * f_one * (a + c) + f_one**2
    )
    return Sector(
        momentum=momentum,
        branch=branch,
        minors=minors,
        factor=factor,
        coefficients=(a, b, c),
        f_one=f_one,
        nonstationarity=nonstationarity,
        nonstationarity_square=nonstationarity_square,
        equal_middle=canonical(branch.gram[1, 1] - branch.gram[2, 2]) == 0,
        window_reduction=canonical(f_one + nonstationarity_square) == 0,
        leading_coefficient_is_second_minor=canonical(a - minors[1]) == 0,
        cancellation_identity=canonical(f_one - (a + b + c)) == 0,
        constant_in_parameters=not bool(f_one.free_symbols),
        leading_coefficient_varies=any(
            canonical(sp.diff(a, variable)) != 0 for variable in TAU
        ),
        positive_constant_term=bool(c > 0),
        discriminant_identity=canonical(factor.discriminant() - discriminant_form)
        == 0,
        parameter_values=tuple(
            canonical(f_one.subs(point_substitution(point)))
            for point in PARAMETER_POINTS
        ),
        point_profiles=tuple(
            sign_profile(minors, point) for point in PARAMETER_POINTS
        ),
    )


def fixture_sectors(shear: sp.Rational) -> tuple[tuple[sp.Matrix, ...], tuple[Sector, Sector]]:
    fixture = base.fixture_data(shear)
    propagators = tuple(
        b111.momentum_block(fixture.propagator, momentum)
        for momentum in range(4)
    )
    return propagators, (
        analyze_sector(propagators[0], 0),
        analyze_sector(propagators[2], 2),
    )


@dataclass(frozen=True)
class OppositeSignClosure:
    parity_identities: bool
    normal_profile: tuple[int, ...]
    opposite_profile: tuple[int, ...]
    transfer_invariant: bool


def opposite_sign_closure(sector: Sector) -> OppositeSignClosure:
    opposite_gram = -sector.branch.gram
    opposite_minors = leading_minors(opposite_gram)
    return OppositeSignClosure(
        parity_identities=all(
            canonical(
                opposite_minors[index]
                - (-1) ** (index + 1) * sector.minors[index]
            )
            == 0
            for index in range(4)
        ),
        normal_profile=sign_profile(sector.minors, FILE_POINT),
        opposite_profile=sign_profile(opposite_minors, FILE_POINT),
        transfer_invariant=transfer_factor(opposite_gram) == sector.factor,
    )


@dataclass(frozen=True)
class ReverseClosure:
    branch: Branch
    affine_single_parameter: bool
    determinant_degree_bound: int
    zero_points: tuple[int, ...]
    zero_values: tuple[sp.Expr, ...]
    determinant_identically_zero: bool


def reverse_closure(propagator: sp.Matrix) -> ReverseClosure:
    branch = self_branch(propagator, reverse=True)
    active_symbols = set().union(*(entry.free_symbols for entry in branch.gram))
    affine_single_parameter = bool(
        active_symbols == {TAU[0]}
        and any(sp.diff(entry, TAU[0]) != 0 for entry in branch.gram)
        and all(canonical(sp.diff(entry, TAU[0], 2)) == 0 for entry in branch.gram)
    )
    determinant = canonical(branch.gram.det(method="domain-ge"))
    zero_values = tuple(canonical(determinant.subs(TAU[0], point)) for point in REVERSE_ZERO_POINTS)
    return ReverseClosure(
        branch=branch,
        affine_single_parameter=affine_single_parameter,
        determinant_degree_bound=branch.gram.rows,
        zero_points=REVERSE_ZERO_POINTS,
        zero_values=zero_values,
        determinant_identically_zero=determinant == 0,
    )


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


SCOPE_KEYS = (
    "window_identity",
    "equal_middle",
    "negative_square",
    "parameter_identity",
    "stationarity",
    "toeplitz",
    "exactly_empty",
    "pairing",
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
        "window_identity": "window identity" in note,
        "equal_middle": (
            "equal middle window diagonals" in note
            or "equal middle diagonals" in note
            or "y11 = y22" in note
        ),
        "negative_square": (
            "minus a perfect square" in note
            or "minus the squared modulus" in note
        ),
        "parameter_identity": "identically in the branch parameters" in note,
        "stationarity": "stationarity" in note,
        "toeplitz": "toeplitz" in note,
        "exactly_empty": "exactly empty" in note,
        "pairing": (
            "action-derived pairing" in note or "modular pairing" in note
        ),
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
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    return result


def square_text(value: sp.Rational) -> str:
    return f"({value.p}/{value.q})^2"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority",
        "Block 116 parent note/runner/cache and ancestors 115--103 are exact content-bound authorities",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "scripts/admissibility_dirac_kahler_chart_invariant_contractivity_obstruction_2026_08_15.py",
            "logs/runner-cache/admissibility_dirac_kahler_chart_invariant_contractivity_obstruction_2026_08_15.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 116)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    window = symbolic_window_identity()
    tested_window_residual = (
        sp.Integer(1) if mutation == "break_window_identity" else window.residual
    )
    checks.check(
        "B-the-window-identity",
        "for a fully symbolic Hermitian 3x3 window, f(1)=(Y00-Y11)(Y11-Y22)-|Y01-Y12|^2 exactly",
        window.factor.degree() == 2
        and window.residual == 0
        and tested_window_residual == 0,
    )

    primary_propagators, primary = fixture_sectors(PRIMARY_SHEAR)
    branch_structure = all(
        sector.branch.system_shape[1] == 15
        and sector.branch.system_rank == 12
        and sector.branch.free_count == 3
        and sector.branch.solve_residual_zero
        and sector.branch.involution
        and sector.branch.reality
        and sector.branch.hermiticity
        for sector in primary
    )
    tested_equal_middle = tuple(sector.equal_middle for sector in primary)
    if mutation == "break_middle_diagonal":
        tested_equal_middle = (False, tested_equal_middle[1])
    checks.check(
        "C-equal-middle-diagonals",
        "both symbolic self sectors have Y11-Y22=0, hence f_k(1)=-|Y01-Y12|^2 identically",
        branch_structure
        and all(sector.equal_middle for sector in primary)
        and all(tested_equal_middle)
        and all(sector.window_reduction for sector in primary),
    )

    primary_expected = tuple(-value**2 for value in PRIMARY_SQUARES)
    tested_primary_expected = primary_expected
    if mutation == "break_square_constant":
        tested_primary_expected = (primary_expected[0] + 1, primary_expected[1])
    parameter_dependence_claimed = mutation == "claim_parameter_dependent"
    contractive_point_claimed = mutation == "claim_contractive_point"
    primary_non_pd_counts = tuple(
        sum(profile != (1, 1, 1, 1) for profile in sector.point_profiles)
        for sector in primary
    )
    checks.check(
        "D-the-perfect-square-constants",
        "f_0(1) and f_2(1) are the pinned negative rational squares at four exact points including non-PD points; a=det(Y|{0,1}) is the second minor and cancels in a+b+c, so every PD pair of roots strictly straddles one and both contractive regions are exactly empty",
        tuple(sector.f_one for sector in primary) == primary_expected
        and tuple(sector.f_one for sector in primary) == tested_primary_expected
        and all(
            sector.parameter_values == (expected,) * len(PARAMETER_POINTS)
            for sector, expected in zip(primary, primary_expected)
        )
        and len(set(PARAMETER_POINTS)) >= 3
        and all(sector.point_profiles[0] == (1, 1, 1, 1) for sector in primary)
        and all(count >= 2 for count in primary_non_pd_counts)
        and all(
            sector.leading_coefficient_is_second_minor
            and sector.cancellation_identity
            and sector.constant_in_parameters
            and sector.leading_coefficient_varies
            and sector.positive_constant_term
            and sector.discriminant_identity
            and sector.f_one < 0
            for sector in primary
        )
        and not parameter_dependence_claimed
        and not contractive_point_claimed,
    )

    opposite = tuple(opposite_sign_closure(sector) for sector in primary)
    reverse = tuple(
        reverse_closure(primary_propagators[momentum]) for momentum in (0, 2)
    )
    tested_opposite_profiles = tuple(item.opposite_profile for item in opposite)
    if mutation == "break_sign_pattern":
        tested_opposite_profiles = ((1, 1, 1, 1), tested_opposite_profiles[1])
    tested_degree_bounds = tuple(item.determinant_degree_bound for item in reverse)
    tested_zero_counts = tuple(len(item.zero_points) for item in reverse)
    if mutation == "break_degree_argument":
        tested_degree_bounds = (5, tested_degree_bounds[1])
        tested_zero_counts = (6, tested_zero_counts[1])
    checks.check(
        "E-family-closures",
        "the opposite-sign families invert odd Sylvester minors, show profile (-,+,-,+) at the displayed witness, and share the even transfer pencil so the negative square transports to any of their positive points; each reverse family is affine in one parameter with determinant degree <=4 and seven displayed zeros, hence det Y=0 identically",
        all(
            item.parity_identities
            and item.normal_profile == (1, 1, 1, 1)
            and item.opposite_profile == (-1, 1, -1, 1)
            and item.transfer_invariant
            for item in opposite
        )
        and all(profile == (-1, 1, -1, 1) for profile in tested_opposite_profiles)
        and all(
            item.branch.system_rank == 14
            and item.branch.free_count == 1
            and item.branch.solve_residual_zero
            and item.branch.involution
            and item.branch.reality
            and item.branch.hermiticity
            and item.affine_single_parameter
            and item.determinant_degree_bound <= 4
            and len(set(item.zero_points)) >= 7
            and all(value == 0 for value in item.zero_values)
            and item.determinant_identically_zero
            for item in reverse
        )
        and all(bound <= 4 for bound in tested_degree_bounds)
        and all(count >= 7 for count in tested_zero_counts),
    )

    _, second = fixture_sectors(SECOND_SHEAR)
    second_expected = tuple(-value**2 for value in SECOND_SQUARES)
    tested_second_expected = second_expected
    if mutation == "mismatch_second_fixture":
        tested_second_expected = (second_expected[0] + 1, second_expected[1])
    checks.check(
        "F-second-fixture",
        "at c=3/5 both exact f_k(1) values are the pinned negative squares and the same all-PD root-straddling argument makes both contractive regions empty",
        tuple(sector.f_one for sector in second) == second_expected
        and tuple(sector.f_one for sector in second) == tested_second_expected
        and all(sector.point_profiles[0] == (1, 1, 1, 1) for sector in second)
        and all(
            sector.equal_middle
            and sector.window_reduction
            and sector.leading_coefficient_is_second_minor
            and sector.cancellation_identity
            and sector.constant_in_parameters
            and sector.positive_constant_term
            and sector.discriminant_identity
            and sector.f_one < 0
            for sector in second
        ),
    )

    note = normalized_note()
    note_scope = scope_certificate(note, mutation)
    all_sectors = primary + second
    stationary_already_claimed = mutation == "claim_stationary_already"
    checks.check(
        "G-stationarity-diagnosis",
        "the obstruction is minus the squared window non-stationarity Y01-Y12; contractivity requires Y01=Y12, the Toeplitz stationarity supplied by the action-derived/modular pairing construction",
        all(
            sector.window_reduction
            and sector.nonstationarity != 0
            and not sector.nonstationarity.free_symbols
            and sector.f_one == -sector.nonstationarity_square
            for sector in all_sectors
        )
        and note_scope["stationarity"]
        and note_scope["toeplitz"]
        and note_scope["pairing"]
        and not stationary_already_claimed,
    )

    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "the note carries the exact identity, stationarity, chart-only OS, N1--N8, W1, five N5 resolutions, axiom, ADM, gravity, and TOE firewalls",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 300,
    )

    print(
        "PRIMARY_SQUARES: "
        f"f0(1)=-{square_text(PRIMARY_SQUARES[0])}; "
        f"f2(1)=-{square_text(PRIMARY_SQUARES[1])}; "
        f"points={PARAMETER_POINTS}; non_PD_counts={primary_non_pd_counts}"
    )
    print(
        "SECOND_FIXTURE: c=3/5; "
        f"f0(1)=-{square_text(SECOND_SQUARES[0])}; "
        f"f2(1)=-{square_text(SECOND_SQUARES[1])}"
    )
    print(
        "FAMILY_CLOSURES: opposite_sign=(-,+,-,+); "
        f"reverse_degree<=4; reverse_zero_points={REVERSE_ZERO_POINTS}; detY=0"
    )
    print(f"RUNTIME_SECONDS: {time.monotonic() - started:.3f}")
    print(
        "N5: per_element: exact window, equal-diagonal, negative-square, Sylvester, and singular-family identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: every positive point of the displayed main and opposite-sign branches has transfer roots strictly straddling one, and the reversed triangular family has no positive point"
    )
    print(
        "per_block: the displayed self charts are empty by closed form and the stationary action-derived pairing remains live"
    )
    print(
        "lattice_wide: checked and not executed — the stationary action-derived/modular pairing, curved OS positivity beyond the displayed carrier, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the self-chart contractive regions are exactly empty by a closed-form identity — the obstruction is the pairing's non-stationarity, so the finite OS package requires the action-derived pairing"
    )
    print(
        "DECISION_CUT: advance the stationary/modular pairing construction; reject further dressing-side searches on the displayed charts"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
