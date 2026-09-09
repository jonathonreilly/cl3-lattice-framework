---
claim_id: admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_bounded_theorem_note_2026-08-23
claim_type: bounded_theorem
claim_scope: >-
  For one explicitly supplied translation-invariant twenty-two-edge reflected
  curvature action at mu=1/1024, two separately chosen stationary sections
  each meet a metric-coupled vertical pole on one declared real momentum path.
  At spatial momentum (pi/2,0,0), the thresholded odd-sector gauge-border
  Laurent polynomial has fourteen finite nonzero roots and its local TT-plus
  covariance has negative raw one- and two-step Hankel witnesses. These are
  finite numerical statements under the displayed conventions and tolerances;
  they do not exhaust section atlases or select a physical gravity law,
  boundary state, transfer, source, Record clock, refinement, or continuum.
upstream_dependencies: []
runner: scripts/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.py
---

# Finite reflected-curvature section poles and TT spectral weights

**Date:** 2026-08-23; corrected source package 2026-09-09

**Type:** `bounded_theorem`

**Status:** finite conditional result; `audit_status=unset`

## Result

Consider the supplied reflected twenty-two-edge quadratic symbol

\[
 Q_\mu(q)=Q_{\rm union}(q)+\mu D(-q)^T D(q),
 \qquad \mu=1/1024,                                      \tag{1}
\]

with its ten-column common-metric map `M(q)` and exact four-column Ward map.
The calculation establishes two bounded results.

1. Each of two separately chosen twelve-dimensional complements becomes
   singular on its own declared real momentum path. At the singular point the
   full action still has rank eighteen, the Ward map has rank four, and the
   vertical null row couples nontrivially to the metric block. Thus stationary
   elimination is generically incompatible there and nonunique on its
   compatibility surface.
2. At spatial momentum `(pi/2,0,0)`, the declared odd-reflection gauge border
   has fourteen finite nonzero thresholded Laurent roots. Three inside roots
   couple to the local TT-plus row. Their residues reproduce the first nine
   gated direct moments and give negative raw one- and two-step Hankel forms.

The first result refutes continuation of those two particular sections on
those paths. It is no exhaustive atlas theorem. The second refutes a positive
raw odd-quotient transfer under the displayed Euclidean-dagger convention. It
is not a gravity failure and supplies no physical half-space construction.

## Current source closure

The active primary imports a source-only finite fixture containing exactly the
exercised action, reflection-union, metric, gauge, curvature, TT-row, and
Hankel definitions. The fixture records the hashes of the six current parent
implementations from which those definitions were extracted and imports only
`scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py`
at runtime. The parent files' wider claim prose and historical controllers are
not premises of this result.

The companion checker shares that source-only finite fixture and the
fundamental Regge tables. It independently constructs complete QR complements
and directly sums the full quotient covariance at 256 and 512 temporal modes.
Its calculation is independent of the primary's SVD complement and
Laurent-residue implementations; it is not an independent source for the
shared supplied action.

The exact original two-commit review packet, all nineteen changed endpoints,
all recovered versions, the fourteen-file campaign pack, the 87-line
historical plan append, old cache, and reviewer evidence are preserved under
`.claude/science/physics-loops/schur-poles-7338-correction-20260909/review-packet/`.
They are dated history and carry no current scientific authority. The current
shared `ARTIFACT_PLAN.md` and manifest are not replaced by historical bytes.

## Stationary-section calculation

For any declared complement matrix `N`, write the action in metric and
vertical coordinates as

\[
 C(q)=N(q)^\dagger Q_\mu(q)N(q),\qquad
 B(q)=N(q)^\dagger Q_\mu(q)M(q).                         \tag{2}
\]

Stationarity of the vertical coordinate `n` requires

\[
 C(q)n=-B(q)h.                                           \tag{3}
\]

Where `C` is invertible, the induced stationary section is

\[
 s(q)=M(q)-N(q)C(q)^{-1}B(q),\qquad
 N(q)^\dagger Q_\mu(q)s(q)=0.                            \tag{4}
\]

