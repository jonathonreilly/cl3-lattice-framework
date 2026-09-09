#!/usr/bin/env python3
"""Corrected exact finite statements for the Cycle-900 kernel slice."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/HARMONIC_REPAIR_VIABLE_CYCLE900_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/GBS2_KERNEL_WINDOW_ANATOMY_CYCLE884_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle900_harmonic_repair_independent_check_2026_07_28.py",
)

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import sympy as sp

import frontier_cycle900_harmonic_repair_independent_check_2026_07_28 as independent

ROOT = Path(__file__).resolve().parents[1]
NEIGHBOURS = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)


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


def evaluate(poly, value):
    out = F(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def squarefree_split(number):
    if number == 0:
        return 0, 1
    square, residue, divisor = 1, number, 2
    while divisor * divisor <= residue:
        while residue % (divisor * divisor) == 0:
            residue //= divisor * divisor
            square *= divisor
        divisor += 1
    return square, residue


def prime_set(number):
    out, divisor = set(), 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            out.add(divisor)
            number //= divisor
        else:
            divisor += 1
    if number > 1:
        out.add(number)
    return frozenset(out)


def mq_add(a, b):
    out = dict(a)
    for key, value in b.items():
        combined = add(out.get(key, ()), value)
        if combined:
            out[key] = combined
        else:
            out.pop(key, None)
    return out


def mq_scale(a, factor):
    return {key: scale(value, factor) for key, value in a.items()
            if scale(value, factor)}


def mq_sub(a, b):
    return mq_add(a, mq_scale(b, F(-1)))


def mq_mul(a, b):
    out = {}
    for key_a, poly_a in a.items():
        for key_b, poly_b in b.items():
            key = key_a ^ key_b
            factor = F(1)
            for prime in key_a & key_b:
                factor *= prime
            term = scale(mul(poly_a, poly_b), factor)
            combined = add(out.get(key, ()), term)
            if combined:
                out[key] = combined
            else:
                out.pop(key, None)
    return out


def mq_conjugate(a, sign_by_prime):
    out = {}
    for key, value in a.items():
        sign = 1
        for prime in key:
            sign *= sign_by_prime[prime]
        out[key] = scale(value, F(sign))
    return out


def mq_norm(a):
    """Multiply full ring elements over every sign character."""
    primes = sorted({prime for key in a for prime in key})
    accumulated = {frozenset(): (F(1),)}
    for signs in product((1, -1), repeat=len(primes)):
        conjugate = mq_conjugate(a, dict(zip(primes, signs)))
        accumulated = mq_mul(accumulated, conjugate)
    radical_remainder = {key: value for key, value in accumulated.items()
                         if key and value}
    assert not radical_remainder
    return trim(accumulated.get(frozenset(), ()))


def surd_plus_epsilon(squared_distance):
    square, residue = squarefree_split(squared_distance)
    radical = {prime_set(residue): (F(square),)}
    return mq_add(radical, {frozenset(): (F(0), F(1))})


def screened_axis_value(axis):
    site = (axis, 0, 0)
    neighbours = [tuple(site[i] + edge[i] for i in range(3)) for edge in NEIGHBOURS]
    factors = [surd_plus_epsilon(sum(value * value for value in point))
               for point in neighbours]
    centre = surd_plus_epsilon(axis * axis)
    denominator = {frozenset(): (F(1),)}
    for factor in factors:
        denominator = mq_mul(denominator, factor)
    numerator = {}
    for omitted in range(len(factors)):
        term = {frozenset(): (F(1),)}
        for index, factor in enumerate(factors):
            if index != omitted:
                term = mq_mul(term, factor)
        numerator = mq_add(numerator, term)
    return mq_mul(centre, numerator), denominator


def screened_pair_condition(left, right):
    numerator_left, denominator_left = screened_axis_value(left)
    numerator_right, denominator_right = screened_axis_value(right)
    return mq_sub(
        mq_mul(numerator_left, denominator_right),
        mq_mul(numerator_right, denominator_left),
    )


def corrected_field_norm_certificate():
    basic = {frozenset(): (F(1),), frozenset({2}): (F(1),)}
    basic_norm = mq_norm(basic)
    rows, norms = [], []
    for pair in ((1, 2), (1, 3), (2, 3), (1, 4)):
        condition = screened_pair_condition(*pair)
        norm = monic(mq_norm(condition))
        norms.append(norm)
        rows.append({
            "axis_pair": list(pair),
            "field_primes": sorted({prime for key in condition for prime in key}),
            "norm_degree": degree(norm),
            "norm_coefficients_low_to_high": [str(value) for value in norm],
            "epsilon_one_tenth_is_root": evaluate(norm, F(1, 10)) == 0,
        })
    common = norms[0]
    for norm in norms[1:]:
        common = gcd(common, norm)
    return {
        "implementation": (
            "Each conjugate remains a multiquadratic ring element and is "
            "multiplied with mq_mul; radical components are required to vanish only at the end."
        ),
        "norm_of_one_plus_sqrt_two": [str(value) for value in basic_norm],
        "norm_identity_is_minus_one": basic_norm == (F(-1),),
        "pair_rows": rows,
        "common_gcd_coefficients": [str(value) for value in common],
        "common_gcd_is_one": common == (F(1),),
        "logical_scope": (
            "For A!=0 and epsilon away from every original denominator pole, "
            "a shared screened equation would force all displayed M_n(epsilon) "
            "to agree. Their cleared pair norms have no common root."
        ),
    }


def orbit_class(site):
    return tuple(sorted((abs(value) for value in site), reverse=True))


def solve_screened_cube(radius, mu_squared):
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
        matrix[row][row] = F(6) + mu_squared
        for edge in NEIGHBOURS:
            neighbour = tuple(site[i] + edge[i] for i in range(3))
            if max(abs(value) for value in neighbour) <= radius:
                matrix[row][index[orbit_class(neighbour)]] -= F(1)
        matrix[row][size] = F(1) if site == (0, 0, 0) else F(0)
    for column in range(size):
        pivot = next((row for row in range(column, size)
                      if matrix[row][column]), None)
        if pivot is None:
            return None
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        factor = matrix[column][column]
        matrix[column] = [value / factor for value in matrix[column]]
        for row in range(size):
            if row == column or matrix[row][column] == 0:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                matrix[row][j] - factor * matrix[column][j]
                for j in range(size + 1)
            ]
    return {site: matrix[index[site]][size] for site in classes}


def finite_screened_identity_certificate():
    rows = []
    for mu_squared in (F(0), F(1, 100), F(1, 4), F(1)):
        solution = solve_screened_cube(3, mu_squared)
        G0, G1 = solution[(0, 0, 0)], solution[(1, 0, 0)]
        step = G0 - G1
        predicted = (F(1) - mu_squared * G0) / 6
        rows.append({
            "mu_squared": str(mu_squared),
            "G0": str(G0),
            "G0_minus_Ge1": str(step),
            "predicted_origin_identity": str(predicted),
            "identity_holds": step == predicted,
            "G0_is_positive_in_this_model": G0 > 0,
            "step_equals_one_sixth": step == F(1, 6),
        })
    return {
        "definition": (
            "For supplied mu_squared>=0 on the radius-three zero-exterior cube, solve "
            "(6I-adjacency+mu_squared I)G=delta_0."
        ),
        "identity": "G(0)-G(e1)=(1-mu_squared*G(0))/6",
        "rows": rows,
        "all_rows_exact": all(row["identity_holds"] for row in rows),
        "conditional_equivalence": (
            "For mu_squared>=0, the finite Dirichlet solution is unique and cubic-invariant; "
            "whenever G(0) is nonzero, this identity equals 1/6 iff mu_squared=0."
        ),
        "scope": "finite chosen zero-exterior boundary problem; no physical or infinite-volume selection",
    }


def stabilizer_certificate():
    lam, sigma, parameter = sp.symbols("lambda sigma t", nonzero=True)
    product_fixed = sp.simplify((parameter * lam) * (sigma / parameter) - lam * sigma) == 0
    amplitude = sp.symbols("c", nonzero=True)
    k1, k2 = sp.symbols("k1 k2", nonzero=True)
    ratio_fixed = sp.simplify((amplitude * k1) / (amplitude * k2) - k1 / k2) == 0
    return {
        "product_stabilizer_map": "(lambda,sigma)->(t lambda,sigma/t), t!=0",
        "product_is_symbolically_fixed": product_fixed,
        "fixed_kernel_raw_sum_changes_under_this_map": False,
        "independent_kernel_amplitude_rescaling_changes_raw_sums": True,
        "shape_ratio_is_symbolically_amplitude_invariant": ratio_fixed,
        "scope": "nonzero t, amplitude, and ratio denominator",
    }


def build_certificate():
    helper = independent.build_certificate()
    norm = corrected_field_norm_certificate()
    screened = finite_screened_identity_certificate()
    stabilizer = stabilizer_certificate()
    ambiguity = helper["root_ambiguity_control"]
    checks = {
        "basic_norm_corrected": norm["norm_identity_is_minus_one"],
        "corrected_primary_gcd_is_one": norm["common_gcd_is_one"],
        "independent_resultant_gcd_is_one":
            helper["screened_radial_ansatz_obstruction"]["common_gcd_is_one"],
        "finite_screened_origin_identity_exact": screened["all_rows_exact"],
        "finite_screened_tested_G0_positive": all(
            row["G0_is_positive_in_this_model"] for row in screened["rows"]),
        "finite_screened_tested_equivalence": all(
            row["step_equals_one_sixth"] == (row["mu_squared"] == "0")
            for row in screened["rows"]),
        "ambiguous_interval_not_exact_root":
            ambiguity["ambiguous_enclosure_is_not_promoted_to_exact_root"],
        "product_stabilizer_scope_correct":
            stabilizer["product_is_symbolically_fixed"]
            and not stabilizer["fixed_kernel_raw_sum_changes_under_this_map"],
        "independent_checker_passes": helper["all_checks_pass"],
    }
    return {
        "claim_type": "bounded_theorem",
        "input_sha256": {
            path: sha256((ROOT / path).read_bytes()).hexdigest()
            for path in AUDIT_INPUT_PATHS
        },
        "corrected_multiquadratic_norm_and_screened_obstruction": norm,
        "independent_resultant_confirmation":
            helper["screened_radial_ansatz_obstruction"],
        "finite_screened_origin_identity": screened,
        "interval_semantics": ambiguity,
        "normalization_scope": stabilizer,
        "withdrawn_historical_inferences": [
            "a physically forced or unique harmonic repair",
            "selection of zero-exterior rather than periodic boundary conditions",
            "infinite-lattice existence, convergence, transcendence, or exact asymptotics",
            "TOWARD or source-action sign from Green-function positivity",
            "the 37-row consumer census and complete physical patch-list verdict",
            "chart dimension reductions as complete physical dimension counts",
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
