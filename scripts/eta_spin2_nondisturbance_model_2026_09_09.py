"""Finite source-only extraction for corrected Eta spin-2 notes.
No historical controller, Git authority guard, physical compiler or cache is imported.
Exact upstream bodies and extraction provenance are in the dated recovery packet.
"""
from __future__ import annotations
import itertools
from collections import Counter
from typing import Iterable
from functools import cache
import sympy as sp
import eta_spin2_joint_model_2026_09_09 as b10
R=sp.Rational
I=sp.I
I2=sp.eye(2)
X=sp.Matrix(((0,1),(1,0)))
Y=sp.Matrix(((0,-I),(I,0)))
Z=sp.diag(1,-1)
PAULIS=(X,Y,Z)
def equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def flat(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(tuple(matrix))


def kron(*matrices: sp.MatrixBase) -> sp.Matrix:
    result = sp.Matrix(((1,),))
    for matrix in matrices:
        result = sp.kronecker_product(result, matrix)
    return result


@cache
def shell_facts() -> dict[str, object]:
    q0, q1, q2, q3, q4, ux, uy, uz, s = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz s", real=True
    )
    parameters = (q0, q1, q2, q3, q4, ux, uy, uz, s)
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4), (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    vectors = b10.joint_vectors(tensor, spatial, s)
    positive = []
    antipodal = []
    for axis in range(3):
        direction = sp.zeros(3, 1)
        direction[axis] = 1
        plus = b10.b9.DIRECTIONS.index(direction)
        minus = b10.b9.DIRECTIONS.index(-direction)
        positive.extend(vectors[plus])
        antipodal.append(equal(vectors[plus], -vectors[minus]))
    jacobian = sp.Matrix(positive).jacobian(parameters)
    zero_vectors = tuple(vector.subs(dict.fromkeys(parameters, 0))
                         for vector in vectors)
    return {
        "parameters": parameters,
        "tensor": tensor,
        "spatial": spatial,
        "vectors": vectors,
        "jacobian": jacobian,
        "rank": jacobian.rank(),
        "determinant": sp.factor(jacobian.det()),
        "antipodal": all(antipodal),
        "maximally_mixed": all(equal(vector, sp.zeros(3, 1))
                               for vector in zero_vectors),
    }


@cache
def pair_algebra_facts() -> dict[str, object]:
    differences = tuple(kron(pauli, I2) - kron(I2, pauli)
                        for pauli in PAULIS)
    sums = (
        sp.simplify((differences[1] * differences[2]
                     - differences[2] * differences[1]) / (2 * I)),
        sp.simplify((differences[2] * differences[0]
                     - differences[0] * differences[2]) / (2 * I)),
        sp.simplify((differences[0] * differences[1]
                     - differences[1] * differences[0]) / (2 * I)),
    )
    expected_sums = tuple(kron(pauli, I2) + kron(I2, pauli)
                          for pauli in PAULIS)
    first = tuple(sp.simplify((summed + difference) / 2)
                  for summed, difference in zip(sums, differences))
    second = tuple(sp.simplify((summed - difference) / 2)
                   for summed, difference in zip(sums, differences))
    expected_first = tuple(kron(pauli, I2) for pauli in PAULIS)
    expected_second = tuple(kron(I2, pauli) for pauli in PAULIS)
    local_basis = tuple(
        kron(left, right)
        for left in (I2,) + PAULIS for right in (I2,) + PAULIS
    )
    basis_rank = sp.Matrix.hstack(*(flat(item) for item in local_basis)).rank()
    return {
        "differences": differences,
        "commutator_sums": all(equal(left, right)
                               for left, right in zip(sums, expected_sums)),
        "first_local": all(equal(left, right)
                           for left, right in zip(first, expected_first)),
        "second_local": all(equal(left, right)
                            for left, right in zip(second, expected_second)),
        "basis_rank": basis_rank,
        "full_six_qubit_dimension": basis_rank ** 3,
    }


@cache
def identity_kraus_span_facts() -> dict[str, object]:
    """Exact constraint count for operators in the identity-Choi support.

    A vectorized d-by-d operator is proportional to the identity exactly when
    every off-diagonal coordinate vanishes and every diagonal coordinate
    equals the first.  The constraints have distinct pivots: d(d-1)
    off-diagonal pivots plus d-1 diagonal pivots.  This computes, rather than
    assumes, the one-dimensional support used by the extension lemma.
    """
    d = 2 ** 6
    off_diagonal_pivots = {
        row * d + column
        for row in range(d) for column in range(d) if row != column
    }
    diagonal_pivots = {index * d + index for index in range(1, d)}
    constraint_rank = len(off_diagonal_pivots) + len(diagonal_pivots)
    identity_coordinates = tuple(
        1 if row == column else 0
        for row in range(d) for column in range(d)
    )
    identity_satisfies = all(
        identity_coordinates[index] == 0 for index in off_diagonal_pivots
    ) and all(
        identity_coordinates[index] == identity_coordinates[0]
        for index in diagonal_pivots
    )
    return {
        "constraint_rank": constraint_rank,
        "nullity": d * d - constraint_rank,
        "identity_satisfies": identity_satisfies,
        "scalar_support": identity_satisfies and d * d - constraint_rank == 1,
    }


@cache
def fixed_point_and_choi_facts() -> dict[str, object]:
    shell = shell_facts()
    algebra = pair_algebra_facts()
    # The identity-channel Choi vector on d=64 has d nonzero unit entries.
    # Its outer product therefore has rank one and trace d without allocating
    # a dense 4096-by-4096 matrix.
    d = 2 ** 6
    omega = sp.SparseMatrix(d * d, 1, {(index * d + index, 0): 1
                                      for index in range(d)})
    omega_norm = (omega.T * omega)[0]
    beta = sp.symbols("beta", real=True)
    off_diagonal_minor = sp.Matrix(((1, beta), (beta, 0))).det()
    span = identity_kraus_span_facts()
    pure_marginal_forces_product = (
        omega_norm == d and span["constraint_rank"] == d * d - 1
        and span["scalar_support"]
        and sp.factor(off_diagonal_minor) == -beta ** 2
    )
    return {
        "bistochastic_anchor": shell["maximally_mixed"],
        "fixed_tangent_rank": shell["rank"],
        "fixed_algebra_dimension": algebra["full_six_qubit_dimension"],
        "identity_choi_rank": 1 if omega_norm != 0 else 0,
        "identity_choi_trace": omega_norm,
        "off_diagonal_minor": off_diagonal_minor,
        "kraus_span_nullity": span["nullity"],
        "pure_marginal_forces_product": pure_marginal_forces_product,
        "constant_complement_rank": 0 if pure_marginal_forces_product else shell["rank"],
        "target_complement_rank": shell["rank"],
    }


@cache
def even_shell_facts() -> dict[str, object]:
    shell = shell_facts()
    even_symbols = sp.symbols("e0:9", real=True)
    even_vectors = tuple(sp.Matrix(even_symbols[3 * axis:3 * axis + 3])
                         for axis in range(3))
    augmented = []
    for direction, vector in zip(b10.b9.DIRECTIONS, shell["vectors"]):
        axis = next(index for index in range(3) if direction[index] != 0)
        augmented.append(sp.expand(vector + even_vectors[axis]))
    base_matrix = b10.odd_shell_matrix(shell["vectors"])
    augmented_matrix = b10.odd_shell_matrix(tuple(augmented))
    output_coordinates = sp.Matrix.vstack(*augmented)
    all_parameters = shell["parameters"] + even_symbols
    return {
        "odd_decoder_unchanged": equal(base_matrix, augmented_matrix),
        "target_rank": output_coordinates.jacobian(shell["parameters"]).rank(),
        "full_rank": output_coordinates.jacobian(all_parameters).rank(),
        "even_count": len(even_symbols),
    }


@cache
def classical_record_control_facts() -> dict[str, object]:
    """Orthogonal Record bits can be copied without the quantum obstruction."""
    cnot = sp.Matrix((
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 1, 0),
    ))
    zero = sp.Matrix((1, 0))
    one = sp.Matrix((0, 1))
    copied_zero = cnot * kron(zero, zero)
    copied_one = cnot * kron(one, zero)
    return {
        "unitary": equal(cnot.T.conjugate() * cnot, sp.eye(4)),
        "zero_copy": equal(copied_zero, kron(zero, zero)),
        "one_copy": equal(copied_one, kron(one, one)),
        "orthogonal": (zero.T * one)[0] == 0,
        "open_nine_parameter": False,
    }


