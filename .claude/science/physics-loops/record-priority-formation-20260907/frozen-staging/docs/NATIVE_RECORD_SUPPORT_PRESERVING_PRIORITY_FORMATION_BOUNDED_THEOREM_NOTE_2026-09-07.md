---
claim_id: native_record_support_preserving_priority_formation_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional mathematical result with supplied mechanism or profile constraint; no physical selector is derived."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07
runner: scripts/native_record_support_preserving_priority_formation_2026_09_07.py
---

**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; independent audit owns any verdict.

~~~yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
source_of_blocker_text: frontier_question
artifact_role: theorem
target_claim_type: bounded_theorem
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

# A conditional extension from local formation odds to permanent Records

This is a conditional result, not an axiom-derived activation law. It uses the current minimal axioms' distinction between the conditional content distribution and the still-unsupplied formation site/rate. The latest monotone theorem supplies laws for a prescribed order class; it does not supply that class as physical. The result here is a well-defined symmetry-covariant alternative activation construction, its precise relation to those finite monotone laws, and a support/permanence test. It does not derive quantum dynamics or an apparatus from Records.

## Prior art and actual contribution

The decreasing-arrival-path stabilization method is established. Penrose and Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Proposition1 and its proof (pp5,15), use factorial decreasing-path probabilities to construct infinite bounded-degree deposition processes: https://arxiv.org/pdf/math/0503519 . The ancestor estimate below is not a new probabilistic theorem. Here it is applied with a full finite-menu conditional Record kernel, fixed prior Records and equivariant outcome marks. The formation-specific points are: exactly which conditional law is realized without redrawing old contents; when ongoing support survives appends; and the condition under which this process realizes the existing monotone law rather than a different schedule mixture.

## Domain and supplied ingredients

Let G=Z3 with nearest-neighbor degree6. At each site a state is either blank or one member of a supplied finite menu M. The actual test menu is the six Bloch-axis projectors already supplied by the formation notes, with the proper cubic action. A rule r_x(s|eta) is a normalized probability on M for EVERY partial recorded-neighbor configuration eta, including empty eta. It is local and covariant. Zeros are allowed in the general statement. No rule is inferred merely from M2(C).

Fix an arbitrary deterministic pre-existing Record configuration on B subset G. These contents never change. On G minus B supply iid Exp(lambda) times T_x, lambda>0, and independent iid Exp(1) variables E_(x,s) for each menu element. All clocks and marks are independent of the initial Records. At T_x, use the already formed neighbors and choose the unique minimizer of E_(x,s)/r_x(s|eta), with zero probabilities assigned infinite score. Exponential races give conditional outcome probability r_x(s|eta). In law this construction is covariant; indeed simultaneously permuting label-indexed marks gives an equivariant coding. No arbitrary ordered CDF menu is physically preferred.

This imports a clock law, a start slice, independent noise and the menu/rule. It supplies no preferred lattice site or direction. A nonsymmetric initial B breaks symmetry only through the supplied initial condition. Random correlated initial Records can themselves carry long-range dependence, so no iid mixing conclusion is asserted for them.

## Infinite recursive construction and permanence

Orient an edge from x to a blank neighbor y if T_y<T_x. The contents at x depend recursively only on earlier neighbors and fixed initial Records. A decreasing path of n edges is self-avoiding. There are at most6*5^(n-1) such paths from a fixed site; along any fixed path iid continuous times have each relative ordering with probability1/(n+1)!. Therefore

    P(a decreasing path of length n from x) <= min(1,6*5^(n-1)/(n+1)!), n>=1.

The bound tends to0. A locally finite ancestor graph of unbounded depth has paths of every finite length, so each site's ancestor set is finite almost surely. Countability makes this simultaneous at every site. Recursively evaluate that finite directed acyclic graph from its earliest vertices. Shared ancestors are evaluated with the same marks, ensuring consistency between roots. This is the unique process satisfying the supplied activation times and local race rule: induction on the finite ancestor graph forces every output.

Initial Records are leaves; their fixed contents can be read as conditions, never resampled. At time t, a newly available Record at x is present exactly when T_x<=t, and thereafter its content is unchanged. Every initially blank site forms at finite time almost surely. There is no first event on the infinite initially empty lattice: the infimum of iid exponential times is0 and is not attained. No increasing global enumeration is required. Local finite-window computations stabilize once they contain all ancestors and their adjacent fixed-Record conditions. A window missing those conditions is a different finite model, not automatically an exact marginal.

At a site's formation, its own mark is independent of the prior generated history. Thus its conditional content law really is r_x; the construction has not conditioned on a favorable realized order or outcome. For exponential times the resulting cylinder generator is

    (Lf)(rho)=lambda sum_(x blank) sum_s r_x(s|eta_x(rho))[f(rho with x=s)-f(rho)].

For a cylinder f the sum has only finitely many nonzero summands. This is a supplied classical irreversible birth law, not a Hamiltonian or GKSL derivation. Scaling lambda changes the temporal law but not the final priority order distribution; the axioms do not select lambda.

## What 'admissible' must mean

There are two logically different requirements. Formation-time support says a new content lies in the support at the instant it forms. The construction above always satisfies that and permanently preserves contents. Ongoing support additionally asks that each already present content remain in the current local support after later neighbor insertions. The axiom wording must not be silently strengthened or weakened between these readings.

