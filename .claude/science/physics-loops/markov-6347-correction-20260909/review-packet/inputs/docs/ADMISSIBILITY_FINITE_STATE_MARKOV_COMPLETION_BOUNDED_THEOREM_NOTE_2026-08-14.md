---
claim_id: admissibility_finite_state_markov_completion_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "For the displayed Block84 linear-response Record law, every finite configuration of M_2(C) Records has a finite eligible frontier of size at most six times the old domain, and one normalized finite-atomic transition kernel that copies all old contents and independently appends supported spectral projectors at the synchronous prestate frontier. The kernel is Borel on the standard-Borel space of finite Record maps, is time-homogeneous in its iteration ordinal, is translation/proper-cubic covariant, has finite propagation speed at most one lattice edge per tick, and recursively defines normalized finite-time histories from every finite initial state. Every nonempty finite full-Z3 state has an explicit extreme-site growth witness and therefore cannot halt under this candidate. The inherited twelve-site two-cube halt is a supplied boundary restriction: the same full Record set embedded in Z3 has 32 eligible outside sites, while the origin process continues with a 102-site fifth shell. The synchronous scheduler is supplied and load-bearing; dynamic within-tick recomputation exposes five extra candidates after one seed-frontier write. This closes a mathematical arbitrary-finite-state Markov/process interface for one candidate, not selection or adoption of the law, an arbitrary-infinite-state process, a physical clock/rate, source/energy typing, gravity, audit retention, obligation retirement, or TOE percentage movement."
upstream_dependencies:
  - minimal_axioms
  - admissibility_taxicab_shell_record_instrument_cylinder_law_bounded_theorem_note_2026-08-14
runner: scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py
---

# Finite-State Markov Completion Of The Record-Only Admissibility Member

**Date:** 2026-08-14

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign retention.

**Primary runner:**
[`scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py`](../scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py)

**Scientific parents:**

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md`](ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md)

## Result up front

The Block84 seed cylinder extends to a mathematically complete one-step kernel
and finite-time history law from **every finite Record configuration**.

Let `R` be a finite partial map from `Z^3` to `M_2(C)` and let

```text
o_R(x) = 1 if x is in dom(R), and 0 otherwise,
d_a(x) = o_R(x+e_a) - o_R(x-e_a).
```

For every unread site with `d(x) != 0`, retain the Block84 projectors and
linear weights

```text
P_s(d) = [I + s d.sigma/sqrt(k)]/2,
p_s(d) = [1 + s sqrt(k)/3]/2,
k = |d|^2 in {1,2,3},       s in {+1,-1}.
```

Let `F(R)` be the set of those sites. One synchronous transition reads the
same prestate `R`, independently draws one sign at every site in `F(R)`,
copies all old Records, and appends `P_s(d)` at the new sites. For a sign map
`s:F(R)->{+1,-1}`, its atom has mass

```text
K(R,{R_s}) = product_(x in F(R)) p_(s(x))(d_R(x)).
```

The new results are:

1. `F(R)` is finite, disjoint from `dom(R)`, and
   `|F(R)| <= 6 |dom(R)|` for every finite input.
2. The transition has exactly `2^|F(R)|` distinct atoms and total mass one.
3. Old contents are copied by identity. Formation geometry and probabilities
   depend on Record presence, not old Record content.
4. The complete kernel is translation and proper-cubic covariant. Block84's
   exact 26-direction projector certificate supplies the internal matrix
   transport; this note proves the arbitrary-domain condition transport.
5. The space of all finite `M_2(C)`-valued Record maps is standard-Borel,
   though not countable. The generated `I/2` plus 26-projector subspace is
   countable. The finite-atomic kernel is Borel on the full space and its
   normalized cylinders define a Markov history from every finite initial
   state.
6. Propagation is at most one lattice edge per iteration. The origin seed
   attains that bound and continues to produce the exact taxicab balls.
7. Every nonempty finite full-lattice state has a new site. Hence this
   candidate has no nonempty finite halt on `Z^3`.
8. The two-cube waves `3,4,3,1,0` halt only because formation is restricted
   to twelve supplied sites. Embed the filled patch in the full lattice and
   it has 32 eligible outside sites. The origin law's fifth shell has 102.
9. Frozen-prestate writes commute, but dynamic recomputation is inequivalent:
   after one of the six seed-frontier writes, five additional distance-two
   sites become eligible in the same putative tick.

This is significant global-process progress for the cleaner Record-only
route. It is still a displayed member, not an adopted law. The current axioms
do not select its occupancy difference, factor `1/3`, spatial-to-Pauli action,
spectral support, linear response, synchronous scheduler, conditional
independence, or initial state. Its iteration ordinal is not physical time.
No source is typed as energy-momentum and no gravity identity is proved.

There is zero TOE percentage movement, and the retained-positive end-to-end
theory count remains zero.

## 1. Exact arbitrary-state transition

### 1.1 Finite frontier

Every site in `F(R)` must be a nearest neighbor of at least one site in
`dom(R)`: if all six neighbors were absent, all three components of `d` would
vanish. A finite domain of size `N` has at most `6N` nearest-neighbor
candidates. Removing old sites and cancellation cases can only reduce that
set. Therefore

```text
F(R) intersect dom(R) = empty,
|F(R)| <= 6 |dom(R)| < infinity.
```

The runner exhausts all 128 subsets of a seven-site asymmetric test host and
checks the bound plus an actual adjacent old site for every candidate. The
displayed proof is general; the enumeration is an adversarial implementation
check, not the proof's domain restriction.

### 1.2 Local atoms and normalization

For every nonzero `d in {-1,0,1}^3`, `k` is `1`, `2`, or `3`, so both
Block84 weights are strictly positive and

```text
p_+(d) + p_-(d) = 1.
```

Different sign assignments give different Record maps because `P_+(d)` and
`P_-(d)` are distinct at every new site. Hence there are `2^|F(R)|` atoms.
Their mass sums by finite distributivity:

```text
sum_(s:F->{+,-}) product_(x in F) p_(s(x))(d(x))
  = product_(x in F) [p_+(d(x))+p_-(d(x))]
  = 1.
