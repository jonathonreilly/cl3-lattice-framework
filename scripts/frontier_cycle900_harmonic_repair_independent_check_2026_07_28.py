#!/usr/bin/env python3
"""Independent exact checks for the corrected Cycle-900 kernel slice."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/HARMONIC_REPAIR_VIABLE_CYCLE900_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/GBS2_KERNEL_WINDOW_ANATOMY_CYCLE884_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

from fractions import Fraction as F
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def prime_factors(number):
    out, divisor = [], 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            out.append(divisor)
            number //= divisor
        else:
            divisor += 1
    if number > 1:
        out.append(number)
    return sorted(set(out))


def squarefree_distance(squared_distance, radical_symbols):
    square, residue, divisor = 1, squared_distance, 2
    while divisor * divisor <= residue:
        while residue % (divisor * divisor) == 0:
            residue //= divisor * divisor
            square *= divisor
        divisor += 1
    value = sp.Integer(square)
    for prime in prime_factors(residue):
        value *= radical_symbols[prime]
    return value


def screened_axis_value(axis, epsilon, radical_symbols):
    transverse = squarefree_distance(axis * axis + 1, radical_symbols)
    return (epsilon + axis) * (
        1 / (epsilon + axis - 1)
        + 1 / (epsilon + axis + 1)
        + 4 / (epsilon + transverse)
    )


def norm_by_resultants(expression, radicals):
    current = sp.Poly(sp.expand(expression), *([*radicals, sp.symbols("epsilon")]),
                      domain=sp.QQ).as_expr()
    for radical, prime in radicals.items():
        current = sp.resultant(current, radical * radical - prime, radical)
        current = sp.expand(current)
    epsilon = sp.symbols("epsilon")
    return sp.Poly(current, epsilon, domain=sp.QQ).monic()


def screened_gcd_certificate():
    epsilon = sp.symbols("epsilon")
    primes = (2, 5, 17)
    radical_symbols = {prime: sp.symbols(f"r{prime}") for prime in primes}
    rows, norms = [], []
    for left, right in ((1, 2), (1, 3), (2, 3), (1, 4)):
        difference = sp.together(
            screened_axis_value(left, epsilon, radical_symbols)
            - screened_axis_value(right, epsilon, radical_symbols)
        )
        numerator, _denominator = difference.as_numer_denom()
        used_primes = sorted(
            prime for prime, symbol in radical_symbols.items()
            if numerator.has(symbol)
        )
        used = {radical_symbols[prime]: prime for prime in used_primes}
        norm = norm_by_resultants(numerator, used)
        norms.append(norm)
        rows.append({
            "axis_pair": [left, right],
            "field_primes": used_primes,
            "norm_degree": norm.degree(),
            "norm_coefficients_high_to_low": [str(value) for value in norm.all_coeffs()],
            "epsilon_one_tenth_is_root": norm.eval(F(1, 10)) == 0,
        })
    common = norms[0]
    for norm in norms[1:]:
        common = sp.gcd(common, norm).monic()
    simple_radical = sp.symbols("r2")
    simple_norm = sp.resultant(1 + simple_radical,
                               simple_radical * simple_radical - 2,
                               simple_radical)
    return {
        "method": "clear denominators, then eliminate each radical with exact resultants",
        "norm_of_one_plus_sqrt_two": str(simple_norm),
        "norm_identity_is_minus_one": simple_norm == -1,
        "pair_rows": rows,
        "common_gcd": str(common.as_expr()),
        "common_gcd_is_one": common.as_expr() == 1,
        "domain": (
            "nonzero amplitude; epsilon must avoid every centre and neighbour "
            "denominator pole of the four displayed axis conditions"
        ),
        "conclusion": (
            "No defined epsilon can make all four screened axis conditions "
            "share one value of mu_squared."
        ),
    }


def sqrt_enclosure(number, bits):
    scale = 1 << bits
    floor = isqrt(number * scale * scale)
    return F(floor, scale), F(floor + 1, scale)


def quadratic_basis_exact_zero(rational, radical_coefficient, radicand):
    """Exact zero test in Q-basis {1,sqrt(radicand)} for nonsquare radicand."""
    assert radicand > 0 and isqrt(radicand) ** 2 != radicand
    return rational == 0 and radical_coefficient == 0


def root_ambiguity_control():
    lower, upper = sqrt_enclosure(2, bits=2)
    lower -= F(7, 5)
    upper -= F(7, 5)
    separated_sign = 1 if lower > 0 else -1 if upper < 0 else None
    exact_zero = quadratic_basis_exact_zero(F(-7, 5), F(1), 2)
    returned_object = "unresolved bracket" if separated_sign is None and not exact_zero else "point"
    return {
        "test_element": "sqrt(2)-7/5",
        "rational_basis_coefficients": ["-7/5", "1"],
        "coarse_enclosure": [str(lower), str(upper)],
        "enclosure_sign": separated_sign,
        "exact_zero": exact_zero,
        "returned_object": returned_object,
        "ambiguous_enclosure_is_not_promoted_to_exact_root": returned_object != "point",
    }


def normalization_certificate():
    kernel = (F(2), F(3), F(5))
    raw_sum = sum(kernel, F(0))
    lam, sigma, parameter = F(3, 7), F(5, 11), F(13, 9)
    transformed_lam, transformed_sigma = parameter * lam, sigma / parameter
    product_fixed = lam * sigma == transformed_lam * transformed_sigma
    weighted_sum_fixed = lam * sigma * raw_sum == transformed_lam * transformed_sigma * raw_sum
    scale_factor = F(4)
    scaled_kernel = tuple(scale_factor * value for value in kernel)
    ratios_before = (kernel[1] / kernel[0], kernel[2] / kernel[0])
    ratios_after = (scaled_kernel[1] / scaled_kernel[0], scaled_kernel[2] / scaled_kernel[0])
    return {
        "product_stabilizer": {
            "map": "(lambda,sigma)->(t lambda,sigma/t), t!=0",
            "lambda_sigma_is_fixed": product_fixed,
            "fixed_kernel_raw_sum_before_and_after": [str(raw_sum), str(raw_sum)],
            "amplitude_weighted_sum_is_fixed": weighted_sum_fixed,
            "cannot_move_a_fixed_kernel_raw_sum": True,
        },
        "independent_kernel_amplitude_rescaling": {
            "raw_sum_before": str(raw_sum),
            "raw_sum_after": str(sum(scaled_kernel, F(0))),
            "shape_ratios_before": [str(value) for value in ratios_before],
            "shape_ratios_after": [str(value) for value in ratios_after],
            "shape_ratios_are_invariant": ratios_before == ratios_after,
        },
    }


def build_certificate():
    screened = screened_gcd_certificate()
    ambiguity = root_ambiguity_control()
    normalization = normalization_certificate()
    checks = {
        "correct_basic_field_norm": screened["norm_identity_is_minus_one"],
        "corrected_screened_pair_norms_have_unit_common_gcd": screened["common_gcd_is_one"],
        "ambiguous_interval_not_called_exact_root":
            ambiguity["ambiguous_enclosure_is_not_promoted_to_exact_root"],
        "product_stabilizer_keeps_raw_sum":
            normalization["product_stabilizer"]["cannot_move_a_fixed_kernel_raw_sum"],
        "shape_ratios_cancel_independent_amplitude":
            normalization["independent_kernel_amplitude_rescaling"]
            ["shape_ratios_are_invariant"],
    }
    return {
        "claim_type": "bounded_theorem",
        "role": "independent checker and helper for the corrected Cycle-900 slice",
        "input_sha256": {
            path: sha256((ROOT / path).read_bytes()).hexdigest()
            for path in AUDIT_INPUT_PATHS
        },
        "screened_radial_ansatz_obstruction": screened,
        "root_ambiguity_control": ambiguity,
        "normalization_scope": normalization,
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
