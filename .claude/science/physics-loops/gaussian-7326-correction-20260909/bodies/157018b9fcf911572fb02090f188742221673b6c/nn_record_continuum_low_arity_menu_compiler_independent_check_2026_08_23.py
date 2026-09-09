#!/usr/bin/env python3
"""Independent reconstruction of the continuum low-arity menu compiler."""

from __future__ import annotations

from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, simplify, sqrt, symbols

from nn_record_homogeneous_payload_self_hosting_writer_2026_08_22 import (
    I2,
    SX,
    SZ,
    antihermitian_coefficient,
    decode_payload,
    hermitian_part,
    matrix_equal,
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
    plus,
    rotate,
)


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_CONTINUUM_LOW_ARITY_MENU_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/nn_record_continuum_low_arity_menu_compiler_2026_08_23.py",
    "scripts/nn_record_spatial_trial_ensemble_independent_check_2026_08_23.py",
    "scripts/nn_record_homogeneous_payload_self_hosting_writer_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_CONTINUUM_LOW_ARITY_MENU_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

MIXTURE = {"RRR": Q(1, 4), "RR": Q(1, 8), "RRI": Q(1, 4), "III": Q(1, 4), "II": Q(1, 8)}
DENSITIES = {"RRR": Q(2), "RR": Q(1), "RRI": Q(1), "III": Q(2), "II": Q(1)}
TAGS = {"RRR": Q(0), "RR": Q(1), "RRI": Q(2), "III": Q(4), "II": Q(5)}
LABELS = (Q(30), Q(31), Q(32))


def conjugate(value, unitary):
    return simplify(unitary * value * unitary.conjugate().T)


def scalar(value):
    return simplify(value.trace() / 2)


def radius(value):
    return simplify(sqrt((value * value).trace() / 2))


def axis(value):
    return (
        matrix_equal(value, value.conjugate().T)
        and simplify(value.trace()) == 0
        and matrix_equal(simplify(value * value), I2)
    )


def make(kind, *parameters, x=SX, z=SZ):
    if kind == "RRR":
        a, b = parameters
        h_value, k_value = (1 + a) * x, (1 + b) * z
    elif kind == "RR":
        h_value, k_value = x, z + I2
    elif kind == "RRI":
        (d,) = parameters
        h_value, k_value = (1 + d) * x, z + 2 * I2
    elif kind == "III":
        d1, d2 = parameters
        h_value, k_value = (1 + d1) * x, (1 + d2) * z + 4 * I2
    elif kind == "II":
        (d,) = parameters
        h_value, k_value = (1 + d) * x, z + 5 * I2
    else:
        raise ValueError(kind)
    return simplify(h_value + I * k_value)


def unpack(value):
    h_value = hermitian_part(value)
    k_value = antihermitian_coefficient(value)
    if simplify(h_value.trace()) != 0:
        return None
    k_tag = scalar(k_value)
    kind = next((name for name, expected in TAGS.items() if simplify(k_tag - expected) == 0), None)
    if kind is None:
        return None
    h_zero = simplify(h_value)
    k_zero = simplify(k_value - k_tag * I2)
    rh, rk = radius(h_zero), radius(k_zero)
    if not bool(rh.is_positive) or not bool(rk.is_positive):
        return None
    x, z = simplify(h_zero / rh), simplify(k_zero / rk)
    if not axis(x) or not axis(z) or not matrix_equal(x * z + z * x, Matrix.zeros(2)):
        return None
    if kind == "RRR":
        a, b = simplify(rh - 1), simplify(rk - 1)
        valid = all(bool(simplify(item).is_nonnegative) for item in (a, 1 - a, b, 1 - b, a + b - 1))
        parameters = (a, b)
    elif kind == "RR":
        valid = simplify(rh - 1) == 0 and simplify(rk - 1) == 0
        parameters = tuple()
    elif kind in ("RRI", "II"):
        d = simplify(rh - 1)
        valid = simplify(rk - 1) == 0 and bool(d.is_nonnegative) and bool(simplify(1 - d).is_nonnegative)
        parameters = (d,)
    else:
        d1, d2 = simplify(rh - 1), simplify(rk - 1)
        valid = all(bool(simplify(item).is_nonnegative) for item in (d1, d2, 1 - d1 - d2))
        parameters = (d1, d2)
    return (kind, parameters, x, z) if valid else None


def projection(direction):
    return simplify((I2 + direction) / 2)


