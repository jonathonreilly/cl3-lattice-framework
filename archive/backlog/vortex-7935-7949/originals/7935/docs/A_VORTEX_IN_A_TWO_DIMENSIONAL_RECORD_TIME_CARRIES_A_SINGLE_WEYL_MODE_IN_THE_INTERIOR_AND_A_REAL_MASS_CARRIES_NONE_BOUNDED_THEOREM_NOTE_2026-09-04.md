---
claim_id: vortex_two_dimensional_record_time_single_weyl_interior_real_mass_none
claim_type: bounded_theorem
claim_scope: "In the free-field one-particle sector, on the named finite sizes only, with record time treated throughout as a SUPPLIED TWO-dimensional extra coordinate -- two ordered chains (s_1, s_2) of N sites each with nearest-neighbour adjacency, hermitian momenta K_1 and K_2, a Wilson Laplacian r_s (L_1 + L_2), the seven-generator embedding Gamma_i = s_i (x) B, Gamma_4 = I (x) alpha_1, Gamma_5 = I (x) alpha_2, Gamma_6 = I (x) alpha_3, Gamma_7 = I (x) alpha_4 with CHI = Gamma_4 Gamma_5 Gamma_6 Gamma_7, a supplied complex mass field m_1 + i m_2, a supplied size N and a supplied end convention, none of which is derived from any axiom: (T1) two record-time coordinates plus a complex mass need seven anticommuting Hermitian generators, Cl(7)'s irreducible representation is 8-dimensional so the algebra is exactly saturated, CHI = Gamma_4 Gamma_5 Gamma_6 Gamma_7 = -i Gamma_1 Gamma_2 Gamma_3 with both identities at residual 0.0e+00, and the one-dimensional control built inside this code path with the genuine Cl(5) operator reproduces the landed one-dimensional counting rule digit for digit at N_s = 64 -- two light states per transverse mode, max|E| 5.288e-16, next |E| 0.801213, wall window [24,40) +0.999975296343 doubled by the physical spin to +1.999950593 against the landed +1.999950592685428, left end -1.000000000, right end +0.000000000, net -3.33e-16. (T2) A REAL mass on a two-dimensional record time carries no 3+1D handed species at all: the seventh generator is unused, is site-diagonal and satisfies {Gamma_7, D_4} = {Gamma_7, CHI} = 0.0e+00, so every zero mode has a same-site partner of opposite chirality and the chirality density vanishes POINTWISE -- verified at 24x24 on a wall in s_1 (16 light states, max|E| 2.992e-01, max_x |chi(x)| 1.147e-15), the crossed-wall quadrant (16, 2.213e-01, 8.726e-16), the radial wall (8, 2.128e-01, 7.876e-16) and the uniform topological mass (20, 2.898e-01, 1.164e-15), worst 1.164e-15; a wall in s_1 is a codimension-one wall in a two-dimensional transverse space and its light-state count grows with the square, 8 at 16x16 against 16 at 24x24, not the one-dimensional pairing. (T3) A COMPLEX mass of winding n gives exactly 2n light states and interior chirality n: -0.999951866 at n = -1, +0.999951866 at n = +1, +1.999642307 at n = +2 and +2.998444682 at n = +3 on a 24x24 square, and +0.999939457 at 32x32 with the compensating -0.997255950 on the outer boundary ring; the count is unchanged by the end convention (core disc +0.990842962 hard against +0.990842449 free), by the core shape (tanh core interior +0.999933139) and by the core position (two light states at every offset computed); a cut-free heat-kernel index density reproduces +0.999939457240 in the core and -0.997255709 on the ring at lambda = 0.1 with sum 8.9e-16; at N = 20 the eight-component light space is an exact <chi> = +1 doublet with 99.7352 percent core weight and an exact <chi> = -1 doublet with 7.6e-07, of opposite handedness +1.000000000 against -1.000000000; and H(p)^2 = (sum_i sin^2 p_i) 1 + D_4(p)^2 holds at relative residual below 6.7e-17, giving |E(q)| = sqrt(sin^2 q + Delta(q)^2) confirmed directly at q = 0.10 pi as 0.309016995324 against 0.309016995324. (T4) The net chirality over the whole square is identically zero on all fourteen profiles and sizes computed, worst |net| 6.60e-15, because {D_4, CHI} = 0 at residual 0.0e+00 makes D_4 off-diagonal in the CHI eigenbasis with a SQUARE off-diagonal block, so dim ker A = dim ker A^dag identically and the finite-lattice index is zero by linear algebra alone; but the vortex's asymptotic vacuum has constant modulus |m| = 0.800000 at every site, is gapped at all four record-time zone corners for every phase (0.800000, at least 1.200000, at least 3.200000) and contains no interface anywhere, and a vortex/antivortex pair with zero boundary winding has no boundary mode at all, |chi(edge)| = 1.1e-17, with both interior species intact at +0.987455583 and -0.987455583. (T5) [statement] The price: the result turns entirely on a mass that is complex with a winding phase; the repository's landed occupancy-to-mass bridge supplies a real monotone mass and calls itself a motivated model/bridge and not a derivation, and there is no landed occupancy-to-phase map anywhere; a two-dimensional record time is, by the landed time-axis note's T3, a different type of object from a history, and the vortex needs that note's horn A, a branching record order whose record-inclusion order is not total, which T3 rejects because a realized history is a sequence with one index; at the operator layer a second ordered parameter is excluded only by the underived premise B-AXIS.3; and no Callan-Harvey flow is computed here because there is no gauge coupling anywhere. This is a CONDITIONAL PRICE NOTE: it states what a two-dimensional record time would buy and what it would cost, and nothing here says the axioms permit either supplied item. Interactions, dynamics, any fermion determinant, gauge coupling of any kind, curved record geometry, sizes other than those named, and windings outside n in {-1, +1, +2, +3} are out of scope. Nothing here is derived from any axiom, no axiom is amended, no status is set, no hypothesis is adopted, and no registry entry is created."
upstream_dependencies: []
runner: scripts/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.py
---

