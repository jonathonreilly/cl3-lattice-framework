# The identity was purity talking: the pair-complement theorem, and the ladder collapses to one sequence — Cycle 931

Date: 2026-08-05

Authority: none

Audit: unset

Status: bounded worked result (owner-directed mass-lane closure,
window 2b; no axiom surface touched). The additivity identity Cycle
929 measured at 8e-14 and published unexplained is DERIVED — and
the mechanism is none of the three candidates the block was
launched with. It is the PAIR-COMPLEMENT THEOREM: with the global
state pure, the frozen partition exhausting every non-pointer site,
and the statistic conditioning on the pointer in the Z basis, the
identity C_ab + C_Rb = 2 sum_z p_z S(rho_Fb^z) holds BRANCH BY
BRANCH and exactly, with no assumption on the branch weights, the
Hamiltonian beyond arm symmetry, the field, or the time. Adding arm
exchangeability collapses the entire per-pair law to ONE entropy
sequence — C(m_a, m_b) = s(m_a) + s(m_b) - s(m_a + m_b) with the
reflection s(k) = s(d-k) — from which 929's measured additivity,
its exhausting-rung relation, and its last-step law all follow
identically. The exhausting-pair departure COMES OUT of the
derivation (the reflection wrapping), not patched in. A sealed
prediction closed 929's declared-unconstructible both-merged region
at the state level to 9.7e-15. The SSA-equality and perturbative
readings are refuted by computation; what remains empirical is
named exactly: the concave shape of s(k) itself.

Claim type: bounded_theorem

Runners:

- [`frontier_cycle931_additivity_identity_2026_07_28.py`](../scripts/frontier_cycle931_additivity_identity_2026_07_28.py)
- [`frontier_cycle931_additivity_identity_independent_check_2026_07_28.py`](../scripts/frontier_cycle931_additivity_identity_independent_check_2026_07_28.py)

Receipt:

- [`additivity_identity_cycle931_receipt_2026_07_28.json`](../outputs/additivity_identity_cycle931_receipt_2026_07_28.json)
- [`additivity_identity_independent_check_cycle931_receipt_2026_07_28.json`](../outputs/additivity_identity_independent_check_cycle931_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). The spec's three candidate mechanisms
were declared non-premises and the derivation is a FOURTH structure
the state analysis exposed — followed per the minimal-premise rule.
Three self-caught implementation traps are disclosed for
re-implementers (an unsigned-integer underflow building Z operators
— the pinned runner casts to int8 first; a Hermitian-vs-symmetric
eigensolver mix-up caught by a tooth; a timing string briefly
leaking into the "timing-free" digest, now guarded by a hard-fail).
Independent audit still required.

## Q1 — the structure (computed first, symbolically where feasible)

The statistic's definition byte-verified from the frozen memo:
C_ab = I(F_a : F_b | Z_S), evaluated as the branch-averaged entropy
combination with the off-diagonal pointer blocks zeroed; the pinned
917/929 implementation quoted verbatim and matched. On all 8
certified cells (d = 3..6 at both frozen fields, Jt = 0.7):

- the branch weights are exactly balanced (|p_z - 1/2| <= 1.1e-16,
  by the global X-flip symmetry);
- **the pointer-conditioned branch is PURE** (S of all d leaves
  given z at 1.4e-15) — the frozen partition exhausts every
  non-pointer site, so "the rest" is always the complement;
- every k-leaf reduced state is THE SAME state (exchangeability
  spread over all C(d, k) subsets at 3.9e-15);
- the reflection s(k) = s(d-k) holds at 8.8e-16 (Sylvester:
  complementary subsystems of a pure state share a spectrum).

The m-dependence therefore enters NOWHERE except through block
sizes: C_ab = s(|a|) + s(|b|) - s(|a| + |b|), and
G_d(m) = s(m) + s(1) - s(m+1).

## Q2 — the candidates, attacked

- **(a) Exchangeability: necessary, NOT sufficient — refuted as
  the mechanism.** A d-leaf block of a (d+1)-star is exactly
  exchangeable but mixed; its additivity residual is 7.0e-3 —
  eleven orders above the measured 8.3e-14. Symmetry gives "s
  depends on size"; the telescoping needs purity.
