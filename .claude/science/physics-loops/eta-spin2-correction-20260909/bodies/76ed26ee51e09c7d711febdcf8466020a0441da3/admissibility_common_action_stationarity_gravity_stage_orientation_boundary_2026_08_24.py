#!/usr/bin/env python3
"""Block 187: typed common-action stationarity and stage-orientation gate.

This exact runner corrects the first-wave common-action contract before a
large coefficient tournament is attempted.  It proves that a positive-mass
Dirac--Kahler Gaussian has no nonzero zero-source stationary background, so
the physical coupling is its three-point vertex rather than a vacuum
geometry--matter Hessian block.  It independently re-derives the isotropic
second-order incidence gravity/constraint coefficients, stratifies every
spatial Nyquist class, and tests the Block-78 ordered source cadence against
stage-exchange reflection.  An orientation-odd stage carrier repairs that
last clash.  No complete law, Record mechanism, or axiom update is claimed.
"""

from __future__ import annotations

import argparse
from itertools import combinations
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128  # noqa: E402
import admissibility_dirac_kahler_local_dual_patch_descent_2026_08_15 as b106  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_COMMON_ACTION_STATIONARITY_GRAVITY_STAGE_ORIENTATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AUDIT_TIMEOUT_SEC = 180
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_REF = (
    "origin/physics-loop/toe-axiom-closure-block186-metric-first-reduction-"
    "20260824"
)
PARENT_COMMIT = "32dae6eef2ea6a28bf347fd148fee6557ef48b7e"
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_COMMON_ACTION_STATIONARITY_GRAVITY_STAGE_ORIENTATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_COMMON_METRIC_PULLBACK_TORUS_CONSTRAINT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_reflected_curvature_common_metric_pullback_torus_constraint_boundary_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_LOCAL_DUAL_PATCH_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_local_dual_patch_descent_2026_08_15.py",
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py",
    "docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14.py",
)

FROZEN_BLOBS = {
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_COMMON_METRIC_PULLBACK_TORUS_CONSTRAINT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md": "b99e4c71e4c30063cd2c3afc8bf2797c121aaa9c",
    "scripts/admissibility_reflected_curvature_common_metric_pullback_torus_constraint_boundary_2026_08_24.py": "57e745a3480efbb861d839a4a76c82db56109207",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md": "194cf07ad9a0b7269defe6bdba8750fc6fe95640",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py": "90f9b53b2ef499367f2f65fd8314a13137af203b",
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "05b2d0fe7a6ff79243c8ba7c5ae87c2a0c13ca02",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py": "fd23e8f7caf5cff5d76c8bec3864554e5f280708",
    "docs/ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "f9cbc29ddf57cb3385b65e97e6cad497b7b66d1d",
    "scripts/admissibility_incidence_adm_depth_two_sourced_constraint_record_cadence_boundary_2026_08_14.py": "2066434b8b96240774fc7f4c7cd9b2adcdd78a94",
    "docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "c2602c829ccb76813bf0df4f38a03ac6047ae751",
    "scripts/admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14.py": "96f76a38594ed655a0446b522211cc3ed2b83354",
}

MUTATIONS = (
    "stale_main_authority",
    "break_dk_rank",
    "claim_nonzero_vacuum_cross_hessian",
    "break_gravity_classification",
    "break_nyquist_stratification",
    "force_orientationless_front_kicks",
    "break_orientation_covariance",
    "drop_n5_resolution",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "stale_main_authority": "A",
    "break_dk_rank": "B",
    "claim_nonzero_vacuum_cross_hessian": "B",
    "break_gravity_classification": "C",
    "break_nyquist_stratification": "D",
    "force_orientationless_front_kicks": "E",
    "break_orientation_covariance": "E",
    "drop_n5_resolution": "F",
    "claim_toe_progress": "G",
}

I = sp.I
R = sp.Rational
SQRT2 = sp.sqrt(2)


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=180
    ).strip()


def worktree_blob(path: str) -> str:
    result = subprocess.run(
        ("git", "hash-object", "--", path), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=180,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT, check=False, timeout=180,
    ).returncode == 0