# A vortex in a two-dimensional record time carries a single Weyl mode in the interior, and a real mass carries none

**Date:** 2026-09-04
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.py`](../scripts/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.py)
**Runner cache:**
[`logs/runner-cache/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.txt`](../logs/runner-cache/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.txt)
**Parents:** none. Every premise used below is declared in this note; the one-dimensional construction it departs from is rebuilt from scratch by the runner, not imported.

A free-field diagnostic on a supplied **one-dimensional** record time gives a counting rule with two halves: the number of localized handed species equals the transition count of the
band-inversion index bracketed by the trivial vacuum, so it is always **even**; and the net chirality over the record-time volume is **zero**. That result names its own opening in as many words --
higher-dimensional and branching record time is out of scope, and is "precisely where the counting rule of `T3` could fail". This note takes that opening at face value and asks the question it
poses: **does a two-dimensional record time evade the rule?** It is a **conditional price note**. It computes what a second record-time coordinate would buy and states exactly what it would cost,
and it never asserts that the axioms permit the cost.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite free-field linear-algebra theorems about one declared object: a complex mass on a supplied two-dimensional record-time square. The Clifford identities of T1, the pointwise-vanishing mechanism of T2 and the square-block identity of T4 are zero-residual statements; the light-state counts are integers; the interior chiralities, heat-kernel densities, handedness numbers and dispersions are floating-point cross-checks at the stated tolerance; the index-equals-winding statement of T3 is a verification on a declared finite family, not a proof."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-size theorem, and route to the lane that owns record structure the two questions this note does not decide: whether a record order with two independent directions is admissible at all, and whether any occupancy-to-mass bridge can carry a phase."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. The zero-residual and integer items are exact; the items tagged `[numerical]` are
floating-point cross-checks at the stated tolerance. `T3` is a **verification on a declared finite family**, and is labelled as such wherever it appears.

1. `T1` (`A`). The algebra, and the one-dimensional counting rule reproduced digit for digit inside this code path.
2. `T2` (`B`). A real mass on a two-dimensional record time: the chirality density vanishes pointwise.
3. `T3` (`C`). A complex mass of winding `n`: the index equals the winding number.
4. `T4` (`D`). Why the net over the finite square is zero anyway, and why that is not a second interface.
5. `T5` (`E`). The price, and the supplied items it is a function of.

## Imports and authority

Imported scientific authority: none load-bearing. The Jackiw-Rossi vortex zero mode, the Callan-Harvey inflow argument, the Kaplan/Shamir domain-wall construction and the Nielsen-Ninomiya counting
are standard methodology; "Jackiw-Rossi" and "Callan-Harvey" appear below as **plain-text pointers carrying no authority**, every object is redeclared here, and the runner recomputes every
statement from scratch. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- [`DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md`](DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md): the one-dimensional periodic construction whose four-component convention the control of `T1` matches.
- `THE_RECORD_TIME_DOMAIN_WALL_ON_AN_OPEN_INTERVAL_WHERE_THE_PARTNER_WEYL_MODE_LIVES_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open branch): the one-dimensional counting rule whose two halves this note separates, and the source of the `+1.999950592685428` the control of `T1` reproduces. Not linked; it is not on the main line.
- [`TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md`](TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md): `T3`, quoted verbatim in `T5`, which classifies the object this construction needs.
- [`SINGLE_CLOCK_INDEPENDENT_COMMUTING_TRANSFER_FACTOR_N5_NO_GO_NOTE_2026-06-17.md`](SINGLE_CLOCK_INDEPENDENT_COMMUTING_TRANSFER_FACTOR_N5_NO_GO_NOTE_2026-06-17.md)
  and [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md): the status of `B-AXIS.3`, quoted verbatim in `T5`.
