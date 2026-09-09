#!/usr/bin/env python3
"""Exact checks for a relational multi-menu Record compiler and its boundary."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, limit, oo, simplify, sqrt, symbols

from nn_record_homogeneous_payload_self_hosting_writer_2026_08_22 import (
    APPEND_ORDER,
    I2,
    SX,
    SZ,
    antihermitian_coefficient,
    content_mass,
    decode_payload,
    hermitian_part,
    is_rank_one_projector,
    local_law,
    matrix_equal,
    recorded_neighbor_contents,
    trace_weight,
)
from nn_record_isolated_shape_compiler_2026_08_22 import (
    BALL_OFFSETS,
    ROOT_EXCLUSION_RADIUS,
    ROTATIONS,
    ROTATED_STAGES,
    actual_growth_frontier,
    all_stage_states,
    congruent_to_full_block,
    formation_rate,
    geometric_frontier,
    halo,
    l1_distance,
    prefix_embeddings,
    root_eligible,
    rotate_site,
    subtract,
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


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_RELATIONAL_MENU_COMPILER_AND_CONTEXT_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/NN_RECORD_SPATIAL_TRIAL_ENSEMBLE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/nn_record_spatial_trial_ensemble_2026_08_23.py",
    "docs/NN_RECORD_ISOLATED_SHAPE_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/nn_record_isolated_shape_compiler_2026_08_22.py",
    "scripts/nn_record_homogeneous_payload_self_hosting_writer_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_RELATIONAL_MENU_COMPILER_AND_CONTEXT_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

H_STAR = Matrix([[1, 1], [1, 2]])
BASE_PAYLOAD = simplify(H_STAR + I * SZ)
SETTINGS = ("coarse", "refined", "ternary-a", "ternary-b")
SETTING_TAGS = {setting: Q(index) for index, setting in enumerate(SETTINGS)}
LABELS = {
    "coarse-plus": Q(10),
    "shared-minus": Q(11),
    "fine-a": Q(12),
    "fine-b": Q(13),
    "shared-e0": Q(14),
    "a1": Q(15),
    "a2": Q(16),
    "b1": Q(17),
    "b2": Q(18),
}


@dataclass(frozen=True)
class RelationalMenuOrbitLaw:
    """Equal mixture of four Haar-conjugacy orbits distinguished by scalar tags."""

    representatives: tuple[Matrix, ...]
    masses: tuple[Q, ...]


@dataclass(frozen=True)
class OutcomeSpec:
    name: str
    effect: Matrix
    label: Q

    @property
    def content(self) -> Matrix:
        return simplify(self.effect + I * self.label * I2)


@dataclass(frozen=True)
class RelationalTrialCertificate:
    anchor: tuple[int, int, int]
    target: tuple[int, int, int]
    rotation_index: int
    displacement: tuple[int, int, int]
    setting: str
    outcome: str
    effect: Matrix
    payload: Matrix


def setting_payload(setting: str) -> Matrix:
    return simplify(BASE_PAYLOAD + I * SETTING_TAGS[setting] * I2)


ROOT_REPRESENTATIVES = tuple(setting_payload(setting) for setting in SETTINGS)


def scalar_tag(value: Matrix):
    return simplify(antihermitian_coefficient(value).trace() / 2)


def setting_of(value: Matrix) -> str | None:
    tag = scalar_tag(value)
    for setting, candidate in SETTING_TAGS.items():
        if simplify(tag - candidate) == 0:
            return setting
    return None


def relational_axes(payload: Matrix) -> tuple[Matrix, Matrix] | None:
    """Recover the covariant X/Z frame carried by one tagged generic payload."""
    tag = scalar_tag(payload)
    z_axis = simplify(antihermitian_coefficient(payload) - tag * I2)
    h_value = hermitian_part(payload)
    if simplify(h_value.trace() - H_STAR.trace()) != 0:
        return None
    h_zero = simplify(h_value - h_value.trace() * I2 / 2)
    x_axis = simplify(h_zero + z_axis / 2)
    if not (
        matrix_equal(simplify(x_axis * x_axis), I2)
        and matrix_equal(simplify(z_axis * z_axis), I2)
        and matrix_equal(simplify(x_axis * z_axis + z_axis * x_axis), Matrix.zeros(2))
    ):
        return None
    return x_axis, z_axis


def projector(x_axis: Matrix, z_axis: Matrix, nx, nz) -> Matrix:
    return simplify((I2 + nx * x_axis + nz * z_axis) / 2)


def menu_specs(payload: Matrix) -> tuple[OutcomeSpec, ...] | None:
    setting = setting_of(payload)
    axes = relational_axes(payload)
    if setting is None or axes is None or decode_payload(payload) is None:
        return None
    x_axis, z_axis = axes
    pz = simplify((I2 + z_axis) / 2)
    mz = simplify(I2 - pz)
    if setting == "coarse":
        return (
            OutcomeSpec("coarse-plus", pz, LABELS["coarse-plus"]),
            OutcomeSpec("shared-minus", mz, LABELS["shared-minus"]),
        )
    if setting == "refined":
        return (
            OutcomeSpec("fine-a", pz / 2, LABELS["fine-a"]),
            OutcomeSpec("fine-b", pz / 2, LABELS["fine-b"]),
            OutcomeSpec("shared-minus", mz, LABELS["shared-minus"]),
        )
    e0 = simplify(pz / 2)
    if setting == "ternary-a":
        n1 = projector(x_axis, z_axis, 4 * sqrt(2) / 9, -Q(7, 9))
        n2 = projector(x_axis, z_axis, -2 * sqrt(2) / 3, Q(1, 3))
        return (
            OutcomeSpec("shared-e0", e0, LABELS["shared-e0"]),
            OutcomeSpec("a1", simplify(Q(9, 10) * n1), LABELS["a1"]),
            OutcomeSpec("a2", simplify(Q(3, 5) * n2), LABELS["a2"]),
        )
    m1 = projector(x_axis, z_axis, 2 * sqrt(2) / 3, -Q(1, 3))
    m2 = projector(x_axis, z_axis, -2 * sqrt(2) / 3, -Q(1, 3))
    return (
        OutcomeSpec("shared-e0", e0, LABELS["shared-e0"]),
        OutcomeSpec("b1", simplify(Q(3, 4) * m1), LABELS["b1"]),
        OutcomeSpec("b2", simplify(Q(3, 4) * m2), LABELS["b2"]),
    )


def support_equal(left, right) -> bool:
    if len(left) != len(right):
        return False
    return all(
        any(matrix_equal(content, other) for other, _ in right)
        for content, _ in left
    )


def is_scaled_rank_one_effect(effect: Matrix) -> bool:
    scale = simplify(effect.trace())
    return (
        matrix_equal(effect, effect.conjugate().T)
        and bool(scale.is_positive)
        and bool(simplify(1 - scale).is_nonnegative)
        and is_rank_one_projector(simplify(effect / scale))
    )


def law_mass(law, content: Matrix):
    return simplify(
        sum((mass for candidate, mass in law if matrix_equal(candidate, content)), Q(0))
    )


def terminal_law(payload: Matrix, variant: str = "trace"):
    specs = menu_specs(payload)
    decoded = decode_payload(payload)
    setting = setting_of(payload)
    if specs is None or decoded is None or setting is None:
        return None
    masses = [trace_weight(decoded.preparation, spec.effect) for spec in specs]
    if variant == "context-skew":
        if setting == "refined":
            delta = Q(1, 42)
            masses[0] = simplify(masses[0] - delta / 2)
            masses[1] = simplify(masses[1] - delta / 2)
            masses[2] = simplify(masses[2] + delta)
        elif setting == "ternary-b":
            delta = Q(1, 84)
            masses[0] = simplify(masses[0] + delta)
            masses[1] = simplify(masses[1] - delta)
    elif variant != "trace":
        raise ValueError(f"unknown terminal-law variant: {variant}")
    return tuple((spec.content, simplify(mass)) for spec, mass in zip(specs, masses))


def relational_content_law(neighbors, variant: str = "trace"):
    if not neighbors:
        return RelationalMenuOrbitLaw(ROOT_REPRESENTATIVES, (Q(1, 4),) * 4)
    if len(neighbors) == 6 and all(matrix_equal(value, neighbors[0]) for value in neighbors):
        terminal = terminal_law(neighbors[0], variant)
        if terminal is not None:
            return terminal
    return local_law(neighbors)


def parse_relational_trial(records, component) -> RelationalTrialCertificate | None:
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
    specs = menu_specs(payload)
    if specs is None or not all(
        matrix_equal(records[site], payload) for site in carriers
    ):
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
    return RelationalTrialCertificate(
        anchor=anchor,
        target=target,
        rotation_index=rotation_index,
        displacement=displacement,
        setting=setting_of(payload),
        outcome=match.name,
        effect=match.effect,
        payload=payload,
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

    decoded = tuple(decode_payload(payload) for payload in ROOT_REPRESENTATIVES)
    common_preparation = decoded[0].preparation
    common_projector = decoded[0].projector
    check(
        "record-visible-shared-preparation",
        all(item is not None for item in decoded)
        and all(matrix_equal(item.preparation, common_preparation) for item in decoded)
        and all(matrix_equal(item.projector, common_projector) for item in decoded)
        and tuple(setting_of(payload) for payload in ROOT_REPRESENTATIVES) == SETTINGS
        and len({scalar_tag(payload) for payload in ROOT_REPRESENTATIVES}) == 4,
        "four disjoint scalar-tag orbits retain one decoded preparation/projector quotient and expose the setting before outcome",
    )

    menus = {setting: menu_specs(setting_payload(setting)) for setting in SETTINGS}
    menu_sums = {
        setting: simplify(sum((spec.effect for spec in specs), Matrix.zeros(2)))
        for setting, specs in menus.items()
    }
    coarse_minus = menus["coarse"][1]
    fine_minus = menus["refined"][2]
    a_e0 = menus["ternary-a"][0]
    b_e0 = menus["ternary-b"][0]
    check(
        "relational-effect-menu-algebra",
        all(matrix_equal(total, I2) for total in menu_sums.values())
        and all(
            is_scaled_rank_one_effect(spec.effect)
            for specs in menus.values()
            for spec in specs
        )
        and matrix_equal(coarse_minus.content, fine_minus.content)
        and matrix_equal(a_e0.content, b_e0.content)
        and matrix_equal(menus["refined"][0].effect, menus["refined"][1].effect)
        and not matrix_equal(menus["refined"][0].content, menus["refined"][1].content)
        and matrix_equal(
            simplify(menus["refined"][0].effect + menus["refined"][1].effect),
            menus["coarse"][0].effect,
        ),
        "all eleven operators are positive scaled rank-one effects, all menus resolve I, and the shared/refined Records are exact",
    )

    trace_laws = {
        setting: terminal_law(setting_payload(setting), "trace") for setting in SETTINGS
    }
    pz = trace_weight(common_preparation, common_projector)
    fine_union = simplify(sum(mass for _, mass in trace_laws["refined"][:2]))
    expected_a = (Q(1, 7), (21 + 6 * sqrt(2)) / 35, (9 - 6 * sqrt(2)) / 35)
    expected_b = (Q(1, 7), (6 + 3 * sqrt(2)) / 14, (6 - 3 * sqrt(2)) / 14)
    check(
        "selected-trace-menu-kernel",
        pz == Q(2, 7)
        and all(simplify(sum(mass for _, mass in law)) == 1 for law in trace_laws.values())
        and fine_union == pz
        and law_mass(trace_laws["coarse"], coarse_minus.content) == Q(5, 7)
        and law_mass(trace_laws["refined"], fine_minus.content) == Q(5, 7)
        and law_mass(trace_laws["ternary-a"], a_e0.content) == Q(1, 7)
        and law_mass(trace_laws["ternary-b"], b_e0.content) == Q(1, 7)
        and all(
            simplify(found - expected) == 0
            for (_, found), expected in zip(trace_laws["ternary-a"], expected_a)
        )
        and all(
            simplify(found - expected) == 0
            for (_, found), expected in zip(trace_laws["ternary-b"], expected_b)
        ),
        "the selected trace branch exactly reproduces every displayed binary, refined, and noncollinear ternary mass",
    )

    skew_laws = {
        setting: terminal_law(setting_payload(setting), "context-skew")
        for setting in SETTINGS
    }
    skew_fine_union = simplify(sum(mass for _, mass in skew_laws["refined"][:2]))
    check(
        "context-skew-paired-law",
        all(support_equal(trace_laws[setting], skew_laws[setting]) for setting in SETTINGS)
        and all(simplify(sum(mass for _, mass in law)) == 1 for law in skew_laws.values())
        and all(bool(simplify(mass).is_positive) for law in skew_laws.values() for _, mass in law)
        and skew_laws["refined"][0][1] == skew_laws["refined"][1][1] == Q(11, 84)
        and skew_fine_union == Q(11, 42)
        and skew_fine_union != pz
        and law_mass(skew_laws["refined"], fine_minus.content) == Q(31, 42)
        and law_mass(skew_laws["coarse"], coarse_minus.content) == Q(5, 7)
        and law_mass(skew_laws["ternary-a"], a_e0.content) == Q(1, 7)
        and law_mass(skew_laws["ternary-b"], b_e0.content) == Q(13, 84),
        "a normalized positive same-support Law preserves duplicate-label symmetry yet breaks both cross-program shared-event equalities",
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
        for setting in SETTINGS:
            payload = setting_payload(setting)
            moved = conjugate(payload, unitary)
            before_specs = menu_specs(payload)
            after_specs = menu_specs(moved)
            covariant = covariant and (
                setting_of(moved) == setting
                and matrix_equal(
                    decode_payload(moved).preparation,
                    conjugate(common_preparation, unitary),
                )
                and all(
                    left.name == right.name
                    and left.label == right.label
                    and matrix_equal(right.effect, conjugate(left.effect, unitary))
                    for left, right in zip(before_specs, after_specs)
                )
            )
            for variant in ("trace", "context-skew"):
                before = terminal_law(payload, variant)
                after = terminal_law(moved, variant)
                covariant = covariant and all(
                    simplify(left_mass - right_mass) == 0
                    and matrix_equal(right_content, conjugate(left_content, unitary))
                    for (left_content, left_mass), (right_content, right_mass) in zip(before, after)
                )
    check(
        "internal-frame-covariance",
        covariant,
        "five exact basis changes preserve setting tags, conjugate every effect/Record, and leave both kernel tables invariant",
    )

    stages, exact_partition, completed_quiet, unfinished_count = all_stage_states(BASE_PAYLOAD)
    terminal_pairs = tuple(
        (carriers, next(iter(geometric_frontier(carriers, 11))))
        for carriers in stages[-2]
    )
    parsed = []
    sample_records = None
    for carriers, target in terminal_pairs:
        for setting in SETTINGS:
            payload = setting_payload(setting)
            for spec in menu_specs(payload):
                records = {site: payload for site in carriers}
                records[target] = spec.content
                certificate = parse_relational_trial(records, frozenset(records))
                parsed.append(
                    certificate is not None
                    and certificate.target == target
                    and certificate.anchor in carriers
                    and certificate.setting == setting
                    and certificate.outcome == spec.name
                    and matrix_equal(certificate.effect, spec.effect)
                )
                if sample_records is None and setting == "ternary-a":
                    sample_records = records
    check(
        "exhaustive-relational-parser",
        exact_partition
        and completed_quiet
        and unfinished_count == 895
        and len(terminal_pairs) == 120
        and len(parsed) == 1320
        and all(parsed),
        "all 120 placements times eleven setting/outcome branches decode one static frame, setting, effect, label, and terminal",
    )

    unfinished_rejects = all(
        parse_relational_trial({site: BASE_PAYLOAD for site in state}, state) is None
        for level in stages[:-1]
        for state in level
    )
    sample_component = frozenset(sample_records)
    hostile_site = min(halo(sample_component) - sample_component)
    hostile = dict(sample_records)
    hostile[hostile_site] = setting_payload("coarse")
    hostile_component = next(
        component for component in connected_components(hostile) if component & sample_component
    )
    malformed_carriers, malformed_target = terminal_pairs[0]
    malformed = {site: Matrix.zeros(2) for site in malformed_carriers}
    malformed[malformed_target] = I2
    check(
        "false-positive-and-hostile-controls",
        unfinished_rejects
        and parse_relational_trial(hostile, hostile_component) is None
        and parse_relational_trial(malformed, frozenset(malformed)) is None,
        "all unfinished histories, hostile adjacency, and a tag-zero invalid relational frame fail the final-state parser",
    )

    sample_certificate = parse_relational_trial(sample_records, sample_component)
    spatial_covariant = True
    displacement = (7, -4, 3)
    moved_records = translated_records(sample_records, displacement)
    moved_certificate = parse_relational_trial(moved_records, frozenset(moved_records))
    spatial_covariant = moved_certificate is not None and (
        moved_certificate.target == add(sample_certificate.target, displacement)
        and moved_certificate.setting == sample_certificate.setting
        and moved_certificate.outcome == sample_certificate.outcome
    )
    for rotation in ROTATIONS:
        rotated = {rotate_site(rotation, site): content for site, content in sample_records.items()}
        certificate = parse_relational_trial(rotated, frozenset(rotated))
        spatial_covariant = spatial_covariant and (
            certificate is not None
            and certificate.target == rotate_site(rotation, sample_certificate.target)
            and certificate.setting == sample_certificate.setting
        )
    basis_parser = True
    for unitary in exact_unitaries:
        moved = conjugated_records(sample_records, unitary)
        certificate = parse_relational_trial(moved, frozenset(moved))
        basis_parser = basis_parser and (
            certificate is not None
            and certificate.setting == sample_certificate.setting
            and certificate.outcome == sample_certificate.outcome
            and matrix_equal(certificate.effect, conjugate(sample_certificate.effect, unitary))
        )
    check(
        "certificate-covariance",
        spatial_covariant and basis_parser,
        "translations, all 24 proper cubic rotations, and five internal basis changes commute with relational parsing",
    )

    canonical_target = next(iter(geometric_frontier(frozenset(CANONICAL_CARRIER_PATH), 11)))
    canonical_sequence = CANONICAL_CARRIER_PATH + (canonical_target,)
    sequence_legal = root_eligible({}, canonical_sequence[0])
    sequence_records = {}
    fine_payload = setting_payload("refined")
    for index, site in enumerate(canonical_sequence):
        if index == 0:
            root_law = relational_content_law(tuple())
            sequence_legal = sequence_legal and isinstance(root_law, RelationalMenuOrbitLaw)
            sequence_records[site] = fine_payload
        elif index < 11:
            neighbors = recorded_neighbor_contents(sequence_records, site)
            sequence_legal = sequence_legal and (
                formation_rate(sequence_records, site) == 1
                and content_mass(relational_content_law(neighbors), fine_payload) == 1
            )
            sequence_records[site] = fine_payload
        else:
            read = relational_content_law(recorded_neighbor_contents(sequence_records, site))
            sequence_legal = sequence_legal and (
                formation_rate(sequence_records, site) == 1
                and simplify(sum(mass for _, mass in read)) == 1
            )
            sequence_records[site] = read[0][0]
    tau = symbols("tau", positive=True)
    event_count = len(canonical_sequence)
    delta = tau / event_count
    ball_size = len(BALL_OFFSETS[ROOT_EXCLUSION_RADIUS])
    designated = (exp(-delta) * delta) ** event_count
    quiet = exp(-(ball_size * tau - event_count * delta))
    setting_mass = RelationalMenuOrbitLaw(ROOT_REPRESENTATIVES, (Q(1, 4),) * 4).masses[1]
    cylinder = simplify(setting_mass * designated * quiet)
    check(
        "positive-per-setting-cylinder",
        sequence_legal
        and event_count == len(set(canonical_sequence)) == 12
        and max(l1_distance(site) for site in canonical_sequence) <= 4
        and ball_size == 1159
        and cylinder == exp(-1159 * tau) * (tau / 12) ** 12 / 4
        and bool(cylinder.subs(tau, Q(12, 1159)).is_positive),
        "each setting has a derived positive B9 twelve-slot cylinder exp(-1159*tau)(tau/12)^12/4",
    )

    intensity = symbols("lambda_s", positive=True)
    n = symbols("n", integer=True, positive=True)
    volume = (2 * n + 1) ** 3
    boundary = simplify(volume - (2 * n - 1) ** 3)
    all_ratios = all(
        simplify((intensity * mass) / intensity) == mass
        for family in (trace_laws, skew_laws)
        for law in family.values()
        for _, mass in law
    )
    check(
        "conditional-spatial-frequency-algebra",
        all_ratios and limit(boundary / volume, n, oo) == 0,
        "positive setting intensity cancels for both exact Laws outcome-by-outcome and cubic boundary/volume tends to zero",
    )

    translation_classes = {}
    for completed in stages[-1]:
        minimum = min(completed)
        normalized = frozenset(subtract(site, minimum) for site in completed)
        root_offset = subtract((0, 0, 0), minimum)
        translation_classes.setdefault(normalized, set()).add(root_offset)
    erased_payloads = tuple(simplify(payload - I * scalar_tag(payload) * I2) for payload in ROOT_REPRESENTATIVES)
    changed_h = simplify(Matrix([[2, 0], [0, 1]]) + I * SZ + I * I2)
    check(
        "setting-and-history-controls",
        len(translation_classes) == 24
        and {len(offsets) for offsets in translation_classes.values()} == {5}
        and all(matrix_equal(erased_payloads[0], payload) for payload in erased_payloads[1:])
        and not matrix_equal(decode_payload(changed_h).preparation, common_preparation),
        "final geometry retains five-way causal-root ambiguity; erasing the scalar token aliases settings, while changing H breaks preparation sharing",
    )

    plus_rate = pz
    thinned = simplify(plus_rate / (plus_rate + (1 - plus_rate) / 2))
    check(
        "outcome-dependent-thinning-control",
        thinned == Q(4, 9) and thinned != plus_rate,
        "keeping shared-minus outcomes at half rate moves the coarse plus ratio from 2/7 to 4/9",
    )

    x_path = CANONICAL_CARRIER_PATH
    y_path = (
        (5, 4, 0), (4, 4, 0), (5, 3, 0), (3, 4, 0), (3, 3, 0),
        (3, 3, -1), (4, 3, -1), (3, 3, 1), (4, 3, 1), (3, 2, 0), (4, 2, 0),
    )
    payload_b = simplify(2 * BASE_PAYLOAD)
    collision_records = {x_path[0]: BASE_PAYLOAD, y_path[0]: payload_b}
    jointly_reachable = True
    for stage, candidate in enumerate(x_path[1:9], start=1):
        current = actual_growth_frontier(collision_records)
        jointly_reachable = jointly_reachable and any(
            match[0] == stage and matrix_equal(match[3], BASE_PAYLOAD)
            for match in current.get(candidate, ())
        )
        collision_records[candidate] = BASE_PAYLOAD
    for stage, candidate in enumerate(y_path[1:9], start=1):
        current = actual_growth_frontier(collision_records)
        jointly_reachable = jointly_reachable and any(
            match[0] == stage and matrix_equal(match[3], payload_b)
            for match in current.get(candidate, ())
        )
        collision_records[candidate] = payload_b
    frontier = actual_growth_frontier(collision_records)
    x_ten, y_ten = x_path[9], y_path[9]
    after_x = dict(collision_records)
    after_x[x_ten] = BASE_PAYLOAD

    def sites_for(payload):
        return {
            site for site, matches in frontier.items()
            if any(matrix_equal(match[3], payload) for match in matches)
        }

    after_y = {
        site for site, matches in actual_growth_frontier(after_x).items()
        if any(matrix_equal(match[3], payload_b) for match in matches)
    }
    check(
        "radius-eight-collision-mutation",
        l1_distance(x_path[0], y_path[0]) == 9
        and root_eligible({x_path[0]: BASE_PAYLOAD}, y_path[0], radius=8)
        and jointly_reachable
        and sites_for(BASE_PAYLOAD) == {x_ten}
        and sites_for(payload_b) == {y_ten}
        and l1_distance(x_ten, y_ten) == 1
        and not after_y,
        "deleting one exclusion layer restores the exact P9/P9 fork and one writer jams the other",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    required = (
        "Record-visible setting",
        "same-process forgetting",
        "context-skew",
        "non-collinear ternary",
        "does not force trace",
        "No Minimal Axioms edit",
        "TOE percentages remain unchanged",
        "N1 — Alternative Route Enumeration",
        "N8 — Cross-Cycle Echo",
    )
    check(
        "source-contract",
        all(fragment in note_text for fragment in required),
        "the note binds the selected construction, exact mutant, non-trace boundary, axiom posture, score posture, and N1-N8 gate",
    )

    print("per_element: every effect matrix, scalar label, trace mass, and context-skew mass is checked")
    print("per_site: four pre-outcome setting payloads and eleven terminal outcomes are parsed at each site role")
    print("per_mode: checked and not executed — no spectral-mode or mode-exhaustion claim is made")
    print("per_block: all 895 unfinished shapes and 1320 completed setting/outcome components are checked")
    print("lattice_wide: checked and not executed — ergodicity is analytic; the runner checks cylinder and Følner algebra only")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