```

The empty product is one, so a state with empty frontier has the identity
transition. The runner checks all 26 local direction types, 32 arbitrary
finite domains, and explicitly sums the origin seed's 64 atoms. A probability
mutation of `+1/100` fails this gate.

### 1.3 Complete Record update

For one branch `s`, define

```text
R_s(x) = R(x)                  for x in dom(R),
         P_(s(x))(d_R(x))      for x in F(R).
```

No other site is in the new partial map. Old contents are neither read by the
formation predicate nor rewritten. The runner tests 31 nonempty domains with
two different exact old-content tables. Their frontiers, local directions,
and branch weights agree; every old matrix is unchanged and every new matrix
is its supported projector. Content feedback and overwrite mutations fail.

Content blindness is a property of this candidate, not a consequence of the
Record axiom and not a claim that realistic matter must ignore Record content.

## 2. State-space and Markov theorem

### 2.1 Correct state-space type

The full finite-Record space is **not countable**. For each finite lattice
domain `D`, its content space is a finite Cartesian power of `M_2(C)`, a
finite-dimensional real vector space with its Borel sigma-algebra. There are
countably many finite subsets of `Z^3`. Thus the disjoint union

```text
S_fin = union_(D finite subset Z^3) {D} x M_2(C)^D
```

is a standard-Borel space. It is generally uncountable because even one
Record may carry continuously varying content.

The particular process generated from the central `I/2` seed uses only 26
distinct spectral projectors plus `I/2`. Its finite-map reachable subspace is
countable. The runner verifies those alphabet counts but does not replace the
full state domain by the smaller generated orbit.

### 2.2 Borel kernel

On each domain stratum, `F(R)`, every `d_R(x)`, and every atom weight depend
only on the discrete domain `D`. An atom copies the old continuous content by
the identity map and appends finitely many fixed matrices. It is therefore a
Borel map on that stratum. The countable disjoint union over finite domains is
Borel, so `K` is a finite-atomic Markov kernel on `S_fin`.

The same formula is used at every iteration. It has no tick index and is
time-homogeneous in the mathematical iteration ordinal.

### 2.3 Finite histories

For an initial probability measure `mu_0` on `S_fin`, recursively define the
finite-time cylinders

```text
mu_(0:T)(dR_0 ... dR_T)
  = mu_0(dR_0) K(R_0,dR_1) ... K(R_(T-1),dR_T).
