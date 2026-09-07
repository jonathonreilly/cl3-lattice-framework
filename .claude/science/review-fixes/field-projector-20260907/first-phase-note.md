---
claim_id: spin_half_cubic_ice_finite_detuning_projector_maxwell_stiffness_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite-component nonnegative Green-function and constant-trial mixed-estimator identities for the supplied cubic-ice ring Hamiltonian; corrected sampling and nominal shared-reference covariance code with bounded tiny-state controls. Original finite-population production figures are historical and unvalidated after the sampling overflow finding. No fresh finite-detuning positivity, convergence, thermodynamic stiffness or physical Maxwell certificate is supplied by this repair."
upstream_dependencies:
  - minimal_axioms
  - spin_half_cubic_ice_positive_topological_electric_stiffness_bounded_theorem_note_2026-09-03
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
  - u1_role_encoded_doubled_incidence_nearest_neighbor_gauge_law_bounded_theorem_note_2026-09-03
runner: scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py
---

# Conditional cubic-ice projector and finite-protocol electric-flux fit

**Original date:** 2026-09-03. **Source repair:** 2026-09-07.

The exact finite Green-function and mixed-estimator identities below survive.
The historical production receipt does not validate the repaired producer:
positive burn caused one more sample write than the arrays allocated, and the
flux-fit uncertainty omitted the shared zero-flux reference covariance. This
first repair corrects those source defects and scopes the interpretation. It
has not rerun the original production protocol or established fresh positive
finite-detuning coefficients.

The supplied link carrier, ice constraint, Hamiltonian, detunings, initial
components and projection prescription are model data. They are not selected
by the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). The
[first-order parent](SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md)
provides a finite-protocol comparison, while the
[RK parent](SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)
separates exact finite algebra, declared sampling, trial-state twist controls
and an imported phase comparison. The
[role compiler](U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md)
does not supply a one-qubit-per-physical-site implementation of this ice-ring
Hamiltonian.

**Runner:** [projector source](../scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py).
**Historical cache:** [unchanged original payload](../logs/runner-cache/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.txt).
The cache intentionally retains its original source and input hashes, old
12/0 check count and 266.42-second runtime. It is stale for this corrected
source and current helpers; it is neither replaced by a tiny-control receipt
nor presented as successful corrected production.

## Exact conditional finite-component identities

On an even periodic cubic carrier let each positive-coordinate link carry
`n_i(r) in {0,1}`, and impose three occupied incident links at each vertex.
Let `N_f(C)` count alternating geometric square plaquettes, including the
multiplicity of distinct geometric moves with the same endpoints. With ring
amplitude one, define

```text
M=3 L^3,
H(V)=D-A+(V-1)N_f,
D_CC=N_f(C),
delta_v=V-1.
```

Here A counts geometric allowed square flips on a specified connected
component. Fixed-flux initialization does not assert that all configurations
with the same flux form one component, nor that a selected component has the
smallest energy among them. Singleton frozen components are allowed.

For `0<=V<1`, set `G=I-H/M`. Each geometric allowed flip contributes `1/M`
to G, and

```text
G_CC=1-V N_f(C)/M >= 1-V > 0,
b(C)=sum_D G_DC=1-delta_v N_f(C)/M >= 1.
```

Thus G is nonnegative, irreducible on a nonsingleton connected move component,
and has positive diagonal. Its Perron vector is the strictly positive lowest
H eigenvector, since its eigenvalues are `1-E/M`. The positive diagonal also
avoids a period-two power-iteration obstruction. At the RK endpoint V=1 the
connected graph Laplacian has the constant ground vector directly; no separate
aperiodicity assertion at that endpoint is needed.

The exact weighted single-walker step multiplies the incoming weight by b,
chooses a geometric plaquette uniformly among M, and flips a flippable square
with probability `1/b`. Hence each allowed geometric move has transition
probability `1/(M b)`, and the remaining probability is `G_CC/b`. After
weighting, this is precisely the G column. Geometric multiplicities are summed.
The implementation is not a Trotter approximation to another Hamiltonian.
Fixed-population resampling and finite projection time remain approximations
to iterating G on the whole component; a finite population is not its exact
Perron vector.