At a simple vertical zero with normalized null vector `v`, equation (3)
implies the compatibility condition

\[
 v^\dagger B(q)h=0.                                      \tag{5}
\]

The measured row `v^dagger B` is nonzero in both cases below. Consequently a
generic metric vector violates (5); a compatible vector leaves the component
of `n` along `v` undetermined. This finite linear-algebra implication does not
rely on interpreting `h` or `n` as physical degrees of freedom.

| tested section | path parameter | momentum at pole | endpoint inertias | `||v^dagger B||` | fraction of `||B||` |
|---|---:|---|---|---:|---:|
| `N(q)=ker M(q)^dagger` | `0.20168910657044` | `(0.03771324,0,0.14080556,0)` | `(10-,2+) -> (9-,3+)` | `0.00457296` | `0.16737` |
| `N0=ker M(0)^dagger` | `0.82229616322200` | `(-2.22520254,-2.29628408,0.57407102,0)` | `(10-,2+) -> (11-,1+)` | `1.65801854` | `0.24903` |

At both points the numerical ranks are

```text
rank M = 10,  rank[M,N] = 22,  rank Q_mu = 18,
rank Ward = 4,  rank C = 11.
```

The first non-Ward singular value of the full action is respectively about
`2.98e-3` and `4.02e-3`. The Ward residual is below `1e-12`, and rotating the
basis within either chosen complement preserves the vertical spectrum. These
checks separate the vertical zero from a full-action Ward zero.

The two separately chosen charts use distinct tested complements. Their separate pole
witnesses do not prove physical independence of section regularity from any
other open obligation, and they do not exclude a patch atlas or a different
action-derived section.

## Odd bordered Laurent calculation

At spatial momentum `k=(pi/2,0,0)`, put `z=exp(i q_t)` and write

\[
 Q_k(z)=\sum_{r=-2}^{2} A_r(k)z^r.                       \tag{6}
\]

The `y <-> z` odd edge sector has dimension six and contains one odd Ward
column. The displayed gauge border is

\[
 \mathcal B_k(z)=
 \begin{pmatrix}
   -Q_{k,{\rm odd}}(z) & G_{\rm odd}(-q)\\
   G_{\rm odd}(q)^T & 0
 \end{pmatrix}.                                          \tag{7}
\]

The primary reconstructs its determinant by Laurent-polynomial arithmetic.
At the declared coefficient threshold it has support `-7,...,+7`, fourteen
finite nonzero roots, seven roots inside the unit disk, reciprocal pairing to
`1.4e-11`, and direct determinant reconstruction error below `6e-15`. The
minimum inside-root separation exceeds `3.1e-4`, the unit-circle gap exceeds
`0.44`, and every refined root passes its stated residual and simple-root
denominator gates. The smallest normalized derivative denominator is about
`3.14e-12`, so this remains a conditioned double-precision certificate rather
than an exact algebraic root theorem.

For a simple root `z_a`, right and left border null vectors give the scalar
observable weight