```

Normalization of `K` makes these cylinders normalized and projectively
consistent. The standard Ionescu--Tulcea construction on standard-Borel
spaces therefore gives a path measure. For a point initial state the formula
is simply repeated finite summation. The runner checks the two-step total
mass and a positive four-tick cylinder explicitly.

This is a mathematical Markov history, not physical outcome actualization,
seconds, a Lorentzian causal order, or a laboratory repeated-preparation law.
Physical time remains open.

## 3. Covariance on arbitrary finite states

For a translation `a`, let `(aR)(a+x)=R(x)`. Directly,

```text
d_(aR)(a+x)=d_R(x),
F(aR)=a+F(R).
```

For a proper signed-permutation rotation `G`, let old contents transform by
the supplied Block84 lift `U_G`. Then

```text
d_(GR)(Gx)=G d_R(x),
k(Gd)=k(d),
F(GR)=G F(R),
U_G P_s(d) U_G^dagger=P_s(Gd).
```

The radial weights depend only on `k`, so branch masses are invariant when
the complete input and output maps are transported. This proves

```text
K(GR, G A) = K(R,A)
```

for every Borel set `A`, and likewise for translations: at fixed `R`, either
side reduces to the same finite sum over transported support atoms. The
runner checks 32 domains under all 24 rotations and two translations. Exact
projector covariance over all 26 directions is inherited only through the
byte-bound Block84 runner/cache receipt; it is not silently reproved or
enlarged.

Covariance verifies the supplied spatial-to-Pauli action. It does not derive
or select that action from Lattice plus Qubit.

## 4. Propagation and global non-halting

### 4.1 Finite causal cone

Every new site is adjacent to the old domain. Inductively, after `t` updates,
every Record lies within lattice `ell^1` distance at most `t` of the initial
domain. Also

```text
|dom(R_(t+1))| <= 7 |dom(R_t)|,
```

so every finite-time state remains finite. The origin seed realizes the exact
balls `B_t`, hence reaches distance exactly `t`.

This is finite propagation in lattice-edges per iteration. Calling it speed
`c`, a time metric, or Lorentzian causality would require a physical duration
per iteration and a causal interpretation not supplied here.

### 4.2 Every nonempty finite state grows

Let `D=dom(R)` be finite and nonempty. Choose `y in D` with maximal first
coordinate and set `x=y+e_1`. Then `x` and `x+e_1` are outside `D`, while
`x-e_1=y` is inside. Consequently

```text
d_1(x)=o(x+e_1)-o(x-e_1)=0-1=-1,
```

so `x in F(R)`. Therefore

```text
D nonempty and finite  =>  F(R) nonempty.
```

The empty state is fixed, but no nonempty finite full-`Z^3` state halts under
this displayed law. This is a theorem about the exact occupancy-difference
candidate. It is not a universal no-go for other formation laws, bounded
domains, resource exhaustion, or infinite configurations.

The runner checks the extreme-site witness on all 127 nonempty subsets of its
seven-site hostile host and iterates three asymmetric states for five steps.

## 5. Scheduler and finite-boundary falsifiers

### 5.1 The synchronous scheduler is supplied

The transition reads one frozen prestate and writes distinct unread sites.
Once the branch signs are fixed, those append operations commute: their order
does not change the output because no write is re-read during the tick.

Dynamic recomputation is a different law. From the origin seed the frozen
frontier has six sites. Append the lexicographically first one and recompute;
five new distance-two sites become eligible beyond the original frontier.
Thus a cascading in-place scheduler is not equivalent to the synchronous
kernel. The synchronous scheduler is supplied and load-bearing.

This exact witness prevents “all local writes are disjoint” from being used to
infer schedule independence. Disjoint targets close fixed-prestate assembly,
not equality with a law that changes its read state inside the tick.

### 5.2 The two-cube halt is not a full-lattice horizon

Block84's restricted twelve-site fixture fills in waves

```text
3, 4, 3, 1, 0.
```

That restricted map then halts because sites outside the supplied patch are
not candidates. Put the same twelve occupied sites back into `Z^3` and the
full formula finds 32 eligible outside sites. Separately, the unrestricted
origin process has fifth-shell size

```text
4(5)^2+2 = 102.
```

Therefore the two-cube halt is a supplied boundary restriction. It is not a
full-lattice event horizon, late-time fixed point, resource exhaustion result,
or physical causal boundary. This does not invalidate the finite fixture; it
fixes its interpretation.

## 6. Axiom, resource, source, and gravity decision

The current four axioms permit a downstream rule of this type but do not
select it. The exact debits remain:

| item | status after this theorem |
|---|---|
| finite Record-map state domain | current Record ontology; exact kernel supplied here |
| neighbor difference `d` and formation predicate `d!=0` | candidate law, not axiom-derived |
| spatial-to-Pauli action | supplied; covariance verified, selection open |
| spectral support and linear weights | supplied; the Block84 cubic twin remains |
| synchronous prestate scheduler | supplied and proven load-bearing |
| conditional independence | supplied; correlated kernels with the same marginals remain possible |
| outcome actualization | represented by kernel atoms; physical draw mechanism not derived |
| seed or initial distribution | arbitrary finite input allowed mathematically; physical initial law open |
| blank capacity | the infinite lattice supplies unrecorded sites; physical resource interpretation open |
| physical time/rate | not supplied; iteration ordinal only |
| source/energy dictionary | not supplied; Record count is not promoted to energy |
| gravity | no stress tensor, normalization, Ward identity, connection, or metric response |

In particular, linear response is not selected, and physical time remains open.

The shortest retained-positive route is now sharper:

1. independently retain this arbitrary-finite-state kernel theorem;
2. derive the full local law from a microscopic channel, or obtain owner
   approval for a narrowly scoped downstream primitive registering the
   **complete** Block84 transition—condition, action, support, weights,
   scheduler, and product kernel;
3. keep the physical initial condition, time/rate, source, and gravity outside
   that primitive unless separately justified;
4. only then type a source and execute the nonlinear Ward/connection test.

Registering only the twelve-site fixture or only `p_+(k)` would be
insufficient. Editing Record is unnecessary for this Record-only route; the
law belongs downstream of Admissibility unless the owner explicitly chooses a
constitutional placement. No axiom or primitive is adopted here.

## 7. Gravity and TOE map

This theorem closes mathematical global-process and fixed-prestate overlap
for one candidate on every finite state. It does not close physical time or
gravity. Finite-patch clock/source identities of this kind remain iteration
counts, inclusion-exclusion, or inversion of supplied incidence data; none
types energy-momentum or supplies a Ward identity. Those portfolio results
were inspected for route ranking but are not dependencies or inputs here.

The strict TOE map is unchanged:

| TOE lane | repository map | physical bridge | autonomous law | current ceiling |
|---|---:|---:|---:|---:|
| operational / Records | 95% | 92% | 50% | 99% |
| causal / time | 76% | 72% | 41% | 99% |
| inertia / matter | 95% | 96% | 75% | 99% |
| gravity / source / resources | 70% | 45% | 29% | 94% |
| Born / history | 84% | 63% | 34% | 99% |

This is route-confidence and candidate-completion progress. There is zero TOE
percentage movement until adoption and independent retention retire named
obligations.

## 8. Exact falsifiers

The bounded theorem fails if any of the following occurs:

- a finite input has an infinite frontier or violates `|F(R)|<=6|R|`;
- a nonzero direction lacks two positive normalized weights;
- a transition's atoms fail to total one;
- old Record content affects this candidate's frontier or branch weights;
- an update overwrites an old Record or appends unsupported content;
- a translation or proper cubic rotation fails to transport the complete
  arbitrary-domain kernel;
- a nonempty finite full-lattice state lacks the extreme-site growth witness;
- a new site propagates more than one lattice edge per iteration;
- dynamic recomputation is promoted as equivalent to the frozen scheduler;
- the filled two-cube patch is promoted as a full-lattice halt;
- the full finite-Record space is called countable rather than
  standard-Borel; or
- the candidate is promoted to adopted law, physical time, energy source,
  gravity, retention, or TOE score movement.

The runner includes independent mutations for stale authority, a spurious
infinite frontier, broken normalization, content feedback, overwrite,
noncovariance, a false finite halt, dynamic scheduling, erased outside
frontier, time dependence, and law overclaim. Each mutation must fail exactly
its named gate.

## 9. No-Go Discipline gate

The only negative claims shipped are scoped to the displayed law:

1. no nonempty **finite** state halts on the full lattice under this exact
   neighbor-difference formation rule;
2. the inherited two-cube halt is not a full-`Z^3` horizon; and
3. current authority does not select or adopt the displayed kernel.

None says that finite halts, bounded universes, other laws, infinite-state
stationarity, physical time, or gravity are impossible.

### N1 — Alternative-route enumeration and normalization

The three negative targets are deliberately narrow:

```text
C1: under this exact synchronous occupancy-difference law, no nonempty finite
    full-Z3 Record domain halts;
