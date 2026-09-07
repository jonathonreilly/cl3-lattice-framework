---
claim_id: u1_gauss_support_forcing_extended_payload_class_bounded_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "On the supplied parity-role compilation with positive even side n >= 4, the oriented real-linear first-order nearest-neighbor four-role class has ten coefficients (exact classifications on sides 4 and 6), and positive diagonal conservation leaves three coupling scales. Generic electric SF-all requires a2=0 and u_E rho_V=0, and magnetic SF-all requires b=0 and u_B rho_C=0. SF-all together with CONS guarantees both auxiliaries freeze at every state; without CONS their own rates can grow or drift. The exact maximal zero-charge sector and propagating branch count are stated for the tested conservative three-speed member a=-2,a2=2,q=1,r=-1,b=-3,b2=3. The nonempty charged obstruction requires nonzero compatible charge, CONS and nonzero longitudinal coupling in that same row. The doubled inert-coin class has sixteen coefficients, six after conservation, and four K coefficients after all-charge invariance removes the two onsite mixings. Its general weighted SVD uses metric whitening and may have zero/equal singular values. The onsite-phase kernel obstruction excludes only the specified pair of zero-onsite curl copies, not general real mode decomposition. Block02 is a bounded proof dependency. No formal four-axiom independence theorem or physical dynamics selection is claimed."
upstream_dependencies:
  - minimal_axioms
  - u1_dynamics_class_axiom_adjudication_bounded_note_2026-09-05
runner: scripts/u1_gauss_support_forcing_extended_class_2026_09_05.py
---

# Conditional Gauss Invariance: Conservative Auxiliary Freezing and the Remaining Coin Family

**Date:** 2026-09-05
**Claim type:** bounded_theorem
**Status:** corrected conditional source; historical review receipts below bind the original source only. Formal audit is deferred. This note changes no audit
verdict, TOE score, axiom, or approved primitive, and it proposes none.
**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Primary runner:** `scripts/u1_gauss_support_forcing_extended_class_2026_09_05.py`
**Cached receipt:** `logs/runner-cache/u1_gauss_support_forcing_extended_class_2026_09_05.txt`
(`TOTAL: PASS=98 FAIL=0`; exact integer, rational and symbolic arithmetic only)

**Target.** Within the declared scalar class and its explicitly stated inert-coin
extension, determine what supplied Gauss-surface invariance implies, with CONS
and coefficient hypotheses retained where needed. Exact finite alternatives
show which payload features can remain. These alternatives are not complete
models of all four axioms.

**Current context and provenance (2026-09-07).** Corrected source associated
with historical #7913/#7915/#7917 is on main; #7893/#7903 are quoted only for
their distinct carrier/context, not imported as a proof of these supplied rows.
Closed #7980 was routed into #7984; it was not a prior science acceptance.
The corrected [block02 canonical note](U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md)
is an explicit bounded proof dependency for the improved-curl and damped
witnesses below. It is pinned with this note and the memo in the runner's
`AUDIT_INPUT_PATHS`; runtime still reconstructs its own matrices and reads only
the memo. The [dated correction overlay](../.claude/science/physics-loops/u1-maxwell-landing-core-20260905/CORRECTION_2026-09-07.md)
is authoritative over all fifteen immutable original packet bodies. Historical
PASS text validates neither this correction nor a present audit status.
“SUPPLIED IN THIS CONDITIONAL CLASS” is a scope label, not a formal theorem of
four-axiom non-derivability or proof that the examples model every axiom.

## Result up front

| obligation (item 7 of the declared class, at its scope) | verdict | from what | existence witness (all exact, side 6) |
|---|---|---|---|
| no vertex payload participates | DERIVED-CONDITIONAL-ON(SF-all on the electric row, EC, CONS): the vertex payload is frozen (`d phi/dt = 0` at every state) and decoupled (it enters no other rate), in every charge sector. With SF-all and EC alone: decoupled (`a2 = 0`), while its own rate is `a rho_V + u_V phi`. For the tested three-speed member only, SF-0 has the constant auxiliary sector and the stated branch count; the charged obstruction is row-specific and assumes nonzero compatible charge, CONS and nonzero longitudinal coupling | `d/dt(d0^T E) = a2 d0^T d0 phi + u_E d0^T E` exactly (the face block `d0^T C^T` vanishes); `d0^T d0 != 0`; invariance for every `phi` forces `a2 = 0`; conservation ties `a` to `a2` | the three-speed member (`a = -2, a2 = 2, q = 1, r = -1, b = -3, b2 = 3`): covariant, nearest-neighbor, conservative, chain-compatible, and a zero-charge state with `phi = delta` leaves the electric surface immediately |
| no cube payload participates | the same, DERIVED-CONDITIONAL-ON(SF-all on the magnetic row, EC, CONS), by the odd-shift self-duality of the compilation and by independent execution | `d/dt(d2 B) = b d2 d2^T psi + u_B d2 B` exactly (the edge block `d2 C` vanishes) | the same member with `psi = delta` leaves the magnetic surface |
| no extra coin participates | SUPPLIED IN THIS CONDITIONAL CLASS (not bought by the Gauss rows under either reading) | under the declared doubled law (the coin index inert under rotations, a supply like OL) the exact coin class is sixteen-dimensional; conservation leaves six parameters; the rows cut only the two onsite mixings (six to four) and cannot cut the coupling `K (x) C`, whose members decouple after metric whitening and orthogonal SVD; singular values may coincide or vanish. The onsite-phase witness is excluded by nonzero all-charge invariance | the complex law with onsite phase `theta = 3/7`: preserves both zero-charge rows, nearest-neighbor, covariant, conservative, edge-to-face blocks exactly `C`, two real components per site, kernel dimension 0 against 116 for two decoupled copies; the `K (x) C` law with `K = [[1,1],[0,1]]`: preserves every charged surface, mixes the components in the site basis |
| no hidden time payload participates | SUPPLIED IN THIS CONDITIONAL CLASS; at the linear level identical to the coin obligation | `z1'' = 2 G z1' - (G^2 + theta^2) z1` exactly: the complex law's physical pair obeys a closed second-order law whose auxiliary pair is its time derivative; the second-order law has radius two | the same complex law, read as a first-order law on an enlarged payload |

Two consequences at the scope of the declared class.

- Item 7 splits. Its cube half is not an independent supply once item 5's
  magnetic row is read as support forcing (all-charge reading) inside the
  class's own other items; its vertex half folds the same way into the
  electric row — supplied by the lane through `#7893`/`#7903` and used by
  `#7917`'s section-6 mode count without being declared among its seven items
  — together with the class's items: the surfaces are invariant only for
  members with no vertex or cube coupling, and conservation then freezes the
  payloads. Its coin/hidden-time half is untouched by the rows: the coin is
  cut from six parameters to four, never to zero.
