# Four matched ablations: finite current support is not fuel starvation

The observed disappearance is failure of a thresholded support comparator, not
exact disappearance of currents. At actual pre2, the largest live current in each
path lies between 0.0032046973 and 0.0295257787; pre4 between 0.0052532649 and
0.0320832909. None has four live edges above magnitude 0.02. All densities in all
four ablations remain inside [0.1,0.9].

The preregistration was written before the ablation run. No inputs or parameters
were fitted. The runner imports only the frozen independent orbital checker,
checks its SHA256, and writes all 360 matched rows (90 per ablation). Its A currents
agree with the frozen actual result exactly. The checker received only an expressly
authorized head-metadata correction between diagnosis runs; no physics changed.

## Results

Counts of path-prefix rows with at least four live currents of magnitude >=0.02:

| Surface | Number of rows | A: width1 + waits | B: width1 + zero waits | C: ideal + waits | D: ideal + zero waits |
|---|---:|---:|---:|---:|---:|
| pre1 | 3 | 3 | 3 | 3 | 3 |
| post1 | 3 | 2 | 3 | 3 | 3 |
| pre2 | 6 | 0 | 6 | 4 | 6 |
| post2 | 6 | 0 | 6 | 6 | 4 |
| pre3 | 12 | 8 | 12 | 12 | 8 |
| post3 | 12 | 6 | 12 | 12 | 6 |
| pre4 | 24 | 0 | 24 | 24 | 12 |
| post4 | 24 | 0 | 20 | 18 | 10 |

C and D are the formal overlap-kernel-one limit, not normalized finite-energy
battery preparations. Zero waits are mathematical endpoint comparisons, not an
alternative autonomous realization with the declared gamma.

For pre2, removing wait averaging while retaining the actual battery restores all
six support passes; removing battery dephasing while retaining waits restores four
of six. The remaining ideal-with-waits failures have first deletion edge 0=(0,1),
with paths [0,3] and [0,4]. Both pass in D. Thus wait dynamics/averaging alone can
produce this loss for those frozen paths; battery dephasing contributes additional
failures for the other four. This is a matched comparison, not an additive loss
allocation: phases and thresholding prevent such an interpretation.

For pre4, either removing wait averaging or replacing the finite packet channel by
the ideal channel restores all 24 passes. Their combination in the actual channel
is implicated in universal threshold failure. Curiously D passes only 12/24:
finite-battery zero-wait mixing and ideal-channel wait dynamics can each distribute
current onto additional live edges. Coherence removal is therefore not uniformly
monotone in this support metric. A single ranking of battery coherence, waiting,
and transport is false even in this finite fixture.

In D the matter covariance is precisely the prepared C0 for every mask. Only the
list of observable live edges changes. Its drop from five supported edges at pre1
to three or four at pre4 is therefore exactly deletion of some initially carrying
edges for this comparator. This separates a direct topology contribution, but
A/B/C also change or evolve the covariance, so D does not furnish an additive
causal decomposition of those cases.

The original trajectory front comparator passes 24/24 in every ablation. For A,
the selected-edge pre1 magnitudes are 0.2105157918, 0.1760624278, 0.1760624278, so
its trajectory maximum is already above 0.05 at event1. That comparator does not
establish sustained late-event transport; the pre2/pre4 support failures remain.

## Energy and resource interpretation

Actual battery mean rises from 48.5 to weighted 50.58261239969652 at post4; eight
fuel quanta remain. The independent direct energy-domain moment and conservation
ledger agree within 1.8e-13, caps are safe, and each allowed edge rate is the same
gamma. The observed failures do not result from exhausted fuel, a cap refusal, or
insufficient battery energy suppressing event rates. The finite packet's translation
overlap attenuates matter coherences; that is distinct from availability of energy.
Ideal ablations remove this resource-coherence effect mathematically without
supplying a physically normalized infinite-coherence battery. No entropy,
locality, renewal, or finite closed-apparatus conclusion follows.

## Does a generic real Hamiltonian force zero event-mean current?

No. In a real orbital eigenbasis, each covariance entry evolves as
C_ab(T)=C_ab(0) exp[-i(e_a-e_b)T]. Positive-time event averaging takes its integral
against the declared waiting density. That integral is generally complex and
nonzero; neither reality of H nor nondegeneracy forces the averaged covariance
to be real. A phase-pulsed input is already complex. Even real input covariances
can develop imaginary off-diagonal entries unless an additional invariance holds.
The nonzero A pre2/pre4 maxima above directly exclude exact generic cancellation
as the explanation for this fixture's failed thresholds.

There are precise more restricted statements. Any real covariance has zero
instantaneous currents for the declared imaginary antisymmetric bond operators.
A real covariance that commutes with real H stays real and has zero current.
For real initial covariance, a time distribution symmetric under T -> -T gives
a real average because C(-T)=C(T)*; our positive exponential event times do not
have this symmetry. The infinite Cesaro time average is sum_lambda P_lambda C
P_lambda. For nondegenerate real H this is real, hence every bond current vanishes.
With degeneracies, complex coherences within a degenerate eigenspace survive and
can support stationary circulating bond currents; zero gap terms are NOT removed
by time averaging. A sufficient degenerate-case condition is that every retained
block P_lambda C P_lambda is real. These are exact algebraic statements, not
claims that the finite four-event average equals its infinite-time limit.

The actual spectra include degeneracies, and no nondegenerate approximation was
used: direct time quadrature retains all zero-gap and nonzero-gap entries. Battery
kernel grouping likewise retains every degenerate initial-energy group coherently.
One cannot explain an alternating finite support count solely by the slogan
"dephasing kills currents". The finite phases, graph-dependent spectra, coherent
blocks, and numerical thresholds all matter.

## Reproduction and limits

Run `python3 /private/tmp/toe-autonomous-orbital-20260907/diagnosis/run.py`.
See PREREGISTRATION.md, run.py, results.json (all currents/densities/path front
maxima), and summary.json. This is a bounded diagnosis, not a formal new claim or
PR. No primary source was imported, no fitting or sweep occurred, and no source
changes beyond the separately requested head metadata correction were made.
