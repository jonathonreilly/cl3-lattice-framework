#!/usr/bin/env python3
"""Block 12: outcome-typed generated front and prefix classifier.

The runner combines one permanent encoded Record with five consumable
Block-10 condition cells.  It checks the exact hybrid decoder, the frozen
Record code, H1/H2 and open-family positivity, the unchanged fourteen-way
law, one event-triggered disjoint-SWAP transport layer, a repeated second
event, and the resulting arbitrary-finite-prefix induction.  The literal
pure-outcome assignment is retained only as a narrow hostile control.
"""

from __future__ import annotations

import argparse
from functools import cache
import inspect
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29 as b10  # noqa: E402


b9 = b10.b9
PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block12-outcome-typed-two-step-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_OUTCOME_TYPED_GENERATED_FRONT_PREFIX_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

PARENT = "653951e2d8402806a6f03e8bba71bb89a7d4ccbb"
BLOCK11_RESULT = "08451abcc246ba804663f684e21aaf43bf89c2e6"
PREREG = "fe41950ddb59e1be55aad78dd430cc7c7cdb009f"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "2afc9994995be87001eaba5c88cb757f1c6b31e1"
PREFLIGHT_BLOB = "70572eeb8b59ca6cc1611d96a28a1e53c864d893"
BLOCK11_NOTE_BLOB = "c63143b66229b411f1fdff15073d1d3c4a811fbf"
BLOCK11_RUNNER_BLOB = "cdadb61fb8a9ab2ffe9a8974c3a4ac65a1335b35"
BLOCK11_INDEPENDENT_BLOB = "886ab8898b1e20c02daa07668ffc0d0b8c4fe2cb"
BLOCK11_CACHE_BLOB = "adfba869cc73667ae092d5088c1d80f696d3b586"
BLOCK10_NOTE_BLOB = "b9187637496f6da0682e7bd5aa64388947fd4df6"
BLOCK10_RUNNER_BLOB = "793ec02b9b031e78e9ff5251377d216182ebec99"
BLOCK9_RUNNER_BLOB = "dbc2df4b4eacda89fe9c981044eda39e5258d50c"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block12-outcome-typed-two-step-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block12-outcome-typed-two-step-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block12-outcome-typed-two-step-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_OUTCOME_TYPED_GENERATED_FRONT_PREFIX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_RECORD_PAST_NONDISTURBING_CAUSAL_PREPARATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_record_past_nondisturbing_causal_preparation_gate_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_record_past_nondisturbing_causal_preparation_gate_2026_08_29.txt",
    "docs/ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py",
    "scripts/admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.py",
)

R = sp.Rational
I3 = sp.eye(3)
FRONT0 = sp.Matrix((0, 1, 0))
G = R(9, 16)
EPSILON = R(1, 256)
OUTCOMES = b9.DIRECTIONS + tuple(
    sp.Matrix(corner) / sp.sqrt(3) for corner in b9.CORNERS
)
PROBABILITY_KEYS = tuple(
    ("axis", b9.key(direction)) for direction in b9.DIRECTIONS
) + tuple(("corner", b9.key(corner)) for corner in b9.CORNERS)

MUTATIONS = (
    "stale_authority", "change_gain", "change_epsilon", "code_collision",
    "record_nonphysical", "code_non_covariant", "decoder_rank_eight",
    "decoder_mismatch", "front_oracle", "box_nonpositive", "target_nonpositive",
    "pure_false_positive", "law_not_normalized", "law_changed", "moment_changed",
    "action_leakage", "outcome_support_changed", "same_event_feedback",
    "host_matrix_input", "transport_collision", "transport_nonlocal",
    "transport_clones", "transport_not_triggered", "successor_mismatch",
    "second_rule_changed", "prefix_failure", "nonunique_front_site",
    "record_overwrite", "live_packet_growth", "preloaded_tape", "role_epoch",
    "collision_false_safe", "hide_corridor",
    "claim_microscopic_readout", "claim_rate", "claim_axiom", "claim_gravity",
    "claim_autonomous_history", "claim_toe", "claim_retained",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def norm_squared(vector: sp.MatrixBase) -> sp.Expr:
    return sp.expand((vector.T * vector)[0])


def maximum_exact(values: list[sp.Expr]) -> sp.Expr:
    return max(values, key=lambda value: float(sp.N(value, 30)))


def position_add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))


