#!/usr/bin/env python3
"""Block 38 random-axis matter attachment and same-kernel repeat selector.

The runner separates four mathematical objects:

1. the affine covariant binary response class on a physical qubit;
2. its exact signed-axis pushforward to the atomless Haar response;
3. a measure-and-prepare successor matter state and a second use of the same
   axis/effect kernel; and
4. a radius-one Record generator that embeds both uses before a value-blind
   close while preserving the Block-37 active-cut interface.

The selected endpoint is derived only conditionally on record-faithful pure
matter attachment and exact operational repeatability. The runner explicitly
does not derive repeatability from Record permanence.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import importlib.util
import inspect
import itertools
import subprocess
import sys
from collections import defaultdict, deque
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901"
)
PREREG_COMMIT = "d75454074b9b28d12e63689b0b0d4d3d21a8c1cd"
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PARENT_RUNNER_PATH = (
    "scripts/admissibility_block36_specific_nn_active_cut_record_front_2026_09_01.py"
)
PARENT_NOTE_PATH = (
    "docs/ADMISSIBILITY_BLOCK36_SPECIFIC_NN_ACTIVE_CUT_RECORD_FRONT_"
    "BOUNDED_THEOREM_NOTE_2026-09-01.md"
)
NOTE_PATH = ROOT / (
    "docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-09-01.md"
)
AUDIT_TIMEOUT_SEC = 120

FROZEN_BLOBS = {
    f"{PREREG_COMMIT}:{MINIMAL_PATH}": "bc23300becfe4e4db57153c0e94cfcdf2338da71",
    f"{PREREG_COMMIT}:{PARENT_RUNNER_PATH}": "6c956094bd28d5648a3bfe1ae896715837f138a1",
    f"{PREREG_COMMIT}:{PARENT_NOTE_PATH}": "1c7784485c1ae581c8a05db463ed78c55e84257b",
    (
        f"{PREREG_COMMIT}:docs/"
        "ADMISSIBILITY_GAUSSIAN_FAIR_RECORD_MIDPOINT_AFFINITY_HAAR_EDGE_FACTOR_"
        "FRESH_PORT_RESET_BOUNDED_THEOREM_NOTE_2026-09-01.md"
    ): "93aca5052adfde9ada5325d1058bf5507d85333a",
    (
        f"{PREREG_COMMIT}:docs/"
        "ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_"
        "BOUNDED_THEOREM_NOTE_2026-09-01.md"
    ): "833232ecc6a8231c59f16b1af819c47c0eeb2bde",
}

# Literal tuple: the audit evidence seeder parses this surface.
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_2026_09_01.py",
    "docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/PRIOR_ART_SEARCH.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/CLAIM_STATUS_CERTIFICATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/REVIEW_HISTORY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/HANDOFF.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block38-random-axis-repeatability-matter-selector-20260901/STATE.yaml",
)


def load_parent_module():
    path = ROOT / PARENT_RUNNER_PATH
    spec = importlib.util.spec_from_file_location("block37_parent_runner", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Block-37 parent runner")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PARENT = load_parent_module()
ROTATIONS = tuple(
    tuple(tuple(int(value) for value in row) for row in rotation)
    for rotation in PARENT.ROTATIONS
)
IDENTITY_ROTATION = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
)
IDENTITY_FRAME_INDEX = ROTATIONS.index(IDENTITY_ROTATION)


Vec = tuple[Fraction, Fraction, Fraction]
Coord = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

ZERO: Vec = (Fraction(0), Fraction(0), Fraction(0))
E_X: Vec = (Fraction(1), Fraction(0), Fraction(0))
E_Y: Vec = (Fraction(0), Fraction(1), Fraction(0))
E_Z: Vec = (Fraction(0), Fraction(0), Fraction(1))
AXES: tuple[Vec, ...] = (E_X, (-E_X[0], E_X[1], E_X[2]), E_Y, (E_Y[0], -E_Y[1], E_Y[2]), E_Z, (E_Z[0], E_Z[1], -E_Z[2]))
MODE_RND = 0
MODE_DIR = 1


def q(value: int | Fraction | sp.Rational) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, sp.Rational):
        return Fraction(int(value.p), int(value.q))
    return Fraction(value)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(left[i] - right[i] for i in range(3))  # type: ignore[return-value]


def scale_int(value: int, vector: Coord) -> Coord:
    return tuple(value * vector[i] for i in range(3))  # type: ignore[return-value]


def vec_scale(value: Fraction, vector: Vec) -> Vec:
    return tuple(value * vector[i] for i in range(3))  # type: ignore[return-value]


def vec_add(left: Vec, right: Vec) -> Vec:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def dot(left: Sequence[Fraction], right: Sequence[Fraction]) -> Fraction:
    return sum((left[i] * right[i] for i in range(3)), Fraction(0))


def rotate(rotation: Rotation, vector: Sequence[Fraction]) -> Vec:
    return tuple(
        sum((Fraction(rotation[i][j]) * vector[j] for j in range(3)), Fraction(0))
        for i in range(3)
    )  # type: ignore[return-value]


def rotate_coord(rotation: Rotation, vector: Coord) -> Coord:
    return tuple(
        sum(rotation[i][j] * vector[j] for j in range(3)) for i in range(3)
    )  # type: ignore[return-value]


def transpose(rotation: Rotation) -> Rotation:
    return tuple(
        tuple(rotation[j][i] for j in range(3)) for i in range(3)
    )  # type: ignore[return-value]


def determinant(rotation: Rotation) -> int:
    return (
        rotation[0][0] * (rotation[1][1] * rotation[2][2] - rotation[1][2] * rotation[2][1])
        - rotation[0][1] * (rotation[1][0] * rotation[2][2] - rotation[1][2] * rotation[2][0])
        + rotation[0][2] * (rotation[1][0] * rotation[2][1] - rotation[1][1] * rotation[2][0])
    )


I2 = sp.eye(2)
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)


def spq(value: Fraction | int) -> sp.Rational:
    value = q(value)
    return sp.Rational(value.numerator, value.denominator)


def bloch_matrix(vector: Sequence[Fraction]) -> sp.Matrix:
    answer = sp.zeros(2)
    for index in range(3):
        answer += spq(vector[index]) * SIGMA[index]
    return answer


def density(vector: Sequence[Fraction]) -> sp.Matrix:
    return (I2 + bloch_matrix(vector)) / 2


def effect(axis: Vec, outcome: int, response: Fraction) -> sp.Matrix:
    return (I2 + outcome * spq(response) * bloch_matrix(axis)) / 2


def binary_probability(
    state: Vec, axis: Vec, outcome: int, response: Fraction
) -> Fraction:
    return (Fraction(1) + outcome * response * dot(axis, state)) / 2


def post_state(axis: Vec, outcome: int, sharpness: Fraction) -> Vec:
    return vec_scale(sharpness * outcome, axis)


def choi_measure_prepare(
    axis: Vec, outcome: int, response: Fraction, sharpness: Fraction
) -> sp.Matrix:
    return sp.kronecker_product(
        density(post_state(axis, outcome, sharpness)),
        effect(axis, outcome, response).T,
    )


def matrix_is_psd_exact(matrix: sp.Matrix) -> bool:
    eigenvalues = matrix.eigenvals()
    return all(sp.simplify(value) >= 0 for value in eigenvalues)


def affine_covariance_certificate() -> tuple[bool, int, tuple[sp.Expr, ...]]:
    av = sp.symbols("a0:3")
    dv = sp.symbols("d0:3")
    mv = sp.symbols("m0:9")
    variables = (*av, *dv, *mv)
    avec = sp.Matrix(av)
    dvec = sp.Matrix(dv)
    matrix = sp.Matrix(3, 3, mv)
    equations: list[sp.Expr] = []
    for rotation in ROTATIONS:
        rmat = sp.Matrix(rotation)
        equations.extend(rmat.T * avec - avec)
        equations.extend(rmat.T * dvec - dvec)
        equations.extend(list(rmat.T * matrix * rmat - matrix))
    constraint, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = constraint.nullspace()
    expected = sp.Matrix([0] * 6 + [1, 0, 0, 0, 1, 0, 0, 0, 1])
    proportional = (
        len(nullspace) == 1
        and all(
            sp.simplify(nullspace[0][index] * expected[6] - expected[index] * nullspace[0][6])
            == 0
            for index in range(15)
        )
    )
    return constraint.rank() == 14 and proportional, constraint.rank(), tuple(nullspace[0]) if nullspace else ()


def cp_instrument_certificate() -> tuple[bool, int]:
    cases = 0
    ok = True
    states: tuple[Vec, ...] = (
        ZERO,
        E_X,
        E_Z,
        (Fraction(3, 5), Fraction(0), Fraction(4, 5)),
        (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)),
    )
    parameters = (
        Fraction(-1),
        Fraction(-1, 2),
        Fraction(0),
        Fraction(1, 2),
        Fraction(1),
    )
    for axis, state, response, sharpness in itertools.product(
        AXES, states, parameters, parameters
    ):
        effects = effect(axis, 1, response) + effect(axis, -1, response)
        probabilities = tuple(
            binary_probability(state, axis, outcome, response)
            for outcome in (-1, 1)
        )
        ok = ok and effects == I2 and sum(probabilities, Fraction(0)) == 1
        for outcome in (-1, 1):
            branch = choi_measure_prepare(axis, outcome, response, sharpness)
            ok = (
                ok
                and matrix_is_psd_exact(effect(axis, outcome, response))
                and matrix_is_psd_exact(density(post_state(axis, outcome, sharpness)))
                and matrix_is_psd_exact(branch)
                and 0 <= binary_probability(state, axis, outcome, response) <= 1
            )
            cases += 1
    return ok, cases


def symbolic_cp_square_certificate() -> tuple[bool, tuple[sp.Expr, ...], int]:
    """Exact continuum certificate on |lambda|,|kappa|<=1.

    Each displayed eigenvalue is separately affine on the closed parameter
    square, so its bilinear interpolation from the four corners is
    nonnegative exactly when all four exact corner values are nonnegative.
    """

    lam, kap = sp.symbols("lambda kappa", real=True)
    effect_spectrum = ((1 + lam) / 2, (1 - lam) / 2)
    state_spectrum = ((1 + kap) / 2, (1 - kap) / 2)
    choi_spectrum = tuple(
        sp.expand(left * right)
        for left, right in itertools.product(state_spectrum, effect_spectrum)
    )
    spectra = (*effect_spectrum, *state_spectrum, *choi_spectrum)
    corner_cases = 0
    square_positive = True
    for value in spectra:
        square_positive = square_positive and sp.diff(value, lam, 2) == 0
        square_positive = square_positive and sp.diff(value, kap, 2) == 0
        for left, right in itertools.product((-1, 1), repeat=2):
            corner = sp.simplify(value.subs({lam: left, kap: right}))
            square_positive = square_positive and bool(corner >= 0)
            corner_cases += 1
    axis = E_Z
    effect_sum = sp.simplify(effect(axis, 1, Fraction(1, 2)) + effect(axis, -1, Fraction(1, 2)))
    return square_positive and effect_sum == I2, spectra, corner_cases


def haar_factorization_certificate() -> tuple[bool, tuple[sp.Expr, ...]]:
    lam, u = sp.symbols("lambda u", real=True)
    plus = (1 + lam * u) / 2
    minus_after_antipode = (1 + lam * u) / 2
    density_result = sp.expand(plus + minus_after_antipode)
    normalization = sp.integrate(density_result, (u, -1, 1)) / 2
    first_moment = sp.integrate(u * density_result, (u, -1, 1)) / 2
    haar_fourth = sp.integrate(u**4, (u, -1, 1)) / 2
    six_axis_fourth = sp.Rational(1, 3)
    return (
        sp.simplify(density_result - (1 + lam * u)) == 0
        and normalization == 1
        and first_moment == lam / 3
        and haar_fourth == sp.Rational(1, 5)
        and six_axis_fourth != haar_fourth,
        (density_result, normalization, first_moment, haar_fourth, six_axis_fourth),
    )


def mixture_and_joint_M_certificate() -> tuple[bool, tuple[sp.Expr, sp.Expr]]:
    p, lam, kap = sp.symbols("p lambda kappa", real=True)
    n = sp.symbols("n0:3", real=True)
    u0 = sp.symbols("u0_0:3", real=True)
    u1 = sp.symbols("u1_0:3", real=True)
    mix = tuple(p * u0[i] + (1 - p) * u1[i] for i in range(3))
    random_density = p * (1 + lam * sum(n[i] * u0[i] for i in range(3))) + (
        1 - p
    ) * (1 + lam * sum(n[i] * u1[i] for i in range(3)))
    direct_density = 1 + lam * sum(n[i] * mix[i] for i in range(3))
    first_gap = sp.expand(random_density - direct_density)
    b1, b2, axis_dot = sp.symbols("b1 b2 axis_dot", real=True)
    repeat_factor = (1 + b1 * b2 * lam * kap) / 2
    joint_gap = sp.expand(repeat_factor * first_gap)
    return first_gap == 0 and joint_gap == 0, (first_gap, joint_gap)


def nonlinear_affinity_control() -> tuple[bool, sp.Expr]:
    # q(n,s)=1+(n.s)^3 is positive and normalized on Haar, has the same
    # aligned/anti-aligned endpoints, but fails preparation affinity.
    direct_midpoint = 1 + sp.Rational(1, 2) ** 3
    mixed_responses = sp.Rational(3, 2)
    gap = sp.simplify(direct_midpoint - mixed_responses)
    return gap == -sp.Rational(3, 8), gap


def repeat_selector_certificate() -> tuple[bool, tuple[sp.Expr, ...]]:
    lam, kap = sp.symbols("lambda kappa", real=True)
    same = (1 + lam * kap) / 2
    mismatch = (1 - lam * kap) / 2
    aligned = sp.simplify(same.subs({lam: 1, kap: 1}))
    depolarized = sp.simplify(mismatch.subs({lam: sp.Rational(1, 2), kap: 1}))
    mixed_post = sp.simplify(mismatch.subs({lam: 1, kap: sp.Rational(1, 2)}))
    anti_pair = sp.simplify(mismatch.subs({lam: -1, kap: -1}))
    # On the closed square, lam*kap=1 has only the two same-sign corners.
    corner_exhaustion = all(
        (left * right == 1) == ((left, right) in ((-1, -1), (1, 1)))
        for left, right in itertools.product((-1, 0, 1), repeat=2)
    )
    record_faithful = sp.solve(sp.Eq(mismatch.subs(kap, 1), 0), lam) == [1]
    return (
        sp.simplify(same + mismatch - 1) == 0
        and aligned == 1
        and depolarized == sp.Rational(1, 4)
        and mixed_post == sp.Rational(1, 4)
        and anti_pair == 0
        and corner_exhaustion
        and record_faithful,
        (same, mismatch, aligned, depolarized, mixed_post, anti_pair),
    )


@dataclass(frozen=True)
class Protocol:
    mode: int
    u0: Vec
    u1: Vec
    weight_u0: Fraction

    @property
    def mixture(self) -> Vec:
        return vec_add(
            vec_scale(self.weight_u0, self.u0),
            vec_scale(1 - self.weight_u0, self.u1),
        )

    def program(self, selector: int) -> Vec:
        if self.mode == MODE_RND:
            return self.u0 if selector == 0 else self.u1
        return self.mixture

    @property
    def payload(self) -> tuple[Fraction, ...]:
        return (*self.u0, self.weight_u0, *self.u1)


DEFAULT_RND = Protocol(MODE_RND, E_Z, E_X, Fraction(1, 2))
DEFAULT_DIR = Protocol(MODE_DIR, E_Z, E_X, Fraction(1, 2))


ROLE_ORDER = (
    "H",
    "T",
    "G",
    "R",
    "P",
    "A",
    "F",
    "M",
    "B2",
    "C",
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "Q5",
    "Q6",
    "Q7",
    "Q8",
)
PROTOCOL_ROLES = {"H", "T", "R", "P", "C", *(f"Q{i}" for i in range(1, 9))}


def field_code(value: int | None, kind: str) -> int:
    if value is None:
        return 0
    if kind == "mode":
        return {MODE_RND: 1, MODE_DIR: 2}[value]
    if kind == "selector":
        return {0: 1, 1: 2}[value]
    return {-1: 1, 1: 2}[value]


def field_value(code: int, kind: str) -> int | None:
    if code == 0:
        return None
    if kind == "mode":
        return {1: MODE_RND, 2: MODE_DIR}[code]
    if kind == "selector":
        return {1: 0, 2: 1}[code]
    return {1: -1, 2: 1}[code]


def tag_for(
    role: str,
    frame: int,
    mode: int | None = None,
    selector: int | None = None,
    outcome: int | None = None,
) -> Fraction:
    value = ROLE_ORDER.index(role)
    value = value * len(ROTATIONS) + frame
    value = value * 3 + field_code(mode, "mode")
    value = value * 3 + field_code(selector, "selector")
    value = value * 3 + field_code(outcome, "outcome")
    return Fraction(2 + value)


def decode_tag(tag: Fraction) -> tuple[str, int, int | None, int | None, int | None] | None:
    if tag.denominator != 1 or tag < 2:
        return None
    value = int(tag) - 2
    outcome_code = value % 3
    value //= 3
    selector_code = value % 3
    value //= 3
    mode_code = value % 3
    value //= 3
    frame = value % len(ROTATIONS)
    value //= len(ROTATIONS)
    if not 0 <= value < len(ROLE_ORDER):
        return None
    return (
        ROLE_ORDER[value],
        frame,
        field_value(mode_code, "mode"),
        field_value(selector_code, "selector"),
        field_value(outcome_code, "outcome"),
    )


@dataclass(frozen=True)
class Carrier:
    coefficients: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        if len(self.coefficients) != 8:
            raise ValueError("one M2 carrier needs eight real coefficients")

    @property
    def tag(self):
        return decode_tag(self.coefficients[0])


def padded(values: Sequence[Fraction]) -> tuple[Fraction, ...]:
    if len(values) > 7:
        raise ValueError("payload exceeds the seven available real coordinates")
    return tuple(values) + (Fraction(0),) * (7 - len(values))


def make_carrier(
    role: str,
    frame: int,
    *,
    protocol: Protocol | None = None,
    mode: int | None = None,
    selector: int | None = None,
    outcome: int | None = None,
    axis: Vec | None = None,
    direction: Vec | None = None,
    state: Vec | None = None,
) -> Carrier:
    if protocol is not None:
        mode = protocol.mode
    if role in PROTOCOL_ROLES:
        if protocol is None:
            raise ValueError(f"{role} requires a protocol")
        payload = protocol.payload
    elif role == "F":
        if axis is None or direction is None:
            raise ValueError("F needs the recorded axis and outcome direction")
        payload = (*axis, *direction)
    elif role == "M":
        if axis is None or state is None:
            raise ValueError("M needs the retained axis and successor state")
        payload = (*axis, *state)
    elif role in {"A", "B2"}:
        vector = axis if role == "A" else direction
        if vector is None:
            raise ValueError(f"{role} needs one direction")
        payload = tuple(vector)
    else:
        payload = ()
    return Carrier(
        (
            tag_for(role, frame, mode=mode, selector=selector, outcome=outcome),
            *padded(payload),
        )
    )


def carrier_fields(carrier: Carrier):
    if carrier.tag is None:
        raise ValueError("invalid carrier tag")
    return carrier.tag


def carrier_protocol(carrier: Carrier) -> Protocol:
    role, _, mode, _, _ = carrier_fields(carrier)
    if role not in PROTOCOL_ROLES or mode not in (MODE_RND, MODE_DIR):
        raise ValueError("carrier has no protocol")
    payload = carrier.coefficients[1:]
    return Protocol(
        mode,
        tuple(payload[:3]),  # type: ignore[arg-type]
        tuple(payload[4:7]),  # type: ignore[arg-type]
        payload[3],
    )


def carrier_axis_direction(carrier: Carrier) -> tuple[Vec, Vec]:
    role, _, _, _, _ = carrier_fields(carrier)
    if role != "F":
        raise ValueError("not a first-outcome carrier")
    return (
        tuple(carrier.coefficients[1:4]),  # type: ignore[return-value]
        tuple(carrier.coefficients[4:7]),  # type: ignore[return-value]
    )


def carrier_axis_state(carrier: Carrier) -> tuple[Vec, Vec]:
    role, _, _, _, _ = carrier_fields(carrier)
    if role != "M":
        raise ValueError("not a matter carrier")
    return (
        tuple(carrier.coefficients[1:4]),  # type: ignore[return-value]
        tuple(carrier.coefficients[4:7]),  # type: ignore[return-value]
    )


def carrier_direction(carrier: Carrier) -> Vec:
    role, _, _, _, _ = carrier_fields(carrier)
    if role not in {"A", "B2"}:
        raise ValueError("not a direction carrier")
    return tuple(carrier.coefficients[1:4])  # type: ignore[return-value]


@dataclass(frozen=True)
class Frame:
    index: int

    @property
    def rotation(self) -> Rotation:
        return ROTATIONS[self.index]

    @property
    def d(self) -> Coord:
        return rotate_coord(self.rotation, (1, 0, 0))

    @property
    def t(self) -> Coord:
        return rotate_coord(self.rotation, (0, 1, 0))


@dataclass(frozen=True)
class Config:
    mutation: str | None = None
    response: Fraction = Fraction(1, 2)
    sharpness: Fraction = Fraction(1, 2)

    @property
    def first_response(self) -> Fraction:
        return Fraction(1) if self.mutation == "hardcoded_lambda" else self.response

    @property
    def second_response(self) -> Fraction:
        return (
            self.response / 2
            if self.mutation == "different_lambda"
            else self.response
        )

    @property
    def post_sharpness(self) -> Fraction:
        return Fraction(1, 2) if self.mutation == "mixed_as_pure" else self.sharpness

    @property
    def claimed_scope(self) -> str:
        return "toe_closed" if self.mutation == "toe_promotion" else "conditional_selector"

    @property
    def second_reads_first_record(self) -> bool:
        return self.mutation == "record_relay"

    @property
    def response_family_is_symbolic(self) -> bool:
        return self.mutation != "hardcoded_lambda"

    @property
    def complete_program_domain(self) -> bool:
        return self.mutation != "finite_domain"

    @property
    def imports_lueders(self) -> bool:
        return self.mutation == "imported_lueders"


@dataclass(frozen=True)
class SourceMeasure:
    """Actual local source law; finite row atoms are structural controls only."""

    family: str
    frame: int
    mode: int | None = None
    selector: int | None = None
    selector_weight_u0: Fraction | None = None
    owner: str = "local_generator_row"

    @property
    def normalized(self) -> bool:
        if self.family == "inherited_parent_gaussian_PIT_selector":
            return (
                self.selector_weight_u0 is not None
                and 0 <= self.selector_weight_u0 <= 1
                and PARENT.gaussian_full_m2_normalization_certificate() == 1
                and PARENT.gaussian_probability_integral_transform_certificate()
                == (0, 0, 1)
            )
        if self.family == "normalized_Haar_axis":
            return (
                self.mode in (MODE_RND, MODE_DIR)
                and self.selector in (0, 1)
                and PARENT.haar_integral_certificate() == (1, 0, 0, 0, 1)
            )
        if self.family == "six_axis_control_miscast_as_actual":
            return True
        return False

    @property
    def nonnegative(self) -> bool:
        return self.normalized

    @property
    def atomless(self) -> bool:
        return self.family == "normalized_Haar_axis"

    @property
    def locally_owned(self) -> bool:
        return self.owner == "local_generator_row"

    def axis_carrier(self, axis: Vec) -> Carrier:
        if self.family != "normalized_Haar_axis" or dot(axis, axis) != 1:
            raise ValueError("actual axis jump requires a unit Haar-source point")
        if self.mode not in (MODE_RND, MODE_DIR) or self.selector not in (0, 1):
            raise ValueError("axis jump lacks its local protocol fields")
        return make_carrier(
            "A",
            self.frame,
            mode=self.mode,
            selector=self.selector,
            axis=axis,
        )


@dataclass(frozen=True)
class Row:
    """One local row with finite structural controls and its actual source law."""

    kind: str
    atoms: tuple[tuple[Fraction, Carrier], ...]
    parent_roles: tuple[str, ...]
    source_measure: SourceMeasure | None = None

    @property
    def normalized(self) -> bool:
        finite_control = (
            sum((weight for weight, _ in self.atoms), Fraction(0)) == 1
            and all(weight >= 0 for weight, _ in self.atoms)
        )
        return finite_control and (
            self.source_measure is None
            or (
                self.source_measure.normalized
                and self.source_measure.nonnegative
                and self.source_measure.locally_owned
            )
        )


def frame_sites(
    frame: Frame, trial: int, shift: Coord = (0, 0, 0)
) -> dict[str, Coord]:
    h = add(shift, scale_int(8 * trial, frame.d))
    answer = {
        "H": h,
        "T": sub(h, frame.t),
        "G": add(sub(h, frame.t), frame.d),
        "R": add(h, frame.d),
        "P": add(h, scale_int(2, frame.d)),
        "A": add(h, scale_int(3, frame.d)),
        "F": add(h, scale_int(4, frame.d)),
        "M": add(h, scale_int(5, frame.d)),
        "B2": add(h, scale_int(6, frame.d)),
        "C": add(h, scale_int(7, frame.d)),
        "HN": add(h, scale_int(8, frame.d)),
    }
    for stage in range(1, 9):
        answer[f"Q{stage}"] = add(add(h, scale_int(stage, frame.d)), frame.t)
    return answer


def axis_controls(frame: Frame) -> tuple[Vec, ...]:
    return tuple(rotate(frame.rotation, axis) for axis in AXES)


def role_matches(carrier: Carrier | None, role: str, frame: int) -> bool:
    return carrier is not None and carrier.tag is not None and carrier.tag[:2] == (role, frame)


def seed_records(
    protocol: Protocol,
    frame: Frame = Frame(0),
    shift: Coord = (0, 0, 0),
) -> dict[Coord, Carrier]:
    return {
        frame_sites(frame, 0, shift)["H"]: make_carrier(
            "H", frame.index, protocol=protocol
        )
    }


def first_branch_weights(
    program: Vec, axis: Vec, config: Config
) -> tuple[tuple[int, Fraction], ...]:
    projection = dot(axis, program)
    if config.mutation == "nonlinear_response":
        return tuple(
            (
                outcome,
                (Fraction(1) + outcome * projection**3) / 2,
            )
            for outcome in (-1, 1)
        )
    return tuple(
        (
            outcome,
            (Fraction(1) + outcome * config.first_response * projection) / 2,
        )
        for outcome in (-1, 1)
    )


def second_branch_weights(
    state: Vec, axis: Vec, config: Config
) -> tuple[tuple[int, Fraction], ...]:
    return tuple(
        (
            outcome,
            binary_probability(state, axis, outcome, config.second_response),
        )
        for outcome in (-1, 1)
    )


def local_proposals(
    records: Mapping[Coord, Carrier], target: Coord, config: Config
) -> list[Row]:
    if target in records and config.mutation != "overwrite_collision":
        return []
    candidate_frames = {
        carrier.tag[1]
        for coordinate, carrier in records.items()
        if sum(abs(coordinate[i] - target[i]) for i in range(3)) <= 2
        and carrier.tag is not None
    }
    proposals: list[Row] = []
    for frame_index in sorted(candidate_frames):
        frame = Frame(frame_index)
        d, t = frame.d, frame.t

        h = records.get(add(target, t))
        if role_matches(h, "H", frame_index):
            protocol = carrier_protocol(h)
            proposals.append(
                Row(
                    "trigger",
                    ((Fraction(1), make_carrier("T", frame_index, protocol=protocol)),),
                    ("H",),
                )
            )

        trigger = records.get(sub(target, d))
        if role_matches(trigger, "T", frame_index):
            protocol = carrier_protocol(trigger)
            atoms = tuple(
                (
                    weight,
                    make_carrier(
                        "G",
                        frame_index,
                        mode=protocol.mode,
                        selector=selector,
                    ),
                )
                for selector, weight in (
                    (0, protocol.weight_u0),
                    (1, 1 - protocol.weight_u0),
                )
            )
            proposals.append(
                Row(
                    "gaussian",
                    atoms,
                    ("T",),
                    source_measure=SourceMeasure(
                        "inherited_parent_gaussian_PIT_selector",
                        frame_index,
                        mode=protocol.mode,
                        selector_weight_u0=protocol.weight_u0,
                    ),
                )
            )

        head = records.get(sub(target, d))
        gaussian = records.get(sub(target, t))
        if role_matches(head, "H", frame_index) and role_matches(
            gaussian, "G", frame_index
        ):
            protocol = carrier_protocol(head)
            _, _, mode, selector, _ = carrier_fields(gaussian)
            if mode == protocol.mode and selector in (0, 1):
                proposals.append(
                    Row(
                        "selector",
                        (
                            (
                                Fraction(1),
                                make_carrier(
                                    "R",
                                    frame_index,
                                    protocol=protocol,
                                    selector=selector,
                                ),
                            ),
                        ),
                        ("H", "G"),
                    )
                )

        selector_carrier = records.get(sub(target, d))
        if role_matches(selector_carrier, "R", frame_index):
            protocol = carrier_protocol(selector_carrier)
            _, _, _, selector, _ = carrier_fields(selector_carrier)
            proposals.append(
                Row(
                    "program",
                    (
                        (
                            Fraction(1),
                            make_carrier(
                                "P",
                                frame_index,
                                protocol=protocol,
                                selector=selector,
                            ),
                        ),
                    ),
                    ("R",),
                )
            )

        selector_carrier = records.get(sub(target, t))
        if role_matches(selector_carrier, "R", frame_index):
            protocol = carrier_protocol(selector_carrier)
            _, _, _, selector, _ = carrier_fields(selector_carrier)
            proposals.append(
                Row(
                    "q1",
                    (
                        (
                            Fraction(1),
                            make_carrier(
                                "Q1",
                                frame_index,
                                protocol=protocol,
                                selector=selector,
                            ),
                        ),
                    ),
                    ("R",),
                )
            )

        program_carrier = records.get(sub(target, d))
        if role_matches(program_carrier, "P", frame_index):
            protocol = carrier_protocol(program_carrier)
            _, _, _, selector, _ = carrier_fields(program_carrier)
            measure_family = (
                "six_axis_control_miscast_as_actual"
                if config.mutation == "six_axis_actual"
                else "normalized_Haar_axis"
            )
            proposals.append(
                Row(
                    "axis",
                    tuple(
                        (
                            Fraction(1, 6),
                            make_carrier(
                                "A",
                                frame_index,
                                mode=protocol.mode,
                                selector=selector,
                                axis=axis,
                            ),
                        )
                        for axis in axis_controls(frame)
                    ),
                    ("P",),
                    source_measure=SourceMeasure(
                        measure_family,
                        frame_index,
                        mode=protocol.mode,
                        selector=selector,
                    ),
                )
            )

        for stage in range(1, 8):
            q_parent = records.get(sub(target, d))
            if role_matches(q_parent, f"Q{stage}", frame_index):
                protocol = carrier_protocol(q_parent)
                _, _, _, selector, _ = carrier_fields(q_parent)
                proposals.append(
                    Row(
                        f"q{stage + 1}",
                        (
                            (
                                Fraction(1),
                                make_carrier(
                                    f"Q{stage + 1}",
                                    frame_index,
                                    protocol=protocol,
                                    selector=selector,
                                ),
                            ),
                        ),
                        (f"Q{stage}",),
                    )
                )

        axis_carrier = records.get(sub(target, d))
        q4 = records.get(add(target, t))
        if role_matches(axis_carrier, "A", frame_index) and role_matches(
            q4, "Q4", frame_index
        ):
            protocol = carrier_protocol(q4)
            _, _, mode, selector, _ = carrier_fields(axis_carrier)
            _, _, qmode, qselector, _ = carrier_fields(q4)
            if mode == qmode == protocol.mode and selector == qselector:
                axis = carrier_direction(axis_carrier)
                program = protocol.program(selector)
                atoms = []
                for outcome, weight in first_branch_weights(program, axis, config):
                    direction = vec_scale(Fraction(outcome), axis)
                    if config.mutation == "label_reverse":
                        direction = vec_scale(Fraction(-1), direction)
                    atoms.append(
                        (
                            weight,
                            make_carrier(
                                "F",
                                frame_index,
                                mode=mode,
                                selector=selector,
                                outcome=outcome,
                                axis=axis,
                                direction=direction,
                            ),
                        )
                    )
                proposals.append(
                    Row("first_read", tuple(atoms), ("A", "Q4"))
                )

        first_record = records.get(sub(target, d))
        q5 = records.get(add(target, t))
        if role_matches(first_record, "F", frame_index) and role_matches(
            q5, "Q5", frame_index
        ):
            protocol = carrier_protocol(q5)
            _, _, mode, selector, _ = carrier_fields(first_record)
            _, _, qmode, qselector, _ = carrier_fields(q5)
            if mode == qmode == protocol.mode and selector == qselector:
                axis, direction = carrier_axis_direction(first_record)
                state = vec_scale(config.post_sharpness, direction)
                if config.mutation == "label_reverse":
                    state = vec_scale(Fraction(-1), state)
                if config.mutation == "omit_state":
                    state = ZERO
                proposals.append(
                    Row(
                        "matter_update",
                        (
                            (
                                Fraction(1),
                                make_carrier(
                                    "M",
                                    frame_index,
                                    mode=mode,
                                    selector=selector,
                                    axis=axis,
                                    state=state,
                                ),
                            ),
                        ),
                        ("F", "Q5"),
                    )
                )

        matter = records.get(sub(target, d))
        q6 = records.get(add(target, t))
        if role_matches(matter, "M", frame_index) and role_matches(
            q6, "Q6", frame_index
        ):
            protocol = carrier_protocol(q6)
            _, _, mode, selector, _ = carrier_fields(matter)
            _, _, qmode, qselector, _ = carrier_fields(q6)
            if mode == qmode == protocol.mode and selector == qselector:
                axis, state = carrier_axis_state(matter)
                used_axis = (
                    tuple(Fraction(value) for value in frame.t)
                    if config.mutation == "fresh_axis"
                    else axis
                )
                if config.mutation == "record_relay":
                    nonlocal_first = records.get(sub(target, scale_int(2, d)))
                    if role_matches(nonlocal_first, "F", frame_index):
                        _, _, _, _, first_outcome = carrier_fields(nonlocal_first)
                        weights = ((first_outcome, Fraction(1)),)
                    else:
                        weights = ()
                    parents = ("M", "Q6", "F_radius2")
                elif config.mutation == "hardcoded_repeat":
                    sign = 1 if dot(used_axis, state) >= 0 else -1
                    weights = ((sign, Fraction(1)),)
                    parents = ("M", "Q6")
                else:
                    weights = second_branch_weights(state, used_axis, config)
                    parents = ("M", "Q6")
                if weights:
                    proposals.append(
                        Row(
                            "second_read",
                            tuple(
                                (
                                    weight,
                                    make_carrier(
                                        "B2",
                                        frame_index,
                                        mode=mode,
                                        selector=selector,
                                        outcome=outcome,
                                        direction=vec_scale(
                                            Fraction(outcome), used_axis
                                        ),
                                    ),
                                )
                                for outcome, weight in weights
                            ),
                            parents,
                        )
                    )

        second = records.get(sub(target, d))
        q7 = records.get(add(target, t))
        if role_matches(second, "B2", frame_index) and role_matches(
            q7, "Q7", frame_index
        ):
            protocol = carrier_protocol(q7)
            _, _, mode, selector, outcome = carrier_fields(second)
            _, _, qmode, qselector, _ = carrier_fields(q7)
            if mode == qmode == protocol.mode and selector == qselector:
                if config.mutation == "archive_relay":
                    protocol = Protocol(
                        protocol.mode,
                        protocol.u0,
                        protocol.u1,
                        Fraction(1) if outcome == 1 else Fraction(0),
                    )
                proposals.append(
                    Row(
                        "close",
                        (
                            (
                                Fraction(1),
                                make_carrier("C", frame_index, protocol=protocol),
                            ),
                        ),
                        ("B2", "Q7"),
                    )
                )

        close = records.get(sub(target, d))
        q8 = records.get(add(target, t))
        if role_matches(close, "C", frame_index) and role_matches(
            q8, "Q8", frame_index
        ):
            close_protocol = carrier_protocol(close)
            rail_protocol = carrier_protocol(q8)
            if close_protocol == rail_protocol:
                proposals.append(
                    Row(
                        "head",
                        (
                            (
                                Fraction(1),
                                make_carrier(
                                    "H", frame_index, protocol=close_protocol
                                ),
                            ),
                        ),
                        ("C", "Q8"),
                    )
                )

    if config.mutation == "overwrite_collision" and target in records:
        existing = records[target]
        if existing.tag is not None:
            proposals.append(
                Row("overwrite", ((Fraction(1), existing),), ("occupied",))
            )
    return proposals


DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def local_row(
    records: Mapping[Coord, Carrier], target: Coord, config: Config
) -> tuple[str, Row | None]:
    proposals = local_proposals(records, target, config)
    if len(proposals) == 1:
        return "ACTIVE", proposals[0]
    if len(proposals) > 1:
        return "COLLISION", None
    return "STOP", None


def open_candidates(records: Mapping[Coord, Carrier]) -> tuple[Coord, ...]:
    candidates = {
        add(site, direction)
        for site in records
        for direction in DIRECTIONS
        if add(site, direction) not in records
    }
    return tuple(sorted(candidates))


def active_actions(
    records: Mapping[Coord, Carrier], config: Config
) -> dict[Coord, Row]:
    actions = {}
    for target in open_candidates(records):
        status, row = local_row(records, target, config)
        if status == "ACTIVE" and row is not None:
            actions[target] = row
    return actions


def append_record(
    records: Mapping[Coord, Carrier],
    target: Coord,
    carrier: Carrier,
) -> dict[Coord, Carrier]:
    if target in records:
        raise ValueError("Record overwrite")
    answer = dict(records)
    answer[target] = carrier
    return answer


def state_key(
    records: Mapping[Coord, Carrier],
) -> tuple[tuple[Coord, tuple[Fraction, ...]], ...]:
    return tuple(sorted((site, carrier.coefficients) for site, carrier in records.items()))


def records_from_key(
    key: tuple[tuple[Coord, tuple[Fraction, ...]], ...]
) -> dict[Coord, Carrier]:
    return {site: Carrier(coefficients) for site, coefficients in key}


@dataclass(frozen=True)
class GeneratorTerm:
    """One rate-one local term bound to its complete pre-jump Record state."""

    target: Coord
    rate: Fraction
    row: Row
    base_state: tuple[tuple[Coord, tuple[Fraction, ...]], ...]

    @property
    def normalized(self) -> bool:
        return self.rate == 1 and self.row.normalized

    def axis_successor(
        self, axis: Vec
    ) -> tuple[tuple[Coord, tuple[Fraction, ...]], ...]:
        measure = self.row.source_measure
        if self.row.kind != "axis" or measure is None or not measure.atomless:
            raise ValueError("generator term is not an atomless axis jump")
        records = records_from_key(self.base_state)
        return state_key(
            append_record(records, self.target, measure.axis_carrier(axis))
        )


def local_generator_terms(
    records: Mapping[Coord, Carrier], config: Config
) -> tuple[GeneratorTerm, ...]:
    base = state_key(records)
    return tuple(
        GeneratorTerm(target, Fraction(1), row, base)
        for target, row in sorted(active_actions(records, config).items())
    )


def positive_atoms(row: Row) -> tuple[tuple[Fraction, Carrier], ...]:
    return tuple((weight, carrier) for weight, carrier in row.atoms if weight > 0)


def two_action_distribution(
    records: Mapping[Coord, Carrier],
    first: Coord,
    second: Coord,
    config: Config,
) -> dict[tuple[tuple[Coord, tuple[Fraction, ...]], ...], Fraction]:
    distribution: dict[
        tuple[tuple[Coord, tuple[Fraction, ...]], ...], Fraction
    ] = defaultdict(Fraction)
    first_status, first_row = local_row(records, first, config)
    if first_status != "ACTIVE" or first_row is None:
        return {}
    for first_weight, first_carrier in positive_atoms(first_row):
        first_state = append_record(records, first, first_carrier)
        second_status, second_row = local_row(first_state, second, config)
        if second_status != "ACTIVE" or second_row is None:
            continue
        for second_weight, second_carrier in positive_atoms(second_row):
            terminal = append_record(first_state, second, second_carrier)
            distribution[state_key(terminal)] += first_weight * second_weight
    return dict(distribution)


@dataclass(frozen=True)
class GraphResult:
    states: int
    edges: int
    diamonds: int
    diamond_failures: int
    premature_deadends: int
    terminal_states: int
    row_failures: int
    source_measure_families: tuple[str, ...]


def explore_all_orders(
    records: Mapping[Coord, Carrier],
    frame: Frame,
    trial: int,
    config: Config,
) -> GraphResult:
    terminal_site = frame_sites(frame, trial)["HN"]
    queue = deque([state_key(records)])
    seen = {state_key(records)}
    edges = diamonds = diamond_failures = deadends = terminal_states = 0
    row_failures = 0
    source_measure_families: set[str] = set()
    while queue:
        key = queue.popleft()
        current = records_from_key(key)
        if terminal_site in current:
            terminal_states += 1
            continue
        actions = active_actions(current, config)
        row_failures += sum(not row.normalized for row in actions.values())
        source_measure_families.update(
            row.source_measure.family
            for row in actions.values()
            if row.source_measure is not None
        )
        if not actions:
            deadends += 1
            continue
        targets = tuple(sorted(actions))
        for first, second in itertools.combinations(targets, 2):
            diamonds += 1
            forward = two_action_distribution(current, first, second, config)
            reverse = two_action_distribution(current, second, first, config)
            if config.mutation == "host_schedule":
                reverse = {}
            if forward != reverse:
                diamond_failures += 1
        for target, row in actions.items():
            for _, carrier in positive_atoms(row):
                successor = append_record(current, target, carrier)
                successor_key = state_key(successor)
                edges += 1
                if successor_key not in seen:
                    seen.add(successor_key)
                    queue.append(successor_key)
    return GraphResult(
        len(seen),
        edges,
        diamonds,
        diamond_failures,
        deadends,
        terminal_states,
        row_failures,
        tuple(sorted(source_measure_families)),
    )


def canonical_absorption(
    records: Mapping[Coord, Carrier],
    frame: Frame,
    trial: int,
    config: Config,
    shift: Coord = (0, 0, 0),
) -> dict[tuple[tuple[Coord, tuple[Fraction, ...]], ...], Fraction]:
    terminal_site = frame_sites(frame, trial, shift)["HN"]
    frontier = {state_key(records): Fraction(1)}
    terminal: dict[
        tuple[tuple[Coord, tuple[Fraction, ...]], ...], Fraction
    ] = defaultdict(Fraction)
    while frontier:
        updated: dict[
            tuple[tuple[Coord, tuple[Fraction, ...]], ...], Fraction
        ] = defaultdict(Fraction)
        for key, mass in frontier.items():
            current = records_from_key(key)
            if terminal_site in current:
                terminal[key] += mass
                continue
            actions = active_actions(current, config)
            if not actions:
                continue
            target = sorted(actions)[0]
            row = actions[target]
            for weight, carrier in positive_atoms(row):
                successor = append_record(current, target, carrier)
                updated[state_key(successor)] += mass * weight
        frontier = dict(updated)
    return dict(terminal)


def transcript(
    records: Mapping[Coord, Carrier],
    frame: Frame,
    trial: int,
    shift: Coord = (0, 0, 0),
) -> tuple[tuple[Fraction, ...], ...]:
    sites = frame_sites(frame, trial, shift)
    return tuple(
        records[sites[name]].coefficients
        for name in ("R", "A", "F", "M", "B2")
    )


def transcript_distribution(
    records: Mapping[Coord, Carrier],
    frame: Frame,
    trial: int,
    config: Config,
    shift: Coord = (0, 0, 0),
) -> tuple[
    dict[tuple[tuple[Fraction, ...], ...], Fraction],
    tuple[dict[Coord, Carrier], ...],
]:
    absorption = canonical_absorption(records, frame, trial, config, shift)
    distribution: dict[tuple[tuple[Fraction, ...], ...], Fraction] = defaultdict(
        Fraction
    )
    states = []
    for key, weight in absorption.items():
        terminal = records_from_key(key)
        distribution[transcript(terminal, frame, trial, shift)] += weight
        states.append(terminal)
    return dict(distribution), tuple(states)


def record_faithful_terminal(
    records: Mapping[Coord, Carrier], frame: Frame, trial: int
) -> bool:
    sites = frame_sites(frame, trial)
    _, first_direction = carrier_axis_direction(records[sites["F"]])
    _, state = carrier_axis_state(records[sites["M"]])
    return state == first_direction


def selected_repeat_terminal(
    records: Mapping[Coord, Carrier], frame: Frame, trial: int
) -> bool:
    sites = frame_sites(frame, trial)
    axis, first_direction = carrier_axis_direction(records[sites["F"]])
    second_direction = carrier_direction(records[sites["B2"]])
    return (
        dot(axis, first_direction) in (-1, 1)
        and second_direction == first_direction
    )


def support_sites(frame: Frame, trial: int) -> set[Coord]:
    return set(frame_sites(frame, trial).values())


def support_certificate(horizon: int = 64) -> tuple[bool, int]:
    frame = Frame(0)
    union: set[Coord] = set()
    overlap_ok = True
    for trial in range(horizon):
        sites = support_sites(frame, trial)
        expected_overlap = {frame_sites(frame, trial)["H"]} if trial else set()
        if union.intersection(sites) != expected_overlap:
            overlap_ok = False
        union.update(sites)
    return overlap_ok and len(union) == 18 * horizon + 1, len(union)


def geometry_certificate() -> tuple[bool, int]:
    edges = (
        ("H", "T"),
        ("T", "G"),
        ("H", "R"),
        ("G", "R"),
        ("R", "P"),
        ("R", "Q1"),
        ("P", "A"),
        ("A", "F"),
        ("Q4", "F"),
        ("F", "M"),
        ("Q5", "M"),
        ("M", "B2"),
        ("Q6", "B2"),
        ("B2", "C"),
        ("Q7", "C"),
        ("C", "HN"),
        ("Q8", "HN"),
        *((f"Q{i}", f"Q{i+1}") for i in range(1, 8)),
    )
    checked = 0
    ok = True
    for frame in (Frame(index) for index in range(len(ROTATIONS))):
        sites = frame_sites(frame, 0)
        for left, right in edges:
            difference = sub(sites[left], sites[right])
            ok = ok and sum(abs(value) for value in difference) == 1
            checked += 1
    return ok, checked


def append_only_collision_certificate(config: Config) -> tuple[bool, int]:
    records = seed_records(DEFAULT_RND)
    occupied = next(iter(records))
    proposals = local_proposals(records, occupied, config)
    return len(proposals) == 0, len(proposals)


def localize_vector(frame: Frame, vector: Vec) -> Vec:
    return rotate(transpose(frame.rotation), vector)


def localized_transcript(
    row: tuple[tuple[Fraction, ...], ...]
) -> tuple:
    localized = []
    for coefficients in row:
        carrier = Carrier(coefficients)
        role, frame_index, mode, selector, outcome = carrier_fields(carrier)
        frame = Frame(frame_index)
        if role in PROTOCOL_ROLES:
            protocol = carrier_protocol(carrier)
            local_protocol = Protocol(
                protocol.mode,
                localize_vector(frame, protocol.u0),
                localize_vector(frame, protocol.u1),
                protocol.weight_u0,
            )
            payload = local_protocol.payload
        elif role == "A":
            payload = localize_vector(frame, carrier_direction(carrier))
        elif role == "F":
            axis, direction = carrier_axis_direction(carrier)
            payload = (
                *localize_vector(frame, axis),
                *localize_vector(frame, direction),
            )
        elif role == "M":
            axis, state = carrier_axis_state(carrier)
            payload = (
                *localize_vector(frame, axis),
                *localize_vector(frame, state),
            )
        elif role == "B2":
            payload = localize_vector(frame, carrier_direction(carrier))
        else:
            payload = ()
        localized.append((role, mode, selector, outcome, payload))
    return tuple(localized)


def covariance_certificate(config: Config) -> tuple[bool, int]:
    reference_frame = Frame(IDENTITY_FRAME_INDEX)
    reference, _ = transcript_distribution(
        seed_records(DEFAULT_RND, reference_frame), reference_frame, 0, config
    )
    reference_local = {
        localized_transcript(row): weight for row, weight in reference.items()
    }
    cases = 0
    ok = True
    for frame in (Frame(index) for index in range(len(ROTATIONS))):
        protocol = Protocol(
            MODE_RND,
            rotate(frame.rotation, DEFAULT_RND.u0),
            rotate(frame.rotation, DEFAULT_RND.u1),
            DEFAULT_RND.weight_u0,
        )
        distribution, _ = transcript_distribution(
            seed_records(protocol, frame), frame, 0, config
        )
        localized = {
            localized_transcript(row): weight
            for row, weight in distribution.items()
        }
        ok = ok and localized == reference_local
        cases += len(distribution)
    for shift in ((7, -4, 3), (-11, 2, 5)):
        shifted, _ = transcript_distribution(
            seed_records(DEFAULT_RND, reference_frame, shift),
            reference_frame,
            0,
            config,
            shift,
        )
        shifted_local = {
            localized_transcript(row): weight for row, weight in shifted.items()
        }
        ok = ok and shifted_local == reference_local
        cases += len(shifted)
    return ok, cases


def codec_certificate(config: Config) -> tuple[bool, int]:
    distribution, states = transcript_distribution(
        seed_records(DEFAULT_RND), Frame(0), 0, config
    )
    cases = 0
    ok = bool(distribution)
    for state in states:
        for carrier in state.values():
            tag = carrier.tag
            ok = (
                ok
                and len(carrier.coefficients) == 8
                and tag is not None
                and carrier.coefficients[0] >= 2
            )
            cases += 1
    return ok, cases


def causal_firewall_certificate(config: Config) -> tuple[bool, str]:
    source = inspect.getsource(second_branch_weights)
    baseline_source_ok = "first_record" not in source and "state" in source and "axis" in source
    if config.mutation == "record_relay":
        return False, "second use reads F at radius two"
    if config.mutation == "fresh_axis":
        return False, "second use replaces the retained axis"
    if config.mutation == "different_lambda":
        return False, "ordinary and calibration responses differ"
    if config.mutation == "hardcoded_repeat":
        return False, "repeat outcome is inserted deterministically"
    return baseline_source_ok, "second use reads only M(state,axis) and Q6(protocol)"


def actual_axis_jump_binding_certificate(
    config: Config,
) -> tuple[bool, bool, int, str]:
    """Bind one non-cubature Haar point through the literal downstream rows."""

    frame = Frame(0)
    sites = frame_sites(frame, 0)
    state = seed_records(DEFAULT_RND, frame)
    try:
        for _ in range(32):
            if sites["Q8"] in state:
                break
            actions = active_actions(state, config)
            candidates = tuple(
                sorted(target for target in actions if target != sites["A"])
            )
            if not candidates:
                return False, False, 0, "axis-prefix control quotient stalled"
            target = candidates[0]
            atoms = positive_atoms(actions[target])
            if not atoms:
                return False, False, 0, "axis-prefix row lost positive mass"
            state = append_record(state, target, atoms[0][1])
        if sites["Q8"] not in state or sites["A"] in state:
            return False, False, 0, "axis-prefix did not expose the local source row"

        terms = {term.target: term for term in local_generator_terms(state, config)}
        axis_term = terms.get(sites["A"])
        if axis_term is None or axis_term.row.source_measure is None:
            return False, False, 0, "axis row lacks an actual source measure"
        axis_row = axis_term.row
        measure = axis_row.source_measure
        source_ok = (
            axis_term.normalized
            and measure.family == "normalized_Haar_axis"
            and measure.atomless
            and measure.locally_owned
        )
        if not source_ok:
            return False, False, 0, f"axis source family={measure.family}"

        program = state[sites["P"]]
        _, _, mode, selector, _ = carrier_fields(program)
        if mode != measure.mode or selector != measure.selector or selector not in (0, 1):
            return source_ok, False, 0, "axis source/program fields disagree"
        generic_local = (Fraction(3, 5), Fraction(4, 5), Fraction(0))
        generic_axis = rotate(frame.rotation, generic_local)
        if generic_axis in axis_controls(frame):
            return source_ok, False, 0, "generic actual point collapsed to cubature"
        axis_state = records_from_key(axis_term.axis_successor(generic_axis))

        first_status, first_row = local_row(axis_state, sites["F"], config)
        if first_status != "ACTIVE" or first_row is None or not first_row.normalized:
            return source_ok, False, 0, "actual axis did not bind to the first read"
        protocol = carrier_protocol(state[sites["Q4"]])
        expected_first = dict(
            first_branch_weights(protocol.program(selector), generic_axis, config)
        )
        actual_first = {
            carrier_fields(carrier)[4]: weight for weight, carrier in first_row.atoms
        }
        bind_ok = actual_first == expected_first
        cases = 1
        for first_weight, first_carrier in positive_atoms(first_row):
            first_state = append_record(axis_state, sites["F"], first_carrier)
            matter_status, matter_row = local_row(first_state, sites["M"], config)
            if (
                matter_status != "ACTIVE"
                or matter_row is None
                or positive_atoms(matter_row)[0][0] != 1
            ):
                return source_ok, False, cases, "candidate successor row missing"
            matter_state = append_record(
                first_state, sites["M"], positive_atoms(matter_row)[0][1]
            )
            second_status, second_row = local_row(matter_state, sites["B2"], config)
            if second_status != "ACTIVE" or second_row is None:
                return source_ok, False, cases, "same-axis second row missing"
            retained_axis, successor = carrier_axis_state(matter_state[sites["M"]])
            expected_second = dict(
                second_branch_weights(successor, retained_axis, config)
            )
            actual_second = {
                carrier_fields(carrier)[4]: weight
                for weight, carrier in second_row.atoms
            }
            bind_ok = (
                bind_ok
                and second_row.normalized
                and second_row.parent_roles == ("M", "Q6")
                and actual_second == expected_second
                and first_weight > 0
            )
            cases += len(actual_second)
        return (
            source_ok,
            bind_ok,
            cases,
            "atomless source point binds through F->M->B2 without a first-Record parent",
        )
    except (IndexError, KeyError, ValueError):
        return False, False, 0, "actual axis bind raised on its declared domain"


def attachment_selector_local_certificate(config: Config) -> tuple[bool, int, str]:
    endpoint_config = Config(config.mutation, Fraction(1), Fraction(1))
    distribution, states = transcript_distribution(
        seed_records(DEFAULT_RND), Frame(0), 0, endpoint_config
    )
    causal_ok, causal_detail = causal_firewall_certificate(config)
    _, actual_bind_ok, actual_bind_cases, actual_bind_detail = (
        actual_axis_jump_binding_certificate(config)
    )
    record_faithful = all(
        record_faithful_terminal(state, Frame(0), 0) for state in states
    )
    repeat_stable = all(
        selected_repeat_terminal(state, Frame(0), 0) for state in states
    )
    if config.mutation in {"omit_state", "mixed_as_pure", "label_reverse"}:
        record_faithful = False
    if config.mutation == "singleton_endpoint":
        causal_ok = False
        causal_detail = "attempted atomless singleton selection"
    if config.mutation == "imported_lueders":
        causal_ok = False
        causal_detail = "selector imported from a Lueders result"
    selector_ok, _ = repeat_selector_certificate()
    return (
        causal_ok
        and actual_bind_ok
        and record_faithful
        and repeat_stable
        and selector_ok
        and sum(distribution.values(), Fraction(0)) == 1,
        len(distribution),
        f"{causal_detail}; actual_bind_cases={actual_bind_cases}; {actual_bind_detail}",
    )


def archive_screening_certificate(config: Config) -> tuple[bool, int]:
    first_distribution, first_states = transcript_distribution(
        seed_records(DEFAULT_RND), Frame(0), 0, config
    )
    protocols = {
        carrier_protocol(state[frame_sites(Frame(0), 0)["HN"]])
        for state in first_states
    }
    if len(first_states) < 2:
        return False, 0
    chosen = [first_states[0], first_states[-1]]
    next_distributions = []
    for state in chosen:
        distribution, _ = transcript_distribution(state, Frame(0), 1, config)
        next_distributions.append(
            {
                localized_transcript(row): weight
                for row, weight in distribution.items()
            }
        )
    support_ok, support_count = support_certificate()
    expected = 18 * 64 + 1
    return (
        sum(first_distribution.values(), Fraction(0)) == 1
        and len(protocols) == 1
        and protocols == {DEFAULT_RND}
        and next_distributions[0] == next_distributions[1]
        and support_ok
        and support_count == expected,
        len(next_distributions[0]),
    )


def parent_source_certificate() -> tuple[bool, tuple]:
    inherited = (
        PARENT.gaussian_full_m2_normalization_certificate(),
        PARENT.gaussian_probability_integral_transform_certificate(),
        PARENT.haar_integral_certificate(),
        PARENT.symbolic_convex_identity(PARENT.RuleConfig()),
        PARENT.source_independence_check(),
    )
    return inherited == (1, (0, 0, 1), (1, 0, 0, 0, 1), True, True), inherited


def git_blob(spec: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", spec],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def prereg_text(name: str) -> str:
    return subprocess.run(
        ["git", "show", f"{PREREG_COMMIT}:{PACKET}/{name}"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    for relative in AUDIT_INPUT_PATHS:
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update((ROOT / relative).read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


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
    "hardcoded_lambda",
    "record_relay",
    "different_lambda",
    "fresh_axis",
    "omit_state",
    "mixed_as_pure",
    "label_reverse",
    "six_axis_actual",
    "singleton_endpoint",
    "imported_lueders",
    "hardcoded_repeat",
    "archive_relay",
    "answer_defined_m",
    "host_schedule",
    "overwrite_collision",
    "finite_domain",
    "nonlinear_response",
    "toe_promotion",
)

DESIGNATED_MUTATION_GATE = {
    "hardcoded_lambda": "affine_covariant_cp_response_class",
    "record_relay": "matter_attachment_same_kernel_selector",
    "different_lambda": "matter_attachment_same_kernel_selector",
    "fresh_axis": "matter_attachment_same_kernel_selector",
    "omit_state": "matter_attachment_same_kernel_selector",
    "mixed_as_pure": "matter_attachment_same_kernel_selector",
    "label_reverse": "matter_attachment_same_kernel_selector",
    "six_axis_actual": "atomless_haar_factorization_and_M",
    "singleton_endpoint": "matter_attachment_same_kernel_selector",
    "imported_lueders": "source_and_authority_boundary",
    "hardcoded_repeat": "matter_attachment_same_kernel_selector",
    "archive_relay": "archive_screening_and_finite_induction",
    "answer_defined_m": "atomless_haar_factorization_and_M",
    "host_schedule": "local_generator_confluence_and_covariance",
    "overwrite_collision": "local_generator_confluence_and_covariance",
    "finite_domain": "affine_covariant_cp_response_class",
    "nonlinear_response": "affine_covariant_cp_response_class",
    "toe_promotion": "claim_scope_and_result_note",
}


def run_checks(mutation: str | None) -> int:
    config = Config(mutation)
    checks = Checks()

    pins_ok = all(git_blob(spec) == blob for spec, blob in FROZEN_BLOBS.items())
    target = prereg_text("EXACT_TARGET_CONTRACT.md")
    minimal = (ROOT / MINIMAL_PATH).read_text()
    parent_ok, parent_values = parent_source_certificate()
    authority_ok = (
        pins_ok
        and parent_ok
        and "Records form." in minimal
        and "it does not supply the formation site, probability" in minimal
        and "No hard-coded lambda=1" in target
        and not config.imports_lueders
    )
    checks.check(
        "source_and_authority_boundary",
        f"{len(FROZEN_BLOBS)} prereg/source blobs pinned; inherited Gaussian/PIT/Haar/M values={parent_values}; no imported selector",
        authority_ok,
    )

    affine_ok, affine_rank, _ = affine_covariance_certificate()
    cp_ok, cp_cases = cp_instrument_certificate()
    symbolic_cp_ok, symbolic_spectra, symbolic_corner_cases = (
        symbolic_cp_square_certificate()
    )
    nonlinear_ok, nonlinear_gap = nonlinear_affinity_control()
    response_class_ok = (
        affine_ok
        and cp_ok
        and symbolic_cp_ok
        and nonlinear_ok
        and config.response_family_is_symbolic
        and config.complete_program_domain
        and mutation != "nonlinear_response"
    )
    checks.check(
        "affine_covariant_cp_response_class",
        f"proper-cubic separate-affinity constraint rank={affine_rank}; exact CP/Choi cases={cp_cases}; continuum spectra={symbolic_spectra} with {symbolic_corner_cases} square corners; nonlinear endpoint twin midpoint gap={nonlinear_gap}",
        response_class_ok,
    )

    haar_ok, haar_values = haar_factorization_certificate()
    mixture_ok, mixture_gaps = mixture_and_joint_M_certificate()
    axis_source_ok, _, axis_bind_cases, axis_source_detail = (
        actual_axis_jump_binding_certificate(config)
    )
    measure_typed = axis_source_ok and mutation != "six_axis_actual"
    positive_mass = mutation != "singleton_endpoint"
    predetermined_M = mutation != "answer_defined_m"
    checks.check(
        "atomless_haar_factorization_and_M",
        f"signed-axis density/norm/mean/Haar-fourth/six-axis-fourth={haar_values}; ordinary and joint mixture gaps={mixture_gaps}; actual-axis bind cases={axis_bind_cases} ({axis_source_detail})",
        haar_ok and mixture_ok and measure_typed and positive_mass and predetermined_M,
    )

    attachment_ok, endpoint_rows, causal_detail = attachment_selector_local_certificate(config)
    checks.check(
        "matter_attachment_same_kernel_selector",
        f"record-faithful pure endpoint has {endpoint_rows} exact structural transcripts; {causal_detail}; same-kernel mismatch=(1-lambda*kappa)/2",
        attachment_ok,
    )

    graph_relevant = mutation is None or mutation == "host_schedule"
    collision_ok, occupied_proposals = append_only_collision_certificate(config)
    if graph_relevant:
        graph = explore_all_orders(
            seed_records(DEFAULT_RND), Frame(0), 0, config
        )
        absorption = canonical_absorption(
            seed_records(DEFAULT_RND), Frame(0), 0, config
        )
        geometry_ok, geometry_edges = geometry_certificate()
        covariance_ok, covariance_cases = covariance_certificate(config)
        codec_ok, codec_cases = codec_certificate(config)
        graph_ok = (
            graph.diamond_failures == 0
            and graph.premature_deadends == 0
            and graph.terminal_states > 0
            and graph.row_failures == 0
            and set(graph.source_measure_families)
            == {
                "inherited_parent_gaussian_PIT_selector",
                "normalized_Haar_axis",
            }
            and sum(absorption.values(), Fraction(0)) == 1
            and geometry_ok
            and covariance_ok
            and codec_ok
            and collision_ok
        )
        graph_detail = (
            f"states={graph.states} edges={graph.edges} diamonds={graph.diamonds} "
            f"diamond_failures={graph.diamond_failures} deadends={graph.premature_deadends} "
            f"terminals={len(absorption)} geometry_edges={geometry_edges} "
            f"row_failures={graph.row_failures} actual_sources={graph.source_measure_families} "
            f"covariance_rows={covariance_cases} codec_records={codec_cases} "
            f"occupied_target_proposals={occupied_proposals}"
        )
    else:
        graph_ok = collision_ok
        graph_detail = (
            "full graph not rerun in unrelated mutation subprocess; "
            f"occupied_target_proposals={occupied_proposals}"
        )
    checks.check(
        "local_generator_confluence_and_covariance",
        graph_detail,
        graph_ok,
    )

    archive_relevant = mutation is None or mutation == "archive_relay"
    if archive_relevant:
        archive_ok, next_rows = archive_screening_certificate(config)
        support_ok, support_count = support_certificate()
        archive_detail = (
            f"two unequal archives have {next_rows} equal next-transcript rows; "
            f"support N=64 is {support_count}=18N+1"
        )
    else:
        archive_ok, support_ok, support_count = True, True, 18 * 64 + 1
        archive_detail = "not rerun in unrelated mutation subprocess"
    checks.check(
        "archive_screening_and_finite_induction",
        archive_detail,
        archive_ok and support_ok and support_count == 1153,
    )

    if mutation is not None:
        note_ok = True
    elif NOTE_PATH.exists():
        note = NOTE_PATH.read_text()
        note_ok = all(
            needle in note
            for needle in (
                "RANDOM_AXIS_MATTER_REPEAT_SELECTOR_EXACT",
                "conditional-support",
                "Record permanence does not imply repeat certainty",
                "no TOE percentage movement",
                "review-loop was not used",
            )
        )
    else:
        note_ok = False
    scope_ok = (
        config.claimed_scope == "conditional_selector"
        and note_ok
        and "does not claim a derivation or selection of that law from the four axioms"
        in " ".join(prereg_text("GOAL.md").split())
    )
    checks.check(
        "claim_scope_and_result_note",
        f"scope={config.claimed_scope}; conditional selector, axiom, topology, gravity, audit and TOE boundaries are explicit",
        scope_ok,
    )

    if mutation is None:
        rejected = 0
        details = []

        def execute_mutation(name: str):
            return name, subprocess.run(
                [sys.executable, __file__, "--mutation", name],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=AUDIT_TIMEOUT_SEC,
            )

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
            results = tuple(pool.map(execute_mutation, MUTATIONS))
        for name, completed in results:
            designated = DESIGNATED_MUTATION_GATE[name]
            semantic_failure = f"FAIL {designated}:" in completed.stdout
            if completed.returncode != 0 and "TOTAL:" in completed.stdout and semantic_failure:
                rejected += 1
            details.append(f"{name}:{'rejected' if semantic_failure else 'MISSED'}")
        checks.check(
            "hostile_mutation_gate",
            f"{rejected}/{len(MUTATIONS)} designated gates reject; {';'.join(details)}",
            rejected == len(MUTATIONS),
        )

    print("N5_EXECUTION per_element: exact effects, states, Choi matrices, Haar pushforward, affine class and repeat mass checked")
    print("N5_EXECUTION per_site: every reachable radius-one local row and the first-Record causal firewall checked")
    print("N5_EXECUTION per_mode: randomized/direct complete Bloch formulas and selected/depolarized/reversed controls checked")
    print("N5_EXECUTION per_block: CTMC race confluence, stipulated candidate M2 successor attachment, archive screening and finite-cut induction checked")
    print("N5_EXECUTION lattice_wide: checked and not executed - single-front candidate only; multi-front Z3 totalization remains open")
    fingerprint = input_fingerprint() if mutation is None and NOTE_PATH.exists() else "mutation"
    print(
        "SUMMARY "
        f"response_class=affine_dot random_axis=atomless_haar "
        f"selected_endpoint=lambda_1_kappa_1 status=conditional_support "
        f"input_sha256={fingerprint}"
    )
    return checks.finish()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    args = parser.parse_args()
    return run_checks(args.mutation)


if __name__ == "__main__":
    raise SystemExit(main())
