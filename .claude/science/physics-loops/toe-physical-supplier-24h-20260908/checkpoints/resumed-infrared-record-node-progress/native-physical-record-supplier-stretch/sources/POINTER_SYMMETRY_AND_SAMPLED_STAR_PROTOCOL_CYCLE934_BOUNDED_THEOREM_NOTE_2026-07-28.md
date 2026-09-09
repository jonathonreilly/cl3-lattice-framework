---
claim_type: bounded_theorem
runner: scripts/frontier_cycle934_pointer_gates_2026_07_28.py
independent_checker: scripts/frontier_cycle934_pointer_gates_independent_check_2026_07_28.py
actual_current_surface_status: conditional-support
---
# Pointer symmetry and a supplied sampled star protocol — Cycle934

Date: 2026-08-05; corrected 2026-09-09

Type: bounded_theorem

Status: conditional finite mathematics; independent correction confirmation pending.

Primary runner: [frontier_cycle934_pointer_gates_2026_07_28.py](../scripts/frontier_cycle934_pointer_gates_2026_07_28.py)

Companion: [frontier_cycle934_pointer_gates_independent_check_2026_07_28.py](../scripts/frontier_cycle934_pointer_gates_independent_check_2026_07_28.py)

The [current governing memo](MINIMAL_AXIOMS_2026-06-29.md) sets the authority
boundary. The quantum state, tensor factors, Hamiltonian, pointer measurement,
fragment partition, times and thresholds below are supplied mathematical
objects. No historical scalar Record/additivity clause or physical formation,
basis, clock or mass supplier is restored. [Exact correction history](../.claude/science/physics-loops/pointer-6005-correction-20260909/HISTORY.md)
preserves all15 original additions, three earlier versions, and their recovered
inputs. Seven of those additions were Cycle932 runner/evidence bodies; their
presence does not accept the absent Cycle932 note or all of sibling #6001.

## Conditional collective representation

Let d>=1 arms and one pointer be qubits. On the star K_(1,d), supply

    H = -Z_S sum_(j=1)^d Z_j - lambda_pointer X_S
        - lambda_arm sum_(j=1)^d X_j,
    psi_0 = |+>^(tensor(d+1)),

with real fields, unit Ising couplings, and each arm its own fragment. The
whole-arm permutations commute with H and fix psi_0, so evolution remains in
C² tensor Sym^d(C²). In the normalized Dicke basis |z,m>, m flipped arms,

    H_(z,m;z,m) = -(1-2z)(d-2m),
    H_(z,m+1;z,m) = -lambda_arm sqrt((m+1)(d-m)),
    H_(1-z,m;z,m) = -lambda_pointer.

The arm coefficient follows by counting the m-to-m+1 spin flips between
normalized sums of computational words. The initial coefficient is
sqrt(binomial(d,m))/sqrt(2^(d+1)) in each pointer sector. This constructs the
exact2(d+1)-dimensional restriction, without needing parent campaigns or their
status labels. It does not state that this is a minimal possible representation.

For pointer-Z branch z of probability p_z>0, let a_m be the normalized Dicke
amplitudes and x_m=a_m/sqrt(binomial(d,m)). The normalized coefficient matrix
across k arms and d-k arms is

    T^(k)_(m,q) = sqrt(binomial(k,m) binomial(d-k,q)) x_(m+q).

Each left/right computational word has the same x_(m+q); their two normalized
sums give the displayed factors. Hence T T* is the branch marginal in the
symmetric k-arm basis. Its spectrum gives the branch entropy. Averaging those
entropies over p_z defines s(k). Purity and transposition yield
s(k)=s(d-k), s(0)=s(d)=0, and for d>=2 the two-arm conditional mutual
information is C_ab=2s(1)-s(2). This is a pure-branch information identity,
not an axiom concerning physical Records.

For one arm define

    chi_1 = S(sum_z p_z rho_1^z) - sum_z p_z S(rho_1^z),
    H_Z = h2(p_0),

