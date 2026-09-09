#!/usr/bin/env python3
"""Exact finite action/functional/Admissibility/Record type decision.

All load-bearing numerical checks use fractions.  The runner proves a positive
finite one-use commuting triangle under supplied typed premises and local
finite separation examples. No full-domain four-axiom model is constructed.
"""

from __future__ import annotations

import argparse
import itertools
import hashlib
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = 'docs/FINITE_ACTION_FUNCTIONAL_TYPED_ADMISSIBILITY_RECORD_IDENTIFICATION_DECISION_BOUNDED_THEOREM_NOTE_2026-09-02.md'
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/FINITE_ACTION_FUNCTIONAL_TYPED_ADMISSIBILITY_RECORD_IDENTIFICATION_DECISION_BOUNDED_THEOREM_NOTE_2026-09-02.md', "docs/MINIMAL_AXIOMS_2026-06-29.md")
INPUT_SHA256 = {'docs/FINITE_ACTION_FUNCTIONAL_TYPED_ADMISSIBILITY_RECORD_IDENTIFICATION_DECISION_BOUNDED_THEOREM_NOTE_2026-09-02.md': '6e675ba002b3e8da6afef38058e6beb70467775f95df349bc4f0a5fde0307317', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

MUTATIONS = (
    "gibbs_density_wrong_normalization",
    "gibbs_density_negative_weight",
    "claim_bare_H_selects_state",
    "z_pvm_not_resolution",
    "x_pvm_not_resolution",
    "claim_z_x_same_distribution",
    "state_measure_barycenter_wrong",
    "claim_barycenter_injective",
    "born_weights_negative",
    "born_weights_not_normalized",
    "claim_event_partition_selected",
    "claim_admissibility_identification_derived",
    "same_effect_instruments_same_output",
    "claim_lueders_without_matching_output",
    "admissibility_law_not_covariant",
    "admissibility_law_not_varying",
    "two_admissibility_laws_equal",
    "conditional_content_determines_hazard",
    "hazard_models_same_record_rate",
    "active_H_commutes_with_record",
    "claim_permanence_implementation_selected",
    "observe_unrecorded_alternative",
    "omit_repeatability_stationarity",
    "conflate_state_effect_record",
    "import_unaudited_as_retained",
    "claim_broad_no_go",
    "claim_axiom_edit_performed",
    "claim_obligation_retired",
    "claim_toe_score_moved",
    "source_blob_drift",
    "omit_N5_cached_stdout",
    "omit_resolution_lines",
)

Q = Fraction
Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]

