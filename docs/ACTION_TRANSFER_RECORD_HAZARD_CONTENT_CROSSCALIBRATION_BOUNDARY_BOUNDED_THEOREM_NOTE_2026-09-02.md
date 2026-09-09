---
claim_id: action_transfer_record_hazard_content_crosscalibration_boundary_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "For a positive qubit transfer W, gamma_*>0, and a normalized zero-first-moment Record-event measure, a supplied linear trace-flux rule gives marked intensity q(n)=gamma_* Tr(WP_n) and total hazard Gamma=gamma_* Tr(W)/2. A tomographically spanning menu is additionally required to infer a unique neutral first-opportunity input, and an isotropic second moment is additionally required to identify the conditional Bloch vector from its mean. Relative to an isotropic baseline, constant determinant is equivalent to Gamma/Gamma_0=(1-|r|^2)^(-1/2). Two supplied stopped-process architectures sharing that parametrization are separated: for nonscalar W a same-qubit action-weighted Kraus process has no-jump filtering and non-exponential survival, whereas scalar W is an exact exponential null case; a one-level orthogonal blank/Record direct sum has exponential survival and an absorbing full Record operator sector. Their two-site races differ at W_1=I, W_2=diag(2,1/2): 1/2 versus 4/9. The action, trace-flux identification, carrier/stop/history law, common positive rate multiplier, composite Record typing, and empirical corpus remain supplied; current axioms do not select the candidate, and no action-to-hazard obligation is retired."
upstream_dependencies:
  - minimal_axioms
runner: scripts/action_transfer_record_hazard_crosscal_2026_09_02.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
audit_status: unset
obligation_retirement: 0
toe_percentage_movement: 0
---

# Action-transfer Record hazard/content cross-calibration and the microscopic architecture fork

**Date:** 2026-09-02

**Claim type:** bounded_theorem

**Role:** conditional physical-law discriminator

**Audit status:** unset; independent audit is a separate lane

**Correction record:**
[`PR #7837 correction history`](../.claude/science/physics-loops/action-transfer-7837-correction-20260909/REVIEW_HISTORY.md)

**Current premise boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Primary runner:**
[`scripts/action_transfer_record_hazard_crosscal_2026_09_02.py`](../scripts/action_transfer_record_hazard_crosscal_2026_09_02.py)

**Independent helper runner:**
[`scripts/independent_action_transfer_record_hazard_crosscal_2026_09_02.py`](../scripts/independent_action_transfer_record_hazard_crosscal_2026_09_02.py)

## Result up front

This block does **not** derive a new action-to-hazard bridge. It supplies one
candidate bridge and proves a narrow exact architecture discriminator. The
2026-09-02 campaign reported that it had not found the joined discriminator on
its frozen base or inspected open heads; that historical search is not a
current exhaustive novelty claim.

Let a positive qubit transfer be

\[
W_\eta=\alpha_\eta(I+r_\eta\cdot\sigma),\qquad
\alpha_\eta>0,\quad |r_\eta|<1.
\]

If one **declared** event-flux law assigns the marked Record intensity

\[
q_\eta(n)\,\mu(dn)
=\gamma_*\operatorname{Tr}(W_\eta P_n)\,\mu(dn),
\qquad P_n={I+n\cdot\sigma\over2},
\]

for a normalized zero-mean mark measure and a common `gamma_*>0`, then

\[
\Gamma_\eta=\int q_\eta(n)\mu(dn)=\gamma_*\alpha_\eta,
\qquad
\det W_\eta=\alpha_\eta^2(1-|r_\eta|^2).
\]

Relative to an isotropic baseline `W_0=alpha_0 I`, the following is an exact
biconditional:

\[
\boxed{
\det W_\eta=\det W_0
\iff
{\Gamma_\eta\over\Gamma_0}
={1\over\sqrt{1-|r_\eta|^2}} .}
\]

This is **not specific to exponentiation**. A traceless action
`W=exp(-A)` is one sufficient realization because
`det W=exp(-Tr A)=1`. Calling it action-generated is predictive only when
`A` is fixed independently before the Record data; otherwise `A=-log W` is
only a reparameterization.

The same positive-transfer/intensity parametrization has two different exact
stopped-process completions. Trace-flux data alone do not select either
instrument; in Route B, the unobserved Kraus-multiplicity factorization is
gauge rather than additional physical content:

1. A same-qubit Kraus completion is normalized and CP, but no-jump results
   filter the blank when `W` is nonscalar. Its survival is then a nontrivial
   mixture of exponentials; scalar `W=cI` is the exact single-exponential null
   case. For positive `gamma_*`, the eventual
   mark distribution loses the initial action bias. It becomes a permanent
   first-Record process only after a supplied external stop/history flag;
   otherwise the same instrument can jump again and overwrite the qubit.
2. An orthogonal blank plus a two-dimensional Record sector gives a
   memoryless exponential jump, keeps the blank unchanged conditional on no
   jump, and makes the entire formed Record sector absorbing.

They are distinguishable without measuring time. For two co-enabled sites

\[
W_1=I,\qquad W_2=\operatorname{diag}(2,1/2),
\]

the memoryless orthogonal-blank law predicts

\[
\Pr(1\text{ wins})={4\over9},
\]

whereas the same-qubit survival-filter law predicts exactly

\[
\Pr(1\text{ wins})={1\over2}.
\]

Winner identity, order, context, and formed content can all be permanent
Records; no absolute duration is used. This is a falsifiable choice between
two supplied architectures, not a restatement of Admissibility and not a
derivation of either architecture.

The current four axioms do not select the action, event-flux rule, scalar
normalization, microscopic carrier, or race history. **No governing axiom text
is changed.** Formal accounting remains **zero obligation retirement** and
**zero TOE percentage movement** pending owner selection, retention, and an
actual Record corpus.

## 1. Exact objects and measure requirements

Let `mu` be a normalized measure on unit Bloch directions satisfying

\[
\int n\,\mu(dn)=0.
\]

This alone gives the total-hazard identity. To infer the full conditional
Bloch vector from marks, require additionally

\[
\int nn^T\mu(dn)={I_3\over3}.
\]

Haar measure on `S^2` has both moments. It is not required. The uniform
measure on the six signed cubic axes also has both moments exactly, so every
machine check can be finite. Three recorded binary PVM contexts give another
tomographically complete operational implementation.

These conditions do different work. Normalization alone does not imply the
half-trace hazard. Zero first moment gives `int P_n mu(dn)=I/2` and hence the
half-trace identity. A unique matrix inferred from the resolved weights
requires the effects in the registered menu to span the Hermitian `2 x 2`
operators. The isotropic second moment is one sufficient spanning condition
and additionally turns the observed mean direction into `r/3`.

Write

\[
P_n={I+n\cdot\sigma\over2},\qquad
\int P_n\mu(dn)={I\over2}.
\]

Under the proposed marked density

\[
q_W(n)=\gamma_*\operatorname{Tr}(P_nW),
\]

the total hazard and conditional mark law are

\[
\Gamma_W={\gamma_*\over2}\operatorname{Tr}W,
\qquad
p_W(dn)={q_W(n)\over\Gamma_W}\mu(dn)
=[1+r\cdot n]\mu(dn).
\]

With the isotropic second moment,

\[
\mathbb E_W[n]={r\over3}.
\]

This last equation is an inference from repeated Records. It does not say
that an individual Record is a probability or that probabilities are readable
before Records exist.

## 2. The constant-determinant theorem

Every strictly positive Hermitian `2 x 2` matrix has the unique decomposition

\[
W=\alpha(I+r\cdot\sigma),
\quad
\alpha={\operatorname{Tr}W\over2},
\quad
r_i={\operatorname{Tr}(W\sigma_i)\over\operatorname{Tr}W}.
\]

The Pauli identity `(r.sigma)^2=|r|^2 I` gives

\[
\det W=\alpha^2(1-|r|^2).
\]

For an isotropic baseline `W_0=alpha_0 I`,
`det W_0=alpha_0^2` and
`Gamma/Gamma_0=alpha/alpha_0`. Therefore

\[
\det W=\det W_0
\iff
\alpha^2(1-|r|^2)=\alpha_0^2
\iff
{\Gamma\over\Gamma_0}={1\over\sqrt{1-|r|^2}}.
\]

Both implications are used. This is not a one-direction fit.

For the traceless exponential family

\[
A_\eta=-h m_\eta\cdot\sigma,
\qquad W_\eta=e^{-A_\eta},
\]

write `x=h|m|`. Then

