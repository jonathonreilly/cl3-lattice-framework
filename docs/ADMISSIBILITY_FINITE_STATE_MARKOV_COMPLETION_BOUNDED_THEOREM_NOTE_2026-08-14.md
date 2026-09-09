# A finite-state Markov completion for one supplied Record law

Date: 2026-08-14 (corrected 2026-09-09 after focused review of original PR
6347)

**Authority:** none

**Audit:** unset

**Type:** bounded_theorem

**Status:** corrected conditional finite theorem. The displayed local response,
Pauli action, synchronous product scheduler, and finite initial Record map are
supplied mathematical choices. No physical law is selected or adopted.

**Primary runner:**
[`frontier_admissibility_finite_state_markov_completion_2026_08_14.py`](../scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py)

**Independent check:**
[`frontier_admissibility_finite_state_markov_completion_independent_check_2026_09_09.py`](../scripts/frontier_admissibility_finite_state_markov_completion_independent_check_2026_09_09.py)

**Execution evidence:**

- primary cache:
  `logs/runner-cache/frontier_admissibility_finite_state_markov_completion_2026_08_14.txt`
- independent cache:
  `logs/runner-cache/frontier_admissibility_finite_state_markov_completion_independent_check_2026_09_09.txt`

The primary imports the corrected current Block84 helper and declares that
helper's complete text-input closure. The checker reconstructs the decisive
finite geometry and normalization without importing Block84. Both are bounded
support for the proof below; finite enumeration does not by itself prove the
standard-Borel statements.

The supplied formulas come from the corrected
[Block84 note](ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md).
The current [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) provide the comparison
surface. They do not supply the response values, spatial-to-Pauli action,
product scheduler, initial state, or physical clock used below. The other
Block84 text inputs are package-local comparison sources and add no physical
premise to this result.

## 1. Supplied finite kernel

Let `D` be a finite subset of `Z^3` and let a Record state be a map

```text
R : D -> M_2(C).
```

Old matrix contents may be arbitrary. Write `o_D(x)=1` when `x` is in `D`
and zero otherwise. For the three positive coordinate vectors `e_i`, define

```text
d_D(x)_i = o_D(x+e_i) - o_D(x-e_i),
F(D) = {x not in D : x is adjacent to D and d_D(x) != 0}.
```

For `x` in `F(D)`, put `k=|d_D(x)|^2`, so `k` is one of `1,2,3`. The supplied
linear response uses

```text
P_s(d) = (I + s d.sigma/sqrt(k))/2,
p_s(d) = (1 + s sqrt(k)/3)/2,       s in {-1,+1}.
```

For a sign assignment `s:F(D)->{-1,+1}`, the output `T_s R` copies every old
Record and appends `P_{s(x)}(d_D(x))` at each forming site. The displayed
transition kernel is

```text
K(R, .) = sum_s [ product_{x in F(D)} p_{s(x)}(d_D(x)) ] delta_{T_s R}(.).
```

This formula reads one frozen prestate and supplies conditional independence
across its forming sites. It is one candidate completion of the Block84 local
law. Conditional independence, synchrony, and physical outcome actualization
are not derived here.

## 2. Finite frontier and normalization

Every candidate is one of the at most six nearest neighbors of a point of
`D`. Therefore

```text
F(D) intersect D = empty,       |F(D)| <= 6|D|.
```

For every nonzero `d` in `{-1,0,1}^3`, the Pauli identity gives

```text
(d.sigma)^2 = |d|^2 I.
```

Thus `P_+(d)` and `P_-(d)` are distinct complementary rank-one projectors.
Since `k<9`, both displayed weights are strictly positive and their sum is
one. The product kernel consequently has exactly `2^|F(D)|` distinct atoms
and total mass one. When `F(D)` is empty, the empty product gives the single
identity atom. Every update copies old contents exactly, so Record permanence
holds for this candidate.

The primary checks all 26 nonzero local directions, explicitly sums the 64
atoms from the origin seed, and tests 128 finite domains on a seven-site host.
Those checks test the implementation. The preceding formulas carry the
general finite-domain result.

## 3. Standard-Borel Markov interface

The set of finite subsets of the countable lattice is countable. For fixed
finite `D`, the content space `M_2(C)^D` is finite-dimensional and Polish.
Hence the disjoint union

```text
X_fin = disjoint_union_{D finite subset Z^3} M_2(C)^D
```

is standard-Borel.

On a fixed `D` stratum, `F(D)`, the weights, and the appended matrices are
fixed. Each atom map is the identity on old matrix coordinates and constant
on appended coordinates, so it is Borel. A finite weighted sum of these atom
maps is a Borel probability kernel on that stratum; the countable stratum
partition makes `K` a Borel kernel on `X_fin`.

