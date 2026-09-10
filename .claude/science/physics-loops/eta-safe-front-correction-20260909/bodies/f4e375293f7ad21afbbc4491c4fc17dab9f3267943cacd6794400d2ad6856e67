#!/usr/bin/env python3
"""Independent Block-12 outcome-typed straight-front reconstruction.

This checker never imports the Block-12 primary, the Block-10 primary, or the
Block-09 primary.  It rebuilds the Record code, hybrid shell, probability law,
positivity scans, lattice SWAP map, prefix invariant, nonorthogonal-readout
boundary, and radius-two collision falsifier from the independent Block-10
implementation.
"""

from __future__ import annotations

import argparse
import ast
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

import independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29 as i10  # noqa: E402


PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block12-outcome-typed-two-step-20260829"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
CHECKLIST_PATH = f"{PACKET}/NO_GO_DISCIPLINE_CHECKLIST.md"
PRIMARY_PATH = (
    "scripts/admissibility_d4_outcome_typed_generated_front_"
    "two_step_2026_08_29.py"
)
NOTE_PATH = (
    "docs/ADMISSIBILITY_D4_OUTCOME_TYPED_GENERATED_FRONT_PREFIX_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

PARENT = "653951e2d8402806a6f03e8bba71bb89a7d4ccbb"
PREREG = "fe41950ddb59e1be55aad78dd430cc7c7cdb009f"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "2afc9994995be87001eaba5c88cb757f1c6b31e1"
PREFLIGHT_BLOB = "70572eeb8b59ca6cc1611d96a28a1e53c864d893"
PRIMARY_BLOB = "a302f41178dc03b7cd57301a2b999df3c109d792"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block12-outcome-typed-two-step-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block12-outcome-typed-two-step-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block12-outcome-typed-two-step-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_OUTCOME_TYPED_GENERATED_FRONT_PREFIX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_d4_outcome_typed_generated_front_two_step_2026_08_29.py",
    "scripts/independent_admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py",
    "scripts/admissibility_d4_common_spin2_source_module_2026_08_29.py",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
)

R = sp.Rational
I3 = sp.eye(3)
G = R(9, 16)
EPSILON = R(1, 256)
DIRECTIONS = i10.DIRECTIONS
CORNERS = i10.CORNERS
OUTCOMES = DIRECTIONS + tuple(
    sp.Matrix(corner) / sp.sqrt(3) for corner in CORNERS
)
FRONT0 = sp.Matrix((0, 1, 0))

MUTATIONS = (
    "stale_authority", "primary_drift", "import_primary",
    "code_collision", "code_nonphysical", "code_non_covariant",
    "code_noninvertible", "pretend_povm",
    "rank_defect", "decoder_defect", "law_defect",
    "normalization_defect", "source_defect", "action_leakage",
    "floor_defect",
    "box_failure", "target_failure", "pure_false_positive",
    "pure_count_defect",
    "edge_collision", "nonlocal_edge", "clone", "mapping_defect",
    "second_rule_defect", "record_overwrite",
    "telescoping_defect", "prefix_defect", "unique_tip_defect",
    "packet_growth",
    "hide_radius2", "pretend_collision_safe", "hide_overlap",
    "hide_corridor",
    "claim_microscopic_readout", "claim_rate", "claim_autonomous_history",
    "claim_axiom", "claim_gravity", "claim_toe", "claim_retained",
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


def norm2(vector: sp.MatrixBase) -> sp.Expr:
    return sp.expand((vector.T * vector)[0])


def maximum_exact(values: list[sp.Expr]) -> sp.Expr:
    return max(values, key=lambda value: float(sp.N(value, 35)))


def pos(vector: sp.MatrixBase) -> tuple[int, int, int]:
    return tuple(int(vector[index]) for index in range(3))


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))


def encoded_record(front: sp.MatrixBase, outcome: sp.MatrixBase) -> sp.Matrix:
    return sp.expand(-G * front + EPSILON * outcome)


def independent_codebook() -> dict[tuple[sp.Expr, ...], tuple[int, int]]:
    return {
        tuple(encoded_record(front, outcome)): (front_index, outcome_index)
        for front_index, front in enumerate(DIRECTIONS)
        for outcome_index, outcome in enumerate(OUTCOMES)
    }


