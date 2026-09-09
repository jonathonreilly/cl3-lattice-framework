# d=3 Bar-Location Measurement: Pre-commission Design Scout

**Date:** 2026-07-10  
**Status:** design memo only; no measurement or derivation — FROZEN 2026-07-10 after supervisor line review. One correction applied at freeze: the excess-gate baseline is re-anchored from the ground doublet to the verified `t=0` preparation (see the baseline section for the measured and structural reasons); the doublet is retained as stationary control and reported diagnostic.  
**Decision sought:** freeze one laptop-feasible successor protocol for measuring the d=3 registration-bar location after the uniform-quench single-qubit pilot returned no certified redundancy.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.

No formation rule.

Sets no audit status.

## Executive decision

Commission **route C: coarse axial sectors plus a cubic-class pointer-contrast preparation** on the open `3 x 3 x 3` cube. The center and all six axial face sites start in `+X`; the twelve edge sites and eight corner sites start in `+Z`. The six face sites are the recording sites. The edge and corner sites are initially quiet sites. The 26 non-center sites are partitioned into two five-qubit and four four-qubit fragments by the exact tie-break below. The primary expected witness is the disjoint opposite pair of five-qubit fragments.

This route answers all three measured failures rather than asking the pilot for a later favorable time. It changes a register from one qubit to a bounded multi-qubit sector; it keeps each recording face transverse; and it makes every other neighbor of a recording face initially `Z`-aligned, so those neighbors do not immediately entangle with the face under their `ZZ` bonds. The five-qubit opposite pair also retains all four other neighbors of each of its recording faces. Information redistributed inside either five-qubit fragment remains available to that fragment.

The preparation remains uniform on each proper-cubic site orbit: center, face, edge, and corner. The Hamiltonian preserves the proper-cubic invariant sector. Every fragment or fragment-pair marginal is evaluated through the complete proper-rotation average of that declared subset. The orbit reduction is therefore exact. The tie-break chooses an analysis axis; it does not choose an axis in the Hamiltonian or preparation.

The headline onset deadline remains `Jt <= 1`. In the isolated center--face `ZZ` mechanism, a `+X` recording qubit conditioned on the two values of `Z_S` develops orthogonal conditional states at `Jt = pi/4`, approximately `0.785`. Every fragment contains its recording face, so no propagation hop is required before the fragment can record. The contrast preparation therefore supplies no reason to move the deadline. A first hit after `Jt=1` is reported as a late diagnostic and fails CHECK-03; it never rescues the measurement.

The claim-bearing state grid remains `Jt = 0:0.1:10` at each `lambda`. Expensive fragment-pair marginals use the predeclared subgrid in the cost section. On rows outside that subgrid, `C_ab` and `R_ind` are null, not interpolated. In this memo, “first sampled time” for registration means the first time on that declared certification subgrid.

## Fixed interpretation and scope

Use the open cube with coordinates `(x,y,z) in {-1,0,1}^3` and pointer carrier `S=(0,0,0)`. Set `J=1` and

`H_lambda = - sum_<ij> Z_i Z_j - lambda sum_i X_i`,

with `lambda in {0.05,0.10,0.20}` and open boundaries. No bond, field, or fragment membership changes during a trace.

For pointer projectors `P_z` and a fragment `F`, record content is the Holevo information

`chi_Z(S:F) = S(sum_z p_z rho_F^z) - sum_z p_z S(rho_F^z)`.

Full quantum mutual information is not substituted. For two fragments, conditional independence is

`C_ab = I(F_a:F_b | Z_S)`

on the state dephased in `Z_S`. Compute it exactly as

`C_ab = sum_z p_z [S(rho_Fa^z)+S(rho_Fb^z)-S(rho_FaFb^z)]`.

The joint tensor order is `(S,F_a,F_b)`, with each fragment in its declared coordinate order. Zero the off-diagonal `S` blocks before evaluating the formula; pointer coherence is not conditional classical information. A fragment certifies at tolerance `delta` only if

1. `H(Z_S) >= 0.05 bit`;
2. `chi_Z(S:F) >= (1-delta) H(Z_S)`;
3. `chi_Z(S:F)(t) - chi_Z(S:F)(0) >= 0.02 bit`, with the `t=0`
   value verified at most `1e-9 bit` (see the baseline section: the
   excess gate is anchored at the verified-uncorrelated preparation,
   not at the ground doublet);
4. it belongs to a subset whose every pair has `C_ab <= 0.02 bit`.

With a verified product preparation the excess gate is implied by any
content-gate pass; it is retained for structural comparability with
the d=1 protocol and becomes binding only if the `t=0` verification
ever measures nonzero initial correlation.

Use `delta in {0.05,0.10,0.20}`, with headline `delta=0.10`. `R_ind` is the largest pairwise-independent certifying subset, found by exhaustive search over the six labels. Ties between maximum subsets are broken by the label order `(+x,-x,+y,-y,+z,-z)`, using the lexicographically first subset in that order. Registration is the first certification-sampled time with `R_ind >= 2`. The persistence flag requires three consecutive certification samples with `R_ind >= 2`. It is a finite-sample flag, not permanent storage.

At every state-grid sample define

`theta(t) = (1/6) sum_a ([1-Tr rho_(S,a)(t)^2] - [1-Tr rho_(S,a)(0)^2])`,

where `a` runs over the six center bonds and the subtrahend is the same trajectory's `t=0` value — exactly zero for the verified product preparation, retained in the formula so the map is stated trajectory-relative for the same reason as the excess gate. `theta` is unnormalized and unclipped. `theta*` is `theta` at the first hit. No interpolation, rescaling, or negative-value clipping is allowed. The stationary doublet's bond mixedness is reported as a diagnostic, never subtracted.

## Route table

The cost multipliers below use the measured pilot cadence of approximately `128 s` per state-grid step and the marginal-unit convention frozen in the cost section. “Kill” means that the route can no longer return a positive physics verdict under its declared protocol; physics absence maps to `BAR-NOT-PINNED`, exit 1. A resource or numerical failure maps to `MACHINERY-FAIL`, exit 2.

