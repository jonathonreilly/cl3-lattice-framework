# Finite action/functional and typed Admissibility/Record identification decision

**Date:** 2026-09-02
**Claim type:** bounded synthesis/decision with exact recomputed witnesses
**Surface status:** conditional support; current-axiom entailment fails on an
explicit finite model pair
**Audit status:** unset
**TOE accounting:** zero obligation retirement and zero TOE-percentage movement

## Result

There is a useful positive closure and a decisive remaining separation.

The component mathematics is not claimed as new. The August 10 global-
measure/menu note already owns the raw type separation, the August 12 note
owns barycenter evaluation, and the June/July Record notes plus open PR
`#7831` own the relevant finite writer forms. This artifact's role is to join
those boundaries to a finite action package, test literal current-axiom
entailment, and expose the exact owner decision. Its scientific novelty/value
gate is assessed separately and does not pass merely because the synthesis is
clearer.

A completely specified finite Gibbs action package does determine one unique
normalized positive functional. Once a finite effect partition and a matching
instrument are also supplied, its branch traces form a normalized probability
law and its normalized branches can carry the matching Record contents. That
commuting triangle is exact.

The current four axioms do not, by themselves, identify all of those objects.
In particular:

1. `M_2(C)` is an operator algebra. Its density matrices, normalized positive
   functionals, effects, effect partitions, and classical probability measures
   over candidate state objects have different types.
2. One fixed state functional does not choose which effect partition is the
   registered physical question.
3. The literal Admissibility distribution can differ from the action-induced
   effect weights while all four axioms and the same downstream action package
   are kept fixed.
4. Equal effect weights do not determine the post-outcome content unless a
   matching-output premise is supplied.
5. A conditional content law does not determine formation site, hazard/rate,
   cadence, or a physical permanence implementation.

This is a narrow entailment result, not a claim that an end-to-end physical
model is impossible and not a claim that a new axiom is the only repair. The
most important program decision is now explicit: either record an owner-
approved typed interpretation that identifies Admissibility with registered
quantum event probabilities, or require each candidate physical action to
prove that identification as a downstream bridge.

## What can actually be observed

Only Records are read. The matrices, effects, unformed alternatives, and
probability weights below are model objects. Probabilities and supported
possibilities can be inferred from repeated Record contents only under a
supplied protocol that reproduces the neighboring condition, preparation,
registration, cadence, and sampling/stationarity assumptions. No single
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

That is the premise boundary sharpened in open PR `#7831`. The present result
does not duplicate its one-site theorem; it shows why the matching-output
premise is part of the physical Record identification rather than a consequence
of the effects alone.

## 6. Decisive current-axiom model pair

The following pair holds the lattice, one-site algebra, downstream action
weights (2), registered `Z` menu, and Record vocabulary fixed. In each theory
there is one translation- and proper-cubic-covariant nearest-neighbor rule. Let
`n` be the invariant count of neighboring one-Records and define

```text
mu_A(1|n)=(n+1)/8,          mu_A(0|n)=(7-n)/8,
mu_B(1|n)=(2n+1)/14,        mu_B(0|n)=(13-2n)/14.     (9)
```

Both laws have full support for `n=0,...,6`, are normalized, and vary with the
neighbor condition. Records can form, sample the selected law conditional on
formation, lock `Pz+` or `Pz-`, remain unique per site, and be permanent. Thus
each is a model of the literal four axioms.

The action functional from (2), evaluated on the registered `Z` menu, equals
`mu_A`. It does not equal `mu_B`; for example the one-probabilities at `n=0`
are `1/8` and `1/14`. Since the same action package and the same literal axiom
text coexist with either law, the current axioms do not entail

```text
mu_eta(a) = omega_action,eta(E_eta,a).               (10)
```

This is a countermodel to entailment only. Adding (10) as a physical bridge is
consistent with the axioms, and model `A` explicitly realizes it.

The explicitly non-governing reading note in Admissibility says that its
distribution concerns which possibility a forming Record locks. That is strong
evidence for the friendly intended semantics, but it does not type an effect
partition or name equality (10) in the governing axiom sentences.

## 7. Formation and permanence remain separate

At `n=2`, `mu_A(1|n)=3/8`. A process with formation hazard `h=1/3` and a process
with hazard `h=2/3` have the same conditional content law but different joint
one-Record probabilities, `1/8` and `1/4` per supplied opportunity. Both can
form almost surely over an indefinitely repeated schedule and keep at most one
permanent Record at a site. Conditional Admissibility weights do not select the
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

Then branch traces equal `mu_eta(a)`, the branches are exhaustive, and repeated
matched Record experiments estimate those probabilities. The dependency map
is:

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
construction is retained.

Only the owner can decide whether the existing words were intended to carry
Option A or B. This note records candidates; it changes no canonical memo.

## 10. No-go discipline for the narrow entailment result

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

### N2 — wall-independence audit

| Wall pair | Exact witness |
|---|---|
| action formula vs state functional | same bare `H`, distinct positive states |
| state functional vs event registration | same `rho`, `Z` and `X` menus in (3) |
| action/event weights vs Admissibility identity | same action/menu, laws `mu_A` and `mu_B` in (9) |
| effects vs Record output | instruments `K` and `L` in (8) |
| conditional content vs formation allocation | hazards `1/3` and `2/3` |
| permanent Record requirement vs implementation | active `[X,Pz+] != 0` versus gated dynamics |

These exhibits establish logical independence on the stated finite surface.
They do not assert that Nature chooses the objects independently.

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

Permitted conclusion: the literal current axioms do not entail the joined
typed identification in every model. Forbidden conclusions include “quantum
probabilities cannot be derived,” “Record physics is impossible,” “a new axiom
is necessary,” or “all action routes fail.” The runner emits an explicit N5
line and all five resolution levels.

### N6 — partial-closure path scan

Retained positives are preserved: complete finite Gibbs semantics closes the
functional subwall; a registered POVM closes normalization; matching rank-one
output closes the one-site Lüders branch; a gate or stable pointer can satisfy
permanence. None is erased by the entailment countermodel.

### N7 — strongest steelman

The strongest friendly reading joins the Admissibility reading note to Record:
the axiom already intends a law over quantum alternatives, conditional on
formation, and Record locks the sampled alternative. If “physical action” is
defined to include its normalized measure and if “possibility” already means a
registered branch/event, then (10) can be a semantic identity rather than a new
dynamical law. That reading is coherent and model `A` realizes it. The exact
problem is that the governing text does not currently type those identifications,
so hostile model `B` also satisfies its literal sentences.

### N8 — cross-cycle echo

The result agrees with, but does not promote, the unaudited August effect-
carrier, global-measure/menu, barycenter, and formation-site notes. It also
explains the remaining hypotheses in open PRs `#7830` and `#7831`. Block 46/47
showed that concrete local Record probabilities and discriminators exist; this
block explains why those successes did not identify the physical law or move a
TOE lane.

## Claim custody

This is a bounded exact decision artifact on the frozen finite examples and
literal current axiom surface. The cited source notes are unaudited and are not
used as retained authorities. No audit verdict, canonical axiom change,
approved primitive, action selection, formation rate, obligation retirement,
or TOE score change is claimed.

The standard component lemmas and their one-step composition fail the hard
scientific-novelty gate. This note is retained only as a portfolio/owner-
decision checkpoint and is not proposed for a PR.

No canonical axiom text will be changed without an explicit owner decision on
exact wording.