\[
W=\cosh x\,I+\sinh x\,\widehat m\cdot\sigma,
\quad
r=\tanh x\,\widehat m,
\quad
{\Gamma\over\gamma_*}=\cosh x.
\]

The boxed relation follows. Exponentiation is sufficient because it preserves
the determinant of a traceless generator, not because the theorem uniquely
selects a Gibbs law.

## 3. The scalar-shift and free-hazard controls

For

\[
A_\eta\mapsto A_\eta+c_\eta I,
\]

the transfer rescales as `W_eta -> exp(-c_eta)W_eta`. The normalized content
vector `r_eta` is unchanged, while `Gamma_eta` is multiplied by
`exp(-c_eta)`. Thus a context-dependent scalar shift is directly visible in
Record races and breaks the determinant/content prediction.

A **common scalar shift is absorbed into the rate unit** `gamma_*` and cannot
be found by clock-free comparisons. The absolute value of `gamma_*` requires
a physical duration/tick calibration. The approved kinetic-isotropy and scale
primitives do not supply a dimensionless formation coefficient.

More generally, multiplying every `q_eta` by an arbitrary positive
neighbor-dependent `g(eta)` leaves the conditional content law unchanged and
changes formation races. This is the exact model family behind the statement
that content probabilities alone do not determine formation rate.

## 4. Route Q — a same-qubit first-event survival-filter law

Take one qubit, a positive `W`, and a step satisfying

\[
\delta t\,\gamma_*\lVert W\rVert\le1.
\]

The Kraus density

\[
K_n=\sqrt{2\delta t\,\gamma_*}\,P_nW^{1/2},
\qquad
K_0=(I-\delta t\,\gamma_*W)^{1/2}
\]

is exactly normalized because

\[
K_0^\dagger K_0+
\int K_n^\dagger K_n\mu(dn)
=I-\delta t\gamma_*W
+2\delta t\gamma_*W^{1/2}{I\over2}W^{1/2}=I.
\]

Every nonzero jump output is `P_n`, since

\[
P_nXP_n=\operatorname{Tr}(P_nX)P_n.
\]

Let `D=W^(1/2)rho W^(1/2)-W/2`. Reproducing every resolved
first-opportunity weight says `Tr(P_nD)=0` on the registered menu. If that menu
spans the Hermitian `2 x 2` operators, as the six signed axes do, then `D=0`;
invertibility of `W` gives the unique input `rho=I/2`. Zero first moment by
itself does not give this conclusion. For example, with only the two signed
`z` effects,

\[
W=\operatorname{diag}(2,1/2),\qquad
\rho=\begin{pmatrix}1/2&1/4\\1/4&1/2\end{pmatrix}
\]

has the same two resolved weights as `rho=I/2`, while its off-diagonal
coherence is undetected.

The no-jump state is nevertheless

\[
\rho_0'=
{(I-\delta t\gamma_*W)^{1/2}\rho
 (I-\delta t\gamma_*W)^{1/2}
 \over1-\delta t\gamma_*\operatorname{Tr}(W\rho)},
\]

which differs from `I/2` precisely when `W` is nonscalar. Reapplying the
first-opportunity law after such a miss would silently add a reset.

In continuous time, starting from `I/2`,

\[
\widetilde\rho_t={1\over2}e^{-\gamma_*Wt},
\qquad
S(t)={1\over2}\operatorname{Tr}e^{-\gamma_*Wt}.
\]

At `W=diag(e^x,e^{-x})`, survival is

\[
S(t)={e^{-\gamma_*e^x t}+e^{-\gamma_*e^{-x}t}\over2},
\]

For `x != 0` this is not the single exponential with rate
`gamma_* cosh x`; for `x=0`, or more generally `W=cI`, it is exactly
`exp(-gamma_* c t)`. The integrated mark weight for `gamma_*>0` is

\[
\int_0^\infty\gamma_*\operatorname{Tr}
 [P_nWe^{-\gamma_*Wt}]dt
=\operatorname{Tr}P_n=1.
\]

Consequently eventual marks follow the base measure `mu`; the action survives
in time/content correlations and early formation, not in the time-marginalized
eventual content. At `gamma_*=0` there is no event and no normalized eventual
mark law, so neither this integral nor a race ratio applies. The
**same-qubit survival-filtering law remains a live
positive theory**. It is simply not the requested stationary memoryless law.
Nor is it an autonomous permanent-Record writer on the same qubit: after a
jump, reapplying the instrument can jump again. The race comparison below
therefore treats it as a supplied stopped process whose first jump is archived
by an external Record/history rule.

