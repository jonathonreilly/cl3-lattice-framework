# GOAL — block 03: the Gauss rows as support forcing on the extended payload class (light lane)

Correction (2026-09-05, after delivery, supervisor): the contract below attributes the phrase
"order-independent site-level support forcing among corner records" to open PRs #7893/#7903 in
quotation marks. The primary's quote-fidelity check found it in neither #7893's body nor its
head-branch note; it is a science-record précis carried from block 01's ledger (corrected there).
#7893's own sentence is "Gauss's law is then a record-diagonal relation at each corner, i.e. a
support condition of the law in the axioms' own vocabulary." The note quotes only that. The
contract text is left as written below, as the record of what was asked.

Selected from OPPORTUNITY_QUEUE.md (block-02 refresh, candidate 2 = SUPPLIED_INPUT_LEDGER.md row 4
in its narrowed "shape only" form) after block 02 exhibited that a vertex payload changes the
declared class (a third, longitudinal branch; two conservative speeds). Branch
physics-loop/u1-maxwell-landing-core-block03-gauss-support-20260905, stacked on block 02 (PR #7980).
This block's note must be self-contained: block 02's note and pack are context and evidence
addresses, never audit inputs.

## Exact target contract (proof-search governance)
Target statement | On the supplied period-two role compilation of the cubic gauge complex onto Z^3
(parity roles; oriented d0, C, d2; sector zero — rebuilt from the parity rule inside the runner),
take the EXTENDED payload: one real component at every vertex-role, edge-role, face-role AND
cube-role site (phi, E, B, psi). Classify EXACTLY the translation- and proper-cubic-covariant real
linear nearest-neighbour generator class on it under the oriented (vector-type) transformation law
in the compilation's sign basis (block 02 found dimension 7 with a vertex payload: three onsite
terms, C, C^T, d0, d0^T; the cube payload adds d2, d2^T and an onsite term — measure the dimension),
and its positive-diagonal-energy-conserving subfamily (expected: independent speeds for the vertex
and cube couplings). Read the two Gauss rows — the electric row d0^T E = rho_V (the ice/charge rule
that open PRs #7893, #7903 implement as "order-independent site-level support forcing among corner
records") and the magnetic row d2 B = rho_C — as SUPPORT FORCING in Admissibility's sense: a
constraint surface that the law's flow must preserve (the admissible support is invariant under
the evolution). Determine EXACTLY: (a) which members of the conservative extended class preserve
each Gauss surface (d/dt of the row vanishes identically on the surface); (b) whether preservation
forces the vertex payload (resp. the cube payload) to be a constant of motion on the surface — and
in the zero-charge sector to be frozen — so that on the Gauss sector the extended class collapses
to block 02's one-speed edge/face law, i.e. whether #7917's item 7 ("no vertex, cube, extra coin,
or hidden time payload") is, in its vertex/cube half, DERIVED-CONDITIONAL-ON(item 5's Gauss rows
read as support forcing + the extended conservative class); (c) which parts of item 7 the Gauss
rows do NOT buy — the internal coin (block 02's complex two-component law, which preserves both
Gauss rows) and a hidden time payload — with explicit exact witnesses that satisfy both Gauss rows,
every axiom sentence relied on, and violate item 7; (d) the branch count on the Gauss sector on
the side-6 torus, exactly (the longitudinal branch's fate).
Quantifiers/domain | the role-compiled cubic tori of sides 4 and 6 (exact), size-free arguments
where they exist (connectedness of the torus is the expected lever: a harmonic function on a
connected finite graph is constant); every conservative member of the extended covariant class;
"preserves" as defined above; "follows" means a proof from the named premises with every
hypothesis carried through every step.
Allowed premises | the four axioms and approved primitives (registry check before every wall
sentence); the supplied compilation; block 02's named premises (LR, IP-B, OL, SI) only where
re-stated in this note; the Gauss rows as SUPPLIED constraint content — their shape is
Admissibility's support clause ("'available'/'admissible' denotes its support"), their content
(which neighbour combinations are admissible) and the background charge are supplied; say so.
Forbidden weakenings | treating #7893/#7917/#7952 as authority (evidence addresses, quoted at
scope, verified verbatim against the live PR bodies before quoting); reading the Gauss row as a
dynamics; importing continuum Gauss law or electromagnetism; claiming the Gauss rows are derived
from the axioms; using #7917's class as a premise.
Required edge cases | the harmonic/zero-mode sector on the torus (a constant vertex payload is a
constant of motion: state exactly what "frozen" means and what the global constant does); a
supplied nonzero background charge rho_V (does the collapse survive; what does the vertex
payload do); the E-side/B-side symmetry of the argument; the coin; whether item 5's "preserves
the magnetic Gauss row" (block 02's constraint-surface reading) is the same notion used here.
Completion witness | scripts/u1_gauss_support_forcing_extended_class_2026_09_05.py — an exact,
fail-closed runner (AUDIT_TIMEOUT_SEC at top level; runner_cache conventions per
scripts/runner_cache.py's docstring; no float is evidence) that classifies the extended class,
computes the conservative subfamily symbolically, tests Gauss-surface preservation member by
member, exhibits the collapse or its failure, the coin witness, the background-charge case, and
the side-6 branch count on the Gauss sector; emitting the N5 certificate lines per_element:/
per_site:/per_mode:/per_block:/lattice_wide: (>= 40 chars each) if any sentence is negative;
docs/U1_GAUSS_SUPPORT_FORCING_EXTENDED_PAYLOAD_CLASS_BOUNDED_NOTE_2026-09-05.md with the
obligation table (electric row, magnetic row, coin, hidden time), the machine-status block
(physics-loop fields and enums, claim type bounded_theorem or open_gate as honest, trace
upstream_support with consumer = the light lane's terminal via block 02's residual), an Imports
section, N1-N8 for any family-level negative, falsifiers, a Review record; V1-V5 answered in
writing in the pack's REVIEW_HISTORY.md; RESULTS_block03.md with the full runner output and the
honest list of what could not be established.
Outcomes that do not count | "plausibly"; a derivation of the Gauss rows themselves; any claim
that item 7 follows from the axioms alone; a table without runner witnesses.

## Value gate V1-V5 (draft; the primary answers it in writing before any PR)
V1: block 02's residual wall W_P (the payload, item 7) — this block tests whether the SUPPLIED
Gauss rows (item 5) buy the vertex/cube half of it; the coin half is expected to remain a supply.
V2: the extended-class classification with the cube payload, the preservation computation, the
collapse theorem or its refutation, the coin and background-charge witnesses. V3: Admissibility's
support clause (the Gauss rows' shape), the compilation, the torus connectedness lever. V4:
nontrivial (an exact class, a constraint-dynamics computation, explicit witnesses). V5: block 02
exhibited the vertex payload and its two speeds; this block composes the class with the constraint
and answers a different item of the residual. Prior-art sweep against the refreshed origin/main is
mandatory at block start.
