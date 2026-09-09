---
claim_id: directed_formation_sweep_registers_direction_of_motion_not_handedness_2026_09_05
claim_type: bounded_theorem
claim_scope: "One-particle and determinantal record numerics on declared finite geometries, with a complete many-body tree check on two small blocks and complete integer enumerations over the ternary nearest-neighbour profile alphabet. SUPPLIED, none of it read out of any axiom: the body-diagonal second mass M2 with its winding phase and the 12x12x24 string (PR #7949) as PR #7989 rebuilt it, the half-filled sea and the determinantal record law (PR #7883), the star tick with the rotated kernel K = G P G+ (PR #7986), the record-time vortex construction of PR #7935 in full, and this note's own tick model (site-set Model A with end-recorded hop deletion and tau), its formation sweeps with their quadrant construction and seam, its regions, columns, rules and order-pseudoscalar. (T1) Under the tick model a formation sweep directed along the string axis separates the string's core right-mover from its time-reversal partner, the anti-string's core left-mover, at order one: registration odds 0.1366 against 0.6048 at the core, Delta_core = -0.46825 at tau = 0.5 with the transfer to the ring Delta_ring = +0.54803, the T-partner identity exact at 0.0e+00 in the density and 0.0e+00 in total variation at the pattern level and many-body, growing with the string length (-0.4683, -0.5031, -0.5264 at L_z = 24, 48, 96), stable in the transverse size (-0.4352, -0.4683, -0.4507) and momentum (-0.5444, -0.5270, -0.4683), and superlinear at small tau (Delta/tau = -0.22, -0.53, -0.81 at tau = 0.05, 0.1, 0.25). (T2) The screw sense of the sweep contributes exactly nothing on the string: Delta(screw+) - Delta(screw-) <= 1.7e-16 at every pitch and direction with the densities pointwise mirror images to 3.6e-17, because the string is its own sigma_x image and sigma_x maps screw+ onto screw-; with the core off the mirror plane the screw difference is a boundary effect falling like the ring weight, -4.0e-03, -7.8e-04, +2.1e-04 at N_s = 8, 12, 16. (T3) C2(x) composed with complex conjugation is an exact anti-unitary symmetry of the string, giving Delta(S) = -Delta(C2(x) S) to 2.8e-16 and pointwise 6.9e-17, so every C2(x)-closed family of sweeps averages to exactly zero while reversal-closed screw families keep a seam of +0.002 to +0.006; and the rotated kernel is even under sigma_z times particle-hole times tau reversal, 6.6e-17 pointwise and 9.4e-15 in total variation. (T4) On the record-time vortex the registration is exactly time-even for every sweep, tau and momentum (<= 2.2e-15), certified by a site-diagonal conserved helicity and the transverse anti-unitary alpha_1 alpha_4 at 0.0e+00; the anti-vortex is C conj(H) C+ for a monomial site-independent C at residual 0.0e+00; and the spiral sense registers a parity-odd, time-even difference of a few percent (0.9196 against 0.9469 at pitch 2) because the Wilson vortex is not its own mirror image. (T5) On the cube and the slab no covariant nearest-neighbour rule selects a handed formation order: complete dynamic-programming counts over the 3^V ternary configurations give mean order-pseudoscalar exactly 0.000e+00 for every rule with or without empty menus, the readable class admits every order (1961990553600 = 12! x 2^12 complete paths, 0 dead ends), the rule that forbids one chiral shape admits screw+ and screw- with all 4096 value assignments, and the mechanism is identified on the slab. Interactions, wider windows, other geometries, other momenta and boundary conditions, and the uniform-order average are out of scope. No axiom is changed, no status is set, no hypothesis is adopted, and no registry entry is created."
upstream_dependencies: []
runner: scripts/directed_formation_sweep_direction_of_motion_not_handedness_check_2026_09_05.py
---

# A time-directed formation sweep registers the direction of motion of the string's movers at order one and the screw sense of the sweep registers nothing: the mirror difference is an exact zero on the string, the record-time vortex's registration is exactly time-even, and no nearest-neighbour rule selects a handed order (bounded, one-particle with a many-body check, declared sweeps)