C2: the displayed twelve-site halt is not a halt of that same state embedded
    under the full-Z3 rule;
C3: the current axiom plus approved-primitive surface does not select or adopt
    the displayed response and product scheduler.
```

The approach families below are normalized by primary object, load-bearing
mechanism, and terminal obligation. Every row was attempted in this cycle and
cites the current primary runner; no row is presented as ruled out by an
unaudited prior source.

| id / target | normalized family | attack attempted | why the attack does not overturn the target; exact current-cycle evidence | honesty / disposition |
|---|---|---|---|---|
| R1 / C1 | algebraic finite-domain extremum / maximal first coordinate / produce `F(D)=empty` | seek a nonempty finite domain whose neighbor differences all cancel | `growth_certificate()` constructs `x=y+e1` with `d1(x)=-1` for arbitrary finite nonempty `D`; Gate F checks the proof implementation | **ATTEMPTED — CLOSED** |
| R2 / C1 | hostile finite counterexample scan / asymmetric occupancy cancellation / exhibit one finite halt | exhaust all 127 nonempty subsets of the seven-site asymmetric host | every tested domain retains the extreme-site witness; this is an adversarial implementation check subordinate to R1, not the universal proof (`growth_certificate()`, Gate F) | **ATTEMPTED — CLOSED** |
| R3 / C2 | boundary/initial-domain comparison / embed the filled finite carrier / preserve its halt on `Z^3` | reuse the halted twelve-site state without changing its Record contents | the unrestricted formula exposes 32 outside sites (`patch_boundary_certificate()`, Gate H), so the restricted stop does not survive the embedding | **ATTEMPTED — CLOSED** |
| R4 / C2 | increasing-region lattice limit / taxicab-shell invariant / obtain late finite saturation | continue the unrestricted origin process beyond the patch's fourth wave | the fifth shell has 102 sites and the exact-ball checks continue through radius six; R1 separately excludes every later finite nonempty halt (`growth_certificate()` and `patch_boundary_certificate()`, Gates F/H) | **ATTEMPTED — CLOSED** |
| R5 / C1-C2 | dynamical scheduler / within-tick recomputation / recover the same transition with a different update order | append one seed-frontier site and immediately recompute eligibility | five new distance-two candidates appear; the route changes the law rather than refuting C1 or C2 (`scheduler_certificate()`, Gate G) | **ATTEMPTED — CLOSED** |
| R6 / C3 | symmetry/representation selector / radial response covariance / force the linear weights | impose the same normalization, support, and proper-cubic covariance on linear and cubic responses | both response pairs are positive and normalized in all three `k` sectors but differ in all three; covariance therefore does not select linear response (`selection_countermodel_certificate()`, Gate C) | **ATTEMPTED — CLOSED** |
| R7 / C3 | alternate global correlation / equal one-site marginals / force the product kernel | compare independent signs with one common sign on the same `k=2` sector | both laws normalize and have the same one-site mean, while their history variances differ; the marginal law does not select independence (`selection_countermodel_certificate()`, Gate C) | **ATTEMPTED — CLOSED** |
| R8 / C3 | dependency/registry reclassification / live premise lookup / find the complete law already supplied | inspect current `minimal_axioms` and every current approved-primitive source through the live four-node registry | the registry contains only minimal axioms, scale reference, kinetic isotropy, and realized-state reference; their source guards supply no Record-law response or scheduler (`authority_certificate()`, Gate A; [`axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json)) | **ATTEMPTED — CLOSED** |

R2 is retained as a numerical/falsifier family rather than counted as a second
proof of R1. Even if R2 were removed as proof-family duplication, R1 and
R3--R8 leave seven materially distinct families. Modified formation laws,
finite resources, arbitrary infinite starts, microscopic channel derivations,
and owner-approved registration remain live positive routes in N6/N7; they are
not counted as failed attacks on these candidate-specific targets.