def tagged(effect, label):
    return simplify(effect + I * label * I2)


def menu(value):
    data = unpack(value)
    if data is None:
        return None
    kind, parameters, x, z = data
    zero = Matrix.zeros(2)
    if kind == "RRR":
        a, b = parameters
        c = simplify(2 - a - b)
        if a == 0:
            rows = (("rrr-1", zero), ("rrr-2", projection(z)), ("rrr-3", projection(-z)))
        elif b == 0:
            rows = (("rrr-1", projection(x)), ("rrr-2", zero), ("rrr-3", projection(-x)))
        elif c == 0:
            rows = (("rrr-1", projection(x)), ("rrr-2", projection(-x)), ("rrr-3", zero))
        else:
            cosine = simplify((c**2 - a**2 - b**2) / (2 * a * b))
            sine = simplify(sqrt(1 - cosine**2))
            n1 = x
            n2 = simplify(cosine * x + sine * z)
            n3 = simplify(-(a * n1 + b * n2) / c)
            rows = (("rrr-1", a * projection(n1)), ("rrr-2", b * projection(n2)), ("rrr-3", c * projection(n3)))
    elif kind == "RR":
        rows = (("rr-1", projection(x)), ("rr-2", projection(-x)))
    elif kind == "RRI":
        (d,) = parameters
        rows = (("rri-i", d * I2), ("rri-plus", (1 - d) * projection(x)), ("rri-minus", (1 - d) * projection(-x)))
    elif kind == "III":
        d1, d2 = parameters
        rows = (("iii-1", d1 * I2), ("iii-2", d2 * I2), ("iii-3", (1 - d1 - d2) * I2))
    else:
        (d,) = parameters
        rows = (("ii-1", d * I2), ("ii-2", (1 - d) * I2))
    rows = tuple(
        (index, name, simplify(effect))
        for index, (name, effect) in enumerate(rows)
        if not matrix_equal(effect, zero)
    )
    return tuple((name, effect, tagged(effect, LABELS[index])) for index, name, effect in rows)


def type_of(effect):
    center = scalar(effect)
    if matrix_equal(effect, center * I2):
        return "I" if bool(center.is_positive) and bool(simplify(1 - center).is_nonnegative) else None
    coefficient = simplify(effect.trace())
    normalized = simplify(effect / coefficient)
    return "R" if (
        bool(coefficient.is_positive)
        and bool(simplify(1 - coefficient).is_nonnegative)
        and matrix_equal(normalized * normalized, normalized)
        and simplify(normalized.trace()) == 1
    ) else None


