---
claim_id: u1_dynamics_class_axiom_adjudication_bounded_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "On a supplied parity-role cubic compilation with positive even side n >= 4, exact real-linear first-order generator classification gives item 5 from (1,2L,3,4,7,OL) and item 4 from (1,2L,3,5,6,7), with the latter covariance in the oriented representation. Finite classification, chain, conservation, spectrum and alternative-law controls are executed on sides 4,6,8. The alternatives have explicitly delimited retained premises: ordered conditional-mean relaxation is deterministic and is not an Admissibility sampler or a derived diffusive process; the three-shear tick has complete radius three and a non-onsite modified metric; the nonlinear witness conserves a quartic energy. Textual non-supply and finite alternatives do not establish formal axiom independence, an exhaustive independent-wall count, physical electromagnetism, or a selected dynamics."
upstream_dependencies:
  - minimal_axioms
runner: scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py
---

# Conditional Redundancy in the Supplied Real-Linear Edge/Face Generator Class

**Date:** 2026-09-05
**Claim type:** bounded_theorem
**Status:** corrected conditional source; historical review receipts below bind the original source only. Formal audit is deferred. This note changes no audit
verdict, TOE score, axiom, or approved primitive, and it proposes none.
**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Primary runner:**
[`scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py`](../scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py)
**Cached receipt:**
[`logs/runner-cache/u1_dynamics_class_axiom_adjudication_2026_09_05.txt`](../logs/runner-cache/u1_dynamics_class_axiom_adjudication_2026_09_05.txt)
(`TOTAL: PASS=110 FAIL=0`; exact integer, rational and symbolic arithmetic only)

**Target.** Classify conditional implications among the seven declared generator
items, and distinguish those exact results from textual non-supply and finite
alternative laws. “SUPPLIED IN THIS CONDITIONAL CLASS” means an assumption of
this analysis that is not supplied by the quoted memo text; it is not a formal
non-derivability or independence theorem for all models of the four axioms.
The real-coordinate capacity calculation is not a complete axiom model.

**Current context and provenance (2026-09-07).** Corrected source associated with
historical PRs #7913, #7915, #7917, #7920 and #7921 is now on main. Their original
branches are provenance, not current verdicts; their qualified mathematics is
not broadened here. This runner reconstructs the compilation and all its own
witnesses. All fifteen original dated packet bodies under
`.claude/science/physics-loops/u1-maxwell-landing-core-20260905/` are immutable
history. The [dated correction overlay](../.claude/science/physics-loops/u1-maxwell-landing-core-20260905/CORRECTION_2026-09-07.md)
supersedes their current claim/status summaries for this corrected source.

## Result up front

