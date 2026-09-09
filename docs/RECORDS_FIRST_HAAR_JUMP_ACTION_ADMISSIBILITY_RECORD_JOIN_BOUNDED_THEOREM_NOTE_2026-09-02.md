---
runner: scripts/records_first_haar_jump_action_admissibility_record_join_2026_09_02.py
---
# Records-first Haar jump on a supplied finite domain

Date: 2026-09-02; corrected 2026-09-09
Type: bounded_theorem
Status: conditional finite mathematics; independent landing confirmation pending

Primary runner: `scripts/records_first_haar_jump_action_admissibility_record_join_2026_09_02.py`

This construction joins a six-slot density map, a normalized local Haar
instrument, a finite permanent-write Markov process and adaptive coarse-event
calibration. It supplies no physical selection of the instrument, rate or Record
carrier. The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) is the sole repo
premise used here: its Admissibility distribution clause is governing. Only the
subsequent reading notes are interpretive. The clause requires a distribution
that depends on and varies with neighbor conditions; it does not specify this
law's numerical response or formation rate.

The supplied conditions are the density-state restriction inside the larger
`M_2(C)` algebra, pure projectors as Record contents, content access in a common
internal frame, normalized spherical Haar measure, the six-slot boundary rule,
the aligned local instrument and a finite-volume exponential-race process.
They remain conditions, including the physical ability to read/use the proposed
Record contents. No microscopic write implementation or full four-axiom model
is established. Formal audit is deferred; no TOE obligation is retired.

## The candidate law

Let `V` be a finite subset of `Z^3` with inherited nearest-neighbor adjacency.
A site is either
open or carries one permanent pure-state Record

\[
P(n)=\frac{I+n\cdot\sigma}{2},\qquad n\in S^2.
\]

For each open `x`, index **all six directional slots** by
`d in {+e1,-e1,+e2,-e2,+e3,-e3}`. The slot contains the projector
at `x+d` if that site is in `V` and recorded. It contains `I/2` if the site
is open **or outside V**. This boundary placeholder is an explicit supplied
boundary condition, not a read of an absent or unrecorded site. Define

\[
\rho_x(C)=\frac16\sum_{d}\widetilde\rho_{x,d}(C)
 =\frac{I+\bar r_x(C)\cdot\sigma}{2},\qquad
\bar r_x(C)=\frac16\sum_d\widetilde r_{x,d}(C).
\]

Each of the six summands is a density matrix. In particular an isolated
site has six placeholders, `rho_x=I/2` and a normalized uniform mark law.
Summing only actual neighbors and dividing by six would instead give trace
`degree(x)/6`; at a degree-three corner it gives `1/2`, and at an isolated
site zero. That defective definition is withdrawn. With normalized
rotation-invariant measure `mu` on `S^2`, define the branch operation

\[
\mathcal J_x(dn)(\rho)=2P(n)\rho P(n)\,\mu(dn).
\]

The resulting marked generator on bounded functions of the finite Record
configuration is

\[
(Lf)(C)=\sum_{x\text{ open}}\int_{S^2}
  \bigl[f(C\cup\{x\mapsto P(n)\})-f(C)\bigr]
  \bigl[1+\bar r_x(C)\cdot n\bigr]\,\mu(dn).
\]

This single displayed generator includes both the total formation hazard and
the conditional Record content. There is no second hidden activation coin.
Recorded sites are absent from the sum and are therefore absorbing.

## Theorem 1 — legal local state and symmetry

For every legal Record configuration, `rho_x(C)` is a density matrix. Each
neighbor Bloch vector has norm at most one, so

\[
\lVert\bar r_x\rVert\leq\frac16\sum_d\lVert\widetilde r_{x,d}\rVert\leq1.
\]

Therefore the two eigenvalues `(1+-|bar r_x|)/2` are nonnegative and the trace
is one. The all-open condition gives `bar r_x=0`; hence it introduces no
preferred qubit direction and still nucleates Records uniformly.

The arithmetic mean is invariant under every proper-cubic permutation of the
six neighbor slots and is equivariant under a common qubit-frame rotation. The local rule commutes with translations and cubic rotations when the domain
and its slot data are transformed together; a fixed finite boundary need not
have those global symmetries. It varies: one `+x` Record among five open
neighbors gives `bar r=e_x/6`, whereas the all-open condition gives zero.