| Route | Expected onset mechanism | Adapted pilot check and cost | Predeclared kill signature and verdict | What the outcome buys |
|---|---|---|---|---|
| **A. Coarse sectors, pilot preparation** | The uniform `(1,1,1)/sqrt(3)` quench writes the same small face imprint as the pilot, but a coarse sector retains information subsequently redistributed among its sites. | CHECK-03 uses the six-sector partition below. A Z certification step is `1.83x`; an early step including X singleton control is `2.25x`, and the lazy-X-pair worst case is `3.50x`. The frozen subgrids keep total observer work near the pilot campaign. | If no coarse singleton reaches the content and excess gates by `Jt=1`, or every certifying pair has `C_ab>0.02 bit`, route A is killed as `BAR-NOT-PINNED`. | Positive: coarse capacity alone resolves the pilot negative. Negative: the uniformly transverse environment remains self-scrambling even when internal fragment scrambling is retained. |
| **B. Pointer contrast, axial one-qubit fragments** | The center and six recording faces are transverse while edge and corner sites are `Z`-quiet. The direct center--face bond can rotate a recording face without immediate entanglement from its other neighbors. | The pilot fragment and pair checks carry over with the new class preparation. The per-step marginal count is the pilot count, approximately `1.00x`. | If axial `chi_Z` again stays far below `(1-delta)H`, the route is killed as `BAR-NOT-PINNED`; pointer drift above `0.10` or an X-pointer onset also kills CHECK-02 with the same physics verdict. | Positive: preparation noise, not capacity, caused the pilot negative. Negative: quieting the exterior does not repair the measured one-qubit capacity limit. This route does not satisfy the commission's requirement that the successor change what a register is. |
| **C. Coarse sectors plus pointer contrast — selected** | A transverse face receives the direct conditional phase; its assigned quiet neighbors suppress early external scrambling and provide local capacity. The opposite five-qubit pair has no shared site or direct lattice bond. | All five checks use the coarse layout. A Z certification step is `1.83x`; an early step with X singleton control is `2.25x`; the lazy-X-pair worst case is `3.50x`; non-pair rows are `0.58x`. The complete frozen schedule projects to `13.45 h`. | A missing headline event at any lambda, loss of pointer control, failure of the opposite-pair independence gate, or delta factor `>=1.5` gives `BAR-NOT-PINNED`. Numerical, schema, RSS, or validation failure gives `MACHINERY-FAIL`. | Positive: the combined named successor pins an effective bar for this comparator. Negative: even the strongest `k<=5`, invariant-sector successor allowed by the laptop budget does not pin it. The combined route does not separately identify which of its two changes was necessary. |
| **D. Two hemispherical 13-site fragments** | Each half-cube is a maximal antenna. Only one pair exists, so `R_ind` is capped at 2 and depends on independence across the seam. | CHECK-03 becomes one two-fragment test. A 13-qubit conditional density matrix has dimension `8192` and about `1 GiB` per complex matrix before eigensolver scratch; it has `4,194,304x` as many accumulator entries as a two-qubit `4x4` pair matrix. The required 27-qubit joint accumulator is outside the generic path, so the step multiplier is effectively unbounded under this budget. | The preflight memory/time estimate itself kills route D before a physics run. Attempting a reduced observable that omits the seam joint state is `MACHINERY-FAIL`, not a negative measurement. If a valid implementation later fits and the one pair fails, the verdict would be `BAR-NOT-PINNED`. | A future positive would show two maximal antennas but no redundancy beyond two. A future negative would rule out even half-volume registers. Route D is not laptop-feasible under this commission. |

For route D only, the evaluated partition is fixed as follows. `H_+` contains all nine sites with `x=+1`, the three sites `(0,+1,z)`, and `(0,0,+1)`. `H_-` is the other thirteen non-center sites. This exact definition does not make the required marginals affordable.

**RED — SECTOR BREAK:** a preparation that distinguishes one face, edge, or corner from another member of the same site class leaves the invariant sector. A fragment observable evaluated at one unaveraged, non-symmetry-closed subset also leaves the supported observable path. Dense raw evolution would require a `2^27` complex state plus Krylov work vectors, is expected to exceed the `10 GiB` RSS or the `14 h` wall limit, and is effectively ruled out. No selected element has this defect: the center is its own orbit, the preparation is class-uniform, and every subset operator is averaged over all 24 proper rotations.

## Fragment geometry for route C

The following six lists are the complete partition. Coordinate order inside a list fixes tensor-factor order for every stored density matrix.

`F_(+x) = [(+1,0,0),(+1,+1,0),(+1,-1,0),(+1,0,+1),(+1,0,-1)]`

`F_(-x) = [(-1,0,0),(-1,+1,0),(-1,-1,0),(-1,0,+1),(-1,0,-1)]`

`F_(+y) = [(0,+1,0),(0,+1,+1),(+1,+1,+1),(-1,+1,+1)]`

`F_(+z) = [(0,0,+1),(0,-1,+1),(+1,-1,+1),(-1,-1,+1)]`

`F_(-y) = [(0,-1,0),(0,-1,-1),(+1,-1,-1),(-1,-1,-1)]`

`F_(-z) = [(0,0,-1),(0,+1,-1),(+1,+1,-1),(-1,+1,-1)]`.

The equivalent tie-break algorithm is:

1. assign each axial face site to its own signed-axis fragment;
2. assign an edge with `x != 0` to `F_(sign(x)x)`;
3. for an edge with `x=0` and for every corner, ignore the corner's `x` sign and map `(sign(y),sign(z))` by `(+,+)->+y`, `(-,+)->+z`, `(-,-)->-y`, and `(+,-)->-z`.

