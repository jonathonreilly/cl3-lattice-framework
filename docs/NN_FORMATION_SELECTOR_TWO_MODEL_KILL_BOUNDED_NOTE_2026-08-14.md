---
claim_id: nn_formation_selector_two_model_kill_bounded_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "For the Block71 five-M2 same-carrier packet candidate, an explicit 15-SWAP precompaction, a 53-primitive nearest-neighbour compilation of the 29-gate algebraic word, a four-SWAP archive, and one marker gate give a 73-primitive finite candidate on 15 sites while preserving every displaced factor. The exact rank-four readiness projector factors through a 23-gate unitary whose nearest-neighbour compilation costs 39 primitives, so a nondemolition conjugation query costs 78 primitives plus three onsite tests. An explicit symmetric atomic three-Record coupling conditional on an available matter bit gives the four exact branch weights in all 24 proper-cubic frames. Under the additional iid product-endpoint premise, exact-one-marker probability is at most one half; an explicit visible-tag nearest-neighbour factorization escapes that bound. Two normalized covariant full-support one-site kernels and two positive event hazards demonstrate extensional nonselection on the tested interface. These are finite compatible constructions and a narrow conditional obstruction; they do not supply the physical gate/update law, clean preparation, a live-M2-to-Record controller bridge, an integrated one-probability-space formation instrument, formation site/rate/draw, global confluence, gravity, an axiom edit, an audit verdict, obligation retirement, or TOE percentage movement."
runner: scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py
---

# Nearest-neighbour formation selector and two-model kill

**Date:** 2026-08-14

**Type:** `bounded_theorem`

**Audit authority:** independent audit only; no audit status is applied here.

**Status:** exact finite candidate mathematics; no physical law selected

**Constitutional effect:** none. This is **not an axiom edit**, and it does not
register an approved primitive.

**TOE accounting:** no audit-retained obligation is retired. There is **zero
TOE percentage movement**.

Primary runner:
[`scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py`](../scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py)

Direct scientific inputs:

- [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md); and
- [Block71 same-carrier packet](SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md).

The original branch ancestry is historical provenance. Current authority is
the exact current memo and selected parent files, separately content-bound by
the runner. Its four declared inputs include the imported Block71 program;
the older long candidate stack is not authority.

## Result up front

This block changes the route diagnosis in three material ways.

First, the finite non-nearest-neighbour geometry in Block71 is not a
representability obstruction. Put the five roles around the compact star

```text
root c = (-1,1,0)
P = c + (1,0,0)       M = c + (0,0,1)
B = c + (0,-1,0)      R = c
A = c + (0,0,-1).
```

An exact 15-SWAP factor permutation moves the five original factors to this
star. Eight of the twenty two-M2 gates are already center-to-leaf. Each of the
twelve leaf-to-leaf gates is implemented by a returned two-SWAP conjugation
through the center. Therefore the 29-gate word becomes

```text
9 onsite gates + 20 NN two-M2 gates + 24 routing SWAPs = 53 primitives.
```

Four more SWAPs place `P,M,B` at the three Record targets, and one onsite
Hadamard makes the marker. The complete candidate costs

```text
15 + 53 + 4 + 1 = 73 nearest-neighbour/onsite primitives
```

on 15 sites. Every temporary transit is returned. The final token permutation
is injective, moves the three arbitrary target prestates to three unique output
sites, and preserves arbitrary coherence and external entanglement. This is a
candidate circuit identity. Lattice and Qubit do not themselves authorize
SWAP, controlled rotations, this gate order, or a program counter.

Second, the Block71 readiness projector is also exactly compilable. With

```text
theta = 2 atan(sqrt(2/5)),       phi = pi - 2 theta,
Q = P1_P tensor I_M tensor I_B tensor P0_R tensor P0_A,
```

define

```text
V = CRY(M,R;theta) CRY(B,R;theta) CCRY(M,B,R;phi)
    CNOT(R,A) Toffoli(M,B->A).
```

The existing exact decompositions expand `V` to 23 logical gates: 14 two-site
and nine onsite. Compact-star routing adds 16 SWAPs, so `V` costs 39 NN
primitives. Numerically and algebraically,

```text
Pi_ready = V Q V^dagger,
||Pi_ready - V Q V^dagger||_F = 7.8e-16.
```

A nondemolition conjugation query costs 78 NN primitives plus the three onsite
binary tests in `Q`. A coherent physical yes/no instrument would additionally
need a clean pointer and conjunction rule. More importantly, the query
recognizes clean candidate rays; it does not create their supplied
`P=1,B=R=A=0` resources. **Clean preparation remains open**.

