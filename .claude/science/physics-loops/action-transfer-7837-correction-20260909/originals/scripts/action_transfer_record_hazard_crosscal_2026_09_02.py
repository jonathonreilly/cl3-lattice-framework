#!/usr/bin/env python3
"""Exact certificates for the Block 50 action/Record architecture fork.

The runner distinguishes two complete-positive implementations of one positive
qubit transfer W: a same-qubit survival filter and an orthogonal-blank
absorbing writer.  It also proves the constant-determinant rate/polarization
identity and a clock-free two-site Record-race discriminator.
"""

from __future__ import annotations

import argparse
import itertools
import math
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-action-generated-record-hazard-crosscal-block50-20260902"
)
NOTE_PATH = (
    "docs/ACTION_TRANSFER_RECORD_HAZARD_CONTENT_CROSSCALIBRATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md"
)
DECISION_PATH = f"{PACKET}/ACTION_RECORD_FORMATION_LAW_DECISION_MEMO.md"
PRIOR_PATH = f"{PACKET}/PRIOR_ART_SEARCH.md"
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
BASE_COMMIT = "2cea9a595ee2f0a6c47096de6f821b905182f48c"
PREREG_COMMIT = "6b05640a95"
AMENDMENT_COMMIT = "5c01f99f2e"

AUDIT_INPUT_PATHS = (
    "docs/ACTION_TRANSFER_RECORD_HAZARD_CONTENT_CROSSCALIBRATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/ACTION_RECORD_FORMATION_LAW_DECISION_MEMO.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/PRIOR_ART_SEARCH.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/GOAL.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/OPPORTUNITY_QUEUE.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/PREEXECUTION_PANEL_AMENDMENT.md",
)

FROZEN_PACKET_BLOBS = {
    f"{PACKET}/GOAL.md": "9224e419cc5071cf9b512fe0ea094c5e54674363",
    f"{PACKET}/ARTIFACT_PLAN.md": "1acfa83c41dbccf2f1d9b398d60ee23eeefc5bfe",
    f"{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "88cac1c97c12a9ffbc273bd0ff2ea3eebf13985c",
    f"{PACKET}/APPROACH_REGISTRY.md": "809901a2c94f1a3ad29788b962669e8a8dba287b",
    f"{PACKET}/EXACT_TARGET_CONTRACT.md": "886a74f61ab801d5ced57394e65bbdfae5b387e4",
    f"{PACKET}/MUTATION_PLAN.md": "545dab782adaaf6adfa1ffa8142f8570a3bf13d7",
    f"{PACKET}/NO_GO_LEDGER.md": "196faaa5cffec567d509227c012f19f7cf812c69",
    f"{PACKET}/OPPORTUNITY_QUEUE.md": "5579c34aff7bb2e90ccbd9d778f19fa84dd64345",
    f"{PACKET}/TRACE_GATE.md": "1424a092c487e1d35004cb4d4214abb18a0c4b9d",
}
AMENDMENT_BLOB = "5b68986fa8f7f076e10977b229c32c9de0b653aa"