The lists contain 5, 5, 4, 4, 4, and 4 sites, respectively, sum to 26, and have empty pairwise intersections. Every face, all twelve edges, and all eight corners occur exactly once. There is no remainder and no overlap. The ordering of fragment labels for all graph algorithms is `(+x,-x,+y,-y,+z,-z)`, even though the coordinate lists above place the four-fragment cycle in its geometric order.

`F_(+x)` and `F_(-x)` each contain one recording face and all four of that face's non-center neighbors. They are separated by two lattice spacings and share no lattice bond. Each four-qubit fragment contains one recording face, one assigned edge, and two assigned corners. Orthogonal fragments meet along inter-fragment lattice bonds. No seam bond is removed from the Hamiltonian.

### Symmetry classes used by the observer

The six individual fragment values are reconstructed from two exact proper-rotation classes:

- `closed-five`: `F_(+x),F_(-x)`;
- `wedge-four`: `F_(+y),F_(-y),F_(+z),F_(-z)`.

All fifteen unordered fragment pairs are reconstructed from five exact proper-rotation classes:

- `opposite-55`: `(F_(+x),F_(-x))`;
- `opposite-44`: `(F_(+y),F_(-y))`, `(F_(+z),F_(-z))`;
- `plus-x-orthogonal`: `(F_(+x),F_q)` for `q in {+y,-y,+z,-z}`;
- `minus-x-orthogonal`: `(F_(-x),F_q)` for `q in {+y,-y,+z,-z}`;
- `transverse-orthogonal`: `(+y,+z)`, `(+z,-y)`, `(-y,-z)`, `(-z,+y)`.

The observer must populate all six vertices and all fifteen graph edges before running the maximum-subset search. It may contract one representative per class because each representative operator is averaged over its complete 24-rotation orbit. It must not replace `plus-x-orthogonal` and `minus-x-orthogonal` by one assumed value; the declared partition does not make that equality part of the supported proper-rotation classification.

The expected ordering is qualitative, not a gate: `C_ab` should be smallest for opposite pairs and larger for orthogonal pairs that communicate across seams. In particular, the five-site opposite pair is expected to remain below `0.02 bit` while one or more orthogonal classes may exceed it. The `R_ind` search is designed for that outcome. Correlated orthogonal pairs may be rejected while the opposite pair supplies `R_ind=2`. No raw count of six crossing singletons substitutes for this graph calculation.

## Preparation and onset mechanism

Use the product state whose exact Bloch vectors are

- center: `n_center=(1,0,0)`, the `+X` state;
- every axial face: `n_face=(1,0,0)`, the `+X` state;
- every edge: `n_edge=(0,0,1)`, the `+Z` state;
- every corner: `n_corner=(0,0,1)`, the `+Z` state.

Thus `H(Z_S)=1 bit` at `t=0`, and all intersite Holevo information is zero at `t=0`. The six face sites are recording sites because they are transverse to the `ZZ` interaction. The twenty edge and corner sites are quiet sites at preparation. A `Z`-eigenstate site acquires only a conditional phase from a `ZZ` bond and carries no imprint in its own reduced state at that instant; quiet sites are therefore not asserted to be records. They are included in coarse fragments to retain information if the transverse field and seam bonds later move the face imprint into the local block.

Conditioned on `Z_S=+1` or `-1`, a face initially in `+X` rotates in opposite directions about `Z`. Its other neighbors initially in `+Z` supply deterministic phases rather than immediate entangling noise. This is the direct write mechanism. The transverse field eventually moves the quiet sites away from `+Z`, so the protection is only a finite-time preparation contrast. The observer therefore records the face, edge, and corner Bloch components at every state-grid row; it does not assume the exterior remains quiet.

No term is changed after preparation. In particular, the transverse field remains on at all sites, seam bonds remain on, and no controlled-copy gate is inserted at the center.

## Baseline convention (supervisor correction at freeze)

The worker draft anchored the excess gate at the equal stationary mixture of the two lowest invariant-sector eigenstates. That definition is basis-invariant inside the doublet — it repairs the eigensolver-orientation ambiguity the pilot measured — but it is unusable as a gate baseline here: in the deep ferromagnetic phase the equal doublet mixture is the classical all-up/all-down mixture up to small transverse dressing, its pointer-conditional fragment states are near-perfectly distinguishable, and therefore `chi_GS approx H(Z_S) approx 1 bit` at every commissioned `lambda`. An excess gate `chi - chi_GS >= 0.02 bit` would demand `chi >= 1.02 bit` against the ceiling `chi <= H(Z_S) <= 1 bit`: the verdict would be `BAR-NOT-PINNED` by construction before any evolution ran. A protocol whose negative is provable in advance is not a measurement. (The pilot avoided this only because its eigensolver happened to return symmetry-broken doublet members with small `chi_GS` — the very ambiguity being repaired.)

The frozen convention is therefore:

- **Excess gate baseline = the trajectory's own `t=0` value.** Excess is `chi_Z(S:F)(t) - chi_Z(S:F)(0)`, and CHECK-01 verifies `chi_Z(S:F)(0) <= 1e-9 bit` for every fragment, pair, and one-site reduction (exact product preparation). Dynamically formed content is measured from the verified-uncorrelated start — the product-quench analog of the d=1 protocol's kick-on-vacuum subtraction. The gate's non-vacuous role belongs to protocols that begin on correlated backgrounds; here it is a guard that binds only if the `t=0` verification fails.
- **The stationary doublet is retained as control and diagnostic, not as a gate baseline.** For every `lambda`, construct `rho_GS^(2) = (|g_0><g_0| + |g_1><g_1|)/2` with `E_0 <= E_1` in the verified invariant sector. Both eigenpair residuals at most `1e-8`, norm errors at most `1e-9`, `|<g_0|g_1>|` at most `1e-9`; energies and splitting `E_1-E_0` reported. Its role: (a) the CHECK-01 stationary false-positive control — a repeated observable row built from `rho_GS^(2)`, with ITS OWN first row as the `t=0` anchor, fed through the identical event routine must give event counts `[0,0,0]` and time-stationary observables to tolerance, exercising evolution, marginal reconstruction, and gate logic on a state whose excess is algebraically zero; (b) the reported diagnostic `chi_GS^(2)(Z_S:F)` per fragment class — the static record content of the comparator's vacuum, expected near `1 bit`, quoted in the note as the measured reason the ground state cannot serve as an excess baseline in the ferromagnetic phase.

