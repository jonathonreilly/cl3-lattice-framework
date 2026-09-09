---
claim_id: generation_count_is_spatial_dimension_on_k1_undefined_on_k0_2026_09_03
claim_type: bounded_theorem
claim_scope: "Supplied one-particle operators on even periodic finite tori: M_W=d I-H_K0/2; exact corner eigenvectors and corner-restricted binomial multiplicities for lambda>0; finite numerical ambient spectra and observable algebras at d=2,3 with L=4,6,8 and d=4 with L=4,6. Isolation is checked only at named points, with explicit noncorner collisions at lambda=2/5 and 2/3. K0 energy alone does not isolate the hw=1 corners, but its stated translation/rotation algebra contains their central projector. No physical generation, species, mass, clock, continuum limit, or kinetic-selection theorem."
upstream_dependencies: []
runner: scripts/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.py
runner_cache: logs/runner-cache/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.txt
---

# Finite Wilson corner levels and the available K0 corner projector

**Date:** 2026-09-03; source correction 2026-09-09.
**Type:** bounded_theorem
**Surface:** supplied finite operators and numerical checks.
**Audit:** deferred under the current owner directive; this note applies no grade.

The stable filename preserves the original claim's identity, not its former physical title.
The original note, runner and 24/0 historical cache are preserved byte for byte outside
active documentation discovery under `.claude/science/physics-loops/generation-correction-20260909/originals/`.
The current note corrects the former continuous isolation claim and algebraic nonselection claim.

**Primary runner:** [scripts/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.py](../scripts/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.py).
**Runner cache:** [logs/runner-cache/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.txt](../logs/runner-cache/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.txt).

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) delimit the framework interpretation.
They do not supply the one-particle Hilbert space, hopping coefficients, a physical clock,
Born readout, or identification of corner labels with permanent Records or generations.
Those physical bridges remain open. The finite calculation below declares its own operators;
no historical kinetic-class or generation campaign is a proof dependency. The old contextual
quotations and proposed cross-note edits remain in the preserved original, without importing
its authority labels or licensing a new premise here.

## 1. Supplied objects and exact affine identity (T1)

Use one particle on a periodic even `L^d` torus, `L>=4`, with plain shifts
`T_mu|x>=|x+mu>` and `T_mu|p>=exp(-i p_mu)|p>`. Put
`eta_mu(x)=(-1)^(x_1+...+x_(mu-1))` and define

```text
H_K0  = sum_mu (T_mu + T_mu^*)
H_K1r = sum_mu eta_mu (T_mu + T_mu^*)
H_K1  = i sum_mu eta_mu (T_mu - T_mu^*)
M_W   = sum_mu [I - (T_mu + T_mu^*)/2] = d I - H_K0/2.
```

The last identity follows by collecting terms. Hence `[H_K0,M_W]=0`, whereas the
computed norm `||[H_K1,M_W]||=27.71` at `d=3,L=4` is nonzero.
The two compared operator families are `H_K1+lambda M_W` and `H_K0+lambda M_W`,
with supplied real `lambda>=0`. The affine identity assigns no physical leading order,
kinetic selection, derivative expansion, or calibrated mass to either family.

The dense matrices have integer or half-integer coefficients; eigenvalues, residuals,
ranks and trigonometric enumerations in the runner use floating-point tolerances.
Exact identities below follow from the displayed algebra, rather than from a small residual.
No volume sequence or continuous parameter interval is certified by the finite scans.

## 2. K1 corner sector and pointwise ambient spectra (T2)

For the periodic corner waves `c in {0,pi}^d`, each `sin(c_mu)=0`, so
`H_K1|c>=0`, `M_W|c>=2 hw(c)|c>`, and
`(H_K1+lambda M_W)|c>=2 lambda hw(c)|c>` for every real lambda.
The staggered terms anticommute in pairs; their squares give
`H_K1^2|p>=4 sum_mu sin(p_mu)^2 |p>`. Thus the kernel is exactly the `2^d`
corner span on these even periodic grids. At `lambda>0`, the restriction to that span
has multiplicities `C(d,k)` at `2 lambda k`; at `lambda=0` all those restricted levels coincide.
This does not determine the ambient multiplicities when noncorner eigenvalues collide.

