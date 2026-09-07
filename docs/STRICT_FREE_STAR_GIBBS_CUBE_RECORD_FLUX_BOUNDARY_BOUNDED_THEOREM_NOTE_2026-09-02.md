# Strict-free star Gibbs / cube Record-flux boundary

## Status and result

**Claim type:** bounded theorem.

**Surface status:** conditional support.

**TOE accounting:** zero obligation retirement and no lane-score change.

**Current correction (2026-09-07):** the construction-level separations below
do not establish pairwise independence of the physical obligations. Historical
packet status and process directions are dated provenance; the
[correction record](../.claude/science/review-fixes/local-gibbs-z3-record-20260907/CORRECTION.md)
states the current source and evidence boundary. No audit grade is assigned.

**Primary runner:**
[`scripts/strict_free_star_gibbs_cube_record_flux_boundary_2026_09_02.py`](../scripts/strict_free_star_gibbs_cube_record_flux_boundary_2026_09_02.py)

There is a sharp, exact distinction between what a diagonal Record probability
formed from an acyclic six-link star can learn and what an ordinary local
occupation Record can learn after a loop-bearing cubic-cell evolution.

On an incident star, every link phase is removable by rephasing the leaves.
Consequently every spectral preparation followed by occupation readout is
blind to the `K0/K1` loop-flux bit. A full finite-star Fock Gibbs state still
produces a positive, normalized, genuinely neighbor-varying law for all 729
neighboring conditions: zero-Record, one-Record, or blank/no Record. It gives an explicit
strict-free witness for the coefficient-to-weight gap that the July 3
restatement had already recognized: scalar link coefficients do not imply
constant Admissibility probabilities.

The blindness can end when the protocol traverses a loop-bearing cell. One common
cube protocol prepares one corner, evolves for one common cadence, asks whether
the opposite corner was reached, and forms the same gated target-site Record
(with an optional common pointer dilation).
It produces Record probability one for `K0` and zero for `K1`. The final effect
is only target-site occupation—a local Record—not an exotic multi-site
observable. The coherence is in the cell-scale evolution between preparation
and readout. This does not select K1; it proves that the action bit is
operationally available under the full supplied protocol: action, unrecorded
preparation, boundary isolation, cadence, occupation instrument/formation,
and post-read gate.

## Supplied objects

Let the center of a seven-mode star be `0`, its leaves be `d=1,...,6`, and

```text
h(t) = sum_d [t_d |0><d| + conjugate(t_d) |d><0|],  |t_d|=1.
H_F(t) = dGamma(h(t)).
```

The graded Fock composition, this candidate action, inverse temperature
`beta>0`, zero chemical potential, the finite incident-star preparation, the
occupation instrument, finite-cube boundary isolation, the cube cadence, and
post-write gating are supplied. An auxiliary pointer dilation is optional and
requires an extra carrier. None is derived from the four minimal axioms or the
approved primitives.

The cube source `|000>` is a supplied unrecorded pre-formation state, not a
permanent occupation Record; the first literal Record in that protocol forms
at the final target-site PVM. Likewise, equations (1) and (2) are adopted as an
action-conditioned stochastic kernel (or as conditional correlations of a
state prepared before Records form). They are not action-alone thermalization
or update dynamics acting on already permanent neighboring Record carriers.

This is a local formation/update rule: the neighboring Record condition labels
the supplied kernel and its next-site outcome distribution. It is not silently
identified with one global equilibrium state.

## 1. Structural tree blindness

With

```text
D = diag(1, conjugate(t_1), ..., conjugate(t_6)),
```

one has `h(t)=D h(1) D*`. Every occupation projector commutes with `D`.
Therefore

```text
f(h(t)) = D f(h(1)) D*
```

for every spectral function `f` defined on this finite spectrum, and all
diagonal occupation probabilities agree for every phase assignment. This is
not a Gibbs-specific accident. A tree has no gauge-invariant phase loop.

The result is strict free matter: `H_F` is quadratic and number conserving.
No density-density term, twisted SWAP, hard-core replacement, fitted effect,
or branch-specific writer is used.

## 2. Exact finite-star Gibbs law

Write

```text
C = cosh(beta sqrt(6)),  S = sinh(beta sqrt(6)).
```

Since `h^3=6h`,

```text
L = exp(-beta h)
  = I + (C-1) h^2/6 - S h/sqrt(6).
```

In the grand-canonical number-conserving Fock Gibbs state, the exact weight of
occupied set `A` is `det(L_A)/det(I+L)`. For a leaf set with `m` occupied
members,

```text
W(center=0,m) = 1 + m(C-1)/6,
W(center=1,m) = C - m(C-1)/6.
```

Their sum is `C+1`, so

```text
P(n_0=1 | m) = [C-m(C-1)/6]/(C+1).                 (1)
```