All nonlinear quantities on the doublet are evaluated after mixing. First form the unnormalized conditioned marginal

`sigma_F^z = Tr_not(F,S)(P_z rho_GS^(2) P_z)`,

then set `p_z=Tr sigma_F^z`, `rho_F^z=sigma_F^z/p_z`, and compute `chi_GS^(2)` from that ensemble. Do not average the two eigenstates' scalar Holevo values. Likewise, first marginalize `rho_GS^(2)` to a center bond and then compute its purity; do not average two purities. The same rule applies to the X-pointer control and pair conditional information on the doublet.

## Observable set and sampling schedule

At every main state-grid sample `Jt=0:0.1:10`, stream:

- center `p_z`, `H(Z_S)`, and total-variation drift from `t=0`;
- both conditional coarse-fragment marginal classes, their `chi_Z`, the trajectory excess `chi_Z(t)-chi_Z(0)`, and the doublet diagnostic `chi_GS^(2)`, copied to all six explicit fragment labels;
- one-site conditional reductions of each coarse marginal, with face, edge, and corner `chi_Z` and excess, and the capacity gain `G_F = chi_Z(S:F)-max_(i in F) chi_Z(S:i)`;
- all singleton certification flags for each delta;
- the six center-bond entries and `theta(t)`;
- face, edge, and corner Bloch vectors, the quiet-shell loss `Q_quiet(t)=1-(mean_edge <Z>+mean_corner <Z>)/2`, and face transverse retention `<X>_face`;
- shell excess profile, `sum_F Delta chi_F`, first sampled maximizer, and `xi_reg`, defined as the largest Manhattan shell whose one-site reduction has excess at least `0.02 bit` at that maximizer;
- state norm, density-matrix Hermiticity/trace/negativity, entropy bounds, orbit normalization, symmetry-class consistency, and RSS.

The face reduction obtained from `closed-five` must agree with the face reduction obtained from `wedge-four` to `1e-9`; all edge reductions obtained in either type must also agree to `1e-9`. After that gate passes, use the arithmetic mean of the equivalent reductions for the face and edge shell rows. Corner reductions come from `wedge-four`. A disagreement is machinery failure, not a physical anisotropy signal, because the state and Hamiltonian are proper-cubic invariant.

The main fragment-pair certification subgrid is

`T_C = {0.0,0.1,...,1.2} union {1.5,2.0,5.0,10.0}`.

At each time in `T_C`, also stream the five pair-class joint marginals, populate all fifteen `C_ab`, and compute `R_ind`, its deterministic witness, first hits, and consecutive-sample count for every delta. At other main-grid times those fields are JSON null with reason `not-on-frozen-pair-subgrid`. They are never filled by interpolation or by a post-run choice. The full `0.1` resolution is retained through `1.2` so an onset at the `Jt=1` deadline has two following samples for the persistence flag. The four late pair samples are recurrence diagnostics; they do not rescue CHECK-03.

The dt-halving machinery trace is only at `lambda=0.10`, on `Jt=0:0.05:1.10`. Every one of its 23 rows is a pair-certification row. This interval contains the full headline window and two samples after a deadline hit. Compare the first event and `theta*` to the main-grid trace restricted to `Jt<=1.10`. Require onset shift at most `0.10` and relative `theta*` shift at most `5%`. No event on both restricted grids passes this machinery subcheck as physics absence, as in the pilot.

For the X-declared-pointer demolition control, evaluate the same two coarse-fragment types at every main sample `Jt=0:0.1:1`. Evaluate all five X-conditioned pair classes lazily whenever at least two physical fragments pass the X singleton gates for any declared delta. This lazy rule is fixed before launch. A null pair field is lawful only when fewer than two X singletons pass, which proves `R_ind(X)<2` at that row.

## The five checks

The checks retain the pilot's order and fail-closed logic.

**CHECK-01 — preparation verification and stationary control.** The class-product preparation at `t=0` must have coarse-fragment, fragment-pair, and one-site Holevo information at most `1e-9 bit` — this anchors the trajectory-relative excess gate. At each lambda, construct `rho_GS^(2)` by the frozen rule and feed its repeated observable row, anchored at its own first row, through the identical event routine: require event counts `[0,0,0]` in delta order and time-stationary observables to tolerance. Require every dynamical excess to be `chi(t)-chi(0)` without clipping, and report the doublet diagnostic `chi_GS^(2)` per fragment class. Both doublet eigenpairs and every conditioned density matrix must pass their machinery tolerances. Any failure here is machinery failure, because this check tests exact preparation factorization, stationarity of the full observable pipeline, and numerical reconstruction.

**CHECK-02 — pointer demolition and contrast panel.** Retain the centered-Frobenius convention

`C_F(H,O) = ||[H,O]||_F / (||H||_F ||O-Tr(O)I/d||_F)`.

Across center, face, edge, and corner classes require `max C_F(H,Z_i) < min C_F(H,X_i)` and report `Y_i`. At every headline onset require center-Z total-variation drift from `t=0` at most `0.10`. The X-declared-pointer control passes only if it has no excess-gated `R_ind>=2` onset by `Jt=1`. Also report `Q_quiet` and `<X>_face` at the Z-pointer onset; these two contrast observables diagnose the mechanism but add no new numerical threshold. A failure of the commutator ordering, drift gate, or X control is physics absence under the declared comparator and maps to `BAR-NOT-PINNED`.