- **(b) The SSA-equality reading: REFUTED by computation.** A
  Markov chain needs I(A:R|B) = 0; the certified states carry
  I(A:R|B) >= 0.0045 bit — while I(A:R|B) - I(A:R) sits at 2.3e-14
  (the pure-tripartite identity, which is the CORRECT information
  form: I(A:B) + I(R:B) = 2S(B) = I(AR:B)). "Additivity in block
  size" is also refuted: s is strictly concave; the identity is a
  reflection, not a linearity.
- **(c) Perturbative: REFUTED.** At non-claim strong fields the
  statistic reaches 0.99-1.29 bits — far outside any small-field
  expansion — while the additivity residual stays at 5.8e-13.
  Exactness at machine precision at every order kills a
  leading-order account.
- **(d) PURITY: the mechanism — derived.**

## The theorem

**Pair-complement theorem.** Hypotheses, exact: H1 the global
state is pure; H2 the partition exhausts every non-pointer site (a
property of the frozen rule); H3 the statistic conditions on the
pointer in the Z basis (no assumption on the branch weights — the
identity holds in each branch separately). Then for any two
fragments a, b with R the rest:

    C_ab + C_Rb = 2 sum_z p_z S(rho_Fb^z) = C_(aR)b.

With H4 (arm exchangeability — a coordinate star, or ANY spider
with pairwise isomorphic arms): C(m_a, m_b) = s(m_a) + s(m_b) -
s(m_a + m_b), with s(k) = s(d-k) and s(0) = s(d) = 0 — whence
**G_d(m) + G_d(d-1-m) = 2 s(1) = G_d(d-1)** (the 929 identity),
the exhausting rung 2 s(1) forced, and the last-step law
G_d(d-1) - G_d(d-2) = G_d(1) = T(d) identically (929's own
published sentence, now a corollary). NOT used: the Hamiltonian
beyond arm symmetry, the field, the time, the branch weights,
fragment sizes beyond arm count, or the labelling rule.

## The seal (zero new cells evaluated at seal time)

Built from pinned bytes alone via s(1) = G(d-1)/2 and the
recursion; the reflection and s(d) = 0 NOT imposed, so they are
predictions. All seven sealed predictions verified: the
reflection and s(d) = 0 from the pinned ladder alone (1.6e-13);
**the 14 both-merged pair values — the region 929's structural
lemma declared unconstructible — predicted and verified at the
state level to 9.7e-15** (sample: d=6 at 0.10, C(3|3) sealed
0.032756162100354, measured ...359); the exhausting rung; the
identity at 208 cells (200 off the 929 grid, d to 10, fields to
2.0, four times) at 5.8e-13; nine hypothesis-ablation
constructions all failing additivity (the hypotheses are
load-bearing); and the exhausting-pair law C_ab = 2S(a) = 2S(b) in
ANY geometry (22 rows, 2.3e-13).

## Gates, teeth, checker