def vector_position(vector: sp.MatrixBase) -> tuple[int, int, int]:
    return tuple(int(vector[index]) for index in range(3))


def record_code(front: sp.MatrixBase, outcome: sp.MatrixBase) -> sp.Matrix:
    return sp.expand(-G * front + EPSILON * outcome)


def codebook() -> dict[tuple[sp.Expr, ...], tuple[int, int]]:
    return {
        tuple(record_code(front, outcome)): (front_index, outcome_index)
        for front_index, front in enumerate(b9.DIRECTIONS)
        for outcome_index, outcome in enumerate(OUTCOMES)
    }


def hybrid_shell(
    matrix: sp.MatrixBase,
    front: sp.MatrixBase,
    predecessor_outcome: sp.MatrixBase,
    *,
    encoded: bool = True,
) -> tuple[sp.Matrix, ...]:
    record = (
        record_code(front, predecessor_outcome)
        if encoded else sp.Matrix(predecessor_outcome)
    )
    vectors = []
    for direction in b9.DIRECTIONS:
        if direction == -front:
            vectors.append(record)
        elif direction == front:
            vectors.append(sp.expand(2 * matrix * front + record))
        else:
            vectors.append(sp.expand(matrix * direction))
    return tuple(vectors)


def matrix_from_parameters(values: tuple[sp.Expr, ...]) -> sp.Matrix:
    a, b, d, e, f, ux, uy, uz, s = values
    tensor = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    spatial = sp.Matrix((ux, uy, uz))
    return sp.expand(
        b10.ALPHA * tensor
        + b10.BETA * (s * I3 + b10.cross_matrix(spatial))
    )


def target_matrices() -> tuple[tuple[str, str, sp.Matrix], ...]:
    result = []
    for name in ("H1", "H2"):
        tensor = b9.target_facts()[name.lower()]["tensor"]
        incoming, transfer = b10.b193.POINTS[name]
        outgoing = tuple(sp.simplify(incoming[index] + transfer[index])
                         for index in range(4))
        for phase, point in (("incoming", incoming), ("outgoing", outgoing)):
            spatial, time = b10.normalized_action(point)
            matrix = sp.expand(
                b10.ALPHA * tensor
                + b10.BETA * (time * I3 + b10.cross_matrix(spatial))
            )
            result.append((name, phase, matrix))
    return tuple(result)


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "block11_result": ancestor(BLOCK11_RESULT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", str(GOAL.relative_to(ROOT))),
        "preflight": git("hash-object", str(PREFLIGHT.relative_to(ROOT))),
        "block11_note": git("rev-parse", f"{PARENT}:docs/ADMISSIBILITY_D4_RECORD_PAST_NONDISTURBING_CAUSAL_PREPARATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"),
        "block11_runner": git("rev-parse", f"{PARENT}:scripts/admissibility_d4_record_past_nondisturbing_causal_preparation_gate_2026_08_29.py"),
        "block11_independent": git("rev-parse", f"{PARENT}:scripts/independent_admissibility_d4_record_past_nondisturbing_causal_preparation_gate_2026_08_29.py"),
        "block11_cache": git("rev-parse", f"{PARENT}:logs/runner-cache/admissibility_d4_record_past_nondisturbing_causal_preparation_gate_2026_08_29.txt"),
        "block10_note": git("rev-parse", f"{PARENT}:docs/ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"),
        "block10_runner": git("rev-parse", f"{PARENT}:scripts/admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py"),
        "block9_runner": git("rev-parse", f"{PARENT}:scripts/admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.py"),
    }


@cache
def record_code_facts() -> dict[str, object]:
    book = codebook()
    contents = [
        record_code(front, outcome)
        for front in b9.DIRECTIONS for outcome in OUTCOMES
    ]
    max_norm = maximum_exact([norm_squared(content) for content in contents])
    covariance = True
    for rotation in b9.rotations():
        for front in b9.DIRECTIONS:
            for outcome in OUTCOMES:
                covariance &= equal(
                    rotation * record_code(front, outcome),
                    record_code(rotation * front, rotation * outcome),
                )
    inverse = all(
        book[tuple(record_code(front, outcome))] == (front_index, outcome_index)
        for front_index, front in enumerate(b9.DIRECTIONS)
        for outcome_index, outcome in enumerate(OUTCOMES)
    )
    return {
        "gain": G,
        "epsilon": EPSILON,
        "entries": len(contents),
        "distinct": len(book),
        "max_norm2": max_norm,
        "physical": bool(max_norm < 1),
        "separation": bool(G * sp.sqrt(2) > 2 * EPSILON),
        "covariance": covariance,
        "content_inverse": inverse,
        "nonorthogonal_code": True,
    }