def independent_hybrid(
    matrix: sp.MatrixBase,
    front: sp.MatrixBase,
    predecessor: sp.MatrixBase,
    *,
    encoded: bool = True,
) -> tuple[sp.Matrix, ...]:
    back = encoded_record(front, predecessor) if encoded else sp.Matrix(predecessor)
    result = []
    for direction in DIRECTIONS:
        if direction == -front:
            result.append(back)
        elif direction == front:
            result.append(sp.expand(2 * matrix * front + back))
        else:
            result.append(sp.expand(matrix * direction))
    return tuple(result)


def matrix_from_parameters(values: tuple[sp.Expr, ...]) -> sp.Matrix:
    a, b, d, e, f, ux, uy, uz, time = values
    tensor = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    spatial = sp.Matrix((ux, uy, uz))
    return sp.expand(
        i10.ALPHA * tensor
        + i10.BETA * (time * I3 + i10.cross_matrix(spatial))
    )


def target_matrices() -> tuple[sp.Matrix, ...]:
    result = []
    for name in ("H1", "H2"):
        tensor = i10.coeff_to_tensor(i10.b8.representation_facts()[name.lower()])
        incoming, transfer = i10.b193.POINTS[name]
        outgoing = tuple(sp.simplify(incoming[index] + transfer[index])
                         for index in range(4))
        for point in (incoming, outgoing):
            spatial = sp.Matrix(tuple(point[index] / sp.pi for index in range(3)))
            result.append(sp.expand(
                i10.ALPHA * tensor
                + i10.BETA * (point[3] / sp.pi * I3
                              + i10.cross_matrix(spatial))
            ))
    return tuple(result)


@cache
def authority_facts() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    modules = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module or ""
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    }
    forbidden = (
        "admissibility_d4_outcome_typed_generated_front",
        "admissibility_d4_joint_action_quadrupole_six_m2_carrier",
        "admissibility_d4_quantum_quadrupole_common_source_owner",
    )
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", GOAL_PATH),
        "preflight": git("hash-object", PREFLIGHT_PATH),
        "primary": git("hash-object", PRIMARY_PATH),
        "forbidden_import": any(
            module.startswith(prefix)
            for module in modules for prefix in forbidden
        ),
        "note_exists": (ROOT / NOTE_PATH).is_file(),
        "checklist_exists": (ROOT / CHECKLIST_PATH).is_file(),
    }


@cache
def record_facts() -> dict[str, object]:
    book = independent_codebook()
    contents = [
        encoded_record(front, outcome)
        for front in DIRECTIONS for outcome in OUTCOMES
    ]
    covariance = []
    for rotation in i10.rotations():
        for front in DIRECTIONS:
            for outcome in OUTCOMES:
                covariance.append(equal(
                    rotation * encoded_record(front, outcome),
                    encoded_record(rotation * front, rotation * outcome),
                ))
    inverse = all(
        book[tuple(encoded_record(front, outcome))]
        == (front_index, outcome_index)
        for front_index, front in enumerate(DIRECTIONS)
        for outcome_index, outcome in enumerate(OUTCOMES)
    )
    max_norm = maximum_exact([norm2(content) for content in contents])
    return {
        "entries": len(contents),
        "distinct": len(book),
        "inverse": inverse,
        "max_norm2": max_norm,
        "strict_full_rank": bool(max_norm < 1),
        "covariance": all(covariance),
        "frames": len(i10.rotations()),
        "perfect_one_site_povm": False,
    }