- The residual supply of the terminal recorded by block 02 (payload and its
  transformation law, time rule, locality, conservation) therefore sharpens
  on the payload wall: what remains supplied there is the one-component
  clause (items 1 and 7's coin clause) with its transformation law, not the
  edge/face support of the payload.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite coefficient classification and conditional Gauss identities; generic invariance is separated from CONS freezing and the specified three-speed sector. Structural arguments require positive even n >= 4. The source asserts no formal axiom independence."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "The class assumes payload and transformation law, a time rule, locality and energy conservation; block02 proves only the explicitly premised 2L redundancy implications. No independent-wall count or four-axiom non-derivability is established."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Consumers must retain EC, CONS and the supplied row/charge interpretation for auxiliary freezing; the sector count refers to the specified three-speed member. Block02 proof witnesses are explicitly pinned. The one-component assumption and possible transfer constructions remain open supplies, without an independent-wall count."
conditional_surface_status: "Finite side-4/6 classification and witnesses; structural arguments on positive even n >= 4. Generic SF-all, SF-all+CONS, special-member SF-0 and row-specific charged obstructions have distinct hypotheses. No derived Gauss content or selected dynamics."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. The setting: what is supplied, what the axioms say, what is named

**The declared obligation (quoted at scope).** The historical PR `#7917`'s body
declares its result "Within the declared real, linear, first-order,
nearest-neighbor edge/face, proper-cubic, gauge-compatible,
positive-diagonal-energy-conserving class, the only nonzero generator is the
oriented Yee/Maxwell curl pair up to field normalization and one speed. This
is a bounded conditional classification, not an axiom derivation or
TOE-status change." and keeps "Split-step and enlarged-state exact ticks
remain live." The note on its head branch lists the class's seventh item as
"7. no vertex, cube, extra coin, or hidden time payload participates." Block
02 (historical closed PR `#7980` (routed into #7984)) recorded that item as a supply in this conditional class with a vertex
witness (a third branch, two speeds). This note asks whether the Gauss rows —
item 5's magnetic row, and the electric row that the lane supplies through
`#7893`/`#7903` and that `#7917` uses in its section-6 mode count without
declaring it among the seven items — buy any of it.

**The Gauss rows as supplied content (a named supply, never derived here).**
The electric row `d0^T E = rho_V` and the magnetic row `d2 B = rho_C`, with
supplied background charges `rho_V` (on vertices) and `rho_C` (on cubes). The
open PR `#7893`'s body reads the electric row on quantum links as "Gauss's law
is then a record-diagonal relation at each corner, i.e. a support condition of
the law in the axioms' own vocabulary." and states "`G_v = (div E)_v - rho_v`
is pure `Z`, commutes with the coupled hop and with the face ring exchange,
and sums to `-Q`." This note takes from that only the shape: a Gauss row is a
condition on the records around a vertex (the six edge-role neighbors of a
vertex-role site) that restricts which combinations are admissible. That
shape is Admissibility's support clause — the memo's reading note (3):
"'available'/'admissible' denotes its support -- on finite menus, exactly the
possibilities of nonzero probability." — and the 2026-08-05 revision:
"availability became the distribution's support". What is supplied and not
derived: which combinations (the linear row itself), the background charge,
and the compilation on which the row lives. This note does not claim the
rows follow from any axiom sentence.

**Support forcing, two readings (both named, both executed).** A law's flow
"preserves" a constraint surface when every state on the surface evolves
into states on the surface. Two readings are distinguished throughout:

- SF-all (all-charge support forcing): for every supplied background charge
  the admissible set `S_E(rho_V) = {(phi, E, B, psi) : d0^T E = rho_V}` —
  with `phi`, `B`, `psi` unconstrained, because the row constrains only the
  edge records — is invariant under the flow; likewise
  `S_M(rho_C) = {d2 B = rho_C}`. Equivalently, the time derivative of the row
  vanishes identically on the surface. This is the contract's definition.
- SF-0 (sector reading): the law is only required to have a consistent
  restriction to the admissible set — its Gauss sector is the largest subset
  of the admissible set that the flow leaves invariant. A member may fail
  SF-all and still have a nonempty Gauss sector.

**The supplied role compilation (a named supply).** On an even periodic cubic
lattice every site carries a role label equal to its coordinate parity up to
one of eight sector offsets; Hamming weight zero, one, two, three is vertex,
edge, face, cube; an edge on axis `i` is oriented along `e_i`; a face with
normal `e_k` has the ordered plane pair `(i, j)` with `e_i x e_j = e_k`. The
oriented incidence maps are the vertex gradient `d0`, the edge-to-face curl
`C` (a face reads `E_i(f - e_j)`, `-E_i(f + e_j)`, `E_j(f + e_i)`,
`-E_j(f - e_i)`), and the face-to-cube divergence `d2`. The historical PR `#7913`'s
body: "Valid even-torus role fields are exactly eight translated sectors."
The runner rebuilds sector zero from the parity rule alone and re-proves the
facts it uses; the law-level statements hold in every sector by translation.

**The extended payload.** One real component at every site: `phi` at
vertex-role sites, `E` at edge-role sites, `B` at face-role sites, `psi` at
cube-role sites. State dimension `n^3` on the side-`n` torus (64 on side 4,
216 on side 6).

**The axiom sentences relied on (verbatim, checked by the runner against the
memo).** Lattice: "Physical sites are the points of the cubic lattice `Z^3`,
with nearest-neighbor adjacency, standard translations, and proper cubic
rotations about each site." and "No site is privileged. Sites are
distinguished by the supplied lattice structure alone." Qubit: "The full
one-site possibility domain has algebraic presentation `M_2(C)`." and "No
possibility is privileged. Possibilities are distinguished by the supplied
algebraic structure alone." Admissibility: "There is one fixed
nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." and "For each site, the probability
distribution over the possibilities is determined by, and varies with, the
nearest-neighbor conditions." and the support reading note quoted above.
Record: "When present, a record locks exactly one admissible local
possibility." "A site never carries more than one record; records are
permanent." "Only records are readable. A readout value is determined by
record content alone. A site with no record cannot be read." Qualification:
"Further physical structure requires a retained derivation or bridge, or
explicit approved-primitive registration, before use as a premise." and "A
law privileges no states. Its domain is a supplied condition, and at every
state where the condition holds it gives exactly one answer." The memo's own
boundary: "Admissibility is not a dynamics axiom." and it does not "choose a
Hamiltonian or transfer operator ... define a time metric, or provide a
record-production process or physical persistence dynamics".

**Primitive registry check.** `docs/audit/data/axiom_premise_nodes.json` was
read before every wall sentence below: the scale-reference primitive is
units only; the kinetic-isotropy primitive supplies the structural ratio
`c_t = c_s` and, by its own note, "is not a new dynamics"; the realized-state
primitive is pointwise evaluation only. None is classified as a wall, an
import, or a source of bounded status; none supplies a Gauss row, a payload
clause, or a constraint-preservation principle.

**The named premises.** Every conditional verdict names these; none is an
axiom; each is shown load-bearing by a witness.

- SF-all, SF-0: the two readings of support forcing above, applied to the
  supplied rows. A third reading sits between them and is named where used:
  SF-zero, the invariance of the zero-charge surfaces alone — a coefficient
  statement weaker than SF-all (on the four-role class it cuts `a2` but not
  `u_E`, leaving nine of the ten coefficients; with conservation it coincides
  with SF-all).
- EC (the extended covariant class): the law is real, linear, first order and
  continuous in time; a site derivative reads itself and its six physical
  nearest neighbors only; the law is covariant under the even lattice
  translations that preserve the sector and the 24 proper cubic rotations
  about a vertex-role site, acting on the four-role payload by the oriented
  law in the compilation's sign basis (OL of block 02 extended by scalar
  vertex and cube payloads: `phi` and `psi` transform as scalars, `E` as the
  vector component along the edge axis, `B` as the vector component along the
  face normal). Rotations about an edge- or face-role site do not preserve the
  roles, and the odd shift `(1, 1, 1)` exchanges them; requiring covariance
  under that shift as well would cut the class to its five self-dual members
  (the refuting checker's execution), which is not the class of the declared
  items. For the coin class, EC includes the doubled law in which the coin
  index carries the trivial representation of the rotation group (OL-coin) —
  a supply of the same kind as OL: with the sign character on the second
  component instead, the coin class is twelve-dimensional and the mixing
  witness below is not covariant (the checker's execution; the verdict
  survives, the numbers are relative to OL-coin). EC bundles items 2, 3 and 4
  of the declared class together with OL; it is a supply exactly as those
  items are.
- CONS (item 6 on the four-role payload): a positive, diagonal, proper-cubic
  field energy `sum_roles w_role |field|^2 / 2` with positive weights is
  conserved.
- CONN (a fact of the supplied nondegenerate compilation, used as a lever): the nondegenerate even torus (n >= 4) is
  connected under nearest-neighbor adjacency, so the kernel of the vertex
  Laplacian `d0^T d0` and of the cube Laplacian `d2 d2^T` is exactly the
  constants (executed on sides 4 and 6).

## 2. Compilation facts (executed on sides 4 and 6)

The runner establishes exactly: the role census (`n^3/8` vertices and cubes,
`3 n^3/8` edges and faces); the shells (a vertex sees six edges, an edge two
vertices and four faces, a face four edges and two cubes, a cube six faces;
never a same-role neighbor); the parity theorem in its four-role form (the
torus distance is odd exactly between roles of opposite parity, so every
vertex-edge, edge-face, face-cube and vertex-cube coupling has odd physical
radius); the chain identities `C d0 = 0` and `d2 C = 0` over the integers;
the row patterns (`d0` rows `(+1, -1)`, curl rows `(+1, +1, -1, -1)`, `d2`
rows three `+1` and three `-1`) with every incidence entry at physical
distance one; the covariance of `d0`, `C` and `d2` under all 24 proper
rotations about a vertex in the oriented four-role law and under every even
translation, and that the four-role law is a genuine signed-permutation
representation (composition checked on all 24 x 24 pairs).

**The connectedness lever.** `ker(d0^T d0)` and `ker(d2 d2^T)` are exactly
the constants (dimension one each), `rank d0 = n_V - 1`,
`rank d2 = n_C - 1`; the sum rules `d0 1 = 0` and `d2^T 1 = 0` hold, so
every electric charge `d0^T E` and every magnetic charge `d2 B` sums to zero;
and the image of `d0^T` is exactly the zero-sum vertex vectors (solvable for
a dipole, unsolvable for a monopole). A charged surface is therefore
nonempty iff the supplied charge sums to zero — the first thing a supplied
background charge must satisfy on a torus.

**The odd-shift self-duality (the E-side/B-side symmetry, executed).** The
translation by `(1, 1, 1)` — a "standard translation" of the Lattice axiom
that maps sector zero to sector `(1, 1, 1)` — maps roles `V -> C`, `E -> F`,
`F -> E`, `C -> V` and conjugates `(d0, C, d2)` to `(-d2^T, C^T, -d0^T)`
exactly, entry by entry. Every magnetic statement below is the electric one
transported by this translation; the runner nonetheless executes both sides
independently.

## 3. The extended class and its conservative cut

**Theorem (exact, sides 4 and 6).** The real linear nearest-neighbor
generators on `(phi, E, B, psi)` covariant under the even translations and
the 24 proper rotations about a vertex, under the oriented four-role law,
form exactly the ten-dimensional space

```text
d phi/dt = u_V phi + a d0^T E
d E/dt   = a2 d0 phi + u_E E + r C^T B
d B/dt   = q C E + u_B B + b d2^T psi
d psi/dt = b2 d2 B + u_C psi
```

Proof: the 56 translation-covariant nearest-neighbor patterns (vertex onsite
and six vertex-from-edge; three edge onsite, six edge-from-vertex, twelve
edge-from-face; three face onsite, twelve face-from-edge, six
face-from-cube; cube onsite and six cube-from-face) are closed under
conjugation by every rotation (checked), and the nullspace of the covariance
constraints under all 24 rotations has dimension ten on side 4 and on side 6,
containing the ten named members, which are independent. A generic member
with all ten coefficients nonzero is covariant under all 24 rotations and all
even translations with support radius exactly one. (Block 02's seven-
dimensional vertex class is the `b = b2 = u_C = 0` slice.)

**Conservation (symbolic).** With `M = diag(w_V, w_E, w_B, w_C) (x) I`, the
blockwise equations of `M G + G^T M = 0` are `2 w u = 0` on each diagonal
block and `(w_V a + w_E a2) d0^T = 0`, `(w_E r + w_B q) C^T = 0`,
`(w_B b + w_C b2) d2^T = 0` on the three coupling blocks; since `d0^T`, `C^T`,
`d2^T` are nonzero matrices, CONS is exactly the cut

```text
u_V = u_E = u_B = u_C = 0,   a2 = -w_V a / w_E,   r = -w_B q / w_E,   b2 = -w_B b / w_C,
```

three free coupling scales: an edge/face speed, a vertex/edge speed, a
face/cube speed. The three-speed member `a = -2, a2 = 2, q = 1, r = -1,
b = -3, b2 = 3` (unit weights) has metric-skew defect zero and `dH/dt = 0`
exactly on a random rational state; a member violating one cut condition
does not.

## 4. The Gauss rates as functionals, and the collapse theorem

**The rates (exact, coefficient by coefficient, side 6).** For every member
of the class,

```text
d/dt (d0^T E) = a2 (d0^T d0) phi + u_E (d0^T E)            [the face block r d0^T C^T = 0 identically]
d/dt (d2 B)   = b (d2 d2^T) psi + u_B (d2 B)               [the edge block q d2 C = 0 identically]
```

The runner computes the rate functional of each of the ten unit members as a
matrix on the whole state and confirms that the electric rate receives
exactly `d0^T d0` from `a2`, `d0^T` from `u_E`, the zero matrix from `r`
(that is the chain identity), and nothing from the other seven coefficients;
mirror for the magnetic rate. The vertex and cube Laplacians are nonzero
(rank 26 on side 6).

**Theorem (collapse; exact on sides 4 and 6; the algebra is size-uniform on positive even n >= 4).**
Let `G` be any member of the ten-parameter class and `rho_V` a supplied
zero-sum charge.

1. The electric surface `S_E(rho_V)` is invariant under `exp(tG)` for all `t`
   iff `a2 = 0` and `u_E rho_V = 0`. Proof: on `S_E(rho_V)` the rate is
   `a2 (d0^T d0) phi + u_E rho_V`, and `phi` ranges over all vertex vectors;
   `a2 (d0^T d0) = 0` iff `a2 = 0` because `d0^T d0 != 0`. No other
   coefficient enters. Executed: the three-speed member fails on the
   zero-charge state `phi = delta`, `E = B = psi = 0` (the rate is
   `2 (d0^T d0) delta != 0`); a member with `a2 = 0` and `u_E = 0` but every
   other coefficient nonzero has the rate functional identically zero.
2. The magnetic surface `S_M(rho_C)` is invariant iff `b = 0` and
   `u_B rho_C = 0`. Same proof with `d2 d2^T`; executed with `psi = delta`.
3. If `G` also satisfies CONS, then `a2 = 0` iff `a = 0` and `b = 0` iff
   `b2 = 0` (positive weights). Hence the members that preserve both surfaces
   and conserve are exactly `G = c [[0, 0, 0, 0], [0, 0, -C^T, 0],
   [0, C, 0, 0], [0, 0, 0, 0]]` after field normalization — block 02's
   one-speed edge/face law — with `d phi/dt = 0` and `d psi/dt = 0`
   identically: the vertex and cube payloads are frozen at every state, on
   and off the surfaces, in every charge sector. Executed on both sides.

**What "frozen" means, exactly.** Under the collapsed law the vertex payload
is a constant of motion trivially: its rate is the zero functional. It is
also inert: no other rate reads it. The entire frozen spatial profile it may carry does nothing; it need not
be spatially constant under the collapsed all-state law. Without CONS (SF-all and EC only), invariance gives `a2 = 0` and
`u_E rho_V = 0`, and the vertex payload's own rate is `a rho_V + u_V phi`: it
is decoupled from `E` and `B` but may read them. For `u_V = 0` its second
time derivative vanishes exactly (executed: `d phi/dt = a rho_V`,
`d^2 phi/dt^2 = 0` on a dipole surface), so `phi(t) = phi(0) + t a rho_V` —
a multiple of the background charge, frozen in the zero-charge sector only
when `u_V=0`. For example `u_V=1`, `a2=u_E=0` preserves both Gauss functionals
but has `phi_dot=phi`; the runner executes this nonfrozen counterexample.

**Verdict on the vertex/cube half of item 7.** DERIVED-CONDITIONAL-ON(SF-all,
EC, CONS): no vertex or cube payload participates — the payloads are frozen
and decoupled. DERIVED-CONDITIONAL-ON(SF-all, EC) for the weaker "does not
participate in the edge/face dynamics" (decoupled, not necessarily frozen).
Relative to the four axioms alone the verdict inherits the status of its
premises: the rows are supplied content (their shape is the support clause),
EC and CONS are the supplies block 02 recorded. The three-speed member is the
witness that SF-all is load-bearing (it satisfies EC and CONS and violates
the row); the `a2 = 0, a = 3/2` member is the witness that CONS is
load-bearing for "frozen".

## 5. The Gauss sector and branch count of the specified three-speed member

The conservative member `a=-2,a2=2,q=1,r=-1,b=-3,b2=3` fails both
SF-all rows. The following maximal-sector and branch statements concern this
member, not every non-preserving EC member. With `b=b2=0` and the same electric
couplings, an arbitrary nonconstant cube profile is stationary; that actual
counterexample prevents a generic constant-psi conclusion. Both nonzero
longitudinal couplings are needed to constrain both auxiliaries; nonzero
transverse coupling is needed to call modes propagating. Under SF-0 the
question is what part of the admissible set this member can be restricted to. The runner computes the exact
maximal invariant subspace inside the zero-charge surface (the intersection
of the kernels of `P G^k`, iterated until the row space stabilizes — two
steps here) for the three-speed member:

- electric row only: exactly `{d0^T E = 0, phi constant}` (dimension 50 on
  side 4, 164 on side 6): connectedness is the lever, because the condition
  `(d0^T d0) phi = 0` is `phi in ker(d0^T d0)`, which is the constants;
- both rows: exactly the Gauss sector `{d0^T E = 0, d2 B = 0, phi constant,
  psi constant}` (dimension 36 on side 4, 112 on side 6).

On the Gauss sector the three-speed member and the one-speed member agree
as linear maps (the vertex and cube couplings are invisible there, because
`d0` of a constant and `d2^T` of a constant vanish and the charges vanish),
the flow maps the sector into itself, and `phi`, `psi` have zero rate on it.
So under SF-0 the collapse is a collapse of the dynamics on the sector, not
of the coefficients: the vertex speed exists but acts on no admissible state.

**Branch count on the Gauss sector (side 6, exact).** By the chain
identities `-G^2` of the three-speed member is block diagonal: E-block
`4 d0 d0^T + C^T C` with multiplicities `{0:3, 3:12, 6:24, 9:16, 12:6, 24:12,
36:8}` (sum 81), B-block `C C^T + 9 d2^T d2` with `{0:3, 3:12, 6:24, 9:16,
27:6, 54:12, 81:8}`, vertex block `4 d0^T d0`, cube block `9 d2 d2^T`. Off the
sector there are, on the edge side, three branches at each of the 26 nonzero coarse momenta:
two transverse at speed one (52 modes) and one longitudinal at speed two
(`26 = 6 + 12 + 8`); on the face side three as well, the cube coupling supplying a further branch at speed three in place of the longitudinal one, on
the face side. On the sector, `C^T C` restricted to `ker d0^T` has
multiplicities `{0:3, 3:12, 6:24, 9:16}` (sum 55) and `C C^T` restricted to
`ker d2` the same: exactly two propagating modes per nonzero momentum, the
longitudinal and cube branches absent, three plus three harmonic zero modes
plus the two frozen constants. The sector spectrum is independent of the
vertex and cube speeds — `4 d0 d0^T` vanishes on `ker d0^T` — so it is block
02's count. The longitudinal branch's fate: it lives entirely in `im d0`,
which the electric row removes; it is not killed by the flow, it is
inadmissible.

## 6. A supplied nonzero background charge

Let `rho_V` be a supplied **nonzero** zero-sum charge (a dipole is executed on both
sides; a monopole gives an empty surface).

- Every `a2=u_E=0` member preserves the whole charged electric surface.
  Its auxiliary rate is `a rho_V+u_V phi`, not generally zero. Under CONS the
  one-speed law freezes the full auxiliary profile; the general nonconservative
  member need not. The collapse with CONS survives a background charge.
- A conservative member with `a a2 != 0` has NO invariant subset of the
  charged surface. Exact: the states whose charge is constant in time are
  exactly `{phi constant, d0^T E = 0}` (the unobservable subspace of the pair
  `(P G, G)`), and their charge is zero; so `rho_V` is not in the image of
  the constraint on that subspace and the affine system is inconsistent. The
  mechanism, read off the functionals: the vertex payload is sourced by the
  charge (`d phi/dt = a rho_V`), develops a gradient at once (a zero-sum
  nonzero charge is never constant), and the gradient drives the row off the
  surface (`d/dt(d0^T E) = a2 (d0^T d0) phi`). Under a background charge the
  vertex coupling is not merely invisible; it is inconsistent with the row.
- A non-conservative member with `a2=u_E=u_V=0`, `a != 0` keeps the charged electric surface
  and drifts the vertex payload linearly, `phi(t) = phi(0) + t a rho_V`.
- An onsite edge term `u_E != 0` with `a2 = 0` preserves the zero-charge
  surface and not a charged one: the charge decays at rate `u_E`
  (executed).
- The complex coin law rotates a two-component charge instead of preserving
  it (section 7).

For a nonzero compatible magnetic charge, the analogous obstruction requires
CONS and `b*b2 != 0`; it is a separate row-specific statement. Zero charges,
zero longitudinal couplings and arbitrary nonconservative coefficients are
not covered by either charged obstruction.

## 7. The coin: what the rows cut and what they cannot

**The exact coin class (side 4).** On the two-component edge/face payload
`(E_1, E_2, B_1, B_2)` the 120 translation-covariant nearest-neighbor
patterns (the 30 edge/face patterns times four coin pairs) have covariance
nullspace of dimension sixteen under the rotation group (generated exactly by
the two 90-degree rotations, closure checked): `span{onsite E, onsite B, C,
C^T} (x) M_2(R)` — under the declared doubled law OL-coin, in which the coin
index is inert under rotations (a stipulation of the same kind as OL, not a
finding; section 1).

**Conservation (executed for two weight choices).** With positive diagonal
weights in the coin basis, the cut leaves exactly six parameters: a free
`2 x 2` matrix `K` in the face-from-edge block `K (x) C` (the reverse block
is then `-W_E^{-1} K^T W_B (x) C^T`), one skew onsite mixing `theta_E` on
the edges and one `theta_B` on the faces; every diagonal onsite entry
vanishes.

**The rows on the coin (executed on a generic member `theta_E = 2/3`,
`theta_B = -1/5`, `K = [[1, 2], [3, -1]]`).** The electric rate functional is
exactly `(Theta_E (x) d0^T) E` with `Theta_E` the skew mixing matrix — the
coupling contributes `R (x) d0^T C^T = 0`. So: under SF-all a charged surface
is preserved iff `theta_E = 0` (on a dipole charge in component one the rate
is `theta_E (0, rho)`), the magnetic row likewise cuts `theta_B`, and the
two rows together cut the conservative coin family from six parameters to
four — the whole of `K (x) C`. Under SF-zero the rate vanishes identically on
every zero-charge surface, so nothing is cut, and under SF-0 (the sector
reading) nothing is cut either. In no reading does the second component
disappear. Under SF-all the residue is exactly `K (x) C` with
`R=-W_E^{-1}K^T W_B`. First whiten the metric: `e=W_E^{1/2}E`,
`b=W_B^{1/2}B`, and set `A=W_B^{1/2}K W_E^{-1/2}`. If
`A=U Sigma V^T`, then `e'=V^T e`, `b'=U^T b` give separate curl blocks at
the nonnegative singular values. This is orthogonal after whitening; the
original-coordinate maps are metric isometries, generally not Euclidean
orthogonal. Singular values can be equal or zero. Only the explicit
`K=[[1,1],[0,1]]` unit-weight witness has two distinct positive speeds.
Its normalized vectors require a real algebraic extension: an actual entry
has minimal polynomial `5z^4-5z^2+1`, so the full orthogonal SVD is not over
`Q(sqrt(5))`. The runner checks both that SVD and a nontrivial weighted example.

**Witness one (zero-charge reading): block 02's complex law**,
`dE/dt = -C^T B + i theta E`, `dB/dt = C E + i theta B`, `theta = 3/7`. On a
random state of the double zero-charge sector (with harmonic parts) the
rates of both rows vanish exactly for both components; the assembled real
generator is antisymmetric (conserves `sum |E|^2 + |B|^2`), has support
radius one, is covariant under all 24 rotations in the doubled oriented law,
and its edge-to-face blocks are exactly `C`; it carries two real components
per site. Its site components mix, and it is not similar to the specified pair of
zero-onsite local curl copies: `ker G_theta` has dimension zero
(`theta^2 = 9/49` is not an eigenvalue of `C^T C` or `C C^T`) while two
decoupled copies of the one-speed law have kernel dimension 116; kernel
dimension is a similarity invariant, so no real change of basis maps it
to that particular pair. This does not exclude general real decoupling.
An explicit real orthogonal basis splits a tensor mode into oscillator
blocks with frequencies `omega-theta` and `omega+theta`; the runner checks
this countercontrol. It does not construct two zero-onsite local curl copies. A harmonic edge field, a zero mode of the one-speed
law, acquires the rate `theta` under it. On a charged surface it does not
preserve the surface: the rate is `theta J (d0^T E)`, the two-component
charge rotates in the coin plane and its per-vertex modulus has zero rate.
So the statement "the complex law preserves both Gauss rows" is true at zero
charge and false on a charged surface; block 02 did not execute it and this
note corrects the expectation carried in the pack.

**Witness two (all-charge reading): the `K (x) C` law**, `theta = 0`,
`K = [[1, 1], [0, 1]]`: antisymmetric, radius one, covariant, both rate
functionals identically zero for both components (every charged surface
preserved), and its `B_1`-from-`E_2` block is `C` — the components mix in the
site basis. It is, over the reals, two decoupled copies at distinct speeds
(the coin change of basis `B' = (K^T (x) I) B` turns it into
`K^T K (x) C` against `I (x) C^T`, and `K^T K = [[1, 1], [1, 2]]` has
characteristic polynomial `lambda^2 - 3 lambda + 1` with discriminant 5, two
distinct positive irrational eigenvalues). It violates item 7 as declared
(an extra coin participates) and the terminal's "one speed".

**Verdict on the coin clause.** SUPPLIED IN THIS CONDITIONAL CLASS: not reached by the rows in
the stated readings within this class, and not explicitly supplied by the
quoted memo text (section 12). The Qubit
sentence bounds a linear one-site payload to eight real components (executed
here, runner section J, as the real dimension of `M_2(C)`; also block 02,
section 7); two fit.

## 8. Hidden time

A hidden time payload is an auxiliary variable that makes the physical
components obey a higher-order law in time. For a real linear first-order
law on an enlarged payload this is the coin seen from the physical pair.
Executed on the complex law: with `z1 = (E_1, B_1)`, `z2 = (E_2, B_2)` and
`G` the one-speed generator, `z1'' = 2 G z1' - (G^2 + theta^2) z1` exactly on
a random state, and `z2 = (G z1 - z1') / theta` — the auxiliary pair is a
function of the physical pair and its velocity. The second-order law is not
nearest-neighbor: `G^2` has support radius exactly two. So the hidden time
payload is the coin, and it trades locality for the extra component; the
Gauss rows do not see it because they do not see the coin. Verdict: SUPPLIED IN THIS CONDITIONAL CLASS, coextensive with the coin clause at the linear level. (Block 02's
finite tick and nonlinear witnesses are not hidden-time laws: they keep the
minimal payload.)

## 9. Item 5's notion against the notion used here

Block 02 read item 5's "preserves the magnetic Gauss row" as the identity
`d2 L = 0` on the face-from-edge block `L`. On the minimal `(E, B)` payload
with a general covariant member `[[u, r C^T], [q C, v]]` the magnetic rate
functional is exactly `v (d2 B)`: the coupling contributes `q d2 C = 0`
identically. So on the coupling block the identity reading and the
constraint-surface reading coincide, and the surface reading additionally
cuts the onsite term `v` only when a magnetic background charge is supplied.
On the extended payload it is the surface reading that does the new work:
it cuts the face-from-cube coefficient `b`, which no identity on `L` sees.
The two notions are the same on the declared class and differ exactly where
this note extends it.

## 10. The four-row obligation table with the strength of the missing lemma

| obligation | verdict | derivation, or the exact terminal missing lemma | strength of the missing lemma against the obligation |
|---|---|---|---|
| no vertex payload | DERIVED-CONDITIONAL-ON(SF-all, EC, CONS); decoupled-only under (SF-all, EC); sector-inert for the specified conservative three-speed member under SF-0 | sections 4-6 (exact functionals; `d0^T d0 != 0`; connectedness for the sector; nonzero row-specific charge has no invariant subset under CONS and nonzero longitudinal coupling) | the premises are the class's own other items plus the reading of its Gauss row; none is the obligation restated |
| no cube payload | the same by the odd-shift duality (and independent execution) | sections 2, 4 | the same |
| no extra coin | SUPPLIED IN THIS CONDITIONAL CLASS | missing: a sentence restricting a site's evolving coordinates to one; the rows cut the coin's onsite mixings only (six to four) | comparable: it is the one-component clause of item 1 |
| no hidden time payload | SUPPLIED IN THIS CONDITIONAL CLASS (coextensive with the coin at the linear level) | missing: the same sentence; the second-order identity shows the auxiliary pair is the velocity | comparable |

## 11. What is and is not claimed

Claimed: the exact finite statements of sections 2-9 on the side-4 and
side-6 compiled tori; the size-uniform on positive even n >= 4 algebra (chain identities, the odd-shift
duality, connectedness of the nondegenerate even torus (n >= 4), the block structure of `-G^2`); the
verdicts with their named premises; the witnesses.

Not claimed: that any Gauss row, any item of the declared class, or item 7
follows from the four axioms alone; that any dynamics class is selected; any
infinite-volume, continuum, thermodynamic or Lorentz statement; any Record
readout of `E`, `B`, `phi` or `psi`; any identification with
electromagnetism; any change to an axiom or primitive; any audit verdict.
Historical PR identities are provenance; current corrected-main context and
the bounded block02 proof dependency are distinguished above. The eight-component capacity bound is executed here
(runner section J) and is also block 02's; it is used only to close route R7
of the gate.

## 12. No-Go Discipline Gate

The finite coin constructions show that the supplied Gauss rows do not
remove the extra component in this declared representation. The memo does
not explicitly supply a one-component rule. These are conditional mathematics
and textual scope, not a formal independence theorem for all axiom models.

### N1 — Alternative route enumeration

Each row is a distinct family under the tuple (object, mechanism, terminal
obligation). Computed coefficient/coin statements are distinct from textual
readings and approved-primitive context; none supplies a complete axiom model.

| route | what it would attempt | why it fails here | marker |
|---|---|---|---|
| R1 all-charge invariance | require every charged surface invariant and hope the coin dies with the onsite terms | it cuts exactly `theta_E`, `theta_B` (six to four) and leaves `K (x) C`, which preserves every charged surface (runner section J) | ATTEMPTED |
| R2 per-component rows | impose the rows on each coin component separately, or on every real linear combination of components | the rate functional is `(Theta_E (x) d0^T) E`; any linear combination of the rows sees only `Theta_E`, never `K` (runner section J) | ATTEMPTED |
| R3 no-privileged-possibility | read Qubit's "No possibility is privileged" as forbidding a second coordinate | the complex law's coin rotation is a symmetry of the law (the onsite phase distinguishes no possibility); the sentence concerns the domain's structure, and `M_2(C)` has eight real coordinates (block 02's bound, context) | ATTEMPTED |
| R4 one record, one coordinate | read "a record locks exactly one admissible local possibility" as one real evolving coordinate per site | one possibility of `M_2(C)` carries eight real coordinates; one record is one point of the domain, not one real number; and the components here are unrecorded possibilities (the open bridge of block 02's SI) | ATTEMPTED |
| R5 spectral route | use the coin law's nonzero zero-momentum frequency `theta` against a supplied gaplessness | the rows do not see frequencies (their functionals are static), and `theta = 0` (the `K (x) C` family) is gapless and still a coin | ATTEMPTED |
| R6 kinetic-isotropy primitive | read `c_t = c_s` as fixing one component per site | the registered primitive's own note: "not a new dynamics", supplies only the graining ratio; registry check performed; it supplies no payload clause | RULED OUT BY PRIOR (approved primitive source note, registry node `kinetic_isotropy_primitive`) |
| R7 capacity bound | tighten Qubit's eight-component bound to one | the bound is eight, executed here (runner section J) as the real dimension of `M_2(C)`, as block 02 also executed it; two components fit and the sentence names no smaller number | ATTEMPTED (executed here) |

### N2 — Complete pair coverage without an independence count

Predicates: `W_G` = preservation of all supplied compatible charged surfaces;
`W_EC` = the extended real-linear first-order nearest-neighbor covariant class
with its declared oriented representations; `W_C` = positive onsite diagonal
quadratic conservation; `W_coin` = one-component/no hidden-time restriction;
`W_VC` = **zero auxiliary rates and no auxiliary feedback into E/B**, not the
absence of an auxiliary variable or its spatial constancy. The scalar class
and its declared inert-coin extension are distinguished where used.

| pair | first implies second? | second implies first? | scope / remaining obligation |
|---|---|---|---|
| `W_G`, `W_EC` | no: improved curl | no: three-speed member | block02 improved curl preserves rows with radius three; three-speed member fails rows |
| `W_G`, `W_C` | no: drifting member | no: three-speed member | drift and three-speed members supply finite distinctions, not full axiom models |
| `W_G`, `W_coin` | no: K family | no: scalar three-speed member | K family preserves all rows with two components; scalar three-speed member fails them |
| `W_G`, `W_VC` | conditional on W_EC and W_C | unresolved | exact scalar collapse; W_G alone allows u_V=1 and phi growth |
| `W_EC`, `W_C` | unresolved | unresolved | no complete reciprocal bundle proof; block02 damped construction is a bounded proof import |
| `W_EC`, `W_coin` | no in inert-coin extension: complex law | no: improved curl | doubled class and improved-curl example relax different bundles |
| `W_EC`, `W_VC` | unresolved | unresolved | three-speed member has active auxiliaries; converse not established |
| `W_C`, `W_coin` | no: complex law | no: damped scalar law | complex and damped examples are scoped mathematical alternatives |
| `W_C`, `W_VC` | conditional only jointly with W_G and W_EC | unresolved | three-speed member disproves automatic freezing; drifting phi does not satisfy W_VC and supplies no reverse witness |
| `W_coin`, `W_VC` | unresolved | unresolved | scalar versus auxiliary restrictions are separate predicates; no valid full-bundle witness supplied |

The finite “no” entries concern only the indicated pair; they neither hold
all other bundles fixed nor model all four axioms. All ten pairs are present.
The positive theorem is the conjunction
`W_G + W_EC + W_C => W_VC` for the scalar class; this does not establish
four or five independent walls. Unproved directions remain unresolved.

### N3 — Hidden-wall scan

The scan phrases were searched in this note. "Supplied", "declared" and
"named premise" mark the compilation, the Gauss rows and their charges, and
the premises SF-all, SF-0, EC, CONS, OL, all listed in section 1 as explicit
premises. "Registered"/"registry" occur only in the primitive registry check,
a cited approved-premise surface, not a condition. "By construction", "as is
standard", "naturally", "obviously", "standard QFT", "bridge context" and
"background" occur only in "background charge", which is a named supply. The
sizes 4 and 6, the three-speed coefficients, the coin parameters
(`theta = 3/7`; `theta_E = 2/3`, `theta_B = -1/5`, `K = [[1,2],[3,-1]]`;
`K = [[1,1],[0,1]]`) and the dipole charge are declared finite choices of the
executed witnesses and bind their conclusions. The generic SF-all theorem
is coefficient-uniform on the nondegenerate compilation; the sector/branch
statements require the specified three-speed member and the charged
obstruction requires its stated same-row coefficients and CONS. Connectedness
is proved for the supplied compilation, not a payload-selection axiom.

### N4 — Residual matching

| cited surface (status, read from `docs/audit/data/ledger/<xx>/<id>.json` on this branch) | residual it attacks | residual claimed here | match |
|---|---|---|---|
| historical PR `#7917` (corrected source on main; no audit claim) | the class is not derived from the axioms | item 7's two halves separated; the vertex/cube half conditional on the class's own row | partial: same residual, sharpened on one item; not a prior witness |
| historical closed PR `#7980` (block02 canonical proof dependency) | the residual supply is item-exact (payload, time, locality, conservation) | the conditional auxiliary/coin distinction, with block02 proof witnesses pinned | bounded proof dependency: this note uses its improved-curl and damped witnesses |
| open PR `#7893` (unlanded, no ledger row) | Gauss's law as a support condition among records on quantum links | the Gauss row's shape as the support clause | partial (shape only); its content is a different carrier; not a witness |
| `two_endpoint_gauss_law_invariance_profile_bounded_theorem_note_2026-06-05` (bounded_theorem, unaudited) | endpoint invariance of link-transport operators under Gauss generators | invariance of a constraint surface under a field flow | no: different object; context |
| `signed_gravity_continuum_graded_einstein_localization_note` (bounded_theorem, unaudited) | a Ward/Bianchi constraint surface preserved under formal jet transport | a Gauss surface preserved under a lattice flow | no: same notion, different object and mechanism; context |
| `axiom_first_reeh_schlieder_theorem_note_2026-05-01` (bounded_theorem, unaudited) | the largest invariant subspace of an operator commutant | the maximal invariant subspace inside a constraint surface | no: same tool, different object; context |
| `energy_gauss_constraint_obstruction_route_b_note_2026-07-08` (no_go, unaudited; its docs surface archived) | an energy obstruction for a commuting-auxiliary constraint ansatz | none here | no |
| `chiral_3plus1d_coupled_coin_note` (bounded_theorem, unaudited) | a quantum-walk coin family | a second real field component | no: the word is shared, the object is not |
| `dynamics_nontriviality_selection_firewall_2026-06-06` (no_go, unaudited) | a class is not a selection | none here (this note derives an item inside a class, conditionally) | no |
| `record_classical_semigroup_boundary_2026-06-06` (bounded_theorem, unaudited) | no reversible flow on the post-record algebra | none here | no |

The coin constructions are executed locally. N2 additionally relies on the
explicitly declared block02 improved-curl/damped proof dependency; other rows
are context comparisons, not inherited negative verdicts.

### N5 — Rhetoric and resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "the vertex/cube payloads collapse" | executed: every coefficient's contribution to both rate functionals | executed: delta states at one vertex / one cube; dipole charges | executed: sector multiplicities against full-space multiplicities | executed: the four blocks of `-G^2` and of the rate functionals | executed: maximal invariant subspaces on the whole side-4 and side-6 tori |
| "the rows do not remove the coin" | executed: the 120-pattern coin basis, the sixteen-dimensional class, the six-parameter cut | executed: two components per site read off the assembled generators | executed: kernel dimensions 0 and 116; the harmonic mode's rate `theta` | executed: `K (x) C` and `Theta (x) I` blocks separately | executed: both witnesses assembled on the whole side-6 torus |
| "a nonzero compatible charged surface has no invariant subset under CONS and the same row's nonzero longitudinal coupling" | executed: the unobservable subspace of `(PG, G)` row by row | executed: the dipole at two vertices | — | executed: the affine consistency test | executed: sides 4 and 6 |
| "hidden time is the coin" | executed: the second-order identity entry by entry | — | — | executed: radius of `G^2` | executed: side 6 |

The finite sector resolution refers to the specified three-speed member;
the charged obstruction carries its same-row nonzero coupling, nonzero
compatible charge and CONS hypotheses. The coin kernel comparison names two
zero-onsite local curl copies. None of these finite controls proves formal
four-axiom independence or an independent-wall count.

### N6 — Partial-closure paths and primitive scan

The registry was reread (section 1); no primitive supplies a Gauss row, a
payload clause or a preservation principle, and none is classified as a
wall. Convention or reframing paths found:

- adopting SF-all as the reading of "support forcing" is itself a choice:
  SF-0 is weaker and gives a sector statement instead of a coefficient
  statement; both are executed and both freeze the vertex payload on the
  admissible states, so the vertex/cube verdict does not depend on the
  choice, only its form does;
- adopting a coin change of basis to call the `K (x) C` family "two copies
  of the one-speed law" reframes the coin, it does not remove it (two
  components per site remain, at two speeds);
- the declared class's "one speed" and item 7 could be restated with the
  vertex/cube clause dropped and the one-component clause kept: a convention
  restatement at the terminal's own scope, closing nothing at axiom level;
- `docs/repo/DEFERRED_DECISIONS.md` on `origin/main` parks six owner-bar
  decisions; the parked `M_4(C)` Qubit-domain enlargement would change the
  capacity bound (eight to thirty-two), not any verdict here; none of the
  six names a payload principle.

No path closes `W_coin` by convention. This note does not say "a new axiom
is required"; it says no axiom sentence and no reading of the supplied rows
reaches the wall.

### N7 — Steelman

Hostile reviewer: "The coin is already excluded by the framework you quote.
The Gauss row is a support condition among the corner RECORDS; a record
locks exactly one admissible local possibility, so a record is one number
per site, and a two-component payload would need two records at one site,
which Record forbids. Your coin witnesses violate 'A site never carries more
than one record'." The route is concrete and has a named terminal
obligation. Its gap: a record locks one possibility of the one-site domain,
whose algebraic presentation `M_2(C)` has eight real dimensions; one record
is one point of that domain, and a point carries as many real coordinates as
the domain does. "One record" bounds the payload to one point, not to one
real number; the executed bound is eight components (here and in block 02),
and two fit.
Moreover the components of every law in this note are unrecorded
possibilities evolving between formations — the open bridge block 02 names as
SI — so the Record sentence does not yet bind them at all. What would close
the route is a retained bridge from the recorded readout to a one-real-
coordinate payload per site; no member supplies it. The steelman therefore
does not defeat the scoped claim (the rows and the sentences do not reach
the coin) but it does forbid the broader one ("no route"), which this note
does not make. Disposition: the negative stays at family level with the
readout bridge recorded as the route.

### N8 — Cross-cycle echo

| similar prior wall | retired? | mechanism since | applies here? |
|---|---|---|---|
| block 02's payload wall `W_P` (items 1, 7, OL; historical closed PR `#7980` (routed into #7984)) | partly, here: the vertex/cube clause folds into the Gauss rows | this block's collapse theorem | the coin clause remains; it is `W_coin` |
| the static law does not select the time rule (historical PR `#7915`, its W1) | no | none | untouched; the rows are static content and select no time rule |
| allowed class is not a selected law (`dynamics_nontriviality_selection_firewall_2026-06-06`, unaudited) | no | none | this block derives an item inside a class conditionally; no selection is claimed |
| the sister lane's "alphabet escape" (an enlarged per-site alphabet as an escape from a wall; gravity lane pack, unlanded) | no | none | the coin is the light lane's alphabet escape; the same shape, a different object, and this note records it as a supply, not an escape |
| the evolution axis is declared (single-clock notes, unaudited) | no | reframing as a declared premise | the same reframing is available for SF-all versus SF-0 (a reading choice); executed both ways here |

No structurally similar wall was retired by a mechanism not considered here.

**Coverage result:** all pair predicates and unresolved directions are explicit;
finite alternatives and textual non-supply do not prove formal four-axiom
independence. No independent-wall count or applied audit grade is asserted.

## 13. Falsifiers

The bounded theorem fails if any of the following is found:

- a nearest-neighbor real linear generator on the four-role payload,
  covariant under the even translations and the 24 proper rotations about a
  vertex under the oriented law in the compilation's sign basis, outside the
  ten-dimensional span (sides 4 or 6);
- a real representation of the rotation group on the coin index other than
  the declared trivial one that leaves the sixteen-dimensional count intact
  (with the sign character the checker finds twelve; the sixteen is relative
  to the declared doubled law);
- a member of the class with `a2 != 0` under which the zero-charge electric
  surface is invariant, or a member with `b != 0` under which the magnetic
  surface is; or a nonzero vector in `ker(d0^T d0)` or `ker(d2 d2^T)` that is
  not constant on a positive even torus with n >= 4;
- a conservative member with `a a2 != 0` that leaves a nonempty invariant
  subset of a nonzero compatible electric-charge surface, or a member with `a2 = 0` that does not
  preserve the zero-charge surface;
- a multiplicity of `C^T C` on `ker d0^T` (side 6) other than
  `{0:3, 3:12, 6:24, 9:16}`, or a failure of the specified three-speed member's
  stated restricted spectrum;
- a covariant nearest-neighbor generator on the two-component payload outside
  the sixteen-dimensional class, or a conservative coin member whose electric
  rate functional is not `(Theta_E (x) d0^T) E`;
- a real change of basis carrying the complex law to the specified two zero-onsite local
  curl copies of the one-speed law (its kernel dimension is 0 against 116);
- a witness law that fails a property it is claimed to keep (each property
  of each witness is an executed check);
- an axiom sentence, read at its own scope, that names a Gauss row, a
  constraint-preservation principle, or the number of evolving real
  coordinates at a site.

## Imports

Every underivable input, in plain language, with role, provenance and
open-bridge status stated separately.

- The period-two role compilation (parity roles, oriented `d0`, `C`, `d2`,
  doubled incidence). Role: the arena of every statement. Provenance:
  declared by the light lane's own construction (the historical PR `#7913`),
  rebuilt here from the parity rule. Open bridge: its compilation into the
  homogeneous physical-site law is named open by that PR at its scope; not
  examined here.
- The two Gauss rows and their background charges. Role: the supplied
  constraint content whose preservation is tested. Provenance: the magnetic
  row is `#7917`'s item 5; the electric row is supplied by `#7893`/`#7903`
  and used by `#7917`'s section-6 mode count without being declared among its
  seven items; both are read here as support forcing. Open bridge: the shape is Admissibility's support
  clause; the content (the linear row, the charge) and the identification of
  the row's records with the compiled payload are supplied; the reading of
  "support forcing" as SF-all or SF-0 is a choice, both executed.
- The named premises EC (with OL), CONS, SF-all, SF-0. Role: the hypotheses
  of the conditional verdicts. Provenance: block 02's premises restated in
  section 1 and this note's two readings. Open bridge: SI's connection
  between unrecorded components and the Qualification's record
  configurations (the historical PR `#7915`'s wall W4, at its scope).
- The finite sizes (sides 4 and 6) and the rational witness parameters. Role:
  the executed instances. Provenance: declared here. Open bridge: none; the
  algebra of sections 4-6 is size-uniform on positive even n >= 4 and the classification's constraint
  system is the same linear system at both executed sides.
- Computational tools: integer and rational arithmetic, `sympy` for the
  symbolic cuts and the characteristic polynomial. Role: exact evidence.
  Provenance: standard software; no physics content.
- No comparator is used: continuum Gauss law, Maxwell theory and constraint
  mechanics enter nowhere as inputs; the notion of an invariant constraint
  surface is defined in section 1 and computed exactly.
- The corrected block02 canonical note is a bounded proof dependency for its
  improved-curl and damped constructions, with an upstream citation edge and
  an actual cache input pin. It imports no runtime helper. The other historical
  PR identities above are contextual provenance and grant no inherited verdict.

## Historical review record (original 2026-09-05 source only)

Worker provenance: drafted by a Fable primary seat under the block-03
contract of the campaign pack (`GOAL_block03.md`), with the value gate V1-V5
answered in the pack's `REVIEW_HISTORY.md` before any PR. Refuting checker:
an Opus 5 seat on disjoint machinery (lexicographic state layout, flipped
sign conventions, Levi-Civita curl, the class by signed orbit counting with
no pattern basis, the rate functionals solved rather than checked, ranks
over two primes with exact rational confirmation; 74 independent checks;
CHECKER_block03_findings.md) returned FIX FIRST with no verdict refuted:
findings CK-01..CK-07 (the electric row is not a declared item of the class;
the symmetry group stated in the scope was the wrong one; route R7 leaned on
an unexecuted bound; the doubled law is a premise; the SF-all coin residue is
decoupled copies; SF-0 was used in two senses; a branch miscount), each
verified by the supervisor and applied in the fix pass recorded in the pack's
`REVIEW_HISTORY.md`; its three planted mutations and one fidelity spot-check
were all caught. Independence class: single family (Claude), cross-model —
Fable primary, Opus 5 refuting checker, supervisor line-by-line review with
hand verification of the rate identity, the unobservable-subspace chain and
its dimensions, the coin cut, the hidden-time identity and the sector
multiplicities.
Independent-math checks per conformance section 6, performed by hand
against the runner: the blockwise skew equations of section 3; the rate
identity `d0^T (a2 d0 phi + u_E E + r C^T B) = a2 d0^T d0 phi + u_E d0^T E`
from `(C d0)^T = 0`; the odd-shift conjugation signs of section 2 (entry by
entry on one face and one edge); the unobservable-subspace chain
`P G x = a2 L phi`, `P G^2 x = a a2 L d0^T E`, `P G^3 x = a a2^2 L^2 phi`; the
side-6 multiplicities from the coarse momentum census (26 nonzero momenta;
longitudinal eigenvalues `4 x {3, 6, 9}` with counts `6, 12, 8`); the coin
cut count `16 - 10 = 6`; the second-order identity by substitution. Mutation
checks on scratch copies of the runner (`ROOT` repointed at the worktree; the
repo copy untouched), fourteen probes covering every check family, all
detected with a nonzero exit code (counts in the pack's `RESULTS_block03.md`):
an axiom sentence altered (1 failure, the memo read); one curl sign flipped
(40, from the chain identities down); the z-faces dropped from `d2` (30);
the face payload made scalar (8, from the covariance of `C`); the
classification run under one rotation only (3, the dimension); the
conservation cut's sign (1); the skew defect zeroed (1, the broken member);
the electric rate computed with the unsigned divergence (5); the
edge-from-vertex coupling made inert (13, from conservation of the
three-speed member); the observability stack stopped early (6, the invariant
subspaces); the restricted-multiplicity sign (2, the sector count); the coin
phase set to zero (the kernel-dimension check, after which the mutant aborts
at the hidden-time reconstruction, which divides by the phase); the
second-order coefficient changed (1); the magnetic rate read off the edge
rows (6). The checker's three planted defects were caught as well (the
magnetic rate sign, 3 failures; an invariance test accepting `a2 != 0`, 1;
the coin cut's coupling equations dropped, 2), and its fidelity spot-check
reproduced the primary's second-order-coefficient row exactly. Nothing landed
is replaced or narrowed (this is a new note). Hard landing
conditions: none; no helper runner; the citation-graph manifest co-lands for
the one added node at close.

Quote-fidelity finding for the supervisor (outside this block's file set):
the pack's supplied-input ledger row 4 and the block-03 contract attribute
the phrase "order-independent site-level support forcing among corner
records" to the open PR `#7893`; the live body does not contain it (its
sentence is quoted in section 1), and the note on that PR's head branch does
not contain it either. It is a précis, and this note does not quote it.

## Verification

Run:

```text
python3 scripts/u1_gauss_support_forcing_extended_class_2026_09_05.py
```

Expected final line:

```text
TOTAL: PASS=98 FAIL=0
```

The runner declares `AUDIT_TIMEOUT_SEC = 900`. Runtime reads only the
axiom memo. `AUDIT_INPUT_PATHS` additionally pins both canonical notes for
claim scope and the bounded block02 proof dependency. No repository helper is imported.
The displayed counts describe the corrected finite receipt; the historical
review record above describes the original source only.
