# What the Cycle-947 compiler facts establish, and what remains open for H0

Date: 2026-07-28 (corrected 2026-09-09 after focused review of original PR
6017)

**Authority:** none

**Audit:** unset

**Type:** bounded_theorem

**Status:** corrected finite result. The original campaign's universal H0
refutation, physical lane/site identification, distribution-independence
claim, minimal-causal-cone claim, full-symmetry claim, and unique-successor
recommendation are withdrawn.

**Primary runner:**
[`frontier_cycle947_h0_discharge_2026_07_28.py`](../scripts/frontier_cycle947_h0_discharge_2026_07_28.py)

**Independent check:**
[`frontier_cycle947_h0_discharge_independent_check_2026_07_28.py`](../scripts/frontier_cycle947_h0_discharge_independent_check_2026_07_28.py)

**Execution evidence:**

- primary cache: `logs/runner-cache/frontier_cycle947_h0_discharge_2026_07_28.txt`
- primary receipt: `outputs/h0_discharge_cycle947_receipt_2026_07_28.json`
- checker cache: `logs/runner-cache/frontier_cycle947_h0_discharge_independent_check_2026_07_28.txt`
- checker receipt: `outputs/h0_discharge_independent_check_cycle947_receipt_2026_07_28.json`
- current ship receipt: `outputs/h0_discharge_block_cycle947_ship_receipt_2026_07_28.json`

The two runners are self-contained. The primary declares no repository input.
The checker reads only the frozen primary source and its generated cache, both
by exact SHA-256. Neither runner imports the old Cycle-719 controller chain or
executes the historical compiler campaign.

## Declared finite constructions

The result concerns five small mathematical constructions. They are
counterexamples to implications used by the original argument; they are not a
physical model.

1. **Packed-word grammar.** Let every `c[i]` be a non-negative integer whose
   binary coordinates are called lanes. The supplied grammar contains only
   updates `c[i] ^= E`, where `E` is built from `c[j]`, non-negative integer
   literals, and `&`, `|`, and `^`. Each operator acts coordinatewise, so a
   structural induction makes every accepted expression lane-local. This
   leaves wire indices independent of lane indices: the accepted update
   `c[1] ^= c[0]` couples two wires inside each lane. The primary exhausts the
   two-wire/two-lane XOR fixture, and the checker independently exhausts all
   96 two-bit coordinate identities for the three operator bases.

2. **External-choice law.** The deterministic update is `y := b`, where `b`
   is supplied externally. At fixed `b`, the trajectory has no neighboring
   condition as an argument. If `U` is uniform on `{0,1,2,3}` and
   `b = 1` exactly when `U < 1 + 2n`, then
   `P(y=1 | n=0)=1/4` and `P(y=1 | n=1)=3/4`. Fixed-choice trajectory
   independence therefore does not imply distribution independence unless a
   condition-independent choice law is separately supplied. A Bernoulli menu
   supports both outputs only for `0 < mu < 1`; at `mu=0` or `mu=1` its
   support is a singleton.

3. **Static reachability.** The scheduled program `x ^= y; x ^= y` contains
   the structural edge `y -> x`, while its exact composed map is the identity
   on all four Boolean inputs. Static control-to-target reachability can thus
   strictly overapproximate semantic dependence. On the separate chain
   `a -> b -> c -> d`, the depth-two backward set is smaller than the fixed
   point. These are graph facts; neither set is certified as a minimal
   physical causal cone.

4. **Order versus gate multiset.** The orders `CNOT(a->b), CNOT(b->a)` and
   `CNOT(b->a), CNOT(a->b)` contain the same two gates, and wire swap exchanges
   the two gate types. Their exact maps on the four Boolean inputs differ.
   A gate multiset, including one invariant under that involution, does not
   determine the scheduled composed map.

