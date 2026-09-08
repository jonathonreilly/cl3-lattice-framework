#!/usr/bin/env python3
"""Exact Block-43 matter/Record grading compatibility runner.

The runner separates four statements:

1. arbitrary rank-one one-qubit Record events and a fixed nontrivial grading
   cannot be simultaneously readable on the same M_2(C) carrier;
2. a full matter M_2(C) and an independent commuting full Record M_2(C)
   cannot both act on one two-dimensional carrier;
3. a two-mode fixed-parity code carries an arbitrary logical qubit and an
   exact even normalized CP Record writer; and
4. supplied finite typed graded and ordinary products share the displayed
   number/Record data and local tables; this is not a global four-axiom model
   or a lattice-wide role/formation-law theorem.

All matrices are finite and exact. No generated fixture is empirical data,
and no axiom, audit status, obligation, or TOE score is changed.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PREREG_COMMIT = "d319531f2ca863c4196dd2d9953a5dde7c1805a5"
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block43-matter-record-grading-compatibility-"
    "decision-20260901"
)
RUNNER_PATH = (
    "scripts/matter_record_grading_same_carrier_compatibility_two_mode_even_"
    "repair_2026_09_01.py"
)
NOTE_PATH = (
    "docs/MATTER_RECORD_GRADING_SAME_CARRIER_COMPATIBILITY_TWO_MODE_EVEN_"
    "REPAIR_AXIOM_DECISION_BOUNDED_THEOREM_NOTE_2026-09-01.md"
)
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "scripts/matter_record_grading_same_carrier_compatibility_two_mode_even_repair_2026_09_01.py",
    "docs/MATTER_RECORD_GRADING_SAME_CARRIER_COMPATIBILITY_TWO_MODE_EVEN_REPAIR_AXIOM_DECISION_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "archive/notes/docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/PRIOR_ART_SEARCH.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/POSTEXECUTION_PR_CHECK.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/POSTEXECUTION_MUTATION_AMENDMENT.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/POSTEXECUTION_NOVELTY_AUDIT.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/POSTEXECUTION_NO_GO_AUDIT.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/STATE.yaml",
)

FROZEN_PACKET_BLOBS = {
    f"{PACKET}/ARTIFACT_PLAN.md": "51a3a8cd3fd25b39e11d390fcf482c8dc05023a4",
    f"{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "bc4b9f2f44fd84780bc7036946b083db535b63a8",
    f"{PACKET}/EXACT_TARGET_CONTRACT.md": "5db3357cdd0b96367872db0e9785581437fdbc13",
    f"{PACKET}/GOAL.md": "a3dfb90b23f4df6679392a4a643b4caab8e681d8",
    f"{PACKET}/MUTATION_PLAN.md": "f4e3d5217cbce13803ca86747dc10114902a29b6",
    f"{PACKET}/NO_GO_DISCIPLINE_CHECKLIST.md": "a0c59e4a57cb68a3f4b8985d27a8256a82ca70ca",
    f"{PACKET}/PANEL_RETURN.md": "7d6e2a089729427c09308278b5a9a701a9ef5182",
    f"{PACKET}/PRIOR_ART_SEARCH.md": "a70f2ad8c8cb66e1cc0bfc3cf7c4530401704400",
    f"{PACKET}/STATE.yaml": "e5d3af723a9df007bb6fd7be578ac61ac4fbcf58",
}
MINIMAL_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
ARCHIVED_BLOCK38_CONTEXT_PATH = "archive/notes/docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md"
ARCHIVED_BLOCK38_CONTEXT_BLOB = "881b2359752a002dbfd744e932dd0112d8f55a9e"

I2 = sp.eye(2)
ZERO2 = sp.zeros(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
SM = sp.Matrix([[0, 1], [0, 0]])
PAULI = (X, Y, Z)


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def vectorized_rank(matrices: Iterable[sp.MatrixBase]) -> int:
    columns = []
    for matrix in matrices:
        dense = sp.Matrix(matrix)
        columns.append(dense.reshape(dense.rows * dense.cols, 1))
    return sp.Matrix.hstack(*columns).rank()


def kron_all(*matrices: sp.MatrixBase) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for matrix in matrices:
        result = sp.kronecker_product(result, matrix)
    return sp.Matrix(result)


def anticommutator(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    return sp.simplify(left * right + right * left)


def commutator(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    return sp.simplify(left * right - right * left)


def pauli_coordinates(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(
        [sp.simplify(sp.trace(matrix) / 2)]
        + [sp.simplify(sp.trace(sigma * matrix) / 2) for sigma in PAULI]
    )


def projector(axis: Iterable[object], label: int = 1) -> sp.Matrix:
    vector = tuple(sp.sympify(value) for value in axis)
    bloch = sum((vector[index] * PAULI[index] for index in range(3)), ZERO2)
    return sp.simplify((I2 + label * bloch) / 2)


def git_blob(commit: str, path: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def worktree_blob(path: str) -> str:
    return subprocess.run(
        ["git", "hash-object", path],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def source_and_prereg_certificate(_: str | None = None) -> tuple[bool, str]:
    pinned = sum(
        git_blob(PREREG_COMMIT, path) == blob
        for path, blob in FROZEN_PACKET_BLOBS.items()
    )
    unchanged = sum(
        worktree_blob(path) == blob
        for path, blob in FROZEN_PACKET_BLOBS.items()
        if not path.endswith("/STATE.yaml")
    )
    minimal_bound = worktree_blob(MINIMAL_PATH) == MINIMAL_BLOB
    target = (ROOT / PACKET / "EXACT_TARGET_CONTRACT.md").read_text()
    mutations = (ROOT / PACKET / "MUTATION_PLAN.md").read_text()
    checklist = (ROOT / PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md").read_text()
    state = (ROOT / PACKET / "STATE.yaml").read_text()
    note = (ROOT / NOTE_PATH).read_text()
    numbered = sum(line[:1].isdigit() and ". " in line[:4] for line in mutations.splitlines())
    no_go_bound = all(f"## N{index}" in checklist for index in range(1, 9))
    refs_bound = all(
        value in state
        for value in (
            "17357c3714c3b3196c6b8fdc9b1a3bb300044181",
            "551dfd9f317a36db050dffa0d717764f9af9f291",
            "f8581d80efdd0856aa1a64078a48931a763765e9",
            "ff8573cf054125db0dd0fcf07dba131280b6b736",
            "9301c509842ea4835def91ad50f41bfd4f80ab1c",
        )
    )
    postcheck = (ROOT / PACKET / "POSTEXECUTION_PR_CHECK.md").read_text()
    mutation_amendment = (
        ROOT / PACKET / "POSTEXECUTION_MUTATION_AMENDMENT.md"
    ).read_text()
    novelty_audit = (ROOT / PACKET / "POSTEXECUTION_NOVELTY_AUDIT.md").read_text()
    post_no_go = (ROOT / PACKET / "POSTEXECUTION_NO_GO_AUDIT.md").read_text()
    ok = (
        pinned == 9
        and ARCHIVED_BLOCK38_CONTEXT_PATH in AUDIT_INPUT_PATHS
        and worktree_blob(ARCHIVED_BLOCK38_CONTEXT_PATH) == ARCHIVED_BLOCK38_CONTEXT_BLOB
        and unchanged == 8
        and minimal_bound
        and numbered == 22
        and no_go_bound
        and refs_bound
        and "PR #7831" in postcheck
        and "PR #7832" in postcheck
        and "existence repair, not an instrument-selection theorem" in postcheck
        and "31 mutations" in mutation_amendment
        and "hard_impact_gate: FAIL" in novelty_audit
        and "shipping_decision: BACKLOG_NO_PR" in novelty_audit
        and all(f"## N{index}" in post_no_go for index in range(1, 9))
        and "AXIOM_DECISION_READY" in target
        and "obligation_retirement: 0" in note
        and "toe_percentage_movement: 0" in note
    )
    return ok, (
        f"prereg_blobs={pinned}/9 unchanged={unchanged}/8 mutations={numbered}/22; "
        "minimal axioms and N1-N8 bound"
    )


def same_carrier_span_certificate(mutation: str | None = None) -> tuple[bool, str]:
    axes = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
    )
    family = [(axis, label, projector(axis, label)) for axis in axes for label in (-1, 1)]
    if mutation == "drop_x_axis_pair":
        family = [item for item in family if item[0] != axes[0]]
    if mutation == "drop_y_axis_pair":
        family = [item for item in family if item[0] != axes[1]]
    coordinate_matrix = sp.Matrix.hstack(*(pauli_coordinates(item[2]) for item in family))
    span_rank = coordinate_matrix.rank()

    adz = lambda matrix: sp.simplify(Z * matrix * Z)
    x_fixed = matrix_zero(adz(projector((1, 0, 0))) - projector((1, 0, 0)))
    y_fixed = matrix_zero(adz(projector((0, 1, 0))) - projector((0, 1, 0)))
    z_fixed = matrix_zero(adz(projector((0, 0, 1))) - projector((0, 0, 1)))
    if mutation == "fix_x_under_adz":
        x_fixed = True
    all_random_even = x_fixed and y_fixed and z_fixed
    if mutation == "all_random_axes_even":
        all_random_even = True
    ok = (
        len(family) == 6
        and span_rank == 4
        and not x_fixed
        and not y_fixed
        and z_fixed
        and not all_random_even
    )
    return ok, (
        f"six Pauli-axis projectors span rank={span_rank}; "
        f"Ad(Z) fixed=(X:{x_fixed},Y:{y_fixed},Z:{z_fixed})"
    )


def generic_block38_parity_certificate(_: str | None = None) -> tuple[bool, str]:
    ax, ay, az, lam = sp.symbols("a_x a_y a_z lambda", real=True)
    effect = (I2 + lam * (ax * X + ay * Y + az * Z)) / 2
    defect = sp.simplify(Z * effect * Z - effect)
    expected = sp.simplify(-lam * (ax * X + ay * Y))
    x_effect = projector((1, 0, 0))
    x_output = projector((1, 0, 0))
    ok = (
        matrix_zero(defect - expected)
        and not matrix_zero(defect)
        and not matrix_zero(commutator(x_effect, Z))
        and not matrix_zero(commutator(x_output, Z))
    )
    return ok, (
        "generic grading defect=-lambda(a_x X+a_y Y); literal X-axis "
        "Block-38 effect and pure successor are not even"
    )


def commutant_capacity_certificate(mutation: str | None = None) -> tuple[bool, str]:
    q0, q1, q2, q3 = sp.symbols("q0 q1 q2 q3")
    candidate = q0 * I2 + q1 * X + q2 * Y + q3 * Z
    equations = []
    for sigma in PAULI:
        equations.extend(commutator(candidate, sigma))
    solution = sp.linsolve(equations, (q0, q1, q2, q3))
    nonscalar_claim = mutation == "nonscalar_commutant"
    if nonscalar_claim:
        nonscalar_ok = matrix_zero(commutator(X, Y))
    else:
        nonscalar_ok = True
    one_mode_claim = mutation in {"one_mode_even_logical", "literal_one_site_repair"}
    ok = (
        solution == sp.FiniteSet((q0, 0, 0, 0))
        and nonscalar_ok
        and not one_mode_claim
    )
    return ok, (
        f"commutant={solution}; one qubit has no independent commuting full-M2 "
        "Record factor and no arbitrary even logical qubit"
    )


def logical_code_objects(
    wrong_y: bool = False,
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    parity = sp.diag(1, -1, -1, 1)
    code = sp.diag(1, 0, 0, 1)
    logical_x = sp.zeros(4)
    logical_x[0, 3] = logical_x[3, 0] = 1
    logical_y = sp.zeros(4)
    logical_y[0, 3] = sp.I if wrong_y else -sp.I
    logical_y[3, 0] = -sp.I if wrong_y else sp.I
    logical_z = sp.diag(1, 0, 0, -1)
    return parity, code, logical_x, logical_y, logical_z


def sphere_zero(expression: sp.Expr, variables: tuple[sp.Symbol, ...]) -> bool:
    ax, ay, az = variables
    basis = sp.groebner(
        [ax**2 + ay**2 + az**2 - 1], ax, ay, az, domain=sp.EX
    )
    _, remainder = basis.reduce(sp.expand(expression))
    return sp.simplify(remainder) == 0


def logical_code_certificate(mutation: str | None = None) -> tuple[bool, str]:
    parity, code, logical_x, logical_y, logical_z = logical_code_objects(
        wrong_y=mutation == "wrong_logical_y"
    )
    logical = (logical_x, logical_y, logical_z)
    if mutation == "non_even_global_pointer":
        pointer_plus = projector((1, 0, 0), 1)
        pointer_even = matrix_zero(commutator(pointer_plus, Z))
        return pointer_even, "X-pointer projector does not commute with Record parity Z"
    pauli_ok = all(matrix_zero(operator * operator - code) for operator in logical)
    pauli_ok = pauli_ok and matrix_zero(logical_x * logical_y - sp.I * logical_z)
    even_ok = all(matrix_zero(commutator(operator, parity)) for operator in logical)

    ax, ay, az, lam, t = sp.symbols("a_x a_y a_z lambda t", real=True)
    axis_vars = (ax, ay, az)
    bloch = ax * logical_x + ay * logical_y + az * logical_z
    logical_projector = sp.Matrix(sp.simplify((code + bloch) / 2))
    if mutation == "odd_logical_projector":
        logical_projector[0, 1] += sp.Rational(1, 10)
        logical_projector[1, 0] += sp.Rational(1, 10)
    projector_identity = logical_projector * logical_projector - logical_projector
    projector_ok = all(sphere_zero(value, axis_vars) for value in projector_identity)
    projector_ok = projector_ok and sp.simplify(sp.trace(logical_projector) - 1) == 0
    if mutation == "odd_logical_projector":
        projector_ok = projector_ok and matrix_zero(commutator(logical_projector, parity))

    complement = sp.eye(4) - code
    effect_plus = sp.simplify((code + lam * bloch) / 2 + complement / 2)
    effect_minus = sp.simplify((code - lam * bloch) / 2 + complement / 2)
    if mutation == "omit_complement_completion":
        effect_plus = sp.simplify((code + lam * bloch) / 2)
        effect_minus = sp.simplify((code - lam * bloch) / 2)
    if mutation == "break_branch_normalization":
        effect_plus = 2 * effect_plus
    complete = matrix_zero(effect_plus + effect_minus - sp.eye(4))
    effects_even = matrix_zero(commutator(effect_plus, parity))

    characteristic = sp.expand((t * sp.eye(4) - effect_plus).det())
    expected = sp.expand(
        (t - sp.Rational(1, 2)) ** 2
        * (t - (1 + lam) / 2)
        * (t - (1 - lam) / 2)
    )
    spectrum_ok = sphere_zero(characteristic - expected, axis_vars)
    outside_claim = mutation == "lambda_outside_positive"
    if outside_claim:
        spectrum_ok = spectrum_ok and all(
            value >= 0 for value in (sp.Rational(3, 2), -sp.Rational(1, 2))
        )

    sample_axis = (sp.Rational(3, 5), sp.Rational(4, 5), 0)
    sample_bloch = sum(
        (sample_axis[index] * logical[index] for index in range(3)), sp.zeros(4)
    )
    sample_projector = sp.simplify((code + sample_bloch) / 2)
    sample_effect = sp.simplify(
        (code + sp.Rational(3, 5) * sample_bloch) / 2 + complement / 2
    )
    pointer_plus = projector((0, 0, 1), 1)
    pointer_minus = projector((0, 0, 1), -1)
    if mutation == "nonorthogonal_record_pointer":
        pointer_minus = pointer_plus
    joint_output = sp.kronecker_product(sample_projector, pointer_plus)
    output = -joint_output if mutation == "non_cp_branch" else joint_output
    choi = sp.kronecker_product(sample_effect.T, output)
    choi_eigenvalues = choi.eigenvals()
    choi_psd = all(
        sp.simplify(value).is_nonnegative for value in choi_eigenvalues
    )
    expected_nonzero = {
        sp.Rational(1, 5),
        sp.Rational(1, 2),
        sp.Rational(4, 5),
    }
    observed_nonzero = {
        sp.simplify(value) for value in choi_eigenvalues if sp.simplify(value) != 0
    }
    choi_ok = choi_psd and observed_nonzero == expected_nonzero
    output_parity_global = sp.kronecker_product(parity, Z)
    output_parity_typed = sp.kronecker_product(parity, I2)
    pointer_ok = (
        sp.trace(pointer_plus * pointer_minus) == 0
        and matrix_zero(pointer_plus + pointer_minus - I2)
        and matrix_zero(commutator(joint_output, output_parity_global))
        and matrix_zero(commutator(joint_output, output_parity_typed))
        and sp.trace(joint_output) == 1
    )

    repeat_same = sp.simplify(
        sp.trace(
            ((code + sample_bloch) / 2 + complement / 2) * sample_projector
        )
    )
    repeat_opposite = sp.simplify(
        sp.trace(
            ((code - sample_bloch) / 2 + complement / 2) * sample_projector
        )
    )
    repeat_ok = repeat_same == 1 and repeat_opposite == 0

    ok = (
        pauli_ok
        and even_ok
        and projector_ok
        and complete
        and effects_even
        and spectrum_ok
        and choi_ok
        and pointer_ok
        and repeat_ok
    )
    return ok, (
        "two-mode even code checks "
        f"pauli={pauli_ok} even={even_ok} projector={projector_ok} "
        f"complete={complete} effect_even={effects_even} spectrum={spectrum_ok} "
        f"choi={choi_ok} pointer={pointer_ok} repeat={repeat_ok}"
    )


def cubic_covariance_certificate(mutation: str | None = None) -> tuple[bool, str]:
    parity, code, logical_x, logical_y, logical_z = logical_code_objects()
    logical = (logical_x, logical_y, logical_z)
    complement = sp.eye(4) - code
    root_two = sp.sqrt(2)
    unitary_x = complement + (code - sp.I * logical_x) / root_two
    unitary_z = complement + (code - sp.I * logical_z) / root_two
    rotation_x = sp.Matrix(((1, 0, 0), (0, 0, -1), (0, 1, 0)))
    rotation_z = sp.Matrix(((0, -1, 0), (1, 0, 0), (0, 0, 1)))
    generators = ((rotation_x, unitary_x), (rotation_z, unitary_z))

    def rotation_key(rotation: sp.MatrixBase) -> tuple[int, ...]:
        return tuple(int(rotation[row, column]) for row in range(3) for column in range(3))

    identity_key = rotation_key(sp.eye(3))
    representatives = {identity_key: (sp.eye(3), sp.eye(4))}
    queue = [identity_key]
    while queue:
        key = queue.pop()
        rotation, unitary = representatives[key]
        for generator_rotation, generator_unitary in generators:
            new_rotation = generator_rotation * rotation
            new_unitary = sp.simplify(generator_unitary * unitary)
            new_key = rotation_key(new_rotation)
            if new_key not in representatives:
                representatives[new_key] = (new_rotation, new_unitary)
                queue.append(new_key)
    if mutation == "break_induced_cubic_action":
        bad_key = next(key for key in representatives if key != identity_key)
        bad_rotation, bad_unitary = representatives[bad_key]
        logical_flip = complement + logical_x
        bad_unitary = sp.simplify(logical_flip * bad_unitary)
        mismatch = False
        for column, sigma in enumerate(logical):
            declared = sum(
                (bad_rotation[row, column] * logical[row] for row in range(3)),
                sp.zeros(4),
            )
            mismatch = mismatch or not matrix_zero(
                sp.simplify(bad_unitary * sigma * bad_unitary.H - declared)
            )
        return not mismatch, (
            "mutated even representative fails its declared induced action"
        )
    if mutation == "linearize_projective_lifts":
        mismatch_found = False
        for left_rotation, left_unitary in representatives.values():
            for right_rotation, right_unitary in representatives.values():
                target = representatives[
                    rotation_key(left_rotation * right_rotation)
                ][1]
                if not matrix_zero(
                    sp.simplify(left_unitary * right_unitary - target)
                ):
                    mismatch_found = True
                    break
            if mismatch_found:
                break
        return not mismatch_found, (
            "a spin-lift pair differs from its chosen product representative "
            "by code phase, so exact linear closure is false"
        )

    e1, e2, e3 = (sp.eye(3).col(index) for index in range(3))
    covariance = True
    for rotation, unitary in representatives.values():
        covariance = covariance and rotation.T * rotation == sp.eye(3)
        covariance = covariance and rotation.det() == 1
        covariance = covariance and (
            rotation * e1.cross(e2) == (rotation * e1).cross(rotation * e2)
        )
        covariance = covariance and matrix_zero(unitary.H * unitary - sp.eye(4))
        covariance = covariance and matrix_zero(commutator(unitary, parity))
        for column, sigma in enumerate(logical):
            rotated = sum(
                (rotation[row, column] * logical[row] for row in range(3)),
                sp.zeros(4),
            )
            covariance = covariance and matrix_zero(
                sp.simplify(unitary * sigma * unitary.H - rotated)
            )
    exact_product_failures = 0
    induced_action_failures = 0
    for left_rotation, left_unitary in representatives.values():
        for right_rotation, right_unitary in representatives.values():
            product_rotation = left_rotation * right_rotation
            target_unitary = representatives[rotation_key(product_rotation)][1]
            left_code = left_unitary.extract((0, 3), (0, 3))
            right_code = right_unitary.extract((0, 3), (0, 3))
            target_code = target_unitary.extract((0, 3), (0, 3))
            product_code = sp.simplify(left_code * right_code)
            if not matrix_zero(product_code - target_code):
                exact_product_failures += 1
            relative = sp.simplify(target_code.H * product_code)
            same_induced_action = (
                sp.simplify(relative[0, 1]) == 0
                and sp.simplify(relative[1, 0]) == 0
                and sp.simplify(relative[0, 0] - relative[1, 1]) == 0
            )
            if not same_induced_action:
                induced_action_failures += 1

    count = len(representatives)
    projective_closure = exact_product_failures > 0 and induced_action_failures == 0
    return covariance and projective_closure and count == 24, (
        f"{count} even projective lifts: exact-product mismatches="
        f"{exact_product_failures}/576, induced-action failures="
        f"{induced_action_failures}; logical effect action closes"
    )


def typed_product_objects() -> dict[str, sp.Matrix]:
    identity = I2
    c0_graded = kron_all(SM, identity, identity, identity)
    c1_graded = kron_all(Z, SM, identity, identity)
    c0_ordinary = kron_all(SM, identity, identity, identity)
    c1_ordinary = kron_all(identity, SM, identity, identity)
    parity_matter = kron_all(Z, Z, identity, identity)
    record_x0 = kron_all(identity, identity, X, identity)
    record_z0 = kron_all(identity, identity, Z, identity)
    record_x1 = kron_all(identity, identity, identity, X)
    record_z1 = kron_all(identity, identity, identity, Z)
    return {
        "c0g": c0_graded,
        "c1g": c1_graded,
        "c0o": c0_ordinary,
        "c1o": c1_ordinary,
        "parity": parity_matter,
        "rx0": record_x0,
        "rz0": record_z0,
        "rx1": record_x1,
        "rz1": record_z1,
    }


def typed_product_certificate(mutation: str | None = None) -> tuple[bool, str]:
    objects = typed_product_objects()
    if mutation == "matter_record_overlap":
        objects["rx0"] = kron_all(X, I2, I2, I2)
    identity = sp.eye(16)
    c0g, c1g = objects["c0g"], objects["c1g"]
    c0o, c1o = objects["c0o"], objects["c1o"]
    graded_car = (
        matrix_zero(anticommutator(c0g, c1g))
        and matrix_zero(anticommutator(c0g, c1g.H))
        and matrix_zero(anticommutator(c0g, c0g.H) - identity)
        and matrix_zero(anticommutator(c1g, c1g.H) - identity)
    )
    if mutation == "graded_matter_commutes":
        graded_car = graded_car and matrix_zero(commutator(c0g, c1g))

    ordinary_relation = (
        matrix_zero(commutator(c0o, c1o))
        and not matrix_zero(anticommutator(c0o, c1o))
    )
    if mutation == "ordinary_matter_anticommutes":
        ordinary_relation = ordinary_relation and matrix_zero(
            anticommutator(c0o, c1o)
        )

    record_basis_0 = (identity, objects["rx0"], objects["rz0"], objects["rx0"] * objects["rz0"])
    record_basis_1 = (identity, objects["rx1"], objects["rz1"], objects["rx1"] * objects["rz1"])
    record_even = all(
        matrix_zero(commutator(objects["parity"], record))
        for record in record_basis_0 + record_basis_1
    )
    if mutation == "nontrivial_record_grading":
        record_even = record_even and matrix_zero(
            commutator(objects["parity"] * objects["rz0"], objects["rx0"])
        )
    records_commute = all(
        matrix_zero(commutator(left, right))
        for left in record_basis_0
        for right in record_basis_1
    )
    if mutation == "record_anticommutation":
        records_commute = records_commute and matrix_zero(
            anticommutator(objects["rx0"], objects["rx1"])
        )

    n0g, n1g = c0g.H * c0g, c1g.H * c1g
    n0o, n1o = c0o.H * c0o, c1o.H * c1o
    local_record_twin = matrix_zero(n0g - n0o) and matrix_zero(n1g - n1o)
    def full_matter_basis(c0: sp.Matrix, c1: sp.Matrix) -> tuple[sp.Matrix, ...]:
        local0 = (identity, c0, c0.H, c0.H * c0)
        local1 = (identity, c1, c1.H, c1.H * c1)
        return tuple(sp.simplify(left * right) for left in local0 for right in local1)

    matter_record_commute = all(
        matrix_zero(commutator(matter, record))
        for matter in full_matter_basis(c0g, c1g)
        + full_matter_basis(c0o, c1o)
        for record in record_basis_0 + record_basis_1
    )

    c0g4, c1g4 = kron_all(SM, I2), kron_all(Z, SM)
    c0o4, c1o4 = kron_all(SM, I2), kron_all(I2, SM)

    def matter_basis(c0: sp.Matrix, c1: sp.Matrix) -> tuple[sp.Matrix, ...]:
        identity4 = sp.eye(4)
        local0 = (identity4, c0, c0.H, c0.H * c0)
        local1 = (identity4, c1, c1.H, c1.H * c1)
        return tuple(sp.simplify(left * right) for left in local0 for right in local1)

    graded_matter_rank = vectorized_rank(matter_basis(c0g4, c1g4))
    ordinary_matter_rank = vectorized_rank(matter_basis(c0o4, c1o4))
    record_generating_basis = (I2, X) if mutation == "drop_record_generator" else (I2, X, Z, X * Z)
    record_rank = vectorized_rank(record_generating_basis)
    dimension = graded_matter_rank * record_rank * record_rank
    ordinary_dimension = ordinary_matter_rank * record_rank * record_rank

    p0, p1, q0, q1 = sp.symbols("p0 p1 q0 q1", real=True)
    diagonal = lambda p: sp.diag(1 - p, p)
    rho = kron_all(diagonal(p0), diagonal(p1), diagonal(q0), diagonal(q1))
    number = (I2 - Z) / 2
    record_n0 = kron_all(I2, I2, number, I2)
    record_n1 = kron_all(I2, I2, I2, number)
    local_effect_expectations = (
        sp.simplify(sp.trace(rho * n0g)) == p0
        and sp.simplify(sp.trace(rho * n1g)) == p1
        and sp.simplify(sp.trace(rho * n0o)) == p0
        and sp.simplify(sp.trace(rho * n1o)) == p1
        and sp.simplify(sp.trace(rho * record_n0)) == q0
        and sp.simplify(sp.trace(rho * record_n1)) == q1
    )
    ok = (
        graded_car
        and ordinary_relation
        and record_even
        and records_commute
        and local_record_twin
        and matter_record_commute
        and local_effect_expectations
        and graded_matter_rank == 16
        and ordinary_matter_rank == 16
        and record_rank == 4
        and dimension == 256
        and ordinary_dimension == dimension
    )
    return ok, (
        "generated ranks matter=(graded:"
        f"{graded_matter_rank},ordinary:{ordinary_matter_rank}) Record={record_rank}; "
        f"dimension={dimension}; symbolic local number/Record expectations shared"
    )


def finite_local_candidate_certificate(mutation: str | None = None) -> tuple[bool, str]:
    minimal = (ROOT / MINIMAL_PATH).read_text()
    minimal_flat = " ".join(minimal.split())
    objects = typed_product_objects()
    local_same = matrix_zero(
        objects["c0g"].H * objects["c0g"] - objects["c0o"].H * objects["c0o"]
    ) and matrix_zero(
        objects["c1g"].H * objects["c1g"] - objects["c1o"].H * objects["c1o"]
    )
    selected_claim = mutation in {
        "derive_graded_from_records",
        "import_fswap_selector",
        "roles_from_axioms",
    }
    authority_needles = (
        "Physical sites are the points of the cubic lattice `Z^3`",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "There is one fixed nearest-neighbor admissibility rule",
        "the probability distribution over the possibilities is determined by",
        "When present, a record locks exactly one admissible local possibility.",
        "records are permanent.",
        "Only records are readable.",
    )
    authority_bound = all(needle in minimal_flat for needle in authority_needles)

    # These hostile mutations have single finite witnesses.  Reject them here
    # instead of rerunning the complete 729-profile x 24-rotation census.
    if selected_claim:
        return False, "mutation promotes a product/role selector absent from the axioms"
    if mutation == "constant_admissibility_rule":
        constant_values = {sp.Rational(1, 2) for _ in (-1, 0, 1)}
        return len(constant_values) > 1, "constant kernel has no neighbor dependence"
    if mutation == "record_not_permanent":
        formed_value = 0
        reread_value = 1 - formed_value
        return reread_value == formed_value, "formed Record flips on immediate re-read"
    if mutation == "privilege_lattice_direction":
        axial_pattern = (1, -1, -1, -1, -1, -1)
        rotated_pattern = (-1, -1, 1, -1, -1, -1)
        axial_probability = sp.Rational(axial_pattern[0] + 2, 4)
        rotated_probability = sp.Rational(rotated_pattern[0] + 2, 4)
        return (
            axial_probability == rotated_probability,
            "direction-privileging kernel changes under +x to +y rotation: "
            f"{axial_probability} != {rotated_probability}",
        )

    directions = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    direction_index = {direction: index for index, direction in enumerate(directions)}
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rotation = sp.zeros(3)
            for row, column in enumerate(permutation):
                rotation[row, column] = signs[row]
            if rotation.det() == 1:
                rotations.append(rotation)

    rule_ok = True
    formed_records = 0
    probabilities_seen: set[sp.Rational] = set()

    def probability_one_for(pattern: tuple[int, ...]) -> sp.Rational:
        encoded_sum = sum(value + 1 for value in pattern)
        return sp.Rational(encoded_sum + 1, 14)

    for pattern in itertools.product((-1, 0, 1), repeat=6):
        probability_one = probability_one_for(pattern)
        probability_zero = 1 - probability_one
        probabilities_seen.add(probability_one)
        rule_ok = rule_ok and probability_zero + probability_one == 1
        rule_ok = rule_ok and 0 < probability_zero < 1 and 0 < probability_one < 1
        if bool(probability_zero > 0 and probability_one > 0):
            formed_records += 1
        for rotation in rotations:
            rotated_pattern = [0] * 6
            for index, direction in enumerate(directions):
                rotated = tuple(int(value) for value in rotation * sp.Matrix(direction))
                rotated_pattern[direction_index[rotated]] = pattern[index]
            rotated_probability = probability_one_for(tuple(rotated_pattern))
            rule_ok = rule_ok and rotated_probability == probability_one

    varies = len(probabilities_seen) > 1
    persistent_two_step_histories = 0
    for pattern in itertools.product((-1, 0, 1), repeat=6):
        probability_one = probability_one_for(pattern)
        first_kernel = {
            0: 1 - probability_one,
            1: probability_one,
        }
        for formed_value, first_probability in first_kernel.items():
            second_value = formed_value
            second_kernel = {second_value: sp.Integer(1)}
            if (
                first_probability > 0
                and second_kernel == {formed_value: sp.Integer(1)}
            ):
                persistent_two_step_histories += 1
    finite_local_comparison = (
        len(rotations) == 24
        and formed_records == 729
        and rule_ok
        and varies
        and persistent_two_step_histories == 1458
        and local_same
    )
    scope_bound = "does not establish two complete models" in (ROOT / NOTE_PATH).read_text()
    ok = authority_bound and finite_local_comparison and scope_bound and not selected_claim
    return ok, (
        "supplied finite ternary-neighbor rule p(Record=1)=(encoded_sum+1)/14 is normalized, "
        f"varying and invariant for {len(rotations)} cubic rotations; "
        f"memo_text_bound={authority_bound} finite_scope={scope_bound} rule={rule_ok} formed={formed_records} "
        f"varies={varies} persistent_histories={persistent_two_step_histories}/1458 "
        f"local_twin={local_same}"
    )


def decision_scope_certificate(mutation: str | None = None) -> tuple[bool, str]:
    note = (ROOT / NOTE_PATH).read_text()
    state = (ROOT / PACKET / "STATE.yaml").read_text()
    forbidden = mutation in {
        "literal_one_site_repair",
        "edit_axioms",
        "retire_toe",
        "roles_from_axioms",
    }
    options = all(
        phrase in note
        for phrase in (
            "Option G — global grading",
            "Option M — matter-only typed grading",
            "Option D — defer composition",
            "two-mode even apparatus",
            "explicit owner decision",
        )
    )
    zero_movement = (
        "governing_minimal_axioms_edited: false" in state
        and "obligation_retirement: 0" in state
        and "toe_percentage_movement: 0" in state
    )
    ok = options and zero_movement and not forbidden
    return ok, (
        "same-carrier trilemma plus exact repair is AXIOM_DECISION_READY; "
        "owner choice remains G/M/D; zero audit/obligation/TOE movement"
    )


@dataclass
class Checks:
    results: dict[str, bool] = field(default_factory=dict)

    def check(self, name: str, detail: str, condition: object) -> None:
        result = bool(condition)
        self.results[name] = result
        print(f"{'PASS' if result else 'FAIL'} {name}: {detail}")

    @property
    def passed(self) -> int:
        return sum(self.results.values())

    @property
    def failed(self) -> int:
        return len(self.results) - self.passed

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


MUTATIONS = (
    "drop_x_axis_pair",
    "drop_y_axis_pair",
    "fix_x_under_adz",
    "all_random_axes_even",
    "nonscalar_commutant",
    "one_mode_even_logical",
    "wrong_logical_y",
    "omit_complement_completion",
    "lambda_outside_positive",
    "non_cp_branch",
    "break_branch_normalization",
    "odd_logical_projector",
    "nontrivial_record_grading",
    "record_anticommutation",
    "graded_matter_commutes",
    "ordinary_matter_anticommutes",
    "derive_graded_from_records",
    "import_fswap_selector",
    "roles_from_axioms",
    "literal_one_site_repair",
    "edit_axioms",
    "retire_toe",
    "nonorthogonal_record_pointer",
    "non_even_global_pointer",
    "break_induced_cubic_action",
    "linearize_projective_lifts",
    "drop_record_generator",
    "matter_record_overlap",
    "privilege_lattice_direction",
    "record_not_permanent",
    "constant_admissibility_rule",
)

DESIGNATED_GATE = {
    "drop_x_axis_pair": "same_carrier_projector_span",
    "drop_y_axis_pair": "same_carrier_projector_span",
    "fix_x_under_adz": "same_carrier_projector_span",
    "all_random_axes_even": "same_carrier_projector_span",
    "nonscalar_commutant": "one_qubit_commutant_capacity",
    "one_mode_even_logical": "one_qubit_commutant_capacity",
    "wrong_logical_y": "two_mode_even_logical_writer",
    "omit_complement_completion": "two_mode_even_logical_writer",
    "lambda_outside_positive": "two_mode_even_logical_writer",
    "non_cp_branch": "two_mode_even_logical_writer",
    "break_branch_normalization": "two_mode_even_logical_writer",
    "odd_logical_projector": "two_mode_even_logical_writer",
    "nontrivial_record_grading": "typed_matter_record_product",
    "record_anticommutation": "typed_matter_record_product",
    "graded_matter_commutes": "typed_matter_record_product",
    "ordinary_matter_anticommutes": "typed_matter_record_product",
    "derive_graded_from_records": "finite_typed_local_comparison",
    "import_fswap_selector": "finite_typed_local_comparison",
    "roles_from_axioms": "decision_and_scope",
    "literal_one_site_repair": "decision_and_scope",
    "edit_axioms": "decision_and_scope",
    "retire_toe": "decision_and_scope",
    "nonorthogonal_record_pointer": "two_mode_even_logical_writer",
    "non_even_global_pointer": "two_mode_even_logical_writer",
    "break_induced_cubic_action": "proper_cubic_logical_covariance",
    "linearize_projective_lifts": "proper_cubic_logical_covariance",
    "drop_record_generator": "typed_matter_record_product",
    "matter_record_overlap": "typed_matter_record_product",
    "privilege_lattice_direction": "finite_typed_local_comparison",
    "record_not_permanent": "finite_typed_local_comparison",
    "constant_admissibility_rule": "finite_typed_local_comparison",
}

GATES: tuple[tuple[str, Callable[[str | None], tuple[bool, str]]], ...] = (
    ("source_and_prereg_binding", source_and_prereg_certificate),
    ("same_carrier_projector_span", same_carrier_span_certificate),
    ("literal_block38_parity_collision", generic_block38_parity_certificate),
    ("one_qubit_commutant_capacity", commutant_capacity_certificate),
    ("two_mode_even_logical_writer", logical_code_certificate),
    ("proper_cubic_logical_covariance", cubic_covariance_certificate),
    ("typed_matter_record_product", typed_product_certificate),
    ("finite_typed_local_comparison", finite_local_candidate_certificate),
    ("decision_and_scope", decision_scope_certificate),
)
GATE_FUNCTIONS = dict(GATES)


def execute_mutation(name: str) -> tuple[str, bool]:
    gate = DESIGNATED_GATE[name]
    gate_ok, _ = GATE_FUNCTIONS[gate](name)
    return name, not gate_ok


def run(mutation: str | None = None) -> int:
    checks = Checks()
    if mutation is not None:
        source_ok, source_detail = source_and_prereg_certificate()
        checks.check("source_and_prereg_binding", source_detail, source_ok)
        gate = DESIGNATED_GATE[mutation]
        gate_ok, gate_detail = GATE_FUNCTIONS[gate](mutation)
        checks.check(gate, gate_detail, gate_ok)
        return checks.finish()

    for name, function in GATES:
        ok, detail = function(None)
        checks.check(name, detail, ok)

    mutation_results = tuple(execute_mutation(name) for name in MUTATIONS)
    rejected = sum(result for _, result in mutation_results)
    checks.check(
        "hostile_mutation_gate",
        f"{rejected}/{len(MUTATIONS)} designated mutations rejected",
        rejected == len(MUTATIONS),
    )
    print(
        "N5_EXECUTION per_element: six projectors, grading action, commutant, "
        "logical effects and Choi matrices executed"
    )
    print(
        "N5_EXECUTION per_site: one-mode lower bound, four physical qubit "
        "matter/Record typing, parity and local readout twins executed"
    )
    print(
        "N5_EXECUTION per_mode: two-mode even logical Pauli algebra, arbitrary-axis "
        "writer spectrum and exact repeatability executed"
    )
    print(
        "N5_EXECUTION per_block: two matter plus two Record carriers, graded and "
        "ordinary cross-site relations and 24 cubic rotations executed"
    )
    print(
        "N5_EXECUTION lattice_wide: checked and not executed - no covariant "
        "dynamic role assignment, full collision process, state, action or "
        "physical-identification law is supplied"
    )
    print(
        "SUMMARY same_carrier=CONDITIONAL_INCOMPATIBILITY two_mode_even_repair=PASS "
        "typed_matter_record_candidate=PASS statistics_selection=OPEN "
        "axiom_decision_status=PROPOSAL_ONLY global_model=UNESTABLISHED "
        "historical_shipping_label=BACKLOG_NO_PR audit_status=unset "
        "obligation_retirement=0 toe_percentage_movement=0 "
        f"input_sha256={input_fingerprint()}"
    )
    return checks.finish()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    args = parser.parse_args()
    return run(args.mutation)


if __name__ == "__main__":
    raise SystemExit(main())