Third, there is no universal tag-free endpoint no-go. Conditional on an
available bit `m`, let

```text
p_00 = p_01 = 1/2,       p_10 = 1/5,       p_11 = 4/5.
```

For two symmetric endpoints of an oriented right-angle star, the exact joint
law

```text
J_m(K_minus,K_b) = p_mb/2,
J_m(K_b,K_minus) = p_mb/2
```

normalizes, produces exactly one marker, and gives both endpoints the same
marginal

```text
mu_m = (1/2) delta_Kminus
     + (p_m0/2) delta_K0
     + (p_m1/2) delta_K1.
```

Every one of 192 `(m,b,orientation,frame)` cases decodes correctly. This
**atomic coupling is compatible, not derived**. It is an additional joint
formation law, not a consequence of the one-site marginal wording in
Admissibility.

Under the stricter added premise that the two symmetric endpoint outputs are
conditionally iid, if either endpoint has marker probability `a`, then

```text
Pr(exactly one marker) = 2a(1-a)
                       = 1/2 - 2(a-1/2)^2
                       <= 1/2.
```

The desired probability is one. That is a real half-unit gap, but only for the
**strict product/Markov reading**. The atomic `J_m` escapes it. So does an
explicit visible `K_plus` tag on the four-site NN path

```text
tag -- head -- root -- metadata.
```

With uniform `m` prior and joint weights `p_mb/2`, the reverse conditionals are

```text
Pr(m|b=0) = (5/7,2/7),       Pr(m|b=1) = (5/13,8/13).
```

The runner executes the complete NN graphical factorization

```text
Pr(tag=K_plus) = 1,
Pr(head=K_minus | tag=K_plus) = 1,
Pr(root=K_m | head=K_minus) = 1/2,
Pr(metadata=K_b | root=K_m) = p_mb.
```

Those five normalized local kernels multiply to `p_mb/2`; the packet decoder
and complete-map scanner recover all 96 `(m,b,frame)` cases. This is an atomic
joint graphical model, not a claim that Records form sequentially along the
path. That repair consumes an additional readable Record and changes the packet.
An unrecorded tag would merely reopen the live-substrate bridge.

## The decisive failure of integration

The positive pieces still do not form one physical law. They currently occupy
three different probability/control layers:

1. a continuous one-site Admissibility support measure on `M_2(C)`;
2. the discrete conditional atomic law `J_m` over a three-Record packet; and
3. an event hazard `q` supplying no-event versus formation.

Full support in the first layer is not a branch-weight bridge: an exact
projector can be supported while having zero singleton mass. The second layer
does supply the desired discrete weights, but only conditional on an available
`m`. The third layer changes occurrence cadence without changing the
conditional weights.

The controller typing is the sharpest blocker. The current axioms say both
that a state is a configuration of Records and that only Records are readable.
Before the candidate event, the live matter label `m` in the Block71 circuit is
not a Record and is absent from the six-neighbour Record conditions. Hence two
pre-event Record states that differ only in unrecorded `m` expose the same
Admissibility input but require different rows

```text
(1/2,1/2) != (1/5,4/5).
```

No Record-only nearest-neighbour controller can distinguish those inputs
without one of three changes:

- make `m` a pre-existing readable Record;
- jointly generate `m` and `b`, which changes the task from reading a live
  matter input to generating a correlated packet; or
- supply a lawful live-M2-to-formation controller bridge.

The **live-substrate bridge remains open**. This is not evidence that gravity
or Record formation is impossible; it is an exact localization of the
interface that must be specified.

## Two-model selector kill

For neighbour profile `n in {0,...,6}`, define normalized complex Gaussian
one-site densities

```text
K1: alpha(n) = 1+n,       K2: alpha(n) = 2+n,
rho_alpha(A) = (alpha/pi)^4 exp(-alpha ||A||_F^2).
```

Both are translation/proper-cubic covariant, vary with the NN condition, and
have full support. Their blank-profile second moments are respectively four
and two, so they are inequivalent. In fact `alpha_t(n)=1+t+n` for every real
`t>0` gives a continuum. This proves nonselection of the extensional one-site
values by the displayed axiom text; it does not identify the actual kernel.

Independently, on an isolated unique opportunity, both

```text
L1: q = 1,         L2: q = 1/2
```

