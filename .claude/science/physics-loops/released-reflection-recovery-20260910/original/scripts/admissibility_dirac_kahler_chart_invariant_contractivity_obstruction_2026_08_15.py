#!/usr/bin/env python3
"""Block 116: exact chart-invariant contractivity-obstruction certificate.

The committed Block 115 witness and its transfer factors are reconstructed
from exact QQ(i) data.  A distinct denominator-200 point of the same
32-real-dimensional paired-block chart is rebuilt exactly, proving that the
even Gram sectors and their transfer factors are frozen across the chart.
The resulting obstruction is chart-local: it is not an OS or positive-variety
no-go.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_transfer_spectrum_selection_gap_2026_08_15 as prior


witness_source = prior.prior
paired_source = witness_source.prior.prior
momentum = witness_source.momentum
base = prior.base
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_"
    "OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_"
    "GAP_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_transfer_spectrum_selection_"
    "gap_2026_08_15.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_transfer_spectrum_"
    "selection_gap_2026_08_15.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_GAP_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_transfer_spectrum_selection_gap_2026_08_15.py",
    "logs/runner-cache/admissibility_dirac_kahler_transfer_spectrum_selection_gap_2026_08_15.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "4e566b14a6352a9a62590252a9755c7a103c1b9e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block115-transfer-spectrum-selection-gap-20260815"
)
PARENT_COMMIT = "c78301fef7521d0518f485f1bf9266983c9e516a"
PARENT_NOTE_BLOB = "498bd9796c64452560bd7d29b0e2894bfa65b44c"
PARENT_RUNNER_BLOB = "8e66909cd4bbe992baf119d4cc7083bad2869e10"
PARENT_CACHE_BLOB = "30e6a3a3d8620e52d9a130c32a886283b1ecd79b"
ANCESTOR_COMMITS = (
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

SHEAR = sp.Rational(5, 13)
IDENTITY_32 = sp.eye(32)
PLATEAU_DENOMINATOR = 200
ROOT_SCALE = 10**6
PLATEAU_Q_NUMERATOR_PAIRS = (
    ((255, -43), (232, 16), (-5, -26), (27, 284)),
    ((-23, 347), (-154, 162), (26, -143), (56, -67)),
    ((-185, -633), (-33, -387), (350, -797), (8, 105)),
    ((-42, -104), (24, 17), (-232, 247), (43, -46)),
)
F0_COEFFICIENT_PIN = (
    240551220040889870812178294535809284844643543367917958,
    -291801878443785401379820600522977512484145379126480301,
    25674305116199140209012757725867816390883233973960300,
)
F0_AT_ONE_PIN = (
    -25576353286696390358629548261300411248618601784602043
)
F2_COEFFICIENT_PIN = (
    5175261142208185330195747399956023340238344517047759,
    -6033804201790765437297938355001793292322654475638139,
    536815344990418589208178945880770658322516674278000,
)
PLATEAU_ROOT_ISOLATIONS = (
    ((95504, 95505), (1117550, 1117551)),
    ((142698, 142699), (985094, 985095)),
    ((97045, 97046), (1068847, 1068848)),
    ((588287, 588288), (902037, 902038)),
)
WINDOW_ROOT_ISOLATIONS = (
    ((71662, 71663), (3732532, 3732533)),
    ((1019740, 1019741), (15884778, 15884779)),
    ((63490, 63491), (3563012, 3563013)),
    ((365428, 365429), (1113186, 1113187)),
)
WINDOW_K0_COEFFICIENT_PIN = (
    247930031518545454339980740529607322063826834613872026782399364041241587791125,
    -943174322604288957200306328033832930345548160666695339716971417013923733443327,
    66317219474813773877705299317310893232393268017190639583287202161756453496100,
)
SQUARED_ROOTS_K0_COEFFICIENT_PIN = (
    57864889463160616620695740751253144733828515763827814718981460853640524048604158646556048292254011818889764,
    -72796365424514183380930557656340009144384975239247958069728308017548667895245867567622197956398227042915801,
    659169943199689346430154766803878852641795665637025426309614176299991887275030265351391703898465976090000,
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
    return sp.cancel(sp.expand(value))


def normalized(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.applyfunc(sp.expand)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return prior.matrix_equal(left, right)


def exact_rank(matrix: sp.Matrix) -> int:
    return prior.exact_rank(matrix)


def primitive_from_coefficients(
    coefficients: tuple[sp.Expr, ...], variable: sp.Symbol
) -> sp.Poly:
    rational = sp.Poly.from_list(coefficients, gens=variable, domain=sp.QQ)
    _, integral = rational.clear_denoms(convert=True)
    primitive = integral.primitive()[1]
    return -primitive if primitive.LC() < 0 else primitive


def polynomial_signs(polynomials: tuple[sp.Poly, ...]) -> tuple[int, ...]:
    return tuple(int(sp.sign(polynomial.eval(1))) for polynomial in polynomials)


def two_root_isolation_certificate(
    factor: sp.Poly, intervals: tuple[tuple[int, int], ...]
) -> bool:
    if len(intervals) != 2 or factor.degree() != 2:
        return False
    a, b, c = factor.all_coeffs()
    first, second = intervals
    points = tuple(
        sp.Rational(endpoint, ROOT_SCALE)
        for interval in intervals
        for endpoint in interval
    )
    values = tuple(factor.eval(point) for point in points)
    return bool(
        a > 0
        and b < 0
        and c > 0
        and factor.discriminant() > 0
        and 0 <= first[0] < first[1] < second[0] < second[1]
        and values[0] > 0
        and values[1] < 0
        and values[2] < 0
        and values[3] > 0
    )


def above_one_profile(
    isolations: tuple[tuple[tuple[int, int], ...], ...]
) -> tuple[int, ...]:
    if any(
        lower < ROOT_SCALE < upper
        for intervals in isolations
        for lower, upper in intervals
    ):
        raise ArithmeticError("an isolation interval contains one")
    return tuple(
        sum(lower >= ROOT_SCALE for lower, _ in intervals)
        for intervals in isolations
    )


MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_plateau_involution",
    "claim_plateau_equals_witness",
    "break_sector_freeze",
    "break_f0_pin",
    "claim_f0_contractive",
    "break_profile_signs",
    "claim_semigroup",
    "break_two_step_profile",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_variety_exhausted",
    "claim_axiom_amendment",
    "claim_toe_progress",
)


@dataclass(frozen=True)
class PlateauData:
    q: sp.Matrix
    first_paired_block: sp.Matrix
    third_paired_block: sp.Matrix
    operator: sp.Matrix
    gram: sp.Matrix
    transfer: prior.TransferData
    leading_minors: tuple[sp.Expr, ...]
    leading_minor_signs: tuple[int, ...]
    system_shape: tuple[int, int]
    system_rank: int
    solve_residual_zero: bool


def plateau_q() -> sp.Matrix:
    return sp.Matrix(
        4,
        4,
        lambda row, column: (
            sp.Rational(
                PLATEAU_Q_NUMERATOR_PAIRS[row][column][0],
                PLATEAU_DENOMINATOR,
            )
            + I
            * sp.Rational(
                PLATEAU_Q_NUMERATOR_PAIRS[row][column][1],
                PLATEAU_DENOMINATOR,
            )
        ),
    )


def reconstruct_plateau(fixture, witness) -> PlateauData:
    q = plateau_q()
    propagator_blocks = tuple(
        momentum.momentum_block(fixture.propagator, sector)
        for sector in range(4)
    )
    origin, directions, system, rhs = paired_source.pair_newton_system(
        propagator_blocks[1], propagator_blocks[3], q
    )
    if system.shape != (32, 32) or len(directions) != 32:
        raise ArithmeticError("the paired-chart Hermiticity system is not 32 by 32")
    coefficients = system.inv(method="DM") * rhs
    first_paired_block = normalized(
        origin
        + sum(
            (coefficients[index] * directions[index] for index in range(32)),
            sp.zeros(8),
        )
    )
    third_paired_block = normalized(
        momentum.J * first_paired_block.conjugate() * momentum.J
    )
    operator = normalized(
        witness_source.assemble_from_momentum(
            (
                witness.blocks[0],
                first_paired_block,
                witness.blocks[2],
                third_paired_block,
            )
        )
    )
    gram = normalized(base.dressed_gram(operator, fixture))
    leading_minors, leading_minor_signs = prior.positive_leading_minors(gram)
    return PlateauData(
        q,
        first_paired_block,
        third_paired_block,
        operator,
        gram,
        prior.transfer_certificate(gram),
        leading_minors,
        leading_minor_signs,
        system.shape,
        exact_rank(system),
        matrix_equal(system * coefficients, rhs),
    )


@dataclass(frozen=True)
class WindowData:
    factors: tuple[sp.Poly, ...]
    isolations: tuple[tuple[tuple[int, int], ...], ...]
    profile: tuple[int, ...]
    k0_squared_roots_factor: sp.Poly


def two_step_window(transfer: prior.TransferData) -> WindowData:
    variable = sp.symbols("lambda", real=True)
    factors = tuple(
        prior.primitive_transfer_factor(
            block.extract((0, 1), (0, 1)),
            block.extract((2, 3), (2, 3)),
            variable,
        )
        for block in transfer.blocks
    )
    a, b, c = transfer.factors[0].all_coeffs()
    squared_roots_factor = primitive_from_coefficients(
        (a * a, -(b * b - 2 * a * c), c * c), variable
    )
    return WindowData(
        factors,
        WINDOW_ROOT_ISOLATIONS,
        above_one_profile(WINDOW_ROOT_ISOLATIONS),
        squared_roots_factor,
    )


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


SCOPE_KEYS = (
    "chart_invariant",
    "frozen",
    "plateau_profile",
    "window_profile",
    "non_semigroup",
    "self_block",
    "pairing",
    "chart_no_point",
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
        "chart_invariant": (
            "chart invariant" in note or "chart-invariant" in note
        ),
        "frozen": "frozen" in note,
        "plateau_profile": "(1, 0, 1, 0)" in note,
        "window_profile": "(1, 2, 1, 1)" in note,
        "non_semigroup": "not a semigroup" in note,
        "self_block": "self-block" in note,
        "pairing": (
            "action-derived pairing" in note or "modular pairing" in note
        ),
        "chart_no_point": (
            "no transfer-contractive point exists on the displayed chart"
            in note
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


CONSEQUENCE_KEYS = (
    "vary_self_blocks",
    "action_pairing",
    "displayed_chart_only",
    "not_variety_exhausted",
)


def consequence_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "vary_self_blocks": (
            "self-block" in note
            and (
                "varying the self-blocks" in note
                or "self-block variation" in note
                or "self-block-varying" in note
            )
        ),
        "action_pairing": (
            "action-derived pairing" in note or "modular pairing" in note
        ),
        "displayed_chart_only": (
            "no transfer-contractive point exists on the displayed chart"
            in note
        ),
        "not_variety_exhausted": (
            "does not exhaust the positive variety" in note
        ),
    }
    if mutation == "claim_variety_exhausted":
        result["not_variety_exhausted"] = False
    return result


def isolation_text(intervals: tuple[tuple[int, int], ...]) -> str:
    return ",".join(
        f"({lower}/{ROOT_SCALE},{upper}/{ROOT_SCALE})"
        for lower, upper in intervals
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
        "Block 115 parent note/runner/cache and ancestors 114--103 are exact content-bound authorities",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_GAP_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "scripts/admissibility_dirac_kahler_transfer_spectrum_selection_gap_2026_08_15.py",
            "logs/runner-cache/admissibility_dirac_kahler_transfer_spectrum_selection_gap_2026_08_15.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"]
            for number in range(103, 115)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    fixture = base.fixture_data(SHEAR)
    witness = witness_source.pinned_witness(SHEAR)
    witness_gram = normalized(
        witness_source.left_dressed_gram(witness.operator, fixture)
    )
    witness_transfer = prior.transfer_certificate(witness_gram)
    plateau = reconstruct_plateau(fixture, witness)

    plateau_involution_rank = exact_rank(
        plateau.operator * plateau.operator - IDENTITY_32
    )
    tested_involution_rank = (
        1 if mutation == "break_plateau_involution" else plateau_involution_rank
    )
    claimed_plateau_equals_witness = mutation == "claim_plateau_equals_witness"
    plateau_witness_rank = exact_rank(plateau.operator - witness.operator)
    checks.check(
        "B-the-plateau-point",
        "the pinned denominator-200 point has A^2=I, reflection reality, Gram Hermiticity, sixteen positive minors, and rank(A_plateau-A_witness)=16",
        PLATEAU_DENOMINATOR == 200
        and len(PLATEAU_Q_NUMERATOR_PAIRS) == 4
        and all(len(row) == 4 for row in PLATEAU_Q_NUMERATOR_PAIRS)
        and plateau.operator.shape == (32, 32)
        and plateau_involution_rank == 0
        and tested_involution_rank == 0
        and exact_rank(
            fixture.reflection
            * plateau.operator.conjugate()
            * fixture.reflection
            - plateau.operator
        )
        == 0
        and matrix_equal(plateau.gram, plateau.gram.H)
        and len(plateau.leading_minors) == 16
        and plateau.leading_minor_signs == (1,) * 16
        and plateau_witness_rank == 16
        and not claimed_plateau_equals_witness,
    )

    sector_difference_ranks = tuple(
        exact_rank(plateau_block - witness_block)
        for plateau_block, witness_block in zip(
            plateau.transfer.blocks, witness_transfer.blocks
        )
    )
    tested_sector_difference_ranks = (
        (0, 4, 1, 4)
        if mutation == "break_sector_freeze"
        else sector_difference_ranks
    )
    plateau_f0_coefficients = tuple(
        plateau.transfer.factors[0].all_coeffs()
    )
    tested_f0_coefficients = (
        (plateau_f0_coefficients[0] + 1,) + plateau_f0_coefficients[1:]
        if mutation == "break_f0_pin"
        else plateau_f0_coefficients
    )
    plateau_momentum_blocks = tuple(
        momentum.momentum_block(plateau.operator, sector)
        for sector in range(4)
    )
    checks.check(
        "C-chart-invariance",
        "the chart varies only the paired blocks while the self-blocks are frozen, so f_0 and f_2 are invariants of the entire 32-dimensional chart",
        plateau.system_shape == (32, 32)
        and plateau.system_rank == 32
        and plateau.solve_residual_zero
        and matrix_equal(plateau_momentum_blocks[0], witness.blocks[0])
        and matrix_equal(plateau_momentum_blocks[2], witness.blocks[2])
        and sector_difference_ranks == (0, 4, 0, 4)
        and tested_sector_difference_ranks == (0, 4, 0, 4)
        and plateau.transfer.factors[0] == witness_transfer.factors[0]
        and plateau.transfer.factors[2] == witness_transfer.factors[2]
        and plateau_f0_coefficients == F0_COEFFICIENT_PIN
        and tested_f0_coefficients == F0_COEFFICIENT_PIN
        and tuple(plateau.transfer.factors[2].all_coeffs())
        == F2_COEFFICIENT_PIN,
    )

    f0 = plateau.transfer.factors[0]
    upper_root_interval = PLATEAU_ROOT_ISOLATIONS[0][1]
    upper_root_lower = sp.Rational(upper_root_interval[0], ROOT_SCALE)
    upper_root_upper = sp.Rational(upper_root_interval[1], ROOT_SCALE)
    claimed_f0_contractive = mutation == "claim_f0_contractive"
    checks.check(
        "D-the-obstruction-root",
        "f_0(1) is exactly negative and its unremovable upper root is isolated in (1117550/10^6,1117551/10^6), so no transfer-contractive point exists on the entire chart",
        f0.eval(1) == F0_AT_ONE_PIN
        and F0_AT_ONE_PIN < 0
        and upper_root_interval == (1117550, 1117551)
        and f0.eval(upper_root_lower) < 0
        and f0.eval(upper_root_upper) > 0
        and two_root_isolation_certificate(
            f0, PLATEAU_ROOT_ISOLATIONS[0]
        )
        and sector_difference_ranks[0] == 0
        and plateau.transfer.factors[0] == witness_transfer.factors[0]
        and not claimed_f0_contractive,
    )

    plateau_signs = polynomial_signs(plateau.transfer.factors)
    tested_plateau_signs = (
        (-1, -1, -1, 1)
        if mutation == "break_profile_signs"
        else plateau_signs
    )
    plateau_profile = above_one_profile(PLATEAU_ROOT_ISOLATIONS)
    odd_contraction_certificates = tuple(
        prior.hermitian_pd_two_by_two(
            plateau.transfer.sources[sector]
            - plateau.transfer.shifted[sector]
        )
        for sector in (1, 3)
    )
    checks.check(
        "E-the-plateau-profile",
        "at the plateau f_k(1) signs are (-,+,-,+), the profile is (1,0,1,0), and both roots in each odd sector are isolated below one",
        plateau_signs == (-1, 1, -1, 1)
        and tested_plateau_signs == (-1, 1, -1, 1)
        and plateau_profile == (1, 0, 1, 0)
        and all(
            two_root_isolation_certificate(factor, intervals)
            for factor, intervals in zip(
                plateau.transfer.factors, PLATEAU_ROOT_ISOLATIONS
            )
        )
        and all(
            upper < ROOT_SCALE
            for sector in (1, 3)
            for _, upper in PLATEAU_ROOT_ISOLATIONS[sector]
        )
        and all(odd_contraction_certificates),
    )

    window = two_step_window(witness_transfer)
    window_signs = polynomial_signs(window.factors)
    tested_window_profile = (
        (1, 1, 1, 1)
        if mutation == "break_two_step_profile"
        else window.profile
    )
    claimed_semigroup = mutation == "claim_semigroup"
    window_k0_coefficients = tuple(window.factors[0].all_coeffs())
    squared_roots_k0_coefficients = tuple(
        window.k0_squared_roots_factor.all_coeffs()
    )
    checks.check(
        "F-two-step-non-semigroup",
        "the witness {0,1}->{2,3} window has signs (-,+,-,-), profile (1,2,1,1), both k=1 roots above one, and its k=0 primitive is not the squared-roots transform",
        window_signs == (-1, 1, -1, -1)
        and window.profile == (1, 2, 1, 1)
        and tested_window_profile == (1, 2, 1, 1)
        and all(
            two_root_isolation_certificate(factor, intervals)
            for factor, intervals in zip(
                window.factors, WINDOW_ROOT_ISOLATIONS
            )
        )
        and all(
            lower > ROOT_SCALE
            for lower, _ in WINDOW_ROOT_ISOLATIONS[1]
        )
        and window_k0_coefficients == WINDOW_K0_COEFFICIENT_PIN
        and squared_roots_k0_coefficients
        == SQUARED_ROOTS_K0_COEFFICIENT_PIN
        and window.factors[0] != window.k0_squared_roots_factor
        and WINDOW_K0_COEFFICIENT_PIN
        != SQUARED_ROOTS_K0_COEFFICIENT_PIN
        and not claimed_semigroup,
    )

    note = normalized_note()
    consequences = consequence_certificate(note, mutation)
    checks.check(
        "G-consequences",
        "contractivity on the positive variety requires self-block variation beyond the displayed chart or the action-derived pairing; the note makes no variety-wide no-go claim",
        set(consequences) == set(CONSEQUENCE_KEYS)
        and all(consequences.values()),
    )

    scope = scope_certificate(note, mutation)
    checks.check(
        "H-scope",
        "the note preserves the chart-only obstruction, both profiles, non-semigroup result, N1--N8, W1, five N5 resolutions, OS, axiom, ADM, gravity, and TOE firewalls",
        set(scope) == set(SCOPE_KEYS) and all(scope.values()),
    )

    print(
        "PLATEAU: "
        f"D={PLATEAU_DENOMINATOR}; rank(Ap-Aw)={plateau_witness_rank}; "
        f"sector_difference_ranks={sector_difference_ranks}; PD_minors=16"
    )
    print(
        "F0_OBSTRUCTION: "
        f"coefficients={plateau_f0_coefficients}; f0(1)={f0.eval(1)}; "
        f"upper_root=({upper_root_interval[0]}/{ROOT_SCALE},{upper_root_interval[1]}/{ROOT_SCALE})"
    )
    print(
        "ROOT_ISOLATIONS: "
        f"plateau k1={isolation_text(PLATEAU_ROOT_ISOLATIONS[1])}; "
        f"k3={isolation_text(PLATEAU_ROOT_ISOLATIONS[3])}; "
        f"window k1={isolation_text(WINDOW_ROOT_ISOLATIONS[1])}"
    )
    print(
        "PROFILES: "
        f"plateau signs={plateau_signs} above_one={plateau_profile}; "
        f"window signs={window_signs} above_one={window.profile}; "
        f"k0_window_coefficients={window_k0_coefficients}; "
        f"k0_squared_roots_coefficients={squared_roots_k0_coefficients}"
    )
    print(f"RUNTIME_SECONDS: {time.monotonic() - started:.3f}")
    print(
        "N5: per_element: exact plateau, freeze, root-isolation, and non-semigroup identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: the even sectors are frozen chart invariants while the odd sectors contract below one at the plateau"
    )
    print(
        "per_block: the unremovable obstruction root is exactly isolated and the two-step window is not the square of the one-step transfer"
    )
    print(
        "lattice_wide: checked and not executed — self-block-varying positive charts, the action-derived/modular pairing, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the contractivity obstruction is a chart invariant — the even Gram sectors are frozen across the entire displayed positive chart, so the finite OS package requires self-block variation or the action-derived pairing"
    )
    print(
        "DECISION_CUT: advance self-block-varying charts and the modular pairing; reject further paired-block searches on the displayed chart"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
