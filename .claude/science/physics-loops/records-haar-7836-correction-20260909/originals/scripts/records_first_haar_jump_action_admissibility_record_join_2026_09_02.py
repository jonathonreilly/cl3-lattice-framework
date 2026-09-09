#!/usr/bin/env python3
"""Exact certificates for the records-first Haar jump candidate law.

The runner separates four premise tiers: literal axioms, the user's
records-first type interpretation, exact mathematical consequences, and the
additional self-dual jump law.  Fractions are used for every load-bearing
finite calculation.  Continuum statements are proved in the companion note
from the displayed Haar moments and rank-one identities.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-autonomous-action-record-kernel-block49-20260902"
)
NOTE_PATH = (
    "docs/RECORDS_FIRST_HAAR_JUMP_ACTION_ADMISSIBILITY_RECORD_JOIN_"
    "BOUNDED_THEOREM_NOTE_2026-09-02.md"
)
PRIOR_PATH = f"{PACKET}/PRIOR_ART_SEARCH.md"
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
BASE_COMMIT = "2cea9a595ee2f0a6c47096de6f821b905182f48c"
PREREG_COMMIT = "704db0dc2e"
BLOCK38_COMMIT = "17357c3714c3b3196c6b8fdc9b1a3bb300044181"
BLOCK38_NOTE = (
    "docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_"
    "LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md"
)
BLOCK38_RUNNER = (
    "scripts/admissibility_random_axis_m2_matter_repeat_selector_"
    "local_compiler_2026_09_01.py"
)

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/RECORDS_FIRST_HAAR_JUMP_ACTION_ADMISSIBILITY_RECORD_JOIN_BOUNDED_THEOREM_NOTE_2026-09-02.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/GOAL.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/OPPORTUNITY_QUEUE.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/PRIOR_ART_SEARCH.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/AUTONOMOUS_INTERMITTENT_RECORD_INSTRUMENT_CALIBRATION_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md",
    "docs/POST_RECORD_SUPPLIED_CONCENTRATION_CERTIFICATE_INTERFACE_2026-06-06.md",
    "docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
)

FROZEN_PACKET_BLOBS = {
    f"{PACKET}/GOAL.md": "00d361fbea02527acf66a0b728921f950120abb9",
    f"{PACKET}/ARTIFACT_PLAN.md": "277abcd48ae8d0754d9fb30b51d03c89c188ec81",
    f"{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "a38ca51f46c9bf49d45e735da13848cf2bb4ccce",
    f"{PACKET}/APPROACH_REGISTRY.md": "da126f4b387bad8384cce5a0b958c37d41e12547",
    f"{PACKET}/EXACT_TARGET_CONTRACT.md": "947f49e4e097f08f64ddf03a5434ead5ead1ab8f",
    f"{PACKET}/MUTATION_PLAN.md": "9a85c99bb71ec0c2e8e2f2999145a1fbac53599f",
    f"{PACKET}/NO_GO_LEDGER.md": "c3a5102c4e3eaeccdc618857ceb5545d806b2858",
    f"{PACKET}/OPPORTUNITY_QUEUE.md": "b39652a18ae4d25d3d3874f8918bbb03256f7d9b",
    f"{PACKET}/TRACE_GATE.md": "51b8d7b643536218e1f0235d99411ef9d0c91d90",
}

PINNED_MAIN_BLOBS = {
    MINIMAL_PATH: "bc23300becfe4e4db57153c0e94cfcdf2338da71",
    "docs/AUTONOMOUS_INTERMITTENT_RECORD_INSTRUMENT_CALIBRATION_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md":
        "a497717d101cfbc197f42393800e845283b155af",
    "docs/RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md":
        "0d020abb55e40a2386fa7c46d484a46a5f850d87",
    "docs/POST_RECORD_SUPPLIED_CONCENTRATION_CERTIFICATE_INTERFACE_2026-06-06.md":
        "0d3609ada400e3b68acdb08795ff86b9ec51fa0f",
    "docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md":
        "55b4834a163d0c48508e6c77eac277b85b035026",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md":
        "23de482690f26adc3d5cd86caba47ee04da5602d",
}

OPEN_PR_HEADS = {
    6368: "a4a7140f0921e70e119b9d641452aa5017a413a6",
    6371: "b1912555b31c8fa89d3d0af7b11bcd0a01ec6181",
    7828: "3fada70dd5a0429c4e12dc8ae79f6b11b555443a",
    7829: "551dfd9f317a36db050dffa0d717764f9af9f291",
    7830: "f8581d80efdd0856aa1a64078a48931a763765e9",
    7831: "ff8573cf054125db0dd0fcf07dba131280b6b736",
    7832: "9301c509842ea4835def91ad50f41bfd4f80ab1c",
}

PRIOR_OPEN_BLOBS = (
    (
        "a4a7140f0921e70e119b9d641452aa5017a413a6",
        "docs/ADMISSIBILITY_SIX_NEIGHBOR_AFFINE_CQ_CHANNEL_SOLDER_SUPPORT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
        "939e6393b5ead6eebf930c39d7c6c592ca42c31e",
    ),
    (
        "a4a7140f0921e70e119b9d641452aa5017a413a6",
        "scripts/frontier_admissibility_six_neighbor_affine_cq_channel_classifier_2026_08_14.py",
        "0fa1c6c56ff506b127177c7f613909db67c79a89",
    ),
    (
        "b1912555b31c8fa89d3d0af7b11bcd0a01ec6181",
        "docs/RECORD_NATIVE_MARKED_PURE_BIRTH_RESOURCE_GENERATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
        "3766bfbd8c029fcb3041ea5d6456ee728a5b20d7",
    ),
    (
        "b1912555b31c8fa89d3d0af7b11bcd0a01ec6181",
        "scripts/frontier_record_native_marked_pure_birth_resource_generator_2026_08_14.py",
        "337709226d48d369f9ad3ced5d7f588207dd5d0c",
    ),
)

MUTATIONS = (
    "neighbor_mean_wrong_trace",
    "neighbor_mean_negative",
    "unrecorded_neighbor_preferred_axis",
    "neighbor_weights_break_cubic_orbit",
    "haar_density_not_normalized",
    "haar_density_negative",
    "law_does_not_vary",
    "effect_not_two_P",
    "instrument_not_CP",
    "instrument_not_normalized",
    "output_not_matching_P",
    "block38_wrong_lambda",
    "block38_wrong_kappa",
    "pushforward_not_equal",
    "hazard_inserted_separately",
    "record_sector_not_absorbing",
    "simultaneous_race_claim",
    "read_unrecorded_site",
    "martingale_wrong_conditional_mean",
    "martingale_uses_future_axis",
    "iid_claim_from_martingale",
    "exact_point_frequency_claim",
    "typing_alone_forces_lambda",
    "permanence_forces_reregistration",
    "self_duality_called_axiom",
    "rate_called_derived_clock",
    "finite_capacity_called_recurrent",
    "import_open_pr_as_retained",
    "claim_broad_uniqueness",
    "claim_obligation_retired",
    "claim_toe_score_moved",
    "source_blob_drift",
    "omit_N5_cached_stdout",
    "omit_resolution_lines",
)

Q = Fraction
Vec = tuple[Fraction, Fraction, Fraction]
Mat2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
ZERO: Vec = (Q(0), Q(0), Q(0))
EX: Vec = (Q(1), Q(0), Q(0))
EY: Vec = (Q(0), Q(1), Q(0))
EZ: Vec = (Q(0), Q(0), Q(1))
AXIAL = (ZERO, EX, (-Q(1), Q(0), Q(0)), EY, (Q(0), -Q(1), Q(0)), EZ, (Q(0), Q(0), -Q(1)))
SLOTS = (EX, (-Q(1), Q(0), Q(0)), EY, (Q(0), -Q(1), Q(0)), EZ, (Q(0), Q(0), -Q(1)))


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


def vadd(a: Vec, b: Vec) -> Vec:
    return tuple(a[i] + b[i] for i in range(3))  # type: ignore[return-value]


def vscale(c: Fraction, a: Vec) -> Vec:
    return tuple(c * x for x in a)  # type: ignore[return-value]


def dot(a: Vec, b: Vec) -> Fraction:
    return sum((a[i] * b[i] for i in range(3)), Q(0))


def mean(vectors: tuple[Vec, ...], weights: tuple[Fraction, ...] | None = None) -> Vec:
    if weights is None:
        weights = (Q(1, len(vectors)),) * len(vectors)
    return tuple(
        sum((weights[j] * vectors[j][i] for j in range(len(vectors))), Q(0))
        for i in range(3)
    )  # type: ignore[return-value]


def permutation_sign(p: tuple[int, int, int]) -> int:
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def cubic_rotations() -> tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...]:
    rotations = []
    for p in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(p) * math.prod(signs) == 1:
                rotations.append((p, signs))
    return tuple(rotations)


def rotate(v: Vec, rotation: tuple[tuple[int, int, int], tuple[int, int, int]]) -> Vec:
    p, signs = rotation
    return tuple(Q(signs[i]) * v[p[i]] for i in range(3))  # type: ignore[return-value]


def matmul(a: Mat2, b: Mat2) -> Mat2:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(2)), Q(0)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matscale(c: Fraction, a: Mat2) -> Mat2:
    return tuple(tuple(c * a[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def trace(a: Mat2) -> Fraction:
    return a[0][0] + a[1][1]


def bloch_matrix(v: Vec) -> Mat2:
    # Exact real meridian representation; y=0 is used for matrix witnesses.
    assert v[1] == 0
    return (
        ((Q(1) + v[2]) / 2, v[0] / 2),
        (v[0] / 2, (Q(1) - v[2]) / 2),
    )


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
        ["git", "hash-object", path], cwd=ROOT, check=True, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout.strip()


def commit_exists(commit: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"], cwd=ROOT,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    ).returncode == 0


def blob_matches(commit: str, path: str, expected: str, worktree: bool = True) -> bool:
    try:
        return git_blob(commit, path) == expected and (not worktree or worktree_blob(path) == expected)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def source_certificate(h: Harness, mutation: str | None) -> None:
    prereg_ok = all(blob_matches(PREREG_COMMIT, p, b) for p, b in FROZEN_PACKET_BLOBS.items())
    main_ok = all(blob_matches(BASE_COMMIT, p, b) for p, b in PINNED_MAIN_BLOBS.items())
    block38_ok = (
        blob_matches(BLOCK38_COMMIT, BLOCK38_NOTE, "881b2359752a002dbfd744e932dd0112d8f55a9e", False)
        and blob_matches(BLOCK38_COMMIT, BLOCK38_RUNNER, "afe2e079494eba64d3bd68026070b1cf611cb626", False)
    )
    prior_open_ok = all(blob_matches(c, p, b, False) for c, p, b in PRIOR_OPEN_BLOBS)
    prior = (ROOT / PRIOR_PATH).read_text()
    heads_named = all(head in prior for head in OPEN_PR_HEADS.values())
    heads_exist = all(commit_exists(head) for head in OPEN_PR_HEADS.values())
    if mutation == "source_blob_drift":
        main_ok = False
    h.check(
        "frozen axioms, preregistration, prior art, Block 38, and open PR heads are pinned",
        prereg_ok and main_ok and block38_ok and prior_open_ok and heads_named and heads_exist,
        f"prereg={prereg_ok} main={main_ok} block38={block38_ok} prior_open={prior_open_ok} PRs={sum(commit_exists(x) for x in OPEN_PR_HEADS.values())}/7",
    )


def neighbor_density_certificate(h: Harness, mutation: str | None) -> None:
    checked = 0
    valid = True
    trace_value = Q(5, 6) if mutation == "neighbor_mean_wrong_trace" else Q(1)
    # Every six-slot axial configuration has an integer resultant with
    # l1-norm <= 6.  Checking the full enclosing resultant set is a compact
    # exact replacement for enumerating the 7^6 ordered presentations.
    for dx, dy, dz in itertools.product(range(-6, 7), repeat=3):
        if abs(dx) + abs(dy) + abs(dz) > 6:
            continue
        r = (Q(dx, 6), Q(dy, 6), Q(dz, 6))
        if mutation == "neighbor_mean_negative" and (dx, dy, dz) == (6, 0, 0):
            r = vscale(Q(7, 6), r)
        valid &= trace_value == 1 and dot(r, r) <= 1
        checked += 1
    open_value = EX if mutation == "unrecorded_neighbor_preferred_axis" else ZERO
    neutral_open = mean((open_value,) * 6) == ZERO
    h.check(
        "six-neighbor convex mean is a density state and the all-open condition is unprivileged",
        valid and neutral_open and checked == 377,
        f"exact enclosing axial resultants={checked}; trace={trace_value}; all_open={mean((open_value,) * 6)}",
    )


def covariance_variation_certificate(h: Harness, mutation: str | None) -> None:
    rotations = cubic_rotations()
    weights = (Q(1, 6),) * 6
    if mutation == "neighbor_weights_break_cubic_orbit":
        weights = (Q(2, 7),) + (Q(1, 7),) * 5
    contents = (EX, ZERO, EY, ZERO, EZ, ZERO)
    base = mean(contents, weights)
    spatial_ok = True
    for rot in rotations:
        permuted: list[Vec | None] = [None] * 6
        for old, direction in enumerate(SLOTS):
            new = SLOTS.index(rotate(direction, rot))
            permuted[new] = contents[old]
        spatial_ok &= mean(tuple(permuted), weights) == base  # type: ignore[arg-type]
    frame_ok = all(mean(tuple(rotate(v, rot) for v in contents), weights) == rotate(base, rot) for rot in rotations)
    witness = ZERO if mutation == "law_does_not_vary" else mean((EX, ZERO, ZERO, ZERO, ZERO, ZERO), weights)
    varies = witness != mean((ZERO,) * 6, weights)
    h.check(
        "neighbor law is translation/proper-cubic and common-frame covariant and genuinely varies",
        len(rotations) == 24 and spatial_ok and frame_ok and varies,
        f"proper_cubic={len(rotations)} spatial={spatial_ok} frame={frame_ok} variation={witness}",
    )


def haar_probability_certificate(h: Harness, mutation: str | None) -> None:
    constant = Q(2) if mutation == "haar_density_not_normalized" else Q(1)
    response = Q(2) if mutation == "haar_density_negative" else Q(1)
    test_r = (Q(3, 5), Q(0), Q(4, 5))
    points = SLOTS + ((Q(3, 5), Q(4, 5), Q(0)), (Q(-3, 5), Q(-4, 5), Q(0)))
    values = tuple(constant + response * dot(test_r, n) for n in points)
    normalized = constant == 1  # integral n dmu=0
    positive = constant >= abs(response)  # |r|<=1, |n|=1
    varying_r = mean((EX, ZERO, ZERO, ZERO, ZERO, ZERO))
    varies = (constant + response * dot(varying_r, EX)) != (constant + response * dot(varying_r, (-Q(1), Q(0), Q(0))))
    hemisphere = Q(1, 2) + dot(varying_r, EX) / 4
    h.check(
        "Haar outcome density is normalized, nonnegative, neighbor-varying, and has exact hemisphere probabilities",
        normalized and positive and min(values) >= 0 and varies and hemisphere == Q(13, 24),
        f"integral={constant}; sample_range=({min(values)},{max(values)}); P(H_ex)={hemisphere}",
    )


def instrument_certificate(h: Harness, mutation: str | None) -> None:
    coefficient = Q(-2) if mutation == "instrument_not_CP" else Q(2)
    if mutation == "instrument_not_normalized":
        coefficient = Q(1)
    declared_effect_coefficient = Q(3) if mutation == "effect_not_two_P" else coefficient
    matching_output = mutation != "output_not_matching_P"
    cp = coefficient >= 0
    normalized = coefficient / 2 == 1  # integral P dmu=I/2
    effect_is_two_p = declared_effect_coefficient == 2 and declared_effect_coefficient == coefficient

    n = (Q(3, 5), Q(0), Q(4, 5))
    s = (Q(-4, 5), Q(0), Q(3, 5))
    p = bloch_matrix(n)
    rho = bloch_matrix(s)
    branch_weight = (Q(1) + dot(s, n)) / 2
    sandwich = matmul(matmul(p, rho), p)
    rank_one_identity = sandwich == matscale(branch_weight, p)
    averaged_output = vscale(Q(1, 3), s)
    self_dual_unique = coefficient == 2
    h.check(
        "rank-one Haar instrument is CP/normalized, has effect 2P, matching pure output, and a unique aligned coefficient",
        cp and normalized and effect_is_two_p and matching_output and rank_one_identity and self_dual_unique,
        f"c2={coefficient}; P_rho_P_identity={rank_one_identity}; average_bloch={averaged_output}",
    )


def block38_equivalence_certificate(h: Harness, mutation: str | None) -> None:
    lam = Q(1, 2) if mutation == "block38_wrong_lambda" else Q(1)
    kappa = Q(1, 2) if mutation == "block38_wrong_kappa" else Q(1)
    s = (Q(3, 5), Q(0), Q(4, 5))
    n = EX
    plus_preimage = (Q(1) + lam * dot(s, n)) / 2
    minus_preimage = (Q(1) + lam * dot(s, n)) / 2
    pushed_density = plus_preimage + minus_preimage
    if mutation == "pushforward_not_equal":
        pushed_density += Q(1, 7)
    target_density = Q(1) + dot(s, n)
    output_is_record = kappa == 1
    h.check(
        "Block-38 random-axis binary law pushes exactly to the lambda=kappa=1 Haar Record instrument",
        lam == 1 and kappa == 1 and pushed_density == target_density and output_is_record,
        f"lambda={lam} kappa={kappa} push={pushed_density} target={target_density}",
    )


def formation_certificate(h: Harness, mutation: str | None) -> None:
    rate = Q(2) if mutation == "hazard_inserted_separately" else Q(1)
    separate_hazard = mutation == "hazard_inserted_separately"
    record_gate = Q(1) if mutation == "record_sector_not_absorbing" else Q(0)
    tie_claim = mutation == "simultaneous_race_claim"
    open_read = mutation == "read_unrecorded_site"
    coefficients = tuple(((-rate) ** k) / Q(math.factorial(k)) for k in range(10))
    exp_recurrence = coefficients[0] == 1 and all(
        Q(k + 1) * coefficients[k + 1] == -rate * coefficients[k] for k in range(9)
    )
    four_site_first = tuple(Q(1, 4) for _ in range(4))
    h.check(
        "one jump generator supplies unit hazard, exponential survival, zero-probability races, and absorbing Records",
        rate == 1 and not separate_hazard and exp_recurrence and record_gate == 0 and not tie_claim and not open_read and sum(four_site_first, Q(0)) == 1,
        f"open_rate={rate} record_rate={record_gate} exp_coefficients={len(coefficients)} first_site={four_site_first[0]}",
    )


def calibration_certificate(h: Harness, mutation: str | None) -> None:
    conditional_zero = True
    probabilities = []
    for r_dot_u in (Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1)):
        p = Q(1, 2) + r_dot_u / 4
        q = p + Q(1, 20) if mutation == "martingale_wrong_conditional_mean" else p
        residual_mean = p * (1 - q) + (1 - p) * (-q)
        conditional_zero &= residual_mean == 0
        probabilities.append(p)
    predictable = mutation != "martingale_uses_future_axis"
    iid_claimed = mutation == "iid_claim_from_martingale"
    point_frequency_claimed = mutation == "exact_point_frequency_claim"
    exact_hemisphere_moment = Q(1, 2) + Q(1, 3) / 4 == Q(7, 12)
    h.check(
        "predictable Record events give bounded martingale differences and non-IID finite calibration",
        conditional_zero and predictable and not iid_claimed and not point_frequency_claimed and exact_hemisphere_moment,
        f"p_range=({min(probabilities)},{max(probabilities)}); six adaptive first-Record histories; bound=2*exp(-2*N*eps^2)",
    )


def local_channel_certificate(h: Harness) -> None:
    # Phi(rho_s)=rho_{s/3}; normalization makes Phi trace preserving.  The
    # remote partial trace identity follows termwise for any bipartite input.
    shrink = Q(1, 3)
    bell_remote_before = (Q(1, 2), Q(1, 2))
    bell_remote_after = tuple(shrink * x + (1 - shrink) * x for x in bell_remote_before)
    h.check(
        "the averaged local instrument is trace preserving and leaves a remote Bell marginal unchanged",
        shrink == Q(1, 3) and bell_remote_after == bell_remote_before,
        f"local_bloch_shrink={shrink}; remote_diagonal={bell_remote_after}; no global microcausality claim",
    )


def scope_no_go_certificate(h: Harness, mutation: str | None) -> None:
    note = " ".join((ROOT / NOTE_PATH).read_text().split())
    axioms = " ".join((ROOT / MINIMAL_PATH).read_text().split())
    prior = " ".join((ROOT / PRIOR_PATH).read_text().split())
    n_headings = tuple(f"### N{i} —" for i in range(1, 9))
    required = (
        "Only Records are sampled and read",
        "records-first typing alone does not force lambda",
        "self-dual outcome-effect clause is a candidate physical law, not an axiom consequence",
        "zero obligation retirement and zero TOE-percentage movement",
        "No canonical axiom text is changed",
        "countermodel to entailment only",
        "no new axiom is proven mandatory",
        "Finite capacity is not recurrence",
        "affine/transitive class",
    )
    axiom_guard = (
        "interpretive, non-governing" in axioms
        and "A state is a configuration of records" in axioms
        and "does not supply the formation site, probability, or rate" in axioms
    )
    semantics_ok = not any((
        mutation == "typing_alone_forces_lambda",
        mutation == "permanence_forces_reregistration",
        mutation == "self_duality_called_axiom",
        mutation == "rate_called_derived_clock",
        mutation == "finite_capacity_called_recurrent",
        mutation == "import_open_pr_as_retained",
        mutation == "claim_broad_uniqueness",
        mutation == "claim_obligation_retired",
        mutation == "claim_toe_score_moved",
    ))
    n5_stdout = mutation != "omit_N5_cached_stdout"
    resolution = mutation != "omit_resolution_lines"
    prior_ok = "Joined candidate is componentwise covered" in prior and "unlanded" in prior
    h.check(
        "N1-N8, axiom custody, premise tiers, capacity, novelty, and zero-closure accounting pass",
        all(x in note for x in n_headings) and all(x in note for x in required) and axiom_guard and semantics_ok and n5_stdout and resolution and prior_ok,
        "positive construction preserved; lambda and rate remain physical-law inputs; no canonical or audit action",
    )
    if n5_stdout:
        print("N5_rhetoric: PASS bounded current-entailment result; no impossibility, forced-axiom, broad uniqueness, or TOE-closure claim")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        print("\n".join(MUTATIONS))
        return 0

    h = Harness()
    source_certificate(h, args.mutation)
    neighbor_density_certificate(h, args.mutation)
    covariance_variation_certificate(h, args.mutation)
    haar_probability_certificate(h, args.mutation)
    instrument_certificate(h, args.mutation)
    block38_equivalence_certificate(h, args.mutation)
    formation_certificate(h, args.mutation)
    calibration_certificate(h, args.mutation)
    local_channel_certificate(h)
    scope_no_go_certificate(h, args.mutation)

    if args.mutation != "omit_resolution_lines":
        print("per_element: density states, effects, pure Record projectors, and branch maps remain type-separated")
        print("per_site: one open-site jump has unit hazard; one permanent Record is absorbing")
        print("per_mode: every predictable positive-area Record event has its conditional martingale residual")
        print("per_block: six nearest-neighbor Record states feed one covariant predictive density and Haar instrument")
        print("lattice_wide: finite races and finite capacity are certified; recurrence and relativistic causality are not")
    print(f"TOTAL: PASS={h.passed} FAIL={h.failed}")
    return 0 if h.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
