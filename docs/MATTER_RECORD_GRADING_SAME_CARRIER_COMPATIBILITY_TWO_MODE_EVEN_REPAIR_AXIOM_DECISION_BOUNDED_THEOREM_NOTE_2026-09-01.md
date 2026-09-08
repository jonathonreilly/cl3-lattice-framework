---
claim_id: matter_record_grading_same_carrier_compatibility_two_mode_even_repair_axiom_decision_bounded_theorem_note_2026-09-01
claim_type: bounded_theorem
claim_scope: "For one complex qubit carrier, the six Pauli-axis rank-one projectors span M_2(C), so any linear grading that fixes all arbitrary-axis readable events is the identity; for the fixed grading Ad(Z), generic random-axis rank-one effects and pure outputs are not even, and the commutant of a full matter M_2(C) on that carrier is scalar. On two qubit modes the fixed-total-parity code span{|00>,|11>} carries an exact logical M_2(C); every logical rank-one projector is parity-even, the displayed full-space binary effect family is positive exactly for |lambda|<=1 and complete, and its measure-and-prepare branches form an even normalized CP instrument with an orthogonal Record pointer and exact same-axis repeatability at lambda=1. On four qubit sites, a supplied typed product with two graded matter factors and two trivially graded Record factors realizes matter CAR and full commuting Record matrices, while an ordinary-product twin has the same abstract one-site M_2(C) presentations, identical even number/Record surfaces, and commuting odd matter generators. One supplied local scalar kernel gives identical 729 neighbor profiles and 1458 two-step histories for both typed finite constructions; those displayed data do not select the cross-site product. No global four-axiom model or covariant lattice-wide role law is constructed. Carrier typing remains additional proposal data rather than a conclusion of that twin. No axiom is amended; the global, matter-only typed, and deferred options remain an explicit owner decision."
runner: scripts/matter_record_grading_same_carrier_compatibility_two_mode_even_repair_2026_09_01.py
runner_cache: logs/runner-cache/matter_record_grading_same_carrier_compatibility_two_mode_even_repair_2026_09_01.txt
claim_grade: unset
audit_status: unset
hard_impact_gate: FAIL
shipping_decision: BACKLOG_NO_PR
axiom_decision_status: AXIOM_DECISION_READY
obligation_retirement: 0
toe_percentage_movement: 0
---

# Matter/Record grading compatibility: the one-carrier trilemma and the two-mode even repair

## Result

Under two explicit identification premises, three properties do not coexist
on one qubit:

1. #7827's separate candidate effect/successor carrier is identified with the
   physical matter carrier, and its effect/output itself must be even-readable;
2. that same `M_2(C)` carries a fixed nontrivial parity grading; and
3. readability means membership in that grading's even algebra.

The linear-algebra incompatibility is exact after those premises. It is not an
unconditional contradiction among the PRs: #7827 does not independently
establish its `M` carrier as retained matter, and #7831 declares operational
evenness rather than deriving it.

There is also a constructive repair. Two physical qubit modes have an even
two-dimensional sector, `span{|00>,|11>}`, which carries a complete logical
qubit. Every logical Bloch projector is even. An arbitrary-axis binary
instrument can therefore be implemented with parity-even effects and outputs,
then written to ordinary binary Record pointers. At the sharp endpoint its
second use returns the same label with probability one.

This supplies one repair of the conditional measurement architecture. It
does **not** derive fermionic
statistics. A graded-matter construction and an ordinary-matter construction
retain the displayed finite local number/Record data and differ in their
cross-site odd relation. This proves nonselection by those data under supplied
roles and products, not a global four-axiom countermodel theorem.

## Authority and execution boundary

The exact runner is
[`scripts/matter_record_grading_same_carrier_compatibility_two_mode_even_repair_2026_09_01.py`](../scripts/matter_record_grading_same_carrier_compatibility_two_mode_even_repair_2026_09_01.py).
Its frozen output is
[`logs/runner-cache/matter_record_grading_same_carrier_compatibility_two_mode_even_repair_2026_09_01.txt`](../logs/runner-cache/matter_record_grading_same_carrier_compatibility_two_mode_even_repair_2026_09_01.txt).

