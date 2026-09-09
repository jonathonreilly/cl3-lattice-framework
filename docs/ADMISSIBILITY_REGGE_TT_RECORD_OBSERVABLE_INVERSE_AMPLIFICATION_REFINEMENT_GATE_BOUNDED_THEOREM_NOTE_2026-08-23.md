---
claim_id: admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_bounded_theorem_note_2026-08-23
claim_type: bounded_theorem
claim_scope: >-
  For the explicitly supplied finite L=5 Kuhn-complex Regge-plus-deficit-square
  fixtures at alpha=1/1024 and metric amplitude 1e-4, the nongauge/displacement
  Schur identity, five-complex-dimensional metric-to-edge lift fibers, response
  variation across named representatives, and raw-Fourier versus metric-encoder
  refinement mismatch are established on the enumerated branches, harmonics,
  and period pairs. No physical quotient, observable, source law, norm,
  refinement law, gravity verdict, or continuum theorem is selected.
upstream_dependencies: []
runner: scripts/admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_2026_08_23.py
---

# Finite Regge observable-lift and refinement boundary

**Date:** 2026-08-23; corrected source package 2026-09-09

**Type:** `bounded_theorem`

**Status:** finite conditional result; `audit_status=unset`

## Result

This note studies one supplied Euclidean finite model. It uses the 4D Kuhn
complex geometry exposed by
`frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py`, the
finite action

\[
  I(\ell)=\sum_h A_h(\ell)\,[\delta_h(\ell)+\alpha\delta_h(\ell)^2],
  \qquad \alpha=1/1024,
\]

and two fixed L=5 source labels. The geometry module supplies only the listed
finite functions and tables used by the runner. Its wider historical prose is
not imported as a premise.

The calculation proves two finite statements.

1. The supplied metric labels do not select a unique edge covector. Distinct
   representatives with the same metric target and flat-displacement
   annihilation give different values of the displayed inverse-response
   diagnostic.
2. Parseval-normalized raw-edge Fourier injection is an isometry on the named
   band, while identity transport of the same metric coefficients neither
   preserves the metric Gram form nor intertwines the momentum-dependent
   metric encoder on the enumerated period pairs.

These are finite nonselection witnesses for the supplied data. They do not
show that a physical quotient or refinement law cannot be derived from a
future action, state, source, or observable construction.

## Exact finite closure

The active runner imports one extracted helper containing only the exercised
`SliceModel` and batched action-gradient definitions. Those definitions are
provenance-bound to the exact reviewed Block 59 and Block 62 bytes in the
correction archive. The helper imports the current main Regge geometry module.
The active calculation does not import the historical Block 59--62 campaigns
or the historical `ARTIFACT_PLAN.md`.

For either supplied source label the L=5 edge space has dimension 75. With ten
average metric coordinates fixed, the computed real bases have dimensions

```text
49 nongauge + 16 displacement + 10 fixed average = 75.
```

Both branches solve their 49 projected equations to the stated tolerance at
metric response `1e-4`. The external edge source remains the supplied
Moore--Penrose convention used to define this fixture. It is not derived as a
physical source law.

## Schur identity and phase ratio

Let the finite real Hessian in orthonormal nongauge and displacement bases be

\[
  H=\begin{pmatrix}A&B\\B^T&D\end{pmatrix},\qquad
  S=D-B^TA^{-1}B.
\]

For projected observable columns `(o_n,o_d)`, block Gaussian elimination gives

\[
\begin{aligned}
 o^TH^{-1}o
 &=o_n^TA^{-1}o_n\\
 &\quad +(o_d-B^TA^{-1}o_n)^TS^{-1}
              (o_d-B^TA^{-1}o_n).                    \tag{1}
\end{aligned}
\]

This follows directly by multiplying the triangular block factorization of
`H`; it is not inferred from the numerical residual. The primary checks (1)
on all 48 named shifted or cancelled phase-paired responses. An independent
dense calculation also checks (1) when the fixed two-by-two form is negative
definite.

Call the first term `F(o)` and the second `C(o)`. On every executed fixture
`F(o)` is definite. Congruence by `|F|^{-1/2}` therefore justifies

\[
  \rho(o)=\max\left|
  \operatorname{eig}\bigl(F(o)^{-1}C(o)\bigr)\right|,       \tag{2}
\]

with the common sign removed before the symmetric generalized eigensolve.
This is a formal susceptibility ratio for the supplied finite Euclidean
Hessian. The calculation supplies no Lorentzian covariance or matter/source
second variation.

## Affine metric-to-edge lift fibers

At a named nonzero momentum, the metric encoder
`M(k): C^10 -> C^15` has rank ten. For a metric covector `t`, the dual lift
equation is

\[
  M(k)^\dagger o=t.                                      \tag{3}
\]

The full solution set is

\[
  o=o_{\rm MP}+n,\qquad n\in\ker M(k)^\dagger,            \tag{4}
\]

and rank-nullity gives a five-complex-dimensional affine fiber. The metric and
gauge definitions give `G(k)=M(k)T(k)`. Hence a conserved target satisfying
`T(k)^\dagger t=0` obeys