**CHECK-03 — events, causal ordering, independence, and persistence.** At headline `delta=0.10`, every lambda must have a certification-subgrid first hit with `R_ind>=2` by `Jt=1`. The event witness must name its fragments and all pair values used by the maximum-subset search. For one-site reductions, define the first `0.02-bit` excess crossings `t_face`, `t_edge`, and `t_corner`, with a missing crossing represented by `+infinity`. Require `t_face <= t_edge <= t_corner`; if all are missing, this ordering passes but cannot by itself create an event. Require the headline event to persist for three consecutive certification samples. A hit at `Jt=1` therefore must remain at `1.1` and `1.2`. Raw singleton multiplicity without an independent pair, a first hit after the deadline, reversed shell ordering, or fewer than three consecutive samples fails CHECK-03 and maps to `BAR-NOT-PINNED`.

**CHECK-04 — delta insensitivity.** For each delta, take the median `theta*` over the three lambdas. A missing event at any `(lambda,delta)`, a nonfinite or nonpositive median, or

`max_delta median(theta*) / min_delta median(theta*) >= 1.5`

fails the check. The headline remains `delta=0.10`. No lambda or tolerance is dropped after inspection. CHECK-04 physics failure maps to `BAR-NOT-PINNED`.

**CHECK-05 — bar location.** At headline delta, print each lambda's `theta*`, their median and range, and label each eventful case `inside` when `theta*>=0.2` and `BAR-BELOW-WINDOW` otherwise. No event is `unavailable`, never zero. `BAR-BELOW-WINDOW` is a CHECK-05 flag, not a verdict class. If CHECK-01 through CHECK-04 and machinery pass, a below-window bar still returns `BAR-DERIVED-EFFECTIVE`, exit 0, with the flag attached.

The machinery gate separately requires both ground residuals at most `1e-8`, state-norm error at most `1e-9`, entropy-bound error at most `1e-9`, density-matrix Hermiticity/trace/negativity error at most `1e-9`, cubic-equivalent observable disagreement at most `1e-9`, the dt-halving gate above, peak RSS below `10 GiB`, exact stream/checkpoint identity, and completion below `14 h`. Physics absence is `BAR-NOT-PINNED`, exit 1, never `MACHINERY-FAIL`.

## Engine extensions required in block02

The commissioned engine currently prepares only the uniform `(1,1,1)/sqrt(3)` product state, exposes fixed one-qubit conditionals, exposes fixed two-qubit pair conditionals, and precomputes flip masks for at most two off-diagonal sites. Those capabilities cannot produce this protocol's `k=4,5` fragment states or its fragment-pair joint states. Block02 must add every item below before a claim-bearing run.

1. **Class-product preparation.** Add a public reduced-state constructor taking exact one-qubit vectors for center, face, edge, and corner. It must compute each representative amplitude from bit counts in the four site-class masks and multiply by `sqrt(orbit_size)`. It must reject nonuniform values within a class. Persistent output is one `complex128` orbit vector, about `85.5 MiB`; class-count scratch is at most four `uint8` orbit arrays, about `21.4 MiB`, and may be chunked lower. Work is one `O(27 x 5,605,504)` preparation pass, once per protocol.

2. **Reusable raw-configuration to orbit lookup for marginals.** Recreate once per process and retain in memory the engine's exact `2^27`-entry `int32` raw-to-orbit map, checksum-bound to the orbit basis. It is `512 MiB` and is not added to the persistent table cache. It is shared by all marginal gathers and must not create a raw `2^27` complex state. Raw invariant amplitudes are recovered in chunks as `psi_orbit/sqrt(orbit_size)`. Construction is included in block02 setup timing; a checksum mismatch is machinery failure.

3. **Arbitrary symmetry-averaged conditional fragment marginals.** Add a generic subset API for an ordered coordinate list of at most five non-center sites and a center pointer projector in Z or X. It must return the two normalized `2^k x 2^k` conditional density matrices and their probabilities, using the complete proper-rotation orbit of the joint pointer/subset operator. For `k=5`, the two complex accumulators total `32 KiB`; conservative BLAS and gather scratch is budgeted at `64 MiB`. Each requested fragment type is one `O(2^27)`-class gather and is costed at `1.25` pilot marginal units. Partial traces must supply all one-site and nested diagnostics without another full gather.

4. **Fragment-pair plus pointer joint marginals.** Add a generic API for two declared disjoint fragments and the center, with a hard assertion of no shared coordinate. It must use tensor order `(S,F_a,F_b)`, dephase S, and evaluate the weighted conditional-mutual-information formula above. The largest case is `5+5+1=11` qubits, Hilbert dimension `2048`. A full `complex128` joint density matrix is `64 MiB`; diagonalization and partial-trace scratch are capped at `256 MiB`. The `5+4+1` and `4+4+1` cases are dimensions `1024` and `512`, with matrices of `16 MiB` and `4 MiB`. Pair types are processed sequentially. Each pair type is one `O(2^27)`-class gather and is costed at `1.50` pilot marginal units. The API must return `I(F_a:F_b|Z_S)` from the joint state, not from separately reconstructed marginals.

5. **Subset-orbit descriptors and class verification.** Add immutable descriptors for the two fragment and five pair classes listed above. At setup, enumerate all 24 transformed coordinate tuples, verify the stated class memberships, verify the 26-site partition and all 15 pair mappings, and record a descriptor checksum in every artifact. No physical fragment value may be copied from a class unless this check passes. Descriptor memory is negligible; setup work is negligible compared with one gather.

6. **Two-state ground baseline.** Extend the real symmetric Lanczos path to return the two lowest orthonormal eigenstates of the proper-cubic invariant sector and both residuals. Retaining the second `complex128` state adds about `85.5 MiB`; the two-state cache is about `171 MiB` before container overhead. The existing bounded Krylov subspace remains under the RSS guard. Baseline marginals must be accumulated linearly from both states before any entropy or purity is evaluated.

7. **Independent dense-slab validation of every new path.** The default validation mode must compare class-product amplitudes, both `k=4,5` conditional marginals, all three joint sizes `q=9,10,11`, X conditioning, partial traces, and doublet mixing against raw-state partial traces on the existing open `3 x 3 x 2` methods slab. Maximum elementwise deviation is `1e-9`; validation RSS remains below `4 GiB` and wall time below 15 minutes. The slab is methods-only and carries no physics conclusion.