### N2 — Wall-independence audit

Let

```text
W1 = exact response/support/formation-law selection
W2 = spatial-to-M2 action and soldering selection
W3 = synchronous product scheduler plus physical actualization
W4 = initial-state, resource, and arbitrary-infinite-domain law
W5 = physical duration, rate, causal metric, and Lorentzian interpretation
W6 = source/energy/stress typing and normalization
W7 = gravity action, nonlinear Ward identity, and connection response
```

| pair | left closes right? | right closes left? | independent? | exact directional reason |
|---|---|---|---|---|
| W1/W2 | no | no | yes | W1 radial weights do not select W2 internal action; W2 action permits many W1 supports and responses |
| W1/W3 | no | no | yes | W1 one-site probabilities do not choose W3 synchronous independence/actualization; W3 scheduler hosts many W1 local laws |
| W1/W4 | no | no | yes | W1 transition formula chooses no W4 universe initial state/resource; W4 initial data do not select W1 weights |
| W1/W5 | no | no | yes | W1 discrete probabilities have no W5 duration; a W5 clock metric does not choose the W1 local kernel |
| W1/W6 | no | no | yes | W1 event odds do not type W6 energy; a W6 stress dictionary does not select W1 formation probabilities |
| W1/W7 | no | no | yes | a W1 Record law supplies no W7 gravity action; W7 gravity can couple to another W1 matter law |
| W2/W3 | no | no | yes | W2 covariance action does not choose W3 update ordering; W3 scheduler can run with trivial or faithful W2 action |
| W2/W4 | no | no | yes | W2 Pauli frame creates no W4 seed/capacity; W4 initial conditions do not choose a W2 representation |
| W2/W5 | no | no | yes | W2 internal transport supplies no W5 duration/causal cone; W5 time data do not select W2 soldering |
| W2/W6 | no | no | yes | W2 action on contents is not a W6 energy map; W6 scalar occupancy sources can ignore W2 content action |
| W2/W7 | no | no | yes | W2 internal action does not establish W7 Ward/connection equations; W7 gravity does not uniquely fix W2 here |
| W3/W4 | no | no | yes | W3 synchronous product updates do not generate W4 initial data; a W4 seed does not choose W3 independence/actuality |
| W3/W5 | no | no | yes | a W3 iteration order is not a W5 physical rate; a W5 time metric does not choose W3 product correlations |
| W3/W6 | no | no | yes | W3 actual formation does not assign W6 energy; a W6 source map does not determine W3 event concurrency |
| W3/W7 | no | no | yes | a W3 scheduler supplies no W7 gravity action; a W7 connection law does not actualize W3 Record draws |
| W4/W5 | no | no | yes | W4 initial/resource data do not define W5 duration; a W5 clock does not select a W4 seed/infinite-state measure |
| W4/W6 | no | no | yes | W4 Record capacity is not W6 stress normalization; a W6 source does not generate the W4 initial state |
| W4/W7 | no | no | yes | a W4 boundary condition does not prove W7 gravity dynamics; W7 gravity does not choose this W4 finite-state domain |
| W5/W6 | no | no | yes | W5 rate/cadence does not determine W6 energy per event; a W6 stress value does not supply a W5 time metric |
| W5/W7 | no | no | yes | a W5 clock alone gives no W7 nonlinear Ward identity; W7 gravity still needs W5 physical-time interpretation |
| W6/W7 | no | no | yes | a W6 typed source need not obey the W7 connection identity; a W7 vacuum action does not type this W6 source |

The collapsed wall set is exactly `{W1,W2,W3,W4,W5,W6,W7}`: no directional
implication removes a member. No wall is hidden inside mathematical Markov
closure. This theorem supplies a candidate part of W3 for frozen finite-state
histories, while leaving physical actuality and every selection in W1--W7
open.

### N3 — Hidden-wall scan

The complete source note, including this checklist, was scanned for the
current trigger list. The classifications below cover every hit family; the
final hash-bound review re-runs the scan after line numbers settle.