\[
  G(k)^\dagger o=T(k)^\dagger M(k)^\dagger o=0            \tag{5}
\]

for every representative in (4). The companion checker reconstructs this
factorization and a conserved target on 32 period/axis/harmonic fixtures from
the same finite fixture and Regge metric/gauge definitions. This checks the
implementation against a second calculation; it is not an independent source
of those shared definitions.

For the primary's named targets, `n_edge` is the normalized projection of the
first usable coordinate covector in the fixed `DIRS15` order into
`ker M^dagger`. The tested representatives are
`o_MP + lambda n_edge` for `lambda=(0,1,10)`, plus one full-fiber
least-squares representative. All preserve (3) and (5) within the declared
tolerances.

Across all twelve named fibers, the ratio spread ranges from `9.61` to about
`4.77e6`. Each of the eight TT fibers contains a value below one and a value
above one; the four source-tensor-labeled candidate fibers also cross one.
They are readout candidates for the already fixed source labels, not
alternative physical edge sources. The least-squares representative reduces
the dressed overlap in every named fiber, with nine reductions exceeding a
factor 50. That is another representative-dependence witness, not a selected
repair.

## Raw and metric refinement are different questions

For odd period `L` and nonzero non-Nyquist harmonic `m`, let `F_{L,m}` be the
Parseval-normalized real raw-edge Fourier encoder. Orthogonality of sine and
cosine on the finite cycle gives

\[
  F_{L,m}^T F_{L,m}=I_{30}.
\]

Thus `J_fc=F_f F_c^T` is isometric on the specified coarse raw band. The
metric encoder is instead

\[
  E_{L,m}=F_{L,m}\,\mathcal R[M(2\pi m/L)].               \tag{6}
\]

Identity transport of metric coefficients is an edge-norm isometry only if
the realified Gram matrices agree. The primary and companion checker each
compute both the generalized Gram deviation and

\[
  \epsilon_{fc}=\frac{\|J_{fc}E_c-E_f\|_F}{\|E_f\|_F}.    \tag{7}
\]

For harmonics 1 and 2 and consecutive period pairs `5->7`, `7->9`, and
`9->11`, the raw isometry residual is below `5e-12`, every generalized Gram
deviation exceeds `0.01`, and every encoder defect exceeds `0.05`. These
finite values refute this identity transport. They do not refute all possible
physical coarse/fine maps or establish a continuum limit.

## Open obligations and scope

Observable reduction or section, quotient norm, directed refinement, source
transport, state/update convergence, Lorentzian positivity, and nonlinear
constraint propagation are **distinct open obligations that may interact**.
The examples above separate several implications; they do not prove pairwise
or collective independence of those obligations.

The finite result does not select a physical law. It does not identify the
source candidates with Record observables, identify an iteration with time,
prove physical covariance, kill a gravity route, establish an all-L or
full-lattice statement, amend an axiom, move a TOE percentage, or retire an
obligation. No audit has run.

### N1 -- alternatives

Canonical or action-weighted reduction, nonlinear relational observables,
matter/source completion, typed fixed-volume refinement, connection variables,
improved actions, and Lorentzian state/update reconstruction remain open.

### N2 -- wall relations

The open obligations above may share hypotheses or solutions. The current
witnesses establish no theorem that one wall is independent of another.

### N3 -- hidden conditions

The calculation fixes ten average metric directions, uses a Euclidean Hessian,
uses a Moore--Penrose source convention, samples two harmonics and four odd
periods, and does not take a fixed-region lattice-spacing limit.

### N4 -- residual match

The finite witnesses address representative and identity-transport ambiguity
only. Wider Ward, transfer, or continuum claims from earlier campaigns are not
premises here.

### N5 -- resolution ladder

The primary covers two L=5 Hessians, 12 lift fibers, 48 phase-paired responses,
and 12 directed refinement comparisons. The companion checker exercises a
genuinely separate negative-fixed Schur case. Its 32 metric/gauge fixtures and
12 refinement comparisons reimplement the calculations while sharing the
declared finite fixture and Regge metric/gauge definitions.

### N6 -- partial closure

A derived physical section or a typed coarse/fine map would close one part of
the open boundary without settling the other parts.

### N7 -- steelman

The Moore--Penrose lift is reproducible and could later be selected by physical
structure. The current finite data alone do not supply that selection.

### N8 -- historical recurrence

Earlier route discussions are preserved in the exact review archive as dated
history. Repetition of a question is not evidence for a particular answer.

This packet supports the displayed finite underdetermination witnesses. It
does not claim route exhaustiveness or an impossibility theorem.

## Historical custody

The original note, runner, cache, all four authored `ARTIFACT_PLAN.md` endpoint
versions, all 19 reviewed input bodies, and the complete 47-artifact original
review packet are preserved byte-for-byte under
`.claude/science/physics-loops/regge-refinement-7335-correction-20260909/`.
Historical plan and route-preference prose has no current scientific authority.
The existing main `ARTIFACT_PLAN.md` is unchanged.