The shared `512 MiB` lookup, the largest `256 MiB` marginal work area, the extra `85.5 MiB` eigenstate, and `200 MiB` of chunk/checkpoint allowance add less than `1.1 GiB` to the pilot's measured `4.11 GiB` peak. Because pair types are sequential, the design peak is conservatively `6.5 GiB`, below the `10 GiB` guard. A code path that expands a `2^27` complex state, retains multiple pair matrices, or precomputes arbitrary high-flip tables is outside this design.

## Step-cost model and overnight budget

The target machine is the commissioned `16 GB` RAM, 10-core M4. The process RSS guard is `10 GiB`; the claim-bearing wall limit is 14 hours.

Define one pilot marginal unit as one sixth of the measured `128 s` pilot step: `u=128/6=21.33... s`. The six reference families are three conditional one-site classes, two conditional axial-pair classes, and one center-bond state. This allocation deliberately charges evolution, Python overhead, and I/O across the six units; it is a planning upper envelope, not a claim that those operations time equally. Charge a coarse singleton `1.25u`, a fragment-pair joint `1.50u`, and the unchanged center bond `1.00u`.

A main Z certification row costs `11u`, or `1.83x` the six-unit pilot step. Through `Jt=1`, the mandatory two X singleton types raise that row to `13.5u`, or `2.25x`. If the predeclared lazy X gate fires, its five pair types raise the worst row to `21u`, or `3.50x`. A main row without pair or X work costs `3.5u`, or `0.58x`. The campaign budget below pessimistically charges the `3.50x` case at every early main row.

The exact count is:

| Work block | Samples | Marginals per sample | Weighted units |
|---|---:|---:|---:|
| Main Z rows, all lambdas | `3 x 101 = 303` | two coarse types plus one center bond | `303 x (2x1.25+1) = 1060.5` |
| Main Z pair subgrid | `3 x 17 = 51` | five pair types | `51 x 5x1.50 = 382.5` |
| dt-halving Z rows | `23` | two coarse types plus one center bond | `23 x 3.5 = 80.5` |
| dt-halving Z pairs | `23` | five pair types | `23 x 7.5 = 172.5` |
| X demolition, worst case | `3 x 11 = 33` | two coarse types and, pessimistically, all five lazy pair types | `33 x (2x1.25+5x1.50) = 330.0` |
| Z and X doublet baselines | `3` lambdas, two eigenstates | Z: two coarse, five pair, one bond; X: two coarse, five pair | `3 x 2 x (11+10) = 126.0` |
| **Total observer envelope** |  |  | **`2152.0u`** |

`2152u` is `45,909 s`, or `12.75 h`. Reserve `0.70 h` for checksummed cache loading, the second-eigenstate Lanczos overhead, checkpoint serialization, and final reporting. The predeclared planning total is therefore **`13.45 h`**, leaving `0.55 h` below the 14-hour cap. The count assumes the already validated orbit basis and Hamiltonian tables are warm. If those caches are absent, their one-time reconstruction belongs to `--validate`; the claim-bearing `--full` run does not start in the same overnight window.

Before `--full`, validation must time one `k=4`, one `k=5`, and each `q=9,10,11` gather on a cube state and use the exact sample counts above to project completion. The launch gate is projected total at most `13.5 h` and projected RSS at most `8 GiB`. If either projection fails, `--full` refuses to start and reports `MACHINERY-FAIL`; the runner must be optimized. It must not thin the frozen grids, omit a pair class, change the fragment partition, or reinterpret a missing marginal as independence. During a full run, the existing projected-completion line and `10 GiB` RSS guard remain active.

## Runner and artifact contract

Block02 implements `scripts/d3_bar_location_measurement_2026_07_10.py`. Its modes and exit behavior carry over unchanged:

- default or `--validate`: methods validation only, labeled `SLAB-METHODS-ONLY`, exit 0 on validation pass and 2 on machinery failure;
- `--full`: claim-bearing cube run, exit 0 for `BAR-DERIVED-EFFECTIVE`, 1 for `BAR-NOT-PINNED`, and 2 for `MACHINERY-FAIL`;
- `--report`: read completed artifacts and regenerate the final report without evolution or observable reconstruction, with the same verdict exit code.

Use cache directory `logs/runner-cache/d3_bar_location_checkpoints/`. Main streams are `lam_0p05_observables.jsonl`, `lam_0p10_observables.jsonl`, and `lam_0p20_observables.jsonl`. The fine stream is `dt_half_lam_0p10_observables.jsonl`. Freeze schema literals

- `d3-bar-location-observable-v1`;
- `d3-bar-location-checkpoint-v1`;
- `d3-bar-location-ground-doublet-v1`.

Ground caches are `ground_doublet_3x3x3_lam_0p05.npz`, `ground_doublet_3x3x3_lam_0p10.npz`, and `ground_doublet_3x3x3_lam_0p20.npz` in that directory. `protocol_hash` is the SHA-256 digest of the supervisor-frozen UTF-8 bytes of this memo. Any later memo edit changes the hash and invalidates resume/report artifacts.

Append and `fsync` one complete JSON object for every state-grid row. Every row contains:

- `schema`, `run_kind`, `geometry`, `lam`, `dt`, `step`, and `jt`;
- `protocol_hash`, `basis_checksum`, `fragment_descriptor_checksum`, and the four exact preparation Bloch vectors;
- `pointer_z` and, where scheduled, `pointer_x`;
- `fragment_types`, containing the two conditional marginal summaries, density diagnostics, one-site reductions, capacity gains, GS values, and excesses;
- `fragments`, containing all six physical labels, ordered coordinate lists, type references, and singleton flags for all deltas;
- `pair_subgrid`, `pair_types`, and `pair_conditional_mi_bits`, with five class values and all fifteen physical mappings when sampled, otherwise JSON null plus the frozen reason;
- `r_ind`, `certifying_subsets`, and consecutive-sample counts for each delta, null off the pair subgrid;
- `center_bonds`, `theta`, shell and contrast profiles, `Q_quiet`, `<X>_face`, and `xi_reg`;
- `risk_signatures` and `diagnostics`, including norm, entropy, density, symmetry, RSS, and timing values.

