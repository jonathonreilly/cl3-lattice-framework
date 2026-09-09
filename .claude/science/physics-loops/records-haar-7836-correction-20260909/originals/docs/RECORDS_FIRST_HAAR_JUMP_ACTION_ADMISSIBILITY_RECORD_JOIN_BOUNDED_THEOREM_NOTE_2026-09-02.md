# Records-first Haar-jump action / Admissibility / Record join

Date: 2026-09-02
Status: exact bounded composite; componentwise prior art; below PR value gate
Base: `origin/main@2cea9a595ee2f0a6c47096de6f821b905182f48c`

## Result in one sentence

There is a smallest explicit finite-volume Markov law in which neighboring
pure Record contents determine a predictive qubit density, one normalized
self-dual Haar jump both selects and physically writes a matching pure Record,
and subsequent Record events calibrate the conditional probabilities without
IID assumptions; however, the self-dual clause and its unit rate are candidate
physical law, not consequences of the current four axioms.

This is a positive construction and useful decision map, not new retained
science or TOE closure. It records **zero obligation retirement and zero
TOE-percentage movement**.

## Prior-art stop

A hostile search after execution found that open PR `#6368` at
`a4a7140f0921e70e119b9d641452aa5017a413a6` already owns the exact arithmetic
six-content decoder with open neighbors represented by `I/2`, including its
positivity, covariance, and uniform-weight boundary. Open PR `#6371` at
`b1912555b31c8fa89d3d0af7b11bcd0a01ec6181` already owns the general
normalized Borel-mark pure-birth Record generator, exponential races,
append-only permanence, and even a finite-seed full-lattice process theorem.
Block 38/PR `#7827` owns the sharp random-axis first-write endpoint.

The only remaining assembly delta here is the Records-filtration martingale
calibration. That is correct, but it is a standard conditional-probability
consequence and does not pass the program's V2/V5 high-value gate. The block is
therefore packaged as a duplicate-aware checkpoint, with no PR.

There is also a live compatibility fork with open PRs `#7830-#7831`. Under
their declared one-site parity-even readability hypothesis, the only readable
rank-one projectors are the two fixed diagonal directions. Generic Haar
`P(n)` contains odd/off-diagonal content. This block is therefore an
alternative ungraded physical-matter candidate unless its Record is lifted to
a multi-site even logical carrier. It does not silently consume that open
grading hypothesis.

## Premise tiers

The result keeps four logically different layers separate.

1. **Literal current axioms.** Lattice, Qubit, Admissibility, and Record are
   read exactly from `MINIMAL_AXIOMS_2026-06-29.md`. In particular, the
   Admissibility probability sentence is interpretive and non-governing, and
   the memo does not supply the formation site, probability, or rate.
2. **Records-first interpretation.** Physical possibilities in the
   physical-matter Record subsort are qubit-state alternatives; only Records
   are sampled and read; probabilities and possibility support are inferred
   epistemically from repeated Records. This must not be broadened to identify
   all of `M_2(C)` with the density body.
3. **Mathematics.** Convexity, normalized Haar moments, rank-one projector
   identities, finite exponential races, and martingale concentration are
   derived once their objects are supplied.
4. **Candidate physical law.** Unrecorded neighbors contribute `I/2`, the
   affine neighbor map is the arithmetic mean, the jump is aligned and
   self-dual, and its rate is one in lattice-time units.

No canonical axiom text is changed by this block.

## The candidate law

Let `G=(V,E)` be a finite nearest-neighbor cubic subgraph. A site is either
open or carries one permanent pure-state Record

\[
P(n)=\frac{I+n\cdot\sigma}{2},\qquad n\in S^2.
\]

For an open site `x`, let a recorded neighbor contribute its projector and an
open neighbor contribute `I/2`. Define

\[
\rho_x(C)=\frac16\sum_{y\sim x}\rho_y(C)
          =\frac{I+\bar r_x(C)\cdot\sigma}{2},
\qquad
\bar r_x(C)=\frac16\sum_{y\sim x}r_y(C),
\]

where `r_y=n_y` for a Record and `r_y=0` for an open neighbor. With normalized
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
\lVert\bar r_x\rVert\leq\frac16\sum_{y\sim x}\lVert r_y\rVert\leq1.
\]

Therefore the two eigenvalues `(1+-|bar r_x|)/2` are nonnegative and the trace
is one. The all-open condition gives `bar r_x=0`; hence it introduces no
preferred qubit direction and still nucleates Records uniformly.