- [`RECORD_FORMATION_FRONT_IS_THE_DOMAIN_WALL_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md`](RECORD_FORMATION_FRONT_IS_THE_DOMAIN_WALL_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md): the occupancy-to-mass bridge, which supplies a **real, monotone** mass and calls itself "a motivated model/bridge, not a derivation".
- [`DOMAIN_WALL_EDGE_ANOMALY_INFLOW_SPECTRAL_FLOW_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md`](DOMAIN_WALL_EDGE_ANOMALY_INFLOW_SPECTRAL_FLOW_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md): the one-dimensional inflow whose two-dimensional analogue is **not** computed here.
- [`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`](NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md): there is no `gamma_5` inside the one-site algebra.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): the axioms quoted in "Setting". No grade of theirs is cited and no hypothesis is adopted.

## Setting

The framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations,
and proper cubic rotations about each site." The lattice is physical. **Record / Fixed Reality**: "Records form."; "When present, a record locks exactly one admissible local possibility. **A site
never carries more than one record; records are permanent.**"; "Only records are readable."

Records **register**; a site registers one record and it is permanent, so the per-site record set is a **singleton** and there is no per-site stack to index. Record time is therefore not
obtainable from the site algebra: it is **supplied data**, and a *second* record-time coordinate is a second helping of supplied data. Everything in "Definitions" below is declared, and nothing in
it is derived.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the eight-component embedding, the supplied two-dimensional
record-time square with its `K_1`, `K_2`, `r_s (L_1 + L_2)`, `Gamma_4 ... Gamma_7`, complex mass `m_1 + i m_2`, size `N` and end convention, and the Hamiltonian built from them. `P1` (`A`) fixes
the algebra and reproduces the one-dimensional control that every later comparison is read against; `P2` (`B`) is the real-mass pointwise-vanishing mechanism, which uses `P1`'s seventh generator;
`P3` (`C`) the winding index, its robustness, its cut-free confirmation and its Weyl data, which uses `P1`'s chirality; `P4` (`D`) the square-block identity and the pair geometry, which uses
`P3`'s profiles; `P5` (`E`) the supplied-item decomposition and the price. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

```text
alpha_1..4    t1 (x) o1, t1 (x) o2, t1 (x) o3, t2 (x) I           Cl(4) on C^4
B             alpha_1 alpha_2 alpha_3 alpha_4 = -t3 (x) I         Hermitian, B^2 = 1
embedding     Gamma_i = s_i (x) B  (i = 1,2,3)                    physical spatial
              Gamma_4 = I (x) alpha_1, Gamma_5 = I (x) alpha_2    record time      SUPPLIED
              Gamma_6 = I (x) alpha_3, Gamma_7 = I (x) alpha_4    the complex mass SUPPLIED
chirality     CHI = Gamma_4 Gamma_5 Gamma_6 Gamma_7 = -i G_1 G_2 G_3   A SPECIES LABEL
handedness    Tr(V_1 V_2 V_3) / 2i on the projected spatial velocities  THE WEYL SIGN
H(p)          sum_i sin(p_i) Gamma_i + K_1 (x) Gamma_4 + K_2 (x) Gamma_5
              + [ diag(m_1) + r_s (L_1+L_2) + r sum_i (1 - cos p_i) ] (x) Gamma_6
              + diag(m_2) (x) Gamma_7
D_4           the 4-component transverse operator; H(0) = I_2 (x) D_4
K_1, K_2      hermitian nearest-neighbour momenta on the two open chains   SUPPLIED
L_1, L_2      Wilson Laplacians; 'hard' ends hold the diagonal at 1.0,
              'free' ends at 0.5                                           SUPPLIED
m_1 + i m_2   the record-time mass field on the N x N square               SUPPLIED
vortex n      m = M e^{i n theta}, constant modulus, or M tanh(r/a) e^{i n theta}
pair          m = M e^{i(theta_L - theta_R)}: winding +1 and -1 inside, 0 at the boundary
chi(x)        the basis-free chirality density on the light subspace, summed over it
interior      the square with a pad of N/6 removed; edge is the complement
core          the disc r < max(3, N/6) about the vortex core
```

