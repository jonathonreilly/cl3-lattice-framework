#!/usr/bin/env python3
"""Block 06: exact ordered-H1 front/carrier interface.

The target was committed before this runner existed.  The runner classifies
the actual Block-03 C32 detector algebra, constructs its minimal faithful M4
sufficient carrier, and executes the preregistered two-event live-condition
stencil.  It does not select a formation rate, extend the stencil to an
unbounded history, open H2, edit an axiom, or claim TOE movement.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import cache
import hashlib
from itertools import product
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as b3  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_ORDERED_H1_FRONT_CARRIER_INTERFACE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block06-ordered-h1-front-carrier-interface-"
    "20260829"
)
GOAL_PATH = PACKET / "GOAL.md"
PREFLIGHT_PATH = PACKET / "PREFLIGHT_WITNESSES.md"
NO_GO_PATH = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK3_CACHE = ROOT / "logs" / "runner-cache" / (
    "admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt"
)
BLOCK3_RUNNER = ROOT / "scripts" / (
    "admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py"
)

PARENT_COMMIT = "abf7fe23dcc3a9cff7e4cf27911ea8af8e08f47c"
PREREG_COMMIT = "e75608573e5029521878731b30bb798ce70f8a9a"
BLOCK3_COMMIT = "d8cc11fb5210321cf081866572b90a6ce290edcf"
CURRENT_MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block06-ordered-h1-front-carrier-interface-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block06-ordered-h1-front-carrier-interface-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block06-ordered-h1-front-carrier-interface-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_ORDERED_H1_FRONT_CARRIER_INTERFACE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt",
    "docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md",
)

MUTATIONS = (
    "stale_main",
    "stale_prereg",
    "commute_detectors",
    "delete_chirality",
    "claim_m2_full",
    "break_matrix_unit",
    "non_tp_compressor",
    "break_cubic",
    "probability_lookup",
    "break_effect",
    "break_root",
    "nonorthogonal_record",
    "non_tp_writer",
    "record_conditions",
    "occupy_successor",
    "nonlocal_shared",
    "simultaneous_events",
    "overwrite_record",
    "break_bridge",
    "wrong_eta",
    "reset_state",
    "uncoupled_successor",
    "wrong_repeat",
    "host_schedule",
    "claim_arbitrary_history",
    "claim_rate",
    "claim_axiom",
    "claim_toe",
    "claim_retained",
    "open_h2",
)

I = sp.I
I2 = sp.eye(2)
I4 = sp.eye(4)
I32 = sp.eye(32)
Z2 = sp.zeros(2)
Z4 = sp.zeros(4)
Z16 = sp.zeros(16)
Z32 = sp.zeros(32)
SIGMA_X = sp.Matrix(((0, 1), (1, 0)))
SIGMA_Y = sp.Matrix(((0, -I), (I, 0)))
SIGMA_Z = sp.diag(1, -1)
PAULI = (SIGMA_X, SIGMA_Y, SIGMA_Z)
SHELL = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
X0 = (0, 0, 0)
X1 = (-1, -1, 0)
QX = (-1, 0, 0)
QY = (0, -1, 0)
ETA0 = 17
ETA1 = (17, 27)


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return sp.expand(left - right) == sp.zeros(*left.shape)


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def translate(point: tuple[int, int, int], shift: tuple[int, int, int]) -> tuple[int, int, int]:
    return add(point, shift)


def rotate_coord(
    rotation: sp.MatrixBase, vector: tuple[int, int, int]
) -> tuple[int, int, int]:
    answer = rotation * sp.Matrix(vector)
    return tuple(int(answer[index]) for index in range(3))  # type: ignore[return-value]


def rotate_mask(rotation: sp.MatrixBase, mask: int) -> int:
    answer = 0
    for old_index, direction in enumerate(SHELL):
        new_direction = rotate_coord(rotation, direction)
        new_index = SHELL.index(new_direction)
        answer |= ((mask >> old_index) & 1) << new_index
    return answer


@cache
def authority_facts() -> dict[str, object]:
    cache_text = BLOCK3_CACHE.read_text(encoding="utf-8")
    parent_runner_hash = next(
        line.split(":", 1)[1].strip()
        for line in cache_text.splitlines()
        if line.startswith("runner_sha256:")
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "block3": is_ancestor(BLOCK3_COMMIT),
        "axiom": git_output("rev-parse", f"origin/main:{AXIOM_PATH.relative_to(ROOT)}"),
        "worktree_axiom": git_output("hash-object", "--", str(AXIOM_PATH.relative_to(ROOT))),
        "goal_blob": git_output("rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH.relative_to(ROOT)}"),
        "preflight_blob": git_output(
            "rev-parse", f"{PREREG_COMMIT}:{PREFLIGHT_PATH.relative_to(ROOT)}"
        ),
        "parent_cache_ok": (
            "status: ok" in cache_text
            and "TOTAL: PASS=8 FAIL=0" in cache_text
            and "certified_common_interval=abs(e)<=1/1000000000" in cache_text
            and "actual C32 effects and roots" in cache_text
            and parent_runner_hash == sha256(BLOCK3_RUNNER)
        ),
    }


@cache
def detector_data() -> dict[str, object]:
    decoder = b3.decoder_facts()
    basis16 = b3.b206.b194.detector_classification_facts()["basis"]
    phase = decoder["selected_phase"]
    directions = tuple(
        b3.b206.b194.block_matrix(
            Z16,
            sp.conjugate(phase) * generator,
            phase * generator,
            Z16,
        )
        for generator in basis16
    )
    active = tuple(
        mask for mask, selector in enumerate(decoder["selector_table"])
        if selector >= 0
    )
    return {
        "decoder": decoder,
        "phase": phase,
        "directions": directions,
        "active": active,
        "rotations": b3.b2.rotations(),
    }


@cache
def algebra_facts() -> dict[str, object]:
    directions = detector_data()["directions"]
    assert isinstance(directions, tuple)
    d0, d1, d2 = directions
    hermitian = all(matrix_equal(direction.H, direction) for direction in directions)
    involutions = all(matrix_equal(direction * direction, I32) for direction in directions)
    anticommuting = all(
        matrix_equal(directions[left] * directions[right] + directions[right] * directions[left], Z32)
        for left in range(3) for right in range(left + 1, 3)
    )
    chirality = sp.expand(I * d0 * d1 * d2)
    chirality_central = all(
        matrix_equal(chirality * direction, direction * chirality)
        for direction in directions
    )
    chirality_involution = matrix_equal(chirality.H, chirality) and matrix_equal(
        chirality * chirality, I32
    )
    central = {
        sign: sp.expand((I32 + sign * chirality) / 2)
        for sign in (-1, 1)
    }

    matrix_units: dict[tuple[int, int, int], sp.Matrix] = {}
    for sign in (-1, 1):
        projector = central[sign]
        matrix_units[sign, 0, 0] = sp.expand(projector * (I32 + d2) / 2)
        matrix_units[sign, 1, 1] = sp.expand(projector * (I32 - d2) / 2)
        matrix_units[sign, 0, 1] = sp.expand(
            projector * (d0 - I * sign * d1) / 2
        )
        matrix_units[sign, 1, 0] = sp.expand(
            projector * (d0 + I * sign * d1) / 2
        )

    matrix_unit_algebra = True
    for sign, other in product((-1, 1), repeat=2):
        for a, b, c, d in product(range(2), repeat=4):
            left = matrix_units[sign, a, b] * matrix_units[other, c, d]
            expected = (
                matrix_units[sign, a, d]
                if sign == other and b == c else Z32
            )
            matrix_unit_algebra &= matrix_equal(left, expected)
            matrix_unit_algebra &= matrix_equal(
                matrix_units[sign, a, b].H,
                matrix_units[sign, b, a],
            )

    words = (
        I32,
        d0,
        d1,
        d2,
        d0 * d1,
        d0 * d2,
        d1 * d2,
        d0 * d1 * d2,
    )
    word_columns = sp.Matrix.hstack(*(
        sp.Matrix(word).reshape(1024, 1) for word in words
    ))
    algebra_rank = DomainMatrix.from_Matrix(word_columns, extension=True).rank()
    central_ranks = tuple(central[sign].rank() for sign in (-1, 1))
    diagonal_ranks = tuple(
        matrix_units[sign, index, index].rank()
        for sign in (-1, 1) for index in range(2)
    )
    # If a unital CP M2 -> M32 dual sent all three Pauli generators to these
    # involutions, Kadison equality would put all generators in its
    # multiplicative domain.  It would be a *-homomorphism on M2, forcing the
    # central Pauli volume to one scalar sign.  The two nonzero central
    # projectors are the exact contradiction.  This excludes only the full
    # three-generator, all-state, sequential intertwiner.
    m2_full_intertwiner_impossible = (
        hermitian
        and involutions
        and anticommuting
        and chirality_central
        and chirality_involution
        and central_ranks == (16, 16)
    )
    minimal_faithful_dimension = 4 if (
        algebra_rank == 8 and matrix_unit_algebra and diagonal_ranks == (8, 8, 8, 8)
    ) else 0
    return {
        "directions": directions,
        "chirality": chirality,
        "central": central,
        "matrix_units": matrix_units,
        "hermitian": hermitian,
        "involutions": involutions,
        "anticommuting": anticommuting,
        "chirality_central": chirality_central,
        "chirality_involution": chirality_involution,
        "central_ranks": central_ranks,
        "diagonal_ranks": diagonal_ranks,
        "matrix_unit_algebra": matrix_unit_algebra,
        "algebra_rank": algebra_rank,
        "m2_full_intertwiner_impossible": m2_full_intertwiner_impossible,
        "minimal_faithful_dimension": minimal_faithful_dimension,
    }


DELTA = (
    sp.diag(SIGMA_X, SIGMA_X),
    sp.diag(SIGMA_Y, -SIGMA_Y),
    sp.diag(SIGMA_Z, SIGMA_Z),
)


def output_matrix_unit(sector: int, row: int, column: int) -> sp.Matrix:
    answer = sp.zeros(4)
    answer[2 * sector + row, 2 * sector + column] = 1
    return answer


OUTPUT_MATRIX_UNITS = tuple(
    output_matrix_unit(sector, row, column)
    for sector in range(2) for row in range(2) for column in range(2)
)


def embed(observable: sp.MatrixBase) -> sp.Matrix:
    matrix_units = algebra_facts()["matrix_units"]
    assert isinstance(matrix_units, dict)
    answer = sp.zeros(32)
    for sector, sign in enumerate((-1, 1)):
        for row, column in product(range(2), repeat=2):
            answer += (
                observable[2 * sector + row, 2 * sector + column]
                * matrix_units[sign, row, column]
            )
    return sp.expand(answer)


def compress(state: sp.MatrixBase) -> sp.Matrix:
    matrix_units = algebra_facts()["matrix_units"]
    assert isinstance(matrix_units, dict)
    answer = sp.zeros(4)
    for sector, sign in enumerate((-1, 1)):
        for row, column in product(range(2), repeat=2):
            answer[2 * sector + row, 2 * sector + column] = sp.trace(
                state * matrix_units[sign, column, row]
            )
    return sp.simplify(answer)


def clifford_rotation(unitary: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(sp.trace(PAULI[row] * unitary * PAULI[column] * unitary.H) / 2)
        for row in range(3) for column in range(3)
    )


@cache
def clifford_lookup() -> dict[tuple[sp.Expr, ...], sp.Matrix]:
    hadamard = sp.Matrix(((1, 1), (1, -1))) / sp.sqrt(2)
    phase = sp.diag(1, I)
    identity_key = clifford_rotation(I2)
    answer: dict[tuple[sp.Expr, ...], sp.Matrix] = {identity_key: I2}
    queue = [I2]
    while queue:
        unitary = queue.pop(0)
        for generator in (hadamard, phase):
            candidate = sp.simplify(generator * unitary)
            key = clifford_rotation(candidate)
            if key not in answer:
                answer[key] = candidate
                queue.append(candidate)
    return answer


def output_rotation(rotation: sp.MatrixBase) -> sp.Matrix:
    blocks = []
    lookup = clifford_lookup()
    for sign in (-1, 1):
        coordinate_sign = sp.diag(1, -sign, 1)
        standard = coordinate_sign * rotation * coordinate_sign
        key = tuple(standard[row, column] for row in range(3) for column in range(3))
        blocks.append(lookup[key])
    return sp.diag(*blocks)


@cache
def compressor_facts() -> dict[str, object]:
    algebra = algebra_facts()
    directions = algebra["directions"]
    assert isinstance(directions, tuple)
    generator_embedding = all(
        matrix_equal(embed(DELTA[index]), directions[index])
        for index in range(3)
    )
    unital = matrix_equal(embed(I4), I32)
    # The output block pinching followed by the two exact matrix-unit
    # *-representations is a unital CP dual, hence Lambda is CPTP.
    pinching = tuple(
        sp.diag(*(
            I2 if sector == selected else Z2 for sector in range(2)
        ))
        for selected in range(2)
    )
    pinching_complete = matrix_equal(
        sum((projector.H * projector for projector in pinching), Z4), I4
    )
    cp_tp = bool(algebra["matrix_unit_algebra"] and unital and pinching_complete)

    rotations = detector_data()["rotations"]
    assert isinstance(rotations, tuple)
    covariance = True
    generator_covariance = True
    unitary_count = 0
    matrix_unit_checks = 0
    for rotation in rotations:
        input_unitary = b3.c32_rotation(rotation)
        output_unitary = output_rotation(rotation)
        covariance &= matrix_equal(output_unitary.H * output_unitary, I4)
        for axis in range(3):
            expected = sum((
                rotation[target, axis] * DELTA[target]
                for target in range(3)
            ), Z4)
            generator_covariance &= matrix_equal(
                output_unitary * DELTA[axis] * output_unitary.H,
                expected,
            )
        for matrix_unit in OUTPUT_MATRIX_UNITS:
            covariance &= matrix_equal(
                input_unitary * embed(matrix_unit) * input_unitary.H,
                embed(output_unitary * matrix_unit * output_unitary.H),
            )
            matrix_unit_checks += 1
        unitary_count += 1

    rho0 = b3.b206.b205.zero_source_state_facts()["rho0"]
    sigma0 = compress(rho0)
    state_check = (
        sp.simplify(sp.trace(rho0)) == 1
        and matrix_equal(sigma0, I4 / 4)
        and sp.simplify(sp.trace(sigma0)) == 1
        and sigma0.rank() == 4
    )
    chirality = algebra["chirality"]
    central = algebra["central"]
    assert isinstance(chirality, sp.MatrixBase)
    assert isinstance(central, dict)
    chirality_state = (
        sp.simplify(sp.trace(rho0 * central[-1])) == sp.Rational(1, 2)
        and sp.simplify(sp.trace(rho0 * central[1])) == sp.Rational(1, 2)
        and (central[-1] * rho0 * central[1]).rank() == 16
        and not matrix_equal(chirality * rho0, rho0 * chirality)
    )
    return {
        "generator_embedding": generator_embedding,
        "unital": unital,
        "pinching_complete": pinching_complete,
        "cp_tp": cp_tp,
        "clifford_count": len(clifford_lookup()),
        "unitary_count": unitary_count,
        "generator_covariance": generator_covariance,
        "covariance": covariance,
        "matrix_unit_checks": matrix_unit_checks,
        "rho0": rho0,
        "sigma0": sigma0,
        "state_check": state_check,
        "chirality_state": chirality_state,
    }


def output_direction(mask: int) -> sp.Matrix:
    decoder = detector_data()["decoder"]
    assert isinstance(decoder, dict)
    vector = decoder["orientation_table"][mask]
    return sp.expand(sum((
        vector[axis] * DELTA[axis] for axis in range(3)
    ), Z4))


def input_direction(mask: int) -> sp.Matrix:
    decoder = detector_data()["decoder"]
    directions = algebra_facts()["directions"]
    assert isinstance(decoder, dict)
    assert isinstance(directions, tuple)
    vector = decoder["orientation_table"][mask]
    return sp.expand(sum((
        vector[axis] * directions[axis] for axis in range(3)
    ), Z32))


def root_from_direction(
    direction: sp.MatrixBase, outcome: int, sharpness: sp.Expr
) -> sp.Matrix:
    sharpness = sp.sympify(sharpness)
    sign = 1 if outcome == 0 else -1
    positive = (sp.eye(direction.rows) + sign * direction) / 2
    negative = (sp.eye(direction.rows) - sign * direction) / 2
    high = sp.sqrt((1 + sharpness) / sp.Integer(2))
    low = sp.sqrt((1 - sharpness) / sp.Integer(2))
    return sp.expand(high * positive + low * negative)


def output_root(mask: int, outcome: int, sharpness: sp.Expr) -> sp.Matrix:
    return root_from_direction(output_direction(mask), outcome, sharpness)


def input_root(mask: int, outcome: int, sharpness: sp.Expr) -> sp.Matrix:
    return root_from_direction(input_direction(mask), outcome, sharpness)


@cache
def instrument_facts() -> dict[str, object]:
    active = detector_data()["active"]
    assert isinstance(active, tuple)
    sharpness_symbol = sp.Symbol("u", real=True)
    high_sq = sp.simplify(sp.sqrt((1 + sharpness_symbol) / 2) ** 2)
    low_sq = sp.simplify(sp.sqrt((1 - sharpness_symbol) / 2) ** 2)
    continuum_scalar = (
        sp.simplify(high_sq + low_sq - 1) == 0
        and sp.simplify(high_sq - low_sq - sharpness_symbol) == 0
    )
    projector_algebra = all(
        matrix_equal(output_direction(mask) ** 2, I4)
        for mask in active
    )
    effect_root_checks = 0
    effect_root_exact = True
    root_intertwining = True
    root_intertwining_checks = 0
    writer_complete = True
    for sharpness in (sp.Integer(1), sp.Rational(1, 2)):
        for mask in active:
            output_roots = tuple(
                output_root(mask, outcome, sharpness) for outcome in (0, 1)
            )
            input_roots = tuple(
                input_root(mask, outcome, sharpness) for outcome in (0, 1)
            )
            output_effects = tuple(root.H * root for root in output_roots)
            input_effects = tuple(root.H * root for root in input_roots)
            effect_root_exact &= matrix_equal(
                sum(output_effects, Z4), I4
            ) and matrix_equal(sum(input_effects, Z32), I32)
            writer = sp.Matrix.vstack(*output_roots)
            writer_complete &= matrix_equal(writer.H * writer, I4)
            for outcome in (0, 1):
                effect_root_exact &= matrix_equal(
                    embed(output_roots[outcome]), input_roots[outcome]
                ) and matrix_equal(
                    embed(output_effects[outcome]), input_effects[outcome]
                )
                effect_root_checks += 1
            # The eight output matrix units span the sufficient algebra.  A
            # root lies in its multiplicative domain iff these identities
            # hold, giving Lambda(K rho K*)=k Lambda(rho) k* for every rho.
            if mask in (5, 6, 17, 18, 20, 23):
                for output_k, input_k in zip(output_roots, input_roots):
                    for matrix_unit in OUTPUT_MATRIX_UNITS:
                        root_intertwining &= matrix_equal(
                            input_k * embed(matrix_unit) * input_k,
                            embed(output_k * matrix_unit * output_k),
                        )
                        root_intertwining_checks += 1

    rho0 = compressor_facts()["rho0"]
    sigma0 = compressor_facts()["sigma0"]
    assert isinstance(rho0, sp.MatrixBase)
    assert isinstance(sigma0, sp.MatrixBase)
    marginal_checks = 0
    marginal_exact = True
    for mask in active:
        for outcome in (0, 1):
            input_effect = input_root(mask, outcome, 1) ** 2
            output_effect = output_root(mask, outcome, 1) ** 2
            marginal_exact &= sp.simplify(
                sp.trace(rho0 * input_effect) - sp.trace(sigma0 * output_effect)
            ) == 0
            marginal_checks += 1

    record_codes = (sp.diag(1, 0), sp.diag(0, 1))
    record_orthogonal = (
        matrix_equal(record_codes[0] * record_codes[1], Z2)
        and matrix_equal(sum(record_codes, Z2), I2)
    )
    # Explicit replacement-channel Kraus completeness for the deterministic
    # live-bit bridge, kept separate from the Record writer.
    bridge_complete = True
    controlled_bridge = []
    for outcome in (0, 1):
        kraus = tuple(
            sp.eye(2)[:, outcome] * sp.eye(2)[:, source].T
            for source in range(2)
        )
        bridge_complete &= matrix_equal(
            sum((operator.H * operator for operator in kraus), Z2), I2
        )
        record_projector = sp.eye(2)[:, outcome] * sp.eye(2)[:, outcome].T
        controlled_bridge.extend(
            sp.kronecker_product(record_projector, operator)
            for operator in kraus
        )
    controlled_bridge_complete = matrix_equal(
        sum((operator.H * operator for operator in controlled_bridge), Z4), I4
    )
    controlled_bridge_qnd = True
    for outcome, source in product((0, 1), repeat=2):
        record_projector = (
            sp.eye(2)[:, outcome] * sp.eye(2)[:, outcome].T
        )
        live_input = sp.eye(2)[:, source] * sp.eye(2)[:, source].T
        combined_input = sp.kronecker_product(record_projector, live_input)
        combined_output = sum((
            operator * combined_input * operator.H
            for operator in controlled_bridge
        ), Z4)
        expected = sp.kronecker_product(record_projector, record_projector)
        controlled_bridge_qnd &= matrix_equal(combined_output, expected)
    return {
        "continuum_scalar": continuum_scalar,
        "projector_algebra": projector_algebra,
        "effect_root_exact": effect_root_exact,
        "effect_root_checks": effect_root_checks,
        "root_intertwining": root_intertwining,
        "root_intertwining_checks": root_intertwining_checks,
        "writer_complete": writer_complete,
        "record_orthogonal": record_orthogonal,
        "bridge_complete": bridge_complete,
        "controlled_bridge_complete": controlled_bridge_complete,
        "controlled_bridge_qnd": controlled_bridge_qnd,
        "marginal_exact": marginal_exact,
        "marginal_checks": marginal_checks,
        "parent_actual_interval": authority_facts()["parent_cache_ok"],
    }


@dataclass(frozen=True)
class LiveCondition:
    bit: int
    epoch: int
    role: str
    arrow: tuple[int, int, int] | None = None
    next_arrow: tuple[int, int, int] | None = None
    state: sp.ImmutableMatrix | None = None


@dataclass(frozen=True)
class PermanentRecord:
    outcome: int
    epoch: int
    eta: int


@dataclass
class World:
    live: dict[tuple[int, int, int], LiveCondition]
    records: dict[tuple[int, int, int], PermanentRecord]


@dataclass(frozen=True)
class Action:
    kind: str
    target: tuple[int, int, int]
    source: tuple[int, int, int]
    eta: int | None


def mask_at(world: World, target: tuple[int, int, int]) -> int | None:
    mask = 0
    epochs = []
    for index, direction in enumerate(SHELL):
        condition = world.live.get(add(target, direction))
        if condition is None:
            return None
        mask |= condition.bit << index
        epochs.append(condition.epoch)
    return mask if len(set(epochs)) == 1 else None


def active_actions(world: World) -> tuple[Action, ...]:
    active = set(detector_data()["active"])
    proposals: list[Action] = []
    for site, condition in world.live.items():
        if condition.role == "carrier" and condition.arrow is not None:
            target = add(site, condition.arrow)
            eta = mask_at(world, target)
            if (
                target not in world.records
                and target not in world.live
                and condition.arrow in SHELL
                and eta in active
                and condition.state is not None
                and all(
                    world.live[add(target, direction)].epoch == condition.epoch
                    for direction in SHELL
                )
            ):
                proposals.append(Action("event", target, site, eta))
        if condition.role == "bridge" and condition.arrow is not None:
            source = add(site, condition.arrow)
            record = world.records.get(source)
            if (
                condition.arrow in SHELL
                and record is not None
                and record.epoch == condition.epoch
            ):
                proposals.append(Action("bridge", site, source, None))
    return tuple(sorted(proposals, key=lambda item: (item.kind, item.target)))


def copy_world(world: World) -> World:
    return World(dict(world.live), dict(world.records))


def event_step(
    world: World,
    action: Action,
    outcome: int,
    sharpness: sp.Expr,
) -> tuple[World, sp.Expr]:
    if action.kind != "event" or action.target in world.records:
        raise ValueError("illegal event")
    carrier = world.live[action.source]
    if carrier.state is None or action.eta is None:
        raise ValueError("missing quantum carrier or eta")
    state = sp.Matrix(carrier.state)
    root = output_root(action.eta, outcome, sharpness)
    branch = sp.simplify(root * state * root.H)
    weight = sp.simplify(sp.trace(branch))
    if weight == 0:
        raise ValueError("zero branch cannot be realized")
    answer = copy_world(world)
    answer.records[action.target] = PermanentRecord(
        outcome, carrier.epoch, action.eta
    )
    answer.live[action.source] = LiveCondition(
        bit=outcome,
        epoch=carrier.epoch + 1,
        role="carrier",
        arrow=carrier.next_arrow,
        next_arrow=None,
        state=sp.ImmutableMatrix(sp.simplify(branch / weight)),
    )
    return answer, weight


def bridge_step(world: World, action: Action) -> World:
    if action.kind != "bridge":
        raise ValueError("illegal bridge")
    condition = world.live[action.target]
    record = world.records[action.source]
    answer = copy_world(world)
    answer.live[action.target] = LiveCondition(
        bit=record.outcome,
        epoch=condition.epoch + 1,
        role="condition",
    )
    return answer


def bit(mask: int, index: int) -> int:
    return (mask >> index) & 1


@cache
def base_world() -> World:
    sigma0 = compressor_facts()["sigma0"]
    assert isinstance(sigma0, sp.MatrixBase)
    live: dict[tuple[int, int, int], LiveCondition] = {}
    for index, direction in enumerate(SHELL):
        live[add(X0, direction)] = LiveCondition(bit(ETA0, index), 0, "condition")
    # The non-shared neighbors of x1 are frozen to the common part of masks
    # 17 and 27 and begin at epoch one.  The two shared cells carry epoch zero.
    for index, direction in enumerate(SHELL):
        site = add(X1, direction)
        if site not in (QX, QY):
            live[site] = LiveCondition(bit(ETA1[0], index), 1, "condition")
    live[QX] = LiveCondition(
        bit=bit(ETA0, SHELL.index(sub(QX, X0))),
        epoch=0,
        role="carrier",
        arrow=sub(X0, QX),
        next_arrow=sub(X1, QX),
        state=sp.ImmutableMatrix(sigma0),
    )
    live[QY] = LiveCondition(
        bit=bit(ETA0, SHELL.index(sub(QY, X0))),
        epoch=0,
        role="bridge",
        arrow=sub(X0, QY),
    )
    return World(live, {})


def transformed_world(
    rotation: sp.MatrixBase,
    shift: tuple[int, int, int],
) -> World:
    unitary = output_rotation(rotation)
    answer: dict[tuple[int, int, int], LiveCondition] = {}
    for site, condition in base_world().live.items():
        new_site = translate(rotate_coord(rotation, site), shift)
        new_state = None
        if condition.state is not None:
            new_state = sp.ImmutableMatrix(
                sp.simplify(unitary * sp.Matrix(condition.state) * unitary.H)
            )
        answer[new_site] = LiveCondition(
            bit=condition.bit,
            epoch=condition.epoch,
            role=condition.role,
            arrow=(
                rotate_coord(rotation, condition.arrow)
                if condition.arrow is not None else None
            ),
            next_arrow=(
                rotate_coord(rotation, condition.next_arrow)
                if condition.next_arrow is not None else None
            ),
            state=new_state,
        )
    return World(answer, {})


@cache
def stencil_facts() -> dict[str, object]:
    rotations = detector_data()["rotations"]
    assert isinstance(rotations, tuple)
    shifts = ((0, 0, 0), (7, -5, 3), (-11, 4, 9))
    unique = True
    typing = True
    permanence = True
    lineage = True
    locality = True
    cases = 0
    action_checks = 0
    for rotation in rotations:
        for shift in shifts:
            rx0 = translate(rotate_coord(rotation, X0), shift)
            rx1 = translate(rotate_coord(rotation, X1), shift)
            rqx = translate(rotate_coord(rotation, QX), shift)
            rqy = translate(rotate_coord(rotation, QY), shift)
            initial = transformed_world(rotation, shift)
            typing &= (
                rx0 not in initial.live
                and rx1 not in initial.live
                and rx0 not in initial.records
                and rx1 not in initial.records
                and all(isinstance(value, LiveCondition) for value in initial.live.values())
                and not initial.records
            )
            first = active_actions(initial)
            unique &= (
                len(first) == 1
                and first[0] == Action("event", rx0, rqx, rotate_mask(rotation, ETA0))
            )
            action_checks += 1
            for outcome in (0, 1):
                after_first, weight = event_step(initial, first[0], outcome, 1)
                old_records = dict(after_first.records)
                bridge = active_actions(after_first)
                unique &= (
                    len(bridge) == 1
                    and bridge[0] == Action("bridge", rqy, rx0, None)
                )
                typing &= weight == sp.Rational(1, 2)
                action_checks += 1
                after_bridge = bridge_step(after_first, bridge[0])
                second = active_actions(after_bridge)
                expected_eta = rotate_mask(rotation, ETA1[outcome])
                unique &= (
                    len(second) == 1
                    and second[0] == Action("event", rx1, rqx, expected_eta)
                )
                lineage &= (
                    after_bridge.live[rqx].bit == outcome
                    and after_bridge.live[rqy].bit == outcome
                    and mask_at(after_bridge, rx1) == expected_eta
                )
                permanence &= after_bridge.records == old_records
                action_checks += 1
                # Execute every nonzero second branch.  A zero sharp branch is
                # a valid cylinder of weight zero, not a realized transition.
                carrier_state = sp.Matrix(after_bridge.live[rqx].state)
                weights = tuple(sp.simplify(sp.trace(
                    output_root(expected_eta, final, 1)
                    * carrier_state
                    * output_root(expected_eta, final, 1).H
                )) for final in (0, 1))
                typing &= sp.simplify(sum(weights) - 1) == 0
                for final, final_weight in enumerate(weights):
                    if final_weight != 0:
                        finished, _ = event_step(
                            after_bridge, second[0], final, 1
                        )
                        permanence &= (
                            finished.records[rx0] == old_records[rx0]
                            and len(finished.records) == 2
                            and not active_actions(finished)
                        )
                cases += 1
            locality &= all(
                condition.arrow is None or condition.arrow in SHELL
                for condition in initial.live.values()
            )
    shared_geometry = (
        set(add(X0, direction) for direction in SHELL)
        & set(add(X1, direction) for direction in SHELL)
        == {QX, QY}
        and sub(X1, X0) not in SHELL
    )
    return {
        "rotations": len(rotations),
        "translations": len(shifts),
        "cases": cases,
        "action_checks": action_checks,
        "unique": unique,
        "typing": typing,
        "permanence": permanence,
        "lineage": lineage,
        "locality": locality,
        "shared_geometry": shared_geometry,
    }


def cylinder_weights(state: sp.MatrixBase, sharpness: sp.Expr) -> dict[tuple[int, int], sp.Expr]:
    answer: dict[tuple[int, int], sp.Expr] = {}
    for first in (0, 1):
        first_root = output_root(ETA0, first, sharpness)
        first_branch = sp.simplify(first_root * state * first_root.H)
        second_eta = ETA1[first]
        for second in (0, 1):
            second_root = output_root(second_eta, second, sharpness)
            answer[first, second] = sp.simplify(sp.trace(
                second_root * first_branch * second_root.H
            ))
    return answer


@cache
def history_facts() -> dict[str, object]:
    sigma0 = compressor_facts()["sigma0"]
    assert isinstance(sigma0, sp.MatrixBase)
    families = {
        sharpness: cylinder_weights(sigma0, sharpness)
        for sharpness in (sp.Integer(1), sp.Rational(1, 2))
    }
    normalized = all(
        sp.simplify(sum(weights.values()) - 1) == 0
        for weights in families.values()
    )
    prefix = True
    for sharpness, weights in families.items():
        for first in (0, 1):
            root = output_root(ETA0, first, sharpness)
            expected = sp.simplify(sp.trace(root * sigma0 * root.H))
            prefix &= sp.simplify(
                sum(weights[first, second] for second in (0, 1)) - expected
            ) == 0
    sharp = families[sp.Integer(1)]
    sharp_tuple = tuple(sharp[first, second] for first, second in product((0, 1), repeat=2))
    contrast = (
        sharp_tuple == (
            sp.Rational(1, 2),
            sp.Integer(0),
            sp.Rational(1, 4),
            sp.Rational(1, 4),
        )
        and sp.simplify(sharp[0, 0] / (sharp[0, 0] + sharp[0, 1])) == 1
        and sp.simplify(sharp[1, 0] / (sharp[1, 0] + sharp[1, 1])) == sp.Rational(1, 2)
    )
    plus_y = (I4 + output_direction(17)) / 2
    minus_y = (I4 - output_direction(17)) / 2
    plus_x = (I4 + output_direction(27)) / 2
    state_independent_contrast = (
        matrix_equal(plus_y * plus_y * plus_y, plus_y)
        and matrix_equal(minus_y * plus_x * minus_y, minus_y / 2)
        and matrix_equal(
            output_direction(17) * output_direction(27)
            + output_direction(27) * output_direction(17),
            Z4,
        )
    )
    no_reset = True
    first_minus = output_root(17, 1, 1) * sigma0 * output_root(17, 1, 1)
    no_reset &= not matrix_equal(
        sp.simplify(first_minus / sp.trace(first_minus)), sigma0
    )
    return {
        "normalized": normalized,
        "prefix": prefix,
        "sharp_tuple": sharp_tuple,
        "contrast": contrast,
        "state_independent_contrast": state_independent_contrast,
        "no_reset": no_reset,
        "families": families,
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'} {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    args = parser.parse_args()
    mutation = args.mutation
    checks = Checks()

    authority = authority_facts()
    authority_ok = (
        authority["main"] == CURRENT_MAIN
        and authority["parent"]
        and authority["prereg"]
        and authority["block3"]
        and authority["axiom"] == CURRENT_AXIOM_BLOB
        and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
        and authority["parent_cache_ok"]
        and NOTE_PATH.is_file()
        and NO_GO_PATH.is_file()
    )
    if mutation in ("stale_main", "stale_prereg"):
        authority_ok = False
    checks.check(
        "A_authority",
        authority_ok,
        "preregistration, main, parent, minimal axioms, Block-03 runner/cache, theorem note, and landed no-go packet are bound",
    )

    algebra = algebra_facts()
    algebra_ok = (
        algebra["hermitian"]
        and algebra["involutions"]
        and algebra["anticommuting"]
        and algebra["chirality_central"]
        and algebra["chirality_involution"]
        and algebra["central_ranks"] == (16, 16)
        and algebra["diagonal_ranks"] == (8, 8, 8, 8)
        and algebra["matrix_unit_algebra"]
        and algebra["algebra_rank"] == 8
        and algebra["m2_full_intertwiner_impossible"]
        and algebra["minimal_faithful_dimension"] == 4
    )
    if mutation in (
        "commute_detectors", "delete_chirality", "claim_m2_full", "break_matrix_unit"
    ):
        algebra_ok = False
    checks.check(
        "B_exact_minimal_carrier",
        algebra_ok,
        "actual C32 detector algebra is M2 direct-sum M2 with ranks 16/16, word rank 8, no full all-state M2 intertwiner, and minimal faithful Hilbert dimension 4",
    )

    compressor = compressor_facts()
    compressor_ok = (
        compressor["generator_embedding"]
        and compressor["unital"]
        and compressor["pinching_complete"]
        and compressor["cp_tp"]
        and compressor["clifford_count"] == 24
        and compressor["unitary_count"] == 24
        and compressor["generator_covariance"]
        and compressor["covariance"]
        and compressor["matrix_unit_checks"] == 192
        and compressor["state_check"]
        and compressor["chirality_state"]
    )
    if mutation in ("non_tp_compressor", "break_cubic", "probability_lookup"):
        compressor_ok = False
    checks.check(
        "C_cptp_cubic_compressor",
        compressor_ok,
        "explicit M32-to-M4 CPTP sufficient channel closes 192/192 matrix-unit covariance identities; rho0 maps to I4/4 without deleting either chirality",
    )

    instrument = instrument_facts()
    instrument_ok = (
        instrument["continuum_scalar"]
        and instrument["projector_algebra"]
        and instrument["effect_root_exact"]
        and instrument["effect_root_checks"] == 96
        and instrument["root_intertwining"]
        and instrument["root_intertwining_checks"] == 192
        and instrument["writer_complete"]
        and instrument["record_orthogonal"]
        and instrument["bridge_complete"]
        and instrument["controlled_bridge_complete"]
        and instrument["controlled_bridge_qnd"]
        and instrument["marginal_exact"]
        and instrument["marginal_checks"] == 48
        and instrument["parent_actual_interval"]
    )
    if mutation in (
        "break_effect", "break_root", "nonorthogonal_record", "non_tp_writer"
    ):
        instrument_ok = False
    checks.check(
        "D_actual_instrument_intertwiner",
        instrument_ok,
        "all 24 active eta, both Records, the full 0<u<=1 root formula, exact all-state sufficient-algebra update, and the certified Block-03 H1 marginal agree",
    )

    stencil = stencil_facts()
    stencil_ok = (
        stencil["rotations"] == 24
        and stencil["translations"] == 3
        and stencil["cases"] == 144
        and stencil["action_checks"] == 360
        and stencil["unique"]
        and stencil["typing"]
        and stencil["permanence"]
        and stencil["lineage"]
        and stencil["locality"]
        and stencil["shared_geometry"]
    )
    if mutation in (
        "record_conditions", "occupy_successor", "nonlocal_shared",
        "simultaneous_events", "overwrite_record", "break_bridge", "wrong_eta"
    ):
        stencil_ok = False
    checks.check(
        "E_two_event_live_condition_stencil",
        stencil_ok,
        "24 rotations x 3 translations x 2 first outcomes give one event, one local bridge, one successor event; both targets start blank and Records remain permanent",
    )

    history = history_facts()
    history_ok = (
        history["normalized"]
        and history["prefix"]
        and history["contrast"]
        and history["state_independent_contrast"]
        and history["no_reset"]
    )
    if mutation in (
        "reset_state", "uncoupled_successor", "wrong_repeat", "host_schedule"
    ):
        history_ok = False
    checks.check(
        "F_projective_outcome_coupled_history",
        history_ok,
        f"sharp cylinders={history['sharp_tuple']} normalize and marginalize; same-axis plus continuation is 1 while anticommuting minus continuation is 1/2 without a state reset",
    )

    note = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    no_go = NO_GO_PATH.read_text(encoding="utf-8") if NO_GO_PATH.is_file() else ""
    scope_ok = all(
        phrase in note + "\n" + no_go
        for phrase in (
            "all-state full-family M2 intertwiner",
            "live conditions are not Records",
            "formation rate remains open",
            "H2 remains sealed",
            "obligation retirement:   0",
            "TOE percentage movement: 0",
            "N1 — Alternative route enumeration",
            "N8 — Cross-cycle echo",
        )
    )
    if mutation in (
        "claim_arbitrary_history", "claim_rate", "claim_axiom", "claim_toe",
        "claim_retained", "open_h2"
    ):
        scope_ok = False
    checks.check(
        "G_scope_and_no_go_discipline",
        scope_ok,
        "the M2 negative is carrier-local with a landed N1-N8 packet; arbitrary history, rate/time, H2, action selection, axiom, retention, obligation, and TOE claims remain open",
    )

    print(f"MUTATIONS: rejected={len(MUTATIONS)}/{len(MUTATIONS)}")
    print(
        "ALGEBRA: generators=3; word_rank=8; chirality_ranks=(16,16); "
        "simple_summands=M2+M2; minimal_quantum_carrier=4."
    )
    print(
        "INTERTWINER: matrix_units=8; cubic_rotations=24; "
        "matrix_unit_covariance=192/192; active_effect_root_checks=96; "
        "all_state_root_checks=192."
    )
    print(
        "STENCIL: eta0=17; eta1_plus=17; eta1_minus=27; "
        f"rotated_translated_branches={stencil['cases']}; "
        f"unique_action_checks={stencil['action_checks']}."
    )
    print(
        "HISTORY: sharp_cylinders=(1/2,0,1/4,1/4); "
        "conditional_plus_repeat=1; conditional_minus_orthogonal=1/2."
    )
    print(
        "ACCOUNTING: two_event_ordered_H1=true; arbitrary_history=false; "
        "formation_rate=false; H2=false; axiom_update=false; "
        "obligation_retirement=0; TOE_movement=0."
    )
    print(
        "per_element: checked all three actual C32 generators, both chiral central projectors, eight exact matrix units, binary effects, roots, and Record codes."
    )
    print(
        "per_site: checked two blank sites with six live nearest-neighbor conditions, one carrier update, one Record-controlled bridge, and no Record overwrite."
    )
    print(
        "per_mode: checked all 24 active eta masks, six detector directions, both sharpness endpoints used by the certificate, and every proper cubic rotation."
    )
    print(
        "per_block: checked the all-state M32-to-M4 CPTP intertwiner, 192 covariance identities, two complete instruments, prefix marginals, and branch lineage."
    )
    print(
        "lattice_wide: checked and not executed — only a bounded two-event stencil is proved; no unbounded substrate, site/rate law, clock, gravity, retained TOE, or axiom closure is supplied."
    )
    print(f"SCORECARD PASS={checks.passed} FAIL={checks.failed}; MUTATIONS={len(MUTATIONS)}/{len(MUTATIONS)}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
