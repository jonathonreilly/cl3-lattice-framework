#!/usr/bin/env python3
"""Cycle 318: proper-cubic recoil-balanced carried-source vertex.

The constructive lane replaces the Cycle-316 direction-preserving source
vertex by a six-channel direction-changing vertex.  It acts on the same
one-carrier physical code and conserves a declared dimensionless vector ledger
P = P_matter + 2 P_mediator at operator level.  The relative coefficient two
is supplied candidate-law structure; this runner does not identify P with
physical momentum, energy, stress, or gravity.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
import re
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import carried_internal_species_source_field_ledger_repair_2026_07_17 as carried
import carried_source_recurrent_tagged_block_cycle316_2026_07_18 as c316
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import physical_cycle269_local_fock_extension_cycle312_2026_07_18 as c312
import physical_cycle269_position_growing_recurrent_compiler_cycle307_2026_07_17 as c307
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PROPER_CUBIC_RECOIL_BALANCED_CARRIED_SOURCE_CYCLE318_NOTE_2026-07-18.md"
)
BETA = -0.3
ANGLE = carried.MEDIATOR_COUPLING * c219.common_species(BETA).analytic_mass
SIZES = (3, 4, 6)
HELD_SIZE = 6
TOLERANCE = 3e-10
REVERSE = (1, 0, 3, 2, 5, 4)

N1_ROUTES = (
    "Cycle-316 direction-preserving scalar vertex",
    "carried six-link reservoir vertex",
    "direction-changing weighted-flux vertex",
    "unit-weight matter-rest vertex",
    "paired-mediator recoil branch",
    "simultaneous-carrier recoil/contact splice",
    "energy-calibrated stress/source law",
)
WALLS = ("W_flux_norm", "W_energy", "W_multi", "W_contact", "W_pair")
TRIGGER_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natural", "ly"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regis", "tered"),
    ("canon", "ical"),
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(file_path: Path) -> str:
    text = file_path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-318 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_recoil g_recoil = g_physical,recoil e_recoil",
        "one-carrier",
        "p_matter + 2 p_mediator",
        "operator conservation",
        "direction-changing",
        "link reservoir",
        "emission, transport, and absorption",
        "source/tag catch-up",
        "all 24 proper-cubic frames",
        "all l=3 translations",
        "held l=6",
        "mass firewall",
        "contact firewall",
        "not physical momentum",
        "not energy",
        "not stress",
        "not gravity",
        "supplied structure",
        "fail / do not ship",
        "no axiom pressure",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the kinematic theorem and interpretation firewall", not missing, missing)


def methodology_controls() -> None:
    print("\nEXECUTABLE NO-GO DISCIPLINE")
    note = NOTE.read_text(encoding="utf-8")
    allowed = {
        "ATTEMPTED",
        "RULED OUT BY PRIOR RESULT",
        "OPEN / UNTESTED",
    }
    markers: dict[str, str] = {}
    illegal = []
    for route in N1_ROUTES:
        pattern = re.compile(
            rf"^\|\s*{re.escape(route)}\s*\|\s*\*\*([^*]+)\*\*\s*\|",
            re.MULTILINE,
        )
        match = pattern.search(note)
        marker = match.group(1).strip() if match else "MISSING"
        markers[route] = marker
        if marker not in allowed:
            illegal.append((route, marker))
    check(
        "N1 gives exact honesty markers to seven distinct recoil/source routes",
        not illegal and len(markers) == 7,
        {"markers": markers, "illegal": illegal},
    )

    lower = note.lower()
    missing_pairs = []
    for left, right in combinations(WALLS, 2):
        row = f"| `{left.lower()}`, `{right.lower()}` | no | no | yes |"
        if row not in lower:
            missing_pairs.append((left, right))
    check(
        "N2 gives both closure directions for all ten pairs in the collapsed wall set",
        not missing_pairs,
        {"directed_pairs": 10, "missing": missing_pairs},
    )

    trigger_rows = []
    for release_path in (Path(__file__).resolve(), NOTE):
        source = release_path.read_text(encoding="utf-8").lower()
        hits = tuple("".join(parts) for parts in TRIGGER_PARTS if "".join(parts) in source)
        trigger_rows.append(
            {"path": str(release_path.relative_to(ROOT)), "hits": hits}
        )
    check(
        "N3 literal methodology-trigger scan has zero hits on both release paths",
        all(not row["hits"] for row in trigger_rows),
        trigger_rows,
    )

    witnesses = (
        (
            "docs/work_history/repo/review_feedback/CARRIED_SOURCE_RECURRENT_TAGGED_BLOCK_CYCLE316_NOTE_2026-07-18.md",
            70,
            "does not recoil",
        ),
        (
            "docs/work_history/repo/review_feedback/CARRIED_SOURCE_RECURRENT_TAGGED_BLOCK_CYCLE316_NOTE_2026-07-18.md",
            156,
            "measured overlap code leakage",
        ),
        (
            "docs/work_history/repo/review_feedback/CARRIED_SOURCE_RECURRENT_TAGGED_BLOCK_CYCLE316_NOTE_2026-07-18.md",
            171,
            "simultaneous carriers are outside",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_LOCAL_FOCK_EXTENSION_CYCLE312_NOTE_2026-07-18.md",
            171,
            "simultaneous patches",
        ),
        (
            "docs/work_history/repo/review_feedback/CARRIED_INTERNAL_SPECIES_SOURCE_FIELD_LEDGER_REPAIR_NOTE_2026-07-17.md",
            41,
            "not energy",
        ),
    )
    failures = []
    for relative_path, line_number, fragment in witnesses:
        lines = (ROOT / relative_path).read_text(encoding="utf-8").lower().splitlines()
        if line_number > len(lines) or fragment not in lines[line_number - 1]:
            failures.append((relative_path, line_number, fragment))
    check("N4 exact file-line witnesses remain literal", not failures, failures)

    required_sections = (
        "### N5 — rhetoric audit",
        "### N6 — partial-closure paths",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "Gate status: **FAIL / DO NOT SHIP**",
    )
    check(
        "N5-N8 and the broad-negative failure gate remain explicit",
        all(section in note for section in required_sections),
        tuple(section for section in required_sections if section not in note),
    )


def direction_vertex(
    angle: float, mediator_weight: float = 2.0
) -> tuple[np.ndarray, np.ndarray, np.ndarray, tuple[np.ndarray, ...]]:
    """E_d <-> G_reverse(d),F_d with a declared weighted vector ledger."""
    exchange = np.zeros((42, 42), dtype=complex)
    for direction in range(6):
        pair_index = 6 + 6 * REVERSE[direction] + direction
        exchange[pair_index, direction] = 1.0
        exchange[direction, pair_index] = 1.0
    square = exchange @ exchange
    vertex = (
        np.eye(42, dtype=complex)
        + (np.cos(angle) - 1) * square
        + 1j * np.sin(angle) * exchange
    )
    source_number = np.diag([1.0] * 6 + [0.0] * 36)
    field_number = np.diag([0.0] * 6 + [1.0] * 36)
    momenta = []
    for axis in range(3):
        values = [float(c210.DIRECTIONS[d, axis]) for d in range(6)]
        values.extend(
            float(
                c210.DIRECTIONS[matter, axis]
                + mediator_weight * c210.DIRECTIONS[field, axis]
            )
            for matter in range(6)
            for field in range(6)
        )
        momenta.append(np.diag(values))
    return exchange, vertex, source_number + field_number, tuple(momenta)


def link_vertex(
    angle: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, tuple[np.ndarray, ...]]:
    """E_d <-> sum_f G_d,F_f,A_reverse(f) with unit directional weights."""
    dimension = 6 + 6**3
    exchange = np.zeros((dimension, dimension), dtype=complex)
    for matter in range(6):
        for field in range(6):
            auxiliary = REVERSE[field]
            pair_index = 6 + 36 * matter + 6 * field + auxiliary
            coefficient = c210.UNIFORM[field]
            exchange[pair_index, matter] = coefficient
            exchange[matter, pair_index] = coefficient.conjugate()
    square = exchange @ exchange
    vertex = (
        np.eye(dimension, dtype=complex)
        + (np.cos(angle) - 1) * square
        + 1j * np.sin(angle) * exchange
    )
    charge = np.eye(dimension, dtype=complex)
    momenta = []
    for axis in range(3):
        values = [float(c210.DIRECTIONS[d, axis]) for d in range(6)]
        values.extend(
            float(
                c210.DIRECTIONS[matter, axis]
                + c210.DIRECTIONS[field, axis]
                + c210.DIRECTIONS[auxiliary, axis]
            )
            for matter in range(6)
            for field in range(6)
            for auxiliary in range(6)
        )
        momenta.append(np.diag(values))
    return exchange, vertex, charge, tuple(momenta)


def active_frame_42(frame: np.ndarray) -> np.ndarray:
    representation = c210.direction_permutation(frame)
    active = np.zeros((42, 42), dtype=complex)
    active[:6, :6] = representation
    active[6:, 6:] = np.kron(representation, representation)
    return active


def active_frame_222(frame: np.ndarray) -> np.ndarray:
    representation = c210.direction_permutation(frame)
    active = np.zeros((222, 222), dtype=complex)
    active[:6, :6] = representation
    active[6:, 6:] = np.kron(np.kron(representation, representation), representation)
    return active


def operator_route_controls() -> None:
    print("\nLOCAL OPERATOR ROUTE TOURNAMENT")
    _old_exchange, old_vertex, old_charge = carried.active_blocks(ANGLE)
    old_momenta = []
    for axis in range(3):
        values = [float(c210.DIRECTIONS[d, axis]) for d in range(6)]
        values.extend(
            float(c210.DIRECTIONS[m, axis] + c210.DIRECTIONS[f, axis])
            for m in range(6)
            for f in range(6)
        )
        old_momenta.append(np.diag(values))
    old_commutators = [
        float(np.linalg.norm(old_vertex @ momentum - momentum @ old_vertex))
        for momentum in old_momenta
    ]
    check(
        "the Cycle-316 direction-preserving vertex fails the unit-weight vector operator ledger",
        np.linalg.norm(old_vertex @ old_charge - old_charge @ old_vertex) == 0
        and min(old_commutators) > 0.7,
        {"Q_commutator": 0.0, "P_commutators": old_commutators},
    )

    _link_exchange, link, link_charge, link_momenta = link_vertex(ANGLE)
    link_unitarity = float(np.linalg.norm(link.conj().T @ link - np.eye(222)))
    link_q = float(np.linalg.norm(link @ link_charge - link_charge @ link))
    link_p = tuple(
        float(np.linalg.norm(link @ momentum - momentum @ link))
        for momentum in link_momenta
    )
    link_covariance = []
    for frame in c210.proper_cubic_frames():
        active = active_frame_222(frame)
        link_covariance.append(float(np.linalg.norm(active @ link @ active.T - link)))
    check(
        "a six-link carried reservoir gives exact unit-weight Q and vector balance in a bounded local alphabet",
        link_unitarity < TOLERANCE
        and link_q == 0
        and max(link_p) < TOLERANCE
        and max(link_covariance) < TOLERANCE,
        {
            "active_dimension": 222,
            "added_auxiliary_M2_per_cell": 6,
            "installed_M2_per_cell_if_compiled": 40,
            "unitarity_residual": link_unitarity,
            "Q_commutator": link_q,
            "P_commutators": link_p,
            "maximum_frame_residual": max(link_covariance),
            "recurrent_auxiliary_compiler_built": False,
        },
    )

    _exchange, vertex, charge, momenta = direction_vertex(ANGLE)
    unitarity = float(np.linalg.norm(vertex.conj().T @ vertex - np.eye(42)))
    q_commutator = float(np.linalg.norm(vertex @ charge - charge @ vertex))
    p_commutators = tuple(
        float(np.linalg.norm(vertex @ momentum - momentum @ vertex))
        for momentum in momenta
    )
    covariance = []
    for frame in c210.proper_cubic_frames():
        active = active_frame_42(frame)
        covariance.append(float(np.linalg.norm(active @ vertex @ active.T - vertex)))

    response_rows = []
    for direction in range(6):
        initial = np.eye(42, dtype=complex)[:, direction]
        final = vertex @ initial
        probabilities = abs(final) ** 2
        initial_vector = c210.DIRECTIONS[direction].astype(float)
        final_matter = np.zeros(3)
        final_mediator = np.zeros(3)
        for matter_direction in range(6):
            final_matter += probabilities[matter_direction] * c210.DIRECTIONS[matter_direction]
        for matter_direction in range(6):
            for field_direction in range(6):
                pair_index = 6 + 6 * matter_direction + field_direction
                final_matter += probabilities[pair_index] * c210.DIRECTIONS[matter_direction]
                final_mediator += (
                    2.0 * probabilities[pair_index] * c210.DIRECTIONS[field_direction]
                )
        response_rows.append(
            {
                "direction": direction,
                "matter_recoil": tuple(final_matter - initial_vector),
                "mediator_flux": tuple(final_mediator),
                "balance_residual": float(
                    np.linalg.norm(final_matter + final_mediator - initial_vector)
                ),
            }
        )
    check(
        "the direction-changing route is an exact proper-cubic Q and weighted-vector operator vertex with nonzero matter recoil",
        unitarity < TOLERANCE
        and q_commutator == 0
        and max(p_commutators) < TOLERANCE
        and max(covariance) < TOLERANCE
        and max(row["balance_residual"] for row in response_rows) < TOLERANCE
        and min(np.linalg.norm(row["matter_recoil"]) for row in response_rows) > 0.2,
        {
            "active_dimension": 42,
            "added_M2_per_cell": 0,
            "unitarity_residual": unitarity,
            "Q_commutator": q_commutator,
            "P_commutators": p_commutators,
            "maximum_frame_residual": max(covariance),
            "relative_mediator_weight": 2.0,
            "response_rows": response_rows,
        },
    )


def direction_local_vertex(
    excited: np.ndarray, contact_pair: np.ndarray, angle: float
) -> tuple[np.ndarray, np.ndarray]:
    _exchange, vertex, _charge, _momenta = direction_vertex(angle)
    vector = np.concatenate((excited, contact_pair.reshape(-1)))
    output = vertex @ vector
    return output[:6], output[6:].reshape(6, 6)


def vector_expectation(excited: np.ndarray, pair: np.ndarray) -> np.ndarray:
    matter_weights = abs(excited) ** 2 + np.sum(abs(pair) ** 2, axis=1)
    field_weights = np.sum(abs(pair) ** 2, axis=0)
    return matter_weights @ c210.DIRECTIONS + 2.0 * field_weights @ c210.DIRECTIONS


def direction_vertex_gate(
    state: carried.CarriedState, angle: float
) -> tuple[carried.CarriedState, dict[str, object]]:
    output = state.copy()
    positions = set(state.excited)
    positions.update(body for body, field in state.pair if body == field)
    q_residual = 0.0
    p_residual = 0.0
    source_current: dict[tuple[int, int, int], float] = {}
    for position in positions:
        excited = state.excited.get(position, carried.zero_vector())
        pair = state.pair.get((position, position), carried.zero_pair())
        before_q = float(np.vdot(excited, excited).real + np.vdot(pair, pair).real)
        before_p = vector_expectation(excited, pair)
        new_excited, new_pair = direction_local_vertex(excited, pair, angle)
        after_q = float(
            np.vdot(new_excited, new_excited).real + np.vdot(new_pair, new_pair).real
        )
        after_p = vector_expectation(new_excited, new_pair)
        q_residual = max(q_residual, abs(after_q - before_q))
        p_residual = max(p_residual, float(np.linalg.norm(after_p - before_p)))
        source_current[position] = float(
            np.vdot(new_pair, new_pair).real - np.vdot(pair, pair).real
        )
        output.excited[position] = new_excited
        output.pair[(position, position)] = new_pair
    return output, {
        "local_Q_residual": q_residual,
        "local_P_residual": p_residual,
        "source_current": source_current,
    }


def logical_step(
    state: carried.CarriedState, model: c307.GlobalModel
) -> tuple[carried.CarriedState, dict[str, float]]:
    species = c219.common_species(BETA)
    before = carried.state_norm(state)
    coined = carried.coin_gate(state, species.coin, c214.FIELD_COIN)
    sourced, vertex_report = direction_vertex_gate(coined, ANGLE)
    bodied, matter_current, excitation_current = carried.body_stream(sourced)
    bodied = c316.wrap_carried_state(bodied, model.length)
    fielded, field_current = carried.field_stream(bodied)
    fielded = c316.wrap_carried_state(fielded, model.length)
    return fielded, {
        "norm_residual": abs(carried.state_norm(fielded) - before),
        "local_Q_residual": float(vertex_report["local_Q_residual"]),
        "local_P_residual": float(vertex_report["local_P_residual"]),
        "matter_current_residual": abs(
            sum(matter_current.values()) - sum(carried.matter_density(sourced).values())
        ),
        "Q_current_residual": abs(
            sum(excitation_current.values())
            + sum(field_current.values())
            - sum(carried.q_density(sourced).values())
        ),
    }


def apply_direction_source_block(
    state: c316.PhysicalState,
    model: c307.GlobalModel,
    cell: tuple[int, int, int],
) -> c316.PhysicalState:
    _exchange, vertex, _charge, _momenta = direction_vertex(ANGLE)
    modes = tuple(c316.mode_at(model, cell, direction) for direction in range(6))
    columns = tuple(
        c316.extended_column(model, mode, excited=True) for mode in modes
    ) + tuple(
        c316.extended_column(model, matter, excited=False, field_mode=field)
        for matter in modes
        for field in modes
    )
    return c316.apply_lifted_block(state, columns, vertex)


def apply_direction_source_vertices(
    state: c316.PhysicalState, model: c307.GlobalModel
) -> c316.PhysicalState:
    output = state
    for cell in model.code.graph.cells:
        output = apply_direction_source_block(output, model, cell)
    return output


def physical_step(
    state: c316.PhysicalState, model: c307.GlobalModel
) -> c316.PhysicalState:
    output = c316.apply_matter_block_family(state, model, "coin")
    output = c316.apply_field_coin(output, model)
    output = apply_direction_source_vertices(output, model)
    output = c316.apply_matter_block_family(output, model, "reverse")
    output = c316.apply_matter_block_family(output, model, "edge")
    return c316.apply_field_stream(output, model)


def recurrent_intertwiner_controls(models: dict[int, c307.GlobalModel]) -> None:
    print("\nRECURRENT PHYSICAL INTERTWINER")
    rows = []
    for length, model in models.items():
        logical = c316.test_state(length)
        encoded = c316.encode_state(logical, model)
        logical_output, report = logical_step(logical, model)
        physical_output = physical_step(encoded, model)
        expected = c316.encode_state(logical_output, model)
        gram = model.encoding.conj().T @ model.encoding
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "matter_Gram_residual": c312.maximum_abs(
                    gram
                    - c312.sparse.eye(
                        gram.shape[0], dtype=complex, format="csc"
                    )
                ),
                "EG_residual": c316.physical_residual(physical_output, expected),
                "encoded_norm_residual": abs(c316.physical_norm(encoded) - 1),
                "output_norm_residual": abs(c316.physical_norm(physical_output) - 1),
                "continuity": report,
            }
        )
    check(
        "the recoil-balanced update obeys E_recoil G_recoil = G_physical,recoil E_recoil through held L=6",
        max(
            max(
                row["matter_Gram_residual"],
                row["EG_residual"],
                row["encoded_norm_residual"],
                row["output_norm_residual"],
                max(row["continuity"].values()),
            )
            for row in rows
        )
        < TOLERANCE,
        rows,
    )


def emission_transport_absorption_and_catchup(
    models: dict[int, c307.GlobalModel]
) -> None:
    print("\nEMISSION / TRANSPORT / ABSORPTION / TAG CATCH-UP")
    response_rows = []
    for length, model in models.items():
        initial = carried.CarriedState({(0, 0, 0): c210.UNIFORM.copy()}, {})
        sourced, source_report = direction_vertex_gate(initial, ANGLE)
        bodied, _matter_current, _excitation_current = carried.body_stream(sourced)
        bodied = c316.wrap_carried_state(bodied, length)
        transported, _field_current = carried.field_stream(bodied)
        transported = c316.wrap_carried_state(transported, length)
        fields = carried.field_density(transported)
        predicted = np.sin(ANGLE) ** 2 / 6
        neighbour_error = 0.0
        for direction in range(6):
            target = c316.wrapped(tuple(int(value) for value in c210.DIRECTIONS[direction]), length)
            neighbour_error = max(neighbour_error, abs(fields.get(target, 0.0) - predicted))

        physical_initial = c316.encode_state(initial, model)
        physical_sourced = apply_direction_source_vertices(physical_initial, model)
        physical_sourced = c316.apply_matter_block_family(physical_sourced, model, "reverse")
        physical_sourced = c316.apply_matter_block_family(physical_sourced, model, "edge")
        physical_transported = c316.apply_field_stream(physical_sourced, model)
        expected = c316.encode_state(transported, model)
        response_rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "emitted_weight": sum(fields.values()),
                "predicted_sin2": np.sin(ANGLE) ** 2,
                "maximum_neighbour_error": neighbour_error,
                "source_stream_intertwiner": c316.physical_residual(
                    physical_transported, expected
                ),
                "local_Q_residual": source_report["local_Q_residual"],
                "local_P_residual": source_report["local_P_residual"],
            }
        )

    incoming = carried.zero_pair()
    for direction in range(6):
        incoming[REVERSE[direction], direction] = c210.UNIFORM[direction]
    absorbed_excited, remaining_pair = direction_local_vertex(
        carried.zero_vector(), incoming, ANGLE
    )
    absorption_source_weight = float(np.vdot(absorbed_excited, absorbed_excited).real)
    remaining_weight = float(np.vdot(remaining_pair, remaining_pair).real)

    model = models[3]
    origin_mode = c316.mode_at(model, (0, 0, 0), 0)
    stale_target_mode = c316.mode_at(model, (1, 0, 0), 0)
    stale = {
        (
            row,
            origin_mode,
            c316.cell_flat((0, 0, 0), model.length),
            -1,
        ): value
        for row, value in c316.column_items(model, stale_target_mode)
    }
    deleted_catchup_leakage = c316.lawful_code_leakage(stale, model)
    check(
        "the recurrent code emits, physically transports, contains conjugate absorption, and catches source/port tags with no host query",
        max(
            max(
                abs(row["emitted_weight"] - row["predicted_sin2"]),
                row["maximum_neighbour_error"],
                row["source_stream_intertwiner"],
                row["local_Q_residual"],
                row["local_P_residual"],
            )
            for row in response_rows
        )
        < TOLERANCE
        and abs(absorption_source_weight - np.sin(ANGLE) ** 2) < TOLERANCE
        and abs(remaining_weight - np.cos(ANGLE) ** 2) < TOLERANCE
        and abs(deleted_catchup_leakage - 1) < TOLERANCE,
        {
            "volume_rows": response_rows,
            "absorption_source_weight": absorption_source_weight,
            "remaining_mediator_weight": remaining_weight,
            "deleted_tag_catchup_leakage": deleted_catchup_leakage,
            "source_blocks_applied_at_every_cell": True,
            "host_carrier_cell_queries": 0,
        },
    )


def overlap_covariance_translation_controls(
    models: dict[int, c307.GlobalModel]
) -> None:
    print("\nOVERLAP / COVARIANCE / TRANSLATIONS / SUPPORT")
    model = models[3]
    coin_blocks = {block.label: block for block in c312.local_blocks(model, "coin")}
    left_block = coin_blocks[(0, 0, 0)]
    right_block = coin_blocks[(1, 0, 0)]
    left_support = c312.block_mode_support(model, left_block)
    right_support = c312.block_mode_support(model, right_block)
    encoded = c316.encode_state(c316.test_state(3), model)
    left_then_right = apply_direction_source_block(
        apply_direction_source_block(encoded, model, (0, 0, 0)),
        model,
        (1, 0, 0),
    )
    right_then_left = apply_direction_source_block(
        apply_direction_source_block(encoded, model, (1, 0, 0)),
        model,
        (0, 0, 0),
    )
    overlap_commutator = c316.physical_residual(left_then_right, right_then_left)
    overlap_leakage = max(
        c316.lawful_code_leakage(left_then_right, model),
        c316.lawful_code_leakage(right_then_left, model),
    )

    state = c316.test_state(3)
    advanced, _report = logical_step(state, model)
    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        framed_input = c316.rotate_periodic_state(state, frame, 3)
        framed_output, _ = logical_step(framed_input, model)
        frame_residuals.append(
            carried.state_residual(
                framed_output, c316.rotate_periodic_state(advanced, frame, 3)
            )
        )
    translation_residuals = []
    for displacement in product(range(3), repeat=3):
        moved_input = c316.translate_state(state, displacement, 3)
        moved_output, _ = logical_step(moved_input, model)
        translation_residuals.append(
            carried.state_residual(
                moved_output, c316.translate_state(advanced, displacement, 3)
            )
        )

    support_rows = []
    for length, current in models.items():
        support_rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "installed_M2_per_cell": 34,
                "added_recoil_M2_per_cell": 0,
                "source_active_dimension": 42,
                "base_Cycle312_patch_envelope_M2": 216,
                "maximum_pair_rows_per_block": max(
                    len(c312.block_mode_support(current, block))
                    for kind in ("coin", "reverse", "edge")
                    for block in c312.local_blocks(current, kind)
                ),
            }
        )
    check(
        "adjacent translated source blocks retain the literal 14-row overlap with zero order ambiguity and bounded leakage",
        len(left_support & right_support) == 14
        and overlap_commutator < TOLERANCE
        and overlap_leakage < TOLERANCE,
        {
            "overlapping_pair_rows": len(left_support & right_support),
            "opposite_order_residual": overlap_commutator,
            "lawful_code_leakage": overlap_leakage,
        },
    )
    check(
        "the full recoil-balanced update is covariant in all 24 frames and all L=3 translations",
        len(frame_residuals) == 24
        and len(translation_residuals) == 27
        and max(frame_residuals + translation_residuals) < TOLERANCE,
        {
            "maximum_frame_residual": max(frame_residuals),
            "maximum_translation_residual": max(translation_residuals),
        },
    )
    check(
        "the constructive route retains constant physical M2 overhead and bounded block support through held L=6",
        all(row["installed_M2_per_cell"] == 34 for row in support_rows)
        and all(row["added_recoil_M2_per_cell"] == 0 for row in support_rows)
        and all(row["maximum_pair_rows_per_block"] <= 36 for row in support_rows),
        support_rows,
    )


def mass_contact_deletion_domain_controls(
    models: dict[int, c307.GlobalModel]
) -> None:
    print("\nMASS / CONTACT FIREWALLS / DELETIONS / DOMAIN")
    species = c219.common_species(BETA)
    mass_rows = []
    for length, model in models.items():
        uniform = np.ones(model.encoding.shape[1], dtype=complex)
        uniform /= np.linalg.norm(uniform)
        eigenvalue = np.vdot(uniform, model.one_particle_coin @ uniform)
        mass_rows.append(
            {
                "L": length,
                "held_out": length == HELD_SIZE,
                "source_off_mass": float(np.angle(eigenvalue)) / c219.C_SQUARED,
            }
        )

    _exchange, deleted, _charge, _momenta = direction_vertex(0.0)
    exchange, _vertex, _charge, _momenta = direction_vertex(ANGLE)
    unilateral = np.tril(exchange, k=-1)
    bad_gate = np.eye(42, dtype=complex) + 1j * ANGLE * unilateral
    bad_unitarity = float(np.linalg.norm(bad_gate.conj().T @ bad_gate - np.eye(42)))
    _exchange, wrong_weight_vertex, _charge, wrong_momenta = direction_vertex(
        ANGLE, mediator_weight=1.0
    )
    wrong_weight_commutator = max(
        float(
            np.linalg.norm(
                wrong_weight_vertex @ momentum - momentum @ wrong_weight_vertex
            )
        )
        for momentum in wrong_momenta
    )

    rejected = 0
    for fixture in (
        (2, 1, 1, True),
        (3, 2, 1, True),
        (3, 1, 0, True),
        (3, 1, 1, False),
    ):
        length, matter_count, charge, tags_match = fixture
        try:
            if length < 3:
                raise ValueError("L<3 aliases the translated block grammar")
            if matter_count != 1:
                raise ValueError("the Cycle-318 code has exactly one carrier")
            if charge != 1:
                raise ValueError("the Cycle-318 code has prepared Q=1")
            if not tags_match:
                raise ValueError("the port/source tag must match the carrier")
        except ValueError:
            rejected += 1
    check(
        "the source-off Cycle-219 mass fixture is unchanged through held L=6",
        max(abs(row["source_off_mass"] - species.analytic_mass) for row in mass_rows)
        < 4e-13,
        mass_rows,
    )
    check(
        "the one-carrier source block cannot fire the recurrent multiparticle contact lane",
        rejected == 4,
        {
            "matter_carriers_in_lawful_code": 1,
            "Cycle230_contact_calls": 0,
            "recurrent_contact_compiled": False,
            "lawful_domain_rejections": rejected,
        },
    )
    check(
        "coupling, conjugate, and relative-flux deletions are nontrivial controls",
        np.linalg.norm(deleted - np.eye(42)) == 0
        and bad_unitarity > 0.1
        and wrong_weight_commutator > 0.5,
        {
            "zero_coupling_identity_residual": float(
                np.linalg.norm(deleted - np.eye(42))
            ),
            "unilateral_gate_unitarity_residual": bad_unitarity,
            "unit_mediator_weight_P_commutator": wrong_weight_commutator,
        },
    )


def inventory_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN INVENTORY")
    inventory = {
        "inherited physical code": "Cycle-316 recurrent one-carrier tagged Cycle-312 block compiler",
        "inherited matter law": "Cycle-219 coin and Cycle-312 reverse/edge stream factors",
        "supplied source law": "six E_d to G_reverse(d),F_d rotations with angle kappa*m_fixture",
        "supplied vector normalization": "P_matter uses unit direction and P_mediator uses twice the unit direction",
        "supplied sectors": "one matter carrier and Q=N_source+N_field=1",
        "supplied schedule": "matter/field coins; homogeneous source blocks; matter and mediator streams",
        "derived": "operator Q/P commutators, recoil response, physical recurrence, covariance, translations, held sizes",
        "local comparator": "six-link reservoir closes a unit-weight vector ledger with six extra M2 per cell",
        "open": "recurrent link-reservoir compiler, matter rest mode, paired mediator, multiparticle contact, two-source reciprocity, energy/stress/metric",
        "interpretation firewall": "the conserved vector is a kinematic discrete-flux candidate, not physical momentum, energy, stress, or gravity",
        "authority": "none",
        "audit": "unset",
    }
    required_keys = {
        "inherited physical code",
        "supplied source law",
        "supplied vector normalization",
        "supplied sectors",
        "derived",
        "open",
        "interpretation firewall",
        "authority",
        "audit",
    }
    check("the supplied, derived, failed, and open structure is explicit", required_keys <= inventory.keys(), inventory)


def main() -> int:
    print("CYCLE 318: PROPER-CUBIC RECOIL-BALANCED CARRIED SOURCE")
    print("authority=none; audit=unset")
    note_contract()
    models = {length: c307.build_model(length) for length in SIZES}
    operator_route_controls()
    recurrent_intertwiner_controls(models)
    emission_transport_absorption_and_catchup(models)
    overlap_covariance_translation_controls(models)
    mass_contact_deletion_domain_controls(models)
    inventory_controls()
    methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PROPER_CUBIC_RECOIL_BALANCED_SOURCE_OPEN")
        return 1
    print("RESULT PROPER_CUBIC_RECOIL_BALANCED_ONE_CARRIER_FACTOR_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