At `d=3,L=4,6,8`, the historical finite outputs are retained:

- Kernel dimensions `8/8/8`; corner-span residual at most `8.0e-15`.
- Corner identities were checked over `lambda=(0.1,0.25,0.5,1,2)` in d=3,
  and at `lambda=0.1` in d=2,4; combined residual at most `1.3e-14`.
- At each of `lambda=0.1,0.25,0.5`, ambient multiplicities are `(1,3,3,1)`.
- At `lambda=1` they are `(5,3,3,5)/(1,3,3,1)/(5,3,3,5)`.
- At `lambda=2` they are `(2,10,10,2)/(1,3,3,1)/(2,18,18,2)`.
- At `lambda=0.1`, clearance from the actual orthogonal complement of the corner span
  is `1.500/1.182/0.844`. The unperturbed nonzero floor is
  `2 sin(2 pi/L)=2.0000/1.7321/1.4142` for these three sizes.

These are named points, not an isolation window. At `d=3,L=4`, the noncorner wave
with grid label `n=(3,2,2)`, or `p=(-pi/2,pi,pi)`, obeys
`H_K1 v=-2v` and `M_W v=5v`, hence has energy `-2+5 lambda`.
At `lambda=2/5` it meets the hw=0 corner energy 0 (ambient multiplicity 2, corner 1).
At `lambda=2/3` it meets the hw=1 energy `4/3` (ambient multiplicity 4, corner 3).
Both lie below 1. The original continuous isolation statement and the statement
that hw=1 stays exactly threefold through 1 are false.
The corrected clearance diagonalizes the corner orthogonal complement, so a colliding
noncorner state cannot disappear merely because its eigenvalue equals a corner level.

On the hw=1 corner span, the plain translation characters have one minus sign and
all other signs plus. The proper signed axis cycle acts transitively on these d labels.
Its powers and the rank-one character projectors produce every matrix unit `E_ij`.
Thus their generated algebra on this supplied corner span is `M_d(C)`, with scalar commutant.
At d=3, lambda=0.1 the ambient energy-0.2 space equals this span at L=4,6,8:
dimension 3, algebra dimension 9, commutant 1, translation residual `9.3e-15`,
unitary cycle with `R^3=I` and trace 0. These compressed observables are not a theorem
that plain translations or the cycle are global symmetries of the whole K1 operator.

## 3. K0 energy degeneracy and a central selector (T3)

`H_K0|p>=2 sum_mu cos(p_mu)|p>`. At d=3 and L=4,6,8 its zero set contains
`20/24/68` grid momenta and no corners. Proper-rotation orbit sizes are
`[8,12]/[12,12]/[8,12,24,24]`. On that kernel `M_W=3 I` (residual `4.0e-14`).
Globally,

```text
H_K0 + lambda M_W = d lambda I + (1-lambda/2) H_K0.
```

For `lambda!=2`, its eigenspaces are the same as H_K0's, with shifted/rescaled energies.
At `lambda=2` the entire matrix collapses to `2d I`; it is an important exception to
any assertion that the energy-level structure is unchanged. The d=3 band extrema
of H_K0 have multiplicity 1 at energies +6 and -6 for all three sizes.
Those are one-dimensional eigenspaces, not derived particle species.

At lambda=0.1, the level containing the hw=1 corners has energy 2.2,
`sum cos(p_mu)=1`, and dimension `15/27/39`. Plane-wave residual is `1.9e-14`.
The stated algebra here uses **all momentum projectors** and the axis cycle R;
its orbits are `5/9/13` triples, one of them the corner triple. The algebra is
`M_3(C)^(direct sum 5/9/13)`, with dimension `45/81/117` and commutant `5/9/13`.
This does not mean that no algebraic corner selector exists.

For every even L define the translation polynomial

```text
P_corner = product_mu [(2/L) sum_(j=0)^(L/2-1) T_mu^(2j)].
```

