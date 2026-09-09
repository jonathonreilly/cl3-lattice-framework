# L2: two stipulated face operator algebras

**Date:** 2026-06-04; source correction 2026-09-09
**Type:** bounded_theorem
**Scope:** supplied finite mathematics; no physical selection or audit verdict.
**Primary runner:** [diagonal_l2_face_algebra_dimension_audit.py](../scripts/diagonal_l2_face_algebra_dimension_audit.py)
**Cached output:** [diagonal_l2_face_algebra_dimension_audit.txt](../logs/runner-cache/diagonal_l2_face_algebra_dimension_audit.txt)
**Original history:** [exact original and correction record](../.claude/science/physics-loops/diagonal-adjacency-7870-correction-20260909/CORRECTION_HISTORY.md).

This note compares two finite generator families. Neither family is derived
as the unique action of a link connection. In the current
[qubit-link note](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md),
a connection is conditionally a unitary map between two-dimensional fibers.
That convention does not supply the tensor-sum action below or a label-space
hopping Hamiltonian. This distinction is an input boundary, not a defect in
the finite calculations.

## A. Simultaneous endpoint action on four qubits

Supply `(C^2)^{tensor 4}` and the four-cycle edges
`01,12,23,30`. For each edge `ab` include
`i(sigma_j^(a)+sigma_j^(b))`, `j=x,y,z`, and include the global `i I_16`.
These are anti-Hermitian operators on one 16-dimensional tensor space.
For this graph their real Lie algebra is

```
g_A = su(2)_0 direct-sum su(2)_1 direct-sum su(2)_2 direct-sum su(2)_3
      direct-sum u(1),       dimension 13.
```

Every generator lies in the displayed algebra, giving the upper bound.
For the lower bound, overlapping edges isolate local Pauli directions:
`[i(sigma_x^0+sigma_x^1),i(sigma_y^1+sigma_y^2)]=-2i sigma_z^1`.
Cycling Pauli directions gives the full local triple at site 1. Subtract
it from adjacent edge sums to obtain neighboring triples and propagate
around the four-cycle. The twelve local traceless generators and identity
are independent. Different site triples commute, each is an ideal, and the
derived algebra has dimension 12. Adding diagonals `02,13` does not change
this algebra because their generators already lie in it. This proof is for
the stated family and graph; connectedness alone for an arbitrary endpoint-sum
graph is not asserted to suffice.

There is NO faithful su(3) embedding into `g_A`. A homomorphism from the simple
real Lie algebra `su(3)` to each `su(2)` summand is zero or injective. The
latter is impossible since 8>3; its map to the abelian center is zero since
`su(3)=[su(3),su(3)]`. Thus every coordinate projection is zero.

## B. Two hopping quadratures on a label space

On `C^n`, for each supplied edge `ab` include
`i(E_ab+E_ba)` and `E_ab-E_ba`. All are traceless anti-Hermitian.
For a connected graph these generate `su(n)`: commutators along paths give
both off-diagonal quadratures for every pair; their mutual commutators give
`i(E_aa-E_bb)`. Those matrices span the entire traceless anti-Hermitian
space. Consequently the four-cycle and the complete four-label graph both
give `su(4)`, dimension 15.

The full generated algebra is not equal to `su(3)`, but it **does contain a
faithful su(3)**. Explicitly

```
phi(X) = diag(X,0),     X in su(3),
[phi(X),phi(Y)] = phi([X,Y]).
```

This real-linear map preserves trace and adjoint and is injective since its
upper-left block is X. The runner tests all eight basis images, all 64 basis
brackets and membership in the computed four-label algebra. The original
no-embedding assertion for this family was false.

For the separately supplied abstract labels `{100,010,001}`, all pairs have
Hamming distance 2. Including their triangle of both quadratures generates
`su(3)` on `C^3`; including only Hamming-distance-one pairs gives no generators.
This is an algebra on the three labels, sometimes called horizontal; it does
not identify physical generations or an independent color factor. If three
independent generations and three colors are additionally stipulated as a
full tensor-product carrier, its dimension is 9, not 3. That conditional
arithmetic neither rules out every physical realization nor selects this one.

## What remains supplied

A closure equality concerns operators, not the number of independent link
variables or coupling constants. A new variable may enter an old operator
basis with a new coefficient. Spatial links, abstract labels and BZ corners
also require distinct identifications; a translation-invariant spatial hop is
diagonal in momentum and need not mix corners. No unique connection, color
selection, chiral matter, action or Record formation follows here.
This note does not change axioms; the [current four-axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies only
framework context. No parent campaign or historical status is accepted.

The exact short proofs above support the algebraic statements. The unchanged
numerical closure algorithm uses real/imaginary flattening and rank tolerance
`10^-9`; its dimensions are finite floating checks of those proofs, not a
proof of an unrestricted classification.
