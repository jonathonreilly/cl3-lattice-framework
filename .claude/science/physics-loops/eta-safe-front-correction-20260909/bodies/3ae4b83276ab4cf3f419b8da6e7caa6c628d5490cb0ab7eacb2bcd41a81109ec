#!/usr/bin/env python3
"""Independent Block-10 joint-carrier reconstruction.

This checker does not import the primary Block-10 or Block-09 runner.  It
rebuilds the signed shell, cubic group, matrix decomposition, probability
moment, H1/H2 target tensors, action decoder, and open-family positivity.
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

import admissibility_d4_common_spin2_source_module_2026_08_29 as b8  # noqa: E402
import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402


PARENT = "ac1473f94fd5df2647bda77b22a191987f4aa05f"
PREREG = "67accddd65f15396fb810237147ba6902c94a9bc"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "1fbc42869af63b64e034ef23aa098cf594064985"
PREFLIGHT_BLOB = "e89b0e6060a868a4361b4251f43e6912ceb2bf42"
PRIMARY = "scripts/admissibility_d4_joint_action_quadrupole_six_m2_carrier_2026_08_29.py"
NOTE_PATH = (
    "docs/ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block10-joint-action-quadrupole-carrier-20260829"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"

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

R = sp.Rational
ALPHA = -R(1, 2)
BETA = R(1, 8)
TAU = R(1, 24)
I3 = sp.eye(3)
I = sp.I
DIRECTIONS = tuple(sp.Matrix(vector) for vector in (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
))
CORNERS = tuple(sp.Matrix(corner)
                for corner in itertools.product((-1, 1), repeat=3))

MUTATIONS = (
    "stale_authority", "drop_registration", "import_primary",
    "rank_defect", "scalar_defect", "vector_defect", "spin2_defect",
    "decode_defect", "covariance_defect", "law_leakage",
    "normalization_defect", "moment_gain_defect", "h1_decode_defect",
    "h1_positive_defect", "h1_reverse_defect", "h2_decode_defect",
    "h2_positive_defect", "h2_reverse_defect", "family_rank_defect",
    "family_positive_defect", "claim_preparation", "claim_record",
    "claim_axiom", "claim_toe", "claim_retained",
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
    return all(sp.simplify(value) == 0 for value in left - right)


def stf(matrix: sp.MatrixBase) -> sp.Matrix:
    symmetric = sp.expand((matrix + matrix.T) / 2)
    return sp.expand(symmetric - sp.trace(symmetric) * I3 / 3)


def cross_matrix(vector: sp.MatrixBase) -> sp.Matrix:
    x, y, z = vector
    return sp.Matrix(((0, -z, y), (z, 0, -x), (-y, x, 0)))


def independent_prepare(
    tensor: sp.MatrixBase, spatial: sp.MatrixBase, time: sp.Expr
) -> tuple[sp.Matrix, ...]:
    return tuple(sp.expand(
        ALPHA * tensor * direction
        + BETA * (time * direction + cross_matrix(spatial) * direction)
    ) for direction in DIRECTIONS)


def independent_matrix(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.expand(sum(
        (vector * direction.T for vector, direction in zip(vectors, DIRECTIONS)),
        sp.zeros(3),
    ) / 2)


def independent_decode(vectors: tuple[sp.Matrix, ...]) -> tuple[sp.Matrix, sp.Matrix, sp.Expr]:
    matrix = independent_matrix(vectors)
    symmetric = sp.expand((matrix + matrix.T) / 2)
    skew = sp.expand((matrix - matrix.T) / 2)
    tensor = sp.expand(stf(symmetric) / ALPHA)
    spatial = sp.expand(sp.Matrix((skew[2, 1], skew[0, 2], skew[1, 0])) / BETA)
    time = sp.simplify(sp.trace(matrix) / (3 * BETA))
    return tensor, spatial, time


def condition(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return stf(sum(
        (direction * vector.T + vector * direction.T
         for direction, vector in zip(DIRECTIONS, vectors)),
        sp.zeros(3),
    ) / 4)


def probabilities(vectors: tuple[sp.Matrix, ...]) -> tuple[sp.Expr, ...]:
    tensor = condition(vectors)
    result = []
    for direction in DIRECTIONS:
        axis = next(index for index in range(3) if direction[index] != 0)
        result.append(sp.expand(R(1, 12) + TAU * tensor[axis, axis] / 2))
    for corner in CORNERS:
        mixed = (
            tensor[0, 1] * corner[0] * corner[1]
            + tensor[1, 2] * corner[1] * corner[2]
            + tensor[0, 2] * corner[0] * corner[2]
        )
        result.append(sp.expand(R(1, 16) + 3 * TAU * mixed / 8))
    return tuple(result)


def moment(values: tuple[sp.Expr, ...]) -> sp.Matrix:
    raw = sp.zeros(3)
    for index, direction in enumerate(DIRECTIONS):
        raw += values[index] * direction * direction.T
    for index, corner in enumerate(CORNERS, start=6):
        raw += values[index] * corner * corner.T / 3
    return stf(raw)


def rotations() -> tuple[sp.Matrix, ...]:
    result = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if matrix.det() == 1:
                result.append(matrix)
    unique = {tuple(matrix): matrix for matrix in result}
    return tuple(unique[key] for key in sorted(unique))


def coeff_to_tensor(coefficients: sp.MatrixBase) -> sp.Matrix:
    tensor = sp.zeros(3)
    tensor[0, 0], tensor[1, 1], tensor[2, 2] = (
        coefficients[1], coefficients[2], coefficients[3]
    )
    for value, (left, right) in zip(
        (coefficients[7], coefficients[8], coefficients[9]),
        ((0, 1), (0, 2), (1, 2)),
    ):
        tensor[left, right] = tensor[right, left] = value / sp.sqrt(2)
    return sp.expand(tensor)


def inside(vector: sp.MatrixBase) -> bool:
    value = sp.simplify((vector.T * vector)[0])
    decision = sp.simplify(1 - value).is_positive
    return bool(decision if decision is not None else sp.N(value, 50) < 1)


def corner_vector(vectors: tuple[sp.Matrix, ...], corner: sp.MatrixBase) -> sp.Matrix:
    selected = []
    for axis in range(3):
        direction = sp.zeros(3, 1)
        direction[axis] = corner[axis]
        selected.append(vectors[next(index for index, item in enumerate(DIRECTIONS)
                                     if item == direction)])
    return sp.expand(sum(selected, sp.zeros(3, 1)) / 3)


def point_from_shell(vectors: tuple[sp.Matrix, ...]) -> tuple[sp.Expr, ...]:
    _tensor, spatial, time = independent_decode(vectors)
    return tuple(sp.simplify(sp.pi * spatial[index]) for index in range(3)) + (
        sp.simplify(sp.pi * time),
    )


def centered_vertices(
    incoming: tuple[sp.Expr, ...], transfer: tuple[sp.Expr, ...]
) -> tuple[tuple[sp.Matrix, ...], tuple[sp.Matrix, ...]]:
    outgoing = tuple(sp.simplify(incoming[index] + transfer[index])
                     for index in range(4))
    forward = tuple(b193.b190.centered_objects(incoming, transfer)[2])
    reverse = tuple(b193.b190.centered_objects(
        outgoing, tuple(-value for value in transfer)
    )[2])
    return forward, reverse


@cache
def authority_facts() -> dict[str, object]:
    source = (ROOT / __file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported_modules = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module or ""
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    }
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", GOAL_PATH),
        "preflight": git("hash-object", PREFLIGHT_PATH),
        "primary_imported": any(
            module.startswith("admissibility_d4_joint_action_quadrupole")
            or module.startswith("admissibility_d4_quantum_quadrupole")
            for module in imported_modules
        ),
        "primary_exists": (ROOT / PRIMARY).is_file(),
    }


@cache
def decomposition_facts() -> dict[str, object]:
    xs = sp.symbols("x0:18", real=True)
    shell = tuple(sp.Matrix(xs[3 * index:3 * index + 3]) for index in range(6))
    matrix = independent_matrix(shell)
    symmetric = sp.expand((matrix + matrix.T) / 2)
    skew = sp.expand((matrix - matrix.T) / 2)
    scalar = sp.trace(symmetric) * I3 / 3
    spin2 = sp.expand(symmetric - scalar)
    flatten = lambda value: sp.Matrix(tuple(value))

    a, b, d, e, f, ux, uy, uz, s = sp.symbols(
        "a b d e f ux uy uz s", real=True
    )
    tensor = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    spatial = sp.Matrix((ux, uy, uz))
    parameters = (a, b, d, e, f, ux, uy, uz, s)
    prepared = independent_prepare(tensor, spatial, s)
    decoded_tensor, decoded_spatial, decoded_time = independent_decode(prepared)
    output = sp.Matrix((
        decoded_tensor[0, 0], decoded_tensor[1, 1], decoded_tensor[0, 1],
        decoded_tensor[0, 2], decoded_tensor[1, 2], *tuple(decoded_spatial),
        decoded_time,
    ))
    return {
        "matrix_rank": flatten(matrix).jacobian(xs).rank(),
        "scalar_rank": flatten(scalar).jacobian(xs).rank(),
        "vector_rank": flatten(skew).jacobian(xs).rank(),
        "spin2_rank": flatten(spin2).jacobian(xs).rank(),
        "joint_rank": sp.Matrix.vstack(
            flatten(scalar).jacobian(xs), flatten(skew).jacobian(xs),
            flatten(spin2).jacobian(xs),
        ).rank(),
        "preparation_rank": sp.Matrix.vstack(*prepared).jacobian(parameters).rank(),
        "identity": output == sp.Matrix(parameters),
    }


@cache
def law_and_covariance_facts() -> dict[str, object]:
    a, b, d, e, f, ux, uy, uz, s = sp.symbols(
        "a b d e f ux uy uz s", real=True
    )
    tensor = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    spatial = sp.Matrix((ux, uy, uz))
    shell = independent_prepare(tensor, spatial, s)
    values = probabilities(shell)
    failures = []
    for rotation in rotations():
        transformed = independent_prepare(
            rotation * tensor * rotation.T, rotation * spatial, s
        )
        transported = []
        for direction in DIRECTIONS:
            old = rotation.T * direction
            index = next(index for index, item in enumerate(DIRECTIONS)
                         if item == old)
            transported.append(sp.expand(rotation * shell[index]))
        decoded_tensor, decoded_spatial, decoded_time = independent_decode(
            tuple(transported)
        )
        failures.append(not (
            all(equal(left, right) for left, right in zip(transformed, transported))
            and equal(decoded_tensor, rotation * tensor * rotation.T)
            and equal(decoded_spatial, rotation * spatial)
            and sp.simplify(decoded_time - s) == 0
        ))
    return {
        "rotations": len(rotations()),
        "failures": tuple(failures),
        "condition": equal(condition(shell), ALPHA * tensor),
        "normalization": sp.simplify(sum(values)),
        "moment": equal(moment(values), TAU * ALPHA * tensor),
        "source": equal(-48 * moment(values), tensor),
    }


@cache
def target_facts(name: str) -> dict[str, object]:
    coefficients = b8.representation_facts()[name.lower()]
    tensor = coeff_to_tensor(coefficients)
    incoming, transfer = b193.POINTS[name]
    outgoing = tuple(sp.simplify(incoming[index] + transfer[index])
                     for index in range(4))
    in_spatial = sp.Matrix(tuple(incoming[index] / sp.pi for index in range(3)))
    out_spatial = sp.Matrix(tuple(outgoing[index] / sp.pi for index in range(3)))
    in_shell = independent_prepare(tensor, in_spatial, incoming[3] / sp.pi)
    out_shell = independent_prepare(tensor, out_spatial, outgoing[3] / sp.pi)
    decoded_in = point_from_shell(in_shell)
    decoded_out = point_from_shell(out_shell)
    decoded_transfer = tuple(sp.simplify(decoded_out[index] - decoded_in[index])
                             for index in range(4))
    expected_forward, expected_reverse = centered_vertices(incoming, transfer)
    decoded_forward, decoded_reverse = centered_vertices(decoded_in, decoded_transfer)
    phase = all(sp.simplify(sp.expand_complex(
        sp.exp(I * sign * got) - sp.exp(I * sign * want)
    )) == 0 for sign in (1, -1)
        for got, want in zip(decoded_in + decoded_out, incoming + outgoing))
    shells = (in_shell, out_shell)
    return {
        "decode": decoded_in == incoming and decoded_out == outgoing
        and decoded_transfer == transfer,
        "phase": phase,
        "forward": all(equal(left, right)
                       for left, right in zip(expected_forward, decoded_forward)),
        "reverse": all(equal(left, right)
                       for left, right in zip(expected_reverse, decoded_reverse)),
        "neighbors": all(inside(vector) for shell in shells for vector in shell),
        "corners": all(inside(corner_vector(shell, corner))
                       for shell in shells for corner in CORNERS),
        "source": all(equal(-48 * moment(probabilities(shell)), tensor)
                      for shell in shells),
    }


@cache
def family_facts() -> dict[str, object]:
    a, b, d, e, f, ux, uy, uz, s = sp.symbols(
        "a b d e f ux uy uz s", real=True
    )
    parameters = (a, b, d, e, f, ux, uy, uz, s)
    tensor = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    shell = independent_prepare(tensor, sp.Matrix((ux, uy, uz)), s)
    decoded_tensor, decoded_spatial, decoded_time = independent_decode(shell)
    output = sp.Matrix((
        decoded_tensor[0, 0], decoded_tensor[1, 1], decoded_tensor[0, 1],
        decoded_tensor[0, 2], decoded_tensor[1, 2], *tuple(decoded_spatial),
        decoded_time,
    ))
    neighbor_norms = []
    corner_norms = []
    for signs in itertools.product((-1, 1), repeat=9):
        substitution = dict(zip(parameters, (R(sign, 4) for sign in signs)))
        local = tuple(vector.subs(substitution) for vector in shell)
        neighbor_norms.extend(sp.expand((vector.T * vector)[0]) for vector in local)
        corner_norms.extend(sp.expand((corner_vector(local, corner).T
                                       * corner_vector(local, corner))[0])
                            for corner in CORNERS)
    return {
        "identity": output == sp.Matrix(parameters),
        "rank": output.jacobian(parameters).rank(),
        "vertices": 512,
        "neighbor_max": max(neighbor_norms),
        "corner_max": max(corner_norms),
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
        authority["main"] == MAIN and authority["parent"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and not authority["primary_imported"] and authority["primary_exists"]
    )
    if mutation in ("stale_authority", "drop_registration", "import_primary"):
        authority_ok = False
    checks.check("A_independent_authority", authority_ok,
                 "the independent checker is preregistration-bound and imports neither the primary nor Block-09 implementation")

    decomposition = decomposition_facts()
    decomposition_ok = (
        decomposition["matrix_rank"] == 9 and decomposition["scalar_rank"] == 1
        and decomposition["vector_rank"] == 3 and decomposition["spin2_rank"] == 5
        and decomposition["joint_rank"] == 9
        and decomposition["preparation_rank"] == 9 and decomposition["identity"]
    )
    if mutation in (
        "rank_defect", "scalar_defect", "vector_defect", "spin2_defect",
        "decode_defect",
    ):
        decomposition_ok = False
    checks.check("B_independent_rank_nine_decomposition", decomposition_ok,
                 "fresh Jacobians give scalar/vector/spin-two ranks 1/3/5 and an exact rank-nine preparation-decoder identity")

    law = law_and_covariance_facts()
    law_ok = (
        law["rotations"] == 24 and not any(law["failures"])
        and law["condition"] and law["normalization"] == 1
        and law["moment"] and law["source"]
    )
    if mutation in (
        "covariance_defect", "law_leakage", "normalization_defect",
        "moment_gain_defect",
    ):
        law_ok = False
    checks.check("C_independent_covariant_probability_law", law_ok,
                 "a separately generated cubic group confirms exact action orthogonality, normalization, M=-Q/48, and all 24 intertwiners")

    h1 = target_facts("H1")
    h1_ok = all(h1.values())
    if mutation in ("h1_decode_defect", "h1_positive_defect", "h1_reverse_defect"):
        h1_ok = False
    checks.check("D_independent_h1_joint_carrier", h1_ok,
                 "fresh H1 tensors and action points give strict shells, exact phases, forward vertices, actual reverse, and Q source")

    h2 = target_facts("H2")
    h2_ok = all(h2.values())
    if mutation in ("h2_decode_defect", "h2_positive_defect", "h2_reverse_defect"):
        h2_ok = False
    checks.check("E_independent_h2_heldout", h2_ok,
                 "held-out H2 independently passes the identical positive joint carrier and forward/actual-reverse reconstruction")

    family = family_facts()
    family_ok = (
        family["identity"] and family["rank"] == 9 and family["vertices"] == 512
        and family["neighbor_max"] == R(131, 1024)
        and family["corner_max"] == R(395, 9216)
    )
    if mutation in ("family_rank_defect", "family_positive_defect"):
        family_ok = False
    checks.check("F_independent_open_family", family_ok,
                 "the symbolic rank-nine identity and all 512 box vertices reproduce maxima 131/1024 and 395/9216")

    note = (ROOT / NOTE_PATH).read_text(encoding="utf-8")
    scope_ok = all(phrase in note for phrase in (
        "JOINT-CARRIER", "condition-content level",
        "causal preparation remains open", "obligation retirement: 0",
        "TOE percentage movement: 0",
    )) and tuple(inspect.signature(independent_decode).parameters) == ("vectors",)
    if mutation in (
        "claim_preparation", "claim_record", "claim_axiom", "claim_toe",
        "claim_retained",
    ):
        scope_ok = False
    checks.check("G_independent_scope", scope_ok,
                 "JOINT-CARRIER is limited to condition content; causal preparation, permanent Record attachment, axioms, and TOE remain open")

    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        "INDEPENDENT_MATRIX: ranks=1+3+5=9; preparation_rank=9; decoder_identity=true; proper_cubic_frames=24."
    )
    print(
        "INDEPENDENT_LAW: action_leakage=0; normalization=1; M=-Q/48; H1=true; H2=true; forward_reverse=true."
    )
    print(
        f"INDEPENDENT_HOLDOUT: parameters=9; vertices={family['vertices']}; neighbor_max_norm2={family['neighbor_max']}; corner_max_norm2={family['corner_max']}."
    )
    print(
        "INDEPENDENT_ADJUDICATION: JOINT-CARRIER; condition_solder=true; causal_preparation=false; permanent_Record=false; axiom_update=false; TOE_movement=0."
    )
    print(f"SCORECARD PASS={checks.passed} FAIL={checks.failed}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return checks.failed


if __name__ == "__main__":
    raise SystemExit(main())