| item (as declared) | verdict | from what | existence witness (all exact) |
|---|---|---|---|
| 1. one real `E` per edge-role site, one real `B` per face-role site | SUPPLIED IN THIS CONDITIONAL CLASS (with one derived bound: at most eight real linear coordinates per site, from Qubit's `M_2(C)`) | no axiom sentence names which coordinate of the possibility domain evolves, nor that one does | a complex (two-real-component) law with an onsite phase: conservative, nearest-neighbor, covariant, gauge-compatible |
| 2. real, linear, first-order, continuous-time evolution | SUPPLIED IN THIS CONDITIONAL CLASS; the memoryless (first-order) clause alone is DERIVED-CONDITIONAL-ON(SI) | the axioms name no time parameter (the memo lists "time metric" and "physical persistence dynamics" among the open gates); the Qualification's one-answer sentence gives memorylessness once the field configuration is taken as the law's state (SI) | a reversible finite tick with complete radius three and a non-onsite conserved metric; a nonlinear quartic-energy law; the complex two-component law. These relax multiple bundled items; section 5 executes deterministic relaxation only |
| 3. a site derivative reads itself and its six physical nearest neighbors only | DERIVED-CONDITIONAL-ON(IP-B); the premise is target-equivalent for this item | "six physical nearest neighbors" is a Lattice fact; what they are (two vertices and four faces for an edge; four edges and two cubes for a face; never a same-role site; opposite-role couplings only at odd distance) is a compilation fact; that a dynamics reads only them is inherited only if the dynamics reads what the Admissibility rule reads (IP-B) | the improved-curl law `L = C(1 + eps C^T C)`: conservative, covariant, gauge- and chain-compatible, minimal payload, support radius three |
| 4. translation and proper-cubic covariance | DERIVED-CONDITIONAL-ON(items 1, 2L, 3, 5, 6, 7) with no orientation premise beyond the oriented `d_0`/`d_2` that item 5 itself names (the covariance is exhibited for the oriented representation); also DERIVED-CONDITIONAL-ON(LR) from the axioms | nearest-neighbor face rows with `L d_0 = 0` and `d_2 L = 0` are exactly the multiples of the oriented curl by one lattice-wide scalar (exact nullspace); conservation then fixes the reverse block and kills onsite terms, and the result is covariant. From the axioms: Lattice's "No site is privileged. Sites are distinguished by the supplied lattice structure alone." read as binding the dynamical law (LR) | an anisotropic law (orientation coefficients 1, 2, 3): conservative, nearest-neighbor, gauge-invariant, not covariant — and, as a consequence, not magnetic-Gauss preserving; a site-privileging law (one face row doubled) |
| 5. the edge-to-face map is invariant under `A -> A + d_0 lambda` and preserves the magnetic Gauss row | DERIVED-CONDITIONAL-ON(items 1, 2L, 3, 4, 7 and OL, the vector-type transformation law of the payload) | the sector-preserving stabilizer of a face-role site (a `D_4` of proper rotations named by the Lattice axiom) fixes exactly the oriented-curl stencil on the four boundary edges; all sixteen signed-permutation payload representations are classified: eight admit a coupling, four distinct couplings result, and only the curl is gauge- and chain-compatible | the unoriented law on the unsigned incidence `S`: conservative, covariant (scalar representation), nearest-neighbor, minimal payload, `S d_0 != 0`, `d_2 S != 0`, no soft mode at zero momentum |
| 6. a positive, diagonal, proper-cubic field energy is conserved | SUPPLIED IN THIS CONDITIONAL CLASS | inside the covariant family `[[u, r C^T],[q C, v]]` conservation is the two-condition cut `u = v = 0`, `w_E r + w_B q = 0`; no axiom sentence names a conserved quantity, a reversible flow, or a stationary measure for a field evolution; the ordered deterministic mean sweep decreases the energy (section 5); no stochastic energy monotonicity is inferred | damped (`u = v < 0`), overdamped (`u = 0, v < 0`: slow root `-s^2 - s^4/gamma - ...`, the diffusive branch), same-sign (`r = +q`: real eigenvalues) — each nearest-neighbor, covariant, gauge- and chain-compatible, minimal payload |
| 7. no vertex, cube, extra coin or hidden time payload | SUPPLIED IN THIS CONDITIONAL CLASS | no axiom sentence restricts which role sites carry an evolving coordinate | a scalar vertex payload `phi`: conservative, nearest-neighbor (a vertex reads its six edges), covariant, gauge-compatible edge-to-face map; a third branch per nonzero momentum (the edge operator becomes the Hodge Laplacian) and a two-speed conservative family |

Two conditional consequences survive: `(1,2L,3,4,7,OL) => 5` and
`(1,2L,3,5,6,7) => 4`. Here **2L means the real-linear first-order generator
clauses of item 2**, in the declared continuous-time matrix formulation. Neither
proof removes those clauses from its premises or proves independence from the
whole time-rule bundle. These implications reorganize a supplied class; they
do not count independent walls or derive that class from the memo.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite real-linear classification and explicitly scoped alternative constructions; structural proofs require positive even n >= 4. Textual non-supply is distinguished from a formal axiom-independence theorem."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "The four axioms do not currently select that class. In particular, they do not state real linear first-order evolution, energy conservation, minimal (E,B) payload, or continuous time."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "A consumer may use either conditional redundancy direction only with 2L and all its other premises. Payload, time, locality and energy supplies remain explicit; pair directions without valid witnesses remain unresolved. The transfer/reflection-positivity route remains open."
conditional_surface_status: "Exact finite controls on sides 4,6,8; nondegenerate structural arguments on positive even n >= 4; LR,IP-B,OL,SI and 2L are retained where used. No selected dynamics or broad axiom non-derivability result."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. The setting: what is supplied, what the axioms say, what is named

**The declared class (quoted at scope from the historical PR `#7917`).** "Declare
the following weak-field dynamics class on the role-compiled physical
lattice: 1. one real electric component lives at each edge-role site and one
real magnetic component at each face-role site; 2. evolution is real, linear,
first order, and continuous in time; 3. a site derivative may use its own
component and the dynamical components among its six physical nearest
neighbors, but no farther site; 4. the law is translation- and
proper-cubic-covariant; 5. the edge-to-face map is invariant under
`A -> A+d_0 lambda` and preserves the magnetic Gauss row; 6. a positive,
diagonal, proper-cubic field energy is conserved; and 7. no vertex, cube,
extra coin, or hidden time payload participates." Its own boundary (the PR body, and the note on its head branch): "This is a
bounded conditional classification, not an axiom derivation or TOE-status
change." and "The
four axioms do not currently select that class. In particular, they do not
state real linear first-order evolution, energy conservation, minimal
`(E,B)` payload, or continuous time." This note adjudicates that boundary
item by item; it neither uses the class as a premise nor treats the PR as
authority.

**The supplied role compilation (a named supply, never derived here).** On a positive even periodic cubic lattice with side `n >= 4` every site carries a role label equal to its
coordinate parity up to one of eight sector offsets; Hamming weight zero,
one, two, three is vertex, edge, face, cube; an edge on axis `i` is
oriented along `e_i`; a face with normal `e_k` has the ordered plane pair
`(i, j)` with `e_i x e_j = e_k`. The oriented incidence maps are the vertex
gradient `d_0`, the edge-to-face curl `C` (a face reads `E_i(f - e_j)`,
`-E_i(f + e_j)`, `E_j(f + e_i)`, `-E_j(f - e_i)`), and the face-to-cube
divergence `d_2`. This is the doubled incidence declared in the historical PR `#7913` ("Valid even-torus role fields are exactly eight translated
sectors."); the
runner rebuilds it from the parity rule alone and re-proves its facts. Sector
zero is used throughout; the law-level statements hold in every sector by
translation.

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
nearest-neighbor conditions." Record: "Records form." "A site never carries
more than one record; records are permanent." "Only records are readable. A
readout value is determined by record content alone. A site with no record
cannot be read." Qualification: "A law privileges no states. Its domain is a
supplied condition, and at every state where the condition holds it gives
exactly one answer." The memo's own boundary: "Admissibility is not a
dynamics axiom." It does not "choose a Hamiltonian or transfer operator ...
define a time metric, or provide a record-production process or physical
persistence dynamics"; "arrow, record-production dynamics, physical
persistence dynamics, time metric, and local observability of records"
remain outside axiom content; and "The 2026-08-13 owner-approved revision
removed the named scalar functional `I`, finite additivity over disjoint
record collections, and `I(empty)=0` from Record."

**Primitive registry check.** `docs/audit/data/axiom_premise_nodes.json`
was read: the scale-reference primitive is units only; the kinetic-isotropy
primitive supplies the structural ratio `c_t = c_s` and, by its own note, "is
not a new dynamics"; the realized-state primitive is pointwise evaluation
only. None is classified below as a wall, an import, or a source of bounded
status; none supplies any of the seven items.

**The named premises.** These are explicit conditions, not new axioms.
2L denotes the real-linear first-order generator clauses of item 2. The nonlinear
map `E_dot=0, B_dot=C(E^3)` is nearest-neighbor and oriented-covariant but fails
gauge compatibility (24 nonzero defect entries on side 4); it shows why 2L
cannot be dropped from the item-5 tuple. No claim is made that each whole
bundled premise has an independent witness.

- LR (law-level reading): the dynamical law is a law in the Qualification's
  sense, so that Lattice's no-privileged-site sentence and the
  Qualification's no-privileged-state sentence bind it, with the proper
  cubic rotations about each site counted as part of "the supplied lattice
  structure" because the Lattice axiom names them.
- IP-B (neighborhood inheritance): the dynamical rule at a site is a fixed
  function of the same six-neighbor conditions the Admissibility rule reads.
- IP-A (hypothetical per-site sampling identification): the per-site update of
  the dynamics draws the site's value from the Admissibility conditional
  given the current neighbor conditions. No complete update schedule or
  inference from this hypothetical draw to the item-3 generator is supplied.
- OL (orientation law): the edge payload transforms as an oriented edge
  quantity and the face payload as an oriented face quantity — the vector
  components along the edge axis and the face normal — the same convention
  the compilation uses for its oriented link value.
- SI (state identification): the configuration of the dynamical components
  is the domain element on which the law acts, so that the Qualification's
  one-answer sentence applies to it.

## 2. Compilation facts, and which of them are lattice facts

The runner establishes exactly, on the side-4, side-6 and side-8 tori:

- the role census (`n^3/8` vertices and cubes, `3 n^3/8` edges and faces), the
  shell census (an edge sees two vertices and four faces; a face sees four
  edges and two cubes; a vertex six edges; a cube six faces), and the absence
  of any same-role nearest-neighbor pair;
- the parity theorem: the torus distance between an edge site and a face
  site is always odd, between two same-role sites always even. Hence an
  opposite-role coupling has physical radius one or at least three, and a
  same-role coupling has radius at least two;
- the chain identities `C d_0 = 0`, `d_2 C = 0` over the integers; every
  curl row couples a face to four nearest-neighbor edges with signs
  `(+1, +1, -1, -1)`;
- the eight parity translates satisfy the neighbor bit-flip rule (translation
  permutes sectors); every proper rotation about a site of every role type
  maps the role field onto one of the eight sectors, and rotations about a
  vertex or cube site fix the sector (24 each) while about an edge or face
  site exactly eight do;
- the oriented curl and the gradient are covariant under all 24 proper
  rotations about a vertex and under all even translations.

Adjudication of item 3's phrase "six physical nearest neighbors": that a
site has six nearest neighbors is the Lattice axiom (adjacency on `Z^3`).
Which roles they carry, that no same-role site is among them, and that a
face's boundary sits at physical distance one, are facts of the supplied
compilation, not of the lattice. That a dynamics reads only them is neither:
it is a property of a supplied dynamics, inherited only under IP-B.

## 3. Covariance forces the curl: the classification behind item 5

**Theorem (exact, side 4; stabilizer argument at every positive even size n >= 4).** Let the
payload be one real component at every edge-role and face-role site,
transforming under the sector-preserving lattice symmetries by a signed
permutation. Up to a diagonal sign relabelling of the payload — the
compilation's own sign basis is part of the supply, and OL names it — every
such transformation law is induced from a character of
the site stabilizer (a `D_4` of proper rotations about the site, all named by
the Lattice axiom); the characters are realized by tensor transport, so the
edge payload transforms as a scalar or as the vector component along its
axis, each optionally twisted by the rotation group's global sign character
(the parity of the axis permutation), and likewise the face payload as a
scalar or as the vector component along its normal. This gives sixteen laws
in the compilation's sign basis. (A sign relabelling gives a further
signed-permutation law with the same site action — the runner's witness
negates the payload at every `z`-normal face; its covariant coupling `D C`
satisfies `D C d_0 = 0` but `d_2 D C != 0` — which is why OL's convention
clause is load-bearing rather than decorative.) For each, the space of translation- and
proper-cubic-covariant real linear nearest-neighbor generators on the payload
is computed exactly as the nullspace of the covariance constraints on the 30
translation-covariant nearest-neighbor patterns:

- the onsite terms are always covariant (two dimensions);
- a covariant edge-face coupling exists exactly when the two characters
  agree on the in-plane 180-degree flip (eight of sixteen laws), and it is
  then unique up to scale in each direction (total dimension four);
- the eight coupling-admitting laws carry exactly four distinct couplings:
  the oriented curl `C` (for the vector/vector law and its global sign
  twist), the unsigned incidence `S` (scalar/scalar and its twist), and their
  two sign-twisted partners whose one-face stencils are `(1,-1,-1,1)` and
  `(1,-1,1,-1)`;
- exactly `C` satisfies `X d_0 = 0` and `d_2 X = 0`.

The one-face argument that makes this uniform for positive even n >= 4: the eight
sector-preserving proper rotations about a face-role site act on the four
boundary-edge values; the 90-degree rotation about the normal cycles them
with the vector signs `(a, b, c, d) -> (-d, a, -b, c)`, and the only stencil
invariant under it with the face value fixed is `(1, 1, -1, -1)`, the
oriented curl; for the scalar law it is `(1, 1, 1, 1)`. The runner performs
this stabilizer computation for all sixteen character pairs and separately
re-derives, by its own row reduction, that the gauge-invariant one-face
stencils are exactly the curl multiples.

**Verdict on item 5.** Given items 1, 2L, 3, 7 (real-linear first-order generator, one real component, nearest
neighbor, no other payload) and item 4 (covariance), the edge-to-face map is
a multiple of the covariant coupling; under OL that coupling is the oriented
curl, and both clauses of item 5 are then the chain identities of the
compilation. So item 5 is DERIVED-CONDITIONAL-ON(1, 2L, 3, 4, 7, OL). The
witness that OL is load-bearing is the unoriented law
`[[0, -S^T],[S, 0]]`: nearest-neighbor, covariant under the scalar
representation, conserving `(|E|^2 + |B|^2)/2`, minimal payload, with
`S d_0 != 0` and `d_2 S != 0`, and with no soft mode at zero momentum (the
unsigned incidence maps the three constant edge fields to three independent
face fields while the curl annihilates them). Relative to the four axioms
alone, item 5 inherits the status of its premises: OL is a supply (the
axioms fix no transformation law for a payload they do not name), and items
1, 2L, 3, 4, 7 are adjudicated in their own rows. The conclusion does not rest
on the enumeration: section 4's nullspace theorem is representation-free —
any nearest-neighbor face row with `L d_0 = 0` and `d_2 L = 0` is a
lattice-wide multiple of the curl — so only the curl is gauge- and
chain-compatible whatever transformation law is supplied.

## 4. Compatibility forces covariance: the redundancy behind item 4

**Theorem (exact, sides 4 and 6 in full generality).** Let each face row read only its four boundary edges with free
coefficients (96 unknowns on side 4). The constraints `L d_0 = 0` and
`d_2 L = 0` alone — no covariance assumed — leave exactly a one-dimensional
space, spanned by the oriented curl. The mechanism: gauge invariance on one
face star forces each row to be a multiple `q_f` of its own curl; the
magnetic Gauss identity around every cube then forces `q_f` equal on all six
faces of the cube (each cube edge lies in exactly two of them with opposite
signs), and cube connectivity makes `q_f` one lattice-wide scalar (on side 6 the
full 324-coefficient nullspace is again one-dimensional and spanned by the
curl, and the reduced nullspace over the 81 face coefficients is the
all-ones vector). With item 6, the diagonal blocks vanish and the reverse block is the
weighted negative adjoint `-(w_B / w_E) q C^T`, so the generator is
`c [[0, -C^T],[C, 0]]` after normalization — covariant under all 24 proper
rotations and all even translations.

**Verdict on item 4.** DERIVED-CONDITIONAL-ON(1, 2L, 3, 5, 6, 7), with no
orientation premise beyond item 5's own: the oriented structure enters
through `d_0` and `d_2` inside item 5 itself, and the covariance is
exhibited for the oriented (vector/vector) representation and its global
sign twist — the same matrix is not covariant under any of the other
fourteen laws, so "covariant" here means covariant under the law the
compilation's oriented incidence selects. The anisotropic law with orientation coefficients
`(1, 2, 3)` is the witness in both directions: it is nearest-neighbor,
conservative, minimal-payload and gauge-invariant (`L d_0 = 0`), it is not
covariant, and — this is the same fact seen from the other side — it fails
`d_2 L = 0`. A second witness, one face row doubled, breaks translation
covariance and the magnetic chain identity: `L d_0=0` still holds, but
`d_2 L` has eight nonzero entries on side 4. It does not keep item 5.
At side two the constructor has `d_0=C=d_2=0`; a nonzero nearest-neighbor
map then obeys both constraints without being a curl multiple. This is the
explicit excluded degenerate boundary of the structural theorem.

**The axiom lever.** Item 4 is the one item with a sentence of its own in the
axioms: "No site is privileged. Sites are distinguished by the supplied
lattice structure alone." A law with a site-dependent coefficient
distinguishes sites by something other than the supplied structure; a law
with an orientation-dependent coefficient distinguishes directions the
Lattice axiom's named rotations relate. Under LR — that the dynamical law is
a law in the Qualification's sense and so bound by these sentences — item 4
is DERIVED-CONDITIONAL-ON(LR), and the compilation's covariance (re-proved in
section 2) carries the covariance from the lattice to the compiled payload.
LR is weaker than the item (it is a reading of scope, not a statement about
any generator) and it is not forced: the Qualification allows "further
physical structure" to be supplied, and a supplied dynamics may be read as
exempt from the no-privileged-site sentence. The two witnesses above are the
laws LR excludes.