Sizes: `M = 0.8`, `r = r_s = 1`, light cut `|E| < 0.30`, hard ends unless stated. `N_s = 64` for the one-dimensional control; `N = 24` for the profile table and the robustness checks; `N = 16` for
the light-state growth; `N = 32` for the size row, the cumulative radial profile and the heat-kernel density; `N = 20` for the eight-component checks; `N = 12` and `N = 8` for the operator
identities. Because `{D_4, CHI} = 0` exactly, `D_4` is off-diagonal in the `CHI` eigenbasis with a **square** block `A`, and one singular value decomposition of `A` gives the whole spectrum and
the whole chirality density; the largest dense matrix is therefore `2048 x 2048` for the transverse work and `3200 x 3200` for the eight-component work, both inside the declared bound.

## Theorem 1 -- the algebra is exactly saturated, and the one-dimensional rule reproduces

**Conclusion.** Two record-time coordinates plus a complex mass need **seven** mutually anticommuting Hermitian generators. The irreducible representation of `Cl(7)` is **8-dimensional**, so the
spinor is eight-component and the algebra is **exactly saturated** -- seven is the maximum for `8 x 8` -- with `max ||{Gamma_A, Gamma_B} - 2 delta_AB|| = 0.0e+00`. The 3+1D chirality is the volume
element of the physical spatial Clifford algebra inside the enlarged one: `CHI = Gamma_4 Gamma_5 Gamma_6 Gamma_7 = -i Gamma_1 Gamma_2 Gamma_3`, **both identities at residual `0.0e+00`**, with
`CHI^2 = 1`, Hermitian and traceless, commuting with `Gamma_1,2,3` and anticommuting with `Gamma_4 ... Gamma_7` at `0.0e+00`. Built inside this code path with the **genuine** `Cl(5)` operator `d =
K_s sigma_2 + [diag(m) + r_s L_s] sigma_3` and `chi = i sigma_2 sigma_3`, the one-dimensional control at `N_s = 64` gives two light states per transverse mode, `max|E| = 5.288e-16` against a next
`|E|` of `0.801213`, wall window `[24,40)` chirality `+0.999975296343` -- doubled by the physical spin to the four-component convention, `+1.999950593` against the landed `+1.999950592685428`,
**digit for digit** -- with `-1.000000000` at the left end, `+0.000000000` at the right and a net of `-3.33e-16`.

**Method.** The same construction as the landed one-dimensional chirality, one dimension up. There is no contradiction with the no-per-site-chirality theorem: `Gamma_i = s_i (x) B` is not
`sigma_i`, and `-i Gamma_1 Gamma_2 Gamma_3 = I (x) B` is not an element of the one-site `M_2(C)`.

## Theorem 2 -- a real mass on a two-dimensional record time carries no handed species at all

**Conclusion.** With a purely real mass the seventh generator `Gamma_7` is **unused**. It is **site-diagonal** and satisfies `{Gamma_7, D_4} = {Gamma_7, CHI} = 0.0e+00`, so it maps `ker D_4` to
`ker D_4` and flips the chirality **without leaving the site**: every zero mode has a same-site partner of opposite chirality, and the 3+1D chirality density vanishes **pointwise**, not merely on
average. Verified at `24 x 24` on four declared real profiles: a wall in `s_1` (16 light states, `max|E|` `2.992e-01`, next `0.382635`, `max_x |chi(x)| = 1.147e-15`), the crossed-wall quadrant
(`16`, `2.213e-01`, `0.305534`, `8.726e-16`), the radial wall (`8`, `2.128e-01`, `0.352697`, `7.876e-16`) and the uniform topological mass (`20`, `2.898e-01`, `0.352601`, `1.164e-15`) -- worst
`1.164e-15`, with the net zero on each. A wall in `s_1` is a codimension-**one** wall in a **two**-dimensional transverse space, and its light-state count **grows with the square**: `8` at `16 x
16` against `16` at `24 x 24`, a dispersing band along the uncompactified `s_2` rather than the one-dimensional wall's two zero modes.

**Reading, not theorem.** The pointwise vanishing is an identity of the algebra, independent of the profile and of the end convention. The one-dimensional case has no such operator: there the
transverse algebra is `Cl(2)` on `C^2`, the third anticommuting `2 x 2` matrix **is** the chirality, and `2 x 2` admits no fourth. That dimensional accident is what makes the one-dimensional
counting rule non-trivial, and what makes the two-dimensional real-mass rule trivial. On the evidence here, a second record-time coordinate carrying the framework's **real** mass is strictly
**worse** than one: it carries nothing handed at all.

## Theorem 3 -- a complex mass of winding n: the index equals the winding number