For every `beta>0`, (1) has full support and varies strictly with the number
of neighboring one-Records. It depends only on the proper-cubic invariant
count, and the tree gauge proves exact equality for the uniform `K0` and
staggered `K1` phase assignments.

At the exact runner fixture `beta sqrt(6)=log 2`, `C=5/4` and

```text
P(n_0=1 | m) = (30-m)/54,
```

with endpoints `5/9` and `4/9`. This temperature is not fitted or physically
selected; the theorem holds for the full positive-beta family.

If `a,z,u` count neighboring one-Records, zero-Records, and blank sites, then
the blank leaves are traced rather than assigned an outcome. Summing their
exact occupied-set weights gives

```text
W0 = 2^u [1+(C-1)(a+u/2)/6],
W1 = 2^u [1+(C-1)(z+u/2)/6],
P1 = [1+(C-1)(z+u/2)/6]/(C+1).                    (2)
```

At `C=5/4`, (2) is `(48+2z+u)/108`. The runner checks all `3^6=729`
conditions and all 24 proper rotations.

## 3. The global-consistency fork

Three meanings of “Gibbs law” must remain separate.

First, (1) is the honest Gibbs conditional of the finite seven-mode quantum
star. But translating (1) to every site does not make it the conditional
system of one positive global nearest-neighbor equilibrium measure. Its
complete-shell odds are

```text
r_m = [6+(6-m)q]/[6+m q],  q=C-1.
```

A count-symmetric positive pairwise nearest-neighbor Markov field on the
triangle-free cubic graph has log-odds affine in `m`, hence must satisfy
`r_0 r_2=r_1^2`. Here

```text
r_0 r_2-r_1^2 = 2 q^3(q+2)/[(q+3)(q+6)^2] > 0.   (3)
```

Second, there is a clean globally consistent escape, but it uses a separate
edge parameter. For a unit two-site hop at inverse temperature `beta_e`, let
`E=cosh(beta_e)`. Its diagonal Gibbs weights are `1` for equal occupations and
`E` for unequal occupations. On any finite graph with a complete binary Record
configuration, multiplying those factors defines the positive classical
measure proportional to `E^(number of disagreeing edges)`, with exact full
conditional

```text
P_edge(n_0=1 | a,z,0) = E^z/(E^a+E^z).            (4)
```

The star fixture `C=5/4` uses `beta_star=log(2)/sqrt(6)`; the edge fixture
`E=5/4` uses `beta_e=log(2)`. Their equal rational values are only a runner
convenience, not a same-temperature identity.

There is also an explicit positive ternary Record-snapshot completion. Give
blank its own state `B` and use a symmetric pair potential with binary block
`psi(0,0)=psi(1,1)=1`, `psi(0,1)=psi(1,0)=E`, and neutral blank couplings
`psi(0,B)=psi(1,B)=R>0`; take any `psi(B,B)>0` (the runner uses `11/10`).
Conditional on the center forming a binary Record,

```text
P_edge(n_0=1 | a,z,u; n_0 != B) = E^z/(E^a+E^z). (5)
```

The product of these positive pair potentials is a consistent finite-volume
static three-state Markov measure on every finite graph. No infinite-volume
phase is selected. Equation (5) does **not** treat blank as an unobserved
binary neighbor. Those semantics do
not cancel: on one binary cube at `E=5/4`, conditioning one neighbor to zero
and marginalizing the rest gives `54875/98523`, not `5/9`. Neither (4) nor (5)
is the quantum state `exp[-beta sum_e H_e]` for noncommuting hopping terms.

This corrects two frozen-contract misses rather than hiding them:
preregistered item 9 reused the star parameter `C` as a same-temperature unit
edge weight, and incorrectly applied binary blank-neighbor cancellation to
`u>0`. The execution separates `E` from `C`; only the `u=0` binary full
conditional survives; and the explicit ternary model in (5) is the corrected
all-`u` alternative.

Third, the honest isolated-cube finite-volume Gibbs state sees flux. On that
eight-site fixture its one-particle Gibbs-kernel diagonals are

```text
(exp(-beta H0))_xx = cosh(beta)^3,
(exp(-beta H1))_xx = cosh(sqrt(3) beta).
```

The beta-squared terms agree, but the beta-fourth coefficients are `21/4!`
and `9/4!`. More directly, the full-Fock partition functions are

```text
Z0 = 256 cosh(3 beta/2)^2 cosh(beta/2)^6,
Z1 = 256 cosh(sqrt(3) beta/2)^8.
```

Their difference begins with `-128 beta^4`; the probability difference for
the literal all-empty configuration Record begins with `beta^4/512`. Thus
local-star equality cannot be promoted to a loop-bearing finite-volume Gibbs
equality. Closing the tree through one elementary square already restores phase sensitivity:
the positive- and negative-flux plaquettes give `(h^4)_00=8` and `4`.