Large density matrices are transient and are not serialized into JSONL. Store their deterministic checksums, dimensions, traces, minimum eigenvalues, and derived scalars. Any later reconstruction requires the checkpointed state and is not part of `--report`.

Checkpoints remain atomic, uncompressed NPZ files named `<trace>_step_<NNN>.npz`. Write at step zero, every ten state steps, completion, and on SIGTERM after the latest complete row. Each checkpoint contains the state and SHA-256 checksum, all accumulated JSON rows, exact trace coordinates, initial-state checksum and reference norm, protocol/basis/fragment checksums, and the complete doublet/control metadata. Resume accepts only exact schema, checksum, preparation, lambda, grid, and row/stream matches. A cache mismatch raises; it is never silently repaired. A stream without a matching checkpoint is not resumable. `--report` requires a complete final checkpoint and byte-equivalent normalized JSON content between checkpoint rows and the JSONL stream.

The final stdout contract remains six single-line records in this order: `SETUP`, `EVENTS`, `PROFILE+DEMOLITION`, `BAR`, `CHECKS+MACHINERY`, and `TOTAL`. Failure output preserves the same six-line shape with unavailable physics fields and `TOTAL MACHINERY-FAIL`. Every stdout mode, JSONL row, checkpoint metadata block, and report cache must carry these exact three sentences:

`Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.`

`No formation rule.`

`Sets no audit status.`

## Risk signatures

1. **Empty QND/writeability window, adapted.** The exact panel is `max_F chi_Z/H(Z_S)`, `max_F Delta chi_F`, center-Z total-variation drift, the centered-Frobenius ordering, and the X-pointer `R_ind`. A stable pointer with every coarse `chi_Z/H` below `1-delta` is an empty write window. A content crossing only after Z drift exceeds `0.10`, after commutator ordering fails, or with an X-pointer event is an empty QND window. Either signature fails CHECK-02 or CHECK-03 and gives `BAR-NOT-PINNED`.

2. **Correlated-channel fake, adapted.** Record the raw singleton count `R_raw`, all five pair-class values, and `R_ind`. The signature is `R_raw>=2` while every pair among certifying fragments has `C_ab>0.02 bit`. Six simultaneous coarse crossings do not alter that result. The exact false-positive diagnostic is `R_raw-R_ind`; a positive difference is reported, and `R_ind<2` fails CHECK-03.

3. **Coarse-fragment seam leakage — new.** Define

`L_seam(t) = max(C_plus-x-orthogonal, C_minus-x-orthogonal, C_transverse-orthogonal)`

and report it beside `C_opposite-55` and `C_opposite-44`. The expected design signature is `L_seam>0.02` with at least one opposite class at or below `0.02`; the graph then discards seam-correlated orthogonal pairs and may still retain an opposite witness. The kill signature is both opposite classes above `0.02` whenever their member fragments certify. That leaves no independent opposite witness and, if no other pair survives, fails CHECK-03 as `BAR-NOT-PINNED`.

4. **Contrast loss and reflected wavefront — new.** Use `Q_quiet(t)`, `<X>_face`, the shell first-crossing times, `theta(t)`, and pair values at `1.5,2,5,10`. Early growth of `Q_quiet` concurrent with falling face `chi_Z` is contrast loss. A collapse and revival of `theta` or `chi_Z`, accompanied by an edge/corner-first excess crossing or a late jump in opposite-pair `C_ab`, is an open-boundary return. A headline event still must precede the return and pass `t_face<=t_edge<=t_corner`; a returned-wave first hit is late or locality-failing and gives `BAR-NOT-PINNED`.

5. **Capacity without coarse gain — route diagnostic.** Report `G_F=chi_F-max_i chi_i` for both fragment types. `G_F` near zero while all one-site values repeat the pilot-scale peak shows that the larger register did not retain additional recoverable content. This has no separate threshold: the frozen content and excess gates decide the verdict. It prevents a negative result from being described as a successful capacity repair.

## What would kill the selected route

“Survives” means only that a route remains a scientifically distinct future test. It does not predict success and does not authorize switching routes inside this measurement.