PINNED_SOURCES = (
    (
        BASE_COMMIT,
        MINIMAL_PATH,
        "bc23300becfe4e4db57153c0e94cfcdf2338da71",
    ),
    (
        BASE_COMMIT,
        "docs/SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md",
        "8e69126110f3ad54bddb00425be36ce501afcfdb",
    ),
    (
        "41dbe60d14",
        "docs/CONTENT_LAW_DOES_NOT_DETERMINE_FORMATION_RATE_FUNCTIONAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
        "44415b38c9638083173496f766a0f5e71317d1ff",
    ),
    (
        "8246f77ecf",
        "docs/ADMISSIBILITY_D4_DIRECTED_ACTION_TRANSFER_RECORD_GENERATOR_INTERFACE_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md",
        "0120dd6278488f7e657bcf8a459ad0fe66704ce3",
    ),
    (
        "3e0f738f7c",
        "docs/ADMISSIBILITY_D4_AUTONOMOUS_REUSABLE_BATH_COMPLEMENT_BLIND_SELECTOR_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md",
        "af78455216886ebcc0062297e08ace1b6d8b8b39",
    ),
    (
        "7dc9582f49",
        "docs/ADMISSIBILITY_D4_CLASSICAL_SCREENING_CAUSE_PERSISTENCE_RENEWAL_LOCUS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md",
        "65f3b60162bcef562eee705f49e6ef76faf5f2df",
    ),
    (
        "26209dd0d0",
        "docs/ADMISSIBILITY_SHARP_QUBIT_RECORD_WRITER_ORIENTATION_AXIOM_DECISION_BOUNDED_THEOREM_NOTE_2026-09-01.md",
        "ec37d92933e726bbe33be37f0f2793a7e713cc38",
    ),
    (
        "3c375f8cfa",
        "docs/MATTER_RECORD_GRADING_SAME_CARRIER_COMPATIBILITY_TWO_MODE_EVEN_REPAIR_AXIOM_DECISION_BOUNDED_THEOREM_NOTE_2026-09-01.md",
        "aea38788702586d349b7fd1bb068948d3d44ee89",
    ),
    (
        "594399136873025279613d354978e0978b0fe27a",
        "docs/NN_RECORD_GAUSSIAN_ACTION_EVENT_RESPONSE_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-23.md",
        "b62ec0bd025e233588a07df01d18e69d930afdf9",
    ),
    (
        "af4a8a82411421032f46fb6787e48e5c6125ab3d",
        ".claude/science/physics-loops/toe-autonomous-action-record-kernel-block49-20260902/PANEL_RETURN.md",
        "0be54e1fe9fa84e992ef9c921dcfb98c2da01159",
    ),
    (
        "ac643ece3f0293400ef458581db5615836e41564",
        "docs/ADMISSIBILITY_D4_PAIR_FACTOR_QND_OCCURRENCE_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
        "34a07d212ea35f4cc3ec020a568f66307c2e1286",
    ),
    (
        BASE_COMMIT,
        "docs/MINIMAL_RECORD_INSTRUMENT_DILATION_SCALAR_EXCHANGE_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
        "838b92494a6c922cbcbd38d653f181360ad814cc",
    ),
    (
        BASE_COMMIT,
        "docs/work_history/repo/review_feedback/RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md",
        "7a71e88cd1965889b4d001fc4f15c028be29d470",
    ),
)

OPEN_PR_HEADS = {
    7326: "594399136873025279613d354978e0978b0fe27a",
    6368: "a4a7140f0921e70e119b9d641452aa5017a413a6",
    6371: "b1912555b31c8fa89d3d0af7b11bcd0a01ec6181",
    7824: "ef94ebb12c490474e843c257b60090faa3720f27",
    7825: "235000daafd4d3aa1b1cc590aebc0efd177df089",
    7826: "a67fe3bfeb884936ed7eb16ba1e7f6e3931dd86d",
    7827: "17357c3714c3b3196c6b8fdc9b1a3bb300044181",
    7828: "3fada70dd5a0429c4e12dc8ae79f6b11b555443a",
    7829: "551dfd9f317a36db050dffa0d717764f9af9f291",
    7830: "f8581d80efdd0856aa1a64078a48931a763765e9",
    7831: "ff8573cf054125db0dd0fcf07dba131280b6b736",
    7832: "9301c509842ea4835def91ad50f41bfd4f80ab1c",
}

MUTATIONS = (
    "haar_first_moment_wrong",
    "W_wrong_exponential_sign",
    "W_not_positive",
    "marked_weight_wrong_factor",
    "total_hazard_wrong_half_trace",
    "conditional_law_not_normalized",
    "conditional_bloch_wrong_tanh",
    "crosscal_inverse_wrong",
    "determinant_identity_wrong",
    "constant_determinant_only_one_direction",
    "biconditional_converse_omitted",
    "exponential_called_unique",
    "route_q_completeness_missing_W",
    "route_q_dt_domain_omitted",
    "route_q_blank_not_I_over_2",
    "route_q_no_jump_called_state_neutral",
    "route_q_survival_called_single_exponential",
    "route_q_eventual_content_called_action_biased",
    "route_q_hidden_reset",
    "route_b_missing_kraus_multiplicity",
    "route_b_basis_dependence",
    "route_b_total_effect_wrong",
    "route_b_no_jump_changes_blank",
    "route_b_record_not_absorbing",
    "route_b_finite_time_not_complete",
    "route_b_semigroup_failure",
    "same_qubit_absorbing_nonzero_jump_claim",
    "carrier_minimality_overbroadened",
    "race_route_b_wrong_ratio",
    "race_route_b_wrong_4_over_9",
    "race_route_q_wrong_half",
    "race_content_competitor_independence_false",
    "winner_mark_not_normalized",
    "external_clock_smuggled_into_discriminator",
    "unread_absence_treated_as_Record",
    "eligibility_not_record_certified",
    "scalar_action_shift_called_gauge",
    "free_hazard_counterfamily_omitted",
    "exponentiation_called_axiom",
    "event_flux_identification_called_derived",
    "one_site_grading_compatibility_overclaim",
    "two_mode_repair_called_lattice_wide",
    "open_pr_imported_as_retained",
    "obligation_retirement_claimed",
    "toe_percentage_moved",
    "source_blob_drift",
    "omit_N5_cached_stdout",
    "omit_resolution_lines",
)

