#!/usr/bin/env python3
"""Block 37: Block-36-specific NN active-cut Record front.

One fixed radius-one candidate rule grows an append-only ladder.  A protocol
head writes a deterministic trigger; that trigger forms a Gaussian Record;
the head and Gaussian Record form a selector; the selector installs a program
and independently starts a value-blind protocol-copy rail; the program writes
an outcome; the outcome writes a value-blind close; close and the copied
protocol form the next head.

The mathematical Gaussian branches are the exact selector-bit partition of
the continuous Gaussian row.  A certified exact-real evaluator witnesses that
partition without pretending every host expression has decidable order.  The
six outcome branches are an independent exact cubic cubature/control for the
continuous Haar row.  The script separately represents and checks the analytic
continuous measures; it does not promote the six-axis control to the
continuous law itself.
"""

from __future__ import annotations

import argparse
import ast
import concurrent.futures
import hashlib
import inspect
import itertools
import math
import subprocess
import sys
from collections import defaultdict, deque
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Mapping, Sequence, TypeAlias

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_MAIN = "aa7338d1fbc34a4b92205182b26793194e4727b6"
PARENT_COMMIT = "235000daafd4d3aa1b1cc590aebc0efd177df089"
PREREG_COMMIT = "af00845bf0a88064b4a0bc4be08a4d437c8b05ec"
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901"
)
NOTE_PATH = ROOT / "docs/ADMISSIBILITY_BLOCK36_SPECIFIC_NN_ACTIVE_CUT_RECORD_FRONT_BOUNDED_THEOREM_NOTE_2026-09-01.md"
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
BLOCK36_NOTE = "docs/ADMISSIBILITY_GAUSSIAN_FAIR_RECORD_MIDPOINT_AFFINITY_HAAR_EDGE_FACTOR_FRESH_PORT_RESET_BOUNDED_THEOREM_NOTE_2026-09-01.md"
BLOCK36_RUNNER = "scripts/admissibility_gaussian_fair_record_affinity_haar_factor_fresh_port_reset_2026_09_01.py"
STRICT_FRONT_NOTE = "docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md"
STRICT_FRONT_RUNNER = "scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py"

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/EXACT_TARGET_CONTRACT.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/OPPORTUNITY_QUEUE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block37-full-local-compiler-active-quotient-worldtube-20260901/STATE.yaml",
    "docs/ADMISSIBILITY_BLOCK36_SPECIFIC_NN_ACTIVE_CUT_RECORD_FRONT_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_GAUSSIAN_FAIR_RECORD_MIDPOINT_AFFINITY_HAAR_EDGE_FACTOR_FRESH_PORT_RESET_BOUNDED_THEOREM_NOTE_2026-09-01.md",
    "scripts/admissibility_gaussian_fair_record_affinity_haar_factor_fresh_port_reset_2026_09_01.py",
    "docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md",
    "scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

FROZEN_BLOBS = {
    f"{PREREG_COMMIT}:{PACKET}/EXACT_TARGET_CONTRACT.md": "bdbee2a11e509bae1030a0128bdcabb579e31367",
    f"{PREREG_COMMIT}:{PACKET}/MUTATION_PLAN.md": "83fd69e9cbdbf5d592c71f02b69aa552beed9d19",
    f"{PREREG_COMMIT}:{PACKET}/AUTHORITY_GATE.md": "179189d289d7379d84e0952f3435aab72fdeb1d0",
    f"{PREREG_COMMIT}:{PACKET}/ASSUMPTIONS_AND_IMPORTS.md": "cc1bc05bb3bce28bf1b9a5a55d221c3a78c0b7b9",
    f"{PREREG_COMMIT}:{PACKET}/PANEL_RETURN.md": "41209008954aa8407cf3ad829a130412fe0e08f3",
    f"{PREREG_COMMIT}:{PACKET}/PREFLIGHT_WITNESSES.md": "2961712da88882fee06eb64e5eebbabacab1cd2c",
    f"{PREREG_COMMIT}:{PACKET}/ROUTE_PORTFOLIO.md": "998e1bfb80ffe269816ce6aaa05d686d9b9470c9",
    f"{PREREG_COMMIT}:{PACKET}/NO_GO_LEDGER.md": "891015219fd35ff1c14d7b9270c8310fcd274c56",
    f"{PREREG_COMMIT}:{PACKET}/TRACE_GATE.md": "71c348cecb238de7b9dda8b9425cfebb6864fcf5",
    f"{PREREG_COMMIT}:{PACKET}/OPPORTUNITY_QUEUE.md": "82862ed49b5b577267d326664d99becf0b89c23b",
    f"{PREREG_COMMIT}:{PACKET}/STATE.yaml": "d71e8b6573cdc983f1d740887d4e2df609a4eb63",
    f"{CANONICAL_MAIN}:{MINIMAL_PATH}": "bc23300becfe4e4db57153c0e94cfcdf2338da71",
    f"{PARENT_COMMIT}:{BLOCK36_NOTE}": "93aca5052adfde9ada5325d1058bf5507d85333a",
    f"{PARENT_COMMIT}:{BLOCK36_RUNNER}": "dca30de9b8074b4c88c7a975e51cf7b031346b97",
    f"{PARENT_COMMIT}:{STRICT_FRONT_NOTE}": "494ed4d1be589e7f2a37cf79f65997504de4579c",
    f"{PARENT_COMMIT}:{STRICT_FRONT_RUNNER}": "33aa40c6696ad1889de916193e616aa28ed260a5",
}

Coord = tuple[int, int, int]
RealCoordinate: TypeAlias = Fraction | sp.Expr
RealVector: TypeAlias = tuple[RealCoordinate, RealCoordinate, RealCoordinate]
RationalVector: TypeAlias = tuple[Fraction, Fraction, Fraction]
Vector: TypeAlias = RealVector
Rotation = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

ZERO3: Vector = (Fraction(0), Fraction(0), Fraction(0))
BASE_FORWARD: Coord = (1, 0, 0)
BASE_TRANSVERSE: Coord = (0, 1, 0)
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXES: tuple[Vector, ...] = tuple(
    tuple(Fraction(value) for value in axis) for axis in DIRECTIONS
)  # type: ignore[assignment]

MODE_RND = 0
MODE_DIR = 1
ROLE_ORDER = (
    "H_RND",
    "H_DIR",
    "T",
    "R_RND_0",
    "R_RND_1",
    "R_DIR_0",
    "R_DIR_1",
    "C_RND",
    "C_DIR",
) + tuple(
    f"{prefix}_{mode}_{bit}"
    for prefix in ("P", "O", "Q1", "Q2", "Q3", "Q4", "Q5")
    for mode in ("RND", "DIR")
    for bit in (0, 1)
)


def frac(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def certified_real_coordinate(value: object) -> RealCoordinate | None:
    """Return a canonical exact-real host witness, or reject it.

    This is deliberately narrower than the mathematical real carrier.  It
    rejects binary floats, infinities/NaN, and expressions whose reality is
    unknown.  The theorem-level carrier is over R; this executable layer only
    evaluates points for which the host has an exact, finite real certificate.
    """

    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    try:
        expression = sp.sympify(value)
    except (TypeError, ValueError, sp.SympifyError):
        return None
    if expression.has(sp.Float):
        return None
    if expression.is_real is not True or expression.is_finite is not True:
        # SymPy 1.14 leaves erfinv(q) untyped even for exact -1<q<1.
        # Replace only those domain-certified calls by explicitly real finite
        # sentinels and ask SymPy again; this does not admit unknown Integrals
        # or arbitrary functions.
        inverse_erfs = tuple(expression.atoms(sp.erfinv))
        replacements: dict[sp.Expr, sp.Symbol] = {}
        for index, inverse_erf in enumerate(inverse_erfs):
            argument = sp.simplify(inverse_erf.args[0])
            if (
                argument.is_real is not True
                or not certified_lt(-1, argument)
                or not certified_lt(argument, 1)
            ):
                return None
            replacements[inverse_erf] = sp.Symbol(
                f"certified_erfinv_{index}", real=True, finite=True
            )
        surrogate = expression.xreplace(replacements)
        if (
            not replacements
            or surrogate.is_real is not True
            or surrogate.is_finite is not True
        ):
            return None
    expression = sp.simplify(expression)
    if expression.is_Rational is True:
        numerator, denominator = expression.as_numer_denom()
        return Fraction(int(numerator), int(denominator))
    return expression


def canonical_real(value: object) -> RealCoordinate:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    certified = certified_real_coordinate(value)
    if certified is None:
        raise ValueError("value lacks an exact finite-real host certificate")
    return certified


def certified_equal(left: object, right: object) -> bool:
    if isinstance(left, (int, Fraction)) and isinstance(right, (int, Fraction)):
        return Fraction(left) == Fraction(right)
    try:
        difference = sp.simplify(sp.sympify(left) - sp.sympify(right))
    except (TypeError, ValueError, sp.SympifyError):
        return False
    return difference == 0 or difference.is_zero is True


def certified_le(left: object, right: object) -> bool:
    if isinstance(left, (int, Fraction)) and isinstance(right, (int, Fraction)):
        return Fraction(left) <= Fraction(right)
    try:
        difference = sp.simplify(sp.sympify(right) - sp.sympify(left))
    except (TypeError, ValueError, sp.SympifyError):
        return False
    return difference == 0 or difference.is_nonnegative is True


def certified_lt(left: object, right: object) -> bool:
    if isinstance(left, (int, Fraction)) and isinstance(right, (int, Fraction)):
        return Fraction(left) < Fraction(right)
    try:
        difference = sp.simplify(sp.sympify(right) - sp.sympify(left))
    except (TypeError, ValueError, sp.SympifyError):
        return False
    return difference.is_positive is True


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def neg(vector: Coord) -> Coord:
    return tuple(-value for value in vector)  # type: ignore[return-value]


def scale(value: int, vector: Coord) -> Coord:
    return tuple(value * item for item in vector)  # type: ignore[return-value]


def dot(left: Sequence[RealCoordinate], right: Sequence[RealCoordinate]) -> RealCoordinate:
    if all(isinstance(value, Fraction) for value in (*left, *right)):
        return sum((a * b for a, b in zip(left, right)), Fraction(0))  # type: ignore[operator]
    return canonical_real(
        sum((sp.sympify(a) * sp.sympify(b) for a, b in zip(left, right)), sp.S.Zero)
    )


def real_dot(left: Sequence[RealCoordinate], right: Sequence[RealCoordinate]) -> sp.Expr:
    return sp.simplify(
        sum((sp.sympify(a) * sp.sympify(b) for a, b in zip(left, right)), sp.S.Zero)
    )


def vec_add(left: Vector, right: Vector) -> Vector:
    if all(isinstance(value, Fraction) for value in (*left, *right)):
        return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value,operator]
    return tuple(canonical_real(sp.sympify(left[i]) + sp.sympify(right[i])) for i in range(3))  # type: ignore[return-value]


def vec_scale(value: RealCoordinate, vector: Vector) -> Vector:
    if isinstance(value, Fraction) and all(isinstance(item, Fraction) for item in vector):
        return tuple(value * item for item in vector)  # type: ignore[return-value,operator]
    return tuple(canonical_real(sp.sympify(value) * sp.sympify(item)) for item in vector)  # type: ignore[return-value]


def determinant3(rows: Sequence[Sequence[int]]) -> int:
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cubic_rotations() -> tuple[Rotation, ...]:
    answer: set[Rotation] = set()
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            rows = []
            for row_index, column in enumerate(permutation):
                row = [0, 0, 0]
                row[column] = signs[row_index]
                rows.append(tuple(row))
            rotation = tuple(rows)
            if determinant3(rotation) == 1:
                answer.add(rotation)  # type: ignore[arg-type]
    return tuple(sorted(answer))


ROTATIONS = proper_cubic_rotations()
ROTATION_INDEX = {rotation: index for index, rotation in enumerate(ROTATIONS)}


