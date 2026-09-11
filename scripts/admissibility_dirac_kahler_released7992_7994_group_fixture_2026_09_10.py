#!/usr/bin/env python3
"""Minimal proper-cubic-group supplier for corrected Blocks 215--217.

The historical Block 215 imported an otherwise unused Block 201 module only
for ``signed_permutations``.  This bounded helper carries that construction
directly: all determinant-one signed permutation matrices in three
dimensions.  It supplies no theorem, axiom, physical interpretation, or
claim from the historical module.
"""

from __future__ import annotations

import itertools

import sympy as sp

# Two finite indexing literals used directly by Blocks 215--217 but absent
# from the narrower corrected Block 213 supplier namespace.
GAUGE_FACE_ORDER = (
    ("tx", 0), ("ty", 0), ("xy", 0),
    ("tx", 1), ("ty", 1), ("xy", 1),
)
CORNER_DEGREE = (0, 1, 1, 2, 1, 2, 2, 3)


def signed_permutations() -> tuple:
    """Return the 24 determinant-one signed 3 x 3 permutations."""
    result = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            matrix = sp.zeros(3, 3)
            for row in range(3):
                matrix[row, permutation[row]] = signs[row]
            if matrix.det() == 1:
                result.append(matrix)
    return tuple(result)


def supplier_certificate() -> bool:
    """Cheap exact shape, uniqueness, orthogonality, and determinant check."""
    matrices = signed_permutations()
    keys = {tuple(matrix) for matrix in matrices}
    return bool(
        len(matrices) == len(keys) == 24
        and all(matrix.shape == (3, 3) for matrix in matrices)
        and all(matrix.T * matrix == sp.eye(3) for matrix in matrices)
        and all(matrix.det() == 1 for matrix in matrices)
        and GAUGE_FACE_ORDER == (
            ("tx", 0), ("ty", 0), ("xy", 0),
            ("tx", 1), ("ty", 1), ("xy", 1),
        )
        and CORNER_DEGREE == tuple(sum(corner) for corner in itertools.product((0, 1), repeat=3))
    )