The stated uniqueness is deliberately narrow. In the **affine/transitive
class** of neighbor maps that (i) commute with every common internal rotation,
(ii) treat the proper-cubic orbit of six slots transitively, (iii) send the
all-open tuple to zero, and (iv) reproduce a constant six-neighbor Bloch
vector, the constant offset is zero by rotation invariance. Each real 3-by-3 linear
block commutes with every rotation. The half-turns about coordinate axes kill
its off-diagonal entries and rotations exchanging axes equalize its diagonal
entries, so each block is scalar. Slot transitivity makes
all six scalars equal, and constant reproduction fixes each to `1/6`. No
broader nonlinear uniqueness is claimed.

## Theorem 2 — normalized matching Record instrument

For a qubit density `rho_s=(I+s.sigma)/2`, the rank-one identity gives

\[
P(n)\rho_sP(n)=\operatorname{Tr}[\rho_sP(n)]P(n)
              =\frac{1+s\cdot n}{2}P(n).
\]

Consequently

\[
\mathcal J(dn)(\rho_s)=(1+s\cdot n)P(n)\,\mu(dn),
\qquad
p_s(dn)=(1+s\cdot n)\mu(dn).
\]

The density is nonnegative because `|s.n|<=1`, and it is normalized by
`int n dmu=0`. Every branch is completely positive because it has the single
Kraus density `sqrt(2)P(n)`. Its effect density is exactly `2P(n)` and its
normalized successor is the matching pure state `P(n)` wherever the branch
weight is positive. Zero-weight branches need no normalized successor. Normalization follows
from

\[
\int 2P(n)\,\mu(dn)=I.
\]

Within the covariant aligned single-Kraus family `K_n=cP(n)`, normalization
forces `|c|^2/2=1`; therefore `|c|^2=2`, unique up to an irrelevant phase.
That is a conditional uniqueness theorem. The choice that the physical jump
belongs to this aligned self-dual family is not derived.

The unconditioned channel has Bloch action

\[
\Phi(\rho_s)=\int(1+s\cdot n)P(n)\,\mu(dn)=\rho_{s/3},
\]

using `int n_i n_j dmu=delta_ij/3`. It is trace preserving. Applied locally to
one share of a bipartite state, it leaves the remote reduced density unchanged;
for any remote operator `B`, the adjoint maps `I tensor B` to itself because
`int K_n^* K_n dmu=I`. Equality of every remote expectation proves the
partial-trace statement for every bipartite input. This is a local-channel
statement; global microcausality or relativity does not follow.

The runner integrates the actual complex 2-by-2 branch maps with the six-axis
quadrature. Its first and second moments equal Haar moments, so it is exact
for these degree-at-most-two integrands. It is not a replacement of the
atomless mark law by a six-atom process. Completeness is computed from the
actual Kraus products; a Bell-state channel and partial trace are also computed.

## Theorem 3 — first-write algebraic comparison

For comparison, supply the following random-axis formula, historically called
Block 38: draw a Haar axis `a`, then a binary label `b` with

\[
E_b^\lambda(a)=\frac{I+b\lambda a\cdot\sigma}{2},
\qquad
\mathcal I_{a,b}^{\lambda,\kappa}(\rho)
=\operatorname{Tr}[E_b^\lambda(a)\rho]\rho_{\kappa ba}.
\]

Push the two preimages `(a=n,b=+1)` and `(a=-n,b=-1)` to the signed direction
`n=ba`. Their scalar densities add:

\[
\frac{1+\lambda n\cdot s}{2}
+\frac{1+\lambda n\cdot s}{2}
=1+\lambda n\cdot s.
\]

At `lambda=kappa=1`, the output is `P(n)` and the pushed-forward operation is
exactly `J(dn)`. Thus the candidate is the exact first-write pushforward of the
Block-38 endpoint, not merely a match of scalar probabilities.

