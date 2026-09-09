# Finite action/functional and typed Admissibility/Record identification decision

**Date:** 2026-09-02
**Type:** bounded_theorem
**Surface status:** conditional finite synthesis; global four-axiom model extension remains open
**Audit status:** unset
**TOE accounting:** zero obligation retirement and zero TOE-percentage movement

**Primary runner:** [exact finite checks](../scripts/finite_action_functional_typed_admissibility_record_identification_2026_09_02.py)
**Evidence:** [current source-bound cache](../logs/runner-cache/finite_action_functional_typed_admissibility_record_identification_2026_09_02.txt)
**Governing context:** [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
**History:** [original note](../.claude/science/physics-loops/functional-record-7852-correction-20260909/originals/docs/FINITE_ACTION_FUNCTIONAL_TYPED_ADMISSIBILITY_RECORD_IDENTIFICATION_DECISION_BOUNDED_THEOREM_NOTE_2026-09-02.md) and
[correction and complete recovery map](../.claude/science/physics-loops/functional-record-7852-correction-20260909/CORRECTION_HISTORY.md).

## Result

There is a useful positive closure and a decisive remaining separation.

The component mathematics is not claimed as new. The dated packet records
prior-art comparisons to August effect/menu notes and June/July writer notes.
Those comparisons and old PR/status observations are historical custody, not
proof suppliers or current acceptance of those campaigns. The finite matrix
and probability arguments used here are given below and recomputed directly.
This synthesis identifies supplied interfaces; it does not settle entailment
by every model of the four framework axioms.

A completely specified finite Gibbs action package does determine one unique
normalized positive functional. Once a finite effect partition and a matching
instrument are also supplied, its branch traces form a normalized probability
law and its normalized branches can carry the matching Record contents. That
commuting triangle is exact.

The following type distinctions and finite non-identification examples are
established on the displayed supplied domains:

1. `M_2(C)` is an operator algebra. Its density matrices, normalized positive
   functionals, effects, effect partitions, and classical probability measures
   over candidate state objects have different types.
2. One fixed state functional does not choose which effect partition is the
   registered physical question.
3. On the 64 binary neighbor configurations, two covariant conditional laws
   coexist with the same supplied action weights, and only one matches them.
   A full-domain four-axiom model realizing either law is not constructed.
4. Equal effect weights do not determine the post-outcome content unless a
   matching-output premise is supplied.
5. A conditional content law does not determine formation site, hazard/rate,
   cadence, or a physical permanence implementation.

This is local finite non-identification, not a full-framework independence
theorem or an impossibility result. It does not show that a new axiom is the
only repair. The owner options below remain unadopted proposals; a physical
construction could instead supply and justify the required interfaces.

## What can actually be observed

Only Records are read. The matrices, effects, unformed alternatives, and
probability weights below are model objects. Probabilities and supported
possibilities can be inferred from repeated Record contents only under a
supplied protocol that reproduces the neighboring condition, preparation,
registration and cadence, with a joint sampling law that justifies consistency.
IID independent-reset trials are a sufficient extra assumption (§8).
Stationarity alone is insufficient. No single
Record displays its probability, and no unrecorded branch is treated as a
direct observation.

## 1. The necessary type distinctions

Let `A=M_2(C)`. The following objects cannot be interchanged merely because
they admit matrix representations:

| Object | Exact type | Role |
|---|---|---|
| one-site observable algebra | `A` | algebraic presentation |
| quantum state | normalized positive functional `omega:A->C`, equivalently a density matrix `rho` | assigns affine effect weights |
| effect | `E in A`, `0 <= E <= I` | one possible registered event |
| finite event partition | effects `{E_a}` with `sum_a E_a=I` | one registered question/menu |
| classical possibility law | probability measure `nu` on a chosen possibility space | distribution over possibility objects |
| instrument branch | completely positive map `J_a` with `J_a^*(I)=E_a` | probability plus post-outcome state |
| Record content | one permanent readable local possibility | actual readable result |

The current Qubit axiom says that the full one-site possibility domain has
algebraic presentation `M_2(C)`. It does not say whether a possibility is an
arbitrary algebra element, a state, a pure ray, an effect-event, or a labelled
branch block. The framework's separate use of “state” for a configuration of
Records makes silent type identification especially unsafe.

## 2. Positive theorem: a complete finite Gibbs package selects a functional

Let `H=H*` be a finite Hermitian matrix, let `beta>0`, and declare that the
physical state semantics of this package is the normalized Gibbs functional.
Then

```text
rho_H = exp(-beta H) / Tr exp(-beta H),
omega_H(E) = Tr(rho_H E).                            (1)
```

The exponential is positive definite, its trace is positive, and therefore
`rho_H` is positive with unit trace. Equation (1) is consequently normalized
and positive. There is exactly one such `rho_H` under the displayed Gibbs
semantics because the matrix exponential and scalar normalization are unique.

For the exact runner family, let `n` count one-Records among six neighboring
binary Records and use the positive action-weight matrix

```text
W_n = diag(7-n, n+1),        n=0,...,6.
rho_n = W_n / Tr(W_n) = diag((7-n)/8, (n+1)/8).       (2)
```

Equivalently, `H_n=-log W_n` at `beta=1`. This avoids numerical
exponentiation and certifies (1) exactly over rational entries.

This closure is conditional on what “action package” means. A bare Hamiltonian
or action polynomial without a state/preparation, boundary, temperature, and
normalization prescription admits many normalized positive functionals. For
example, the same bare two-level Hamiltonian is compatible with both pure
states `Pz+` and `Px+`. Thus the `I-4` action-to-functional wall collapses in a
finite realization only when the physical action declaration includes the
normalized state/measure semantics; calling a formula an action is not enough.

## 3. A functional does not select the registered event partition

At `n=1`, (2) is

```text
rho = diag(3/4,1/4).
```

Both

```text
Z menu: {Pz+,Pz-} = {(I+Z)/2,(I-Z)/2},
X menu: {Px+,Px-} = {(I+X)/2,(I-X)/2}
```

are positive resolutions of the identity. Yet (1) gives

```text
p_Z=(3/4,1/4),             p_X=(1/2,1/2).            (3)
```

The same action-selected functional therefore supports distinct physical
questions with distinct distributions. Basis covariance says that equivalent
representations of one fixed event have the same probability; it does not say
that the `Z` event and the `X` event are the same event, nor does it select one.

Conditional on a registered effect resolution `{E_a}`, positivity and
normalization do force

```text
p(a)=omega_H(E_a)>=0,       sum_a p(a)=1.             (4)
```

Equation (4) is the finite Born form. The missing physical step is not its
algebra; it is which effects constitute the experiment and whether the
Admissibility distribution is identified with (4).

## 4. A distribution over states is not an effect functional

Consider two classical ensembles of density matrices:

```text
nu_Z = (1/2) delta_(Pz+) + (1/2) delta_(Pz-),
nu_X = (1/2) delta_(Px+) + (1/2) delta_(Px-).         (5)
```

They are different measures with different supports, but both have barycenter
`I/2`. Hence for every effect `E`,

```text
integral Tr(sigma E) d nu_Z(sigma)
 = Tr((I/2)E)
 = integral Tr(sigma E) d nu_X(sigma).               (6)
```

The barycenter map from classical state ensembles to effect functionals is
therefore non-injective. A measure over possible quantum states contains a
different kind of information from a state functional evaluated on effects.
One may deliberately connect them by (6), but the connection is a map/quotient,
not a type identity.

The converse ambiguity already appears on one binary menu. The two positive
functionals with density matrices `Px+` and `Px-` both assign `(1/2,1/2)` to
the `Z` menu, while they assign probabilities `1` and `0` to the effect `Px+`.
Thus agreement with an action law on one PVM does not determine a functional
on the full algebra.

Nor can menu-dependent event probabilities generally be reinterpreted as raw
singleton masses on one global space of matrix points. If all four distinct
projectors `Pz+`, `Pz-`, `Px+`, and `Px-` were assigned singleton weights that
separately normalized both two-outcome menus, finite additivity would give
total mass `2`. A registered partition, menu-indexed kernel, or effect-
functional descent is necessary; matrix-point identity is not enough.

There is also a positive collapse route. The six effects

```text
E_(+-a) = P_(+-a)/3,       a in {x,y,z},
```

sum to `I` and span the four-real-dimensional Hermitian part of `M_2(C)`. For
`rho=(I+r dot sigma)/2` in Bloch notation,

```text
p_(+-a)=(1+-r_a)/6,        r_a=3[p_(+a)-p_(-a)].      (7)
```

Consequently a physically registered informationally complete menu determines
the entire positive functional from its probabilities. “Functional” and
“outcome law” are not independent walls once that event interface is supplied.

## 5. Equal probabilities do not force matching Record content

For the `Z` menu, define two one-Kraus-per-outcome instruments. The matching
instrument uses

```text
K_+ = |0><0|,              K_- = |1><1|,
```

while the flipped-output instrument uses

```text
L_+ = |1><0|,              L_- = |0><1|.              (8)
```

Both have the same effects:

```text
K_a^* K_a = L_a^* L_a = Pz_a,
sum_a Pz_a=I.
```

They therefore have identical branch traces on every input. Their normalized
outputs are opposite: `K_a` prepares the state matching label `a`, whereas
`L_a` prepares the other state. This is not a failure of complete positivity;
all four maps have explicit Kraus forms.

If one additionally requires a rank-one PVM outcome to lock the matching
rank-one output, the branch becomes the Lüders/measure-and-prepare map

```text
J_a(rho)=Tr(Pz_a rho) Pz_a.
```

The historical packet compared this boundary to PR `#7831`; no proof or
current status from that PR is imported. The explicit Kraus calculations here
show why matching output is an additional supplied interface, rather than a
consequence of the effects alone.

## 6. Local finite law pair; full-model extension remains open

Fix a binary Record vocabulary, a registered `Z` menu, and the action weights
(2). On the 64 binary configurations of six recorded neighbors let `n` count
ones, and define

```text
mu_A(1|n)=(n+1)/8,          mu_A(0|n)=(7-n)/8,
mu_B(1|n)=(2n+1)/14,        mu_B(0|n)=(13-2n)/14.     (9)
```

Both laws have full support on this binary menu for `n=0,...,6`, normalize,
and vary with `n`. Depending only on the count makes them invariant under
proper cubic permutations of the six neighbor slots. Using the same rule at
each site gives translation covariance on this supplied restricted domain.

The action weights (2) on the `Z` menu equal `mu_A`, while `mu_B` differs:
at `n=0` their one-probabilities are `1/8` and `1/14`. Thus local normalization,
count covariance and this supplied action package do not force

```text
mu_eta(a) = omega_action,eta(E_eta,a).               (10)
```

This example does not construct a full-domain four-axiom model. In particular,
it does not extend the rule to arbitrary `M_2(C)` possibilities and all mixed
no-Record/Record neighbor conditions, or supply a compatible global formation
process without privileged possibilities. The fixed-condition one-site kernel
in §7 does not fill those gaps. Full-framework entailment or independence of
(10) therefore remains unestablished by this pair. No impossibility of such an
extension is claimed. Law `A` realizes (10) only on the displayed finite domain.

The memo's interpretive reading connects the Admissibility distribution to
content conditional on formation. We keep that current premise separate from
the supplied event map, action weights and local constructions here.

## 7. Formation and permanence remain separate

At the fixed recorded-neighbor condition `n=2`, `mu_A(1|n)=3/8`. A one-site process with formation hazard `h=1/3` and a process
with hazard `h=2/3` have the same conditional content law but different joint
one-Record probabilities, `1/8` and `1/4` per supplied opportunity. For independent hazard trials while the site is blank, each has survival
probability `(1-h)^k` after `k` supplied opportunities, hence forms almost
surely and has absorbing single-Record states. This is a local kernel, not a
global formation realization on the full possibility/neighbor domain. Conditional Admissibility weights do not select the
opportunity schedule, site, probability, or rate.

Likewise, the active Hamiltonian `H=X` does not preserve the `Z` Record
projector because `[X,Pz+] != 0`. A formation-triggered gate setting the
incident post-write Hamiltonian to zero, or a separate stable pointer carrier,
can preserve it. The Record axiom requires permanence; it does not select one
of these physical implementations.

## 8. Exact sufficient commuting triangle

For each neighboring condition `eta`, the following typed premises are
sufficient:

1. a fully specified finite action/state package derives a normalized positive
   functional `omega_eta`;
2. a physical registration supplies effects `{E_eta,a}` summing to `I`;
3. the physical identification (10) holds;
4. a normalized instrument has effect `E_eta,a` on branch `a` and its
   normalized output carries the matching Record possibility/label;
5. a formation allocation chooses when and where the conditional experiment
   occurs; and
6. post-formation dynamics preserves the Record content.

Then the one-use branch traces equal `mu_eta(a)` and the branches are
exhaustive. Those six premises alone do not imply consistent frequencies.

A sufficient seventh premise is a joint product protocol: each trial uses a
fresh carrier (or an auxiliary reset that does not erase a permanent Record),
the same preparation, neighbor condition and registered instrument, and an
independent draw. For a fixed event with probability `p`, the indicators
`X_1,...,X_m` are IID Bernoulli(`p`). For integer `m>=1` and `epsilon>0`, their empirical frequency `F_m` satisfies

```text
E[F_m]=p,    Var(F_m)=p(1-p)/m,
Pr(|F_m-p|>=epsilon) <= p(1-p)/(m epsilon^2).
```

The variance follows by summing independent indicator covariances, and the
last bound follows from Chebyshev's inequality. Thus the estimate is consistent
in probability. A separately supplied stationary ergodic joint process with
this marginal also gives almost-sure consistency by the ergodic theorem; no
physical ergodicity or reset implementation is derived here.

Stationarity alone is insufficient. Draw one `B~Bernoulli(1/4)` and set every
`X_i=B`. Each trial has the same marginal as `rho=diag(3/4,1/4)` measured in the
`Z` menu, but `F_m=B` and `Var(F_m)=3/16` for every `m`. This stationary,
perfectly correlated joint law obeys the one-use statistics and never
concentrates at `1/4`. The runner computes this contrast exactly at `m=4`:
IID variance `3/64`, correlated variance `3/16`. The general variance result
uses the displayed joint assumptions, not that finite check alone.

The dependency map is:

| Link | Status under current surface |
|---|---|
| complete finite Gibbs package -> positive functional | derived mathematics |
| bare action -> complete state package | open physical semantics |
| functional + supplied effects -> normalized Born weights | derived mathematics |
| physical event/menu registration | open unless supplied by an interaction/writer |
| action weights = Admissibility law | exact independent identification (10) |
| effect outcome -> matching Record content | open unless matching-output instrument supplied |
| Records form | axiom content |
| formation site/probability/rate | explicitly outside Admissibility content |
| Record permanence | axiom requirement |
| physical persistence mechanism | explicitly outside axiom content |
| frequency consistency | additional IID/reset or stated ergodic joint law |

The calculation therefore collapses part of the old `I-4` slogan but does not
retire the full physical bridge.

There is an equally valid direct classical factorization if Admissibility is
kept as a measure `mu_eta` on a possibility space: a physically registered
measurable partition `{A_eta,a}` gives
`p(a|eta,formation)=mu_eta(A_eta,a)` without first constructing an effect
functional. That route still needs the physical partition and its Record-
content interpretation. The effect-functional route is needed when the program
also requires consistent probabilities across quantum effect menus.

## 9. Owner decision surface — no axiom edit performed

Three non-equivalent options are now sharp.

### Option A — state-space clarification only

Candidate exact clarification:

> In Qubit and Admissibility, the algebra `M_2(C)` presents the local quantum
> system. A “possible local quantum state” is a normalized positive functional
> on that algebra (equivalently a density matrix), and a probability
> distribution over such possibilities is a measure on that state space.

This resolves the algebra/state type ambiguity. It does **not** derive effect
event probabilities, select a registered question, or close (10).

### Option B — registered-effect probability semantics

Candidate substantive clause:

> For each neighboring condition `eta` and each physically registered finite
> local effect resolution `{E_eta,a}` with `sum_a E_eta,a=I`, Admissibility is a
> normalized positive functional `omega_eta` on `M_2(C)` and assigns the event
> probabilities `mu_eta(a)=omega_eta(E_eta,a)`. Conditional on formation for
> that registration, Record locks content carrying the matching label `a`.

This closes the typed probability/outcome triangle conditional on a physical
registration. It adds real structure: effect events, functional positivity,
and the matching-label link. It still does not select the registration, action,
formation allocation, clock, or persistence mechanism.

### Option C — keep axioms minimal and require a downstream bridge

Adopt no axiom change. A candidate action closes this seam only when it proves
all three of: a complete physical state functional, a registered event map, and
identity (10), followed by a matching Record instrument. This is the most
conservative reading but leaves the TOE lane conditional until such a physical
construction is established within its stated domain.

Only the owner can decide whether the existing words were intended to carry
Option A or B. This note records candidates; it changes no canonical memo.

## 10. Boundary discipline for the local finite result

### N1 — alternative route enumeration

| Route | Status | Result |
|---|---|---|
| fully normalized finite Gibbs/Euclidean measure | attempted | selects a unique functional; positive partial closure |
| bare Hamiltonian/action polynomial | attempted | does not select preparation/state semantics |
| POVM additivity / Busch-Gleason route | prior exact mathematics | forces trace form after registered effects and additivity; does not select registration or (10) |
| state-ensemble barycenter | attempted | supplies an effect functional non-injectively; does not identify the physical ensemble |
| controlled-copy or Lüders writer | prior/open-PR construction | closes an instrument after measurement/output premises are supplied |
| interaction-selected stable pointer sectors | open positive route | could derive registration and matching content in one concrete model |
| repeated-Record tomography | open empirical route | can estimate an implemented law; does not derive which law is fundamental |
| owner-approved typed axiom interpretation | open governance route | could make intended probability semantics explicit |

### N2 — finite separation witnesses

| Wall pair | Exact witness |
|---|---|
| action formula vs state functional | same bare `H`, distinct positive states |
| state functional vs event registration | same `rho`, `Z` and `X` menus in (3) |
| action/event weights vs Admissibility identity | same action/menu, laws `mu_A` and `mu_B` in (9) |
| effects vs Record output | instruments `K` and `L` in (8) |
| conditional content vs formation allocation | hazards `1/3` and `2/3` |
| permanent Record requirement vs implementation | active `[X,Pz+] != 0` versus gated dynamics |

These exhibits separate the choices only on their stated supplied finite
surfaces. They do not establish independence in all complete framework models
or assert that Nature chooses the objects independently.

### N3 — hidden-wall scan

The words “action,” “state,” “possibility,” “event,” and “outcome” can hide a
preparation/boundary condition, temperature, normalization, basis/menu,
physical registration, conditional-versus-unconditional probability,
formation schedule, clock, pointer carrier, and post-write gate. All are kept
visible here.

### N4 — residual matching

The terminal probability residual is equation (10), together with a typed event
registration. The matching-content residual is the instrument output premise.
Formation allocation and persistence dynamics are separate downstream
residuals. “Born rule missing” or “measurement missing” is too coarse.

### N5 — rhetoric and resolution audit

Permitted conclusion: the displayed local finite data do not force the
joined typed identification. Full-domain four-axiom independence is open. Forbidden conclusions include “quantum
probabilities cannot be derived,” “Record physics is impossible,” “a new axiom
is necessary,” or “all action routes fail.” The runner emits an explicit N5
scope line and all five resolution levels. Phrase guards check publication
consistency only; they are not mathematical proofs or audit verdicts.

### N6 — partial-closure path scan

The conditional positives are preserved: complete finite Gibbs semantics closes the
functional subwall; a registered POVM closes normalization; matching rank-one
output closes the one-site Lüders branch; a gate or stable pointer can satisfy
permanence. None is erased by the finite separation examples.

### N7 — strongest steelman

The strongest friendly reading joins the Admissibility reading note to Record:
the axiom already intends a law over quantum alternatives, conditional on
formation, and Record locks the sampled alternative. If “physical action” is
defined to include its normalized measure and if “possibility” already means a
registered branch/event, then (10) can be a semantic identity rather than a new
dynamical law. That reading is coherent, and law `A` realizes the equality locally. A full
realization of either law would still have to supply the domain extension and
formation conditions in §6. Law `B` is not claimed to satisfy all governing
sentences on their full domains.

### N8 — cross-cycle echo

The original packet compared these examples to August effect/carrier, menu,
barycenter and formation notes, PRs `#7830`/`#7831`, and Blocks 46/47. Those
comparisons, statuses and earlier claims are preserved as dated history. No
parent campaign is accepted or needed for the explicit calculations here.
The present scope correction supersedes the old full-axiom countermodel label.

## Claim custody

This is a bounded conditional synthesis of the displayed finite examples,
interpreted against the linked current memo. Historical source notes and ledger
status are not used as proof authority. No audit verdict, canonical axiom change,
approved primitive, action selection, formation rate, obligation retirement,
or TOE score change is claimed.

The original novelty failure, no-PR decision, ten-check cache and 32-mutation
claim remain unchanged in the dated history. They describe the old checkpoint;
they do not control the current owner-authorized correction and review.
The corrected cache is a fresh execution, not a restamp of those old receipts.
Formal audit is deferred; no current scientific status follows from history.

No canonical axiom text will be changed without an explicit owner decision on
exact wording.