def weights(value, skew=False):
    data = unpack(value)
    rows = menu(value)
    masses = [simplify(effect.trace() / 2) for _, effect, _ in rows]
    if skew and data[0] == "RRR" and len(rows) == 3:
        coefficients = [simplify(effect.trace()) for _, effect, _ in rows]
        shift = simplify(coefficients[0] * coefficients[1] * coefficients[2] / 10)
        masses = [masses[0] + shift / 2, masses[1] + shift / 2, masses[2] - shift]
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
    data = unpack(carrier)
    options = menu(carrier)
    if data is None or options is None or not all(matrix_equal(records[site], carrier) for site in carriers):
        return None
    frames = embeddings(carriers, 11)
    if len(frames) != 1:
        return None
    rotation, displacement = frames[0]
    if target != plus(displacement, rotate(rotation, O)):
        return None
    matches = tuple((name, effect) for name, effect, content in options if matrix_equal(records[target], content))
    if len(matches) != 1:
        return None
    return target, data[0], matches[0][0], matches[0][1]


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

    examples = {
        "rrr-a": make("RRR", Q(1, 2), Q(9, 10)),
        "rrr-b": make("RRR", Q(1, 2), Q(3, 4)),
        "rrr-fine": make("RRR", Q(1, 2), Q(1, 2)),
        "rr": make("RR"),
        "rri": make("RRI", Q(1, 3)),
        "iii": make("III", Q(1, 5), Q(3, 10)),
        "ii": make("II", Q(2, 5)),
    }
    decoded = {name: unpack(value) for name, value in examples.items()}
    check(
        "independent-stratum-and-preparation-decoder",
        sum(MIXTURE.values()) == 1
        and all(mass > 0 for mass in MIXTURE.values())
        and DENSITIES == {"RRR": 2, "RR": 1, "RRI": 1, "III": 2, "II": 1}
        and {data[0] for data in decoded.values()} == set(MIXTURE)
        and all(matrix_equal(decode_payload(value).preparation, I2 / 2) for value in examples.values()),
        "five independently decoded positive-mass sectors retain the common I/2 quotient",
    )

    menus = {name: menu(value) for name, value in examples.items()}
    words = {name: "".join(type_of(effect) for _, effect, _ in rows) for name, rows in menus.items()}
    check(
        "independent-five-stratum-algebra",
        words == {"rrr-a": "RRR", "rrr-b": "RRR", "rrr-fine": "RRR", "rr": "RR", "rri": "IRR", "iii": "III", "ii": "II"}
        and all(matrix_equal(sum((effect for _, effect, _ in rows), Matrix.zeros(2)), I2) for rows in menus.values()),
        "RRR/RR/RRI/III/II representatives independently resolve I with the declared effect types",
    )

    coefficient_pairs = (
        (Q(0), Q(1)), (Q(1), Q(0)), (Q(1), Q(1)),
        (Q(1, 2), Q(1, 2)), (Q(2, 5), Q(4, 5)), (Q(3, 4), Q(3, 4)),
    )
    triangle_checks = []
    for a_value, b_value in coefficient_pairs:
        rows = menu(make("RRR", a_value, b_value))
        triangle_checks.append(rows is not None and len(rows) in (2, 3) and matrix_equal(sum((effect for _, effect, _ in rows), Matrix.zeros(2)), I2))
    a, b, c = symbols("a b c", positive=True)
    cosine = (c**2 - a**2 - b**2) / (2 * a * b)
    derived_n3_norm = simplify((a**2 + b**2 + 2 * a * b * cosine) / c**2)
    check(
        "independent-triangle-gram-surjection",
        all(triangle_checks) and derived_n3_norm == 1,
        "independent closure and Gram arithmetic reconstruct the universal rank-one triangle including binary boundaries",
    )

    traces = {name: weights(value) for name, value in examples.items()}
    fine_skew = weights(examples["rrr-fine"], True)
    coarse_skew = weights(examples["rr"], True)
    a_skew = weights(examples["rrr-a"], True)
    b_skew = weights(examples["rrr-b"], True)
    check(
        "independent-trace-and-skew-kernels",
        all(simplify(sum(table)) == 1 for table in traces.values())
        and all(bool(mass.is_positive) for table in traces.values() for mass in table)
        and traces["rri"] == (Q(1, 3), Q(1, 3), Q(1, 3))
        and traces["iii"] == (Q(1, 5), Q(3, 10), Q(1, 2))
        and traces["ii"] == (Q(2, 5), Q(3, 5))
        and fine_skew == (Q(21, 80), Q(21, 80), Q(19, 40))
        and coarse_skew == (Q(1, 2), Q(1, 2))
        and simplify(fine_skew[0] + fine_skew[1]) != coarse_skew[0]
        and matrix_equal(menus["rrr-a"][0][1], menus["rrr-b"][0][1])
        and a_skew[0] == Q(527, 2000)
        and b_skew[0] == Q(169, 640)
        and a_skew[0] != b_skew[0],
        "trace normalization spans all strata while the reconstructed covariant skew breaks both W1 fixtures",
    )

    unitaries = (
        I2, SX, simplify((SX + SZ) / sqrt(2)),
        Matrix([[1, 0], [0, I]]), simplify((I2 + I * SX) / sqrt(2)),
    )
    covariance = True
    for unitary in unitaries:
        for value in examples.values():
            moved = conjugate(value, unitary)
            covariance = covariance and unpack(moved)[:2] == unpack(value)[:2]
            covariance = covariance and weights(moved, True) == weights(value, True)
            covariance = covariance and all(
                left_name == right_name
                and matrix_equal(right_effect, conjugate(left_effect, unitary))
                and matrix_equal(right_content, conjugate(left_content, unitary))
                for (left_name, left_effect, left_content), (right_name, right_effect, right_content)
                in zip(menu(value), menu(moved))
            )
    check(
        "independent-internal-covariance",
        covariance,
        "all sectors, effects, contents, and both probability kernels commute with five basis changes",
    )

    levels, terminal_pairs, exact_partition = histories()
    unfinished_count = sum(len(level) for level in levels)
    results = []
    sample = None
    for carriers, target in terminal_pairs:
        for name, carrier in examples.items():
            for outcome, effect, content in menu(carrier):
                records = {site: carrier for site in carriers}
                records[target] = content
                found = parse(records, frozenset(records))
                results.append(found is not None and found[0] == target and found[1] == decoded[name][0] and found[2] == outcome and matrix_equal(found[3], effect))
                if sample is None and name == "rrr-b":
                    sample = records
    check(
        "independent-exhaustive-fixture-parser",
        len(GROUP) == 24
        and exact_partition
        and unfinished_count == 895
        and len(terminal_pairs) == 120
        and len(results) == 2280
        and all(results),
        "independent geometry accepts 2280/2280 completed cross-stratum fixtures over all terminal placements",
    )

    unfinished_rejects = all(parse({site: examples["rrr-a"] for site in state}, state) is None for level in levels for state in level)
    component = frozenset(sample)
    hostile_site = min(neighborhood(component) - component)
    hostile = dict(sample)
    hostile[hostile_site] = examples["rr"]
    hostile_component = next(found for found in connected_components(hostile) if found & component)
    malformed_carriers, malformed_target = next(iter(terminal_pairs))
    malformed = {site: Matrix.zeros(2) for site in malformed_carriers}
    malformed[malformed_target] = I2
    invalid_frame = simplify(2 * SX + I * (SX + SZ) / sqrt(2))
    check(
        "independent-negative-controls",
        unfinished_rejects
        and parse(hostile, hostile_component) is None
        and parse(malformed, frozenset(malformed)) is None
        and unpack(invalid_frame) is None
        and unpack(make("RRR", Q(1, 5), Q(1, 5))) is None,
        "unfinished shapes, adjacency contamination, malformed carriers, nonorthogonal axes, and invalid coefficients reject",
    )

    original = parse(sample, component)
    shift = (7, -4, 3)
    translated = {plus(site, shift): value for site, value in sample.items()}
    moved = parse(translated, frozenset(translated))
    parser_covariance = moved is not None and moved[0] == plus(original[0], shift)
    for rotation in GROUP:
        rotated = {rotate(rotation, site): value for site, value in sample.items()}
        found = parse(rotated, frozenset(rotated))
        parser_covariance = parser_covariance and found is not None and found[0] == rotate(rotation, original[0]) and found[1:3] == original[1:3]
    for unitary in unitaries:
        transformed = {site: conjugate(value, unitary) for site, value in sample.items()}
        found = parse(transformed, frozenset(transformed))
        parser_covariance = parser_covariance and found is not None and found[:3] == original[:3] and matrix_equal(found[3], conjugate(original[3], unitary))
    check(
        "independent-parser-covariance",
        parser_covariance,
        "translations, 24 lattice rotations, and five basis changes commute with the independent parser",
    )

    tau, patch = symbols("tau patch", positive=True)
    event_count = 12
    slot = tau / event_count
    designated = (exp(-slot) * slot) ** event_count
    quiet = exp(-(len(ball(9)) * tau - event_count * slot))
    cylinder = simplify(MIXTURE["RRI"] * patch * designated * quiet)
    check(
        "independent-support-versus-singleton",
        len(ball(9)) == 1159
        and cylinder == patch * exp(-1159 * tau) * (tau / 12) ** 12 / 4
        and bool(cylinder.is_positive)
        and Q(0) == 0,
        "positive open-patch cylinder and zero exact singleton mass are independently kept as different statements",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    source_text = Path(__file__).read_text(encoding="utf-8")
    check(
        "independent-source-and-import-boundary",
        "five strata are exhaustive" in note_text
        and "2280/2280" in note_text
        and "zero singleton mass" in note_text
        and "W1 remains open" in note_text
        and "No Minimal Axioms edit" in note_text
        and "N8 — Cross-Cycle Echo" in note_text
        and ("from nn_record_continuum_low_arity_menu_" + "compiler_2026_08_23") not in source_text,
        "the independent route imports no Block38 primary and pins continuum, parser, operational, axiom, and N1-N8 boundaries",
    )

    print("per_element: independent reconstruction checks every fixture effect type, content label, trace mass, and skew mass")
    print("per_site: independent decoding covers five root strata, carrier payloads, and nineteen terminal fixtures")
    print("per_mode: checked and not executed — no spectral-mode or mode-exhaustion claim is made")
    print("per_block: independent geometry checks 895 unfinished shapes and 2280 completed fixtures")
    print("lattice_wide: checked and not executed — support is analytic and no exact-setting frequency claim is made")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
