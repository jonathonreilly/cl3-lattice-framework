# The shape is a Hankel spectrum, and no formula was ever possible: s(k) derived — Cycle 933

Date: 2026-08-05

Authority: none

Audit: unset

Status: bounded worked result (owner-directed mass-lane closure,
window 2b; no axiom surface touched). The lane's remaining
empirical object — the concave shape of s(k) that the
pair-complement theorem left as the values behind all its
relations — is DERIVED, twice over. Structurally: the
pointer-conditioned branch lies EXACTLY in the symmetric subspace
(components outside at 6e-17), so s(k) is the entropy of the
squared singular values of a binomially-weighted HANKEL matrix
built from one (d+1)-term amplitude sequence obtained from a
2(d+1)-dimensional linear problem — reproducing every pinned value
at 1.2e-14 (the exact grade of the measurements). And negatively:
a hard NO-GO — at the frozen fields as exact rationals, the
collective Hamiltonian's characteristic polynomial at d = 4 has
Galois group S5, NOT SOLVABLE BY RADICALS — so no elementary
closed form for s(k) can exist at any certified degree beyond
d = 3; the structural form is the strongest possible answer. The
entanglement mechanism is named and ablated (the pointer's OWN
transverse term is the entire source — switch it off and every
s(k) is exactly zero), the leading order is the non-analytic
lambda^2 log(1/lambda) with its coefficient in closed form, every
one-line k-law is refuted at grade, and the consequences are
sealed and cashed: the full baseline table T(d), the multiplicity
ladder, the arity-dilution law, and the independence-gate crossing
fields lambda*(d) are now DERIVED for star geometries — verified
by sealed predictions off every measured grid.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle933_sk_shape_2026_07_28.py`](../scripts/frontier_cycle933_sk_shape_2026_07_28.py)
- [`frontier_cycle933_sk_shape_independent_check_2026_07_28.py`](../scripts/frontier_cycle933_sk_shape_independent_check_2026_07_28.py)

Receipt:

- [`sk_shape_cycle933_receipt_2026_07_28.json`](../outputs/sk_shape_cycle933_receipt_2026_07_28.json)
- [`sk_shape_independent_check_cycle933_receipt_2026_07_28.json`](../outputs/sk_shape_independent_check_cycle933_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). One spec-framing correction made and
disclosed: a pure PRODUCT branch predicts s(k) = 0 for every k (not
"k s(1) truncated by purity", which is the mixed-branch ansatz) —
the measured values sit 12 orders above that floor. One sympy trap
corrected on the record (the second galois_group return is the
alternating flag, not solvability — replaced by an explicit
classification of non-solvable transitive subgroups, and the
checker confirms the no-go with NO CAS at all). Two checker-side
instrumentation bugs self-caught and disclosed (a
symmetry-breaking control that did not break the symmetry; a
tolerance set below the double-precision floor). A real
determinism leak found and fixed with a hard guard (a lemma-timing
key inside the timing-free payload — the third block to hit this
trap class; the guard now scans). Independent audit still
required.

## The derivation, in three steps

1. **The collective reduction (L1, symbolic):** on the star, the
   frozen Hamiltonian is H = -2 Z_0 Jz - lambda X_0 - 2 lambda Jx
   on C^2 (x) Sym^d — dimension 2(d+1), not 2^(d+1). The frozen
   preparation (quoted from the memo and the pinned implementation:
   the pointer AND every recording neighbour start in +X) is
   symmetric, so the whole evolution stays in the subspace:
   measured leakage 6.2e-17, with the checker's broken-symmetry
   control (a one-arm longitudinal field) reading 0.186 — the hunt
   can see a violation.
2. **The Hankel form (L2, exact matrix identity):** writing the
   branch as a Dicke-amplitude sequence x_n, the k-arm reduced
   state is V T T^t V^t with T^(k)_{m,q} = sqrt(C(k,m) C(d-k,q))
   x_{m+q} — s(k) is the entropy of the normalised squared
   singular values of that binomially-weighted Hankel matrix.
   Residual against ALL pinned values: 1.216e-14 absolute. Free
   corollaries, now theorems: the reflection s(k) = s(d-k) IS
   transposition (T^(d-k) = T^(k)^t identically — true for any
   symmetric branch, no dynamics used); s(0) = s(d) = 0 is
   rank-1; the 931 collapse follows because only block sizes
   enter T.
3. **The no-go (L6, exact rationals):** a parity operator splits
   the collective Hamiltonian into two blocks of dimension d+1;
   at both frozen fields the d = 4 blocks' characteristic
   polynomials are irreducible with Galois group S5 — not
   solvable by radicals. **No elementary formula in (d, k,
   lambda, t) can exist for d >= 4.** The checker confirms with
   no CAS: exact-Fraction Faddeev-LeVerrier characteristic
   polynomials in the integer Dicke basis, hand-written mod-p
   distinct-degree factorisation, Dedekind's theorem — both S5
   witnesses (a 5-cycle and a transposition) exhibited. Scope
   stated exactly: proven at d in {2, 3, 4} at the frozen
   rationals — solvability fails ALREADY at d = 4, which kills
   the elementary-form reading at every certified degree except
   d = 3.

## The mechanism, ablated

**The pointer's own transverse term lambda X_0 is the entire
source of arm entanglement.** Set it to zero: every s(k) collapses
to exactly 0 (1.3e-14) at all 8 certified cells — because with the
pointer frozen, the conditioned arm Hamiltonian is a sum of
single-arm terms and every pointer-flip history carries an
identical product state; the branch's entanglement is exactly the
non-collinearity of those histories (the checker's algebraic
witness: [Z_0, H] = 0 with the pointer field off). Set the ARM
field to zero instead and s(k) moves only ~1e-3 relative — which
is candidate B: an ELEMENTARY closed form (each Z_j conserved;
two-level formulas) that is exact in that limit and carries a
DERIVED error law (relative error = c(d) lambda^2, verified over
five field decades) — refuted AT GRADE as a value for the frozen
protocol (1.7e-3 / 6.7e-3 at the certified fields) and kept as
the controlled approximation it is.

## The expansion and the refuted k-laws

Leading order is **lambda^2 log(1/lambda) — non-analytic** — with
the coefficient sum E_k in closed form (manifestly
reflection-symmetric; E_0 = E_d = 0 identically; verified to
lambda^2 scaling exactly, and by the checker at 60 digits to
3.0e-16). The k-dependence is NOT k(d-k) (departure 10.7% at d=4
rising to 76% at d=10). Every one-line k-law — H2-of-k(d-k), the
geometric family, the quadratic — is refuted at grade (residuals
8-11 orders above 1e-11), with the degeneracy disclosed honestly:
reflection leaves floor(d/2) independent values, so d = 3 fits
anything and the first genuine two-parameter test is d = 6.
Concavity enters TWICE (E_k concave in k; -x log x concave in
epsilon) — neither alone.

## Consequences (derived vs empirical, stated to avoid overreach)

**Now DERIVED for star geometries, from the 2(d+1) reduction with
no full-space object anywhere:** the entire pinned baseline table
T(d) = 2s(1) - s(2) (16 rows, 3.0e-14); the 929 multiplicity
ladder (28 rungs, 8.4e-14); the arity-dilution law; the
reflection and boundary identities; and **the independence-gate
crossing lambda*(d)** (solvable; sealed values returning
T = 0.020000000000 at 7e-15 on the untouched full-space route).
Composed with the window: 932's edge-counting + 933's amplitudes
= the star certification structure derived end to end, at 932's
stated grid-phase scope.

**Stays empirical/imported, said plainly:** the frozen
Hamiltonian, preparation, partition rule, and comparison time;
every geometry whose arms are NOT pairwise isomorphic (chains,
loops, mixed-arm spiders — the reduction needs arm-permutation
symmetry); 926's conjunction where decided on non-star controls
(the A-family ARE coordinate stars and are covered; B/C/D/E are
not); the pointer-side statistics (chi, excess, H_Z) — the
checker's overreach audit exhibits two cells with s(1) equal to
2e-3 whose chi differ by 0.36 bit: **s(k) alone does not decide
926's conjunction**; and the t_open regularity (932's named
open).

## The seal (nine cells, all off every measured grid)

Built from the derived reduction alone with a hard-failing guard
proving ZERO full-space evaluations of any sealed cell before the
digest was fixed; then verified by the untouched full 2^(d+1)
route: T(13)/T(14)/T(15) at both fields (9.7e-13); the full d=13
ladder (1.5e-13); off-grid fields and times (4.0e-15;
declared non-claim); the mechanism at new degrees (7.6e-14); the
E_k coefficients at d=9 (primary at the double-precision floor;
settled by the checker at 60 digits — the primary's number alone
should not be read as E_k's accuracy, disclosed); the
gate-crossing fields for six degrees (6.6e-15).

## Gates, teeth, checker

Primary: every restriction surface at deviation exactly 0 (the
929 ladder and additivity; the 927/929 T(d) table; 931's 44
s(k) values and 28 identity residuals); 21/21 constants
seven-way; FOUR propagator routes (three full-space + the
collective route); 15/15 teeth including the planted
almost-fitting form (x(1 + 1e-9), caught at 1e-11), the planted
product branch (12 orders), the ablation-sensitivity tooth, and
the int8-underflow guard the 931 disclosure demanded; runtime
5.0 s. Checker: SUPPORTED, 15/15 teeth, ZERO refutations, ZERO
findings — reversed site order, Krylov/Pade, SVD entropies with
no density matrix, 50-60-digit mpmath, and the no-CAS Galois
confirmation; the Sym^d hunt across strong fields, late times,
and off-grid degrees at 1.5e-16 with a working
broken-symmetry control; runtime 9.6 s. Deterministic double-runs
across separate processes for both.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "the s(k) shape (Cycle 931's named residue: the concave sequence behind the pair-complement relations — 'deriving it would give the ladder's actual values'; also Cycle 932's amplitude-law import)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "DERIVED as the Hankel-spectrum form on Sym^d (exact at the pinned grade; the reflection is transposition; the mechanism is the pointer's own transverse term, ablated to exactly zero) WITH the Galois no-go (S5 at d=4 — no elementary formula exists; retire any hunt for one); the baseline table, multiplicity ladder, dilution law, and gate-crossing fields lambda*(d) are now derived for stars — composed with 932's edge counting, the star certification structure is derived end to end at the stated grid-phase scope; carry the non-overreach sentence (s(k) does not decide the pointer-side gates or non-isomorphic-arm geometries); named residuals: t_open(lambda), the isomorphic-arm-spider extension of the reduction (the frozen preparation is non-uniform along arms), the non-star empirical territory"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the derivation is for star (and by the checker's scope test, symmetric-subspace) geometries at the frozen preparation; candidate A is a structural closed form (a finite matrix construction), not an elementary formula — the S5 no-go proves none exists for d >= 4 (proven at the frozen rationals for d in {2,3,4}; solvability fails already at d=4); degrees 7-15 are abstract stars carrying no certification; off-grid fields/times are non-claim; the primary's sealed E_k row is floor-limited and settled by the checker's 60-digit route"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the subspace membership, the matrix identity, and the reflection-as-transposition are verified symbolically and at 6e-17 numerically with a working broken-symmetry control; the structural form reproduces every pinned value at 1.2e-14 and every derived consequence at 3e-14/8e-14; the no-go is established by two independent routes including a no-CAS exact-arithmetic confirmation with explicit witnesses; nine sealed cells built under a hard no-pre-evaluation guard verify on the untouched full-space route; the checker refutes nothing"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the three frozen memos (Hamiltonian, preparation, statistic —
  byte-quoted), the 927/929/931 primaries + receipts (all
  reproduced at zero), the axiom memo (pinned).

### Derived

- the collective reduction and the exact Sym^d membership;
- the Hankel-spectrum structural form (exact at grade) with
  reflection-as-transposition and the boundary identities;
- the Galois no-go (no elementary formula, d >= 4);
- the mechanism (the pointer's transverse term; ablated);
- the non-analytic leading order with closed-form coefficients
  and the refutation of every one-line k-law at grade;
- the derived consequences: T(d), the ladder, the dilution law,
  lambda*(d) — sealed and cashed off-grid;
- candidate B as a controlled approximation with a derived error
  law.

### Open

- t_open(lambda) and the pointer-side gates (chi/excess/H_Z) —
  NOT determined by s(k) (the overreach audit's 0.36-bit
  witness); the natural capstone question;
- the isomorphic-arm-spider extension of the reduction;
- the non-star empirical territory (the reduction's honest
  boundary).

## Verdict

The last number the lane could not explain turns out to have been
protected by mathematics itself: the amplitudes behind s(k) live
in a five-fold symmetric group's shadow, so the formula everyone
would have hunted does not exist — and the right answer was never
a formula but a structure. One symmetric sequence, folded through
binomial weights into a Hankel matrix, reproduces every rung,
every baseline, every crossing field the lane has measured, to
the last digit the measurements possess; its reflection symmetry
is a transposition, its boundary zeros are rank-one facts, and
its entire entanglement is bought by the one term everyone would
have guessed last — the pointer's own private field, without
which every branch is a product and every s is zero. With the
window theorem holding the clock and this block holding the
amplitudes, the star lane's certification story is derived from
the dynamics end to end, and what remains outside — the pointer's
own gates, the unsymmetric geometries — is drawn on the map as
exactly what it is. Independent audit still required.