## 5. Conservation (item 6): a two-condition cut that no axiom sentence makes

Inside the covariant nearest-neighbor family of section 3 (vector/vector law)
the general generator is

```text
G = [[u I, r C^T],
     [q C, v I]],           u, v, q, r real.
```

Positive diagonal conservation, `M G + G^T M = 0` with `M = diag(w_E I, w_B I)`
and `w_E, w_B > 0`, is blockwise `2 w_E u = 0`, `2 w_B v = 0`,
`w_E r + w_B q = 0` (symbolic, checked). So item 6 is exactly the cut
`u = v = 0`, `r = -(w_B / w_E) q`, after which field rescaling leaves the
one-speed generator. The runner checks the surviving member exactly: metric
skew defect zero; `dH/dt = 0` on a random rational field; both Gauss rows
preserved; on the side-6 torus the edge operator `C^T C` satisfies
`Q(Q-3)(Q-6)(Q-9) = 0` with multiplicities `{0:29, 3:12, 6:24, 9:16}`, i.e.
two transverse branches at each of the 26 nonzero momenta, the 29 zero modes
being 26 gradients and three harmonic fields; the face operator has the same
nonzero multiplicities. Per-site energy `E_e^2 / 2` is not conserved even by
this member; only the lattice-wide sum is.

