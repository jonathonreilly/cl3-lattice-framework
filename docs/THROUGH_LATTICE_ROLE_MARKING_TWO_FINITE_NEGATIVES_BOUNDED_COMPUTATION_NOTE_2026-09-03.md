---
claim_id: through_lattice_role_marking_two_finite_negatives_bounded_computation_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Six finite claims T1-T6 for explicitly supplied binary-star and quantum-star templates, with complete value-reading intended orbits and period histograms, numerical ranks and finite-projection diagnostics distinguished from exact bit algebra, an exact PSD common-kernel aliasing proof, product as well as particular entangled junk, and the two junk-free Z-pin EVEN 1D cases retained. No full rule-class, physical Record-formation, clock, probability or global selection theorem; all original protocols and numeric data remain identified."
upstream_dependencies: [minimal_axioms_2026-06-29]
runner: scripts/through_lattice_role_marking_two_finite_negatives_check_2026_09_03.py
---

# Through-lattice role marking: finite unwanted configurations and a one-dimensional positive case

**Date:** 2026-09-03; source correction 2026-09-08.
**Claim type:** bounded_theorem
**Status:** bounded, conditional source; no scientific grade assigned.
**Primary runner:** [through_lattice_role_marking_two_finite_negatives_check_2026_09_03.py](../scripts/through_lattice_role_marking_two_finite_negatives_check_2026_09_03.py)
**Runner cache:** [through_lattice_role_marking_two_finite_negatives_check_2026_09_03.txt](../logs/runner-cache/through_lattice_role_marking_two_finite_negatives_check_2026_09_03.txt)
**Correction provenance:** [dated correction and four verbatim original bodies](../.claude/science/review-fixes/carriers-7869-7880-20260908/REVIEW_CORRECTION.md).
Historical checkpoint identifier: `through_lattice_role_marking_two_finite_negatives`. The actual claim ID is derived from this note's filename.

## Authority and supplied setting