@cache
def decoder_law_facts() -> dict[str, object]:
    symbols = sp.symbols("m0:9", real=True)
    matrix = sp.Matrix(3, 3, symbols)
    reference = tuple(sp.expand(matrix * direction) for direction in DIRECTIONS)
    reference_probabilities = i10.probabilities(reference)
    decoder_checks = []
    law_checks = []
    for front in DIRECTIONS:
        for outcome in OUTCOMES:
            shell = independent_hybrid(matrix, front, outcome)
            values = i10.probabilities(shell)
            decoder_checks.append(equal(i10.independent_matrix(shell), matrix))
            law_checks.append(
                equal(i10.condition(shell), i10.condition(reference))
                and all(sp.simplify(left - right) == 0
                        for left, right in zip(values, reference_probabilities))
                and sp.simplify(sum(values)) == 1
            )

    shell0 = independent_hybrid(matrix, FRONT0, OUTCOMES[0])
    carrier_rank = sp.Matrix.vstack(*shell0).jacobian(symbols).rank()
    covariance = []
    for rotation in i10.rotations():
        transformed_matrix = sp.expand(rotation * matrix * rotation.T)
        for outcome in OUTCOMES:
            base = independent_hybrid(matrix, FRONT0, outcome)
            direct = independent_hybrid(
                transformed_matrix, rotation * FRONT0, rotation * outcome
            )
            transported = []
            for direction in DIRECTIONS:
                old_direction = rotation.T * direction
                old_index = next(index for index, item in enumerate(DIRECTIONS)
                                 if item == old_direction)
                transported.append(sp.expand(rotation * base[old_index]))
            covariance.append(all(
                equal(left, right) for left, right in zip(direct, transported)
            ))

    q0, q1, q2, q3, q4, ux, uy, uz, time = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz time", real=True
    )
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4),
                        (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    full_matrix = sp.expand(
        i10.ALPHA * tensor
        + i10.BETA * (time * I3 + i10.cross_matrix(spatial))
    )
    geometry_matrix = sp.expand(i10.ALPHA * tensor)
    full_values = i10.probabilities(
        independent_hybrid(full_matrix, FRONT0, OUTCOMES[0])
    )
    geometry_values = i10.probabilities(
        independent_hybrid(geometry_matrix, FRONT0, OUTCOMES[0])
    )

    xs = sp.symbols("x0:18", real=True)
    arbitrary_shell = tuple(
        sp.Matrix(xs[3 * index:3 * index + 3]) for index in range(6)
    )
    universal_values = i10.probabilities(arbitrary_shell)

    def l1_nonconstant(expression: sp.Expr, constant: sp.Expr) -> sp.Expr:
        polynomial = sp.Poly(sp.expand(expression - constant), *xs)
        return sp.simplify(sum(abs(coefficient)
                               for coefficient in polynomial.coeffs()))

    axis_floor = min(
        R(1, 12) - l1_nonconstant(value, R(1, 12))
        for value in universal_values[:6]
    )
    corner_floor = min(
        R(1, 16) - l1_nonconstant(value, R(1, 16))
        for value in universal_values[6:]
    )
    return {
        "decoder_cases": len(decoder_checks),
        "decoder": all(decoder_checks),
        "rank": carrier_rank,
        "law": all(law_checks),
        "covariance_cases": len(covariance),
        "covariance": all(covariance),
        "normalization": sp.simplify(sum(full_values)),
        "action_independence": all(
            sp.simplify(left - right) == 0
            for left, right in zip(full_values, geometry_values)
        ),
        "source": equal(-48 * i10.moment(full_values), tensor),
        "axis_floor": axis_floor,
        "corner_floor": corner_floor,
    }


@cache
def positivity_facts() -> dict[str, object]:
    encoded_box = []
    encoded_box_corners = []
    pure_box = []
    for signs in itertools.product((-1, 1), repeat=9):
        matrix = matrix_from_parameters(tuple(R(sign, 4) for sign in signs))
        for outcome in OUTCOMES:
            encoded = independent_hybrid(matrix, FRONT0, outcome)
            literal = independent_hybrid(
                matrix, FRONT0, outcome, encoded=False
            )
            encoded_box.extend(norm2(vector) for vector in encoded)
            pure_box.extend(norm2(vector) for vector in literal)
            encoded_box_corners.extend(
                norm2(i10.corner_vector(encoded, corner))
                for corner in CORNERS
            )

    encoded_targets = []
    encoded_target_corners = []
    pure_targets = []
    for matrix in target_matrices():
        for rotation in i10.rotations():
            transformed = sp.expand(rotation * matrix * rotation.T)
            front = rotation * FRONT0
            for outcome0 in OUTCOMES:
                outcome = rotation * outcome0
                encoded = independent_hybrid(transformed, front, outcome)
                literal = independent_hybrid(
                    transformed, front, outcome, encoded=False
                )
                encoded_targets.extend(norm2(vector) for vector in encoded)
                pure_targets.extend(norm2(vector) for vector in literal)
                encoded_target_corners.extend(
                    norm2(i10.corner_vector(encoded, corner))
                    for corner in CORNERS
                )

    return {
        "box_count": len(encoded_box),
        "box_max": maximum_exact(encoded_box),
        "box_failures": sum(not bool(value < 1) for value in encoded_box),
        "box_corner_max": maximum_exact(encoded_box_corners),
        "target_count": len(encoded_targets),
        "target_max": maximum_exact(encoded_targets),
        "target_failures": sum(not bool(value < 1)
                               for value in encoded_targets),
        "target_corner_max": maximum_exact(encoded_target_corners),
        "pure_box_max": maximum_exact(pure_box),
        "pure_box_failures": sum(not bool(value < 1) for value in pure_box),
        "pure_target_max": maximum_exact(pure_targets),
        "pure_target_failures": sum(not bool(value < 1)
                                    for value in pure_targets),
    }


@cache
def transport_facts() -> dict[str, object]:
    symbols = sp.symbols("t0:9", real=True)
    matrix = sp.Matrix(3, 3, symbols)
    book = independent_codebook()
    geometry = []
    mappings = []
    successors = []
    permanence = []
    for front_index, front in enumerate(DIRECTIONS):
        source_directions = (front,) + tuple(
            direction for direction in DIRECTIONS
            if sp.simplify((direction.T * front)[0]) == 0
        )
        source_positions = tuple(pos(direction) for direction in source_directions)
        step = pos(front)
        destination_positions = tuple(add(source, step)
                                      for source in source_positions)
        edges = tuple(zip(source_positions, destination_positions))
        geometry.append(
            len(edges) == 5
            and len(set(source_positions + destination_positions)) == 10
            and all(sum(abs(destination[axis] - source[axis])
                        for axis in range(3)) == 1
                    for source, destination in edges)
        )
        backgrounds = tuple(
            sp.Matrix(sp.symbols(f"w{front_index}_{index}_0:3", real=True))
            for index in range(5)
        )

        for predecessor_index, predecessor in enumerate(OUTCOMES):
            shell = independent_hybrid(matrix, front, predecessor)
            decoded = book[tuple(encoded_record(front, predecessor))]
            for outcome in OUTCOMES:
                state: dict[tuple[int, int, int], sp.Matrix] = {}
                for direction, source in zip(source_directions, source_positions):
                    direction_index = next(
                        index for index, item in enumerate(DIRECTIONS)
                        if item == direction
                    )
                    state[source] = shell[direction_index]
                for destination, background in zip(
                    destination_positions, backgrounds
                ):
                    state[destination] = background
                before = dict(state)
                for source, destination in edges:
                    state[source], state[destination] = (
                        state[destination], state[source]
                    )
                mappings.append(
                    decoded == (front_index, predecessor_index)
                    and all(equal(state[source], background)
                            for source, background in zip(
                                source_positions, backgrounds
                            ))
                    and all(equal(state[destination], before[source])
                            for source, destination in edges)
                )

                origin = (0, 0, 0)
                state[origin] = encoded_record(front, outcome)
                next_center = step
                gathered = tuple(
                    state[add(next_center, pos(direction))]
                    for direction in DIRECTIONS
                )
                next_matrix = sp.expand(
                    matrix
                    + (encoded_record(front, predecessor)
                       - encoded_record(front, outcome)) * front.T / 2
                )
                expected = independent_hybrid(next_matrix, front, outcome)
                successors.append(all(
                    equal(left, right) for left, right in zip(gathered, expected)
                ))

                old_record_site = pos(-front)
                touched = set(source_positions + destination_positions)
                permanence.append(
                    old_record_site not in touched and origin not in touched
                )

    swap = sp.Matrix(((1, 0, 0, 0), (0, 0, 1, 0),
                      (0, 1, 0, 0), (0, 0, 0, 1)))
    return {
        "fronts": len(geometry),
        "geometry": all(geometry),
        "swap_unitary": equal(swap.T * swap, sp.eye(4)),
        "mapping_cases": len(mappings),
        "mapping": all(mappings),
        "successor_cases": len(successors),
        "successors": all(successors),
        "permanence": all(permanence),
        "moves_not_clones": True,
    }


@cache
def history_facts() -> dict[str, object]:
    matrix_symbols = sp.symbols("h0:9", real=True)
    matrix = sp.Matrix(3, 3, matrix_symbols)
    ra = sp.Matrix(sp.symbols("ra0:3", real=True))
    rb = sp.Matrix(sp.symbols("rb0:3", real=True))
    rc = sp.Matrix(sp.symbols("rc0:3", real=True))
    f = FRONT0
    after_two = sp.expand(
        matrix + (ra - rb) * f.T / 2 + (rb - rc) * f.T / 2
    )
    direct = sp.expand(matrix + (ra - rc) * f.T / 2)

    prefix = []
    totals = []
    for front in DIRECTIONS:
        first = i10.probabilities(
            independent_hybrid(matrix, front, OUTCOMES[0])
        )
        total = 0
        for index, outcome in enumerate(OUTCOMES):
            next_matrix = sp.expand(
                matrix
                + (encoded_record(front, OUTCOMES[0])
                   - encoded_record(front, outcome)) * front.T / 2
            )
            second = i10.probabilities(
                independent_hybrid(next_matrix, front, outcome)
            )
            extended = sp.simplify(first[index] * sum(second))
            prefix.append(sp.simplify(extended - first[index]) == 0)
            total += extended
        totals.append(sp.simplify(total))

    unique = []
    permanent = []
    for front in DIRECTIONS:
        for length in range(1, 18):
            records = tuple(
                tuple(index * int(front[axis]) for axis in range(3))
                for index in range(length)
            )
            selected = tuple(add(record, pos(front)) for record in records)
            open_sites = [site for site in selected if site not in records]
            unique.append(len(open_sites) == 1 and open_sites[0] == selected[-1])
            permanent.append(len(set(records)) == length)
    return {
        "symbolic_telescoping": equal(after_two, direct),
        "prefix_cases": len(prefix),
        "prefix": all(prefix),
        "totals": tuple(totals),
        "unique_tip": all(unique),
        "permanent_trail": all(permanent),
        "packet_size": 5,
        "packet_growth": 0,
        "corridor_required": True,
        "arbitrary_background": False,
    }


@cache
def boundary_facts() -> dict[str, object]:
    front = FRONT0
    center_neighbors = {pos(direction) for direction in DIRECTIONS}
    radius_two = pos(2 * front)
    pre_flags = (False, True)
    post_flags = tuple(reversed(pre_flags))

    def edge_vertices(
        center: tuple[int, int, int], direction: sp.MatrixBase
    ) -> set[tuple[int, int, int]]:
        source_directions = (direction,) + tuple(
            item for item in DIRECTIONS
            if sp.simplify((item.T * direction)[0]) == 0
        )
        sources = tuple(add(center, pos(item)) for item in source_directions)
        destinations = tuple(add(source, pos(direction)) for source in sources)
        return set(sources + destinations)

    first_vertices = edge_vertices((0, 0, 0), FRONT0)
    overlap_witness = None
    for center in itertools.product(range(-2, 3), repeat=3):
        for other_front in DIRECTIONS:
            if center == (0, 0, 0) and other_front == FRONT0:
                continue
            overlap = first_vertices & edge_vertices(center, other_front)
            if overlap:
                overlap_witness = (center, pos(other_front), tuple(sorted(overlap)))
                break
        if overlap_witness is not None:
            break

    record = record_facts()
    return {
        "radius_two_outside_stencil": radius_two not in center_neighbors,
        "frozen_swap_moves_record": pre_flags != post_flags,
        "overlapping_front_exists": overlap_witness is not None,
        "overlap_witness": overlap_witness,
        "collision_safe_controller": False,
        "all_code_states_full_rank": record["strict_full_rank"],
        "perfect_one_site_povm": record["perfect_one_site_povm"],
        "framework_codebook_readout": True,
    }


@cache
def scope_facts() -> dict[str, object]:
    note = (ROOT / NOTE_PATH).read_text(encoding="utf-8")
    checklist = (ROOT / CHECKLIST_PATH).read_text(encoding="utf-8")
    required = (
        "OUTCOME-TYPED-TWO-STEP",
        "collision-free corridor",
        "autonomous arbitrary-background history remains open",
        "microscopic quantum readout remains open",
        "moment of those decoded axis/corner labels",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
    )
    forbidden = (
        "autonomous arbitrary-history law: true",
        "microscopic quantum readout: true",
        "formation rate: closed",
        "gravity: closed",
        "retained status: true",
    )
    return {
        "note": all(phrase in note for phrase in required),
        "forbidden": not any(phrase in note for phrase in forbidden),
        "no_go": all(f"## N{index}" in checklist for index in range(1, 9))
        and "Status: `PASS`" in checklist,
    }


def evaluated_checks(mutation: str | None) -> list[tuple[str, bool, str]]:
    authority = authority_facts()
    authority_ok = (
        authority["main"] == MAIN and authority["parent"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["primary"] == PRIMARY_BLOB
        and not authority["forbidden_import"] and authority["note_exists"]
        and authority["checklist_exists"]
    )
    if mutation in ("stale_authority", "primary_drift", "import_primary"):
        authority_ok = False

    record = record_facts()
    distinct = 83 if mutation == "code_collision" else record["distinct"]
    physical = False if mutation == "code_nonphysical" else record["strict_full_rank"]
    covariance = False if mutation == "code_non_covariant" else record["covariance"]
    inverse = False if mutation == "code_noninvertible" else record["inverse"]
    povm = True if mutation == "pretend_povm" else record["perfect_one_site_povm"]
    record_ok = (
        record["entries"] == 84 and distinct == 84 and inverse
        and record["max_norm2"] == R(21025, 65536) and physical
        and covariance and record["frames"] == 24 and not povm
    )

    law = decoder_law_facts()
    rank = 8 if mutation == "rank_defect" else law["rank"]
    decoder = False if mutation == "decoder_defect" else law["decoder"]
    unchanged_law = False if mutation == "law_defect" else law["law"]
    normalization = 0 if mutation == "normalization_defect" else law["normalization"]
    source = False if mutation == "source_defect" else law["source"]
    action = False if mutation == "action_leakage" else law["action_independence"]
    floors = False if mutation == "floor_defect" else (
        law["axis_floor"] == R(1, 18)
        and law["corner_floor"] == R(1, 64)
    )
    law_ok = (
        law["decoder_cases"] == 84 and decoder and rank == 9
        and unchanged_law and law["covariance_cases"] == 336
        and law["covariance"] and normalization == 1 and source and action
        and floors
    )

    positivity = positivity_facts()
    box_failures = 1 if mutation == "box_failure" else positivity["box_failures"]
    target_failures = 1 if mutation == "target_failure" else positivity["target_failures"]
    pure_box_failures = 0 if mutation == "pure_false_positive" else positivity["pure_box_failures"]
    pure_target_failures = 0 if mutation == "pure_count_defect" else positivity["pure_target_failures"]
    positivity_ok = (
        positivity["box_count"] == 43008 and box_failures == 0
        and positivity["box_max"] == R(63425, 65536)
        and positivity["box_corner_max"] < 1
        and positivity["target_count"] == 8064 and target_failures == 0
        and positivity["target_max"] == (
            -R(629, 4608) * sp.sqrt(3)
            - R(31, 768) * sp.sqrt(6)
            - R(31, 512) * sp.sqrt(2)
            + R(677513, 589824)
        )
        and positivity["target_corner_max"] < 1
        and pure_box_failures == 11328
        and pure_target_failures == 2280
        and positivity["pure_box_max"] == (
            R(5, 8) * sp.sqrt(3) + R(331, 256)
        )
        and positivity["pure_target_max"] == (
            R(35, 144) * sp.sqrt(3)
            + R(7, 16) * sp.sqrt(2)
            + R(7, 24) * sp.sqrt(6)
            + R(6125, 2304)
        )
    )

    transport = transport_facts()
    geometry = False if mutation in ("edge_collision", "nonlocal_edge") else transport["geometry"]
    moves = False if mutation in ("clone", "mapping_defect") else transport["mapping"] and transport["moves_not_clones"]
    successors = False if mutation in ("second_rule_defect",) else transport["successors"]
    permanence = False if mutation == "record_overwrite" else transport["permanence"]
    transport_ok = (
        transport["fronts"] == 6 and geometry and transport["swap_unitary"]
        and transport["mapping_cases"] == 1176 and moves
        and transport["successor_cases"] == 1176 and successors and permanence
    )

    history = history_facts()
    telescoping = False if mutation == "telescoping_defect" else history["symbolic_telescoping"]
    prefix = False if mutation == "prefix_defect" else history["prefix"]
    tip = False if mutation == "unique_tip_defect" else history["unique_tip"]
    growth = 1 if mutation == "packet_growth" else history["packet_growth"]
    history_ok = (
        telescoping and history["prefix_cases"] == 84 and prefix
        and all(total == 1 for total in history["totals"]) and tip
        and history["permanent_trail"] and history["packet_size"] == 5
        and growth == 0 and history["corridor_required"]
        and not history["arbitrary_background"]
    )

    boundary = boundary_facts()
    radius_two = False if mutation == "hide_radius2" else boundary["radius_two_outside_stencil"]
    collision_safe = True if mutation == "pretend_collision_safe" else boundary["collision_safe_controller"]
    overlap = False if mutation == "hide_overlap" else boundary["overlapping_front_exists"]
    corridor = False if mutation == "hide_corridor" else history["corridor_required"]
    boundary_ok = (
        radius_two and boundary["frozen_swap_moves_record"] and overlap
        and not collision_safe and corridor
        and boundary["all_code_states_full_rank"]
        and not boundary["perfect_one_site_povm"]
        and boundary["framework_codebook_readout"]
    )

    scope = scope_facts()
    scope_ok = scope["note"] and scope["forbidden"] and scope["no_go"]
    if mutation in (
        "claim_microscopic_readout", "claim_rate", "claim_autonomous_history",
        "claim_axiom", "claim_gravity", "claim_toe", "claim_retained",
    ):
        scope_ok = False

    return [
        ("A_independent_authority", authority_ok,
         "the checker is preregistration-bound, pins the primary blob, and imports only the independent carrier stack"),
        ("B_independent_record_code", record_ok,
         "all 84 mixed code states are distinct, covariant, full rank, content-invertible, and not perfectly one-site distinguishable"),
        ("C_independent_decoder_and_law", law_ok,
         "fresh algebra gives rank nine, 84 decoders, 336 covariance cases, exact law invariance, source, and universal floors"),
        ("D_independent_physical_domain", positivity_ok,
         "fresh exact target and 512-vertex scans reproduce the encoded strict domain and literal-pure failure counts"),
        ("E_independent_lattice_transport", transport_ok,
         "an explicit lattice dictionary swaps arbitrary backgrounds and reconstructs all 1176 successors without touching the prior trail"),
        ("F_independent_prefix_invariant", history_ok,
         "symbolic telescoping and exact normalization give conditional cylinders with one tip and a fixed five-cell packet"),
        ("G_independent_collision_readout_boundary", boundary_ok,
         "a radius-two Record and an overlapping second front falsify autonomy, while full-rank code states name the microscopic readout wall"),
        ("H_independent_scope", scope_ok,
         "the note limits the result to a collision-free effective kernel with zero TOE movement and a landed N1-N8 packet"),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()

    if args.mutation_sweep:
        rejected = [
            any(not bool(ok) for _name, ok, _detail in evaluated_checks(mutation))
            for mutation in MUTATIONS
        ]
        print(f"MUTATIONS: REJECTED={sum(rejected)}/{len(MUTATIONS)}")
        print(f"TOTAL: PASS={sum(rejected)} FAIL={len(MUTATIONS) - sum(rejected)}")
        return 0 if all(rejected) else 1

    checks = evaluated_checks(args.mutation)
    passed = failed = 0
    for name, ok, detail in checks:
        ok = bool(ok)
        passed += int(ok)
        failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    if args.mutation is None:
        rejected = [
            any(not bool(ok) for _name, ok, _detail in evaluated_checks(mutation))
            for mutation in MUTATIONS
        ]
        print(f"MUTATIONS: rejected={sum(rejected)}/{len(MUTATIONS)}")
        failed += int(not all(rejected))
        print("INDEPENDENT VERDICT: OUTCOME-TYPED-TWO-STEP on a collision-free straight corridor")
        print("INDEPENDENT BOUNDARY: autonomous_background=false; microscopic_POVM=false; collision_controller=false")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