normalize, refuse an occupied target, and use the same conditional atomic
`p(b|m)`. They differ in expected event/Record/source-hop counts. Current
Admissibility explicitly leaves formation site and rate downstream, so no
displayed premise selects one hazard. These models are compatible candidate
extensions, not simultaneously adopted laws and not a derivation of either.

The selector kill is therefore honest but narrow: the present axioms plus the
Block71 packet do not uniquely determine the one-site values, event hazard, or
controller bridge. Writing down one member of either family would be
law-selection theater.

The scope sentinels are literal: support is not a branch-weight bridge;
clean preparation remains open; a downstream formation primitive remains unapproved;
global multi-event confluence remains open; this is not an axiom edit; and
there is zero TOE percentage movement.

## Exact axiom/downstream-law update ledger

No contradiction forces an edit to Lattice, Qubit, Admissibility, or Record.
The least invasive repair is an owner-approved **downstream formation
primitive**. If the intent is instead that the four axioms alone determine an
end-to-end formation law, then their semantic surface is incomplete in the
following exact places.

| datum | current text supplies | missing decision | minimum repair surface |
|---|---|---|---|
| controller domain | Record configurations; only Records readable | whether unrecorded onsite `M_2(C)` data may control formation | choose Record-only input, or explicitly extend lawful controller state to live local possibilities |
| probability object | one-site probability distribution from NN conditions | whether multi-site Record formation is product, Markov-factorized, or one atomic joint measure | state an atomic finite-update kernel or a factorization rule |
| realized transition | support and Record locking | no-event mass, opportunity/site rule, rate, draw, and physical membership append | include a normalized instrument/kernel whose outcomes are finite Record updates including refusal |
| operations | local possibility algebra | no gate set, SWAP dynamics, program counter, or update ordering | approve a local transition primitive or derive it from a retained dynamics |
| resources | none of the clean five-factor preparation | provenance/debit for `P=1,B=R=A=0` and any pointer/tag | specify preparation, conserved capacity, or an initial-condition boundary |
| global action | translation/rotation covariance of the rule | arbitration of overlapping opportunities and increasing-region consistency | give a homogeneous scheduler/QCA/instrument and prove confluence or order independence |

A decision-ready candidate wording, not adopted here, is:

> A formation law is a translation- and proper-cubic-covariant normalized
> kernel from a declared local controller state to finite atomic Record updates,
> including no-event/refusal. Its controller domain, joint factorization,
> opportunity rule, rate, realized draw, update instrument, and resource debit
> are part of the law.

That sentence names the missing type but does not select its values. To make
the Block71 packet physical, the registered primitive would additionally have
to choose Record-only versus live-M2 conditioning, adopt or replace `J_m`, set
`q` and site arbitration, authorize the local operations, and account for the
clean inputs. No minimal numerical choice is forced by the present framework.

## TOE lanes

Because retained obligations, not candidate artifacts, control the map, the
lane scores remain unchanged:

| lane | repository | physical | autonomous | ceiling |
|---|---:|---:|---:|---:|
| operational / Records | 95% | 92% | 50% | 99% |
| causal / time | 76% | 72% | 41% | 99% |
| inertia / matter | 95% | 96% | 75% | 99% |
| gravity / source / resources | 70% | 45% | 29% | 94% |
| Born / history | 84% | 63% | 34% | 99% |

The significant progress is route confidence: finite NN formation and
readiness representability are positive, and the atomic coupling proves that
endpoint symmetry alone is not fatal. The controlling obligation is now the
typed integrated formation primitive. The percentages do not move until that
law is retained end to end.

## No-Go Discipline gate

**Gate outcome:** PASS for two narrow statements: (i) iid symmetric endpoints
cannot produce exactly one marker with probability above one half; and (ii)
the executed axiom interface does not select a unique member of the displayed
kernel/hazard families. FAIL and demoted for any universal tag-free no-go,
formation impossibility, axiom-necessity claim, or physical-law selection.

### N1 — Alternative-route enumeration and normalization

Routes are normalized by `(object, mechanism, terminal obligation)`.

