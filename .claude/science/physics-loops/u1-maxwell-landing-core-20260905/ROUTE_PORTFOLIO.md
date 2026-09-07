# Route portfolio — light lane

## Prior-art sweep — origin/main @ e249016f75, 2026-09-05
  git grep -n -iE "(yee|maxwell.*uniqueness|uniqueness.*maxwell|landing.core.*light|emergent.*maxwell|photon.*dispersion)" origin/main -- 'docs/*.md'
  git ls-tree -r --name-only origin/main -- docs/ | grep -iE "YEE|GAUSS_LAW|GAUGE_LAW|LANDING_CORE|MAXWELL|PHOTON"
Hits: AXIOM_FIRST_STEFAN_BOLTZMANN (omega = c k as an input — context only);
WAVE_EQUATION_SELF_FIELD (a Yee-style stencil in an older wave lane — not the
gauge generator); TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE (June; a
Record-side invariance profile — non-matching); older U1 notes (fermion
number conservation, ABJ, flavor idempotents — non-matching). Target: OPEN.

## Block 02 prior-art sweep — origin/main @ e249016f759f224d9b429932cd0d1db4d452dc1a (fetched 2026-09-05, before any block-02 science)
Commands (all run from the block-02 worktree):
  git fetch origin main; git rev-parse origin/main
  git grep -n -iE "<pattern>" origin/main -- 'docs/*.md'   for each of the statement patterns:
    (first.order|first order).*(forced|derived|supplied) | nearest.neighbo.*covarian.*rule | energy.*conserv.*(forced|axiom) |
    gauge.compatib | role compilation | dynamics class | existence witness | continuous.time.*(axiom|forced|supplied) |
    minimal.*payload | permanen.*(revers|tick|dynamic|conserv) | conserv.*(quantity|energy).*(record|admissib|axiom) |
    (axiom|framework).*(name|suppl|state).*no.*time | time.*(parameter|metric).*(open|outside|not.*axiom|supplied) |
    linear.*(evolution|dynamics).*(forced|derived|not.*axiom|supplied) | reversib.*(record|permanen|admissib) |
    dissipat.*(sampler|admissib|axiom) | edge.*face.*incidence | covarian.*sentence.*(derived|forced|lever) |
    two.*(distinct|explicit).*(covariant|nearest.neighbor).*(law|rule) | admissib.*(is not|not a).*dynamics |
    stencil.*(forced|unique|derived) | (curl|circulation).*(forced|unique|covarian) | oriented.*(curl|stencil).*(covarian|rotation) |
    gauge.invarian.*(follows from|consequence of|redundant|forced by|derived from).*(covarian|rotation|symmetr) |
    conservative.*(principle|axiom|primitive) | self.adjoint.*(generator|hamiltonian).*(axiom|supplied|not derived) |
    fourth axiom | diffusive.*(branch|sampler).*(conserv|maxwell) | unsigned.*incidence | parity.*(odd|even).*(distance|neighbo).*(edge|face)
  git grep -n -iE "maxwell|dynamics class|first.order|conserved energy|gauge.compat" origin/main -- docs/audit/data/derivation_obligations.json 'docs/audit/data/ledger/*.json'
  git ls-tree -r --name-only origin/main -- docs/ | grep -iE "CONSERV|DYNAMICS_AXIOM|MAXWELL|CURL|GAUGE_INVARIAN|TIME_SELECTION|SINGLE_CLOCK"
Hits read at their statement, with ledger status at origin/main (all unaudited or meta; none retained):
- INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08 (no_go, unaudited): "first-order-in-space is the
  unsupplied antecedent" — the SPATIAL order of the matter kinetic operator; item 2 here is the TEMPORAL order of a field law.
  Non-matching object; shape context only.
- RECORD_MARKOV_GENERATOR_PREMISE_CLASSIFIER_2026-06-06 (meta) and RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06
  (no_go, unaudited): a continuous-time claim needs "embeddability, a supplied generator, a clock interval, and a rate/unit
  normalization" — record-production kernels. Same shape as item 2's continuous-time clause (supplied generator and clock),
  different object. Context.
- RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06 (bounded_theorem, unaudited): no nontrivial reversible Hamiltonian-like flow on
  the finite post-record algebra. Supports "Record supplies no flow" (route R1 of the N-gate); object is the post-record algebra,
  not the unrecorded field. Non-matching result.
- DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06 (no_go, unaudited): "allowed dynamics class != selected Hamiltonian/action"
  for the Wilson gauge-invariant-local class. Same SHAPE (a class is not a selection), different class and mechanism. N8 echo.
- DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05 (bounded_theorem,
  unaudited): record preservation + locality + Hermiticity => gauge-invariant-local class, under supplied bridges (two-endpoint
  Gauss records, a supplied Hermitian H). A DIFFERENT route to gauge invariance; this block's route is the cubic covariance of the
  compiled payload and the gauge-plus-chain nullspace. Non-matching mechanism; N8 echo.
