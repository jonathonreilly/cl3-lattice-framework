#!/usr/bin/env python3
"""Corrected finite kernel statements for Cycle 884.

This runner supplies its own finite zero-exterior Dirichlet problem.  It does
not identify that problem with the framework's physical response law.  A
separate direct symbolic route and the independent helper both check the
nonzero radial massless-ansatz obstruction.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/GBS2_KERNEL_WINDOW_ANATOMY_CYCLE884_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle884_gbs2_independent_check_2026_07_28.py",
)

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

import frontier_cycle884_gbs2_independent_check_2026_07_28 as independent

ROOT = Path(__file__).resolve().parents[1]
NEIGHBOURS = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)


def orbit_class(site):
    return tuple(sorted((abs(value) for value in site), reverse=True))


def solve_dirichlet_cube(radius, mu_squared=F(0)):
    """Solve (6 I - adjacency + mu_squared I) G = delta_0 exactly."""
    classes = [
        (a, b, c)
        for a in range(radius + 1)
        for b in range(a + 1)
        for c in range(b + 1)
    ]
    index = {site: position for position, site in enumerate(classes)}
    size = len(classes)
    matrix = [[F(0)] * (size + 1) for _ in range(size)]
    for site in classes:
        row = index[site]
        matrix[row][row] += F(6) + mu_squared
        for edge in NEIGHBOURS:
            neighbour = tuple(site[i] + edge[i] for i in range(3))
            if max(abs(value) for value in neighbour) <= radius:
                matrix[row][index[orbit_class(neighbour)]] -= F(1)
        matrix[row][size] = F(1) if site == (0, 0, 0) else F(0)

    for column in range(size):
        pivot = next((row for row in range(column, size)
                      if matrix[row][column] != 0), None)
        if pivot is None:
            return None, False
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        pivot_value = matrix[column][column]
        matrix[column] = [value / pivot_value for value in matrix[column]]
        for row in range(size):
            if row == column or matrix[row][column] == 0:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                matrix[row][j] - factor * matrix[column][j]
                for j in range(size + 1)
            ]
    return {site: matrix[index[site]][size] for site in classes}, True


def laplacian_equation_residual(solution, radius, site, mu_squared=F(0)):
    value = (F(6) + mu_squared) * solution[site]
    for edge in NEIGHBOURS:
        neighbour = tuple(site[i] + edge[i] for i in range(3))
        if max(abs(entry) for entry in neighbour) <= radius:
            value -= solution[orbit_class(neighbour)]
    target = F(1) if site == (0, 0, 0) else F(0)
    return value - target


def finite_dirichlet_certificate():
    rows = []
    largest = None
    for radius in (2, 3, 4):
        solution, unique = solve_dirichlet_cube(radius)
        assert solution is not None
        residuals = [
            laplacian_equation_residual(solution, radius, site)
            for site in solution
        ]
        step = solution[(0, 0, 0)] - solution[(1, 0, 0)]
        rows.append({
            "radius": radius,
            "unknown_orbit_classes": len(solution),
            "exact_elimination_found_every_pivot": unique,
            "all_equation_residuals_zero": all(value == 0 for value in residuals),
            "G0_minus_Ge1": str(step),
            "G0_minus_Ge1_equals_one_sixth": step == F(1, 6),
            "all_finite_cube_values_positive": all(value > 0 for value in solution.values()),
        })
        largest = solution
    anisotropy = largest[(3, 0, 0)] - largest[(2, 2, 1)]
    return {
        "definition": (
            "On Lambda_R={x in Z^3: ||x||_infinity<=R}, solve "
            "(6I-adjacency)G_R=delta_0 with G_R=0 outside Lambda_R."
        ),
        "rows": rows,
        "radius_four_equal_euclidean_radius_difference_G300_minus_G221": str(anisotropy),
        "radius_four_model_is_not_euclidean_radial": anisotropy != 0,
        "scope": (
            "finite zero-exterior boundary problems only; no infinite-volume "
            "existence, convergence, decay, or physical Poisson selection is inferred"
        ),
    }


def sympy_radial_obstruction():
    epsilon = sp.symbols("epsilon")
    rows, norms = [], []
    for axis, radicand in ((1, 2), (2, 5)):
        rational_part = (
            1 / (epsilon + axis - 1)
            + 1 / (epsilon + axis + 1)
            - 6 / (epsilon + axis)
        )
        rational_numerator, rational_denominator = sp.cancel(
            rational_part
        ).as_numer_denom()
        U = sp.Poly(sp.expand(rational_numerator * epsilon
                              + 4 * rational_denominator), epsilon, domain=sp.QQ)
        V = sp.Poly(rational_numerator, epsilon, domain=sp.QQ)
        common = sp.gcd(U, V).monic()
        reduced_u = sp.exquo(U, common)
        reduced_v = sp.exquo(V, common)
        norm = sp.Poly(reduced_u.as_expr() ** 2
                       - radicand * reduced_v.as_expr() ** 2,
                       epsilon, domain=sp.QQ).monic()
        norms.append(norm)
        rows.append({
            "site": [axis, 0, 0],
            "quadratic_field": f"Q(sqrt({radicand}))",
            "cancelled_factor": str(common.as_expr()),
            "reduced_norm_degree": norm.degree(),
            "reduced_norm_coefficients_high_to_low": [str(x) for x in norm.all_coeffs()],
        })
    common_norm = sp.gcd(norms[0], norms[1]).monic()
    return {
        "route": "direct SymPy construction from the two displayed residuals",
        "site_rows": rows,
        "common_reduced_norm_gcd": str(common_norm.as_expr()),
        "common_reduced_norm_gcd_is_one": common_norm.as_expr() == 1,
        "logical_scope": (
            "For A!=0 and epsilon outside {0,-1,-2,-sqrt(2),-3,-sqrt(5)}, "
            "simultaneous discrete harmonicity at the two axis sites is impossible."
        ),
    }


def build_certificate():
    memo = (ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8")
    normalized_memo = " ".join(memo.split())
    helper = independent.build_certificate()
    finite = finite_dirichlet_certificate()
    radial = sympy_radial_obstruction()
    checks = {
        "current_memo_denies_dynamics_selection":
            "does not choose a Hamiltonian or transfer operator" in normalized_memo,
        "finite_cube_elimination_found_every_pivot": all(
            row["exact_elimination_found_every_pivot"] for row in finite["rows"]),
        "finite_cube_equations_exact": all(
            row["all_equation_residuals_zero"] for row in finite["rows"]),
        "finite_cube_identity_exact": all(
            row["G0_minus_Ge1_equals_one_sixth"] for row in finite["rows"]),
        "finite_cube_values_positive": all(
            row["all_finite_cube_values_positive"] for row in finite["rows"]),
        "finite_cube_nonradial_example": finite["radius_four_model_is_not_euclidean_radial"],
        "primary_radial_norm_gcd_is_one": radial["common_reduced_norm_gcd_is_one"],
        "independent_radial_norm_gcd_is_one":
            helper["radial_massless_obstruction"]["common_reduced_norm_gcd_is_one"],
        "conditional_range_one_invariant_dimension_is_two":
            helper["supplied_range_one_stencil"]
            ["invariant_coefficient_space_dimension"] == 2,
        "independent_scope_counterexamples_pass": helper["all_checks_pass"],
    }
    return {
        "claim_type": "bounded_theorem",
        "input_sha256": {
            path: sha256((ROOT / path).read_bytes()).hexdigest()
            for path in AUDIT_INPUT_PATHS
        },
        "finite_dirichlet_model": finite,
        "nonzero_radial_massless_ansatz_obstruction": radial,
        "independent_confirmation": {
            "radial_massless_obstruction": helper["radial_massless_obstruction"],
            "supplied_range_one_stencil": helper["supplied_range_one_stencil"],
            "implication_counterexamples": helper["implication_counterexamples"],
        },
        "withdrawn_historical_inferences": [
            "Record finite additivity as current axiom content",
            "finite additivity collapses arbitrary shell weights to an annulus",
            "locality, linearity and cubic covariance select a nearest-neighbour inverse",
            "an exact lattice dilation law or p=1 forcing",
            "positivity selects the physical TOWARD sign",
            "finite Dirichlet pivots prove an infinite decaying Green function",
            "chart residuals or stabilizer dimension as complete physical counts",
        ],
        "checks": checks,
        "all_checks_pass": all(checks.values()),
    }


def main():
    payload = build_certificate()
    print(json.dumps(payload, indent=2, sort_keys=True))
    passed = sum(bool(value) for value in payload["checks"].values())
    failed = len(payload["checks"]) - passed
    for name, value in payload["checks"].items():
        print(f"{'PASS' if value else 'FAIL'} {name}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