| Failure mode | Frozen detection and consequence | Routes or methods that still survive |
|---|---|---|
| **No coarse singleton reaches content** | At one or more lambdas, every coarse fragment remains below `(1-delta)H` or below `0.02-bit` excess through the headline deadline. CHECK-03 fails; total is `BAR-NOT-PINNED`. | Route A can test whether the contrast preparation itself was harmful. Route D remains a future larger-fragment test if a controlled method becomes affordable. Route B is disfavored because it reduces capacity back to the measured failing unit. |
| **The contrast preparation demolishes Z or admits X records** | Center-Z drift exceeds `0.10` at a headline hit, commutator ordering fails, or X-declared `R_ind>=2` occurs by `Jt=1`. CHECK-02 fails; total is `BAR-NOT-PINNED`. | Route A retains the pilot preparation with the same coarse fragments. A different class-uniform contrast vector would be a new protocol and is not tuned here. |
| **All certifying coarse pairs are correlated** | `R_raw>=2` but every eligible pair has `C_ab>0.02 bit`, including `opposite-55` and `opposite-44`. CHECK-03 fails; total is `BAR-NOT-PINNED`. | Route B retains the pilot's nearly independent one-site channels but not its capacity. Larger volumes with spatial buffers may separate coarse sectors. Route D has only one seam and is not expected to improve this failure. |
| **Information appears in outer quiet shells first** | The derived one-site crossings violate `t_face<=t_edge<=t_corner`, or the first event coincides with the late return panel. CHECK-03 fails as a locality/boundary-contamination result; total is `BAR-NOT-PINNED`. | A larger open cube or controlled open-system method may separate outward propagation from reflection. No small-box retiming survives. |
| **The `t=0` anchor fails verification** | Any fragment, pair, or one-site Holevo information exceeds `1e-9 bit` at `t=0`, so the trajectory-relative excess gate has no verified uncorrelated anchor. CHECK-01 fails; total is `MACHINERY-FAIL` (the preparation, not the physics, is broken). | The doublet diagnostic `chi_GS^(2)` is still reported. A correlated-background variant would be a new protocol with a nontrivial excess baseline, declared in advance — it is not a repair of this one. |
| **Theta is tolerance-controlled** | Any missing delta event, nonpositive median, or median factor `>=1.5` fails CHECK-04. Total is `BAR-NOT-PINNED`. | A different physical comparator may test model dependence. No tolerance may be removed or selected after the run. |
| **The bar is stable but below 0.2** | CHECK-01 through CHECK-04 and machinery pass, but at least one headline `theta*<0.2`. CHECK-05 is `BAR-BELOW-WINDOW`. | The measurement survives and returns `BAR-DERIVED-EFFECTIVE`, exit 0, with the flag. A new normalization chosen to move the bar does not survive. |
| **A hit does not persist for three samples** | The first `R_ind>=2` row is followed by fewer than two further certifying rows. CHECK-03 fails; total is `BAR-NOT-PINNED`. | A larger or effectively open environment may test durable storage. The transient time and `theta*` are reported but do not pin the bar. |
| **The enlarged observer does not fit** | Validation deviation exceeds `1e-9`, projected wall exceeds `13.5 h`, projected RSS exceeds `8 GiB`, live RSS exceeds `10 GiB`, or an artifact identity check fails. | Optimization of the same frozen observer survives. The incomplete run is `MACHINERY-FAIL`, exit 2, and carries no physics conclusion. Dense sector-breaking evolution and post-hoc grid thinning do not survive. |

## Verdict wiring and commission decision

Verdict order is exact:

1. If machinery fails or CHECK-01 fails, return `MACHINERY-FAIL`, exit 2.
2. Otherwise, if any of CHECK-02, CHECK-03, or CHECK-04 fails, return `BAR-NOT-PINNED`, exit 1.
3. Otherwise return `BAR-DERIVED-EFFECTIVE`, exit 0.

CHECK-05 then reports `inside` or attaches `BAR-BELOW-WINDOW`. It never changes the verdict class. A missing onset, a correlated-channel failure, a late onset, contrast loss, delta sensitivity, or failed finite-time persistence is physics absence and therefore `BAR-NOT-PINNED`, never `MACHINERY-FAIL`.

Commission route C only if block02 validation passes every new marginal path, the exact fragment descriptor, the doublet baseline, the calibrated wall projection, and the RSS projection. Do not launch route A, B, or D as a fallback in the same measurement. Do not change the preparation vector, fragment tie-break, pair subgrid, onset deadline, baseline mixture, or tolerance after inspecting any physical row.

A positive outcome buys the following bounded statement: in this declared finite d=3 Ising comparator and under the supplied QD reading, a class-uniform pointer-contrast preparation produces excess-gated, conditionally independent redundancy onset in disjoint coarse fragments, with the reported tolerance stability and effective bar location. It does not show that either coarse capacity or preparation contrast was separately necessary.

A negative outcome buys a sharper successor boundary than the pilot: the exact open `3^3` model fails even after single-qubit registers are replaced by the largest disjoint `k<=5` sectors that fit the joint-marginal budget and after the exterior is made initially quiet without leaving the invariant sector. The failure is localized by content, excess, pointer, seam, shell-order, persistence, and tolerance observables. It does not prove that larger volumes, larger fragments, or another Hamiltonian class cannot register.

## Finite-volume qualification

Every recording face lies on a face of the open cube. Every coarse fragment contains boundary sites, and the four-qubit fragments include corners. There is no radial buffer between a recording face and the open boundary. Fragment seams are physical nearest-neighbor bonds, not analysis-only contacts.

The pilot already measured strong recurrences inside the same `Jt<=10` grid at `lambda=0.05`. The contrast preparation can reflect a wavefront from the boundary on the same finite timescale. The full-grid pointer, theta, shell, and four late pair samples expose those returns, but they cannot turn three samples into macroscopic permanence. A positive result supports only the predeclared short-time persistence flag. It establishes neither a volume-stable plateau nor thermodynamic permanence. A first hit attributable to a returned wave fails the causal-order/deadline check.

## Boundaries

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.

No formation rule.

Sets no audit status.

The Hamiltonian, preparation, fragment partition, pointer reading, QD convention, tolerances, ground-doublet mixture, theta map, time grids, and finite-volume boundary are comparator inputs. They are not supplied by the framework's minimal axioms. No outcome derives the interaction, pointer basis, formation dynamics, numerical bar, gravity, or a thermodynamic record law.

## Source-convention ledger

This design uses only the five commissioned sources:

- `docs/D3_REGISTRATION_PILOT_DESIGN_SCOUT_2026-07-09.md` for the route/check/risk/cost structure, observable conventions, and original runner gates;
- `docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md` for the measured single-qubit capacity and recoherence negative, the ground-doublet ambiguity, recurrence evidence, and named successor;
- `docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md` for the kicked-charge preparation analogy, conditional-independent redundancy shape, and physics-absence verdict semantics;
- `scripts/d3_cubic_orbit_engine_2026_07_09.py` for the exact invariant-sector boundary, existing memory layout, current preparation/marginal limits, RSS guards, and validation machinery;
- `scripts/d3_registration_onset_pilot_2026_07_09.py` for modes, atomic checkpoint/resume behavior, JSONL/report discipline, check ordering, dt-halving logic, and verdict wiring.

All route expectations, cost weights, and risk mechanisms in this memo are premeasurement design estimates. Once supervisor-frozen, the explicit protocol above is the block02 predeclaration.