| trigger hit family | classification | exact disposition |
|---|---|---|
| `axiom`, `primitive`, `registered` | cited accepted authority or explicit owner-governance route | the only accepted occurrences point to [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), [`axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json), or their three current source notes; the proposed Record-law primitive remains W1/W3 and is not used |
| `boundary`, `initial condition`, `background` | explicit W4 condition, never hidden | finite patch restriction, seed/initial data, resources, and an infinite stationary background are named alternatives; none enters the finite-state proof silently |
| `normalization` | either proved kernel property or explicit W6 residual | local/transition normalization is proved in Gates C/I; source/stress normalization remains W6 |
| `sector` | genuine non-load-bearing mathematical context | `k=1,2,3` labels radial response classes used in Gate C; no physical matter-sector identification follows |
| `convention` | N6 governance scan, non-load-bearing | no relabeling convention is used to select weights, correlations, time, source, or gravity |
| `wall`, `admission`, `obstruction` | checklist vocabulary naming the explicit collapsed W1--W7 set | these words introduce no extra premise; every scientific residual is already in N2 |
| `canonical` | quoted filename/title or law-completeness echo, non-load-bearing | the historical completeness-contract and schedule-probe names are N8 search hits only and carry no authority here |
| `by construction`, `as is standard`, `bridge context`, `naturally`, `obviously`, `standard QFT`, `we assume`, `the framework provides`, `ansatz` | no load-bearing occurrence | none is used as a proof step or premise phrase |

The semantic terms are also pinned: the full finite-content state space is
uncountable standard-Borel; `independent` means the supplied product kernel;
`synchronous` means one frozen prestate; `speed` means lattice edges per
iteration; and `complete` means the finite-state mathematical kernel for one
displayed member. None of those terms imports physical actuality, time,
energy, or gravity.

### N4 — Residual matching

First, the scientific dependency residuals are matched exactly:

| cited source and exact locator | source residual/result | residual used here | exact match? | use |
|---|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md:57-73,77-83,92,114-130,173-190`](MINIMAL_AXIOMS_2026-06-29.md) | nearest-neighbor distribution and Record formation/permanence, while exact law values, scheduler, time, source, and gravity stay outside | accepted ontology plus C3 current-authority boundary | yes | live `origin/main` bytes checked in Gate A |
| [`axiom_premise_nodes.json:1-48`](audit/data/axiom_premise_nodes.json) and the three `current_path` sources | exactly four premise nodes; none supplies a Record response/product scheduler | C3 present nonselection/nonadoption | yes | registry and all three sources checked in Gate A |
| [`ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md:155-340`](ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md) | one displayed finite-map local law, seed cylinders, covariance, and permanence | candidate formula and internal projector transport | yes at parent scope | byte-bound parent note/runner/cache; arbitrary-state theorem is new here |
| [parent note `:342-391`](ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md) | restricted two-cube waves and frequency controls | finite fixture only | yes for fixture; no for full-lattice horizon | patch waves recomputed; parent not cited for C2 conclusion |
| primary runner `finite_state_certificate()` through `history_certificate()` | finite-domain typing, kernel, covariance, growth, scheduler, patch embedding, and history | C1/C2 plus positive finite-state theorem | yes | executed directly; exact function locators replace approximate line ranges |

Second, every prior wall/campaign mentioned later as an echo is checked before
it can be used as a witness:

| prior citation and exact locator | prior residual attacked | present residual | match? | witness use here |
|---|---|---|---|---|
| [`CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md:31-50,195-215`](work_history/repo/review_feedback/CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md) | fields required for a complete predictive law | finite STATE/ATOMIC_LAW/CONTINUATION versus still-open actuality/time | partial, not exact | dropped as proof; N8 checklist echo only |
| [`COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md:81-170`](work_history/repo/review_feedback/COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md) | inequivalent complete sampled laws under a shared constitutional surface | C3 response/correlation nonselection | same residual shape, different concrete laws | not proof; current Gate C supplies its own twins |
| [`CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md:14-48,226-294`](work_history/repo/review_feedback/CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md) | sequential schedule equivalence versus an exact atomic/predecessor rule | frozen append versus dynamic recomputation | yes | conceptual witness only; current Gate G executes the exact present law |
| [`POST_RECORD_TWO_STATE_MARKOV_STABILITY_INTERFACE_2026-06-06.md:15-45,70-90`](POST_RECORD_TWO_STATE_MARKOV_STABILITY_INTERFACE_2026-06-06.md) | conditional stability for a supplied two-state kernel | Borel history for this supplied finite-state kernel | partial, different state/kernel | dropped as proof; terminology boundary only |
| [`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md:298-356`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md) | global measure/menu/effect interface remains underdetermined | C3 exact finite PVM response/product selection | related but not exact | dropped as proof; N8 route comparison only |
| [`KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md:15-37,67-112`](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md) | an unfixed graining ratio was owner-registered as a narrow primitive | possible owner registration of the complete Record law | governance analogy, not scientific residual match | never used as proof; N6/N8 governance mechanism only |

After dropping every nonexact prior witness, C1--C3 still depend on zero prior
campaigns: their evidence is the current primary runner plus the accepted
premise bytes. No parent or historical note is credited with the new
arbitrary-state theorem.

### N5 — Rhetoric and granularity audit

The substantive negative phrases reduce to C1--C3 plus one present-authority
boundary C4: “the iteration ordinal is not a supplied physical clock.” The
resolution matrix records both executed and deliberately unasserted scopes.

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| C1: no nonempty finite halt under this exact law | checked: the extreme candidate has exact `d1=-1` | checked on 127 nonempty hostile domains | checked for empty/nonempty, seed, and asymmetric multi-seed modes | checked by Gate F with five-step propagation and six exact seed balls | proved for every nonempty finite `D subset Z^3`; infinite `D` and other laws are not asserted |
| C2: the two-cube stop is not a full-lattice halt of the embedded state | not a one-element claim; no per-element generalization asserted | checked: all outside candidates are enumerated and total 32 | checked by restricted-patch versus full-lattice embedding, plus unrestricted seed mode | checked by Gate H on waves `3,4,3,1,0` and shell five `102` | checked only for this exact embedded patch; no theorem about every finite boundary is asserted |
| C3: present authority does not select/adopt this law | checked: linear/cubic weights both normalize for each `k`, and product/common-sign laws share one-site means | checked over all 26 local directions where response applies | checked for linear/cubic response and product/correlated history modes | checked against live minimal-axiom and four-node premise-registry bytes in Gates A/C | present-authority claim only; future microscopic derivation or owner approval is not ruled out |
| C4: iteration is not supplied physical time | not executed: a local probability has no duration observable in this model | not executed: sites carry no clock/rate field | checked only as a time-homogeneous mathematical iteration mode | current axiom/registry scope checked; no physical duration source found or imported | checked and not executed — no physical-clock, Lorentzian, or empirical-rate theorem is claimed |

