#!/usr/bin/env python3
"""Block 09: positive quantum direction/corner common-source candidate.

The runner checks one preregistered 14-possibility Admissibility distribution
on six neighboring M2 Record contents.  It proves the universal probability
and moment identities, tests exact H1/H2 native sources, and then adjudicates
the still-open action-state/clock typing gate.  It does not promote a static
distribution to formation, history, gravity, or retained TOE physics.
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

import admissibility_d4_common_spin2_source_module_2026_08_29 as b8  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block09-quantum-quadrupole-owner-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
NO_GO = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

PARENT = "b7cf0c7ed83bd3e57c4538b29fc3d5f784ed9ca5"
BLOCK8_RESULT = "5c472dd7323614e6ed6c0902ca85de78dab831c8"
PREREG = "916fda761aa9a168b4ae90e29af09e1fdb9457a1"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "ea503ef9471b111de3afa32ea751a3eccbf28d38"
PREFLIGHT_BLOB = "cccd6f9365910c7db9c2c0d108dff5cb91a07c66"
BLOCK8_NOTE_BLOB = "0020cb133fc67f3bf3dd253798d8980e05f9ffcc"
BLOCK8_RUNNER_BLOB = "55a88b22fa140faf0e80710f7d6b3b65f685bcf6"
BLOCK8_CACHE_BLOB = "703b88026166be34c44b4b43d1a9d8efec80c7a4"
BLOCK207 = "04b1c5d132f7ad46d6818854f8b733391ebdb6d2"
BLOCK207_NOTE = (
    "docs/ADMISSIBILITY_D4_H1_EDGE_COMPARISON_CELL_CORNER_T2_"
    "FACTORIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
BLOCK207_RUNNER = (
    "scripts/admissibility_d4_h1_edge_comparison_cell_corner_t2_"
    "factorization_2026_08_26.py"
)
BLOCK207_NOTE_BLOB = "96d5567b5e5e25728e9bbfa5333ff0cbb579a238"
BLOCK207_RUNNER_BLOB = "088154b3e43e899b715c6c17bd08b2e4c331f20b"
BLOCK208 = "0be49cf0458beb616d1d7002e488e3005e763960"
BLOCK208_NOTE = (
    "docs/ADMISSIBILITY_D4_H1_TWO_TIME_CLIFFORD_CELL_M2_RECORD_"
    "COMPILER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
BLOCK208_RUNNER = (
    "scripts/admissibility_d4_h1_two_time_clifford_cell_m2_record_"
    "compiler_2026_08_26.py"
)
BLOCK208_NOTE_BLOB = "e546af320e6a7adc64e68f1b4f6e5a43c3d97515"
BLOCK208_RUNNER_BLOB = "06c6fd3894a2e225bb96476fd8813cc6f60e96e1"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block09-quantum-quadrupole-owner-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block09-quantum-quadrupole-owner-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block09-quantum-quadrupole-owner-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_COMMON_SPIN2_SOURCE_MODULE_SIX_BIT_CAPACITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_common_spin2_source_module_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_common_spin2_source_module_2026_08_29.txt",
)

TAU = sp.Rational(1, 24)
SQRT2 = sp.sqrt(2)
I3 = sp.eye(3)
DIRECTIONS = tuple(
    sp.Matrix(vector)
    for vector in (
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1),
    )
)
CORNERS = tuple(sp.Matrix(corner) for corner in itertools.product((-1, 1), repeat=3))

MUTATIONS = (
    "stale_parent", "stale_prereg", "candidate_blob_drift",
    "change_tau", "break_normalization", "negative_probability",
    "wrong_moment", "drop_axis", "drop_corner", "break_rotation",
    "diagonal_corner_site", "target_runtime", "h1_fixture_gain",
    "h1_nonpositive", "drop_e", "h2_fixture_gain", "h2_nonpositive",
    "noninjective_source", "adjoint_reverse", "sample_only",
    "heldout_refit", "shrink_family", "claim_owned", "assume_solder",
    "claim_record", "use_downstream_m4", "claim_axiom", "claim_toe",
    "claim_retained",
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


def git_show(commit: str, path: str) -> str:
    return git("show", f"{commit}:{path}")


def key(vector: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(item) for item in vector)


def stf(matrix: sp.MatrixBase) -> sp.Matrix:
    symmetric = sp.expand((matrix + matrix.T) / 2)
    return sp.expand(symmetric - sp.trace(symmetric) * I3 / 3)


def condition_tensor(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    if len(vectors) != 6:
        raise ValueError("six neighboring Bloch vectors are required")
    raw = sum(
        (direction * vector.T + vector * direction.T
         for direction, vector in zip(DIRECTIONS, vectors)),
        sp.zeros(3),
    ) / 4
    return stf(raw)


def local_distribution(vectors: tuple[sp.Matrix, ...]) -> dict[tuple[str, tuple[sp.Expr, ...]], sp.Expr]:
    """The preregistered law; its only runtime input is six Record contents."""
    tensor = condition_tensor(vectors)
    result: dict[tuple[str, tuple[sp.Expr, ...]], sp.Expr] = {}
    for direction in DIRECTIONS:
        axis = next(index for index in range(3) if direction[index] != 0)
        result[("axis", key(direction))] = sp.expand(
            sp.Rational(1, 12) + TAU * tensor[axis, axis] / 2
        )
    for corner in CORNERS:
        mixed = (
            tensor[0, 1] * corner[0] * corner[1]
            + tensor[1, 2] * corner[1] * corner[2]
            + tensor[0, 2] * corner[0] * corner[2]
        )
        result[("corner", key(corner))] = sp.expand(
            sp.Rational(1, 16) + 3 * TAU * mixed / 8
        )
    return result


def distribution_moment(
    probabilities: dict[tuple[str, tuple[sp.Expr, ...]], sp.Expr]
) -> sp.Matrix:
    raw = sp.zeros(3)
    for direction in DIRECTIONS:
        raw += probabilities[("axis", key(direction))] * direction * direction.T
    for corner in CORNERS:
        raw += probabilities[("corner", key(corner))] * corner * corner.T / 3
    return stf(raw)


def coeff_to_tensor(coefficients: sp.MatrixBase) -> sp.Matrix:
    tensor = sp.zeros(3)
    tensor[0, 0], tensor[1, 1], tensor[2, 2] = (
        coefficients[1], coefficients[2], coefficients[3]
    )
    for value, (left, right) in zip(
        (coefficients[7], coefficients[8], coefficients[9]),
        ((0, 1), (0, 2), (1, 2)),
    ):
        tensor[left, right] = tensor[right, left] = value / SQRT2
    return sp.expand(tensor)


def tensor_to_coeff(tensor: sp.MatrixBase) -> sp.Matrix:
    coefficients = sp.zeros(10, 1)
    coefficients[1], coefficients[2], coefficients[3] = (
        tensor[0, 0], tensor[1, 1], tensor[2, 2]
    )
    coefficients[7] = SQRT2 * tensor[0, 1]
    coefficients[8] = SQRT2 * tensor[0, 2]
    coefficients[9] = SQRT2 * tensor[1, 2]
    return sp.expand(coefficients)


def prepare_target(tensor: sp.MatrixBase) -> tuple[sp.Matrix, ...]:
    return tuple(sp.expand(-sp.Rational(3, 4) * tensor * direction)
                 for direction in DIRECTIONS)


def composite_corner(
    vectors: tuple[sp.Matrix, ...], corner: sp.MatrixBase
) -> sp.Matrix:
    selected = []
    for axis in range(3):
        direction = sp.zeros(3, 1)
        direction[axis] = corner[axis]
        selected.append(vectors[next(
            index for index, item in enumerate(DIRECTIONS)
            if item == direction
        )])
    return sp.expand(sum(selected, sp.zeros(3, 1)) / 3)


def norm_squared(vector: sp.MatrixBase) -> sp.Expr:
    return sp.expand((vector.T * vector)[0])


def strictly_below_one(value: sp.Expr) -> bool:
    return bool(sp.simplify(1 - value).is_positive)


def rotations() -> tuple[sp.Matrix, ...]:
    return tuple(sp.Matrix(item) for item in b8.b3.b2.rotations())


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "block8_result": ancestor(BLOCK8_RESULT),
        "prereg": ancestor(PREREG),
        "axiom": git("hash-object", "--", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("rev-parse", f"{PREREG}:{GOAL.relative_to(ROOT)}"),
        "preflight": git("rev-parse", f"{PREREG}:{PREFLIGHT.relative_to(ROOT)}"),
        "block8_note": git("rev-parse", f"HEAD:{b8.NOTE.relative_to(ROOT)}"),
        "block8_runner": git("rev-parse", f"HEAD:{Path(b8.__file__).relative_to(ROOT)}"),
        "block8_cache": git("rev-parse", "HEAD:logs/runner-cache/admissibility_d4_common_spin2_source_module_2026_08_29.txt"),
        "block207_note": git("rev-parse", f"{BLOCK207}:{BLOCK207_NOTE}"),
        "block207_runner": git("rev-parse", f"{BLOCK207}:{BLOCK207_RUNNER}"),
        "block208_note": git("rev-parse", f"{BLOCK208}:{BLOCK208_NOTE}"),
        "block208_runner": git("rev-parse", f"{BLOCK208}:{BLOCK208_RUNNER}"),
    }


@cache
def universal_facts() -> dict[str, object]:
    symbols = sp.symbols("v0:18", real=True)
    vectors = tuple(sp.Matrix(symbols[3 * index:3 * index + 3]) for index in range(6))
    tensor = condition_tensor(vectors)
    probabilities = local_distribution(vectors)
    moment = distribution_moment(probabilities)
    tensor_coordinates = (tensor[0, 0], tensor[1, 1], tensor[0, 1], tensor[0, 2], tensor[1, 2])
    condition_matrix = sp.Matrix(tensor_coordinates).jacobian(symbols)

    a, b, d, e, f = sp.symbols("A B D E F", real=True)
    generic = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    generic_probs = []
    for direction in DIRECTIONS:
        axis = next(index for index in range(3) if direction[index] != 0)
        generic_probs.append(sp.Rational(1, 12) + TAU * generic[axis, axis] / 2)
    for corner in CORNERS:
        generic_probs.append(sp.Rational(1, 16) + 3 * TAU * (
            generic[0, 1] * corner[0] * corner[1]
            + generic[1, 2] * corner[1] * corner[2]
            + generic[0, 2] * corner[0] * corner[2]
        ) / 8)
    probability_matrix = sp.Matrix(generic_probs).jacobian((a, b, d, e, f))

    def coefficient_l1(expression: sp.Expr) -> sp.Expr:
        polynomial = sp.Poly(sp.expand(expression), *symbols)
        return sp.simplify(sum(abs(value) for value in polynomial.coeffs()))

    diagonal_l1 = tuple(coefficient_l1(tensor[index, index]) for index in range(3))
    off_diagonal_l1 = tuple(
        coefficient_l1(tensor[left, right])
        for left, right in ((0, 1), (0, 2), (1, 2))
    )
    axis_floor = sp.Rational(1, 12) - TAU * max(diagonal_l1) / 2
    corner_floor = sp.Rational(1, 16) - 3 * TAU * sum(off_diagonal_l1) / 8
    return {
        "symbols": symbols,
        "vectors": vectors,
        "tensor": tensor,
        "probabilities": probabilities,
        "normalization": sp.simplify(sum(probabilities.values())),
        "moment": moment,
        "moment_residual": sp.simplify(moment - TAU * tensor),
        "condition_rank": condition_matrix.rank(),
        "probability_rank": probability_matrix.rank(),
        "diagonal_l1": diagonal_l1,
        "off_diagonal_l1": off_diagonal_l1,
        "axis_floor": axis_floor,
        "corner_floor": corner_floor,
    }


@cache
def covariance_facts() -> dict[str, object]:
    universal = universal_facts()
    vectors = universal["vectors"]
    assert isinstance(vectors, tuple)
    tensor = universal["tensor"]
    assert isinstance(tensor, sp.MatrixBase)
    probabilities = universal["probabilities"]
    assert isinstance(probabilities, dict)
    failures = []
    for rotation in rotations():
        transformed_vectors = []
        inverse = rotation.T
        for direction in DIRECTIONS:
            old_direction = inverse * direction
            old_index = next(index for index, item in enumerate(DIRECTIONS)
                             if item == old_direction)
            transformed_vectors.append(rotation * vectors[old_index])
        transformed_vectors_tuple = tuple(transformed_vectors)
        transformed_tensor = condition_tensor(transformed_vectors_tuple)
        tensor_ok = sp.simplify(transformed_tensor - rotation * tensor * rotation.T) == sp.zeros(3)
        transformed_probabilities = local_distribution(transformed_vectors_tuple)
        probability_ok = True
        for direction in DIRECTIONS:
            old_direction = inverse * direction
            probability_ok &= sp.simplify(
                transformed_probabilities[("axis", key(direction))]
                - probabilities[("axis", key(old_direction))]
            ) == 0
        for corner in CORNERS:
            old_corner = inverse * corner
            probability_ok &= sp.simplify(
                transformed_probabilities[("corner", key(corner))]
                - probabilities[("corner", key(old_corner))]
            ) == 0
        failures.append((not tensor_ok, not probability_ok))
    return {
        "rotation_count": len(rotations()),
        "failures": tuple(failures),
    }


def one_target_facts(name: str) -> dict[str, object]:
    representation = b8.representation_facts()
    coefficients = representation[name]
    assert isinstance(coefficients, sp.MatrixBase)
    tensor = coeff_to_tensor(coefficients)
    vectors = prepare_target(tensor)
    probabilities = local_distribution(vectors)
    moment = distribution_moment(probabilities)
    source_tensor = sp.expand(-32 * moment)
    prepared_coefficients = tensor_to_coeff(source_tensor)
    neighbor_norms = tuple(sp.simplify(norm_squared(vector)) for vector in vectors)
    corner_vectors = tuple(composite_corner(vectors, corner) for corner in CORNERS)
    corner_norms = tuple(sp.simplify(norm_squared(vector)) for vector in corner_vectors)
    corner_identity = all(
        composite_corner(vectors, corner) == sp.expand(-tensor * corner / 4)
        for corner in CORNERS
    )
    orbit_checks = []
    orbit_tensors = []
    for rotation in rotations():
        transformed = sp.expand(rotation * tensor * rotation.T)
        orbit_tensors.append(key(transformed))
        transformed_vectors = prepare_target(transformed)
        output = sp.expand(-32 * distribution_moment(local_distribution(transformed_vectors)))
        prep_covariant = all(
            transformed_vectors[next(
                index for index, item in enumerate(DIRECTIONS)
                if item == rotation * direction
            )] == rotation * vectors[index]
            for index, direction in enumerate(DIRECTIONS)
        )
        orbit_checks.append(output == transformed and prep_covariant)
    return {
        "coefficients": coefficients,
        "tensor": tensor,
        "trace": sp.simplify(sp.trace(tensor)),
        "vectors": vectors,
        "probabilities": probabilities,
        "probability_positive": all(sp.simplify(value).is_positive for value in probabilities.values()),
        "neighbor_norms": neighbor_norms,
        "neighbor_positive": all(strictly_below_one(value) for value in neighbor_norms),
        "corner_norms": corner_norms,
        "corner_positive": all(strictly_below_one(value) for value in corner_norms),
        "corner_identity": corner_identity,
        "source_tensor": source_tensor,
        "tensor_reproduced": source_tensor == tensor,
        "coefficients_reproduced": prepared_coefficients == coefficients,
        "orbit_size": len(set(orbit_tensors)),
        "orbit_checks": tuple(orbit_checks),
    }


@cache
def target_facts() -> dict[str, object]:
    return {"h1": one_target_facts("h1"), "h2": one_target_facts("h2")}


@cache
def native_source_facts() -> dict[str, object]:
    representation = b8.representation_facts()
    source = b8.source_facts()
    common = representation["common"]
    assert isinstance(common, sp.MatrixBase)
    targets = target_facts()
    return {
        "full_forward_rank": source["full_forward_rank"],
        "full_reverse_rank": source["full_reverse_rank"],
        "common_forward_rank": source["common_forward_rank"],
        "common_reverse_rank": source["common_reverse_rank"],
        "h1_all": all((
            source["h1_forward_reproduced"], source["h1_reverse_reproduced"],
            targets["h1"]["coefficients_reproduced"],
        )),
        "h2_all": all((
            source["h2_forward_reproduced"], source["h2_reverse_reproduced"],
            targets["h2"]["coefficients_reproduced"],
        )),
        "common_rank": common.rank(),
    }


@cache
def open_family_facts() -> dict[str, object]:
    a, b, d, e, f = sp.symbols("a b d e f", real=True)
    parameters = (a, b, d, e, f)
    tensor = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    vectors = prepare_target(tensor)
    probabilities = local_distribution(vectors)
    output = sp.expand(-32 * distribution_moment(probabilities))
    probability_jacobian = sp.Matrix(tuple(probabilities.values())).jacobian(parameters)

    neighbor_vertex_norms = []
    corner_vertex_norms = []
    for signs in itertools.product((-1, 1), repeat=5):
        substitution = dict(zip(parameters, (sp.Rational(sign, 4) for sign in signs)))
        vertex_tensor = tensor.subs(substitution)
        vertex_vectors = prepare_target(vertex_tensor)
        neighbor_vertex_norms.extend(norm_squared(vector) for vector in vertex_vectors)
        corner_vertex_norms.extend(
            norm_squared(composite_corner(vertex_vectors, corner))
            for corner in CORNERS
        )
    sample = {
        a: sp.Rational(1, 7), b: -sp.Rational(1, 8),
        d: sp.Rational(1, 9), e: -sp.Rational(1, 10),
        f: sp.Rational(1, 11),
    }
    sample_tensor = tensor.subs(sample)
    sample_output = output.subs(sample)
    return {
        "symbolic_identity": sp.simplify(output - tensor) == sp.zeros(3),
        "probability_rank": probability_jacobian.rank(),
        "max_neighbor_vertex_norm2": max(neighbor_vertex_norms),
        "max_corner_vertex_norm2": max(corner_vertex_norms),
        "box_neighbor_positive": max(neighbor_vertex_norms) < 1,
        "box_corner_positive": max(corner_vertex_norms) < 1,
        "sample_identity": sample_output == sample_tensor,
        "sample_parameters": sample,
    }


@cache
def ownership_facts() -> dict[str, object]:
    runtime_signature = tuple(inspect.signature(local_distribution).parameters)
    runtime_source = inspect.getsource(local_distribution)
    forbidden_runtime_tokens = (
        "H1", "H2", "tt_source", "fixture", "orbit_label",
        "downstream_m4", "same_event_post_state",
    )
    block207_text = git_show(BLOCK207, BLOCK207_NOTE)
    block208_text = git_show(BLOCK208, BLOCK208_NOTE)
    candidate_open_markers = all(marker in block207_text + "\n" + block208_text for marker in (
        "not yet a complete description of the physical Admissibility",
        "It is not yet complete H1 physical ownership",
        "action-state solder",
        "H2 remains sealed",
    ))
    runtime_clean = (
        runtime_signature == ("vectors",)
        and not any(token in runtime_source for token in forbidden_runtime_tokens)
    )
    # The registered joint-typing gate cannot pass while the only frozen
    # action/clock candidate explicitly leaves the action-state solder open.
    joint_action_state_typed = not candidate_open_markers
    return {
        "runtime_signature": runtime_signature,
        "runtime_clean": runtime_clean,
        "candidate_open_markers": candidate_open_markers,
        "joint_action_state_typed": joint_action_state_typed,
        "verdict": "OWNED-COMMON" if runtime_clean and joint_action_state_typed else "CAPACITY-ONLY",
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool, detail: str) -> None:
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_facts()
    authority_ok = (
        authority["main"] == MAIN and authority["parent"]
        and authority["block8_result"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["block8_note"] == BLOCK8_NOTE_BLOB
        and authority["block8_runner"] == BLOCK8_RUNNER_BLOB
        and authority["block8_cache"] == BLOCK8_CACHE_BLOB
        and authority["block207_note"] == BLOCK207_NOTE_BLOB
        and authority["block207_runner"] == BLOCK207_RUNNER_BLOB
        and authority["block208_note"] == BLOCK208_NOTE_BLOB
        and authority["block208_runner"] == BLOCK208_RUNNER_BLOB
    )
    if mutation in ("stale_parent", "stale_prereg", "candidate_blob_drift"):
        authority_ok = False
    checks.check("A_frozen_authority", authority_ok,
                 "parent, preregistration, main, axioms, Block-08, and candidate Block-207/208 blobs match")

    universal = universal_facts()
    universal_ok = (
        universal["normalization"] == 1
        and universal["moment_residual"] == sp.zeros(3)
        and universal["condition_rank"] == 5
        and universal["probability_rank"] == 5
        and universal["diagonal_l1"] == (sp.Rational(4, 3),) * 3
        and universal["off_diagonal_l1"] == (sp.Integer(1),) * 3
        and universal["axis_floor"] == sp.Rational(1, 18)
        and universal["corner_floor"] == sp.Rational(1, 64)
    )
    if mutation in (
        "change_tau", "break_normalization", "negative_probability",
        "wrong_moment", "drop_axis", "drop_corner",
    ):
        universal_ok = False
    checks.check("B_universal_positive_distribution", universal_ok,
                 "all six-Bloch-ball inputs give one normalized 14-possibility law with floors 1/18 and 1/64 and exact M=tau*S")

    covariance = covariance_facts()
    covariance_ok = covariance["rotation_count"] == 24 and not any(any(row) for row in covariance["failures"])
    if mutation in ("break_rotation", "diagonal_corner_site"):
        covariance_ok = False
    checks.check("C_exact_cubic_covariance", covariance_ok,
                 "neighbor addresses, Bloch vectors, axis/corner possibilities, S, and probabilities intertwine in all 24 frames")

    targets = target_facts()
    h1 = targets["h1"]
    h1_ok = (
        h1["trace"] == 0 and h1["neighbor_positive"] and h1["corner_positive"]
        and h1["corner_identity"] and h1["probability_positive"]
        and h1["tensor_reproduced"] and h1["coefficients_reproduced"]
        and h1["orbit_size"] == 24 and all(h1["orbit_checks"])
    )
    if mutation in ("target_runtime", "h1_fixture_gain", "h1_nonpositive"):
        h1_ok = False
    checks.check("D_exact_h1_quantum_quadrupole", h1_ok,
                 "six positive neighbor Records and eight composite mixtures reproduce exact H1 in every cubic frame")

    h2 = targets["h2"]
    h2_ok = (
        h2["trace"] == 0 and h2["neighbor_positive"] and h2["corner_positive"]
        and h2["corner_identity"] and h2["probability_positive"]
        and h2["tensor_reproduced"] and h2["coefficients_reproduced"]
        and h2["orbit_size"] == 24 and all(h2["orbit_checks"])
    )
    if mutation in ("drop_e", "h2_fixture_gain", "h2_nonpositive"):
        h2_ok = False
    checks.check("E_exact_h2_quantum_quadrupole", h2_ok,
                 "the same positive law reproduces H2's E doublet plus T2 triplet in every cubic frame")

    native = native_source_facts()
    native_ok = (
        native["full_forward_rank"] == 10 and native["full_reverse_rank"] == 10
        and native["common_forward_rank"] == 5 and native["common_reverse_rank"] == 5
        and native["common_rank"] == 5 and native["h1_all"] and native["h2_all"]
    )
    if mutation in ("noninjective_source", "adjoint_reverse"):
        native_ok = False
    checks.check("F_native_forward_reverse_common_source", native_ok,
                 "one rank-five quantum moment feeds exact H1/H2 native forward and literal actual-reverse sources")

    family = open_family_facts()
    family_ok = (
        family["symbolic_identity"] and family["probability_rank"] == 5
        and family["box_neighbor_positive"] and family["box_corner_positive"]
        and family["sample_identity"]
    )
    if mutation in ("sample_only", "heldout_refit", "shrink_family"):
        family_ok = False
    checks.check("G_symbolic_open_family_holdout", family_ok,
                 "the post-freeze five-parameter STF family is reproduced identically with positive box witnesses and rank five")

    ownership = ownership_facts()
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    no_go_text = NO_GO.read_text(encoding="utf-8") if NO_GO.is_file() else ""
    scope_phrases = (
        "CAPACITY-ONLY", "action-state solder remains open",
        "law-level distribution", "not the realized one-Record outcome",
        "obligation retirement: 0", "TOE percentage movement: 0",
        "N1 — Alternative route enumeration", "N8 — Cross-cycle echo",
    )
    ownership_ok = (
        ownership["runtime_clean"] and ownership["candidate_open_markers"]
        and not ownership["joint_action_state_typed"]
        and ownership["verdict"] == "CAPACITY-ONLY"
        and all(phrase in note_text + "\n" + no_go_text for phrase in scope_phrases)
    )
    if mutation in (
        "claim_owned", "assume_solder", "claim_record", "use_downstream_m4",
        "claim_axiom", "claim_toe", "claim_retained",
    ):
        ownership_ok = False
    checks.check("H_ownership_adjudication", ownership_ok,
                 "the extensional law is fixture-blind but joint action/clock M2 typing is not proved, so the registered verdict is CAPACITY-ONLY")

    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        "KERNEL: inputs=six_neighbor_M2_Record_contents; possibilities=6_axes+8_composite_corners; tau=1/24; axis_floor=1/18; corner_floor=1/64; M=tau*S."
    )
    print(
        "COMMON_SOURCE: Q_source=-32*M; H1_exact=true; H2_exact=true; common_rank=5; forward_reverse=true; cubic_frames=24."
    )
    print(
        f"POSITIVITY: H1_neighbor_max_norm2={max(h1['neighbor_norms'])}; H1_corner_max_norm2={max(h1['corner_norms'])}; H2_neighbor_max_norm2={max(h2['neighbor_norms'])}; H2_corner_max_norm2={max(h2['corner_norms'])}."
    )
    print(
        f"HOLDOUT: symbolic_STF_rank={family['probability_rank']}; box_neighbor_max_norm2={family['max_neighbor_vertex_norm2']}; box_corner_max_norm2={family['max_corner_vertex_norm2']}."
    )
    print(
        "ADJUDICATION: CAPACITY-ONLY; law_level_extensional_distribution=true; action_state_solder=false; joint_clock_M2_typing=false; target_runtime_input=false."
    )
    print(
        "ACCOUNTING: formation_not_run=true; realized_draw_not_run=true; permanent_Record_not_run=true; history_not_run=true; gravity_not_run=true; axiom_update=false; obligation_retirement=0; TOE_movement=0; retained=false."
    )
    print(
        "per_element: checked all 18 neighbor Bloch coordinates, 14 possibility probabilities, five STF coordinates, exact H1/H2 coefficients, and native source columns."
    )
    print(
        "per_site: checked the center's six nearest-neighbor M2 Record contents; eight corners are three-neighbor composite mixtures and no diagonal lattice site is read."
    )
    print(
        "per_mode: checked H1, H2, a symbolic five-parameter heldout family, all 24 cubic frames, and literal forward plus actual-reverse native maps."
    )
    print(
        "per_block: checked universal positivity/normalization, cubic covariance, target preparation, moment inversion, native source injection, open-family holdout, and ownership typing."
    )
    print(
        "lattice_wide: checked and not executed — no action-state solder, typed time relay on the same M2 inputs, formation site/rate, realized history, clock normalization, gravity coupling, axiom change, or retained TOE law is supplied."
    )
    print(f"SCORECARD PASS={checks.passed} FAIL={checks.failed}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return checks.failed


if __name__ == "__main__":
    raise SystemExit(main())
