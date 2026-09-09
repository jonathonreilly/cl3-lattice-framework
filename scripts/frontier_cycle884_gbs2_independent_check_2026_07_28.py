#!/usr/bin/env python3
"""Independent exact checks for the corrected Cycle-884 kernel slice.

The checks are deliberately finite and premise-light.  They establish a
two-site obstruction for a nonzero radial massless ansatz and give explicit
counterexamples to two implications asserted by the historical runner.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/GBS2_KERNEL_WINDOW_ANATOMY_CYCLE884_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def determinant(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_cubic_rotations():
    matrices = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(tuple(
                signs[row] if column == permutation[row] else 0
                for column in range(3)
            ) for row in range(3))
            if determinant(matrix) == 1:
                matrices.append(matrix)
    return matrices


def rotate(matrix, site):
    return tuple(sum(matrix[row][column] * site[column] for column in range(3))
                 for row in range(3))


def range_one_stencil_certificate():
    rotations = proper_cubic_rotations()
    support = ((0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0),
               (0, -1, 0), (0, 0, 1), (0, 0, -1))
    unseen, orbits = set(support), []
    while unseen:
        representative = min(unseen)
        orbit = {rotate(matrix, representative) for matrix in rotations}
        orbits.append(sorted(orbit))
        unseen -= orbit
    return {
        "explicitly_supplied_support": "{0,+/-e1,+/-e2,+/-e3}",
        "proper_cubic_rotation_count": len(rotations),
        "support_orbit_sizes": sorted(len(orbit) for orbit in orbits),
        "invariant_coefficient_space_dimension": len(orbits),
        "family": "one centre coefficient and one common neighbour coefficient",
        "scope": (
            "conditional on this supplied seven-point support; covariance does "
            "not select either coefficient, an inverse, or a physical response law"
        ),
    }


def trim(poly):
    out = list(poly)
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(a, b):
    n = max(len(a), len(b))
    return trim(tuple(
        (a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
        for i in range(n)
    ))


def scale(a, factor):
    return trim(tuple(factor * value for value in a))


def sub(a, b):
    return add(a, scale(b, F(-1)))


def mul(a, b):
    if not a or not b:
        return ()
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(tuple(out))


def degree(poly):
    return len(poly) - 1 if poly else -1


def monic(poly):
    return scale(poly, F(1) / poly[-1]) if poly else poly


def remainder(a, b):
    out = list(trim(a))
    while out and degree(tuple(out)) >= degree(b):
        shift = degree(tuple(out)) - degree(b)
        factor = out[-1] / b[-1]
        for index, coefficient in enumerate(b):
            out[shift + index] -= factor * coefficient
        out = list(trim(tuple(out)))
    return trim(tuple(out))


def gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, remainder(a, b)
    return monic(a)


def divide_exact(a, b):
    quotient = [F(0)] * max(0, degree(a) - degree(b) + 1)
    residual = list(trim(a))
    while residual and degree(tuple(residual)) >= degree(b):
        shift = degree(tuple(residual)) - degree(b)
        factor = residual[-1] / b[-1]
        quotient[shift] += factor
        for index, coefficient in enumerate(b):
            residual[shift + index] -= factor * coefficient
        residual = list(trim(tuple(residual)))
    assert not trim(tuple(residual))
    return trim(tuple(quotient))


def site_residual(axis):
    """Return U,V,W,D for R=(U+V sqrt(D))/W at (axis,0,0)."""
    D = axis * axis + 1
    terms = (
        (F(1), F(axis - 1), F(0)),
        (F(1), F(axis + 1), F(0)),
        (F(4), F(0), F(1)),
        (F(-6), F(axis), F(0)),
    )
    U, V, W = (), (), (F(1),)
    for coefficient, rational_part, radical_part in terms:
        t_plus_a = (rational_part, F(1))
        numerator_u = scale(t_plus_a, coefficient)
        numerator_v = (-coefficient * radical_part,)
        denominator = sub(mul(t_plus_a, t_plus_a),
                          (radical_part * radical_part * D,))
        U, V, W = (
            add(mul(U, denominator), mul(numerator_u, W)),
            add(mul(V, denominator), mul(numerator_v, W)),
            mul(W, denominator),
        )
    return U, V, W, D


def quadratic_route_certificate():
    rows, norms = [], []
    poles = {
        1: ["0", "-1", "-2", "-sqrt(2)"],
        2: ["-1", "-2", "-3", "-sqrt(5)"],
    }
    for axis in (1, 2):
        U, V, W, D = site_residual(axis)
        common = gcd(U, V)
        reduced_u = divide_exact(U, common)
        reduced_v = divide_exact(V, common)
        norm = monic(sub(mul(reduced_u, reduced_u),
                         scale(mul(reduced_v, reduced_v), F(D))))
        norms.append(norm)
        rows.append({
            "site": [axis, 0, 0],
            "quadratic_field": f"Q(sqrt({D}))",
            "cancelled_factor_coefficients_low_to_high": [str(x) for x in common],
            "cancelled_factor_divides_cleared_denominator": not remainder(W, common),
            "reduced_norm_degree": degree(norm),
            "reduced_norm_coefficients_low_to_high": [str(x) for x in norm],
            "undefined_epsilon_values": poles[axis],
        })
    common_norm = gcd(norms[0], norms[1])
    return {
        "ansatz": "f_epsilon(x)=A/(|x|+epsilon)",
        "domain": "A != 0 and epsilon avoids every listed denominator pole",
        "site_rows": rows,
        "common_reduced_norm_gcd_coefficients": [str(x) for x in common_norm],
        "common_reduced_norm_gcd_is_one": common_norm == (F(1),),
        "conclusion": (
            "No epsilon in the stated domain makes the nonzero radial ansatz "
            "discrete harmonic at both tested sites."
        ),
    }


def implication_counterexamples():
    sites = ((1, 0, 0), (2, 0, 0), (3, 0, 0))
    weights = {site: F(sum(value * value for value in site) + 1, 7)
               for site in sites}

    def readout(subset):
        return sum((weights[site] for site in subset), F(0))

    left, right = {sites[0]}, {sites[1], sites[2]}
    additive = readout(left | right) == readout(left) + readout(right)
    distinct_shell_weights = len(set(weights.values())) == 3

    rho = {(0, 0, 0): F(2), (1, 0, 0): F(-3)}
    eta = {(0, 1, 0): F(5)}

    def add_fields(a, b):
        return {key: a.get(key, F(0)) + b.get(key, F(0))
                for key in a.keys() | b.keys()}

    identity = lambda field: dict(field)
    identity_linear = identity(add_fields(rho, eta)) == add_fields(identity(rho), identity(eta))
    unit = {(0, 0, 0): F(1)}
    no_tail = identity(unit).get((2, 0, 0), F(0)) == 0
    return {
        "supplied_finite_additivity_counterexample": {
            "additivity_holds": additive,
            "three_distinct_shell_weights": [str(weights[site]) for site in sites],
            "annular_or_two_boundary_collapse_does_not_follow": distinct_shell_weights,
        },
        "local_linear_covariant_response_counterexample": {
            "operator": "identity response K(rho)=rho",
            "linearity_check": identity_linear,
            "translation_and_cubic_covariance": "exact by pointwise identity",
            "unit_source_value_at_distance_two": "0",
            "nonzero_power_law_tail_does_not_follow": no_tail,
        },
    }


def build_certificate():
    memo = (ROOT / AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8")
    normalized_memo = " ".join(memo.split())
    inputs = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    radial = quadratic_route_certificate()
    counterexamples = implication_counterexamples()
    stencil = range_one_stencil_certificate()
    checks = {
        "current_record_axiom_explicitly_excludes_finite_additivity":
            "Finite additivity, a named scalar collection functional" in memo,
        "current_axioms_do_not_choose_a_hamiltonian_or_transfer_operator":
            "does not choose a Hamiltonian or transfer operator" in normalized_memo,
        "radial_obstruction_gcd_is_one": radial["common_reduced_norm_gcd_is_one"],
        "finite_additivity_does_not_collapse_shell_weights":
            counterexamples["supplied_finite_additivity_counterexample"]
            ["annular_or_two_boundary_collapse_does_not_follow"],
        "identity_response_blocks_operator_and_tail_forcing":
            counterexamples["local_linear_covariant_response_counterexample"]
            ["nonzero_power_law_tail_does_not_follow"],
        "supplied_range_one_stencil_has_two_invariant_coefficients":
            stencil["proper_cubic_rotation_count"] == 24
            and stencil["support_orbit_sizes"] == [1, 6]
            and stencil["invariant_coefficient_space_dimension"] == 2,
    }
    return {
        "claim_type": "bounded_theorem",
        "role": "independent checker and helper for the corrected Cycle-884 slice",
        "input_sha256": inputs,
        "radial_massless_obstruction": radial,
        "supplied_range_one_stencil": stencil,
        "implication_counterexamples": counterexamples,
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
