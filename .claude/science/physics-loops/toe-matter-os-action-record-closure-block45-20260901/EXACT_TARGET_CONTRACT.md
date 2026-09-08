# Exact target contract

## Frozen source object

Let `A` be the adjacency matrix of the four-cycle, `h=-A`, and `g=h+3I`.
Choose the Euclidean step `delta=log 2` and define

```text
B = 2^(-g) = (1/128) [[25,15, 9,15],
                      [15,25,15, 9],
                      [ 9,15,25,15],
                      [15, 9,15,25]],

K = B^2 = (1/4096) [[289,255,225,255],
                    [255,289,255,225],
                    [225,255,289,255],
                    [255,225,255,289]].
```

The sole quadratic matter source is

```text
S = sum_x (bar_chi_0x chi_0x + bar_chi_1x chi_1x)
    - sum_xy K_xy bar_chi_0x chi_1y
```

with Grassmann multiplication and link reflection interchanging the two
slices and barred/unbarred generators.

## Required certificates

1. **Source binding.** Preregistered claims, exact matrices, parent helpers,
   minimal axioms, and the Block 44 comparison are blob-bound.
2. **One-particle recovery.** `B` is the unique positive square root of `K`;
   both are positive and D4 invariant.  Exact spectral calculus recovers
   `g=(131072 K^2-36992 K+1311 I)/255` and hence the nearest-neighbor local
   generator `h=g-3I` without fitting.
3. **OS reconstruction.** `Theta(S)=S`; the full OS Gram is positive
   semidefinite of rank 16 and the occupation sub-Gram is positive definite
   of rank 16.
4. **CAR from the functional.** The unnormalized reconstructed fields have
   central covariance `K^-1`; `f=B psi` has exact CAR under the OS adjoint.
5. **Action-to-Fock extraction.** Coefficients of the action's actual
   cross-boundary factor `exp(bar_eta K xi)` in ordered Grassmann monomials
   equal the minors `det K[A,B]`.  Those coefficients form `Gamma(K)` with
   vacuum coefficient one.  `Gamma(I)=I` and exact coefficient/composition
   checks give `Gamma(B)^2=Gamma(K)`; no scalar residue is supplied.
6. **Transfer/generator identity.** The coefficient-derived matrix obeys
   `Gamma(K)=4^(-dGamma(g))`, verified by exact spectral projectors.  The
   reconstructed bilinear `sum f_x^dag g_xy f_y` is intertwined with the same
   `dGamma(g)`, so the transfer generator is not inserted after OS
   reconstruction.
7. **Dictionary discriminator.** The intertwiner from reconstructed fields to
   the ordered qubit-net Jordan-Wigner fields has exact nullity one and full
   rank; the analogous intertwiner to the commuting hard-core fields has
   nullity zero.
8. **Physical fixed-charge law.** In the `Q=2` sector,
   `dGamma(g)=dGamma(h)+6I`; the chemical shift changes only a global phase.
   The reconstructed `dGamma(h)` two-particle block equals the CAR square
   hopping block.
9. **Current.** Peierls differentiation of that same `h` gives the oriented
   U(1) current and exact continuity at all four sites.  This is an accounting
   bridge, not a claim that current causes Record formation.
10. **Operational discriminator.** From initial occupation `1010`, the
    opposite-corner event `0101` is CAR-dark for all real cadence.  The
    commuting hard-core comparison with the same supplied real-time
    `h` reaches it deterministically at `z*=pi/(2 sqrt(2))`.  The latter is a
    hostile comparison, not a second transfer derived from the Berezin action.
11. **Record.** The same even target/complement projectors feed one common
    CPTP pointer writer, giving disjoint deterministic pointer support at
    `z*`; later matter-only evolution fixes the pointer projectors.
12. **Scope firewall.** I-4 physical-functional identification, selection of
    this action, time units/cadence, preparation, writer/formation, pointer
    decoupling, and general Born calibration remain explicit imports.

## Hard kills

The block fails if any of the following occurs:

- `Gamma(K)` is postulated or built independently rather than extracted from
  the action cross-kernel coefficients;
- a Jordan-Wigner carrier supplies the CAR result before OS reconstruction;
- `B^2 != K`, positivity/RP fails, or the recovered generator is not `h+3I`;
- the vacuum coefficient or operator normalization is inserted by hand;
- the reconstructed transfer generator differs from the coefficient-derived
  transfer;
- a nonzero hard-core intertwiner survives;
- the writer, event, or cadence queries the product label;
- a relative-probability, Record-formation, I-4, axiom-closure, or general
  staggered-action claim is made; or
- strict prior-art review finds no reduction of the named action-to-Fock
  conditional.

Failure yields `BACKLOG_NO_PR`, zero obligation retirement, and zero TOE score
movement.  Any minimal-axiom wording remains a proposal requiring exact owner
approval.