**Conclusion.** A complex mass `M e^{i n theta}` on the square gives **exactly `2n` light states** and interior chirality `n`. At `24 x 24`: `-0.999951866` at `n = -1`, `+0.999951866` at `n = +1`
(`max|E| = 2.727e-07` against a next `|E|` of `0.35586`), `+1.999642307` at `n = +2` and `+2.998444682` at `n = +3`. At `32 x 32` the winding-1 number is `+0.999939457` inside `r < N/4` with
`-0.997255950` on the outer boundary ring; cumulatively inside radius `W` the chirality reads `+0.818503353`, `+0.990842714`, `+0.999939457` and `+0.999994126` at `W = 2, 4, 8, 12`. The count is a
property of the defect: unchanged by the end convention (core disc `+0.990842962` hard against `+0.990842449` free), by the core shape (`tanh` core, interior `+0.999933139` against `+0.999951866`
for constant modulus) and by the core position (two light states at every offset computed, the chirality inside a disc about the **origin** falling `+0.990842962`, `+0.960656303`, `+0.717660942`
as the core sits elsewhere). A **cut-free** heat-kernel index density `q(x) = Tr_x[CHI exp(-D_4^2/lambda^2)]`, which uses no light-mode cut anywhere, gives `+0.999939457240` in the core and
`-0.997255709` on the ring at `lambda = 0.1` with `sum_x q = -8.9e-16`, and `+0.999938991630 / -0.996845485` at `lambda = 0.2`. On the full eight-component operator at `N = 20` the four light
states satisfy `H PSI = PSI E` at residual `1.4e-14` with `max|E| = 5.362e-06` against a next `|E|` of `0.387679`, and `CHI` splits them into an **exact** `+1.000000000` doublet, core-bound to
`99.7352%`, and an **exact** `-1.000000000` doublet holding `7.6e-07` of its weight in the core; the projected velocities close the Clifford algebra (`||V^2 - 1|| <= 9.4e-16`) and the handedness
is `+1.000000000` at the core against `-1.000000000` on the boundary. Finally `H(p)^2 = (sum_i sin^2 p_i) 1 + D_4(p)^2` holds as an operator identity at relative residual `<= 6.7e-17` at `N = 12`
and `N = 20`, so the localized branch is an exact Weyl cone `|E(q)| = sqrt(sin^2 q + Delta(q)^2)`; diagonalizing the eight-component operator directly at `q = 0.10 pi` gives `0.309016995324`
against the predicted `0.309016995324`, agreeing to ten decimals.

**Status of this statement.** This is a **verification on a declared finite family** -- windings `n in {-1, +1, +2, +3}`, two core shapes, two end conventions, three core positions and the named
sizes -- and **not a proof**. It is not offered as a general theorem about record-time geometries.

**Disclosure.** The `n = 3` interior number at `24 x 24` reads `+2.998444682`, a deficit of `1.556e-03` against the lower windings' `4.8e-05`. This is the pad-4 interior mask cutting the broader
winding-3 modes on a `24 x 24` square, a finite-size property of the mask; the integer statement -- exactly `2n = 6` light states -- is exact, and the winding-1 deficit falls to `6.05e-05` at `32
x 32`. The runner tags that row `[2e-03]` and says why. Two further conventions deserve a line. `<chi>` is a species label and the handedness is reported separately throughout; and in **this**
embedding handedness `= +<chi>`, whereas in the landed one-dimensional embedding it is `-<chi>`, so a reader comparing the two notes' tables will see the correlation flip sign. Both label the same
physics.

## Theorem 4 -- the net over the finite square is zero, and the partner is not a second interface

**Conclusion.** `{D_4, CHI} = 0` holds at residual `0.0e+00` on the lattice for every profile and every end convention, so in the `CHI` eigenbasis `D_4 = [[0, A], [A^dag, 0]]` at residual
`0.0e+00` with `A` **square** -- each `CHI` eigenspace has dimension `2 N^2`. For a square matrix `dim ker A = dim ker A^dag` identically, so the index of **any** finite lattice realization is
zero by linear algebra alone: a statement about **finiteness**, not about the record-time geometry. The net chirality is accordingly zero on all fourteen profiles and sizes computed, worst `|net|
= 6.60e-15`. **But the vortex is not another interface geometry.** Its asymptotic vacuum has constant modulus `|m| = 0.800000` at every site, so no site carries a vanishing mass; it is gapped at
all four record-time zone corners for every phase of the winding (`0.800000` at `(0,0)`, at least `1.200000` at `(pi,0)` and `(0,pi)`, at least `3.200000` at `(pi,pi)`), so the Wilson term keeps
the doubler corners out of the index; and it contains **no interface anywhere**. A vortex/antivortex pair -- winding `+1` and `-1` inside, **zero** winding at the square's boundary -- has **no
boundary mode at all**, `|chi(edge)| = 1.1e-17`, with both interior species intact at `+0.987455583` and `-0.987455583` on the two cores and a net of `-1.55e-15`.

**Reading, not theorem.** The compensating species of `T3` is a **boundary effect of nonzero boundary winding**, not a second defect. In one dimension one cannot have a single wall and no second
interface; here one can have a single vortex and no second defect, and the pair geometry makes that decisive by removing the boundary species outright while leaving both interior ones.