The constant-trial row sum is `E_local(C)=delta_v N_f(C)`. For the exact
positive eigenvector psi_0, symmetry gives

```text
E_0=<1|H|psi_0>/<1|psi_0>
   =delta_v sum_C N_f(C) psi_0(C)/sum_C psi_0(C).
```

This is an exact finite mixed-estimator identity. Applying the same expression
to a finite branching population defines an estimator, not an identity between
that population and the exact eigenstate.

The original complete-L2 diagonalizations reported:

| V | Phi | E_0 |
| --- | --- | --- |
| 0.95 | 0 | -0.402736506 |
| 0.95 | 1 | -0.328353309 |
| 0.90 | 0 | -0.810822412 |
| 0.90 | 1 | -0.664101443 |

Their eigenvector mixed-estimator check is distinct from the old 2048-walker
comparison, which is affected by the unsafe sampling loop. The repair's tiny
exact controls can check finite algebra and transitions without validating
that historical stochastic comparison.

## Corrected sampling convention and unchanged production settings

One attempted sweep consists of M attempted Green-function steps per walker.
Complete `burn_sweeps` whole sweeps with no sample, then take one sample after
each of the following `sample_sweeps` complete sweeps. The sample step numbers
are exactly

```text
(burn_sweeps+1) M, ..., (burn_sweeps+sample_sweeps) M.
```

This also defines zero burn: the first sample is after M steps. The burn
endpoint itself is never a sample. The corrected loop uses a strict `>` burn
boundary, checks the index before every write, and requires the final count
to equal the allocated sample count. It does not enlarge arrays or quietly
change the requested sample count. Invalid negative counts, empty populations,
nonpositive sample/resampling counts and unsupported delta_v>0 are rejected.

The original production settings remain unchanged:

| Runs | Walkers | Classical warmup | Projector burn | Samples |
| --- | --- | --- | --- | --- |
| L2 exact-energy comparisons, both V and Phi=0,1 | 2048 | 100 | 200 | 500 |
| L4,6,8 full Phi=0,...,L/2 curves | 256 | 100 | 150 | 300 |
| L10 Phi=0,L/2 endpoints | 256 | 100 | 150 | 300 |
| Compound L8 endpoint controls | 512 | 150 | 250 | 500 |

The two detunings are exactly V=0.95 and V=0.90. The fixed original seeds,
resampling interval `max(16,M//8)`, ten time blocks and 480-second production
budget remain in the source. The sample correction must be tested before any
new expensive run; no production run is part of this first repair.

The compound L8 control changes population, initialization family, warmup,
burn, sampling length and seeds together. The start flips two oppositely
oriented noncontractible lines at zero net flux, then inserts the required
flux. A nonlocal preparation operation does not prove its endpoint is in a
different local-move component. Agreement under this compound change would be
a finite sensitivity diagnostic. It would not separately establish population
convergence, projection convergence, mixing, component equality or a global
minimum. Finite warmup likewise gives no mixing guarantee.

The actual execution checks recompute one walker's flippability at each sample
and every final walker's flippability, Gauss charge and flux. The complete
local proof and tiny transition controls are separate mathematical evidence.
The production code does not instrument every accepted flip's full invariants.
The original effective-population floor `>0.90` and final distinct-state floor
`>0.25` at L>=4 remain guards against immediate collapse, not convergence proofs.

## The same fitted estimator with shared-reference covariance

Let independently estimated sector energies have nominal block errors sigma_i,
and let index zero denote the common zero-flux reference. Define

```text
x_i=Phi_i^2/L,
y_i=E_i-E_0,
w_i=1/max(sqrt(sigma_i^2+sigma_0^2),1e-12)^2,
a_i=w_i x_i / sum_j w_j x_j^2,
U_fit=2 sum_i a_i y_i.
```

The weighted through-origin point estimator is unchanged. Under the stated
nominal independence of the underlying energy estimates,