**No axiom sentence reaches the cut.** Admissibility determines a
distribution and its variation; the memo says it does not "choose a
Hamiltonian or transfer operator". Record's sentences concern locking,
uniqueness, permanence and readability of records; none names a quantity
conserved along an evolution of unrecorded possibilities, and "records are
permanent" cannot be read as a tick or as reversibility of a field law: a
site records once, so a field that evolves at a site is not a sequence of
records there. Qubit names a domain, not a flow on it; Lattice names sites
and their symmetries. The Qualification's "gives exactly one answer" is
about determination, not invariance.

**The three witnesses**, each nearest-neighbor, covariant, with the
gauge-compatible edge-to-face block `q C`, and minimal payload:

- damped, `u = v = -1/3`, `q = 1`, `r = -1`: `dH/dt < 0` on a random rational
  field; trace `-54` on side 6, so no positive form of any kind is conserved;
- overdamped, `u = 0`, `v = -2`, `q = 2`, `r = -1`: per transverse mode with
  symbol `s` the characteristic polynomial is
  `lambda^2 + gamma lambda + gamma s^2`, whose slow root is
  `-s^2 - s^4/gamma - ...` — the diffusive infrared root of this
  separately supplied generator — against the conservative member's `+/- i s`;
- same-sign, `r = +q`: `G^2 = diag(C^T C, C C^T)` has the eigenvalue `9 > 0`,
  so `G` has real eigenvalues and conserves no positive form.

**Deterministic conditional-mean relaxation is a separate construction.**
For the formal quadratic weight `exp(-kappa |CA|^2/2)`, each single-edge
conditional is a proper Gaussian when `Q_ee>0`, with `Q=C^T C`. The full-space
weight is improper because gradient and harmonic directions are flat. The
runner executes one fixed-order Gauss-Seidel sweep of conditional means,
which decreases `A^T Q A/2` on its supplied rational state. It makes no random
draws. A single-coordinate mean reads Q-coupled edges at distance two; this
is not a bound on the complete ordered sweep's radius. On side 4 the actual
sweep has a translation commutator with 572 nonzero entries.

At zero and `kappa=1`, the single-edge conditional variance is `1/Q_ee=1/4`
and its expected post-draw energy is `1/2`, whereas the deterministic mean
sweep fixes zero. Thus the calculation proves neither stochastic energy
monotonicity nor IP-A covariance/locality nor selection of a diffusive time
law. No auxiliary nearest-neighbor sampler is constructed here. The symbolic
overdamped eigenvalue calculation above is for its separately supplied
continuous generator. Current main's corrected time-fork context likewise
keeps the projected OU process and finite auxiliary heat bath distinct.