Repeating the same `K` at each integer step makes the mathematical chain time
homogeneous. Given any initial probability measure on `X_fin`, the standard
iterated-kernel construction gives consistent finite cylinders and a path
measure. This conclusion supplies neither an initial physical state nor a
physical draw mechanism. The step label is an iteration ordinal, not a
duration, clock, rate, causal metric, or Lorentzian interval.

## 4. Conditional spatial covariance

Let `G=(a,Q)` act on sites by `Gx=a+Qx`, where `Q` is a determinant-one
signed permutation of the coordinate axes. Direct substitution gives

```text
d_{GD}(Gx) = Q d_D(x),       F(GD) = G F(D).
```

The weights depend only on `|d|^2`. Under the supplied Block84 Pauli lift
`U_Q`, the projector identity is

```text
U_Q P_s(d) U_Q^* = P_s(Qd).
```

Therefore pushing forward every old matrix by the same conjugation and every
site by `G` transports the complete finite-atomic kernel. The projective sign
of the lift cancels under conjugation. This is covariance conditional on the
supplied spatial-to-Pauli action; it does not derive or uniquely select that
action.

## 5. Growth and propagation for finite states

Suppose `D` is finite and nonempty. Choose `y` with maximal first coordinate
and let `x=y+e_1`. Both `x` and `x+e_1` are outside `D`, while `x-e_1=y` is
inside. Hence

```text
d_D(x)_1 = -1,
```

so `x` belongs to `F(D)`. Every nonempty finite state therefore has a forming
site under this exact full-lattice formula. This is a positive growth lemma
for the displayed candidate. It says nothing about arbitrary infinite
states, finite-resource laws, altered formation predicates, or other
kernels.

Every new candidate is adjacent to the old domain. Induction then bounds the
distance reached after `n` iterations by `n` lattice edges from the initial
domain. No physical speed follows without a supplied duration and causal
interpretation.

## 6. Scheduler and boundary controls

With the prestate frozen and branch signs fixed, writes have distinct targets
and do not read one another. Their append order therefore commutes. An actual
different operand gives the scheduler control: start from the origin, append
the lexicographically first one of its six candidates, and immediately
recompute against the changed domain. Five new distance-two sites appear
inside that same update. Dynamic recomputation is a different law; no forced
Boolean flag is credited as a scientific mutation.

On the supplied twelve-site two-cube patch, the restricted frontier fills in
waves

```text
3, 4, 3, 1, 0.
```

Embedding the same filled state back into the full lattice exposes 32 forming
sites outside the patch. The restricted halt is therefore a boundary fact of
that fixture. It is not a full-lattice horizon, resource-exhaustion theorem,
late-time fixed point, or physical causal boundary.

## 7. Selection and physical boundary

The finite construction does not select its supplied law. Block84 also gives
a positive normalized cubic response on the same projectors. A common-sign
correlated kernel can share the product kernel's one-site mean while having a
different history variance. Spatial covariance and local marginals therefore
do not by themselves choose the linear product response.

Established here:

- a finite frontier and `6|D|` bound for every finite Record domain;
- a normalized finite-atomic Borel kernel on the finite Record-map space;
- exact copying of old matrix contents and supported appended projectors;
- conditional translation and proper-cubic covariance;
- consistent finite histories for any supplied initial probability measure;
- the finite-state growth lemma and one-edge-per-iteration propagation;
- fixed-prestate append commutativity and actual dynamic inequivalence; and
- the exact twelve-site boundary artifact.

Not established here:

- an adopted or uniquely selected physical law;
- derivation or selection of the spatial-to-Pauli action;
- physical synchrony, conditional independence, or outcome actuality;
- a physical initial state, capacity law, or process from arbitrary infinite initial states;
- physical time, energy, stress, source normalization, or gravity;
- an axiom or approved-primitive change; or
- audit retention, obligation retirement, or TOE percentage movement.

The August 14 portfolio percentages, then-current audit counts, route ranking,
twenty-one-pair wall table, and claim that no retirement mechanism was missed
are preserved in the historical packet. They are not current theorem results
and carry no present governance authority.

## 8. Reproduction and status

Run the primary once and then the independent checker under the declared
30-second/2-GiB external bounds. Both emit predicate-derived standard totals.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "one supplied finite-state Markov kernel and its exact finite growth, covariance, scheduler, and boundary consequences"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "general finite-domain proofs with bounded implementation checks and an independent finite reconstruction"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

No audit has run. Audit status remains unset, consistent with the
campaign direction to defer formal audit until there is a solid TOE candidate.
