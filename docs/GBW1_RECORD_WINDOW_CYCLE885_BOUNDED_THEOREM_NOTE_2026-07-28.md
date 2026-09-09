---
claim_type: bounded_theorem
runner: scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py
independent_checker: scripts/frontier_cycle885_gbw1_independent_check_2026_07_28.py
actual_current_surface_status: conditional-support
---
# Finite supplied window maps and the all-superset disjointness obstruction — Cycle885

Date: 2026-07-28; corrected 2026-09-09

Type: bounded_theorem

Status: conditional finite mathematics; original-reviewer confirmation pending.

Primary runner: [frontier_cycle885_gbw1_record_window_2026_07_28.py](../scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py)

Companion: [frontier_cycle885_gbw1_independent_check_2026_07_28.py](../scripts/frontier_cycle885_gbw1_independent_check_2026_07_28.py)

## Supplied finite protocol

The [current memo](MINIMAL_AXIOMS_2026-06-29.md) is the authority boundary.
The [corrected Cycles887/892 note](GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md)
provides the existing conditional context; its current source is unchanged.
No removed scalar-Record/additivity wording is reinstated. Configuration bits,
assigned depth labels, weights(1,2), source, kernel, windows and barrier below
are supplied mathematical definitions, not a physical Record or formation law.

Use the exact twelve original configurations: single, pair, shell1, ball1,
annulus_1_4, hollow_annulus, Lshape, plane_square, chain, sparse_a, sparse_b,
offcentre_ball. Their full deterministic definitions are in the bounded model
helper. The two sparse configurations use the original LCG seeds7 and2909;
content is coordinate parity and depth is one plus the rank of squared radius
about the configuration barycentre. These are finite fixtures, not a dynamics.

Use Box={-4,...,4}^3, nearest-neighbor steps, depthD=4, and a uniform real
seed1/|S| on all box sites closest to the configuration barycentre. A barrier
forbids positive-length landings on its sites; zero-step seeds remain allowed.
At fixed R and barrier, c_L(x)=count_L(x)/|S| and

    A_theta(x)=sum_(L=0)^4 c_L(x) u(theta)^L,
    u(theta)=((1-theta^2)+2i theta)/(1+theta^2),
    Z(R,theta,W)=sum_(x in W intersect Box)|A_theta(x)|^2.

The six original rational samples are1/2,1/3,2/5,1/7,3/8,5/6. The nine
explicit containment-holding windows are support; Minkowski sums with the
L1 balls of radius1 and2 and with{0,+/-2e_i}; bounding box; axis-segment
closure; size-keyed inflation at |R|>3; supplied-readout-keyed inflation at
I>6; and bounding-box union radius1 dilation. The last two keyed maps choose
support otherwise. These definitions retain the original nine-map subcatalogue;
there is no claim that it exhausts windows or follows from the axioms.

Write M_d(W)=sum_x sum_(|L-L'|=d)c_L(x)c_L'(x). Then
Z=sum_(d=0)^4 M_d T_d(p), p=(1-theta^2)/(1+theta^2). The d>0 coefficients
include both ordered cross terms. The helper computes integer path counts and
spectrum numerators before division by |S|^2, exactly preserving this rational
model. Six distinct p samples determine every degree-at-most-four polynomial.
Potential path support is theta-independent; coherent nonzero amplitude support
can shrink by cancellation. No implication from two source parities alone is
used; odd interference requires actual opposite-length-parity coarrival.

## Conditional set-map results

For any nonempty finite rotation-invariant structuring set S, W_S(R)=supp(R)+S
is equivariant under translations and proper cubic rotations, monotone in
support, and nonconstant. The singleton{0} recovers S, proving distinct S give
distinct maps. In particular arbitrary integer-radius L1 dilations survive these
**supplied** requirements. Neither Record permanence nor the absence of a
privileged site selects a detector window, barrier, centre, or dilation radius.
Barycentre and extremal-shell barycentre are two equivariant centre conventions;
the original twelve configurations distinguish them on four configurations.

The runner retains all1,440 original rotation/translation comparisons per
selected map and all35 adjacent depth-truncation comparisons. Support has zero
equivariance failures. A fixed origin cube fails1,152 comparisons, all involving
translation; the exterior nearest-neighbor shell retracts on24/35 pairs.
These finite counts are not tests over all translations or all supersets.
Dilation equivariance and monotonicity instead follow from the set identities.
The runner also retains original centre-disagreement and theta-incidence rows.

If W is defined on **all** finite supports, is monotone for every A subset B,
and W(A) is disjoint from A for every A, then W is identically empty. For any
x in W(A), disjointness implies x notin A; monotonicity gives x in W(A union{x}),
contradicting disjointness there. This proves the conditional obstruction.
It does not force a physical detector to obey those two extra hypotheses.
The shell is a concrete nonempty disjoint map that violates monotonicity.

Depth cutoff stability is a statement about the supplied finite filtration:
above the largest assigned label the truncated support equals the whole support.
It is not physical clock gauge. For barrier=support, every positive-step landing
avoids support, so support mass is exactly |S intersect supp(R)|/|S|^2 from
zero-step seeds, independent of theta. On the exterior boundary shell, the
original finite protocol gives theta dependence on seven of twelve configurations.
That conditional normalization dependence does not forbid positive, parameter-
dependent normalization and supplies no physical linear/quadratic identification.

## Retained and historical scope

The old six-coordinate classification, scalar Record authority, extent selection,
physical barrier identification, absolute clock language, and independent residual
count are withdrawn. Finite counts, explicit map constructions, filtration
stability, and the all-superset theorem above survive under stated premises.
The annular fill statistics and former audit/status/controller claims remain exact
historical evidence; no claim of fresh replay is made for them. The original
checker narrowings are preserved without treating every old printed check as a
current scientific verdict.

## Evidence and recovery

The bounded primary regenerates this unit's finite results. Its companion uses
focused independent arithmetic controls with openly shared fixture definitions;
it does not claim independence merely because it avoids importing the primary.
The current cache binds the exact note, governing memo, existing892 context,
model and checker sources. Historical controller/status/lexical-scan campaigns
are not run. All original assigned endpoints and intermediate versions, including
old878/887/892 bodies, are preserved in [correction history](../.claude/science/physics-loops/time-windows-6009-correction-20260909/HISTORY.md).
Unsupported old verdicts and historical cache totals remain recovery only.

This unit does not accept all of6009 or any other constituent scope. Existing
878/887/892/904 sources remain authoritative at their current status and unchanged.
Physical Record/readout, barrier/window selection, Born/event lift, source/action,
formation clock, dynamics and TOE closure remain open. No audit grade is applied;
formal audit is deferred by the owner.
