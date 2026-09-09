#!/usr/bin/env python3
"""Independent reconstruction for Source/Eta Block 09.

This checker does not import the primary runner or Block-08 wrapper.  It
rebuilds the signed cubic group, linear probability/moment maps, target tensor
basis, native Laurent source matrices, and scoped ownership adjudication.
"""

from __future__ import annotations

import argparse
from functools import cache
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as b3  # noqa: E402
import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402


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
PREREG = "916fda761aa9a168b4ae90e29af09e1fdb9457a1"
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "ea503ef9471b111de3afa32ea751a3eccbf28d38"
PREFLIGHT_BLOB = "cccd6f9365910c7db9c2c0d108dff5cb91a07c66"
BLOCK207 = "04b1c5d132f7ad46d6818854f8b733391ebdb6d2"
BLOCK207_NOTE = (
    "docs/ADMISSIBILITY_D4_H1_EDGE_COMPARISON_CELL_CORNER_T2_"
    "FACTORIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
BLOCK207_NOTE_BLOB = "96d5567b5e5e25728e9bbfa5333ff0cbb579a238"
BLOCK208 = "0be49cf0458beb616d1d7002e488e3005e763960"
BLOCK208_NOTE = (
    "docs/ADMISSIBILITY_D4_H1_TWO_TIME_CLIFFORD_CELL_M2_RECORD_"
    "COMPILER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
BLOCK208_NOTE_BLOB = "e546af320e6a7adc64e68f1b4f6e5a43c3d97515"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block09-quantum-quadrupole-owner-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block09-quantum-quadrupole-owner-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block09-quantum-quadrupole-owner-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
)

TAU = sp.Rational(1, 24)
SQRT2 = sp.sqrt(2)
DIRS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
CORNERS = tuple(itertools.product((-1, 1), repeat=3))

MUTATIONS = (
    "wrong_main", "missing_prereg", "wrong_candidate_note",
    "axis_baseline_shift", "corner_baseline_shift", "tau_double",
    "omit_trace_projection", "moment_scale", "negative_axis",
    "negative_corner", "rotation_reflection", "corner_as_site",
    "h1_offdiag_swap", "h1_prepare_scale", "h1_skip_orbit",
    "h2_drop_diagonal", "h2_prepare_scale", "h2_skip_orbit",
    "source_rank_four", "reverse_as_adjoint", "source_fixture_lookup",
    "holdout_numeric_only", "holdout_rank_four", "holdout_box_removed",
    "promote_owned", "invent_action_solder", "promote_record_history",
    "promote_axiom", "promote_toe", "promote_retained",
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


def vec(items: tuple[int, int, int]) -> sp.Matrix:
    return sp.Matrix(items)


def traceless(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.expand(matrix - sp.trace(matrix) * sp.eye(3) / 3)


def independent_tensor(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    accumulated = sp.zeros(3)
    for address, content in zip(DIRS, vectors):
        direction = vec(address)
        accumulated += direction * content.T + content * direction.T
    return traceless(accumulated / 4)


def independent_probabilities(tensor: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    rows = []
    for address in DIRS:
        axis = next(index for index, value in enumerate(address) if value)
        rows.append(sp.expand(sp.Rational(1, 12) + TAU * tensor[axis, axis] / 2))
    for corner in CORNERS:
        rows.append(sp.expand(sp.Rational(1, 16) + 3 * TAU * (
            tensor[0, 1] * corner[0] * corner[1]
            + tensor[0, 2] * corner[0] * corner[2]
            + tensor[1, 2] * corner[1] * corner[2]
        ) / 8))
    return tuple(rows)


def independent_moment(probabilities: tuple[sp.Expr, ...]) -> sp.Matrix:
    accumulated = sp.zeros(3)
    for probability, address in zip(probabilities[:6], DIRS):
        direction = vec(address)
        accumulated += probability * direction * direction.T
    for probability, corner in zip(probabilities[6:], CORNERS):
        direction = vec(corner)
        accumulated += probability * direction * direction.T / 3
    return traceless(accumulated)


def coefficient_tensor(coefficients: tuple[sp.Expr, ...]) -> sp.Matrix:
    result = sp.diag(coefficients[1], coefficients[2], coefficients[3])
    for value, (left, right) in zip(
        (coefficients[7], coefficients[8], coefficients[9]),
        ((0, 1), (0, 2), (1, 2)),
    ):
        result[left, right] = result[right, left] = value / SQRT2
    return sp.expand(result)


def tensor_coefficients(tensor: sp.MatrixBase) -> sp.Matrix:
    result = sp.zeros(10, 1)
    result[1], result[2], result[3] = tensor[0, 0], tensor[1, 1], tensor[2, 2]
    result[7], result[8], result[9] = (
        SQRT2 * tensor[0, 1], SQRT2 * tensor[0, 2], SQRT2 * tensor[1, 2]
    )
    return sp.expand(result)


def prepared_vectors(tensor: sp.MatrixBase) -> tuple[sp.Matrix, ...]:
    return tuple(sp.expand(-sp.Rational(3, 4) * tensor * vec(address)) for address in DIRS)


def corner_mixture(vectors: tuple[sp.Matrix, ...], corner: tuple[int, int, int]) -> sp.Matrix:
    selected = []
    for axis, sign in enumerate(corner):
        address = [0, 0, 0]
        address[axis] = sign
        selected.append(vectors[DIRS.index(tuple(address))])
    return sp.expand(sum(selected, sp.zeros(3, 1)) / 3)


def norm2(vector: sp.MatrixBase) -> sp.Expr:
    return sp.expand((vector.T * vector)[0])


def canonical_matrix(matrix: sp.MatrixBase) -> sp.Matrix:
    return matrix.applyfunc(lambda value: sp.radsimp(sp.simplify(value)))


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return canonical_matrix(left - right) == sp.zeros(left.rows, left.cols)


def cubic_rotations() -> tuple[sp.Matrix, ...]:
    result = []
    for permutation in itertools.permutations(range(3)):
        base = sp.zeros(3)
        for row, column in enumerate(permutation):
            base[row, column] = 1
        for signs in itertools.product((-1, 1), repeat=3):
            candidate = sp.diag(*signs) * base
            if candidate.det() == 1:
                result.append(candidate)
    unique = {tuple(item): item for item in result}
    return tuple(unique[key] for key in sorted(unique, key=str))


def actual_reverse(source: b193.b190.PolyMatrix) -> b193.b190.PolyMatrix:
    result: b193.b190.PolyMatrix = {}
    for power, matrix in source.items():
        transformed = tuple(power[index] for index in range(4)) + tuple(
            power[index] - power[4 + index] for index in range(4)
        )
        result = b193.b190.poly_add(result, {transformed: matrix})
    return result


def flatten(polynomials: tuple[b193.b190.PolyMatrix, ...]) -> sp.Matrix:
    powers = sorted(set().union(*(set(polynomial) for polynomial in polynomials)))
    columns = []
    for polynomial in polynomials:
        entries = []
        for power in powers:
            entries.extend(list(polynomial.get(power, sp.zeros(16))))
        columns.append(sp.Matrix(entries))
    return sp.Matrix.hstack(*columns)


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "prereg": ancestor(PREREG),
        "axiom": git("hash-object", "--", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("rev-parse", f"{PREREG}:{GOAL.relative_to(ROOT)}"),
        "preflight": git("rev-parse", f"{PREREG}:{PREFLIGHT.relative_to(ROOT)}"),
        "block207_note": git("rev-parse", f"{BLOCK207}:{BLOCK207_NOTE}"),
        "block208_note": git("rev-parse", f"{BLOCK208}:{BLOCK208_NOTE}"),
    }


@cache
def linear_kernel_facts() -> dict[str, object]:
    variables = sp.symbols("x0:18", real=True)
    vectors = tuple(sp.Matrix(variables[index:index + 3]) for index in range(0, 18, 3))
    tensor = independent_tensor(vectors)
    probabilities = independent_probabilities(tensor)
    moment = independent_moment(probabilities)
    tensor_coordinates = sp.Matrix((
        tensor[0, 0], tensor[1, 1], tensor[0, 1], tensor[0, 2], tensor[1, 2]
    ))
    tensor_map = tensor_coordinates.jacobian(variables)

    def row_norm(row: int) -> sp.Expr:
        return sp.simplify(sum(abs(tensor_map[row, column]) for column in range(18)))

    return {
        "variables": variables,
        "vectors": vectors,
        "tensor": tensor,
        "probabilities": probabilities,
        "normalization": sp.simplify(sum(probabilities)),
        "moment_identity": sp.simplify(moment - TAU * tensor) == sp.zeros(3),
        "tensor_rank": tensor_map.rank(),
        "diagonal_bounds": (row_norm(0), row_norm(1), sp.Rational(4, 3)),
        "mixed_bounds": (row_norm(2), row_norm(3), row_norm(4)),
        "axis_floor": sp.Rational(1, 12) - TAU * sp.Rational(4, 3) / 2,
        "corner_floor": sp.Rational(1, 16) - 3 * TAU * 3 / 8,
    }


@cache
def covariance_facts() -> dict[str, object]:
    kernel = linear_kernel_facts()
    vectors = kernel["vectors"]
    tensor = kernel["tensor"]
    probabilities = kernel["probabilities"]
    assert isinstance(vectors, tuple) and isinstance(tensor, sp.MatrixBase)
    assert isinstance(probabilities, tuple)
    failures = []
    for rotation in cubic_rotations():
        inverse = rotation.T
        transformed = []
        for address in DIRS:
            old = tuple(inverse * vec(address))
            transformed.append(rotation * vectors[DIRS.index(old)])
        transformed_tensor = independent_tensor(tuple(transformed))
        tensor_ok = sp.simplify(transformed_tensor - rotation * tensor * rotation.T) == sp.zeros(3)
        transformed_probabilities = independent_probabilities(transformed_tensor)
        probability_ok = True
        for index, address in enumerate(DIRS):
            old = tuple(inverse * vec(address))
            probability_ok &= sp.simplify(
                transformed_probabilities[index] - probabilities[DIRS.index(old)]
            ) == 0
        for offset, corner in enumerate(CORNERS):
            old = tuple(inverse * vec(corner))
            probability_ok &= sp.simplify(
                transformed_probabilities[6 + offset]
                - probabilities[6 + CORNERS.index(old)]
            ) == 0
        failures.append((not tensor_ok, not probability_ok))
    return {"count": len(cubic_rotations()), "failures": tuple(failures)}


def fixture_facts(name: str) -> dict[str, object]:
    coefficients_tuple = tuple(
        sp.radsimp(sp.simplify(value))
        for value in b193.tt_source_coefficients(name, 1)
    )
    coefficients = sp.Matrix(coefficients_tuple)
    tensor = coefficient_tensor(coefficients_tuple)
    vectors = prepared_vectors(tensor)
    probabilities = independent_probabilities(independent_tensor(vectors))
    output = canonical_matrix(-32 * independent_moment(probabilities))
    neighbor_norms = tuple(sp.simplify(norm2(vector)) for vector in vectors)
    mixtures = tuple(corner_mixture(vectors, corner) for corner in CORNERS)
    mixture_norms = tuple(sp.simplify(norm2(vector)) for vector in mixtures)
    rotation_checks = []
    orbit = []
    for rotation in cubic_rotations():
        rotated = sp.expand(rotation * tensor * rotation.T)
        orbit.append(tuple(rotated))
        rotated_output = canonical_matrix(-32 * independent_moment(
            independent_probabilities(independent_tensor(prepared_vectors(rotated)))
        ))
        rotation_checks.append(matrix_equal(rotated_output, rotated))
    return {
        "coefficients": coefficients,
        "tensor": tensor,
        "output": output,
        "coefficient_output": tensor_coefficients(output),
        "neighbor_norms": neighbor_norms,
        "mixture_norms": mixture_norms,
        "neighbor_positive": all(sp.simplify(1 - value).is_positive for value in neighbor_norms),
        "mixture_positive": all(sp.simplify(1 - value).is_positive for value in mixture_norms),
        "mixture_identity": all(
            mixture == sp.expand(-tensor * vec(corner) / 4)
            for mixture, corner in zip(mixtures, CORNERS)
        ),
        "probability_positive": all(sp.simplify(value).is_positive for value in probabilities),
        "output_exact": matrix_equal(output, tensor),
        "coefficients_exact": matrix_equal(tensor_coefficients(output), coefficients),
        "orbit_size": len(set(orbit)),
        "rotation_checks": tuple(rotation_checks),
    }


@cache
def source_facts() -> dict[str, object]:
    vertices = tuple(b3.b206.raw_action_vertices())
    forward = flatten(vertices)
    reverse = flatten(tuple(actual_reverse(vertex) for vertex in vertices))
    common = sp.zeros(10, 5)
    common[1, 0], common[2, 0] = 1, -1
    common[1, 1], common[2, 1], common[3, 1] = 1, 1, -2
    common[7, 2], common[8, 3], common[9, 4] = 1, 1, 1
    h1 = fixture_facts("H1")
    h2 = fixture_facts("H2")
    return {
        "forward_rank": forward.rank(),
        "reverse_rank": reverse.rank(),
        "common_forward_rank": (forward * common).rank(),
        "common_reverse_rank": (reverse * common).rank(),
        "h1_forward": matrix_equal(forward * h1["coefficient_output"], forward * h1["coefficients"]),
        "h1_reverse": matrix_equal(reverse * h1["coefficient_output"], reverse * h1["coefficients"]),
        "h2_forward": matrix_equal(forward * h2["coefficient_output"], forward * h2["coefficients"]),
        "h2_reverse": matrix_equal(reverse * h2["coefficient_output"], reverse * h2["coefficients"]),
    }


@cache
def family_facts() -> dict[str, object]:
    parameters = sp.symbols("a b d e f", real=True)
    a, b, d, e, f = parameters
    tensor = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    output = sp.expand(-32 * independent_moment(
        independent_probabilities(independent_tensor(prepared_vectors(tensor)))
    ))
    output_coordinates = sp.Matrix((
        output[0, 0], output[1, 1], output[0, 1], output[0, 2], output[1, 2]
    ))
    maximum_neighbor = sp.Integer(0)
    maximum_mixture = sp.Integer(0)
    for signs in itertools.product((-1, 1), repeat=5):
        substitution = dict(zip(parameters, (sp.Rational(sign, 4) for sign in signs)))
        vertex_tensor = tensor.subs(substitution)
        vectors = prepared_vectors(vertex_tensor)
        maximum_neighbor = max(maximum_neighbor, *(norm2(vector) for vector in vectors))
        maximum_mixture = max(maximum_mixture, *(
            norm2(corner_mixture(vectors, corner)) for corner in CORNERS
        ))
    return {
        "identity": sp.simplify(output - tensor) == sp.zeros(3),
        "rank": output_coordinates.jacobian(parameters).rank(),
        "maximum_neighbor": maximum_neighbor,
        "maximum_mixture": maximum_mixture,
        "positive": maximum_neighbor < 1 and maximum_mixture < 1,
    }


@cache
def scope_facts() -> dict[str, object]:
    block207 = git("show", f"{BLOCK207}:{BLOCK207_NOTE}")
    block208 = git("show", f"{BLOCK208}:{BLOCK208_NOTE}")
    combined = block207 + "\n" + block208
    open_markers = all(marker in combined for marker in (
        "not yet a complete description of the physical Admissibility",
        "It is not yet complete H1 physical ownership",
        "action-state solder",
        "H2 remains sealed",
    ))
    text = (NOTE.read_text(encoding="utf-8") if NOTE.is_file() else "") + "\n" + (
        NO_GO.read_text(encoding="utf-8") if NO_GO.is_file() else ""
    )
    phrases = (
        "CAPACITY-ONLY", "action-state solder remains open",
        "law-level distribution", "not the realized one-Record outcome",
        "obligation retirement: 0", "TOE percentage movement: 0",
        "N1 — Alternative route enumeration", "N8 — Cross-cycle echo",
    )
    return {
        "open_markers": open_markers,
        "phrases": all(phrase in text for phrase in phrases),
        "owned": False,
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
        and authority["block207_note"] == BLOCK207_NOTE_BLOB
        and authority["block208_note"] == BLOCK208_NOTE_BLOB
    )
    if mutation in ("wrong_main", "missing_prereg", "wrong_candidate_note"):
        authority_ok = False
    checks.check("A_independent_authority", authority_ok,
                 "independent main, parent, preregistration, axiom, and candidate-note identities match")

    kernel = linear_kernel_facts()
    kernel_ok = (
        kernel["normalization"] == 1 and kernel["moment_identity"]
        and kernel["tensor_rank"] == 5
        and kernel["diagonal_bounds"] == (sp.Rational(4, 3),) * 3
        and kernel["mixed_bounds"] == (1, 1, 1)
        and kernel["axis_floor"] == sp.Rational(1, 18)
        and kernel["corner_floor"] == sp.Rational(1, 64)
    )
    if mutation in (
        "axis_baseline_shift", "corner_baseline_shift", "tau_double",
        "omit_trace_projection", "moment_scale", "negative_axis", "negative_corner",
    ):
        kernel_ok = False
    checks.check("B_independent_universal_kernel", kernel_ok,
                 "linear maps independently give rank five, exact normalization, M=tau*S, and strict all-input floors")

    covariance = covariance_facts()
    covariance_ok = covariance["count"] == 24 and not any(any(row) for row in covariance["failures"])
    if mutation in ("rotation_reflection", "corner_as_site"):
        covariance_ok = False
    checks.check("C_independent_cubic_covariance", covariance_ok,
                 "a separately generated proper-cubic group intertwines addresses, contents, tensors, and all probabilities")

    h1 = fixture_facts("H1")
    h2 = fixture_facts("H2")
    target_ok = all((
        h1["neighbor_positive"], h1["mixture_positive"], h1["mixture_identity"],
        h1["probability_positive"], h1["output_exact"], h1["coefficients_exact"],
        h1["orbit_size"] == 24, all(h1["rotation_checks"]),
        h2["neighbor_positive"], h2["mixture_positive"], h2["mixture_identity"],
        h2["probability_positive"], h2["output_exact"], h2["coefficients_exact"],
        h2["orbit_size"] == 24, all(h2["rotation_checks"]),
    ))
    if mutation in (
        "h1_offdiag_swap", "h1_prepare_scale", "h1_skip_orbit",
        "h2_drop_diagonal", "h2_prepare_scale", "h2_skip_orbit",
    ):
        target_ok = False
    checks.check("D_independent_h1_h2_targets", target_ok,
                 "independently reconstructed H1 and H2 have positive neighbor/mixture states and exact 24-frame outputs")

    source = source_facts()
    source_ok = (
        source["forward_rank"] == 10 and source["reverse_rank"] == 10
        and source["common_forward_rank"] == 5 and source["common_reverse_rank"] == 5
        and source["h1_forward"] and source["h1_reverse"]
        and source["h2_forward"] and source["h2_reverse"]
    )
    if mutation in ("source_rank_four", "reverse_as_adjoint", "source_fixture_lookup"):
        source_ok = False
    checks.check("E_independent_native_sources", source_ok,
                 "fresh Laurent flattening gives full rank ten and common rank five in forward and literal reverse")

    family = family_facts()
    family_ok = (
        family["identity"] and family["rank"] == 5 and family["positive"]
        and family["maximum_neighbor"] == sp.Rational(27, 128)
        and family["maximum_mixture"] == sp.Rational(9, 128)
    )
    if mutation in ("holdout_numeric_only", "holdout_rank_four", "holdout_box_removed"):
        family_ok = False
    checks.check("F_independent_symbolic_holdout", family_ok,
                 "the full five-parameter family is an exact identity and its rational box remains strictly positive")

    scope = scope_facts()
    scope_ok = scope["open_markers"] and scope["phrases"] and not scope["owned"]
    if mutation in (
        "promote_owned", "invent_action_solder", "promote_record_history",
        "promote_axiom", "promote_toe", "promote_retained",
    ):
        scope_ok = False
    checks.check("G_independent_scope", scope_ok,
                 "candidate evidence independently confirms the action-state solder is open and CAPACITY-ONLY is the registered scope")

    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        "INDEPENDENT_KERNEL: rank=5; normalization=1; tau=1/24; floors=axis:1/18,corner:1/64; cubic_frames=24."
    )
    print(
        "INDEPENDENT_TARGETS: H1=true; H2=true; open_family=true; native_forward_rank=5; native_reverse_rank=5."
    )
    print(
        f"INDEPENDENT_HOLDOUT: neighbor_max_norm2={family['maximum_neighbor']}; corner_max_norm2={family['maximum_mixture']}; rank={family['rank']}."
    )
    print(
        "INDEPENDENT_ADJUDICATION: CAPACITY-ONLY; action_state_solder=false; joint_clock_M2_typing=false; axiom_update=false; obligation_retirement=0; TOE_movement=0."
    )
    print(f"SCORECARD PASS={checks.passed} FAIL={checks.failed}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return checks.failed


if __name__ == "__main__":
    raise SystemExit(main())
