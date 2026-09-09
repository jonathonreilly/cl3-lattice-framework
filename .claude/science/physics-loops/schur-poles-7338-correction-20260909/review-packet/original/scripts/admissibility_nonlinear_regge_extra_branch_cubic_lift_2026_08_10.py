#!/usr/bin/env python3
"""Check the exact nonlinear lift of the homogeneous extra Regge branch.

The runner expands the actual four-dimensional Kuhn/Coxeter Regge action in
the exact number field Q(sqrt(2),sqrt(3)).  It proves the cubic and quartic
coefficients along the independent quadratic zero branch, reconstructs the
complete cubic metric/extra-branch normal form, and compares its leading
gradient image with the declared Block-15/16 compact source covectors.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import permutations
import json
from math import factorial
from pathlib import Path
import sys

import mpmath as mp
import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 240

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NONLINEAR_REGGE_EXTRA_BRANCH_CUBIC_LIFT_"
    "SOURCE_COMPATIBILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REACTION_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
PREMISE_REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
PRIMITIVE_PATHS = (
    ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_NONLINEAR_REGGE_EXTRA_BRANCH_CUBIC_LIFT_SOURCE_COMPATIBILITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_COMPACT_REGGE_HOMOGENEOUS_REACTION_RANK_KKT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
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


DEGREE = 3
ZERO_EXP = (0, 0)
K = sp.QQ.algebraic_field(sp.sqrt(2), sp.sqrt(3))

EXTRA = tuple(
    sp.sympify(value) / 8
    for value in (
        -sp.sqrt(2), -sp.sqrt(2), 0, -sp.sqrt(2), 0,
        0, sp.sqrt(6), -sp.sqrt(2), 0, 0,
        sp.sqrt(6), 0, sp.sqrt(6), sp.sqrt(6), -4 * sp.sqrt(2),
    )
)


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


def kval(value):
    try:
        return K.convert(value)
    except Exception:
        return K.from_sympy(sp.sympify(value))


def ksqrt(value):
    return K.from_sympy(sp.sqrt(K.to_sympy(value)))


@dataclass(frozen=True)
class Jet:
    coeffs: dict[tuple[int, int], object]

    def __post_init__(self) -> None:
        clean = {}
        for exp, value in self.coeffs.items():
            converted = kval(value)
            if sum(exp) <= DEGREE and converted != K.zero:
                clean[exp] = converted
        object.__setattr__(self, "coeffs", clean)

    @classmethod
    def constant(cls, value) -> "Jet":
        value_k = kval(value)
        return cls({ZERO_EXP: value_k} if value_k != K.zero else {})

    @classmethod
    def monomial(cls, exp: tuple[int, int], value) -> "Jet":
        value_k = kval(value)
        return cls({exp: value_k} if value_k != K.zero else {})

    def coefficient(self, exp: tuple[int, int]):
        return self.coeffs.get(exp, K.zero)

    @property
    def c0(self):
        return self.coefficient(ZERO_EXP)

    def __add__(self, other) -> "Jet":
        rhs = as_jet(other)
        out = dict(self.coeffs)
        for exp, value in rhs.coeffs.items():
            out[exp] = out.get(exp, K.zero) + value
            if out[exp] == K.zero:
                del out[exp]
        return Jet(out)

    __radd__ = __add__

    def __neg__(self) -> "Jet":
        return Jet({exp: -value for exp, value in self.coeffs.items()})

    def __sub__(self, other) -> "Jet":
        return self + (-as_jet(other))

    def __rsub__(self, other) -> "Jet":
        return as_jet(other) - self

    def __mul__(self, other) -> "Jet":
        rhs = as_jet(other)
        out: dict[tuple[int, int], object] = {}
        for left_exp, left_value in self.coeffs.items():
            for right_exp, right_value in rhs.coeffs.items():
                exp = (left_exp[0] + right_exp[0], left_exp[1] + right_exp[1])
                if sum(exp) > DEGREE:
                    continue
                out[exp] = out.get(exp, K.zero) + left_value * right_value
                if out[exp] == K.zero:
                    del out[exp]
        return Jet(out)

    __rmul__ = __mul__

    def __truediv__(self, other) -> "Jet":
        return self * jet_inverse(as_jet(other))

    def __rtruediv__(self, other) -> "Jet":
        return as_jet(other) * jet_inverse(self)

    def __pow__(self, exponent: int) -> "Jet":
        if exponent < 0:
            return jet_inverse(self ** (-exponent))
        result = Jet.constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result


def as_jet(value) -> Jet:
    return value if isinstance(value, Jet) else Jet.constant(value)


def jet_inverse(value: Jet) -> Jet:
    if value.c0 == K.zero:
        raise ZeroDivisionError("jet has zero constant coefficient")
    residual = (value - Jet.constant(value.c0)) * (K.one / value.c0)
    series = Jet.constant(1)
    power = Jet.constant(1)
    for order in range(1, DEGREE + 1):
        power = power * residual
        series += (-1 if order % 2 else 1) * power
    return series * (K.one / value.c0)


def jet_sqrt(value: Jet) -> Jet:
    if value.c0 == K.zero:
        raise ZeroDivisionError("sqrt jet has zero constant coefficient")
    residual = (value - Jet.constant(value.c0)) * (K.one / value.c0)
    series = Jet.constant(1)
    power = Jet.constant(1)
    for order in range(1, DEGREE + 1):
        power = power * residual
        series += kval(sp.binomial(sp.Rational(1, 2), order)) * power
    return ksqrt(value.c0) * series


def jet_acos_delta(value: Jet) -> Jet:
    """acos(value)-acos(value.c0), through the configured total degree."""
    x = value.c0
    residual = value - Jet.constant(x)
    sine = ksqrt(K.one - x * x)
    first = -K.one / sine
    second = -x / (sine ** 3)
    third = -(K.one + kval(2) * x * x) / (sine ** 5)
    result = (
        first * residual
        + (second / kval(2)) * residual ** 2
        + (third / kval(6)) * residual ** 3
    )
    if DEGREE >= 4:
        fourth = -kval(3) * x * (kval(3) + kval(2) * x * x) / (sine ** 7)
        result += (fourth / kval(24)) * residual ** 4
    return result


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


def action_jet(probe_direction: tuple[object, ...]) -> Jet:
    lengths = []
    for index, direction in enumerate(regge.DIRS15):
        ell0 = sp.sqrt(sum(direction))
        lengths.append(
            Jet.constant(ell0)
            + Jet.monomial((1, 0), EXTRA[index])
            + Jet.monomial((0, 1), probe_direction[index])
        )
    squared = tuple(length * length for length in lengths)

    @lru_cache(maxsize=None)
    def area(classes: tuple[int, int, int]) -> Jet:
        qa, qb, qc = (squared[index] for index in classes)
        area_squared = (
            2 * qa * qb + 2 * qa * qc + 2 * qb * qc
            - qa * qa - qb * qb - qc * qc
        ) / 16
        return jet_sqrt(area_squared)

    @lru_cache(maxsize=None)
    def angle_delta(missing: tuple[int, int], classes: tuple[int, ...]) -> Jet:
        q = {pair: squared[classes[index]] for index, pair in enumerate(regge.PAIRS5)}

        def qq(i: int, j: int) -> Jet:
            return q[(min(i, j), max(i, j))]

        def dot(i: int, j: int, base: int) -> Jet:
            if i == j:
                return qq(base, i)
            return (qq(base, i) + qq(base, j) - qq(i, j)) / 2

        a, b = missing
        p, qv, rv = [vertex for vertex in range(5) if vertex not in missing]
        g11, g12, g22 = dot(qv, qv, p), dot(qv, rv, p), dot(rv, rv, p)
        determinant = g11 * g22 - g12 * g12

        def projected_pair(left: int, right: int) -> Jet:
            li1, li2 = dot(qv, left, p), dot(rv, left, p)
            ri1, ri2 = dot(qv, right, p), dot(rv, right, p)
            projection = (
                g22 * li1 * ri1
                - g12 * (li1 * ri2 + li2 * ri1)
                + g11 * li2 * ri2
            ) / determinant
            return dot(left, right, p) - projection

        nab = projected_pair(a, b)
        naa = projected_pair(a, a)
        nbb = projected_pair(b, b)
        cosine = nab / jet_sqrt(naa * nbb)
        return jet_acos_delta(cosine)

    total = Jet.constant(0)
    for triangle in regge.TRI_CLASSES:
        area_classes = triangle_edge_classes(triangle)
        deficit = Jet.constant(0)
        for simplex in regge.STARS[triangle]:
            local = {vertex: index for index, vertex in enumerate(simplex)}
            hinge = sorted(local[vertex] for vertex in triangle)
            missing = tuple(sorted(index for index in range(5) if index not in hinge))
            deficit -= angle_delta(missing, simplex_edge_classes(simplex))
        total += area(area_classes) * deficit
    return total


def exact_metric_columns() -> tuple[tuple[object, ...], ...]:
    columns = []
    for left, right in regge.HCOMPS:
        column = []
        for direction in regge.DIRS15:
            length = sp.sqrt(sum(direction))
            if left == right:
                column.append(sp.Rational(direction[left], 2) / length)
            else:
                column.append(sp.Rational(direction[left] * direction[right], 1) / length)
        columns.append(tuple(column))
    return tuple(columns)


def show(value) -> str:
    return str(sp.simplify(K.to_sympy(value)))


def coordinate_permutation_certificate() -> tuple[bool, str]:
    coordinate_permutations = tuple(permutations(range(4)))

    def permute_vector(vector, permutation):
        out = [0, 0, 0, 0]
        for source, target in enumerate(permutation):
            out[target] = vector[source]
        return tuple(out)

    base_simplices = {
        tuple(tuple(vertex) for vertex in simplex)
        for simplex in regge.cell_simplices((0, 0, 0, 0))
    }
    triangles = set(regge.TRI_CLASSES)
    extra_by_direction = dict(zip(regge.DIRS15, EXTRA))
    for permutation in coordinate_permutations:
        mapped_simplices = {
            tuple(permute_vector(vertex, permutation) for vertex in simplex)
            for simplex in base_simplices
        }
        mapped_triangles = {
            tuple(permute_vector(vertex, permutation) for vertex in triangle)
            for triangle in triangles
        }
        if mapped_simplices != base_simplices or mapped_triangles != triangles:
            return False, "coordinate permutation failed to preserve the Kuhn complex"
        if any(
            sp.simplify(extra_by_direction[permute_vector(direction, permutation)] - value)
            != 0
            for direction, value in extra_by_direction.items()
        ):
            return False, "coordinate permutation failed to preserve the extra branch"
    return True, "24 coordinate permutations preserve the complex, hinge classes, and g"


def metric_pair_orbits() -> tuple[set[tuple[int, int]], ...]:
    component_index = {component: index for index, component in enumerate(regge.HCOMPS)}

    def mapped_component(index: int, permutation: tuple[int, ...]) -> int:
        left, right = regge.HCOMPS[index]
        return component_index[tuple(sorted((permutation[left], permutation[right])))]

    all_pairs = {(left, right) for left in range(10) for right in range(left, 10)}
    unseen = set(all_pairs)
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = set()
        for permutation in permutations(range(4)):
            mapped = tuple(
                sorted(
                    (
                        mapped_component(seed[0], permutation),
                        mapped_component(seed[1], permutation),
                    )
                )
            )
            orbit.add(mapped)
        orbits.append(orbit)
        unseen -= orbit
    return tuple(orbits)


def uniform_action_mp(t_value: mp.mpf) -> mp.mpf:
    """Independent high-precision homogeneous action per translation cell."""
    extra = [mp.mpf(str(sp.N(value, mp.mp.dps + 10))) for value in EXTRA]
    lengths = [
        mp.sqrt(sum(direction)) + t_value * extra[index]
        for index, direction in enumerate(regge.DIRS15)
    ]
    squared = [length * length for length in lengths]
    area_cache = {}
    angle_cache = {}

    def area(classes):
        if classes not in area_cache:
            qa, qb, qc = (squared[index] for index in classes)
            area_cache[classes] = mp.sqrt(
                (
                    2 * qa * qb + 2 * qa * qc + 2 * qb * qc
                    - qa * qa - qb * qb - qc * qc
                )
                / 16
            )
        return area_cache[classes]

    def angle(missing, classes):
        key = (missing, classes)
        if key in angle_cache:
            return angle_cache[key]
        q = {pair: squared[classes[index]] for index, pair in enumerate(regge.PAIRS5)}

        def qq(i, j):
            return q[(min(i, j), max(i, j))]

        def dot(i, j, base):
            if i == j:
                return qq(base, i)
            return (qq(base, i) + qq(base, j) - qq(i, j)) / 2

        a, b = missing
        p, qv, rv = [vertex for vertex in range(5) if vertex not in missing]
        g11, g12, g22 = dot(qv, qv, p), dot(qv, rv, p), dot(rv, rv, p)
        determinant = g11 * g22 - g12 * g12

        def projected_pair(left, right):
            li1, li2 = dot(qv, left, p), dot(rv, left, p)
            ri1, ri2 = dot(qv, right, p), dot(rv, right, p)
            return dot(left, right, p) - (
                g22 * li1 * ri1
                - g12 * (li1 * ri2 + li2 * ri1)
                + g11 * li2 * ri2
            ) / determinant

        nab = projected_pair(a, b)
        naa = projected_pair(a, a)
        nbb = projected_pair(b, b)
        angle_cache[key] = mp.acos(nab / mp.sqrt(naa * nbb))
        return angle_cache[key]

    total = mp.mpf("0")
    for triangle in regge.TRI_CLASSES:
        deficit = 2 * mp.pi
        for simplex in regge.STARS[triangle]:
            local = {vertex: index for index, vertex in enumerate(simplex)}
            hinge = sorted(local[vertex] for vertex in triangle)
            missing = tuple(sorted(index for index in range(5) if index not in hinge))
            deficit -= angle(missing, simplex_edge_classes(simplex))
        total += area(triangle_edge_classes(triangle)) * deficit
    return total


def path_gram_data():
    t = sp.Symbol("t", real=True)
    extra_by_weight = {
        0: sp.Integer(0),
        1: -sp.sqrt(2) / 8,
        2: sp.Integer(0),
        3: sp.sqrt(6) / 8,
        4: -sp.sqrt(2) / 2,
    }
    length = {
        weight: sp.sqrt(weight) + t * extra_by_weight[weight]
        for weight in range(5)
    }
    gram = sp.Matrix(
        4,
        4,
        lambda left, right: sp.expand(
            (
                length[left + 1] ** 2
                + length[right + 1] ** 2
                - length[abs(left - right)] ** 2
            )
            / 2
        ),
    )
    minors = tuple(sp.factor(gram[:size, :size].det(), extension=sp.sqrt(2)) for size in range(1, 5))
    roots = sorted(
        float(sp.re(root))
        for root in sp.nroots(minors[-1])
        if abs(float(sp.im(root))) < 1.0e-10
    )
    lower = max(root for root in roots if root < 0)
    upper = min(root for root in roots if root > 0)
    return t, minors, lower, upper


def main() -> int:
    global DEGREE
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    reaction_note = REACTION_NOTE_PATH.read_text(encoding="utf-8")
    regge_note = REGGE_NOTE_PATH.read_text(encoding="utf-8")
    premise_registry = json.loads(PREMISE_REGISTRY_PATH.read_text(encoding="utf-8"))
    primitive_notes = tuple(
        " ".join(path.read_text(encoding="utf-8").split())
        for path in PRIMITIVE_PATHS
    )
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())

    print("external_scientific_inputs: none; exact Taylor algebra is performed on the supplied actual Regge action")
    print("package_local_integrity_reads: current axioms, Block 17, and the retained 4D Kuhn/Coxeter carrier are source-bound")
    print("analytic_boundary: homogeneous action coefficients and the complete cubic null-sector polynomial are exact in Q(sqrt(2),sqrt(3))")
    print("physical_boundary: full nonlinear source solutions, action selection, boundary, coupling, Lorentzian dynamics, and realized history remain open")

    checks.check(
        "source-current-axiom-boundary",
        "Admissibility is not a dynamics axiom" in axiom_flat
        and "source/action and physical-observable identification" in axiom_flat,
    )
    checks.check(
        "source-parent-boundary",
        "dim K = 11 = 10 constant-metric modes + 1 nonmetric flat branch" in reaction_note
        and "one exactly flat branch" in regge_note,
    )
    registered_nodes = {
        node_id: node["current_path"]
        for node_id, node in premise_registry["nodes"].items()
    }
    checks.check(
        "source-approved-primitive-boundary",
        registered_nodes.get("scale_reference_primitive")
        == "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"
        and registered_nodes.get("kinetic_isotropy_primitive")
        == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
        and registered_nodes.get("realized_state_primitive")
        == "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
        and "units conversion, not a physics axiom" in primitive_notes[0]
        and "It is not a fourth spatial dimension, not a new dynamics" in primitive_notes[1]
        and "It does not supply a state, state-selection rule" in primitive_notes[2],
        "the three approved primitives supply no geometry action, source law, constraint, boundary, coupling, or nonlinear solution",
    )

    columns = exact_metric_columns()
    metric_matrix = sp.Matrix(15, 10, lambda row, column: columns[column][row])
    extra_vector = sp.Matrix(EXTRA)
    symmetry_ok, symmetry_detail = coordinate_permutation_certificate()
    checks.check("exact-coordinate-symmetry", symmetry_ok, symmetry_detail)
    checks.check(
        "exact-extra-vector-geometry",
        sp.simplify(extra_vector.dot(extra_vector)) == 1
        and metric_matrix.T * extra_vector == sp.zeros(10, 1),
        "g is unit and exactly orthogonal to all ten constant-metric tangents",
    )

    DEGREE = 3
    zero_direction = tuple(sp.Integer(0) for _ in regge.DIRS15)
    diagonal_jet = action_jet(columns[0])
    shear_jet = action_jet(columns[4])
    b_diagonal = diagonal_jet.coefficient((2, 1))
    b_shear = shear_jet.coefficient((2, 1))
    q_diagonal = diagonal_jet.coefficient((1, 2))
    q_shear = shear_jet.coefficient((1, 2))

    orbits = metric_pair_orbits()
    q_orbit_values = []
    for orbit in orbits:
        left, right = min(orbit)
        if left == right:
            value = q_diagonal if left < 4 else q_shear
        else:
            summed = tuple(columns[left][row] + columns[right][row] for row in range(15))
            sum_value = action_jet(summed).coefficient((1, 2))
            left_diag = q_diagonal if left < 4 else q_shear
            right_diag = q_diagonal if right < 4 else q_shear
            value = (sum_value - left_diag - right_diag) / kval(2)
        q_orbit_values.append(value)
    checks.check(
        "exact-cubic-metric-polarization",
        [len(orbit) for orbit in orbits] == [4, 6, 12, 12, 6, 12, 3]
        and b_diagonal == K.zero
        and b_shear == kval(8)
        and all(value == K.zero for value in q_orbit_values),
        "b=(0,0,0,0,8,8,8,8,8,8); all seven S4 orbits of the symmetric u*x*x tensor vanish",
    )

    extra_hessian_orbits = []
    for weight in range(1, 5):
        index = next(
            position
            for position, direction in enumerate(regge.DIRS15)
            if sum(direction) == weight
        )
        probe = tuple(sp.Integer(position == index) for position in range(15))
        extra_hessian_orbits.append(action_jet(probe).coefficient((1, 1)))
    checks.check(
        "exact-extra-quadratic-nullity",
        all(value == K.zero for value in extra_hessian_orbits),
        "one exact Hessian pairing vanishes in each of the four edge-weight orbits",
    )

    DEGREE = 4
    pure_extra = action_jet(zero_direction)
    directional_coefficients = [pure_extra.coefficient((order, 0)) for order in range(5)]
    checks.check(
        "exact-nonlinear-extra-branch-lift",
        directional_coefficients
        == [K.zero, K.zero, K.zero, kval(-4 * sp.sqrt(2)), kval(sp.Rational(4023, 256))],
        "S_R(tg)=-4*sqrt(2)*t^3+(4023/256)*t^4+O(t^5) per translation cell",
    )

    b_vector = sp.Matrix([0, 0, 0, 0, 8, 8, 8, 8, 8, 8])
    two_stream, bundle_a, bundle_b = reaction.exact_source_rows()
    sources = two_stream.row_join(bundle_a).row_join(bundle_b)
    metric_covectors = sp.simplify(metric_matrix.T * sources)
    extra_covectors = sp.simplify(extra_vector.T * sources)
    expected_metric_covectors = sp.Matrix(
        [
            [sp.sqrt(2) / 2, 1, 1],
            [0, 1, 1],
            [0, 1, 1],
            [1 + sp.sqrt(2) / 2, 3, 3],
            [0, 0, 1],
            [0, 0, 1],
            [sp.sqrt(2), 2, 2],
            [0, 0, 1],
            [0, 2, 2],
            [0, 2, 2],
        ]
    )
    checks.check(
        "exact-declared-source-null-covectors",
        metric_covectors == expected_metric_covectors
        and extra_covectors == sp.Matrix([[-sp.sqrt(2) / 4, 0, 3 * sp.sqrt(2) / 4]]),
    )
    source_span_ranks = [
        b_vector.row_join(metric_covectors[:, column]).rank() for column in range(3)
    ]
    checks.check(
        "leading-cubic-source-image-boundary",
        source_span_ranks == [2, 2, 2],
        "the cubic metric-gradient image is span(b); each declared metric source covector is nonparallel",
    )

    mp.mp.dps = 70
    independent_coefficients = mp.taylor(uniform_action_mp, mp.mpf("0"), 4)
    independent_errors = (
        abs(independent_coefficients[0]),
        abs(independent_coefficients[1]),
        abs(independent_coefficients[2]),
        abs(independent_coefficients[3] + 4 * mp.sqrt(2)),
        abs(independent_coefficients[4] - mp.mpf(4023) / 256),
    )
    checks.check(
        "independent-high-precision-action-reconstruction",
        max(independent_errors) < mp.mpf("1e-55"),
        "max coefficient error=" + mp.nstr(max(independent_errors), 8),
    )
    t_sample = mp.mpf("0.02")
    uniform_sample = uniform_action_mp(t_sample)
    box_sample = regge.box_action(
        3,
        lambda edge_class, anchor: float(t_sample) * float(EXTRA[edge_class]),
    ) / (3 ** 4)
    checks.check(
        "actual-periodic-box-action-match",
        abs(float(uniform_sample) - box_sample) < 8.0e-13
        and uniform_action_mp(-t_sample) > 0
        and uniform_sample < 0,
        f"S_cell(-0.02)={float(uniform_action_mp(-t_sample)):.12e}; S_cell(+0.02)={float(uniform_sample):.12e}",
    )

    t_symbol, gram_minors, lower_boundary, upper_boundary = path_gram_data()
    sample_points = (-0.4, 0.0, 0.3)
    interior_positive = all(
        float(minor.subs(t_symbol, value)) > 0
        for value in sample_points
        for minor in gram_minors
    )
    checks.check(
        "nondegenerate-simplex-domain",
        interior_positive
        and abs(lower_boundary - (-0.458860264423508)) < 2.0e-12
        and abs(upper_boundary - 0.340150409120162) < 2.0e-12,
        f"connected positive-Gram interval around zero is approximately ({lower_boundary:.12f},{upper_boundary:.12f})",
    )

    checks.check(
        "theorem-source-surface",
        all(
            phrase in note_flat
            for phrase in (
                "-4sqrt(2)",
                "4023/256",
                "complete cubic null-sector polynomial",
                "candidate amendment",
                "fixed TOE percentages remain unchanged",
            )
        ),
    )
    checks.check(
        "no-go-discipline-source-surface",
        all(f"N{index}" in note for index in range(1, 9))
        and "No full nonlinear source no-go" in note_flat
        and "higher-order mixed branch" in note_flat,
    )
    checks.check(
        "canonical-axiom-nonmutation",
        all(
            phrase not in axiom_flat
            for phrase in (
                "complete cubic null-sector polynomial",
                "nonlinear extra-branch lift certificate",
                "full nonlinear source compatibility",
            )
        ),
    )

    print("per_element: checked exact Taylor coefficients for all four edge-weight symmetry orbits and both metric-component orbits")
    print("per_site: checked one complete homogeneous translation cell with all fifty triangle classes and all two hundred forty dihedral contributions")
    print("per_mode: checked the compact k=0 eleven-dimensional null sector, its ten metric coordinates, and its independent extra coordinate")
    print("per_block: checked the positive cubic/quartic lift, complete cubic normal form, declared-source comparison, and candidate-axiom boundary")
    print("lattice_wide: checked an actual periodic L=3 box against the uniform-cell action; inhomogeneous and open-boundary nonlinear solutions were not executed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