## 5. Route B — orthogonal blank and absorbing Record sectors

Let

\[
\mathcal H_{dyn}=\mathbb C|B\rangle\oplus\mathbb C^2_R.
\]

For any qubit basis `{e_1,e_2}`, define

\[
V_{n,j}=\sqrt{\gamma_*}
\langle n|W^{1/2}|e_j\rangle
|n_R\rangle\langle B|.
\]

For a discrete mark measure, include `sqrt(mu_n)` in each operator; the
integral notation below includes it in `mu(dn)`. Summing the Kraus multiplicity
gives

\[
\sum_jV_{n,j}|B\rangle\langle B|V_{n,j}^\dagger
=q_W(n)P_n,
\]

and summing all marks gives

\[
\int\sum_jV_{n,j}^\dagger V_{n,j}\mu(dn)
=\Gamma_W|B\rangle\langle B|.
\]

The resulting marked operation is basis independent because a basis change
only unitary-mixes the Kraus operators. This also means that the particular
`W^(1/2)` Kraus representation is not a separately observable microscopic
mechanism; after summing the multiplicity, the physical input used here is the
declared density `q_W(n)`.

The Lindblad generator is

\[
\mathcal L(X)=
\int\sum_jV_{n,j}XV_{n,j}^\dagger\mu(dn)
-{1\over2}\{\Gamma_W|B\rangle\langle B|,X\}.
\]

It gives `S(t)=exp(-Gamma_W t)` from the blank. Every operator supported in
the Record sector is fixed, so formed Records are absorbing. An exact
finite-time instrument is

\[
K_0(T)=e^{-\Gamma_WT/2}|B\rangle\langle B|+\Pi_R,
\]

\[
K_{n,j}(T)=
\sqrt{{1-e^{-\Gamma_WT}\over\Gamma_W}}V_{n,j}.
\]

To make the operator claim explicit, write a general operator in blank/Record
blocks as

\[
X=\begin{pmatrix}a&z\\y&R\end{pmatrix},\qquad
\tau_W={1\over\Gamma_W}\int\sum_j
V_{n,j}|B\rangle\langle B|V_{n,j}^\dagger\,\mu(dn),
\]

and put `s=exp(-Gamma_W T)`. The full finite channel is

\[
\Phi_s(X)=
\begin{pmatrix}
sa&\sqrt{s}\,z\\
\sqrt{s}\,y&R+(1-s)a\tau_W
\end{pmatrix}.
\]

Thus it fixes every operator in the complete Record block, damps both
blank/Record coherence blocks by `sqrt(s)`, and deposits the blank population
in `tau_W`. Direct substitution gives
`Phi_s o Phi_t = Phi_{st}` on every matrix unit. This full-operator statement
is stronger than completeness or equality of the total jump effect: a
spurious phase on one Record basis vector preserves those scalar checks but
changes Record and blank/Record coherences. Both runners check the nine matrix
units, the four Record-block units, semigroup composition, a rotated Kraus
basis, and this phase negative control. No no-jump reset is needed because the
blank is a one-dimensional sector and conditional survival leaves it unchanged.

## 6. The exact carrier boundary and finite parity-safe escape

Suppose a designated formation jump `L` acts on the same two-dimensional
carrier and has zero post-formation intensity on every pure Record ray. Then
`L|n>=0` for every Record ray. The two orthogonal `z` rays already span the
carrier, so `L=0`. Thus a **single two-dimensional Kraus carrier** cannot use a
nonzero designated append jump while making the complete pure-qubit orbit a
zero-intensity absorbing sector.

This is deliberately narrow. It says nothing against a hybrid stochastic
state space with a separate no-Record status, an explicit stop/reset, a
restricted nonspanning menu, survival filtering, an environment-carried flag,
or a larger block.

Under the optional fixed global parity hypothesis, two qubits have an even
sector of dimension two: enough for a logical qubit but not an orthogonal
blank plus that logical qubit. Three qubits have an even sector of dimension
four. Choose

\[
|B\rangle=|000\rangle,
\quad |0_L\rangle=|011\rangle,
\quad |1_L\rangle=|101\rangle.
\]