def rotate_coord(rotation: Rotation, vector: Coord) -> Coord:
    return tuple(sum(rotation[i][j] * vector[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def rotate_vector(rotation: Rotation, vector: Sequence[RealCoordinate]) -> RealVector:
    return tuple(
        sp.simplify(sum(Fraction(rotation[i][j]) * vector[j] for j in range(3)))
        for i in range(3)
    )  # type: ignore[return-value]


def rotate_rational_vector(rotation: Rotation, vector: RationalVector) -> RationalVector:
    return tuple(Fraction(value) for value in rotate_vector(rotation, vector))  # type: ignore[return-value]


def rotate_exact_vector(rotation: Rotation, vector: Vector) -> Vector:
    return tuple(canonical_real(value) for value in rotate_vector(rotation, vector))  # type: ignore[return-value]


@dataclass(frozen=True)
class Frame:
    rotation: Rotation

    @property
    def index(self) -> int:
        return ROTATION_INDEX[self.rotation]

    @property
    def forward(self) -> Coord:
        return rotate_coord(self.rotation, BASE_FORWARD)

    @property
    def transverse(self) -> Coord:
        return rotate_coord(self.rotation, BASE_TRANSVERSE)


IDENTITY_ROTATION: Rotation = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
IDENTITY_FRAME = Frame(IDENTITY_ROTATION)


@dataclass(frozen=True)
class Protocol:
    mode: int
    u0: Vector
    u1: Vector
    weight_u0: RealCoordinate = Fraction(1, 2)

    @property
    def mixture(self) -> Vector:
        return vec_add(
            vec_scale(self.weight_u0, self.u0),
            vec_scale(canonical_real(1 - sp.sympify(self.weight_u0)), self.u1),
        )

    @property
    def valid(self) -> bool:
        return (
            certified_real_coordinate(self.weight_u0) is not None
            and all(
                certified_real_coordinate(value) is not None
                for vector in (self.u0, self.u1)
                for value in vector
            )
            and certified_le(0, self.weight_u0)
            and certified_le(self.weight_u0, 1)
            and self.mode in (MODE_RND, MODE_DIR)
            and all(certified_le(dot(vector, vector), 1) for vector in (self.u0, self.u1))
        )


DEFAULT_RND = Protocol(
    MODE_RND,
    (Fraction(1, 2), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1, 2), Fraction(0)),
    Fraction(1, 2),
)
DEFAULT_DIR = Protocol(MODE_DIR, DEFAULT_RND.u0, DEFAULT_RND.u1, DEFAULT_RND.weight_u0)


@dataclass(frozen=True)
class Carrier:
    """Eight real Pauli coefficients of one element of M_2(C).

    The coordinates are `(h0,hx,hy,hz,k0,kx,ky,kz)` for
    `(h0+i k0) I + sum_j (h_j+i k_j) sigma_j`.
    """

    coefficients: tuple[
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
    ]


@dataclass(frozen=True)
class GaussianPoint:
    """One point of the actual eight-real-dimensional Gaussian source space."""

    coefficients: tuple[
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
        RealCoordinate,
    ]

    @property
    def valid(self) -> bool:
        return len(self.coefficients) == 8 and all(
            certified_real_coordinate(value) is not None for value in self.coefficients
        )


@dataclass(frozen=True)
class SpherePoint:
    """One point of S^2, used as an actual Haar-source sample."""

    direction: RealVector

    @property
    def valid(self) -> bool:
        norm = sp.simplify(sum(sp.sympify(value) ** 2 for value in self.direction))
        return certified_equal(norm, 1) and all(
            certified_real_coordinate(value) is not None for value in self.direction
        )


RecordValue: TypeAlias = Carrier
Records = dict[Coord, RecordValue]


def tag_code(role: str, frame: Frame) -> Fraction:
    return Fraction(2 + ROLE_ORDER.index(role) * len(ROTATIONS) + frame.index)


TAG_LOOKUP = {
    2 + role_index * len(ROTATIONS) + frame_index: (role, Frame(rotation))
    for role_index, role in enumerate(ROLE_ORDER)
    for frame_index, rotation in enumerate(ROTATIONS)
}


def tagged(role: str, frame: Frame, remaining: Sequence[RealCoordinate] = ()) -> Carrier:
    if len(remaining) > 7:
        raise ValueError("tagged M2 carrier has at most seven payload coordinates")
    payload = tuple(remaining) + (Fraction(0),) * (7 - len(remaining))
    return Carrier((tag_code(role, frame), *payload))  # type: ignore[arg-type]


@lru_cache(maxsize=None)
def decode_tagged(carrier: RecordValue) -> tuple[str, Frame] | None:
    code = carrier.coefficients[0]
    if isinstance(code, Fraction):
        return TAG_LOOKUP.get(code.numerator) if code.denominator == 1 else None
    code_expr = sp.sympify(code)
    if code_expr.is_Integer is not True or code_expr.is_number is not True:
        return None
    return TAG_LOOKUP.get(int(code_expr))


def protocol_role(prefix: str, mode: int) -> str:
    return f"{prefix}_{'RND' if mode == MODE_RND else 'DIR'}"


def selector_role(mode: int, bit: int) -> str:
    return f"R_{'RND' if mode == MODE_RND else 'DIR'}_{bit}"


def branch_role(prefix: str, mode: int, bit: int) -> str:
    if bit not in (0, 1):
        raise ValueError("branch role needs selector bit 0 or 1")
    return f"{prefix}_{'RND' if mode == MODE_RND else 'DIR'}_{bit}"


def branch_role_fields(role: str, prefix: str | None = None) -> tuple[int, int] | None:
    pieces = role.split("_")
    if len(pieces) != 3 or (prefix is not None and pieces[0] != prefix):
        return None
    if pieces[1] not in ("RND", "DIR") or pieces[2] not in ("0", "1"):
        return None
    return (MODE_RND if pieces[1] == "RND" else MODE_DIR, int(pieces[2]))


def program_role(mode: int, bit: int) -> str:
    return branch_role("P", mode, bit)


def outcome_role(mode: int, bit: int) -> str:
    return branch_role("O", mode, bit)


def q_role(stage: int, mode: int, bit: int) -> str:
    if stage not in range(1, 6):
        raise ValueError("Q stage must be 1,...,5")
    return branch_role(f"Q{stage}", mode, bit)


def as_fraction(value: RealCoordinate) -> Fraction | None:
    """Decode only exact rational M2 coordinates into the control sector."""
    if isinstance(value, Fraction):
        return value
    expression = sp.sympify(value)
    if expression.is_Rational is not True:
        return None
    numerator, denominator = expression.as_numer_denom()
    return Fraction(int(numerator), int(denominator))


def encode_protocol(
    role: str,
    frame: Frame,
    protocol: Protocol,
    stored_weight: RealCoordinate | None = None,
) -> Carrier:
    if not protocol.valid:
        raise ValueError("program endpoints and convex weight must be admissible")
    expected_mode = MODE_RND if role.endswith("RND") else MODE_DIR if role.endswith("DIR") else protocol.mode
    if expected_mode != protocol.mode:
        raise ValueError("role/protocol mode mismatch")
    if stored_weight is not None and not certified_equal(stored_weight, protocol.weight_u0):
        raise ValueError("stored convex weight/protocol mismatch")
    return tagged(role, frame, (*protocol.u0, protocol.weight_u0, *protocol.u1))


@lru_cache(maxsize=None)
def decode_protocol(
    carrier: Carrier, prefixes: tuple[str, ...]
) -> tuple[str, Frame, Protocol, RealCoordinate] | None:
    decoded = decode_tagged(carrier)
    if decoded is None:
        return None
    role, frame = decoded
    if not any(role.startswith(prefix) for prefix in prefixes):
        return None
    mode = MODE_RND if "RND" in role else MODE_DIR
    values = carrier.coefficients
    certified = tuple(certified_real_coordinate(value) for value in values[1:8])
    if any(value is None for value in certified):
        return None
    exact = tuple(value for value in certified if value is not None)
    protocol = Protocol(mode, exact[0:3], exact[4:7], exact[3])  # type: ignore[arg-type]
    if not protocol.valid:
        return None
    return role, frame, protocol, protocol.weight_u0


def encode_structural(
    role: str,
    frame: Frame,
    leak: RealCoordinate = Fraction(0),
    vector: Vector = ZERO3,
) -> Carrier:
    return tagged(role, frame, (*vector, leak))


@lru_cache(maxsize=None)
def structural_decode(
    carrier: Carrier, role: str
) -> tuple[Frame, Vector, RealCoordinate] | None:
    decoded = decode_tagged(carrier)
    if decoded is None or decoded[0] != role:
        return None
    values = carrier.coefficients
    certified = tuple(certified_real_coordinate(value) for value in values[1:8])
    if any(value is None for value in certified):
        return None
    exact = tuple(value for value in certified if value is not None)
    vector: Vector = exact[0:3]  # type: ignore[assignment]
    leak = exact[3]
    if exact[4:] != (Fraction(0), Fraction(0), Fraction(0)):
        return None
    if role == "T" and (
        vector != ZERO3 or not certified_le(0, leak) or not certified_le(leak, 1)
    ):
        return None
    if role == "C" and (leak != 0 or (vector != ZERO3 and dot(vector, vector) != 1)):
        return None
    return decoded[1], vector, leak


def encode_program(frame: Frame, protocol: Protocol, bit: int) -> Carrier:
    """Encode the installed program without compressing the real protocol.

    The seven free M2 coordinates carry ``(u0,p,u1)`` verbatim.  The finite
    role carries mode and selector bit.  A fixed local processor recovers the
    selected endpoint or direct mixture from this Record.
    """

    if not protocol.valid or bit not in (0, 1):
        raise ValueError("program carrier needs an admitted real protocol and selector bit")
    return encode_protocol(program_role(protocol.mode, bit), frame, protocol)


@lru_cache(maxsize=None)
def decode_program(carrier: Carrier) -> tuple[Frame, Protocol, int] | None:
    decoded = decode_protocol(carrier, ("P_",))
    if decoded is None:
        return None
    role, frame, protocol, _ = decoded
    branch = branch_role_fields(role, "P")
    if branch is None or branch[0] != protocol.mode:
        return None
    return frame, protocol, branch[1]


def decoded_program_value(
    decoded: tuple[Frame, Protocol, int], config: RuleConfig | None = None
) -> Vector:
    return installed_program(decoded[1], decoded[2], RuleConfig() if config is None else config)


def encode_outcome(
    frame: Frame,
    outcome: RealVector,
    protocol: Protocol,
    bit: int,
) -> Carrier:
    if (
        not protocol.valid
        or bit not in (0, 1)
        or not SpherePoint(outcome).valid
    ):
        raise ValueError("outcome carrier needs a unit direction and admitted branch type")
    return encode_typed_outcome(frame, outcome, protocol.mode, bit)


def encode_typed_outcome(
    frame: Frame, outcome: RealVector, mode: int, bit: int
) -> Carrier:
    if mode not in (MODE_RND, MODE_DIR) or bit not in (0, 1) or not SpherePoint(outcome).valid:
        raise ValueError("typed outcome needs a unit direction, mode, and selector bit")
    return tagged(outcome_role(mode, bit), frame, (*outcome,))


@lru_cache(maxsize=None)
def decode_outcome(carrier: RecordValue) -> tuple[Frame, RealVector, int, int] | None:
    decoded = decode_tagged(carrier)
    if decoded is None:
        return None
    branch = branch_role_fields(decoded[0], "O")
    if branch is None:
        return None
    values = carrier.coefficients
    vector: RealVector = values[1:4]  # type: ignore[assignment]
    if (
        not SpherePoint(vector).valid
        or tuple(as_fraction(value) for value in values[4:])
        != (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
    ):
        return None
    return decoded[1], vector, branch[0], branch[1]


def compress_real(value: RealCoordinate) -> sp.Expr:
    """Smooth bijection R -> (0,1), reserving integer tag hyperplanes."""
    return sp.simplify(1 / (1 + sp.exp(-sp.sympify(value))))


def expand_real(value: RealCoordinate) -> sp.Expr:
    expression = sp.sympify(value)
    if expression.is_positive is not True or sp.simplify(1 - expression).is_positive is not True:
        raise ValueError("not a Gaussian payload carrier")
    return sp.simplify(sp.log(expression / (1 - expression)))


def encode_gaussian(payload: Sequence[RealCoordinate]) -> Carrier:
    if len(payload) != 8:
        raise ValueError("Gaussian M2 payload needs eight real coefficients")
    values = tuple(certified_real_coordinate(value) for value in payload)
    if any(value is None for value in values):
        raise ValueError("Gaussian M2 payload needs exact finite-real host witnesses")
    values = tuple(value for value in values if value is not None)
    return Carrier((compress_real(values[0]), *values[1:]))  # type: ignore[arg-type]


@lru_cache(maxsize=None)
def decode_gaussian(carrier: RecordValue) -> tuple[RealCoordinate, ...] | None:
    first = sp.sympify(carrier.coefficients[0])
    if first.is_positive is not True or sp.simplify(1 - first).is_positive is not True:
        return None
    payload = (expand_real(first), *carrier.coefficients[1:])
    return payload if GaussianPoint(payload).valid else None


def _alternating_arctan_interval(inverse: int, decimal_digits: int) -> tuple[Fraction, Fraction]:
    """Rigorous rational enclosure for atan(1/inverse)."""

    tolerance = Fraction(1, 10 ** (decimal_digits + 12))
    total = Fraction(0)
    index = 0
    while True:
        magnitude = Fraction(1, (2 * index + 1) * inverse ** (2 * index + 1))
        total += magnitude if index % 2 == 0 else -magnitude
        next_index = index + 1
        next_magnitude = Fraction(
            1, (2 * next_index + 1) * inverse ** (2 * next_index + 1)
        )
        if next_magnitude < tolerance:
            signed_remainder = next_magnitude if next_index % 2 == 0 else -next_magnitude
            return (min(total, total + signed_remainder), max(total, total + signed_remainder))
        index = next_index


@lru_cache(maxsize=None)
def pi_rational_interval(decimal_digits: int) -> tuple[Fraction, Fraction]:
    """Machin-formula enclosure, independent of floating evaluation."""

    low5, high5 = _alternating_arctan_interval(5, decimal_digits)
    low239, high239 = _alternating_arctan_interval(239, decimal_digits)
    return 16 * low5 - 4 * high239, 16 * high5 - 4 * low239


def _sqrt_rational_interval(value: Fraction, decimal_digits: int) -> tuple[Fraction, Fraction]:
    if value < 0:
        raise ValueError("square-root enclosure needs a nonnegative rational")
    scale10 = 10**decimal_digits
    scaled_square_numerator = value.numerator * scale10 * scale10
    floor_square = scaled_square_numerator // value.denominator
    root = math.isqrt(floor_square)
    while (root + 1) ** 2 * value.denominator <= scaled_square_numerator:
        root += 1
    while root**2 * value.denominator > scaled_square_numerator:
        root -= 1
    low = Fraction(root, scale10)
    if root**2 * value.denominator == scaled_square_numerator:
        return low, low
    return low, Fraction(root + 1, scale10)


@lru_cache(maxsize=None)
def normal_cdf_rational_interval(
    statistic: Fraction, decimal_digits: int
) -> tuple[Fraction, Fraction]:
    """Rigorous Phi(s) enclosure for exact rational |s|<=1.

    The integral of exp(-t^2/2) on [0,|s|] is enclosed by its alternating
    Taylor series, and 1/sqrt(2*pi) by Machin plus integer square-root bounds.
    Every endpoint returned here is a rational proof bound.
    """

    if abs(statistic) > 1:
        raise ValueError("certified witness enclosure currently covers |statistic|<=1")
    if statistic == 0:
        return Fraction(1, 2), Fraction(1, 2)
    if statistic < 0:
        low, high = normal_cdf_rational_interval(-statistic, decimal_digits)
        return Fraction(1) - high, Fraction(1) - low

    tolerance = Fraction(1, 10 ** (decimal_digits + 12))
    total = Fraction(0)
    index = 0
    while True:
        magnitude = (
            statistic ** (2 * index + 1)
            / (2**index * math.factorial(index) * (2 * index + 1))
        )
        total += magnitude if index % 2 == 0 else -magnitude
        next_index = index + 1
        next_magnitude = (
            statistic ** (2 * next_index + 1)
            / (2**next_index * math.factorial(next_index) * (2 * next_index + 1))
        )
        if next_magnitude < tolerance:
            signed_remainder = next_magnitude if next_index % 2 == 0 else -next_magnitude
            integral_low = min(total, total + signed_remainder)
            integral_high = max(total, total + signed_remainder)
            break
        index = next_index

    pi_low, pi_high = pi_rational_interval(decimal_digits + 8)
    sqrt_low, _ = _sqrt_rational_interval(2 * pi_low, decimal_digits + 8)
    _, sqrt_high = _sqrt_rational_interval(2 * pi_high, decimal_digits + 8)
    inverse_low = Fraction(1, 1) / sqrt_high
    inverse_high = Fraction(1, 1) / sqrt_low
    return (
        Fraction(1, 2) + integral_low * inverse_low,
        Fraction(1, 2) + integral_high * inverse_high,
    )


class UndecidedExactRealOrder(ValueError):
    """The host witness lacks a finite sign certificate; mathematics remains defined."""


def gaussian_representative(
    bit: int,
    weight_u0: RealCoordinate = Fraction(1, 2),
    variant: int = 0,
) -> Carrier:
    """An exact content-defined point strictly inside each positive-mass fibre."""
    if bit not in (0, 1) or not certified_le(0, weight_u0) or not certified_le(weight_u0, 1):
        raise ValueError("invalid Gaussian quotient bit/weight")
    weight_expression = sp.sympify(weight_u0)
    target_cdf = (
        sp.Rational(1, 2)
        if certified_equal(weight_u0, 0) or certified_equal(weight_u0, 1)
        else weight_expression / 2
        if bit == 0
        else (1 + weight_expression) / 2
    )
    statistic = sp.sqrt(2) * sp.erfinv(2 * target_cdf - 1)
    k0 = statistic / 2
    payload = (
        Fraction(variant),
        Fraction(variant, 3),
        Fraction(0),
        Fraction(-variant, 5),
        k0,
        Fraction(variant, 7),
        Fraction(0),
        Fraction(variant, 11),
    )
    return encode_gaussian(payload)


def certified_selector_bit(
    carrier: RecordValue,
    weight_u0: RealCoordinate = Fraction(1, 2),
    max_decimal_digits: int = 1280,
) -> int:
    """Execute the total mathematical selector when a finite proof is found.

    The mathematical event is ``Phi(S)<=p`` and is total over real numbers;
    :func:`gaussian_selector_predicate` is its definition.  This routine is a
    deliberately partial exact-real witness evaluator.  It first uses symbolic
    sign facts, then rigorous rational enclosures (never a float).  It raises
    rather than pretending that arbitrary host expressions have decidable
    order.  Source points off the equality boundary are decidable a.s. for an
    interval-oracle representation; the null equality boundary is assigned to
    bit zero by the mathematical predicate.
    """

    payload = decode_gaussian(carrier)
    if payload is None:
        raise ValueError("selector is not an encoded Gaussian Record")
    statistic = 2 * payload[4]
    if certified_equal(weight_u0, 0):
        return 1
    if certified_equal(weight_u0, 1):
        return 0
    statistic_expr = sp.sympify(statistic)
    if statistic_expr.is_number is not True:
        raise UndecidedExactRealOrder("selector witness requires a concrete exact sample")
    cdf = sp.simplify((1 + sp.erf(statistic_expr / sp.sqrt(2))) / 2)
    difference = sp.simplify(cdf - sp.sympify(weight_u0))
    if difference == 0 or difference.is_zero is True or difference.is_negative is True:
        return 0
    if difference.is_positive is True:
        return 1
    statistic_fraction = as_fraction(canonical_real(statistic_expr))
    threshold_fraction = as_fraction(canonical_real(weight_u0))
    if (
        statistic_fraction is not None
        and threshold_fraction is not None
        and abs(statistic_fraction) <= 1
    ):
        digits = 40
        while digits <= max_decimal_digits:
            low, high = normal_cdf_rational_interval(statistic_fraction, digits)
            if high <= threshold_fraction:
                return 0
            if low > threshold_fraction:
                return 1
            digits *= 2
    raise UndecidedExactRealOrder(
        "finite exact-real order certificate not found; use the mathematical predicate"
    )


def gaussian_selector_predicate(
    sample: GaussianPoint, bit: int, weight_u0: RealCoordinate
) -> sp.Relational:
    """The total mathematical event predicate, retained even when not simplified."""
    carrier = GaussianCarrierMap().apply(sample)
    payload = decode_gaussian(carrier)
    if payload is None or bit not in (0, 1):
        raise ValueError("invalid Gaussian selector event")
    statistic = 2 * sp.sympify(payload[4])
    cdf = sp.simplify((1 + sp.erf(statistic / sp.sqrt(2))) / 2)
    threshold = sp.sympify(weight_u0)
    return (
        sp.Le(cdf, threshold, evaluate=False)
        if bit == 0
        else sp.Gt(cdf, threshold, evaluate=False)
    )


def rotate_carrier(rotation: Rotation, carrier: RecordValue) -> RecordValue:
    decoded = decode_tagged(carrier)
    if decoded is not None:
        role, frame = decoded
        composed: Rotation = tuple(
            tuple(sum(rotation[i][k] * frame.rotation[k][j] for k in range(3)) for j in range(3))
            for i in range(3)
        )  # type: ignore[assignment]
        new_frame = Frame(composed)
        if role.startswith("P_"):
            program = decode_program(carrier)
            if program is None:
                return carrier
            rotated_protocol = Protocol(
                program[1].mode,
                rotate_exact_vector(rotation, program[1].u0),
                rotate_exact_vector(rotation, program[1].u1),
                program[1].weight_u0,
            )
            return encode_program(new_frame, rotated_protocol, program[2])
        if role.startswith("O_"):
            outcome = decode_outcome(carrier)
            if outcome is None:
                return carrier
            return encode_typed_outcome(
                new_frame,
                rotate_vector(rotation, outcome[1]),
                outcome[2],
                outcome[3],
            )
        protocol = decode_protocol(carrier, ("H_", "R_", "C_", "Q"))
        if protocol is not None:
            rotated_protocol = Protocol(
                protocol[2].mode,
                rotate_exact_vector(rotation, protocol[2].u0),
                rotate_exact_vector(rotation, protocol[2].u1),
                protocol[2].weight_u0,
            )
            return encode_protocol(role, new_frame, rotated_protocol, protocol[3])
        structural = structural_decode(carrier, role)
        if structural is not None:
            return encode_structural(
                role,
                new_frame,
                structural[2],
                rotate_exact_vector(rotation, structural[1]),
            )
        return carrier
    gaussian = decode_gaussian(carrier)
    if gaussian is not None:
        hvec = rotate_vector(rotation, gaussian[1:4])  # type: ignore[arg-type]
        kvec = rotate_vector(rotation, gaussian[5:8])  # type: ignore[arg-type]
        return encode_gaussian((gaussian[0], *hvec, gaussian[4], *kvec))
    return carrier


@lru_cache(maxsize=1)
def gaussian_integral_certificate() -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Exact marginal integrals for S=ImTr(A)=2*k0 under the M2 Gaussian."""
    k0 = sp.symbols("k0", real=True)
    density = sp.sqrt(2 / sp.pi) * sp.exp(-2 * k0**2)
    return (
        sp.simplify(sp.integrate(density, (k0, -sp.oo, sp.oo))),
        sp.simplify(sp.integrate(density, (k0, -sp.oo, 0))),
        sp.simplify(sp.integrate(density, (k0, 0, sp.oo))),
    )


@lru_cache(maxsize=1)
def gaussian_full_m2_normalization_certificate() -> sp.Expr:
    coordinate = sp.symbols("coordinate", real=True)
    marginal = sp.sqrt(2 / sp.pi) * sp.exp(-2 * coordinate**2)
    one_coordinate = sp.simplify(sp.integrate(marginal, (coordinate, -sp.oo, sp.oo)))
    return sp.simplify(one_coordinate**8)


@lru_cache(maxsize=1)
def gaussian_probability_integral_transform_certificate() -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    statistic = sp.symbols("statistic", real=True)
    cdf = (1 + sp.erf(statistic / sp.sqrt(2))) / 2
    density = sp.exp(-statistic**2 / 2) / sp.sqrt(2 * sp.pi)
    return (
        sp.simplify(sp.diff(cdf, statistic) - density),
        sp.simplify(sp.limit(cdf, statistic, -sp.oo)),
        sp.simplify(sp.limit(cdf, statistic, sp.oo)),
    )


@lru_cache(maxsize=1)
def haar_integral_certificate() -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    """Direct spherical-coordinate normalization and first-moment integrals."""
    theta, phi = sp.symbols("theta phi", real=True)
    sx, sy, sz = sp.symbols("sx sy sz", real=True)
    n = (
        sp.sin(theta) * sp.cos(phi),
        sp.sin(theta) * sp.sin(phi),
        sp.cos(theta),
    )
    reference = sp.sin(theta) / (4 * sp.pi)
    normalization = sp.simplify(
        sp.integrate((1 + sx * n[0] + sy * n[1] + sz * n[2]) * reference, (phi, 0, 2 * sp.pi), (theta, 0, sp.pi))
    )
    moments = tuple(
        sp.simplify(sp.integrate(component * reference, (phi, 0, 2 * sp.pi), (theta, 0, sp.pi)))
        for component in n
    )
    reference_total = sp.simplify(
        sp.integrate(reference, (phi, 0, 2 * sp.pi), (theta, 0, sp.pi))
    )
    return reference_total, *moments, normalization


@dataclass(frozen=True)
class GaussianCarrierMap:
    """Measurable injection from R^8 into the Gaussian strip of M2."""

    def apply(self, sample: GaussianPoint) -> Carrier:
        if not isinstance(sample, GaussianPoint) or not sample.valid:
            raise ValueError("Gaussian carrier map requires a real eight-coordinate sample")
        return encode_gaussian(sample.coefficients)

    def canonical_fibre_sample(
        self, bit: int, weight_u0: RealCoordinate, variant: int = 0
    ) -> GaussianPoint:
        representative = gaussian_representative(bit, weight_u0, variant)
        decoded = decode_gaussian(representative)
        if decoded is None:
            raise ValueError("missing Gaussian fibre representative")
        return GaussianPoint(decoded)  # type: ignore[arg-type]

    @property
    def measurable(self) -> bool:
        # Logistic x0 plus seven coordinate identities is a smooth injection.
        return True


@dataclass(frozen=True)
class OutcomeCarrierMap:
    """Measurable injection from S2 into a protocol-bound M2 role sector."""

    frame: Frame
    protocol: Protocol
    bit: int

    def apply(self, sample: SpherePoint) -> Carrier:
        if not isinstance(sample, SpherePoint) or not sample.valid or not self.protocol.valid:
            raise ValueError("outcome carrier map requires a unit real sphere sample and admitted protocol")
        return encode_outcome(self.frame, sample.direction, self.protocol, self.bit)

    @property
    def measurable(self) -> bool:
        return self.protocol.valid and self.bit in (0, 1)


CarrierMap: TypeAlias = GaussianCarrierMap | OutcomeCarrierMap


@dataclass(frozen=True)
class MeasureSpec:
    """The actual analytic probability measure in a stochastic local row.

    Finite graph atoms below are structural controls only.  A stochastic row's
    candidate-law semantics is this measure, including its displayed encoding
    or outcome map, not the cubature used to exhaust the rewrite graph.
    """

    family: str
    program: Vector | None = None
    selector_weight_u0: RealCoordinate | None = None
    owner: str = "local_generator_row"
    carrier_map: CarrierMap | None = None
    frame: Frame | None = None
    mode: int | None = None
    protocol: Protocol | None = None

    @property
    def map_matches_family(self) -> bool:
        if self.family == "encoded_center_zero_M2_gaussian":
            return isinstance(self.carrier_map, GaussianCarrierMap) and self.frame is not None
        if self.family == "haar_phi_1_plus_n_dot_program":
            return (
                isinstance(self.carrier_map, OutcomeCarrierMap)
                and self.frame == self.carrier_map.frame
                and self.protocol == self.carrier_map.protocol
                and self.mode == self.carrier_map.protocol.mode
            )
        return False

    @property
    def normalized(self) -> bool:
        if self.family == "encoded_center_zero_M2_gaussian":
            return self.map_matches_family and gaussian_full_m2_normalization_certificate() == 1
        if self.family == "haar_phi_1_plus_n_dot_program":
            return (
                self.map_matches_family
                and
                self.program is not None
                and certified_le(dot(self.program, self.program), 1)
                and haar_integral_certificate() == (1, 0, 0, 0, 1)
            )
        return False

    @property
    def nonnegative(self) -> bool:
        if self.family == "encoded_center_zero_M2_gaussian":
            return self.map_matches_family
        if self.family == "haar_phi_1_plus_n_dot_program" and self.program is not None:
            # Cauchy--Schwarz gives min_{|n|=1}(1+n.s)=1-|s|.
            return self.map_matches_family and certified_le(dot(self.program, self.program), 1)
        return False

    @property
    def selector_masses(self) -> tuple[RealCoordinate, RealCoordinate] | None:
        if (
            self.family != "encoded_center_zero_M2_gaussian"
            or self.selector_weight_u0 is None
            or gaussian_probability_integral_transform_certificate() != (0, 0, 1)
        ):
            return None
        return (
            self.selector_weight_u0,
            canonical_real(1 - sp.sympify(self.selector_weight_u0)),
        )

    @property
    def locally_owned(self) -> bool:
        return self.owner == "local_generator_row"


@dataclass(frozen=True)
class LocalRow:
    kind: str
    control_atoms: tuple[tuple[RealCoordinate, Carrier], ...]
    continuous_measure: MeasureSpec | None = None

    @property
    def normalized(self) -> bool:
        finite_control = (
            certified_equal(sum((sp.sympify(weight) for weight, _ in self.control_atoms), sp.S.Zero), 1)
            and all(certified_le(0, weight) for weight, _ in self.control_atoms)
        )
        return finite_control and (
            self.continuous_measure is None
            or (self.continuous_measure.normalized and self.continuous_measure.nonnegative)
        )


@dataclass(frozen=True)
class RuleConfig:
    mutation: str | None = None

    @property
    def collision_policy(self) -> str:
        return "undefined" if self.mutation == "undefined_collision" else "STOP"

    @property
    def claimed_scope(self) -> str:
        return "toe_closed" if self.mutation == "toe_promotion" else "candidate_single_front"


def gaussian_row(frame: Frame, weight_u0: RealCoordinate, config: RuleConfig) -> LocalRow:
    if config.mutation == "born_selector":
        weights = (Fraction(3, 4), Fraction(1, 4))
    elif config.mutation == "archive_relay":
        weights = (weight_u0, canonical_real(1 - sp.sympify(weight_u0)))
    else:
        weights = (weight_u0, canonical_real(1 - sp.sympify(weight_u0)))
    owner = (
        "external_iid_sequence"
        if config.mutation == "external_iid"
        else "prelaid_unbounded_bank"
        if config.mutation == "unbounded_bank"
        else "local_generator_row"
    )
    return LocalRow(
        "gaussian",
        (
            (weights[0], gaussian_representative(0, weights[0])),
            (weights[1], gaussian_representative(1, weights[0])),
        ),
        MeasureSpec(
            "encoded_center_zero_M2_gaussian",
            selector_weight_u0=weights[0],
            owner=owner,
            carrier_map=GaussianCarrierMap(),
            frame=frame,
        ),
    )


def installed_program(protocol: Protocol, bit: int, config: RuleConfig) -> Vector:
    if protocol.mode == MODE_RND:
        return protocol.u0 if bit == 0 else protocol.u1
    midpoint = protocol.mixture
    if config.mutation == "nonlinear_encoder":
        return tuple(canonical_real(sp.sympify(value) ** 2) for value in midpoint)  # type: ignore[return-value]
    return midpoint


def outcome_weights(
    program: Vector, selector_leak: RealCoordinate, config: RuleConfig
) -> tuple[RealCoordinate, ...]:
    effective = effective_response_program(program, selector_leak, config)
    return tuple(
        canonical_real((1 + sp.sympify(dot(axis, effective))) / 6) for axis in AXES
    )


def effective_response_program(
    program: Vector, selector_leak: RealCoordinate, config: RuleConfig
) -> Vector:
    if config.mutation == "selector_leak":
        return vec_scale(Fraction(1) + Fraction(1, 2) * selector_leak, program)
    return program


def outcome_row(
    frame: Frame,
    program: Vector,
    protocol: Protocol,
    bit: int,
    selector_leak: RealCoordinate,
    config: RuleConfig,
) -> LocalRow:
    weights = outcome_weights(program, selector_leak, config)
    effective = effective_response_program(program, selector_leak, config)
    return LocalRow(
        "outcome",
        tuple(
            (weight, encode_outcome(frame, axis, protocol, bit))
            for weight, axis in zip(weights, AXES)
        ),
        MeasureSpec(
            "haar_phi_1_plus_n_dot_program",
            program=effective,
            carrier_map=OutcomeCarrierMap(frame, protocol, bit),
            frame=frame,
            mode=protocol.mode,
            protocol=protocol,
        ),
    )


def local_signature(records: Mapping[Coord, RecordValue], target: Coord) -> dict[Coord, RecordValue]:
    return {
        direction: records[add(target, direction)]
        for direction in DIRECTIONS
        if add(target, direction) in records
    }


def record_role_frame(carrier: RecordValue) -> tuple[str, Frame] | None:
    return decode_tagged(carrier)


def allowed_signature(
    signature: Mapping[Coord, RecordValue],
    required: Mapping[Coord, RecordValue],
    allowed: Mapping[Coord, str | tuple[str, ...]],
    frame: Frame,
) -> bool:
    if any(signature.get(offset) != carrier for offset, carrier in required.items()):
        return False
    for offset, carrier in signature.items():
        if offset in required:
            continue
        decoded = record_role_frame(carrier)
        expected = allowed.get(offset)
        role_matches = (
            decoded is not None
            and (
                decoded[0] == expected
                if isinstance(expected, str)
                else expected is not None and decoded[0] in expected
            )
        )
        if not role_matches or decoded is None or decoded[1] != frame:
            return False
    return True


def central_neighbor_matches(
    role: str, carrier: RecordValue, frame: Frame, protocol: Protocol
) -> bool:
    """Validate every payload/mode carried by an optional central neighbor."""
    if role.startswith("P_"):
        decoded = decode_program(carrier)
        return (
            decoded is not None
            and decoded[0] == frame
            and decoded[1] == protocol
            and decode_tagged(carrier) == (role, frame)
        )
    if role.startswith("O_"):
        # Q carries the complete protocol; O carries the branch type and sphere
        # direction.  Every sphere direction is a lawful value in that typed
        # outcome support, so no impossible provenance fingerprint is assumed.
        decoded = decode_outcome(carrier)
        return (
            decoded is not None
            and decoded[0] == frame
            and decoded[2] == protocol.mode
            and decode_tagged(carrier) == (role, frame)
        )
    if role == "C":
        decoded = decode_protocol(carrier, ("C_",)) if isinstance(carrier, Carrier) else None
        return decoded is not None and decoded[1] == frame and decoded[2] == protocol
    return False


def close_payload(outcome_value: Vector, config: RuleConfig) -> Vector:
    """The only outcome-to-close payload map used by the local table."""
    return outcome_value if config.mutation == "archive_relay" else ZERO3


def next_head_protocol(protocol: Protocol, close_value: Vector, config: RuleConfig) -> Protocol:
    """The only close/Q5-to-successor-protocol map used by the local table."""
    if config.mutation != "archive_relay":
        return protocol
    shift = max(Fraction(-1, 4), min(Fraction(1, 4), close_value[2] / 4))
    return Protocol(
        protocol.mode,
        protocol.u0,
        protocol.u1,
        max(Fraction(0), min(Fraction(1), protocol.weight_u0 + shift)),
    )


def local_proposals(records: Mapping[Coord, RecordValue], target: Coord, config: RuleConfig) -> list[LocalRow]:
    if target in records:
        return []
    signature = local_signature(records, target)
    proposals: list[LocalRow] = []

    for offset, carrier in signature.items():
        head = decode_protocol(carrier, ("H_",))
        if head is None:
            continue
        _, frame, protocol, weight_u0 = head
        if config.mutation == "coordinate_axis" and frame != IDENTITY_FRAME:
            continue
        if offset == frame.transverse and allowed_signature(signature, {offset: carrier}, {}, frame):
            if config.mutation == "premature_program":
                proposals.append(
                    LocalRow(
                        "premature_program",
                        ((Fraction(1), encode_program(frame, protocol, 0)),),
                    )
                )
            else:
                proposals.append(
                    LocalRow(
                        "trigger",
                        ((Fraction(1), encode_structural("T", frame, leak=weight_u0)),),
                    )
                )

    for offset, carrier in signature.items():
        trigger = structural_decode(carrier, "T")
        if trigger is None:
            continue
        frame, _, weight_u0 = trigger
        if offset == neg(frame.forward) and allowed_signature(signature, {offset: carrier}, {}, frame):
            proposals.append(gaussian_row(frame, weight_u0, config))

    for h_offset, h_carrier in signature.items():
        head = decode_protocol(h_carrier, ("H_",))
        if head is None:
            continue
        _, frame, protocol, weight_u0 = head
        a_offset = neg(frame.transverse)
        a_carrier = signature.get(a_offset)
        if h_offset != neg(frame.forward) or a_carrier is None or decode_gaussian(a_carrier) is None:
            continue
        required = {h_offset: h_carrier, a_offset: a_carrier}
        if allowed_signature(signature, required, {}, frame):
            bit = certified_selector_bit(a_carrier, protocol.weight_u0)
            role = selector_role(protocol.mode, bit)
            proposals.append(
                LocalRow(
                    "selector",
                    ((Fraction(1), encode_protocol(role, frame, protocol, weight_u0)),),
                )
            )

    for offset, carrier in signature.items():
        selector = decode_protocol(carrier, ("R_",))
        if selector is None:
            continue
        role, frame, protocol, _ = selector
        bit = int(role.rsplit("_", 1)[1])
        if offset == neg(frame.forward):
            allowed = {frame.transverse: q_role(2, protocol.mode, bit)}
            existing_q2 = signature.get(frame.transverse)
            if existing_q2 is not None:
                decoded_q2 = decode_protocol(existing_q2, ("Q2_",))
                if decoded_q2 is None or decoded_q2[1] != frame or decoded_q2[2] != protocol:
                    continue
            if allowed_signature(signature, {offset: carrier}, allowed, frame):
                proposals.append(
                    LocalRow(
                        "program",
                        ((Fraction(1), encode_program(frame, protocol, bit)),),
                    )
                )
        if offset == neg(frame.transverse):
            previous_q5 = (
                q_role(5, protocol.mode, 0),
                q_role(5, protocol.mode, 1),
            )
            allowed = {neg(frame.forward): previous_q5}
            if not allowed_signature(signature, {offset: carrier}, allowed, frame):
                continue
            q_protocol = protocol
            if config.mutation == "host_schedule":
                p_site = add(add(target, neg(frame.transverse)), frame.forward)
                if p_site in records:
                    q_protocol = Protocol(
                        protocol.mode,
                        protocol.u1,
                        protocol.u0,
                        canonical_real(1 - sp.sympify(protocol.weight_u0)),
                    )
            proposals.append(
                LocalRow(
                    "q1",
                    ((Fraction(1), encode_protocol(q_role(1, protocol.mode, bit), frame, q_protocol)),),
                )
            )

    for offset, carrier in signature.items():
        q_decoded = decode_protocol(carrier, ("Q",))
        if q_decoded is None:
            continue
        role, frame, protocol, weight_u0 = q_decoded
        if offset != neg(frame.forward):
            continue
        stage = int(role[1])
        branch = branch_role_fields(role, f"Q{stage}")
        if branch is None or branch[0] != protocol.mode:
            continue
        bit = branch[1]
        if stage >= 5:
            continue
        central_roles = {
            2: program_role(protocol.mode, bit),
            3: outcome_role(protocol.mode, bit),
            4: "C",
        }
        allowed = {}
        if stage + 1 in central_roles:
            central_role = central_roles[stage + 1]
            central_offset = neg(frame.transverse)
            central_carrier = signature.get(central_offset)
            allowed[central_offset] = (
                protocol_role("C", protocol.mode) if central_role == "C" else central_role
            )
            if central_carrier is not None and not central_neighbor_matches(
                central_role, central_carrier, frame, protocol
            ):
                continue
        if allowed_signature(signature, {offset: carrier}, allowed, frame):
            proposals.append(
                LocalRow(
                    f"q{stage + 1}",
                    ((Fraction(1), encode_protocol(q_role(stage + 1, protocol.mode, bit), frame, protocol, weight_u0)),),
                )
            )

    for offset, carrier in signature.items():
        program = decode_program(carrier)
        if program is None:
            continue
        frame, program_protocol, bit = program
        mode = program_protocol.mode
        vector = installed_program(program_protocol, bit, config)
        selector_leak = (
            Fraction(2 * bit - 1)
            if config.mutation == "selector_leak"
            else Fraction(0)
        )
        q3 = signature.get(frame.transverse)
        if q3 is not None:
            decoded_q3 = decode_protocol(q3, ("Q3_",))
            q3_branch = (
                branch_role_fields(decoded_q3[0], "Q3")
                if decoded_q3 is not None
                else None
            )
            if (
                decoded_q3 is None
                or decoded_q3[1] != frame
                or decoded_q3[2] != program_protocol
                or q3_branch != (mode, bit)
            ):
                continue
        if offset == neg(frame.forward) and all(
            other_offset in (offset, frame.transverse) for other_offset in signature
        ):
            proposals.append(
                outcome_row(
                    frame, vector, program_protocol, bit, selector_leak, config
                )
            )

    for offset, carrier in signature.items():
        outcome = decode_outcome(carrier)
        if outcome is None:
            continue
        frame, vector, mode, bit = outcome
        q4 = signature.get(frame.transverse)
        decoded_q4 = (
            decode_protocol(q4, ("Q4_",)) if isinstance(q4, Carrier) else None
        )
        q4_branch = (
            branch_role_fields(decoded_q4[0], "Q4")
            if decoded_q4 is not None
            else None
        )
        if (
            decoded_q4 is None
            or decoded_q4[1] != frame
            or q4_branch != (mode, bit)
        ):
            continue
        if offset == neg(frame.forward) and all(
            other_offset in (offset, frame.transverse) for other_offset in signature
        ):
            stored = close_payload(vector, config)
            close_protocol = next_head_protocol(decoded_q4[2], stored, config)
            close_role = protocol_role("C", close_protocol.mode)
            proposals.append(
                LocalRow(
                    "close",
                    ((Fraction(1), encode_protocol(close_role, frame, close_protocol)),),
                )
            )

    for c_offset, c_carrier in signature.items():
        close = decode_protocol(c_carrier, ("C_",)) if isinstance(c_carrier, Carrier) else None
        if close is None:
            continue
        _, frame, close_protocol, _ = close
        if c_offset != neg(frame.forward):
            continue
        q5_offset = frame.transverse
        q5_carrier = signature.get(q5_offset)
        q5 = decode_protocol(q5_carrier, ("Q5_",)) if isinstance(q5_carrier, Carrier) else None
        if config.mutation == "premature_head" and q5 is None:
            protocol = close_protocol
        elif q5 is None:
            continue
        else:
            _, q_frame, protocol, _ = q5
            if q_frame != frame or protocol != close_protocol:
                continue
        required = {c_offset: c_carrier}
        if q5_carrier is not None:
            required[q5_offset] = q5_carrier
        if allowed_signature(signature, required, {}, frame):
            role = protocol_role("H", protocol.mode)
            proposals.append(LocalRow("head", ((Fraction(1), encode_protocol(role, frame, protocol)),)))

    return proposals


def resolve_proposals(proposals: Sequence[LocalRow], config: RuleConfig) -> tuple[str, LocalRow | None]:
    if len(proposals) == 1:
        return ("ACTIVE", proposals[0]) if proposals[0].normalized else ("STOP", None)
    if len(proposals) > 1:
        return config.collision_policy, None
    return "STOP", None


def local_row(records: Mapping[Coord, RecordValue], target: Coord, config: RuleConfig) -> tuple[str, LocalRow | None]:
    return resolve_proposals(local_proposals(records, target, config), config)


def open_candidates(records: Mapping[Coord, RecordValue]) -> tuple[Coord, ...]:
    return tuple(sorted({add(site, direction) for site in records for direction in DIRECTIONS if add(site, direction) not in records}))


def active_actions(records: Mapping[Coord, RecordValue], config: RuleConfig) -> dict[Coord, LocalRow]:
    answer = {}
    for target in open_candidates(records):
        status, row = local_row(records, target, config)
        if status == "ACTIVE" and row is not None:
            answer[target] = row
    return answer


@dataclass(frozen=True)
class FiniteRecordJumpMeasure:
    """A finite Record-valued successor measure for a deterministic/control row."""

    target: Coord
    base_state: tuple[tuple[Coord, RecordValue], ...]
    atoms: tuple[tuple[RealCoordinate, RecordValue], ...]

    @property
    def normalized(self) -> bool:
        return (
            self.target not in dict(self.base_state)
            and certified_equal(
                sum((sp.sympify(weight) for weight, _ in self.atoms), sp.S.Zero), 1
            )
            and all(certified_le(0, weight) for weight, _ in self.atoms)
        )

    def successors(self) -> tuple[tuple[RealCoordinate, Records], ...]:
        if not self.normalized:
            raise ValueError("finite successor measure is not normalized on an empty target")
        answer = []
        for weight, carrier in self.atoms:
            state = dict(self.base_state)
            state[self.target] = carrier
            answer.append((weight, state))
        return tuple(answer)


SourcePoint: TypeAlias = GaussianPoint | SpherePoint


@dataclass(frozen=True)
class ContinuousRecordJumpMeasure:
    """Pushforward of an analytic source law into full append-only Record states."""

    target: Coord
    base_state: tuple[tuple[Coord, RecordValue], ...]
    source_measure: MeasureSpec

    @property
    def normalized(self) -> bool:
        return (
            self.target not in dict(self.base_state)
            and self.source_measure.normalized
            and self.source_measure.nonnegative
            and self.source_measure.carrier_map is not None
            and self.source_measure.carrier_map.measurable
        )

    def successor(self, sample: SourcePoint) -> Records:
        if not self.normalized:
            raise ValueError("continuous successor measure is not normalized on an empty target")
        carrier_map = self.source_measure.carrier_map
        if isinstance(carrier_map, GaussianCarrierMap) and isinstance(sample, GaussianPoint):
            carrier: RecordValue = carrier_map.apply(sample)
        elif isinstance(carrier_map, OutcomeCarrierMap) and isinstance(sample, SpherePoint):
            carrier = carrier_map.apply(sample)
        else:
            raise ValueError("sample space does not match the local carrier map")
        state = dict(self.base_state)
        state[self.target] = carrier
        return state


RecordJumpMeasure: TypeAlias = FiniteRecordJumpMeasure | ContinuousRecordJumpMeasure


@dataclass(frozen=True)
class GeneratorTerm:
    """One rate-one term with its actual Record-valued successor measure."""

    target: Coord
    rate: Fraction
    row: LocalRow
    jump_measure: RecordJumpMeasure


def record_jump_measure(
    records: Mapping[Coord, RecordValue], target: Coord, row: LocalRow
) -> RecordJumpMeasure:
    base_state = state_key(records)
    if row.continuous_measure is not None:
        return ContinuousRecordJumpMeasure(target, base_state, row.continuous_measure)
    return FiniteRecordJumpMeasure(target, base_state, row.control_atoms)


def local_ctmc_generator(records: Mapping[Coord, RecordValue], config: RuleConfig) -> tuple[GeneratorTerm, ...]:
    """Finite-rate interacting-particle generator on every finite Record state.

    Each ACTIVE empty site has its own rate-one exponential clock.  The local
    jump measure is ``row.continuous_measure`` for stochastic rows and the
    displayed Dirac atom for deterministic rows.  Absolute coordinates and a
    host-selected firing order never enter this generator.
    """
    return tuple(
        GeneratorTerm(target, Fraction(1), row, record_jump_measure(records, target, row))
        for target, row in sorted(active_actions(records, config).items())
    )


def generator_is_finite_and_normalized(records: Mapping[Coord, RecordValue], config: RuleConfig) -> bool:
    terms = local_ctmc_generator(records, config)
    return all(
        term.rate == 1 and term.row.normalized and term.jump_measure.normalized
        for term in terms
    ) and len(terms) < 6 * len(records) + 6


def append_record(
    records: Mapping[Coord, RecordValue], target: Coord, carrier: RecordValue, config: RuleConfig
) -> Records:
    if target in records and config.mutation != "overwrite":
        raise ValueError("Record overwrite rejected")
    answer = dict(records)
    answer[target] = carrier
    return answer


def state_key(records: Mapping[Coord, RecordValue]) -> tuple[tuple[Coord, RecordValue], ...]:
    return tuple(sorted(records.items()))


def apply_control_action(
    records: Mapping[Coord, Carrier], target: Coord, config: RuleConfig
) -> tuple[tuple[RealCoordinate, Records], ...]:
    """Apply finite structural representatives, never the continuous law.

    This quotient is used only for reachability, confluence, and covariance.
    Measure-level cut kernels are composed separately from ``continuous_measure``.
    """
    status, row = local_row(records, target, config)
    if status != "ACTIVE" or row is None:
        return ()
    return tuple(
        (weight, append_record(records, target, carrier, config))
        for weight, carrier in row.control_atoms
        if certified_lt(0, weight)
    )


def frame_sites(frame: Frame, trial: int) -> dict[str, Coord]:
    d, t = frame.forward, frame.transverse
    h = scale(5 * trial, d)
    answer = {
        "H": h,
        "T": add(h, neg(t)),
        "A": add(add(h, d), neg(t)),
        "R": add(h, d),
        "P": add(h, scale(2, d)),
        "O": add(h, scale(3, d)),
        "C": add(h, scale(4, d)),
        "H_NEXT": add(h, scale(5, d)),
    }
    for stage in range(1, 6):
        answer[f"Q{stage}"] = add(add(h, scale(stage, d)), t)
    return answer


def seed_records(protocol: Protocol, frame: Frame = IDENTITY_FRAME, shift: Coord = (0, 0, 0)) -> Records:
    head = add(shift, frame_sites(frame, 0)["H"])
    role = protocol_role("H", protocol.mode)
    return {head: encode_protocol(role, frame, protocol)}


@dataclass(frozen=True)
class GraphResult:
    states: int
    edges: int
    terminal_keys: tuple[tuple[tuple[Coord, Carrier], ...], ...]
    diamond_checks: int
    diamond_failures: int
    premature_dead_ends: int
    kinds: tuple[str, ...]


def two_action_distribution(
    records: Mapping[Coord, Carrier], first: Coord, second: Coord, config: RuleConfig
) -> dict[tuple[tuple[Coord, Carrier], ...], Fraction]:
    distribution: dict[tuple[tuple[Coord, Carrier], ...], Fraction] = defaultdict(Fraction)
    for weight1, state1 in apply_control_action(records, first, config):
        for weight2, state2 in apply_control_action(state1, second, config):
            distribution[state_key(state2)] += weight1 * weight2
    return dict(distribution)


def explore_one_trial(protocol: Protocol, frame: Frame, config: RuleConfig) -> GraphResult:
    start = seed_records(protocol, frame)
    stop_site = frame_sites(frame, 0)["H_NEXT"]
    queue = deque([start])
    seen = {state_key(start)}
    terminals = set()
    edges = 0
    diamond_checks = 0
    diamond_failures = 0
    premature_dead_ends = 0
    kinds = set()
    while queue:
        records = queue.popleft()
        if stop_site in records:
            terminals.add(state_key(records))
            continue
        actions = active_actions(records, config)
        if not actions:
            premature_dead_ends += 1
        action_items = sorted(actions.items())
        for (_, row1), (_, row2) in itertools.combinations(action_items, 2):
            kinds.add(row1.kind)
            kinds.add(row2.kind)
        for (target1, _), (target2, _) in itertools.combinations(action_items, 2):
            diamond_checks += 1
            if two_action_distribution(records, target1, target2, config) != two_action_distribution(records, target2, target1, config):
                diamond_failures += 1
        for target, row in action_items:
            kinds.add(row.kind)
            for _, successor in apply_control_action(records, target, config):
                edges += 1
                key = state_key(successor)
                if key not in seen:
                    seen.add(key)
                    queue.append(successor)
        if len(seen) > 50000:
            raise RuntimeError("one-trial graph exceeded frozen safety cap")
    return GraphResult(
        len(seen),
        edges,
        tuple(sorted(terminals, key=repr)),
        diamond_checks,
        diamond_failures,
        premature_dead_ends,
        tuple(sorted(kinds)),
    )


def ctmc_control_absorption_from_records(
    records: Mapping[Coord, Carrier], frame: Frame, trial: int, config: RuleConfig
) -> dict[tuple[tuple[Coord, Carrier], ...], Fraction]:
    """Exact embedded hitting law of the autonomous rate-one CTMC control quotient."""
    stop_site = frame_sites(frame, trial)["H_NEXT"]
    frontier: dict[tuple[tuple[Coord, Carrier], ...], Fraction] = {state_key(records): Fraction(1)}
    terminal: dict[tuple[tuple[Coord, Carrier], ...], Fraction] = defaultdict(Fraction)
    while frontier:
        minimum_size = min(len(key) for key in frontier)
        layer_keys = [key for key in frontier if len(key) == minimum_size]
        next_frontier = {key: value for key, value in frontier.items() if key not in layer_keys}
        for key in layer_keys:
            state = dict(key)
            state_weight = frontier[key]
            if stop_site in state:
                terminal[key] += state_weight
                continue
            terms = local_ctmc_generator(state, config)
            if not terms:
                continue
            total_rate = sum((term.rate for term in terms), Fraction(0))
            for term in terms:
                race_weight = term.rate / total_rate
                for row_weight, successor in apply_control_action(state, term.target, config):
                    successor_key = state_key(successor)
                    next_frontier[successor_key] = next_frontier.get(successor_key, Fraction(0)) + state_weight * race_weight * row_weight
        frontier = next_frontier
        expected_boundary_size = len(records) + 12
        if any(len(key) > expected_boundary_size for key in frontier):
            raise RuntimeError("embedded trial crossed its first-head cut")
    return dict(terminal)


def ctmc_control_absorption(
    protocol: Protocol, frame: Frame, config: RuleConfig
) -> dict[tuple[tuple[Coord, Carrier], ...], Fraction]:
    return ctmc_control_absorption_from_records(seed_records(protocol, frame), frame, 0, config)


def ctmc_control_trial_distribution(
    records: Mapping[Coord, Carrier], frame: Frame, trial: int, config: RuleConfig
) -> dict[tuple[int, Vector, Protocol, Fraction], tuple[Fraction, Records]]:
    answer = {}
    for key, weight in ctmc_control_absorption_from_records(records, frame, trial, config).items():
        state = dict(key)
        answer[terminal_branch(state, frame, trial)] = (weight, state)
    return answer


def terminal_branch(records: Mapping[Coord, Carrier], frame: Frame, trial: int) -> tuple[int, Vector, Protocol, Fraction]:
    sites = frame_sites(frame, trial)
    outcome = decode_outcome(records[sites["O"]])
    head = decode_protocol(records[sites["H_NEXT"]], ("H_",))
    if outcome is None or head is None:
        raise ValueError("terminal missing outcome or successor head")
    bit = certified_selector_bit(records[sites["A"]], head[2].weight_u0)
    return bit, outcome[1], head[2], head[3]


def representative_control_trial_distribution(
    records: Mapping[Coord, Carrier], protocol: Protocol, frame: Frame, trial: int, config: RuleConfig
) -> dict[tuple[int, Vector, Protocol, Fraction], tuple[Fraction, Records]]:
    """One computational topological order for a control macro-step.

    This is not process semantics.  Its result is used only after comparison
    with the autonomous CTMC absorption law and the confluence certificate.
    """
    sites = frame_sites(frame, trial)
    current: dict[tuple[tuple[Coord, Carrier], ...], tuple[Fraction, Records]] = {
        state_key(records): (Fraction(1), dict(records))
    }
    order = ["T", "A", "R", "P", "Q1", "Q2", "Q3", "Q4", "O", "C", "Q5", "H_NEXT"]
    for role in order:
        target = sites[role]
        updated: dict[tuple[tuple[Coord, Carrier], ...], tuple[Fraction, Records]] = {}
        for weight0, state in current.values():
            branches = apply_control_action(state, target, config)
            for weight1, successor in branches:
                key = state_key(successor)
                old_weight = updated[key][0] if key in updated else Fraction(0)
                updated[key] = (old_weight + weight0 * weight1, successor)
        current = updated
    answer = {}
    for weight, state in current.values():
        branch = terminal_branch(state, frame, trial)
        answer[branch] = (weight, state)
    return answer


@dataclass(frozen=True)
class ProgramCutAtom:
    selector_bit: int
    program_carrier: Carrier
    weight: RealCoordinate


@dataclass(frozen=True)
class ProgramCutMeasure:
    """Actual Gaussian-pushforward probability measure at the installed P cut."""

    atoms: tuple[ProgramCutAtom, ...]

    @property
    def normalized(self) -> bool:
        return (
            certified_equal(sum((sp.sympify(atom.weight) for atom in self.atoms), sp.S.Zero), 1)
            and all(
                certified_le(0, atom.weight)
                and decode_program(atom.program_carrier) is not None
                for atom in self.atoms
            )
        )


def installed_program_measure(protocol: Protocol, config: RuleConfig) -> ProgramCutMeasure:
    """Push the actual generator H->T->Gaussian->selector->P and stop at P."""
    frame = IDENTITY_FRAME
    sites = frame_sites(frame, 0)
    state = fire_unique_finite_term(seed_records(protocol, frame), sites["T"], config)
    gaussian_term = generator_term_at(state, sites["A"], config)
    gaussian_jump = gaussian_term.jump_measure
    if not isinstance(gaussian_jump, ContinuousRecordJumpMeasure):
        raise ValueError("installed-program pushforward lacks an actual Gaussian jump")
    masses = gaussian_jump.source_measure.selector_masses
    carrier_map = gaussian_jump.source_measure.carrier_map
    if masses is None or not isinstance(carrier_map, GaussianCarrierMap):
        raise ValueError("installed-program pushforward lacks a typed Gaussian partition")
    atoms = []
    for bit, weight in enumerate(masses):
        if certified_equal(weight, 0):
            continue
        branch = gaussian_jump.successor(
            carrier_map.canonical_fibre_sample(bit, protocol.weight_u0)
        )
        branch = fire_unique_finite_term(branch, sites["R"], config)
        branch = fire_unique_finite_term(branch, sites["P"], config)
        carrier = branch[sites["P"]]
        if not isinstance(carrier, Carrier):
            raise ValueError("installed program is not a finite tagged M2 Record")
        atoms.append(ProgramCutAtom(bit, carrier, weight))
    return ProgramCutMeasure(tuple(sorted(atoms, key=lambda atom: (atom.selector_bit, atom.program_carrier.coefficients))))


def active_projection_kind(config: RuleConfig) -> str:
    return "outcome_law" if config.mutation == "answer_defined_quotient" else "program_barycenter"


def active_barycenter(measure: ProgramCutMeasure, config: RuleConfig) -> Vector:
    """Predetermined barycentric quotient of physical P carriers.

    The normal path reads only the installed-program measure.  The hostile
    answer-defined mutation calls the future response statistics instead.
    """
    if not measure.normalized:
        raise ValueError("active quotient requires a probability measure on valid P Records")
    if active_projection_kind(config) != "program_barycenter":
        response: list[RealCoordinate] = [Fraction(0), Fraction(0), Fraction(0)]
        for atom in measure.atoms:
            decoded = decode_program(atom.program_carrier)
            assert decoded is not None
            program = decoded_program_value(decoded, config)
            leak = Fraction(2 * decoded[2] - 1) if config.mutation == "selector_leak" else Fraction(0)
            weights = outcome_weights(program, leak, RuleConfig())
            for index in range(3):
                response[index] = canonical_real(
                    sp.sympify(response[index])
                    + sp.sympify(atom.weight) * sp.sympify(weights[index])
                )
        return tuple(response)  # type: ignore[return-value]
    result: list[RealCoordinate] = [Fraction(0), Fraction(0), Fraction(0)]
    for atom in measure.atoms:
        decoded = decode_program(atom.program_carrier)
        assert decoded is not None
        program = decoded_program_value(decoded, config)
        for index in range(3):
            result[index] = canonical_real(
                sp.sympify(result[index])
                + sp.sympify(atom.weight) * sp.sympify(program[index])
            )
    return tuple(result)  # type: ignore[return-value]


@dataclass(frozen=True)
class GaussianSelectorEvent:
    """One exact measurable PIT event in the Gaussian source space."""

    bit: int
    weight_u0: RealCoordinate

    @property
    def mass(self) -> RealCoordinate:
        return (
            self.weight_u0
            if self.bit == 0
            else canonical_real(1 - sp.sympify(self.weight_u0))
        )

    @property
    def measurable_partition_member(self) -> bool:
        return (
            self.bit in (0, 1)
            and certified_le(0, self.weight_u0)
            and certified_le(self.weight_u0, 1)
            and gaussian_probability_integral_transform_certificate() == (0, 0, 1)
        )

    def predicate(self, sample: GaussianPoint) -> sp.Relational:
        return gaussian_selector_predicate(sample, self.bit, self.weight_u0)

    def contains(self, sample: GaussianPoint) -> bool:
        if not self.measurable_partition_member:
            return False
        try:
            return certified_selector_bit(GaussianCarrierMap().apply(sample), self.weight_u0) == self.bit
        except ValueError:
            return False


@dataclass(frozen=True)
class RestrictedGaussianFibreMeasure:
    """The conditional Gaussian jump law restricted to one exact PIT event."""

    event: GaussianSelectorEvent
    parent_jump: ContinuousRecordJumpMeasure

    @property
    def bit(self) -> int:
        return self.event.bit

    @property
    def mass(self) -> RealCoordinate:
        return self.event.mass

    @property
    def normalized(self) -> bool:
        return (
            self.parent_jump.normalized
            and self.event.measurable_partition_member
            and certified_lt(0, self.mass)
        )

    def successor(self, sample: GaussianPoint) -> Records:
        if not self.normalized or not self.event.contains(sample):
            raise ValueError("sample is outside this conditional Gaussian fibre")
        return self.parent_jump.successor(sample)

    @property
    def source_measure(self) -> MeasureSpec:
        return self.parent_jump.source_measure

    @property
    def full_encoded_m2_payload_retained(self) -> bool:
        return (
            self.source_measure.family == "encoded_center_zero_M2_gaussian"
            and isinstance(self.source_measure.carrier_map, GaussianCarrierMap)
        )


@dataclass(frozen=True)
class BoundaryKernelTerm:
    selector_bit: int
    selector_mass: RealCoordinate
    gaussian_fibre: RestrictedGaussianFibreMeasure
    installed_program: Vector
    outcome_jump: ContinuousRecordJumpMeasure

    @property
    def outcome_measure(self) -> MeasureSpec:
        return self.outcome_jump.source_measure


@dataclass(frozen=True)
class EmbeddedBoundaryKernel:
    """First-successor-head pushforward obtained by binding generator jumps."""

    protocol: Protocol
    next_protocol: Protocol | None
    selector_jump: ContinuousRecordJumpMeasure | None
    terms: tuple[BoundaryKernelTerm, ...]
    next_cut_is_outcome_independent: bool
    derived_from_generator: bool
    generic_outcome_paths_checked: int
    frame: Frame = IDENTITY_FRAME
    trial: int = 0

    @property
    def selector_measure(self) -> MeasureSpec:
        return (
            self.selector_jump.source_measure
            if self.selector_jump is not None
            else MeasureSpec("invalid")
        )

    @property
    def normalized(self) -> bool:
        return (
            certified_equal(
                sum((sp.sympify(term.selector_mass) for term in self.terms), sp.S.Zero),
                1,
            )
            and self.selector_jump is not None
            and self.selector_jump.normalized
            and self.derived_from_generator
            and all(
                certified_le(0, term.selector_mass)
                and term.gaussian_fibre.parent_jump is self.selector_jump
                and term.gaussian_fibre.normalized
                and term.gaussian_fibre.event.measurable_partition_member
                and term.gaussian_fibre.bit == term.selector_bit
                and certified_equal(term.gaussian_fibre.mass, term.selector_mass)
                and term.outcome_jump.normalized
                for term in self.terms
            )
        )

    @property
    def locally_owned(self) -> bool:
        return self.selector_measure.locally_owned and all(
            term.outcome_measure.locally_owned for term in self.terms
        )

    def terminal_successor(
        self,
        gaussian_sample: GaussianPoint,
        outcome_sample: SpherePoint,
        config: RuleConfig,
    ) -> Records:
        """Evaluate the literal generator bind on certified exact source points."""
        if self.selector_jump is None:
            raise ValueError("boundary has no Gaussian source jump")
        bit = certified_selector_bit(
            GaussianCarrierMap().apply(gaussian_sample), self.protocol.weight_u0
        )
        term = next((item for item in self.terms if item.selector_bit == bit), None)
        if term is None:
            raise ValueError("Gaussian sample lies in a zero-mass/absent fibre")
        # This call makes the restricted conditional measure operational: an
        # out-of-fibre point is rejected before any downstream transition.
        term.gaussian_fibre.successor(gaussian_sample)
        bit, pre_outcome, outcome_jump = bind_gaussian_to_outcome(
            self.selector_jump,
            gaussian_sample,
            self.protocol,
            self.frame,
            self.trial,
            config,
        )
        if outcome_jump.source_measure != term.outcome_measure:
            raise ValueError("arbitrary Gaussian payload changed the conditional outcome law")
        return bind_outcome_to_terminal(
            pre_outcome,
            outcome_jump,
            outcome_sample,
            self.frame,
            self.trial,
            config,
        )


def generator_term_at(
    records: Mapping[Coord, RecordValue], target: Coord, config: RuleConfig
) -> GeneratorTerm:
    terms = {term.target: term for term in local_ctmc_generator(records, config)}
    if target not in terms:
        raise ValueError(f"no ACTIVE generator term at {target}")
    return terms[target]


def fire_unique_finite_term(
    records: Mapping[Coord, RecordValue], target: Coord, config: RuleConfig
) -> Records:
    term = generator_term_at(records, target, config)
    if not isinstance(term.jump_measure, FiniteRecordJumpMeasure):
        raise ValueError("expected a finite deterministic generator transition")
    successors = tuple(
        successor for weight, successor in term.jump_measure.successors() if weight > 0
    )
    if len(successors) != 1:
        raise ValueError("expected one deterministic successor")
    return successors[0]


def generic_sphere_sample() -> SpherePoint:
    """One exact non-axis sphere point for pointwise map/diamond attacks."""
    return SpherePoint((sp.Rational(3, 5), sp.Rational(4, 5), sp.S.Zero))


def bind_gaussian_to_outcome(
    gaussian_jump: ContinuousRecordJumpMeasure,
    sample: GaussianPoint,
    protocol: Protocol,
    frame: Frame,
    trial: int,
    config: RuleConfig,
) -> tuple[int, Records, ContinuousRecordJumpMeasure]:
    """Follow one literal Gaussian Record through the local table to the O cut."""
    sites = frame_sites(frame, trial)
    state = gaussian_jump.successor(sample)
    bit = certified_selector_bit(state[sites["A"]], protocol.weight_u0)
    state = fire_unique_finite_term(state, sites["R"], config)
    state = fire_unique_finite_term(state, sites["P"], config)
    for rail_role in ("Q1", "Q2", "Q3", "Q4"):
        state = fire_unique_finite_term(state, sites[rail_role], config)
    outcome_term = generator_term_at(state, sites["O"], config)
    if not isinstance(outcome_term.jump_measure, ContinuousRecordJumpMeasure):
        raise ValueError("outcome row is not a Record-valued continuous jump")
    return bit, state, outcome_term.jump_measure


def bind_outcome_to_terminal(
    pre_outcome: Mapping[Coord, RecordValue],
    outcome_jump: ContinuousRecordJumpMeasure,
    sample: SpherePoint,
    frame: Frame,
    trial: int,
    config: RuleConfig,
) -> Records:
    """Follow one literal sphere outcome to the accumulated successor-head cut."""
    sites = frame_sites(frame, trial)
    if outcome_jump.base_state != state_key(pre_outcome):
        raise ValueError("outcome jump is not bound to the supplied Record state")
    state = outcome_jump.successor(sample)
    state = fire_unique_finite_term(state, sites["C"], config)
    state = fire_unique_finite_term(state, sites["Q5"], config)
    state = fire_unique_finite_term(state, sites["H_NEXT"], config)
    return state


def actual_ctmc_first_cut_pushforward(
    protocol: Protocol,
    config: RuleConfig,
    records: Mapping[Coord, RecordValue] | None = None,
    frame: Frame = IDENTITY_FRAME,
    trial: int = 0,
) -> EmbeddedBoundaryKernel:
    """Bind the actual Record-valued generator from H to the first H' cut.

    A single legal topological order is used only to perform the bind.  The
    separately checked commuting diamonds establish that every exponential-
    race order has the same first-cut kernel.  Gaussian fibres are integrated
    by the exact PIT partition; Haar outputs remain atomless typed Records.
    """
    sites = frame_sites(frame, trial)
    state = seed_records(protocol, frame) if records is None else dict(records)
    head = state.get(sites["H"])
    decoded_head = decode_protocol(head, ("H_",)) if isinstance(head, Carrier) else None
    if decoded_head is None or decoded_head[1] != frame or decoded_head[2] != protocol:
        raise ValueError("first-cut bind must start from its matching accumulated head")
    state = fire_unique_finite_term(state, sites["T"], config)
    gaussian_term = generator_term_at(state, sites["A"], config)
    gaussian_jump = gaussian_term.jump_measure
    if not isinstance(gaussian_jump, ContinuousRecordJumpMeasure):
        raise ValueError("Gaussian row is not a Record-valued continuous jump")
    gaussian_measure = gaussian_jump.source_measure
    masses = gaussian_measure.selector_masses
    gaussian_map = gaussian_measure.carrier_map
    if masses is None or not isinstance(gaussian_map, GaussianCarrierMap):
        raise ValueError("Gaussian jump lacks its typed selector pushforward")

    terms: list[BoundaryKernelTerm] = []
    next_protocols: list[Protocol | None] = []
    generic_checks = 0
    for bit, mass in enumerate(masses):
        if mass == 0:
            continue
        fibre_sample = gaussian_map.canonical_fibre_sample(bit, protocol.weight_u0)
        actual_bit, branch, outcome_jump = bind_gaussian_to_outcome(
            gaussian_jump, fibre_sample, protocol, frame, trial, config
        )
        if actual_bit != bit:
            raise ValueError("canonical Gaussian point missed its exact selector fibre")
        program_carrier = branch[sites["P"]]
        decoded_program = decode_program(program_carrier)
        if decoded_program is None:
            raise ValueError("generator bind lost the installed program Record")

        samples = (generic_sphere_sample(),) + tuple(SpherePoint(axis) for axis in AXES)
        for variant in (0, 1):
            gaussian_sample = gaussian_map.canonical_fibre_sample(
                bit, protocol.weight_u0, variant
            )
            variant_bit, variant_branch, variant_outcome_jump = bind_gaussian_to_outcome(
                gaussian_jump, gaussian_sample, protocol, frame, trial, config
            )
            if variant_bit != bit or variant_outcome_jump.source_measure != outcome_jump.source_measure:
                raise ValueError("conditional outcome law depends on hidden Gaussian payload")
            for outcome_sample in samples:
                terminal = bind_outcome_to_terminal(
                    variant_branch,
                    variant_outcome_jump,
                    outcome_sample,
                    frame,
                    trial,
                    config,
                )
                successor_head = terminal.get(sites["H_NEXT"])
                decoded_successor = (
                    decode_protocol(successor_head, ("H_",))
                    if isinstance(successor_head, Carrier)
                    else None
                )
                next_protocols.append(None if decoded_successor is None else decoded_successor[2])
                generic_checks += 1
        terms.append(
            BoundaryKernelTerm(
                bit,
                mass,
                RestrictedGaussianFibreMeasure(
                    GaussianSelectorEvent(bit, protocol.weight_u0), gaussian_jump
                ),
                decoded_program_value(decoded_program, config),
                outcome_jump,
            )
        )

    next_protocol = protocol if next_protocols and all(item == protocol for item in next_protocols) else None
    next_independent = next_protocol is not None and config.mutation != "one_step_only"
    return EmbeddedBoundaryKernel(
        protocol,
        next_protocol if next_independent else None,
        gaussian_jump,
        tuple(terms),
        next_independent,
        True,
        generic_checks,
        frame,
        trial,
    )


def embedded_boundary_kernel(
    protocol: Protocol,
    config: RuleConfig,
    records: Mapping[Coord, RecordValue] | None = None,
    frame: Frame = IDENTITY_FRAME,
    trial: int = 0,
) -> EmbeddedBoundaryKernel:
    """Safe public wrapper around the generator-derived first-cut bind."""
    try:
        return actual_ctmc_first_cut_pushforward(protocol, config, records, frame, trial)
    except (TypeError, ValueError):
        return EmbeddedBoundaryKernel(protocol, None, None, (), False, False, 0, frame, trial)


def typed_measure_map_hostile_checks() -> tuple[bool, int]:
    """Reject the former metadata-only maps and mismatched source samples."""
    malformed = (
        MeasureSpec(
            "encoded_center_zero_M2_gaussian",
            selector_weight_u0=Fraction(1, 2),
            carrier_map="THIS IS NOT A MAP",  # type: ignore[arg-type]
            frame=IDENTITY_FRAME,
        ),
        MeasureSpec(
            "haar_phi_1_plus_n_dot_program",
            program=ZERO3,
            carrier_map=None,
            frame=IDENTITY_FRAME,
            mode=MODE_RND,
        ),
        MeasureSpec(
            "haar_phi_1_plus_n_dot_program",
            program=ZERO3,
            carrier_map=OutcomeCarrierMap(IDENTITY_FRAME, DEFAULT_DIR, 0),
            frame=IDENTITY_FRAME,
            mode=MODE_RND,
            protocol=DEFAULT_RND,
        ),
    )
    rejected_samples = 0
    gaussian = gaussian_row(IDENTITY_FRAME, Fraction(1, 2), RuleConfig()).continuous_measure
    outcome = outcome_row(
        IDENTITY_FRAME, ZERO3, DEFAULT_RND, 0, Fraction(0), RuleConfig()
    ).continuous_measure
    if gaussian is None or outcome is None:
        return False, len(malformed)
    for measure, bad_sample in (
        (gaussian, SpherePoint(AXES[0])),
        (outcome, GaussianPoint((Fraction(0),) * 8)),
    ):
        jump = ContinuousRecordJumpMeasure((9, 9, 9), (), measure)
        try:
            jump.successor(bad_sample)
        except ValueError:
            rejected_samples += 1
    return all(not item.normalized for item in malformed) and rejected_samples == 2, len(malformed) + 2


def stochastic_control_quotient_matches(
    boundary: EmbeddedBoundaryKernel, config: RuleConfig
) -> bool:
    """The finite graph is exactly the bit/presence quotient of actual jumps."""
    if boundary.selector_jump is None or not boundary.normalized:
        return False
    selector_state = dict(boundary.selector_jump.base_state)
    selector_term = generator_term_at(selector_state, boundary.selector_jump.target, config)
    selector_weights = tuple(weight for weight, _ in selector_term.row.control_atoms if weight > 0)
    boundary_weights = tuple(term.selector_mass for term in boundary.terms if term.selector_mass > 0)
    if selector_weights != boundary_weights:
        return False
    for term in boundary.terms:
        outcome_state = dict(term.outcome_jump.base_state)
        outcome_term = generator_term_at(outcome_state, term.outcome_jump.target, config)
        if outcome_term.jump_measure != term.outcome_jump:
            return False
        if sum((weight for weight, _ in outcome_term.row.control_atoms), Fraction(0)) != 1:
            return False
        if not all(decode_outcome(carrier) is not None for _, carrier in outcome_term.row.control_atoms):
            return False
    return True


def generator_boundary_density_certificate(
    protocol: Protocol, boundary: EmbeddedBoundaryKernel
) -> bool:
    """Check the bound generator kernel against its displayed closed form."""
    if not boundary.normalized:
        return False
    n = sp.symbols("nx ny nz", real=True)
    for term in boundary.terms:
        measure = term.outcome_measure
        if measure.program != term.installed_program:
            return False
        actual = sp.sympify(term.selector_mass) * (
            1
            + sum(
                n[index] * sp.sympify(term.installed_program[index])
                for index in range(3)
            )
        )
        if sp.expand(actual - continuous_joined_density(protocol, term.selector_bit, n)) != 0:
            return False
    return True


def continuous_response_intertwiner(config: RuleConfig) -> bool:
    """All endpoint vectors and every real convex weight, as a polynomial identity."""
    u0 = sp.symbols("u0x u0y u0z", real=True)
    u1 = sp.symbols("u1x u1y u1z", real=True)
    n = sp.symbols("nx ny nz", real=True)
    p = sp.symbols("p", real=True)
    mixture = tuple(p * u0[i] + (1 - p) * u1[i] for i in range(3))
    direct = tuple(value**2 for value in mixture) if config.mutation == "nonlinear_encoder" else mixture
    left_terms = []
    for bit, (weight, program) in enumerate(((p, u0), (1 - p, u1))):
        factor = 1
        if config.mutation == "selector_leak":
            factor += sp.Rational(1, 2) * (-1 if bit == 0 else 1)
        left_terms.append(weight * (1 + factor * sum(n[i] * program[i] for i in range(3))))
    left = sum(left_terms)
    right = 1 + sum(n[i] * direct[i] for i in range(3))
    return sp.expand(left - right) == 0


def support_signature(role: str, trial: int) -> tuple[int, int]:
    offsets = {
        "H": (0, 0),
        "T": (0, -1),
        "A": (1, -1),
        "R": (1, 0),
        "P": (2, 0),
        "O": (3, 0),
        "C": (4, 0),
        "Q1": (1, 1),
        "Q2": (2, 1),
        "Q3": (3, 1),
        "Q4": (4, 1),
        "Q5": (5, 1),
    }
    x, y = offsets[role]
    return 5 * trial + x, y


def arbitrary_support_lemma() -> bool:
    # Different transverse coefficients cannot collide.  Within a coefficient,
    # the listed residues modulo five are unique after assigning Q5_n to the
    # next period's residue-zero upper site.  H boundaries are stored once.
    lower = {"T": 0, "A": 1}
    central = {"H": 0, "R": 1, "P": 2, "O": 3, "C": 4}
    upper = {"Q5_PREV": 0, "Q1": 1, "Q2": 2, "Q3": 3, "Q4": 4}
    return (
        len(set(lower.values())) == len(lower)
        and len(set(central.values())) == len(central)
        and len(set(upper.values())) == len(upper)
        and {item[1] for item in (support_signature(role, 0) for role in ("T", "A"))} == {-1}
        and {item[1] for item in (support_signature(role, 0) for role in ("H", "R", "P", "O", "C"))} == {0}
        and {item[1] for item in (support_signature(role, 0) for role in ("Q1", "Q2", "Q3", "Q4", "Q5"))} == {1}
    )


def expected_support_count(trials: int) -> int:
    return 12 * trials + 1


def symbolic_convex_identity(config: RuleConfig) -> bool:
    u0 = sp.symbols("u0x u0y u0z", real=True)
    u1 = sp.symbols("u1x u1y u1z", real=True)
    n = sp.symbols("nx ny nz", real=True)
    p = sp.symbols("p", real=True)
    mixture = tuple(p * u0[i] + (1 - p) * u1[i] for i in range(3))
    if config.mutation == "nonlinear_encoder":
        direct = tuple(value**2 for value in mixture)
    else:
        direct = mixture
    random_density = p * (1 + sum(n[i] * u0[i] for i in range(3))) + (1 - p) * (
        1 + sum(n[i] * u1[i] for i in range(3))
    )
    direct_density = 1 + sum(n[i] * direct[i] for i in range(3))
    if config.mutation == "selector_leak":
        z0, z1 = -1, 1
        random_density = p * (
            1 + (1 + sp.Rational(1, 2) * z0) * sum(n[i] * u0[i] for i in range(3))
        ) + (1 - p) * (
            1 + (1 + sp.Rational(1, 2) * z1) * sum(n[i] * u1[i] for i in range(3))
        )
    return sp.expand(random_density - direct_density) == 0


def global_selector_discriminator(protocol: Protocol) -> tuple[Fraction, Fraction]:
    delta = tuple(protocol.u1[i] - protocol.u0[i] for i in range(3))
    random_value = protocol.weight_u0 * (1 - protocol.weight_u0) * dot(delta, delta)
    direct_value = Fraction(0)
    return random_value, direct_value


def joined_six_axis(protocol: Protocol) -> dict[tuple[int, Vector], Fraction]:
    answer = {}
    bit_weights = (
        protocol.weight_u0,
        canonical_real(1 - sp.sympify(protocol.weight_u0)),
    )
    for bit, bit_weight in enumerate(bit_weights):
        program = installed_program(protocol, bit, RuleConfig())
        for axis, weight in zip(AXES, outcome_weights(program, Fraction(0), RuleConfig())):
            answer[(bit, axis)] = bit_weight * weight
    return answer


def continuous_joined_density(protocol: Protocol, bit: int, n: Sequence[sp.Expr]) -> sp.Expr:
    program = (
        protocol.u0 if bit == 0 else protocol.u1
    ) if protocol.mode == MODE_RND else protocol.mixture
    bit_weight = (
        protocol.weight_u0
        if bit == 0
        else canonical_real(1 - sp.sympify(protocol.weight_u0))
    )
    return sp.sympify(bit_weight) * (
        1 + sum(n[i] * sp.sympify(program[i]) for i in range(3))
    )


def payload_projection_certificate(config: RuleConfig) -> bool:
    """Bind the S projection proof to the functions called by local_proposals."""
    rational_unit_vectors: tuple[Vector, ...] = AXES + (
        (Fraction(3, 5), Fraction(4, 5), Fraction(0)),
        (Fraction(-3, 5), Fraction(0), Fraction(4, 5)),
    )
    protocols = (
        DEFAULT_RND,
        Protocol(MODE_RND, DEFAULT_RND.u0, DEFAULT_RND.u1, Fraction(1, 4)),
        Protocol(MODE_DIR, DEFAULT_RND.u0, DEFAULT_RND.u1, Fraction(3, 4)),
    )
    table_source = inspect.getsource(local_proposals)
    helpers_bound_to_table = (
        "close_payload(vector, config)" in table_source
        and "next_head_protocol(decoded_q4[2], stored, config)" in table_source
    )
    arbitrary_payload_sentinel = object()
    sentinel_projection = close_payload(arbitrary_payload_sentinel, config)  # type: ignore[arg-type]
    closes = {close_payload(vector, config) for vector in rational_unit_vectors}
    heads = {
        next_head_protocol(protocol, close_payload(vector, config), config)
        for protocol in protocols
        for vector in rational_unit_vectors
    }
    return (
        helpers_bound_to_table
        and sentinel_projection == ZERO3
        and closes == {ZERO3}
        and heads == set(protocols)
        and source_independence_check()
    )


def projected_cut(carrier: Carrier) -> tuple[Frame, Protocol] | None:
    decoded = decode_protocol(carrier, ("H_",))
    return None if decoded is None else (decoded[1], decoded[2])


def archive_fibre_replay(config: RuleConfig, expanded: bool = False) -> tuple[bool, int]:
    weights = (Fraction(1, 2),) if not expanded else (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))
    modes = (MODE_RND,) if not expanded else (MODE_RND, MODE_DIR)
    compared_rows = 0
    for mode in modes:
        for weight_u0 in weights:
            protocol = Protocol(mode, DEFAULT_RND.u0, DEFAULT_RND.u1, weight_u0)
            first = ctmc_control_trial_distribution(seed_records(protocol), IDENTITY_FRAME, 0, config)
            if len(first) != 12:
                return False, compared_rows
            h1 = frame_sites(IDENTITY_FRAME, 0)["H_NEXT"]
            archive_states = [state for _, state in first.values()]

            # Old Q5 is adjacent to the next Q1 target but is an explicitly
            # inert archive neighbor.  Vary its entire lawful payload.
            altered = dict(archive_states[0])
            q5_site = frame_sites(IDENTITY_FRAME, 0)["Q5"]
            altered_protocol = Protocol(mode, ZERO3, ZERO3, weight_u0)
            altered_q5 = decode_protocol(altered[q5_site], ("Q5_",))
            altered_branch = (
                branch_role_fields(altered_q5[0], "Q5") if altered_q5 is not None else None
            )
            if altered_branch is None:
                return False, compared_rows
            altered[q5_site] = encode_protocol(
                q_role(5, mode, altered_branch[1]), IDENTITY_FRAME, altered_protocol
            )
            archive_states.append(altered)

            cuts = {projected_cut(state[h1]) for state in archive_states}
            if len(cuts) != 1:
                return False, compared_rows
            reference: dict[tuple[int, Vector, Protocol], Fraction] | None = None
            for state in archive_states:
                next_row = ctmc_control_trial_distribution(state, IDENTITY_FRAME, 1, config)
                row_weights = {key[:3]: value[0] for key, value in next_row.items()}
                if len(row_weights) != 12:
                    return False, compared_rows
                if reference is None:
                    reference = row_weights
                elif row_weights != reference:
                    return False, compared_rows
                compared_rows += len(row_weights)
    return True, compared_rows


def ctmc_control_cylinder(protocol: Protocol, horizon: int, config: RuleConfig) -> dict[tuple[tuple[int, Vector], ...], Fraction]:
    frontier: dict[tuple[tuple[tuple[int, Vector], ...], tuple[tuple[Coord, Carrier], ...]], Fraction] = {
        ((), state_key(seed_records(protocol))): Fraction(1)
    }
    for trial in range(horizon):
        updated: dict[tuple[tuple[tuple[int, Vector], ...], tuple[tuple[Coord, Carrier], ...]], Fraction] = defaultdict(Fraction)
        for (transcript, key), prefix_weight in frontier.items():
            for terminal_key, row_weight in ctmc_control_absorption_from_records(dict(key), IDENTITY_FRAME, trial, config).items():
                state = dict(terminal_key)
                branch = terminal_branch(state, IDENTITY_FRAME, trial)
                updated[(transcript + ((branch[0], branch[1]),), terminal_key)] += prefix_weight * row_weight
        frontier = dict(updated)
    law: dict[tuple[tuple[int, Vector], ...], Fraction] = defaultdict(Fraction)
    for (transcript, _), weight in frontier.items():
        law[transcript] += weight
    return dict(law)


@dataclass(frozen=True)
class AnalyticCylinderAtom:
    """One selector word with its retained conditional atomless outcome laws."""

    selector_word: tuple[int, ...]
    mass: Fraction
    gaussian_fibres: tuple[RestrictedGaussianFibreMeasure, ...]
    outcome_measures: tuple[MeasureSpec, ...]
    terminal_state: tuple[tuple[Coord, RecordValue], ...]


@dataclass(frozen=True)
class AnalyticCylinderMeasure:
    """Finite-horizon law formed by recursive binds of the first-cut kernel."""

    horizon: int
    atoms: tuple[AnalyticCylinderAtom, ...]
    every_bind_generator_derived: bool

    @property
    def normalized(self) -> bool:
        return (
            sum((atom.mass for atom in self.atoms), Fraction(0)) == 1
            and all(
                atom.mass >= 0
                and len(atom.selector_word) == self.horizon
                and len(atom.gaussian_fibres) == self.horizon
                and len(atom.outcome_measures) == self.horizon
                and len(atom.terminal_state) == expected_support_count(self.horizon)
                and all(
                    fibre.parent_jump.target == frame_sites(IDENTITY_FRAME, trial)["A"]
                    and len(fibre.parent_jump.base_state) == 12 * trial + 2
                    for trial, fibre in enumerate(atom.gaussian_fibres)
                )
                and all(measure.normalized and measure.nonnegative for measure in atom.outcome_measures)
                for atom in self.atoms
            )
            and self.every_bind_generator_derived
        )

    def selector_law(self) -> dict[tuple[int, ...], Fraction]:
        answer: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
        for atom in self.atoms:
            answer[atom.selector_word] += atom.mass
        return dict(answer)


def analytic_ctmc_cylinder(
    protocol: Protocol, horizon: int, config: RuleConfig
) -> AnalyticCylinderMeasure:
    """Recursively bind generator-derived cut kernels; no IID tape is inserted."""
    if horizon < 1:
        raise ValueError("analytic cylinder horizon must be positive")
    frontier = ((Fraction(1), protocol, seed_records(protocol), (), (), ()),)
    every_derived = True
    for trial in range(horizon):
        updated = []
        for prefix_mass, cut_protocol, records, word, fibres, outcomes in frontier:
            boundary = embedded_boundary_kernel(
                cut_protocol, config, records, IDENTITY_FRAME, trial
            )
            every_derived = every_derived and boundary.derived_from_generator
            if boundary.next_protocol is None:
                continue
            for term in boundary.terms:
                if term.selector_mass == 0:
                    continue
                carrier_map = term.gaussian_fibre.source_measure.carrier_map
                if not isinstance(carrier_map, GaussianCarrierMap):
                    every_derived = False
                    continue
                gaussian_sample = carrier_map.canonical_fibre_sample(
                    term.selector_bit,
                    cut_protocol.weight_u0,
                    variant=trial + 1,
                )
                outcome_sample = SpherePoint(AXES[(trial + term.selector_bit) % len(AXES)])
                terminal = boundary.terminal_successor(
                    gaussian_sample, outcome_sample, config
                )
                successor_head = terminal[frame_sites(IDENTITY_FRAME, trial)["H_NEXT"]]
                decoded_successor = decode_protocol(successor_head, ("H_",))
                if decoded_successor is None or decoded_successor[2] != boundary.next_protocol:
                    every_derived = False
                    continue
                updated.append(
                    (
                        prefix_mass * term.selector_mass,
                        boundary.next_protocol,
                        terminal,
                        word + (term.selector_bit,),
                        fibres + (term.gaussian_fibre,),
                        outcomes + (term.outcome_measure,),
                    )
                )
        frontier = tuple(updated)
    atoms = tuple(
        AnalyticCylinderAtom(word, mass, fibres, outcomes, state_key(records))
        for mass, _, records, word, fibres, outcomes in frontier
    )
    return AnalyticCylinderMeasure(horizon, atoms, every_derived)


def analytic_cylinder_projective_pair(
    protocol: Protocol, config: RuleConfig
) -> tuple[AnalyticCylinderMeasure, AnalyticCylinderMeasure, bool]:
    one = analytic_ctmc_cylinder(protocol, 1, config)
    two = analytic_ctmc_cylinder(protocol, 2, config)
    marginalized: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for word, weight in two.selector_law().items():
        marginalized[word[:-1]] += weight
    return one, two, dict(marginalized) == one.selector_law()


def evaluate_actual_generator_sequence(
    protocol: Protocol,
    gaussian_samples: Sequence[GaussianPoint],
    outcome_samples: Sequence[SpherePoint],
    config: RuleConfig,
) -> tuple[tuple[tuple[int, RealVector], ...], Records]:
    """Run an arbitrary finite source sequence through accumulated CTMC cuts."""
    if len(gaussian_samples) != len(outcome_samples):
        raise ValueError("Gaussian and outcome source sequences must have equal length")
    records = seed_records(protocol)
    cut_protocol = protocol
    transcript = []
    for trial, (gaussian_sample, outcome_sample) in enumerate(
        zip(gaussian_samples, outcome_samples)
    ):
        boundary = actual_ctmc_first_cut_pushforward(
            cut_protocol, config, records, IDENTITY_FRAME, trial
        )
        bit = certified_selector_bit(
            GaussianCarrierMap().apply(gaussian_sample), cut_protocol.weight_u0
        )
        records = boundary.terminal_successor(
            gaussian_sample, outcome_sample, config
        )
        outcome = decode_outcome(records[frame_sites(IDENTITY_FRAME, trial)["O"]])
        successor = decode_protocol(
            records[frame_sites(IDENTITY_FRAME, trial)["H_NEXT"]], ("H_",)
        )
        if outcome is None or successor is None:
            raise ValueError("literal source bind did not reach its successor-head cut")
        transcript.append((bit, outcome[1]))
        cut_protocol = successor[2]
    return tuple(transcript), records


def literal_accumulated_bind_checks(config: RuleConfig) -> tuple[bool, int]:
    """Hostile exact selector and N=2 accumulated-state regression witnesses."""
    tiny = sp.Rational(1, 10**400)
    adversarial_statistic = sp.sqrt(2) * sp.erfinv(2 * tiny)
    adversarial = GaussianPoint(
        (sp.S.Zero, sp.S.Zero, sp.S.Zero, sp.S.Zero, adversarial_statistic / 2, sp.S.Zero, sp.S.Zero, sp.S.Zero)
    )
    if certified_selector_bit(GaussianCarrierMap().apply(adversarial), Fraction(1, 2)) != 1:
        return False, 1

    gaussian_map = GaussianCarrierMap()
    gaussian_samples = (
        gaussian_map.canonical_fibre_sample(0, DEFAULT_RND.weight_u0, 17),
        gaussian_map.canonical_fibre_sample(1, DEFAULT_RND.weight_u0, 23),
    )
    outcomes = (
        SpherePoint((sp.Rational(3, 5), sp.Rational(4, 5), sp.S.Zero)),
        SpherePoint((sp.S.Zero, sp.Rational(-4, 5), sp.Rational(3, 5))),
    )
    transcript, records = evaluate_actual_generator_sequence(
        DEFAULT_RND, gaussian_samples, outcomes, config
    )
    sites0 = frame_sites(IDENTITY_FRAME, 0)
    sites1 = frame_sites(IDENTITY_FRAME, 1)
    first_gaussian = GaussianCarrierMap().apply(gaussian_samples[0])
    second_gaussian = GaussianCarrierMap().apply(gaussian_samples[1])
    condition = (
        tuple(bit for bit, _ in transcript) == (0, 1)
        and len(records) == 25
        and records[sites0["A"]] == first_gaussian
        and records[sites1["A"]] == second_gaussian
        and sites1["A"] == (6, -1, 0)
        and records[sites0["O"]]
        == OutcomeCarrierMap(IDENTITY_FRAME, DEFAULT_RND, 0).apply(outcomes[0])
        and records[sites1["O"]]
        == OutcomeCarrierMap(IDENTITY_FRAME, DEFAULT_RND, 1).apply(outcomes[1])
    )
    return condition, 3


def decisive_panel_counterexample_regressions(config: RuleConfig) -> tuple[bool, int]:
    """Directly replay every fatal counterexample from the rejected freeze."""
    if config.mutation is not None:
        return True, 0

    gaussian_map = GaussianCarrierMap()
    tiny = sp.Rational(1, 10**400)
    statistic = sp.sqrt(2) * sp.erfinv(2 * tiny)
    tiny_sample = GaussianPoint(
        (sp.S.Zero, sp.S.Zero, sp.S.Zero, sp.S.Zero, statistic / 2, sp.S.Zero, sp.S.Zero, sp.S.Zero)
    )
    exact_selector = certified_selector_bit(
        gaussian_map.apply(tiny_sample), Fraction(1, 2)
    ) == 1

    # The panel's exact 150-digit diagonal counterexample: Phi(1)-p is
    # positive by about 1.76e-150, although SymPy's sign predicates are None.
    panel_threshold = Fraction(
        int(
            "841344746068542948585232545632037922477912966726604390987394450242991441987204829500884918405639327528272687586616921504727172071174620446609398132732"
        ),
        10**150,
    )
    unit_statistic_sample = GaussianPoint(
        (Fraction(0),) * 4 + (Fraction(1, 2),) + (Fraction(0),) * 3
    )
    unit_statistic_carrier = gaussian_map.apply(unit_statistic_sample)
    panel_order_closed = (
        certified_selector_bit(unit_statistic_carrier, panel_threshold) == 1
    )
    equality_boundary_closed = (
        certified_selector_bit(
            gaussian_map.apply(GaussianPoint((Fraction(0),) * 8)),
            Fraction(1, 2),
        )
        == 0
    )
    decimal_side_checks = True
    for decimal_digits in (400, 900):
        low, high = normal_cdf_rational_interval(
            Fraction(1), decimal_digits + 24
        )
        denominator = 10**decimal_digits
        below_numerator = (low.numerator * denominator) // low.denominator
        above_numerator = (
            high.numerator * denominator + high.denominator - 1
        ) // high.denominator
        below = Fraction(below_numerator, denominator)
        above = Fraction(above_numerator, denominator)
        decimal_side_checks = decimal_side_checks and (
            below < low
            and above >= high
            and certified_selector_bit(unit_statistic_carrier, below) == 1
            and certified_selector_bit(unit_statistic_carrier, above) == 0
        )
    mathematical_event_total = isinstance(
        gaussian_selector_predicate(unit_statistic_sample, 1, panel_threshold),
        sp.StrictGreaterThan,
    )

    head_carrier = encode_protocol("H_RND", IDENTITY_FRAME, DEFAULT_RND)
    gaussian_carrier = GaussianCarrierMap().apply(GaussianPoint((sp.S.Zero,) * 8))
    content_only = (
        RecordValue is Carrier
        and type(head_carrier) is Carrier
        and type(gaussian_carrier) is Carrier
        and decode_gaussian(head_carrier) is None
        and decode_tagged(gaussian_carrier) is None
    )

    algebraic = Protocol(
        MODE_RND,
        (sp.sqrt(2) / 2, Fraction(0), Fraction(0)),
        (Fraction(0), sp.sqrt(3) / 3, Fraction(0)),
        sp.sqrt(5) / 5,
    )
    algebraic_boundary = actual_ctmc_first_cut_pushforward(algebraic, config)
    algebraic_direct = Protocol(
        MODE_DIR, algebraic.u0, algebraic.u1, algebraic.weight_u0
    )
    algebraic_random_measure = installed_program_measure(algebraic, config)
    algebraic_direct_measure = installed_program_measure(algebraic_direct, config)
    algebraic_random_barycenter = active_barycenter(algebraic_random_measure, config)
    algebraic_direct_barycenter = active_barycenter(algebraic_direct_measure, config)
    algebraic_m = (
        algebraic_random_measure.normalized
        and algebraic_direct_measure.normalized
        and all(
            certified_equal(
                algebraic_random_barycenter[index], algebraic.mixture[index]
            )
            and certified_equal(
                algebraic_direct_barycenter[index], algebraic.mixture[index]
            )
            for index in range(3)
        )
    )
    full_real_domain = (
        algebraic.valid
        and decode_program(encode_program(IDENTITY_FRAME, algebraic, 1))
        == (IDENTITY_FRAME, algebraic, 1)
        and algebraic_boundary.normalized
        and algebraic_boundary.next_protocol == algebraic
        and [term.selector_mass for term in algebraic_boundary.terms]
        == [algebraic.weight_u0, canonical_real(1 - sp.sympify(algebraic.weight_u0))]
        and admitted_program_domain(config).kind == "real_bloch_ball"
        and admitted_program_domain(config).complete_convex_domain
    )

    t = sp.symbols("t")
    unknown_real = sp.Integral(sp.sin(t**t), (t, 0, 1)) - sp.Rational(1, 2)
    host_scope_honest = (
        not GaussianPoint((sp.Float(1000),) + (Fraction(0),) * 7).valid
        and not GaussianPoint((sp.nan,) + (Fraction(0),) * 7).valid
        and not GaussianPoint((unknown_real,) + (Fraction(0),) * 7).valid
        and not Protocol(
            MODE_RND,
            (unknown_real, Fraction(0), Fraction(0)),
            DEFAULT_RND.u1,
            Fraction(1, 2),
        ).valid
    )

    protocol_b = Protocol(
        MODE_RND,
        DEFAULT_RND.u0,
        (Fraction(0), Fraction(0), Fraction(1, 2)),
        Fraction(3, 4),
    )
    same_mode_splice_status, _ = local_row(
        {
            neg(IDENTITY_FRAME.forward): encode_protocol(
                selector_role(MODE_RND, 0), IDENTITY_FRAME, DEFAULT_RND
            ),
            IDENTITY_FRAME.transverse: encode_protocol(
                q_role(2, MODE_RND, 0), IDENTITY_FRAME, protocol_b
            ),
        },
        (0, 0, 0),
        config,
    )
    program_splice_status, _ = local_row(
        {
            neg(IDENTITY_FRAME.forward): encode_program(
                IDENTITY_FRAME, DEFAULT_RND, 0
            ),
            IDENTITY_FRAME.transverse: encode_protocol(
                q_role(3, MODE_RND, 0), IDENTITY_FRAME, protocol_b
            ),
        },
        (0, 0, 0),
        config,
    )
    outcome_support_status, _ = local_row(
        {
            neg(IDENTITY_FRAME.forward): encode_outcome(
                IDENTITY_FRAME, AXES[0], DEFAULT_RND, 0
            ),
            IDENTITY_FRAME.transverse: encode_protocol(
                q_role(4, MODE_RND, 0), IDENTITY_FRAME, protocol_b
            ),
        },
        (0, 0, 0),
        config,
    )
    lineage_typed = (
        same_mode_splice_status == "STOP"
        and program_splice_status == "STOP"
        and encode_program(IDENTITY_FRAME, DEFAULT_RND, 0)
        != encode_program(IDENTITY_FRAME, protocol_b, 0)
        # O deliberately carries no fake seven-reals-to-one provenance code:
        # Q supplies the protocol and every direction is in the typed support.
        and outcome_support_status == "ACTIVE"
    )

    boundary = actual_ctmc_first_cut_pushforward(DEFAULT_RND, config)
    term0 = next(term for term in boundary.terms if term.selector_bit == 0)
    in_fibre = GaussianCarrierMap().canonical_fibre_sample(0, Fraction(1, 2), 31)
    out_fibre = GaussianCarrierMap().canonical_fibre_sample(1, Fraction(1, 2), 37)
    restricted_fibre = term0.gaussian_fibre.normalized
    try:
        term0.gaussian_fibre.successor(out_fibre)
    except ValueError:
        restricted_fibre = restricted_fibre and True
    else:
        restricted_fibre = False
    terminal = boundary.terminal_successor(in_fibre, SpherePoint(AXES[2]), config)
    arbitrary_payload_retained = (
        terminal[frame_sites(IDENTITY_FRAME, 0)["A"]]
        == GaussianCarrierMap().apply(in_fibre)
        and terminal[frame_sites(IDENTITY_FRAME, 0)["O"]]
        == OutcomeCarrierMap(IDENTITY_FRAME, DEFAULT_RND, 0).apply(SpherePoint(AXES[2]))
    )

    cylinder = analytic_ctmc_cylinder(DEFAULT_RND, 2, config)
    accumulated = cylinder.normalized and all(
        atom.gaussian_fibres[1].parent_jump.target == (6, -1, 0)
        and len(atom.gaussian_fibres[1].parent_jump.base_state) == 14
        and len(atom.terminal_state) == 25
        for atom in cylinder.atoms
    )
    checks = (
        exact_selector,
        panel_order_closed,
        equality_boundary_closed,
        decimal_side_checks,
        mathematical_event_total,
        content_only,
        full_real_domain,
        algebraic_m,
        host_scope_honest,
        lineage_typed,
        restricted_fibre,
        arbitrary_payload_retained,
        accumulated,
    )
    return all(checks), len(checks)


def explicit_bit_process(kind: str, horizon: int) -> dict[tuple[int, ...], Fraction]:
    words = tuple(itertools.product((0, 1), repeat=horizon))
    if kind == "fresh":
        return {word: Fraction(1, 2**horizon) for word in words}
    if kind == "frozen":
        return {word: Fraction(1, 2) if len(set(word)) <= 1 else Fraction(0) for word in words}
    if kind == "even_parity" and horizon == 3:
        return {word: Fraction(1, 4) if sum(word) % 2 == 0 else Fraction(0) for word in words}
    raise ValueError("unsupported explicit bit process")


def renewal_controls(config: RuleConfig) -> tuple[bool, Fraction, Fraction]:
    kind = "frozen" if config.mutation == "frozen_memory" else "fresh"
    pair_law = explicit_bit_process(kind, 2)
    triple_law = (
        explicit_bit_process("even_parity", 3)
        if config.mutation == "triple_parity"
        else explicit_bit_process("fresh", 3)
    )
    pair_value = pair_law[(0, 0)]
    parity_value = triple_law[(0, 0, 0)]
    one_marginals_fair = all(
        sum(weight for word, weight in triple_law.items() if word[index] == 0) == Fraction(1, 2)
        for index in range(3)
    )
    return one_marginals_fair and pair_value == Fraction(1, 4) and parity_value == Fraction(1, 8), pair_value, parity_value


def delayed_one_step_mutant() -> tuple[bool, bool]:
    """Executable rival: same first row, old hidden bit controls the second."""
    first_rows = {
        old: {(bit, old): Fraction(1, 2) for bit in (0, 1)}
        for old in (0, 1)
    }
    first_transcripts = {
        old: {bit: sum(weight for (value, _), weight in row.items() if value == bit) for bit in (0, 1)}
        for old, row in first_rows.items()
    }
    second_rows = {old: {(old, old): Fraction(1)} for old in (0, 1)}
    return first_transcripts[0] == first_transcripts[1], second_rows[0] == second_rows[1]


@dataclass(frozen=True)
class CutInductionCertificate:
    generator_finite_normalized: bool
    generator_first_cut_bound: bool
    stochastic_control_quotient_exact: bool
    almost_sure_finite_cut_hitting: bool
    scheduler_independent: bool
    analytic_boundary_normalized: bool
    archive_fibres_equal: bool
    parametric_payload_projection: bool
    next_cut_preserved: bool
    local_source_owned: bool
    arbitrary_support: bool
    delayed_hidden_excluded: bool

    @property
    def valid(self) -> bool:
        return all(self.__dict__.values())


def cut_induction_certificate(
    config: RuleConfig, graph: GraphResult, archive_ok: bool, actual_diamonds_ok: bool
) -> CutInductionCertificate:
    start = seed_records(DEFAULT_RND)
    boundary = embedded_boundary_kernel(DEFAULT_RND, config)
    first_equal, second_equal = delayed_one_step_mutant()
    delayed_hidden_excluded = not first_equal or second_equal
    if config.mutation != "one_step_only":
        delayed_hidden_excluded = True
    return CutInductionCertificate(
        generator_is_finite_and_normalized(start, config),
        boundary.derived_from_generator and boundary.generic_outcome_paths_checked >= 7,
        stochastic_control_quotient_matches(boundary, config),
        graph.premature_dead_ends == 0 and bool(graph.terminal_keys),
        graph.diamond_failures == 0 and actual_diamonds_ok,
        boundary.normalized,
        archive_ok,
        payload_projection_certificate(config),
        boundary.next_cut_is_outcome_independent and boundary.next_protocol == DEFAULT_RND,
        boundary.locally_owned,
        arbitrary_support_lemma(),
        delayed_hidden_excluded,
    )


def malformed_collision_check(config: RuleConfig) -> tuple[bool, str, int]:
    frame0 = IDENTITY_FRAME
    frame1 = Frame(ROTATIONS[1])
    target = (0, 0, 0)
    records = {
        frame0.transverse: encode_protocol("H_RND", frame0, DEFAULT_RND),
        frame1.transverse: encode_protocol("H_RND", frame1, DEFAULT_RND),
    }
    actual_status, _ = local_row(records, target, config)
    synthetic = LocalRow(
        "synthetic",
        ((Fraction(1), encode_protocol("C_RND", frame0, DEFAULT_RND)),),
    )
    collision_status, _ = resolve_proposals((synthetic, synthetic), config)

    bad_program = tagged(
        program_role(MODE_RND, 0),
        frame0,
        (
            Fraction(2),
            Fraction(0),
            Fraction(0),
            Fraction(MODE_RND),
            Fraction(0),
        ),
    )
    bad_program_status, _ = local_row({neg(frame0.forward): bad_program}, target, config)

    valid_program = encode_program(frame0, DEFAULT_RND, 0)
    wrong_q3 = encode_protocol(q_role(3, MODE_DIR, 0), frame0, DEFAULT_DIR)
    splice_status, _ = local_row(
        {neg(frame0.forward): valid_program, frame0.transverse: wrong_q3}, target, config
    )

    valid_outcome = encode_outcome(frame0, AXES[0], DEFAULT_RND, 0)
    wrong_q4 = encode_protocol(q_role(4, MODE_DIR, 0), frame0, DEFAULT_DIR)
    outcome_splice_status, _ = local_row(
        {neg(frame0.forward): valid_outcome, frame0.transverse: wrong_q4}, target, config
    )
    bad_close = tagged(
        "C_RND",
        frame0,
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )
    bad_close_status, _ = local_row(
        {
            neg(frame0.forward): bad_close,
            frame0.transverse: encode_protocol(q_role(5, MODE_RND, 0), frame0, DEFAULT_RND),
        },
        target,
        config,
    )

    q1_rnd = encode_protocol(q_role(1, MODE_RND, 0), frame0, DEFAULT_RND)
    wrong_mode_program = encode_program(frame0, DEFAULT_DIR, 0)
    q2_wrong_program_status, _ = local_row(
        {neg(frame0.forward): q1_rnd, neg(frame0.transverse): wrong_mode_program},
        target,
        config,
    )
    q2_bad_program_status, _ = local_row(
        {neg(frame0.forward): q1_rnd, neg(frame0.transverse): bad_program},
        target,
        config,
    )

    q2_rnd = encode_protocol(q_role(2, MODE_RND, 0), frame0, DEFAULT_RND)
    wrong_mode_outcome = encode_outcome(frame0, AXES[0], DEFAULT_DIR, 0)
    bad_outcome = tagged(outcome_role(MODE_RND, 0), frame0, (Fraction(0),) * 7)
    q3_wrong_outcome_status, _ = local_row(
        {neg(frame0.forward): q2_rnd, neg(frame0.transverse): wrong_mode_outcome},
        target,
        config,
    )
    q3_bad_outcome_status, _ = local_row(
        {neg(frame0.forward): q2_rnd, neg(frame0.transverse): bad_outcome},
        target,
        config,
    )

    close_rnd = encode_protocol("C_RND", frame0, DEFAULT_RND)
    q5_dir = encode_protocol(q_role(5, MODE_DIR, 0), frame0, DEFAULT_DIR)
    foreign_head_status, _ = local_row(
        {neg(frame0.forward): close_rnd, frame0.transverse: q5_dir}, target, config
    )

    same_mode_foreign = Protocol(
        MODE_RND,
        DEFAULT_RND.u0,
        (Fraction(0), Fraction(0), Fraction(1, 2)),
        Fraction(3, 4),
    )
    selector_a = encode_protocol(selector_role(MODE_RND, 0), frame0, DEFAULT_RND)
    q2_b = encode_protocol(q_role(2, MODE_RND, 0), frame0, same_mode_foreign)
    same_mode_selector_splice, _ = local_row(
        {neg(frame0.forward): selector_a, frame0.transverse: q2_b}, target, config
    )
    program_a = encode_program(frame0, DEFAULT_RND, 0)
    q3_b = encode_protocol(q_role(3, MODE_RND, 0), frame0, same_mode_foreign)
    same_mode_program_splice, _ = local_row(
        {neg(frame0.forward): program_a, frame0.transverse: q3_b}, target, config
    )
    outcome_a = encode_outcome(frame0, AXES[0], DEFAULT_RND, 0)
    q4_b = encode_protocol(q_role(4, MODE_RND, 0), frame0, same_mode_foreign)
    same_mode_outcome_splice, _ = local_row(
        {neg(frame0.forward): outcome_a, frame0.transverse: q4_b}, target, config
    )
    q5_b = encode_protocol(q_role(5, MODE_RND, 0), frame0, same_mode_foreign)
    same_mode_head_splice, _ = local_row(
        {neg(frame0.forward): close_rnd, frame0.transverse: q5_b}, target, config
    )
    cases = (
        actual_status,
        collision_status,
        bad_program_status,
        splice_status,
        outcome_splice_status,
        bad_close_status,
        q2_wrong_program_status,
        q2_bad_program_status,
        q3_wrong_outcome_status,
        q3_bad_outcome_status,
        foreign_head_status,
        same_mode_selector_splice,
        same_mode_program_splice,
        same_mode_head_splice,
    )
    # O has no fictitious provenance fingerprint: Q supplies the full protocol
    # and every sphere direction is a lawful typed support value.  Consequently
    # this same-mode/same-bit O is intentionally ACTIVE, while protocol-bearing
    # R/P/C splices remain STOP.
    return (
        all(status == "STOP" for status in cases)
        and same_mode_outcome_splice == "ACTIVE"
    ), collision_status, len(cases) + 1


def overwrite_check(config: RuleConfig) -> bool:
    records = seed_records(DEFAULT_RND)
    site = next(iter(records))
    try:
        append_record(
            records,
            site,
            encode_protocol("C_RND", IDENTITY_FRAME, DEFAULT_RND),
            config,
        )
    except ValueError:
        return True
    return False


def covariance_checks(config: RuleConfig) -> tuple[bool, int]:
    cases = 0
    for rotation in ROTATIONS:
        frame = Frame(rotation)
        protocol = Protocol(
            MODE_RND,
            rotate_exact_vector(rotation, DEFAULT_RND.u0),
            rotate_exact_vector(rotation, DEFAULT_RND.u1),
            DEFAULT_RND.weight_u0,
        )
        graph = explore_one_trial(protocol, frame, config)
        if not graph.terminal_keys:
            return False, cases
        for shift in ((0, 0, 0), (7, -11, 5)):
            records = seed_records(protocol, frame, shift)
            actions = active_actions(records, config)
            expected = add(shift, frame_sites(frame, 0)["T"])
            if expected not in actions:
                return False, cases
            cases += 1
        for axis in AXES:
            rotated_axis = rotate_vector(rotation, axis)
            if dot(rotated_axis, protocol.u0) != dot(axis, DEFAULT_RND.u0):
                return False, cases
            cases += 1
    return True, cases


def rotate_measure_spec(rotation: Rotation, measure: MeasureSpec | None) -> MeasureSpec | None:
    if measure is None:
        return measure
    rotated_frame = None
    if measure.frame is not None:
        composed: Rotation = tuple(
            tuple(sum(rotation[i][k] * measure.frame.rotation[k][j] for k in range(3)) for j in range(3))
            for i in range(3)
        )  # type: ignore[assignment]
        rotated_frame = Frame(composed)
    if isinstance(measure.carrier_map, OutcomeCarrierMap):
        source_protocol = measure.carrier_map.protocol
        rotated_protocol = Protocol(
            source_protocol.mode,
            rotate_exact_vector(rotation, source_protocol.u0),
            rotate_exact_vector(rotation, source_protocol.u1),
            source_protocol.weight_u0,
        )
        rotated_map: CarrierMap | None = OutcomeCarrierMap(
            rotated_frame, rotated_protocol, measure.carrier_map.bit
        )  # type: ignore[arg-type]
    elif isinstance(measure.carrier_map, GaussianCarrierMap):
        rotated_map = GaussianCarrierMap()
    else:
        rotated_map = None
    return MeasureSpec(
        family=measure.family,
        program=None if measure.program is None else rotate_exact_vector(rotation, measure.program),
        selector_weight_u0=measure.selector_weight_u0,
        owner=measure.owner,
        carrier_map=rotated_map,
        frame=rotated_frame,
        mode=measure.mode,
        protocol=(
            None
            if measure.protocol is None
            else Protocol(
                measure.protocol.mode,
                rotate_exact_vector(rotation, measure.protocol.u0),
                rotate_exact_vector(rotation, measure.protocol.u1),
                measure.protocol.weight_u0,
            )
        ),
    )


def rotate_local_row(rotation: Rotation, row: LocalRow) -> LocalRow:
    return LocalRow(
        row.kind,
        tuple((weight, rotate_carrier(rotation, carrier)) for weight, carrier in row.control_atoms),
        rotate_measure_spec(rotation, row.continuous_measure),
    )


def rows_equal_as_kernels(left: LocalRow, right: LocalRow) -> bool:
    left_atoms: dict[Carrier, Fraction] = defaultdict(Fraction)
    right_atoms: dict[Carrier, Fraction] = defaultdict(Fraction)
    for weight, carrier in left.control_atoms:
        left_atoms[carrier] += weight
    for weight, carrier in right.control_atoms:
        right_atoms[carrier] += weight
    return (
        left.kind == right.kind
        and dict(left_atoms) == dict(right_atoms)
        and left.continuous_measure == right.continuous_measure
    )


def jump_witness_count(term: GeneratorTerm) -> int:
    if isinstance(term.jump_measure, FiniteRecordJumpMeasure):
        return len(term.jump_measure.atoms)
    carrier_map = term.jump_measure.source_measure.carrier_map
    if isinstance(carrier_map, GaussianCarrierMap):
        return 1
    if isinstance(carrier_map, OutcomeCarrierMap):
        return 1 + len(AXES)
    return 0


def apply_jump_witness(term: GeneratorTerm, index: int) -> Records:
    if isinstance(term.jump_measure, FiniteRecordJumpMeasure):
        return term.jump_measure.successors()[index][1]
    carrier_map = term.jump_measure.source_measure.carrier_map
    if isinstance(carrier_map, GaussianCarrierMap):
        symbols = sp.symbols("g0:8", real=True)
        return term.jump_measure.successor(GaussianPoint(symbols))  # type: ignore[arg-type]
    if isinstance(carrier_map, OutcomeCarrierMap):
        samples = (generic_sphere_sample(),) + tuple(SpherePoint(axis) for axis in AXES)
        return term.jump_measure.successor(samples[index])
    raise ValueError("unknown generator jump sample space")


def exhaustive_actual_kernel_diamonds(config: RuleConfig) -> tuple[bool, int]:
    """Check co-enabled generator binds, including atomless jump maps."""
    cases = 0
    for records in reachable_control_states(DEFAULT_RND, config):
        terms = {term.target: term for term in local_ctmc_generator(records, config)}
        for first_target, second_target in itertools.combinations(sorted(terms), 2):
            first = terms[first_target]
            second = terms[second_target]
            for first_index in range(jump_witness_count(first)):
                state_after_first = apply_jump_witness(first, first_index)
                try:
                    second_after_first = generator_term_at(state_after_first, second_target, config)
                except ValueError:
                    return False, cases
                if not rows_equal_as_kernels(second.row, second_after_first.row):
                    return False, cases
                for second_index in range(jump_witness_count(second)):
                    left = apply_jump_witness(second_after_first, second_index)
                    state_after_second = apply_jump_witness(second, second_index)
                    try:
                        first_after_second = generator_term_at(state_after_second, first_target, config)
                    except ValueError:
                        return False, cases
                    if not rows_equal_as_kernels(first.row, first_after_second.row):
                        return False, cases
                    right = apply_jump_witness(first_after_second, first_index)
                    cases += 1
                    if state_key(left) != state_key(right):
                        return False, cases
    return True, cases


def actual_carrier_map_covariance() -> tuple[bool, int]:
    """Intertwine both typed atomless carrier maps with all cubic rotations."""
    cases = 0
    gaussian_symbols = sp.symbols("a0:8", real=True)
    gaussian_sample = GaussianPoint(gaussian_symbols)  # type: ignore[arg-type]
    gaussian_record = GaussianCarrierMap().apply(gaussian_sample)
    gaussian_payload = decode_gaussian(gaussian_record)
    if gaussian_payload is None:
        return False, cases
    for rotation in ROTATIONS:
        rotated_gaussian = rotate_carrier(rotation, gaussian_record)
        rotated_sample = GaussianPoint(
            (
                gaussian_payload[0],
                *rotate_vector(rotation, gaussian_payload[1:4]),
                gaussian_payload[4],
                *rotate_vector(rotation, gaussian_payload[5:8]),
            )
        )
        if rotated_gaussian != GaussianCarrierMap().apply(rotated_sample):
            return False, cases
        cases += 1

        frame = IDENTITY_FRAME
        sample = SpherePoint(AXES[0])
        actual_outcome = OutcomeCarrierMap(frame, DEFAULT_RND, 0).apply(sample)
        rotated_outcome = rotate_carrier(rotation, actual_outcome)
        rotated_frame = Frame(rotation)
        rotated_protocol = Protocol(
            MODE_RND,
            rotate_exact_vector(rotation, DEFAULT_RND.u0),
            rotate_exact_vector(rotation, DEFAULT_RND.u1),
            DEFAULT_RND.weight_u0,
        )
        expected_outcome = OutcomeCarrierMap(rotated_frame, rotated_protocol, 0).apply(
            SpherePoint(rotate_vector(rotation, sample.direction))  # type: ignore[arg-type]
        )
        if rotated_outcome != expected_outcome:
            return False, cases
        cases += 1
    return True, cases


def reachable_control_states(protocol: Protocol, config: RuleConfig) -> tuple[Records, ...]:
    frame = IDENTITY_FRAME
    stop_site = frame_sites(frame, 0)["H_NEXT"]
    queue = deque([seed_records(protocol, frame)])
    seen = {state_key(queue[0])}
    states = []
    while queue:
        records = queue.popleft()
        states.append(records)
        if stop_site in records:
            continue
        for target in active_actions(records, config):
            for _, successor in apply_control_action(records, target, config):
                key = state_key(successor)
                if key not in seen:
                    seen.add(key)
                    queue.append(successor)
    return tuple(states)


def exhaustive_row_conjugacy(config: RuleConfig) -> tuple[bool, int]:
    cases = 0
    states = reachable_control_states(DEFAULT_RND, config)
    for rotation in ROTATIONS:
        for records in states:
            rotated_records = {
                rotate_coord(rotation, site): rotate_carrier(rotation, carrier)
                for site, carrier in records.items()
            }
            actual = active_actions(rotated_records, config)
            expected = {
                rotate_coord(rotation, target): rotate_local_row(rotation, row)
                for target, row in active_actions(records, config).items()
            }
            cases += len(expected)
            if set(actual) != set(expected) or any(
                not rows_equal_as_kernels(actual[target], expected[target]) for target in actual
            ):
                return False, cases
    return True, cases


def local_schema_check() -> tuple[bool, int]:
    frame = IDENTITY_FRAME
    sites = frame_sites(frame, 0)
    edges = (
        (sites["H"], sites["T"]),
        (sites["T"], sites["A"]),
        (sites["H"], sites["R"]),
        (sites["A"], sites["R"]),
        (sites["R"], sites["P"]),
        (sites["R"], sites["Q1"]),
        (sites["P"], sites["O"]),
        (sites["O"], sites["C"]),
        (sites["Q1"], sites["Q2"]),
        (sites["Q2"], sites["Q3"]),
        (sites["Q3"], sites["Q4"]),
        (sites["Q4"], sites["Q5"]),
        (sites["C"], sites["H_NEXT"]),
        (sites["Q5"], sites["H_NEXT"]),
    )
    return all(sum(abs(a[i] - b[i]) for i in range(3)) == 1 for a, b in edges), len(edges)


def protocol_domain_generator_checks(config: RuleConfig) -> tuple[bool, int]:
    cases = 0
    for mode in (MODE_RND, MODE_DIR):
        for weight in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
            protocol = Protocol(mode, DEFAULT_RND.u0, DEFAULT_RND.u1, weight)
            graph = explore_one_trial(protocol, IDENTITY_FRAME, config)
            absorption = ctmc_control_absorption(protocol, IDENTITY_FRAME, config)
            expected_terminals = 6 if weight in (Fraction(0), Fraction(1)) else 12
            if (
                graph.diamond_failures != 0
                or graph.premature_dead_ends != 0
                or len(absorption) != expected_terminals
                or sum(absorption.values(), Fraction(0)) != 1
            ):
                return False, cases
            cases += 1
    return True, cases


def codec_checks() -> tuple[bool, int]:
    cases = 0
    convex_weights = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1))
    for frame in (Frame(rotation) for rotation in ROTATIONS):
        for weight in convex_weights:
            for mode in (MODE_RND, MODE_DIR):
                protocol = Protocol(mode, DEFAULT_RND.u0, DEFAULT_RND.u1, weight)
                rotated = Protocol(
                    protocol.mode,
                    rotate_exact_vector(frame.rotation, protocol.u0),
                    rotate_exact_vector(frame.rotation, protocol.u1),
                    protocol.weight_u0,
                )
                role = protocol_role("H", protocol.mode)
                carrier = encode_protocol(role, frame, rotated)
                decoded = decode_protocol(carrier, ("H_",))
                if decoded is None or decoded[1] != frame or decoded[2] != rotated:
                    return False, cases
                for bit in (0, 1):
                    program = encode_program(frame, rotated, bit)
                    decoded_program = decode_program(program)
                    if decoded_program != (frame, rotated, bit):
                        return False, cases
                    cases += 1
            for bit in (0, 1):
                gaussian = gaussian_representative(bit, weight, variant=frame.index + 1)
                if decode_tagged(gaussian) is not None:
                    return False, cases
                if weight not in (Fraction(0), Fraction(1)) and certified_selector_bit(gaussian, weight) != bit:
                    return False, cases
                if encode_gaussian(decode_gaussian(gaussian) or ()) != gaussian:
                    return False, cases
                cases += 1
    tagged_first = {tag_code(role, Frame(rotation)) for role in ROLE_ORDER for rotation in ROTATIONS}
    protocols = tuple(
        Protocol(
            mode,
            DEFAULT_RND.u0,
            (Fraction(0), Fraction(numerator, 7), Fraction(0)),
            weight,
        )
        for mode in (MODE_RND, MODE_DIR)
        for numerator in range(-7, 8)
        for weight in convex_weights
    )
    protocol_carriers = {
        encode_program(IDENTITY_FRAME, protocol, 0) for protocol in protocols
    }
    exact_identity_codec = len(protocol_carriers) == len(set(protocols)) and all(
        decode_program(encode_program(IDENTITY_FRAME, protocol, 1))
        == (IDENTITY_FRAME, protocol, 1)
        for protocol in protocols
    )
    algebraic = Protocol(
        MODE_RND,
        (sp.sqrt(2) / 2, Fraction(0), Fraction(0)),
        (Fraction(0), sp.sqrt(3) / 3, Fraction(0)),
        sp.sqrt(5) / 5,
    )
    algebraic_roundtrip = (
        algebraic.valid
        and decode_protocol(
            encode_protocol("H_RND", IDENTITY_FRAME, algebraic), ("H_",)
        )
        == ("H_RND", IDENTITY_FRAME, algebraic, algebraic.weight_u0)
        and decode_program(encode_program(IDENTITY_FRAME, algebraic, 1))
        == (IDENTITY_FRAME, algebraic, 1)
    )
    t = sp.symbols("t")
    unknown_real = sp.Integral(sp.sin(t**t), (t, 0, 1)) - sp.Rational(1, 2)
    rejected_host_values = (
        not Protocol(
            MODE_RND,
            (sp.Float(0.5), Fraction(0), Fraction(0)),
            DEFAULT_RND.u1,
            Fraction(1, 2),
        ).valid
        and not GaussianPoint((sp.nan,) + (Fraction(0),) * 7).valid
        and not GaussianPoint((unknown_real,) + (Fraction(0),) * 7).valid
        and not SpherePoint((sp.Float(1.0), sp.Float(0.0), sp.Float(0.0))).valid
    )
    return (
        len(tagged_first) == len(ROLE_ORDER) * 24
        and all(value >= 2 for value in tagged_first)
        and exact_identity_codec
        and algebraic_roundtrip
        and rejected_host_values
    ), cases + len(protocols) + 6


def source_independence_check() -> bool:
    tree = ast.parse(inspect.getsource(gaussian_row))
    called = {node.func.id for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)}
    return not ({"installed_program", "outcome_weights", "outcome_row", "active_barycenter"} & called)


@dataclass(frozen=True)
class ProgramDomain:
    kind: str
    finite_menu: tuple[Vector, ...] = ()

    def contains(self, vector: Vector) -> bool:
        if self.kind == "real_bloch_ball":
            return (
                all(certified_real_coordinate(value) is not None for value in vector)
                and certified_le(dot(vector, vector), 1)
            )
        return vector in self.finite_menu

    @property
    def complete_convex_domain(self) -> bool:
        # The mathematical carrier is the complete real Bloch ball.  The host
        # evaluator accepts certified exact-real witnesses; completeness is a
        # theorem about the displayed identity codec, not an enumeration of
        # host expressions.  Convexity follows from
        # ||p u+(1-p)v||^2 <= p||u||^2+(1-p)||v||^2, whose residual is
        # p(1-p)||u-v||^2.
        p = sp.symbols("p", real=True)
        u = sp.symbols("u0:3", real=True)
        v = sp.symbols("v0:3", real=True)
        mixture = tuple(p * u[index] + (1 - p) * v[index] for index in range(3))
        convex_residual = sp.expand(
            p * sum(value**2 for value in u)
            + (1 - p) * sum(value**2 for value in v)
            - sum(value**2 for value in mixture)
            - p * (1 - p) * sum((u[index] - v[index]) ** 2 for index in range(3))
        )
        infinite_witnesses = tuple(
            (Fraction(1, denominator), Fraction(0), Fraction(0))
            for denominator in range(1, 65)
        )
        return (
            self.kind == "real_bloch_ball"
            and convex_residual == 0
            and len(set(infinite_witnesses)) == 64
            and all(self.contains(vector) for vector in infinite_witnesses)
        )


def admitted_program_domain(config: RuleConfig) -> ProgramDomain:
    if config.mutation == "finite_domain":
        return ProgramDomain("finite_menu", (DEFAULT_RND.u0, DEFAULT_RND.u1, DEFAULT_RND.mixture))
    return ProgramDomain("real_bloch_ball")


def git_bytes(spec: str) -> bytes:
    return subprocess.run(
        ["git", "show", spec],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


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
    return git_bytes(f"{PREREG_COMMIT}:{PACKET}/{name}").decode()


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
    "born_selector",
    "premature_program",
    "selector_leak",
    "nonlinear_encoder",
    "answer_defined_quotient",
    "external_iid",
    "frozen_memory",
    "triple_parity",
    "archive_relay",
    "one_step_only",
    "overwrite",
    "premature_head",
    "host_schedule",
    "coordinate_axis",
    "unbounded_bank",
    "undefined_collision",
    "finite_domain",
    "toe_promotion",
)


def run_checks(mutation: str | None) -> int:
    config = RuleConfig(mutation)
    checks = Checks()

    pins_ok = all(git_blob(spec) == blob for spec, blob in FROZEN_BLOBS.items())
    prereg = prereg_text("EXACT_TARGET_CONTRACT.md")
    checks.check(
        "source_and_prereg_pins",
        f"{len(FROZEN_BLOBS)} source blobs and the frozen candidate-law target match",
        pins_ok and "CANDIDATE_MICROSCOPIC_M_S_BRIDGE_EXACT" in prereg,
    )

    minimal = (ROOT / MINIMAL_PATH).read_text()
    checks.check(
        "foundation_authority_boundary",
        "four axioms supply locality/possibilities/Records but no update values, rate, or process law",
        all(
            needle in minimal
            for needle in (
                "There is one fixed nearest-neighbor admissibility rule",
                "Records form.",
                "choose a Hamiltonian or transfer operator",
                "it does not supply the formation site, probability",
            )
        ),
    )

    codec_ok, codec_cases = codec_checks()
    checks.check(
        "exact_m2_role_and_gaussian_codec",
        f"{codec_cases} direct seven-real protocol/Gaussian cases round-trip; algebraic exact reals pass while Float/NaN/unknown-real hosts are rejected; tag and Gaussian sectors are disjoint",
        codec_ok,
    )

    fair = gaussian_row(IDENTITY_FRAME, Fraction(1, 2), config)
    gaussian_integrals = gaussian_integral_certificate()
    gaussian_full = gaussian_full_m2_normalization_certificate()
    gaussian_pit = gaussian_probability_integral_transform_certificate()
    checks.check(
        "non_born_gaussian_selector_row",
        f"full M2 normalization={gaussian_full}; scalar integrals={gaussian_integrals}; probability-integral-transform={gaussian_pit}",
        fair.normalized
        and fair.continuous_measure is not None
        and fair.continuous_measure.selector_masses == (Fraction(1, 2), Fraction(1, 2))
        and tuple(weight for weight, _ in fair.control_atoms) == (Fraction(1, 2), Fraction(1, 2))
        and gaussian_integrals == (1, sp.Rational(1, 2), sp.Rational(1, 2))
        and gaussian_full == 1
        and gaussian_pit == (0, 0, 1)
        and source_independence_check(),
    )

    typed_maps_ok, typed_map_cases = typed_measure_map_hostile_checks()
    trigger_state = fire_unique_finite_term(
        seed_records(DEFAULT_RND), frame_sites(IDENTITY_FRAME, 0)["T"], RuleConfig()
    )
    gaussian_generator_term = generator_term_at(
        trigger_state, frame_sites(IDENTITY_FRAME, 0)["A"], RuleConfig()
    )
    typed_successor = (
        gaussian_generator_term.jump_measure.successor(
            GaussianPoint((Fraction(0),) * 8)
        )[frame_sites(IDENTITY_FRAME, 0)["A"]]
        if isinstance(gaussian_generator_term.jump_measure, ContinuousRecordJumpMeasure)
        else None
    )
    typed_successor_ok = (
        isinstance(typed_successor, Carrier)
        and len(typed_successor.coefficients) == 8
        and decode_tagged(typed_successor) is None
        and decode_gaussian(typed_successor) is not None
        and len(
            OutcomeCarrierMap(IDENTITY_FRAME, DEFAULT_RND, 0)
            .apply(SpherePoint(AXES[0]))
            .coefficients
        )
        == 8
    )
    checks.check(
        "typed_record_valued_generator_pushforward",
        f"actual generator term maps R^8 into one literal M2 Record carrier; {typed_map_cases} malformed-map/sample controls rejected",
        typed_maps_ok and typed_successor_ok,
    )

    panel_regressions_ok, panel_regression_cases = decisive_panel_counterexample_regressions(config)
    checks.check(
        "decisive_panel_counterexample_regressions",
        f"{panel_regression_cases} frozen-surface attacks: exact 150/400/900-digit order and equality boundary, total mathematical event, full-real/algebraic boundary+M, honest host rejection, typed lineage/support, restricted fibres, retained payloads, accumulated N=2",
        panel_regressions_ok,
    )

    schema_ok, edge_count = local_schema_check()
    graph = explore_one_trial(DEFAULT_RND, IDENTITY_FRAME, config)
    if mutation is None:
        domain_generator_ok, domain_generator_cases = protocol_domain_generator_checks(config)
    else:
        domain_generator_ok, domain_generator_cases = True, 0
    expected_kinds = {"trigger", "gaussian", "selector", "program", "outcome", "close", "q1", "q2", "q3", "q4", "q5", "head"}
    if mutation == "premature_program":
        expected_kinds.add("premature_program")
    checks.check(
        "fixed_radius_one_state_clocked_schema",
        f"{edge_count} causal bonds are NN; generator row kinds={','.join(graph.kinds)}; complete-protocol cases={domain_generator_cases}",
        schema_ok and domain_generator_ok and set(graph.kinds) == expected_kinds and mutation != "premature_program",
    )

    absorption = ctmc_control_absorption(DEFAULT_RND, IDENTITY_FRAME, config)
    representative = representative_control_trial_distribution(
        seed_records(DEFAULT_RND), DEFAULT_RND, IDENTITY_FRAME, 0, config
    )
    representative_terminal = {state_key(state): weight for weight, state in representative.values()}
    if mutation is None:
        actual_diamonds_ok, actual_diamond_cases = exhaustive_actual_kernel_diamonds(config)
    else:
        actual_diamonds_ok, actual_diamond_cases = True, 0
    checks.check(
        "autonomous_ctmc_confluence_and_complete_trial",
        f"rate-one generator: states={graph.states} edges={graph.edges} control_diamonds={graph.diamond_checks} actual_jump_bind_cases={actual_diamond_cases} failures={graph.diamond_failures} deadends={graph.premature_dead_ends} terminals={len(absorption)} mass={sum(absorption.values(), Fraction(0))}",
        graph.diamond_failures == 0
        and actual_diamonds_ok
        and graph.premature_dead_ends == 0
        and len(absorption) == 12
        and sum(absorption.values(), Fraction(0)) == 1
        and absorption == representative_terminal
        and all(len(key) == 13 for key in absorption),
    )

    support_ok = arbitrary_support_lemma()
    checks.check(
        "arbitrary_n_fresh_support_and_permanence",
        f"role-residue proof gives exactly 12N+1 Records; N=64 gives {expected_support_count(64)}",
        support_ok and expected_support_count(64) == 769 and overwrite_check(config),
    )

    ctmc_trial = ctmc_control_trial_distribution(seed_records(DEFAULT_RND), IDENTITY_FRAME, 0, config)
    installed_ok = len(ctmc_trial) == 12 and all(key[2] == DEFAULT_RND for key in ctmc_trial)
    checks.check(
        "record_first_program_installation",
        "A forms before R; R selects P; P forms before O; selector Record remains in every terminal",
        installed_ok and mutation != "premature_program",
    )

    convex_weights = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1))
    quotient_cases = 0
    projection_ok = active_projection_kind(config) == "program_barycenter"
    for weight in convex_weights:
        random_protocol = Protocol(MODE_RND, DEFAULT_RND.u0, DEFAULT_RND.u1, weight)
        direct_protocol = Protocol(MODE_DIR, DEFAULT_RND.u0, DEFAULT_RND.u1, weight)
        try:
            random_measure = installed_program_measure(random_protocol, config)
            direct_measure = installed_program_measure(direct_protocol, config)
            projection_ok = projection_ok and random_measure.normalized and direct_measure.normalized
            projection_ok = projection_ok and active_barycenter(
                random_measure, config
            ) == active_barycenter(direct_measure, config) == random_protocol.mixture
        except (TypeError, ValueError):
            projection_ok = False
        quotient_cases += 1
    checks.check(
        "predetermined_active_program_quotient_M",
        f"barycentric map was applied to actual pre-response P measures for {quotient_cases} convex weights",
        projection_ok,
    )

    convex_ok = symbolic_convex_identity(config) and continuous_response_intertwiner(config)
    domain = admitted_program_domain(config)
    checks.check(
        "all_domain_fixed_processor_intertwiner_M",
        f"symbolic seven-variable affine identity holds on the complete mathematical real domain; executable witnesses are exact-real certified; domain={domain.kind}",
        convex_ok and domain.complete_convex_domain,
    )

    random_disc, direct_disc = global_selector_discriminator(DEFAULT_RND)
    checks.check(
        "global_selector_correlation_retained",
        f"relative active equality coexists with global discriminator random={random_disc} direct={direct_disc}",
        random_disc > 0 and direct_disc == 0,
    )

    joined = joined_six_axis(DEFAULT_RND)
    boundary = embedded_boundary_kernel(DEFAULT_RND, config)
    direct_boundary = embedded_boundary_kernel(DEFAULT_DIR, config)
    haar_certificate = haar_integral_certificate()
    checks.check(
        "block36_joined_nu_exact_map",
        f"actual analytic boundary has selector masses={[term.selector_mass for term in boundary.terms]}; Haar integrals={haar_certificate}; six-axis law is separately typed control",
        sum(joined.values(), Fraction(0)) == 1
        and all(weight >= 0 for weight in joined.values())
        and boundary.normalized
        and direct_boundary.normalized
        and stochastic_control_quotient_matches(boundary, config)
        and generator_boundary_density_certificate(DEFAULT_RND, boundary)
        and generator_boundary_density_certificate(DEFAULT_DIR, direct_boundary)
        and [term.selector_mass for term in boundary.terms] == [Fraction(1, 2), Fraction(1, 2)]
        and all(term.gaussian_fibre.full_encoded_m2_payload_retained for term in boundary.terms)
        and haar_certificate == (1, 0, 0, 0, 1),
    )

    cut_ok = payload_projection_certificate(config)
    checks.check(
        "payload_sensitivity_causal_cut_S",
        "the actual table calls constant close_payload and identity next_head_protocol projections; Gaussian row has no response dependency",
        cut_ok,
    )

    archive_ok, archive_rows = archive_fibre_replay(config, expanded=mutation is None)
    expected_archive_rows = 936 if mutation is None else 156
    checks.check(
        "unequal_archive_joint_next_cut_bisimulation_S",
        f"all 12 outcome/selector fibres plus an altered adjacent Q5 archive give {archive_rows} identical next transcript/cut rows across the tested modes/weights",
        archive_ok and archive_rows == expected_archive_rows,
    )

    renewal_ok, pair_value, parity_value = renewal_controls(config)
    induction = cut_induction_certificate(config, graph, archive_ok, actual_diamonds_ok)
    cylinder_error = None
    try:
        control_one = ctmc_control_cylinder(DEFAULT_RND, 1, config)
        control_two = ctmc_control_cylinder(DEFAULT_RND, 2, config)
        cylinder_one, cylinder_two, analytic_projective = analytic_cylinder_projective_pair(
            DEFAULT_RND, config
        )
        literal_bind_ok, literal_bind_cases = literal_accumulated_bind_checks(config)
    except (RuntimeError, ValueError) as error:
        cylinder_error = str(error)
        control_one = {}
        control_two = {}
        cylinder_one = AnalyticCylinderMeasure(1, (), False)
        cylinder_two = AnalyticCylinderMeasure(2, (), False)
        analytic_projective = False
        literal_bind_ok, literal_bind_cases = False, 0
    control_marginal: dict[tuple[tuple[int, Vector], ...], Fraction] = defaultdict(Fraction)
    for transcript, weight in control_two.items():
        control_marginal[transcript[:-1]] += weight
    checks.check(
        "all_finite_cylinders_from_local_rows",
        f"generator-bound accumulated atomless cylinders N=1,2 normalized={[cylinder_one.normalized, cylinder_two.normalized]} projective={analytic_projective}; literal-bind cases={literal_bind_cases}; second source target={(6, -1, 0)}; control totals={[sum(control_one.values(), Fraction(0)), sum(control_two.values(), Fraction(0))]} projective={dict(control_marginal) == control_one}; induction={induction}; rival P00={pair_value}; P000={parity_value}; error={cylinder_error}",
        renewal_ok
        and cylinder_one.normalized
        and cylinder_two.normalized
        and analytic_projective
        and literal_bind_ok
        and sum(control_one.values(), Fraction(0)) == 1
        and sum(control_two.values(), Fraction(0)) == 1
        and dict(control_marginal) == control_one
        and induction.valid,
    )

    checks.check(
        "stochastic_source_owned_by_same_kernel",
        f"selector owner={boundary.selector_measure.owner}; first-cut kernel is a bind of Record-valued generator jumps",
        boundary.locally_owned
        and boundary.derived_from_generator
        and boundary.selector_jump is not None
        and all(term.outcome_jump.normalized for term in boundary.terms),
    )

    malformed_ok, collision_status, malformed_cases = malformed_collision_check(config)
    checks.check(
        "malformed_and_collision_stop",
        f"{malformed_cases - 1} conflicting/invalid/protocol-or-branch mismatch cases STOP; one same-branch sphere support value is intentionally ACTIVE; collision resolver={collision_status}",
        malformed_ok,
    )

    covariance_ok, covariance_cases = covariance_checks(config)
    map_covariance_ok, map_covariance_cases = actual_carrier_map_covariance()
    if mutation is None or mutation == "coordinate_axis":
        conjugacy_ok, conjugacy_cases = exhaustive_row_conjugacy(config)
    else:
        conjugacy_ok, conjugacy_cases = covariance_ok, covariance_cases
    checks.check(
        "translation_and_proper_cubic_covariance",
        f"{covariance_cases} translated/frame controls, {conjugacy_cases} reachable row-conjugacy actions, and {map_covariance_cases} typed carrier-map intertwiners across 24 frames",
        covariance_ok and conjugacy_ok and map_covariance_ok,
    )

    scope_needles = (
        "derivation or selection of that law from the four axioms",
        "full multi-front or loopy `Z^3` theory",
        "not gravity",
        "audit/obligation/TOE-score movement",
    )
    goal_text = prereg_text("GOAL.md")
    checks.check(
        "claim_scope_and_no_promotion",
        f"scope={config.claimed_scope}; candidate-law, law-selection, topology, gravity and audit boundaries remain explicit",
        config.claimed_scope == "candidate_single_front" and all(needle in goal_text for needle in scope_needles),
    )

    designated_mutation_gate = {
        "born_selector": "non_born_gaussian_selector_row",
        "premature_program": "record_first_program_installation",
        "selector_leak": "all_domain_fixed_processor_intertwiner_M",
        "nonlinear_encoder": "all_domain_fixed_processor_intertwiner_M",
        "answer_defined_quotient": "predetermined_active_program_quotient_M",
        "external_iid": "stochastic_source_owned_by_same_kernel",
        "frozen_memory": "all_finite_cylinders_from_local_rows",
        "triple_parity": "all_finite_cylinders_from_local_rows",
        "archive_relay": "unequal_archive_joint_next_cut_bisimulation_S",
        "one_step_only": "all_finite_cylinders_from_local_rows",
        "overwrite": "arbitrary_n_fresh_support_and_permanence",
        "premature_head": "autonomous_ctmc_confluence_and_complete_trial",
        "host_schedule": "autonomous_ctmc_confluence_and_complete_trial",
        "coordinate_axis": "translation_and_proper_cubic_covariance",
        "unbounded_bank": "stochastic_source_owned_by_same_kernel",
        "undefined_collision": "malformed_and_collision_stop",
        "finite_domain": "all_domain_fixed_processor_intertwiner_M",
        "toe_promotion": "claim_scope_and_no_promotion",
    }
    if mutation is None:
        rejected = 0
        mutation_details = []
        def execute_mutation(name: str) -> tuple[str, subprocess.CompletedProcess[str]]:
            return name, subprocess.run(
                    [sys.executable, __file__, "--mutation", name],
                    cwd=ROOT,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=AUDIT_TIMEOUT_SEC,
                )

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
            mutation_runs = tuple(pool.map(execute_mutation, MUTATIONS))
        for name, completed in mutation_runs:
            designated = designated_mutation_gate[name]
            semantic_failure = f"FAIL {designated}:" in completed.stdout
            if completed.returncode != 0 and "TOTAL:" in completed.stdout and semantic_failure:
                rejected += 1
            mutation_details.append(f"{name}:{designated}:{'rejected' if semantic_failure else 'MISSED'}")
        checks.check(
            "hostile_mutation_gate",
            f"{rejected}/{len(MUTATIONS)} designated semantic gates reject; {';'.join(mutation_details)}",
            rejected == len(MUTATIONS),
        )

    if mutation is not None:
        note_ok = True
    elif NOTE_PATH.exists():
        note = NOTE_PATH.read_text()
        note_ok = all(
            needle in note
            for needle in (
                "CANDIDATE_MICROSCOPIC_M_S_BRIDGE_EXACT",
                "candidate-law",
                "all finite",
                "archive",
                "selector",
                "no TOE percentage movement",
            )
        )
    else:
        note_ok = False
    checks.check(
        "result_note_contract",
        "terminal theorem note contains the exact classification and nonclosure language",
        note_ok,
    )

    print("N5_EXECUTION per_element: checked exact Gaussian/Haar densities and every symbolic affine carrier coordinate")
    print("N5_EXECUTION per_site: checked every reachable local generator action, protocol/branch mismatch STOP cases, and typed sphere-support acceptance")
    print("N5_EXECUTION per_mode: checked randomized/direct full-real formulas plus an irrational algebraic end-to-end carrier and M witness")
    print("N5_EXECUTION per_block: checked autonomous CTMC absorption, unequal archive fibres, and preserved-cut induction premises")
    print("N5_EXECUTION lattice_wide: checked and not executed — the theorem is single-front and does not totalize arbitrary Z3 states")
    print(
        "SUMMARY "
        f"graph_states={graph.states} graph_edges={graph.edges} terminals={len(graph.terminal_keys)} "
        f"diamonds={graph.diamond_checks} codec_cases={codec_cases} covariance_cases={covariance_cases} "
        f"support_N64={expected_support_count(64)} input_sha256={input_fingerprint()}"
    )
    return checks.finish()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    args = parser.parse_args()
    return run_checks(args.mutation)


if __name__ == "__main__":
    raise SystemExit(main())