The runner binds the committed preregistration packet, the current minimal
axiom blob, this note, and its own source. It executes exact matrices only.
No generated state or transcript is observational evidence.
The [governing minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.
The [B38 candidate note](../archive/notes/docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md)
is supplied comparison context, not an accepted global model; this runner
reconstructs the relevant effect, parity and product algebra without importing
B38 or B37. The [dated correction overlay](../.claude/science/review-fixes/blocks42-43-20260907/CORRECTION.md)
qualifies the 23 unchanged historical packet bodies and their old status labels.

The compared open-PR heads are:

- PR #7827, `17357c3714c3b3196c6b8fdc9b1a3bb300044181`: the
  arbitrary-axis one-mode Record/matter repeat compiler;
- PR #7829, `551dfd9f317a36db050dffa0d717764f9af9f291`: the
  ordinary-versus-graded matter composition boundary; and
- PR #7830, `f8581d80efdd0856aa1a64078a48931a763765e9`: the
  parity-even readable algebra;
- PR #7831, `ff8573cf054125db0dd0fcf07dba131280b6b736`: the
  one-site even Lüders/Record-cell classification; and
- PR #7832, `9301c509842ea4835def91ad50f41bfd4f80ab1c`: the
  even-sector relocation of cubic response to hopping.

None is treated as merged authority. Their mathematical objects are redefined
and executed here at the intersection needed for the compatibility question.

## Definitions

Let `I,X,Y,Z` be the Pauli basis of `M_2(C)`. For
`j in {x,y,z}` and `b in {-1,+1}` define

```text
P_{j,b} = (I + b sigma_j)/2.
```

A fixed grading is a linear involutive `*-automorphism gamma`. An event is
even when `gamma(E)=E`. The explicit candidate grading is `gamma=Ad(Z)`.

On two qubit modes define

```text
Pi  = Z tensor Z,
P_C = |00><00| + |11><11|,

X_L = |00><11| + |11><00|,
Y_L = -i|00><11| + i|11><00|,
Z_L = |00><00| - |11><11|.
```

For a real unit vector `a`, label `b`, and `|lambda|<=1` define

```text
P_L(a,b) = (P_C + b a.sigma_L)/2,

F_L(a,b;lambda)
  = (P_C + b lambda a.sigma_L)/2 + (I-P_C)/2.

R_b = (I + b Z_R)/2.
```

The complement term is a declared fair completion outside the code. It is
not a claim that non-code input is a faithful logical preparation.

## Theorem 1 — arbitrary one-qubit Records force the grading to be trivial

**Conclusion.** If a linear grading of `M_2(C)` fixes all six
`P_{j,b}`, it is the identity.

**Proof.** For every `j`,

```text
P_{j,+} + P_{j,-} = I,
P_{j,+} - P_{j,-} = sigma_j.
```

The six projectors therefore span `{I,X,Y,Z}=M_2(C)`. A linear map fixing
the spanning family fixes the whole algebra. This proof does not assume that
the grading is inner. It therefore applies to every fixed linear grading on
this carrier. QED.

For the explicit nontrivial grading `Ad(Z)`,

```text
Ad(Z)[(I + lambda(a_x X+a_y Y+a_z Z))/2]
  - (I + lambda(a_x X+a_y Y+a_z Z))/2
  = -lambda(a_x X+a_y Y).
```

At a nonzero response, an effect is even only when its axis lies on the
grading axis. The same calculation applies to the pure branch output. Thus
the literal random-axis one-mode effect/output surface in PR #7827 is not a
one-site parity-even readable surface under PR #7829's fixed grading. PR
#7830's result that only the two grading-axis rank-one projectors are even is
the same local fact; the new result is the exact cross-PR incompatibility.

## Theorem 2 — one qubit cannot hide a separate full Record algebra

**Conclusion.** In the defining two-dimensional representation,

```text
M_2(C)' = C I.
```

Hence a full matter `M_2(C)` and an independent commuting full Record
`M_2(C)` cannot both act faithfully on the same qubit.

**Proof.** Write `Q=q_0 I+q_1 X+q_2 Y+q_3 Z`. The three equations
`[Q,X]=[Q,Y]=[Q,Z]=0` give `q_1=q_2=q_3=0`. QED.

This is a capacity statement, not a statistics theorem. It excludes the
verbal repair “use the same qubit but call one copy matter and the other
Record.” Separate full matrix roles require separate physical qubit sites or
a larger local carrier.

## Theorem 3 — two modes are sufficient and minimal for the even logical repair

**Conclusion.** Within fixed-parity complex qubit modes, two physical modes
are the minimum that can carry an arbitrary parity-even logical qubit.

**Proof.** For one mode the even algebra of any nontrivial grading is
two-dimensional and commutative, unitarily equivalent to `span{I,Z}`. It
cannot contain `M_2(C)`. For two modes the `Pi=+1` sector is the
two-dimensional code `C=span{|00>,|11>}`. The displayed logical operators
satisfy

```text
X_L^2 = Y_L^2 = Z_L^2 = P_C,
X_L Y_L = i Z_L
```

and cyclic permutations, and every one commutes with `Pi`. They therefore
generate a full `M_2(C)` on `C`. QED.

For every unit `a`, `P_L(a,b)` is Hermitian, has trace one,
commutes with `Pi`, and obeys

```text
P_L(a,b)^2 = P_L(a,b).
```

It is a rank-one projector on the code for every Bloch direction, not only
the grading axis.

This is an existence repair, not an instrument-selection theorem. PR #7831
independently shows why that distinction is essential: on a two-mode cell,
even Kraus operators with the same rank-one output admit a four-real-
dimensional effect family and two complete even instruments can have
different effects. The formula below selects one normalized, covariant,
fair-complement instrument; no axiom forces it.

The full-space effect has exact spectrum

```text
spec F_L(a,b;lambda)
  = {(1-lambda)/2, 1/2, 1/2, (1+lambda)/2}.
```

It is positive exactly for `|lambda|<=1`, is parity-even, and obeys
`F_L(a,+;lambda)+F_L(a,-;lambda)=I`.

Let `R_b` be the two orthogonal parity-pointer projectors on a separate
physical Record qubit. Define the branch map

```text
J_b(rho)
  = Tr(F_L(a,b;lambda) rho) [P_L(a,b) tensor R_b].
```

Its Choi matrix is
`F_L(a,b;lambda)^T tensor P_L(a,b) tensor R_b`, hence is positive. The
pointer projectors are orthogonal and exhaustive. The two branch traces sum
to `Tr(rho)`, so `{J_+,J_-}` is a normalized CP instrument whose outcome
is literally stored in a Record qubit. Both the effect and output are even.
For global grading use `Pi_out=Pi tensor Z_R`; for a trivially graded typed
Record carrier use `Pi_out=Pi tensor I_R`. The displayed pointer commutes
with both choices, and in either case

```text
J_b(Pi rho Pi) = Pi_out J_b(rho) Pi_out.
```

At `lambda=1`, a second use on `P_L(a,b)` gives the same effect with
probability one and the opposite effect with probability zero. This is the
exact arbitrary-axis parity-even replacement for the one-mode writer.

A supplied projective logical lift of the proper cubic group acts on
`(X_L,Y_L,Z_L)` by all 24 oriented signed permutations. The runner constructs
all 24 even unitary representatives exactly. Their matrices close only up to
code-space phase, as expected for a spin lift; all 576 pair products are
checked for exact closure of the induced conjugation action on the logical
algebra, not equality of the chosen unitary representatives. Because the
induced maps preserve dot and cross products, they preserve Pauli
multiplication and carry `P_L(a,b)` and `F_L(a,b;lambda)` to the
corresponding rotated-axis objects. The internal code formula selects no
spatial direction. Choosing and transporting the two physical lattice sites
that realize an apparatus is a separate covariance problem; the logical lift
is not claimed to be the tensor square of the one-site rotation action.

## Theorem 4 — finite typed products share the displayed local data

Use four physical qubit sites: two matter carriers `m_0,m_1` and two Record
carriers `r_0,r_1`. This is not an enlargement of the one-site algebra; every
site still carries `M_2(C)`.

In one matrix representation of the graded candidate,

```text
c_0 = sigma_- tensor I,
c_1 = Z tensor sigma_-
```

on the two matter factors. The `Z` in the second line is a representation of
the graded product, not a physically selected site order. Exact execution
gives

```text
{c_0,c_1}=0,
{c_0,c_1^dagger}=0,
{c_j,c_j^dagger}=I.
```

The two Record factors carry the trivial grading. Every matrix in each Record
`M_2(C)` is even, distinct Record algebras commute, and they commute with
the even matter number operators.

The ordinary twin uses

```text
d_0 = sigma_- tensor I,
d_1 = I tensor sigma_-.
```

Now `[d_0,d_1]=0` and `{d_0,d_1}!=0`. Nevertheless

```text
c_j^dagger c_j = d_j^dagger d_j
```

for both sites, and the Record carrier matrices are identical. Thus every
site has the same abstract `M_2(C)` possibility presentation, while the even
number projectors, binary Record matrices, and the symbolic local
number/Record effect expectations executed here are identical. The embeddings of the odd local
generators are not identical matrices; their cross-site relation is exactly
what differs.

The runner derives rather than inserts the dimension. The 16 ordered
monomials generated by the two matter-mode bases have vectorized rank 16 in
both candidates; each full Record basis has rank 4. Tensor independence gives
`16*4*4=256` for both four-qubit presentations. On the generic diagonal
state with matter occupations `p_0,p_1` and Record occupations `q_0,q_1`,
the four local number/Record effects return exactly those same four symbols
in both candidates.

### Supplied local kernel and finite histories

The finite comparison uses a scalar local candidate rule motivated by the
Record sentences; keyword compatibility is not a proof of all four axioms.
For a center and six neighbors, use two parity-projector Record labels and
encode each neighboring condition as

```text
-1 = no Record, 0 = Record P_0, 1 = Record P_1.
```

For a blank center and its ordered six-neighbor tuple `s`, define the one
fixed local candidate probability rule

```text
p(P_1 | s) = [1 + sum_d (s_d+1)]/14,
p(P_0 | s) = 1 - p(P_1 | s).
```

Across all `3^6=729` neighboring conditions these probabilities lie
strictly between zero and one, sum to one, and vary from `1/14` to
`13/14`. The rule contains no site coordinate and depends only on the
symmetric neighbor sum; the runner checks invariance under all 24
proper-cubic permutations of the six directions. A forming Record locks the
sampled `P_0` or `P_1`; an already locked value is returned unchanged,
and a blank has no readout. The runner executes all 1,458
formation-then-re-read two-step local histories. It does not execute a global
asynchronous formation schedule.

Attach the same local table and formation/re-read steps to the two supplied
finite typed products. They have identical displayed local data while their
odd generators commute in one and anticommute in the other. This comparison
does not construct a global formation schedule or a covariant lattice-wide
matter/Record role law, and therefore does not establish two complete models
of the four axioms. The scalar rule's direction-permutation covariance is
separate from covariance of the supplied carrier roles and product embeddings.

The typed graded algebra is nonempty and exact. These finite local observations
do not select it over the ordinary candidate. A global nonselection theorem
would require full models satisfying the actual Admissibility/Record semantics.

## What this changes in the active PR stack

| surface | exact consequence |
|---|---|
| PR #7827: arbitrary-axis one-mode successor | Its separate candidate `M` is not already retained matter. If an owner identifies it with fixed-graded Matter and requires its effect/output to be even-readable, the literal one-site form fails; otherwise the pointer-only/separate-carrier route remains live. |
| PR #7829: Candidate Q | Algebraically consistent, but it changes the measurement/Record architecture. Candidate Q does not by itself supply apparatus placement or Record/matter role typing. |
| PR #7830: even readable algebra | Its one-site restriction is confirmed; the two-mode code supplies the earliest full arbitrary-axis logical qubit while remaining even. |
| PR #7831: one-site Lüders/Record cell | Its one-site uniqueness is compatible with Theorem 1. Its explicit two-mode nonuniqueness prevents this note from promoting the repair instrument to a derived law. |
| PR #7832: cubic response relocation | Its scalar one-site result confirms the incompatibility beyond measurement, while its six-dimensional hopping response leaves a separate channel-selection problem after relocation. |
| exchange/`GL_F` routes | May test a supplied statistics law, but do not select which abstract carrier is physical matter without an identification clause. |

This is route-decision progress: five open surfaces now have one explicit
compatibility contract and a tested repair. The constituent algebra overlaps
prior retained work, so the post-execution novelty audit does not grade the
package as hard impact. It is not obligation retirement because the remaining
choice is constitutional.

## Owner decision matrix

### Option G — global grading

Declare one fixed matter parity per qubit mode and graded composition across
all quantum modes. One-site readable quantum events are restricted to the
fixed parity PVM. Arbitrary-axis quantum states, effects, and writers use the
two-mode even apparatus above; final binary Records can still be ordinary
parity bits.

This is the smallest single product-law clause and avoids a new carrier-role
predicate. Its price is broad migration: the literal one-site arbitrary-Bloch
reading in PR #7827 and every similar lane must be recompiled into an encoded
multi-site statement. PR #7832 adds that the first-order cubic response also
moves to a multi-site hopping channel whose equivariant family has six
parameters; the grading does not select one of those parameters.

### Option M — matter-only typed grading

Declare that matter-role factors compose by the graded product while
Record/apparatus factors are trivially graded. This preserves a full readable
Record `M_2(C)` and makes matter CAR local on its supplied surface.

It is less disruptive to existing Record writers, but it costs more law data:
the framework must say what physically distinguishes a matter carrier from a
Record carrier, how roles are assigned without privileging lattice sites, and
how the product behaves when a Record forms. A static checkerboard typing
would break the stated translation symmetry; a dynamic typing needs a
history-indexed algebra/product rule. That rule is not supplied or executed
here.

### Option D — defer composition

Adopt neither clause. Keep ordinary and graded matter chains conditional and
use each only behind an explicit dependency. This makes no migration mistake,
but it cannot close the matter-statistics or downstream action-functional
lanes.

## Recommendation

At the finite-algebra level, Option G uses the fewest new clauses because the
two-mode even apparatus removes its apparent inability to express arbitrary
quantum questions. It is not yet a lattice-wide winner: a covariant placement
and transport law for those multi-site apparatuses is still missing. For
minimum near-term repository migration, Option M is attractive, but only
after a covariant role-assignment/product rule is actually constructed.
Option D remains the honest default until the owner makes an explicit owner
decision.

The next high-leverage test, if Option M is preferred, is not another exchange
experiment. It is a finite history-indexed consistency campaign: form a Record,
change the carrier's role, and test associativity, locality, translation
covariance, and preservation of all earlier Record algebras. Failure there
would favor Option G; success would make Option M an exact competing clause.

## No-go discipline and retained positive routes

The complete post-execution N1–N8 audit is bound in
[`POSTEXECUTION_NO_GO_AUDIT.md`](../.claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/POSTEXECUTION_NO_GO_AUDIT.md);
the corrected novelty disposition is in
[`POSTEXECUTION_NOVELTY_AUDIT.md`](../.claude/science/physics-loops/toe-source-eta-ownership-block43-matter-record-grading-compatibility-decision-20260901/POSTEXECUTION_NOVELTY_AUDIT.md).

This note does not claim that fermions, arbitrary measurement, or a TOE are
impossible. The positive routes retained are:

1. global grading plus the exact two-mode even apparatus;
2. matter-only grading plus a future covariant role law;
3. a rotation-covariant real Clifford carrier;
4. deferred conditional products; and
5. empirical identification of a framework carrier with known fermionic
   matter followed by calibrated use of the selected candidate.

The span/commutant calculation, even-code construction and ordinary/graded
finite comparison establish their stated conditional results. They do not prove
pairwise independence among local grading, product, roles, apparatus capacity,
event class, state, dynamics, functional and physical identification. No
independent-wall count or minimal assumption set is claimed. Relations between
these remaining obligations are unresolved unless a displayed construction
establishes that particular direction under the same assumptions. Historical
N2 labels such as “current-axiom semantic twins” are narrowed by the dated
overlay to the finite table/typing scope above. The prior instrument alternatives
remain comparisons, not new independence proofs or accepted parent campaigns.

## Scope limits

- No graded product, role typing, state, Hamiltonian, action, matter
  functional, exchange sign, or physical carrier identification is derived
  from the four axioms.
- The two-mode result is a finite fixed-parity complex-qubit theorem; it is
  not a universal minimum over arbitrary real or higher-dimensional carriers.
- The 24 exact logical cubic lifts do not derive a translation- and
  rotation-covariant placement or pairing of apparatus sites on `Z^3`, nor do
  they repair the one-site complex-grading covariance wall by themselves.
- The four-site typed algebra and 1,458 local histories are finite constructions,
  not full four-axiom models or a covariant dynamic role law on `Z^3`.
- A Jordan-Wigner matrix representation is used to execute the graded
  relations; its order is not promoted to physical content.
- No axiom text, primitive registry, audit surface, ledger, obligation, or TOE
  score is changed by this note.

## Reproduction

Run:

```bash
python3 scripts/matter_record_grading_same_carrier_compatibility_two_mode_even_repair_2026_09_01.py
```

The green result must end in `TOTAL: PASS=10 FAIL=0`. The runner also executes
all 31 hostile mutations and requires every designated gate to reject its
mutation.
