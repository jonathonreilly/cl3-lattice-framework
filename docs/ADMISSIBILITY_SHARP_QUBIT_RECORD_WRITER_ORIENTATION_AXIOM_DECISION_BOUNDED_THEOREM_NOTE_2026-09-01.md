---
claim_id: admissibility_sharp_qubit_record_writer_orientation_axiom_decision_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
runner: scripts/admissibility_sharp_writer_orientation_axiom_decision_2026_09_01.py
runner_cache: logs/runner-cache/admissibility_sharp_writer_orientation_axiom_decision_2026_09_01.txt
actual_current_surface_status: bounded-support
target_claim_id: Block37_W1_law_parameter_selection
authority: none
audit_required_before_effective_retained: true
---

# Sharp qubit Record writer and the remaining orientation decision

**Date:** 2026-09-01

## Result in one paragraph

Exact same-label repeatability of a nontrivial two-outcome qubit CP instrument
with the displayed effects forces its reduced one-qubit instrument to be
rank-one projective. This removes the continuous
Block-38 response ambiguity: `|lambda|=1`. It does not choose the global
orientation of an otherwise untyped binary label. The Born-oriented and
anti-oriented instruments have the same unconditional channel, exact repeat
behavior, and fixed externally scheduled post-first label-transition kernel.
They are **not** twins on the literal Block-38 typed carrier: that carrier fixes
the Record direction `n=b a` and its faithful successor as `rho_n`, whereas the
anti-oriented endpoint outputs `rho_-n`. An independently oriented preparation
or a support-faithful Record-to-quantum-event calibration therefore separates
them immediately. The current four axioms supply neither that calibration nor
affinity of the probabilities *conditional on formation*, so the honest result is expected to be
an axiom/bridge decision inventory, not W1 retirement. Exact repeatability is
also a named conditional physical premise; Record permanence does not supply
it.

## Source and premise boundary (2026-09-07 correction)