def partial_trace_two(matrix: sp.MatrixBase, traced: int) -> sp.Matrix:
    result = sp.zeros(2)
    for left in range(2):
        for right in range(2):
            if traced == 1:
                result[left, right] = sum(
                    matrix[2 * left + index, 2 * right + index]
                    for index in range(2)
                )
            else:
                result[left, right] = sum(
                    matrix[2 * index + left, 2 * index + right]
                    for index in range(2)
                )
    return sp.simplify(result)


@cache
def approximate_clone_control_facts() -> dict[str, object]:
    """Exact optimal symmetric 1-to-2 cloner as a relaxed-premise control."""
    swap = sp.zeros(4)
    for left in range(2):
        for right in range(2):
            swap[2 * right + left, 2 * left + right] = 1
    symmetric = (sp.eye(4) + swap) / 2
    kraus = []
    for blank in range(2):
        embedding = sp.zeros(4, 2)
        for value in range(2):
            embedding[2 * value + blank, value] = 1
        kraus.append(sp.sqrt(R(2, 3)) * symmetric * embedding)

    def channel(operator: sp.MatrixBase) -> sp.Matrix:
        return sp.simplify(sum(
            (item * operator * item.T.conjugate() for item in kraus),
            sp.zeros(4),
        ))

    completeness = sp.simplify(sum(
        (item.T.conjugate() * item for item in kraus), sp.zeros(2)
    ))
    pauli_marginals = all(
        equal(partial_trace_two(channel(pauli), traced), R(2, 3) * pauli)
        for pauli in PAULIS for traced in (0, 1)
    )
    identity_marginals = all(
        equal(partial_trace_two(channel(I2), traced), I2)
        for traced in (0, 1)
    )
    return {
        "tp": equal(completeness, I2),
        "marginal_shrink": pauli_marginals,
        "identity": identity_marginals,
        "shrink": R(2, 3),
        "exact_copy": False,
        "prefix_safe": False,
    }