```text
Sigma_ij=delta_ij sigma_i^2+sigma_0^2,
Var(U_fit)=4 a^T Sigma a
          =4 [sum_i a_i^2 sigma_i^2 + sigma_0^2 (sum_i a_i)^2].
```

The second term was omitted off the diagonal in the original slope error.
The repaired six-error comparison uses the square root of this estimator's
nominal variance. For a deterministic three-flux test with U=1 and all energy
errors 0.1, the old error 0.1714285714 becomes 0.2099562637 while U stays one.
The one-endpoint formula already includes the two energy errors; no off-diagonal
shared-reference term exists when there is only one difference.

Ten blocks of one resampled population do not establish independence,
autocorrelation control, negligible population bias or calibrated confidence
coverage. Correlation between separate energy estimates, if introduced by a
future paired sampling design, must be propagated from that actual design.
The fixed six-error threshold is nominal diagnostic arithmetic, not a rigorous
confidence statement. The old summary cache has no per-flux block histories
from which a corrected production covariance or new error bars can be recovered.

## Coarse-field comparison, not the bare microscopic electric square

The supplied microscopic observable is `E_i(r)=epsilon(r)(n_i(r)-1/2)`.
Every microscopic link satisfies `E_i(r)^2=1/4`; therefore the literal operator
`(U/2) sum_links E_link^2` is `3 U L^3/8` times identity. It cannot distinguish
these flux sectors.

A distinct **supplied coarse-field comparison** defines a uniform c-number
field `e_bar_x=Phi/L^2`, `e_bar_y=e_bar_z=0` and volume L^3. Its energy functional
`(U/2) L^3 |e_bar|^2` gives `U Phi^2/(2L)`. This normalization motivates the
predictor. A fitted coefficient for selected-start finite-protocol energies
does not derive that functional from the bare microscopic electric square,
select a coarse-graining law, or measure a physical electromagnetic U.

The maximum Phi=L/2 obeys `Phi/L^2<=1/(2L)`, so the declared endpoint sequence
has shrinking mean field density. That fact alone neither removes finite-size
bias nor justifies a thermodynamic stiffness. The original four alternative
fit predictors are |Phi|, |Phi|/L, Phi^2 and a nonzero-sector step. Their residual
comparisons remain fixed finite model diagnostics; failure of one comparison
would not rule out every possible phase or response model.

## Historical numerical record and pending production evidence

The following are literal old summaries, **not repaired production results**:

| V | U4 | U6 | Compound-control U8 | Endpoint U10 | Mean U/abs(delta_v) |
| --- | --- | --- | --- | --- | --- |
| 0.95 | 0.162431 | 0.158859 | 0.161363 | 0.167899 | 3.252761 |
| 0.90 | 0.323246 | 0.316443 | 0.321798 | 0.322970 | 3.211140 |

The old joint quadratic residuals were 0.00014972 and 0.00007401, with old
relative volume spreads about 5.6% and 2.1%. Their apparent agreement and
positive signs do not cure the sampling overflow. The original cached source
hash is `8becfe5e91a731e38bc056b69044f03f8c40ced504641ba6893f3410893c1706`, and
its declared-input fingerprint is
`3c58cd9e3a66fa268a03c885c7305ba4d1c4a505800468e4342a58d8e4625766`.
Neither identifies the repaired runner on corrected current-main helpers.

The first-order parent reports the finite-protocol component-fit comparison
`U_fit/abs(delta_v)=3.183873 +/- 0.154786`. The code retains 3.183873 as the
original central benchmark and retains the original 20% comparison; it is not
a universal constant or a calibrated equality test. Its actual parent note and
helper source are declared and read as inputs. Current parent qualification of
component selection, nominal errors, supplied phase comparison and physical
implementation remains applicable.