5. **Covariance subgroup versus full symmetry.** The identity rule on three
   Boolean coordinates commutes with a flip of only one coordinate on all
   eight states. Hence covariance of a fixed rule under a supplied subgroup
   cannot by itself classify the rule's full automorphism group. Separately,
   the primary enumerates the 24 signed-permutation matrices of determinant
   `+1`; the checker regenerates the same group from three quarter turns.
   Their centered affine actions on the declared three-by-three-by-three box
   contain no permutation that moves exactly two box points and exchanges
   them. This last statement concerns only the supplied proper-cube subgroup.
   Applying it to physical sites requires an explicit injective equivariant
   lane-to-point map.

## Consequences for the ten historical H0 clauses

The ten labels below belong to the original chosen checklist. Their count is
bookkeeping for that checklist and is not a coordinate-independent measure of
progress toward a TOE.

| Clause | Correct current disposition |
|---|---|
| H0a1 | Bit-diagonal compilation is conditional representation mathematics. It does not force a physical-site interpretation. |
| H0a2 | Lane partition and duplicate-layout consistency are finite representation facts, not a physical-site quotient. |
| H0a3 | No physical embedding is supplied. A token search cannot prove that no embedding or alternative interpretation exists. |
| H0b1 | The syntax gives finite structural containment. It does not give a minimal semantic causal cone. |
| H0b2 | Trajectory independence holds with external choices fixed. Distribution independence additionally needs a condition-independent choice law and the site bridge. |
| H0c1 | Distinct endpoint patterns are finite menu-cardinality data only. |
| H0c2 | Branch existence does not imply nonzero support. For a Bernoulli menu, both outcomes occur only at an interior parameter. |
| H0c3 | The physical possibility-domain and encoding bridge remain unsupplied. Absence of matching tokens is not a no-existence proof. |
| H0d1 | The supplied wire relabeling preserves lanes structurally. The corrected finite package retains the splice-order counterexample and makes no sampled-to-global automorphism promotion. |
| H0d2 | Descent to an axiom-level conclusion remains conditional on explicit domain, site, and action bridges. |

## Proof boundary

The finite results establish separations between concepts that the original
argument identified: lanes and physical sites; fixed-choice trajectories and
choice distributions; static reachability and semantic causality; unordered
gate data and scheduled maps; and covariance under a named subgroup and a
full automorphism group. They show that the individual implication steps do
not follow from only the conditions supplied for those steps. They do not
refute a strengthened theorem with additional physical premises.

They do not establish a physical lane-to-site map, independence of the actual
choice supplier, a one-site domain/action bridge, a minimal semantic causal
cone, or the full symmetry group of an axiom-compatible physical law. H0 is
not discharged or refuted here. No unique successor, new primitive, framework
axiom, physical prediction, or TOE closure follows.

## Historical source and evidence disposition

The exact eight original endpoint files, twelve intermediate source bodies,
six raw commit patches, all direct and static historical inputs, and the full
105-artifact original review receipt are preserved under
`.claude/science/physics-loops/h0-6017-correction-20260909/review-packet/`.
`SOURCE_PRESERVATION.json` verifies the recovery. The old 24.6-second and
19.1-second outputs, large compiler counts, 46-file/113-edge Cycle-719 ancestry,
and moving historical premise pins remain attributed history. They were not
replayed and carry no current authority. The corrected Cycle-878 source on
current main is unchanged.

## Reproduction and status

Run the primary and then the checker under the declared 30-second/2-GiB
process-group bounds. The primary emits nine predicate-derived certificates;
the checker uses independent coordinate, counting, GF(2)-matrix, permutation,
and generator-closure routes and fails closed on a pin or predicate mismatch.
Both emit standard `TOTAL: PASS=<n> FAIL=<n>` lines. The ship receipt binds
their final source, caches, receipts, exact inputs, resource records, and the
historical disposition.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "finite implications and counterexamples on the declared constructions only; all physical bridges and H0 remain open"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite constructions plus an independent route for each consequential implication separation"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

No formal audit has run. Audit status remains unset, consistent with the
campaign direction to defer formal audit until there is a solid TOE candidate.