\[
 a_a={1\over z_a}
 { (o^T x_a)(w_a^T o)\over
   w_a^T\mathcal B'_k(z_a)x_a}.                          \tag{8}
\]

Exactly three inside roots couple on both sides to the local same-time
TT-plus row while passing the edge and border-multiplier residuals:

| root `z` | TT spectral weight | finite role |
|---:|---:|---|
| `-2.4543907e-5` | `+1.5176104e-4` | negative spectral point |
| `+2.9116902e-4` | `-2.1745073e-4` | positive point with negative weight |
| `+0.266171727` | `+0.581884812` | positive dominant branch |

Four other inside roots vanish on one TT coupling or fail the edge/multiplier
condition and contribute no retained TT residue. The three coupled residues
reconstruct the first nine directly sampled inverse-covariance moments with
maximum relative error below `7e-10`. Although the implementation computes
thirteen moments for matrix construction and diagnostics, only those first
nine are covered by the reconstruction gate.

For a positive one-step transfer, shifted moment matrices

\[
 H^{(1)}_{ij}=c_{i+j+1}                                  \tag{9}
\]

must be positive semidefinite. The executed order-two matrix has minimum
eigenvalue about `-4.43e-9`. Passing to two steps maps each spectral point to
`z_a^2` but does not change its weight. The executed order-three matrix built
from even moments has minimum eigenvalue about `-3.30e-7`. The companion's
direct 256- and 512-mode quotient sums reproduce both signs without using the
primary's Laurent roots. As a control, retaining only the positive dominant
root gives positive-semidefinite one- and two-step matrices.

These are raw quotient statements for the selected local row and Euclidean
quotient. A different physical inner product, contour, constraint, observable,
or boundary state could change the relevant transfer problem and remains to
be derived.

## Domain, tolerances, and non-imports

The finite domain consists of one translation-invariant reflected unit-cell
symbol with 22 edge coordinates, ten common-metric columns, four Ward columns,
two declared real section paths, one odd reflection sector, and one spatial
momentum. The calculation uses `mu=1/1024`, Euclidean dagger, double precision,
32 temporal samples to reconstruct coefficient matrices, 4096 samples for the
primary's direct moment comparison, and the explicit gates in the runner.

Degenerate endpoints, zero or infinite polynomial roots, the even sector,
other momenta, inhomogeneous carriers, nonlinear backgrounds, all possible
sections, exact root completeness, all-lattice limits, and continuum limits
are outside the quantified result.

No observation, fitted parameter, external literature theorem, physical
source dictionary, Record law, clock, Lorentzian inner product, state, update,
refinement map, selection principle, audit verdict, or new framework premise
is imported. No physical gravity law is selected. No axiom is amended. No TOE
percentage is assigned. No formal audit has run.

## Open obligations and stress test

### N1 -- alternative routes

A source-compatible patch atlas, action-weighted or canonical reduction,
positive half-space contour, matter/source completion, connection or holonomy
variables, improved action, nonlinear relational observable, and typed
coarse/fine state map remain open.

### N2 -- wall relations

Section regularity, quotient positivity, observable choice, boundary state,
source law, and refinement may share hypotheses or solutions. This packet
proves no pairwise or collective independence among those open obligations.

### N3 -- hidden conditions

The result depends on the supplied finite action, coefficient `mu`, two
complements, two paths, one local TT row, one momentum, reflection convention,
Euclidean dagger, thresholding, and numerical conditioning. None is promoted
to a derived physical choice.

### N4 -- residual match

The section witnesses address only continuation of the two named stationary
sections. The Hankel witnesses address only positivity of the displayed raw
odd quotient. Neither is treated as a theorem about the distinct nonlinear
source-bearing Regge action or a physical state/update construction.

### N5 -- executed resolutions

The primary resolves all 22 edge coordinates, ten metric columns, four Ward
columns, both declared paths, the complete thresholded fourteen-root set, and
the first nine gated moment reconstructions at the selected momentum. The
companion uses complete QR complements and 256/512-mode quotient sums. No
inhomogeneous per-site or Brillouin-zone-wide calculation was executed.

### N6 -- partial closure

A valid atlas could repair the section problem without selecting a positive
transfer. A positive physical form could repair the transfer problem without
choosing a metric representative. Either would be useful partial progress.

### N7 -- strongest escape

The strongest live escape is a derived half-space contour and constraint atlas
that projects the hostile modes out of physical source/observable support,
with explicit patch transitions and positivity. A changed or improved action
that preserves locality and Ward identities is another live route.

### N8 -- cross-cycle scope

Historical campaign language about gravity, Records, or terminal route closure
is not carried forward. Only the displayed finite definitions and calculated
witnesses survive as current claims. The archived original packet remains
available for provenance and later detailed audit.

## Verification

Primary:

```bash
python3 scripts/cached_runner_output.py scripts/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.py --refresh
```

Companion:

```bash
python3 scripts/cached_runner_output.py scripts/reflected_curvature_schur_poles_independent_check_2026_09_09.py --refresh
```

Expected aggregate summaries after the final source freeze are `PASS=8 FAIL=0`
and `PASS=5 FAIL=0`. These runner results support the finite claim; they are
not an audit verdict.