Other negative wording is narrower: content blindness is a property of this
candidate, covariance verifies but does not select the supplied action, and no
occupancy count is promoted to energy. Those clauses inherit C3/C4's
present-authority scope; none is a universal impossibility claim.

The cached primary-runner output lands the required execution certificate with
one substantive line for each canonical resolution class:

```text
per_element: checked all 26 nonzero neighbour directions, both spectral outcomes, linear/cubic normalized response pairs, the 27-symbol generated alphabet, projector transport, and exact append contents
per_site: checked 128 finite domains, six-neighbour frontier bounds, 127 extreme-site growth witnesses, old Record contents, two translations, and 24 proper-cubic rotations
per_mode: checked empty, nonempty, single-seed, asymmetric multi-seed, linear/cubic response, product/common-sign correlation, frozen synchronous, dynamic recomputation, finite-patch, and full-lattice modes
per_block: checked live axiom and four-node primitive registry, exact Block84 receipt, arbitrary-state transition normalization, permanence, standard-Borel Markov cylinders, scheduler dependence, and the two-cube boundary artifact
lattice_wide: checked the exact local formula and finite-state full-Z3 transition for every finite input type, plus general proofs encoded in the note; checked and not executed — no arbitrary infinite initial configuration, physical clock, typed energy/source, Ward identity, or gravity coupling is claimed
```

“Every finite input type” refers to the proved structural formula, not brute
enumeration of infinitely many finite domains. The runner's finite hostile
sets test the implementation; the adjacent-candidate and extreme-site proofs
carry the universal finite-domain claims.

### N6 — Partial-closure path scan