A future production run must generate a new source/input-bound receipt from
the corrected sampler and report the corrected nominal covariance errors.
The unchanged requirements are four L2 comparisons within the original
`max(8*error,0.004)` tolerance; six-nominal-error positivity of full curves and
endpoints; same-volume quadratic residual below 0.25 times linear; compound L8
agreement within 15%; joint quadratic residual below 0.20 times the best of four
controls; volume spread and first-order central comparison below 20%; and the
existing population/diversity floors. No expected PASS is supplied now. These
finite checks would still leave independent convergence and physical-bridge
obligations open even if a future run passed them all.

## Program, prior-art and no-go boundaries

This unit supplies exact finite Green-function/mixed-estimator algebra and a
repaired executable protocol. It does not yet resolve the original question
whether the reported finite-detuning flux coefficient survives corrected
production. The RK parent's finite algebra and variational twist controls do
not become a matched relaxed magnetic response through this electric producer.
No positive magnetic stiffness, photon pole, charge potential, thermodynamic
phase, physical-site composite or empirical electromagnetic dictionary is
established here.

The original note cites Hermele, Fisher and Balents,
[“Pyrochlore Photons”](https://arxiv.org/abs/cond-mat/0305401), as prior art for
the supplied spin-half spin-liquid setting. This repair makes no model/method
priority claim and supplies no new verification of an imported phase argument.
That literature context is distinct from actual tiny controls or stochastic
production executed in this unit.

N1 records executed, historical and open work separately. The first repair's
bounded controls are exact tiny transition columns, local/incremental count
checks, resampling/reference checks, compiled sample-count/bounds tests and a
shared-reference covariance calculation. The original full production is
historical and awaits replacement. First-order and phase arguments are parent
context. Charge response, transverse spectrum, matched magnetic response,
separate convergence ladders, component classification and a physical-site
compiler remain possible future work. This is not an enumeration proving
completeness of a fixed number of independent routes.

N2 names unresolved tasks without an independence theorem: thermodynamic and
dynamical control, physical-site implementation, matter/backreaction, and law
selection/empirical identification. Their pairwise implications have not been
established here. Some measurements may constrain several tasks at once; they
must not be counted as independent walls merely because they have different
names.

N3 preserves all supplied carrier, Hamiltonian, component, flux, estimator,
resampling, finite-size and runtime assumptions. N4 distinguishes exact local
identities from repaired-code controls and still-pending production; no parent
residual is retired merely by an old positive table. N5 distinguishes actual
sampled/final instrumentation from a proof about every local move. N6 leaves
alternative carriers, coarse observables, estimators, start components and
convergence plans open. N7 acknowledges the sampling overflow, shared-reference
error, finite-population bias and uncertain mixing as substantive limitations.
N8 records the historical attempt to continue the first-order fit to two finite
detunings, without treating its old green receipt or imported magnetic/phase
context as a current result. No no-go or formal audit verdict is issued.

## Current author status and trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: >-
  No reviewed downstream physical consumer is selected. The historical
  finite-detuning flux fit needs safe corrected sampling and same-estimator
  covariance before new production evidence can support a finite comparison.
source_of_blocker_text: review_loop
reachability_to_target: supports
artifact_role: theorem
next_trace_action: >-
  Independently confirm the corrected source and bounded tiny controls, then
  consider a separately authorized fixed-protocol production run with current
  inputs. Preserve convergence and physical identification as open obligations.
conditional_surface_status: >-
  Exact finite G and mixed-estimator algebra for supplied model data; corrected
  source with tiny controls; no fresh production evidence or physical coefficient.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: >-
  Conditional exact algebra is separated from pending stochastic output.
  Author classification and tiny controls do not confer a scientific grade.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Original provenance: #7941 head `8ac1ccdfa1735fd6facdf910defb964469fba35a`, base
`2814c6768e4d7b38048f70ad7883b4951cb12da3`; its three source files remain exact
at #7966 head `369f785003f19c1ec5e8c4a6f1155c2827a7986b`. This source repair uses
landed main `94e90cbf928cb35fa1b50e894cd897c94b73077f` and its corrected helpers.
The original note, producer and cache are preserved verbatim in the external
author/review packets; the selected in-repository cache remains byte-identical
historical evidence. The unlanded eleven-path source/receipt unit is not an
input or dependency of this correction.