## Theorem 5 -- the price [statement]

**Conclusion.** The construction is a function of the one-dimensional note's seven supplied items -- an ordered record-time coordinate with nearest-neighbour adjacency, `K_s`, `r_s L_s`, a
record-time Clifford generator, a mass field `m(s)`, an unbounded extent and an end convention -- **plus exactly two named here**: a **second** ordered record index `s_2`, independent of the
first, with its own momentum, Wilson term and Clifford generator; and a **phase-valued** mass `m_1 + i m_2` carrying a winding, with its seventh Clifford generator and the eight-component
embedding. Rebuilt from those alone the operator reproduces at residual `0.0`, and no term is redundant (withdrawing them changes the operator by `33.226`, `33.226`, `110.278`, `27.153`). The
price of the two added items is this.

1. **The phase.** The whole result turns on the mass being complex with a winding phase. The repository's landed occupancy-to-mass bridge supplies "an explicit monotone
   record-occupancy front", `m(s) = M (2 theta(s) - 1)`, and says of itself: *"The map is a motivated model/bridge, not a derivation from full record-production
   dynamics."* It is **real** and **monotone**, and `T2` shows that on a two-dimensional record time a real mass carries **nothing handed at all**. There is no landed
   occupancy-to-**phase** map anywhere in the repository, not even a motivated one.