All have total parity `+1`. Every logical `P_L(n)`, action `A_L`, transfer
`W_L`, and jump `|n_L><B|` commutes with total parity. The determinant and race
algebra is unchanged on the logical code.

This is a finite algebraic construction, not a lattice-wide Record compiler.
Composite Record identity, joint formation, decoder, covariant three-site
allocation, overlap arbitration, and the cross-site product are still
supplied. Since grading is not a current axiom, this is a **conditional
compatibility fork, not an axiom inconsistency**.

## 7. Clock-free two-site Record discriminator

For two disjoint sites with frozen conditions, additive memoryless generators,
and common `gamma_*`, the first-event law is

\[
\Pr(I=i,n\in dn,t\in dt)
=e^{-(\Gamma_1+\Gamma_2)t}q_i(n)dt\,\mu(dn).
\]

Integrating out duration gives

\[
\Pr(I=i)={\Gamma_i\over\Gamma_1+\Gamma_2},
\qquad
\Pr(n\in dn\mid I=i)=[1+r_i\cdot n]\mu(dn).
\]

Thus

\[
{\Pr(I=1)\over\Pr(I=2)}
=\sqrt{{1-|r_2|^2\over1-|r_1|^2}},
\qquad
r_i=3\mathbb E[n\mid I=i].
\]

This odds identity requires the displayed comparison family to have equal
transfer determinants, `det W_1=det W_2`; it is not a consequence of an
arbitrary pair of positive transfers.

For `W_1=I` and `W_2=diag(2,1/2)`, one has

\[
r_1=0,\quad r_2={3\over5}\hat z,
\quad \Gamma_1=\gamma_*,\quad
\Gamma_2={5\over4}\gamma_*,
\]

and therefore `Pr(I=1)=4/9`.

For the same-qubit survival filters, additionally supply independent local
no-jump channels and the joint neutral product blank
`rho_12=I_2/2 tensor I_2/2=I_4/4`. Diagonalizing both transfers and integrating
their competing survival mixtures then gives

\[
\Pr_Q(I=1)={1\over4}\sum_{s,t=\pm}
{w_{1,s}\over w_{1,s}+w_{2,t}}.
\]

At eigenvalues `(1,1)` and `(2,1/2)`, this is

\[
{1\over2}\left({1\over3}+{2\over3}\right)={1\over2}.
\]

Moreover, winner-conditioned content in Route Q depends on the competitor's
transfer because the race conditions a survival-filtered state. It does not
in Route B. The `4/9` versus `1/2` difference is therefore a direct Record-only
test of the two supplied stopped-process architectures sharing the same
declared positive-transfer/intensity parametrization.

## 8. What “Record-only” requires

Every trial must permanently certify:

1. the two pre-race neighboring conditions;
2. the registered event/PVM context or mark codec;
3. both sites' eligibility and simultaneous exposure;
4. the first append order and winner identity;
5. the winner's formed Record content; and
6. a fresh-target/trial identifier.

No duration is needed. Absence at an unread site is not itself treated as a
measurement. The eligibility/exposure controller must leave a Record. Across
adaptive trials, the predictive probability is supplied by the candidate law
and the pretrial Record filtration. Only conditional on that premise, a winner
indicator minus its conditional predicted probability is a bounded martingale
difference. This gives finite
concentration without an IID claim; exact law selection still requires a
candidate class, persistent excitation, fresh capacity, and empirical
typicality.

## 9. Proved mathematics versus supplied physics

Proved in this note and runner:

- the finite cubic 2-design moments;
- positive-transfer decomposition and determinant identity;
- the constant-determinant/rate-polarization biconditional;
- the distinction between a zero-first-moment menu and a tomographically
  spanning menu, including an explicit nonspanning counterexample;
- exact CP completeness and pure branch output for Routes Q and B;
- the nonscalar no-jump filtering/non-exponential law, scalar exponential null
  case, and positive-rate eventual-unbiased-content law for Route Q;
- the full-matrix absorbing finite-time semigroup for Route B, including
  blank/Record coherences and all Record-sector operators;
- the narrow same-two-dimensional-Kraus-carrier boundary;
- the three-qubit even algebraic escape; and
- the two exact race predictions `4/9` and `1/2`.

Supplied, not derived:

