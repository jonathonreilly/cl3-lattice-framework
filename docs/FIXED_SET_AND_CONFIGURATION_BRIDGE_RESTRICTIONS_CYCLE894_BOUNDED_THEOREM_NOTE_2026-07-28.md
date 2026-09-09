---
claim_type: bounded_theorem
runner: scripts/frontier_cycle894_interface_attack_2026_07_28.py
independent_checker: scripts/frontier_cycle894_interface_independent_check_2026_07_28.py
actual_current_surface_status: conditional-support
---
# Fixed-set and fixed-configuration bridge restrictions — Cycle894

Date: 2026-07-28; corrected 2026-09-09

Type: bounded_theorem

Status: conditional finite mathematics; original-reviewer confirmation pending.

Primary runner: [frontier_cycle894_interface_attack_2026_07_28.py](../scripts/frontier_cycle894_interface_attack_2026_07_28.py)

Companion: [frontier_cycle894_interface_independent_check_2026_07_28.py](../scripts/frontier_cycle894_interface_independent_check_2026_07_28.py)

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

## Fixed-set obstruction with an actual fixed-set witness

Fix a finite event set E, nonnegative weights mu, and a map phi:E->Box union{bottom}
that is independent of the varied parameters. Fix **literally the same** target
set W. If Z(R0,theta0,W)=0 and Z(R1,theta1,W)>0, then
mu(phi^-1(W))=Z(R,theta,W)/N(R,theta) cannot hold at both parameter points
for any finite positive N: its fixed left side would be both zero and positive.
This theorem assumes phi and mu are fixed; a constructor lacking R/theta
arguments does not impose those restrictions on a subsequently supplied bridge.

The repaired witness uses two actual original configurations, shell1 and
offcentre_ball. Fix W to the union of their support sets (13 literal sites,
printed in the runner), at theta=1/2. This W contains both supports. In shell1,
the origin seed is outside W and all its neighbors are blocked, so mass is0.
In offcentre_ball, the unique centre seed belongs to W and every neighbor is
blocked, so mass is1. W is a supplied common target set; it is not claimed to
be a single one of the nine window-map values across the whole family.

The old witness grouped by **map name**, although W_name(R) changed with R.
That is not a fixed target set. Indeed fixed phi=id and weights mu(a)=0,
mu(b)=1 give masses0 and1 on{a} and{b}; there is no contradiction.

## Fixed-configuration ratio condition

For one fixed R, assume mu and phi are theta-independent and N(R,theta)>0 is
common to the chosen windows. On every parameter where Z(R,theta,W')>0,

    Z(R,theta,W)/Z(R,theta,W')
      =mu(phi^-1(W))/mu(phi^-1(W'))

must be theta-independent. Two exact unequal ratios at positive-denominator
samples therefore refute **this restricted bridge**, even allowing a common
parameter-dependent N. The runner retains all36 pairs on each of12 original
configurations and prints the valid denominator indices and exact ratios.
The seven original theta-moving configurations have such witnesses. The other
five are finite non-obstructions, not a proof that any specified event weighting
admits every required bridge. A theta-dependent phi, a coupled measure, or other
changed hypotheses are not excluded. Common scalar theta dependence alone can
be absorbed into N and is not an obstruction.

## Empty fibres and category restrictions

A positive mass on every event does not force every nonempty target window to
have positive mass: phi({e})={a}, mu(e)=1 gives mass0 to{b}. Window dependence
enters through phi^-1(W) even when individual event weights have no window
argument. Thus the former IF4/IF5 arity and support-faithfulness rejection rules
and the blanket25-cell verdict are withdrawn.

If a **uniform-fibre surjection** from92,260 events to729 sites is imposed,
729 does not divide92,260 (remainder406), so that special surjection cannot
exist. Arbitrary set maps remain possible. If a **group homomorphism** from Z11
to the order24 proper cubic group is imposed, its image order divides both11
and24 and hence is1. This says nothing about all bridges or transport of an
atom-level physical covariance law. Current878's corrected monitor diagnostics
are not promoted to such a law.

## Synthetic weighting data

The original894 fixture manufactured748 per-world counts totaling92,260,
formation times, and occupation1+(world mod7). Its five weight formulas give
zero-atom counts0,0,73,088,73,088,76,184. These are preserved as **synthetic**
finite calculations. The corrected runner aggregates exactly over those original
per-world definitions rather than materializing every identical event weight.
It prints every synthetic count/time and each total/formed-mass fraction.
Aggregate agreement is not original878 input identity. No878 controller, actual
trajectory, physical weighting, independent dimension count, or universal P2-first
route priority is accepted or reconstructed here.

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
