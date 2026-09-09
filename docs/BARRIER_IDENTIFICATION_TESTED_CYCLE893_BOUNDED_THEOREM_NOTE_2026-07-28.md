---
claim_type: bounded_theorem
runner: scripts/frontier_cycle893_barrier_identification_2026_07_28.py
independent_checker: scripts/frontier_cycle893_barrier_independent_check_2026_07_28.py
actual_current_surface_status: conditional-support
---
# Finite barrier fate partitions with a containment hypothesis — Cycle893

Date: 2026-07-28; corrected 2026-09-09

Type: bounded_theorem

Status: conditional finite mathematics; original-reviewer confirmation pending.

Primary runner: [frontier_cycle893_barrier_identification_2026_07_28.py](../scripts/frontier_cycle893_barrier_identification_2026_07_28.py)

Companion: [frontier_cycle893_barrier_independent_check_2026_07_28.py](../scripts/frontier_cycle893_barrier_independent_check_2026_07_28.py)

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

## The finite barrier comparison

The model retains all31 original named maps: five dilations, three restricted
erosions, six neighbor-count thresholds, six support-union thresholds, three
hulls, three keyed maps, and five controls. It also retains the six original
checker additions: radius1/radius2 closings, radius1 opening, local-density
adaptive dilation, radius3 dilation, and nearest-half rank filtering. Exact
set formulas and names are in the bounded helper. The erosion convention is
{x in R: x+S subset R}, including its explicit x in R restriction.

The finite filter means passing all1,440 supplied rotation/translation tests,
all35 depth-truncation pairs and nonconstancy on the twelve fixtures. It is not
an axiom-derived notion of physical admissibility. Every barrier receives a
full nine-window partition of **full mass polynomials**, twelve support/reach
rows and boundary-shell theta-incidence rows. Distinct class counts alone do
not determine a partition relation: P refines Q iff each block of P is contained
in some block of Q. Equal counts can be incomparable, for example
{{1,2},{3,4}} and{{1,3},{2,4}}. The corrected runner uses actual blocks.

The original31-map finite data include24 maps passing the finite filter,
quadratic class counts4 through8 among them,15/24 with no positive-length
support arrivals, and8/24 reproducing the7/12 boundary theta-incidence. The
six extra maps are evaluated separately by name; none makes a finite list
complete. The DFS companion checks every layer for all37x12 actual fixtures.
No original finite partition is promoted to an infinite barrier theorem.

For any supplied barrier with supp(R) subset B, no positive-length path can
land in supp(R), because each landing must lie outside B. Zero-step seeds on
support remain. This proves a sufficient containment condition; equality with
support is unnecessary, and the converse need not hold when paths are confined
elsewhere. Neither absence of positive-length arrivals nor theta-constant mass
means absence of zero-step mass or of motion elsewhere.

Nonempty rotation-invariant finite structuring sets give infinitely many
monotone equivariant dilation maps by the singleton argument. This proves a
family exists; it does not imply the finite fate map applies to all its members.
The original barrier-independence headline, claim that892's conditionality
“dissolves,” and radius1 locality/physical selection filter are withdrawn.
The finite checker additions already refuted the original enumeration's
completeness. Lexical supplier scans and historical ledger classifications
remain history, not a proof exhausting physical mechanisms.

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
