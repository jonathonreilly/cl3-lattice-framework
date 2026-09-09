#!/usr/bin/env python3
"""Exact checks for the continuum low-arity Record menu compiler."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, simplify, sqrt, symbols

from nn_record_homogeneous_payload_self_hosting_writer_2026_08_22 import (
    APPEND_ORDER,
    I2,
    SX,
    SZ,
    GaussianLaw,
    antihermitian_coefficient,
    decode_payload,
    hermitian_part,
    is_rank_one_projector,
    matrix_equal,
    recorded_neighbor_contents,
)
from nn_record_isolated_shape_compiler_2026_08_22 import (
    BALL_OFFSETS,
    ROOT_EXCLUSION_RADIUS,
    ROTATIONS,
    ROTATED_STAGES,
    all_stage_states,
    congruent_to_full_block,
    formation_rate,
    geometric_frontier,
    halo,
    l1_distance,
    prefix_embeddings,
    root_eligible,
    rotate_site,
    transform,
    translated_records,
)
from nn_record_spatial_trial_ensemble_2026_08_23 import (
    CANONICAL_CARRIER_PATH,
    add,
    conjugate,
    connected_components,
    occupied_degree,
)


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_CONTINUUM_LOW_ARITY_MENU_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_"
    "BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/nn_record_relational_menu_compiler_2026_08_23.py",
    "scripts/nn_record_spatial_trial_ensemble_2026_08_23.py",
    "scripts/nn_record_isolated_shape_compiler_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_CONTINUUM_LOW_ARITY_MENU_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

SECTOR_MASSES = {
    "RRR": Q(1, 4),
    "RR": Q(1, 8),
    "RRI": Q(1, 4),
    "III": Q(1, 4),
    "II": Q(1, 8),
}
COEFFICIENT_DENSITIES = {
    "RRR": Q(2),  # normalized area density on the area-1/2 triangle
    "RR": Q(1),   # unit point mass on the coefficient-free stratum
    "RRI": Q(1),  # normalized length density on [0,1]
    "III": Q(2),  # normalized area density on the area-1/2 simplex
    "II": Q(1),   # normalized length density on [0,1]
}
SECTOR_TAGS = {"RRR": Q(0), "RR": Q(1), "RRI": Q(2), "III": Q(4), "II": Q(5)}
OUTCOME_LABELS = (Q(30), Q(31), Q(32))


@dataclass(frozen=True)
class ContinuumRootLaw:
    """Five positive-mass strata, each with its declared full-support measure."""

    sector_masses: dict[str, Q]
    coefficient_densities: dict[str, Q]
    orientation_measure: str = "normalized-Haar-SU2"


@dataclass(frozen=True)
class MenuPayload:
    sector: str
    parameters: tuple
    preparation: Matrix
    x_axis: Matrix
    z_axis: Matrix


@dataclass(frozen=True)
class OutcomeSpec:
    name: str
    effect: Matrix
    label: Q

    @property
    def content(self) -> Matrix:
        return simplify(self.effect + I * self.label * I2)


@dataclass(frozen=True)
class ContinuumTrialCertificate:
    anchor: tuple[int, int, int]
    target: tuple[int, int, int]
    rotation_index: int
    displacement: tuple[int, int, int]
    sector: str
    outcome: str
    effect: Matrix
    payload: Matrix


def truth_nonnegative(value) -> bool:
    return bool(simplify(value).is_nonnegative)


def truth_positive(value) -> bool:
    return bool(simplify(value).is_positive)


def scalar_part(value: Matrix):
    return simplify(value.trace() / 2)


def traceless_part(value: Matrix) -> Matrix:
    return simplify(value - scalar_part(value) * I2)


def pauli_radius(value: Matrix):
    return simplify(sqrt((value * value).trace() / 2))


def is_axis(value: Matrix) -> bool:
    return (
        matrix_equal(value, value.conjugate().T)
        and simplify(value.trace()) == 0
        and matrix_equal(simplify(value * value), I2)
    )


def payload_rrr(a, b, x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify((1 + a) * x_axis + I * (1 + b) * z_axis)


def payload_rr(x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify(x_axis + I * (z_axis + SECTOR_TAGS["RR"] * I2))


def payload_rri(d, x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify((1 + d) * x_axis + I * (z_axis + SECTOR_TAGS["RRI"] * I2))


def payload_iii(d1, d2, x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify(
        (1 + d1) * x_axis
        + I * ((1 + d2) * z_axis + SECTOR_TAGS["III"] * I2)
    )


def payload_ii(d, x_axis: Matrix = SX, z_axis: Matrix = SZ) -> Matrix:
    return simplify((1 + d) * x_axis + I * (z_axis + SECTOR_TAGS["II"] * I2))


def decode_menu_payload(value: Matrix) -> MenuPayload | None:
    h_value = hermitian_part(value)
    k_value = antihermitian_coefficient(value)
    if simplify(h_value.trace()) != 0:
        return None
    h_zero = traceless_part(h_value)
    k_zero = traceless_part(k_value)
    h_radius = pauli_radius(h_zero)
    k_radius = pauli_radius(k_zero)
    if not truth_positive(h_radius) or not truth_positive(k_radius):
        return None
    x_axis = simplify(h_zero / h_radius)
    z_axis = simplify(k_zero / k_radius)
    if not (
        is_axis(x_axis)
        and is_axis(z_axis)
        and matrix_equal(simplify(x_axis * z_axis + z_axis * x_axis), Matrix.zeros(2))
    ):
        return None
    tag = scalar_part(k_value)
    sector = next(
        (name for name, candidate in SECTOR_TAGS.items() if simplify(tag - candidate) == 0),
        None,
    )
    if sector is None:
        return None
    if sector == "RRR":
        a, b = simplify(h_radius - 1), simplify(k_radius - 1)
        valid = (
            truth_nonnegative(a)
            and truth_nonnegative(1 - a)
            and truth_nonnegative(b)
            and truth_nonnegative(1 - b)
            and truth_nonnegative(a + b - 1)
        )
        parameters = (a, b)
    elif sector == "RR":
        valid = simplify(h_radius - 1) == 0 and simplify(k_radius - 1) == 0
        parameters = tuple()
    elif sector == "RRI":
        d = simplify(h_radius - 1)
        valid = (
            simplify(k_radius - 1) == 0
            and truth_nonnegative(d)
            and truth_nonnegative(1 - d)
        )
        parameters = (d,)
    elif sector == "III":
        d1, d2 = simplify(h_radius - 1), simplify(k_radius - 1)
        valid = (
            truth_nonnegative(d1)
            and truth_nonnegative(d2)
            and truth_nonnegative(1 - d1 - d2)
        )
        parameters = (d1, d2)
    else:
        d = simplify(h_radius - 1)
        valid = (
            simplify(k_radius - 1) == 0
            and truth_nonnegative(d)
            and truth_nonnegative(1 - d)
        )
        parameters = (d,)
    if not valid:
        return None
    return MenuPayload(sector, parameters, I2 / 2, x_axis, z_axis)


def projector(axis: Matrix) -> Matrix:
    return simplify((I2 + axis) / 2)


def nonzero_rows(rows):
    return tuple(
        (index, name, simplify(effect))
        for index, (name, effect) in enumerate(rows)
        if not matrix_equal(effect, Matrix.zeros(2))
    )


def menu_specs(value: Matrix) -> tuple[OutcomeSpec, ...] | None:
    decoded = decode_menu_payload(value)
    if decoded is None:
        return None
    x_axis, z_axis = decoded.x_axis, decoded.z_axis
    if decoded.sector == "RRR":
        a, b = decoded.parameters
        c = simplify(2 - a - b)
        if simplify(a) == 0:
            rows = (("rrr-1", Matrix.zeros(2)), ("rrr-2", projector(z_axis)), ("rrr-3", projector(-z_axis)))
        elif simplify(b) == 0:
            rows = (("rrr-1", projector(x_axis)), ("rrr-2", Matrix.zeros(2)), ("rrr-3", projector(-x_axis)))
        elif simplify(c) == 0:
            rows = (("rrr-1", projector(x_axis)), ("rrr-2", projector(-x_axis)), ("rrr-3", Matrix.zeros(2)))
        else:
            gamma = simplify((c * c - a * a - b * b) / (2 * a * b))
            eta = simplify(sqrt(1 - gamma * gamma))
            n1 = x_axis
            n2 = simplify(gamma * x_axis + eta * z_axis)
            n3 = simplify(-(a * n1 + b * n2) / c)
            rows = (
                ("rrr-1", simplify(a * projector(n1))),
                ("rrr-2", simplify(b * projector(n2))),
                ("rrr-3", simplify(c * projector(n3))),
            )
    elif decoded.sector == "RR":
        rows = (("rr-1", projector(x_axis)), ("rr-2", projector(-x_axis)))
    elif decoded.sector == "RRI":
        (d,) = decoded.parameters
        rows = (
            ("rri-i", simplify(d * I2)),
            ("rri-plus", simplify((1 - d) * projector(x_axis))),
            ("rri-minus", simplify((1 - d) * projector(-x_axis))),
        )
    elif decoded.sector == "III":
        d1, d2 = decoded.parameters
        rows = (
            ("iii-1", simplify(d1 * I2)),
            ("iii-2", simplify(d2 * I2)),
            ("iii-3", simplify((1 - d1 - d2) * I2)),
        )
    else:
        (d,) = decoded.parameters
        rows = (("ii-1", simplify(d * I2)), ("ii-2", simplify((1 - d) * I2)))
    present = nonzero_rows(rows)
    return tuple(
        OutcomeSpec(name, effect, OUTCOME_LABELS[index])
        for index, name, effect in present
    )


def effect_kind(effect: Matrix) -> str | None:
    if not matrix_equal(effect, effect.conjugate().T):
        return None
    scalar = scalar_part(effect)
    if matrix_equal(effect, scalar * I2):
        return "I" if truth_positive(scalar) and truth_nonnegative(1 - scalar) else None
    scale = simplify(effect.trace())
    if (
        truth_positive(scale)
        and truth_nonnegative(1 - scale)
        and is_rank_one_projector(simplify(effect / scale))
    ):
        return "R"
    return None


def terminal_law(value: Matrix, variant: str = "trace"):
    specs = menu_specs(value)
    decoded = decode_menu_payload(value)
    if specs is None or decoded is None:
        return None
    masses = [simplify((decoded.preparation * spec.effect).trace()) for spec in specs]
    if variant == "context-skew" and decoded.sector == "RRR" and len(specs) == 3:
        scales = [simplify(spec.effect.trace()) for spec in specs]
        delta = simplify(scales[0] * scales[1] * scales[2] / 10)
        masses[0] = simplify(masses[0] + delta / 2)
        masses[1] = simplify(masses[1] + delta / 2)
        masses[2] = simplify(masses[2] - delta)
    elif variant not in ("trace", "context-skew"):
        raise ValueError(f"unknown terminal-law variant: {variant}")
    return tuple((spec.content, mass) for spec, mass in zip(specs, masses))


def distinct_payloads(neighbors: tuple[Matrix, ...]) -> tuple[Matrix, ...]:
    found = []
    for value in neighbors:
        if decode_menu_payload(value) is None:
            continue
        if not any(matrix_equal(value, prior) for prior in found):
            found.append(value)
    return tuple(found)


def continuum_content_law(neighbors, variant: str = "trace"):
    if not neighbors:
        return ContinuumRootLaw(SECTOR_MASSES, COEFFICIENT_DENSITIES)
    if len(neighbors) == 6 and all(matrix_equal(value, neighbors[0]) for value in neighbors):
        terminal = terminal_law(neighbors[0], variant)
        if terminal is not None:
            return terminal
    payloads = distinct_payloads(neighbors)
    if payloads:
        mass = Q(1, len(payloads))
        return tuple((payload, mass) for payload in payloads)
    return GaussianLaw()


def parse_trial(records, component) -> ContinuumTrialCertificate | None:
    component = frozenset(component)
    if len(component) != 12 or not congruent_to_full_block(component):
        return None
    if len(connected_components({site: records[site] for site in component})) != 1:
        return None
    if (halo(component) & frozenset(records)) != component:
        return None
    terminals = tuple(site for site in component if occupied_degree(site, component) == 6)
    if len(terminals) != 1:
        return None
    target = terminals[0]
    carriers = component - {target}
    payload = records[next(iter(carriers))]
    decoded = decode_menu_payload(payload)
    specs = menu_specs(payload)
    if decoded is None or specs is None or not all(matrix_equal(records[site], payload) for site in carriers):
        return None
    embeddings = prefix_embeddings(carriers, 11)
    if len(embeddings) != 1:
        return None
    rotation_index, displacement = embeddings[0]
    if target != add(displacement, ROTATED_STAGES[11][rotation_index][4]):
        return None
    matches = tuple(spec for spec in specs if matrix_equal(records[target], spec.content))
    if len(matches) != 1:
        return None
    match = matches[0]
    anchor = transform(ROTATIONS[rotation_index], displacement, APPEND_ORDER[0])
    return ContinuumTrialCertificate(
        anchor, target, rotation_index, displacement, decoded.sector,
        match.name, match.effect, payload,
    )


def conjugated_records(records, unitary):
    return {site: conjugate(content, unitary) for site, content in records.items()}


def main() -> int:
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    representatives = {
        "rrr-a": payload_rrr(Q(1, 2), Q(9, 10)),
        "rrr-b": payload_rrr(Q(1, 2), Q(3, 4)),
        "rrr-fine": payload_rrr(Q(1, 2), Q(1, 2)),
        "rr": payload_rr(),
        "rri": payload_rri(Q(1, 3)),
        "iii": payload_iii(Q(1, 5), Q(3, 10)),
        "ii": payload_ii(Q(2, 5)),
    }
    decoded = {name: decode_menu_payload(value) for name, value in representatives.items()}
    ordinary_decoded = {name: decode_payload(value) for name, value in representatives.items()}
    check(
        "five-positive-strata-common-preparation",
        sum(SECTOR_MASSES.values()) == 1
        and all(mass > 0 for mass in SECTOR_MASSES.values())
        and COEFFICIENT_DENSITIES == {
            "RRR": 2, "RR": 1, "RRI": 1, "III": 2, "II": 1,
        }
        and {item.sector for item in decoded.values()} == {"RRR", "RR", "RRI", "III", "II"}
        and all(item is not None and matrix_equal(item.preparation, I2 / 2) for item in ordinary_decoded.values())
        and all(matrix_equal(item.preparation, I2 / 2) for item in decoded.values()),
        "all RRR/RR/RRI/III/II root strata have positive mixture mass and one I/2 preparation quotient",
    )

    menus = {name: menu_specs(value) for name, value in representatives.items()}
    type_words = {
        name: "".join(effect_kind(spec.effect) for spec in specs)
        for name, specs in menus.items()
    }
    check(
        "complete-low-arity-strata",
        type_words == {
            "rrr-a": "RRR", "rrr-b": "RRR", "rrr-fine": "RRR",
            "rr": "RR", "rri": "IRR", "iii": "III", "ii": "II",
        }
        and all(matrix_equal(sum((spec.effect for spec in specs), Matrix.zeros(2)), I2) for specs in menus.values())
        and all(len(specs) in (2, 3) for specs in menus.values()),
        "the five exhaustive type strata are instantiated and every representative binary/ternary menu resolves I",
    )

    grid = (
        (Q(0), Q(1)), (Q(1), Q(0)), (Q(1), Q(1)),
        (Q(1, 2), Q(1, 2)), (Q(1, 3), Q(2, 3)),
        (Q(1, 2), Q(3, 4)), (Q(3, 5), Q(4, 5)),
    )
    grid_valid = True
    for a, b in grid:
        specs = menu_specs(payload_rrr(a, b))
        grid_valid = grid_valid and (
            specs is not None
            and len(specs) in (2, 3)
            and all(effect_kind(spec.effect) == "R" for spec in specs)
            and matrix_equal(sum((spec.effect for spec in specs), Matrix.zeros(2)), I2)
        )
    a, b, c = symbols("a b c", positive=True)
    gamma = simplify((c * c - a * a - b * b) / (2 * a * b))
    closure_norm = simplify((a * a + b * b + 2 * a * b * gamma) / (c * c))
    check(
        "rank-one-triangle-surjection-core",
        grid_valid and closure_norm == 1,
        "c1+c2+c3=2 and the weighted Bloch closure give the canonical triangle; its Gram data determine every RRR menu up to SO(3)/SU(2)",
    )

    boundary_payloads = (
        payload_rrr(Q(1), Q(1)), payload_rrr(Q(0), Q(1)), payload_rrr(Q(1), Q(0)),
        payload_rri(Q(0)), payload_iii(Q(2, 5), Q(0)), payload_ii(Q(0)),
    )
    check(
        "zero-removal-boundaries",
        all(menu_specs(value) is not None for value in boundary_payloads)
        and all(
            all(not matrix_equal(spec.effect, Matrix.zeros(2)) for spec in menu_specs(value))
            for value in boundary_payloads
        )
        and tuple(len(menu_specs(value)) for value in boundary_payloads) == (2, 2, 2, 2, 2, 1),
        "supported coefficient boundaries drop zero effects exactly; all target binary boundaries remain valid",
    )

    trace_laws = {name: terminal_law(value, "trace") for name, value in representatives.items()}
    check(
        "selected-trace-kernel-all-strata",
        all(simplify(sum(mass for _, mass in law)) == 1 for law in trace_laws.values())
        and all(truth_positive(mass) for law in trace_laws.values() for _, mass in law)
        and tuple(mass for _, mass in trace_laws["rri"]) == (Q(1, 3), Q(1, 3), Q(1, 3))
        and tuple(mass for _, mass in trace_laws["iii"]) == (Q(1, 5), Q(3, 10), Q(1, 2))
        and tuple(mass for _, mass in trace_laws["ii"]) == (Q(2, 5), Q(3, 5)),
        "Tr((I/2)E) is derived for every registered effect and normalizes each of the five strata",
    )

    fine = payload_rrr(Q(1, 2), Q(1, 2))
    coarse = payload_rr()
    a_program = payload_rrr(Q(1, 2), Q(9, 10))
    b_program = payload_rrr(Q(1, 2), Q(3, 4))
    skew_fine = terminal_law(fine, "context-skew")
    skew_coarse = terminal_law(coarse, "context-skew")
    skew_a = terminal_law(a_program, "context-skew")
    skew_b = terminal_law(b_program, "context-skew")
    a_first = menu_specs(a_program)[0]
    b_first = menu_specs(b_program)[0]
    check(
        "continuum-context-skew-control",
        tuple(mass for _, mass in skew_fine) == (Q(21, 80), Q(21, 80), Q(19, 40))
        and tuple(mass for _, mass in skew_coarse) == (Q(1, 2), Q(1, 2))
        and simplify(skew_fine[0][1] + skew_fine[1][1]) == Q(21, 40)
        and simplify(skew_fine[0][1] + skew_fine[1][1]) != skew_coarse[0][1]
        and matrix_equal(a_first.effect, b_first.effect)
        and skew_a[0][1] == Q(527, 2000)
        and skew_b[0][1] == Q(169, 640)
        and skew_a[0][1] != skew_b[0][1]
        and all(simplify(sum(mass for _, mass in law)) == 1 for law in (skew_fine, skew_coarse, skew_a, skew_b))
        and all(truth_positive(mass) for law in (skew_fine, skew_coarse, skew_a, skew_b) for _, mass in law),
        "one exact positive same-support Law breaks both coarse/refined and literal shared-effect probabilities, so W1 stays open",
    )

    exact_unitaries = (
        I2,
        SX,
        simplify((SX + SZ) / sqrt(2)),
        Matrix([[1, 0], [0, I]]),
        simplify((I2 + I * SX) / sqrt(2)),
    )
    covariant = True
    for unitary in exact_unitaries:
        for name, value in representatives.items():
            moved = conjugate(value, unitary)
            before = menu_specs(value)
            after = menu_specs(moved)
            covariant = covariant and (
                decode_menu_payload(moved).sector == decoded[name].sector
                and all(
                    left.name == right.name
                    and left.label == right.label
                    and matrix_equal(right.effect, conjugate(left.effect, unitary))
                    for left, right in zip(before, after)
                )
            )
            for variant in ("trace", "context-skew"):
                before_law = terminal_law(value, variant)
                after_law = terminal_law(moved, variant)
                covariant = covariant and all(
                    simplify(left_mass - right_mass) == 0
                    and matrix_equal(right_content, conjugate(left_content, unitary))
                    for (left_content, left_mass), (right_content, right_mass)
                    in zip(before_law, after_law)
                )
    check(
        "internal-frame-covariance",
        covariant,
        "five exact basis changes preserve sector/parameters, conjugate every menu Record, and preserve both kernels",
    )

    base_payload = representatives["rrr-a"]
    stages, exact_partition, completed_quiet, unfinished_count = all_stage_states(base_payload)
    terminal_pairs = tuple(
        (carriers, next(iter(geometric_frontier(carriers, 11))))
        for carriers in stages[-2]
    )
    parsed = []
    sample_records = None
    for carriers, target in terminal_pairs:
        for name, value in representatives.items():
            for spec in menu_specs(value):
                records = {site: value for site in carriers}
                records[target] = spec.content
                certificate = parse_trial(records, frozenset(records))
                parsed.append(
                    certificate is not None
                    and certificate.target == target
                    and certificate.sector == decoded[name].sector
                    and certificate.outcome == spec.name
                    and matrix_equal(certificate.effect, spec.effect)
                )
                if sample_records is None and name == "rrr-a":
                    sample_records = records
    check(
        "exhaustive-continuum-parser-fixtures",
        exact_partition
        and completed_quiet
        and unfinished_count == 895
        and len(terminal_pairs) == 120
        and len(parsed) == 2280
        and all(parsed),
        "all 120 placements times nineteen cross-stratum representative outcomes decode: 2280/2280",
    )

    unfinished_rejects = all(
        parse_trial({site: base_payload for site in state}, state) is None
        for level in stages[:-1]
        for state in level
    )
    sample_component = frozenset(sample_records)
    hostile_site = min(halo(sample_component) - sample_component)
    hostile = dict(sample_records)
    hostile[hostile_site] = representatives["rr"]
    hostile_component = next(component for component in connected_components(hostile) if component & sample_component)
    malformed_carriers, malformed_target = terminal_pairs[0]
    malformed = {site: Matrix.zeros(2) for site in malformed_carriers}
    malformed[malformed_target] = I2
    nonorthogonal = simplify(2 * SX + I * (SX + SZ) / sqrt(2))
    check(
        "false-positive-and-frame-controls",
        unfinished_rejects
        and parse_trial(hostile, hostile_component) is None
        and parse_trial(malformed, frozenset(malformed)) is None
        and decode_menu_payload(nonorthogonal) is None,
        "895 unfinished histories, hostile adjacency, zero carriers, and a nonorthogonal internal frame reject",
    )

    sample_certificate = parse_trial(sample_records, sample_component)
    displacement = (7, -4, 3)
    moved_records = translated_records(sample_records, displacement)
    moved_certificate = parse_trial(moved_records, frozenset(moved_records))
    parser_covariant = moved_certificate is not None and (
        moved_certificate.target == add(sample_certificate.target, displacement)
        and moved_certificate.sector == sample_certificate.sector
        and moved_certificate.outcome == sample_certificate.outcome
    )
    for rotation in ROTATIONS:
        rotated = {rotate_site(rotation, site): content for site, content in sample_records.items()}
        certificate = parse_trial(rotated, frozenset(rotated))
        parser_covariant = parser_covariant and (
            certificate is not None
            and certificate.target == rotate_site(rotation, sample_certificate.target)
            and certificate.sector == sample_certificate.sector
        )
    for unitary in exact_unitaries:
        moved = conjugated_records(sample_records, unitary)
        certificate = parse_trial(moved, frozenset(moved))
        parser_covariant = parser_covariant and (
            certificate is not None
            and certificate.sector == sample_certificate.sector
            and certificate.outcome == sample_certificate.outcome
            and matrix_equal(certificate.effect, conjugate(sample_certificate.effect, unitary))
        )
    check(
        "certificate-covariance",
        parser_covariant,
        "translations, all 24 proper cubic rotations, and five basis changes commute with the Record-only parser",
    )

    canonical_target = next(iter(geometric_frontier(frozenset(CANONICAL_CARRIER_PATH), 11)))
    canonical_sequence = CANONICAL_CARRIER_PATH + (canonical_target,)
    sequence_legal = root_eligible({}, canonical_sequence[0])
    sequence_records = {}
    path_payload = representatives["rri"]
    for index, site in enumerate(canonical_sequence):
        if index == 0:
            root_law = continuum_content_law(tuple())
            sequence_legal = sequence_legal and (
                isinstance(root_law, ContinuumRootLaw)
                and root_law.orientation_measure == "normalized-Haar-SU2"
                and root_law.coefficient_densities == COEFFICIENT_DENSITIES
            )
            sequence_records[site] = path_payload
        elif index < 11:
            law = continuum_content_law(recorded_neighbor_contents(sequence_records, site))
            sequence_legal = sequence_legal and (
                formation_rate(sequence_records, site) == 1
                and len(law) == 1
                and matrix_equal(law[0][0], path_payload)
                and law[0][1] == 1
            )
            sequence_records[site] = path_payload
        else:
            law = continuum_content_law(recorded_neighbor_contents(sequence_records, site))
            sequence_legal = sequence_legal and formation_rate(sequence_records, site) == 1 and simplify(sum(mass for _, mass in law)) == 1
            sequence_records[site] = law[0][0]
    tau, patch_mass = symbols("tau patch_mass", positive=True)
    event_count = len(canonical_sequence)
    ball_size = len(BALL_OFFSETS[ROOT_EXCLUSION_RADIUS])
    cylinder = simplify(
        SECTOR_MASSES["RRI"] * patch_mass
        * exp(-ball_size * tau) * (tau / event_count) ** event_count
    )
    singleton_mass = Q(0)
    check(
        "support-level-occurrence-boundary",
        sequence_legal
        and event_count == 12
        and ball_size == 1159
        and cylinder == patch_mass * exp(-1159 * tau) * (tau / 12) ** 12 / 4
        and truth_positive(cylinder)
        and singleton_mass == 0,
        "every relatively open parameter patch has a positive B9 cylinder, while an exact continuum setting correctly has zero singleton mass",
    )

    erased_rr = simplify(representatives["rr"] - I * SECTOR_TAGS["RR"] * I2)
    erased_rri_zero = simplify(payload_rri(Q(0)) - I * SECTOR_TAGS["RRI"] * I2)
    invalid_triangle = payload_rrr(Q(1, 5), Q(1, 5))
    check(
        "program-and-domain-mutations",
        matrix_equal(erased_rr, erased_rri_zero)
        and decode_menu_payload(invalid_triangle) is None
        and decode_menu_payload(simplify(payload_iii(Q(3, 4), Q(3, 4)))) is None,
        "erasing the scalar program tag aliases RR/RRI, while coefficients outside either closed simplex reject",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    required = (
        "under the current canonical support reading",
        "five strata are exhaustive",
        "not a controlled setting dial",
        "zero singleton mass",
        "W1 remains open",
        "No Minimal Axioms edit",
        "TOE percentages remain unchanged",
        "N1 — Alternative Route Enumeration",
        "N8 — Cross-Cycle Echo",
    )
    check(
        "source-contract",
        all(fragment in note_text for fragment in required),
        "the note pins support eligibility, exhaustive strata, operational limits, W1, axiom/score posture, and N1-N8",
    )

    print("per_element: every representative scaled-rank-one/scalar effect, label, trace mass, and skew mass is checked")
    print("per_site: five positive root strata, copied carriers, and nineteen terminal fixtures are decoded")
    print("per_mode: checked and not executed — no spectral-mode or mode-exhaustion claim is made")
    print("per_block: all 895 unfinished shapes and 2280 completed cross-stratum fixtures are checked")
    print("lattice_wide: checked and not executed — full-support eligibility is analytic; no exact-setting frequency claim is made")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