**Date:** 2026-09-05
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/directed_formation_sweep_direction_of_motion_not_handedness_check_2026_09_05.py`](../scripts/directed_formation_sweep_direction_of_motion_not_handedness_check_2026_09_05.py)
**Runner cache:**
[`logs/runner-cache/directed_formation_sweep_direction_of_motion_not_handedness_check_2026_09_05.txt`](../logs/runner-cache/directed_formation_sweep_direction_of_motion_not_handedness_check_2026_09_05.txt)
**Parents:** none load-bearing. Every object used below is declared in this note and rebuilt from scratch by the runner; the notes named in "Imports and authority" are plain-text pointers carrying no grade and no dependency weight.

The question this note answers is the owner's: *could chirality be obtained from a mirrored configuration of neighbourhood maps applied in record time?* The framework's time is the direction in which records accumulate, so the natural way to make a mirrored configuration act is to sweep the formation front along a screw. The arithmetic below separates two things that the question runs together. A **directed** sweep registers a great deal: it separates a mover from its time-reversal partner at order one. The **screw sense** of that sweep registers nothing at all on the object the handedness line cares about, and the reason is an exact mirror-image identity, not a small number. What a directed sweep sees is the sign of the mover's motion along the arrow of formation - a polar quantity of the `d.J` kind, the record-side image of a current - and not a pseudoscalar handedness.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "T1's time-reversal identity, T2's mirror identity, T3's two anti-unitary identities, T4's helicity certificate and anti-vortex identity, and T5's integer path counts and mean order-pseudoscalar are exact or machine-precision statements on named finite objects; the registration odds, the scans in tau, size, length and momentum, the pattern-level correlators and the vortex spiral odds are floating-point statements on the declared geometries at the stated tolerance. The tick model, the sweeps, the regions and the rules are supplied by this note. No statement here is a proof about the infinite lattice, and none is read out of any axiom."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-size result, and route to the record-time lane the one quantity this note prices but does not compute: whether any formation process whose order statistics are covariant under the proper rotations can register a nonzero time-odd bias at all, given that every C2(x)-closed family averages to exactly zero."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`G`. The zero-residual and integer items are exact; the items tagged `[numerical]` are floating-point statements on the named finite geometries at the stated tolerance.

1. `T1` (`A`, `B`). A time-directed plane sweep along `+z` separates the string's core right-mover from the anti-string's core left-mover at order one.
2. `T2` (`C`). The screw sense of the sweep contributes exactly nothing on the string, and off the mirror plane only a boundary effect.
3. `T3` (`D`). Two exact anti-unitary identities organise the census: `C2(x)` with conjugation, and `sigma_z` with particle-hole and time reversal.
4. `T4` (`E`, `F`). The tick model is certified many-body; on the record-time vortex the registration is exactly time-even and the spiral sense registers a parity-odd, time-even few-percent difference.
5. `T5` (`G`). No covariant nearest-neighbour rule selects a handed formation order on the cube or the slab.

## Imports and authority

Imported scientific authority: none load-bearing. Kawamoto-Smit staggered signs, Jacobi-Anger Chebyshev propagation, determinantal point processes, Burnside's counting lemma and the Jackiw-Rossi vortex mode are standard methodology and appear below only as **plain-text pointers carrying no authority**; every object is redeclared here and the runner recomputes every statement from scratch. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight: `A_MIRROR_ASYMMETRIC_ADMISSIBILITY_RULE_REGISTERS_ITS_OWN_PARITY_ODD_TEXTURE_AND_NOTHING_ELSE_..._BOUNDED_NOTE_2026-09-05.md` (PR #7989, the chiral-rule census and the T-blindness lemma); `THE_STAR_TICKS_RECORD_LAW_IS_EXACTLY_DETERMINANTAL_WITH_A_ROTATED_KERNEL_..._BOUNDED_NOTE_2026-09-05.md` (PR #7986, the rotated kernel); `NO_SITE_WISE_FORMATION_RULE_PRESERVES_THE_SEA_UNDER_TICK_EVOLUTION_..._NOTE_2026-09-03.md` (PR #7947, the set-wise formation unit); `THE_TASTE_SINGLET_SECOND_MASS_IS_A_BODY_DIAGONAL_IMAGINARY_HOP_AND_ITS_VORTEX_STRINGS_CARRY_2N_CO_MOVING_MODES_BOUNDED_THEOREM_NOTE_2026-09-03.md` (PR #7949, the second mass and the string); `A_VORTEX_IN_A_TWO_DIMENSIONAL_RECORD_TIME_CARRIES_A_SINGLE_WEYL_MODE_IN_THE_INTERIOR_AND_A_REAL_MASS_CARRIES_NONE_BOUNDED_THEOREM_NOTE_2026-09-04.md` (PR #7935, the record-time vortex); `A_READABLE_MATTER_LAW_EXISTS_ON_THE_5X5X5_WINDOW_..._BOUNDED_NOTE_2026-09-04.md` (PR #7982, the readable class); `RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (PR #7883, the determinantal record statistics). None is linked and none is on the main line. [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the clauses quoted in "Setting"; no grade of it is cited and no hypothesis is adopted.

## Setting

The framework axioms are quoted, not amended. **Lattice / Physical Locality**, verbatim:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

**Admissibility / Local Constraint**, first clause, verbatim:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

and its second reading note, verbatim:

> (2) Read with Record, the
> distribution concerns which possibility a forming record locks, conditional
> on formation at that site; it does not supply the formation site, probability,
> or rate.

Covariance is demanded under the 24 **proper** rotations only, so a nearest-neighbour rule is allowed to differ from its mirror image; that is the room the owner's idea needs. The reading note is the other half of the setting: the rule does not supply the formation site or the rate, so a formation **order** - and in particular a screw-shaped one - is not axiom content. `T5` asks whether a covariant rule can nevertheless force one by admissibility alone, and finds that on the cube and the slab it cannot. Everything the sweeps do below therefore rests on a supplied directed order.

Supplied by the open branches and taken as they stand: the body-diagonal second mass `M2` with its winding phase and the `12x12x24` string it binds (PR #7949), rebuilt exactly as PR #7989 rebuilt it; the half-filled sea and its determinantal record law (PR #7883); the star tick with the rotated kernel `K = G P G+` (PR #7986); the set-wise formation unit (PR #7947); the record-time vortex on the eight-component embedding (PR #7935). Supplied by this note and by no parent: the tick model in the form used here, the sweeps and their quadrant construction, the regions and columns, the rules and the order-pseudoscalar, and every tolerance.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the string with its sea and movers, the tick model, the sweeps, the regions, the vortex and the profile alphabet (`A`, `F1`, `G1`). `P1` (`B`) is the directed registration and its scans, which uses `P0` and the time-reversal identity. `P2` (`C`) is the screw-sense zero, which uses `P0`'s point-group census. `P3` (`D`) is the two anti-unitary identities and the pattern-level laws, which uses `P0` and `P1`. `P4` (`E`, `F`) is the many-body certification of the tick model and the vortex battery, which uses `P0` and `P3`'s reading of the kernel. `P5` (`G`) is the rule census, which uses `P0`'s alphabet only. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

```text
string        h_KS + m1 eps_v + m2 M2 on a 12x12x24 coarse lattice, one mode per
              site, Kawamoto-Smit signs eta_x = 1, eta_y = (-1)^x,
              eta_z = (-1)^{x+y}; M2[sbar, s] = i(-1)^{b_2} on every 2x2x2 cell
              with even corner; m1 + i m2 = M0 tanh(rho/xi) e^{i n phi} about a
              core at (5.5, 5.5), M0 = 0.7, xi = 2, open plane, periodic
              axis                                                    SUPPLIED
anti-string   conj(h), the winding reversal n -> -n                   SUPPLIED
sea           the 1728 modes of negative energy; the half filling sector
core R        the E > 0 doublet at p = +pi/6 of maximal core weight, dE/dp > 0
ring L        the E > 0 doublet at p = -pi/6 of maximal ring weight, dE/dp < 0
hole          the E < 0 core doublet at p = -pi/6, which also moves +z
tick model    site-set Model A at the coarse one-particle level: a formation
              step records a declared SET of sites, locking their occupations
              with Born odds; between steps the pre-record state runs by
              exp(-i tau h_R), h_R = h with every hop touching a recorded site
              deleted.  The record law of a schedule is determinantal with
              K = G P G+, G = prod exp(-i tau h_{R_i})                THIS NOTE
sweep         cells are (z-slice, quadrant about the core); a screw of pitch p
              and sense s forms the cells of equal t = z - s p (q + 1/2)/4
              together, in increasing t; p = 0 is the plane sweep; direction
              -z is the reversed list                                 THIS NOTE
regions       core rho < 3.5, ring within 2 of the plane edge, bulk the rest
mu(v)         |G psi(v)|^2, the mover's registered excess density, traced over
              the doublet, per mode
Delta_reg     O_reg(+tau) - O_reg(-tau), the registration of the string's mover
              against its time-reversal partner under one and the same sweep
column        the 2x2x4 core column x, y in {5, 6}, z in {10..13}: 16 sites,
              65536 patterns, carrying the sea plus the mover
chi_k^sigma   the signed sum over sigma-mirror pairs of k-subsets of
              det K_S - det K_{sigma S}, exactly odd under the relabelling
A_x           TV(p, sigma_x p), the mirror asymmetry of a pattern law
vortex        PR #7935's record-time vortex: Cl(7) on C^8, Gamma_i = s_i x B,
              Gamma_{4..7} = I x alpha_{1..4}, open N = 16 record-time square
              with hard ends, Wilson r_s(L_1 + L_2), constant-modulus complex
              mass M e^{i theta} with M = 0.8, Bloch momentum p         SUPPLIED
spiral        the same construction in the record-time plane, cells indexed by
              (shell, quadrant), pitch in shells per turn, sense +-  THIS NOTE
profile       ternary map from the six offsets to {open, 0, 1}: the
              nearest-neighbour condition a corner reads
orbit A       (+x:0, -x:1, +y:0, -y:open, +z:1, -z:open) and its 24 proper
              rotations; orbit B its inversion image
rule          a menu in {0, 1} per proper orbit; an empty menu means the site
              cannot form under that condition                       THIS NOTE
Xi            the order-pseudoscalar sum over formation events of
              sum_{u,w recorded, d(u,v) < d(w,v)} det[r_u, r_w, r_v]: odd under
              every mirror, invariant under the proper rotations     THIS NOTE
```

Sizes: the `12x12x24` string in its 12 cell-momentum sectors of dimension 288, with `8x8`, `16x16` and `20x20` planes and `L_z = 48, 96` for the scans; the `2x2x4` core column; the open `2x2x2` and `2x2x3` blocks for the many-body tree, in the 5- and 7-particle sectors of dimension 56 and 792; the record-time vortex at `N = 16` (dimension 2048) with the certificate at `N = 12`; the open `2x2x2` cube and `2x2x3` slab for the rule census. **There is no random number and no seed anywhere in the runner**: every enumeration is complete or a declared sub-family, every sweep is declared, and every eigenproblem is a deterministic LAPACK call. The largest dense matrix built anywhere is `2048 x 2048`; the `3456`-site string and its scans are carried sparse. Declared reductions, with the probe output lines that carry the rest, are listed in "Proof boundary".

## Theorem 1 -- a time-directed sweep registers the direction of motion at order one

**Conclusion.** Under the tick model with the rotated kernel, a plane sweep advancing along `+z` registers the string's core right-mover at the core with odds `0.1366` and its time-reversal partner - the anti-string's core left-mover - with `0.6048`, so `Delta_core = -0.46825` at `tau = 0.5`, with the transfer to the ring `Delta_ring = +0.54803`. The identification of the partner is **exact**: the anti-string carrying `conj(psi_R)` at `+tau` and the string carrying `psi_R` at `-tau` are registered identically site by site at `0.0e+00`, in total variation at `0.0e+00` on the `2x2x4` column with the sea, and at `0.0e+00` in the many-body tree on the `2x2x2` block, where the same sweep separates the pair by `TV = 0.393394`. The bias is the `tau`-odd part of the law: it is `-0.0109, -0.0529, -0.2021, -0.4683, -0.4982, -0.2307` at `tau = 0.05, 0.1, 0.25, 0.5, 1, 2`, saturating near `-0.5` and quasi-periodic beyond. It **grows with the string length** (`-0.4683, -0.5031, -0.5264` at `L_z = 24, 48, 96`) and is stable in the transverse size (`-0.4352, -0.4683, -0.4507` at `N_s = 8, 12, 16`) and in the momentum (`-0.5444, -0.5270, -0.4683` at `p = pi/24, pi/12, pi/6`). The pitch of a screw changes only the magnitude of the directed part (`-0.43744, -0.39396, -0.32929, -0.25016` at pitch 4, 8, 12, 24).

**Reading.** The core right-mover runs away from the advancing front, reaches the seam of the recorded region, cannot reflect - the core branch is chiral - and transfers to the ring's left-moving branch, so it is registered mostly on the ring; the partner runs into the front and is registered at the core. The quantity is `d.J`: the sweep direction against the mover's current.

## Theorem 2 -- the screw sense of the sweep registers exactly nothing on the string

**Conclusion.** At fixed pitch and direction the mirror difference `Delta(screw+) - Delta(screw-)` is `<= 1.7e-16` in the core, the bulk and the ring at pitch 4, 8, 12 and 24, and the registered densities are pointwise mirror images, `max |mu(screw+) - sigma_x mu(screw-)| <= 3.6e-17`; at the pattern level `TV(law(screw+), sigma_x-relabelled law(screw-)) = 1.9e-15`. The reason is an exact identity, not a small number: of the 16 elements of the point group about the core, `sigma_x` sends the string to a gauge copy of itself at `1.1e-16`, the `sigma_x` image of the `+` screw is the `-` screw as a set identity, and the core doublet maps onto itself under `sigma_x` with the `2x2` matrix unitary to `5.3e-15` and eigenvalues `(-1, -1)`. Any `sigma_x`-covariant registered quantity is therefore identical for the two screws. With the core placed off the mirror plane, so that the finite plane breaks `sigma_x`, the screw difference becomes nonzero but falls with the plane size like the mode's ring weight: `-4.0e-03, -7.8e-04, +2.1e-04` at `N_s = 8, 12, 16` with ring weights `0.551, 0.181, 0.057`, while the directed bias on the same geometries stays at `-0.459, -0.478, -0.456`.

**Reading.** The screw sense is a boundary effect; the directed bias is a bulk one. The string's handedness is time-odd and mirror-even, and a mirror-odd sweep cannot see it.

## Theorem 3 -- the two exact anti-unitary identities

**Conclusion.** `C2(x)` composed with complex conjugation is an **exact anti-unitary symmetry of the string**: `C2(x) h = D h_anti D+` at `0.0e+00` for a diagonal gauge, and conjugation returns `h_anti` to `h`. It gives `mu_R(S, +tau) = C2(x) mu_R(C2(x) S, -tau)` pointwise to `6.9e-17` and hence `Delta(S) = -Delta(C2(x) S)` to `2.8e-16` for the plane sweep and every screw, so **every `C2(x)`-closed family of sweeps averages to exactly zero**. For the plane, `C2(x)(plane+)` is `plane-` exactly and the reversal-closed average is `+0.00000`; for a finite screw the two differ by the seam of the quadrant construction, and the reversal-closed screw averages keep `+0.002, +0.003, +0.006, +0.006` at pitch 4, 8, 12, 24. Separately, the rotated kernel is even under `sigma_z` times particle-hole times `tau` reversal: `mu_R(S, +tau) = sigma_z mu_hole(sigma_z S, -tau)` pointwise to `6.6e-17` (plane) and `5.7e-17` (screw), and at the pattern level with the sea to `TV = 9.4e-15`. On the `2x2x4` column the mover's time-odd registration is `TV(R+, R-) = 0.01892` against the sea's own time-odd texture `0.00645`, and the screw's parity-odd record correlators flip sign exactly between the senses (`chi_2 = +0.02367` against `-0.02367`, `chi_3 = +0.05728` against `-0.05728`) with mirror asymmetry `A_x = 0.04437` for the screw and `0.00000` for the plane.

**Reading.** The mirror partner of the right-moving core particle is the right-moving core hole with the arrow of record time reversed. There is no identity relating the string's right-mover law to any left-mover's law under the *same* sweep at the *same* `tau`, which is exactly why the directed bias is nonzero.

## Theorem 4 -- the record-time vortex is the opposite case

**Conclusion.** The tick model is certified many-body: on the open `2x2x2` block with `M2` on, the Lueders tree walked over all `2^V` leaves for the raster, screw+, screw- and slice-wise orders at `tau = 0.5` and `2.0` reproduces the one-particle rotated-kernel law to `3.2e-16` and the invisible-formation formula to `4.5e-17`, with `K^2 - K <= 1.0e-15` and `tr K = N` exactly, and the same on the `2x2x3` block to `8.1e-17`. On PR #7935's record-time vortex the anti-vortex is `C conj(H) C+` for the site-independent internal unitary `C = s_2 x alpha_2 alpha_3 alpha_4` at residual `0.0e+00`, and `C` is **monomial** in the component basis, so PR #7989's time-reversal lemma applies there unchanged - the open item that note left. The registration is then **exactly time-even** for both light modes, the plane sweep and the outward spirals of pitch 2, 4 and 8 in both senses, at `tau = 0.1, 0.5, 2.0`: `O(+tau) = O(-tau)` to `2.2e-15`. The mechanism is certified at `N = 12` at two momenta: the helicity is site-diagonal and commutes with `H` and with every restricted `H_R` (`5.6e-17`), in a helicity sector the even product `alpha_1 alpha_4` - which flips exactly the two generators with imaginary coefficients - satisfies `U conj(h_lam) U+ = h_lam` at `0.0e+00` full and restricted for both helicities, and each light mode has `|<phi|U conj phi>| = 1.0000`. What the spiral sense **does** register there is a parity-odd, time-even difference of a few percent - core odds `0.9196` against `0.9469` at pitch 2, `0.9473` against `0.9605` at pitch 4, `0.8979` against `0.9459` at pitch 8, with the edge mode untouched at `0.9909` - because the record-time mirror of the Wilson vortex is the vortex with `m1 -> -m1` up to `Gamma_2 Gamma_4` at `4.7e-16`, and neither the vortex nor the declared anti-vortex.

**Reading.** Two faces of one coin with opposite discrete labels. The string's handedness is time-odd and mirror-even: a directed sweep separates its movers at order one, a screw does nothing. The record-time vortex's handedness is mirror-odd and time-even: a spiral registers it at the percent level, a directed sweep does nothing.

## Theorem 5 -- no nearest-neighbour rule selects the sweep

**Conclusion.** The 729 ternary nearest-neighbour profiles fall into 57 proper and 56 full orbits, so exactly one chiral orbit pair `(A, B)` exists, and Burnside counting gives `7140` chiral pairs on the 12-offset window, `7960311` on the 18-offset window and `52932198249` on the 26-offset shell - room that no rule here occupies, the Lattice axiom's adjacency clause being nearest-neighbour. Complete dynamic-programming counts over the `3^V` ternary configurations then give, on the **cube** (`2x2x2`, calibration `Xi(screw+) = +1`, `Xi(screw-) = -1`, `Xi(raster) = 0`): no corner has four recorded neighbours, so the all-permissive rule, the maximal chiral rule and the two rules with one chiral menu empty all give `10321920 = 8! x 2^8` complete `(order, value)` paths with 0 dead ends, mean `Xi` exactly `0.000e+00` and final-law mirror asymmetry `0.0e+00` over the 24 improper elements, while every rule empty above two records gives 0 complete paths and `1636608` dead-ended ones. On the **slab** (`2x2x3`, `Xi(screw+/-) = +6/-6`): the readable class admits every order, `1961990553600 = 12! x 2^12` complete paths with 0 dead ends; the maximal chiral rule and the rule forbidding `B` give `1771922718720` (a fraction `0.903`) with `39063306240` dead ends; the rule that forces the chiral shape gives `1405870080` with `19345547712` dead ends while its achiral control gives 0, so every complete path of it passes through an `A`-shaped formation; and **the mean `Xi` over complete paths is exactly `0.000e+00` for every one of them**, while the final-law mirror asymmetry is `0.0e+00`, `6.845e-02` and `5.154e-01`. Under the rule that forbids `B`, all `4096` value assignments complete screw+, screw- and the raster alike on the slab (all `256` on the cube); under the rules that force the chiral shape, none completes any of the three. The mechanism: the global value flip fixes both `A` and `B` (2 of 2 chiral orbits at nearest neighbour), so it does not relate a rule to its mirror; but on the slab every chiral-capable corner shares the full axis `z`, the 16 neighbour-value combinations at a middle corner split as `A: 2, B: 2, achiral: 12`, and reversing the `z`-pair - a flip of the two end slices - exchanges `A` and `B` at every middle corner at once with the **order unchanged**, so the admissible order multiset is mirror-symmetric. On the 12-offset window that argument fails (23355 orbits, 14280 chiral, 128 fixed by the value flip and 14144 sent elsewhere), but no such rule is constructed here.

**Reading.** A chiral rule prunes orders, and can even force every complete path through the chiral shape, yet it writes its handedness into the **values** and never into the **order**. The sweep is a supplied directed order.

## Corollary -- what a directed sweep buys, and what it does not

A directed formation sweep separates a mover from its time-reversal partner at order one. The quantity it registers is `d.J`, the sweep direction against the mover's current: parity-odd under the reflection along the sweep, **time-odd**, and blind to the pseudoscalar sense. It is the record-side image of a current, not of a chirality. Three exact identities fix its character. The time-reversal identity (`0.0e+00`) says what the two registered objects are. The `sigma_x` identity (`3.6e-17`) says the screw sense cannot enter, because the string is its own mirror image. The `C2(x)`-with-conjugation identity (`2.8e-16`) says that the whole bias reverses under a proper rotation composed with time reversal, so **it vanishes exactly over any `C2(x)`-closed family of orders**.

That last point is where the weak sector's requirement bites. A chiral coupling has to be parity-odd and **time-even**, and it has to survive an average over the formation orders a covariant process would actually produce. The bias found here is time-odd and averages to exactly zero over a closed family; the one parity-odd, time-even registration found anywhere in this note - the spiral on the record-time vortex, a few percent - is the registration of a chiral *background* by a chiral *sweep*, with both objects supplied, and it distinguishes a vortex from its mirror image rather than one mover from another in the same background. And the sweep itself is not law content: on the cube and the slab no covariant nearest-neighbour rule selects a handed order, the readable class admitting every order and the chiral rules pruning orders in a mirror-symmetric way. Toward Root B, then: a supplied *chiral* order buys nothing handed, and a supplied *directed* order buys an order-one registration of the direction of motion, which is not the parity-odd, time-even chiral coupling the weak sector needs. What does move is the diagnosis - the obstruction on the string is now a named symmetry (`C2(x)` with conjugation) rather than an absence of effect, and the record-time vortex is shown to sit on the opposite side of both discrete labels.

**Reading, not theorem (this register).** Suppose the world's records are laid down in some order, and ask whether that order can make the world left-handed. Give the order a corkscrew shape and sweep it along a string of matter. Nothing happens: the string looks the same in a mirror, the corkscrew's mirror image is the other corkscrew, and the two give answers identical to the last digit a machine can carry. Now forget the corkscrew and just sweep the front steadily one way along the string. A great deal happens - a mode moving with the front is recorded quite differently from a mode moving against it - but what has been detected is which way the thing is going, not which way it is wound. Reverse the arrow of the sweep and the effect reverses; average over sweeps that come in mirror-and-reverse pairs and it cancels to nothing. So the sweep is a good detector of motion and a blind one for handedness, and the handedness the weak sector wants is still not anywhere in view.

**Disagreements with the expectation, stated plainly.** (1) There is no "core left-mover of the same string": the core branch is chiral, so at `-p` it sits at negative energy and still moves `+z`, and the two movers of one string are the core right-mover and the ring left-mover, or the right-moving particle and the right-moving hole. The clean time-reversal pair is string-right against anti-string-left. (2) The separation of that pair is **order one** (`-0.468`, growing to `-0.526` at `L_z = 96`), not the small effect the question anticipated. (3) The screw contributes an **exact zero**, not a small number, and the reason is a mirror-image identity. (4) The reversal-closed average is **not** the right time-even control: a finite screw has a seam, so reversal-closed screw families leave `+0.002` to `+0.006`; the exact anti-unitary operation is `C2(x)` with conjugation, whose closed families vanish to `2.8e-16`. (5) The record-time vortex's registration is **exactly time-even**, opposite to the string, for a structural reason; the reading that its complex mass is time-violating does not survive at the level of the transverse operator's record law. (6) A chiral rule with empty menus does prune orders, and can force every complete path through the chiral shape, yet its admissible order multiset is exactly mirror-symmetric on the slab. (7) Against the probe write-up this note recomputes: the small-`tau` growth of `Delta_core` is **faster than linear**, not linear - `Delta/tau = -0.22, -0.53, -0.81` at `tau = 0.05, 0.1, 0.25` - and this note uses those values; the recomputed screw-sense bound over the declared sub-family is `1.7e-16` rather than `2.8e-16`, and the recomputed vortex time-evenness bound is `2.2e-15` rather than `1.1e-15`, both machine zero.

## The framework reading -- supplied item by item

**Supplied.** The string of PR #7949 with `M2`, the winding phase, the profile `M0 tanh(rho/xi)` and the core position; the sea and the half filling sector (PR #7883); the star tick and the rotated kernel (PR #7986); the set-wise formation unit (PR #7947); the record-time vortex construction of PR #7935 in full; and, from this note, the tick model with its end-recorded hop-deletion rule and `tau`, the sweeps with their quadrant construction and seam, the regions and columns, the rules, the order-pseudoscalar `Xi` and every tolerance. **Derived, given those:** the point-group census and the schedule set identities; the time-reversal identity and every registration number and scan; the `sigma_x` zero and its off-plane boundary behaviour; the `C2(x)`-with-conjugation and `sigma_z`-particle-hole identities; the pattern-level correlators; the many-body certification; the vortex's exact time-evenness with its certificate and the spiral odds; and the rule counts with the slab mechanism. Nothing here is read out of an axiom; the axiom text is quoted only to fix what covariance demands and that the formation order is not axiom content.

## What is not changed

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. The Lattice and Admissibility axioms are quoted, not weakened.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited. The ledger is fully unaudited since 2026-08-07, and no status word here describes any current audit standing.
- Nothing here is read out of the axioms: the tick model, the sweeps, the regions, the rules and the geometries are declared objects, and no coefficient is derived.
- Nothing here is framed as foreclosing anything. `T5` bounds what a *nearest-neighbour* rule can force on two named clusters; it says nothing about wider windows, larger alphabets or constructions outside the declared setting, and `T1`-`T4` are statements about declared objects at declared sizes.

## Interfaces named for other lanes, not taken up here

- **PR #7989** (the chiral-rule census): its open item is answered - the winding reversal of the record-time vortex *is* a complex conjugation in a record basis up to a monomial site-independent relabelling, so its time-reversal lemma applies there unchanged. Its `T1` census is reproduced here at `57/56`.
- **PR #7986** (the rotated kernel): the kernel is shown to be even under `sigma_z` times particle-hole times `tau` reversal, and its `tau`-odd part is exactly the quantity `T1` measures. Offered to that lane.
- **PR #7947** (the set-wise formation unit): used as declared; the sweeps here are set-wise schedules of exactly that kind.
- **PR #7949** (the second mass and its string): the string's core branch is chiral, so its two in-gap movers at `+-p` are not a mirror pair; and the handedness of that string is time-odd and mirror-even. Both belong to that lane.
- **PR #7935** (the record-time vortex): rebuilt here. Its registration is exactly time-even for a structural reason, and the Wilson vortex is a chiral object whose record-time mirror is the vortex with `m1 -> -m1`. Offered to that lane.
- **PR #7982 and PR #7883** (the readable class and the determinantal statistics): the readable class is shown to admit every formation order on the two clusters, and the determinantal law is the one every statement here is computed in.

## Remaining live routes

1. Whether any formation process with covariant order statistics can register a nonzero time-odd bias at all, given that every `C2(x)`-closed family averages to exactly zero. Nothing here computes the uniform-order average.
2. Wider admissibility windows and larger alphabets, where the chiral orbit count is not one; the 12-offset counts are given but no rule there is constructed.
3. The many-body statements beyond the two small blocks: no interaction, no dynamics for the phase, no anomaly matching, no transverse torus, and no string with its anti-string on one plane.

## Executable claim block

```text
setting: PR #7949's 12x12x24 string with M0 = 0.7, xi = 2, open plane, periodic axis, in 12 sectors of dimension 288 (plus 8x8, 16x16, 20x20 planes and L_z = 48, 96); the 2x2x4 core column; open 2x2x2 and 2x2x3 blocks for the many-body tree; PR #7935's record-time vortex at N = 16 (certificate at N = 12); open 2x2x2 cube and 2x2x3 slab for the rule census; SUPPLIED: M2 and the string, the sea and half filling, the star tick and the rotated kernel, the record-time vortex, and this note's tick model, sweeps, regions, columns, rules and tolerances; axiom clauses quoted from MINIMAL_AXIOMS_2026-06-29.md
T1 directed registration [exact / 1e-4]: V = 3456, Hermitian 0.0e+00, anti-string = conj(h) 0.0e+00, sea 1728, residual 4.8e-15; core R doublet E = +0.51019, dE/dp = +0.8809, core 0.619, ring 0.164; ring L dE/dp = -0.8809, ring 0.876; the core E<0 doublet also dE/dp = +0.8809; T-partner identity 0.0e+00 in density, 0.0e+00 in TV, 0.0e+00 many-body with TV(pair) = 0.393394; plane+ at tau = 0.5: core 0.1366 against 0.6048, Delta_core = -0.46825, Delta_ring = +0.54803, plane- exactly the negative; tau scan -0.0109, -0.0529, -0.2021, -0.4683, -0.4982, -0.2307 with Delta/tau = -0.22, -0.53, -0.81; pitch 4/8/12/24 -0.43744, -0.39396, -0.32929, -0.25016; N_s 8/12/16 -0.4352, -0.4683, -0.4507; L_z 24/48/96 -0.4683, -0.5031, -0.5264; p pi/24, pi/12, pi/6 -0.5444, -0.5270, -0.4683
T2 screw sense [exact / 1e-5]: Delta(screw+) - Delta(screw-) <= 1.7e-16 in core, bulk and ring at every pitch and direction; densities pointwise mirror images 3.6e-17; pattern level 1.9e-15; sigma_x h = D h D+ 1.1e-16, sigma_x(screw+) = screw- exactly, doublet matrix unitary 5.3e-15 with eigenvalues (-1, -1); core off the mirror plane: -4.0e-03, -7.8e-04, +2.1e-04 at N_s = 8, 12, 16 with ring weights 0.551, 0.181, 0.057, directed bias -0.459, -0.478, -0.456
T3 exact symmetries [exact / 1e-5]: C2(x) h = D h_anti D+ 0.0e+00; mu_R(S, +tau) = C2(x) mu_R(C2(x)S, -tau) 6.9e-17; Delta(S) + Delta(C2(x)S) 2.8e-16; plane reversal-closed average +0.00000, screw seams +0.002, +0.003, +0.006, +0.006; sigma_z x particle-hole x tau reversal 6.6e-17 and 5.7e-17 pointwise, TV 9.4e-15; column: static TV 0.01523, |Sigma_R| 32020, mass 0.48078, plane+ Delta -0.01548, TV(R+, R-) 0.01892 against sea 0.00645, chi_2 +0.02367/-0.02367, chi_3 +0.05728/-0.05728, A_x 0.04437 against plane 0.00000
T4 vortex [exact / 1e-4]: many-body tree = one-particle kernel 3.2e-16, = invisible-formation formula 4.5e-17, K^2 - K 1.0e-15, tr K = N, 2x2x3 8.1e-17; anti-vortex = C conj(H) C+ 0.0e+00 with C monomial; light modes |E| = 0.309017, CHI +-1, core 0.965, edge 0.991, dE/dp1 = +0.9511 both; registration time-even to 2.2e-15 (core) and 4.4e-16 (edge) over the declared sweeps and tau, T-partner 5.6e-17; helicity commutators 5.6e-17, U conj(h_lam) U+ = h_lam 0.0e+00, overlap 1.0000; spiral+/spiral- core odds 0.9196/0.9469, 0.9473/0.9605, 0.8979/0.9459, edge 0.9909 both; record-time mirror = vortex with m1 -> -m1 up to Gamma_2 Gamma_4 at 4.7e-16
T5 rule census [exact]: 729 profiles -> 57 proper, 56 full orbits, one chiral pair; Burnside 7140 / 7960311 / 52932198249 chiral pairs on the 12-, 18- and 26-offset windows; cube Xi(screw+/-/raster) +1/-1/0, four rules give 10321920 = 8! x 2^8 complete paths, 0 dead, mean Xi 0.000e+00, asymmetry 0.0e+00, three rules give 0 complete and 1636608 dead; slab Xi +-6, R0 1961990553600 = 12! x 2^12 with 0 dead, chiral rules 1771922718720 with 39063306240 dead, forced-shape rules 1405870080 with 19345547712 dead, achiral control 0, mean Xi 0.000e+00 for all, asymmetry 0.0e+00 / 6.845e-02 / 5.154e-01; 4096 and 256 value assignments complete screw+, screw- and raster under the chiral rule, 0 under the forced-shape rules; value flip fixes both chiral orbits, middle-corner split A 2, B 2, achiral 12, z-pair reversal exchanges A and B at every one; 12-offset window 23355 orbits, 14280 chiral, 128 flip-fixed, 14144 sent elsewhere
supplied: the tick model, the sweeps and their seam, the regions and columns, the rules and Xi; PR #7949's string and M2; the sea and half filling; the star tick and the rotated kernel; PR #7935's vortex; all tolerances
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=25 FAIL=0
```

## Proof boundary

**Geometries.** The `12x12x24` string of PR #7949 as PR #7989 rebuilt it, with `8x8`, `16x16` and `20x20` transverse planes and `L_z = 48, 96` for the scans, open plane, periodic axis, `M0 = 0.7`, `xi = 2`, momenta `p` in `{pi/24, pi/12, pi/8, pi/6}`; the declared tick model with `tau` in `{0.05, 0.1, 0.25, 0.5, 1, 2}`; the declared sweeps (plane, screws of pitch 4, 8, 12, 24 with the quadrant construction and its seam, reversals) and regions (core `rho < 3.5`, ring within 2 of the edge); the `2x2x4` core column for the pattern-level laws; the open `2x2x2` and `2x2x3` blocks for the many-body tree; the record-time vortex at `N = 16` with `M = 0.8`, hard ends and `p = (0.1 pi, 0, 0)`, and the certificate at `N = 12` at that momentum and at `(0.1 pi, 0.06 pi, 0.03 pi)`; the open `2x2x2` cube and `2x2x3` slab with seven declared rules for the census. One particle plus the determinantal record law throughout, apart from the two blocks where the tree is walked in full. Nothing is claimed at other sizes, other profiles, other momenta or other boundary conditions.

**Declared reductions this runner makes,** with the probe output lines that carry the rest. (1) The momentum scan recomputes `p = pi/24, pi/12, pi/6`; `p = pi/8` is **quoted** (`h5_string.py -> out_string.txt:93`: plane+ `Delta_core = -0.54469`). (2) The pitch scan recomputes both senses at pitch 4, 8, 12, 24 swept `+z` and pitch 4 swept `-z`; the `-z` sweeps at pitch 8, 12, 24 are quoted (`out_string.txt:20, 22, 26, 28, 30`). (3) The pattern-level laws are recomputed on the `2x2x4` column; the `2x2x2` column is quoted (`out_string.txt:55-67`: `TV(sea+R, sea) = 0.009634`, plane+ `Delta = -0.011679`, exact checks `0.0e+00 / 1.2e-15 / 6.4e-15`). (4) The off-mirror-plane scan recomputes `N_s = 8, 12, 16` and quotes `N_s = 20` (`h5_string_extra.py -> out_string_extra.txt:20`: mirror difference `-1.51e-04`, ring weight `0.019`). (5) The many-body tree is walked in full on the `2x2x2` block and for one order on the `2x2x3` block; the remaining `2x2x3` orders are quoted (`h5_manybody.py -> out_manybody.txt:10, 12-16`: tree against the one-particle law `1.2e-16`, T-pair `0.0e+00`). (6) The vortex recomputes `N = 16` for the plane sweep and the outward spirals of pitch 2, 4, 8 in both senses; the inward spirals, `plane-` and the whole generic-momentum battery are quoted (`out_vortex.txt:21-46`, `out_vortex2.txt:9-14`: every difference `<= 1.11e-15`), as is the complete 128-product scan for anti-unitary symmetries (`out_vortex2.txt:1, 8, 16`). (7) The slab rule census recomputes five rules and quotes the two mirror rules (`h5_rules.py -> out_rules.txt:21, 23`: identical counts, mean `Xi = 0.000e+00`).

**Not claimed.** That any rule here is the framework's rule - none is landed, and the rules are this note's own supplied objects. Any derivation of `M2`, the winding phase, the core position, the formation order, the sweep, `tau`, or the tick model. The uniform average over all `3456!` formation orders, which is out of reach and about which nothing is said. Anything about the infinite lattice. Anything about wider admissibility windows beyond the orbit counts quoted. **Nothing here is read out of the axioms**; the axiom text is quoted only to fix what covariance demands and that the formation order is not axiom content.

## Review record

**Honest-auditor read.** An auditor should come away with four exact identities and one integer census, in that order. First, **the time-reversal identity**: the anti-string with the conjugated mover at `+tau` and the string with the mover at `-tau` are registered identically, `0.0e+00` in density, in total variation and in the many-body tree, which is what makes `Delta` the separation of a genuine time-reversal pair. Second, **the mirror identity**: the string is its own `sigma_x` image and `sigma_x` exchanges the two screws as sets, so the screw sense contributes `<= 1.7e-16` - an exact zero, not a small effect. Third, **`C2(x)` with conjugation**: `Delta(S) = -Delta(C2(x)S)` to `2.8e-16`, so the whole order-one bias averages to exactly zero over any closed family, which is the sharpest limit on what a directed sweep can be worth. Fourth, **the vortex certificate**: a conserved site-diagonal helicity plus the transverse anti-unitary `alpha_1 alpha_4` at `0.0e+00`, which forces exact time-evenness there. Then the census: mean order-pseudoscalar exactly `0.000e+00` for every declared rule on the cube and the slab, with the slab mechanism identified.

The auditor should also come away with five caveats. The registration numbers are **floating-point statements on declared finite geometries** with a declared tick model, and the tick model, the sweeps and the rules are **supplied by this note**, so what is bounded is what the declared construction gives, not what the axioms give. The order-one separation is between a mover and its **time-reversed** partner, not between two mirror-partner movers in one background, and the note's Root B reading turns on that distinction. The exactly-time-even control is the `C2(x)`-closed family and **not** order reversal, because a finite screw has a seam worth `+0.002` to `+0.006`. `T5` is proved on two small clusters and its mechanism uses that every chiral-capable corner of the slab shares one full axis; larger clusters and wider windows are not enumerated. And three numbers here differ from the probe write-up they were recomputed against - the small-`tau` growth is superlinear rather than linear, and two machine-zero bounds move within the noise - with this note using its own values.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the pointers in "Imports and authority" carry no grade and no weight. The ledger is fully unaudited since 2026-08-07, and no status word in this note describes any current audit standing. Hard landing conditions are a fresh runner and cache pair closing at `PASS=25 FAIL=0`, runtime under the declared `AUDIT_TIMEOUT_SEC = 200` seconds, and passing pipeline and strict-lint gates; independent audit remains a separate lane.

## Validation

Run:

```bash
python3 scripts/directed_formation_sweep_direction_of_motion_not_handedness_check_2026_09_05.py
```

Expected terminal summary:

```text
TOTAL: PASS=25 FAIL=0
```