The arithmetic mean is invariant under every proper-cubic permutation of the
six neighbor slots and is equivariant under a common qubit-frame rotation. It
is translation independent and varies: one `+x` Record among five open
neighbors gives `bar r=e_x/6`, whereas the all-open condition gives zero.

The stated uniqueness is deliberately narrow. In the **affine/transitive
class** of neighbor maps that (i) commute with every common internal rotation,
(ii) treat the proper-cubic orbit of six slots transitively, (iii) send the
all-open tuple to zero, and (iv) reproduce a constant six-neighbor Bloch
vector, Schur covariance makes each linear block scalar, transitivity makes
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
normalized successor is the matching pure state `P(n)`. Normalization follows
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
this is only a one-operation no-signaling check, not a derivation of global
microcausality or relativity.

## Theorem 3 — exact relation to Block 38

Block 38 draws a Haar axis `a`, then a binary label `b` with

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
Block 38's operational repeatability reuses its retained binary axis while
excluding the first Record from the second causal parent set. That latent-axis
repeat protocol is not inherited by the pushed-forward one-write process.

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

The rate `1` is a candidate time normalization. The current axioms and
approved primitives do not identify it with a kinetic, gravitational, or
laboratory clock.

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
p_i=\Pr(n_i\in H_{u_i}\mid\mathcal F_{i-1})
=\frac12+\frac14\bar r_i\cdot u_i.
\]

Here the event site and axis `u_i` may be any predictable functions of the
past Record history `F_(i-1)`. Let `X_i=1{n_i in H_(u_i)}`. Then

\[
D_i=X_i-p_i,
\qquad
\mathbb E[D_i\mid\mathcal F_{i-1}]=0,
\qquad
D_i\in[-p_i,1-p_i].
\]

Thus the residuals are martingale differences even though neighboring
conditions evolve and the Record sequence need not be independent or
stationary. Conditional Hoeffding and iteration give

\[
\Pr\left(\left|\frac1N\sum_{i=1}^ND_i\right|\geq\epsilon\right)
\leq2e^{-2N\epsilon^2}.
\]

Only Records are sampled and read in this statement. `rho_x`, `p_i`, and the
open-site placeholder are predictive objects computed from earlier Records;
no unrecorded alternative is observed. Repeated Records can therefore test
and estimate this supplied conditional law.

That inference is epistemic, not constitutive: observations do not create the
law, finite histories do not prove an exact probability, and atomless
singletons cannot be calibrated by point frequencies. Positive-area coarse
events or bounded Record functions are the measurable targets.

## What is and is not forced

The exact family

\[
\mathcal I_n^\lambda(\rho)
=\operatorname{Tr}[(I+\lambda n\cdot\sigma)\rho]P(n)\,\mu(dn),
\qquad -1\leq\lambda\leq1,
\]

is normalized and completely positive for every displayed `lambda`, and every
branch writes the matching Record `P(n)`. Therefore **records-first typing
alone does not force lambda**. In particular, `lambda=0` and `lambda=1` share
the same output attachment but have different response to the input state.

The strongest same-referent clarification of the user's ontology can identify
Block 38's successor with the locked physical-matter Record and thereby force
`kappa=1`:

\[
\operatorname{lock}(F_{a,b})=M_{a,b}=P(ba).
\]

It still does not force the response parameter or the independent second-use
law. Re-reading the same permanent Record is not a new interrogation.

The equality between outcome effect ray and output Record ray—together with a
single aligned rank-one Kraus density—is what sets `lambda=1` here. This
**self-dual outcome-effect clause is a candidate physical law, not an axiom
consequence**. Likewise, the unit rate is supplied by the candidate generator.

## Smallest owner decision surface

No decision is required to preserve the mathematical result. If the program
wants the records-first interpretation made exact, the narrow safe
clarification is:

> For the physical-matter Record subsort, a branch Record with content `P(ba)`
> locks the exact physical successor used by a later interrogation:
> `lock(F_(a,b)) = M_(a,b) = P(ba)`.

This is deliberately not the sentence “`M_2(C)` is the density-state space.”
Current work uses the full algebra as a larger carrier and the density body as
a restriction.

If the program instead wants this particular candidate dynamics, the smallest
law clause is:

> At an open site, the physical Record-forming operation has the covariant
> aligned rank-one density `J_x(dn)(rho)=2P(n)rho P(n)mu(dn)` evaluated on the
> arithmetic mean of the six neighboring Record states, with an open neighbor
> represented by `I/2`; its coefficient defines one unit of local lattice time.

