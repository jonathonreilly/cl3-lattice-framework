---
claim_id: the_partial_configuration_readout_is_injective_on_the_3_torus_every_law_is_visible_to_records_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "Conditional injectivity of the static partial-configuration map on the supplied 3^24 support-table family over the 3-torus. A verified pool of 3117 realizable masks satisfies 95 positive Boolean coverage requirements and the sufficient two-case separation theorem. The pool failure of C0(22) leaves the global condition unresolved. All 50/144/19 original witnesses and finite solver-supported target/centered-box decisions are preserved; negative decisions require the complete solver path. The seed-component enumerator is not whole-space enumeration, and finite witness occupancies are not minima. No physical membership oracle, preparation/readout bridge or full probability law is derived."
upstream_dependencies:
  - minimal_axioms
  - extensional_nearest_neighbor_rule_deep_probe_2026-07-13
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
runner: scripts/partial_configuration_readout_injective_torus_3_check_2026_09_04.py
registry_id: partial_configuration_readout_injective_torus_3_every_law_visible
---

# Static partial-configuration membership identifies each finite support table on the 3-torus

**Date:** 2026-09-04

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** conditional source; no retained or audited status applied

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/partial_configuration_readout_injective_torus_3_check_2026_09_04.py`](../scripts/partial_configuration_readout_injective_torus_3_check_2026_09_04.py)

**Runner cache:**
[`logs/runner-cache/partial_configuration_readout_injective_torus_3_check_2026_09_04.txt`](../logs/runner-cache/partial_configuration_readout_injective_torus_3_check_2026_09_04.txt)

**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md),
[`EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md`](EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md),
[`ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md),
[`TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md`](TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite mask/CNF identities, 95 verified pool-coverage positives and a sufficient injectivity proof. The original 72 target and two centered-box decisions require actual complete solvers; emitted proof length is not proof checking. Original witnesses are retained with explicit finite domains and physical access limits."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Keep global C0(22), arbitrary-domain extension, minimum geometry and the physical preparation/membership/readout bridge unresolved. The finite support-table theorem supplies none of these by itself."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

Can static membership of partial configurations distinguish every table in the
supplied finite family? This is a mathematical map, not an automatically available
physical readout. The earlier complete-configuration map has 81 static classes
and fibres 3^20; the companion's 44 partial witnesses give at least 1,033,121,304
classes and fibres at most 648. A supplied fixed-order endpoint law is a separate
object and can already distinguish tables within a complete static class.

Here the full 3117-mask certificate proves injectivity of the static map. Actual
preparations, knowledge of the recorded domain, access to counterfactual membership
queries and adequate ensembles remain supplied conditions. No absent site is read.

## Supplied surface (quoted)

Admissibility and Record, current landed wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`), with reading note (3)
fixing the sense of "admissible" below:

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."

> "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability."

> "Records form." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read." "A state is a configuration of records."

A site need not carry a record, but this supplies no static membership oracle.
The formal open symbol labels a supplied configuration domain; it is not a
physical readout of an absent site. The memo supplies no formation schedule,
preparation protocol or arbitrary ensemble. Later neighbors do not erase Records.

## T1 -- the encoding (exact)

A **support table** `T` assigns to each of the 729 ternary neighbour profiles a nonempty subset of `{0,1}`,
covariant under proper cubic rotations and label-equivariant. The 729 profiles fall into 57 proper-cubic orbits;
the global value flip fixes 9 and pairs the other 48 into 24 flip-pairs, each carrying one free ternary digit
`d_i`. Hence 3^24 = 282,429,536,481 tables. A **partial configuration** `c` is admissible under `T` as it stands
iff no recorded site asks for a value its orbit's menu forbids, and the asking is 48 bits: `c` is admissible iff
`mask(c) & block(T) == 0`, where `block(T)` sets bit `2i` iff `d_i = 0` and bit `2i+1` iff `d_i = 1`. Write
`A_p(T)` for this static set of supplied configurations. Its simultaneous local
test is distinct from sequential reachability and from an endpoint probability law.

**The decision problem is local.** `mask(c)` contained in a bit set `S` says: every recorded site's demand bit
lies in `S` or is absent. A site's demand bit is a function of that site's value and its six neighbours'
conditions only, so the condition is a conjunction of constraints on 7-site stars -- a subshift of finite type
-- plus one existential per bit that must occur. That is what makes an exact solve possible, and the runner
checks it against the mask criterion directly. The CNF gives each site one one-hot ternary variable (`open`,
`record 0`, `record 1`) and forbids, for each site and value, every profile code whose demand bit falls outside
`S`, emitted through a prefix trie over the six ternary digits so a wholly forbidden subtree costs one short
clause; a bit required to occur is asserted by a Tseitin disjunction over all (site, profile) placements raising
it.

**The reduction is verified, not assumed.** `mask` is invariant under lattice translation, all 24 proper cubic
rotations acting as `c'(x) = c(Mx)`, and the global 0-1 flip; the runner checks all 27 translations, all 24
rotations and the flip on a declared configuration set, and checks that every profile in orbit A of a flip-pair
is rotatable onto that orbit's canonical representative and every profile in orbit B onto it after the flip. So
on the full torus the demanding site can be pinned at the origin with a canonical
representative. For a centered box, retaining that pin is an additional stated
domain restriction; no arbitrary placement/orientation completeness is inferred.

## T2 -- finite solver-supported digit-confined decisions on the 3^3 torus

For each pair `i` the three digit-confined targets are `{2i}`, `{2i+1}` and `{2i,2i+1}`; any two determine
`d_i`, any one splits `{0,1,2}` into 1+2. All 72 are decided.

```text
satisfiable                            50   masks re-verified by two paths
unsatisfiable                          22   zero targets realised
digits read exactly                    17
digits read to a binary choice          4   pairs 14, 18, 21, 23
digits no digit-confined mask reaches   3   pairs 11, 16, 17
per-digit fibre    3^3 x 2^4                =           432
per-digit classes  3^17 x 2^4               = 2,066,242,608
```

**The 22 negative instances require the complete solver path.** The original
CaDiCaL decisions agree with Glucose and MiniSat on all 22 negatives. The
one-hot/star/required-bit CNF and decoded positive witnesses are checked. Glucose
emits DRUP traces; recording their lengths is not independent proof checking.
Unavailable, failed or indeterminate engines cannot produce a successful negative
verdict. The same rule applies to the negative centered-box decisions in T5.

The old solver-free routine enumerates only the connected recorded component of
its demanding seed. Its original count of 55 leaves and zero target hits is
preserved as that restricted computation. It does not enumerate every extension:
three explicit same-seed legal configurations have disconnected records that it
omits. A separate component could matter to a both-bit target; no reduction
excluding it is claimed. Thus the routine is not an independent negative proof.

**Pair 23 is realised**, by the complete configuration `101000110011010110001111100`, all 27 sites recorded,
demand mask exactly `{46, 47}`. The companion note's per-digit table is corrected here: it listed four pairs as
unseparated; three have no digit-confined witness on this torus, while pair 23
can be split. The companion list contains **44** entries. Six additional
`{2i,2i+1}` targets give **50**; all original configurations are retained.

## T3 -- the static membership map is injective on the 3^3 torus

The digit-confined framing is not the full static map: a mask may constrain several digits at once, and such masks
separate tables the digit-confined ones cannot.

**The criterion.** Write `B = block(T)`; `d` maps to `B` injectively. Since `A_p(T) = { c : mask(c) & B == 0 }`,
`A_p(T) = A_p(T')` exactly when no realisable mask avoids one block set and meets the other. Define, for `b` not
in `B`,

```text
VIS(B, b) :=  some realisable mask m has  b in m  and  m & B == 0
A_v(j)    :=  VIS(B, 2j+v) for every legal B with d_j = 2
C_v(j)    :=  for every legal block set Bd on the 23 digits other than j, some
              realisable m has  m & {2j, 2j+1} = {2j+v}  and  m & Bd == 0
```

**Claim.** If `A_0(j) and A_1(j) and (C_0(j) or C_1(j))` holds for every `j`, then `T -> A_p(T)` is injective.

**Proof.** Take `T` distinct from `T'`, so `B` is distinct from `B'`; without loss some bit `b` lies in `B'` and
not in `B`; let `j = b div 2`. *(i)* If `d_j(T) = 2`, then `A_{b mod 2}(j)` applied at `B` supplies a realisable
`m` with `m & B == 0` and `b` in `m`; since `b` is in `B'`, that `m` lies in `A_p(T)` and not in `A_p(T')`.
*(ii)* Otherwise `d_j(T)` is 0 or 1, so `B` contains the partner bit of `b`, and the two tables differ at `j` as
`{0}` against `{1}`. If `C_{b mod 2}(j)` holds, apply it at `Bd = B` restricted to the digits other than `j`: it
gives a realisable `m` with `m & {2j,2j+1} = {b}` meeting neither `Bd` nor the pair-`j` bits of `B`, hence
`m & B == 0`, while `b` lies in `m` and in `B'`. If the other one holds instead, apply it at `Bd = B'`
restricted to the digits other than `j`; then `T` and `T'` exchange roles and the separating mask lies in
`A_p(T')` and not in `A_p(T)`. Either way `A_p(T)` is distinct from `A_p(T')`. ∎

**Antitonicity.** `VIS(B, b)` is antitone in `B`: enlarging the block set can only lose masks. So `C_v(j)` needs
checking only at **maximal** `Bd` -- every other digit 0 or 1, a fully deterministic law except at pair `j` --
which turns 3^23 candidate laws into 2^23 and puts the search on the hard end. In that form each usable mask
serves exactly a subcube of the deterministic laws, and the requirement is that the subcubes cover the cube.
The declared pool contains **3117 masks,
every one carried with the configuration that realises it and re-verified from that configuration** by both the
vectorised and the scalar path. The 96 pool-coverage requirements -- 48 of type `A`, 48 of type `C` -- are
decided by a from-scratch complete Boolean subcube-cover procedure and by
CaDiCaL and Glucose forced to agree. Every positive pool result implies the
corresponding global condition because each pool mask is realizable. A pool
failure implies no global absence.

```text
declared-pool coverage only:
pairs 0..21, 23 :  A0=Y A1=Y C0=Y C1=Y
pair 22         :  A0=Y A1=Y C0=N C1=Y     (global C0(22) unresolved)
96 pool requirements : 95 met; these positives suffice for injectivity
fibre 1; all 3^24 = 282,429,536,481 tables separated
```

The pool's uncovered block 80,649,380,013,721 is served by the actual 3-torus
configuration `1110..010001......0........`, whose mask is 17,592,320,264,448
and is absent from that pool. This refutes treating the pool gap as a global
obstruction; one added witness does not settle global `C_0(22)`.

**Six small joint masks are gated examples.** The five-record configuration
`101...0...........0........` has mask `{0,2,22}`. Its static response is the
conjunction `d_0 != 0`, `d_1 != 0`, `d_11 != 0`. If known `d_0 = 0`, every
`d_11` choice gives false: knowing a nuisance value does not remove its gate.
All six five/six-record masks are retained. Unconditional separation instead
comes from the full covering criterion, whose witness avoids the other blocked
digits for the particular pair of tables being compared.

## T4 -- the 4^3 and 5^3 tori (verified witnesses)

```text
4^3 : 72 / 72 digit-confined targets satisfiable, k = 2 .. 64 records
5^3 : 72 / 72 digit-confined targets satisfiable, k = 2 .. 64 records
```

All 24 digits are read exactly by isolated digit-confined masks at both sizes, so the per-digit fibre is 1 there
too, and each of the 22 targets the 3^3 torus does not reach becomes individually visible at L = 4. The note
carries the 144 witness configurations and re-verifies each mask against its target by both paths; the
satisfiability search that produced them is not re-run, and that is the one place where these rows rest on
declared data rather than a decision in the runner.

## T5 -- exact mirror identity and two centered-box comparisons

**The 3-cycle mirror lemma.** On the `L^3` torus the two `d`-neighbours of a site `x` are `x+d` and `x-d`. For
`L = 3`, `x-d = x+2d`, so the three sites of any axis line are mutually `d`-adjacent; for `L >= 4` they are not,
and the runner checks both directions at L = 3, 4, 5. Two consequences: if all three sites of a line are
recorded, no site of that line can see open on that axis; and if exactly one is open, both recorded sites see
(open, the other record) -- a mixed axis at one site forces a mirrored one at its partner, carrying that
partner's value. This identity alone is not a classification of all witness
geometry. For each of the 22 target negatives, the runner also tests two specified
centered boxes, keeping the canonical demanding-site pin:

```text
3x3x3 block  : only pair 4's {2i} becomes satisfiable, k = 14
4x4x4 block  : 18 of the 22, including all three targets of 11, 16 and 17
the 4^3 torus: all 22
```

The first domain is the centered 3x3x3 box in the 4-torus, and the second is
the centered 4x4x4 box in the 5-torus. Sites outside the box are fixed open.
The 1/17/4 split means one target is positive in the first box, seventeen more
in the second, and four are positive in the 4-torus but negative in both
specified boxes. It is not a minimum-diameter, all-placement, all-orientation
or required-periodicity theorem. The nineteen original box witnesses remain.

The four residual targets are `14:{2i}`, `20:{2i,2i+1}`, `21:{2i+1}` and
`21:{2i,2i+1}`. Their original 4-torus witnesses have 52,64,64,64 records.
Those are arbitrary witness occupancies, not necessary bounds. Additional
verified configurations for the same targets have **25,20,30,48** records,
respectively. These smaller examples are not claimed minima. All 144 original
larger-torus witnesses and their exact occupancies are preserved.

## Corollary and physical boundary

1. On the declared 3-torus support family, `T -> A_p(T)` is injective: each
   fibre is one. This is a conditional static membership theorem.
2. The 3-torus digit-confined negatives rest on actual complete solvers. All
   24 digits have explicit isolated witnesses on the 4- and 5-tori.
3. The companion bound stands as a finite witness bound; its original list
   understates static distinguishability, but no physical-readout conclusion
   follows from either certificate.
4. No history appears in the static definition. Actual membership access,
   preparation and a supplied distribution of experiments are still required.

The support table is not the full probability measure on M2(C). Different
weights on the same support are not identified by this map. The corrected Q8
and history notes supply only their named finite/nonselection and sequence
context; no broad parent campaign or physical clock is imported.
No physical law is selected, and no empty-site value is read.

## Executable claim block

```text
registry_id: partial_configuration_readout_injective_torus_3_every_law_visible
ternary_profiles_orbits_flipfixed_pairs: 729 / 57 / 9 / 24
support_tables_and_demand_word_bits: 282429536481 / 48
digit_confined_targets_decided_torus_3: 72 (50 satisfiable / 22 not)
historical_seed_component_leaves_and_target_hits: 55 / 0
pairs_with_no_digit_confined_mask: 11 16 17
pairs_read_to_a_binary_choice: 14 18 21 23
digits_exact_binary_blind_torus_3: 17 / 4 / 3
per_digit_fibre_and_classes: 432 / 2066242608
digit_confined_witnesses_torus_3: 50
declared_mask_pool_reverified: 3117
declared_pool_requirements_and_met: 96 / 95 (global C_0(22) unresolved)
true_fibre_and_classes_torus_3: 1 / 282429536481
digit_confined_targets_torus_4_and_5: 72 / 72 at each size
specified_centered_box_comparison: 1 / 17 / 4
original_four_target_witness_records_on_torus_4: 52 / 64 / 64 / 64
additional_same_target_witness_records_not_minima: 25 / 20 / 30 / 48
no_physical_law_is_selected: true
```

## Proof boundary

The theorem is the finite classification above and nothing wider.

- **Complete exactly as scoped.** All 72 digit-confined targets use the complete
  solver path; the 55-leaf routine is seed-component-only. All 96 Boolean pool
  cover problems are decided independently. The 144 larger-torus and nineteen
  box configurations are direct existence certificates. T5's negative box
  decisions require the actual solver; witness-only fallback cannot certify them.

- **A sufficient criterion, and a verified subset.** The criterion of T3 is sufficient, not necessary, and its
  two-case proof is the load-bearing item. The 3117-mask pool is a verified subset of the realisable masks,
  never a census: injectivity established with a subset is a fortiori true, and no impossibility follows from a
  mask's absence from it.
- **Three finite tori and specified boxes.** No arbitrary-size refinement is
  proved, and failure to embed one witness does not prove partition coarsening.
  A valid padding must preserve every recorded-site shell, including its open
  neighbor buffer. No global periodicity or minimum-extent result is inferred.
- **Support tables, not the full rule space.** The 3^24 support tables are the deep probe's finite lower-bound
  witness family under the canonical uniform lift, a stipulation here. No sampling, no seed and no random number
  generator is used anywhere; no premise is edited, no axiom is added, and **no physical law is selected**.

## Review boundary

The sufficient two-case proof and all verified pool masks support the finite
injectivity result. The global pool-negative condition, physical access, general
geometry and minimum occupancy remain outside it. The actual negative solvers
are required; emitted DRUP traces are retained without claiming proof checking.

The September-8 correction preserves the original note/cache under `archive/notes`,
all witnesses and old numeric checks, including the incomplete enumeration's
55 leaves. Its corrections change the stated scope rather than erase data.
Formal audit remains deferred by the owner; this source applies no grade or
audit status. Broader supplier campaigns remain unaccepted.