## 4. Literal Record instrument and its permanence boundary

The common occupation PVM has effects `P0=|0><0|` and `P1=|1><1|`. Its CP
branches are

```text
M_b(rho) = P_b rho P_b.
```

Their traces equal (1) or (2), and their normalized local outputs are the
rank-one alternatives `P_b`. Record formation/actualization selects and locks
one branch; that occurrence is supplied by the Record axiom, not derived by
the CP calculation.

On the one-`M2`-per-site realization, the recorded occupation can remain on
the measured site only if a formation-triggered gate ends all incident
hopping. Then the post-write Hamiltonian commutes with `P_b`. An optional
unitary dilation uses a distinct blank/zero/one pointer and controlled swaps;
the runner checks it, but does not pretend that this extra carrier is already
available at the same site.

Only the resulting Records are read. Equations (1), (2), and (5) are model
assignments of probability and support. Repeated Records under independently
supplied stationarity, matched preparation, and sampling assumptions could
estimate and test their frequencies; no finite Record sample proves full
support, and no unrecorded quantum alternative is treated as a direct
measurement.

The gate or a separately licensed carrier is essential. For bare hopping
`H=t c_1^*c_0+conjugate(t)c_0^*c_1`, `[H,n_0]` is nonzero. An occupation on
the still-hopping matter mode is therefore not itself a permanent Record.
The axioms say Records are permanent; they do not supply this Hamiltonian
implementation.

## 5. Common loop-bearing cube evolution with a local target Record

On the one-particle corner space of a unit cube, let

```text
H0 = X1 + X2 + X3,
H1 = X1 + Z1 X2 + Z1 Z2 X3.
```

These Pauli tensors are coordinate-bit notation for the `8 x 8` one-particle
signed nearest-neighbor adjacency, not three physical onsite qubits. The
strict-free matter Hamiltonians are `H_F,j=dGamma(Hj)` on eight physical
site-`M2`/CAR modes. The runner constructs the signed adjacency independently
and checks equality to both displayed matrices before using their algebra.

The `H0` summands commute. The `H1` summands pairwise anticommute and square
to identity, so `H1^2=3I`. Direct link-sign multiplication gives flux `+1`
on every one of the six faces for `K0` and `-1` on every face for `K1`.

Use the same supplied unrecorded source `|000>`, cadence `z`, and two-outcome target-site
occupation PVM in both branches. On the supplied one-particle sector its local
one-effect is `E*=n_(1,1,1)|_(N=1)=|111><111|` and its zero-effect is `I-E*`.
Here `|111>` labels one lattice position, not three occupied onsite qubits.
Then

```text
|<111|exp(-izH0)|000>|^2 = sin(z)^6,
|<111|exp(-izH1)|000>|^2 = 0.                     (6)
```

The first identity follows by factorizing the commuting evolution. The
second follows from
`exp(-izH1)=cos(sqrt(3)z)I-i sin(sqrt(3)z)H1/sqrt(3)` and the fact that
neither `I` nor the one-edge operator `H1` connects opposite corners. At the
common cadence `z=pi/2`, the literal corner Records are disjoint in the needed
sense: `K0` certainly records the target corner and `K1` never does. The
runner also checks an optional common pointer dilation end to end.

Perfect transfer here is a theorem about the isolated eight-vertex cube.
Leaving homogeneous-lattice exterior bonds active invalidates that exact
finite Hamiltonian. Boundary isolation before evolution and the post-readout
gate are supplied protocol operations. Whether the same local Record
discriminator survives on homogeneous infinite `Z^3` is deliberately left as
the next positive route, not assumed here.

All eight corner/opposite-corner pairs obey the same identities. The 24
proper cube rotations permute this protocol family and the six equal face
fluxes. No single prepared corner is misreported as rotation invariant.

## 6. No-go discipline for the narrow negative statement

### N1 — alternative routes

| Route | Status | Result |
|---|---|---|
| finite-star spectral/Gibbs occupation law | ATTEMPTED | exact phase blindness; varying law survives |
| coherent non-diagonal local effects | OPEN | not ruled out by the diagonal theorem |
| loop-bearing cube evolution plus local Record | ATTEMPTED | succeeds on isolated cube by (6) |
| globally consistent edge-factor law | ATTEMPTED | succeeds as binary (4) or ternary (5), remains flux blind |
| homogeneous `Z^3` local-Record propagator | OPEN | removes the cube-isolation import if successful |
| isolated-cube finite-volume Gibbs law | ATTEMPTED | sees flux; equality claim fails |
| thermal point-cone/FSB selector | PRIOR CLAIM | conditionally selects within its stated surface; no audit status imported |
| empirical process tomography | OPEN | needs observed preparation, cadence, and frequencies |
| explicit matter-functional axiom | OUT OF SCOPE | requires owner-approved governance action |

