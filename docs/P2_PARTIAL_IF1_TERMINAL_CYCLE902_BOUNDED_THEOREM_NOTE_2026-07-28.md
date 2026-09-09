---
claim_type: bounded_theorem
runner: scripts/frontier_cycle902_p2_kernel_attack_2026_07_28.py
independent_checker: scripts/frontier_cycle902_p2_kernel_independent_check_2026_07_28.py
actual_current_surface_status: conditional-support
---
# Finite spectrum rank and a canonical nonnegative bridge model — Cycle902

Date: 2026-07-28; corrected 2026-09-09

Type: bounded_theorem

Status: conditional finite mathematics; original-reviewer confirmation pending.

Primary runner: [frontier_cycle902_p2_kernel_attack_2026_07_28.py](../scripts/frontier_cycle902_p2_kernel_attack_2026_07_28.py)

Companion: [frontier_cycle902_p2_kernel_independent_check_2026_07_28.py](../scripts/frontier_cycle902_p2_kernel_independent_check_2026_07_28.py)

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

## The precise linear minimum

For the original108 configuration/window spectra, form their rational span V
in the degree-at-most-four Chebyshev polynomials. The exact rank is5; the
per-configuration ranks and rows are computed and retained. Therefore every
injective **linear** representation V->Q^k needs k>=5. Evaluation at five
distinct rational p values is injective because a nonzero degree-at-most-four
polynomial has at most four roots. The original six theta samples give six
distinct p values; their first five attain this bound. A modular-rank check of
independent DFS spectra supplies a second lower bound5.

This minimum concerns linear representation of the realized polynomial span.
It is not a minimum physical event space, minimal sufficient statistic, nonlinear
encoding, or axiom-selected kernel coordinate. Rank5 also does not mean every
configuration needs five coordinates or that every future model has this degree.

## Canonical bridge and positivity for the full parameter domain

For each fixed configuration, partition the union of the nine measured windows
and support into Boolean atoms by membership in those ten sets. For an atom A,
set its coefficient vector to the sum of the actual site spectra over x in A.
Use the identity inclusion of these site atoms as the supplied bridge and N=1.
Then coefficient addition reconstructs every window exactly. For every real theta,

    mu_theta(A)=sum_(x in A)|sum_(L=0)^4 c_L(x)u(theta)^L|^2 >=0.

This proves nonnegativity on the full real-theta domain through the actual
sum-of-squares construction. Grid positivity alone is not the proof; positive
Chebyshev coefficients alone would not be one either. Finite additivity follows
from disjoint sums. Normalization is possible wherever the chosen total mass is
positive; no universal physical normalization convention is inferred.

## Conditional coefficient systems

Unknowns are five coefficients per Boolean atom with N fixed to1. Matching
all window coefficients gives the bridge rows. Additional declared rows can
require theta-free atom masses, null masses on identically zero windows, or
identification of the supplied linear content sum with atom mass on support.
Exact rational ranks and augmented ranks determine linear consistency. The
N=1 restriction loses no nonzero common constant-normalizer solutions because
the original equations are homogeneous in coefficients and nu=1/N.

The original finite outcomes are retained: bridge and null-window systems
consistent on12/12, theta-free systems on5/12, and added content identification
on1/12 (single). These are properties of these explicit rows, not a complete
physical interface sheet. A consistent arbitrary coefficient vector need not be
nonnegative for all theta; the canonical squared-amplitude construction witnesses
nonnegative bridge solutions, and on single it also satisfies the added content
rows. Inconsistent linear systems cannot acquire a positive solution.

Support is itself a measured window. Under barrier=support, its mass is the
zero-step seed mass and theta-independent. Thus the content identification
requires supplied I(R)=|S intersect supp(R)|/|S|^2; e.g. ball1 gives13 versus1.
This condition is extra and is not current Record authority. Potential support
is theta-independent, while interference may alter coherent nonzero support.
For single, the original four Boolean-atom coefficient vectors and coefficient-
system nullity after fixing N are printed. Any uniqueness is confined to this
chosen atom algebra and these equations, not all measures or bridges.

The old unrestricted894 verdict, restriction to three historical878 candidates,
monitor covariance lift, and claim that only IF1 remains physically open are
withdrawn. A nonempty target with empty fibre can carry zero mass even for a
support-faithful event measure. The canonical atom model here is explicitly
supplied and does not identify itself with the historical878 event space.

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