For a configuration rho that is currently ongoing-support valid, an append x=s preserves that property if and only if

    s in supp r_x(.|eta_x(rho)), and
    rho_y in supp r_y(.|eta_y(rho with x=s))
      for every recorded neighbor y of x.

All other old sites have unchanged conditions. This is an exact one-step iff, not a sufficient-only heuristic. It can be decided from the radius-two pattern about x. To preserve both the original conditional odds and ongoing validity whenever a site is allowed to form, EVERY s of positive r_x probability must pass the old-neighbor test. Selecting only safe outcomes and renormalizing generally changes the supplied law. An all-or-none site eligibility condition can retain the odds, but its liveness is a separate question. I do not infer infinite liveness for such an inhibited rule from the iid ancestor argument.

For the actual positive native product triples, every partial neighbor condition gives positive weight to all six labels. Thus every old Record stays in support under every future append. The independent-priority construction therefore realizes all three declared requirements simultaneously: exact local formation odds, immutable single Records, and ongoing support. Arbitrary fixed prior contents are then allowed. The theorem uses full support substantively; it does not justify arbitrary zero-support rules.

## Frozen adverse rule: a valid partial state with no ongoing-support completion

On the SAME six-label menu define r uniform if recorded neighbors are empty or contain distinct labels, and point mass at their common label if they are nonempty and identical. This is normalized on the full finite neighbor domain and covariant under all label permutations, hence under proper cubic rotations. It varies with neighbor conditions.

Use a three-site lattice path with endpoint Records0 and1 and a blank center; all other sites blank. Before the center forms, both endpoint Records see no recorded neighbor and are supported. The center sees distinct labels and has all six possibilities. After any center label s, each endpoint sees exactly that one label and requires its own label equal s. No s satisfies both. Thus this partial configuration has no full three-site ongoing-support completion, even with a selected order or modified center probabilities. With the exterior held blank, the endpoints cannot be repaired without changing their Records. On the full lattice, exterior sites may form first: a differently labeled exterior neighbor can make an endpoint's conditions mixed and restore full support. Thus the proved obstruction is to an immediate safe center append, or to completion of the isolated three-site window, NOT to eventual infinite-lattice liveness. This is a precise finite-window obstruction for the stronger support reading; it is NOT a contradiction under formation-time support and NOT an obstruction to the positive native triples.

## Exact connection with the monotone law

On a finite rectangle, for independent clock marks the conditional law given a fixed clock order sigma is exactly the existing product formation law mu_sigma. Conditioning the clock order to be a linear extension of the product partial order is an event involving times only. Every such order has the same recorded nearest-neighbor predecessor set, so the latest monotone theorem gives the same mu_P. The conditional mixture over these orders is therefore exactly mu_P. Unconditioned iid priorities need not give mu_P.

More generally the sufficient criterion for this realization is: each site's recorded neighbor set equals the declared predecessor set, and activation/order selection is independent of the content marks (or otherwise leaves the requisite conditional mark law unchanged). Merely saying the realized order is monotone is insufficient if it was selected from outcome information. For a pre-existing DOWNSET sampled from the mu_P marginal, continuing on the remaining sites in a compatible order reproduces mu_P; fixing those downset values gives its regular conditional continuation, because the DAG factorization leaves exactly the remaining factors. Arbitrary initial subsets are not covered by that conditional-marginal identity: future records can contain evidence about unresolved predecessors.

## Executed discriminator and limits

The frozen runner enumerates all24 orders and all1296 configurations on the open2x2 square, at (3,1,2) and constant(2,2,2). It checks every order's normalization, the two monotone orders' equality, full-mixture normalization and reflection covariance, and retains the actual mixture-versus-monotone difference. It also checks all six adverse center outcomes and the normalized adverse support on all55987 ordered neighbor menus of lengths0 through6. These finite windows have blank exterior and are not asserted to equal infinite-volume restrictions.

This reduces a conditional existence obligation: with an explicitly supplied unbiased activation mechanism the actual positive local Record odds admit a unique infinite irreversible realization without a selected origin or global first event. It leaves formation-mechanism selection, the full M2 possibility domain, any quantum/Born bridge, and the physical meaning of a start slice open. No clock/apparatus construction or generic no-go is being repeated or claimed.

## Current source premises and exact certificate

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) separate local conditional content odds from an unspecified formation mechanism. The menu, positive product rule and existing monotone law are those of the [September 7 monotone formation theorem](ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md), with its [finite-window parent](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md). The supplied iid times, independent race marks and start slice are additional inputs. No ongoing-support reinterpretation is adopted as a new axiom.

The native positive triple gives an open-square random-order versus monotone total variation53347/4416984, with720 differing configurations; the constant control agrees. These are exact finite-window results, not infinite-volume marginals. The original overbroad exterior-repair sentence, its correction and an independent supported two-step exterior repair are retained in the evidence packet.

The standalone [certificate](../scripts/native_record_support_preserving_priority_formation_2026_09_07.py) performs 66 actual assertions under180 seconds/180MiB. It reads no external runtime files and emits strict JSON under `--json`. Integral or finite-menu checks support the written proof; they are not substitutes for its existence, domain and equality arguments.