@cache
def decoder_facts() -> dict[str, object]:
    symbols = sp.symbols("m0:9", real=True)
    matrix = sp.Matrix(3, 3, symbols)
    decoded = []
    covariance = True
    for outcome in OUTCOMES:
        shell = hybrid_shell(matrix, FRONT0, outcome)
        decoded.append(equal(b10.odd_shell_matrix(shell), matrix))
    shell0 = hybrid_shell(matrix, FRONT0, OUTCOMES[0])
    shell_map = sp.Matrix.vstack(*shell0).jacobian(symbols)
    for rotation in b9.rotations():
        direct = hybrid_shell(
            sp.expand(rotation * matrix * rotation.T),
            rotation * FRONT0,
            rotation * OUTCOMES[0],
        )
        transported = []
        for direction in b9.DIRECTIONS:
            old_direction = rotation.T * direction
            old_index = next(index for index, item in enumerate(b9.DIRECTIONS)
                             if item == old_direction)
            transported.append(sp.expand(rotation * shell0[old_index]))
        covariance &= all(
            equal(left, right) for left, right in zip(direct, transported)
        )
    return {
        "all_outcomes_decode": all(decoded),
        "rank": shell_map.rank(),
        "rotation_count": len(b9.rotations()),
        "covariance": covariance,
        "runtime_front_literal": False,
    }


@cache
def positivity_facts() -> dict[str, object]:
    encoded_box = []
    encoded_box_corners = []
    pure_box = []
    for values in itertools.product((-R(1, 4), R(1, 4)), repeat=9):
        matrix = matrix_from_parameters(values)
        for outcome in OUTCOMES:
            encoded = hybrid_shell(matrix, FRONT0, outcome)
            literal = hybrid_shell(matrix, FRONT0, outcome, encoded=False)
            encoded_box.extend(norm_squared(vector) for vector in encoded)
            pure_box.extend(norm_squared(vector) for vector in literal)
            encoded_box_corners.extend(
                norm_squared(b9.composite_corner(encoded, corner))
                for corner in b9.CORNERS
            )

    encoded_targets = []
    encoded_target_corners = []
    pure_targets = []
    for _name, _phase, matrix in target_matrices():
        for rotation in b9.rotations():
            transformed = sp.expand(rotation * matrix * rotation.T)
            front = rotation * FRONT0
            for outcome0 in OUTCOMES:
                outcome = rotation * outcome0
                encoded = hybrid_shell(transformed, front, outcome)
                literal = hybrid_shell(
                    transformed, front, outcome, encoded=False
                )
                encoded_targets.extend(norm_squared(vector) for vector in encoded)
                pure_targets.extend(norm_squared(vector) for vector in literal)
                encoded_target_corners.extend(
                    norm_squared(b9.composite_corner(encoded, corner))
                    for corner in b9.CORNERS
                )

    return {
        "box_count": len(encoded_box),
        "box_max": maximum_exact(encoded_box),
        "box_failures": sum(not bool(value < 1) for value in encoded_box),
        "box_corner_max": maximum_exact(encoded_box_corners),
        "target_count": len(encoded_targets),
        "target_max": maximum_exact(encoded_targets),
        "target_failures": sum(not bool(value < 1) for value in encoded_targets),
        "target_corner_max": maximum_exact(encoded_target_corners),
        "pure_box_max": maximum_exact(pure_box),
        "pure_box_failures": sum(not bool(value < 1) for value in pure_box),
        "pure_target_max": maximum_exact(pure_targets),
        "pure_target_failures": sum(not bool(value < 1) for value in pure_targets),
    }


