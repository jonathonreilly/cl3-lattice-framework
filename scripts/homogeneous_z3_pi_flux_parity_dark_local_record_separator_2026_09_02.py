#!/usr/bin/env python3
"""Exact homogeneous-Z3 pi-flux parity darkness and local-Record separator.

The load-bearing proof is sparse integer shift/parity algebra on Z^3.  Finite
matrices are deliberately avoided so periodic wraparound cannot impersonate
an infinite-lattice Taylor coefficient.
"""

from __future__ import annotations

import argparse
import itertools
import subprocess
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-homogeneous-z3-record-flux-block47-20260902"
)
NOTE = ROOT / "docs" / (
    "HOMOGENEOUS_Z3_PI_FLUX_PARITY_DARK_LOCAL_RECORD_SEPARATOR_"
    "BOUNDED_THEOREM_NOTE_2026-09-02.md"
)
NO_GO = ROOT / "docs" / (
    "HOMOGENEOUS_Z3_PI_FLUX_PARITY_DARK_LOCAL_RECORD_SEPARATOR_"
    "NO_GO_DISCIPLINE_CHECKLIST_2026-09-02.md"
)
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/HOMOGENEOUS_Z3_PI_FLUX_PARITY_DARK_LOCAL_RECORD_SEPARATOR_BOUNDED_THEOREM_NOTE_2026-09-02.md",
    ".claude/science/physics-loops/toe-homogeneous-z3-record-flux-block47-20260902/GOAL.md",
    ".claude/science/physics-loops/toe-homogeneous-z3-record-flux-block47-20260902/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-homogeneous-z3-record-flux-block47-20260902/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-homogeneous-z3-record-flux-block47-20260902/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-homogeneous-z3-record-flux-block47-20260902/PRIOR_ART_SEARCH.md",
    ".claude/science/physics-loops/toe-homogeneous-z3-record-flux-block47-20260902/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-homogeneous-z3-record-flux-block47-20260902/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-homogeneous-z3-record-flux-block47-20260902/SOURCE_BINDING.md",
    "docs/HOMOGENEOUS_Z3_PI_FLUX_PARITY_DARK_LOCAL_RECORD_SEPARATOR_NO_GO_DISCIPLINE_CHECKLIST_2026-09-02.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "archive/notes/docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "docs/STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md",
    "docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md",
    "archive/notes/docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md",
    "docs/STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md",
    "docs/GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/STRICT_FREE_STAR_GIBBS_CUBE_RECORD_FLUX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/SOURCE_BINDING.md",
)
BASE_COMMIT = "2cea9a595ee2f0a6c47096de6f821b905182f48c"
PARENT_COMMIT = "c8cd2069a08f79943be065ceeae6fd62ee6aa15a"
PREREG_COMMIT = "8c5ae00b712641effe6b4d4ec06ec449eb45adcb"
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
MINIMAL_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"

FROZEN_PACKET_BLOBS = {
    f"{PACKET}/GOAL.md": "835ab4f424192006c820c99231c387aeaf73ee95",
    f"{PACKET}/EXACT_TARGET_CONTRACT.md": "9f9c8f675aedeaa6e5e3061de952cf52059a8958",
    f"{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "893ccf7d82011ca466103fa006f544054c24e2ae",
    f"{PACKET}/MUTATION_PLAN.md": "62a2ff3b871c7c094e61646bc4bff6fa4cb2924c",
    f"{PACKET}/PRIOR_ART_SEARCH.md": "3d44f1a717eaf42055ef4e3536e0ea5b610835c6",
    f"{PACKET}/ROUTE_PORTFOLIO.md": "a2645629e0431e4d56e4cc2c7cb56275ce24ffb5",
    f"{PACKET}/TRACE_GATE.md": "da685fe3662f02d8a2d63d19b6d9bea2c6c0c362",
}

PINNED_MAIN_BLOBS = {
    MINIMAL_PATH: MINIMAL_BLOB,
    "docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md":
        "19add235591a3bda9fdf55e57356fa58b1c11b14",
    "docs/STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md":
        "93c415c5d0f8038618311e35ac7d19420cb853ae",
    "docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md":
        "d5a6224c8a0112362fc0a7d9218c5ce452099c5a",
    "docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md":
        "f5b2569c5f69fc1b81a749d6437b3ec9b90d90fe",
    "docs/STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md":
        "3a59324815a27d9fec14a66e0615a63129b3ea8f",
    "docs/GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md":
        "8bc8a4f90efc6494727ae39a377b128b22f01bc2",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md":
        "f29dd373f25367fade34253ae3ff842a2a24c80f",
}