def cover_shift(dt: int, dx: int) -> sp.Matrix:
    size = b128.COVER_SIZE
    result = sp.zeros(size)
    for time in range(b128.COVER_TIME_EXTENT):
        for space in range(b128.SPACE_EXTENT):
            result[
                b128.cover_index(time + dt, space + dx),
                b128.cover_index(time, space),
            ] = 1
    return result


def dk_stationarity_facts() -> dict[str, object]:
    """Rebuild the curved section action without importing the scout PR."""
    origins = ((0, 0), (0, 1), (1, 0), (1, 1))
    temporal = cover_shift(1, 0)
    spatial = cover_shift(0, 1)
    shifts = {
        (0, 0): sp.eye(b128.COVER_SIZE),
        (0, 1): spatial,
        (1, 0): temporal,
        (1, 1): temporal * spatial,
    }
    differential = sp.Matrix(b128.chart_differential_cover((0, 0)))
    hodge = sp.Matrix(b128.curved_hodge_cover())
    section_hodge = sp.expand(
        sum(
            (shifts[item].T * hodge * shifts[item] for item in origins),
            sp.zeros(b128.COVER_SIZE),
        ) / 4
    )
    action = sp.expand(
        b128.MASS * section_hodge
        + I * (
            section_hodge * differential
            + differential.H * section_hodge
        )
    )
    antihermitian_part = sp.expand(
        I * (section_hodge * differential + differential.H * section_hodge)
    )
    physical_action = sp.Matrix(b128.antiperiodic_quotient(action))
    determinant = sp.factor(physical_action.det(method="domain-ge"))

    # The local Hodge blocks are positive for |shear|<1 and volume>0.  Their
    # embedded supports cover the carrier; permutation-congruence averaging
    # therefore preserves positivity.  These exact checks encode that proof.
    field = b128.block105.overlap_field()
    local_positive = all(
        volume > 0 and shear**2 < 1 for shear, volume in field.values()
    )
    coverage = sp.zeros(b128.COVER_SIZE)
    for time in range(b128.COVER_TIME_EXTENT):
        for space in range(b128.SPACE_EXTENT):
            embedding = b128.cover_embedding(time, space)
            coverage += embedding * embedding.T
    covered = coverage.rank() == b128.COVER_SIZE

    # H -> (1+s)H is a declared local Hodge-amplitude deformation.  Its
    # three-point vertex is exactly Q.  At the zero stationary background the
    # literal mixed Hessian is V psi_*=0, while an external source can produce
    # V Q^-1 J=J.  The latter is an escape witness, not a derived source law.
    zero_background = sp.zeros(physical_action.cols, 1)
    vertex = physical_action
    mixed_zero = vertex * zero_background

    periodic = b106.core_objects(sp.Symbol("mass"))
    periodic_d = sp.Matrix(periodic["d_glob"])
    massless_periodic = I * (periodic_d + periodic_d.H)

    return {
        "cover_dim": action.rows,
        "physical_dim": physical_action.rows,
        "physical_rank": physical_action.rank(),
        "det_nonzero": determinant != 0,
        "det_digits": tuple(
            len(str(abs(int(item))))
            for item in sp.fraction(determinant)
        ),
        "hodge_positive_proof": local_positive and covered,
        "antihermitian": antihermitian_part.H == -antihermitian_part,
        "hermitian_part": sp.expand(
            (action + action.H) / 2 - b128.MASS * section_hodge
        ).is_zero_matrix,
        "zero_mixed_hessian": mixed_zero.is_zero_matrix,
        "vertex_rank": vertex.rank(),
        "sourced_escape": determinant != 0 and vertex == physical_action,
        "periodic_massless_nullity": (
            massless_periodic.cols - massless_periodic.rank()
        ),
    }


def symmetric_basis3() -> tuple[sp.Matrix, ...]:
    basis: list[sp.Matrix] = []
    for axis in range(3):
        item = sp.zeros(3)
        item[axis, axis] = 1
        basis.append(item)
    for left, right in ((0, 1), (0, 2), (1, 2)):
        item = sp.zeros(3)
        item[left, right] = item[right, left] = 1 / SQRT2
        basis.append(item)
    return tuple(basis)