| route | normalized object / mechanism / terminal | execution and result | marker |
|---|---|---|---|
| R1 compact circuit | Block71 word / star compaction plus returned SWAP macros / NN representability | executed; 73-primitive packet word passes, so the old distance wall is not terminal | **ATTEMPTED — CLOSED positively** |
| R2 atomic symmetric endpoints | two endpoint Records / correlated joint `J_m` / exact-one marker and branch weights | executed; normalizes and decodes all 192 cases, defeating a universal tag-free no-go | **ATTEMPTED — CLOSED positively** |
| R3 iid endpoints | two endpoint marginals / conditional product / exact-one marker | executed analytically; `2a(1-a)<=1/2`, so this restricted mechanism misses by at least `1/2` | **ATTEMPTED — CLOSED negatively on stated premise** |
| R4 visible tag | four Record sites / NN path factorization / orient marker versus metadata | executed; exact joint and Bayes rows pass, but the extra Record changes the packet | **ATTEMPTED — CLOSED as escape** |
| R5 pre-existing root Record | Record-only controller / condition endpoints on readable `K_m` / distinguish the two weight rows | typed and compatible, but it changes live-input measurement into continuation from an existing Record | **ATTEMPTED — OPEN alternate task** |
| R6 joint generation | root plus endpoints / draw `(m,b)` atomically / avoid reading live `m` | exact joint `p_mb/2` is executed for uniform `m`; it does not couple to the Block71 input | **ATTEMPTED — OPEN alternate task** |
| R7 live-substrate controller | unrecorded M2 plus Records / approved local instrument / preserve matter-dependent semantics | no such retained bridge is supplied or executed | **SEARCHED — OPEN** |
| R8 global QCA/instrument | full lattice / homogeneous local update and overlap arbitration / autonomous formation | not executed; a richer rule could select gate order, clean debit, joint update, and hazard | **SEARCHED — OPEN** |

No route supports a universal no-go. R2 is the decisive steelman against one.
R7 or R8 could close the intended physical task, but requires new retained or
approved law content.

### N2 — Wall-independence audit

The corrected one-event-to-global surfaces are:

```text
W1 = finite NN representability of the packet and readiness maps
W2 = physical operation law plus clean-resource/instrument provenance
W3 = controller domain and access to the matter label m
W4 = extensional one-site Admissibility probability values
W5 = atomic joint multi-site Record coupling
W6 = opportunity/site/rate/no-event/draw selection
W7 = homogeneous overlap arbitration and global confluence
```

All 21 pairs are checked separately:

| pair | W_i closes W_j? | W_j closes W_i? | witness | result |
|---|---|---|---|---|
| W1/W2 | no | no | a circuit identity does not authorize gates or clean inputs; an operation law need not implement this packet | independent |
| W1/W3 | no | no | NN routing does not expose `m`; a typed controller need not compile the word | independent |
| W1/W4 | no | no | compiled gates do not choose probability values; a distribution does not route factors | independent |
| W1/W5 | no | no | representability does not assert atomicity; a joint write need not use this circuit | independent |
| W1/W6 | no | no | a finite word supplies no opportunity clock; a hazard does not compile it | independent |
| W1/W7 | no | no | one support says nothing about overlaps; a global scheduler may use another local map | independent |
| W2/W3 | no | no | authorized gates can still lack a lawful input domain; controller typing does not supply dynamics | independent |
| W2/W4 | no | no | clean operations do not fix Admissibility values; values do not create clean factors | independent |
| W2/W5 | no | no | a gate law can end in sequential writes; atomic coupling does not authorize gates or pointers | independent |
| W2/W6 | no | no | an instrument implementation does not fix event rate; a rate does not provide an instrument | independent |
| W2/W7 | no | no | local resources do not arbitrate overlaps; confluence does not prepare local resources | independent |
| W3/W4 | no | no | knowing whether `m` is visible does not select numeric distributions; a kernel can ignore or encode another controller | independent |
| W3/W5 | no | no | controller access does not impose correlations; `J_m` assumes rather than supplies access to `m` | independent |
| W3/W6 | no | no | a typed local input does not schedule events; a schedule need not expose live M2 | independent |
| W3/W7 | no | no | local observability does not settle simultaneous matches; arbitration does not define controller content | independent |
| W4/W5 | no | no | one-site marginals do not determine a joint coupling; many joints can share marginals | independent |
| W4/W6 | no | no | conditional content odds do not set occurrence; occurrence can vary with fixed content odds | independent |
| W4/W7 | no | no | local values do not prove global consistency; global ordering does not select local values | independent |
| W5/W6 | no | no | an atomic update can occur at any hazard; a hazard can drive sequential or different writes | independent |
| W5/W7 | no | no | one isolated atomic event does not resolve overlaps; a confluent law can use another joint kernel | independent |
| W6/W7 | no | no | isolated-site rate does not arbitrate collisions; arbitration does not fix physical cadence | independent |