- a physical local action/transfer fixed independently of Record outcomes;
- the identification of that positive transfer with unnormalized event flux;
- the registered event effects/mark measure and matching output codec;
- the common rate multiplier and any absolute clock value;
- the blank/history architecture and additive race generator;
- frozen eligibility, fresh capacity, and empirical typicality;
- any composite Record/block identity and covariant allocation; and
- any optional grading or cross-site product.

The event-flux sentence is a candidate downstream physical law. It is not an
unpacking of the four axioms. The earlier Block 50 decision memo is preserved
as attributed campaign history; it is not current premise authority. This note
and the current Minimal Axioms memo are the active prose inputs to the runners.

## 10. Current-axiom and TOE boundary

The current Admissibility distribution is explicitly conditional on Record
formation and does not supply formation site, probability, or rate. The
minimal memo separately withholds transfer operators, dynamics, clocks,
production processes, source/action identification, and probability values.
The three approved primitives supply a units reference, kinetic-form isotropy,
and a realized-state evaluation slot; none supplies this law.

Therefore this packet is a conditional candidate plus a discriminating
experiment. It does not derive a current-axiom consequence, set an audit
verdict, amend a primitive, or retire a registered derivation obligation.

```text
obligation_retirement: 0
toe_percentage_movement: 0
retained_positive_end_to_end_theory: 0
axiom_edit: none
```

This is useful route progress because it converts one *supplied* action-to-rate
candidate into two explicit rival stopped-process laws and a finite Record-only
separator. It does not close Block 20's missing action-to-intensity interface,
because the trace-flux rule is an input. It is not formal TOE closure.

Machine-readable rhetoric guard: this is a constant-determinant positive
transfer theorem. The same-qubit survival-filtering law remains a live positive
theory. The grading issue is a conditional compatibility fork, not an axiom
inconsistency. No governing axiom text is changed.

## 11. Historical prior-art and promotion record

The closest surfaces reported by the 2026-09-02 campaign are disclosed in its
historical
[`PRIOR_ART_SEARCH.md`](../.claude/science/physics-loops/toe-action-generated-record-hazard-crosscal-block50-20260902/PRIOR_ART_SEARCH.md).
That campaign reported selected action-generated marked Poisson laws, complete QND
writers, no-jump backaction, pure-birth processes, generic hazard races,
action/transfer interface inventories, formation-bias warnings, and grading
repairs. Block 49 already states the rate/polarization equation and requests
this joint successor. Those source and open-head observations are retained as
dated provenance, not reasserted as a current exhaustive search. The corrected
scientific surface rests on its explicit mathematics rather than a novelty
classification.

| Value gate | Verdict | Reason |
|---|---|---|
| V1 parent-obligation closure | **FAIL** | No audit-owned parent `verdict_rationale` is closed, and the trace-flux rule needed by Block 20 is supplied rather than derived. |
| V2 exact novelty | **historical NARROW PASS** | The dated campaign reported no inspected source containing the joined survival-filter/eventual-base-mark theorem and exact `4/9` versus `1/2` witness. This correction does not repeat that search. |
| V3 retained-primitive essentiality | **FAIL** | Once `W`, trace flux, carrier, stop/history semantics, and a common race scale are supplied, standard finite-dimensional CP and exponential-race algebra gives the result. |
| V4 difficulty / leverage | **FAIL** | The result is falsifiable and useful, but its determinant, spectral-integral, rational-race, and parity-dimension steps are short standard calculations. |
| V5 structural novelty | **historical NARROW PASS** | The dated campaign reported the joined discriminator absent from its frozen comparison set. This is provenance, not current authority. |

The historical campaign disposition was **BACKLOG_NO_PR**. This correction
does not promote that disposition into an audit verdict. Formal accounting
remains zero obligation retirement and zero TOE percentage movement.

## No-Go Discipline Gate

The only negative theorem shipped is narrow: a designated nonzero append jump
on one two-dimensional Kraus carrier cannot have zero intensity on every ray
of the complete pure-qubit Record orbit. The packet does not claim that
Record formation, a memoryless law, or the TOE is impossible.

### N1 — materially distinct routes