- DYNAMICS_AXIOM_MINIMAL_NONTRIVIALITY_BRANCH_PROPOSAL_2026-06-29 (meta; historical, unadopted PROPOSAL): a proposed fourth axiom,
  "a nonzero, local, self-adjoint generator" — would supply exactly item 2 (continuous linear first-order) and item 6
  (self-adjoint => conservative). Zero premise weight (registry check). Recorded under N6.
- SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11 (no_go, unaudited) and the codimension-one
  evolution note it re-scopes (bounded_theorem, unaudited; the axis demoted to the declared premise B-AXIS): "Record axiom supplies
  no 'time metric'"; the evolution axis is declared. Supports item 2's "no time parameter" at scope; different object.
- ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13 (bounded_theorem, unaudited): two covariant
  nearest-neighbor laws with distinct internal symmetry — the same METHOD (pair-of-models existence witness for non-selection),
  different object (static conditional laws on M_2(C)). Method precedent, non-matching result.
- ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL (2026-07-13) and EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE
  (2026-07-13), both bounded_theorem, unaudited: "Admissibility is not dynamics and supplies neither a transfer operator nor
  physical persistence dynamics"; reversible dynamics versus permanence named as a route price. Context.
- RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15 (bounded_theorem, unaudited): a
  conservation law for record-preserving generation dynamics under a SUPPLIED Hamiltonian on a C3 block; not conservation from
  Record. Non-matching.
- KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09 (approved primitive node): "not a new dynamics". Used at its declared scope only.
- Obligation and ledger rows: no derivation obligation or ledger row names the #7917 class (the members are unlanded open PRs);
  the hits are Maxwell-Boltzmann (dm lane) and first-order Dirac (dirac lane) rows. Non-matching.
No landed statement was found for: rotation covariance forcing the oriented curl on the compiled payload; the redundancy of
gauge/chain compatibility and cubic covariance inside the declared class; the unsigned-incidence covariant law; the odd-distance
parity of edge-face couplings; the dissipation of the admissibility-sampling identification; "role compilation"; an existence
witness for a dynamics-class item. Target state: OPEN after the matched-hit review.

## Approach families for the science block (block 02, chosen from the ledger)
G1 class-restriction derivation — object: #7917's declared class; mechanism:
   reversibility + Record locality forcing first-order/linear/NN; terminal:
   the class as a theorem of the tick structure (strength: would make the
   uniqueness classification unconditional within the framework).
G2 the time-selection fork — object: #7915's Yee time selection; mechanism:
   the Record tick order; terminal: which time selection the framework's
   record structure supplies.
G3 the 3D photon dispersion exponent — object: the transverse mode of the
   spin-half cubic ice at zero vs finite detuning; mechanism: finite-size
   scaling of #7945/#7959's estimators; terminal: is the linear term a
   detuning supply or a derived crossover.
G4 the germ from the Record overlap law — object: #7886/#7887's kappa > 0;
   mechanism: representation positivity; terminal: derive "positive isotropic
   quadratic germ" (#7884's hypothesis) from the Record overlap law itself
   (partially covered).
Block 01 is meta (landing core + ledger); the value gate V1-V5 is applied to
block 02's candidate before any science PR.

## Block 03 prior-art sweep — origin/main @ e249016f759f224d9b429932cd0d1db4d452dc1a (fetched 2026-09-05, before any block-03 science)
Commands (all run from the block-03 worktree):
  git fetch origin main; git rev-parse origin/main
  git grep -n -iE "<pattern>" origin/main -- 'docs/*.md'   for each of the statement patterns (the six required ones first):
    gauss.*(support|forcing|constraint).*(preserv|invariant|frozen|collapse) | vertex.*payload |
    longitudinal.*(branch|mode).*(kill|remove|constraint) | constraint surface.*(flow|preserv) | cube.*payload |
    harmonic.*constant.*(torus|connected) | gauss.*(row|law|sector).*(invariant|preserv|flow) |
    (maximal|largest).*invariant.*(subspace|subset|sector) | unobservable | (extra|internal).*coin | hidden.*time.*payload |
    two.component.*(law|payload|field) | background charge | support forcing | support.*clause.*(gauss|constraint|ice) |
    ice rule | constant of motion.*(vertex|scalar|payload|frozen) | frozen.*(payload|scalar|vertex|cube) |
    invariant.*(surface|manifold|subspace).*(dynamics|flow|law|generator) |
    constraint.*(commut|preserv|invariant).*(dynamics|hamiltonian|generator|evolution) |
    (graph|vertex|cube).*laplacian.*(kernel|constant|connected) | longitudinal | gauss.*(sector|constraint).*(dynamic|evolution|flow|commut) |
    coin.*(payload|component|index|degree) | extended payload|enlarged payload|payload class | first.order.*enlarged|second.order.*(hidden|auxiliary|enlarged)
  git ls-tree -r --name-only origin/main -- docs/ | grep -iE "GAUSS|CONSTRAINT_SURFACE|LONGITUDINAL|PAYLOAD|COIN|HIDDEN_TIME|INVARIANT_SUBSPACE"
