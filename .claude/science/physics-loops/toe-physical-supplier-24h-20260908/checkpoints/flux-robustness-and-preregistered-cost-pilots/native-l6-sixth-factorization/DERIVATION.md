# Sixth-order factorization: exact identity and structural obstruction

This is an independent structural analysis informed by the root's proposed factorization route and the six-invariant classification in `native-l6-sixth-spectator-invariants/DERIVATION.md`. It computes no native sixth coefficient. The result is an obstruction to inferring the full spectator bands from the adjacent coefficient, symmetry, and positivity alone.

Let P be the isolated unperturbed ground cluster, Q=1-P, L=H0-E0, and G=Q L^{-1}Q, extended by zero on P. Let W be the Hermitian perturbation with its scalar part removed. The complete irreducible six-insertion chain is

C6 = -P W G W G W G W G W G W P = -T†T,
T = G^(1/2) W G W G W P.

This exact identity uses all intermediate sectors and all orderings. Where the separate scalar-through-five and folded-term analysis applies, it identifies the sixth nonscalar term modulo a scalar; it does not identify the full sixth scalar energy. Resolving the middle sector gives -sum_F T_F†T_F. It does not justify keeping only a singleton-star middle sector.

For two disjoint six-edge stars, fix three two-edge insertions at each star. Among the 720 orders, only 72 place an entire star in the first three insertions; 648 have a mixed middle toggle. The included actual L6 support control verifies this for opposite-color vertices separated by three links. This counting establishes the defect in a proposed restriction of the word sum; it does not assert that each individual mixed word has a nonzero amplitude.

## Why the Gram sign is insufficient

Modulo an unknown scalar, negative semidefiniteness gives no restriction on a finite Hermitian operator: any Q is lambda I-A†A for suitable A. A concrete isolated finite ladder makes this obstruction compatible with scalar lower perturbative orders. Take four copies of the same finite space, H0=diag(0,I,I,I), and W with nearest-level couplings I,I,A. For an eigenvalue s of A†A, the four-level characteristic polynomial gives

E(u) = -u² + (1-s)u⁶ + O(u⁸).

Thus the effective operator is -u²I + u⁶(I-A†A)+O(u⁸), with scalar coefficients through order five. For any desired symmetry-invariant Hermitian Q, choose A=(lambda I-Q)^(1/2), lambda>||Q||. Its sixth nonscalar operator is Q. Symmetry extends diagonally across the four levels. This is a counterexample to a universal structural inference, not a replacement for the actual native perturbation.

Even within the L6 allowed quadratic magnetic space, adjacent information does not suffice. Write A0=-K² for the canonical pi-flux hopping matrix, whose L6 bands are 12,24,36,48. The polynomial skew matrices

B0 = -K(A0-12I)/16 = (K³+12K)/16,
B1 = K(A0-30I)/2 = (-K³-30K)/2

inherit the magnetic symmetries and opposite-sublattice support. At an adjacent oriented pair with K=-2 and K³=56, both entries equal 2, giving the same positive adjacent coefficient in (i/4) beta^T B beta. Nevertheless B0 has a zero band on A0=12, and B1 changes its orientation relative to K between the lower and upper A0 bands. These are allowed invariant operators, not asserted native coefficients. The zero band is enough to defeat a uniqueness/gap inference; counting its degeneracy is unnecessary here. The control verifies the local cubic and adjacent entries with a declared seam representative; it does not numerically certify the imported full Fourier spectrum.

## Remaining obligation

A useful positivity theorem must add native-specific relations between all T_F, including mixed middle sectors. Examples of sufficient additional work would be an exact functional relation B=-K f(A0) with a proven nonzero/sign bound on every allowed band, or a quantitative domination bound on the five other invariants. Neither follows from the Gram identity, scalar lower orders, or a positive adjacent coefficient. Injectivity of T alone also does not imply a nondegenerate largest singular value or exclude zero spectator frequencies after scalar subtraction.

`controls.py` uses integer/Fraction arithmetic for the 720-order count, the local L6 polynomial entries, and three exact truncated ladder characteristic-polynomial checks. `RESULT.json` preserves the actual output. There is no numerical integration, coefficient scan, phase claim, or performance inference. This closes the proposed generic factorization shortcut, while leaving open stronger identities particular to the native model.