| Route | Object / mechanism / terminal | Result | Marker |
|---|---|---|---|
| same-qubit filter | `K_n=P_nW^(1/2)`; supplied positive-root no-jump evolution with completeness-forced effect | succeeds as a CP theory; stationary memoryless content fails after no-jump without reset | **ATTEMPTED** |
| orthogonal blank direct sum | `C|B> direct_sum C^2_R`; blank-to-Record jumps | succeeds exactly with one extra orthogonal level | **ATTEMPTED** |
| hybrid pure-birth state space | no-Record status plus supplied marked generator | remains live and avoids the single-Kraus-carrier premise; PR #6371 comparator | **ATTEMPTED** |
| explicit reset/fresh target | reprepares the neutral blank after a miss or uses new capacity | remains live but adds history/reset physics; Block33 comparator | **ATTEMPTED** |
| restricted Record menu | absorb only a nonspanning set of rays | remains live; does not meet the full-orbit target | **ATTEMPTED** |
| three-qubit even block | orthogonal blank plus logical qubit inside fixed parity | succeeds algebraically; composite Record placement remains open | **ATTEMPTED** |
| same-carrier zero-intensity full orbit | require the append jump to annihilate every pure ray | the two `z` rays already force the operator to zero | **ATTEMPTED** |
| non-Markov/reversible environment | carry history in distributed or environmental degrees of freedom | live outside the declared Markov/Kraus carrier theorem; Blocks20--21 comparators | **RULED OUT BY PRIOR as a witness for this narrow class only** |

These families differ in primary carrier, invariant, or terminal obligation;
they are not merely different notations for one construction.

### N2 — wall-independence audit

The raw missing items collapse as follows:

- `W1`: independently selected physical transfer, including its
  context-dependent scalar representative; exponentiation is not separate;
- `W2`: transfer-to-event-flux/effect/output identification;
- `W3`: blank, absorption, eligibility, race, reset, and fresh-capacity history
  semantics;
- `W4`: absolute common rate unit, needed for durations but not relative races;
- `W5`: optional composite grading/block placement, relevant only if that
  separate hypothesis is adopted.

These five labels separate mathematical choices that this packet supplies:
its formulas do not derive any one of them from another. That observation is
only an input ledger. It does not prove that the corresponding physical
requirements are independent in a complete framework, that every pair can be
varied while all retained laws remain fixed, or that a future construction
could not close several together. No categorical pairwise physical-independence
claim is made.

The common scalar shift and `gamma_*` are one global rate convention for
relative races, rather than two items. Context-dependent scalar action data
belongs to W1. Haar versus finite cubic marks is not a separate item because
the theorem uses only the displayed moment and spanning conditions.

### N3 — hidden-condition scan

| Phrase/input in proof | Classification |
|---|---|
| “take `W` positive” | explicit candidate domain; physical selection is W1 |
| “event-flux law” | explicit supplied physical condition W2 |
| “same action” | means one independently pinned `W`; otherwise `-log W` is only reparameterization |
| “blank” / “absorbing” | explicit Route-Q or Route-B carrier/history condition W3 |
| “common rate” | explicit W4; cancels only in relative race |
| “registered context” | must be a prior Record in the empirical protocol |
| “frozen race” | explicit W3; no same-event feedback |
| “grading-safe” | conditional W5, not current axiom content |
| “standard CP/Lindblad” | non-load-bearing name; all finite identities are executed |
| “current axioms” | pinned retained premise used only for the non-entailment boundary |

No use of “by construction,” “naturally,” or “the framework provides” hides a
load-bearing condition.

### N4 — residual matching

The following is the original campaign's dated residual inventory. Only the
current Minimal Axioms memo is an active premise of this corrected packet; the
other rows are preserved as attributed search provenance and do not supply a
step of the finite-dimensional proof.

| Witness | Witness residual | Residual used here | Match? |
|---|---|---|---|
| Minimal Axioms, lines 60--69 and 116--130 | conditional content; no action/rate/dynamics | current-entailment boundary only | yes |
| content/rate theorem `41dbe60d14` | normalized content does not fix formation rate | free positive hazard counterfamily | yes |
| Source/Eta Block20 `8246f77ecf` | nine-field action/transfer-to-append-intensity interface missing on inspected stack | conditional completion compared here; not closure because flux is supplied | yes |
| Source/Eta Block21 `3e0f738f7c` | finite reusable bath obstruction in a fixed all-use class | cited only against that bath class | yes |
| Source/Eta Block33 `7dc9582f49` | reset/renewal not selected by visible marginals | explicit-reset condition in W3 | yes |
| Source/Eta Block42 `26209dd0d0` | formation conditioning can bias content | event-flux/history calibration warning | yes |
| Block43 `3c375f8cfa` / PRs #7830--#7832 | conditional grading and finite even logical repair | optional W5 compatibility only | yes |