Zero hits on origin/main docs for: "gauss ... (support|forcing|constraint) ... (preserv|invariant|frozen|collapse)", "vertex ... payload",
"longitudinal ... (branch|mode) ... (kill|remove|constraint)", "cube ... payload", "harmonic ... constant ... (torus|connected)",
"background charge", "support forcing", "hidden ... time ... payload", "constant of motion ... (vertex|scalar|payload|frozen)",
"gauss ... (sector|constraint) ... (dynamic|evolution|flow|commut)", "extended|enlarged payload", "invariant ... (surface|manifold|subspace)
... (dynamics|flow|law|generator)", "constraint ... (commut|preserv|invariant) ... (dynamics|hamiltonian|generator|evolution)".
Hits read at their statement, with ledger status at origin/main (docs/audit/data/ledger/<xx>/<id>.json); none retained:
- SIGNED_GRAVITY_CONTINUUM_GRADED_EINSTEIN_LOCALIZATION_NOTE (bounded_theorem, unaudited): runner line "Ward/Bianchi-compatible
  constraint surface is preserved at every graded jet" — a formal continuum jet transport in the gravity lane; the phrase
  "constraint surface preserved" is the same NOTION (a constraint set left invariant by an evolution) on a different object
  and by a different mechanism (formal jets, no lattice, no Gauss row). Method precedent for the notion only; non-matching result.
- AXIOM_FIRST_REEH_SCHLIEDER_THEOREM_NOTE_2026-05-01 (bounded_theorem, unaudited): "the largest ad_H-invariant subspace of A(O)'
  collapses 256 -> 64 -> 16 -> 4 -> 1" — an operator-algebra commutant computation. Same linear-algebra TOOL (a maximal invariant
  subspace computed by iterated intersection) on a different object; method precedent, non-matching.
- TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05 (bounded_theorem, unaudited): endpoint invariance
  counts of link-transport operators under U(1)/SU(2) endpoint Gauss generators on a four-qubit model — a Record-side operator
  invariance profile, no dynamics, no payload class. Non-matching (as block 01 already recorded).
- energy_gauss_constraint_obstruction_route_b_note_2026-07-08 (no_go, unaudited; ledger title "Adjacent Cell-Energy Obstruction For A
  Commuting-Auxiliary Constraint Ansatz"; its docs surface is archived at archive/notes/docs/, not under docs/ on origin/main): an
  energy/constraint obstruction for an auxiliary-variable ansatz in another lane. Context only; non-matching object.
- CHIRAL_3PLUS1D_COUPLED_COIN_NOTE (bounded_theorem, unaudited; the coin-walks lane README marks the family "historical blocked"):
  a quantum-walk coin (a 2x2 / 6x6 unitary on a walker), not a second real field component on the compiled payload. Non-matching
  object; the word "coin" is shared, the meaning is not.
- The "ice rule" pattern matched only "branch-choice rule" (DM lane, PMNS basin selection) — non-matching; "two.component" matched a
  Koide measure note and the supplied-readout two-component decomposition note (bounded_theorem, unaudited; a readout-context
  decomposition, not a field payload) — non-matching; "longitudinal" matched gauge-vacuum plaquette-ladder notes (longitudinal LINKS
  of a strip, not a longitudinal mode) and the ABJ anomaly bridge (continuum longitudinal gauge-boson modes as an external premise) —
  non-matching; "graph laplacian ... kernel" matched the Z^3 Green-kernel notes (a resolvent normalization, not the kernel-equals-
  constants lever) — non-matching.
- Block 02's own surfaces (this branch's history, not origin/main): the vertex-scalar witness with its Hodge multiplicities and the
  two-speed conservative family are the direct antecedent; block 02 did not test Gauss-surface invariance on the extended payload,
  did not include the cube payload, did not classify the coin class, and asserted (in GOAL_block03's framing) that the complex law
  "preserves both Gauss rows" without executing it — this block executes it and finds the statement true at zero charge and false on
  a charged surface (the charge rotates).
No landed statement was found for: a Gauss row read as an invariant constraint surface of a field law on the compiled payload; a
vertex or cube payload on the compiled lattice; the collapse of an extended conservative class on a Gauss sector; the empty
invariant subset of a charged surface under a vertex-coupled member; the kernel-of-the-Laplacian (connectedness) lever; the
coin class on the compiled payload or its Gauss cut; a hidden-time (second-order) reading of the complex law. Target state: OPEN
after the matched-hit review.
Quote-fidelity finding carried to the supervisor (not a block-03 file): the ledger's row 4 and GOAL_block03.md attribute the phrase
"order-independent site-level support forcing among corner records" to open PR #7893; the live PR body (gh pr view 7893, 2026-09-05)
does not contain it — its sentence is "Gauss's law is then a record-diagonal relation at each corner, i.e. a support condition of
the law in the axioms' own vocabulary." — and the head-branch note's grep for "support forcing" / "order-independent" / "corner
records" returns nothing. The phrase is a précis (the same failure mode as block 02's CK-01/CK-02). This block quotes the body.