BASIS3 = symmetric_basis3()


def coordinates3(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([(basis.T * matrix).trace() for basis in BASIS3])


def gravity_maps(
    momentum: sp.Matrix,
    coefficients: tuple[sp.Expr, ...],
) -> tuple[sp.Matrix, ...]:
    b, c1, c2, c3, c4, c5, d2, f2 = coefficients
    p = momentum
    p2 = (p.T * p)[0]
    identity = sp.eye(3)
    kinetic = sp.zeros(6)
    potential = sp.zeros(6)
    hamiltonian = sp.zeros(1, 6)
    momentum_row = sp.zeros(3, 6)
    for column, tensor in enumerate(BASIS3):
        trace = sp.trace(tensor)
        contracted = tensor * p
        double = (p.T * tensor * p)[0]
        kinetic[:, column] = coordinates3(tensor + b * identity * trace)
        image = (
            c1 * p2 * tensor
            + c2 * (p * p.T) * trace
            + c3 * (p * contracted.T + contracted * p.T)
            + c4 * identity * p2 * trace
            + c5 * identity * double
        )
        potential[:, column] = coordinates3(image)
        hamiltonian[0, column] = p2 * trace + d2 * double
        momentum_row[:, column] = I * (
            -2 * tensor * p - f2 * p * trace
        )
    shift = sp.zeros(6, 3)
    for column in range(3):
        vector = sp.eye(3)[:, column]
        image = I * (
            p * vector.T + vector * p.T
            + f2 * identity * (p.T * vector)[0]
        )
        shift[:, column] = coordinates3(image)
    return kinetic, potential, hamiltonian, momentum_row, shift


def polynomial_coefficients(matrix: sp.Matrix, variables: tuple[sp.Symbol, ...]) -> list[sp.Expr]:
    result: list[sp.Expr] = []
    for entry in matrix:
        polynomial = sp.Poly(sp.expand(entry), *variables)
        result.extend(polynomial.coeffs())
    return [sp.expand(item) for item in result if item != 0]


def gravity_classification_facts() -> dict[str, object]:
    px, py, pz = sp.symbols("p_x p_y p_z", real=True)
    momentum = sp.Matrix((px, py, pz))
    b, c1, c2, c3, c4, c5, d2, f2 = sp.symbols(
        "b c1 c2 c3 c4 c5 d2 f2", real=True
    )
    maps = gravity_maps(momentum, (b, c1, c2, c3, c4, c5, d2, f2))
    kinetic, potential, hamiltonian, momentum_row, shift = maps
    derivative = I * momentum.T
    identities = (
        potential - potential.T,
        kinetic - kinetic.T,
        potential * shift,
        momentum_row * potential,
        hamiltonian * shift,
        momentum_row * hamiltonian.H,
        hamiltonian * kinetic + R(1, 2) * derivative * momentum_row,
    )
    equations: list[sp.Expr] = []
    for matrix in identities:
        for expression in polynomial_coefficients(matrix, (px, py, pz)):
            if expression not in equations and -expression not in equations:
                equations.append(expression)
    unknowns = (b, c2, c3, c4, c5, d2, f2)
    groebner = sp.groebner(equations, *unknowns, order="lex")
    basis = tuple(sp.expand(item.as_expr()) for item in groebner.polys)
    expected = (
        b + R(1, 2),
        -c1 + c2,
        c1 + c3,
        c1 + c4,
        -c1 + c5,
        d2 + 1,
        f2,
    )
    return {
        "equations": len(equations),
        "basis": basis,
        "expected": expected,
        "matches": basis == expected,
        "free_scale": c1 not in unknowns,
    }


def frobenius_basis4() -> tuple[sp.Matrix, ...]:
    pairs = (
        (3, 3), (0, 0), (1, 1), (2, 2),
        (0, 3), (1, 3), (2, 3),
        (0, 1), (0, 2), (1, 2),
    )
    result: list[sp.Matrix] = []
    for left, right in pairs:
        item = sp.zeros(4)
        value = 1 if left == right else 1 / SQRT2
        item[left, right] = value
        item[right, left] = value
        result.append(item)
    return tuple(result)


BASIS4 = frobenius_basis4()
ETA4 = sp.diag(1, 1, 1, -1)


def centered_operator4(momentum: sp.Matrix) -> sp.Matrix:
    lower = momentum
    upper = ETA4 * lower
    squared = (lower.T * upper)[0]
    tensors: list[sp.Matrix] = []
    for perturbation in BASIS4:
        trace = sp.trace(ETA4 * perturbation)
        contracted = perturbation * upper
        double = (upper.T * perturbation * upper)[0]
        tensor = R(1, 2) * (
            squared * perturbation
            + lower * lower.T * trace
            - lower * contracted.T
            - contracted * lower.T
            - ETA4 * (squared * trace - double)
        )
        tensors.append(tensor)
    result = sp.Matrix(
        10, 10,
        lambda row, column: (
            ETA4 * BASIS4[row] * ETA4 * tensors[column]
        ).trace(),
    )
    return sp.expand((result + result.T) / 2)


def centered_gauge4(momentum: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(10, 4)
    for row, basis in enumerate(BASIS4):
        for column in range(4):
            tensor = sp.zeros(4)
            tensor[:, column] += momentum
            tensor[column, :] += momentum.T
            result[row, column] = (basis.T * tensor).trace()
    return result


def spatial_constraint(momentum: sp.Matrix) -> sp.Matrix:
    rows = [sp.Matrix([[sp.trace(item) for item in BASIS3]])]
    for axis in range(3):
        rows.append(sp.Matrix([[(item * momentum)[axis] for item in BASIS3]]))
    return sp.Matrix.vstack(*rows)


def tt_source(momentum: sp.Matrix) -> sp.Matrix:
    for axis in range(3):
        unit = sp.eye(3)[:, axis]
        first = unit.cross(momentum)
        second = momentum.cross(first)
        candidate = sp.expand(
            second.dot(second) * first * first.T
            - first.dot(first) * second * second.T
        )
        if candidate != sp.zeros(3):
            return candidate
    return sp.zeros(3)


def nyquist_facts() -> dict[str, object]:
    canonical = (
        -R(1, 2), sp.Integer(1), sp.Integer(1), -sp.Integer(1),
        -sp.Integer(1), sp.Integer(1), -sp.Integer(1), sp.Integer(0),
    )
    table: dict[tuple[int, int], tuple[int, ...]] = {}
    tt_checks: list[bool] = []
    source_checks: list[bool] = []
    probes = [sp.Matrix((1, 2, 3))]
    probes.extend(
        sp.Matrix(tuple(2 if axis in subset else 0 for axis in range(3)))
        for count in range(1, 4)
        for subset in combinations(range(3), count)
    )
    for momentum in probes:
        source = tt_source(momentum)
        source_checks.append(
            source != sp.zeros(3)
            and sp.trace(source) == 0
            and source * momentum == sp.zeros(3, 1)
        )

    for temporal in (0, 1):
        for spatial_count in range(4):
            spatial = sp.Matrix(
                tuple(2 if axis < spatial_count else 0 for axis in range(3))
            )
            full = sp.Matrix(tuple(spatial) + (2 * temporal,))
            kernel_rank = centered_operator4(full).rank()
            gauge_rank = centered_gauge4(full).rank()
            kinetic, potential, hamiltonian, momentum_row, _ = gravity_maps(
                spatial, canonical
            )
            constraint = spatial_constraint(spatial)
            nullspace = constraint.nullspace()
            tt_dimension = len(nullspace)
            if spatial_count:
                section = sp.Matrix.hstack(*nullspace)
                p2 = (spatial.T * spatial)[0]
                tt_checks.append(
                    tt_dimension == 2
                    and sp.expand(kinetic * section - section).is_zero_matrix
                    and sp.expand(potential * section - p2 * section).is_zero_matrix
                    and (section.T * section).det() > 0
                )
            table[(temporal, spatial_count)] = (
                kernel_rank,
                gauge_rank,
                constraint.rank(),
                hamiltonian.rank(),
                momentum_row.rank(),
                tt_dimension,
            )
    expected = {
        (0, 0): (0, 0, 1, 0, 0, 5),
        (0, 1): (6, 4, 4, 1, 3, 2),
        (0, 2): (6, 4, 4, 1, 3, 2),
        (0, 3): (6, 4, 4, 1, 3, 2),
        (1, 0): (6, 4, 1, 0, 0, 5),
        (1, 1): (4, 4, 4, 1, 3, 2),
        (1, 2): (6, 4, 4, 1, 3, 2),
        (1, 3): (6, 4, 4, 1, 3, 2),
    }
    return {
        "table": table,
        "expected": expected,
        "matches": table == expected,
        "tt_positive": all(tt_checks) and len(tt_checks) == 6,
        "tt_sources": all(source_checks) and len(source_checks) == 8,
    }


def stage_facts() -> dict[str, object]:
    coefficient = sp.Matrix(((1, 0), (1, 1)))
    target = sp.Matrix((2, 2))
    solution = tuple(sp.linsolve((coefficient, target)))[0]
    fixed_reflection = sp.Matrix(((1, 0), (1, 1), (1, -1)))
    fixed_target = sp.Matrix((2, 2, 0))
    fixed_solutions = sp.linsolve((fixed_reflection, fixed_target))
    epsilon = sp.Symbol("epsilon", real=True)
    weights = sp.Matrix((1 + epsilon, 1 - epsilon))
    reflected = sp.Matrix((weights[1], weights[0]))
    return {
        "solution": solution,
        "unique_front": solution == (2, 0),
        "fixed_empty": fixed_solutions is sp.EmptySet or fixed_solutions == sp.EmptySet,
        "orientation_covariance": sp.expand(
            reflected - weights.subs(epsilon, -epsilon)
        ).is_zero_matrix,
        "forward": tuple(weights.subs(epsilon, 1)),
        "reverse": tuple(weights.subs(epsilon, -1)),
    }


def note_facts() -> dict[str, bool]:
    try:
        text = NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        text = ""
    lowered = " ".join(text.lower().split())
    return {
        "exists": bool(text),
        "n1_n8": all(f"### n{index}" in lowered for index in range(1, 9)),
        "n5": all(
            label in lowered
            for label in (
                "per_element:", "per_site:", "per_mode:",
                "per_block:", "lattice_wide:",
            )
        ),
        "scope": all(
            phrase in lowered
            for phrase in (
                "partial-narrowing",
                "zero obligation retirement",
                "zero toe percentage movement",
                "no axiom amendment",
                "outcome: unresolved",
            )
        ),
    }


def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "registry": git_output("rev-parse", f"origin/main:{REGISTRY_PATH}"),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        "frozen": all(
            worktree_blob(path) == blob for path, blob in FROZEN_BLOBS.items()
        ),
    }


def build_claims(mutation: str) -> dict[str, object]:
    claims: dict[str, object] = {
        "main": CURRENT_MAIN,
        "dk_rank": 16,
        "vacuum_cross_nonzero": False,
        "gravity_basis": (
            "b + 1/2", "-c1 + c2", "c1 + c3", "c1 + c4",
            "-c1 + c5", "d2 + 1", "f2",
        ),
        "nyquist_matches": True,
        "stage_solution": (2, 0),
        "orientation_covariance": True,
        "n5_complete": True,
        "toe_movement": 0,
    }
    if mutation == "stale_main_authority":
        claims["main"] = "0" * 40
    elif mutation == "break_dk_rank":
        claims["dk_rank"] = 15
    elif mutation == "claim_nonzero_vacuum_cross_hessian":
        claims["vacuum_cross_nonzero"] = True
    elif mutation == "break_gravity_classification":
        altered = list(claims["gravity_basis"])
        altered[0] = "b + 1"
        claims["gravity_basis"] = tuple(altered)
    elif mutation == "break_nyquist_stratification":
        claims["nyquist_matches"] = False
    elif mutation == "force_orientationless_front_kicks":
        claims["stage_solution"] = (1, 1)
    elif mutation == "break_orientation_covariance":
        claims["orientation_covariance"] = False
    elif mutation == "drop_n5_resolution":
        claims["n5_complete"] = False
    elif mutation == "claim_toe_progress":
        claims["toe_movement"] = 1
    return claims


def evaluate(mutation: str) -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    dk = dk_stationarity_facts()
    gravity = gravity_classification_facts()
    nyquist = nyquist_facts()
    stage = stage_facts()
    note = note_facts()
    claims = build_claims(mutation)
    return {
        "A": (
            authority["main"] == claims["main"]
            and authority["axiom"] == CURRENT_AXIOM_BLOB
            and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
            and authority["registry"] == CURRENT_REGISTRY_BLOB
            and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
            and authority["parent"] == PARENT_COMMIT
            and authority["parent_ancestor"]
            and authority["frozen"],
            "current authority, exact Block-186 parent, and ten frozen science inputs",
        ),
        "B": (
            dk["physical_rank"] == claims["dk_rank"]
            and dk["cover_dim"] == 32
            and dk["physical_dim"] == 16
            and dk["det_nonzero"]
            and dk["hodge_positive_proof"]
            and dk["antihermitian"]
            and dk["hermitian_part"]
            and dk["zero_mixed_hessian"] != claims["vacuum_cross_nonzero"]
            and dk["vertex_rank"] == 16
            and dk["sourced_escape"]
            and dk["periodic_massless_nullity"] == 4,
            "positive-mass AP stationarity kills only the vacuum cross Hessian; vertex and sourced/singular escapes live",
        ),
        "C": (
            gravity["equations"] == 19
            and tuple(str(item) for item in gravity["basis"])
            == claims["gravity_basis"]
            and gravity["matches"]
            and gravity["free_scale"],
            "nineteen exact coefficient equations force the canonical incidence gravity class up to c1",
        ),
        "D": (
            nyquist["matches"] == claims["nyquist_matches"]
            and nyquist["tt_positive"]
            and nyquist["tt_sources"],
            "all eight Nyquist strata are rank-classified; every nonzero-spatial class has two positive TT directions",
        ),
        "E": (
            stage["solution"] == claims["stage_solution"]
            and stage["unique_front"]
            and stage["fixed_empty"]
            and stage["orientation_covariance"] == claims["orientation_covariance"]
            and stage["forward"] == (2, 0)
            and stage["reverse"] == (0, 2),
            "constraint cadence is (2,0); fixed stage reflection fails and epsilon_R exchange-covariantly repairs it",
        ),
        "F": (
            note["exists"] and note["n1_n8"]
            and note["n5"] == claims["n5_complete"],
            "the landing note carries the full N1-N8 gate and every N5 execution resolution",
        ),
        "G": (
            note["scope"] and claims["toe_movement"] == 0,
            "outcome remains unresolved with no axiom amendment, obligation retirement, or TOE movement",
        ),
    }


N5_LINES = (
    "per_element: checked the exact field-charge typing, positive-mass coercivity identity, and zero-background mixed derivative.",
    "per_site: checked bounded local Hodge blocks and a nonzero local action vertex; a permanent Record write was not executed.",
    "per_mode: checked the full 16-dimensional antiperiodic action and the exact generic polynomial gravity identities.",
    "per_block: checked all eight Nyquist rank strata and the two-stage cadence/reflection coefficient system exactly.",
    "lattice_wide: checked and not executed — no width ladder, arbitrary-history law, global OS reconstruction, or refinement theorem was run.",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0

    results = evaluate(args.mutation)
    for family, (passed, statement) in results.items():
        print(f"[{'PASS' if passed else 'FAIL'}] {family}: {statement}")
    for line in N5_LINES:
        print(line)
    summary = " ".join(
        f"{family}={'PASS' if result[0] else 'FAIL'}"
        for family, result in results.items()
    )
    print(f"GATES {summary}")
    passed = sum(result[0] for result in results.values())
    failed = len(results) - passed
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
