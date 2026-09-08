---
claim_id: the_link_models_pair_update_conserves_plaquette_parity_and_the_2x2x2_gauss_sector_splits_into_937_winding_components_bounded_theorem_note_2026-09-04
historical_claim_alias: link_model_qmc_pair_update_parity_winding_sectors_2x2x2
claim_type: bounded_theorem
claim_scope: "For the supplied pure spin-1/2 quantum-link Hamiltonian H=-lambda sum_f P_f, lambda=1, ordinary tensor composition, no matter, and the two declared finite geometries/backgrounds: the 2x2x2 Gauss basis has 9600 states in 937 plaquette-flip connected components and 125 winding classes defined by explicit integer sum(2E) cut flux; zero winding contains the 864-state component plus 16 frozen singletons. Its full and 864-component first spectral gaps are 1.6276099336 and 2.2257853859; an observable decay also requires its spectral overlap, component/ensemble, temperature/projection and estimator. The same-face pair switch preserves each face's parity. The cycle-image rank is 0 on the 47-state L8 ladder component and 10 on the 864-state torus component, an algebraic index1024, not a Gibbs-weight fraction or a mixing certificate. A legal four-face odd-parity closed word is explicitly replayed. Original seeded SSE energy/bin diagnostics agree on the ladder and disagree on the torus; no exclusive causal diagnosis or calibrated coverage is inferred. The six-face selection factor is geometric, not actual legal-loop acceptance. Short restricted-sampler timing is not phase or mixing cost. C Gauss equations are checked at bounded checkpoints, not every flip; cumulative diagnostics and required engine failures are enforced. Equal-time E_e squared is checked; positive-lag code remains unvalidated. All physical role placement, readout, probability and dynamics remain supplied; no three-dimensional phase, infinite-size limit, physical photon, universal sampler necessity, or physical Record formation law is derived."
upstream_dependencies: []
runner: scripts/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.py
---

# The pair update conserves plaquette parity: 937 plaquette-flip connected components and 125 winding classes on the 2x2x2 Gauss sector

**Original date:** 2026-09-04. **Source correction:** 2026-09-08.
**Type:** bounded_theorem. **Status:** bounded conditional source; audit unset.
**Primary runner:** [`scripts/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.py`](../scripts/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.py).
**Current cache:** [`logs/runner-cache/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.txt`](../logs/runner-cache/link_model_qmc_pair_update_parity_winding_sectors_check_2026_09_04.txt).
The filename retains the original historical wording; its title and claims distinguish components from winding classes.

This unit studies a supplied finite quantum-link model and a particular closed-string stochastic-series-expansion (SSE) update. Its useful exact obstruction is narrow: the same-face operator-pair switch cannot change plaquette parity. A finite graph calculation shows that this invariant excludes legal histories on the 2x2x2 torus, although it imposes no additional parity restriction on the declared ladder component. It does not establish the thermal weight of the excluded histories, mixing in the reachable subset, or correctness of all other implementation details.

The original fixed-seed ladder energy comparisons pass their declared numerical diagnostic; the torus comparison fails by 135.5 bin-standard-error units. These numbers are retained. The parity obstruction is a valid independent mathematical result, but neither the numerical discrepancy nor the C scan proves that it is the only cause of the sampler's bias. No phase conclusion follows.