Primary: 21/21 constants byte-verified SIX-way; the statistic
definition byte-verified; the full 929 ladder (28 rungs / 8
cells), the additivity residuals, the T(d) table (d = 2..12), and
the exhausting-pair departure 0.006286487147332459 reproduced at
deviation exactly 0 — the last requiring the rebuild of all 22
contributing d=5 geometries; two disjoint routes; deterministic;
4.2 s. Checker: SUPPORTED, 15/15 teeth, ZERO refutations, 1.2 s —
fully disjoint machinery (Lanczos/Krylov + expm_multiply vs the
primary's Chebyshev/Taylor/eigh; reversed ordering; SVD entropies;
symbolics with NO CAS — exact rationals over a prime field with
hand-written characteristic polynomials and Schwartz-Zippel).
**The hypothesis attack found nothing**: 1000 random pure
permutation-symmetric states with no connection to the frozen
dynamics obey the identity at 2.0e-15 (the H4-dropped control
violates by 0.76 bit — the test can see); the 500-cell
counterexample hunt (476 off-grid) found zero violations; a
50-digit recomputation gives residual 7.6e-49. Two findings
carried: the identity EXTENDS to every isomorphic-arm spider
tested (exactly as H4 predicts — positive scope), and the two
identities separate cleanly (on a loop-carrying non-isomorphic-arm
geometry, additivity fails by 1.9 bit while the H1-H3
pair-complement identity holds at 4.4e-16).

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "the additivity identity G_d(m) + G_d(d-1-m) = G_d(d-1) (Cycle 929, measured at 8e-14, diagnostic-grade, unexplained — the lane's best mechanism handle)"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "DERIVED — the pair-complement theorem (purity + exhaustion + Z-conditioning, branch-by-branch; exchangeability collapses the per-pair law to one sequence with reflection); carry the theorem as the citation for the ladder identities and RETIRE the 'unexplained' flag; the s(k) SHAPE remains empirical (the identity is insensitive to it) — the honest residue; the persistence-razor mechanism is untouched and is now the mass lane's last unexplained mechanism (named successor); the pair-complement identity holds WITHOUT exchangeability (H1-H3 only) — usable on non-symmetric geometries wherever the frozen partition exhausts"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "the theorem is at its stated hypotheses (purity/exhaustion/Z-conditioning; exchangeability only for the ladder form); the both-merged predictions are STATE-LEVEL diagnostics (no frozen geometry realises them — 929's lemma stands; they carry no certification); strong fields and late times are non-claim; degrees 7..12 are abstract stars (lattice constructibility at d>=7 already answered negatively by 929); the general Sylvester identity is machine-verified to small shapes with its numerical consequence verified on every certified cell"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the derivation's hypotheses are each ablated with the identity failing (nine constructions; the exchangeable-but-mixed control at 7e-3); the sealed predictions include a region the parent declared unmeasurable, verified at 1e-14; the checker reproduces everything on fully disjoint machinery including no-CAS symbolics, finds zero violations in a 500-cell hunt, and confirms at 50-digit precision; the refuted readings (SSA-equality, perturbative) are refuted by computation, not argument"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the three frozen memos (the statistic definition byte-quoted),
  the 917/919/926/927/929 primaries + receipts (the ladder and
  departure reproduced at zero; constants six-way), the axiom memo
  (pinned); 921 via the constants cross-check only.

### Derived

- the pair-complement theorem (H1-H3, branch-by-branch) and its
  exchangeable collapse to one sequence with reflection;
- the corollaries: 929's additivity, the exhausting rung, the
  last-step law — all identities now;
- the refutations (exchangeability-as-sufficient; SSA-equality;
  perturbative) by computation;
- the sealed both-merged closure (state-level) and the six other
  sealed predictions;
- the positive-scope extension to isomorphic-arm spiders and the
  clean separation of the two identities.

### Open

- the SHAPE of s(k) (strictly concave, empirical — the identity
  is insensitive to it; deriving it would give the ladder's
  actual values);
- the persistence-razor mechanism (untouched — the mass lane's
  last unexplained mechanism);
- the two-merged-block constructibility (a frozen-rule boundary,
  929's lemma, not revisited).

## Verdict

The identity that held to fourteen digits without a reason turns
out to be the oldest fact in the subject wearing lane clothing: a
pure state knows its complements, so every pair's dependence and
its complement's dependence must sum to a number that cares only
about one side — and on a star, where every arm is every other
arm, that single sentence telescopes into the whole measured
ladder, exhausting rung, departure and all. The three mechanisms
the block carried in died honestly on designed cells, and the one
that survived was found by asking the state what it actually is:
balanced, branch-pure, exchangeable. The seal did what seals are
for — it reached into the region the parent had declared
unbuildable and called fourteen numbers to fourteen digits before
they were computed. What the theorem deliberately cannot do is as
sharp as what it does: it fixes every relation between the rungs
and says nothing about their values, so the lane's remaining
questions are exactly two — the shape of one concave sequence, and
the razor that persistence still balances on. Independent audit
still required.