The primary runner is
[`scripts/admissibility_sharp_writer_orientation_axiom_decision_2026_09_01.py`](../scripts/admissibility_sharp_writer_orientation_axiom_decision_2026_09_01.py);
its current output is [the paired cache](../logs/runner-cache/admissibility_sharp_writer_orientation_axiom_decision_2026_09_01.txt).
The [governing minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.
The [Block-38 typed compiler](../archive/notes/docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md)
supplies the conditional attachment and finite comparison used here; the runner
actually loads its B38 helper and that helper's B37 Gaussian/Haar routines.
Only this used closure is exercised, not either parent campaign or its status.
The July Cycle-20 comparator is read at its exact archived path; its original
path and Git blob remain historical pins. Its former scalar-additivity premise
is dated comparison material, not current Record authority.
The [dated correction overlay](../.claude/science/review-fixes/blocks42-43-20260907/CORRECTION.md)
qualifies the unchanged historical packets. This note and its proposed memo
state extra conditional hypotheses; neither registers or approves a primitive.

## 1. General repeatability theorem

Let `I_{a,b}` be a trace-nonincreasing CP map on one qubit and let

```text
Tr[I_{a,b}(rho)] = Tr[E_b^lambda(a) rho],
E_b^lambda(a) = (I + b lambda a.sigma)/2,
```

where `|a|=1`, `b` is `+1` or `-1`, and `|lambda|<=1`. Normalization is
`E_+ + E_- = I`.

Exact same-label repeatability under a causally independent second use is

```text
Tr[(I-E_b) I_{a,b}(rho)] = 0
```

for every positive input and every nonzero first branch. Although the product
inside the first trace need not itself be positive, cyclicity gives, for the
positive branch output `tau=I_{a,b}(rho)`,

```text
Tr[(I-E_b) tau]
  = Tr[tau^(1/2) (I-E_b) tau^(1/2)] = 0.
```

The middle operator is positive, so it vanishes. Hence each branch output is
supported in the kernel of `I-E_b`, the eigenvalue-one subspace of `E_b`.

For `|lambda|<1`, both eigenvalues `(1+lambda)/2` and `(1-lambda)/2` are
strictly below one. No nonzero branch can then be repeatable, contradicting its
nonzero effect. Therefore

```text
|lambda| = 1.
```

Write the surviving orientation as `epsilon=lambda` in `{+1,-1}`. Then

```text
E_b^epsilon(a) = P_(epsilon b)(a).
```

The allowed output support is one-dimensional. Positivity makes every output
a nonnegative multiple of `P_(epsilon b)`, and the defining branch trace fixes
that multiple. Thus the reduced one-qubit instrument is unique:

```text
I^epsilon_{a,b}(rho)
  = Tr[P_(epsilon b)(a) rho] P_(epsilon b)(a).
```

No Lüders rule, pure poststate, or Block-38 `kappa` value was assumed. They are
consequences at the two sharp endpoints for the reduced map; microscopic
dilations, apparatuses, and generators are not unique.

The July-11 covariant-effect/repeat-certainty theorem reached the same
projective map after importing the rank-one locked-output normal form
`J_i(rho)=Tr(E_i rho)P_i`. The marginal theorem here is narrower than a new
Born derivation but genuinely stronger at that point: branch support and the
unique rank-one output map are derived from repeatability for the general CP
instrument with the displayed binary effects, rather than assumed before the
collapse.

## 2. The exact orientation quotient

The two endpoint instruments are physically sharp but sign-dual. Summing over
labels gives the same dephasing channel:

```text
sum_b I^+_{a,b}(rho) = sum_b I^-_{a,b}(rho).
```

After the first branch, an arbitrary sequence of axes has joint law

```text
Pr_epsilon(b1,...,bN | s)
 = [1 + epsilon b1 a1.s]/2
   product_(j=1)^(N-1) [1 + b_j b_(j+1) a_j.a_(j+1)]/2.
```

For an axis schedule fixed independently of the branch outputs, every later
*label-transition probability* is independent of `epsilon`. Same-axis
repetition is exact for both signs. A global relabeling `b -> -b` identifies
the abstract instruments if the labels and their downstream codec are purely
conventional.

The literal Block-38 Record carrier is stronger than an unlabelled binary port:
it fixes the direction `n=b a` and the record-faithful successor attachment
`M=rho_n`. The `epsilon=-1` instrument instead outputs `rho_-n`; inherited
full `F/M/B2` transcripts therefore separate the endpoints and the anti-
oriented endpoint fails that typed attachment. An aligned preparation gives
the same discriminator:

```text
rho_a under epsilon=+1 gives Record n=+a with certainty;
rho_a under epsilon=-1 gives Record n=-a with certainty.
```

Calling the first orientation “matching” is not a derivation from the four
axioms. It is exactly the additional physical typing carried conditionally by
Block 38. A global codec/generator conjugacy that flips `n` could restore a
quotient only if that conjugacy were separately constructed and proved to
preserve every adaptive schedule and collision; none is supplied here.

## 3. Why current axioms do not orient the writer

The current Admissibility axiom requires one fixed nearest-neighbor-conditioned
probability distribution, but deliberately leaves its form and values open.
The Record axiom says a Record locks one admissible possibility and remains
readable; it does not assert operational repeatability or a preparation/event
calibration.

On the **conditional Block-38 surface**, the answer is already sharper than on
the four axioms alone. Its stipulated typed attachment `F:n=b a -> M:rho_n`
fixes the successor orientation `kappa=+1`; adding exact independent
same-kernel repeatability then forces `lambda=+1`. The anti endpoint reappears
only after relaxing that attachment to `M=rho_(-n)`. Block 42 must not report
this conditional selection as a new consequence of the minimal axioms.

The family

```text
T_s^lambda(dn) = (1 + lambda n.s) mu(dn),
lambda in [-1,1],
```

is normalized, nonnegative, covariant, and neighbor-dependent for every
nonzero `lambda`; the stacked Block-36/38 constructions supply corresponding
conditional finite histories and CP instruments. In particular `lambda=1`
and `lambda=1/2` are supplied normalized local candidate laws with differing
finite response data:

```text
E_lambda[n] = lambda s/3,
Pr(mismatch | kappa=1) = (1-lambda)/2.
```

This is finite candidate-law nonselection by the displayed local data. No
global formation schedule, covariant role law, or complete model of all four
axioms is constructed here. It is not a universal no-go for physical or
empirical law selection.

## 4. Calibration, conditional affinity, and the formation-bias trap

The narrow candidate clause is:

> **Support-faithful quantum-event calibration.** For every registered binary
> rank-one projective ideal context `C=(P,Q)`, `Q=I-P`, fix the exhaustive Record
> events `R_P,R_Q` and their Record-to-block coding independently of the
> response probabilities. Require `Pr(F|C,rho)>0` for every qubit density
> matrix `rho`, including BOTH endpoints `rho=P` and `rho=Q`. The normalized
> conditional response is defined on this entire state space. Exactly one of
> `R_P,R_Q` occurs given `F`. At `rho=P`, `Pr(R_P|F,C,P)=1`, and likewise
> `Pr(R_Q|F,C,Q)=1` at `rho=Q`.

Full-domain positive formation is an additional ideal-context hypothesis,
not a consequence of the current axioms or a rule for arbitrary heralded
processes. In particular both endpoint calibrations must be nonvacuous.

For an aligned pure possibility and event, the affine response gives

```text
1 = Pr(+ | a,a) = (1+lambda)/2,
```

so the clause selects `lambda=+1` inside the affine/covariant class.

The clause alone is strictly weaker than the Born trace law. For example, with
`0<delta<=1/4`, define

```text
g_delta(u) = u + delta u(1-u^2),
p_delta(b|u) = [1 + b g_delta(u)]/2.
```

`g_delta` is odd, maps `[-1,1]` into itself, and has
`g_delta(+1)=+1`, `g_delta(-1)=-1`; hence the response is normalized,
nonnegative, covariant, and support-calibrated. Its nonzero cubic term violates
preparation affinity. Calibration fixes the endpoint orientation, while
physical-preparation equivalence/affinity fixes the linear form. Both logical
jobs must remain visible.

Ordinary additivity of probabilities over disjoint Record events is not
conditional preparation affinity. The former compares events under one
condition; the latter compares conditional Record distributions generated by
operationally equivalent preparation procedures or convex possibility
representatives.

A vague statement that a convex randomizer “represents the mixed possibility”
is still insufficient because this framework conditions content probabilities
on Record formation. Let `x=Tr(P rho)` and define affine joint probabilities

```text
Pr(F | rho)       = f(rho)   = (1+x)/2,
Pr(F and R_P|rho) = h_P(rho) = x,
Pr(F and R_Q|rho) = h_Q(rho) = (1-x)/2.
```

They are nonnegative, normalized by `h_P+h_Q=f`, preparation-noncontextual,
and affine before conditioning. They are also support calibrated at `rho=P`
and `rho=Q`. Nevertheless

```text
Pr(R_P | F,rho) = h_P(rho)/f(rho) = 2x/(1+x),
```

which is nonlinear and non-Born. Formation has reweighted the preparation
branches. The needed consistency condition must therefore be explicit:

```text
q_P(p rho_0+(1-p)rho_1 | F)
  = p q_P(rho_0|F) + (1-p) q_P(rho_1|F)
```

for every fixed registered ideal context, every pair of qubit density matrices
`rho_0,rho_1`, and `0<=p<=1`, on the full positive-formation domain just
specified. Operationally equivalent direct and recorded-randomized
preparations of the same density possibility must have the same conditional
content law. Equal formation rates on the randomizer branches are a sufficient
apparatus certificate in an affine joint-effect model, but are not equivalent
to this clause in complete generality and are not imposed on arbitrary
heralded processes.

The full-domain requirement cannot be replaced by “wherever defined.” Two
exact counterexamples to that weaker wording survive conditional affinity:

- `f=4x(1-x)`, `h_P=h_Q=f/2` is label-swap symmetric with constant
  `q_P=1/2` on `0<x<1`; both calibration endpoints have zero formation.
  At `x=1/4` its conditional value is `1/2`, not the Born value `1/4`.
- `f=1-x`, `h_P=0`, `h_Q=1-x` even has affine joint weights. The `Q`
  endpoint is calibrated, but the `P` endpoint never forms; at `x=1/2`,
  `q_P=0`, not `1/2`.

The corrected positive-formation hypothesis rejects both witnesses. The
runner checks those necessary endpoint failures explicitly; such finite checks
do not certify positive formation for every density matrix in a new apparatus.

Full-domain conditional affinity, positive formation, and support calibration
give a short direct theorem for each
registered one-qubit binary rank-one PVM `{P,I-P}`. Any affine probability on
the density matrices is `q_P(rho)=Tr(E_P rho)` for a unique effect
`0<=E_P<=I`. Calibration gives `Tr(E_P P)=1` and
`Tr(E_P(I-P))=0`; positivity of `E_P` and `I-E_P` kills both off-diagonal
entries in the `P/(I-P)` basis, hence `E_P=P`. Therefore

```text
q_P(rho)=Tr(P rho).
```

This probability theorem needs neither proper-cubic covariance nor the CP
repeatability premise. It does not derive a state-update instrument.

Accordingly there are two different closure packages, not one hidden premise:

```text
positive formation on all density matrices + full-domain conditional content affinity
    + support calibration at both eligible endpoints
    -> binary-projective Born probabilities;

exact operational repeatability + independently oriented Record/state coding
    -> sharp reduced CP instrument.
```

Neither package follows from the current four axioms.

There is also a broader, logically different route already present in the
repository. The June-05 Busch/CFMR qubit effect-Gleason note reproves that a
normalized POVM-additive functional on *all* `M_2(C)` effects must have trace
form. Its current audit-ledger status is `unaudited`, and its hypotheses do not
by themselves say that a quantum effect is a measurable Record event or that
its representing density operator is the prepared local possibility. It is
therefore a useful mathematical comparator, not a substitute for the missing
Record-to-quantum-event bridge. The binary-projective route proved here asks
for less event structure and reaches a correspondingly narrower result.

## 5. Record evidence and the SPAM boundary

One use with fixed known pure preparation `s`, Haar axis `a`, and `n=b a`
has `Y=3 s.n`, `E[Y]=lambda` and `Var(Y)=3-lambda^2`. These marginal
moments alone do not specify a repeated-trial law.

For the following product likelihood, additionally assume that at each trial,
conditional on the full past and the exogenous fixed preparation/axis design,
the label law is `[1+b_i lambda (a_i.s_i)]/2`. This is a supplied fresh-reset
conditional-kernel premise, not Record permanence or one-use calibration.
Under that premise, the conditional log likelihood is

```text
ell(lambda) = sum_i log([1+b_i lambda (a_i.s_i)]/2).
```

For independent fresh uses with fixed known pure preparation `s`, independent
Haar axes, fresh conditional labels, and `n_i=b_i a_i`,

```text
lambda_hat = 3 s . mean_i(n_i),
E[lambda_hat] = lambda,
Var(lambda_hat) = (3-lambda^2)/N.
```

Without trusted preparation magnitude/orientation, this arm identifies only
the product `lambda s`. In a repeat arm, mismatch probability is

```text
q = (1-lambda kappa)/2,
```

so it identifies only `lambda kappa` without an independent poststate
calibration. This is the exact state-preparation-and-measurement gauge; decoding
the poststate with the candidate law itself would be circular.

With a separately established ideal `kappa=1`, one mismatch falsifies exact
`lambda=1`. Conversely, an all-match corpus of any finite size has positive
probability `[(1+lambda)/2]^N` under every `lambda>-1` **under the repeat
arm's fresh-reset product conditional kernel**; this finite product-model
corpus never deductively proves the endpoint. Almost-sure recovery and concentration require separately
declared reset/freshness, recurrence, candidate-class, and typicality premises.

Two correlated counterexamples retain the one-use laws but invalidate an
unqualified product inference. At `lambda=0`, draw one Haar axis/label pair
and copy it into two trials: `Var(mean(Y_1,Y_2))=3`, whereas independent
uses give `3/2`. In general the variance includes
`2 sum_(i<j) Cov(Y_i,Y_j)/N^2` in addition to `(3-lambda^2)/N`.
For the repeat arm, draw one match bit with probability `3/4` and copy it:
two all-matches have probability `3/4`, not `(3/4)^2=9/16`. The runner
executes both witnesses. They are joint-law controls, not empirical data or
counterexamples to a certified fresh-reset experiment.

No qualifying non-synthetic Block-38 corpus or independent `kappa`
calibration is present in the repository. Runner-generated samples, if any,
are test vectors and not empirical evidence.

A noncircular Record-only test must permanently record the context and fixed
codec, trial eligibility/identifier, randomizer branch and preparation
certificate, `R_P/R_Q` when formation occurs, and a timed close/no-formation
Record `N` on an external trial controller, plus reset/freshness certificates.
Absence at the target site is not itself readable. The formation-bias
countermodel predicts eigenpreparation efficiencies `1` and `1/2`, and at the
50/50 mixture predicts conditional `q_P=2/3` instead of the affine value
`1/2`. Finite data can bound or falsify the exact clauses but cannot prove
them deductively; coarse-reading a branch means marginalizing its permanent
Record, never erasing it.

## 6. Exact decision for the axioms

The result leaves three coherent owner choices.

1. **No foundation change.** Keep the complete response family as candidate
   law data and let a future calibrated Record corpus or microscopic writer
   select it. W1 remains open.
2. **Narrow orientation calibration.** Register only support-faithful quantum-event
   calibration with nonvacuous positive formation at both eigenpreparations. This selects the sign within an already-supplied affine
   response class, but nonlinear endpoint-calibrated laws still survive and no
   CP update/repeat law is thereby derived.
3. **Scoped binary-projective calibration primitive.** Register explicit
   positive formation on every qubit density matrix, affinity of the full-domain
   conditional content probabilities, and support-faithful event calibration in a narrowly named, owner-approved
   primitive consumed only by quantum Record/Born claims. The direct effect
   lemma above then gives the Born-oriented one-qubit binary-projective
   probability law without writing the trace formula into the premise.
   Extension to arbitrary effects or higher-dimensional event menus is not
   proved here. This probability result does not by itself derive the sharp CP
   writer; exact operational repeatability or a microscopic formation/update
   theorem remains a separate premise for that instrument conclusion.

A fourth, stronger policy choice would register noncontextual normalized
POVM-effect additivity and an explicit Record/effect identification, then use
the existing effect-Gleason representation theorem. That would cover arbitrary
one-qubit effects, but it assumes more event structure than the two narrow
sentences above and is not silently bundled into this decision.

The third choice is the cleanest if the intended ontology is that possibilities
are quantum-state alternatives and Records are calibrated samples of those
events. It is still a physics postulate, not something forced by permanence
alone. Placing it in a scoped approved primitive is more precise than amending
Admissibility globally: the September-01 historical inventory recorded 539 direct and
2,218 transitive consumers of `minimal_axioms`, and a global edit would trigger a broad premise-
hash re-audit while also overgeneralizing ideal detector behavior.

## 7. Scope and TOE accounting

This block may derive sharpness and isolate one orientation datum. It does not
derive formation site/rate, an actual experimental corpus, typicality, a total
multi-front process, source normalization, gravity response, or a complete
law of Nature. It does not select an absolute clock rate.

The following September-01 decision/shipping labels are preserved as historical
proposal accounting, not a current merge prohibition or an applied audit. No
owner adoption or separate derivation of exact repeatability is asserted:

```text
axiom_decision_status: AXIOM_DECISION_READY
hard_impact_gate: FAIL
shipping_decision: BACKLOG_NO_PR
audit_status: unset
obligation_retirement: 0
toe_percentage_movement: 0
retained_positive_end_to_end_theory: 0
```

No audit verdict is claimed. A proposed axiom sentence is not governing
content and does not by itself retire W1.