This block closes W1 only as candidate mathematics and constructs one candidate
for W5. Because W2 does not authorize the construction and W3/W6 are absent,
W5 is not retired as framework science. W4 is positively shown nonselected;
W7 is unexecuted.

### N3 — Hidden-wall scan

| phrase family | classification |
|---|---|
| `gate`, `SWAP`, `program`, `step`, `execute` | exact candidate matrices and order only; no framework dynamics is inferred |
| `clean`, `zero`, `blank`, `ancilla`, `pointer` | `P=1,B=R=A=0` and any query pointer are explicit resources; no creation mechanism is supplied |
| `state`, `condition`, `controller`, `read` | current state is Records; live `m` is explicitly not silently treated as readable |
| `probability`, `kernel`, `support`, `mass`, `draw` | continuous support, discrete atomic weights, and event hazard are kept as distinct probability objects |
| `joint`, `atomic`, `simultaneous`, `Markov`, `product` | `J_m` is a proposed correlated update; the half-bound is limited to the added iid premise |
| `tag`, `frame`, `orientation`, `role` | frame is decoded from Records; visible tag is debited; no hidden Python role label is a lawful input |
| `clock`, `rate`, `opportunity`, `scheduler`, `replay` | two hazards are comparators; no physical clock or global scheduler is imported |
| `source`, `stress`, `Ward`, `gravity` | none is derived; packet incidence is not physical stress-energy |
| `axiom`, `primitive`, `registered`, `retained` | only current text is authority; proposed wording is not adopted or retained |
| `obstruction`, `no-go`, `wall`, `impossible` | every negative is tied to iid endpoints or the displayed underdetermined interface |

The hidden host inputs are exactly `m`, role/frame, gate step, clean state, and
opportunity clock. The runner exposes rather than imports them.

### N4 — Residual matching

| direct input | content used | positive closure here | residual |
|---|---|---|---|
| current minimal axioms | `Z^3` NN/proper-cubic covariance, one-site `M_2(C)`, Admissibility distribution type, Record configuration/readability/locking | type checks for candidate kernels and Records | all extensional values, controller state, dynamics, joint update, site/rate/draw, and global rule remain downstream |
| Block71 packet | exact 29-gate word, four rays/weights, rank-32 archive, exact packet keys/decoder, dirty-input witness | compiled compact implementation and exact receipt | parent explicitly supplies clean realized branches and no formation law |
| this runner | routes, factor tokens, `VQV^dag`, `J_m`, product identity, Gaussian families, hazards, and mutations | finite candidate theorems and selector diagnostic | no integrated physical law or retained status |

The extensional-rule and controlled-copy notes in N8 are search comparators,
not direct dependencies. Their status and premises are not imported.

### N5 — Rhetoric and granularity audit

The strongest statement is: “the Block71 finite maps are NN-representable; one
exact atomic star law reproduces the weights if `m` is available; iid endpoints
cannot do so; and the current interface does not select the controller, kernel,
or hazard.” It is not: “the framework supplies the circuit,” “the atom is the
actual law,” “formation is impossible,” “an axiom edit is forced,” or “a TOE
lane closed.”

The runner emits these executed granularities:

```text
per_element: checked 29 formation gates, 23 readiness gates, every routed macro basis state, four exact branch weights, and the analytic 2a(1-a) product bound
per_site: checked the 15-site compact route, arbitrary factor permutation, three final Record targets, every NN edge under 24 proper-cubic rotations, and the four-site visible-tag escape
per_mode: checked both matter labels, four (m,b) branches, both marker orientations, 24 frames, two normalized support kernels, and hazards q=1 and q=1/2
per_block: checked Block71 receipt, 73-primitive packet compilation, 78-primitive readiness query, clean-resource deficit, atomic coupling, controller collision, and selector nonuniqueness
lattice_wide: checked and not executed — finite candidate words and isolated-star probability models do not constitute a homogeneous full-Z3 controller, supplied dynamics, or overlap-confluence theorem
```

### N6 — Partial-closure path scan

| component | positive result | remaining terminal |
|---|---|---|
| formation representation | exact 73-primitive NN/onsite candidate on 15 sites | physical gate/update law, order controller, and clean-resource debit |
| readiness | exact 39-primitive `V`; 78-primitive conjugation query | clean pointer/conjunction, physical instrument, and input provenance |
| branch content | symmetric atomic `J_m` gives exact weights and equal endpoint marginals | lawful access to `m` and adoption of the joint kernel |
| product boundary | exact half-bound under iid endpoints | irrelevant once atomic correlation or an explicit tag is allowed |
| Admissibility | two exact normalized covariant full-support examples | actual extensional distribution and its relation to `J_m` |
| occurrence | two normalized positive hazard examples with refusal | selected opportunity/site/rate/draw and a physical time unit |
| global law | none | overlaps, arbitration, translation-homogeneous execution, increasing-region control |
| gravity | no new source law | source typing/normalization, metric law, nonlinear identity, Lorentzian update, and instrument |