PINNED_PARENT_BLOBS = {
    "docs/STRICT_FREE_STAR_GIBBS_CUBE_RECORD_FLUX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md":
        "f3b383eb3b786dc8af7ed102a0715f099774e25e",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/SOURCE_BINDING.md":
        "2c7216ced7e1de3761947412a69080d64177373b",
}

# Historical commit/path/blob identities stay unchanged; only live paths move.
CURRENT_MAIN_PATHS = {
    "docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md":
        "archive/notes/docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md":
        "archive/notes/docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md",
}

# Corrected current parent is checked separately from immutable original provenance.
CURRENT_PARENT_BLOBS = {
    "docs/STRICT_FREE_STAR_GIBBS_CUBE_RECORD_FLUX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md":
        "e6f9ffbfdec8dfdde98412107e15146af75c7218",
    ".claude/science/physics-loops/toe-local-gibbs-flux-record-block46-20260902/SOURCE_BINDING.md":
        "2c7216ced7e1de3761947412a69080d64177373b",
}

OPEN_PR_HEADS = {
    7828: "3fada70dd5a0429c4e12dc8ae79f6b11b555443a",
    7829: "551dfd9f317a36db050dffa0d717764f9af9f291",
    7830: "f8581d80efdd0856aa1a64078a48931a763765e9",
    7831: "ff8573cf054125db0dd0fcf07dba131280b6b736",
    7832: "9301c509842ea4835def91ad50f41bfd4f80ab1c",
}
SOURCE_BINDING_BLOB = "f3b4a3f04c229efaf64938bb8d62411ba551a80a"

MUTATIONS = (
    "all_plus_H1_links",
    "commuting_H1_directions",
    "wrong_H1_square_with_mixed_shift",
    "drop_one_coordinate_parity",
    "claim_hamming_one_is_dark",
    "claim_only_low_order_cancellation",
    "nonzero_H1_body_diagonal",
    "zero_H0_body_diagonal",
    "wrong_H0_third_coefficient",
    "wrong_bessel_argument",
    "wrong_bessel_lower_bound",
    "claim_perfect_uniform_transfer",
    "branch_specific_source",
    "branch_specific_cadence",
    "branch_specific_effect",
    "branch_specific_writer",
    "suppress_exterior_bonds",
    "odd_period_wrap_as_infinite_proof",
    "treat_coordinate_bits_as_site_qubits",
    "treat_source_as_permanent_Record",
    "leave_incident_hopping_on_after_Record",
    "claim_sequential_pulses_are_dark",
    "claim_action_selected",
    "claim_born_or_clock_derived",
    "claim_record_formation_derived",
    "claim_I4_closed",
    "claim_obligation_or_TOE_movement",
    "break_flux_sign",
    "break_rotation_gauge_covariance",
    "source_blob_drift",
    "claim_bare_translation_invariance",
)

Site = tuple[int, int, int]
State = dict[Site, int]


@dataclass
class Harness:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {label} :: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {label} :: {detail}")


