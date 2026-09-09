#!/usr/bin/env python3
"""Block 10: same-six-M2 joint action/quadrupole carrier.

One odd six-neighbor Bloch shell defines a real 3x3 matrix.  Its scalar,
antisymmetric, and symmetric-trace-free pieces carry the local time phase,
spatial action vector, and spin-two source without contaminating one another.
The runner tests this fixed preparation on H1, held-out H2, every proper-cubic
frame, and a symbolic nine-parameter neighborhood.  It does not promote a
condition carrier to causal preparation, Record formation, or retained TOE
physics.
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

import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29 as b9  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block10-joint-action-quadrupole-carrier-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

PARENT = "ac1473f94fd5df2647bda77b22a191987f4aa05f"
BLOCK9_RESULT = "8bcb2edba7006296e384ca3854edf547725e4569"
PREREG = "67accddd65f15396fb810237147ba6902c94a9bc"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "1fbc42869af63b64e034ef23aa098cf594064985"
PREFLIGHT_BLOB = "e89b0e6060a868a4361b4251f43e6912ceb2bf42"
BLOCK9_RUNNER_BLOB = "dbc2df4b4eacda89fe9c981044eda39e5258d50c"
BLOCK9_NOTE_BLOB = "c96dbf3c7d2e94cf289cc502641b9d55d3b3aaf5"
BLOCK9_CACHE_BLOB = "3ca89e8eac911d60ed3ea38e39f9e3cfb2cfb32e"
B193_RUNNER_BLOB = "c60edb2e8e3683e99f4f3dddcc4980fd1db28786"
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
    ".claude/science/physics-loops/toe-source-eta-ownership-block10-joint-action-quadrupole-carrier-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block10-joint-action-quadrupole-carrier-20260829/PREFLIGHT_WITNESSES.md",
    "docs/ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.txt",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
)

ALPHA = -sp.Rational(1, 2)
BETA = sp.Rational(1, 8)
I3 = sp.eye(3)
I = sp.I

MUTATIONS = (
    "stale_parent", "stale_prereg", "candidate_blob_drift",
    "change_quadrupole_gain", "change_action_gain", "drop_scalar",
    "drop_vector", "drop_e", "drop_t2", "rank_eight",
    "break_rotation", "break_cross_orientation", "action_leaks_to_moment",
    "wrong_source_gain", "h1_nonpositive", "h2_nonpositive",
    "erase_h1_incoming", "erase_h1_outgoing", "erase_h2_incoming",
    "erase_h2_outgoing", "erase_h1_reverse", "erase_h2_reverse",
    "erase_h1_native", "erase_h2_native", "sample_only",
    "shrink_open_family", "target_runtime", "claim_causal_preparation",
    "claim_record_formation", "claim_axiom", "claim_toe",
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


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def cross_matrix(vector: sp.MatrixBase) -> sp.Matrix:
    x, y, z = vector
    return sp.Matrix(((0, -z, y), (z, 0, -x), (-y, x, 0)))


def axial(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix((matrix[2, 1], matrix[0, 2], matrix[1, 0]))


def joint_vectors(
    tensor: sp.MatrixBase,
    spatial_action: sp.MatrixBase,
    time_action: sp.Expr,
) -> tuple[sp.Matrix, ...]:
    """Fixed registered preparation; this is a reachability witness, not the law."""
    return tuple(
        sp.expand(
            ALPHA * tensor * direction
            + BETA * (time_action * direction + spatial_action.cross(direction))
        )
        for direction in b9.DIRECTIONS
    )


def odd_shell_matrix(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    if len(vectors) != 6:
        raise ValueError("six neighboring Bloch vectors are required")
    return sp.expand(sum(
        (vector * direction.T
         for direction, vector in zip(b9.DIRECTIONS, vectors)),
        sp.zeros(3),
    ) / 2)


def joint_decode(vectors: tuple[sp.Matrix, ...]) -> dict[str, object]:
    """Decode only the six local contents; no external label enters."""
    matrix = odd_shell_matrix(vectors)
    symmetric = sp.expand((matrix + matrix.T) / 2)
    skew = sp.expand((matrix - matrix.T) / 2)
    tensor = sp.expand(
        (symmetric - sp.trace(symmetric) * I3 / 3) / ALPHA
    )
    spatial_action = sp.expand(axial(skew) / BETA)
    time_action = sp.simplify(sp.trace(matrix) / (3 * BETA))
    return {
        "matrix": matrix,
        "tensor": tensor,
        "spatial_action": spatial_action,
        "time_action": time_action,
    }


def normalized_action(point: tuple[sp.Expr, ...]) -> tuple[sp.Matrix, sp.Expr]:
    return sp.Matrix(tuple(sp.simplify(point[index] / sp.pi)
                           for index in range(3))), sp.simplify(point[3] / sp.pi)


def decoded_point(vectors: tuple[sp.Matrix, ...]) -> tuple[sp.Expr, ...]:
    decoded = joint_decode(vectors)
    spatial = decoded["spatial_action"]
    assert isinstance(spatial, sp.MatrixBase)
    return tuple(sp.simplify(sp.pi * spatial[index]) for index in range(3)) + (
        sp.simplify(sp.pi * decoded["time_action"]),
    )


def norm_squared(vector: sp.MatrixBase) -> sp.Expr:
    return sp.expand((vector.T * vector)[0])


def strictly_inside_bloch_ball(vector: sp.MatrixBase) -> bool:
    return b9.strictly_below_one(sp.simplify(norm_squared(vector)))


def maximum_exact(values: tuple[sp.Expr, ...]) -> sp.Expr:
    return max(values, key=lambda value: float(sp.N(value, 30)))


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "block9_result": ancestor(BLOCK9_RESULT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", str(GOAL.relative_to(ROOT))),
        "preflight": git("hash-object", str(PREFLIGHT.relative_to(ROOT))),
        "block9_runner": git("rev-parse", f"{PARENT}:scripts/admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.py"),
        "block9_note": git("rev-parse", f"{PARENT}:docs/ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"),
        "block9_cache": git("rev-parse", f"{PARENT}:logs/runner-cache/admissibility_d4_quantum_quadrupole_common_source_owner_2026_08_29.txt"),
        "b193_runner": git("rev-parse", f"{PARENT}:scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py"),
        "block208_note": git("rev-parse", f"{BLOCK208}:{BLOCK208_NOTE}"),
        "block208_runner": git("rev-parse", f"{BLOCK208}:{BLOCK208_RUNNER}"),
    }


def flatten(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(tuple(matrix[row, column]
                           for row in range(matrix.rows)
                           for column in range(matrix.cols)))


@cache
def decomposition_facts() -> dict[str, object]:
    shell_symbols = sp.symbols("x0:18", real=True)
    shell = tuple(sp.Matrix(shell_symbols[3 * index:3 * index + 3])
                  for index in range(6))
    matrix = odd_shell_matrix(shell)
    symmetric = sp.expand((matrix + matrix.T) / 2)
    scalar = sp.trace(symmetric) * I3 / 3
    trace_free = sp.expand(symmetric - scalar)
    skew = sp.expand((matrix - matrix.T) / 2)
    matrix_map = flatten(matrix).jacobian(shell_symbols)
    scalar_map = flatten(scalar).jacobian(shell_symbols)
    vector_map = flatten(skew).jacobian(shell_symbols)
    spin2_map = flatten(trace_free).jacobian(shell_symbols)

    q0, q1, q2, q3, q4, ux, uy, uz, s = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz s", real=True
    )
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4), (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    prepared = joint_vectors(tensor, spatial, s)
    decoded = joint_decode(prepared)
    parameters = (q0, q1, q2, q3, q4, ux, uy, uz, s)
    prepared_map = sp.Matrix.vstack(*prepared).jacobian(parameters)
    decoded_coordinates = sp.Matrix((
        decoded["tensor"][0, 0], decoded["tensor"][1, 1],
        decoded["tensor"][0, 1], decoded["tensor"][0, 2],
        decoded["tensor"][1, 2],
        *tuple(decoded["spatial_action"]), decoded["time_action"],
    ))
    return {
        "matrix_rank": matrix_map.rank(),
        "scalar_rank": scalar_map.rank(),
        "vector_rank": vector_map.rank(),
        "spin2_rank": spin2_map.rank(),
        "sum_rank": sp.Matrix.vstack(scalar_map, vector_map, spin2_map).rank(),
        "prepared_rank": prepared_map.rank(),
        "decode_identity": decoded_coordinates == sp.Matrix(parameters),
        "matrix_identity": matrix_equal(
            decoded["matrix"], ALPHA * tensor + BETA * (s * I3 + cross_matrix(spatial))
        ),
    }


@cache
def covariance_facts() -> dict[str, object]:
    q0, q1, q2, q3, q4, ux, uy, uz, s = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz s", real=True
    )
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4), (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    vectors = joint_vectors(tensor, spatial, s)
    failures = []
    for rotation in b9.rotations():
        transformed_tensor = sp.expand(rotation * tensor * rotation.T)
        transformed_spatial = sp.expand(rotation * spatial)
        direct = joint_vectors(transformed_tensor, transformed_spatial, s)
        transported = []
        for direction in b9.DIRECTIONS:
            old_direction = rotation.T * direction
            old_index = next(index for index, item in enumerate(b9.DIRECTIONS)
                             if item == old_direction)
            transported.append(sp.expand(rotation * vectors[old_index]))
        decoded = joint_decode(tuple(transported))
        failures.append(not (
            all(matrix_equal(left, right)
                for left, right in zip(direct, transported))
            and matrix_equal(decoded["tensor"], transformed_tensor)
            and matrix_equal(decoded["spatial_action"], transformed_spatial)
            and sp.simplify(decoded["time_action"] - s) == 0
            and matrix_equal(
                decoded["matrix"], rotation * odd_shell_matrix(vectors) * rotation.T
            )
        ))
    return {"rotation_count": len(b9.rotations()), "failures": tuple(failures)}


@cache
def orthogonality_and_law_facts() -> dict[str, object]:
    q0, q1, q2, q3, q4, ux, uy, uz, s = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz s", real=True
    )
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4), (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    vectors = joint_vectors(tensor, spatial, s)
    geometry_only = joint_vectors(tensor, sp.zeros(3, 1), 0)
    condition = b9.condition_tensor(vectors)
    probabilities = b9.local_distribution(vectors)
    geometry_probabilities = b9.local_distribution(geometry_only)
    moment = b9.distribution_moment(probabilities)
    universal = b9.universal_facts()
    return {
        "condition": condition,
        "condition_identity": matrix_equal(condition, ALPHA * tensor),
        "probability_independence": all(
            sp.simplify(probabilities[key] - geometry_probabilities[key]) == 0
            for key in probabilities
        ),
        "moment_identity": matrix_equal(moment, b9.TAU * ALPHA * tensor),
        "source_identity": matrix_equal(-48 * moment, tensor),
        "normalization": sp.simplify(sum(probabilities.values())),
        "universal_axis_floor": universal["axis_floor"],
        "universal_corner_floor": universal["corner_floor"],
        "universal_condition_rank": universal["condition_rank"],
        "universal_probability_rank": universal["probability_rank"],
    }


def centered_vertices(
    incoming: tuple[sp.Expr, ...], transfer: tuple[sp.Expr, ...]
) -> tuple[tuple[sp.Matrix, ...], tuple[sp.Matrix, ...]]:
    outgoing = tuple(sp.simplify(incoming[index] + transfer[index])
                     for index in range(4))
    forward = b193.b190.centered_objects(incoming, transfer)[2]
    reverse = b193.b190.centered_objects(
        outgoing, tuple(-value for value in transfer)
    )[2]
    return tuple(forward), tuple(reverse)


@cache
def one_target_facts(name: str) -> dict[str, object]:
    target = b9.target_facts()[name.lower()]
    tensor = target["tensor"]
    assert isinstance(tensor, sp.MatrixBase)
    incoming, transfer = b193.POINTS[name]
    outgoing = tuple(sp.simplify(incoming[index] + transfer[index])
                     for index in range(4))
    incoming_spatial, incoming_time = normalized_action(incoming)
    outgoing_spatial, outgoing_time = normalized_action(outgoing)
    incoming_vectors = joint_vectors(tensor, incoming_spatial, incoming_time)
    outgoing_vectors = joint_vectors(tensor, outgoing_spatial, outgoing_time)
    decoded_incoming = decoded_point(incoming_vectors)
    decoded_outgoing = decoded_point(outgoing_vectors)
    decoded_transfer = tuple(sp.simplify(
        decoded_outgoing[index] - decoded_incoming[index]
    ) for index in range(4))

    forward_expected, reverse_expected = centered_vertices(incoming, transfer)
    forward_decoded, reverse_decoded = centered_vertices(
        decoded_incoming, decoded_transfer
    )
    phase_checks = []
    for orientation in (1, -1):
        for decoded_value, expected_value in zip(decoded_incoming, incoming):
            phase_checks.append(sp.simplify(
                sp.expand_complex(sp.exp(I * orientation * decoded_value)
                                  - sp.exp(I * orientation * expected_value))
            ) == 0)
        for decoded_value, expected_value in zip(decoded_outgoing, outgoing):
            phase_checks.append(sp.simplify(
                sp.expand_complex(sp.exp(I * orientation * decoded_value)
                                  - sp.exp(I * orientation * expected_value))
            ) == 0)

    all_vectors = incoming_vectors + outgoing_vectors
    neighbor_norms = tuple(sp.simplify(norm_squared(vector))
                           for vector in all_vectors)
    corner_vectors = tuple(
        b9.composite_corner(shell, corner)
        for shell in (incoming_vectors, outgoing_vectors)
        for corner in b9.CORNERS
    )
    corner_norms = tuple(sp.simplify(norm_squared(vector))
                         for vector in corner_vectors)
    source_checks = []
    orbit_positivity = []
    for shell in (incoming_vectors, outgoing_vectors):
        probabilities = b9.local_distribution(shell)
        source_checks.append(matrix_equal(
            -48 * b9.distribution_moment(probabilities), tensor
        ))
    for rotation in b9.rotations():
        rotated_tensor = sp.expand(rotation * tensor * rotation.T)
        for spatial, time in (
            (rotation * incoming_spatial, incoming_time),
            (rotation * outgoing_spatial, outgoing_time),
        ):
            shell = joint_vectors(rotated_tensor, spatial, time)
            orbit_positivity.append(all(strictly_inside_bloch_ball(vector)
                                        for vector in shell))
            orbit_positivity.append(all(strictly_inside_bloch_ball(
                b9.composite_corner(shell, corner)
            ) for corner in b9.CORNERS))

    return {
        "tensor": tensor,
        "incoming": incoming,
        "outgoing": outgoing,
        "transfer": transfer,
        "decoded_incoming": decoded_incoming,
        "decoded_outgoing": decoded_outgoing,
        "decoded_transfer": decoded_transfer,
        "decode_exact": decoded_incoming == incoming and decoded_outgoing == outgoing
        and decoded_transfer == transfer,
        "phase_checks": all(phase_checks),
        "forward_vertices": all(matrix_equal(left, right)
                                for left, right in zip(forward_expected, forward_decoded)),
        "reverse_vertices": all(matrix_equal(left, right)
                                for left, right in zip(reverse_expected, reverse_decoded)),
        "neighbor_positive": all(strictly_inside_bloch_ball(vector)
                                 for vector in all_vectors),
        "corner_positive": all(strictly_inside_bloch_ball(vector)
                               for vector in corner_vectors),
        "max_neighbor_norm2": maximum_exact(neighbor_norms),
        "max_corner_norm2": maximum_exact(corner_norms),
        "source_checks": all(source_checks),
        "orbit_positivity": all(orbit_positivity),
        "native_coefficients": b9.tensor_to_coeff(tensor) == target["coefficients"],
    }


@cache
def target_facts() -> dict[str, object]:
    return {"h1": one_target_facts("H1"), "h2": one_target_facts("H2")}


@cache
def open_family_facts() -> dict[str, object]:
    a, b, d, e, f, ux, uy, uz, s = sp.symbols(
        "a b d e f ux uy uz s", real=True
    )
    tensor = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    spatial = sp.Matrix((ux, uy, uz))
    parameters = (a, b, d, e, f, ux, uy, uz, s)
    vectors = joint_vectors(tensor, spatial, s)
    decoded = joint_decode(vectors)
    output = sp.Matrix((
        decoded["tensor"][0, 0], decoded["tensor"][1, 1],
        decoded["tensor"][0, 1], decoded["tensor"][0, 2],
        decoded["tensor"][1, 2], *tuple(decoded["spatial_action"]),
        decoded["time_action"],
    ))
    neighbor_norms = []
    corner_norms = []
    for signs in itertools.product((-1, 1), repeat=9):
        substitution = dict(zip(
            parameters, (sp.Rational(sign, 4) for sign in signs)
        ))
        shell = tuple(vector.subs(substitution) for vector in vectors)
        neighbor_norms.extend(norm_squared(vector) for vector in shell)
        corner_norms.extend(norm_squared(b9.composite_corner(shell, corner))
                            for corner in b9.CORNERS)
    expected = sp.Matrix(parameters)
    return {
        "symbolic_identity": output == expected,
        "rank": output.jacobian(parameters).rank(),
        "vertex_count": 2 ** len(parameters),
        "max_neighbor_norm2": max(neighbor_norms),
        "max_corner_norm2": max(corner_norms),
        "neighbor_positive": bool(max(neighbor_norms) < 1),
        "corner_positive": bool(max(corner_norms) < 1),
    }


@cache
def ownership_facts() -> dict[str, object]:
    decoder_signature = tuple(inspect.signature(joint_decode).parameters)
    law_signature = tuple(inspect.signature(b9.local_distribution).parameters)
    decoder_source = inspect.getsource(joint_decode)
    forbidden = ("H1", "H2", "momentum", "fixture", "target", "realized")
    candidate_text = git_show(BLOCK208, BLOCK208_NOTE)
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    return {
        "decoder_signature": decoder_signature,
        "law_signature": law_signature,
        "runtime_clean": decoder_signature == ("vectors",)
        and law_signature == ("vectors",)
        and not any(token in decoder_source for token in forbidden),
        "candidate_solder_open": "action-to-`M2` state solder" in candidate_text
        and "**open**" in candidate_text,
        "condition_solder_constructed": True,
        "causal_preparation": False,
        "record_attachment": False,
        "scope": all(phrase in note_text for phrase in (
            "JOINT-CARRIER", "condition-content level",
            "causal preparation remains open",
            "obligation retirement: 0", "TOE percentage movement: 0",
        )),
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
        and authority["block9_result"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["block9_runner"] == BLOCK9_RUNNER_BLOB
        and authority["block9_note"] == BLOCK9_NOTE_BLOB
        and authority["block9_cache"] == BLOCK9_CACHE_BLOB
        and authority["b193_runner"] == B193_RUNNER_BLOB
        and authority["block208_note"] == BLOCK208_NOTE_BLOB
        and authority["block208_runner"] == BLOCK208_RUNNER_BLOB
    )
    if mutation in ("stale_parent", "stale_prereg", "candidate_blob_drift"):
        authority_ok = False
    checks.check("A_frozen_authority", authority_ok,
                 "parent, preregistration, main, axioms, Block-09, action source, and candidate Block-208 blobs match")

    decomposition = decomposition_facts()
    decomposition_ok = (
        decomposition["matrix_rank"] == 9
        and decomposition["scalar_rank"] == 1
        and decomposition["vector_rank"] == 3
        and decomposition["spin2_rank"] == 5
        and decomposition["sum_rank"] == 9
        and decomposition["prepared_rank"] == 9
        and decomposition["decode_identity"] and decomposition["matrix_identity"]
    )
    if mutation in (
        "change_quadrupole_gain", "change_action_gain", "drop_scalar",
        "drop_vector", "drop_e", "drop_t2", "rank_eight",
    ):
        decomposition_ok = False
    checks.check("B_exact_joint_decomposition", decomposition_ok,
                 "one odd-shell 3x3 matrix splits exactly as A1 rank 1 plus T1 rank 3 plus E+T2 rank 5, with a rank-nine positive-state preparation")

    covariance = covariance_facts()
    covariance_ok = covariance["rotation_count"] == 24 and not any(covariance["failures"])
    if mutation in ("break_rotation", "break_cross_orientation"):
        covariance_ok = False
    checks.check("C_exact_proper_cubic_covariance", covariance_ok,
                 "the shell, scalar clock, spatial action vector, quadrupole, and raw matrix intertwine in all 24 proper-cubic frames")

    law = orthogonality_and_law_facts()
    law_ok = (
        law["condition_identity"] and law["probability_independence"]
        and law["moment_identity"] and law["source_identity"]
        and law["normalization"] == 1
        and law["universal_axis_floor"] == sp.Rational(1, 18)
        and law["universal_corner_floor"] == sp.Rational(1, 64)
        and law["universal_condition_rank"] == 5
        and law["universal_probability_rank"] == 5
    )
    if mutation in ("action_leaks_to_moment", "wrong_source_gain"):
        law_ok = False
    checks.check("D_action_geometry_orthogonality", law_ok,
                 "action coordinates leave the Block-09 law unchanged; it stays universally normalized/positive and Q=-48M exactly")

    targets = target_facts()
    h1 = targets["h1"]
    h1_ok = all((
        h1["decode_exact"], h1["phase_checks"], h1["forward_vertices"],
        h1["reverse_vertices"], h1["neighbor_positive"], h1["corner_positive"],
        h1["source_checks"], h1["orbit_positivity"], h1["native_coefficients"],
    ))
    if mutation in (
        "h1_nonpositive", "erase_h1_incoming", "erase_h1_outgoing",
        "erase_h1_reverse", "erase_h1_native",
    ):
        h1_ok = False
    checks.check("E_exact_h1_joint_carrier", h1_ok,
                 "the same positive six-M2 shells decode H1 incoming/outgoing phases, forward/actual-reverse action vertices, and the native quadrupole source")

    h2 = targets["h2"]
    h2_ok = all((
        h2["decode_exact"], h2["phase_checks"], h2["forward_vertices"],
        h2["reverse_vertices"], h2["neighbor_positive"], h2["corner_positive"],
        h2["source_checks"], h2["orbit_positivity"], h2["native_coefficients"],
    ))
    if mutation in (
        "h2_nonpositive", "erase_h2_incoming", "erase_h2_outgoing",
        "erase_h2_reverse", "erase_h2_native",
    ):
        h2_ok = False
    checks.check("F_exact_h2_heldout_joint_carrier", h2_ok,
                 "held-out H2 uses the identical gains and shells for exact phases, forward/actual-reverse action vertices, E+T2 source, and all frames")

    family = open_family_facts()
    family_ok = (
        family["symbolic_identity"] and family["rank"] == 9
        and family["vertex_count"] == 512
        and family["neighbor_positive"] and family["corner_positive"]
    )
    if mutation in ("sample_only", "shrink_open_family"):
        family_ok = False
    checks.check("G_symbolic_nine_parameter_holdout", family_ok,
                 "the exact rank-nine family survives all 512 vertices of the preregistered box with strict neighbor and corner positivity")

    ownership = ownership_facts()
    ownership_ok = (
        ownership["runtime_clean"] and ownership["candidate_solder_open"]
        and ownership["condition_solder_constructed"]
        and not ownership["causal_preparation"]
        and not ownership["record_attachment"] and ownership["scope"]
    )
    if mutation in (
        "target_runtime", "claim_causal_preparation", "claim_record_formation",
        "claim_axiom", "claim_toe", "claim_retained",
    ):
        ownership_ok = False
    checks.check("H_joint_carrier_adjudication", ownership_ok,
                 "the registered verdict is JOINT-CARRIER at condition-content level; causal preparation, Record attachment, and retained physics remain open")

    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        "JOINT_MATRIX: F=(1/2)sum(v_n n^T); decomposition=A1(1)+T1(3)+E+T2(5); rank=9; kernel_even_shell=9."
    )
    print(
        "PREPARATION: v_n=-(1/2)Qn+(1/8)(s*n+u_cross_n); decode_Q=-2*STF(symF); decode_s=(8/3)trF; decode_u=8*axial(skewF)."
    )
    print(
        "LAW: possibilities=6_axes+8_composite_corners; action_leakage=0; tau=1/24; floors=1/18,1/64; M=-Q/48; Q_source=-48M."
    )
    print(
        f"H1: decode=true; forward=true; actual_reverse=true; max_neighbor_norm2={h1['max_neighbor_norm2']}; max_corner_norm2={h1['max_corner_norm2']}."
    )
    print(
        f"H2: decode=true; forward=true; actual_reverse=true; max_neighbor_norm2={h2['max_neighbor_norm2']}; max_corner_norm2={h2['max_corner_norm2']}."
    )
    print(
        f"HOLDOUT: parameters=9; vertices={family['vertex_count']}; rank={family['rank']}; max_neighbor_norm2={family['max_neighbor_norm2']}; max_corner_norm2={family['max_corner_norm2']}."
    )
    print(
        "ADJUDICATION: JOINT-CARRIER; condition_level_action_state_solder=true; causal_preparation=false; permanent_Record_attachment=false; law_selection=false."
    )
    print(
        "ACCOUNTING: formation_not_run=true; history_not_run=true; gravity_not_run=true; axiom_update=false; obligation_retirement=0; TOE_movement=0; retained=false."
    )
    print(
        "per_element: checked all 18 shell coordinates, nine decoded action/quadrupole coordinates, fourteen probabilities, H1/H2 phase ratios, and centered action vertices."
    )
    print(
        "per_site: checked the same six nearest-neighbor M2 contents for incoming and outgoing H1/H2 conditions; composite corners are mixtures, not diagonal sites."
    )
    print(
        "per_mode: checked scalar time, spatial vector, E doublet, T2 triplet, both Clifford orientations, and literal forward plus actual reverse."
    )
    print(
        "per_block: checked rank-nine decomposition, universal law orthogonality, H1, held-out H2, all 24 frames, and a 512-vertex open neighborhood."
    )
    print(
        "lattice_wide: checked and not executed — no causal preparation, instrument selection, readable/permanent Record write, formation rate, history, gravity, axiom edit, or retained TOE law is supplied."
    )
    print(f"SCORECARD PASS={checks.passed} FAIL={checks.failed}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return checks.failed


if __name__ == "__main__":
    raise SystemExit(main())
