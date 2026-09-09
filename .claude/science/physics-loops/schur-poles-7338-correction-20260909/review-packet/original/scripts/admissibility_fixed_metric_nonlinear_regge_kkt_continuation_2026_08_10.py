#!/usr/bin/env python3
"""Certify an affine metric-tangent Regge background and source branches.

The calculation keeps the ten constant-metric tangent coordinates fixed and
solves the remaining five homogeneous edge equations of the actual 4D
Kuhn/Coxeter Regge action.  A two-variable symmetry reduction is certified by
an interval Krawczyk step; the full five-normal Hessian then supplies an
implicit-function continuation for the three declared compact sources.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
import json
from pathlib import Path
import sys

import mpmath as mp
from mpmath import iv
import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 240

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NONLINEAR_REGGE_EXTRA_BRANCH_CUBIC_LIFT_"
    "SOURCE_COMPATIBILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REACTION_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PREMISE_REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
PRIMITIVE_PATHS = (
    ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_NONLINEAR_REGGE_EXTRA_BRANCH_CUBIC_LIFT_SOURCE_COMPATIBILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "scripts/admissibility_nonlinear_regge_extra_branch_cubic_lift_2026_08_10.py",
    "scripts/admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)

sys.path.insert(0, str(ROOT / "scripts"))
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402
import admissibility_compact_regge_homogeneous_reaction_rank_kkt_boundary_2026_08_10 as reaction  # noqa: E402


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


@dataclass
class Jet2:
    """Scalar value with a first derivative and Hessian."""

    value: object
    grad: list[object]
    hess: list[list[object]]
    ctx: object

    @property
    def n(self) -> int:
        return len(self.grad)

    @classmethod
    def constant(cls, value, n: int, ctx) -> "Jet2":
        zero = ctx.mpf(0)
        converted = value if hasattr(value, "_mpf_") or hasattr(value, "_mpi_") else ctx.mpf(value)
        return cls(converted, [zero for _ in range(n)], [[zero for _ in range(n)] for _ in range(n)], ctx)

    @classmethod
    def variable(cls, value, index: int, n: int, ctx) -> "Jet2":
        out = cls.constant(value, n, ctx)
        out.grad[index] = ctx.mpf(1)
        return out

    def _coerce(self, other) -> "Jet2":
        if isinstance(other, Jet2):
            return other
        return Jet2.constant(other, self.n, self.ctx)

    def __add__(self, other) -> "Jet2":
        rhs = self._coerce(other)
        return Jet2(
            self.value + rhs.value,
            [self.grad[i] + rhs.grad[i] for i in range(self.n)],
            [
                [self.hess[i][j] + rhs.hess[i][j] for j in range(self.n)]
                for i in range(self.n)
            ],
            self.ctx,
        )

    __radd__ = __add__

    def __neg__(self) -> "Jet2":
        return Jet2(
            -self.value,
            [-entry for entry in self.grad],
            [[-entry for entry in row] for row in self.hess],
            self.ctx,
        )

    def __sub__(self, other) -> "Jet2":
        return self + (-self._coerce(other))

    def __rsub__(self, other) -> "Jet2":
        return self._coerce(other) - self

    def __mul__(self, other) -> "Jet2":
        rhs = self._coerce(other)
        grad = [
            self.grad[i] * rhs.value + self.value * rhs.grad[i]
            for i in range(self.n)
        ]
        hess = [
            [
                self.hess[i][j] * rhs.value
                + self.value * rhs.hess[i][j]
                + self.grad[i] * rhs.grad[j]
                + rhs.grad[i] * self.grad[j]
                for j in range(self.n)
            ]
            for i in range(self.n)
        ]
        return Jet2(self.value * rhs.value, grad, hess, self.ctx)

    __rmul__ = __mul__

    def inverse(self) -> "Jet2":
        return unary_jet(
            self,
            lambda value: 1 / value,
            lambda value: -1 / (value * value),
            lambda value: 2 / (value * value * value),
        )

    def __truediv__(self, other) -> "Jet2":
        return self * self._coerce(other).inverse()

    def __rtruediv__(self, other) -> "Jet2":
        return self._coerce(other) * self.inverse()


def unary_jet(value: Jet2, function, first, second) -> Jet2:
    fp = first(value.value)
    fpp = second(value.value)
    return Jet2(
        function(value.value),
        [fp * entry for entry in value.grad],
        [
            [
                fp * value.hess[i][j]
                + fpp * value.grad[i] * value.grad[j]
                for j in range(value.n)
            ]
            for i in range(value.n)
        ],
        value.ctx,
    )


def jet_sqrt(value: Jet2) -> Jet2:
    return unary_jet(
        value,
        value.ctx.sqrt,
        lambda entry: 1 / (2 * value.ctx.sqrt(entry)),
        lambda entry: -1 / (4 * entry * value.ctx.sqrt(entry)),
    )


def jet_acos(value: Jet2) -> Jet2:
    def function(entry):
        if value.ctx is iv:
            return iv.atan2(iv.sqrt(1 - entry * entry), entry)
        return mp.acos(entry)

    return unary_jet(
        value,
        function,
        lambda entry: -1 / value.ctx.sqrt(1 - entry * entry),
        lambda entry: -entry
        / ((1 - entry * entry) * value.ctx.sqrt(1 - entry * entry)),
    )


def edge_class_index(left, right) -> int:
    return regge.edge_class(left, right)[0]


def triangle_edge_classes(vertices) -> tuple[int, int, int]:
    return tuple(
        edge_class_index(vertices[i], vertices[j])
        for i, j in ((0, 1), (0, 2), (1, 2))
    )


def simplex_edge_classes(vertices) -> tuple[int, ...]:
    return tuple(
        edge_class_index(vertices[i], vertices[j]) for i, j in regge.PAIRS5
    )


TRIANGLE_DATA = []
for _triangle in regge.TRI_CLASSES:
    _stars = []
    for _simplex in regge.STARS[_triangle]:
        _local = {vertex: index for index, vertex in enumerate(_simplex)}
        _hinge = sorted(_local[vertex] for vertex in _triangle)
        _missing = tuple(sorted(index for index in range(5) if index not in _hinge))
        _stars.append((_missing, simplex_edge_classes(_simplex)))
    TRIANGLE_DATA.append((triangle_edge_classes(_triangle), tuple(_stars)))
TRIANGLE_DATA = tuple(TRIANGLE_DATA)


def action_jet(lengths: list[Jet2]) -> Jet2:
    n = lengths[0].n
    ctx = lengths[0].ctx
    squared = tuple(length * length for length in lengths)
    area_cache: dict[tuple[int, int, int], Jet2] = {}
    angle_cache: dict[tuple[tuple[int, int], tuple[int, ...]], Jet2] = {}

    def area(classes: tuple[int, int, int]) -> Jet2:
        if classes not in area_cache:
            qa, qb, qc = (squared[index] for index in classes)
            area_cache[classes] = jet_sqrt(
                (
                    2 * qa * qb
                    + 2 * qa * qc
                    + 2 * qb * qc
                    - qa * qa
                    - qb * qb
                    - qc * qc
                )
                / 16
            )
        return area_cache[classes]

    def angle(missing: tuple[int, int], classes: tuple[int, ...]) -> Jet2:
        key = (missing, classes)
        if key in angle_cache:
            return angle_cache[key]
        q = {pair: squared[classes[index]] for index, pair in enumerate(regge.PAIRS5)}

        def qq(i: int, j: int) -> Jet2:
            return q[(min(i, j), max(i, j))]

        def dot(i: int, j: int, base: int) -> Jet2:
            if i == j:
                return qq(base, i)
            return (qq(base, i) + qq(base, j) - qq(i, j)) / 2

        left, right = missing
        base, first, second = [index for index in range(5) if index not in missing]
        g11 = dot(first, first, base)
        g12 = dot(first, second, base)
        g22 = dot(second, second, base)
        determinant = g11 * g22 - g12 * g12

        def projected_pair(i: int, j: int) -> Jet2:
            i1, i2 = dot(first, i, base), dot(second, i, base)
            j1, j2 = dot(first, j, base), dot(second, j, base)
            projection = (
                g22 * i1 * j1
                - g12 * (i1 * j2 + i2 * j1)
                + g11 * i2 * j2
            ) / determinant
            return dot(i, j, base) - projection

        cosine = projected_pair(left, right) / jet_sqrt(
            projected_pair(left, left) * projected_pair(right, right)
        )
        angle_cache[key] = jet_acos(cosine)
        return angle_cache[key]

    total = Jet2.constant(0, n, ctx)
    for area_classes, stars in TRIANGLE_DATA:
        deficit = Jet2.constant(2 * ctx.pi, n, ctx)
        for missing, simplex_classes in stars:
            deficit -= angle(missing, simplex_classes)
        total += area(area_classes) * deficit
    return total


def exact_symmetric_vectors(ctx) -> tuple[list[object], list[object]]:
    zero = sp.Integer(0) if ctx is sp else ctx.mpf(0)
    range_by_weight = {
        1: ctx.sqrt(6) / 8,
        2: -ctx.sqrt(3) / 6,
        3: ctx.sqrt(2) / 8,
        4: zero,
    }
    extra_by_weight = {
        1: -ctx.sqrt(2) / 8,
        2: zero,
        3: ctx.sqrt(6) / 8,
        4: -ctx.sqrt(2) / 2,
    }
    return (
        [range_by_weight[sum(direction)] for direction in regge.DIRS15],
        [extra_by_weight[sum(direction)] for direction in regge.DIRS15],
    )


def exact_anisotropic_vector(ctx, special_coordinate: int = 3) -> list[object]:
    """One exact unit vector in the three-dimensional eigenvalue -16 irrep."""
    zero = sp.Integer(0) if ctx is sp else ctx.mpf(0)
    values = []
    for direction in regge.DIRS15:
        weight = sum(direction)
        contains_special = bool(direction[special_coordinate])
        if weight == 1:
            value = ctx.sqrt(6) / 8 if contains_special else -ctx.sqrt(6) / 24
        elif weight == 2:
            value = -ctx.sqrt(3) / 6 if contains_special else ctx.sqrt(3) / 6
        elif weight == 3:
            value = ctx.sqrt(2) / 8 if contains_special else -3 * ctx.sqrt(2) / 8
        else:
            value = zero
        values.append(value)
    return values


def exact_normal_basis(ctx) -> list[list[object]]:
    """An exact, generally nonorthogonal basis of ``ker(M_0^T)``.

    The first and last columns are the two coordinate-symmetric normal
    directions.  Three of the four tetrahedral anisotropic vectors span the
    standard three-dimensional ``S_4`` representation; their fourth partner is
    minus their sum.
    """
    range_vector, extra_vector = exact_symmetric_vectors(ctx)
    anisotropic = [exact_anisotropic_vector(ctx, index) for index in range(3)]
    columns = [range_vector, *anisotropic, extra_vector]
    return [
        [columns[column][edge] for column in range(5)]
        for edge in range(15)
    ]


def exact_normal_basis_sympy() -> sp.Matrix:
    return sp.Matrix(exact_normal_basis(sp))


def sympy_scalar_in_ctx(value: sp.Expr, ctx):
    """Evaluate the small algebraic source field with directed rounding."""
    value = sp.sympify(value)
    if value.is_Integer:
        return ctx.mpf(int(value))
    if value.is_Rational:
        return ctx.mpf(int(value.p)) / ctx.mpf(int(value.q))
    if value.is_Add:
        return sum(sympy_scalar_in_ctx(term, ctx) for term in value.args)
    if value.is_Mul:
        result = ctx.mpf(1)
        for factor in value.args:
            result *= sympy_scalar_in_ctx(factor, ctx)
        return result
    if value.is_Pow and value.exp == sp.Rational(1, 2):
        return ctx.sqrt(sympy_scalar_in_ctx(value.base, ctx))
    if value.is_Pow and value.exp.is_Integer:
        return sympy_scalar_in_ctx(value.base, ctx) ** int(value.exp)
    raise ValueError(f"unsupported exact scalar: {value!r}")


def exact_source_target(source: sp.Matrix, coupling: sp.Rational, ctx):
    projection = coupling * exact_normal_basis_sympy().T * source
    return [sympy_scalar_in_ctx(entry, ctx) for entry in projection]


def symmetric_action(a, u, ctx=mp) -> Jet2:
    range_vector, extra_vector = exact_symmetric_vectors(ctx)
    a_jet = Jet2.variable(a, 0, 2, ctx)
    u_jet = Jet2.variable(u, 1, 2, ctx)
    lengths = [
        Jet2.constant(ctx.sqrt(sum(direction)), 2, ctx)
        + a_jet * range_vector[index]
        + u_jet * extra_vector[index]
        for index, direction in enumerate(regge.DIRS15)
    ]
    return action_jet(lengths)


def symmetric_anisotropic_action(a, u, v, ctx=mp) -> Jet2:
    range_vector, extra_vector = exact_symmetric_vectors(ctx)
    anisotropic_vector = exact_anisotropic_vector(ctx)
    variables = [Jet2.variable(value, index, 3, ctx) for index, value in enumerate((a, u, v))]
    lengths = [
        Jet2.constant(ctx.sqrt(sum(direction)), 3, ctx)
        + variables[0] * range_vector[index]
        + variables[1] * extra_vector[index]
        + variables[2] * anisotropic_vector[index]
        for index, direction in enumerate(regge.DIRS15)
    ]
    return action_jet(lengths)


def numeric_normal_basis() -> tuple[np.ndarray, np.ndarray]:
    q0 = regge.bloch_Q(np.zeros(4)).real
    eigenvalues, eigenvectors = np.linalg.eigh(q0)
    range_basis = eigenvectors[:, np.abs(eigenvalues) > 1.0e-8]
    exact_range, exact_extra = exact_symmetric_vectors(mp)
    symmetric_range = np.asarray([float(value) for value in exact_range])
    if float(range_basis[:, 0] @ symmetric_range) < 0:
        range_basis[:, 0] *= -1
    extra = np.asarray([float(value) for value in exact_extra])
    return np.column_stack((range_basis, extra)), eigenvalues


def normal_action(coordinates: list[object], basis, ctx=mp) -> Jet2:
    n = 5
    variables = [
        Jet2.variable(coordinates[index], index, n, ctx) for index in range(n)
    ]
    lengths = []
    for edge, direction in enumerate(regge.DIRS15):
        value = Jet2.constant(ctx.sqrt(sum(direction)), n, ctx)
        for column in range(n):
            entry = basis[edge, column] if isinstance(basis, np.ndarray) else basis[edge][column]
            value += variables[column] * entry
        lengths.append(value)
    return action_jet(lengths)


def symmetric_root() -> tuple[mp.mpf, mp.mpf, Jet2]:
    def equations(a, u):
        value = symmetric_action(a, u, mp)
        return value.grad[0], value.grad[1]

    a_root, u_root = mp.findroot(
        equations,
        (mp.mpf("0.01763"), mp.mpf("0.15224")),
        solver="mdnewton",
        tol=mp.mpf("1e-48"),
        maxsteps=30,
    )
    return a_root, u_root, symmetric_action(a_root, u_root, mp)


def krawczyk_certificate(a_root: mp.mpf, u_root: mp.mpf, root_jet: Jet2):
    radius = mp.mpf("1e-9")
    a_box = iv.mpf([mp.nstr(a_root - radius, 70), mp.nstr(a_root + radius, 70)])
    u_box = iv.mpf([mp.nstr(u_root - radius, 70), mp.nstr(u_root + radius, 70)])
    box_jet = symmetric_action(a_box, u_box, iv)
    jacobian_box = box_jet.hess
    center_jacobian = mp.matrix(root_jet.hess)
    inverse = center_jacobian ** -1
    center = mp.matrix([a_root, u_root])
    center_interval = [
        iv.mpf(mp.nstr(a_root, 70)),
        iv.mpf(mp.nstr(u_root, 70)),
    ]
    point_jet = symmetric_action(center_interval[0], center_interval[1], iv)
    inverse_interval = [
        [iv.mpf(mp.nstr(inverse[row, column], 70)) for column in range(2)]
        for row in range(2)
    ]
    newton_center = []
    for row in range(2):
        value = center_interval[row]
        for column in range(2):
            value -= inverse_interval[row][column] * point_jet.grad[column]
        newton_center.append(value)
    delta_box = iv.mpf([mp.nstr(-radius, 70), mp.nstr(radius, 70)])
    krawczyk = []
    for row in range(2):
        value = newton_center[row]
        for column in range(2):
            coefficient = iv.mpf(int(row == column))
            for inner in range(2):
                coefficient -= (
                    inverse_interval[row][inner] * jacobian_box[inner][column]
                )
            value += coefficient * delta_box
        krawczyk.append(value)
    inside = all(
        float(value.a) > float(center[index] - radius)
        and float(value.b) < float(center[index] + radius)
        for index, value in enumerate(krawczyk)
    )
    contraction = max(
        (float(value.b) - float(value.a)) / (2 * float(radius))
        for value in krawczyk
    )
    return inside, contraction, radius


def full_normal_interval_certificate(a_root: mp.mpf, u_root: mp.mpf):
    radius = mp.mpf("1e-9")
    a_box = iv.mpf([mp.nstr(a_root - radius, 70), mp.nstr(a_root + radius, 70)])
    u_box = iv.mpf([mp.nstr(u_root - radius, 70), mp.nstr(u_root + radius, 70)])
    zero = iv.mpf([0, 0])
    value = symmetric_anisotropic_action(a_box, u_box, zero, iv)
    symmetric_determinant = (
        value.hess[0][0] * value.hess[1][1]
        - value.hess[0][1] * value.hess[1][0]
    )
    anisotropic_entry = value.hess[2][2]
    mixed_entries = (value.hess[0][2], value.hess[1][2])
    certified = (
        float(symmetric_determinant.b) < 0
        and float(anisotropic_entry.b) < -1
        and all(float(entry.a) <= 0 <= float(entry.b) for entry in mixed_entries)
    )
    return certified, symmetric_determinant, anisotropic_entry


def newton_source_branch(
    basis,
    start: list[mp.mpf],
    source: sp.Matrix,
    coupling: sp.Rational,
) -> tuple[list[mp.mpf], Jet2, mp.mpf]:
    target = exact_source_target(source, coupling, mp)
    coordinates = list(start)
    for _ in range(12):
        value = normal_action(coordinates, basis)
        residual = mp.matrix(
            [value.grad[index] - target[index] for index in range(5)]
        )
        if mp.norm(residual) < mp.mpf("1e-42"):
            break
        correction = mp.lu_solve(mp.matrix(value.hess), -residual)
        coordinates = [coordinates[index] + correction[index] for index in range(5)]
    value = normal_action(coordinates, basis)
    residual_norm = mp.norm(
        mp.matrix([value.grad[index] - target[index] for index in range(5)])
    )
    return coordinates, value, residual_norm


def normal_krawczyk_certificate(
    center: list[mp.mpf],
    center_jet: Jet2,
    source: sp.Matrix,
    coupling: sp.Rational,
):
    """Certify one five-dimensional sourced normal root."""
    radius = mp.mpf("1e-9")
    boxes = [
        iv.mpf(
            [
                mp.nstr(value - radius, 70),
                mp.nstr(value + radius, 70),
            ]
        )
        for value in center
    ]
    interval_basis = exact_normal_basis(iv)
    box_jet = normal_action(boxes, interval_basis, iv)
    inverse = mp.matrix(center_jet.hess) ** -1
    center_intervals = [iv.mpf(mp.nstr(value, 70)) for value in center]
    point_jet = normal_action(center_intervals, interval_basis, iv)
    inverse_intervals = [
        [iv.mpf(mp.nstr(inverse[row, column], 70)) for column in range(5)]
        for row in range(5)
    ]
    targets = exact_source_target(source, coupling, iv)
    newton_center = []
    for row in range(5):
        value = center_intervals[row]
        for column in range(5):
            value -= inverse_intervals[row][column] * (
                point_jet.grad[column] - targets[column]
            )
        newton_center.append(value)
    delta_box = iv.mpf([mp.nstr(-radius, 70), mp.nstr(radius, 70)])
    krawczyk = []
    for row in range(5):
        value = newton_center[row]
        for column in range(5):
            coefficient = iv.mpf(int(row == column))
            for inner in range(5):
                coefficient -= (
                    inverse_intervals[row][inner]
                    * box_jet.hess[inner][column]
                )
            value += coefficient * delta_box
        krawczyk.append(value)
    inside = all(
        float(value.a) > float(center[index] - radius)
        and float(value.b) < float(center[index] + radius)
        for index, value in enumerate(krawczyk)
    )
    contraction = max(
        (float(value.b) - float(value.a)) / (2 * float(radius))
        for value in krawczyk
    )
    return inside, contraction, radius


def periodic_box_action_value(coordinates: list[object], basis) -> float:
    """Independent value through the original periodic L=3 action."""
    point = np.asarray([float(value) for value in coordinates], dtype=float)
    basis_array = np.asarray(basis, dtype=float)
    delta = basis_array @ point
    return regge.box_action(
        3,
        lambda edge_class, _anchor: float(delta[edge_class]),
    ) / (3 ** 4)


def periodic_box_central_gradient(
    coordinates: list[object],
    basis,
    step: mp.mpf,
) -> np.ndarray:
    gradient = []
    for index in range(5):
        plus = list(coordinates)
        minus = list(coordinates)
        plus[index] += step
        minus[index] -= step
        gradient.append(
            (
                periodic_box_action_value(plus, basis)
                - periodic_box_action_value(minus, basis)
            )
            / (2 * float(step))
        )
    return np.asarray(gradient)


def main() -> int:
    mp.mp.dps = 60
    iv.dps = 50
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent_note = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    reaction_note = REACTION_NOTE_PATH.read_text(encoding="utf-8")
    premise_registry = json.loads(PREMISE_REGISTRY_PATH.read_text(encoding="utf-8"))
    primitive_notes = tuple(
        " ".join(path.read_text(encoding="utf-8").split())
        for path in PRIMITIVE_PATHS
    )
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())

    print("external_scientific_inputs: none; the construction uses the supplied actual Regge action and declared compact sources")
    print("package_local_integrity_reads: current axioms, Block 17 reaction ranks, Block 18 nonlinear lift, and the retained Regge carrier are source-bound")
    print("analytic_boundary: the background and all three finite source continuations have interval Krawczyk certificates")
    print("physical_boundary: the ten affine metric-tangent constraints, targets, action selection, coupling, Lorentzian stability, and realized history remain unselected")

    checks.check(
        "source-current-axiom-boundary",
        "Admissibility is not a dynamics axiom" in axiom_flat
        and "source/action and physical-observable identification" in axiom_flat,
    )
    checks.check(
        "source-parent-boundary",
        "complete cubic null-sector polynomial" in parent_note
        and "full nonlinear source no-go" in parent_note
        and "three/four/eleven-channel" in reaction_note,
    )
    checks.check(
        "source-approved-primitive-boundary",
        premise_registry["nodes"]["scale_reference_primitive"]["current_path"]
        == "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"
        and premise_registry["nodes"]["kinetic_isotropy_primitive"]["current_path"]
        == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
        and premise_registry["nodes"]["realized_state_primitive"]["current_path"]
        == "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
        and "units conversion, not a physics axiom" in primitive_notes[0]
        and "not a new dynamics" in primitive_notes[1]
        and "It does not supply a state, state-selection rule" in primitive_notes[2],
        "approved primitives supply no geometry action, compact ensemble, boundary target, coupling, or stability rule",
    )

    basis, eigenvalues = numeric_normal_basis()
    metric_map_exact = reaction.exact_metric_map()
    metric_map = reaction.matrix_float(metric_map_exact)
    exact_basis_symbolic = exact_normal_basis_sympy()
    exact_basis_numeric = exact_normal_basis(mp)
    exact_basis_float = np.asarray(exact_basis_numeric, dtype=float)
    expected_gram = sp.Matrix(
        [
            [1, 0, 0, 0, 0],
            [0, 1, -sp.Rational(1, 3), -sp.Rational(1, 3), 0],
            [0, -sp.Rational(1, 3), 1, -sp.Rational(1, 3), 0],
            [0, -sp.Rational(1, 3), -sp.Rational(1, 3), 1, 0],
            [0, 0, 0, 0, 1],
        ]
    )
    anisotropic_vector = np.asarray(
        [float(value) for value in exact_anisotropic_vector(mp)], dtype=float
    )
    q0 = regge.bloch_Q(np.zeros(4)).real
    checks.check(
        "exact-affine-metric-tangent-normal-decomposition",
        metric_map_exact.T * exact_basis_symbolic == sp.zeros(10, 5)
        and exact_basis_symbolic.T * exact_basis_symbolic == expected_gram
        and exact_basis_symbolic.rank() == 5
        and sp.Matrix.hstack(metric_map_exact, exact_basis_symbolic).rank() == 15
        and np.linalg.norm(basis.T @ basis - np.eye(5)) < 2.0e-14
        and np.linalg.norm(metric_map.T @ basis) < 2.0e-14
        and np.linalg.matrix_rank(np.column_stack((metric_map, basis)), tol=1.0e-10)
        == 15
        and np.allclose(
            eigenvalues[np.abs(eigenvalues) > 1.0e-8], [-48, -16, -16, -16]
        )
        and abs(float(anisotropic_vector @ anisotropic_vector) - 1.0) < 2.0e-15
        and np.linalg.norm(q0 @ anisotropic_vector + 16 * anisotropic_vector)
        < 5.0e-14,
        "ten metric tangents plus four massive normals and the nonlinear extra branch span all fifteen edge directions",
    )

    coordinate_permutations = tuple(permutations(range(4)))
    direction_index = {
        tuple(direction): index for index, direction in enumerate(regge.DIRS15)
    }
    exact_range_vector, exact_extra_vector = (
        sp.Matrix(vector) for vector in exact_symmetric_vectors(sp)
    )
    anisotropic_vectors = tuple(
        sp.Matrix(exact_anisotropic_vector(sp, index)) for index in range(4)
    )

    def permute_vertex(vertex, permutation) -> tuple[int, ...]:
        return tuple(int(vertex[permutation[index]]) for index in range(4))

    def canonical_vertices(vertices) -> tuple[tuple[int, ...], ...]:
        return tuple(sorted(tuple(int(entry) for entry in vertex) for vertex in vertices))

    triangle_by_vertices = {
        canonical_vertices(triangle): triangle for triangle in regge.TRI_CLASSES
    }

    def triangulation_preserved(permutation) -> bool:
        for triangle in regge.TRI_CLASSES:
            mapped_key = canonical_vertices(
                permute_vertex(vertex, permutation) for vertex in triangle
            )
            if mapped_key not in triangle_by_vertices:
                return False
            mapped_triangle = triangle_by_vertices[mapped_key]
            mapped_stars = {
                canonical_vertices(
                    permute_vertex(vertex, permutation) for vertex in simplex
                )
                for simplex in regge.STARS[triangle]
            }
            target_stars = {
                canonical_vertices(simplex)
                for simplex in regge.STARS[mapped_triangle]
            }
            if mapped_stars != target_stars:
                return False
        return True

    def coordinate_pullback(vector: sp.Matrix, permutation) -> sp.Matrix:
        return sp.Matrix(
            [
                vector[
                    direction_index[
                        tuple(direction[permutation[index]] for index in range(4))
                    ]
                ]
                for direction in regge.DIRS15
            ]
        )

    checks.check(
        "symmetric-subspace-invariance",
        len(coordinate_permutations) == 24
        and sum(anisotropic_vectors, sp.zeros(15, 1)) == sp.zeros(15, 1)
        and sp.Matrix.hstack(*anisotropic_vectors).rank() == 3
        and np.linalg.norm(q0 @ exact_basis_float[:, 0] + 48 * exact_basis_float[:, 0])
        < 5.0e-14
        and np.linalg.norm(q0 @ exact_basis_float[:, 1:4] + 16 * exact_basis_float[:, 1:4])
        < 8.0e-14
        and np.linalg.norm(q0 @ exact_basis_float[:, 4]) < 5.0e-14
        and all(
            triangulation_preserved(permutation)
            and
            coordinate_pullback(exact_range_vector, permutation)
            == exact_range_vector
            and coordinate_pullback(exact_extra_vector, permutation)
            == exact_extra_vector
            and all(
                coordinate_pullback(vector, permutation) in anisotropic_vectors
                for vector in anisotropic_vectors
            )
            for permutation in coordinate_permutations
        ),
        "all 24 coordinate permutations preserve the 50-hinge/240-incidence triangulation, fix the two symmetric normals, and permute four zero-sum anisotropic vectors spanning the standard three-dimensional sector",
    )

    a_root, u_root, root_jet = symmetric_root()
    root_residual = mp.norm(mp.matrix(root_jet.grad))
    inside, contraction, radius = krawczyk_certificate(a_root, u_root, root_jet)
    checks.check(
        "interval-certified-constrained-background",
        root_residual < mp.mpf("1e-48") and inside and contraction < 1.0e-3,
        f"a={mp.nstr(a_root, 16)}; u={mp.nstr(u_root, 16)}; radius={mp.nstr(radius, 3)}; Krawczyk contraction={contraction:.3e}",
    )

    background = [a_root, mp.mpf(0), mp.mpf(0), mp.mpf(0), u_root]
    background_jet = normal_action(background, basis)
    exact_background_jet = normal_action(background, exact_basis_numeric)
    normal_residual = mp.norm(mp.matrix(exact_background_jet.grad))
    full_interval_ok, symmetric_det_interval, anisotropic_interval = (
        full_normal_interval_certificate(a_root, u_root)
    )
    normal_hessian = np.asarray(
        [[float(entry) for entry in row] for row in background_jet.hess], dtype=float
    )
    normal_eigenvalues = np.linalg.eigvalsh(normal_hessian)
    checks.check(
        "full-five-normal-stationarity-and-nondegeneracy",
        normal_residual < mp.mpf("2e-14")
        and full_interval_ok
        and min(abs(normal_eigenvalues)) > 0.2
        and np.count_nonzero(normal_eigenvalues > 0) >= 1
        and np.count_nonzero(normal_eigenvalues < 0) >= 1,
        "normal Hessian eigenvalues="
        + np.array2string(normal_eigenvalues, precision=9, separator=",")
        + f"; interval det_2 upper={float(symmetric_det_interval.b):.6f}; anisotropic upper={float(anisotropic_interval.b):.6f}",
    )

    sources = reaction.exact_source_rows()
    coupling = sp.Rational(1, 100)
    branch_records = []
    for name, source in zip(("two-stream", "bundle-A", "bundle-B"), sources):
        coordinates, value, residual = newton_source_branch(
            exact_basis_numeric, background, source, coupling
        )
        source_inside, source_contraction, source_radius = (
            normal_krawczyk_certificate(
                coordinates,
                value,
                source,
                coupling,
            )
        )
        branch_records.append(
            (
                name,
                coordinates,
                value,
                residual,
                source_inside,
                source_contraction,
                source_radius,
            )
        )
    checks.check(
        "three-interval-certified-source-continuations",
        all(
            record[3] < mp.mpf("1e-38")
            and record[4]
            and record[5] < 5.0e-3
            for record in branch_records
        ),
        "; ".join(
            f"{name}: center=({','.join(mp.nstr(entry, 11) for entry in coordinates)}), residual={mp.nstr(residual, 4)}, radius={mp.nstr(source_radius, 2)}, contraction={source_contraction:.3e}"
            for (
                name,
                coordinates,
                _value,
                residual,
                _source_inside,
                source_contraction,
                source_radius,
            ) in branch_records
        ),
    )

    checks.check(
        "ten-channel-kkt-closure",
        all(record[4] for record in branch_records)
        and metric_map_exact.rank() == 10
        and sp.Matrix.hstack(metric_map_exact, exact_basis_symbolic).rank() == 15,
        "each complete equation residual lies in the ten-dimensional metric-reaction image; the eleventh reaction of the quadratic completion is replaced by native nonlinear response",
    )

    independent_errors = [
        abs(
            periodic_box_action_value(background, exact_basis_numeric)
            - float(exact_background_jet.value)
        ),
        abs(
            periodic_box_action_value(branch_records[-1][1], exact_basis_numeric)
            - float(branch_records[-1][2].value)
        ),
    ]
    independent_background_gradient = periodic_box_central_gradient(
        background,
        exact_basis_numeric,
        mp.mpf("2e-5"),
    )
    bundle_b_target = exact_source_target(sources[-1], coupling, mp)
    bundle_b_target_norm = mp.sqrt(
        sum(entry * entry for entry in bundle_b_target)
    )
    bundle_b_direction = [
        entry / bundle_b_target_norm for entry in bundle_b_target
    ]
    bundle_b_step = mp.mpf("2e-5")
    bundle_b_plus = [
        branch_records[-1][1][index]
        + bundle_b_step * bundle_b_direction[index]
        for index in range(5)
    ]
    bundle_b_minus = [
        branch_records[-1][1][index]
        - bundle_b_step * bundle_b_direction[index]
        for index in range(5)
    ]
    bundle_b_directional_derivative = (
        periodic_box_action_value(bundle_b_plus, exact_basis_numeric)
        - periodic_box_action_value(bundle_b_minus, exact_basis_numeric)
    ) / (2 * float(bundle_b_step))
    bundle_b_gradient_error = abs(
        bundle_b_directional_derivative - float(bundle_b_target_norm)
    )
    checks.check(
        "independent-periodic-box-action-reconstruction",
        max(independent_errors) < 2.0e-11
        and np.max(np.abs(independent_background_gradient)) < 2.0e-8
        and bundle_b_gradient_error < 2.0e-8,
        "background/bundle-B per-cell action errors="
        + np.array2string(np.asarray(independent_errors), precision=3, separator=",")
        + f"; background gradient max={np.max(np.abs(independent_background_gradient)):.3e}; bundle-B source-direction gradient error={bundle_b_gradient_error:.3e}",
    )

    checks.check(
        "theorem-source-surface",
        all(
            phrase in note_flat
            for phrase in (
                "interval Krawczyk",
                "ten affine constraints",
                "three declared source generators",
                "candidate amendment",
                "fixed TOE percentages remain unchanged",
            )
        ),
    )
    checks.check(
        "no-go-discipline-source-surface",
        all(f"N{index}" in note for index in range(1, 9))
        and "not a universal instability no-go" in note_flat
        and "curved and time-dependent" in note_flat,
    )
    checks.check(
        "canonical-axiom-nonmutation",
        all(
            phrase not in axiom_flat
            for phrase in (
                "ten affine fixed-metric constraints",
                "interval Krawczyk",
                "nonlinear Regge KKT continuation",
            )
        ),
    )

    print("per_element: checked all fifteen homogeneous edge directions through the ten-plus-five direct-sum decomposition")
    print("per_site: checked the full fifty-hinge, two-hundred-forty-incidence action per translation cell")
    print("per_mode: checked the compact k=0 five-normal nonlinear system and all ten affine metric reactions")
    print("per_block: checked one interval-certified background, its full normal Hessian, and all three declared source continuations")
    print("lattice_wide: checked the homogeneous periodic sector; curved, time-dependent, inhomogeneous, and open-boundary stability remain outside scope")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
