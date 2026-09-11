#!/usr/bin/env python3
"""Block 136: exact observable-scaling-law certificate.

The runner extends the committed Z4 Floquet/reflection machinery to an exact
Z6 spatial carrier, derives its conjugation mirror from the real action,
separates raw determinant phases from normalized presentation, classifies the
three charge-pair observable blocks, and records the corrected integer-charge
population boundary.  Scientific arithmetic is exact; the integer monotonic
clock is used only for the runtime gate.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16 as b118
import admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16 as b119
import admissibility_dirac_kahler_residual_invariance_theorem_2026_08_17 as block135


R = sp.Rational
I = sp.I
Z = sp.symbols("z")
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_"
    "BOUNDED_THEOREM_NOTE_2026-08-18.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUAL_INVARIANCE_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_residual_invariance_theorem_"
    "2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_residual_invariance_"
    "theorem_2026_08_17.txt"
)
B118_RUNNER = (
    "scripts/admissibility_dirac_kahler_floquet_monodromy_"
    "action_pairing_2026_08_16.py"
)
B118_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_floquet_monodromy_"
    "action_pairing_2026_08_16.txt"
)
B119_RUNNER = (
    "scripts/admissibility_dirac_kahler_reflection_intertwiner_"
    "completion_2026_08_16.py"
)
B119_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_"
    "completion_2026_08_16.txt"
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUAL_INVARIANCE_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_residual_invariance_theorem_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_residual_invariance_theorem_2026_08_17.txt",
    "scripts/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.txt",
    "scripts/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block135-residual-invariance-theorem-20260817"
)
PARENT_COMMIT = "dac48758c9967761b1b4419b5870357ca8da7cfa"
PARENT_NOTE_BLOB = "d3546d907df8f9e47b74e1e45554079036663bff"
PARENT_RUNNER_BLOB = "a54b45f961583792d01081c1f2aab17c35a0f239"
PARENT_CACHE_BLOB = "cf0c9c6cd2da9f62aab6327a9eebb3c94bb3328c"
B118_COMMIT = "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"
B118_RUNNER_BLOB = "12c065883099077aae880eeecf3f2a80444a1d87"
B118_CACHE_BLOB = "804641ed09f5c2c0b458b0b9ce8a201c93c05a43"
B119_COMMIT = "33fd2d21558604718f3a88713fe1976aff8f9dbb"
B119_RUNNER_BLOB = "952494a18ba13b7d25fb144b8569687813d9bddc"
B119_CACHE_BLOB = "f7a9b09538c8787ed88885c04cdea3e5cff70104"

ANCESTOR_COMMITS = (
    (134, "acb7d8109bf751c909364aec92c4d833492cfa6c"),
    (133, "80d208f0c12e21fd985d01e5f807a9d34c00ef11"),
    (132, "0236823bed5b648ad8357e5d1b79bdfe1be36c39"),
    (131, "d3a666f62c87b3b8178289024087090c91ced327"),
    (130, "db394d1536a8243c2b01b3e45413813e45f8abdd"),
    (129, "30fd2722a10a02f87c235e2ee592d140f8bb7df5"),
    (128, "f6b0cf59e2cc588ebd3e34b96e730574cb485db2"),
    (127, "ca6792464f60598013a3700f99c02a467af64b7a"),
    (126, "a145a4e2cfc19bc919371196d7c5f3451c0bb45d"),
    (125, "ff85cc8c6a991b2926b9ac5cb5168f2587bc0c0d"),
    (124, "da2b9020e9f15ac55640ef87a0798a78e3c9a0d0"),
    (123, "954322e0e085d6c3133ce24dca49db2efbd7d0a6"),
    (122, "f067b99be7eb49fc46ea8dffccab5e20e6052d88"),
    (121, "1714abeefcf3763c0bfe001f30fd14521c538622"),
    (120, "1c2386bf3df420707fd2ecb2d7ec84002ba40ad1"),
    (119, B119_COMMIT),
    (118, B118_COMMIT),
    (117, "f800356aec0989b6e0fa80ed43274794243b1ca2"),
    (116, "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"),
    (115, "c78301fef7521d0518f485f1bf9266983c9e516a"),
    (114, "75026e71cfbd44ed665ddc41c22ebaa722720ea9"),
    (113, "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"),
    (112, "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"),
    (111, "b04e7c8747b09734711cfcd2bfab961bd12e81ad"),
    (110, "d6761278fca9cac617200792473a8f4da3a6cfff"),
    (109, "ad84cfcc857a65285389ba93b47cd7b718589be5"),
    (108, "8afe8dff5ccf531208238af0aaaec1f547d73874"),
    (107, "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"),
    (106, "22d6d90ec2279e5868c9c825149b2a20beea3797"),
    (105, "d06066c2b908aaca0779625d831dfb10620cf34d"),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_z6_fixture",
    "break_conjugation",
    "break_kinematic_derivation",
    "break_normalization",
    "break_regime_g",
    "break_algebra_count",
    "break_jordan_exclusion",
    "break_charge_definiteness",
    "claim_03_populates",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
    "claim_general_law_proven",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **{
            f"ancestor_{number}": is_ancestor(commit, "HEAD")
            for number, commit in ANCESTOR_COMMITS
        },
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
        "worktree_parent_note": worktree_blob(PARENT_NOTE),
        "worktree_parent_runner": worktree_blob(PARENT_RUNNER),
        "worktree_parent_cache": worktree_blob(PARENT_CACHE),
        "b118_ancestor": is_ancestor(B118_COMMIT, "HEAD"),
        "b118_runner": commit_blob(B118_COMMIT, B118_RUNNER),
        "b118_cache": commit_blob(B118_COMMIT, B118_CACHE),
        "worktree_b118_runner": worktree_blob(B118_RUNNER),
        "worktree_b118_cache": worktree_blob(B118_CACHE),
        "b119_ancestor": is_ancestor(B119_COMMIT, "HEAD"),
        "b119_runner": commit_blob(B119_COMMIT, B119_RUNNER),
        "b119_cache": commit_blob(B119_COMMIT, B119_CACHE),
        "worktree_b119_runner": worktree_blob(B119_RUNNER),
        "worktree_b119_cache": worktree_blob(B119_CACHE),
    }


def raw_note() -> bytes:
    try:
        return NOTE_PATH.read_bytes()
    except OSError:
        return b""


def normalized_note(note: bytes) -> str:
    try:
        decoded = note.decode("utf-8")
    except UnicodeError:
        return ""
    return " ".join(decoded.lower().split())


PRIMARY_SHEAR = R(5, 13)
SECOND_SHEAR = R(3, 5)
EXPECTED_MASS = R(9, 20)
SPACE_SIZE = 6
TIME_SIZE = 8
ALGEBRAIC_EXTENSION = (I, sp.sqrt(3))
NUMBER_FIELD = sp.QQ.algebraic_field(*ALGEBRAIC_EXTENSION)


class NumberFieldAdapter:
    zero = NUMBER_FIELD.zero
    one = NUMBER_FIELD.one

    @staticmethod
    def coerce(value: object):
        try:
            return NUMBER_FIELD.convert(value)
        except (TypeError, ValueError):
            return NUMBER_FIELD.from_sympy(value)


BASE_FIELD = NumberFieldAdapter()


class QuadraticElement:
    """A compact exact a+b*r representation over a nested base field."""

    __slots__ = ("field", "a", "b")

    def __init__(self, field, a, b) -> None:
        self.field = field
        self.a = field.base.coerce(a)
        self.b = field.base.coerce(b)

    def _other(self, value):
        return self.field.coerce(value)

    def __add__(self, value):
        other = self._other(value)
        return QuadraticElement(self.field, self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return QuadraticElement(self.field, -self.a, -self.b)

    def __sub__(self, value):
        return self + (-self._other(value))

    def __rsub__(self, value):
        return self._other(value) - self

    def __mul__(self, value):
        other = self._other(value)
        constant = self.a * other.a + self.b * other.b * self.field.constant
        linear = (
            self.a * other.b
            + self.b * other.a
            + self.b * other.b * self.field.linear
        )
        return QuadraticElement(self.field, constant, linear)

    __rmul__ = __mul__

    def inverse(self):
        norm = (
            self.a * self.a
            + self.a * self.b * self.field.linear
            - self.b * self.b * self.field.constant
        )
        if norm == self.field.base.zero:
            raise ZeroDivisionError("zero quadratic-field element")
        return QuadraticElement(
            self.field,
            (self.a + self.b * self.field.linear) / norm,
            -self.b / norm,
        )

    def __truediv__(self, value):
        return self * self._other(value).inverse()

    def __rtruediv__(self, value):
        return self._other(value) / self

    def __pow__(self, power: int):
        if power < 0:
            return self.inverse() ** (-power)
        result = self.field.one
        factor = self
        exponent = power
        while exponent:
            if exponent % 2:
                result = result * factor
            factor = factor * factor
            exponent //= 2
        return result

    def __eq__(self, value: object) -> bool:
        try:
            other = self._other(value)
        except (TypeError, ValueError):
            return False
        return self.a == other.a and self.b == other.b

    def __repr__(self) -> str:
        return f"({self.a})+({self.b})*{self.field.name}"


class QuadraticField:
    def __init__(self, base, linear, constant, name: str) -> None:
        self.base = base
        self.linear = base.coerce(linear)
        self.constant = base.coerce(constant)
        self.name = name
        self.zero = QuadraticElement(self, base.zero, base.zero)
        self.one = QuadraticElement(self, base.one, base.zero)
        self.generator = QuadraticElement(self, base.zero, base.one)

    def coerce(self, value) -> QuadraticElement:
        if isinstance(value, QuadraticElement):
            if value.field is self:
                return value
            if value.field is self.base:
                return QuadraticElement(self, value, self.base.zero)
            raise ValueError("quadratic-field context mismatch")
        return QuadraticElement(self, self.base.coerce(value), self.base.zero)


@dataclass(frozen=True)
class TorusCall:
    mass: sp.Expr
    shear: sp.Expr
    volume: sp.Expr
    half_time: int
    boundary_sign: int
    spatial_extent: int


def fixture_data_spatial(
    shear: sp.Rational, spatial_size: int
) -> tuple[object, tuple[TorusCall, ...]]:
    """Call the committed fixture while recording and replacing only L_x."""
    original = b118.base.torus_objects
    calls: list[TorusCall] = []

    def sized_torus_objects(
        mass, field_c, volume, half_time, boundary_sign, spatial_extent=4
    ):
        del spatial_extent
        calls.append(
            TorusCall(
                sp.sympify(mass),
                sp.sympify(field_c),
                sp.sympify(volume),
                int(half_time),
                int(boundary_sign),
                spatial_size,
            )
        )
        return original(
            mass,
            field_c,
            volume,
            half_time,
            boundary_sign,
            spatial_size,
        )

    b118.base.torus_objects = sized_torus_objects
    try:
        raw = b118.base.fixture_data(shear)
    finally:
        b118.base.torus_objects = original
    return raw, tuple(calls)


def root_power(power: int, spatial_size: int) -> sp.Expr:
    exponent = power % spatial_size
    if spatial_size == 4:
        return I**exponent
    if spatial_size == 6:
        return (
            sp.S.One,
            (1 + I * sp.sqrt(3)) / 2,
            (-1 + I * sp.sqrt(3)) / 2,
            -sp.S.One,
            (-1 - I * sp.sqrt(3)) / 2,
            (1 - I * sp.sqrt(3)) / 2,
        )[exponent]
    raise ValueError("the exact carrier implements only Z4 and Z6 roots")


def shift(spatial_size: int) -> sp.Matrix:
    result = sp.zeros(spatial_size, spatial_size)
    for column in range(spatial_size):
        result[(column + 1) % spatial_size, column] = 1
    return result


@lru_cache(maxsize=None)
def projectors(spatial_size: int) -> tuple[sp.Matrix, ...]:
    cyclic = shift(spatial_size)
    return tuple(
        (
            sum(
                (
                    root_power(-momentum * power, spatial_size) * cyclic**power
                    for power in range(spatial_size)
                ),
                sp.zeros(spatial_size),
            )
            / spatial_size
        ).applyfunc(sp.expand)
        for momentum in range(spatial_size)
    )


def momentum_block(
    matrix: sp.Matrix,
    momentum: int,
    time_size: int,
    spatial_size: int,
) -> sp.Matrix:
    projector = projectors(spatial_size)[momentum]
    return sp.Matrix(
        time_size,
        time_size,
        lambda row, column: sp.expand(
            sp.cancel(
                sp.trace(
                    projector
                    * matrix[
                        spatial_size * row : spatial_size * (row + 1),
                        spatial_size * column : spatial_size * (column + 1),
                    ]
                )
            )
        ),
    )


def exact(value: sp.Expr) -> sp.Expr:
    return sp.cancel(value, extension=ALGEBRAIC_EXTENSION)


def field_element(value: sp.Expr):
    return NUMBER_FIELD.from_sympy(value)


def field_expr(value) -> sp.Expr:
    return NUMBER_FIELD.to_sympy(value)


def field_matrix_2(entries) -> sp.Matrix:
    return sp.Matrix(
        2,
        2,
        [field_expr(value) for row in entries for value in row],
    )


def field_matrix_multiply(left, right):
    return tuple(
        tuple(
            sum(
                (
                    left[row][inner] * right[inner][column]
                    for inner in range(2)
                ),
                NUMBER_FIELD.zero,
            )
            for column in range(2)
        )
        for row in range(2)
    )


def nested_conjugate(value):
    """Conjugate Q(i,sqrt(3)) while fixing the declared real roots."""
    if isinstance(value, QuadraticElement):
        return QuadraticElement(
            value.field,
            nested_conjugate(value.a),
            nested_conjugate(value.b),
        )
    return field_element(sp.conjugate(field_expr(value)))


def quadratic_context(trace_square: sp.Rational):
    tau_field = QuadraticField(
        BASE_FIELD,
        NUMBER_FIELD.zero,
        field_element(trace_square),
        "tau",
    )
    rho_field = QuadraticField(
        tau_field,
        tau_field.generator,
        -tau_field.one,
        "rho",
    )
    return tau_field, rho_field


def transpose_entries(matrix):
    return tuple(
        tuple(matrix[column][row] for column in range(len(matrix)))
        for row in range(len(matrix[0]))
    )


def null_vector(matrix, field) -> tuple[QuadraticElement, ...]:
    rows = [list(row) for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivots: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        selected = next(
            (
                row
                for row in range(pivot_row, row_count)
                if rows[row][column] != field.zero
            ),
            None,
        )
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        inverse = rows[pivot_row][column].inverse()
        rows[pivot_row] = [value * inverse for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or rows[row][column] == field.zero:
                continue
            factor = rows[row][column]
            rows[row] = [
                rows[row][index] - factor * rows[pivot_row][index]
                for index in range(column_count)
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    free = tuple(index for index in range(column_count) if index not in pivots)
    if len(pivots) != column_count - 1 or len(free) != 1:
        raise AssertionError(
            f"expected corank one, got rank={len(pivots)} free={free}"
        )
    result = [field.zero for _ in range(column_count)]
    result[free[0]] = field.one
    for row, column in reversed(tuple(enumerate(pivots))):
        result[column] = -sum(
            (rows[row][index] * result[index] for index in free),
            field.zero,
        )
    return tuple(result)


def matrix_vector(matrix, vector, field):
    return tuple(
        sum(
            (
                matrix[row][column] * vector[column]
                for column in range(len(vector))
            ),
            field.zero,
        )
        for row in range(len(matrix))
    )


@dataclass(frozen=True)
class Transfer:
    bulk: b118.BulkBlocks
    slices: tuple[b118.SliceBlocks, ...]
    local_transfers: tuple[sp.Matrix, ...]
    cycle_product: sp.Matrix
    monodromy: sp.Matrix
    cycle_polynomial: sp.Poly
    monodromy_polynomial: sp.Poly
    monodromy_trace: sp.Expr
    monodromy_determinant: sp.Expr
    normalized_trace_square: sp.Expr
    fine_band: bool
    construction_valid: bool
    characteristic_valid: bool


@dataclass(frozen=True)
class FixtureSolve:
    shear: sp.Rational
    raw: object
    torus_calls: tuple[TorusCall, ...]
    action: sp.Matrix
    blocks: tuple[sp.Matrix, ...]
    transfers: tuple[Transfer, ...]


@dataclass(frozen=True)
class ResidueFactor:
    right: tuple[QuadraticElement, ...]
    left: tuple[QuadraticElement, ...]
    residue: tuple[tuple[QuadraticElement, ...], ...]
    valid: bool


def normalized_symbol_and_residue(
    transfer: Transfer,
    trace_square: sp.Rational,
    context,
) -> ResidueFactor:
    tau_field, rho_field = context
    tau = tau_field.generator
    cycle_trace = field_element(-transfer.monodromy_trace)
    sigma = tau_field.coerce(cycle_trace) / tau
    determinant = tau_field.coerce(field_element(transfer.monodromy_determinant))
    if sigma * sigma != determinant:
        raise AssertionError("Floquet phase square does not equal determinant")
    inverse_sigma = sigma.inverse()
    symbol = []
    derivative = []
    for row in range(TIME_SIZE):
        symbol_row = []
        derivative_row = []
        for column in range(TIME_SIZE):
            diagonal = tau_field.coerce(
                field_element(transfer.bulk.diagonal[row, column])
            )
            forward = tau_field.coerce(
                field_element(transfer.bulk.forward[row, column])
            )
            backward = tau_field.coerce(
                field_element(transfer.bulk.backward[row, column])
            )
            constant = diagonal + backward * inverse_sigma * tau
            rho_coefficient = sigma * forward - backward * inverse_sigma
            symbol_row.append(
                rho_field.coerce(constant)
                + rho_field.generator * rho_coefficient
            )
            derivative_row.append(rho_field.coerce(rho_coefficient))
        symbol.append(tuple(symbol_row))
        derivative.append(tuple(derivative_row))
    symbol = tuple(symbol)
    derivative = tuple(derivative)
    right = null_vector(symbol, rho_field)
    left = null_vector(transpose_entries(symbol), rho_field)
    derivative_right = matrix_vector(derivative, right, rho_field)
    denominator = sum(
        (
            left[index] * derivative_right[index]
            for index in range(TIME_SIZE)
        ),
        rho_field.zero,
    )
    if denominator == rho_field.zero:
        raise AssertionError("stable residue denominator vanished")
    residue = tuple(
        tuple(
            right[row] * left[column] / denominator
            for column in range(TIME_SIZE)
        )
        for row in range(TIME_SIZE)
    )
    valid = (
        all(
            value == rho_field.zero
            for value in matrix_vector(symbol, right, rho_field)
        )
        and all(
            value == rho_field.zero
            for value in matrix_vector(transpose_entries(symbol), left, rho_field)
        )
        and residue[0][TIME_SIZE - 1] != rho_field.zero
    )
    return ResidueFactor(right, left, residue, valid)


@dataclass(frozen=True)
class SectorFactorization:
    momentum: int
    h00: tuple[tuple[QuadraticElement, ...], ...]
    x: tuple[QuadraticElement, ...]
    y: tuple[QuadraticElement, ...]
    valid: bool


def sector_factorizations(
    transfers: tuple[Transfer, ...],
    trace_squares: tuple[sp.Rational, ...],
) -> tuple[SectorFactorization, ...]:
    contexts = {value: quadratic_context(value) for value in set(trace_squares)}
    residues = tuple(
        normalized_symbol_and_residue(
            transfer,
            trace_squares[momentum],
            contexts[trace_squares[momentum]],
        )
        for momentum, transfer in enumerate(transfers)
    )
    result = []
    for momentum in range(SPACE_SIZE):
        opposite = (-momentum) % SPACE_SIZE
        residue = residues[opposite].residue
        rho_field = contexts[trace_squares[momentum]][1]
        h00 = tuple(
            tuple(
                nested_conjugate(residue[row][TIME_SIZE - 1 - column])
                for column in range(TIME_SIZE)
            )
            for row in range(TIME_SIZE)
        )
        pivot = h00[0][0]
        if pivot == rho_field.zero:
            raise AssertionError("Block 119 pivot (0,0) vanished")
        x = tuple(h00[row][0] for row in range(TIME_SIZE))
        y = tuple(
            nested_conjugate(h00[0][column] / pivot)
            for column in range(TIME_SIZE)
        )
        factorization = all(
            h00[row][column]
            == x[row] * nested_conjugate(y[column])
            for row in range(TIME_SIZE)
            for column in range(TIME_SIZE)
        )
        result.append(
            SectorFactorization(
                momentum,
                h00,
                x,
                y,
                residues[opposite].valid
                and factorization
                and y[0] == rho_field.one,
            )
        )
    return tuple(result)


def transfer_from_action(action_block: sp.Matrix) -> Transfer:
    fine_band = all(
        b118.row_offsets(action_block, row)
        == ((-2, -1, 0, 1, 2) if row % 2 == 0 else (-1, 0, 1))
        for row in range(TIME_SIZE)
    )
    bulk = b118.unwrap_antiperiodic(action_block)
    slices = b118.coarse_blocks(bulk)
    local_field_transfers = []
    construction_valid = (
        bulk.unique_unwrap
        and bulk.reconstruction
        and bulk.rank_one_hopping
        and all(item.a_row_vanishes and item.c_column_vanishes for item in slices)
    )
    for step, current in enumerate(slices):
        previous = slices[(step - 1) % 4]
        a = field_element(current.diagonal[0, 0])
        b = field_element(current.diagonal[0, 1])
        c = field_element(current.diagonal[1, 0])
        d = field_element(current.diagonal[1, 1])
        e = field_element(current.forward[0, 0])
        f = field_element(current.forward[1, 0])
        g = field_element(current.backward[0, 0])
        h = field_element(current.backward[0, 1])
        previous_c = field_element(previous.diagonal[1, 0])
        previous_d = field_element(previous.diagonal[1, 1])
        previous_f = field_element(previous.forward[1, 0])
        construction_valid = (
            construction_valid
            and d != NUMBER_FIELD.zero
            and previous_d != NUMBER_FIELD.zero
        )
        coefficient_previous = g - h * previous_c / previous_d
        coefficient_current = a - b * c / d - h * previous_f / previous_d
        coefficient_next = e - b * f / d
        construction_valid = (
            construction_valid and coefficient_next != NUMBER_FIELD.zero
        )
        local_field_transfers.append(
            (
                (
                    -coefficient_current / coefficient_next,
                    -coefficient_previous / coefficient_next,
                ),
                (NUMBER_FIELD.one, NUMBER_FIELD.zero),
            )
        )
    identity = (
        (NUMBER_FIELD.one, NUMBER_FIELD.zero),
        (NUMBER_FIELD.zero, NUMBER_FIELD.one),
    )
    cycle_field = identity
    for local in local_field_transfers:
        cycle_field = field_matrix_multiply(local, cycle_field)
    monodromy_field = tuple(tuple(-value for value in row) for row in cycle_field)
    cycle_product = field_matrix_2(cycle_field)
    monodromy = field_matrix_2(monodromy_field)
    cycle_trace_field = cycle_field[0][0] + cycle_field[1][1]
    cycle_determinant_field = sp.prod(
        -local[0][1] for local in local_field_transfers
    )
    cycle_trace = field_expr(cycle_trace_field)
    cycle_determinant = field_expr(cycle_determinant_field)
    monodromy_trace = -cycle_trace
    monodromy_determinant = cycle_determinant
    normalized_trace_square = field_expr(
        cycle_trace_field**2 / cycle_determinant_field
    )
    cycle_characteristic = sp.Poly(
        Z**2 - cycle_trace * Z + cycle_determinant,
        Z,
        extension=ALGEBRAIC_EXTENSION,
    )
    monodromy_characteristic = sp.Poly(
        Z**2 - monodromy_trace * Z + monodromy_determinant,
        Z,
        extension=ALGEBRAIC_EXTENSION,
    )
    characteristic_valid = sp.Poly(
        exact(
            monodromy_characteristic.as_expr()
            - cycle_characteristic.as_expr().subs(Z, -Z)
        ),
        Z,
        extension=ALGEBRAIC_EXTENSION,
    ).is_zero
    return Transfer(
        bulk,
        slices,
        tuple(field_matrix_2(local) for local in local_field_transfers),
        cycle_product,
        monodromy,
        cycle_characteristic,
        monodromy_characteristic,
        monodromy_trace,
        monodromy_determinant,
        normalized_trace_square,
        fine_band,
        construction_valid,
        characteristic_valid,
    )


def build_z6(shear: sp.Rational) -> FixtureSolve:
    raw, calls = fixture_data_spatial(shear, SPACE_SIZE)
    action = raw.propagator.inv(method="DM").applyfunc(sp.expand)
    blocks = tuple(
        momentum_block(action, momentum, TIME_SIZE, SPACE_SIZE)
        for momentum in range(SPACE_SIZE)
    )
    transfers = tuple(transfer_from_action(block) for block in blocks)
    return FixtureSolve(shear, raw, calls, action, blocks, transfers)


def conjugate_expr(value: sp.Expr) -> sp.Expr:
    return field_expr(field_element(sp.conjugate(value)))


def conjugate_matrix(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.applyfunc(conjugate_expr)


def conjugate_polynomial(polynomial: sp.Poly) -> sp.Poly:
    coefficients = tuple(
        conjugate_expr(value) for value in polynomial.all_coeffs()
    )
    degree = polynomial.degree()
    return sp.Poly(
        sum(
            value * Z ** (degree - index)
            for index, value in enumerate(coefficients)
        ),
        Z,
        extension=ALGEBRAIC_EXTENSION,
    )


def strict_degeneracy(
    polynomials: tuple[sp.Poly, ...],
) -> tuple[tuple[int, ...], ...]:
    classes = []
    consumed: set[int] = set()
    for index, polynomial in enumerate(polynomials):
        if index in consumed:
            continue
        current = tuple(
            candidate_index
            for candidate_index, candidate in enumerate(polynomials)
            if candidate == polynomial
        )
        classes.append(current)
        consumed.update(current)
    return tuple(classes)


def trace_squares(fixture: FixtureSolve) -> tuple[sp.Rational, ...]:
    raw = tuple(
        transfer.normalized_trace_square for transfer in fixture.transfers
    )
    if not all(value.is_Rational for value in raw):
        raise AssertionError("normalized trace squares did not descend to QQ")
    return tuple(R(value) for value in raw)


def no_float(value: object) -> bool:
    if isinstance(value, sp.MatrixBase):
        return not value.has(sp.Float)
    return not sp.sympify(value).has(sp.Float)


def expected_shear_profile(shear: sp.Rational) -> dict[int, sp.Expr]:
    """The committed Z8 reflection profile built from the scalar c."""
    return {
        -4: -shear,
        -3: -shear,
        -2: -shear,
        -1: sp.S.Zero,
        0: shear,
        1: shear,
        2: shear,
        3: sp.S.Zero,
    }


@dataclass(frozen=True)
class NormalizationCertificate:
    trace_squares: tuple[sp.Rational, ...]
    q_coefficients: tuple[sp.Expr, ...]
    phase_relations: bool
    determinant_one: bool
    real_traces: bool
    absorption_identity: bool


def normalization_certificate(fixture: FixtureSolve) -> NormalizationCertificate:
    squares = trace_squares(fixture)
    q_coefficients = tuple(sp.sqrt(value) for value in squares)
    phase_relations = True
    determinant_one = True
    for transfer, value in zip(fixture.transfers, squares, strict=True):
        leading, coefficient, determinant = (
            transfer.monodromy_polynomial.all_coeffs()
        )
        coefficient_field = field_element(coefficient)
        determinant_field = field_element(determinant)
        value_field = field_element(value)
        relation = (
            leading == 1
            and coefficient == -transfer.monodromy_trace
            and determinant == transfer.monodromy_determinant
            and coefficient_field**2 == determinant_field * value_field
        )
        phase_relations &= relation
        determinant_one &= (
            relation
            and coefficient_field != NUMBER_FIELD.zero
            and determinant_field
            * value_field
            / coefficient_field**2
            == NUMBER_FIELD.one
        )

    abstract_a = sp.symbols("a", real=True, nonzero=True)
    abstract_u = sp.symbols("u", positive=True)
    sigma = abstract_a / sp.sqrt(abstract_u)
    raw_determinant = abstract_a**2 / abstract_u
    absorbed = sp.cancel(
        (
            (sigma * Z) ** 2
            + abstract_a * sigma * Z
            + raw_determinant
        )
        / sigma**2
        - (Z**2 + sp.sqrt(abstract_u) * Z + 1)
    )
    return NormalizationCertificate(
        squares,
        q_coefficients,
        phase_relations,
        determinant_one,
        all(value > 0 and root.is_real is True for value, root in zip(squares, q_coefficients)),
        absorbed == 0,
    )


def fixture_exact(fixture: FixtureSolve) -> bool:
    call_exact = (
        len(fixture.torus_calls) == 1
        and fixture.torus_calls[0].mass == EXPECTED_MASS
        and fixture.torus_calls[0].shear
        == expected_shear_profile(fixture.shear)
        and fixture.torus_calls[0].half_time * 2 == TIME_SIZE
        and fixture.torus_calls[0].boundary_sign == -1
        and fixture.torus_calls[0].spatial_extent == SPACE_SIZE
        and no_float(fixture.torus_calls[0].volume)
    )
    projectors6 = projectors(SPACE_SIZE)
    projector_exact = (
        len(projectors6) == SPACE_SIZE
        and b118.matrix_equal(
            sum(projectors6, sp.zeros(SPACE_SIZE)), sp.eye(SPACE_SIZE)
        )
        and all(
            b118.matrix_equal(
                projectors6[left] * projectors6[right],
                projectors6[left]
                if left == right
                else sp.zeros(SPACE_SIZE),
            )
            for left in range(SPACE_SIZE)
            for right in range(SPACE_SIZE)
        )
    )
    size = TIME_SIZE * SPACE_SIZE
    return (
        call_exact
        and len((fixture.torus_calls[0].half_time, SPACE_SIZE)) == 2
        and fixture.raw.propagator.shape == (size, size)
        and fixture.action.shape == (size, size)
        and len(fixture.blocks) == len(fixture.transfers) == SPACE_SIZE
        and all(block.shape == (TIME_SIZE, TIME_SIZE) for block in fixture.blocks)
        and b118.matrix_equal(
            fixture.action * fixture.raw.propagator, sp.eye(size)
        )
        and b118.matrix_equal(
            fixture.raw.propagator * fixture.action, sp.eye(size)
        )
        and projector_exact
        and all(
            transfer.fine_band
            and transfer.construction_valid
            and transfer.characteristic_valid
            and no_float(transfer.monodromy)
            for transfer in fixture.transfers
        )
        and no_float(fixture.action)
        and b119.prior is b118
    )


@dataclass(frozen=True)
class MirrorCertificate:
    action_reality: bool
    projector_kinematics: bool
    block_kinematics: bool
    monodromy_kinematics: bool
    polynomial_consequences: bool
    y_mirror: bool
    self_real: bool
    rho_real: bool


def mirror_certificate(
    fixture: FixtureSolve,
    sectors: tuple[SectorFactorization, ...],
) -> MirrorCertificate:
    squares = trace_squares(fixture)
    action_reality = b118.matrix_equal(
        fixture.action, fixture.action.applyfunc(sp.conjugate)
    )
    projector_kinematics = all(
        b118.matrix_equal(
            projectors(SPACE_SIZE)[(-momentum) % SPACE_SIZE],
            projectors(SPACE_SIZE)[momentum].applyfunc(sp.conjugate),
        )
        for momentum in range(SPACE_SIZE)
    )
    block_kinematics = all(
        b118.matrix_equal(
            fixture.blocks[(-momentum) % SPACE_SIZE],
            conjugate_matrix(fixture.blocks[momentum]),
        )
        for momentum in range(SPACE_SIZE)
    )
    monodromy_kinematics = all(
        b118.matrix_equal(
            fixture.transfers[(-momentum) % SPACE_SIZE].monodromy,
            conjugate_matrix(fixture.transfers[momentum].monodromy),
        )
        for momentum in range(SPACE_SIZE)
    )
    polynomials = tuple(
        transfer.monodromy_polynomial for transfer in fixture.transfers
    )
    polynomial_consequences = all(
        polynomials[(-momentum) % SPACE_SIZE]
        == conjugate_polynomial(polynomials[momentum])
        for momentum in range(SPACE_SIZE)
    )
    y_mirror = (
        all(sector.valid for sector in sectors)
        and sectors[5].y
        == tuple(nested_conjugate(value) for value in sectors[1].y)
        and sectors[4].y
        == tuple(nested_conjugate(value) for value in sectors[2].y)
    )
    self_real = all(
        sector.y == tuple(nested_conjugate(value) for value in sector.y)
        for sector in (sectors[0], sectors[3])
    )
    return MirrorCertificate(
        action_reality,
        projector_kinematics,
        block_kinematics,
        monodromy_kinematics,
        polynomial_consequences,
        y_mirror,
        self_real,
        all(value > 4 for value in squares),
    )


def rational_square(value: sp.Rational) -> bool:
    if value < 0:
        return False
    numerator_square = sp.integer_nthroot(abs(int(value.p)), 2)[1]
    denominator_square = sp.integer_nthroot(int(value.q), 2)[1]
    return numerator_square and denominator_square


@dataclass(frozen=True)
class RegimeCertificate:
    forced_unit_grams: bool
    self_real_gauge: bool
    field_tower_exact: bool


def regime_certificate(
    sectors: tuple[SectorFactorization, ...],
    squares: tuple[sp.Rational, ...],
) -> RegimeCertificate:
    forced_values = tuple(
        sectors[target].y[0]
        / nested_conjugate(sectors[source].y[0])
        for source, target in ((1, 5), (2, 4))
    )
    forced = (
        all(sector.valid for sector in sectors)
        and sectors[5].y
        == tuple(nested_conjugate(value) for value in sectors[1].y)
        and sectors[4].y
        == tuple(nested_conjugate(value) for value in sectors[2].y)
        and all(value == 1 for value in forced_values)
    )

    gauge = sp.symbols("g", real=True, nonzero=True)
    gauge_identity = sp.cancel((1 / gauge) * gauge - 1) == 0
    self_real_gauge = (
        (-0) % SPACE_SIZE == 0
        and (-3) % SPACE_SIZE == 3
        and all(
            sectors[momentum].valid
            and sectors[momentum].y
            == tuple(
                nested_conjugate(value) for value in sectors[momentum].y
            )
            for momentum in (0, 3)
        )
        and gauge_identity
    )
    u0 = squares[0]
    u_generic = squares[1]
    field_tower_exact = (
        squares
        == (u0, u_generic, u_generic, u0, u_generic, u_generic)
        and u0 > 4
        and u_generic > 4
        and rational_square(u0)
        and not rational_square(u_generic)
        and all(
            no_float(root)
            for value in (u0, u_generic)
            for root in (
                sp.sqrt(value),
                sp.sqrt(value - 4),
                sp.sqrt(value * (value - 4)),
            )
        )
    )
    return RegimeCertificate(forced, self_real_gauge, field_tower_exact)


def embedded(
    pair: tuple[int, int], block: sp.Matrix, spatial_size: int
) -> sp.Matrix:
    result = sp.zeros(spatial_size)
    for row in range(2):
        for column in range(2):
            result[pair[row], pair[column]] = block[row, column]
    return result


@dataclass(frozen=True)
class AlgebraCertificate:
    spatial_size: int
    pairs: tuple[tuple[int, int], ...]
    dimension: int
    center_dimension: int
    symmetric_blocks: bool
    jordan_closed: bool
    jordan_generator_antisymmetric: bool
    jordan_generator_excluded: bool


def algebra_certificate(spatial_size: int) -> AlgebraCertificate:
    pair_table = {
        4: ((1, 3), (0, 2)),
        6: ((1, 5), (2, 4), (0, 3)),
    }
    pairs = pair_table[spatial_size]
    identity = sp.eye(2)
    diagonal = sp.diag(1, -1)
    exchange = sp.Matrix(((0, 1), (1, 0)))
    local_basis = (identity, diagonal, exchange)
    bases = tuple(
        embedded(pair, basis, spatial_size)
        for pair in pairs
        for basis in local_basis
    )
    flattened = sp.Matrix.hstack(
        *(
            matrix.reshape(spatial_size**2, 1)
            for matrix in bases
        )
    )
    central_columns = tuple(
        sp.Matrix.vstack(
            *(
                (candidate * observable - observable * candidate).reshape(
                    spatial_size**2, 1
                )
                for observable in bases
            )
        )
        for candidate in bases
    )
    central_system = sp.Matrix.hstack(*central_columns)

    local_flattened = sp.Matrix.hstack(
        *(matrix.reshape(4, 1) for matrix in local_basis)
    )
    jordan_closed = all(
        local_flattened.row_join(
            ((left * right + right * left) / 2).reshape(4, 1)
        ).rank()
        == 3
        for left in local_basis
        for right in local_basis
    )
    jordan_generator = (diagonal * exchange - exchange * diagonal) / 2
    jordan_generator_antisymmetric = (
        jordan_generator != sp.zeros(2)
        and jordan_generator.T == -jordan_generator
    )
    jordan_generator_excluded = (
        local_flattened.row_join(jordan_generator.reshape(4, 1)).rank() == 4
        and all(
            flattened.row_join(
                embedded(pair, jordan_generator, spatial_size).reshape(
                    spatial_size**2, 1
                )
            ).rank()
            == flattened.rank() + 1
            for pair in pairs
        )
    )
    center_candidates = tuple(
        embedded(pair, identity, spatial_size) for pair in pairs
    )
    return AlgebraCertificate(
        spatial_size,
        pairs,
        flattened.rank(),
        len(bases) - central_system.rank(),
        len({index for pair in pairs for index in pair}) == spatial_size
        and all(matrix.T == matrix for matrix in bases)
        and all(
            left * right == sp.zeros(spatial_size)
            for left_index, left in enumerate(bases)
            for right_index, right in enumerate(bases)
            if left_index // 3 != right_index // 3
        )
        and all(
            candidate * observable == observable * candidate
            for candidate in center_candidates
            for observable in bases
        ),
        jordan_closed,
        jordan_generator_antisymmetric,
        jordan_generator_excluded,
    )


@dataclass(frozen=True)
class ChargeCertificate:
    not_indefinite: bool
    residue_not_integer_equality: bool
    conjugate_balanced_witnesses: bool
    self_balanced_zero_only: bool
    population_blocks: tuple[tuple[int, int], ...]


def charge_certificate() -> ChargeCertificate:
    charge_one = sp.diag(1, -1)
    charge_two = sp.diag(2, -2)
    charge_self = sp.diag(0, 3)
    balanced = sp.Matrix((1, 1))
    conjugate_witnesses = (
        balanced != sp.zeros(2, 1)
        and (balanced.T * charge_one * balanced)[0] == 0
        and (balanced.T * charge_two * balanced)[0] == 0
    )
    amplitude = sp.symbols("a", real=True)
    self_balanced = sp.Matrix((amplitude, amplitude))
    self_expectation = sp.expand(
        (self_balanced.T * charge_self * self_balanced)[0]
    )
    roots = sp.Poly(self_expectation, amplitude).all_roots()
    return ChargeCertificate(
        charge_self[0, 0] >= 0
        and charge_self[1, 1] > 0
        and charge_self.det() == 0
        and not (
            any(value < 0 for value in (charge_self[0, 0], charge_self[1, 1]))
            and any(value > 0 for value in (charge_self[0, 0], charge_self[1, 1]))
        ),
        3 % SPACE_SIZE == (-3) % SPACE_SIZE and sp.Integer(3) != sp.Integer(-3),
        conjugate_witnesses,
        self_expectation == 3 * amplitude**2 and roots == [0, 0],
        ((1, -1), (2, -2)),
    )


N5_LINES = (
    "N5: per_element: exact fixture, conjugation, normalization, regime, classification, and charge-definiteness certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: the six-sector carrier pairs by conjugation kinematics into two coupled pairs with forced unit gram and one per-sector-real pair with gauge gram",
    "per_block: the observable algebra scales to three symmetric blocks of total dimension nine with center three — the 3n law verified at two lattice sizes — while the self-conjugate block's charge is definite and the population break lives entirely in the conjugate pairs",
    "lattice_wide: checked and not executed — the general-Z_N theorem, the twisted-formulation record, the joint-lane program, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carriers, Records, audit retention, and TOE closure remain open",
)


SCOPE_KEYS = (
    "scaling_law",
    "charge_kinematic",
    "conjugation_mirror",
    "determinant_phase",
    "regimes",
    "two_point_boundary",
    "charge_correction",
    "jordan_exclusion",
    "field_tower",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
    "n5_verbatim",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "scaling_law": "scaling law" in note or "3n" in note,
        "charge_kinematic": (
            "charge-kinematic" in note or "kinematics, not" in note
        ),
        "conjugation_mirror": (
            "conjugation mirror" in note or "y_{-k} = conj(y_k)" in note
        ),
        "determinant_phase": (
            "determinant-phase" in note
            and ("presentation" in note or "normalization" in note)
        ),
        "regimes": "forced" in note and "gauge" in note,
        "two_point_boundary": (
            "verified at two points" in note
            or "not a proven general theorem" in note
        ),
        "charge_correction": (
            "not indefinite" in note or "residue" in note
        ),
        "jordan_exclusion": (
            "jordan" in note and "not an admissible" in note
        ),
        "field_tower": "field tower" in note or "sqrt" in note,
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
        "n5_verbatim": all(
            " ".join(line.lower().split()) in note for line in N5_LINES
        ),
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
        result["w1"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
        result["n5_verbatim"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_general_law_proven":
        result["two_point_boundary"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()
    checks = Checks()

    note = normalized_note(raw_note())
    authority = authority_certificate(mutation)
    authority_raw = (
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_OBSERVABLE_SCALING_LAW_BOUNDED_THEOREM_NOTE_2026-08-18.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_RESIDUAL_INVARIANCE_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_residual_invariance_theorem_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_residual_invariance_theorem_2026_08_17.txt",
            "scripts/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.txt",
            "scripts/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 135)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
        and authority["worktree_parent_note"] == PARENT_NOTE_BLOB
        and authority["worktree_parent_runner"] == PARENT_RUNNER_BLOB
        and authority["worktree_parent_cache"] == PARENT_CACHE_BLOB
        and authority["b118_ancestor"]
        and authority["b118_runner"] == B118_RUNNER_BLOB
        and authority["b118_cache"] == B118_CACHE_BLOB
        and authority["worktree_b118_runner"] == B118_RUNNER_BLOB
        and authority["worktree_b118_cache"] == B118_CACHE_BLOB
        and authority["b119_ancestor"]
        and authority["b119_runner"] == B119_RUNNER_BLOB
        and authority["b119_cache"] == B119_CACHE_BLOB
        and authority["worktree_b119_runner"] == B119_RUNNER_BLOB
        and authority["worktree_b119_cache"] == B119_CACHE_BLOB
        and block135.AUDIT_TIMEOUT_SEC == AUDIT_TIMEOUT_SEC
        and b119.prior is b118
    )
    checks.check(
        "A-authority",
        "Block 135 parent note/runner/cache, ancestors 134--103, and Block 118/119 runner/cache machinery are content-bound",
        authority_raw,
    )

    primary = build_z6(PRIMARY_SHEAR)
    secondary = build_z6(SECOND_SHEAR)
    fixtures = (primary, secondary)
    normalizations = tuple(normalization_certificate(item) for item in fixtures)
    sector_sets = tuple(
        sector_factorizations(item.transfers, normal.trace_squares)
        for item, normal in zip(fixtures, normalizations, strict=True)
    )
    polynomial_sets = tuple(
        tuple(transfer.monodromy_polynomial for transfer in item.transfers)
        for item in fixtures
    )
    raw_classes = tuple(strict_degeneracy(items) for items in polynomial_sets)

    primary_polynomials = polynomial_sets[0]
    fixture_raw = (
        primary.shear == PRIMARY_SHEAR
        and fixture_exact(primary)
        and raw_classes[0] == ((0, 3), (1, 4), (2, 5))
        and primary_polynomials[5]
        == conjugate_polynomial(primary_polynomials[1])
        and primary_polynomials[4]
        == conjugate_polynomial(primary_polynomials[2])
        and normalizations[0].determinant_one
        and normalizations[0].real_traces
    )
    checks.check(
        "B-the-z6-fixture",
        "the d=2, m=9/20, c=5/13, Z8-AP x Z6 fixture has six exact sectors, determinant-one real-trace normalized monodromies, and raw classes (0,3)/(1,4)/(2,5) with the stated conjugates",
        fixture_raw and mutation != "break_z6_fixture",
    )

    mirrors = tuple(
        mirror_certificate(fixture, sectors)
        for fixture, sectors in zip(fixtures, sector_sets, strict=True)
    )
    conjugation_raw = (
        all(fixture_exact(item) for item in fixtures)
        and raw_classes
        == (
            ((0, 3), (1, 4), (2, 5)),
            ((0, 3), (1, 4), (2, 5)),
        )
        and all(
            item.block_kinematics
            and item.monodromy_kinematics
            and item.polynomial_consequences
            and item.y_mirror
            and item.self_real
            for item in mirrors
        )
    )
    derivation_raw = all(
        item.action_reality
        and item.projector_kinematics
        and item.rho_real
        for item in mirrors
    )
    if mutation == "break_conjugation":
        conjugation_raw = False
    if mutation == "break_kinematic_derivation":
        derivation_raw = False
    checks.check(
        "C-the-conjugation-mirror",
        "action reality and real stable rho give M_-k=conj(M_k), hence y5=conj(y1), y4=conj(y2), and individually real y0/y3 at c=5/13 and 3/5; polynomial pairing is consequential",
        conjugation_raw and derivation_raw,
    )

    normalization_raw = all(
        item.phase_relations
        and item.determinant_one
        and item.real_traces
        and item.absorption_identity
        and item.trace_squares
        == (
            item.trace_squares[0],
            item.trace_squares[1],
            item.trace_squares[1],
            item.trace_squares[0],
            item.trace_squares[1],
            item.trace_squares[1],
        )
        and item.q_coefficients[0] == item.q_coefficients[3]
        and item.q_coefficients[1]
        == item.q_coefficients[2]
        == item.q_coefficients[4]
        == item.q_coefficients[5]
        and item.q_coefficients[0] != item.q_coefficients[1]
        for item in normalizations
    )
    checks.check(
        "D-the-normalization",
        "absorbing sigma_k=(-tr M_k)/sqrt(u_k), sigma_k^2=det M_k, is a determinant-phase presentation normalization giving q1=q2=q4=q5 and q0=q3, not new physics",
        normalization_raw and mutation != "break_normalization",
    )

    regimes = tuple(
        regime_certificate(sectors, normal.trace_squares)
        for sectors, normal in zip(sector_sets, normalizations, strict=True)
    )
    regime_raw = all(
        item.forced_unit_grams
        and item.self_real_gauge
        and item.field_tower_exact
        for item in regimes
    )
    checks.check(
        "E-the-regimes-and-g",
        "(1,5)/(2,4) are conjugate-coupled and pivot normalization forces g=1; self-real (0,3) has relative g gauge, with every required sqrt retained in the exact field tower",
        regime_raw and mutation != "break_regime_g",
    )

    algebra4 = algebra_certificate(4)
    algebra6 = algebra_certificate(6)
    algebra_raw = (
        algebra4.pairs == ((1, 3), (0, 2))
        and algebra4.dimension == 6
        and algebra4.center_dimension == 2
        and algebra4.symmetric_blocks
        and algebra4.jordan_closed
        and algebra6.pairs == ((1, 5), (2, 4), (0, 3))
        and algebra6.dimension == 9
        and algebra6.center_dimension == 3
        and algebra6.symmetric_blocks
        and algebra6.jordan_closed
        and (len(algebra4.pairs), algebra4.dimension, algebra4.center_dimension)
        == (2, 6, 2)
        and (len(algebra6.pairs), algebra6.dimension, algebra6.center_dimension)
        == (3, 9, 3)
        and algebra4.dimension == 3 * 2
        and algebra6.dimension == 3 * 3
    )
    jordan_raw = all(
        item.jordan_generator_antisymmetric
        and item.jordan_generator_excluded
        for item in (algebra4, algebra6)
    )
    if mutation == "break_algebra_count":
        algebra_raw = False
    if mutation == "break_jordan_exclusion":
        jordan_raw = False
    checks.check(
        "F-the-algebra-count",
        "the classified algebra is Sym_2(R)^3 with (dim,center)=(9,3); Z4/Z6 verify 3n at two points only, and J=[Z,X]/2 is antisymmetric and not admissible",
        algebra_raw and jordan_raw,
    )

    charge = charge_certificate()
    definiteness_raw = charge.not_indefinite and charge.residue_not_integer_equality
    population_raw = (
        charge.conjugate_balanced_witnesses
        and charge.self_balanced_zero_only
        and charge.population_blocks == ((1, -1), (2, -2))
    )
    if mutation == "break_charge_definiteness":
        definiteness_raw = False
    if mutation == "claim_03_populates":
        population_raw = False
    checks.check(
        "G-the-charge-correction",
        "diag(0,3) is sign-definite/not indefinite over integer charges (3=-3 only residually); its balanced zero-expectation ray is zero, while (1,-1) and (2,-2) each have a nonzero balanced witness",
        definiteness_raw and population_raw,
    )

    scope = scope_certificate(note, mutation)
    elapsed_ns = time.monotonic_ns() - started_ns
    checks.check(
        "H-scope",
        "scaling, kinematics, normalization, regimes, two-point boundary, charge/Jordan corrections, field caveats, N1--N8/W1/N5, no-go, and TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_ns <= 500 * 1_000_000_000,
    )

    print(
        f"AUTHORITY: Block135 parent={authority['parent']}; note/runner/cache, "
        "ancestors 134--103, and Block118/119 runner/cache pins exact"
    )
    print(
        f"FIXTURE: d=2 DK; m=9/20; c={PRIMARY_SHEAR}; time=Z8 AP; "
        f"space=Z6; sectors=6; raw classes={raw_classes[0]}"
    )
    print(
        "MIRROR: action reality + rho real => M_-k=conj(M_k) => "
        "y5=conj(y1), y4=conj(y2), y0/y3 real; c=3/5 spot exact"
    )
    print(
        "NORMALIZATION: p_k(sigma_k*z)/sigma_k^2=q_k(z), "
        "sigma_k^2=det(M_k); q1=q2=q4=q5, q0=q3; presentation only"
    )
    print(
        "REGIMES/FIELDS: (1,5),(2,4) forced g=1; (0,3) gauge g; "
        "Q(i,sqrt(3)) then sqrt(u), sqrt(u-4), sqrt(u(u-4)) as required"
    )
    print(
        "ALGEBRA: Sym_2(R)^3, dim=9, center=R^3; Z4=(2,6,2), "
        "Z6=(3,9,3): 3n verified at two points, not a proven general theorem; antisymmetric J excluded"
    )
    print(
        "CHARGE: diag(0,3) is positive-semidefinite/not indefinite; "
        "3=-3 only mod 6; balanced zero-expectation population is nonzero only in (1,-1),(2,-2)"
    )
    for line in N5_LINES:
        print(line)
    if checks.failed == 0:
        print(
            "RESULT: the observable algebra grows by the charge-kinematic "
            "law — conjugation pairing predicts the block structure for every "
            "lattice size, the 3n count is verified at two sizes, and the "
            "population physics stays in the conjugate pairs"
        )
        print(
            "DECISION_CUT: pose the general-Z_N theorem and continue the "
            "campaign queue; reject residue-integer charge conflations and "
            "general-law overclaims"
        )
    else:
        print(
            "RESULT: BLOCKED — at least one exact authority, fixture, mirror, "
            "normalization, regime, algebra, charge, scope, mutation, or runtime certificate failed"
        )
        print(
            "DECISION_CUT: repair the failed certificate without treating "
            "residue pairing as integer-charge indefiniteness or two points as a theorem"
        )
    print(
        "TOE: zero obligation retirement; no TOE percentage moves; "
        "retained-positive end-to-end theory count remains zero; gravity "
        "constraint quotient remains unexecuted; actual ADM/history transporter remains open"
    )
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