The required registry check read
[`axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json) and each
listed `current_path`, not a prose summary. The result is:

| accepted/proposed path | current status | exact scope relevant here | what it closes |
|---|---|---|---|
| `scale_reference_primitive` | accepted premise | units conversion only | none of C1--C3 or W1--W7 |
| `kinetic_isotropy_primitive` | accepted premise | structural `c_t=c_s`; no dynamics/selector | no Record response, scheduler, or physical duration |
| `realized_state_primitive` | accepted premise | pointwise realized-state slot; no measure/weighting/state choice | no branch probabilities, correlations, or initial state |
| complete Record-law primitive | proposed only, absent from registry | would have to state formation condition, action, support/weights, synchronous scheduler, and joint kernel together | could close governance selection parts of W1--W3 only after explicit owner approval and reviewed policy/registry update |
| microscopic local CP/resource derivation | open scientific route | derive the same complete law while excluding cubic/correlated twins | could retire rather than register W1--W3 imports |
| convention/relabeling | scanned; no applicable closure | coordinate names, outcome labels, or definition changes do not determine probabilities/correlations | none; this is physics content, not a labeling residual |

Open PRs and prior meta-notes were also scanned for an in-flight
convention-only ratification. None supplies this complete law. Block85's
axis-slot condition is a candidate-specific sufficient selector inside a
fixed response class, not an accepted premise and not a microscopic
derivation.

| mechanism | positive closure | why it does not finish TOE | next use |
|---|---|---|---|
| Block84 origin cylinder | exact seed shells, Record contents, product branches | one initial state; law unselected | parent formula and special-case control |
| this arbitrary-finite-state kernel | normalized covariant Markov histories, permanence, finite propagation | finite states only; scheduler/response/action supplied; no physical time/source | prerequisite for complete-law registration or microscopic derivation |
| Block84 cubic twin | complete alternative response on the same process | proves nonselection rather than physical choice | hostile selector control |
| correlated kernel | same one-site marginals with different histories | independence unselected | future fluctuation/actuality discriminator |
| bounded two-cube halt | exact finite saturation | supplied boundary, not global horizon | boundary-condition control only |
| extreme-site witness | exact non-halting for finite nonempty full-lattice states | candidate-specific; says nothing about infinite states/other laws | prevents false horizon claims |
| approved complete-law primitive | could convert supplied law into accepted premise | owner decision and audit absent | highest retained-impact next step after this theorem |
| microscopic CP/resource derivation | could retire rather than register imports | not constructed | strongest scientific steelman |

### N7 — Steelman and strongest surviving escape route

Hostile steelman: this cycle may have completed the wrong mathematical object.
A concrete local CPTP/resource mechanism could read live `M_2(C)` neighbor
content, conserve a finite blank/resource carrier, and induce an effective
Record instrument whose reduced branches equal the linear law while its
microscopic causal footprint forces the synchronous product scheduler. The
terminal obligation is exact: derive the action, projectors, linear weights,
joint kernel, and update order for all 26 nonzero neighbor types, and prove
that the cubic-response and common-sign twins cannot arise from the same
physical mechanism. The current parent explicitly exhibits those twins
([Block84 `:385-445`](ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md)),
so this is an actionable discriminator route rather than rhetoric. A finite
resource or changed formation predicate could likewise halt, but it would be a
different law and therefore would not refute C1/C2.

Resolution: this steelman defeats any universal nonderivability or universal
nonhalting claim, so neither is made. It does not defeat C1/C2, which quantify
only the displayed candidate, or C3, which is indexed to the present live
authority. The microscopic discriminator is queued as the highest-value
scientific route after packaging; if it closes, it should supersede rather
than merely supplement primitive registration.

If that derivation is unavailable, the shortest auditable route is narrower
than an axiom rewrite: register the complete finite-state transition as one
downstream approved primitive, explicitly excluding the initial condition,
physical duration, source, and gravity. Registering a weight table without
the scheduler/product kernel would leave the global law incomplete.

### N8 — Cross-cycle echo audit

The repo search covered prior law-completeness, kernel-selection, scheduler,
global-measure, Markov, and primitive-registration walls. Each candidate's
lifecycle and mechanism are dispositioned explicitly:

| prior echo / indexed mechanism | retired since? | retirement or surviving mechanism | could the mechanism apply here? | addressed disposition |
|---|---|---|---|---|
| [`CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md:31-50,195-215`](work_history/repo/review_feedback/CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md) / fill state, atomic law, continuation, concurrency, actuality | **partly** | this cycle's explicit finite-state kernel retires the mathematical state/update/continuation portion for one candidate; actuality and physical time survive | **yes, and applied** through the standard-Borel kernel and scheduler controls | addressed; no whole-TOE completeness inference |
| [`COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md:81-170`](work_history/repo/review_feedback/COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md) / discriminate inequivalent complete sampled laws | **no** | the present linear/cubic and product/common-sign pairs reproduce the same selection problem with current objects | **yes**: a microscopic discriminator or approved complete-law premise could select one | addressed in Gates A/C and queued in N6/N7; no selection claimed |
| [`CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md:14-48,226-294`](work_history/repo/review_feedback/CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md) / atomic update or causal-predecessor rule | **partly** | frozen-prestate append order commutes, but dynamic recomputation remains a distinct process | **yes, and applied** by declaring/test-driving the synchronous atomic transition | addressed in Gate G; no broader causal-schedule equivalence claimed |
| [`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md:298-356`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md) / distinguish a global measure from local menus/effects | **no** | an explicit finite PVM kernel bypasses the typing gap for this candidate but does not derive or select it | **yes** through microscopic derivation or complete-law approval, not by a definition change | addressed in N6/N7; the global interface wall is not declared retired |
| [`POST_RECORD_TWO_STATE_MARKOV_STABILITY_INTERFACE_2026-06-06.md:15-45,70-90`](POST_RECORD_TWO_STATE_MARKOV_STABILITY_INTERFACE_2026-06-06.md) / supply a kernel before using Markov stability | **partly** | this cycle supplies a Borel kernel on every finite Record map, but no physical time/bridge | **yes, and applied** by constructing rather than merely naming the kernel | addressed in Gates C/I; physical-time language remains excluded |
| [`KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md:15-37,67-112`](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md) plus the live registry / explicit owner-approved primitive registration | **yes for its own graining wall** | owner approval plus a narrow source note, policy record, and registry entry made `c_t=c_s` an accepted premise without pretending derivation | **potentially**, but only for the complete Record law and only after explicit owner approval | considered as Route C, not applied or silently imported; microscopic derivation remains scientifically stronger |

No indexed retirement mechanism was missed: bounded construction was applied
where it fits; atomic scheduling was applied at its exact scope; convention
reframing cannot choose probabilities; and primitive registration is carried
forward as an explicit owner-governance option rather than present authority.
The echoes constrain rhetoric and test selection; they are not hidden
premises.

**Gate verdict:** PASS for the bounded positive arbitrary-finite-state Markov
theorem and the candidate-specific non-halting/boundary controls. No universal
no-go, law adoption, physical-time claim, source identification, gravity
closure, retention, or score movement is shipped.

## 10. Reproduction

```bash
python3 scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py
```

Expected final line:

```text
TOTAL: PASS=10 FAIL=0
```

Mutation controls:

```bash
for mutation in \
  stale_axiom infinite_frontier break_normalization content_feedback \
  overwrite noncovariant false_halt dynamic_scheduler erase_boundary \
  non_markov law_claim
do
  python3 scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py \
    --mutation "$mutation"
done
```

Each mutation must produce exactly `TOTAL: PASS=9 FAIL=1` at its named gate.

## 11. Boundary

Established here:

- a finite frontier and `6N` bound for every finite Record domain;
- normalized finite-atomic transitions from every finite `M_2(C)` Record map;
- exact content-blind formation, supported append, and permanence;
- translation/proper-cubic covariance on arbitrary finite domains;
- the correct uncountable standard-Borel state-space type;
- normalized Markov cylinders and finite-time histories;
- finite propagation at most one lattice edge per iteration;
- an extreme-site proof of no nonempty finite full-lattice halt;
- fixed-prestate append commutativity and dynamic-scheduler inequivalence; and
- the exact two-cube boundary artifact.

Not established here:

- an adopted or uniquely selected physical law or linear response;
- derivation/selection of the spatial-to-Pauli action;
- physical justification of synchrony, conditional independence, or outcome
  actuality;
- a physical initial state, finite resource/capacity law, or arbitrary
  infinite-state process;
- physical time, cadence, Lorentzian causality, or a metric;
- energy-momentum/source typing, normalization, a nonlinear Ward identity,
  connection response, or gravity;
- an axiom edit or approved-primitive registration; or
- audit retention, obligation retirement, or TOE percentage movement.
