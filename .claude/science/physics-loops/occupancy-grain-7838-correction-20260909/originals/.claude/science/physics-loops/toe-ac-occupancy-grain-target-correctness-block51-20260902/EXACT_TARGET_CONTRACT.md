# Exact target contract

## Objects

Let the channel set be `X={s,+,-}` with involution `K(s)=s`, `K(+)=-`.
On the K-real spectral locus write

```text
D = lambda_s lambda_+ lambda_-
  = lambda_s |lambda_+|^2.
```

For any monomial readout assign its sector-degree vector
`deg(F)=(e_s,e_d)`, where `e_d` is the total exponent across the conjugate
doublet.  Its projective grain coordinate is `rho(F)=e_d/e_s` when
`e_s!=0`.

The campaign must check exactly, first in channel-degree coordinates:

```text
deg(D)             = (1,2),  rho(D)=2,
deg(D conjugate D) = (2,4),  rho(D conjugate D)=2.
```

More generally, common power rescaling `(e_s,e_d)->k(e_s,e_d)` preserves
`rho`.  By contrast, counting one atom per K orbit gives aggregated-sector
multiplicity `(1,1)`, while counting channel atoms gives `(1,2)`.

For a positive support vector `nu=(nu_s,nu_d)` and increment
`q=(q_s,q_d)`, the support-sensitive target is

```text
r(nu) = nu_d/(2 nu_s),
r(nu+q)-r(nu)
  = (nu_s q_d - nu_d q_s)/(2 nu_s (nu_s+q_s)).
```

Thus a power/copy change can affect the candidate Koide ratio if and only if
its added support is not proportional to the existing singlet/doublet support.
This is an exact projective statement.  Turning `nu` into physical energy or
probability still requires a separately derived bridge.

## Required distinctions

1. Prove that global full-carrier `det_C` versus `|det_C|^2` is a common power
   horn and cannot by itself select a relative occupancy ratio.
2. Prove that `X/K` versus `X` is a relative-grain horn and does change the
   doublet/singlet ratio.
3. Verify from the finite Grassmann/Pfaffian construction that an invertible
   coordinate change of one complex Gaussian preserves determinant power one;
   power two requires an independent conjugate sector in that construction.
4. Check the current four axioms and approved primitives for a physical matter
   carrier, action, measure, K/CPT event codec, or orbit/channel selector.
5. Reconcile open PR #7340: its `c`-sector exponent is evaluated after the
   singlet fiber is divided out, so it is a sector-local `(1,1)->(1,2)` move,
   not a counterexample to global-power neutrality.
6. Measure the current formal blast radius from live registry/ledger data.
7. Preserve every live route capable of deriving the corrected selector.

## Positive closure gate

Positive closure requires a retained-authority chain deriving all of:

- the physical charged-lepton matter carrier;
- its action and measure;
- the K action on the physical event/channel set;
- the induced Record event partition or equivalent operational measure; and
- whether the doublet is one quotient atom or two channel atoms.

The answer may be either horn.  It must not be fitted to `r=1/2` or `Q=2/3`.

## Target-repair gate

If the present determinant-power wording is projectively neutral, return an
exact decision memo containing proposed replacement wording:

> Derive the physical charged-lepton carrier, action, measure, and K/CPT action;
> prove a presentation-independent factorization
> `Z_phys=Z_s F_d^n Z_rest` in which the singlet factor and normalization are
> held fixed, and derive whether `n=1` (one K-orbit cell) or `n=2` (two
> independently physical channel cells).  Track any global conjugate copy
> separately: it changes the relative occupancy grain only when its support is
> anisotropic between the singlet and doublet sectors.  Do not insert the
> desired charged-lepton value or readout dictionary.

This is a proposal, not an edit to the canonical obligation.

## Hard kill gates

- kill `obligation closure` if no retained action/measure/event bridge exists;
- kill `power selects grain` if both sector exponents scale together;
- kill `real coordinates imply square` if the Berezin Jacobian cancels the
  Pfaffian congruence factor;
- kill `Record supplies sector count` if Record only locks one local
  possibility and supplies no K/CPT event codec;
- kill any proof using the scalar/additive Record clause removed on 2026-08-13;
- kill `new theorem` if the exact result already exists in repo prior art;
- kill `TOE progress` unless an obligation is actually retired;
- kill PR creation unless V1--V5 all pass.