The [current governing memo](MINIMAL_AXIOMS_2026-06-29.md) fixes the interpretation boundary.
All finite operators, states, tensor products, grading, pins and readout conventions below are explicitly supplied mathematical definitions.
They are not derived from the four axioms. A fixed local possibility does not supply a central-sector readout, probability weighting,
physical generation label, clock, state preparation, selection law or permanent Record-formation mechanism.
The old Record central-sector/K-CPT proposal and earlier parent campaigns are historical context only; their original quotations
remain in the dated history. No parent campaign, physical bridge or ancestor authority is accepted by this unit.
Only this note and the current memo are mutable semantic inputs; all matrices and constraints are redeclared locally, with no runtime helper.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: source_correction
artifact_role: conditional_finite_result
next_trace_action: "Independent source confirmation; physical suppliers remain unresolved; formal audit deferred until a solid TOE."
bare_retained_allowed: false
```

## Local construction and evidence boundary

The spacings, free code sites, marker orbit assignments and tensor-product pin states are redeclared below.
The original #7834 48-sector campaign is a historical motivation, not a premise or accepted selection law here.
The spacing-2 arrays are reconstructed directly by `spacing2_templates`; their 48 distinct templates and star-pattern coverage are local finite results.
Ordinary tensor composition, a chosen Z-basis readout and a supplied static frustration-free penalty are definitions, not an axiom-complete model.

T1 uses exact binary orbits. T2 uses complete finite searches on three specified geometries.
T3–T6 mix short exact algebra with floating SVD/eigenvalue/rank and finite-iteration diagnostics.
The runner uses SVD threshold `1e-9*max(1,s_max)`, Gram threshold `1e-8*max(1,w_max)`,
nullity threshold `1e-9`, and eigenvalue-one threshold `1-1e-9` for compressed local projectors.
Original randomized protocols, seeds, residual thresholds, 4-probe estimates and all 17 original IDs are retained.
These numerical thresholds are not certified exact ranks or rigorous error bars. The exact Z-basis controls are labeled separately.

The named one-site pins are the normalized states `|0>`, `|1>`, `|+>=(|0>+|1>)/sqrt(2)`, `|->=(|0>-|1>)/sqrt(2)`, `|i>=(|0>+i|1>)/sqrt(2)` and `|j>=(|0>-i|1>)/sqrt(2)`. The 72 two-dimensional cases are the six-by-six pin pairs times EVEN/FULL; the 128 three-dimensional cases use `{0,1,+,-}^3` times EVEN/FULL; the eight one-dimensional cases use `{0,1,+,-}` times EVEN/FULL. Local tensor factors and slot order are exactly the paired runner's `K_basis_1d`, `K_basis_2d` and `K_basis_3d` definitions. These finite lists do not exhaust continuous pins.

## The operator actually computed after aliasing

For a repeated-slot diagonal isometry `V`, put `A=V† Pi_K V`. Then `0<=A<=I` and the exact eigenvalue-one projector `Q`
satisfies `ker(I-A)=ran(Q)=ker(I-Q)`. Since each summand is positive semidefinite,
`ker(sum_s(I-A_s))=intersection_s ker(I-A_s)=intersection_s ran(Q_s)=ker(sum_s(I-Q_s))`.
The runner computes `H_Q=sum_s(I-Q_s)`, numerically selecting eigenvalues near one, rather than `H_A=sum_s(I-A_s)`.
Their spectra need not agree. In exact arithmetic `0<=I-A<=I-Q`, so an H_Q energy bounds H_A from above for the same vector;
the numerical projector threshold has its own unbounded rounding uncertainty. Reported spectra/residuals are for H_Q.
The two-slot pin criterion `(a|0>+b|1>) tensor (a|0>+b|1>) in span{|00>,|11>}` is exactly `ab=0`.
This criterion concerns the diagonal subspace, not by itself membership in the full K.
Finite alternating products of Q are not asserted to be the exact common-kernel projection. No gap or iteration-bias bound is supplied.

## Definitions

A site's **star** is the site together with its six nearest neighbours: seven sites, seven values, `128` value patterns. A **superlattice role pattern** is a repeating arrangement of pinned site
values whose period exceeds the lattice spacing, with some sites left free; in the locally redeclared spacing-2 example the period is `(4, 2, 2)`, corners, faces and cube centres pinned by coordinate parity and coarse edge sites
free. The lattice itself is unchanged.

A **value-reading star rule** is a predicate on the seven recorded `Z`-values of a star, invariant under the `24` proper rotations; its **penalty** on a configuration is the number of stars it
rejects. Given an intended arrangement, the **maximal** such rule accepts exactly the star patterns realised in the intended configurations over every filling of the free sites; every other rule
of the class accepts at least those, so the maximal rule is the most selective member. **Junk** is a zero-penalty configuration on the torus whose values on the pinned sites are no translate and
no rotation of the intended pattern.

A **spaced superlattice** has coarse spacing `s` and one free code site per coarse edge at position `p` along it: the code sites of the `s`-cell are `(p,0,0)`, `(0,p,0)`, `(0,0,p)` and every other
site is a pinned marker site, with marker values constant on the orbits of the space-group stabiliser of the code sublattice -- `24` rotations at the midpoint `p = s/2`, `C3` otherwise -- so an
**assignment** is one bit per marker orbit.

A **state-reading frustration-free star template** is a positive semidefinite operator `h` on the seven-site star, identical at every site, whose kernel contains the intended role-star states; the
canonical maximal choice is `h = 1 - Pi_K` with `K` the span of those states, and any other template of the class has a kernel at least as large. The zero space of `H = sum_s h_s` is the
intersection of the star kernels, and **junk** here is a zero-energy state outside the span of the intended global states. The **EVEN** variant restricts the free bits around a pinned centre to
even parity; the **FULL** variant does not. On a torus with a side of length `2` the `+` and `-` neighbours along that axis are the same physical site, and the star term is the pullback `h = 1 -
V^dag Pi_K V` through the **diagonal isometry** `V : |b> -> |bb>` on that slot pair.

## Theorem 1 -- the star-pattern orbits, and the spacing-2 vacuity restated

**Conclusion.**

1. The `24` proper rotations and the `48`-element full cubic group induce the **same** `20` orbits on the `128` seven-bit star patterns, with identical canonical representatives. Hence every
   rotation-invariant value-reading star rule is automatically invariant under the full group, inversions included, and no rule of this class distinguishes a pattern from its mirror image.
2. At spacing `2`, on the `4x4x4` torus, the `48` templates of the period-`(4, 2, 2)` role pattern give every corner site six free code neighbours; the corner stars realise all `128` value
   patterns and all `4` adjacent value pairs, so the maximal value-reading star rule at that spacing accepts everything.

**Proof.** Item 1 canonicalises all `128` patterns under both permutation groups of the six neighbour slots and compares the tables entry by entry. Item 2 builds the `48` templates as arrays on
the torus, counts the free neighbours of every pinned site, and enumerates the realised star patterns and adjacent pairs. Both exact.

**Reading, not theorem.** A rule that sees only the seven values around a point has no way to tell left from right. And where every neighbour of a pinned site is free, the seven values around that
site take every arrangement there is, so a rule reading them alone has nothing to reject.

## Theorem 2 -- value-reading star rules on spaced superlattices

**Conclusion.** For the spaced superlattices `s = 3` with both code positions (`10` marker orbits, `1024` covariant assignments each) and `s = 4` midpoint (`9` orbits, `512` assignments):

1. **Zoom-out lemma.** The maximum number of code neighbours of any site is `3` at `s = 3` and `1` at `s = 4` midpoint -- never `6`. No site has an all-code star, so the vacuity of Theorem 1 item
   2 does not apply at either spacing, and any failure below has a different mechanism.
2. The maximal rule accepts its own intended configurations and is covariant: penalty `0` for all `2560` assignments with every code filling, and for `48` sampled assignments over every rotation
   and translate as well. Accepted set sizes span `28`-`111`, `28`-`111` and `8`-`69` of `128`, and `0` assignments are vacuous.
3. The original mixed-marker-mask diagnostic has counts `282/1024`, `282/1024` and `32/512`. It does not establish uniform junk: a uniform configuration must both be accepted and lie outside the complete assignment-specific intended orbit. For all-zero/all-one marker assignments the corresponding uniform state is accepted AND intended. The repaired classifier explicitly excludes these six counterexamples and also checks genuine uniform junk.
4. For every one of the `2560` assignments there is junk on the `s`-torus: `1024`, `1024` and `512` admit it and `0` are junk-free, in `38590` and `16363` branch nodes, at most `133` and `301` for
   a single assignment. The period multiset census of the lexicographically least witness is `489x(3,3,3) 438x(1,1,1) 73x(1,3,3) 24x(1,1,3)` at `s = 3`, the same for both code positions, and
   `321x(1,1,1) 37x(1,2,2) 36x(2,2,2) 33x(1,1,2) 31x(1,1,4) 17x(4,4,4) 15x(1,4,4) 11x(1,2,4) 8x(2,2,4) 3x(2,4,4)` at `s = 4`.
5. Each of the `2560` witnesses tiles to the `2s`-torus, `6^3` and `8^3`, with penalty `0`, and is still no translate or rotation of the intended pattern, so the junk survives the doubled box.

**Proof.** Items 1 to 3 are direct enumerations over the cell and over every assignment. Item 4 is a complete branch-on-first-undetermined-site constraint propagation: at each node the star
constraints are propagated to a fixed point through a lookup of the accepted-pattern set against the known slot bits, a conflict closes the branch, and a completed configuration is either an
intended translate -- and the search continues -- or a witness, whose penalty is recomputed from scratch and whose distinctness from every translate and rotation is checked site by site. Branching
`0` before `1` makes the first witness the lexicographically least one, so the census is a property of the rule and not of a solver. No SAT solver and no external solver is used anywhere. Item 5
tiles each witness and recomputes penalty and distinctness on the doubled torus. The bit enumerations are exact; floating linear algebra is numerical at the stated thresholds.

**Scope.** Junk means outside the complete intended orbit. The census contains 489 full `(3,3,3)` witnesses at each s=3 code position and 17 full `(4,4,4)` witnesses at s=4. A universal period-collapse explanation, or a theorem that a shorter-period witness always exists, is not supplied. The actual repair independently rebuilds the complete proper-rotation/translation orbit for every assignment, checks original and doubled-box membership, compares every reported period against direct coordinate translations, and binds both complete histograms.

## Theorem 3 -- the aliasing lemma for state-reading templates

**Conclusion.**

1. On a torus with a side of length `2` the two `+-` neighbour slots along that axis are the same site, so the star term is the pullback `h = 1 - V^dag Pi_K V`, and the image of the diagonal
   isometry `V` on that slot pair is `span{|00>, |11>}`. The intended star state carries the pinned product `|p>|p>` there, and for `|p> = a|0> + b|1>` that product lies in the diagonal subspace
   exactly when `ab = 0`, that is, exactly for the `Z` eigenstates. For any other pin `V` delivers an entangled diagonal vector instead, and the intended state is a zero mode only if `K` happens
   to contain it. Which pins that happens for is item 2, not a consequence of item 1.
2. On the `2D` `4x2` torus, of the `72` (pin pair, variant) cases, `30` are vacuous -- exactly the `FULL` variant at all `30` pairs with `v != f` -- and of the `42` live cases `22` are faithful,
   meaning the intended states really are zero modes, and `20` are not. The `20` are exactly those with neither pin a `Z` eigenstate.

**Proof.** Item 1 is two lines of algebra on the expansion of `|p>|p>`, checked on all six named pins. Item 2 constructs `Pi_K` by singular value decomposition on the `32`-dimensional star space,
compresses it through the isometry, replaces the compression by its eigenvalue-one projector as specified below, assembles the dense `256x256` Hamiltonian, and evaluates intended products. SVD and eigenvalues are floating numerical calculations; the original four-product diagnostic is retained, with a new complete local-product check for every finite family asserted faithful.

**Reading, not theorem.** When a box is only two sites wide, a site's two neighbours in that direction are one and the same, so the template asks for two copies of one value at once, and only a
definite value is two copies of itself. That is a fact about the small box, and it is why the three-dimensional rows below keep to definite-value pins.

## Theorem 4 -- two dimensions

**Conclusion.**

1. Numerical dense result, `4x2` torus, at the faithful `Z` pins: `v = f = |0>` gives `dim K = 17`, nullity `35` against `23` intended, so `12` junk zero modes in `EVEN` and `4` in `FULL`; `v = |0>`, `f = |1>`
   gives `dim K = 24`, nullity `64` against `28`, so `36` junk. No faithful choice in these six-by-six named pin pairs on this torus is junk-free.
2. Matrix-free, `4x4` torus, no aliasing, state vectors of length `65536` [numerical, seed fixed]: alternating projections from a random start reach residual energy at most `9e-14`, and the
   finite-iteration low-residual vectors carry junk fraction -- weight outside the intended span -- `0.85`-`0.89` at `(+,+)` `EVEN`, `0.31`-`0.33` at `(+,+)` `FULL`, `0.91`-`0.92` at `(0,1)` `EVEN`,
   `0.65`-`0.67` at `(+,-)` `EVEN` and `0.78`-`0.84` at `(0,+)` `EVEN`.
3. four-probe finite-product trace diagnostics targeting kernel dimension from the same runs, `4` probes, one standard error [numerical, stochastic, seed fixed]: `743+-13`, `743+-13`, `1534+-22`, `399+-7` and `690+-17` against
   `96`, `511`, `124`, `128` and `128` intended.

**Proof.** Item 1 is dense and numerical on `8` qubits. Item 2 applies each star's kernel projector in turn to a block of random vectors, using local matrices and blocks of `65536 x 4` amplitudes; several such arrays and the intended-state Gram matrices coexist; the residual energy of the converged block is reported, and the weight inside the intended span is computed against the Gram matrix of the intended product
states, so that span is never materialised either. Item 3 reads the Hutchinson estimator off the same block, the real overlap of each start vector with its finite alternating-projection output. Its mean would target the kernel dimension at an exact projection limit. Four-sample standard error omits finite-iteration bias and is not a confidence certificate. C6/C7 use `estimate-3*SE > intended_rank` as a finite diagnostic acceptance predicate, not as a theorem about the dimension.

**Scope.** The local allowed-space intersection can exceed the span of all intended global product states. Sums of intended global states are already in that global span and cannot explain states outside it. The numerical rows exhibit such an excess for the named finite families; they do not enumerate all possible pins or physical laws.

## Theorem 5 -- three dimensions

**Conclusion.**

1. Numerical SVD: over all `64` pin triples from `{0, 1, +, -}` and both variants, the `3D` seven-site star has `dim K` between `51` and `76` of `128` in `EVEN` and between `65` and `105` in `FULL`, so no
   template of this family is vacuous; and all `16` all-`Z` triples are faithful on the `4x2x2` torus.
2. Matrix-free, `4x2x2` torus, `Z` pins [numerical, seed fixed]: junk fraction `0.56`-`0.62` at `(0,0,0)` `EVEN`, `0.53`-`0.54` at `(0,0,0)` `FULL`, `0.74`-`0.76` at `(0,1,0)` `EVEN` and
   `0.89`-`0.90` at `(0,1,1)` `EVEN`, with residual energy at most `1e-15` and intended-state energy at most `2e-15`; the Hutchinson estimates are `451+-9`, `756+-16`, `988+-18` and `2260+-14`
   against `173`, `349`, `252` and `244` intended [numerical, stochastic, seed fixed].

**Proof.** Item 1 is numerical singular value decomposition on the `128`-dimensional star space, once per triple and variant, with a direct evaluation of the intended states. Item 2 uses the same
matrix-free apparatus as Theorem 4 item 2 on a `16`-qubit torus, the aliased stars compressed through the isometry first.

**Scope.** These are the stated 64 pin triples and four numerical 3D rows. Faithfulness is checked on every intended product in each of the 16 all-Z triples, using local product expectations, without a larger torus campaign.

## Theorem 6 -- what the junk is, and the one-dimensional contrast

**Conclusion.**

1. [numerical, matrix-free, seed fixed] One `2D` and one `3D` junk vector, extracted by removing the intended-span component from a finite-iteration low-residual vector, have energy at most `2e-15` and
   weight inside the intended span at most `7e-31`. Their Schmidt rank across a half cut is `35` and `31` of a possible `256`, and every single-site reduced state is mixed, with purity at most
   `0.661` and `0.725`. No site is pinned to any value.
2. Numerical dense result, with an additional exact Z-basis census: the one-dimensional analogue -- three-site stars on an `8`-ring -- is junk-free at the `Z` pins in the `EVEN` variant, `dim K = 3` and nullity `3` against `3` intended states. The `|+>`
   and `|->` pins in `EVEN` give nullity `9` against `4`, and every tested `FULL` choice gives `47` against `31`. Two of the eight choices are junk-free.

**Proof.** Item 1 reshapes the normalised junk vector into a bipartite matrix across a half cut and takes its singular values, and traces out all but one site for each site in turn. Item 2 is
dense and numerical on `8` qubits.

**Scope and product contrast.** The two extracted vectors have the reported entanglement diagnostics; this does not classify all junk as entangled. In the actual all-Z 3D templates, exact computational-basis nullity/intended counts are `(447,173)`, `(743,349)`, `(999,252)`, `(2286,244)` for `000 EVEN`, `000 FULL`, `010 EVEN`, `011 EVEN`. In particular the all-zero product configuration has zero energy and zero intended overlap for `010/011 EVEN`, with every site purity 1. The runner checks these actual product examples and the two exact 1D Z-pin positive cases. These are static support statements; no site acquires two physical roles or a permanent Record from them.

## Conditional conclusion and live alternatives

For the complete 2,560 assignments on the three named value-reading geometries, the most selective admissible mask still has an unwanted configuration, as certified against the complete intended orbit. Full-period unwanted configurations are part of the result.
For the named 2D/3D pin families the finite exact or numerical evidence shows a local-intersection/global-span gap at the stated precision.
The **two Z-pin EVEN cases on the 1D eight-ring are junk-free**, with exact zero-space and intended dimension 3. The negative summary always excludes this positive exception.
Neither finite family exhausts all star rules, all continuous pins, all spacings, or all states and dynamics allowed by the axioms.

Energetic or non-frustration-free selection, larger direct windows, terms involving more than one star, other local states and mixed value/state rules remain untested alternatives.
The s=4 off-midpoint geometry (23 marker orbits), s=5/s=6 and Haar pins remain excluded scratch contexts; no result is imported from them.
The 4x2x2 box aliases two directions; no non-aliased 4x4x4/64-qubit campaign or thermodynamic conclusion is claimed.
The local kernel argument constrains any PSD term containing the same intended local states, but does not rule out terms penalizing those states or a different intended family.

## N1–N8 negative-scope record

- **N1, attempted routes.** Cubic work executes the representation/commutant, C3 restrictions and the stipulated operator/invariance probes. Role work executes binary-star orbits, three marker geometries and the stated finite quantum-pin families. These are the actual attempts; multiple cases within one family do not manufacture five independent mechanism families. The five-family procedural minimum remains unmet.
- **N2, implication relations.** Mixed-carrier freedom, coefficient freedom, binary unintended configurations, quantum local/global-span excess and physical supplier gaps are different predicates. Their pairwise logical independence under all other hypotheses is not established; no independent-wall count is claimed. The positive 1D exception and mixed carriers remain explicit.
- **N3, hidden premises.** Carrier grading, operator coefficients, torus, marker/pin family, tensor composition, measurement basis and static penalty are supplied. None constructs a physical clock, Born law, preparation or permanent Record process.
- **N4, residual matching.** The 1/2 and 1/4 coefficient examples are supplied choices. The role trace estimates use the unchanged four-probe finite protocol with unbounded projection bias. No measured target or physical value is fitted here.
- **N5, rhetoric.** Finite/specified-domain exclusions replace universal selection, unique-carrier, period-collapse and all-junk-entangled claims. Exact algebra and numerical support are separated throughout.
- **N6, partial paths.** Grading-selected computations, mixed-carrier alternatives, finite unwanted witnesses and 1D positive cases survive. Other coefficient families, pins, energetic terms, larger windows and spacings remain open.
- **N7, strongest alternatives.** The mixed invariant rank-three projector defeats uniqueness; intended uniform configurations defeat the old shortcut; product junk defeats an entanglement-only mechanism; the 1D exact positive case defeats a universal negative. The repaired controls exercise those alternatives.
- **N8, historical echoes.** Earlier flavor/Record and role-pattern claims are dated context, preserved verbatim with original identities. No historical status, unsupported theorem or broader campaign is promoted through a quotation. Formal audit is deferred; this packet assigns no grade.