**Item 6 against the 2026-08-13 revision (the required edge case).** The
revision "removed the named scalar functional `I`, finite additivity over
disjoint record collections, and `I(empty)=0` from Record." A positive
diagonal field energy is a scalar, finitely additive over disjoint site
collections, zero on the empty collection: the exact shape of the removed
structure, transported from records to unrecorded field components. What
the revision implies: the current Record supplies no additive scalar of any
kind, so even a "record energy" is not axiom content, and re-supplying an
additive scalar is a bar item, not a derivation. What it does not imply:
(i) it does not forbid a supplied additive scalar as downstream structure
(the memo: such rows "must cite a separate retained authority or remain
conditional/open"); (ii) it is silent on conservation, which is dynamical —
additivity is static — and the pre-revision Record, which had `I`, named no
dynamics either, so item 6 was never Record content before or after the
revision. Item 6 needs three things: an additive positive scalar, a
dynamics, and the invariance of the first under the second; the revision
removed the first for records; the axioms never contained the second or
third for anything. Verdict: SUPPLIED IN THIS CONDITIONAL CLASS.

## 6. The time rule (item 2): the axioms name no time parameter

The four axioms contain no time parameter, tick, order of events beyond a
site's single record, or update law: the memo lists "time metric" and
"physical persistence dynamics" among the open gates outside axiom content,
and "update laws" among the formation rules it does not supply. The
kinetic-isotropy primitive names "the emergent evolution tick" and fixes
only the ratio `c_t = c_s`; by its own note it is "not a new dynamics", and
whether "one tick is one edge in form" refers to a continuous parameter, a
finite-depth cycle, or only the regulator form is the interpretation
boundary the historical PR `#7921` names for the owner; nothing here reads it as
selecting continuous or discrete time. So "continuous in time" is a supply.
Witness with multiple relaxed premises: the reversible finite tick — the three-shear leapfrog `B += (h/2) C E`,
`E -= h C^T B`, `B += (h/2) C E` — is checked exactly on side 6 at `h = 1/2`:
each shear reads one site and four opposite-role neighbors; `U(-h) U(h)` is
the identity; each shear preserves its Gauss row; the modified energy
`|B|^2/2 + |E|^2/2 - (h^2/8)|C E|^2` is conserved exactly and is positive
because `spec(C^T C) <= 9 < 4/h^2`; and the one-tick map is not `exp(h G)`.
This schedule preserves items 1, 4, 5 and 7 at the checked scope.
Each shear is nearest-neighbor, but the complete map has radius three and
therefore fails the complete-map version of item 3. The metric contains
`C^T C` and is not the onsite diagonal quadratic form of item 6. At `h=1/2`,
side-6 squared singular values 3 and 6 require incompatible onsite weight
ratios `13/16` and `5/8`. The actual modal comparator is the original
generator exponential: at squared singular value 3 the tick has E-entry
`5/8`, while `cos(sqrt(3)/2)>5/8` by a rational alternating-series lower
bound; their upper-right Taylor coefficients also differ at order `h^3`.
This excludes equality to that original exponential, not every continuous
flow embedding. The witness relaxes the time, complete-locality and energy bundles.

"Linear" is a supply. Witness: `dE/dt = -C^T (B + eps B^3)`,
`dB/dt = C E` (componentwise cube, `eps = 1/5`) conserves the positive
energy `|E|^2/2 + |B|^2/2 + (eps/4)|B|^4` exactly, is nearest-neighbor,
covariant and gauge-compatible, and fails homogeneity of degree one.

The quartic energy is not item 6's quadratic diagonal form: the runner also
checks that the original unit quadratic energy has nonzero rate. Thus this
witness is not an independent countermodel obtained by removing linearity alone.

"Real" (one real component) is item 1's supply restated; the complex law of
section 7 is its witness. "Deterministic" is supplied here. Section 5 is deterministic relaxation and
provides no stochastic-law witness for independence of this clause.

The one clause with an axiom lever is "first order". Under SI — the field
configuration is the element of the law's domain — the Qualification's "at
every state where the condition holds it gives exactly one answer" says the
rate (or the next-step distribution) is a function of the configuration
alone: no memory, no velocity outside the state. That is memorylessness, the
first-order clause; it is weaker than item 2 (it gives neither linearity,
determinism, nor a continuous parameter), and it is not independent of item
7: any finite-order law is first-order on an enlarged payload, so
"first-order" is a statement about what the payload is. SI itself is a
supply: the Qualification's state is "a configuration of records", and the
components here are unrecorded possibilities whose connection to records is
the open bridge the historical PR `#7915` lists as its wall W4.

## 7. The payload (items 1 and 7): what Qubit bounds and what it leaves

Qubit names the possibility domain and its presentation `M_2(C)`; it does
not name a coordinate on it that evolves, nor that exactly one real
coordinate does, nor which role sites carry one. The one thing it does fix:
a real-linear one-site coordinate system has at most `dim_R M_2(C) = 8`
components, so a linear one-site payload has at most eight real components
(a nine-component linear payload cannot be a one-site coordinate; a
composite object spread over several sites is outside this bound, as the
historical PR `#7913` notes for its own alphabet). Every witness in this note fits
(one, one, two, one components per site).

Item 1 witness: one complex scalar per edge and face with an onsite phase
`theta = 3/7` — `dE/dt = -C^T B + i theta E`, `dB/dt = C E + i theta B` —
is a real-linear, nearest-neighbor, covariant, gauge-compatible law
conserving `sum |E|^2 + sum |B|^2` exactly, with two real components per
site. It is the minimal member of the payload class the historical PR `#7921`
declares for its radius-one obstruction.

Item 7 witness: a scalar `phi` on the vertex-role sites,
`d phi/dt = -d_0^T E`, `dE/dt = d_0 phi - C^T B`, `dB/dt = C E`. It conserves
`(|phi|^2 + |E|^2 + |B|^2)/2` exactly, is nearest-neighbor (a vertex reads
its six edges, an edge its two vertices and four faces), is covariant, and
keeps the gauge-compatible edge-to-face block. Its edge operator `-G^2|_E`
is the Hodge Laplacian `d_0 d_0^T + C^T C` with multiplicities
`{0:3, 3:18, 6:36, 9:24}` on side 6: three branches at every nonzero
momentum instead of two — the longitudinal sector propagates. And the
extended covariant nearest-neighbor class (dimension seven: three onsite
terms, `C`, `C^T`, `d_0`, `d_0^T`, classified exactly) has a conservative
subfamily with two independent ratios (`a_2 = -w_V a / w_E` and
`r = -w_B q / w_E`), so with a vertex payload the conservative law is unique
only up to two speeds (`a = -2`, `a_2 = 2` is checked to conserve). Item 7 is
what makes the terminal's "up to one speed" true; the axioms do not supply
it.

## 8. Locality (item 3): what is a lattice fact and what needs the identification premise

Section 2 settled the phrase: six neighbors is the Lattice axiom; their
roles and the odd-distance parity of edge-face couplings are compilation
facts. The declared dynamics has item-3 locality under IP-B: the Admissibility sentence is about the
admissibility rule, and the memo says that rule is not a dynamics. IP-B is
exactly as strong as item 3 for the dynamics (it says the rule reads the
six-neighbor conditions), so the verdict is DERIVED-CONDITIONAL-ON(IP-B)
with a target-equivalent premise — a sharpened residual, not a derivation.
Witness without IP-B: the improved curl `L = C (1 + eps C^T C)`,
`eps = 1/7`, on the side-8 torus: the generator `[[0, -L^T],[L, 0]]` is
conservative, gauge- and chain-compatible (`L d_0 = 0`, `d_2 L = 0`),
covariant, minimal payload, and its support radius is exactly three — the
smallest possible beyond one, by the parity theorem.

## 9. The seven-row obligation table

| item | verdict | derivation, or the exact terminal missing lemma | strength of the missing lemma against the item |
|---|---|---|---|
| 1 | SUPPLIED IN THIS CONDITIONAL CLASS | missing: a sentence selecting one evolving real coordinate of `M_2(C)` at edge and face roles; the axioms give only the capacity bound eight | comparable: it is the item |
| 2 | SUPPLIED IN THIS CONDITIONAL CLASS (memoryless clause DERIVED-CONDITIONAL-ON(SI)) | missing: a time parameter and its continuity, linearity, determinism; the Qualification gives memorylessness given SI | continuous time: target-equivalent (a time-parameter supply); linearity and determinism: comparable |
| 3 | DERIVED-CONDITIONAL-ON(IP-B) | IP-B restates the item for the dynamics | target-equivalent (`blocked-equivalent` in the registry sense) |
| 4 | DERIVED-CONDITIONAL-ON(1, 2L, 3, 5, 6, 7); DERIVED-CONDITIONAL-ON(LR) | section 4 (exact nullspace; orientation only through item 5's `d_0`/`d_2`); LR from Lattice's no-privileged-site sentence | LR is weaker than the item (a scope reading); the items 1, 2L, 3, 5, 6, 7 are adjudicated in their rows |
| 5 | DERIVED-CONDITIONAL-ON(1, 2L, 3, 4, 7, OL) | section 3 (exact classification; one-face stabilizer at every positive even size n >= 4) | OL is weaker than the item (a one-bit transformation-law choice among sixteen) |
| 6 | SUPPLIED IN THIS CONDITIONAL CLASS | missing: a conservation, reversibility or self-adjointness principle for an evolution of unrecorded possibilities; the nearest kin was removed from Record on 2026-08-13 and never contained a dynamics | target-equivalent |
| 7 | SUPPLIED IN THIS CONDITIONAL CLASS | missing: a sentence restricting the evolving coordinates to the edge and face roles | comparable: it is the item |

## 10. Explicit remaining assumptions

The named bundles are payload (items 1,7,OL), time rule (item 2), locality
(item 3), conservation (item 6), and the disjunction of symmetry items 4 or 5.
They organize this conditional analysis; five labels do not establish five
independent walls. SI conditionally addresses the memoryless interpretation,
and sections 3–4 give precisely the two implications with 2L retained.
Other pairwise directions without complete witnesses remain unresolved.

## 11. What is and is not claimed

Claimed: the exact finite statements listed in sections 2-8 on the side-4,
side-6 and side-8 compiled tori; the one-face stabilizer argument and the
cube-connectivity argument, which hold at every positive even size n >= 4; the per-item
verdicts with their named premises; the existence witnesses.

Not claimed: that any item follows from the four axioms alone; that any
dynamics class, time rule, or member of the fork is selected; any
infinite-volume, continuum, thermodynamic or Lorentz statement; any Record
readout of `E` or `B`; any identification with electromagnetism; any change
to an axiom or primitive; any audit verdict. Historical PR identities are provenance; corrected main context is identified
above. No historical review label applies a present source or audit verdict.

## 12. No-Go Discipline Gate

The negative scope is textual non-supply plus finite conditional alternatives,
not formal non-derivability from all four axioms. The following N1–N8 record
what was computed, what is contextual and what remains open; they do not add
an independent-wall count or an exhaustive search claim.

### N1 — Alternative route enumeration

Each row is a distinct family under the tuple (object, mechanism, terminal
obligation). Contextual sources and textual arguments are distinguished from executed
finite constructions. No route count is an axiom-independence proof.

| route | what it would attempt | why it fails here | marker |
|---|---|---|---|
| R1 permanence-to-reversibility | infer field conservation from permanent records | textual scope comparison only: permanence does not state a field update. The deterministic mean sweep is not a reversible stochastic update, so it does not decide this proposed bridge | TEXTUAL; bridge unresolved |
| R2 no-privileged-state | read "A law privileges no states" as excluding attractors, hence forcing measure preservation | the damped law applies one rule at every state; and excluding attractors leaves the same-sign law (no attractor, conserves no positive form) and the unoriented law (conserves, but is not the class); the sentence concerns the law's domain, not invariants (runner sections F, H) | ATTEMPTED |
| R3 sampling identification | build a dynamics from Admissibility conditionals (IP-A) | the actual mean sweep is deterministic and scheduling-dependent; the Gaussian single-edge draw raises expected energy from zero. Neither supplies a complete covariant nearest-neighbor sampler or identifies the overdamped law | EXECUTED DISTINCTION; process bridge open |
| R4 kinetic-isotropy primitive | read "the emergent evolution tick" or the OS0 normalization as a self-adjoint transfer structure | the registered primitive's own note: "not a new dynamics", supplies only `c_t = c_s`; registry check performed; the primitive is an approved premise, not a wall, and it supplies no item | RULED OUT BY PRIOR (approved primitive source note, registry node `kinetic_isotropy_primitive`) |
| R5 Record additivity | use the additive record scalar as the energy and its invariance as the law | the structure was removed from Record on 2026-08-13 and, before that, contained no dynamics; the axiom memo is the canonical premise node | RULED OUT BY PRIOR (the axiom memo's 2026-08-13 paragraph) |
| R6 Noether from covariance | derive a conserved quantity from item 4 or LR | a symmetry yields a conserved quantity only through a supplied variational or Hamiltonian structure; the damped law is fully covariant and conserves no positive form (runner section F) | ATTEMPTED |
| R7 per-site unitarity from Qubit | read `M_2(C)` as forcing a per-site norm-preserving update, then sum | the conservative member does not conserve per-site energy (runner section F); the lattice-wide energy is not a per-site fact; and per-site norm preservation with a complete nearest-neighbor map is the object of the historical PR `#7921`'s obstruction at its own scope (an evidence address, not a premise) | ATTEMPTED |
| R8 reflection positivity of a transfer interpretation | supply a Euclidean transfer reading of the compiled static law, prove reflection positivity, reconstruct a self-adjoint generator | not closed: this is the live route of N7; it needs two supplied structures (a path-product transfer interpretation and an evolution axis) | OPEN (not counted as closed) |

### N2 — Pair coverage with explicit unresolved directions

Predicates: `W_P` = items 1,7,OL; `W_T` = the whole item-2 bundle;
`W_L` = complete item-3 locality; `W_C` = item-6 positive onsite quadratic
conservation; `W_S` = item 4 **or** item 5. All examples live on the supplied
compilation. The table records both directions and does not claim that a
multi-premise witness is a complete four-axiom model or proves independence.

The “no” entries below are finite counterexamples to the indicated pair
implication only. They do not hold every other bundle fixed and do not prove
four-axiom independence. The missing reverse W_C/W_T witness stays unresolved.

| pair | first implies second? | second implies first? | exact finite witness scope |
|---|---|---|---|
| `W_P`, `W_T` | no: nonlinear law | no: vertex law | nonlinear keeps minimal oriented payload; vertex law is real-linear continuous but adds phi |
| `W_P`, `W_L` | no: improved curl | no: complex law | radius three versus an extra component at radius one |
| `W_P`, `W_C` | no: damped law | no: vertex law | minimal payload with dissipation; conserved energy with extra phi |
| `W_P`, `W_S` | no: anisotropic law | no: complex law | anisotropy keeps the oriented payload but fails covariance and magnetic chain |
| `W_T`, `W_L` | no: improved curl | no: nonlinear law | linear continuous radius three; radius-one nonlinear rate |
| `W_T`, `W_C` | no: damped law | unresolved | quartic nonlinear energy and tick modified metric do not satisfy W_C |
| `W_T`, `W_S` | no: anisotropic law | no: nonlinear law | linear time with neither symmetry clause; nonlinear covariant/gauge-compatible rate |
| `W_L`, `W_C` | no: damped law | no: improved curl | complete radius one without conservation; quadratic conservation at radius three |
| `W_L`, `W_S` | no: anisotropic law | no: improved curl | radius-one law fails both clauses; improved curl keeps both with radius three |
| `W_C`, `W_S` | no: anisotropic law | no: damped law | unsigned law would not work here because it satisfies W_S via covariance |

The positive conditional implications are separately exact:
`(1,2L,3,4,7,OL) => 5` and `(1,2L,3,5,6,7) => 4`.
No count of independent walls follows from this coverage table.

### N3 — Hidden-wall scan

The scan phrases were searched in this note. "Supplied", "declared" and
"named premise" mark the compilation, OL, SI, IP-A, IP-B and LR, all listed
in section 1 as explicit premises. "Registered"/"registry" occur only in the
primitive registry check, which is a cited approved-premise surface, not a
condition. "By construction", "as is standard", "naturally", "obviously",
"standard QFT", "bridge context" and "background" do not occur as
load-bearing phrases. The sizes 4, 6, 8 and the rational parameters
(`h = 1/2`, `eps = 1/7`, `eps = 1/5`, `theta = 3/7`, `gamma = 2`) are
declared finite choices. They bind the corresponding witness conclusions.
The one-face and connectivity arguments separately require nondegenerate
positive even n >= 4; 2L is explicit wherever a matrix classification is used.

### N4 — Residual matching

| cited surface (status) | residual it attacks | residual claimed here | match |
|---|---|---|---|
| historical PR `#7917` (corrected source on main) | the class is not derived from the axioms | the class, item by item, with witnesses | partial: same residual, sharpened; not a prior witness |
| historical PR `#7915` (corrected source on main) | the static law does not select among three time rules | the deterministic mean sweep is separated from any stochastic/diffusive identification | partial: the supplied overdamped generator remains a separate finite law |
| historical PR `#7921` (corrected source on main) | raw onsite unitarity with a complete radius-one map kills transport | lattice-wide conservation is not a per-site fact | no: different residual; used in R7 as an evidence address only, not as a witness |
| `DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06` (no_go, unaudited) | the Wilson gauge-invariant-local class does not select a Hamiltonian | the declared edge/face class is not selected by the axioms | no: different class and mechanism; context |
| `RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06` (bounded_theorem, unaudited) | no reversible flow on the finite post-record algebra | no conservation principle for unrecorded fields | no: different object; context for R1 |
| `DYNAMICS_FORM_FROM_RECORD_PRESERVATION_..._2026-06-05` (bounded_theorem, unaudited) | gauge covariance of a supplied Hamiltonian from record preservation under bridges | gauge compatibility from cubic covariance of the compiled payload | no: different mechanism; N8 echo |
| `SINGLE_CLOCK_AXIS_SELECTION_..._2026-06-11` (no_go, unaudited) | the evolution axis is a declared premise | the axioms name no time parameter | partial (shape); not needed as a witness |

These are context comparisons, not imported negative theorems. The runner
reconstructs the finite alternatives; their limitations are stated above.

### N5 — Rhetoric and resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "item 6 is not automatic within the supplied linear family" | executed: the four family parameters and the exact two-condition cut | executed: per-site energy is not conserved even by the conservative member, so conservation is a lattice-wide fact only | executed: witness spectra (symbolic slow root; real eigenvalues) | executed: skewness per block | executed on the side-6 torus; no infinite-volume statement |
| "the axioms name no time parameter" | textual (memo integrity read) | — | executed: the actual modal Taylor/exponential comparator distinguishes the original G only | executed: shear by shear | executed: the full tick on side 6 |
| "items 1 and 7 are supplies" | executed: capacity bound eight | executed: two components per site; vertex sites carrying a component | executed: the third branch multiplicities | executed: the seven-dimensional extended class | executed on side 6 |
| "covariance forces the curl" | executed: sixteen characters, four couplings | executed: the face-site stabilizer | — | executed: coupling blocks | executed: side 4 in full generality |

The finite tests certify these supplied mathematical objects and their named
premises. The memo checks establish quoted textual content, not a complete
model of all four axioms. No formal non-derivability, route exhaustion or
independent-wall count follows from this evidence. Resolution labels report
only the actual finite computations.

### N6 — Partial-closure paths and primitive scan

The registry was reread (section 1); no primitive supplies any item and none
is classified as a wall. Convention or reframing paths found:

- adopting the declared class as the candidate law (the historical PR `#7917`'s
  first program choice): a convention adoption; it closes nothing at axiom
  level and is not a derivation;
- the interpretation of "one tick is one edge in form" in the approved
  kinetic-isotropy primitive (named as an owner interpretation boundary by
  the historical PR `#7921`): bears only on item 2's continuous-versus-tick
  clause, not on conservation;
- the historical, unadopted proposal `DYNAMICS_AXIOM_MINIMAL_NONTRIVIALITY_BRANCH_PROPOSAL_2026-06-29`
  (a nonzero local self-adjoint generator): it would supply exactly items 2
  and 6; it has zero premise weight and is an axiom-shaped path, which is
  what the historical PR `#7917`'s second program choice names;
- `docs/repo/DEFERRED_DECISIONS.md` on `origin/main` parks six owner-bar
  decisions; none names a conservative-dynamics principle or a time rule.
  Two are kin to walls here and are recorded as such: the parked
  `M_4(C)` Qubit-domain enlargement would change only the capacity bound of
  section 7 (eight real components per site becomes thirty-two), not any
  verdict; the parked OS-closure residue of the sister lane is kin to the
  reflection-positivity route of N7 and shows that route ends at the same
  owner bar, not at a derivation.

No path closes `W_C` by convention. This note does not say "a new axiom is
required"; it says no axiom sentence reaches the wall and names the live
derivation route (N7).

### N7 — Steelman

Hostile reviewer: "You have shown that no axiom *sentence* names
conservation, but the framework's own program derives its time from
records: the codimension-one evolution construction reads a Euclidean
transfer structure off the record statistics, and once the compiled static
law is reflection positive along a chosen axis, Osterwalder-Schrader
reconstruction gives a positive transfer matrix and a self-adjoint generator
— that is item 6 and the linear continuous first-order clause of item 2 at
once, and the sister lane already records a reflection-positivity closure
for its own action class. Your 'supply in this conditional class' is a failure to run the
reconstruction." The route is concrete and its terminal obligations are
named: (i) a path-product transfer interpretation of the compiled static
law — the light lane's own members declare it supplied ("The factorized
transfer interpretation is an explicit premise", the historical PR `#7886` at its
scope; the block-01 ledger's row 6) — and (ii) an evolution axis, which the
landed single-clock notes carry as a declared premise (B-AXIS, unaudited).
With both supplied, reflection positivity would have to be proved for this
compilation and the reconstruction would deliver a self-adjoint generator on
the reconstructed space, which then has to be shown to be the edge/face
payload of item 1 rather than an enlarged one. That full identification is not established here. The steelman therefore does not defeat the scoped claim
("not reached by an axiom sentence") but it does forbid the broader one
("no route"), which this note does not make. Disposition: the textual and finite conditional claims
stay at their stated scopes with the route recorded as the next derivation target
in the machine-status block.

### N8 — Cross-cycle echo

| similar prior wall | retired? | mechanism since | applies here? |
|---|---|---|---|
| the static law does not select the time rule (historical PR `#7915`, its W1) | no (open) | none | it is this block's `W_T` and `W_C`; the mean sweep selects no stochastic branch; the separately supplied generators remain alternatives |
| allowed class is not a selected law (`DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06`, unaudited) | no | none | the same shape; this block adds that two of the class's items are internally redundant |
| no reversible flow from Record (`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`, unaudited) | no | none | route R1 |
| the evolution axis is declared (single-clock notes, unaudited) | no; reframed from theorem to declared premise on 2026-06-11 | reframing as a declared premise | the same reframing is available for item 2's tick clause and is exactly the interpretation boundary the historical PR `#7921` names; it is not a derivation |
| kinetic-order selector unsupplied (`INDEX_PAIRING_NOT_FORCED_..._2026-06-08`, unaudited) | no | none | different object (spatial order of the matter operator) |
| the sister lane's statistical bridge sealed non-supplied (gravity lane pack, `.claude/science/physics-loops/`) | no; parked at the owner bar | owner decision path | the two supplied structures of N7 are its kin; the same owner path, not a derivation |

No structurally similar wall was retired by a mechanism not considered here.

**Coverage result:** the corrected finite and textual scopes are recorded;
no formal axiom-independence grade or independent-wall count is asserted.
The transfer/reflection-positivity alternative remains open.

## 13. Falsifiers

The bounded theorem fails if any of the following is found:

- a covariant nearest-neighbor edge-to-face coupling on the minimal payload,
  under one of the sixteen signed-permutation laws, that is not one of the
  four listed, or a fifth transformation law of a real one-component payload
  by site permutation in the compilation's sign basis (sign relabellings are
  equivalent laws, excluded by OL, and the runner exhibits one);
- a nearest-neighbor face row with `L d_0 = 0` and `d_2 L = 0` that is not a
  lattice-wide multiple of the oriented curl;
- a proper rotation about a vertex or cube site that changes the sector, or
  an edge-face pair at even physical distance;
- a positive diagonal energy conserved by a member with a nonzero onsite
  scalar or with `w_E r + w_B q != 0`;
- a Gauss-Seidel sweep of the harmonic conditional means that increases the
  energy, or a single-coordinate conditional mean using only radius-one edge inputs;
- a witness law that fails one of the items it is claimed to keep (each is
  checked exactly);
- an axiom sentence, read at its own scope, that names a time parameter, a
  conserved quantity of a field evolution, or an evolving coordinate.

## Imports

Every underivable input, in plain language, with role, provenance and
open-bridge status stated separately.

- The period-two role compilation (parity roles, oriented link value, doubled
  edge/face incidence). Role: the arena of every statement. Provenance:
  declared by the light lane's own construction (the historical PR `#7913`), rebuilt
  here from the parity rule. Open bridge: its compilation into the
  homogeneous physical-site law is named open by that PR at its scope; not
  examined here.
- The named premises LR, IP-A, IP-B, OL, SI (section 1). Role: the hypotheses
  of the conditional verdicts. Provenance: this note's own readings;
  witnesses establish only their explicitly stated finite properties. Open bridge: SI's connection between
  unrecorded components and the Qualification's record configurations is the
  open bridge the historical PR `#7915` lists as its wall W4.
- The finite sizes (sides 4, 6, 8) and the rational witness parameters.
  Role: the executed instances. Provenance: declared here. Open bridge: none;
  the two structural arguments are size-uniform on positive even n >= 4.
- Computational tools: integer and rational arithmetic, `sympy` for the
  symbolic identities. Role: exact evidence. Provenance: standard software;
  no physics content.
- No comparator is used: continuum Maxwell theory, the leapfrog literature,
  and the sampler literature enter nowhere as inputs; the finite tick and
  the deterministic conditional-mean relaxation are re-derived constructions used as witnesses.
- The members (`#7913`, `#7915`, `#7917`, `#7920`, `#7921`, `#7886`) are
  evidence addresses quoted at scope, not imports and not dependencies.

## Historical review record (original 2026-09-05 source only)

Worker provenance: drafted by a Fable primary seat under the block-02
contract of the campaign pack (`GOAL_block02.md`), with the value gate V1-V5
answered in the pack's `REVIEW_HISTORY.md` before any PR. Independence
class: single family (Claude), cross-model — a Fable primary; an Opus 5
refuting checker on disjoint machinery (its own `d_0` sign convention,
Levi-Civita curl signs, exact Fourier block-diagonalization for the
multiplicities, brute-force enumeration of the signed-permutation laws with
no character theory assumed, the gauge-plus-chain nullspace in full
generality on sides 4 and 6, all ten witnesses re-verified: eighty
independent checks, verdict FIX FIRST with no verdict refuted, findings
CK-01..CK-08 all applied in the fix pass recorded in the pack's
`REVIEW_HISTORY.md`); and the supervisor's line-by-line review with hand
verification of the one-face stencil map, the blockwise conservation
equations, the leapfrog invariant and its positivity bound, the side-6
multiplicities from the coarse momentum census, and the cube-connectivity
argument. Independent-math checks per
conformance section 6: the one-face stencil (hand computation, section 3),
the blockwise metric-skew equations (symbolic, section 5), the
cube-connectivity argument (hand, section 4), the finite-tick modified
energy (hand derivation of the kick-drift-kick invariant, section 6), and
the exact multiplicity counts (predicted from the momentum census, section
5). Mutation checks on scratch copies, one per check family, all detected by
the checks they target: axiom sentence altered; one curl sign flipped;
face-character factor dropped; metric-skew defect zeroed; Gauss-Seidel sign
flipped; modified-energy coefficient altered; quartic energy term dropped;
chain constraint disabled; a multiplicity altered; the stabilizer face sign
fixed; the support-radius test disabled; the covariance test disabled. The
checker's three planted defects were caught as well: a `z`-only face-stencil
sign flip (thirty failures, first at the chain identities); translation
covariance made vacuous (caught by the site-privileging witness alone); the
modified-energy coefficient changed to `h^2/6` (caught by the tick check).
Nothing landed is replaced or narrowed (this is a new note). Hard landing
conditions: none; no helper runner; the citation-graph manifest co-lands
for the one added node.

## Verification

Run:

```text
python3 scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py
```

Expected final line:

```text
TOTAL: PASS=110 FAIL=0
```

The runner declares `AUDIT_TIMEOUT_SEC = 900`. Runtime reads only the
axiom memo. `AUDIT_INPUT_PATHS` additionally pins this canonical note for
claim scope. No repository helper is imported.
The displayed counts describe the corrected finite receipt; the historical
review record above describes the original source only.