2. **The second index.** The landed time-axis note's `T3` classifies exactly the object this construction needs, and does so as a **type** claim: *"A realized history is
   a **sequence** (the sibling's note-level definition, imported and flagged): one index. A second independent record-layer clock would be a **2D grid** of
   configurations with two independent nesting directions -- a different **type** of object, not a history."* The vortex needs that note's **horn A**, where *"the
   record-inclusion order is not total and the grid does not embed as a single sequence with one record-monotone direction"* -- a **branching** record order. Horn B's
   total order serializes to one chain, which is the one-dimensional construction and its forced partner interface, because a winding number needs two coordinates.
3. **What is open, and what is not.** At the **operator** layer the second ordered parameter is excluded only by the underived premise `B-AXIS.3`: *"A two-clock
   comparator exists mathematically (two commuting tensor-factor transfers with a 2-dimensional generator span; runner block [C-2CLK]) and is excluded only by
   (B-AXIS.3) -- the premise excludes something realizable, so it is non-vacuous and load-bearing"*, and *"B-AXIS.3 cannot be derived from the current minimal surface by
   appealing only to local tensor factorization, finite Stone uniqueness, or Record durability/additivity."* At the **record** layer `T3` is a type claim and this note
   does not touch it.
4. **No inflow.** No Callan-Harvey flow is computed anywhere in this runner. There is **no gauge coupling at all** -- no background flux quantum, no Peierls phases -- so
   no inflow statement is made, and none may be read into the numbers above.

## Corollary -- what a two-dimensional record time supplies, on the geometries computed

Within the setting declared above, in the free-field one-particle sector, and on the finite sizes named:

1. **With a real mass, a second record-time coordinate is worse than one.** Not a weaker handed species: **no handed species at all**, at any site, on every real
   profile computed, `max_x |chi(x)| <= 1.164e-15`. The one-dimensional counting rule does not carry over, because the extra transverse dimension frees a site-diagonal
   generator that flips the chirality in place.
2. **With a complex mass of winding `n`, the interior carries exactly `n` unpaired species, and the partner is bound on the outer boundary.** A vortex/antivortex pair
   with zero boundary winding removes that partner entirely while both interior species stay intact. So the counting rule's **transition-count half is replaced by a
   winding number**, which can be odd and can be one; and its **net-zero half survives**, but only as a finite-lattice boundary identity that holds by linear algebra on
   a square block, for a reason that has nothing to do with record-time geometry.
3. **So handed matter is reachable in this construction, at a stated price.** The price is a two-dimensional -- branching -- record order, which the landed time-axis
   note classifies as a different type of object from a history, and a phase-valued mass, for which the repository has no bridge.
4. **Nothing here says the axioms permit either.** This note asserts no route. It computes a price and names it for its owner: whether a record order with two
   independent directions is admissible belongs to the lane that owns record structure, and whether any occupancy-to-mass bridge can carry a phase belongs to the lane
   that owns the bridge. Neither question is decided here, and no answer to either is implied by the numbers.

**Reading, not theorem (this register).** Give the record stack two ordered directions instead of one, and a mass that winds around a point like a whirlpool, and a single handed species sits at
the centre with its partner pushed to the far edge, where a second whirlpool turning the other way removes it. A plain wall in two record directions gives nothing handed at all. What this costs is
a record order that branches, which the framework's own account of time says is not a history, and a mass with a phase, which nothing in the framework yet supplies. That is the exact price of
handedness on this route.

## What is not changed

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. `B-AXIS.3` is quoted, not retired; the landed `T3` is quoted, not
  contradicted, and this note does not claim the object `T3` classifies is available.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms: the two record-time coordinates, their operators, their Clifford generators, the complex mass field, its winding, the size and
  the end convention are declared objects, and no coefficient is derived.
- The eight-component embedding is a diagnostic construction, not an axiom, a primitive registration, or a claim about the one-site algebra.
- The index-equals-winding statement of `T3` is not promoted to a proof or to a general statement about record time, and nothing here is framed as foreclosing anything.

## Interfaces named for other lanes, not taken up here

- **The phase bridge.** Whether any occupancy-to-mass map can carry a **phase**, rather than the real monotone value the landed bridge supplies, is untouched here and is
  the single load-bearing gap. It belongs to the lane that owns the bridge.
- **A branching record order.** Whether a record order with two independent directions -- horn A of the landed `T3`, an order that is not total -- is admissible at all
  is a question for the lane that owns record structure. This note computes what such an order would buy; it does not argue that it is available.
- **Callan-Harvey flow with a gauge coupling.** The one-dimensional companion computes an inflow with one non-dynamical `U(1)` flux quantum. Nothing of the kind is
  computed here. The two-dimensional analogue -- flux through the record-time square, spectral flow on the vortex branch -- is the obvious follow-on and is named as
  missing, not attempted.

## Remaining live routes

1. Larger squares and other windings. `N <= 32` for the transverse work, `N = 20` for the eight-component work, and `n in {-1, +1, +2, +3}` are what is computed.
2. Other end conventions and core profiles. Hard and free ends, a constant-modulus core and a `tanh` core, three core positions; other completions are not computed.
3. Smooth two-dimensional fronts. Every profile here is a declared analytic form; a scan over a declared family in the one-dimensional note's idiom is not attempted.
4. The many-body statements. Everything here is one-particle; no sea, no fermion determinant, no anomaly matching.

## Executable claim block

```text
setting: free-field one-particle sector; eight-component embedding Gamma_i = s_i (x) B, Gamma_4..7 = I (x) alpha_1..4, CHI = Gamma_4 Gamma_5 Gamma_6 Gamma_7 = -i Gamma_1 Gamma_2 Gamma_3; record time SUPPLIED as a TWO-dimensional open N x N square with K_1, K_2, r_s (L_1+L_2), a complex mass m_1 + i m_2, a size N and an end convention; M = 0.8, r = r_s = 1, light cut 0.30; axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
T1 algebra + control: Cl(7) on C^8 exactly saturated, max ||{Gamma_A,Gamma_B} - 2 delta|| = 0.0e+00; CHI = Gamma_4 Gamma_5 Gamma_6 Gamma_7 = -i Gamma_1 Gamma_2 Gamma_3 at residual 0.0e+00 / 0.0e+00; 1D control N_s = 64 -> 2 light states per transverse mode, max|E| 5.288e-16, next 0.801213, wall window [24,40) +0.999975296343, doubled +1.999950593 against the landed +1.999950592685428, left end -1.000000000, right end +0.000000000, net -3.33e-16
T2 real mass [1e-12]: Gamma_7 unused and site-diagonal, {Gamma_7,D_4} = {Gamma_7,CHI} = 0.0e+00 -> chirality density zero POINTWISE; 24x24 wall in s_1 (16 light, 2.992e-01, 1.147e-15), quadrant (16, 2.213e-01, 8.726e-16), radial (8, 2.128e-01, 7.876e-16), uniform topological (20, 2.898e-01, 1.164e-15); light-state count grows 8 at 16x16 -> 16 at 24x24
T3 winding index [verified on a declared family, not proved]: exactly 2n light states; interior chirality -0.999951866 / +0.999951866 / +1.999642307 / +2.998444682 at n = -1/+1/+2/+3 on 24x24, +0.999939457 at 32x32 with -0.997255950 on the ring; hard +0.990842962 vs free +0.990842449; tanh core +0.999933139; offsets 0/2/4 all 2 light states; heat kernel lam=0.1 core +0.999939457240 ring -0.997255709 sum -8.9e-16; N=20 eight-component <chi> doublets +1.000000000 / -1.000000000, core weights 0.997352 / 7.6e-07, handedness +1.000000000 / -1.000000000; H^2 identity <= 6.7e-17; |E(0.10 pi)| = 0.309016995324 = sqrt(sin^2 q + Delta^2)
T4 net zero + no interface: {D_4,CHI} = 0.0e+00, block form residual 0.0e+00, A SQUARE -> index 0 by linear algebra; worst |net| 6.60e-15 over 14 profiles and sizes; asymptotic |m| = 0.800000 at every site, zone-corner gaps 0.800000 / >= 1.200000 / >= 3.200000, no interface; vortex/antivortex pair |chi(edge)| = 1.1e-17 with cores +0.987455583 / -0.987455583, net -1.55e-15
T5 price [statement]: seven supplied items from the 1D note plus two named here (a second ordered record index; a phase-valued mass); rebuild residual 0.0, none redundant (33.226 / 33.226 / 110.278 / 27.153); the landed bridge is real and monotone and calls itself "a motivated model/bridge, not a derivation"; no occupancy-to-phase map exists; the landed T3 calls a two-index record order "a different type of object, not a history" and the vortex needs its horn A; B-AXIS.3 is underived and load-bearing; NO gauge coupling and NO Callan-Harvey flow anywhere
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=26 FAIL=0
```

## Proof boundary

Everything is **free field** and **one particle**. There is no interaction, no dynamics, no fermion determinant, and **no gauge coupling of any kind** -- not one background flux quantum. No
anomaly matching is proven, no inflow is computed, and no continuum limit is taken.

All record-time structure is **supplied**: the one-dimensional note's seven items -- an ordered coordinate with nearest-neighbour adjacency, `K_s`, `r_s L_s`, a record-time Clifford generator,
`m(s)`, an unbounded extent, an end condition -- **plus the two named in `T5`**: a second ordered record index independent of the first, and a phase-valued mass with a winding. None is derived
from the four axioms. The second index is the object the landed time-axis `T3` classifies as a different type of object from a history, and the phase is the object for which the repository has no
bridge; both are declared here as supplied data and neither is claimed to be available. The eight-component embedding is a diagnostic construction, not an axiom and not a primitive registration;
`<chi>` is a species label and not the Weyl handedness, which is reported separately throughout.

The sizes are the named finite ones and nothing else: `N_s = 64` for the control, `N = 24` for the profile table and the robustness rows, `N = 16` for the light-state growth, `N = 32` for the
single size row and the cut-free density, `N = 20` for the eight-component checks, `N = 12` and `N = 8` for the operator identities. Nothing is claimed at any other size, and the largest dense
matrix is `3200 x 3200`.

`T3` is **verified on a declared finite family, not proved**: windings `n in {-1, +1, +2, +3}`, a constant-modulus core and a `tanh` core, hard and free ends, three core positions, and the sizes
named. Windings outside that set are not covered, smooth or randomized profiles are not covered, and no scan was run -- there is **no randomness and no seed anywhere in the runner**. The `n = 3`
interior deficit of `1.556e-03` is disclosed under `T3` as a property of the interior mask at `24 x 24`.

`T4`'s net-zero identity is a statement about a **finite** lattice. It is not a statement about the record-time geometry, and it is not offered as foreclosing anything: the interior number of `T3`
and the net of `T4` are two halves of one finite-size statement, and the note says which half each is.

## Review record

An honest auditor should come away with: the algebra saturated and both chirality identities exact at `0.0e+00`, the landed one-dimensional counting rule reproduced digit for digit inside this
code path before anything new is claimed, and then two departures on named finite sizes. First, a **real** mass on a two-dimensional record time carries **no** 3+1D handed species at any site --
an identity of the algebra, `{Gamma_7, D_4} = {Gamma_7, CHI} = 0.0e+00`, verified to `1.164e-15` on four declared profiles. Second, a **complex** mass of winding `n` carries **exactly `n`** in the
interior with exactly `2n` light states, robust to the end convention, the core shape and the core position, confirmed cut-free by a heat-kernel density, and exhibited at `N = 20` as an exact
`<chi> = +1` doublet with `99.74%` core weight, opposite in handedness to the boundary doublet, on an exact Weyl cone.

The auditor should also come away with four caveats. The index-equals-winding statement is a **verification on a declared finite family**, not a proof. The net over the finite square is **zero at
every size and profile computed**, for a reason -- a square off-diagonal block -- that has nothing to do with the record-time geometry, so only the transition-count half of the one-dimensional
rule is replaced. **No gauge coupling and no inflow appear anywhere.** And every piece of the two-dimensional record-time direction is supplied data -- nine items now, the second coordinate and
the phase among them -- so this note bounds what the construction gives, not what the axioms give. It is a **conditional price note**: it states the price and names it for its owner, and it
asserts no route.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the pointers in "Imports and authority" carry no grade and
no weight. Hard landing conditions are a fresh runner and cache pair closing at `PASS=26 FAIL=0`, runtime under the declared `150` seconds, and passing pipeline and strict-lint gates; independent
audit remains a separate lane.

## Validation

Run:

```bash
python3 scripts/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.py
```

Expected terminal summary:

```text
TOTAL: PASS=26 FAIL=0
```