### N2 — wall independence

The following examples separate the stated constructions. They do not
establish that closing one physical obligation can never close another.

| Named obligation | Construction-level separation |
|---|---|
| action selection | both candidate actions support the same star law |
| action-to-probability functional | star exponential and edge factor give different valid laws |
| global consistency | (3) fails for the star law while (4)/(5) pass at their stated semantics |
| dynamical protocol | a static star query is blind while time-separated local target readout (6) sees flux |
| Record permanence | a gated site or extra pointer can persist although active hopping does not |
| clock/preparation | (6) is exact conditional on them but does not generate them |

For every pair of these six named obligations, both full physical implication
directions remain unresolved here. No pairwise-independent or minimal wall
count is established. The finite star/edge compatibility split, static versus
time-separated readout, and gated versus active-hopping persistence examples
retain their displayed hypotheses and conclusions; they are not full models
satisfying all four axioms and all other obligations.

### N3 — hidden-wall scan

The proof checks normalization, support, strict-free CAR typing, number
conservation, phase gauge, all partial neighboring conditions, proper-cubic
covariance, complete-shell compatibility, explicit ternary blank semantics,
the counterexample to binary blank marginalization, same-carrier permanence,
plaquette sharpness, finite-cube isolation, common preparation/PVM/cadence,
and source/prior-art binding. It does not smuggle in branch-specific
temperature or instruments.

### N4 — exact residual

The residual is not “find probabilities.” Equations (1), (2), (4), and (5)
already assign normalized possibilities whose frequencies can be tested
through literal Records under the stated sampling assumptions. The exact
unowned choice is which physical action-to-state/probability functional,
preparation, boundary condition, and cadence the theory licenses. A
star-spectral diagonal law formed before any loop-bearing evolution is blind;
an ordinary local Record after the isolated cell evolution is not.

### N5 — multi-resolution

The executable certificate reports and tests five resolutions:
`per_element` (CAR/edge/face), `per_site` (729 shells), `per_mode` (free
hopping and carrier permanence), `per_block` (star, writer, cube), and
`lattice_wide` (global-consistency and global-Gibbs controls).

### N6 — partial-closure paths

Four positive continuations remain: extend the discriminator to homogeneous
`Z^3`; derive the common evolution/gating protocol from existing structure;
justify the edge-factor functional as the physical update law; or supply an
empirical/owner-approved selector between candidate action-conditioned laws.
The theorem therefore prunes one route and exhibits an escape rather than
declaring a general impossibility.

### N7 — hostile steelman

The strongest objection is correct: a local diagonal effect can see the flux
after loop-bearing evolution, and the isolated-cube Gibbs state is not branch
blind. That objection kills any broad local-Record or thermal no-go. It does
not touch the narrow theorem, because its probability is prepared on an
acyclic radius-one star whose occupation effects are fixed by the leaf gauge.
Equation (6) is retained precisely as the explicit counterexample to
overreach.

### N8 — cross-cycle echo

The July fluxed-ring note already anticipated tree-blind/cycle-sensitive
spectral topology; the July Record normal form already owned generic pointer
writers; the August full-conditional note already owned the Ising-type global
compatibility test; the July 14 predictive-specification tournament already
owned a positive global edge-factor MRF, all 729 Record profiles, and the
remote-dependence warning for partially observed binary neighbors; and the FSB
note already stated its own conditional K1 selection without an effective
audit status imported here. The new contribution is their exact strict-free
joint realization: all 729 local Record conditions, the star/DLR/edge-factor
fork with corrected blank semantics, and one common sharp local target-Record
transcript on the isolated cube. It does not relabel those prior results as
new.

## Consequence for the axiom program

This block supplies an exact action-conditioned witness for an already-recognized
weight gap and identifies a real decision point. Current Admissibility can host (2) as a supplied local
update rule, (4) on completed binary Record conditions, or (5) with explicit
ternary blank semantics. Record can host the local target outcome once
formation and post-write gating are supplied. Neither axiom chooses those
bridges, the isolated evolution used in (6), a physical action, a temperature,
or a clock.

Accordingly this result does not select K1, does not retire `P-KIN` or the
B-BIT, and carries zero obligation retirement. A future axiom update would be
substantive only if it identifies the physical action-to-probability/evolution
map and its operational preparation/cadence; saying merely that neighboring
conditions determine a distribution would restate the current axiom.

## Reproduction

```bash
python3 scripts/strict_free_star_gibbs_cube_record_flux_boundary_2026_09_02.py
```

The runner uses exact SymPy algebra and terminates with a `TOTAL` line.