A finite geometric sum shows each factor is 1 on translation characters +1 or -1
and 0 on the other characters. Thus this is the orthogonal projector onto the entire
corner span. It commutes with every momentum projector, and the axis cycle preserves
that span, so it is central in the stated algebra. On the K0 level `sum cos=d-2`,
a corner satisfies `d-2 hw=d-2`, hence hw=1. The restricted projector has rank d.
In particular at d=3,L=4 it has rank 3 inside the 15-dimensional level. There it is
`product_mu (I+T_mu^2)/2`. This is a nonzero, proper, available algebraic selector;
K0 energy alone does not isolate the triplet, and availability does not privilege it
as a physical readout or generation sector.

## 4. Finite flux and boundary comparisons (T4, T5)

At d=3,L=4 the normalized plaquette flux is +1 for hopping t=1 and -1 for
both t=eta and t=i eta. At lambda=0.1, the mixed hopping
`t=i eta-lambda/2` has two flux values `-0.995012 +/- 0.099751 i`.
These exclude equivalence by a site-local phase frame to either displayed uniform-flux
representative. They do not classify all covariant hopping models or forbid other
symmetry/field structures. Lambda remains a supplied coefficient.

With antiperiodic wrap, H_K1 has no zero modes at L=4,6,8 in d=3.
The minimum absolute energies are `2 sqrt(3) sin(pi/L)=2.4495/1.7321/1.3257`,
on `64=4^3` near-corner momenta; H_K0 has `0/56/0` zero modes.
This is a finite boundary comparison, not a claim that a limiting multiplet or
finite-L Wilson splitting has been proved. In the periodic real frame t=eta,
H_K1r has `8/0/8` zero modes. The specified phase `U=diag(i^|x|)` conjugates
H_K1r to -H_K1 at L=4,8 but not L=6: this phase is periodic only if L is divisible by 4.
No classification of all possible frame maps is asserted.

## 5. Finite dimensional comparison (T6)

The d=2 sizes are L=4,6,8 and the d=4 sizes are L=4,6; there is no d=4,L=8 row.
All numerical rows from the original are retained:

| `d` | K1 zero modes | corner multiplicities at `λ=0.1` | hw=1 corner count | `hw=1` algebra | K0 zero modes | corners in K0 kernel | K0 level holding the `hw=1` corners |
|---|---|---|---|---|---|---|---|
| 2 | `4 = 2^2` | `1+2+1` | **2** | `M_2(C)`, dim 4, commutant 1 | `6 / 10 / 14` | 2 | dim `6 / 10 / 14`, algebra `20 / 36 / 52` |
| 3 | `8 = 2^3` | `1+3+3+1` | **3** | `M_3(C)`, dim 9, commutant 1 | `20 / 24 / 68` | 0 | dim `15 / 27 / 39`, algebra `45 / 81 / 117` |
| 4 | `16 = 2^4` | `1+4+6+4+1` | **4** | `M_4(C)`, dim 16, commutant 1 | `70 / 198` | 6 | dim `28 / 68`, algebra `208 / 528` |


The corner-restricted hw=1 count is `C(d,1)=d` for the supplied label set and observable algebra.
The K0 ambient level algebra is reducible in these finite rows, while the corner projector
remains available. For d=2 and d=4, corners can also lie in the K0 kernel when hw=d/2.
No asymptotic kernel-growth result is inferred from these censuses.

## 6. Interpretation and evidence boundary

This calculation supplies no preferred kinetic branch or perturbative ordering, no
physical generation/species identification, charged-lepton labels, mass hierarchy,
Born rule, physical clock, permanent Record formation, many-body dynamics, or continuum
limit. Calling an hw=1 label count a physical generation count would require those extra
supplies and a physical selection of the observable sector. The available K0 projector
also defeats the old algebraic argument for declaring such a count undefined on that branch.
The old physical title, prose reading, interface promotions and isolation window are withdrawn.

All 24 original check IDs and their numerical predicates are retained. Two added scientific
checks directly test the noncorner collisions/complement clearance and the nontrivial central
projector, including the lambda=2 scalar collapse. A source/input guard binds this note and
the current memo before computation. The runner imports no local scientific helper or data.
Its declared dense cases are finite (largest matrix 6^4=1296); rank and spectral checks are
numerical at their printed tolerances. A successful final cache is evidence for this bounded
protocol, not detailed claim certification or an audit grade.