using base-two entropy. The global X flip F=X_S prod_j X_j commutes with H,
fixes psi_0 and takes Z_S to -Z_S. Thus the pointer-Z probabilities are exactly
(1/2,1/2) at every real time, and H_Z=1. Pointer-Z total-variation drift from
that initial distribution is zero under these hypotheses. This symmetry does
not establish the separately defined X-control or commutator-ordering test.
For any product state across the pointer/arm cut, pointer conditioning at t=0
leaves the arm state unchanged, so chi_1(0)=0. The excess equals chi_1 in this
preparation. Therefore the content conjunction

    H_Z >= .05, chi_1 >= (1-delta)H_Z, chi_1-chi_1(0) >= .02

reduces to chi_1>=1-delta when delta<=.98. This implication includes the
supplied deltas .05,.10,.20; it is not asserted for arbitrary thresholds.

## Exact zero-pointer-field product branches

When lambda_pointer=0, Z_S is conserved. The normalized arm branch is a
product of d identical one-qubit states

    v_z(t) = exp[-it(-(1-2z)Z-lambda_arm X)] |+>.

Consequently every conditional arm entropy s(k) is zero, and

    chi_1(t) = h2((1+|<v_0(t),v_1(t)>|)/2)

is independent of d. This follows from the two nonzero eigenvalues of an
equal mixture of two pure states. The absence of the pointer transverse term
is sufficient for this independence, even with a nonzero supplied arm field.
The finite field ablations below retain that useful mechanism statement;
they imply no uniform perturbation order when the pointer field is restored.

If both fields vanish, the overlap is cos(2t), giving
chi_1=h2((1+|cos(2t)|)/2). Its period is pi/2. For delta=.1 let c* in (0,1)
solve h2((1+c*)/2)=.9. The first content interval is

    [t0, pi/2-t0], t0=acos(c*)/2,
    width=pi/2-2t0.

Numerically t0=.596990388538 and width=.376815549720. These formulas repeat
by integer multiples of pi/2 at zero total field. For d>=2 the conditional
pair statistic vanishes there, so the supplied pair gate does not clip that
interval. For d=1 there are not two fragments, so the pair-qualified event is
absent despite a content window. Exact pi/2 periodicity is not asserted at
nonzero fields: the actual d3/lambda_pointer=lambda_arm=.1 example changes
chi_1 by about .00531070565634 between .7 and .7+pi/2. Nonzero-field revival
rows remain finite scan observations with their actual domain.

## What window counting proves

On a specified real interval [a,b] and infinite grid phase+n h, h>0, the exact
number of samples is max(0,floor((b-phase)/h)-ceil((a-phase)/h)+1). It is
floor((b-a)/h) or that number plus one. Finite-horizon clipping must occur
before applying the formula. A single interval gives consecutive true grid
indices, so counting its points determines that run. To replace an entire
predicate by that one interval requires the additional hypothesis that it
exhausts the relevant true set. Neither the collective reduction nor a finer
scan proves such a hypothesis for every degree or field.

If content and independence hold on intervals [a,b] and [c,e] in the relevant
region, their intersection is [max(a,c),min(b,e)] when nonempty. This is the
conditional clip identity; an independence gate already true at the content
opening permits the simpler shared-opening/minimum-closing formula. Scattered
sets, extra windows or an absent pair require their actual sets to be used.

Distinct continuous windows may merge into one discrete run when their gap
contains no grid point. The actual abstract control [ .2,.31 ] union
[ .39,.51 ] gives four consecutive samples .2,.3,.4,.5 on the .1 grid.
Counting only the first interval gives two and the wrong persistence decision.
This is a counterexample to the unrestricted counting helper, not a claim that
those exact intervals occur in a frozen star corpus. The repaired rule first
forms union membership at every sample and then counts the consecutive run
starting at the first true sample. The elementary single-interval law remains
valid under its own hypotheses.

## Supplied discrete protocol and its missing physical premises

Use sample times .0,.1,...,1.2 plus a declared phase. The model event requires
d>=2, the content conjunction above and C_ab<=.02. The first event must occur
by time1, and its run must contain at least three consecutive true samples.
A full historical protocol decision additionally requires pointer drift<=.10
at the event, X-control passing across the relevant grid, and the separately
specified commutator-ordering condition. Drift is zero here by symmetry.
X-control and commutator ordering are explicit external hypotheses in this
correction, not calculated or derived from the Z statistics.