No gravity, source-current, or reusable-bath result is cited as a universal
formation no-go.

### N5 — rhetoric and resolution audit

| Resolution | Actually tested | Not claimed |
|---|---|---|
| per element | positive `2 x 2` transfer, effects, determinants, Kraus branches | no arbitrary-dimensional classification |
| per site | one same-qubit filter and one direct-sum blank/Record writer | no assertion that a site axiom contains a qutrit |
| per mode | six cubic marks and fixed-parity logical states | no continuous pointer uniqueness |
| per block | two-site races and one three-qubit even embedding | no covariant block allocator or collision totalization |
| lattice-wide | checked and not executed — infinite-volume existence, overlap arbitration, causal propagation, and recurrence remain open | no lattice-wide dynamics or TOE claim |

“A one-qubit carrier cannot do this” is never used without the designated
append-jump, zero-intensity, and full-orbit qualifiers.

### N6 — partial-closure and primitive scan

The 2026-09-02 campaign recorded the following primitive reading:

- `scale_reference_primitive` supplies units only;
- `kinetic_isotropy_primitive` supplies `c_t=c_s` in kinetic form only; and
- `realized_state_primitive` supplies a pointwise realized-state slot only.

Within that dated reading, none supplied a probability rule, event flux,
formation coefficient, reset, grading, or action identification. A named tick
could express a later rate but did not select its dimensionless value. The
current correction independently pins only the Minimal Axioms memo for the
non-entailment boundary and does not revalidate the full historical registry.

Live partial closures are the hybrid no-Record status already present in the
ontology, a finite registered binary-PVM/cubic-menu implementation, the
three-qubit even block, explicit fresh-target archives, and owner adoption of
the narrow downstream formation law. None is misclassified as a mandatory new
axiom.

### N7 — strongest hostile steelman

> The orthogonal-level conclusion is an artifact of demanding a linear Kraus
> carrier. The Record ontology already distinguishes “no Record” from Record
> content, so a hybrid pure-birth generator can use that status without adding
> a qutrit site. Moreover, the same-qubit filter is itself a complete CP law;
> its non-exponential survival is a prediction, not a defect. Therefore this
> block has not proved that autonomous permanent Records require a new local
> degree of freedom.

Correct. That is why the theorem is restricted to a designated append jump
acting on the same two-dimensional quantum carrier with the full pure orbit at
zero post-formation intensity. Hybrid status, same-qubit filtering, explicit
stop/reset, and larger blocks remain positive routes. The steelman defeats a
broader no-go and thereby fixes the present narrow wording; it does not defeat
the two-column linear-algebra proof.

### N8 — cross-cycle echo

The original campaign reported that earlier cycles repeatedly separated normalized content from occurrence rate,
visible renewal from physical reset, action coefficients from append
intensities, and one-site grading from multi-site even encoding. Some apparent
carrier walls were retired by adding distributed pointers or typed blocks;
that same mechanism is explicitly executed here in the orthogonal direct sum
and three-qubit even block. Some normalization walls were reframed as
conventions; here only a **common** scalar is a rate convention, while
context-dependent scalars remain observable by races.

The precedent therefore narrows rather than closes the claim. The packet keeps
hybrid, distributed, reset, finite-menu, and non-Markov routes live.

**Gate disposition:** the narrow same-carrier append-jump theorem and the
current-axiom non-entailment boundary remain eligible for focused review. A
global formation no-go, an axiom-necessity claim, categorical physical
wall-independence, or a statement that the orthogonal-blank law is uniquely
selected is withdrawn. No formal audit verdict is assigned here.

## Reproduction

Run:

```bash
python3 scripts/action_transfer_record_hazard_crosscal_2026_09_02.py
```

Also run the independently executable helper:

```bash
python3 scripts/independent_action_transfer_record_hazard_crosscal_2026_09_02.py
```

The source-bound caches report the actual final pass counts and contain all
five N5 resolution lines. The corrected controls are explicit mathematical
counterexamples and full-channel operator comparisons; the historical
48-Boolean mutation claim receives no current scientific credit. Generated
matrices and trial laws are theorem fixtures, not observational evidence.
