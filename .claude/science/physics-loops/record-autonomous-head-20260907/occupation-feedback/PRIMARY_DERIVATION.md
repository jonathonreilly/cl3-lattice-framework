# Occupation-following head: independent derivation and preregistered design

This is a supplied changed formation law, not a consequence of the axioms. For
head v and incident live edge (v,w), use B_ez=K_ez c_w†c_v. Summing native sign
branches gives B_e†B_e=n_v(1-n_w); the total outgoing matter rate is gamma R_s,
R_s=sum_liveincident n_v(1-n_w). It is generally not scalar. No identity refusal
completion may be added to R_s to recover a graph-degree waiting law. Capping
the energy lift still requires the appropriate refusal complement if the source
support is unsafe, but the frozen global safe support makes that inactive.

Use the direct integral of common total energy Q, with matter Hamiltonian
H_s=H_live+Delta livefuel. At fixed Q every energy-lifted B is the bare matter
B. H_total=Q I; the no-jump map is exp(-iQt)exp(-gamma R_s t/2). Although R_s is
diagonal in the occupation basis, it need not commute with H_s. Thus replacing
this no-jump evolution by exp(-iH_s t) in the reduced matter sector is wrong.

For an edge path p of length k<=4, each initially allowed occupation x maps
uniquely through the directed fermion hops to a final occupation f_p(x), with
fermion sign s_p(x). It is invalid if any source site is empty or target occupied.
At each source mask/head, let r_l(x) be the number of live vacant neighbors of
the occupied head in the evolving occupation. Valid hops imply r_l(x)>=1.
The final occupation map is injective on its valid domain because each hop is
invertible on its allowed source set. It is not an isometry on the whole sector.
The native sign maps for the first four connected/nonbridge deletions are fair
CAR-gauge isometries. Summing their probabilities cancels the factor2^-k; each
individual native-sign branch has2^-k of the edge-path probability.

Initial joint amplitude in the occupation/Q gauge is
F_x(Q)=sum_a <x|P_0(a) psi> beta(Q-a-12Delta).
For fixed dwell tuple t_l and path p, the unnormalized final matter/Q amplitude
is gamma^(k/2) s_p(x) exp[-gamma sum_l r_l(x)t_l/2] exp[-iQ sum_l t_l] F_x(Q)
at occupation f_p(x). At final matter energy b and Q=E+b+(12-k)Delta,
component (x,a,b) has battery shift u=a-b+kDelta and coefficient
<x|P_0(a)psi><b|f_p(x)>s_p(x).

For a density cross term x,y with initial energies a,a' and final energies b,b',
tracing a common battery E contributes K[(a-b)-(a'-b')]. The total-Q phases
contribute exp[-i(b-b') sum_l t_l]. Integrating the probability density of the
specified k jumps over every t_l>=0 gives the exact product
  L_xy(b-b')=product_l gamma/[gamma(r_l(x)+r_l(y))/2+i(b-b')].
The imaginary sign is fixed by ket exp(-iQt) and bra exp(+iQ't), with
Q-Q'=b-b' at common E. This kernel is NOT the normalized scalar exponential
average and its diagonal factors are1/r_l(x). Only after all contractions is
the path density normalized by its trace. It is incorrect to normalize each
occupation contribution or average its rates before integrating.

Group allowed x by their entire ordered rate tuple. For each group g and initial
energy a construct v_ga=sum_{x in g} s_p(x)<x|P_0(a)psi>|f_p(x)>.
Project v_ga into the final eigenbasis. Sum every g,h,a,a',b,b' amplitude pair
with the overlap K and the rate-pair L_gh(b-b'). This is finite and can be
implemented using70final modes, few initial energy groups and a small number
of rate tuples, without any continuum discretization or time quadrature.

The direct battery first moment uses exactly those amplitudes, b=b' after the
matter trace, the zero-finalgap factor L_gh(0), and
 [48.5+(a+a')/2-b+kDelta]K(a-a'). This moment is unnormalized; divide by the
same path trace for its conditional value. Matter energy and fuel expectations
then give a ledger test, never the definition of EB. Source-selection changes
the conditional total-energy distribution, so the unconditional initial mean
is NOT the correct ledger for each normalized path. Directly compute the
path-conditioned initial Q moment with F_x(Q), or sum over the complete
reached-plus-trapped ensemble to compare with the initial total mean.

For exact path probabilities, trace orthogonality f_p(x)!=f_p(y) for x!=y
forces x=y, but F_x(Q) still contains initial-energy coherence. Define
q_x=integral |F_x(Q)|²dQ=sum_aa' <x|P_a psi><psi|P_a'|x>K(a-a').
This is generally not |psi_x|²: the initially factorized energy battery becomes
correlated in the Q gauge. Then P(path)=sum_validx q_x product_l1/r_l(x).
Rational transition weights are exact conditional on x. The q_x are finite
spectral numerical values, so total path probabilities are not asserted rational.
The initial occupied-head and empty-head sectors can both have positive mass;
all r=0 configurations are absorbing dark sectors. Traverse each initial x,
updating mask/head/occupation, retaining all terminal mass, including depth0.
At any depth, reached mass plus earlier trapped mass equals1. Terminal dark
sectors can also arise with occupied head but no vacant live neighbor.

Preregistered probe only: freeze cube,N4,pulse.7,head0,gamma=t=Delta=1,
sine[48,49],cap97; no tuning. First implement the directed-hop/rate exact
configuration census and grouped endpoint algorithm in scratch. Report all
positive-probability four-event prefixes and their probabilities; graph paths
with zero law weight must be reported, not silently excluded. Post-event only:
conditioning on a future selected edge makes pre-event states a distinct
nonlinear selection problem, not the earlier unconditional pre-epoch average.
Do not reuse any fuel-monotonicity lemma. Controls must include dark mass,
wrong scalar graph rates, omitted fermion phases, wrong gap sign, omitted fuel,
path-weight normalization, direct EB and independent occupation-gauge integration.
No transport conclusions will be drawn before a separately frozen execution
and independent check. This document precedes reading the native agent memo.

## Execution freeze (root authorization before execution)

Execute all45graph-prefix post surfaces through4events, keep zero-probability
rows visible, census all configuration trails to traps. No pre-instrument
surface. Preserve every cross-rate coherence. Validate trace/N/Hermiticity/
positivity and independent conditioned-Q ledger; compare exact-rational per-x
reach/trap weights after weighting with q_x. Mutation families: use|psi_x|²,
constant graphdegree rates, lose dark mass, omit cross-rate coherences, omit
fuel, and compare path energy to unconditional initial mean. No optimization
of scientific parameters. Algorithm/resource optimization leaves the frozen
law and all paths intact. The prototype was syntax-checked only before this
execution authorization; no occupation-feedback numerical result was read.