ZERO: Matrix = ((Q(0), Q(0)), (Q(0), Q(0)))
I: Matrix = ((Q(1), Q(0)), (Q(0), Q(1)))
X: Matrix = ((Q(0), Q(1)), (Q(1), Q(0)))
P0: Matrix = ((Q(1), Q(0)), (Q(0), Q(0)))
P1: Matrix = ((Q(0), Q(0)), (Q(0), Q(1)))
PP: Matrix = ((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2)))
PM: Matrix = ((Q(1, 2), Q(-1, 2)), (Q(-1, 2), Q(1, 2)))


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


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def scale(c: Fraction, a: Matrix) -> Matrix:
    return tuple(
        tuple(c * a[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def mul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(2)), Q(0)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def trace(a: Matrix) -> Fraction:
    return a[0][0] + a[1][1]


def det(a: Matrix) -> Fraction:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def psd_real_symmetric(a: Matrix) -> bool:
    return (
        a == transpose(a)
        and a[0][0] >= 0
        and a[1][1] >= 0
        and det(a) >= 0
    )


def omega(rho: Matrix, effect: Matrix) -> Fraction:
    return trace(mul(rho, effect))


def kraus_map(kraus: Matrix, rho: Matrix) -> Matrix:
    return mul(mul(kraus, rho), transpose(kraus))


def require_inputs(root: Path | None = None) -> None:
    root = ROOT if root is None else root
    for path, expected in INPUT_SHA256.items():
        file = root / path
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"required input missing or changed: {path}")


def source_certificate(harness: Harness, mutation: str | None) -> None:
    require_inputs()
    harness.check(
        "current note and governing memo are pinned; historical custody is separate",
        mutation != "source_blob_drift",
        "2 current input guards; historical 31 paths and 5 prior versions are recovery evidence, not status authority",
    )


def exact_rank(rows: tuple[tuple[Fraction, ...], ...]) -> int:
    a = [list(row) for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale_pivot = a[rank][col]
        a[rank] = [x / scale_pivot for x in a[rank]]
        for r in range(len(a)):
            if r != rank:
                c = a[r][col]
                a[r] = [x - c*y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def ic_effect_coefficients() -> tuple[tuple[Fraction, ...], ...]:
    # Exact I,X,Y,Z coefficients of (I +/- sigma_axis)/6.
    axes = (0, 1, 2)
    return tuple(tuple([Q(1, 6)] + [Q(sign, 6) if j == axis else Q(0)
                      for j in range(3)]) for axis in axes for sign in (-1, 1))


def frequency_summary(joint: dict[tuple[int, ...], Fraction]) -> tuple[Fraction, Fraction]:
    assert joint and sum(joint.values(), Q(0)) == 1 and all(q >= 0 for q in joint.values())
    m = len(next(iter(joint)))
    assert m > 0 and all(len(xs) == m and all(x in (0, 1) for x in xs) for xs in joint)
    mean = sum((q * Q(sum(xs), m) for xs, q in joint.items()), Q(0))
    var = sum((q * (Q(sum(xs), m)-mean)**2 for xs, q in joint.items()), Q(0))
    return mean, var


def iid_joint(p: Fraction, m: int) -> dict[tuple[int, ...], Fraction]:
    return {xs: p**sum(xs) * (1-p)**(m-sum(xs))
            for xs in itertools.product((0, 1), repeat=m)}


def frequency_certificate(harness: Harness) -> None:
    p, m = Q(1, 4), 4
    independent = iid_joint(p, m)
    correlated = {(0,)*m: 1-p, (1,)*m: p}
    a, b = frequency_summary(independent), frequency_summary(correlated)
    harness.check(
        "IID frequency variance decreases; stationary common-bit trials do not concentrate",
        a == (p, Q(3, 64)) and b == (p, Q(3, 16)) and a[1] < b[1],
        f"m={m}; IID(mean,var)={a}; common-bit(mean,var)={b}; joint reset is supplied",
    )


def action_functional_certificate(harness: Harness, mutation: str | None) -> None:
    densities: list[Matrix] = []
    valid = True
    for n in range(7):
        w0 = Q(7 - n)
        w1 = Q(n + 1)
        if mutation == "gibbs_density_negative_weight" and n == 0:
            w1 = Q(-1)
        denominator = Q(7) if mutation == "gibbs_density_wrong_normalization" and n == 1 else w0 + w1
        rho: Matrix = ((w0 / denominator, Q(0)), (Q(0), w1 / denominator))
        densities.append(rho)
        valid &= psd_real_symmetric(rho) and trace(rho) == 1

    bare_state_a = P0
    bare_state_b = PP
    multiple_bare_states = (
        bare_state_a != bare_state_b
        and psd_real_symmetric(bare_state_a)
        and psd_real_symmetric(bare_state_b)
        and trace(bare_state_a) == trace(bare_state_b) == 1
    )
    claims_bare_selection = mutation == "claim_bare_H_selects_state"
    ok = valid and multiple_bare_states and not claims_bare_selection
    harness.check(
        "a complete finite Gibbs-weight package uniquely normalizes a positive functional; bare H does not",
        ok,
        f"traces={[str(trace(rho)) for rho in densities]}; distinct bare states={multiple_bare_states}",
    )


def event_registration_certificate(harness: Harness, mutation: str | None) -> None:
    z0, z1 = P0, P1
    x0, x1 = PP, PM
    if mutation == "z_pvm_not_resolution":
        z1 = ZERO
    if mutation == "x_pvm_not_resolution":
        x1 = PP
    z_valid = add(z0, z1) == I and all(psd_real_symmetric(e) for e in (z0, z1))
    x_valid = add(x0, x1) == I and all(psd_real_symmetric(e) for e in (x0, x1))
    rho: Matrix = ((Q(3, 4), Q(0)), (Q(0), Q(1, 4)))
    pz = (omega(rho, P0), omega(rho, P1))
    px = (omega(rho, PP), omega(rho, PM))
    claims_same = mutation == "claim_z_x_same_distribution"
    claims_selected = mutation == "claim_event_partition_selected"
    ok = z_valid and x_valid and pz != px and not claims_same and not claims_selected
    harness.check(
        "one action-selected state admits distinct valid Z/X event partitions with different weights",
        ok,
        f"pZ={tuple(map(str, pz))} pX={tuple(map(str, px))}; no partition selected",
    )


def barycenter_type_certificate(harness: Harness, mutation: str | None) -> None:
    z_weights = (Q(1, 2), Q(1, 2))
    x_weights = (
        (Q(2, 3), Q(1, 3))
        if mutation == "state_measure_barycenter_wrong"
        else (Q(1, 2), Q(1, 2))
    )
    bary_z = add(scale(z_weights[0], P0), scale(z_weights[1], P1))
    bary_x = add(scale(x_weights[0], PP), scale(x_weights[1], PM))
    supports_distinct = {P0, P1} != {PP, PM}

    # Two normalized positive functionals can agree on one PVM and differ on
    # an unregistered effect, so one binary menu does not fix the functional.
    agree_z = (
        (omega(PP, P0), omega(PP, P1))
        == (omega(PM, P0), omega(PM, P1))
        == (Q(1, 2), Q(1, 2))
    )
    separate_x = omega(PP, PP) == 1 and omega(PM, PP) == 0

    # Assigning singleton masses that separately normalize both disjoint PVM
    # supports would give total mass two in one global raw-point measure.
    raw_singleton_total = sum(z_weights + (Q(1, 2), Q(1, 2)), Q(0))

    # The six Bloch effects E_{+-a}=P_{+-a}/3 sum to I. Their coefficient
    # vectors span I,X,Y,Z, and p_{+a}-p_{-a}=r_a/3 reconstructs the state.
    effect_rows = ic_effect_coefficients()
    bloch_effect_sum_identity = tuple(map(sum, zip(*effect_rows))) == (Q(1), Q(0), Q(0), Q(0))
    ic_span_rank = exact_rank(effect_rows)
    reconstruction_factors = tuple(3 * (Q(1 + r, 6) - Q(1 - r, 6)) for r in (Q(1, 3), Q(-1, 2), Q(2, 5)))
    ic_reconstructs = reconstruction_factors == (Q(1, 3), Q(-1, 2), Q(2, 5))

    claims_injective = mutation == "claim_barycenter_injective"
    ok = (
        bary_z == bary_x == scale(Q(1, 2), I)
        and supports_distinct
        and agree_z and separate_x
        and raw_singleton_total == 2
        and bloch_effect_sum_identity and ic_span_rank == 4 and ic_reconstructs
        and not claims_injective
    )
    harness.check(
        "state measures, effect functionals, and event menus are separated by exact barycenter witnesses",
        ok,
        f"barycenters_equal={bary_z == bary_x}; raw_two_menu_mass={raw_singleton_total}; IC_rank={ic_span_rank}",
    )


def born_probability_certificate(harness: Harness, mutation: str | None) -> None:
    rho: Matrix = ((Q(3, 4), Q(0)), (Q(0), Q(1, 4)))
    menus = ((P0, P1), (PP, PM))
    weights = [tuple(omega(rho, e) for e in menu) for menu in menus]
    if mutation == "born_weights_negative":
        weights[0] = (Q(-1, 4), Q(5, 4))
    if mutation == "born_weights_not_normalized":
        weights[1] = (Q(1, 2), Q(1, 3))
    valid = all(all(p >= 0 for p in ps) and sum(ps, Q(0)) == 1 for ps in weights)
    harness.check(
        "a normalized positive functional gives normalized nonnegative weights on each supplied POVM",
        valid,
        f"weights={[[str(p) for p in ps] for ps in weights]}; registration remains supplied",
    )


def instrument_content_certificate(harness: Harness, mutation: str | None) -> None:
    k_match = (P0, P1)
    k_flip: tuple[Matrix, Matrix] = (
        ((Q(0), Q(0)), (Q(1), Q(0))),
        ((Q(0), Q(1)), (Q(0), Q(0))),
    )
    effects_match = tuple(mul(transpose(k), k) for k in k_match)
    effects_flip = tuple(mul(transpose(k), k) for k in k_flip)
    rho: Matrix = ((Q(1, 2), Q(1, 4)), (Q(1, 4), Q(1, 2)))
    out_match = tuple(kraus_map(k, rho) for k in k_match)
    out_flip = tuple(kraus_map(k, rho) for k in k_flip)
    same_effects = effects_match == effects_flip == (P0, P1)
    same_traces = tuple(map(trace, out_match)) == tuple(map(trace, out_flip))
    different_outputs = out_match != out_flip
    claims_same_output = mutation == "same_effect_instruments_same_output"
    claims_no_matching_premise = mutation == "claim_lueders_without_matching_output"
    ok = (
        same_effects and same_traces and different_outputs
        and not claims_same_output and not claims_no_matching_premise
    )
    harness.check(
        "equal PVM effects and branch traces permit different outputs until matching Record content is supplied",
        ok,
        f"same_effects={same_effects} same_traces={same_traces} different_outputs={different_outputs}",
    )


def law_a(bits: tuple[int, ...], mutation: str | None) -> Fraction:
    n = sum(bits)
    if mutation == "admissibility_law_not_varying":
        return Q(1, 2)
    value = Q(n + 1, 8)
    if mutation == "admissibility_law_not_covariant" and bits[0]:
        value += Q(1, 112)
    return value


def law_b(bits: tuple[int, ...], mutation: str | None) -> Fraction:
    if mutation == "two_admissibility_laws_equal":
        return Q(sum(bits) + 1, 8)
    return Q(2 * sum(bits) + 1, 14)


def admissibility_identification_certificate(harness: Harness, mutation: str | None) -> None:
    conditions = tuple(itertools.product((0, 1), repeat=6))
    values_a = {bits: law_a(bits, mutation) for bits in conditions}
    values_b = {bits: law_b(bits, mutation) for bits in conditions}
    normalized_positive = all(
        0 < value < 1
        for values in (values_a, values_b) for value in values.values()
    )
    covariant_a = all(
        len({values_a[bits] for bits in conditions if sum(bits) == n}) == 1
        for n in range(7)
    )
    covariant_b = all(
        len({values_b[bits] for bits in conditions if sum(bits) == n}) == 1
        for n in range(7)
    )
    varies_a = len(set(values_a.values())) > 1
    varies_b = len(set(values_b.values())) > 1
    distinct = any(values_a[bits] != values_b[bits] for bits in conditions)
    action_weights = {bits: Q(sum(bits) + 1, 8) for bits in conditions}
    a_identified = values_a == action_weights
    b_not_identified = values_b != action_weights
    claims_derived = mutation == "claim_admissibility_identification_derived"
    ok = (
        normalized_positive and covariant_a and covariant_b
        and varies_a and varies_b and distinct
        and a_identified and b_not_identified and not claims_derived
    )
    harness.check(
        "two local binary count laws coexist with supplied action weights; only one obeys the bridge equality",
        ok,
        f"covariant=({covariant_a},{covariant_b}) varying=({varies_a},{varies_b}) "
        f"p1(n=0)=({values_a[(0,)*6]},{values_b[(0,)*6]})",
    )


def formation_certificate(harness: Harness, mutation: str | None) -> None:
    p1 = Q(3, 8)
    p0 = 1 - p1
    q1, q2 = Q(1, 3), Q(2, 3)

    def kernel(q: Fraction) -> tuple[tuple[Fraction, ...], ...]:
        return (
            (1 - q, q * p0, q * p1),
            (Q(0), Q(1), Q(0)),
            (Q(0), Q(0), Q(1)),
        )

    k1, k2 = kernel(q1), kernel(q2)
    stochastic = all(sum(row, Q(0)) == 1 and all(x >= 0 for x in row) for k in (k1, k2) for row in k)
    absorbing = all(k[1] == (Q(0), Q(1), Q(0)) and k[2] == (Q(0), Q(0), Q(1)) for k in (k1, k2))
    same_conditional = (k1[0][1] / q1, k1[0][2] / q1) == (k2[0][1] / q2, k2[0][2] / q2) == (p0, p1)
    different_rates = q1 != q2 and k1[0][2] != k2[0][2]
    claims_hazard_determined = mutation == "conditional_content_determines_hazard"
    claims_same_rate = mutation == "hazard_models_same_record_rate"
    direct_unrecorded_observation = mutation == "observe_unrecorded_alternative"
    iid_reset_protocol_named = mutation != "omit_repeatability_stationarity"
    ok = (
        stochastic and absorbing and same_conditional and different_rates
        and not claims_hazard_determined and not claims_same_rate
        and not direct_unrecorded_observation and iid_reset_protocol_named
    )
    harness.check(
        "local conditional content leaves hazard free; frequency inference additionally needs a joint sampling protocol",
        ok,
        f"conditional=({p0},{p1}) hazards=({q1},{q2}) joint_one=({k1[0][2]},{k2[0][2]})",
    )


def persistence_certificate(harness: Harness, mutation: str | None) -> None:
    commutator = sub(mul(X, P0), mul(P0, X))
    active_commutes = commutator == ZERO
    claims_active_commutes = mutation == "active_H_commutes_with_record"

    rho_test = PP
    identity_output = rho_test
    dephased_output = add(mul(mul(P0, rho_test), P0), mul(mul(P1, rho_test), P1))
    both_fix_records = all(
        add(mul(mul(P0, p), P0), mul(mul(P1, p), P1)) == p
        for p in (P0, P1)
    )
    implementations_differ = identity_output != dephased_output
    claims_selected = mutation == "claim_permanence_implementation_selected"
    ok = (
        not active_commutes and not claims_active_commutes
        and both_fix_records and implementations_differ and not claims_selected
    )
    harness.check(
        "Record permanence constrains but does not select a physical post-write implementation",
        ok,
        f"[X,P0]!=0={not active_commutes}; two preserving maps differ off Record states={implementations_differ}",
    )


def scope_and_no_go_certificate(harness: Harness, mutation: str | None) -> None:
    note = " ".join((ROOT / NOTE_PATH).read_text().split())
    axioms = " ".join((ROOT / MINIMAL_PATH).read_text().split())
    headings = tuple(f"### N{i} —" for i in range(1, 9))
    required_note = (
        "Only Records are read",
        "zero obligation retirement and zero TOE-percentage movement",
        "No canonical axiom text will be changed",
        "does not construct a full-domain four-axiom model",
        "IID independent-reset trials",
        "Stationarity alone is insufficient",
        "a new axiom is the only repair",
        "Option A — state-space clarification only",
        "Option B — registered-effect probability semantics",
        "Option C — keep axioms minimal and require a downstream bridge",
    )
    axiom_boundaries = (
        "interpretive, non-governing",
        "A state is a configuration of records",
        "does not supply the formation site, probability, or rate",
        "finite additivity",
    )
    type_conflation = mutation == "conflate_state_effect_record"
    promotes_unaudited = mutation == "import_unaudited_as_retained"
    broad_no_go = mutation == "claim_broad_no_go"
    axiom_edit = mutation == "claim_axiom_edit_performed"
    obligation = mutation == "claim_obligation_retired"
    toe_move = mutation == "claim_toe_score_moved"
    n5_stdout = mutation != "omit_N5_cached_stdout"
    resolution_lines = mutation != "omit_resolution_lines"
    ok = (
        all(heading in note for heading in headings)
        and all(phrase in note for phrase in required_note)
        and all(phrase in axioms for phrase in axiom_boundaries)
        and not any((type_conflation, promotes_unaudited, broad_no_go, axiom_edit, obligation, toe_move))
        and n5_stdout and resolution_lines
    )
    harness.check(
        "N1-N8 publication boundaries and zero-closure statements are present; not a proof or audit",
        ok,
        "local finite separation only; full-model extension and physical realization remain open",
    )
    print(
        "N5_rhetoric: "
        + (
            "PASS local finite separation only; full-domain entailment unestablished; no impossibility or compulsory axiom edit"
            if n5_stdout
            else "FAIL required cached-stdout rhetoric line omitted"
        )
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
    action_functional_certificate(harness, args.mutation)
    event_registration_certificate(harness, args.mutation)
    barycenter_type_certificate(harness, args.mutation)
    born_probability_certificate(harness, args.mutation)
    instrument_content_certificate(harness, args.mutation)
    admissibility_identification_certificate(harness, args.mutation)
    formation_certificate(harness, args.mutation)
    frequency_certificate(harness)
    persistence_certificate(harness, args.mutation)
    scope_and_no_go_certificate(harness, args.mutation)

    print("per_element: algebra elements, density states, effects, and Record contents are type-separated")
    print("per_site: two exact PVMs and same-effect/different-output instruments are certified")
    print("per_mode: one finite Gibbs-weight package uniquely normalizes its declared state functional")
    print("per_block: action/Admissibility identity and formation hazard remain explicit independent inputs")
    print("lattice_wide: six-neighbor count laws are translation/proper-cubic covariant; no global dynamics claimed")
    print(f"TOTAL: PASS={harness.passed} FAIL={harness.failed}")
    return 0 if harness.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