The shortest positive route is now to specify and test one typed integrated
formation primitive, not to optimize the finite circuit further. If no such
primitive is approved or derivable, formation should be recorded as an axiom
interface gap and effort should pivot to the next full-science seam.

### N7 — Steelman and strongest surviving escape route

The strongest criticism is that the runner has made candidate mechanics more
explicit without converting them into physics. The 73-step program needs a
gate law and step controller. `Pi_ready` is a mathematical query, not an
instrument. `J_m` assumes the very controller datum absent from a Record-only
prestate. Gaussian support, discrete output weights, and hazard are not one
probability space. A unique isolated template does not solve competing
translated matches. Thus none of the positive algebra retires occurrence,
Born selection, autonomy, or gravity.

The strongest surviving positive escape is a local covariant instrument whose
declared input includes either a readable root Record or a lawful live-M2
substrate, whose outcomes are atomic finite Record updates plus no-event, and
whose Kraus/classical kernel simultaneously supplies `J_m`, site/rate/draw,
clean-resource disposition, and refusal. A homogeneous QCA or matching process
could then arbitrate overlaps. Such an object would integrate the three
probability layers and could produce real TOE movement. It is not ruled out.

Record-only joint generation, a visible orientation tag, a fresh controlled-
copy fragment, a nonunitary sink with an explicit debit, and an output-root
packet remain live alternatives. Their survival prevents any broader negative.

### N8 — Cross-cycle echo audit

An actual repository search was performed for extensional NN rules, formation
site/rate, controlled copy, atomic updates, controller domains, live M2, and
product endpoints.

| echo | what it contributes | relation to this block | direct authority? |
|---|---|---|---|
| [extensional NN rule deep probe](EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md) | a large covariant rule-family/nonselection witness and explicit formation-rate boundary | corroborates that covariance plus variation does not determine values | no; search comparator only |
| [pointer nondemolition constraint](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md) | pointer and nondemolition resource typing | shows how an instrument can add a clean pointer premise | no; not executed here |
| [controlled-copy isometry](RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md) | a fresh-fragment write mechanism | remains a live alternative if freshness and calibration are supplied | no; not imported |
| [one-step controlled-copy class](RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md) | a narrower local update family | could provide operation syntax but not this controller/hazard selector | no; not imported |
| Block71 same-carrier packet | exact parent rays, archive, and decoder | directly rechecked and compiled here | yes, bounded parent only |

No located echo supplies the combined live-input controller, atomic joint law,
hazard, clean debit, and global arbitration required here. No prior audit grade
is imported. The cross-cycle recurrence is consistent: one-site support,
realized draw, formation site/rate, and instrument dynamics have repeatedly
been separated. This block adds the exact atomic-correlation versus product
fork and the controller collision.

## Verification

Run:

```text
python3 scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py
```

The baseline must end with `FAIL=0`. Each hostile mutation must fail at least
one named check:

```text
stale_axiom non_nn_macro dirty_prep collapse_atomic break_tag
collapse_kernel zero_support fixed_rate law_claim
```

`zero_support` is a hostile semantic control proportional to the Gaussian
outside an open Frobenius ball around `K_minus` and zero inside. The runner
checks the open-ball exclusion; existence of the positive conditioning
constant is analytic and is not numerically integrated. The mutation therefore
does not merely alter a measure-zero density representative.

Independent audit is required before any retained status or TOE movement.

## 2026-09-08 evidence correction: Gaussian mass

Identify `M_2(C)` with eight real coordinates and use ordinary Lebesgue
measure. The displayed Frobenius Gaussian has integral
`rho_alpha(0) (sqrt(pi/alpha))^8 = rho_alpha(0) (pi/alpha)^4 = 1`.
The checker now evaluates the actual density at zero and on all eight real
coordinate axes, plus a mixed-coordinate point, to bind both prefactor and
exponent to this independent integral. Positivity of alpha alone was not a
normalization check; doubling the implemented prefactor is now rejected.
This preserves the stated Gaussian families, moments, and conditional scope.