There is an important boundary: a fresh second Haar jump almost surely does
not reproduce the exact first direction; a singleton has Haar measure zero.
A protocol that retains and reuses a binary axis is an additional second-use
rule. Re-reading an existing permanent Record is also a different operation.
Neither is inherited by this fresh atomless first-write law. This comparison
uses only the displayed formula; it accepts no wider parent theorem.

## Theorem 4 — formation, permanence, and finite capacity

For every open site,

\[
\int [1+\bar r_x\cdot n]\,\mu(dn)=1.
\]

The total local hazard is therefore one and the survival function is
`S(t)=exp(-t)`. For `N` open sites, the next event has total rate `N` and each
site is first with probability `1/N`. Independent continuous exponential
races tie with probability zero. Once a site writes, it never appears in the
generator again, so it holds exactly one permanent Record.

On a finite graph there are at most `|V|` writes. Almost surely all sites
eventually fill and the process stops. **Finite capacity is not recurrence.**
No endless universe, reset law, Record export, or expanding substrate follows.

At each step the exponential race and normalized mark kernel depend only on
the current finite Record map. Those kernels are Borel measurable (the local
Bloch mean is affine in its finite contents), so recursive sampling constructs
the finite Markov process. There are at most as many jumps as initially open
sites; this also prevents explosion.

The rate `1` is a candidate time normalization. No identification with a
kinetic, gravitational or laboratory clock is established here.

## Theorem 5 — Records-only adaptive calibration

For a unit vector `u`, let the actually registered coarse Record event be the
hemisphere

\[
H_u=\{n:n\cdot u\geq0\}.
\]

Normalized Haar geometry gives

\[
\int_{H_u}\mu(dn)=\frac12,
\qquad
\int_{H_u}n\,\mu(dn)=\frac14u,
\]

and hence

\[
p_i=\Pr(n_i\in H_{u_i}\mid\mathcal G_i)
=\frac12+\frac14\bar r_{x_i}(C_{i-1})\cdot u_i.
\]

Here `F_(i-1)` contains the completed past. The exponential race next selects
`x_i`, which generally is **not** `F_(i-1)`-measurable. Let `G_i` contain
that past, the selected site and any test-axis choice made before the mark;
choose `u_i` measurable in `G_i`, without information about the forthcoming
mark. Then `F_(i-1) subset G_i subset F_i`, where `F_i` includes the mark.
The supplied mark law, conditional on `G_i`, is the displayed local density.
Write `X_i=1{n_i in H_(u_i)}` and `D_i=X_i-p_i`. Conditional on `G_i`,
`D_i` has mean zero and lies in `[-p_i,1-p_i]`, an interval of length one.
Conditional Hoeffding therefore gives

\[
\mathbb E[e^{tD_i}\mid\mathcal G_i]\le e^{t^2/8}.
\]

Taking conditional expectation again over the random site gives the same
upper bound conditional on `F_(i-1)`. Since the accumulated prior residual
is `F_(i-1)`-measurable, iteration yields
`E exp(t sum_(i=1)^N D_i) <= exp(N t^2/8)`. Markov's inequality with
`t=4 epsilon` for the upper tail of `sum D_i >= N epsilon`, and with
`-t` for the lower tail, gives

\[
\Pr\left(\left|N^{-1}\sum_{i=1}^ND_i\right|\ge\epsilon\right)
\le 2e^{-2N\epsilon^2}.
\]

This holds for fixed positive `N` no greater than the initial number of open
sites; every such write exists almost surely in this finite unit-rate model.
It is not an unqualified stopping-time or infinite-frequency claim.
For two equally likely selected sites with `s=+u` and `s=-u`, the pre-mark
probabilities are `3/4` and `1/4` while the past-only probability is `1/2`.
The runner enumerates eight two-write coarse histories for disjoint sites
with those six-record neighbor conditions. The second test axis depends on
the first coarse Record, so its probability changes with history. It checks
actual response-function values against the hemisphere integral, conditional
residual means, total probability and the past/site distinction. This is a
finite exact coarse-history control, not a simulated continuum trajectory.

Only Records are sampled and read in this statement. `rho_x`, `p_i`, and the
open-site placeholder are predictive objects computed from earlier Records;
no unrecorded alternative is observed. Repeated Records can therefore test
and estimate this supplied conditional law.

