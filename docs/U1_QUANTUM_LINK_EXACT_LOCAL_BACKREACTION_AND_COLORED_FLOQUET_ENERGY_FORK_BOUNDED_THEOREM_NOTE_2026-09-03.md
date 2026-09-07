# Quantum-Link Exact Local Backreaction and the Colored Floquet Energy Fork

**Status:** proposed_retained
**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct interface parent:**
[`U1_FINITE_STEP_GAUGE_COVARIANT_MATTER_CURRENT_OPERATOR_WORK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_FINITE_STEP_GAUGE_COVARIANT_MATTER_CURRENT_OPERATOR_WORK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Field-work parent:**
[`U1_EXACT_MIDPOINT_SOURCE_WORK_CLOSED_DIPOLE_PURE_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_EXACT_MIDPOINT_SOURCE_WORK_CLOSED_DIPOLE_PURE_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Conserved-source parent:**
[`U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Kinetic normalization boundary:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)

**Runner:**
[`scripts/u1_quantum_link_exact_backreaction_colored_floquet_2026_09_03.py`](../scripts/u1_quantum_link_exact_backreaction_colored_floquet_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/u1_quantum_link_exact_backreaction_colored_floquet_2026_09_03.txt`](../logs/runner-cache/u1_quantum_link_exact_backreaction_colored_floquet_2026_09_03.txt)

## Result up front

The local matter-field energy-backreaction join can be closed exactly on one
oriented bond with a finite flux carrier.

Let a link have flux states

```text
m=-S,...,+S,
```

electric operator `E|m>=m|m>`, and hard-cutoff raising operator

```text
U|m>=|m+1> for m<S,        U|S>=0.
```

Put one charge on the two endpoint matter states `|tail>,|head>`, and use

```text
H_E=(g^2/2) E^2,
H_hop=-t[U tensor |head><tail|+U^dagger tensor |tail><head|],
H_bond=H_E+H_hop.
```

The joint Hamiltonian commutes with both endpoint Gauss generators

```text
G_tail=-E-n_tail,
G_head=+E-n_head.
```

Its exact finite unitary `V=exp(-ih H_bond)` therefore preserves Gauss and
total matter charge. If

```text
E'=V^dagger E V,
Jbar=(E'-E)/h,
```

then the same Hermitian integrated current obeys

```text
Jbar=(n_head'-n_head)/h
    =-(n_tail'-n_tail)/h.
```

Most importantly, the local energy exchange closes exactly:

```text
Delta H_E
 =(g^2 h/4){Jbar,E+E'},
Delta H_hop=-Delta H_E,
Delta H_bond=0.
```

The runner verifies this over `S=1,2,3` and three independent coupling,
hopping, and step triples. This is the missing one-bond backreaction theorem:
matter transfer, flux response, Gauss, unitarity, and opposite work coexist in
one local finite-payload unitary.

The result exposes a separate lattice-wide choice. On two adjacent bonds that
share the middle matter site, each local Hamiltonian still commutes with all
three Gauss generators and each operational layer closes its own work exactly.
But the two bond Hamiltonians do not commute. Consequently:

- the unsplit unitary `exp[-ih(H_1+H_2)]` conserves the summed Hamiltonian
  exactly;
- the finite-depth Lie product has `O(h^2)` one-tick summed-energy drift;
- the palindromic `H_1/2-H_2-H_1/2` product is exactly unitary,
  Gauss-preserving, and reversible, and suppresses that drift to `O(h^3)`;
- the palindromic product has an exactly conserved Hermitian principal Floquet
  generator `H_F`; and
- `H_F-H_1-H_2=O(h^2)` and contains resolved cross-bond matrix entries absent
  from the simple summed Hamiltonian.

Two disjoint bonds commute and provide the exact control: their layer product
equals the unsplit exponential and conserves the summed energy.

Thus local backreaction is not blocked. The remaining fork is which energy
and time law the program intends at finite lattice step:

1. exact evolution under a time-independent summed Hamiltonian;
2. a strict finite-depth reversible tick whose exact energy is its Floquet
   generator; or
3. a larger collision/clock carrier engineered to conserve a simple local
   summed energy exactly.

No axiom currently selects among these. The result therefore advances the
matter-light lane and identifies a real global schedule decision without
turning it into a no-go.

## 1. The finite quantum link

The hard-cutoff shift satisfies

```text
[E,U]=U
```

exactly, including at the upper boundary because both sides annihilate
`|S>`. It is not unitary:

```text
U^dagger U=I-|S><S|.
```

That cost is explicit. The full bond Hamiltonian is nevertheless Hermitian,
so its exponential is exactly unitary.

The hopping term connects

```text
|m,tail> <-> |m+1,head>
```

for `m=-S,...,S-1`. The finite Hilbert space decomposes into `2S` paired
two-state transfer sectors and two dark boundary states,

```text
|S,tail>,                   |-S,head>.
```

The runner checks this degree census for `S=1,2,3`. This is a finite link
model, not the infinite compact rotor and not a cyclic shift that wraps
maximum flux into minimum flux.

The endpoint Gauss values agree across every paired transition. For example,

```text
G_tail |m,tail>=(-m-1)|m,tail>,
G_tail |m+1,head>=(-m-1)|m+1,head>,
```

and similarly for `G_head`. Hence

```text
[G_tail,H_bond]=[G_head,H_bond]=0.
```

Background charge constants may be added to both generators without changing
the commutators. The displayed convention is chosen only to make the transfer
algebra transparent.

## 2. One current closes charge and flux simultaneously

Under the exact bond unitary define

```text
O'=V^dagger O V.
```

Gauss conservation gives

```text
-(E'-E)-(n_tail'-n_tail)=0,
(E'-E)-(n_head'-n_head)=0.
```

Therefore one finite-step operator

```text
Jbar=(E'-E)/h
```

is simultaneously the flux current, head charge gain, and negative tail
charge gain. It is Hermitian because it is a difference of Hermitian
operators.

This directly realizes the interface parent's abstract current from endpoint
transport, now with a dynamical link rather than an external phase. The
runner also checks that `Jbar` approaches the instantaneous Heisenberg current

```text
i[H_bond,E]
```

linearly as `h` is refined. The finite current, not the instantaneous endpoint
operator, is what belongs in an exact tick-level continuity equation.

## 3. Exact opposite local work

The electric energy change is

```text
Delta H_E
 =(g^2/2)(E'^2-E^2).
```

For noncommuting `E` and `E'`, the difference of squares has the exact
anticommutator identity

```text
E'^2-E^2=(1/2){E'+E,E'-E}.
```

Using `E'-E=h Jbar` gives

```text
Delta H_E=(g^2 h/4){Jbar,E+E'}.
```

Because `V` is generated by `H_bond`,

```text
V^dagger H_bond V=H_bond.
```

Therefore

```text
Delta H_hop=-Delta H_E.
```

This is precisely the operator-ordering target identified by the interface
parent, with the electric coefficient `g^2` restored. It is not imposed as a
ledger variable; both sides are independently conjugated operators from the
same joint unitary.

The largest numerical residual in the `S=1,2,3` parameter grid is below
`2e-14`. The analytic reason is the commutation of `V` with its generator,
not numerical tuning.

The theorem closes the local electric part of matter-field backreaction. It
does not yet include a magnetic plaquette layer or the photon tick's modified
curl energy.

## 4. Two adjacent bonds preserve Gauss layer by layer

Now use two finite links and three one-particle matter sites,

```text
0 --e1-- 1 --e2-- 2.
```

Let `H_1` and `H_2` each contain its link electric energy and its covariant
hop. The three Gauss generators are

```text
G_0=-E_1-n_0,
G_1= E_1-E_2-n_1,
G_2= E_2-n_2.
```

Every one of the six commutators

```text
[G_v,H_e]
```

vanishes. Thus any product of the local bond unitaries preserves every Gauss
operator exactly, independent of product order or step size. Each individual
layer also has the one-bond integrated-current and opposite-work identity.

This is the constructive content needed by an edge-colored lattice schedule:
Gauss does not accumulate a Trotter error. The difficulty below is energy of
overlapping inactive interactions, not gauge consistency.

## 5. Exact flow versus strict finite-depth composition

Define

```text
H=H_1+H_2.
```

The exact unsplit flow

```text
U_exact(h)=exp(-ihH)
```

is unitary, Gauss-preserving, and conserves `H` exactly. On the two-bond test
this is a finite local block. This note does not infer that exponentiating the
full lattice sum produces a strict bounded-depth circuit.

The one-sided colored product

```text
U_L(h)=exp(-ihH_2) exp(-ihH_1)
```

is finite depth and Gauss-preserving, but the runner obtains

```text
||U_L^dagger H U_L-H||=O(h^2).
```

The palindromic product

```text
U_S(h)
 =exp[-i(h/2)H_1] exp(-ihH_2) exp[-i(h/2)H_1]
```

obeys

```text
U_S(-h)=U_S(h)^dagger
```

and suppresses the summed-energy drift to

```text
||U_S^dagger H U_S-H||=O(h^3).
```

On the refinement ladder `h=0.4,0.2,0.1,0.05`, the Lie errors fall by four
and the palindromic errors by eight, for both flow error and energy drift.
The runner checks operator norms, not one selected initial state.

The reason is visible locally:

```text
[H_1,H_2] != 0
```

when the bonds share matter site `1`. Evolving with `H_1` changes the inactive
`H_2` hopping operator. On two disjoint bonds the commutator vanishes, the
product equals `exp[-ih(H_1+H_2)]`, and summed energy is exact. This control
isolates overlap rather than flux truncation as the splitting residual.

No no-go follows. Longer products, collision carriers, time-dependent energy,
and exact lattice Hamiltonian evolution remain distinct routes.

## 6. The exact Floquet energy

For each tested small step, the palindromic unitary has a principal Hermitian
generator `H_F` defined by

```text
U_S=exp(-ih H_F).
```

The runner constructs it from a complex Schur decomposition and principal
eigenphases. It verifies

```text
U_S^dagger H_F U_S=H_F
```

to `7e-15`. Therefore the finite-depth tick does have an exact conserved
energy generator on the tested block.

However,

```text
||H_F-H||=O(h^2).
```

Entries of `H_F` at matrix positions where the simple `H_1+H_2` is zero are
also nonzero and scale as `O(h^2)`. They are cross-bond corrections generated
by the palindromic composition.

This is a bounded two-bond statement. It does not prove that the principal
Floquet logarithm on an infinite lattice is finite range, quasi-local under
the required bound, unique across eigenphase crossings, or acceptable as the
physical energy. Those are precisely the global questions now exposed.

## 7. The decision and next discriminator

The local result is unambiguous: exact quantum matter-field backreaction is
possible with finite payload and no Gauss or work mismatch.

The global decision is about time architecture:

| Route | Exact gains | Current cost |
|---|---|---|
| unsplit time-independent Hamiltonian | unitarity, Gauss, simple summed energy | strict finite-depth full-lattice tick not constructed |
| palindromic colored tick | finite depth, unitarity, Gauss, reversibility, exact `H_F` | `H_F` has step-dependent cross-bond corrections |
| enlarged collision/clock law | may keep a simple locally conserved energy and finite depth | extra carrier and explicit construction required |

The highest-value next test is to add the smallest magnetic plaquette layer
to a matter-link block and ask three questions together:

1. does the palindromic tick retain the weak-field two-photon sector;
2. how far does the exact principal Floquet generator spread; and
3. can its leading correction be represented by the existing physical
   neighboring roles rather than a new axiom or payload?

That discriminator connects the exact local backreaction proved here to the
already constructed sourceful photon stack.

## 8. Program and prior-art boundary

The electric-flux plus covariant-hopping Hamiltonian belongs to the standard
Hamiltonian lattice-gauge family; see J. Kogut and L. Susskind,
[“Hamiltonian formulation of Wilson's lattice gauge
theories”](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.395)
(1975). Product-formula order improvement is likewise standard.

The repo-specific contribution is the exact finite-step interface census:
the same integrated operator closes flux, endpoint charge, Gauss, and
anticommutator work, followed by an explicit test of the strict colored-tick
versus summed-energy fork that the sourceful photon program must choose.

Open PR #7903 is a context-only compact-link matter construction. Its code
and conclusions are not inputs to this theorem, and this source does not
change its status.

No axiom edit follows. The minimal axioms do not choose a Hamiltonian,
product schedule, Floquet generator, flux cutoff, or energy observable. The
science first needs the plaquette discriminator above.

## 9. Executable evidence

The runner reports `TOTAL: PASS=23 FAIL=0`. It checks:

- exact hard-cutoff shift algebra and its nonunitary boundary;
- transfer-sector and boundary-state counts for `S=1,2,3`;
- both one-bond Gauss commutators;
- joint unitarity, current equality, Gauss evolution, field work, opposite
  hopping work, and total energy over nine parameter cases;
- instantaneous-current convergence;
- all six adjacent-bond Gauss commutators;
- local exchange on each adjacent operational layer;
- palindromic reversal and Gauss preservation;
- exact unsplit energy;
- Lie and palindromic flow/energy orders;
- exact Floquet conservation, quadratic deviation, and cross-bond entries;
- a disjoint-bond exact control; and
- the shared-bond commutator and inactive-energy change.

## No-Go Discipline Gate

The positive local theorem is paired with a bounded colored-schedule failure.
This gate prevents the `O(h^3)` drift from being promoted into a no-go for
matter-light coupling or local energy.

### N1 — Alternative route enumeration

| Honesty | Route | Outcome |
|---|---|---|
| **ATTEMPTED** | exact one-bond joint exponential | **Positive:** finite payload, unitarity, Gauss, current, and opposite work; checks 1-11. |
| **ATTEMPTED** | exact unsplit adjacent-bond exponential | **Positive:** exact summed energy and Gauss on the two-bond block; check 15. |
| **ATTEMPTED** | one-sided colored product | Local and Gauss-preserving, with `O(h^2)` summed-energy drift; check 16. |
| **ATTEMPTED** | palindromic colored product | **Positive:** local, reversible, Gauss-preserving; summed-energy drift `O(h^3)`; checks 14 and 17-18. |
| **ATTEMPTED** | principal Floquet generator | **Positive exact invariant:** differs from simple `H` and gains cross-bond entries at `O(h^2)`; checks 19-21. |
| **ATTEMPTED** | disjoint-bond product | **Positive control:** exact summed energy because the bonds commute; check 22. |
| **OPEN** | longer product formula | May alter the correction order but does not automatically make simple `H` exact. |
| **OPEN** | collision/clock carrier | Could conserve a simple local energy in strict finite depth; no construction tested here. |
| **OPEN** | full lattice Hamiltonian flow | Exact energy route; strict bounded-depth realization remains untested. |

### N2 — Wall-independence audit

Use

```text
W1 = finite-depth versus exact summed-H evolution,
W2 = locality/range of the exact Floquet generator,
W3 = magnetic plaquette and photon survival,
W4 = flux cutoff and boundary dark states,
W5 = Record preparation/readout and coupling selection.
```

The following motivations do not prove both directions of every pairwise
non-implication. Those logical relations remain unresolved; no independent
wall count or stronger exclusion follows. The positive constructions and
partial witnesses elsewhere in this note retain their stated domains.

| Pair | Relation established? | Existing motivation, not an independence proof |
|---|---:|---|
| W1, W2 | unresolved | a finite-depth tick always has a logarithm, whose locality is separate |
| W1, W3 | unresolved | exact Hamiltonian evolution does not guarantee the desired photon branch |
| W1, W4 | unresolved | product scheduling and flux truncation are distinct |
| W1, W5 | unresolved | time architecture does not select records or coupling |
| W2, W3 | unresolved | a local Floquet generator can have the wrong spectrum |
| W2, W4 | unresolved | generator range is not fixed by link cutoff alone |
| W2, W5 | unresolved | Floquet locality does not supply readout |
| W3, W4 | unresolved | photon survival and boundary saturation are separate limits |
| W3, W5 | unresolved | a photon branch does not fix charge or records |
| W4, W5 | unresolved | payload boundary does not choose physical normalization |

### N3 — Hidden-wall scan

The link uses a hard cutoff, not a unitary cyclic rotor. Matter is restricted
to the one-particle sector. The one-bond result includes only electric and
hopping energy. The adjacent test has two links and three sites at `S=1`.
Principal Floquet phases are taken only on the named small-step ladder. The
operator norms cover the full finite blocks. No full lattice, plaquette,
photon, continuum, Record, or axiom result is inferred.

### N4 — Residual matching

| Surface | Residual | Match here |
|---|---|---|
| finite-step current parent | opposite matter work absent | **positive closure on one bond:** exact joint unitary supplies it |
| source-work parent | current externally supplied | **positive closure on one bond:** dynamical flux and matter produce one current |
| photon tick | finite-depth free magnetic/electric field | **not yet joined:** magnetic plaquette layer remains |
| compact-link context | matter and link Hamiltonian exist | **independent overlap:** current source not imported; finite-step work analyzed here |
| minimal axioms | no transition/energy selector | **unchanged:** Hamiltonian and schedule remain supplied |

### N5 — Rhetoric and resolution audit

“Exact local backreaction” refers only to one active bond. “Exact summed
energy” refers to the unsplit two-bond exponential and disjoint control.
“Floquet energy” refers to the principal logarithm on the tested small finite
block. The palindromic product is not said to conserve the naive summed
Hamiltonian, and its failure is not generalized to longer products, enlarged
carriers, or continuous local Hamiltonians.

The cache contains all five resolution lines:

```text
per_element: finite flux raising, matter transfer, current, and anticommutator work are checked
per_site: both endpoint Gauss generators and the shared middle-vertex generator are checked
per_mode: instantaneous-current and Lie/Strang/Floquet refinement orders are resolved
per_block: one-bond exact backreaction and two-bond overlapping/disjoint controls are checked
lattice_wide: colored local layers preserve Gauss by composition; exact summed energy versus Floquet energy remains the global schedule choice
```

### N6 — Partial-closure paths and primitive check

The approved kinetic primitive does not select an energy or update schedule.
The shortest partial closure is the one-plaquette matter-link tick named in
Section 7. If the exact `H_F` correction remains inside a bounded physical
neighborhood and preserves the photon branch, the finite-depth route advances
without an axiom edit. If it spreads beyond the allowed compiler, the exact
Hamiltonian and collision-carrier routes remain live. A failure of one route
would justify an interpretation decision before an axiom change.

### N7 — Steelman

A hostile reviewer should say the one-bond theorem is standard consequence of
a gauge-invariant Hamiltonian. Correct. Its value is not novelty of the
Kogut-Susskind mechanism; it is closing the repo's exact finite-step current
and operator-work interface in one executable block.

The reviewer should also reject a two-bond result as proof of global Floquet
locality. The note agrees. The cross-bond correction is evidence that the
global question is nontrivial, not evidence that it is impossible. The
one-plaquette/full-neighborhood test is explicitly next.

### N8 — Cross-cycle echo

The immediately prior cycle found that old-time aggregation of colored
currents expands support. This cycle implements the operational local layers
and finds that Gauss and local work close, while energy of inactive overlapping
terms becomes the remaining schedule residual. It avoids repeating the older
mistake of treating exact local identities as automatic global conservation.
The disjoint control and unsplit exact flow keep the positive alternatives
visible.

**Gate result:** PASS for the exact one-bond theorem and the bounded
two-bond schedule fork. Six route families are executed, three enlarged routes
remain open, and no global energy no-go is asserted.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- the hard-cutoff shift violates `[E,U]=U`;
- a paired hop changes either endpoint Gauss value;
- the joint exponential is nonunitary or changes a Gauss generator;
- flux gain differs from head gain or negative tail gain;
- electric work differs from the anticommutator expression;
- hopping energy fails to lose the opposite work;
- either adjacent local Hamiltonian violates a shared Gauss generator;
- the palindromic product is not reversible or Gauss-preserving;
- the stated Lie and palindromic refinement orders fail;
- the unsplit flow changes the summed Hamiltonian;
- the principal Floquet generator is non-Hermitian or not conserved;
- its deviation or extra entries fail the quadratic ladder; or
- disjoint bonds fail the commuting exact-energy control.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_quantum_link_exact_backreaction_colored_floquet_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=23 FAIL=0
```

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A selected electromagnetic law, physical matter/field identification and Record preparation/readout remain open."
source_of_blocker_text: "review_loop"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Review the corrected conditional source and establish the missing physical consumer before claiming framework closure."
conditional_surface_status: "Supplied finite hard-cutoff flux link and one-particle matter Hamiltonian; exact one-bond work and Gauss, bounded adjacent/disjoint schedule tests, and principal Floquet branch; no full-lattice local logarithm, photon spectrum or physical energy selector is derived."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The result is a conditional mathematical theorem on supplied laws and finite domains; author status and a green runner grant no audit retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original source and receipts remain recoverable at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. The finite-block Gauss, current,
work and Floquet claims are preserved. Pairwise relations among the
outstanding physical tasks remain unresolved. All runner timeouts and final
input-bound receipts describe this corrected source. The source status and
trace above state the supplied premises and open physical bridge. Independent
review confirmation and integration validation remain separate; no audit
verdict or effective retained status is asserted.