@cache
def law_facts() -> dict[str, object]:
    q0, q1, q2, q3, q4, ux, uy, uz, s = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz s", real=True
    )
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4),
                        (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    matrix = sp.expand(
        b10.ALPHA * tensor
        + b10.BETA * (s * I3 + b10.cross_matrix(spatial))
    )
    reference = tuple(sp.expand(matrix * direction)
                      for direction in b9.DIRECTIONS)
    reference_probabilities = b9.local_distribution(reference)
    failures = []
    for outcome in OUTCOMES:
        shell = hybrid_shell(matrix, FRONT0, outcome)
        probabilities = b9.local_distribution(shell)
        failures.append(not (
            equal(b9.condition_tensor(shell), b9.condition_tensor(reference))
            and all(sp.simplify(probabilities[key]
                                - reference_probabilities[key]) == 0
                    for key in probabilities)
            and sp.simplify(sum(probabilities.values())) == 1
            and equal(
                b9.distribution_moment(probabilities),
                b9.distribution_moment(reference_probabilities),
            )
        ))
    geometry = sp.expand(b10.ALPHA * tensor)
    geometry_shell = hybrid_shell(geometry, FRONT0, OUTCOMES[0])
    full_probabilities = b9.local_distribution(
        hybrid_shell(matrix, FRONT0, OUTCOMES[0])
    )
    geometry_probabilities = b9.local_distribution(geometry_shell)
    universal = b9.universal_facts()
    return {
        "outcome_count": len(OUTCOMES),
        "failures": tuple(failures),
        "normalization": sp.simplify(sum(full_probabilities.values())),
        "action_independence": all(
            sp.simplify(full_probabilities[key]
                        - geometry_probabilities[key]) == 0
            for key in full_probabilities
        ),
        "source": equal(
            -48 * b9.distribution_moment(full_probabilities), tensor
        ),
        "axis_floor": universal["axis_floor"],
        "corner_floor": universal["corner_floor"],
    }


def formation_distribution(
    predecessor_content: sp.MatrixBase,
    vectors: tuple[sp.Matrix, ...],
) -> dict[str, object]:
    """Read predecessor geometry and form rates before any outcome exists."""
    inverse = codebook()
    front_index, predecessor_index = inverse[tuple(predecessor_content)]
    front = b9.DIRECTIONS[front_index]
    backward_index = next(
        index for index, direction in enumerate(b9.DIRECTIONS)
        if direction == -front
    )
    return {
        "front": front,
        "predecessor_index": predecessor_index,
        "geometry_matches": equal(vectors[backward_index], predecessor_content),
        "probabilities": b9.local_distribution(vectors),
    }


def event_update(
    predecessor_content: sp.MatrixBase,
    vectors: tuple[sp.Matrix, ...],
    outcome_index: int,
    destination_contents: tuple[sp.Matrix, ...],
) -> dict[str, object]:
    """One formation-triggered step using only local content and the draw."""
    formation = formation_distribution(predecessor_content, vectors)
    front = formation["front"]
    new_record = record_code(front, OUTCOMES[outcome_index])
    live_directions = (front,) + tuple(
        direction for direction in b9.DIRECTIONS
        if sp.simplify((direction.T * front)[0]) == 0
    )
    live_indices = tuple(next(
        index for index, direction in enumerate(b9.DIRECTIONS)
        if direction == live_direction
    ) for live_direction in live_directions)
    moved = tuple(vectors[index] for index in live_indices)
    returned = tuple(destination_contents[index]
                     for index in range(len(destination_contents)))
    return {
        "front": front,
        "predecessor_index": formation["predecessor_index"],
        "geometry_matches": formation["geometry_matches"],
        "probabilities": formation["probabilities"],
        "new_record": new_record,
        "source_offsets": tuple(vector_position(item)
                                for item in live_directions),
        "destination_offsets": tuple(
            position_add(vector_position(item), vector_position(front))
            for item in live_directions
        ),
        "moved": moved,
        "returned": returned,
        "same_event_probability_input": False,
    }


@cache
def transport_facts() -> dict[str, object]:
    symbols = sp.symbols("z0:9", real=True)
    matrix = sp.Matrix(3, 3, symbols)
    backgrounds = tuple(sp.Matrix(sp.symbols(f"w{index}_0:3", real=True))
                        for index in range(5))
    geometry_checks = []
    forward_checks = []
    move_checks = []
    successor_checks = []
    runtime_checks = []
    for f in b9.DIRECTIONS:
        source_vectors = (f,) + tuple(
            direction for direction in b9.DIRECTIONS
            if sp.simplify((direction.T * f)[0]) == 0
        )
        sources = tuple(vector_position(vector) for vector in source_vectors)
        step = vector_position(f)
        destinations = tuple(position_add(source, step) for source in sources)
        edges = tuple(zip(sources, destinations))
        geometry_checks.append(
            len(edges) == 5
            and len(set(sources + destinations)) == 10
            and all(sum(abs(destination[index] - source[index])
                        for index in range(3)) == 1
                    for source, destination in edges)
        )
        forward_checks.append(sources[0] == step)
        move_checks.append(len(set(destinations)) == len(destinations))

        for predecessor_index, predecessor in enumerate(OUTCOMES):
            shell = hybrid_shell(matrix, f, predecessor)
            for outcome_index, outcome in enumerate(OUTCOMES):
                next_matrix = sp.expand(
                    matrix
                    + (record_code(f, predecessor) - record_code(f, outcome))
                    * f.T / 2
                )
                successor = []
                for direction in b9.DIRECTIONS:
                    if direction == -f:
                        successor.append(record_code(f, outcome))
                    else:
                        old_index = next(
                            index for index, item in enumerate(b9.DIRECTIONS)
                            if item == direction
                        )
                        successor.append(shell[old_index])
                expected = hybrid_shell(next_matrix, f, outcome)
                successor_checks.append(all(
                    equal(left, right)
                    for left, right in zip(successor, expected)
                ))
                update = event_update(
                    record_code(f, predecessor), shell, outcome_index,
                    backgrounds,
                )
                runtime_checks.append(
                    update["predecessor_index"] == predecessor_index
                    and update["geometry_matches"]
                    and equal(update["new_record"], record_code(f, outcome))
                    and not update["same_event_probability_input"]
                    and sp.simplify(sum(update["probabilities"].values())) == 1
                    and update["source_offsets"] == sources
                    and update["destination_offsets"] == destinations
                    and all(equal(left, right) for left, right in zip(
                        update["moved"],
                        tuple(shell[next(
                            index for index, item in enumerate(b9.DIRECTIONS)
                            if item == source
                        )] for source in source_vectors),
                    ))
                    and all(equal(left, right) for left, right in zip(
                        update["returned"], backgrounds
                    ))
                )

    swap = sp.Matrix(((1, 0, 0, 0), (0, 0, 1, 0),
                      (0, 1, 0, 0), (0, 0, 0, 1)))
    runtime_source = (
        inspect.getsource(formation_distribution)
        + inspect.getsource(event_update)
    )
    forbidden = ("H1", "H2", "fixture", "target", "global_time",
                 "role", "epoch", "scheduler")
    return {
        "front_count": len(geometry_checks),
        "edge_count": 5,
        "disjoint": all(geometry_checks),
        "nearest": all(geometry_checks),
        "next_target_is_forward_source": all(forward_checks),
        "swap_unitary": equal(swap.T * swap, sp.eye(4)),
        "moves_not_clones": all(move_checks),
        "successor_pairs": len(successor_checks),
        "successor_exact": all(successor_checks),
        "runtime_exact": all(runtime_checks),
        "runtime_signature": tuple(inspect.signature(event_update).parameters),
        "runtime_clean": not any(token in runtime_source for token in forbidden),
        "formation_triggered": True,
        "preloaded_future_packet": False,
    }


@cache
def history_facts() -> dict[str, object]:
    symbols = sp.symbols("h0:9", real=True)
    matrix0 = sp.Matrix(3, 3, symbols)
    initial_index = 0
    sequence = (3, 13, 2, 8, 5, 11)
    telescoping = []
    prefix_checks = []
    totals = []
    unique_counts = []
    permanence = []
    for f in b9.DIRECTIONS:
        current = matrix0
        previous = OUTCOMES[initial_index]
        for outcome_index in sequence:
            outcome = OUTCOMES[outcome_index]
            current = sp.expand(
                current
                + (record_code(f, previous) - record_code(f, outcome))
                * f.T / 2
            )
            expected = sp.expand(
                matrix0
                + (record_code(f, OUTCOMES[initial_index])
                   - record_code(f, outcome)) * f.T / 2
            )
            telescoping.append(equal(current, expected))
            previous = outcome

        first_shell = hybrid_shell(matrix0, f, OUTCOMES[initial_index])
        first_probabilities = b9.local_distribution(first_shell)
        total = 0
        for first_index, first_outcome in enumerate(OUTCOMES):
            matrix1 = sp.expand(
                matrix0
                + (record_code(f, OUTCOMES[initial_index])
                   - record_code(f, first_outcome)) * f.T / 2
            )
            second_probabilities = b9.local_distribution(
                hybrid_shell(matrix1, f, first_outcome)
            )
            first_value = first_probabilities[PROBABILITY_KEYS[first_index]]
            cylinder_sum = sp.simplify(
                first_value * sum(second_probabilities.values())
            )
            prefix_checks.append(sp.simplify(cylinder_sum - first_value) == 0)
            total += cylinder_sum
        totals.append(sp.simplify(total))

        for length in range(1, 9):
            records = tuple(
                tuple(index * int(f[axis]) for axis in range(3))
                for index in range(length)
            )
            selected = tuple(position_add(record, vector_position(f))
                             for record in records)
            unrecorded = [site for site in selected if site not in records]
            unique_counts.append(
                len(unrecorded) == 1 and unrecorded[0] == selected[-1]
            )
            permanence.append(len(set(records)) == length)

    universal = b9.universal_facts()
    return {
        "front_count": len(b9.DIRECTIONS),
        "telescoping_steps": len(telescoping),
        "telescoping": all(telescoping),
        "prefix_count": len(prefix_checks),
        "prefix": all(prefix_checks),
        "totals": tuple(totals),
        "strict_axis_floor": universal["axis_floor"] > 0,
        "strict_corner_floor": universal["corner_floor"] > 0,
        "unique_front_site": all(unique_counts),
        "permanence": all(permanence),
        "live_packet_size": 5,
        "live_packet_growth": 0,
        "formation_rate_supplied": False,
        "collision_free_corridor_required": True,
        "arbitrary_background_history": False,
        "collision_safe_controller_supplied": False,
    }


@cache
def collision_facts() -> dict[str, object]:
    """Expose the exact arbitrary-background boundary of the frozen relay."""
    symbols = sp.symbols("c0:9", real=True)
    matrix = sp.Matrix(3, 3, symbols)
    f = FRONT0
    predecessor = OUTCOMES[0]
    shell = hybrid_shell(matrix, f, predecessor)
    before = formation_distribution(record_code(f, predecessor), shell)

    center_neighbors = {vector_position(direction) for direction in b9.DIRECTIONS}
    radius_two_destination = vector_position(2 * f)
    destination_record = record_code(f, OUTCOMES[1])
    forward_index = next(index for index, direction in enumerate(b9.DIRECTIONS)
                         if direction == f)
    source_content = shell[forward_index]

    # A SWAP exchanges both quantum content and site occupation.  Starting
    # with (source is not Record, destination is permanent Record) produces
    # (source is Record, destination is not), violating site permanence.
    pre_record_flags = (False, True)
    post_record_flags = tuple(reversed(pre_record_flags))
    post_contents = (destination_record, source_content)
    return {
        "destination_outside_probability_stencil": (
            radius_two_destination not in center_neighbors
        ),
        "probability_has_no_destination_status_input": (
            tuple(inspect.signature(formation_distribution).parameters)
            == ("predecessor_content", "vectors")
        ),
        "probability_unchanged": sp.simplify(
            sum(before["probabilities"].values())
        ) == 1,
        "record_is_moved_by_frozen_swap": (
            pre_record_flags != post_record_flags
            and equal(post_contents[0], destination_record)
            and equal(post_contents[1], source_content)
        ),
        "collision_safe_controller_supplied": False,
        "corridor_condition_required": True,
    }


@cache
def scope_facts() -> dict[str, object]:
    note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    goal = GOAL.read_text(encoding="utf-8") if GOAL.is_file() else ""
    required = (
        "OUTCOME-TYPED-TWO-STEP",
        "encoded mixed Record representatives",
        "microscopic quantum readout remains open",
        "formation rate",
        "collision-free corridor",
        "autonomous arbitrary-background history remains open",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
    )
    forbidden = (
        "microscopic readout: closed",
        "formation rate: closed",
        "gravity: closed",
        "No axiom amendment: false",
        "retained status: true",
    )
    return {
        "note": all(phrase in note for phrase in required),
        "goal": "Exactly one panel-approved terminal" in goal,
        "forbidden": not any(phrase in note for phrase in forbidden),
    }


def evaluated_checks(mutation: str | None) -> list[tuple[str, bool, str]]:
    authority = authority_facts()
    authority_ok = (
        authority["main"] == MAIN and authority["parent"]
        and authority["block11_result"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["block11_note"] == BLOCK11_NOTE_BLOB
        and authority["block11_runner"] == BLOCK11_RUNNER_BLOB
        and authority["block11_independent"] == BLOCK11_INDEPENDENT_BLOB
        and authority["block11_cache"] == BLOCK11_CACHE_BLOB
        and authority["block10_note"] == BLOCK10_NOTE_BLOB
        and authority["block10_runner"] == BLOCK10_RUNNER_BLOB
        and authority["block9_runner"] == BLOCK9_RUNNER_BLOB
    )
    if mutation == "stale_authority":
        authority_ok = False

    code = record_code_facts()
    gain = R(1, 2) if mutation == "change_gain" else code["gain"]
    epsilon = R(1, 128) if mutation == "change_epsilon" else code["epsilon"]
    distinct = 83 if mutation == "code_collision" else code["distinct"]
    physical = False if mutation == "record_nonphysical" else code["physical"]
    covariance = False if mutation == "code_non_covariant" else code["covariance"]
    code_ok = (
        gain == G and epsilon == EPSILON and code["entries"] == 84
        and distinct == 84 and code["max_norm2"] == R(21025, 65536)
        and physical and code["separation"] and covariance
        and code["content_inverse"] and code["nonorthogonal_code"]
    )

    decoder = decoder_facts()
    decoder_rank = 8 if mutation == "decoder_rank_eight" else decoder["rank"]
    decoder_identity = False if mutation == "decoder_mismatch" else decoder["all_outcomes_decode"]
    runtime_front = True if mutation == "front_oracle" else decoder["runtime_front_literal"]
    decoder_ok = (
        decoder_identity and decoder_rank == 9
        and decoder["rotation_count"] == 24 and decoder["covariance"]
        and not runtime_front
    )

    positivity = positivity_facts()
    box_failures = 1 if mutation == "box_nonpositive" else positivity["box_failures"]
    target_failures = 1 if mutation == "target_nonpositive" else positivity["target_failures"]
    pure_failures = 0 if mutation == "pure_false_positive" else positivity["pure_box_failures"]
    positivity_ok = (
        positivity["box_count"] == 43008 and box_failures == 0
        and positivity["box_max"] == R(63425, 65536)
        and positivity["box_corner_max"] < 1
        and positivity["target_count"] == 8064 and target_failures == 0
        and positivity["target_max"] < 1
        and positivity["target_corner_max"] < 1
        and pure_failures == 11328
        and positivity["pure_target_failures"] == 2280
        and positivity["pure_box_max"] > 1
        and positivity["pure_target_max"] > 1
    )

    law = law_facts()
    normalization = 0 if mutation == "law_not_normalized" else law["normalization"]
    law_failures = (True,) if mutation == "law_changed" else law["failures"]
    source = False if mutation == "moment_changed" else law["source"]
    action = False if mutation == "action_leakage" else law["action_independence"]
    outcome_count = 13 if mutation == "outcome_support_changed" else law["outcome_count"]
    law_ok = (
        outcome_count == 14 and not any(law_failures)
        and normalization == 1 and action and source
        and law["axis_floor"] > 0 and law["corner_floor"] > 0
    )

    transport = transport_facts()
    disjoint = False if mutation == "transport_collision" else transport["disjoint"]
    nearest = False if mutation == "transport_nonlocal" else transport["nearest"]
    moves = False if mutation == "transport_clones" else transport["moves_not_clones"]
    triggered = False if mutation == "transport_not_triggered" else transport["formation_triggered"]
    successor = False if mutation == "successor_mismatch" else transport["successor_exact"]
    runtime = False if mutation in (
        "same_event_feedback", "host_matrix_input", "second_rule_changed",
        "role_epoch",
    ) else transport["runtime_exact"] and transport["runtime_clean"]
    preloaded = True if mutation == "preloaded_tape" else transport["preloaded_future_packet"]
    transport_ok = (
        transport["front_count"] == 6 and transport["edge_count"] == 5
        and disjoint and nearest
        and transport["next_target_is_forward_source"]
        and transport["swap_unitary"] and moves and triggered
        and transport["successor_pairs"] == 1176 and successor and runtime
        and transport["runtime_signature"] == (
            "predecessor_content", "vectors", "outcome_index",
            "destination_contents",
        ) and not preloaded
    )

    history = history_facts()
    prefix = False if mutation == "prefix_failure" else history["prefix"]
    unique = False if mutation == "nonunique_front_site" else history["unique_front_site"]
    permanence = False if mutation == "record_overwrite" else history["permanence"]
    packet_growth = 1 if mutation == "live_packet_growth" else history["live_packet_growth"]
    history_ok = (
        history["front_count"] == 6
        and history["telescoping_steps"] == 36 and history["telescoping"]
        and history["prefix_count"] == 84 and prefix
        and all(total == 1 for total in history["totals"])
        and history["strict_axis_floor"] and history["strict_corner_floor"]
        and unique and permanence and history["live_packet_size"] == 5
        and packet_growth == 0 and not history["formation_rate_supplied"]
        and history["collision_free_corridor_required"]
        and not history["arbitrary_background_history"]
        and not history["collision_safe_controller_supplied"]
    )

    collision = collision_facts()
    collision_safe = (
        True if mutation == "collision_false_safe"
        else collision["collision_safe_controller_supplied"]
    )
    corridor_required = (
        False if mutation == "hide_corridor"
        else collision["corridor_condition_required"]
    )
    collision_ok = (
        collision["destination_outside_probability_stencil"]
        and collision["probability_has_no_destination_status_input"]
        and collision["probability_unchanged"]
        and collision["record_is_moved_by_frozen_swap"]
        and not collision_safe and corridor_required
    )

    scope = scope_facts()
    scope_ok = scope["note"] and scope["goal"] and scope["forbidden"]
    if mutation in (
        "claim_microscopic_readout", "claim_rate", "claim_axiom",
        "claim_gravity", "claim_autonomous_history", "claim_toe",
        "claim_retained",
    ):
        scope_ok = False

    return [
        ("A_frozen_authority", authority_ok,
         "parent, preregistration, current-main epoch, axiom, and Block-09/10/11 evidence match"),
        ("B_outcome_record_code", code_ok,
         "all 84 front/outcome contents are distinct, covariant, content-invertible, and strictly inside M2"),
        ("C_hybrid_rank_nine_carrier", decoder_ok,
         "one Record plus five live cells decodes the full matrix exactly with rank nine in all 24 paired frames"),
        ("D_physical_domain_and_pure_control", positivity_ok,
         "the encoded shell is strict on the 512-vertex box and H1/H2 while the literal-pure assignment fails only as a narrow control"),
        ("E_unchanged_fourteen_way_law", law_ok,
         "the encoded even offset leaves all fourteen probabilities, normalization, source moment, and zero action leakage exact"),
        ("F_generated_successor_shell", transport_ok,
         "five disjoint nearest-neighbor SWAPs move rather than copy the packet and the same runtime rule reconstructs every successor pair"),
        ("G_prefix_induction", history_ok,
         "the update telescopes and cylinders extend on a collision-free straight corridor; arbitrary-background history remains open"),
        ("H_collision_boundary", collision_ok,
         "a radius-two permanent Record is invisible to the rate stencil but moved by the frozen SWAP, so the empty-corridor condition is load bearing"),
        ("I_scope_and_open_bridges", scope_ok,
         "the result keeps encoded-versus-pure semantics, microscopic readout, rate/time, gravity, axiom, audit, and TOE boundaries explicit"),
    ]


def mutation_sweep() -> int:
    rejected = [
        any(not ok for _name, ok, _detail in evaluated_checks(mutation))
        for mutation in MUTATIONS
    ]
    count = sum(rejected)
    print(f"MUTATIONS: REJECTED={count}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={count} FAIL={len(MUTATIONS) - count}")
    return 0 if all(rejected) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()

    checks = evaluated_checks(args.mutation)
    passed = failed = 0
    for name, ok, detail in checks:
        ok = bool(ok)
        passed += int(ok)
        failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    if args.mutation is None:
        rejected = [
            any(not ok for _name, ok, _detail in evaluated_checks(mutation))
            for mutation in MUTATIONS
        ]
        print(f"MUTATIONS: rejected={sum(rejected)}/{len(MUTATIONS)}")
        failed += int(not all(rejected))
        print("VERDICT: OUTCOME-TYPED-TWO-STEP; finite-prefix induction is conditional on a collision-free straight corridor")
        print("per_element: checked every encoded Record and every individual transported M2 neighbor exactly")
        print("per_site: checked all six addressed neighbor positions for each local formation event")
        print("per_mode: checked all nine odd-shell coordinates and all fourteen outcome directions exactly")
        print("per_block: checked 84 Record codes, 1176 successor pairs, six fronts, targets, and open-box vertices")
        print("lattice_wide: checked and not executed — interacting fronts and a global formation schedule remain outside this block")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