That inference is epistemic, not constitutive: observations do not create the
law, finite histories do not prove an exact probability, and atomless
singletons cannot be calibrated by point frequencies. Positive-area coarse
events or bounded Record functions are the measurable targets.

## What the parameter family establishes

The supplied family

\[
\mathcal I_n^\lambda(\rho)
=\operatorname{Tr}[(I+\lambda n\cdot\sigma)\rho]P(n)\,\mu(dn),
\qquad -1\le\lambda\le1,
\]

is CP: the effect is positive and a positive-effect measure-and-prepare map
is CP (diagonalize the effect and take Kraus operators into the output ray).
It is normalized by the Haar first moment and has matching pure output.
Thus output typing alone does not determine the response parameter.
`lambda=0` is a **typing-only** control: its law does not vary with the
neighbors and it does not satisfy that part of Admissibility. The nonzero
choices `lambda=1/2` and `lambda=1` both vary under the one-Record/six-slot
witness, are positive and normalized, and are covariant local laws on this
supplied domain. They differ, for example, in hemisphere probability
`25/48` versus `13/24` when `s=e1/6,u=e1`.

These are comparisons of supplied finite/local kernels, not complete models
of the four axioms on `Z^3`, and they do not prove full-axiom non-entailment.
Matching Record/output rays alone is weaker than aligning the **effect** ray
with that output and requiring one Kraus density `cP(n)`. Within the latter
family normalization fixes `|c|^2=2`. Choosing that family is still supplied.
Multiplying this finite generator by any positive scalar changes waiting
times without changing conditional marks. No laboratory clock is selected.
There is no general proof here that all seven formerly listed physical
requirements are pairwise independent, nor that this is a smallest model or
smallest additional law clause. Those claims are withdrawn.

The unresolved suppliers are the physical carrier/readability of generic
pure projectors, the neighbor-content access and boundary convention, physical
realization/selection of the aligned instrument, and a relation between its
rate and physical clocks. A one-site diagonal-only readable algebra would
exclude generic off-diagonal Haar projectors; this is a conditional compatibility
boundary, not acceptance of another PR's physical grading hypotheses.
Controlled-copy, retained-context, action-derived and other routes remain open.

## Scope and TOE accounting

Proved exactly, conditionally on the candidate-law clauses:

- one finite neighbor-conditioned Record-forming Markov generator;
- normalized CP first-write operations with matching pure Records;
- exact first-write equality to the Block-38 `lambda=kappa=1` pushforward;
- finite-site permanence and race semantics; and
- adaptive coarse-Record calibration without IID or stationarity.

Not proved:

- derivation of self-duality, the numerical rate, or the neighbor mean from the
  literal axioms, or a full-axiom countermodel establishing non-entailment;
- Block 38's independent same-axis repeat protocol from the pushed-forward law;
- an action, energy conservation, matter spectrum, gravity, continuum limit,
  Lorentz invariance, recurrent cosmology, or experimental fit; or
- any registered TOE obligation retirement.

This is a conditional synthesis of useful formulas. Historical comparisons to
#6368, #6371 and #7827 are preserved for recovery; no new novelty or exhaustive
prior-art verdict is claimed here, and no result from those PRs is needed to
prove the formulas above. No reserved supplier is imported.

## Evidence and recovery

The [correction history](../.claude/science/physics-loops/records-haar-7836-correction-20260909/HISTORY.md)
contains the original 26 bodies and five earlier versions outside active note
discovery. The original cache's 10/0 and 34 named-mutation history are historical:
the original primary could not start on current inputs, and some mutation
checks forced flags rather than testing the mathematical implementation.
The reported independent 7/7 has no recoverable source in this packet and is
unavailable evidence. These results are not credited as fresh validation.

The corrected primary checks the actual functions and exact finite fixtures.
The external correction packet records source-mutant controls, frozen source,
actual input hashes, command and genuine bounded stdout. The live cache binds
the runner, this note and the current axiom memo. Historical custody and dated
PR status are not runtime premises. No independent helper is advertised.

```bash
python3 scripts/records_first_haar_jump_action_admissibility_record_join_2026_09_02.py
```