The executable discrete decision therefore takes all three control clauses
as explicit booleans and refuses omitted/non-boolean clauses. Its finite star
tables set them true to evaluate the conditional implication only. A false
clause prevents the corresponding YES. The accompanying tests execute these
countercases. No output YES is a physical certificate or a completed original
full-protocol verification. In particular no universal one-window theorem,
star degree threshold, basis choice, formation event or clock follows.

## Genuine bounded evidence

The primary freshly regenerates the original seven-field opening table at
lambda_pointer=lambda_arm in {.0125,.025,.05,.075,.10,.15,.20}, d=2..8, with
content threshold .9 and opening bracket [.30,.78], using the original
collective formulas and bisection routine. Every original field/degree value
is retained and compared. At each sampled field it records the maximum-minus-
minimum spread, shift relative to the zero-pointer-field one-arm opening,
spread/lambda² and spread/[lambda² log(1/lambda)], and the finite log-log fits.
C=max of those seven spread/lambda² ratios is explicitly a sampled envelope.
The same-sample inequality holds by construction and is not counted as an
independent scientific test. No uniform interval bound or O(lambda²) or
logarithmic asymptotic order is asserted. Adding a function vanishing at those
seven fields changes no sample and can change unsampled or small-field behavior.

Fresh zero-pointer-field controls use d=2,4,8, arm field0,.1,.7 and time0,.7,2.4,
comparing the collective expression with the one-qubit overlap formula and
checking product-branch entropy. The zero-total-field threshold is checked
at its explicit edge. An independent literal-bit Hamiltonian and literal
partial trace compare chi_1,H_Z,s1,C_ab at four small original-review probes:
(d,lambda,t)=(2,.1,.7),(3,.1,.7),(3,0,.7),(2,2,.7). It directly checks the
matrix global-flip symmetry. No Dicke coefficient enters that full-bit matrix.
Numerical agreement below1e-10 is a declared finite tolerance, not a proof of
an asymptotic coefficient. Both routes share the named NumPy eigensolver.

The fresh conditional grid table uses d=1..8, equal fields .05,.10, deltas
.05,.10,.20 and phases0,.01,.05, with13 samples per row. These are discrete
calculations, with the explicit external-control hypotheses above. Four finite
revival scans use (d,lambda)=(3,0),(3,.05),(3,.1),(5,.1), step .025, horizon[0,3].
The copied actual Cycle932 interval counter and Brent solver report sampled
blocks; no unseen-interval or global-uniqueness guarantee is inferred.

The previously literal-True C5 control now executes its advertised synthetic
predicate, true on [.6,.9] and[1.8,2.1], through that very counter at step .05
and horizon[0,3]. It must return two blocks with those endpoints. Replacing the
counter result by an empty list must fail the same assertion. This exercises
the actual retained counter and checks a corresponding fault, while preserving
the original false-green output unchanged. Method labels alone are not tests.
The actual own-note input guard is also challenged with a wrong expected hash.

## Original evidence and scope disposition

All four original caches, six JSON receipts, four source runners and the
original note remain exact historical recovery. The seven vendored Cycle932
bodies are included in that15-path inventory. Three earlier versions retain
their original timing/digest and inference history. The fresh active surface
uses one bounded Cycle934 primary, its actual companion and one model helper;
the old Cycle932 programs are not restored as active controllers. The useful
Cycle932 interval/phase/width evidence survives as historical tables, with the
actual counter function incorporated into the corrected model.

The primary reads the archived934/932 receipts as explicitly historical data.
It preserves old ablations, later-lobe, clipping, phase, width, original corpus
and seal results; it does not restamp the old210.6-second932 campaign or wider
ancestor restrictions as fresh runs. Historical ten-cell seal ordering and
new-field distinctions remain recoverable, not a newly executed holdout.
Historical absence of a finding, quote agreement or a recorded PASS supplies
no present scientific grade. The original absent932 note and sibling #6001
are not silently accepted. All actual runtime inputs are source-bound to the
current governing memo, own note, model, companion and two used historical
receipts. Other recovered inputs remain custody only. Current main science
and all reserved scopes remain unchanged. Formal audit is deferred.