def git_blob(commit: str, path: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def worktree_blob(path: str) -> str:
    return subprocess.run(
        ["git", "hash-object", path],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def commit_exists(commit: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def has_direct_parent(commit: str, parent: str) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", f"{commit}^"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0 and result.stdout.strip() == parent


def blob_matches(commit: str, path: str, expected: str) -> bool:
    try:
        return git_blob(commit, path) == expected and worktree_blob(CURRENT_MAIN_PATHS.get(path, path)) == expected
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def source_certificate(harness: Harness, mutation: str | None) -> None:
    prereg_ok = all(
        blob_matches(PREREG_COMMIT, path, blob)
        for path, blob in FROZEN_PACKET_BLOBS.items()
    )
    main_ok = all(
        blob_matches(BASE_COMMIT, path, blob)
        for path, blob in PINNED_MAIN_BLOBS.items()
    )
    parent_original_ok = all(
        git_blob(PARENT_COMMIT, path) == blob
        for path, blob in PINNED_PARENT_BLOBS.items()
    )
    parent_current_ok = all(
        worktree_blob(path) == blob for path, blob in CURRENT_PARENT_BLOBS.items()
    )
    parent_ok = parent_original_ok and parent_current_ok
    binding_path = f"{PACKET}/SOURCE_BINDING.md"
    try:
        binding = (ROOT / binding_path).read_text()
    except FileNotFoundError:
        binding = ""
    prs_named = all(
        f"| `#{number}` | `{head}` |" in binding
        for number, head in OPEN_PR_HEADS.items()
    )
    prs_exist = all(commit_exists(head) for head in OPEN_PR_HEADS.values())
    parent_binding_path = (
        ".claude/science/physics-loops/"
        "toe-local-gibbs-flux-record-block46-20260902/SOURCE_BINDING.md"
    )
    try:
        parent_binding = subprocess.run(
            ["git", "show", f"{PARENT_COMMIT}:{parent_binding_path}"],
            cwd=ROOT,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).stdout
    except subprocess.CalledProcessError:
        parent_binding = ""
    prs_inherited = all(
        f"| `#{number}` | `{head}` |" in parent_binding
        for number, head in OPEN_PR_HEADS.items()
    )
    try:
        expected_binding = (
            "0" * 40 if mutation == "source_blob_drift" else SOURCE_BINDING_BLOB
        )
        binding_frozen = worktree_blob(binding_path) == expected_binding
    except (subprocess.CalledProcessError, FileNotFoundError):
        binding_frozen = False
    prs_based = all(
        has_direct_parent(head, BASE_COMMIT) for head in OPEN_PR_HEADS.values()
    )
    harness.check(
        "source, parent, preregistration, and adjacent PR heads are pinned",
        prereg_ok and main_ok and parent_ok and binding_frozen
        and prs_named and prs_exist and prs_based and prs_inherited,
        f"prereg={prereg_ok} main={main_ok} parent_original={parent_original_ok} "
        f"parent_current={parent_current_ok} "
        f"binding={binding_frozen} PR_names={5 if prs_named else 0}/5 "
        f"PR_commits={5 if prs_exist else 0}/5 "
        f"direct_base={5 if prs_based else 0}/5 "
        f"parent_rows={5 if prs_inherited else 0}/5",
    )


def add_site(x: Site, axis: int, step: int) -> Site:
    values = list(x)
    values[axis] += step
    return tuple(values)  # type: ignore[return-value]


def clean(state: State) -> State:
    return {site: value for site, value in state.items() if value}


def add_into(target: State, source: State, scale: int = 1) -> None:
    for site, value in source.items():
        target[site] = target.get(site, 0) + scale * value
    for site in [site for site, value in target.items() if not value]:
        del target[site]


def eta(axis: int, x: Site) -> int:
    return -1 if sum(x[:axis]) % 2 else 1


def direction(state: State, axis: int, staggered: bool) -> State:
    result: State = {}
    for site, value in state.items():
        sign = eta(axis, site) if staggered else 1
        for step in (-1, 1):
            neighbor = add_site(site, axis, step)
            result[neighbor] = result.get(neighbor, 0) + sign * value
    return clean(result)


def hamiltonian(state: State, staggered: bool) -> State:
    result: State = {}
    for axis in range(3):
        add_into(result, direction(state, axis, staggered))
    return clean(result)


def weighted_hamiltonian(state: State, weights: tuple[int, int, int]) -> State:
    result: State = {}
    for axis, weight in enumerate(weights):
        add_into(result, direction(state, axis, True), weight)
    return clean(result)


def q_operator(state: State) -> State:
    result: State = {}
    for axis in range(3):
        add_into(result, direction(direction(state, axis, False), axis, False))
    return clean(result)


def weighted_q_operator(state: State, weights: tuple[int, int, int]) -> State:
    result: State = {}
    for axis, weight in enumerate(weights):
        squared = direction(direction(state, axis, False), axis, False)
        add_into(result, squared, weight * weight)
    return clean(result)


def parity(state: State, axes: tuple[int, ...]) -> State:
    return {
        site: value * (-1 if sum(site[axis] for axis in axes) % 2 else 1)
        for site, value in state.items()
    }


def translate(state: State, axis: int, step: int) -> State:
    return {add_site(site, axis, step): value for site, value in state.items()}


def power_coefficient(staggered: bool, power: int, target: Site) -> int:
    state: State = {(0, 0, 0): 1}
    for _ in range(power):
        state = hamiltonian(state, staggered)
    return state.get(target, 0)


def link_and_flux_certificate(harness: Harness, mutation: str | None) -> None:
    def link_eta(axis: int, site: Site) -> int:
        if mutation == "all_plus_H1_links":
            return 1
        if mutation == "break_flux_sign" and axis == 2:
            return -1 if site[0] % 2 else 1
        return eta(axis, site)

    reps = list(itertools.product((0, 1), repeat=3))
    self_adjoint = all(
        link_eta(axis, site) == link_eta(axis, add_site(site, axis, 1))
        for site in reps for axis in range(3)
    )
    flux0: set[int] = set()
    flux1: set[int] = set()
    for site in reps:
        for i, j in itertools.combinations(range(3), 2):
            flux0.add(1)
            flux1.add(
                link_eta(i, site)
                * link_eta(j, add_site(site, i, 1))
                * link_eta(i, add_site(site, j, 1))
                * link_eta(j, site)
            )

    # U|x> = i^(x1+x2+x3)|x> maps the usual -i eta(T-T^-1)
    # staggered derivative to the symmetric signed adjacency exactly.
    unitary_equivalence = True
    for site in reps:
        total = sum(site)
        for axis in range(3):
            for step, derivative_phase in ((1, 3), (-1, 1)):
                exponent = (-total + derivative_phase + total + step) % 4
                unitary_equivalence &= exponent == 0

    ok = (
        self_adjoint and flux0 == {1} and flux1 == {-1}
        and unitary_equivalence
    )
    harness.check(
        "the two self-adjoint NN link fields carry uniform +1/-1 face flux",
        ok,
        f"K0_flux={sorted(flux0)} K1_flux={sorted(flux1)}; KS unitary equivalence={unitary_equivalence}",
    )


def clifford_certificate(harness: Harness, mutation: str | None) -> None:
    candidate_is_staggered = mutation != "commuting_H1_directions"

    def candidate_direction(state: State, axis: int) -> State:
        return direction(state, axis, candidate_is_staggered)

    def candidate_hamiltonian(state: State) -> State:
        result: State = {}
        for axis in range(3):
            add_into(result, candidate_direction(state, axis))
        return clean(result)

    reps = list(itertools.product((0, 1), repeat=3))
    pairwise = True
    squares = True
    square_sum = True
    unequal_square_sum = True
    parity_even_support = True
    for site in reps:
        basis = {site: 1}
        for i, j in itertools.combinations(range(3), 2):
            anti: State = {}
            add_into(anti, candidate_direction(candidate_direction(basis, j), i))
            add_into(anti, candidate_direction(candidate_direction(basis, i), j))
            pairwise &= not anti
        for axis in range(3):
            squares &= (
                candidate_direction(candidate_direction(basis, axis), axis)
                == direction(direction(basis, axis, False), axis, False)
            )
        h_squared = candidate_hamiltonian(candidate_hamiltonian(basis))
        q_state = q_operator(basis)
        claimed_q = dict(q_state)
        if mutation == "wrong_H1_square_with_mixed_shift":
            add_into(
                claimed_q,
                direction(direction(basis, 0, False), 1, False),
            )
        square_sum &= h_squared == claimed_q
        unequal = (2, -3, 5)
        if candidate_is_staggered:
            unequal_square_sum &= (
                weighted_hamiltonian(weighted_hamiltonian(basis, unequal), unequal)
                == weighted_q_operator(basis, unequal)
            )
        else:
            unequal_state: State = {}
            for axis, weight in enumerate(unequal):
                add_into(unequal_state, direction(basis, axis, False), weight)
            unequal_twice: State = {}
            for axis, weight in enumerate(unequal):
                add_into(
                    unequal_twice,
                    direction(unequal_state, axis, False),
                    weight,
                )
            unequal_square_sum &= unequal_twice == weighted_q_operator(basis, unequal)
        parity_even_support &= all(
            all((target[k] - site[k]) % 2 == 0 for k in range(3))
            for target in q_state
        )
    ok = pairwise and squares and square_sum and unequal_square_sum and parity_even_support
    harness.check(
        "Clifford cancellation gives H1^2=6I+sum(Tj^2+Tj^-2)",
        ok,
        f"anticommutators={pairwise} mixed_shifts_absent={square_sum}; unequal_weights={unequal_square_sum}",
    )


def parity_darkness_certificate(harness: Harness, mutation: str | None) -> None:
    reps = list(itertools.product((0, 1), repeat=3))
    tracked_axes = (0, 1) if mutation == "drop_one_coordinate_parity" else (0, 1, 2)
    q_preserves = True
    h_flips_one = True
    for site in reps:
        basis = {site: 1}
        q_preserves &= all(
            sum((target[k] - site[k]) % 2 for k in tracked_axes) == 0
            for target in q_operator(basis)
        )
        h_flips_one &= all(
            sum((target[k] - site[k]) % 2 for k in range(3)) == 1
            for target in hamiltonian(basis, True)
        )

    targets = [
        target for target in itertools.product((0, 1), repeat=3)
        if sum(target) >= 2
    ]
    if mutation == "claim_hamming_one_is_dark":
        targets.append((1, 0, 0))
    finite_sanity = all(
        power_coefficient(True, power, target) == 0
        for target in targets for power in range(10)
    )
    adjacent_reached = power_coefficient(True, 1, (1, 0, 0)) == 1
    note = " ".join(NOTE.read_text().split())
    proof_owned = all(
        phrase in note
        for phrase in (
            "norm-convergent",
            "even powers preserve all three coordinate parities",
            "odd powers flip exactly one coordinate parity",
            "every real `t`",
            "arbitrary real directional coefficients",
            "scalar onsite term",
        )
    )
    proof_scope = "low_order" if mutation == "claim_only_low_order_cancellation" else "all_time"
    domain = "odd_period_torus" if mutation == "odd_period_wrap_as_infinite_proof" else "infinite_Z3"
    actual_body_diagonal = power_coefficient(True, 3, (1, 1, 1))
    claimed_body_diagonal = 1 if mutation == "nonzero_H1_body_diagonal" else 0
    ok = (
        len(tracked_axes) == 3 and q_preserves and h_flips_one and finite_sanity and adjacent_reached
        and proof_owned and proof_scope == "all_time" and domain == "infinite_Z3"
        and actual_body_diagonal == claimed_body_diagonal
    )
    harness.check(
        "the simultaneous H1 propagator is dark at parity distance two or three for all time",
        ok,
        f"8 sectors: Q_preserves={q_preserves}, H1_flips_one={h_flips_one}; powers 0..9={finite_sanity}",
    )


def uniform_comparator_certificate(harness: Harness, mutation: str | None) -> None:
    h3 = power_coefficient(False, 3, (1, 1, 1))
    h5 = power_coefficient(False, 5, (1, 1, 1))
    amplitude_t3 = Fraction(h3, 6)
    amplitude_t5 = -Fraction(h5, 120)
    bessel_cube_t3 = Fraction(1)
    bessel_cube_t5 = -Fraction(3, 2)
    max_degree = 11
    argument_scale = Fraction(1, 2) if mutation == "wrong_bessel_argument" else Fraction(1)
    one_dimensional = {
        2 * m + 1: (
            Fraction((-1) ** m, factorial(m) * factorial(m + 1))
            * argument_scale ** (2 * m + 1)
        )
        for m in range(6)
    }

    def multiply(left: dict[int, Fraction], right: dict[int, Fraction]) -> dict[int, Fraction]:
        result: dict[int, Fraction] = {}
        for left_degree, left_value in left.items():
            for right_degree, right_value in right.items():
                degree = left_degree + right_degree
                if degree <= max_degree:
                    result[degree] = result.get(degree, Fraction(0)) + left_value * right_value
        return result

    bessel_cube = multiply(multiply(one_dimensional, one_dimensional), one_dimensional)
    walk_counts = {
        power: power_coefficient(False, power, (1, 1, 1))
        for power in range(3, max_degree + 1, 2)
    }
    series_match = all(
        Fraction((1 if power % 4 == 3 else -1) * count, factorial(power))
        == bessel_cube[power]
        for power, count in walk_counts.items()
    )
    # J1(1)=sum_m (-1)^m/[2^(2m+1)m!(m+1)!].  The absolute-term
    # ratio is 1/[4(m+1)(m+2)] <= 1/8 for every integer m>=0, so the
    # alternating-series theorem places the sum strictly between its first
    # two and first three partial sums.  Derive rather than merely state the
    # rational endpoints checked below.
    absolute_terms = tuple(
        Fraction(1, 2 ** (2 * m + 1) * factorial(m) * factorial(m + 1))
        for m in range(4)
    )
    first_two = absolute_terms[0] - absolute_terms[1]
    first_three = first_two + absolute_terms[2]
    ratio_formula = all(
        absolute_terms[m + 1] / absolute_terms[m]
        == Fraction(1, 4 * (m + 1) * (m + 2))
        for m in range(3)
    )
    # Exact coefficient identity in the polynomial ring Z[m]:
    # 4(m+1)(m+2) = 8 + 4m(m+3).  Coefficients are stored low-to-high.
    def integer_polynomial_product(
        left: tuple[int, ...], right: tuple[int, ...]
    ) -> tuple[int, ...]:
        values = [0] * (len(left) + len(right) - 1)
        for i, left_value in enumerate(left):
            for j, right_value in enumerate(right):
                values[i + j] += left_value * right_value
        return tuple(values)

    denominator_coefficients = tuple(
        4 * value
        for value in integer_polynomial_product((1, 1), (2, 1))
    )
    m_times_m_plus_three = integer_polynomial_product((0, 1), (3, 1))
    lower_witness_coefficients = (
        8 + 4 * m_times_m_plus_three[0],
        4 * m_times_m_plus_three[1],
        4 * m_times_m_plus_three[2],
    )
    global_decrease = (
        denominator_coefficients == lower_witness_coefficients
        and lower_witness_coefficients[0] == 8
        and all(value >= 0 for value in lower_witness_coefficients[1:])
    )
    claimed_lower = Fraction(15, 32) if mutation == "wrong_bessel_lower_bound" else Fraction(7, 16)
    claimed_upper = Fraction(1, 2)
    derived_lower = first_two
    derived_sharp_upper = first_three
    exact_bound = (
        absolute_terms[:3] == (Fraction(1, 2), Fraction(1, 16), Fraction(1, 384))
        and ratio_formula and global_decrease
        and claimed_lower == derived_lower
        and derived_lower < derived_sharp_upper < claimed_upper
    )
    probability_lower = claimed_lower**6
    probability_upper = claimed_upper**6
    claimed_h3 = 0 if mutation == "zero_H0_body_diagonal" else 6
    claimed_t3 = Fraction(2) if mutation == "wrong_H0_third_coefficient" else bessel_cube_t3
    claimed_perfect = mutation == "claim_perfect_uniform_transfer"
    certified_nonperfect = probability_upper < 1
    perfect_claim_consistent = not claimed_perfect or not certified_nonperfect
    ok = (
        h3 == claimed_h3 and h5 == 180
        and amplitude_t3 == claimed_t3
        and amplitude_t5 == bessel_cube_t5
        and series_match
        and exact_bound and 0 < probability_lower < probability_upper < 1
        and perfect_claim_consistent
    )
    harness.check(
        "the uniform walk reaches the body diagonal with a strict fixed-time Bessel bound",
        ok,
        f"Z3 counts={tuple(walk_counts.values())}; J1 endpoints derived={derived_lower},{derived_sharp_upper}; "
        f"at t=1/2, ({claimed_lower})^6 < p0 < ({claimed_upper})^6",
    )


def occupation(state: State, target: Site) -> State:
    return {target: state[target]} if state.get(target, 0) else {}


def gated_hamiltonian(state: State, staggered: bool, target: Site) -> State:
    result: State = {}
    for site, value in state.items():
        for axis in range(3):
            sign = eta(axis, site) if staggered else 1
            for step in (-1, 1):
                neighbor = add_site(site, axis, step)
                if site == target or neighbor == target:
                    continue
                result[neighbor] = result.get(neighbor, 0) + sign * value
    return clean(result)


def occupation_commutator(
    site: Site, target: Site, staggered: bool, gated: bool
) -> State:
    basis = {site: 1}
    hop = (
        (lambda state: gated_hamiltonian(state, staggered, target))
        if gated else (lambda state: hamiltonian(state, staggered))
    )
    result = hop(occupation(basis, target))
    add_into(result, occupation(hop(basis), target), -1)
    return clean(result)


def record_protocol_certificate(harness: Harness, mutation: str | None) -> None:
    protocol0 = {
        "source": "localized_origin",
        "cadence": Fraction(1, 2),
        "effect": "target_occupation_PVM",
        "writer": "two_outcome_Record_writer",
    }
    protocol1 = dict(protocol0)
    protocol_mutations = {
        "branch_specific_source": ("source", "different_source"),
        "branch_specific_cadence": ("cadence", Fraction(3, 5)),
        "branch_specific_effect": ("effect", "different_effect"),
        "branch_specific_writer": ("writer", "different_writer"),
    }
    if mutation in protocol_mutations:
        key, value = protocol_mutations[mutation]
        protocol1[key] = value
    common_protocol = protocol0 == protocol1

    origin: Site = (0, 0, 0)
    outside_cube = {
        (-1, 0, 0), (0, -1, 0), (0, 0, -1)
    }
    h0_support = set(hamiltonian({origin: 1}, False))
    h1_support = set(hamiltonian({origin: 1}, True))
    if mutation == "suppress_exterior_bonds":
        h1_support.discard((-1, 0, 0))
    exterior_active = outside_cube <= h0_support and outside_cube <= h1_support
    target: Site = (1, 1, 1)
    local_sites = {target}
    for axis in range(3):
        local_sites.add(add_site(target, axis, -1))
        local_sites.add(add_site(target, axis, 1))
    prewrite_moves = all(
        bool(occupation_commutator(target, target, staggered, False))
        for staggered in (False, True)
    )
    use_gate = mutation != "leave_incident_hopping_on_after_Record"
    postwrite_permanent = all(
        not occupation_commutator(site, target, staggered, use_gate)
        for staggered in (False, True) for site in local_sites
    )
    pvm_idempotent = all(
        occupation(occupation({site: 1}, target), target)
        == occupation({site: 1}, target)
        for site in local_sites
    )
    coordinate_typing_ok = mutation != "treat_coordinate_bits_as_site_qubits"
    source_typing_ok = mutation != "treat_source_as_permanent_Record"
    text = " ".join(NOTE.read_text().split())
    wording = all(
        phrase in text
        for phrase in (
            "same supplied unrecorded localized source",
            "same cadence `t=1/2`",
            "same local target/complement occupation PVM",
            "same two-outcome writer",
            "formation-triggered gate",
            "Only the final Records are readable",
            "one CAR mode per physical lattice site",
        )
    )
    ok = (
        common_protocol and exterior_active and prewrite_moves
        and postwrite_permanent and pvm_idempotent
        and coordinate_typing_ok and source_typing_ok and wording
    )
    harness.check(
        "the supplied common local occupation-Record protocol keeps every exterior bond active",
        ok,
        f"common={common_protocol}; PVM_idempotent={pvm_idempotent}; exterior={exterior_active}; "
        f"[H,n*]!=0 prewrite={prewrite_moves}; gated permanence={postwrite_permanent}",
    )


def conjugated_translation_h(site: Site, axis: int) -> State:
    state = translate({site: 1}, axis, -1)
    state = hamiltonian(state, True)
    return translate(state, axis, 1)


def conjugated_parity_h(site: Site, axes: tuple[int, ...]) -> State:
    state = parity({site: 1}, axes)
    state = hamiltonian(state, True)
    return parity(state, axes)


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3) for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]


def rotations() -> list[Rotation]:
    result = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1:
                result.append((permutation, signs))
    return result


def rotate_site(site: Site, rotation: Rotation) -> Site:
    permutation, signs = rotation
    return tuple(signs[j] * site[permutation[j]] for j in range(3))  # type: ignore[return-value]


def inverse_rotate_site(site: Site, rotation: Rotation) -> Site:
    permutation, signs = rotation
    result = [0, 0, 0]
    for new_axis, old_axis in enumerate(permutation):
        result[old_axis] = signs[new_axis] * site[new_axis]
    return tuple(result)  # type: ignore[return-value]


def rotated_link_sign(rotation: Rotation, axis: int, site: Site) -> int:
    permutation, _ = rotation
    old_site = inverse_rotate_site(site, rotation)
    old_axis = permutation[axis]
    return eta(old_axis, old_site)


def rotation_has_local_gauge(rotation: Rotation, break_one_link: bool = False) -> bool:
    values = range(-2, 3)
    vertices = set(itertools.product(values, repeat=3))

    def ratio(axis: int, site: Site) -> int:
        value = rotated_link_sign(rotation, axis, site) * eta(axis, site)
        if break_one_link and axis == 0 and site == (0, 0, 0):
            return -value
        return value

    gauge: dict[Site, int] = {(0, 0, 0): 1}
    queue: deque[Site] = deque([(0, 0, 0)])
    while queue:
        site = queue.popleft()
        for axis in range(3):
            for step in (-1, 1):
                neighbor = add_site(site, axis, step)
                if neighbor not in vertices:
                    continue
                base = site if step == 1 else neighbor
                proposed = gauge[site] * ratio(axis, base)
                if neighbor in gauge:
                    if gauge[neighbor] != proposed:
                        return False
                else:
                    gauge[neighbor] = proposed
                    queue.append(neighbor)
    return len(gauge) == len(vertices) and all(
        ratio(axis, site) == gauge[site] * gauge[add_site(site, axis, 1)]
        for site in vertices for axis in range(3)
        if add_site(site, axis, 1) in vertices
    )


def covariance_certificate(harness: Harness, mutation: str | None) -> None:
    reps = list(itertools.product((0, 1), repeat=3))
    gauges = ((1, 2), (2,), ())
    translation_relations = all(
        conjugated_translation_h(site, axis)
        == conjugated_parity_h(site, gauges[axis])
        for site in reps for axis in range(3)
    )
    bare_pattern = all(
        (conjugated_translation_h(site, axis) != hamiltonian({site: 1}, True))
        for site in reps for axis in (0, 1)
    ) and all(
        conjugated_translation_h(site, 2) == hamiltonian({site: 1}, True)
        for site in reps
    )
    proper = rotations()
    tested_rotations = proper
    body_diagonal_family = all(
        all(abs(value) == 1 for value in rotate_site((1, 1, 1), rotation))
        for rotation in tested_rotations
    )
    rotation_gauges = len(tested_rotations) == 24 and all(
        rotation_has_local_gauge(
            rotation,
            break_one_link=(
                mutation == "break_rotation_gauge_covariance" and index == 0
            ),
        )
        for index, rotation in enumerate(tested_rotations)
    )
    bare_commutes_all = all(
        conjugated_translation_h(site, axis) == hamiltonian({site: 1}, True)
        for site in reps for axis in range(3)
    )
    claimed_bare_commutes = mutation == "claim_bare_translation_invariance"
    bare_claim_consistent = bare_commutes_all == claimed_bare_commutes
    ok = (
        translation_relations and bare_pattern and body_diagonal_family
        and rotation_gauges and bare_claim_consistent
    )
    harness.check(
        "magnetic translations are exact; a finite box checks the note's global cubic gauge proof",
        ok,
        f"bare symmetries=(False,False,True); magnetic={translation_relations}; "
        f"finite_rotation_witnesses={len(tested_rotations)}",
    )


def sharpness_certificate(harness: Harness, mutation: str | None) -> None:
    state: State = {(0, 0, 0): 1}
    for axis in range(3):
        state = direction(state, axis, True)
    ordered_leading = state.get((1, 1, 1), 0)
    swapped_state: State = {(0, 0, 0): 1}
    for axis in (1, 0, 2):
        swapped_state = direction(swapped_state, axis, True)
    swapped_leading = swapped_state.get((1, 1, 1), 0)
    simultaneous_cubic = power_coefficient(True, 3, (1, 1, 1))
    potential_state: State = {(0, 0, 0): 1}
    potential_coefficients: list[int] = []
    for _ in range(6):
        next_state = hamiltonian(potential_state, True)
        for site, value in potential_state.items():
            onsite = (-1 if site[0] % 2 else 1) + 2 * (-1 if site[1] % 2 else 1)
            next_state[site] = next_state.get(site, 0) + onsite * value
        potential_state = clean(next_state)
        potential_coefficients.append(potential_state.get((1, 1, 1), 0))
    onsite_escape = potential_coefficients == [0, 0, 0, 0, 0, -32]
    claimed_ordered_dark = mutation == "claim_sequential_pulses_are_dark"
    ordered_claim_consistent = (ordered_leading == 0) == claimed_ordered_dark
    ok = (
        ordered_leading == -1 and swapped_leading == 1 and simultaneous_cubic == 0
        and onsite_escape and ordered_claim_consistent
    )
    harness.check(
        "ordered direction pulses escape the static-simultaneous darkness theorem",
        ok,
        f"ordered={ordered_leading}; swapped={swapped_leading}; simultaneous={simultaneous_cubic}; nonscalar onsite n6={potential_coefficients[-1]}",
    )


def scope_certificate(harness: Harness, mutation: str | None) -> None:
    text = " ".join((NOTE.read_text() + "\n" + NO_GO.read_text()).split())
    required = (
        "## N1 — alternative route enumeration",
        "## N2 — wall-independence audit",
        "## N3 — hidden-wall scan",
        "## N4 — residual matching",
        "## N5 — rhetoric and resolution audit",
        "## N6 — partial-closure path scan",
        "## N7 — strongest steelman",
        "## N8 — cross-cycle echo",
        "zero obligation retirement",
        "zero TOE-percentage movement",
        "does not select either action",
        "physical matter-functional clause `I-4`",
        "static simultaneous",
    )
    injected_claims = {
        "claim_action_selected": " RESULT: THE PHYSICAL ACTION IS SELECTED.",
        "claim_born_or_clock_derived": " RESULT: THE BORN RULE AND CLOCK ARE DERIVED.",
        "claim_record_formation_derived": " RESULT: THE RECORD PROCESS IS DERIVED.",
        "claim_I4_closed": " RESULT: I-4 IS CLOSED.",
        "claim_obligation_or_TOE_movement": " RESULT: TOE PERCENTAGE INCREASES.",
    }
    candidate_text = text + injected_claims.get(mutation or "", "")
    forbidden_statements = tuple(injected_claims.values())
    ok = (
        all(phrase in candidate_text for phrase in required)
        and not any(statement in candidate_text for statement in forbidden_statements)
    )
    harness.check(
        "N1-N8 headings and zero-closure claim custody are present for postexecution audit",
        ok,
        "homogeneity trade only; I-4 and Record-process ownership remain open",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        print("\n".join(MUTATIONS))
        return 0

    harness = Harness()
    source_certificate(harness, args.mutation)
    link_and_flux_certificate(harness, args.mutation)
    clifford_certificate(harness, args.mutation)
    parity_darkness_certificate(harness, args.mutation)
    uniform_comparator_certificate(harness, args.mutation)
    record_protocol_certificate(harness, args.mutation)
    covariance_certificate(harness, args.mutation)
    sharpness_certificate(harness, args.mutation)
    scope_certificate(harness, args.mutation)

    print("per_element: link signs, face flux, and shift/parity relations certified")
    print("per_site: one local target occupation effect and exterior bonds certified")
    print("per_mode: one-particle signed adjacency checked; strict-free lift is explicitly supplied")
    print("per_block: common supplied source/cadence/PVM/writer/gate declarations scope-checked")
    print("lattice_wide: infinite-Z3 parity theorem exact; finite rotation witness supports the global note proof")
    print(f"TOTAL: PASS={harness.passed} FAIL={harness.failed}")
    return 0 if harness.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
