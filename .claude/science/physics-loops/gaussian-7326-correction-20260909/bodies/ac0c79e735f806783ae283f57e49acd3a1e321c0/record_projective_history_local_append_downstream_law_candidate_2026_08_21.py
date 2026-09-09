#!/usr/bin/env python3
"""Exact finite checks for a provisional projective-history sector Law.

The finite projective domain, calibrated event registration, trace/history
rule, and composite-cylinder coupling are the provisionally selected
sector-Law kernel.  Formation cadence, packet realization, supplied causal
layer, and contingent member remain benchmark or history data.  The script
checks their mathematical consistency and their interface with permanent site
Records; it does not derive any of them from the framework axioms.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import TYPE_CHECKING, Iterable

import sympy as sp


# Static audit-packet binding only.  The independent reconstruction must not be
# imported or executed by this primary runner, but its source must accompany
# the primary in a restricted audit packet.
if TYPE_CHECKING:
    from record_projective_history_local_append_downstream_law_candidate_independent_check_2026_08_21 import (
        MUTATIONS as _independent_mutations,
    )


I2 = sp.eye(2)
Z2 = sp.zeros(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
SQRT2 = sp.sqrt(2)


MUTATIONS = (
    "typed_writer",
    "cylinder",
    "identity",
    "packet",
    "product",
    "bell",
    "local_projection",
    "append",
    "record_fibre",
    "actuality",
    "cadence",
    "ledger",
)

parser = argparse.ArgumentParser()
parser.add_argument("--mutation", choices=MUTATIONS)
args = parser.parse_args()
mutation = args.mutation


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def scalar_equal(left: sp.Expr, right: sp.Expr) -> bool:
    return sp.simplify(left - right) == 0


def projector(observable: sp.Matrix, outcome: int) -> sp.Matrix:
    return sp.simplify((I2 + outcome * observable) / 2)


def embed_left(operator: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(operator, I2)


def embed_right(operator: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(I2, operator)


def branch(state: sp.Matrix, effect: sp.Matrix) -> sp.Matrix:
    return sp.simplify(effect * state * effect)


def weight(state: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(state))


def normalized(state: sp.Matrix) -> sp.Matrix:
    total = weight(state)
    if scalar_equal(total, 0):
        raise ValueError("zero branch has no normalized continuation")
    return sp.simplify(state / total)


def encode_two_qubit_packet(state: sp.Matrix) -> tuple[sp.Matrix, ...]:
    if state.shape != (4, 4):
        raise ValueError("packet encoder expects a 4x4 state")
    return tuple(
        state[2 * row : 2 * row + 2, 2 * col : 2 * col + 2]
        for row in range(2)
        for col in range(2)
    )


def decode_two_qubit_packet(packet: Iterable[sp.Matrix]) -> sp.Matrix:
    blocks = tuple(packet)
    if len(blocks) != 4 or any(block.shape != (2, 2) for block in blocks):
        raise ValueError("packet needs four M2 blocks")
    return sp.Matrix.vstack(
        sp.Matrix.hstack(blocks[0], blocks[1]),
        sp.Matrix.hstack(blocks[2], blocks[3]),
    )


Site = tuple[int, int, int]
DIRECTIONS: tuple[Site, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def add_site(left: Site, right: Site) -> Site:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def scale_site(scale: int, site: Site) -> Site:
    return tuple(scale * value for value in site)  # type: ignore[return-value]


def discover_packet_sites(
    ledger: dict[Site, sp.Matrix], anchor: Site
) -> tuple[Site, ...]:
    """Find the unique four-site straight Record chain leaving an anchor."""
    chains = []
    for direction in DIRECTIONS:
        chain = tuple(add_site(anchor, scale_site(step, direction)) for step in range(1, 5))
        if all(site in ledger for site in chain):
            chains.append(chain)
    if len(chains) != 1:
        raise ValueError("preparation packet needs one unique four-site chain")
    return chains[0]


def decode_packet_from_records(
    ledger: dict[Site, sp.Matrix], anchor: Site
) -> sp.Matrix:
    return decode_two_qubit_packet(
        ledger[site] for site in discover_packet_sites(ledger, anchor)
    )


def transform_site(site: Site) -> Site:
    """One proper cubic rotation followed by a translation."""
    x, y, z = site
    return (-y + 11, x - 7, z + 5)


def transform_ledger(ledger: dict[Site, sp.Matrix]) -> dict[Site, sp.Matrix]:
    return {transform_site(site): content for site, content in ledger.items()}


def joint_probability(
    state: sp.Matrix,
    observable_a: sp.Matrix,
    observable_b: sp.Matrix,
    outcome_a: int,
    outcome_b: int,
) -> sp.Expr:
    effect = sp.kronecker_product(
        projector(observable_a, outcome_a),
        projector(observable_b, outcome_b),
    )
    return weight(branch(state, effect))


def correlation(
    state: sp.Matrix, observable_a: sp.Matrix, observable_b: sp.Matrix
) -> sp.Expr:
    return sp.simplify(
        sum(
            outcome_a
            * outcome_b
            * joint_probability(
                state, observable_a, observable_b, outcome_a, outcome_b
            )
            for outcome_a in (1, -1)
            for outcome_b in (1, -1)
        )
    )


def adjacent(left: Site, right: Site) -> bool:
    return sum(abs(a - b) for a, b in zip(left, right)) == 1


def valid_record_content(content: sp.Matrix) -> bool:
    return (
        content.shape == (2, 2)
        and matrix_equal(content, content.H)
        and matrix_equal(content * content, content)
        and scalar_equal(sp.trace(content), 1)
    )


def local_append(
    ledger: dict[Site, sp.Matrix],
    program_site: Site,
    target_site: Site,
    content: sp.Matrix,
) -> dict[Site, sp.Matrix]:
    if program_site not in ledger:
        raise ValueError("missing program Record")
    if not adjacent(program_site, target_site):
        raise ValueError("target is not nearest-neighbour to its program")
    if target_site in ledger:
        raise ValueError("Record target is already occupied")
    if not valid_record_content(content):
        raise ValueError("outcome is not a registered rank-one M2 content")
    program = ledger[program_site]
    if not (
        matrix_equal(content, program)
        or matrix_equal(content, I2 - program)
    ):
        raise ValueError("outcome content does not match its registered program")
    result = dict(ledger)
    result[target_site] = content
    return result


def ledgers_equal(
    left: dict[Site, sp.Matrix], right: dict[Site, sp.Matrix]
) -> bool:
    return left.keys() == right.keys() and all(
        matrix_equal(left[site], right[site]) for site in left
    )


def select_member(weights: list[sp.Expr], coordinate: sp.Rational) -> int:
    if coordinate < 0 or coordinate >= 1:
        raise ValueError("history coordinate must lie in [0,1)")
    cumulative = sp.Rational(0)
    for index, probability in enumerate(weights):
        cumulative += probability
        if coordinate < cumulative:
            return index
    raise AssertionError("normalized weights did not cover the coordinate")


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


checks: list[Check] = []


def check(name: str, passed: bool, detail: str) -> None:
    checks.append(Check(name=name, passed=bool(passed), detail=detail))


# A. Calibrated binary writer algebra, without probability.
p0 = projector(Z, 1)
p1 = projector(Z, -1)
writer = sp.Matrix.vstack(p0, p1)
q0_out = sp.diag(0, 0, 1, 1) if mutation == "typed_writer" else sp.diag(1, 1, 0, 0)
q1_out = sp.diag(0, 0, 1, 1)
typed_writer = (
    matrix_equal(writer.H * writer, I2)
    and matrix_equal(q0_out * writer, writer * p0)
    and matrix_equal(q1_out * writer, writer * p1)
    and matrix_equal(branch(p0, p1), Z2)
)
check(
    "typed writer has exact endpoint no-fabrication",
    typed_writer,
    "W^dagger W=I, Q_j W=W P_j, and the opposite endpoint block is zero",
)


# B. A sequential projective cylinder is normalized and prefix-consistent.
rho_one = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 6)],
                     [sp.Rational(1, 6), sp.Rational(1, 3)]])
z_children = {a: branch(rho_one, projector(Z, a)) for a in (1, -1)}
terminal_weights: dict[tuple[int, int], sp.Expr] = {}
prefix_ok = True
for a, child in z_children.items():
    child_sum = sp.Rational(0)
    for b in (1, -1):
        grandchild = branch(child, projector(X, b))
        terminal_weights[(a, b)] = weight(grandchild)
        child_sum += weight(grandchild)
    prefix_ok = prefix_ok and scalar_equal(child_sum, weight(child))
cylinder_total = sum(terminal_weights.values())
if mutation == "cylinder":
    cylinder_total -= terminal_weights[(1, 1)]
cylinder_ok = prefix_ok and scalar_equal(cylinder_total, 1)
check(
    "finite projective cylinders normalize and marginalize",
    cylinder_ok,
    f"four exact terminal weights sum to {sp.simplify(sum(terminal_weights.values()))}",
)


# C. Omitting an intervention is not the same as measuring and forgetting it.
rho_plus = sp.Rational(1, 2) * I2 if mutation == "identity" else projector(X, 1)
dephased_z = sum(
    (branch(rho_plus, projector(Z, a)) for a in (1, -1)),
    sp.zeros(2),
)
identity_containment = (
    scalar_equal(weight(rho_plus), 1)
    and scalar_equal(weight(dephased_z), 1)
    and not matrix_equal(rho_plus, dephased_z)
)
check(
    "identity continuation stays distinct from measure-and-forget",
    identity_containment,
    "both normalize, while the omitted intervention preserves X coherence",
)


# D. A supplied packet registration serializes a two-qubit state relationally.
ket01 = sp.Matrix([0, 1, 0, 0])
ket10 = sp.Matrix([0, 0, 1, 0])
singlet = sp.simplify((ket01 - ket10) / SQRT2)
rho_singlet = sp.simplify(singlet * singlet.H)
packet = encode_two_qubit_packet(rho_singlet)
packet_anchor: Site = (-9, 0, 0)
packet_sites = tuple((packet_anchor[0] + step, 0, 0) for step in range(1, 5))
packet_ledger = {packet_anchor: I2}
packet_ledger.update({site: block for site, block in zip(packet_sites, packet)})
packet_roundtrip_ledger = dict(packet_ledger)
if mutation == "packet":
    packet_roundtrip_ledger[packet_sites[0]], packet_roundtrip_ledger[packet_sites[1]] = (
        packet_roundtrip_ledger[packet_sites[1]],
        packet_roundtrip_ledger[packet_sites[0]],
    )
transformed_packet_ledger = transform_ledger(packet_ledger)
packet_ok = (
    matrix_equal(
        decode_packet_from_records(packet_roundtrip_ledger, packet_anchor),
        rho_singlet,
    )
    and matrix_equal(
        decode_packet_from_records(
            transformed_packet_ledger, transform_site(packet_anchor)
        ),
        rho_singlet,
    )
    and all(block.shape == (2, 2) for block in packet)
)
check(
    "supplied anchored M2 packet reconstructs under carried lattice motion",
    packet_ok,
    "one anchor plus four M2 block Records recover the 4x4 singlet packet",
)


# E. Product preparations reduce to the product of local outcome kernels.
rho_a = sp.Matrix([[sp.Rational(3, 4), 0], [0, sp.Rational(1, 4)]])
rho_b = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 4)],
                   [sp.Rational(1, 4), sp.Rational(1, 2)]])
rho_product = rho_singlet if mutation == "product" else sp.kronecker_product(rho_a, rho_b)
product_ok = True
for a in (1, -1):
    for b in (1, -1):
        joint = joint_probability(rho_product, Z, X, a, b)
        local = weight(branch(rho_a, projector(Z, a))) * weight(
            branch(rho_b, projector(X, b))
        )
        product_ok = product_ok and scalar_equal(joint, local)
check(
    "product preparations reduce to local projective kernels",
    product_ok,
    "all four Z/X outcome pairs factor exactly",
)


# F. The supplied nonfactorizing history functional gives no-signalling Bell data.
a0, a1 = Z, X
b0 = sp.simplify((Z + X) / SQRT2)
b1 = b0 if mutation == "bell" else sp.simplify((Z - X) / SQRT2)
observables_a = (a0, a1)
observables_b = (b0, b1)
bell_tables: dict[tuple[int, int], dict[tuple[int, int], sp.Expr]] = {}
no_signalling = True
for x, obs_a in enumerate(observables_a):
    for y, obs_b in enumerate(observables_b):
        table = {
            (a, b): joint_probability(rho_singlet, obs_a, obs_b, a, b)
            for a in (1, -1)
            for b in (1, -1)
        }
        bell_tables[(x, y)] = table
        no_signalling = no_signalling and scalar_equal(sum(table.values()), 1)
for x in range(2):
    for a in (1, -1):
        left = sum(bell_tables[(x, 0)][(a, b)] for b in (1, -1))
        right = sum(bell_tables[(x, 1)][(a, b)] for b in (1, -1))
        no_signalling = no_signalling and scalar_equal(left, right)
for y in range(2):
    for b in (1, -1):
        left = sum(bell_tables[(0, y)][(a, b)] for a in (1, -1))
        right = sum(bell_tables[(1, y)][(a, b)] for a in (1, -1))
        no_signalling = no_signalling and scalar_equal(left, right)
chsh = sp.simplify(
    correlation(rho_singlet, a0, b0)
    + correlation(rho_singlet, a0, b1)
    + correlation(rho_singlet, a1, b0)
    - correlation(rho_singlet, a1, b1)
)
bell_ok = no_signalling and scalar_equal(abs(chsh), 2 * SQRT2)
check(
    "global projective history functional is normalized and no-signalling",
    bell_ok,
    f"CHSH={chsh}; absolute value is 2*sqrt(2)",
)


# G. Its one-site pushforwards equal the candidate's local event marginals.
local_projection_ok = True
for x, obs_a in enumerate(observables_a):
    local_expected = {
        a: weight(branch(sp.Rational(1, 2) * I2, projector(obs_a, a)))
        for a in (1, -1)
    }
    if mutation == "local_projection" and x == 0:
        local_expected[1] += sp.Rational(1, 10)
    for y in range(2):
        for a in (1, -1):
            marginal = sum(
                bell_tables[(x, y)][(a, b)] for b in (1, -1)
            )
            local_projection_ok = local_projection_ok and scalar_equal(
                marginal, local_expected[a]
            )
for y, obs_b in enumerate(observables_b):
    local_expected = {
        b: weight(branch(sp.Rational(1, 2) * I2, projector(obs_b, b)))
        for b in (1, -1)
    }
    for x in range(2):
        for b in (1, -1):
            marginal = sum(
                bell_tables[(x, y)][(a, b)] for a in (1, -1)
            )
            local_projection_ok = local_projection_ok and scalar_equal(
                marginal, local_expected[b]
            )
check(
    "global history weights have consistent two-wing one-site projections",
    local_projection_ok,
    "both singlet-wing marginals equal their local maximally mixed projective laws",
)


# H. Two incomparable commits are genuinely local and order-confluent.
program_a, target_a = (-2, 0, 0), (-1, 0, 0)
target_b, program_b = (1, 0, 0), (2, 0, 0)
supplied_event_layer = {target_a: 1, target_b: 1}
initial_ledger = {program_a: projector(a0, 1), program_b: projector(b0, 1)}
content_a = projector(a0, 1)
content_b = projector(b0, -1)
prefix_a = local_append(initial_ledger, program_a, target_a, content_a)
prefix_b = local_append(initial_ledger, program_b, target_b, content_b)
final_ab = local_append(prefix_a, program_b, target_b, content_b)
final_ba = (
    prefix_b
    if mutation == "append"
    else local_append(prefix_b, program_a, target_a, content_a)
)
confluence_ok = (
    target_a != target_b
    and supplied_event_layer[target_a] == supplied_event_layer[target_b]
    and
    len(prefix_a) == len(initial_ledger) + 1
    and target_b not in prefix_a
    and len(prefix_b) == len(initial_ledger) + 1
    and target_a not in prefix_b
    and ledgers_equal(final_ab, final_ba)
    and all(matrix_equal(final_ab[site], initial_ledger[site]) for site in initial_ledger)
)
try:
    local_append(final_ab, program_a, target_a, content_a)
    occupied_rejected = False
except ValueError:
    occupied_rejected = True
try:
    local_append(initial_ledger, program_a, target_a, projector(X, 1))
    mismatched_content_rejected = False
except ValueError:
    mismatched_content_rejected = True
check(
    "declared concurrent site appends preserve calibration and confluence",
    confluence_ok and occupied_rejected and mismatched_content_rejected,
    "each prefix adds one calibrated Record; both orders share one final ledger",
)


# I. Registered finite Record prefixes reconstruct their declared continuations.
fibre_ok = True
prefix_count = 0
for x, obs_a in enumerate(observables_a):
    for a in (1, -1):
        for y, obs_b in enumerate(observables_b):
            record_ledger = dict(packet_ledger)
            record_ledger[program_a] = projector(obs_a, 1)
            record_ledger[program_b] = projector(obs_b, 1)
            record_ledger = local_append(
                record_ledger, program_a, target_a, projector(obs_a, a)
            )
            reverse_insertion_ledger = dict(reversed(tuple(record_ledger.items())))
            if mutation == "record_fibre" and (x, a, y) == (0, 1, 0):
                reverse_insertion_ledger[program_b] = projector(Y, 1)
            decoded_initial = decode_packet_from_records(
                reverse_insertion_ledger, packet_anchor
            )
            decoded_content = reverse_insertion_ledger[target_a]
            decoded_setting_b = reverse_insertion_ledger[program_b]
            decoded_prefix = branch(decoded_initial, embed_left(decoded_content))
            direct_prefix = branch(rho_singlet, embed_left(projector(obs_a, a)))
            fibre_ok = fibre_ok and matrix_equal(decoded_prefix, direct_prefix)
            for b in (1, -1):
                decoded_outcome_b = (
                    decoded_setting_b if b == 1 else I2 - decoded_setting_b
                )
                future_from_records = weight(
                    branch(decoded_prefix, embed_right(decoded_outcome_b))
                ) / weight(decoded_prefix)
                future_direct = joint_probability(
                    rho_singlet, obs_a, obs_b, a, b
                ) / sum(
                    joint_probability(rho_singlet, obs_a, obs_b, a, k)
                    for k in (1, -1)
                )
                fibre_ok = fibre_ok and scalar_equal(
                    future_from_records, future_direct
                )
            prefix_count += 1
check(
    "registered finite Record prefixes reconstruct the declared future calculator",
    fibre_ok,
    f"checked {prefix_count} A-setting/outcome/B-program prefixes in insertion-independent order",
)


# J. One supplied coordinate selects one member without changing the Law table.
member_keys = ((1, 1), (1, -1), (-1, 1), (-1, -1))
member_weights = [bell_tables[(0, 0)][key] for key in member_keys]
member_low = select_member(member_weights, sp.Rational(1, 20))
member_high = select_member(
    member_weights,
    sp.Rational(1, 20) if mutation == "actuality" else sp.Rational(19, 20),
)
actual_ledgers = []
for member in (member_low, member_high):
    outcome_a, outcome_b = member_keys[member]
    actual_ledger = local_append(
        initial_ledger, program_a, target_a, projector(a0, outcome_a)
    )
    actual_ledger = local_append(
        actual_ledger, program_b, target_b, projector(b0, outcome_b)
    )
    actual_ledgers.append(actual_ledger)
actuality_ok = (
    scalar_equal(sum(member_weights), 1)
    and member_low != member_high
    and len(actual_ledgers[0]) == len(initial_ledger) + 2
    and len(actual_ledgers[1]) == len(initial_ledger) + 2
    and not ledgers_equal(actual_ledgers[0], actual_ledgers[1])
)
check(
    "supplied coordinates select distinct one-member Record ledgers",
    actuality_ok,
    f"one unchanged normalized table supports realized members {member_low} and {member_high}",
)


# K. Supplied competing hazards have a normalized outcome law and one cadence.
gamma, time = sp.symbols("gamma time", positive=True, real=True)
hazards = [sp.simplify(gamma * probability) for probability in member_weights]
if mutation == "cadence":
    hazards[0] *= 2
survival = sp.exp(-gamma * time)
hazards_nonnegative = all(
    sp.ask(sp.Q.nonnegative(sp.simplify(hazard / gamma))) is True
    for hazard in hazards
)
cadence_ok = (
    hazards_nonnegative
    and scalar_equal(sum(hazards), gamma)
    and scalar_equal(-sp.diff(survival, time) / survival, gamma)
    and scalar_equal(survival.subs(time, 0), 1)
    and scalar_equal(sp.limit(survival, time, sp.oo), 0)
)
check(
    "supplied formation hazards are nonnegative and normalize at one cadence",
    cadence_ok,
    "lambda_o>=0, sum_o lambda_o=gamma, S(0)=1, and S(infinity)=0",
)


# L. The finite resource ledger and uncosted handoffs are explicit.
declared_inputs = {
    "preparation_packet_registration": "benchmark_boundary",
    "projective_program_category": "selected_sector_law",
    "event_registration": "selected_sector_law",
    "trace_history_functional": "selected_sector_law",
    "formation_cadence": "benchmark_process",
    "causal_layer": "benchmark_boundary",
    "global_coupling": "selected_sector_law",
    "contingent_member": "contingent_history_data",
}
selected_sector_law_fields = {
    name for name, status in declared_inputs.items() if status == "selected_sector_law"
}
benchmark_or_history_fields = set(declared_inputs) - selected_sector_law_fields
open_handoffs = {
    "packet_genesis",
    "packet_renewal",
    "target_allocation",
    "collision_arbitration",
    "metric_time",
    "energy_cost",
    "matter",
    "gravity",
}
resource_counts = {
    "packet_anchor_records": 1,
    "packet_block_records": len(packet),
    "program_records": len(initial_ledger),
    "new_outcome_records": len(final_ab) - len(initial_ledger),
}
final_record_count = sum(resource_counts.values())
expected_final_record_count = 8 if mutation == "ledger" else 9
ledger_ok = (
    selected_sector_law_fields
    == {
        "projective_program_category",
        "event_registration",
        "trace_history_functional",
        "global_coupling",
    }
    and benchmark_or_history_fields
    == {
        "preparation_packet_registration",
        "formation_cadence",
        "causal_layer",
        "contingent_member",
    }
    and len(open_handoffs) == 8
    and resource_counts
    == {
        "packet_anchor_records": 1,
        "packet_block_records": 4,
        "program_records": 2,
        "new_outcome_records": 2,
    }
    and final_record_count == expected_final_record_count
)
check(
    "finite resource ledger closes and names eight declared open handoffs",
    ledger_ok,
    f"4 selected kernel fields, 4 benchmark/history fields, "
    f"{final_record_count} Records, and {len(open_handoffs)} open handoffs",
)


print(
    "N5_RESOLUTION per_element: exact 2x2 endpoint branch P_1 P_0 P_1=0 "
    "and both 4x2 typed-writer block identities are tested; no general event-weight "
    "selection is claimed."
)
print(
    "N5_RESOLUTION per_site: two distinct nearest-neighbour program/target pairs are "
    "tested for one-site append, permanence, calibration, rewrite rejection, and "
    "two-order confluence; no arbitrary site environment is claimed."
)
print(
    "N5_RESOLUTION per_mode: one-qubit Z/X histories and all four declared two-qubit "
    "Bell setting pairs are tested exactly; no general POVM or field-mode category is claimed."
)
print(
    "N5_RESOLUTION per_block: one four-M2 singlet packet is reconstructed before and "
    "after one carried proper-cubic transform; packet genesis and scalable block renewal "
    "are not tested."
)
print(
    "N5_RESOLUTION lattice_wide: not tested; the runner proves no lattice-wide, "
    "continuum, arbitrary-history, matter, gravity, or TOE closure statement."
)


for item in checks:
    label = "PASS" if item.passed else "FAIL"
    print(f"[{label}] {item.name}: {item.detail}")

passed = sum(item.passed for item in checks)
failed = len(checks) - passed
print(f"TOTAL: PASS={passed} FAIL={failed}")
raise SystemExit(0 if failed == 0 else 1)
