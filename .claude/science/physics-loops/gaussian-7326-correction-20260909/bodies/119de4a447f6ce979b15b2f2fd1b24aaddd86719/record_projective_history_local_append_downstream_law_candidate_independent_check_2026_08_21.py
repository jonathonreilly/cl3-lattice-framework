#!/usr/bin/env python3
"""Independent exact checks for the finite projective-history sector Law.

This reconstruction does not import the primary runner.  It deliberately uses
an eight-Record host-codebook fixture (four packet blocks, two programs, and
two outcomes), not the primary runner's distinct nine-Record anchored
relational packet.  It therefore cross-checks the finite packet algebra but
does not certify the primary's relational decoder or resource count.

The finite projective domain, calibrated event registration, trace/history
weights, and composite-cylinder coupling are the provisionally selected
sector-Law kernel.  Preparation-packet registration, formation cadence,
fixture geometry, and the realized-member coordinate remain benchmark or
history data.  The checker does not infer Record admissibility, spacelike
causal order, an autonomous covariant Law, physical clock calibration,
resource renewal, or the documentary owner decision.  Each optional mutation
changes one physical/input datum and must isolate exactly one of the twelve
gates.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Iterable

import sympy as sp


I2 = sp.eye(2)
O2 = sp.zeros(2)
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
mutation = parser.parse_args().mutation


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(entry) == 0 for entry in left - right
    )


def scalar_equal(left: sp.Expr, right: sp.Expr) -> bool:
    return sp.simplify(left - right) == 0


def nonnegative(value: sp.Expr) -> bool:
    relation = sp.simplify(sp.Ge(sp.simplify(value), 0))
    return relation is sp.true or relation == sp.true


def projector(observable: sp.Matrix, sign: int) -> sp.Matrix:
    if sign not in (-1, 1):
        raise ValueError("projective outcome must be +1 or -1")
    return sp.simplify((I2 + sign * observable) / 2)


def branch(state: sp.Matrix, effect: sp.Matrix) -> sp.Matrix:
    return sp.simplify(effect * state * effect)


def probability(state: sp.Matrix, effect: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(branch(state, effect)))


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
    return probability(state, effect)


def packet_blocks(state: sp.Matrix) -> tuple[sp.Matrix, ...]:
    if state.shape != (4, 4):
        raise ValueError("two-qubit packet source must be 4x4")
    return tuple(
        state[2 * row : 2 * row + 2, 2 * col : 2 * col + 2]
        for row in range(2)
        for col in range(2)
    )


def assemble_packet(blocks: Iterable[sp.Matrix]) -> sp.Matrix:
    data = tuple(blocks)
    if len(data) != 4 or any(block.shape != (2, 2) for block in data):
        raise ValueError("packet registration requires four M2 blocks")
    return sp.Matrix.vstack(
        sp.Matrix.hstack(data[0], data[1]),
        sp.Matrix.hstack(data[2], data[3]),
    )


def rank_one_projector(content: sp.Matrix) -> bool:
    return (
        content.shape == (2, 2)
        and matrix_equal(content, content.H)
        and matrix_equal(content * content, content)
        and scalar_equal(sp.trace(content), 1)
    )


Site = tuple[int, int, int]


def adjacent(left: Site, right: Site) -> bool:
    return sum(abs(a - b) for a, b in zip(left, right)) == 1


def registered_outcome(setting: sp.Matrix, content: sp.Matrix) -> bool:
    return rank_one_projector(setting) and (
        matrix_equal(content, setting) or matrix_equal(content, I2 - setting)
    )


def append_registered_outcome(
    ledger: dict[Site, sp.Matrix],
    program_site: Site,
    target_site: Site,
    content: sp.Matrix,
) -> dict[Site, sp.Matrix]:
    if program_site not in ledger:
        raise ValueError("missing setting Record")
    if not adjacent(program_site, target_site):
        raise ValueError("target is not nearest-neighbour")
    if target_site in ledger:
        raise ValueError("target already carries a Record")
    if not registered_outcome(ledger[program_site], content):
        raise ValueError("content is not an outcome of the recorded setting")
    updated = dict(ledger)
    updated[target_site] = content
    return updated


def ledgers_equal(
    left: dict[Site, sp.Matrix], right: dict[Site, sp.Matrix]
) -> bool:
    return left.keys() == right.keys() and all(
        matrix_equal(left[site], right[site]) for site in left
    )


def choose_member(weights: tuple[sp.Expr, ...], coordinate: sp.Rational) -> int:
    if coordinate < 0 or coordinate >= 1:
        raise ValueError("coordinate must lie in [0,1)")
    cumulative = sp.Rational(0)
    for index, value in enumerate(weights):
        cumulative = sp.simplify(cumulative + value)
        if coordinate < cumulative:
            return index
    raise ValueError("weights are not normalized")


@dataclass(frozen=True)
class Result:
    name: str
    passed: bool
    detail: str


results: list[Result] = []


def check(name: str, passed: bool, detail: str) -> None:
    results.append(Result(name, bool(passed), detail))


# 1. Reconstruct both typed branches and both endpoint exclusions.
p_plus = projector(Z, 1)
p_minus = projector(Z, -1)
writer = sp.Matrix.vstack(p_plus, p_minus)
q_plus = sp.diag(1, 1, 0, 0)
q_minus = sp.diag(0, 0, 1, 1)
q_plus_gate = q_minus if mutation == "typed_writer" else q_plus
typed_ok = (
    matrix_equal(writer.H * writer, I2)
    and matrix_equal(q_plus_gate * writer, writer * p_plus)
    and matrix_equal(q_minus * writer, writer * p_minus)
    and matrix_equal(q_plus_gate * writer * p_minus, sp.zeros(4, 2))
    and matrix_equal(q_minus * writer * p_plus, sp.zeros(4, 2))
)
check(
    "typed writer and both endpoint exclusions",
    typed_ok,
    "W*W=I and Q_j W=W P_j for j=+,-",
)


# 2. Reconstruct the two-stage Z-then-X cylinder and its exact prefixes.
rho_one = sp.Matrix(
    [[sp.Rational(2, 3), sp.Rational(1, 6)],
     [sp.Rational(1, 6), sp.Rational(1, 3)]]
)
terminal: dict[tuple[int, int], sp.Expr] = {}
prefix_ok = True
for first in (1, -1):
    child = branch(rho_one, projector(Z, first))
    for second in (1, -1):
        terminal[(first, second)] = probability(child, projector(X, second))
    prefix_ok = prefix_ok and scalar_equal(
        sum(terminal[(first, second)] for second in (1, -1)),
        sp.trace(child),
    )
expected_terminal = {
    (1, 1): sp.Rational(1, 3),
    (1, -1): sp.Rational(1, 3),
    (-1, 1): sp.Rational(1, 6),
    (-1, -1): sp.Rational(1, 6),
}
terminal_gate = dict(terminal)
if mutation == "cylinder":
    terminal_gate[(1, 1)] += sp.Rational(1, 10)
cylinder_ok = (
    prefix_ok
    and scalar_equal(sum(terminal_gate.values()), 1)
    and all(
        scalar_equal(terminal_gate[key], value)
        for key, value in expected_terminal.items()
    )
)
check(
    "finite projective cylinder normalization",
    cylinder_ok,
    "Z/X weights are exactly 1/3,1/3,1/6,1/6",
)


# 3. Check identity continuation against the explicit Z dephasing channel.
rho_x_plus = I2 / 2 if mutation == "identity" else projector(X, 1)
z_dephased = sum(
    (branch(rho_x_plus, projector(Z, sign)) for sign in (1, -1)), O2
)
identity_ok = (
    matrix_equal(z_dephased, I2 / 2)
    and not matrix_equal(z_dephased, rho_x_plus)
    and scalar_equal(sp.trace(z_dephased), sp.trace(rho_x_plus))
)
check(
    "identity differs from measure-and-forget",
    identity_ok,
    "Z dephasing sends X+ to I/2 while omission leaves X+",
)


# 4. The packet claim is algebraic; Record registration/admissibility is input.
ket01 = sp.Matrix([0, 1, 0, 0])
ket10 = sp.Matrix([0, 0, 1, 0])
singlet = sp.simplify((ket01 - ket10) / SQRT2)
rho_singlet = sp.simplify(singlet * singlet.H)
packet = packet_blocks(rho_singlet)
packet_gate = list(packet)
if mutation == "packet":
    packet_gate[0], packet_gate[1] = packet_gate[1], packet_gate[0]
packet_ok = (
    all(block.shape == (2, 2) for block in packet)
    and matrix_equal(assemble_packet(packet_gate), rho_singlet)
    and not any(rank_one_projector(block) for block in packet)
)
check(
    "host-codebook four-M2 preparation packet round trip",
    packet_ok,
    "8-site alternative only; primary's 9-Record anchored relational packet is not this gate",
)


# 5. Independently test all product Z/X probabilities and normalization.
rho_a = sp.diag(sp.Rational(3, 4), sp.Rational(1, 4))
rho_b = sp.Matrix(
    [[sp.Rational(1, 2), sp.Rational(1, 4)],
     [sp.Rational(1, 4), sp.Rational(1, 2)]]
)
rho_product = (
    rho_singlet
    if mutation == "product"
    else sp.kronecker_product(rho_a, rho_b)
)
product_values: list[sp.Expr] = []
product_ok = True
for outcome_a in (1, -1):
    for outcome_b in (1, -1):
        joint = joint_probability(rho_product, Z, X, outcome_a, outcome_b)
        separate = probability(rho_a, projector(Z, outcome_a)) * probability(
            rho_b, projector(X, outcome_b)
        )
        product_values.append(joint)
        product_ok = product_ok and scalar_equal(joint, separate) and nonnegative(joint)
product_ok = product_ok and scalar_equal(sum(product_values), 1)
check(
    "product preparation reduction",
    product_ok,
    "all four Z/X cells factor and normalize",
)


# 6. Reconstruct all Bell tables, no-signalling, and CHSH.
a_observables = (Z, X)
b_observables = (
    sp.simplify((Z + X) / SQRT2),
    sp.simplify((Z - X) / SQRT2),
)


def build_bell_tables(
    right_observables: tuple[sp.Matrix, sp.Matrix],
) -> dict[tuple[int, int], dict[tuple[int, int], sp.Expr]]:
    return {
        (x, y): {
            (outcome_a, outcome_b): joint_probability(
                rho_singlet,
                observable_a,
                observable_b,
                outcome_a,
                outcome_b,
            )
            for outcome_a in (1, -1)
            for outcome_b in (1, -1)
        }
        for x, observable_a in enumerate(a_observables)
        for y, observable_b in enumerate(right_observables)
    }


def table_correlation(table: dict[tuple[int, int], sp.Expr]) -> sp.Expr:
    return sp.simplify(sum(a * b * value for (a, b), value in table.items()))


bell = build_bell_tables(b_observables)
bell_gate_observables = (
    (b_observables[0], b_observables[0])
    if mutation == "bell"
    else b_observables
)
bell_gate = build_bell_tables(bell_gate_observables)
bell_ok = all(
    scalar_equal(sum(table.values()), 1)
    and all(nonnegative(value) for value in table.values())
    for table in bell_gate.values()
)
for x in range(2):
    for outcome_a in (1, -1):
        bell_ok = bell_ok and scalar_equal(
            sum(bell_gate[(x, 0)][(outcome_a, b)] for b in (1, -1)),
            sum(bell_gate[(x, 1)][(outcome_a, b)] for b in (1, -1)),
        )
for y in range(2):
    for outcome_b in (1, -1):
        bell_ok = bell_ok and scalar_equal(
            sum(bell_gate[(0, y)][(a, outcome_b)] for a in (1, -1)),
            sum(bell_gate[(1, y)][(a, outcome_b)] for a in (1, -1)),
        )
chsh = sp.simplify(
    table_correlation(bell_gate[(0, 0)])
    + table_correlation(bell_gate[(0, 1)])
    + table_correlation(bell_gate[(1, 0)])
    - table_correlation(bell_gate[(1, 1)])
)
bell_ok = bell_ok and scalar_equal(chsh, -2 * SQRT2)
check(
    "supplied global Bell history table",
    bell_ok,
    f"four normalized no-signalling tables give CHSH={chsh}",
)


# 7. Check both one-site reductions and both families of table marginals.
reduced_a = sp.Matrix(
    2, 2, lambda row, col: sum(rho_singlet[2 * row + k, 2 * col + k] for k in range(2))
)
reduced_b = sp.Matrix(
    2, 2, lambda row, col: sum(rho_singlet[2 * k + row, 2 * k + col] for k in range(2))
)
marginals_ok = matrix_equal(reduced_a, I2 / 2) and matrix_equal(reduced_b, I2 / 2)
for x in range(2):
    for y in range(2):
        for outcome in (1, -1):
            expected_left = (
                sp.Rational(3, 5)
                if mutation == "local_projection" and (x, y, outcome) == (0, 0, 1)
                else sp.Rational(1, 2)
            )
            marginals_ok = marginals_ok and scalar_equal(
                sum(bell[(x, y)][(outcome, b)] for b in (1, -1)),
                expected_left,
            )
            marginals_ok = marginals_ok and scalar_equal(
                sum(bell[(x, y)][(a, outcome)] for a in (1, -1)),
                sp.Rational(1, 2),
            )
check(
    "both-wing one-site projections",
    marginals_ok,
    "both reduced states and every left/right marginal equal I/2",
)


# 8. Test calibrated nearest-neighbour appends and a wrong-program hostile.
program_a, target_a = (-2, 0, 0), (-1, 0, 0)
target_b, program_b = (1, 0, 0), (2, 0, 0)
initial_ledger = {
    program_a: projector(a_observables[0], 1),
    program_b: projector(b_observables[0], 1),
}
content_a = projector(a_observables[0], 1)
content_b = projector(b_observables[0], -1)
prefix_a = append_registered_outcome(initial_ledger, program_a, target_a, content_a)
prefix_b = append_registered_outcome(initial_ledger, program_b, target_b, content_b)
final_ab = append_registered_outcome(prefix_a, program_b, target_b, content_b)
final_ba = append_registered_outcome(prefix_b, program_a, target_a, content_a)
final_ba_gate = prefix_b if mutation == "append" else final_ba
try:
    append_registered_outcome(initial_ledger, program_a, target_a, projector(Y, 1))
    wrong_program_rejected = False
except ValueError:
    wrong_program_rejected = True
try:
    append_registered_outcome(final_ab, program_a, target_a, content_a)
    occupied_rejected = False
except ValueError:
    occupied_rejected = True
append_ok = (
    adjacent(program_a, target_a)
    and adjacent(program_b, target_b)
    and not adjacent(target_a, target_b)
    and ledgers_equal(final_ab, final_ba_gate)
    and all(matrix_equal(final_ab[site], initial_ledger[site]) for site in initial_ledger)
    and wrong_program_rejected
    and occupied_rejected
)
check(
    "nonadjacent calibrated appends commute in the supplied causal layer",
    append_ok,
    "registered outcomes append once; wrong-setting content and rewrites are rejected",
)


# 9. Test every declared one-step Bell continuation from packet/program Records.
decoded = assemble_packet(packet)
bloch_vectors = (
    (sp.Integer(0), sp.Integer(0), sp.Integer(1)),
    (sp.Integer(1), sp.Integer(0), sp.Integer(0)),
)
bloch_b = (
    (1 / SQRT2, sp.Integer(0), 1 / SQRT2),
    (-1 / SQRT2, sp.Integer(0), 1 / SQRT2),
)
future_ok = matrix_equal(decoded, rho_singlet)
future_count = 0
for x, observable_a in enumerate(a_observables):
    for y, observable_b in enumerate(b_observables):
        dot = sp.simplify(sum(u * v for u, v in zip(bloch_vectors[x], bloch_b[y])))
        for outcome_a in (1, -1):
            continuation_ledger = {
                program_a: projector(observable_a, 1),
                program_b: projector(observable_b, 1),
            }
            continuation_ledger = append_registered_outcome(
                continuation_ledger,
                program_a,
                target_a,
                projector(observable_a, outcome_a),
            )
            if mutation == "record_fibre" and (x, y, outcome_a) == (0, 0, 1):
                continuation_ledger[program_b] = projector(Y, 1)
            recorded_a = continuation_ledger[target_a]
            recorded_b_program = continuation_ledger[program_b]
            prefix = branch(decoded, sp.kronecker_product(recorded_a, I2))
            denominator = sp.trace(prefix)
            future_ok = future_ok and scalar_equal(denominator, sp.Rational(1, 2))
            for outcome_b in (1, -1):
                recorded_b = (
                    recorded_b_program
                    if outcome_b == 1
                    else I2 - recorded_b_program
                )
                effect_b = sp.kronecker_product(I2, recorded_b)
                reconstructed = sp.simplify(probability(prefix, effect_b) / denominator)
                expected = sp.simplify((1 - outcome_a * outcome_b * dot) / 2)
                future_ok = future_ok and scalar_equal(reconstructed, expected)
                future_count += 1
check(
    "finite packet-and-outcome continuation calculator",
    future_ok and future_count == 16,
    "all 16 use outcome/program Records; this is a global calculator, not a local B-site kernel",
)


# 10. A supplied coordinate selects a member without changing the law table.
member_keys = ((1, 1), (1, -1), (-1, 1), (-1, -1))
member_weights = tuple(bell[(0, 0)][key] for key in member_keys)
weights_before = tuple(member_weights)
member_low = choose_member(member_weights, sp.Rational(1, 20))
member_high_coordinate = (
    sp.Rational(1, 20) if mutation == "actuality" else sp.Rational(19, 20)
)
member_high = choose_member(member_weights, member_high_coordinate)
member_ok = (
    scalar_equal(sum(member_weights), 1)
    and all(nonnegative(value) for value in member_weights)
    and member_low == 0
    and member_high == 3
    and member_low != member_high
    and nonnegative(member_weights[member_low])
    and nonnegative(member_weights[member_high])
    and member_weights == weights_before
)
check(
    "law table versus supplied realized-member coordinate",
    member_ok,
    "coordinates 1/20 and 19/20 select distinct positive cells; coordinate origin is not derived",
)


# 11. Strengthen the supplied competing-hazard consistency checks.
gamma, time = sp.symbols("gamma time", positive=True, real=True)
hazards = tuple(sp.simplify(gamma * value) for value in member_weights)
hazards_gate = list(hazards)
if mutation == "cadence":
    hazards_gate[0] = sp.simplify(2 * hazards_gate[0])
survival = sp.exp(-gamma * time)
integrated_density = sp.integrate(
    sum(hazards_gate) * survival, (time, 0, sp.oo)
)
hazard_ok = (
    all(nonnegative(hazard) for hazard in hazards_gate)
    and scalar_equal(sum(hazards_gate), gamma)
    and scalar_equal(survival.subs(time, 0), 1)
    and scalar_equal(sp.limit(survival, time, sp.oo), 0)
    and scalar_equal(-sp.diff(survival, time) / survival, gamma)
    and scalar_equal(integrated_density, 1)
)
check(
    "supplied nonnegative hazards and survival cadence",
    hazard_ok,
    "hazards are nonnegative, total gamma, S(0)=1, S(infinity)=0, and density integrates to 1",
)


# 12. Cross-check used features against supplied/open inputs and finite resources.
feature_requirements = {
    "packet": {"packet_codebook", "packet_genesis", "fixture_geometry"},
    "history": {
        "projective_program_domain",
        "trace_history_functional",
        "global_joint_coupling",
    },
    "append": {"event_registration", "formation_schedule"},
    "actual_member": {"external_history_coordinate"},
    "hazards": {"formation_cadence", "process_time_semantics"},
}
required_imports = set().union(*feature_requirements.values())
declared_status = {
    "packet_codebook": "benchmark_boundary",
    "packet_genesis": "benchmark_boundary",
    "fixture_geometry": "benchmark_boundary",
    "projective_program_domain": "selected_sector_law",
    "trace_history_functional": "selected_sector_law",
    "global_joint_coupling": "selected_sector_law",
    "event_registration": "selected_sector_law",
    "formation_schedule": "benchmark_process",
    "external_history_coordinate": "contingent_world_data",
    "formation_cadence": "benchmark_process",
    "process_time_semantics": "benchmark_process",
}
selected_sector_law_fields = {
    name for name, status in declared_status.items() if status == "selected_sector_law"
}
open_boundaries = {
    "Admissibility derivation",
    "autonomous covariant genesis",
    "physical clock calibration",
    "resource renewal",
    "actual-member origin",
    "global Record-fibre lumpability",
}
resource_counts = {
    "program_sites": len(initial_ledger),
    "packet_sites": len(packet),
    "fresh_targets": len(set(final_ab) - set(initial_ledger)),
    "complete_fixture_sites": len(set(final_ab) | {(-4, k, 0) for k in range(4)}),
}
resource_counts_gate = dict(resource_counts)
if mutation == "ledger":
    resource_counts_gate["packet_sites"] -= 1
boundary_ok = (
    required_imports == set(declared_status)
    and all(status != "derived" for status in declared_status.values())
    and selected_sector_law_fields
    == {
        "projective_program_domain",
        "trace_history_functional",
        "global_joint_coupling",
        "event_registration",
    }
    and resource_counts_gate
    == {
        "program_sites": 2,
        "packet_sites": 4,
        "fresh_targets": 2,
        "complete_fixture_sites": 8,
    }
    and len(open_boundaries) == 6
)
check(
    "executable import and finite-resource ledger",
    boundary_ok,
    "4 selected kernel fields; benchmark/history inputs remain explicit; "
    "8-site host-codebook alternative (primary anchored fixture has 9)",
)


for result in results:
    status = "PASS" if result.passed else "FAIL"
    print(f"[{status}] {result.name}: {result.detail}")

passed = sum(result.passed for result in results)
failed = len(results) - passed
print(f"TOTAL: PASS={passed} FAIL={failed}")
raise SystemExit(0 if failed == 0 else 1)
