#!/usr/bin/env python3
"""Exact cubic-plus-gauge uniqueness certificate for a quadratic kernel."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product

import sympy as sp


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

AUDIT_TIMEOUT_SEC = 300


@dataclass(frozen=True)
class QuadraticKernelCertificate:
    rotation_count: int
    cubic_only_dimension: int
    transverse_only_dimension: int
    joint_dimension: int
    normalized_kernel: sp.Matrix


def quadratic_kernel_certificate() -> QuadraticKernelCertificate:
    """Solve the cubic-covariant transverse quadratic kernel exactly."""

    momenta = sp.symbols("q0:3")
    monomials = (
        momenta[0] ** 2,
        momenta[1] ** 2,
        momenta[2] ** 2,
        momenta[0] * momenta[1],
        momenta[0] * momenta[2],
        momenta[1] * momenta[2],
    )
    matrix_entries = tuple(
        (row, column)
        for row in range(3)
        for column in range(row, 3)
    )
    coefficients = sp.symbols("a0:36")
    kernel = sp.zeros(3)
    for entry_index, (row, column) in enumerate(matrix_entries):
        polynomial = sum(
            coefficients[6 * entry_index + monomial_index] * monomial
            for monomial_index, monomial in enumerate(monomials)
        )
        kernel[row, column] = polynomial
        kernel[column, row] = polynomial

    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rotation = sp.zeros(3)
            for row in range(3):
                rotation[row, permutation[row]] = signs[row]
            if rotation.det() == 1:
                rotations.append(rotation)

    cubic_equations = []
    momentum_column = sp.Matrix(momenta)
    for rotation in rotations:
        rotated_momenta = rotation * momentum_column
        transformed_arguments = kernel.xreplace(
            {
                momenta[index]: rotated_momenta[index]
                for index in range(3)
            }
        )
        transformed_indices = rotation * kernel * rotation.T
        for row in range(3):
            for column in range(row, 3):
                cubic_equations.extend(
                    sp.Poly(
                        sp.expand(
                            transformed_arguments[row, column]
                            - transformed_indices[row, column]
                        ),
                        momenta,
                    ).coeffs()
                )
    transverse_equations = []
    for component in kernel * momentum_column:
        transverse_equations.extend(
            sp.Poly(sp.expand(component), momenta).coeffs()
        )

    cubic_matrix, _ = sp.linear_eq_to_matrix(
        cubic_equations, coefficients
    )
    transverse_matrix, _ = sp.linear_eq_to_matrix(
        transverse_equations, coefficients
    )
    joint_matrix = cubic_matrix.col_join(transverse_matrix)
    nullspace = joint_matrix.nullspace()
    if len(nullspace) != 1:
        normalized_kernel = sp.zeros(3)
    else:
        substitutions = dict(zip(coefficients, nullspace[0], strict=True))
        solved_kernel = sp.simplify(kernel.subs(substitutions))
        normalization = sp.Poly(
            solved_kernel[0, 0], momenta
        ).coeff_monomial(momenta[1] ** 2)
        normalized_kernel = sp.simplify(solved_kernel / normalization)
    return QuadraticKernelCertificate(
        rotation_count=len(rotations),
        cubic_only_dimension=len(coefficients) - cubic_matrix.rank(),
        transverse_only_dimension=(
            len(coefficients) - transverse_matrix.rank()
        ),
        joint_dimension=len(coefficients) - joint_matrix.rank(),
        normalized_kernel=normalized_kernel,
    )


def main() -> int:
    certificate = quadratic_kernel_certificate()
    q0, q1, q2 = sp.symbols("q0:3")
    maxwell = sp.Matrix(
        (
            (q1**2 + q2**2, -q0 * q1, -q0 * q2),
            (-q0 * q1, q0**2 + q2**2, -q1 * q2),
            (-q0 * q2, -q1 * q2, q0**2 + q1**2),
        )
    )
    conditions = (
        certificate.rotation_count == 24,
        certificate.cubic_only_dimension == 3,
        certificate.transverse_only_dimension == 6,
        certificate.joint_dimension == 1,
        certificate.normalized_kernel == maxwell,
    )
    labels = (
        "the proper cubic group contains exactly twenty-four rotations",
        "cubic covariance alone leaves three symmetric quadratic kernels",
        "gauge transversality alone leaves six symmetric quadratic kernels",
        "their exact intersection is one-dimensional",
        "the surviving normalized kernel is q-squared delta minus q-i q-j",
    )
    passed = 0
    failed = 0
    for condition, label in zip(conditions, labels, strict=True):
        if condition:
            passed += 1
            print(f"[PASS] {passed + failed:02d} {label}")
        else:
            failed += 1
            print(f"[FAIL] {passed + failed:02d} {label}")
    print(
        "KERNEL_DIMENSIONS",
        f"cubic_only={certificate.cubic_only_dimension}",
        f"transverse_only={certificate.transverse_only_dimension}",
        f"joint={certificate.joint_dimension}",
    )
    print(
        "CERTIFICATE: polynomial_order=q2 symmetric_kernel=True "
        "proper_cubic_covariance=True gauge_transversality=True "
        "analyticity_assumed=True higher_orders_unconstrained=True"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