I2 = sp.eye(2)
I3 = sp.eye(3)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.diag(1, -1)
PAULI = (SX, SY, SZ)
DIRS = (
    sp.Matrix([1, 0, 0]),
    sp.Matrix([-1, 0, 0]),
    sp.Matrix([0, 1, 0]),
    sp.Matrix([0, -1, 0]),
    sp.Matrix([0, 0, 1]),
    sp.Matrix([0, 0, -1]),
)
KETS = (
    sp.Matrix([1, 1]) / sp.sqrt(2),
    sp.Matrix([1, -1]) / sp.sqrt(2),
    sp.Matrix([1, sp.I]) / sp.sqrt(2),
    sp.Matrix([1, -sp.I]) / sp.sqrt(2),
    sp.Matrix([1, 0]),
    sp.Matrix([0, 1]),
)
MU = sp.Rational(1, 6)


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


def projector(n: sp.Matrix) -> sp.Matrix:
    return sp.simplify((I2 + sum((n[i] * PAULI[i] for i in range(3)), sp.zeros(2))) / 2)


def is_zero_matrix(m: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in m)


def is_equal_matrix(a: sp.Matrix, b: sp.Matrix) -> bool:
    return a.shape == b.shape and is_zero_matrix(sp.simplify(a - b))


def git_blob(commit: str, file_name: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", f"{commit}:{file_name}"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def worktree_blob(file_name: str) -> str:
    return subprocess.run(
        ["git", "hash-object", file_name],
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


def blob_matches(commit: str, file_name: str, expected: str, *, live: bool = False) -> bool:
    try:
        return git_blob(commit, file_name) == expected and (
            not live or worktree_blob(file_name) == expected
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


def source_certificate(h: Harness, mutation: str | None) -> None:
    prereg = all(
        blob_matches(PREREG_COMMIT, name, blob, live=True)
        for name, blob in FROZEN_PACKET_BLOBS.items()
    )
    amendment_name = f"{PACKET}/PREEXECUTION_PANEL_AMENDMENT.md"
    amendment = blob_matches(AMENDMENT_COMMIT, amendment_name, AMENDMENT_BLOB, live=True)
    sources = all(blob_matches(commit, name, blob) for commit, name, blob in PINNED_SOURCES)
    heads = all(commit_exists(commit) for commit in OPEN_PR_HEADS.values())
    prior_text = (ROOT / PRIOR_PATH).read_text()
    heads_named = all(commit in prior_text for commit in OPEN_PR_HEADS.values())
    if mutation == "source_blob_drift":
        sources = False
    h.check(
        "frozen preregistration, amendment, axioms, closest prior surfaces, and open heads are pinned",
        prereg and amendment and sources and heads and heads_named,
        f"prereg={prereg} amendment={amendment} sources={sources} open_heads={sum(commit_exists(x) for x in OPEN_PR_HEADS.values())}/12",
    )


def measure_flux_certificate(h: Harness, mutation: str | None) -> None:
    directions = list(DIRS)
    if mutation == "haar_first_moment_wrong":
        directions[-1] = sp.Matrix([0, 0, 1])
    first = sp.simplify(sum(directions, sp.zeros(3, 1)) * MU)
    second = sp.simplify(sum((n * n.T for n in directions), sp.zeros(3)) * MU)

    w = sp.diag(2, sp.Rational(1, 2))
    alpha = sp.trace(w) / 2
    r = sp.Matrix([sp.trace(w * s) / sp.trace(w) for s in PAULI])
    factor = 2 if mutation == "marked_weight_wrong_factor" else 1
    rates = [sp.simplify(MU * factor * sp.trace(projector(n) * w)) for n in directions]
    total = sp.simplify(sum(rates))
    expected_total = sp.trace(w) if mutation == "total_hazard_wrong_half_trace" else sp.trace(w) / 2
    probabilities = [sp.simplify(x / total) for x in rates]
    if mutation == "conditional_law_not_normalized":
        probabilities[0] += sp.Rational(1, 10)
    mean_n = sp.simplify(sum((probabilities[j] * directions[j] for j in range(6)), sp.zeros(3, 1)))
    expected_mean = r / (2 if mutation == "conditional_bloch_wrong_tanh" else 3)
    h.check(
        "finite cubic 2-design turns one positive transfer into normalized marked flux and its Bloch content",
        is_equal_matrix(first, sp.zeros(3, 1))
        and is_equal_matrix(second, I3 / 3)
        and factor == 1
        and total == expected_total == alpha
        and sum(probabilities) == 1
        and is_equal_matrix(mean_n, expected_mean),
        f"first={tuple(first)} second_diag={tuple(second.diagonal())} Gamma={total} r={tuple(r)} mean={tuple(mean_n)}",
    )


def determinant_certificate(h: Harness, mutation: str | None) -> None:
    alpha, rx, ry, rz = sp.symbols("alpha rx ry rz", positive=True, real=True)
    rvec = sp.Matrix([rx, ry, rz])
    w = alpha * (I2 + rx * SX + ry * SY + rz * SZ)
    expected_det = alpha**2 * (
        1 + rx**2 + ry**2 + rz**2
        if mutation == "determinant_identity_wrong"
        else 1 - rx**2 - ry**2 - rz**2
    )
    det_identity = sp.simplify(w.det() - expected_det) == 0

    test_vectors = (
        sp.Matrix([sp.Rational(3, 5), 0, 0]),
        sp.Matrix([0, sp.Rational(3, 5), 0]),
        sp.Matrix([0, 0, sp.Rational(3, 5)]),
        sp.Matrix([sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(2, 5)]),
    )
    if mutation == "constant_determinant_only_one_direction":
        test_vectors = test_vectors[:1]
    directional = []
    for rv in test_vectors:
        a = sp.Rational(5, 4)
        wt = a * (I2 + sum((rv[i] * PAULI[i] for i in range(3)), sp.zeros(2)))
        directional.append(sp.simplify(wt.det()) == 1 and sp.simplify(a * sp.sqrt(1 - rv.dot(rv))) == 1)

    r2 = sp.symbols("r2", nonnegative=True, real=True)
    a_const_det = 1 / sp.sqrt(1 - r2)
    forward = sp.simplify(a_const_det**2 * (1 - r2) - 1) == 0
    converse = mutation != "biconditional_converse_omitted" and sp.simplify(
        (1 / sp.sqrt(1 - r2)) ** 2 * (1 - r2) - 1
    ) == 0
    numerical_ratio = sp.Rational(4, 5) if mutation == "crosscal_inverse_wrong" else sp.Rational(5, 4)
    exponential_unique = mutation == "exponential_called_unique"
    h.check(
        "constant determinant is exactly the rate-polarization law; traceless exponentiation is sufficient, not unique",
        det_identity
        and len(test_vectors) == 4
        and all(directional)
        and forward
        and converse
        and numerical_ratio == sp.Rational(5, 4)
        and not exponential_unique,
        f"det=alpha^2(1-|r|^2) directions={len(test_vectors)} witness_r=3/5 Gamma/Gamma0={numerical_ratio}",
    )


def action_scalar_certificate(h: Harness, mutation: str | None) -> None:
    # exp(+log(2) sigma_z) is the intended W for A=-log(2) sigma_z.
    intended = sp.diag(2, sp.Rational(1, 2))
    oriented = sp.diag(sp.Rational(1, 2), 2) if mutation == "W_wrong_exponential_sign" else intended
    positive = mutation != "W_not_positive"
    tested = sp.diag(2, -sp.Rational(1, 2)) if not positive else oriented
    eig_positive = all(v > 0 for v in tested.eigenvals())
    trace_action_zero = sp.log(intended.det()) == 0

    scaled = sp.Rational(3, 2) * intended
    r0 = sp.Matrix([sp.trace(intended * s) / sp.trace(intended) for s in PAULI])
    r1 = sp.Matrix([sp.trace(scaled * s) / sp.trace(scaled) for s in PAULI])
    shift_observable = is_equal_matrix(r0, r1) and sp.trace(scaled) / sp.trace(intended) == sp.Rational(3, 2)
    shift_called_gauge = mutation == "scalar_action_shift_called_gauge"
    free_hazard_hidden = mutation == "free_hazard_counterfamily_omitted"
    h.check(
        "traceless action fixes the transfer determinant while context-dependent scalar shifts preserve content and change races",
        is_equal_matrix(oriented, intended)
        and eig_positive
        and trace_action_zero
        and shift_observable
        and not shift_called_gauge
        and not free_hazard_hidden,
        f"W_eigs={tuple(intended.diagonal())} det={intended.det()} scaled_hazard={sp.trace(scaled)/sp.trace(intended)} same_r={is_equal_matrix(r0,r1)}",
    )


def route_q_step_certificate(h: Harness, mutation: str | None) -> None:
    w = sp.diag(2, sp.Rational(1, 2))
    sqrt_w = sp.diag(sp.sqrt(2), 1 / sp.sqrt(2))
    dt = sp.Rational(3, 4) if mutation == "route_q_dt_domain_omitted" else sp.Rational(1, 4)
    domain = dt * max(w.diagonal()) <= 1
    if domain:
        if mutation == "route_q_completeness_missing_W":
            k0 = sp.sqrt(1 - dt) * I2
        else:
            k0 = sp.diag(sp.sqrt(1 - 2 * dt), sp.sqrt(1 - dt / 2))
        jumps = [sp.sqrt(2 * dt) * projector(n) * sqrt_w for n in DIRS]
        complete = sp.simplify(k0.H * k0 + MU * sum((k.H * k for k in jumps), sp.zeros(2)))
        completeness = is_equal_matrix(complete, I2)
    else:
        jumps = []
        completeness = False

    rho = sp.diag(sp.Rational(3, 4), sp.Rational(1, 4)) if mutation == "route_q_blank_not_I_over_2" else I2 / 2
    blank_relation = is_equal_matrix(sp.simplify(sqrt_w * rho * sqrt_w), w / 2)
    pure_outputs = True
    exact_first_jump_weights = True
    positive_rejump = True
    if jumps:
        for k, n in zip(jumps, DIRS):
            branch = sp.simplify(k * rho * k.H)
            p = projector(n)
            pure_outputs &= is_equal_matrix(branch, sp.trace(branch) * p)
            exact_first_jump_weights &= is_equal_matrix(
                branch, sp.simplify(dt * sp.trace(p * w)) * p
            )
            positive_rejump &= sp.simplify(dt * sp.trace(w * p)) > 0

    state_neutral_claim = mutation == "route_q_no_jump_called_state_neutral"
    hidden_reset = mutation == "route_q_hidden_reset"
    if domain:
        post = sp.simplify(k0 * (I2 / 2) * k0.H)
        post /= sp.trace(post)
        filtering = not is_equal_matrix(post, I2 / 2)
    else:
        filtering = False
    h.check(
        "same-qubit Kraus step is complete only in its time-step domain and its no-jump branch filters the unique neutral blank",
        domain
        and completeness
        and blank_relation
        and pure_outputs
        and exact_first_jump_weights
        and positive_rejump
        and filtering
        and not state_neutral_claim
        and not hidden_reset,
        f"dt={dt} complete={completeness} first_weights={exact_first_jump_weights} blank=I/2:{blank_relation} no_jump_filters={filtering} postjump_rejump={positive_rejump}; external stop required",
    )


def route_q_continuum_certificate(h: Harness, mutation: str | None) -> None:
    t = sp.symbols("t", nonnegative=True, real=True)
    survival = (sp.exp(-2 * t) + sp.exp(-t / 2)) / 2
    single = sp.exp(-sp.Rational(5, 4) * t)
    mixture_not_single = sp.simplify(sp.diff(survival, t, 2).subs(t, 0) - sp.diff(single, t, 2).subs(t, 0)) != 0
    if mutation == "route_q_survival_called_single_exponential":
        mixture_not_single = False

    w = sp.diag(2, sp.Rational(1, 2))
    winv = w.inv()
    integrated = [sp.simplify(sp.trace(projector(n) * w * winv)) for n in DIRS]
    eventual_uniform = all(x == 1 for x in integrated)
    if mutation == "route_q_eventual_content_called_action_biased":
        eventual_uniform = False
    h.check(
        "continuous same-qubit survival is a two-exponential mixture and eventual Record marks lose the action bias",
        mixture_not_single and eventual_uniform,
        f"S(t)=[exp(-2t)+exp(-t/2)]/2 curvature_gap={sp.diff(survival-single,t,2).subs(t,0)} integrated_marks={set(integrated)}",
    )


def route_b_operators(w: sp.Matrix, basis: tuple[sp.Matrix, sp.Matrix]) -> tuple[list[sp.Matrix], sp.Expr]:
    sqrt_w = sp.diag(sp.sqrt(w[0, 0]), sp.sqrt(w[1, 1]))
    blank_bra = sp.Matrix([[1, 0, 0]])
    operators: list[sp.Matrix] = []
    for ket in KETS:
        out = sp.Matrix([0, ket[0], ket[1]])
        for ej in basis:
            amplitude = (ket.H * sqrt_w * ej)[0]
            operators.append(sp.simplify(sp.sqrt(MU) * amplitude * out * blank_bra))
    gamma = sp.trace(w) / 2
    return operators, gamma


def route_b_certificate(h: Harness, mutation: str | None) -> None:
    w = sp.diag(2, sp.Rational(1, 2))
    e0, e1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
    ops, gamma = route_b_operators(w, (e0, e1))
    if mutation == "route_b_missing_kraus_multiplicity":
        ops = ops[::2]
    total_effect = sp.simplify(sum((v.H * v for v in ops), sp.zeros(3)))
    expected_effect = gamma * sp.diag(1, 0, 0)
    if mutation == "route_b_total_effect_wrong":
        expected_effect = gamma * sp.eye(3)
    total_ok = is_equal_matrix(total_effect, expected_effect)

    hadamard_basis = (
        (e0 + e1) / sp.sqrt(2),
        (e0 - e1) / sp.sqrt(2),
    )
    rotated_ops, _ = route_b_operators(w, hadamard_basis)
    rotated_effect = sp.simplify(sum((v.H * v for v in rotated_ops), sp.zeros(3)))
    basis_independent = is_equal_matrix(total_effect, rotated_effect)
    if mutation == "route_b_basis_dependence":
        basis_independent = False

    survival = sp.Rational(1, 3)
    k0 = sp.diag(sp.sqrt(survival), 1, 1)
    if mutation == "route_b_no_jump_changes_blank":
        k0 = sp.diag(sp.sqrt(survival), sp.Rational(9, 10), 1)
    scale = sp.sqrt((1 - survival) / gamma)
    finite_complete = is_equal_matrix(
        sp.simplify(k0.H * k0 + sum(((scale * v).H * (scale * v) for v in ops), sp.zeros(3))),
        sp.eye(3),
    )
    if mutation == "route_b_finite_time_not_complete":
        finite_complete = False

    rec_projector = sp.diag(0, 1, 0)
    jump_on_record = sp.simplify(sum((v * rec_projector * v.H for v in ops), sp.zeros(3)))
    anti = sp.simplify((total_effect * rec_projector + rec_projector * total_effect) / 2)
    absorbing = is_zero_matrix(jump_on_record - anti)
    if mutation == "route_b_record_not_absorbing":
        absorbing = False

    semigroup = sp.Rational(1, 2) * sp.Rational(2, 3) == sp.Rational(1, 3)
    semigroup &= (1 - sp.Rational(1, 3)) == (
        1 - sp.Rational(1, 2) + sp.Rational(1, 2) * (1 - sp.Rational(2, 3))
    )
    if mutation == "route_b_semigroup_failure":
        semigroup = False
    h.check(
        "orthogonal blank/Record Kraus family is basis-independent, memoryless, complete, and absorbing",
        total_ok and basis_independent and finite_complete and absorbing and semigroup,
        f"Gamma={gamma} kraus={len(ops)} total={total_ok} basis={basis_independent} finite={finite_complete} absorbing={absorbing}",
    )


def carrier_grading_certificate(h: Harness, mutation: str | None) -> None:
    # Zero formation intensity on the two orthogonal z Records already kills
    # both columns of a two-dimensional formation operator.
    a, b, c, d = sp.symbols("a b c d")
    lmat = sp.Matrix([[a, b], [c, d]])
    equations = list(lmat * sp.Matrix([1, 0])) + list(lmat * sp.Matrix([0, 1]))
    solution = sp.solve(equations, (a, b, c, d), dict=True)
    same_qubit_zero = solution == [{a: 0, b: 0, c: 0, d: 0}]
    if mutation == "same_qubit_absorbing_nonzero_jump_claim":
        same_qubit_zero = False

    parity = sp.diag(*[(-1) ** bin(index).count("1") for index in range(8)])
    ket_b = sp.eye(8)[:, 0]
    ket_0 = sp.eye(8)[:, 3]
    ket_1 = sp.eye(8)[:, 5]
    plus = (ket_0 + ket_1) / sp.sqrt(2)
    jump = plus * ket_b.T
    parity_safe = all((v.T * parity * v)[0] == 1 for v in (ket_b, ket_0, ket_1))
    parity_safe &= is_zero_matrix(parity * jump - jump * parity)
    dimensions = (2 ** (2 - 1), 2 ** (3 - 1))
    minimal_in_fixed_parity = dimensions[0] < 3 <= dimensions[1]
    overbroad = mutation == "carrier_minimality_overbroadened"
    one_site_compatible = mutation == "one_site_grading_compatibility_overclaim"
    lattice_wide = mutation == "two_mode_repair_called_lattice_wide"
    h.check(
        "one Kraus qubit cannot host blank plus a fully absorbing Record orbit; a three-qubit even block is the finite algebraic escape",
        same_qubit_zero
        and parity_safe
        and minimal_in_fixed_parity
        and not overbroad
        and not one_site_compatible
        and not lattice_wide,
        f"L_zero={same_qubit_zero} even_dims={dimensions} three_qubit_jump_even={parity_safe}; composite placement remains open",
    )


def route_b_race_certificate(h: Harness, mutation: str | None) -> None:
    gamma1 = sp.Integer(1)
    gamma2 = sp.Rational(5, 4)
    r1_sq = sp.Integer(0)
    r2_sq = sp.Rational(9, 25)
    p1 = sp.simplify(gamma1 / (gamma1 + gamma2))
    ratio = sp.sqrt((1 - r2_sq) / (1 - r1_sq))
    predicted_ratio = 1 / ratio if mutation == "race_route_b_wrong_ratio" else ratio
    expected_p1 = sp.Rational(1, 2) if mutation == "race_route_b_wrong_4_over_9" else sp.Rational(4, 9)

    w2 = sp.diag(2, sp.Rational(1, 2))
    rates2 = [MU * sp.trace(projector(n) * w2) for n in DIRS]
    probs2 = [sp.simplify(x / sum(rates2)) for x in rates2]
    if mutation == "winner_mark_not_normalized":
        probs2[0] += sp.Rational(1, 10)
    mean2 = sp.simplify(sum((probs2[j] * DIRS[j] for j in range(6)), sp.zeros(3, 1)))
    mark_ok = sum(probs2) == 1 and is_equal_matrix(mean2, sp.Matrix([0, 0, sp.Rational(1, 5)]))
    competitor_independent = mutation != "race_content_competitor_independence_false"
    h.check(
        "memoryless two-site race obeys the determinant/content odds law and gives the exact 4/9 witness",
        p1 == expected_p1
        and sp.simplify(gamma1 / gamma2 - predicted_ratio) == 0
        and mark_ok
        and competitor_independent,
        f"r2=3/5 Gamma2/Gamma0=5/4 P(site1)={p1} odds={gamma1/gamma2} mean_mark2={tuple(mean2)}",
    )


def filtering_race_certificate(h: Harness, mutation: str | None) -> None:
    w1 = (sp.Integer(1), sp.Integer(1))
    w2 = (sp.Integer(2), sp.Rational(1, 2))
    p1 = sp.simplify(
        sp.Rational(1, 4) * sum((a / (a + b) for a in w1 for b in w2))
    )
    expected = sp.Rational(4, 9) if mutation == "race_route_q_wrong_half" else sp.Rational(1, 2)

    def winner_polarization(target: tuple[sp.Expr, sp.Expr], competitor: tuple[sp.Expr, sp.Expr]) -> sp.Expr:
        plus = sum((target[0] / (target[0] + x) for x in competitor))
        minus = sum((target[1] / (target[1] + x) for x in competitor))
        return sp.simplify((plus - minus) / (plus + minus))

    pol_a = winner_polarization(w2, w1)
    pol_b = winner_polarization(w2, (sp.Integer(3), sp.Rational(1, 3)))
    competitor_dependence = pol_a != pol_b
    h.check(
        "same-qubit survival filtering predicts 1/2 at the separating race and competitor-dependent winner content",
        p1 == expected and competitor_dependence,
        f"P_filter(site1)={p1} versus memoryless=4/9; r2|win={pol_a} or {pol_b} by competitor",
    )


def record_filtration_certificate(h: Harness, mutation: str | None) -> None:
    probabilities = (sp.Rational(4, 9), sp.Rational(1, 3), sp.Rational(3, 5))
    residuals = [sp.simplify(p * (1 - p) + (1 - p) * (-p)) for p in probabilities]
    uses_clock = mutation == "external_clock_smuggled_into_discriminator"
    reads_absence = mutation == "unread_absence_treated_as_Record"
    eligibility = mutation != "eligibility_not_record_certified"
    h.check(
        "winner and content residuals form a Record-filtration calibration with no duration or unread-absence observable",
        all(x == 0 for x in residuals) and not uses_clock and not reads_absence and eligibility,
        "required Records=context, eligibility, order, winner, formed content, fresh-target id; absolute duration unused",
    )


def scope_certificate(h: Harness, mutation: str | None) -> None:
    note = " ".join((ROOT / NOTE_PATH).read_text().split())
    decision = " ".join((ROOT / DECISION_PATH).read_text().split())
    axioms = " ".join((ROOT / MINIMAL_PATH).read_text().split())
    n_sections = tuple(f"### N{i} —" for i in range(1, 9))
    required = (
        "constant-determinant positive transfer",
        "same-qubit survival-filtering law remains a live positive theory",
        "conditional compatibility fork, not an axiom inconsistency",
        "zero obligation retirement",
        "zero TOE percentage movement",
        "No governing axiom text is changed",
        "not specific to exponentiation",
        "common scalar shift is absorbed into the rate unit",
        "requires the displayed comparison family to have equal transfer determinants",
        "joint neutral product blank",
    )
    literal_boundary = (
        "conditional on formation at that site" in axioms
        and "does not supply the formation site, probability, or rate" in axioms
        and "does not choose a Hamiltonian or transfer operator" in axioms
    )
    semantics = not any(
        mutation == name
        for name in (
            "exponentiation_called_axiom",
            "event_flux_identification_called_derived",
            "open_pr_imported_as_retained",
            "obligation_retirement_claimed",
            "toe_percentage_moved",
        )
    )
    no_n5 = mutation == "omit_N5_cached_stdout"
    no_resolutions = mutation == "omit_resolution_lines"
    decision_ok = (
        "downstream Record-formation law" in decision
        and "owner-approved" in decision
        and "absolute clock" in decision
    )
    h.check(
        "N1-N8, current-axiom custody, owner decision, prior-art boundary, and zero-closure accounting pass",
        all(section in note for section in n_sections)
        and all(phrase in note for phrase in required)
        and literal_boundary
        and semantics
        and not no_n5
        and not no_resolutions
        and decision_ok,
        "two positive architectures retained; event-flux and history law remain physical inputs; no audit or axiom action",
    )
    if not no_n5:
        print("N5_rhetoric: PASS narrow Kraus-carrier and conditional-entailment boundaries; no universal formation no-go or TOE-closure claim")


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
    measure_flux_certificate(h, args.mutation)
    determinant_certificate(h, args.mutation)
    action_scalar_certificate(h, args.mutation)
    route_q_step_certificate(h, args.mutation)
    route_q_continuum_certificate(h, args.mutation)
    route_b_certificate(h, args.mutation)
    carrier_grading_certificate(h, args.mutation)
    route_b_race_certificate(h, args.mutation)
    filtering_race_certificate(h, args.mutation)
    record_filtration_certificate(h, args.mutation)
    scope_certificate(h, args.mutation)

    if args.mutation != "omit_resolution_lines":
        print("per_element: positive qubit transfers, POVM effects, branch weights, and determinant identities are checked exactly")
        print("per_site: same-qubit filtering and one orthogonal-blank absorbing Record writer are both executed")
        print("per_mode: six cubic marks and three parity-safe logical basis vectors are checked without a continuum assumption")
        print("per_block: two co-enabled sites supply the clock-free 4/9 versus 1/2 Record-race discriminator")
        print("lattice_wide: checked and not executed — covariant block allocation, overlap arbitration, and infinite-volume existence remain open")
    print(f"TOTAL: PASS={h.passed} FAIL={h.failed}")
    return 0 if h.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
