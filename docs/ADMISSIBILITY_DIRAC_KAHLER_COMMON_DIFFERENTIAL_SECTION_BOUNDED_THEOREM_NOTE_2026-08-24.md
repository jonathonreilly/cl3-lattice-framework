---
claim_id: admissibility_dirac_kahler_common_differential_section_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "the current 8-by-4 cover, its four chart differentials, and the supplied equal-weight section"
depends_on:
  - admissibility_dirac_kahler_curved_carrier_dependency_bounded_theorem_note_2026-08-17
runner: scripts/admissibility_dirac_kahler_common_differential_section_2026_08_24.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A common differential on the supplied redundant section

**Type:** `bounded_theorem`

**Campaign block:** 181. **Status:** corrected bounded theorem; formal audit is
deferred. The five original changed-path occurrences, including the historical
manifest, remain recoverable exactly.

The [primary](../scripts/admissibility_dirac_kahler_common_differential_section_2026_08_24.py)
uses the current [Block 128 carrier](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md),
the underlying [Block 105 matrices](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Chart orbit and graph section

On the supplied dimension-32 cover, each of the four chart differentials
$d_o$, $o\in\{0,1\}^2$, is nilpotent of rank 16. With the plain shifts
$S_o\in\{I,U_x,U_t,U_tU_x\}$,

\[
d_o=S_od_{00}S_o^{-1},\qquad d_oS_o=S_od_{00}.
\]

The graph map $A_0v=(S_ov)_o$ therefore has invariant range under
$\operatorname{diag}(d_o)$. More generally, $S_oC_o$ is an intertwiner
whenever $C_o$ commutes with $d_{00}$. The primary checks this formula for
the nontrivial control $C_o=I+d_{00}$. The naive arithmetic mean of the four
$d_o$ is different: its square has rank 32, so averaging the matrices does
not preserve nilpotency.

## Antiperiodic quotient

Every displayed quotient differential is a nilpotent $16\times16$ matrix of
rank eight. Consequently

\[
\dim\ker d=8,\qquad \operatorname{im}d=\ker d.
\]

The complex is acyclic, but its kernel is not empty: it has eight linearly
independent zero modes at the level of the differential. The temporal chart conjugacy
uses the antiperiodic wrapped shift; the periodic control differs at four
entries. Spatial conjugacy uses the periodic spatial shift. These calculations
identify the wrap in this displayed descent only.

## Supplied section Hodge and completion

For the equal-weight supplied point

\[
H_s=\frac14\sum_o S_o^T H S_o,
\]

the primary checks symmetry, positive definiteness, trace
$927831123589/27222868400$, and 96-entry differences from both the raw curved
$H$ and the flat identity reference. These three finite controls do not
exclude other Hodge constructions or establish a unique section.

The completion $Q(H,d)=mH+i(Hd+d^\dagger H)$ is chart-covariant when both
$H_s$ and $d$ are transported. The two supplied Block-128 physical
completions have different exact $z^{14}$ characteristic coefficients, so
that pair is not similar.

The complex centralizer of the displayed quotient $d_{00}$ has dimension
128. This is the dimension of a commutant. It is not the dimension of a Hodge
moduli space or of a section family, and it does not make equal weights
canonical or unique.

Finally, the spatial translation commutator has rank 32 for the section
completion and also rank 32 for the flat-Hodge control. The measured property
is translation noninvariance on these two matrices; the shared rank is not a
curvature invariant.

## Disposition

The chart orbit, graph intertwiners, corrected quotient acyclicity, supplied
section-Hodge controls, covariant completion, pairwise characteristic
contrast, commutant dimension, and translation-noninvariance controls are
retained. Empty-kernel language, exhaustive Hodge exclusion, canonical or
unique equal weights, moduli-dimension identification, and curvature labels
are withdrawn. Nothing is registered or adopted.