## Machine status and exact target

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
artifact_role: theorem
next_trace_action: "Independent source confirmation of the narrowed finite claims and required evidence; formal audit remains deferred until a solid TOE."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
no_go_packet_status: "five-route procedural minimum is unmet; no packet PASS asserted"
```

The target has four parts: T1 finite Gauss components, cut-flux labels and spectra; T2 the exact pair-parity invariant and finite cycle-image ranks; T3 exact finite thermal references and the original seeded sampler witnesses; T4 a geometric factor, a bounded timing witness and their interpretation limits. All 21 original check IDs A1–A5, B1–B4, C1–C4, D1–D4 and E1–E4 remain.

A1–A3, B1–B4 and C1 use exact integer/bit arithmetic. A4–A5, C2–C4 and E3 are finite floating-point spectral checks at stated tolerances. E1 evaluates a finite geometric formula, not an actual Monte Carlo acceptance. D1–D4 and E2 are required finite-run diagnostics/witnesses. E4 checks the declared source boundary and a finite readout counterexample; it is not an exact theorem proved by a literal `True`.

## Imports, setting and authority

Every mathematical object used in the finite proof is defined here and reconstructed by the standalone runner. The runner imports NumPy, SciPy and the standard library, and compiles its embedded C source. There are no local science-helper imports or externally supplied numerical tables. The note and the current quoted minimal-axiom memo are literal fingerprinted inputs; the runner verifies the current memo bytes and reads the current source boundary.

The following are non-load-bearing historical/context pointers, not newly accepted parent proofs: the corrected current #7911 ring note (finite L8 and historical L20 comparisons), #7893's supplied link notation and electric c-number, and `NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md` (the elementary finite-matrix trace obstruction). The model below redeclares those ingredients. The corrected current #7959 free-end formulation is a representation alternative outside this closed-string update's scope; its full campaign is not rerun or independently approved here. Historical “open PR” or phase language in earlier versions is not current authority.

The four framework axioms are quoted from the [current minimal-axiom memo](MINIMAL_AXIOMS_2026-06-29.md), not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." The lattice is physical. **Qubit**: "Each site has a domain of local possibilities." and "The full one-site
possibility domain has algebraic presentation `M_2(C)`." **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
**Record**: "Records form.", "When present, a record locks exactly one admissible local possibility.", "A site never carries more than one record; records are
permanent.", "Only records are readable." and "A readout value is determined by record content alone."


The mathematical carrier is one supplied two-state link role per edge with ordinary tensor composition. No axiom derives that placement, the Hamiltonian or equilibrium probability law. If a supplied readout assigns the link Z content to `E_e=Z_e/2`, it supplies that diagonal value. Fixed Z-record correlations do not supply off-diagonal `U_e` or `P_f` expectations. The two legal configurations 166 and 2196 are joined by face5: their normalized plus/minus superpositions have identical complete Z-record probability distributions but `P_5` expectations +1 and -1. An additional measurement/readout protocol is needed. Imaginary-time auxiliary configurations are not permanent physical records, and this sampler is not a physical Record formation law.

## Definitions and obligation graph

On the periodic L^3 torus, links belong to their tail vertex. The L2 torus has 24 links, 8 degree-six vertices and 24 four-link faces. The height-one cylinder ladder at L8 has 24 links, 16 degree-three vertices and 8 faces.

```text
E_e = Z_e/2, U_e = (X_e+iY_e)/2 = sigma^+_e
G_v = sum_e s_(v,e) E_e - rho_v, with s=+1 outgoing and -1 incoming
W_f = the oriented four-link product, P_f = W_f + W_f^dag
H = -lambda sum_f P_f, lambda supplied and set to 1
rho_v = 0 on the torus
2rho(t_i)=(-1)^i, 2rho(b_i)=-(-1)^i on the ladder
```

`E_e^2=I/4`, so an electric sum of these squares is a c-number on this supplied spin-half carrier. A face's ordered link tuple `(p,q,u,w)` is flippable iff `b_p=b_q`, `b_u=b_w`, and `b_p!=b_u`; it flips exactly those four bits. The configuration graph has legal Gauss states as vertices and legal one-face flips as labeled edges. A closed walk's parity is the vector of face counts modulo2.

Define the integer cut winding `w_d=sum_(tail coordinate d=0, link direction d) 2E_e`. Gauss divergence and local plaquette flips preserve these three cut fluxes. Winding is a coarser invariant than graph connectivity here; it is not a name for an arbitrary component.

P0 is the supplied geometries, carrier, backgrounds, composition and H. P1 uses P0 for basis/graph/winding/spectra. P2 uses P0 for the pair-update invariant and graph cycle rank. P3 uses P0 for complete finite-component Gibbs references. P4 compares actual fixed-seed runs with P3 under the declared sampling protocol. P5 reports bounded timing/geometric factors and limits. No inference from P4 or P5 to a general physical law, sampler mixing, or phase is made.

## T1: finite Gauss basis, components, winding and spectra

The full L2 Gauss basis contains **9600** states. Every one is explicitly checked at every vertex; the maximum doubled Gauss residual is zero. Slab enumeration assigns each as-yet-unassigned incident link and enforces the current vertex equation. Final re-evaluation is independent of the enumeration's filtering step.

For every even L, the declared configuration

```text
e(v,x)=(-1)^(v_y+v_z), e(v,y)=(-1)^(v_z+v_x), e(v,z)=(-1)^(v_x+v_y)
```

has zero divergence: each direction's incoming and outgoing values agree. Exactly half of the faces are flippable by the same coordinate-sign rule. Direct finite checks give 12/24, 96/192 and 324/648 faces at L=2,4,6. This analytic seed statement does not extend the enumerated component/spectrum results to larger L.

Legal one-face flips split the L2 basis into **937 plaquette-flip connected components**:

| Component size | Number |
|---:|---:|
| 864 | 1 |
| 464 | 6 |
| 252 | 12 |
| 136 | 8 |
| 36 | 6 |
| 6 | 144 |
| 1 | 760 |

Their sizes sum to9600. Actual cut labels on every basis state give **125 winding classes**, and every actual flip preserves them. Zero winding contains the864 component plus16 frozen singletons. Thus even specifying zero winding does not identify a unique reached component or ensemble.

The analytic configuration lies in the864 component. At tolerance1e-9, its ground energy is `-9.0267209135`, equal to the global ground energy; the original full sparse ground vector has unit weight there. The full first excitation gap is `1.6276099336`, while the864 component's own first gap is `2.2257853859`, larger by36.8 percent. The original full first-excitation vector has weight about1.1e-29 on the864 component. Complete spectra of all937 finite blocks now also check the lowest full levels: exactly six components carry the first excited energy, with actual cut labels `(±2,0,0)` and permutations.

This distinguishes finite spectra, not a universal correlation-decay rate. A spectral decomposition of an observable correlation weights each level by its matrix element. A local electric observable in the864 component can couple at2.2257853859; the transverse Fourier observable `E_y(k=(pi,0,0))` instead first couples at2.5172790443. The actual corrected runner constructs this normalized Fourier diagonal observable and checks its total first-level weight below1e-20; the preserved independent review found below3e-30. A constant or conserved observable need not yield a decaying gap at all. Any extracted rate therefore needs the reached component/ensemble, observable overlap, projection or temperature, and estimator assumptions. Winding conservation alone determines none of these choices.

## T2: the actual pair-parity obstruction

Write `H_(1,f)=C I`, `H_(2,f)=lambda P_f` and `K=sum_f(H_(1,f)+H_(2,f))`, so `H=N_p C-K`. With a length-M padded operator string, the supplied weight is

```text
exp(-beta N_p C) beta^n (M-n)!/M! product of nonidentity matrix elements.
```

The implemented update inserts/removes diagonal identities, switches two consecutive operators at the same face when its stated link-sharing window test allows it, and cyclically rotates the string with the corresponding boundary configuration. Cyclic rotation preserves the trace weight; it does not prove complete sampling of a trace ensemble.

The pair switch changes the number of off-diagonal operators at any face by0 or±2. Insert/remove diagonal operations and rotation do not alter that parity. Starting from an empty string, only the even-parity subset is reachable. This elementary invariant holds for the stated switch independent of simulation statistics.

On the47-state ladder component the graph has104 edges and58 independent cycles. On the864-state torus component it has3456 edges and2593 cycles. Exact GF(2) reduction of the face-parity image gives ranks0 and10 respectively, unchanged between the declared depth-first and breadth-first trees. The depth-first odd fundamental-cycle counts are0 and2159; the breadth-first counts are0 and1573. Those counts depend on the chosen basis, while image rank does not. Rank10 means an algebraic kernel index1024 on the cycle space/associated closed-walk parity map. It is **not** the Gibbs weight1/1024, a fraction of all physical histories, or a mixing-time statement.

The six faces of each of the8 geometric cubes have XOR-zero link support. This is a geometric relation only. It does not establish intermediate flippability: all720 six-face orderings for the first cube are illegal from the declared analytic seed in the preserved independent control. A genuine different odd-parity closed walk is explicitly replayed from state15798951 with face word `[20,23,14,17]`; every intermediate face is flippable, every state satisfies Gauss, the endpoint returns to the start and its face parity is nonzero. The original graph-derived fundamental-cycle witness is also retained.

Rank0 makes this particular parity restriction empty on the ladder component; it does not prove ergodicity or correct sampling there. Rank10 excludes a nonempty algebraic class on the torus but does not determine its thermal mass. For example at beta=.0001, positivity and `||H||<=24` give an even-parity thermal-mass lower bound `exp(-24 beta)=.9976028777`: the same rank need not mean weighted dominance of omitted histories. The finite beta8 discrepancy below is retained without such an inference.

## T3: finite references and original seeded witnesses

The L8 ladder basis has49 states and components47,1,1. All basis/vertex equations are checked. The47-state component has `E0=-4.8309586723`, internal gap`.9726557606`, and `<P_f>=.6038698340`. Its density is `E0/L=-.6038698340 lambda`; total energy multiplies that density byL. The historical comparison`-.6035607` is the rounded **L20** value in the corrected current ring source, not an established infinite-size limit.

Complete dense component spectra give the canonical reference `sum_j E_j exp(-beta E_j)/sum_j exp(-beta E_j)`:

| beta | L8 ladder,47 states | L2 torus,864 states |
|---:|---:|---:|
|2| -4.5151826280 | -8.6891572261 |
|4| -4.8053520382 | -9.0239679296 |
|8| -4.8305435458 | -9.0267206703 |
|16| -4.8309585028 | -9.0267209135 |

The original protocol uses seed20260903, C=2,20000 equilibration sweeps and100000 sampling sweeps in40 bins. The ladder energy residuals are`.17,.28,.33,1.12` bin-standard-error units and its beta16 `<P_f>=.604067`. The torus beta8 result is`-8.118460(.006703)`, against`-9.0267206703`, a135.5-bin-standard-error discrepancy and10.1 percent shortfall in energy magnitude.

The original C=1,4,8 comparison uses the same seed,20000 equilibration and40000 sampling sweeps. It gives respectively`-8.103150(.010723)`, `-8.122688(.017783)`, `-8.070141(.026243)`. Together with C=2 these agree within1.8 combined bin-standard-error units, and every result is far from the exact reference. These are finite seeded diagnostics. The common seed and40-bin formula do not establish independent errors across C, confidence coverage, effective sample size, autocorrelation control, equilibration, finite-M accuracy or convergence to the desired weighted ensemble. The disagreement is evidence of failure of this sampling result; the parity theorem does not isolate all possible causes.

The original historical run printed zero closure/illegal counters and equal-time`.25`; its incomplete warmup/Gauss checks did not certify all states. The corrected engine keeps cumulative warmup and production errors, checks explicit signed Gauss equations at initialization, at bounded checkpoints after sweep propagation, cyclic rotation and replay, and at termination. Cadence is `max(1,ceil((neq+nmeas)/16))`, with phase endpoints also checked. Positive state/equation counts and both warmup/final diagnostics are required independently of dump flags. These checks are **not every-flip Gauss checks** and are not complete code correctness. Every forward sweep retains the original closure/illegal diagnostic; warmup errors cannot be erased by resetting production counters.

The equal-time test is only `G_E(0)=1/4`, from squaring stored±1 spins and multiplying by1/4 on sampled strings. It cannot validate positive-lag indexing. The underlying distributional construction uses n+1 independent unit exponentials: dividing by their sum gives uniform Dirichlet spacings, and beta times their first n cumulative sums has the uniform-order-statistic density`n!/beta^n` on the ordered simplex. This elementary derivation is retained. The **positive-lag implementation remains unvalidated**: changing actual `u+tau` to`u` still passes the equal-time test while collapsing every lag. That prior mutant remains explicitly unvalidated rather than being relabeled as a passed time-map check. No physical time law follows.

Required compiler absence, compilation error, engine error, timeout, invalid/missing diagnostics, zero Gauss-check counts, malformed/mismatched bin data or invariant violation prevents successful full-unit evidence. Partial exact results may remain useful but cannot substitute for the required witness rows. Old successful-SKIP outputs remain historical failure evidence.

## T4: geometric factor, operation timing and open alternatives

The finite expression `(lambda/C)^6 N_s/binom(N_p,6)` counts geometric six-subset selection times a putative six-operator ratio. At C=2 it is9.3e-7 on L2 and1.6e-11 on L4. It is not a state-independent acceptance probability: legal intermediate states, proposal details and actual matrix elements must be checked separately. XOR closure alone supplies none of those conditions.

The original short restricted-sampler measurement at L4,beta16,C2 used8000 total sweeps, string length10871 and about.30ms per sweep, extrapolating to59s per200000 sweeps on that hardware. A fresh run reports its actual timing under the unchanged broad cost threshold. This measures operation cost for this update only. It gives no mixing time, error-controlled phase cost, performance of an unwritten algorithm, or fixed sufficient L/beta scaling. A hypothesized beta proportional toL would itself require the relevant spectral scaling, which is not established here.

Loop, cluster and worm proposals may alter the invariant in a different update. Their legality, balance, connectivity, estimator and mixing performance remain obligations. A different representation, such as the current corrected free-end formulation of #7959, is another possible route outside this closed-string invariant. No theorem says every correct three-dimensional sampler must use exactly a loop/cluster/worm, or that writing one will settle the phase cheaply.

No statement here decides whether the three-dimensional physical limit is gapped, gapless, Coulomb, ordered or a photon. The L4 row is a restricted-sampler timing/diagnostic; it is not a phase measurement. The even-L analytic seed identity is the only stated general-L result, and no continuum limit is taken.

## No-Go Discipline Gate

The target is the exact obstruction of the declared same-face pair switch on the stated closed-string representation, not impossibility of equilibrium sampling. The **five-route procedural minimum is unmet**. The current schema's quota is a submission limitation, not evidence against the parity theorem. No N1 packet PASS, new audit or independent-wall count is asserted.

**N1 — Real routes and their status.** The actual obstruction family is the closed-walk/parity formulation: direct update-count invariance and finite graph GF(2) reduction are complementary proofs/checks of the same mechanism, not five families. The actual seeded energy comparison is a numerical validation attempt and fails on the torus; it is not a second impossibility theorem. Loop/cluster/worm and free-end representations are open/out-of-domain alternatives, not falsely labeled attempted failures. No full proof of weighted sampling or mixing for them is supplied here.

**N2 — Conditional dependence.** The pair invariant and nonzero graph-image rank jointly establish the restriction; neither is an independent physical wall. Component confinement, weighted mixing and observable overlap are separate questions. Whether repairing one implies repairing another is not established; all such wider pair directions remain unresolved. No count of independent barriers is inferred.

**N3 — Hidden conditions.** The finite geometries/backgrounds, link carrier, ordinary tensor product, H and lambda, chosen closed-string representation, pair-window rule, initial component, finite-M padding, beta, seed, warmup/bin protocol, explicit signed Gauss equations and bounded checkpoint cadence are declared inputs or algorithm conditions. They are not consequences of the quoted axioms. Numerical diagonalization has a tolerance; the seed proof and parity algebra are exact. A full physical off-diagonal readout and time interpretation are additional open interfaces.

**N4 — Residual matching.** The current ring context supplies only a finite comparison whose values are recomputed here; its historical L20 density supplies no limit. The finite-matrix CCR trace observation distinguishes carrier algebra only; it proves no sampler obstruction. The current free-end formulation changes the representation and thus does not refute this same-pair closed-string invariant. No parent phase or gravity claim is used as proof of the present residual.

**N5 — Resolution.** Per-element: equal-time E squared and the supplied off-diagonal readout counterexample. Per-site: all finite basis/vertex Gauss residuals and bounded C checkpoints. Per-mode: finite spectra, with unvalidated positive-lag implementation and observable overlap explicitly separate. Per-block: finite cycle-image ranks and actual legal closed-word replay. Lattice-wide: only the two finite geometries plus the analytic even-L seed identity; no physical infinite-volume phase or mixing theorem. The primary emits these five substantive resolution statements in its actual cached stdout.

**N6 — Partial closure.** The geometric parity diagnosis and exact finite references are useful without deriving physical dynamics. A changed update or representation may remove this particular invariant without adding an axiom. Improved code, controlled estimators and finite-size analysis remain possible; no universal new-axiom requirement is claimed.

**N7 — Steelman.** A sampler can change its ensemble representation or augment its legal update graph, as a free-end projector representation suggests, and need not carry this particular closed-walk parity restriction. To refute the exact target while keeping its definition one would have to exhibit a same-face pair move that changes a face count by an odd integer, contrary to its definition. To solve the broader sampling problem one instead needs an independently validated proposal/weight/readout/ergodicity construction and controlled finite statistics; this unit does not close that route.

**N8 — Cross-cycle context.** The corrected ring source separates finiteL20 evidence from a limit, and the current free-end source separates its finite algorithm/estimator from a physical phase. Those corrections support the present narrowing. They are context, not extra closed routes, independent proofs, or fresh approval of either parent campaign. Original scratch odd-cycle counts and timings are preserved as history below.

## Current correction and preserved history

The original source head is`4886ac719d2dda0325134fac87f4e790713346ee`, base`a950a1aacfb33c10699dc88ac2f441d7024ad109`. Its complete note, runner, cache, original21/0 execution, nine bin tables, generated geometry/C/binary files and full failed/mutant receipts remain in the frozen original review and Git provenance. The current note supersedes its overbroad readings; it does not retrospectively validate old caches. Current source review is separate and formal audit remains deferred.

The original scratch odd fundamental-cycle count2246 (and its other breadth-first count1563) depends on its tree; this runner's canonical counts2159/1573 remain. Rank10 is the invariant. The original source's roughly100s per200000 L4 sweeps and this run's historical59s are hardware-dependent operation timings only. The C-scan source had omitted run length; the explicitly declared20000/40000 protocol and all resulting original numbers remain. A prior old/new-operator propagation bug was corrected before the original embedded source, but zero diagnostics did not prove absence of other bugs.

The final cache must be genuinely generated from the frozen current source and both declared inputs, with all21 check IDs and required engine rows accounted for within150seconds and the assigned2GiB control. Its fingerprint and output record the actual outcome; this note does not predict it. Actual filename-derived primary/helper consumers must resolve the standalone primary with no helpers. No mutable scientific parent or historical cache is imported merely for provenance.

## Live questions and boundary

The full weighted ensemble and mixing of any proposed parity-changing sampler, estimator/positive-lag validation, observable/component selection, sector exchange, coupled matter, and larger-volume scaling remain open here. The finite census/parity results and original seeded failure witness survive. The carrier, readout, law and lambda remain supplied. No axiom or approved memo is changed, no hypothesis is adopted, no physical electromagnetic identification is derived, and no audit verdict is applied.
