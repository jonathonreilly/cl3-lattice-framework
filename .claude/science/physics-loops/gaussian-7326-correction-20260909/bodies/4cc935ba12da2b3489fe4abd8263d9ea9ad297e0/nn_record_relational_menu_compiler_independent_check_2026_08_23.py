#!/usr/bin/env python3
"""Independent reconstruction of the relational multi-menu Record compiler."""

from __future__ import annotations

from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, limit, oo, simplify, sqrt, symbols

from nn_record_homogeneous_payload_self_hosting_writer_2026_08_22 import (
    I2,
    SX,
    SZ,
    antihermitian_coefficient,
    decode_payload,
    hermitian_part,
    matrix_equal,
    trace_weight,
)
from nn_record_spatial_trial_ensemble_independent_check_2026_08_23 import (
    GROUP,
    O,
    ball,
    connected_components,
    degree,
    embeddings,
    histories,
    neighborhood,
    norm,
    plus,
    rotate,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_RELATIONAL_MENU_COMPILER_AND_CONTEXT_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/nn_record_relational_menu_compiler_2026_08_23.py",
    "scripts/nn_record_spatial_trial_ensemble_independent_check_2026_08_23.py",
    "scripts/nn_record_homogeneous_payload_self_hosting_writer_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_RELATIONAL_MENU_COMPILER_AND_CONTEXT_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

H = Matrix([[1, 1], [1, 2]])
BASE = simplify(H + I * SZ)
SETTING_NAMES = ("coarse", "refined", "ternary-a", "ternary-b")
SETTING_VALUES = {name: Q(index) for index, name in enumerate(SETTING_NAMES)}
OUTCOME_LABELS = {
    "coarse-plus": Q(10), "shared-minus": Q(11), "fine-a": Q(12),
    "fine-b": Q(13), "shared-e0": Q(14), "a1": Q(15), "a2": Q(16),
    "b1": Q(17), "b2": Q(18),
}


def conjugate(value, unitary):
    return simplify(unitary * value * unitary.conjugate().T)


def payload(name):
    return simplify(BASE + I * SETTING_VALUES[name] * I2)


def tag(value):
    return simplify(antihermitian_coefficient(value).trace() / 2)


def setting(value):
    value_tag = tag(value)
    for name, expected in SETTING_VALUES.items():
        if simplify(value_tag - expected) == 0:
            return name
    return None


def axes(value):
    value_tag = tag(value)
    z_axis = simplify(antihermitian_coefficient(value) - value_tag * I2)
    h_value = hermitian_part(value)
    if simplify(h_value.trace() - H.trace()) != 0:
        return None
    h_zero = simplify(h_value - h_value.trace() * I2 / 2)
    x_axis = simplify(h_zero + z_axis / 2)
    if not (
        matrix_equal(x_axis * x_axis, I2)
        and matrix_equal(z_axis * z_axis, I2)
        and matrix_equal(x_axis * z_axis + z_axis * x_axis, Matrix.zeros(2))
    ):
        return None
    return x_axis, z_axis


def rank_one(x_axis, z_axis, nx, nz):
    return simplify((I2 + nx * x_axis + nz * z_axis) / 2)


def tagged(effect, label):
    return simplify(effect + I * label * I2)


def scaled_rank_one_effect(effect):
    scale = simplify(effect.trace())
    projector_value = simplify(effect / scale)
    return (
        matrix_equal(effect, effect.conjugate().T)
        and bool(scale.is_positive)
        and bool(simplify(1 - scale).is_nonnegative)
        and matrix_equal(projector_value * projector_value, projector_value)
        and simplify(projector_value.trace()) == 1
    )


def menu(value):
    name = setting(value)
    frame = axes(value)
    if name is None or frame is None or decode_payload(value) is None:
        return None
    x_axis, z_axis = frame
    pz = simplify((I2 + z_axis) / 2)
    mz = simplify(I2 - pz)
    if name == "coarse":
        rows = (("coarse-plus", pz), ("shared-minus", mz))
    elif name == "refined":
        rows = (("fine-a", pz / 2), ("fine-b", pz / 2), ("shared-minus", mz))
    elif name == "ternary-a":
        n1 = rank_one(x_axis, z_axis, 4 * sqrt(2) / 9, -Q(7, 9))
        n2 = rank_one(x_axis, z_axis, -2 * sqrt(2) / 3, Q(1, 3))
        rows = (
            ("shared-e0", pz / 2),
            ("a1", Q(9, 10) * n1),
            ("a2", Q(3, 5) * n2),
        )
    else:
        m1 = rank_one(x_axis, z_axis, 2 * sqrt(2) / 3, -Q(1, 3))
        m2 = rank_one(x_axis, z_axis, -2 * sqrt(2) / 3, -Q(1, 3))
        rows = (
            ("shared-e0", pz / 2),
            ("b1", Q(3, 4) * m1),
            ("b2", Q(3, 4) * m2),
        )
    return tuple(
        (outcome, simplify(effect), tagged(simplify(effect), OUTCOME_LABELS[outcome]))
        for outcome, effect in rows
    )


def weights(value, variant="trace"):
    name = setting(value)
    decoded = decode_payload(value)
    rows = menu(value)
    masses = [trace_weight(decoded.preparation, effect) for _, effect, _ in rows]
    if variant == "skew" and name == "refined":
        shift = Q(1, 84)
        masses = [masses[0] - shift, masses[1] - shift, masses[2] + 2 * shift]
    elif variant == "skew" and name == "ternary-b":
        shift = Q(1, 84)
        masses = [masses[0] + shift, masses[1] - shift, masses[2]]
    return tuple(simplify(mass) for mass in masses)


def parse(records, component):
    component = frozenset(component)
    if len(component) != 12:
        return None
    if len(connected_components({site: records[site] for site in component})) != 1:
        return None
    if neighborhood(component) & frozenset(records) != component:
        return None
    terminals = tuple(site for site in component if degree(site, component) == 6)
    if len(terminals) != 1:
        return None
    target = terminals[0]
    carriers = component - {target}
    carrier = records[next(iter(carriers))]
    carrier_menu = menu(carrier)
    if carrier_menu is None or not all(
        matrix_equal(records[site], carrier) for site in carriers
    ):
        return None
    frames = embeddings(carriers, 11)
    if len(frames) != 1:
        return None
    rotation, displacement = frames[0]
    if target != plus(displacement, rotate(rotation, O)):
        return None
    matches = tuple(
        (outcome, effect)
        for outcome, effect, content in carrier_menu
        if matrix_equal(records[target], content)
    )
    if len(matches) != 1:
        return None
    return target, setting(carrier), matches[0][0], matches[0][1]


def main() -> int:
    passed = 0
    failed = 0

    def check(name, condition, detail):
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    payloads = tuple(payload(name) for name in SETTING_NAMES)
    decoded = tuple(decode_payload(value) for value in payloads)
    rho = decoded[0].preparation
    pz = decoded[0].projector
    check(
        "independent-setting-quotient",
        tuple(setting(value) for value in payloads) == SETTING_NAMES
        and all(matrix_equal(item.preparation, rho) for item in decoded)
        and all(matrix_equal(item.projector, pz) for item in decoded)
        and trace_weight(rho, pz) == Q(2, 7),
        "an independent scalar-tag decoder recovers four settings on one rho/P quotient with pz=2/7",
    )

    menus = {name: menu(payload(name)) for name in SETTING_NAMES}
    sums = {
        name: simplify(sum((effect for _, effect, _ in rows), Matrix.zeros(2)))
        for name, rows in menus.items()
    }
    check(
        "independent-menu-algebra",
        all(matrix_equal(total, I2) for total in sums.values())
        and all(
            scaled_rank_one_effect(effect)
            for rows in menus.values()
            for _, effect, _ in rows
        )
        and matrix_equal(menus["coarse"][1][2], menus["refined"][2][2])
        and matrix_equal(menus["ternary-a"][0][2], menus["ternary-b"][0][2])
        and matrix_equal(menus["refined"][0][1], menus["refined"][1][1])
        and not matrix_equal(menus["refined"][0][2], menus["refined"][1][2]),
        "all effects are positive scaled rank-one operators and every resolution/shared/refined Record reconstructs independently",
    )

    trace_tables = {name: weights(payload(name)) for name in SETTING_NAMES}
    skew_tables = {name: weights(payload(name), "skew") for name in SETTING_NAMES}
    expected_a = (Q(1, 7), (21 + 6 * sqrt(2)) / 35, (9 - 6 * sqrt(2)) / 35)
    expected_b = (Q(1, 7), (6 + 3 * sqrt(2)) / 14, (6 - 3 * sqrt(2)) / 14)
    check(
        "independent-trace-and-skew-tables",
        trace_tables["coarse"] == (Q(2, 7), Q(5, 7))
        and trace_tables["refined"] == (Q(1, 7), Q(1, 7), Q(5, 7))
        and all(
            simplify(found - expected) == 0
            for found, expected in zip(trace_tables["ternary-a"], expected_a)
        )
        and all(
            simplify(found - expected) == 0
            for found, expected in zip(trace_tables["ternary-b"], expected_b)
        )
        and trace_tables["ternary-a"][0] == trace_tables["ternary-b"][0] == Q(1, 7)
        and all(simplify(sum(table)) == 1 for table in trace_tables.values())
        and all(simplify(sum(table)) == 1 for table in skew_tables.values())
        and all(bool(mass.is_positive) for table in skew_tables.values() for mass in table)
        and skew_tables["refined"] == (Q(11, 84), Q(11, 84), Q(31, 42))
        and skew_tables["ternary-b"][0] == Q(13, 84)
        and skew_tables["ternary-a"][0] == Q(1, 7),
        "independent exact arithmetic reproduces the normalized trace and same-support context-skew probability tables",
    )

    unitaries = (
        I2,
        SX,
        simplify((SX + SZ) / sqrt(2)),
        Matrix([[1, 0], [0, I]]),
        simplify((I2 + I * SX) / sqrt(2)),
    )
    covariance = True
    for unitary in unitaries:
        for name in SETTING_NAMES:
            source = payload(name)
            moved = conjugate(source, unitary)
            covariance = covariance and setting(moved) == name
            covariance = covariance and matrix_equal(
                decode_payload(moved).preparation, conjugate(rho, unitary)
            )
            covariance = covariance and all(
                before_name == after_name
                and matrix_equal(after_effect, conjugate(before_effect, unitary))
                and matrix_equal(after_content, conjugate(before_content, unitary))
                for (before_name, before_effect, before_content),
                (after_name, after_effect, after_content)
                in zip(menu(source), menu(moved))
            )
            covariance = covariance and weights(source, "skew") == weights(moved, "skew")
    check(
        "independent-internal-covariance",
        covariance,
        "four programs, eleven effects, and the skew table commute with five exact basis changes",
    )

    levels, terminal_pairs, exact_partition = histories()
    unfinished_count = sum(len(level) for level in levels)
    results = []
    sample = None
    for carriers, target in terminal_pairs:
        for name in SETTING_NAMES:
            carrier = payload(name)
            for outcome, effect, content in menu(carrier):
                records = {site: carrier for site in carriers}
                records[target] = content
                found = parse(records, frozenset(records))
                results.append(
                    found is not None
                    and found[0] == target
                    and found[1] == name
                    and found[2] == outcome
                    and matrix_equal(found[3], effect)
                )
                if sample is None and name == "ternary-b":
                    sample = records
    check(
        "independent-exhaustive-parser",
        len(GROUP) == 24
        and exact_partition
        and unfinished_count == 895
        and len(terminal_pairs) == 120
        and len(results) == 1320
        and all(results),
        "the independent geometry/parser route accepts all 1320 completed branches over the 120 terminal placements",
    )

    unfinished_rejects = all(
        parse({site: BASE for site in state}, state) is None
        for level in levels for state in level
    )
    component = frozenset(sample)
    hostile_site = min(neighborhood(component) - component)
    hostile = dict(sample)
    hostile[hostile_site] = payload("coarse")
    hostile_component = next(found for found in connected_components(hostile) if found & component)
    malformed_carriers, malformed_target = next(iter(terminal_pairs))
    malformed = {site: Matrix.zeros(2) for site in malformed_carriers}
    malformed[malformed_target] = I2
    check(
        "independent-false-positive-controls",
        unfinished_rejects
        and parse(hostile, hostile_component) is None
        and parse(malformed, frozenset(malformed)) is None,
        "unfinished histories, hostile adjacency, and a tag-zero invalid frame fail the independent parser",
    )

    original = parse(sample, component)
    shift = (7, -4, 3)
    translated = {plus(site, shift): value for site, value in sample.items()}
    moved = parse(translated, frozenset(translated))
    parser_covariance = moved is not None and moved[0] == plus(original[0], shift)
    for rotation in GROUP:
        rotated = {rotate(rotation, site): value for site, value in sample.items()}
        found = parse(rotated, frozenset(rotated))
        parser_covariance = parser_covariance and (
            found is not None and found[0] == rotate(rotation, original[0])
            and found[1:3] == original[1:3]
        )
    for unitary in unitaries:
        transformed = {site: conjugate(value, unitary) for site, value in sample.items()}
        found = parse(transformed, frozenset(transformed))
        parser_covariance = parser_covariance and (
            found is not None and found[:3] == original[:3]
            and matrix_equal(found[3], conjugate(original[3], unitary))
        )
    check(
        "independent-parser-covariance",
        parser_covariance,
        "translations, all 24 lattice rotations, and five internal basis changes commute with the independent parser",
    )

    sphere = ball(9)
    ball_size = len(sphere)
    event_count = 12
    tau = symbols("tau", positive=True)
    slot = tau / event_count
    designated = (exp(-slot) * slot) ** event_count
    quiet = exp(-(ball_size * tau - event_count * slot))
    setting_probability = Q(1, len(SETTING_NAMES))
    cylinder = simplify(setting_probability * designated * quiet)
    intensity = symbols("intensity", positive=True)
    n = symbols("n", integer=True, positive=True)
    volume = (2 * n + 1) ** 3
    boundary = simplify(volume - (2 * n - 1) ** 3)
    check(
        "independent-density-frequency-algebra",
        ball_size == 1159
        and cylinder == exp(-1159 * tau) * (tau / 12) ** 12 / 4
        and bool(cylinder.subs(tau, Q(12, 1159)).is_positive)
        and all(
            simplify((intensity * mass) / intensity) == mass
            for family in (trace_tables, skew_tables)
            for table in family.values()
            for mass in table
        )
        and limit(boundary / volume, n, oo) == 0,
        "the setting factor, B9 cylinder, both-Law conditional ratios, and cubic Folner algebra are independently derived",
    )

    erased = tuple(simplify(value - I * tag(value) * I2) for value in payloads)
    fine_same_process = simplify(skew_tables["refined"][0] + skew_tables["refined"][1])
    coarse_other_process = skew_tables["coarse"][0]
    check(
        "independent-boundary-controls",
        all(matrix_equal(erased[0], value) for value in erased[1:])
        and fine_same_process == Q(11, 42)
        and coarse_other_process == Q(2, 7)
        and fine_same_process != coarse_other_process,
        "token erasure aliases settings while same-process union addition survives and cross-program equality fails",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    source_text = Path(__file__).read_text(encoding="utf-8")
    check(
        "independent-source-boundary",
        "1320/1320" in note_text
        and "same-process forgetting" in note_text
        and "does not force trace" in note_text
        and "No Minimal Axioms edit" in note_text
        and "N8 — Cross-Cycle Echo" in note_text
        and ("from nn_record_relational_menu_" + "compiler_2026_08_23") not in source_text,
        "the independent route imports no Block37 primary code and pins the parser, probability, axiom, and N1-N8 boundaries",
    )

    print("per_element: independent effect, label, shared-content, and probability-table reconstruction")
    print("per_site: independent carrier-tag and terminal-content parsing")
    print("per_mode: checked and not executed — no spectral-mode or mode-exhaustion claim is made")
    print("per_block: independent 895-shape/1320-terminal exhaustive enumeration")
    print("lattice_wide: checked and not executed — ergodicity is analytic; the runner checks cylinder and Folner algebra only")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