Adopting that sentence would supply a physical law. It would not constitute a
derivation from the existing axioms, and no new axiom is proven mandatory:
controlled-copy, action-derived, objective-collapse, deterministic-history,
and other routes remain logically live.

## No-go discipline audit

The only negative result is a **countermodel to entailment only**: the current
axioms plus records-first typing do not select `lambda=1` or the rate. It is not
a no-go for Record physics or Born-type laws.

### N1 — Alternative routes

Direct registered partitions, positive effect functionals, self-dual
instruments, supplied controlled-copy writes, objective jumps, infinite Record
export, deterministic histories, and action-derived kernels were considered.
The present construction positively realizes the self-dual objective-jump
route; the others are not declared impossible.

### N2 — Wall independence

State typing, output/Record attachment (`kappa`), outcome-effect response
(`lambda`), formation hazard, permanence, same-axis second use, and empirical
calibration are independent statements. The normalized family above varies
`lambda` while holding matching output fixed. Multiplying the generator by a
positive constant varies the rate while preserving conditional content.

### N3 — Hidden-wall scan

The construction openly imports the density-body restriction, normalized Haar
measure, the open-neighbor `I/2` placeholder, a common internal frame,
self-duality, a lattice-time unit, finite capacity, and a global finite-volume
race construction. It does not hide a reset, boundary bath, latent repeat
axis, expanding lattice, or relativistic causal theorem.

### N4 — Residual matching

The literal axiom residual is the absent cross-carrier equality and absent
formation/update law. The Block-38 residual is its supplied `lambda`, `kappa`,
and repeat protocol. The finite-process residual is recurrence/export. The
calibration residual is empirical identification of a supplied conditional
law, not existence of probabilities.

### N5 — Rhetoric audit

The cached runner must print a dedicated `N5_rhetoric: PASS` line plus
per-element, per-site, per-mode, per-block, and lattice-wide scope lines. The
result says “not entailed by these premises,” never “impossible,” “a new axiom
is the only repair,” or “all derivations fail.”

### N6 — Partial-closure paths

The positive finite local law, its exact Block-38 first-write equivalence, its
formation semantics, and its adaptive calibration remain valid even though
axiom entailment fails. A same-referent owner clarification can close only
`kappa`; an action derivation could still select the self-dual kernel or rate.

### N7 — Steelman

Under the strongest intended records-first reading, the first Record and the
physical successor are the same pure possibility, so `kappa=1` is definitional.
Even on that reading, permanence of the old Record does not specify a new
causally independent interrogation. The friendly `lambda=kappa=1` endpoint is
preserved as the candidate, not treated as incoherent.

### N8 — Cross-cycle echo

The June controlled-copy note already realizes matching projectors inside a
supplied reversible model; the July autonomous-instrument note already
classifies supplied activation/instrument choices; the IID frequency bridge
and post-Record concentration interface already separate data from formation;
Block 38 already supplies the random-axis response/repeat family. Open PRs
`#6368` and `#6371` own the exact neighbor decoder and the more general marked
pure-birth process. Together these surfaces own every nonstandard component;
the adaptive non-IID calibration is a standard theorem-level wrapper. None is
promoted from `unaudited`, `conditional`, or unlanded custody here.

## Scope and TOE accounting

Proved exactly, conditionally on the candidate-law clauses:

- one finite neighbor-conditioned Record-forming Markov generator;
- normalized CP first-write operations with matching pure Records;
- exact first-write equality to the Block-38 `lambda=kappa=1` pushforward;
- finite-site permanence and race semantics; and
- adaptive coarse-Record calibration without IID or stationarity.

Not proved:

- derivation of self-duality, the numerical rate, or the neighbor mean from the
  literal axioms;
- Block 38's independent same-axis repeat protocol from the pushed-forward law;
- an action, energy conservation, matter spectrum, gravity, continuum limit,
  Lorentz invariance, recurrent cosmology, or experimental fit; or
- any registered TOE obligation retirement.

Accordingly the block is meaningful candidate-law compression and an exact
axiom/law decision surface, but it fails the new-science PR gate and is not a
completed end-to-end TOE lane. The next high-leverage route must couple a
physical action to an independently testable formation-rate/content relation,
not add another marked-generator variant.

## Reproduction

```bash
python3 scripts/records_first_haar_jump_action_admissibility_record_join_2026_09_02.py
python3 scripts/records_first_haar_jump_action_admissibility_record_join_2026_09_02.py --list-mutations
```

Expected baseline tail:

```text
TOTAL: PASS=10 FAIL=0
```
