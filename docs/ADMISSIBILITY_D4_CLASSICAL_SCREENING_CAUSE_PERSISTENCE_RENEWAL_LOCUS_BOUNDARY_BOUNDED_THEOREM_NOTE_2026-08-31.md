# Finite classical screening causes and supplied three-use histories

**Date:** 2026-08-31; correction 2026-09-09.
**Campaign block:** Source/Eta 33.
**Type:** bounded_theorem
**Standing:** conditional mathematical result; physical suppliers remain open.

Descriptions below of exhaustive runner checks refer to the archived original
controller unless named in the current evidence section. The displayed proofs
remain; the current entrypoint does not relabel old executions as fresh.

**Primary runner:** [`admissibility_d4_classical_screening_cause_renewal_locus_gate_2026_08_31.py`](../scripts/admissibility_d4_classical_screening_cause_renewal_locus_gate_2026_08_31.py).
**Current bounded cache:** [execution](../logs/runner-cache/admissibility_d4_classical_screening_cause_renewal_locus_gate_2026_08_31.txt).

Current framework boundary: [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
[32 conditional theorem](ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md).
[Exact original bodies, versions and earlier evidence](../.claude/science/physics-loops/eta-pair-process-correction-20260909/HISTORY.md).

## Result in one paragraph

Block32 left a full strict family of supplied pair laws

\[
q_\lambda(g,h)=
\begin{cases}
(1+3\lambda)/16,&g=h,\\
(1-\lambda)/16,&g\ne h,
\end{cases}
\qquad 0\leq\lambda<1.
\]

This note classifies one candidate ownership rule.  If a finite classical
screening cause is unchanged across two events, has the identical conditional
product response on both uses, and uses fresh conditionally independent
response noise, then compatibility with the Block32 product history
`q_lambda tensor q_lambda` exists exactly at `lambda=0`.  This does **not**
select `lambda=0` physically: a fixed five-response interaction with supplied
iid cause banks and a separate lambda-dependent coherent unitary both realize
every `lambda` in the strict interval.  Moreover, all one- and two-use
marginals can be product while a positive three-use law is not.  The surviving
physics question is who fixes the environment preparation, coupling, or
branchwise reset/source law.

## Imported conditional result

The conditional mathematical input is the Block32 output family and its
two-use product target.  Block28 and Block32 did not derive a value of
`lambda`; they retained the strict interval under their declared supplied-law
condition.  This note independently reconstructs the displayed matrix and
does not promote either supplied law to an axiom.

Write the four-by-four probability matrix as

\[
Q_\lambda=\frac{1-\lambda}{16}J_4+\frac{\lambda}{4}I_4
=\frac14(P_0+\lambda P_\perp),
\]

where `P_0=J_4/4` and `P_perp=I-P_0`.

## Exact static resource facts

The spectrum of `Q_lambda` is

\[
\operatorname{spec}(Q_\lambda)
=\left\{\frac14,\frac\lambda4,\frac\lambda4,\frac\lambda4\right\},
\qquad
\det Q_\lambda=\frac{\lambda^3}{256}.
\]

Consequently its ordinary and nonnegative ranks are one at `lambda=0` and
four for every positive `lambda`.  The nonnegative-rank upper bound follows
from

\[
S_t=P_0+tP_\perp,\qquad t=\sqrt\lambda,
\qquad Q_\lambda=\frac14S_tS_t^T.
\]

Every column of `S_t` is a probability vector for `0<=t<=1`, giving a
four-state product-response decomposition for each individual law.  This is a
static factorization, not a cause carrier or selector.

A single lambda-independent product-response library for the whole family is

\[
R_*=J_4/16,\qquad R_i=e_ie_i^T,
\qquad
Q_\lambda=(1-\lambda)R_*+\frac\lambda4\sum_{i=1}^4R_i.
\]

Five responses are minimal for such a fixed library.  In the `lambda -> 1`
closure, every product distribution contributing to the diagonal-only
endpoint must itself be supported on one diagonal cell.  Four such atoms are
required to cover the four diagonal cells.  Their convex hull contains no
off-diagonal support and therefore cannot contain the fully supported
`Q_0=R_*`; a fifth response is necessary.  This is not a minimum Hilbert-space,
Kraus, archive, or physical-environment dimension.

## Frozen classical-screening theorem

Let `Z` be a finite classical cause with weights `pi_z`.  Conditional on
`Z=z`, let one complete pair outcome `X=(g,h)` have normalized product law

\[
r_z(g,h)=a_z(g)b_z(h),
\qquad q=\sum_z\pi_zr_z.
\]

The theorem's frozen grammar is the single joint statement

\[
P(X_1=x,X_2=y\mid Z=z)=r_z(x)r_z(y).
\]

Thus the same unchanged cause and identical response are used twice, while
the response randomness is fresh on each use.  This is more specific than
average stationarity.

The frozen and renewed two-use histories are

\[
H_F(x,y)=\sum_z\pi_zr_z(x)r_z(y),
\qquad
H_R(x,y)=q(x)q(y).
\]

Their difference is the exact cause covariance

\[
H_F-H_R
=\sum_z\pi_z(r_z-q)(r_z-q)^T\succeq0.
\]

Its trace is the complete-pair repetition excess

\[
\operatorname{tr}(H_F-H_R)
=\sum_z\pi_z\lVert r_z-q\rVert_2^2.
\]

Equality holds if and only if every active (`pi_z>0`) response equals `q`.
Each `r_z` has matrix rank one, so equality for `q_lambda` requires
`rank(Q_lambda)=1`, hence `lambda=0`.  Conversely, at `lambda=0` the one-state
uniform product response supplies an equality witness.  Therefore the locus
of `lambda` values for which **some** factorization in this frozen grammar is
compatible is exactly `{0}`.

The existential qualifier matters.  Not every factorization of `q_0` is
compatible: the four-state row-label factorization still has frozen repeat
gap `3/16`.  Zero-weight cause sectors are unconstrained.

## Why this is not a physical selector

### Supplied iid fixed-interaction control

Let a cause register have five orthogonal sectors `I,D_1,...,D_4`.  Let the
output and archive registers each have a Blank state and sixteen pair labels.
On the five-dimensional Ready/Blank input subspace define

\[
V|I,B_O,B_A\rangle
=\frac14\sum_{g,h}|I,g,h\rangle_{C,O}|g,h\rangle_A,
\]

\[
V|D_i,B_O,B_A\rangle
=|D_i,i,i\rangle_{C,O}|i,i\rangle_A.
\]

The five images are orthonormal, so `V dagger V=I_5` and the map admits a
full-space unitary extension.  The interaction is lambda-independent.  With

\[
\rho_C(\lambda)
=(1-\lambda)|I\rangle\langle I|
+\frac\lambda4\sum_i|D_i\rangle\langle D_i|,
\]

tracing cause and archive gives exactly `Q_lambda`.  Three distinct supplied
cause/output/archive banks acted on by `V tensor V tensor V` give
`q_lambda tensor 3`.  All banks are preinitialized and the cause/archive
outputs remain explicit.  This relocates `lambda` into environment
preparation; it does not derive physical reset or renewal.

### Evolving and hidden-memory controls

For the binary endpoint mixture, with `Delta=q_1-q_0`, the persistent-mode
excess is

\[
H_{\rm persistent}-q_\lambda^{\otimes2}
=\lambda(1-\lambda)\Delta^{\otimes2}.
\]

The probability that both complete pair outcomes separately satisfy `g=h`
has excess `9 lambda(1-lambda)/16`.  The complete-pair equality/repetition
event has the distinct excess `3 lambda(1-lambda)/16`.

For the deliberately restricted row-stochastic family

\[
K=\Pi+\rho(I-\Pi),\qquad 0\leq\rho\leq1,
\]

the residual is `rho lambda(1-lambda) Delta tensor Delta`.  Visible redraw is
`rho=0`.  A hidden label may nevertheless persist while the visible response
class is redrawn, so product output does not imply reset of the complete
environment.  Likewise, a fixed composite cause carrying independent
first-use and second-use labels realizes the product history through
use-dependent conditional responses; that live route lies outside the
identical-response theorem.

### Coherent control

Define

\[
U_\lambda=P_0+e^{i\theta}P_\perp,
\qquad \cos\theta=2\lambda-1.
\]

Then `U_lambda` is unitary, commutes with simultaneous label permutations,
and

\[
|U_\lambda(g,h)|^2=4q_\lambda(g,h).
\]

This control retains the complete strict interval but places `lambda` in the
coupling angle.  A dephased measure-prepare channel with this positive
transition table has canonical Kraus rank sixteen, while the displayed
unitary channel has Kraus rank one.  They share a visible classical transition
table, not a full quantum channel; the table does not determine microscopic
environment dimension.

## Two-use data do not prove three-use renewal

Flatten the sixteen pair outcomes and define

\[
w(g,h)=\begin{cases}3,&g=h,\\-1,&g\ne h,\end{cases}
\qquad \sum_{g,h}w(g,h)=0.
\]

With `b_lambda=(1-lambda)/16` and
`epsilon_lambda=b_lambda^3/54`, set

\[
H_3=q_\lambda^{\otimes3}+\epsilon_\lambda w^{\otimes3}.
\]

Every entry is strictly positive for `0<=lambda<1`.  The negative-sign cases
are bounded below by `53 b_lambda^3/54` (three off-diagonal outcomes) and
`5 b_lambda^3/6` (one off-diagonal outcome).  Since `sum w=0`, all three
two-use contractions and all one-use marginals equal the corresponding
product marginals.  Yet every all-diagonal labeled triple cell is shifted by

\[
27\epsilon_\lambda=b_\lambda^3/2>0.
\]

Thus even complete pair-marginal agreement does not establish a product
three-use law or branchwise predictive reset.  This is an abstract scalar
outcome history, not a third physical Block32 transaction or an
arbitrary-depth construction.  In this counterroute `lambda` remains in the
supplied history law, just as it remains in environment preparation for the
five-cause control or in the coupling for the coherent control.

## Physical and TOE boundary

The retained result distinguishes architectures; it does not choose one.
No local M2 cause carrier, Ready/Spent reset, nearest-neighbor Stinespring
compiler, autonomous cadence, normalized conserved pair source, gravity law,
or Record identification is constructed.  No approved primitive supplies the
missing environment preparation, predictive reset, or source normalization.
Accordingly:

- no axiom amendment is supported;
- no audit or obligation-retirement verdict is claimed;
- no TOE lane percentage moves;
- the next high-leverage fork is branchwise predictive reset versus a
  physically normalized pair-sensitive source.

If a reset derivation only supplies fresh banks while leaving their
`lambda`-dependent preparation unexplained, it relocates rather than closes
the selector.  In that case the source/Ward-normalization pincer outranks more
transaction plumbing.

## Evidence scope after correction

Current named science checks:

- `spectrum_ranks`
- `four_cause_per_law`
- `fixed_five_library`
- `finite_cause_covariance_SOS`
- `existential_frozen_locus`
- `Markov_and_hidden_memory`
- `binary_event_distinction`
- `fixed_isometry_and_supplied_banks`
- `coherent_control`
- `actual4096_three_use_and_changed_epsilon_axis`


The original Block33 numerical definitions and conditional argument are
preserved. The current entrypoint executes the checks it names, with current
source, own-note and actual input identities. Its terminal covers those
bounded checks only. It does not replay or newly certify the original long
controller, original mutation census, or historical custody/status checks.
The complete original execution output and all earlier source versions remain
in the linked recovery inventory, including any earlier failures. Mathematical
claims beyond the named fresh checks retain their displayed proof and the
explicitly historical computation; old outputs are not presented as fresh.
No formal audit verdict or physical TOE closure is asserted.
