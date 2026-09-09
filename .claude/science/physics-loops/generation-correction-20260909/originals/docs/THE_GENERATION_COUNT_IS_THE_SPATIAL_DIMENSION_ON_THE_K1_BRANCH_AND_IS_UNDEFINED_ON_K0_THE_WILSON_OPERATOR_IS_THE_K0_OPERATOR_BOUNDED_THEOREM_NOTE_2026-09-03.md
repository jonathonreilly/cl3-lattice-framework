---
claim_id: generation_count_is_spatial_dimension_on_k1_undefined_on_k0_2026_09_03
claim_type: bounded_theorem
claim_scope: "On the one-particle nearest-neighbour surface of the periodic L^d torus with even L, for d = 2, 3, 4 and L in {4, 6, 8}: the Wilson operator M_W = sum_mu (1 - (T_mu + T_mu^+)/2) equals d*I - H_K0/2 exactly, so it is the K0 kinetic operator up to an affine map and the admitted staggered-Dirac/Wilson surface is H_K1 + lambda*(d*I - H_K0/2). On the K1 branch in the t = i*eta frame the 2^d Brillouin-corner plane waves are exact eigenvectors of H_K1 + lambda*M_W with eigenvalue 2*lambda*hw for every lambda, with degeneracies C(d,k); the hw=1 level has dimension d, plain-translation characters -1 in exactly one slot, and observable algebra M_d(C) with commutant dimension 1, and the corner levels are separated from the bulk for lambda below about 1. On the K0 branch in d = 3 no Brillouin corner is a zero mode; the kernel is {p : sum_mu cos p_mu = 0} with 20, 24, 68 momenta at L = 4, 6, 8, on which M_W is identically 3; the level containing the hw=1 corners has dimension 15, 27, 39 and observable algebra M_3(C)^(+5), M_3(C)^(+9), M_3(C)^(+13) with commutant dimension 5, 9, 13, so no corner multiplet is separated and no generation count is defined there. The combined hopping t = i*eta - lambda/2 has non-uniform plaquette flux and lies outside the two covariant classes; lambda is an admitted parameter. Species semantics, generation labelling, mass hierarchy, gauged-translation characters, antiperiodic finite-L Wilson splitting, and the 3+1D taste census are outside this claim."
upstream_dependencies: []
runner: scripts/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.py
runner_cache: logs/runner-cache/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.txt
---

# The generation count is the spatial dimension on the K1 branch and is undefined on K0; the Wilson operator is the K0 operator

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** independent audit required
**Status:** proposed_retained
**Status authority:** effective status is pipeline-derived after independent audit ratification. This note asserts no grade for
itself or for any note it cites; the ledger has carried no audited grade since 2026-08-07.
**Primary runner:**
[`scripts/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.py`](../scripts/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.txt`](../logs/runner-cache/generation_count_is_spatial_dimension_on_k1_undefined_on_k0_check_2026_09_03.txt)
**Parents:** none as proof dependencies. The notes quoted in section 1 supply the setting and are cited as context; every
operator used below is declared in section 2 and rebuilt from scratch by the runner.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact one-particle operator identities, exact eigenvectors and multiplicities, exact kernel counts, and exact finite-dimensional algebra dimensions on the declared finite tori."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Submit the finite operator theorem to the independent audit lane; route the species, labelling, mass, and 3+1D-census questions to their owning science lanes."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## 1. Setting

The kinetic-class note `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md` declares the licensed kinetic
surface (its §5.1, definition D-kin) as

```text
S = { H_t = Σ_{x,μ} ( t_μ(x) a†_{x+μ̂} a_x + conj ) :  t_μ(x) ∈ C },   (1)
```

with frame redundancy the site-local `U(1)` action `t_μ(x) → conj(u(x+μ̂)) t_μ(x) u(x)` times scale times lattice automorphisms,
and with the frame-invariant plaquette flux `Φ_P = t_μ(x) t_ν(x+μ̂) conj(t_μ(x+ν̂)) conj(t_ν(x))`. On that surface it fixes
exactly two covariant classes (its §2, quoted verbatim):

```text
K0 :  φ = +1   representative t ≡ 1          (scalar tight-binding;
                                              extensive zero surface)
K1 :  φ = −1   representative η⁰             (Kawamoto-Smit class;
      η⁰_1 = 1, η⁰_2 = (−1)^{x₁},             8 isolated Dirac zeros;
      η⁰_3 = (−1)^{x₁+x₂}                     = absorbed naive Dirac)
```

and records the bit between them as unforced (its boundary B-BIT, quoted verbatim): "The selector `φ = −1` (K1 vs K0) is NOT
forced by the specified constraint set; `K0` is the explicit countermodel."

The three-generation notes work on a different, admitted object. `THREE_GENERATION_STRUCTURE_NOTE.md` declares: "the
staggered-Dirac/Wilson realization on `Z^3` is treated as the admitted surface for this bounded row. This note does not derive
that surface," and reads off it that "the Wilson mass term `m(p) = sum_mu (1 - cos p_mu)` depends only on the Hamming weight
`hw(p)`" and that "the `hw=1` orbit is therefore the unique lightest nonzero Wilson-mass triplet on this admitted surface."
`STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md` gives that triplet the translation characters
`T_x: diag(−1,+1,+1)`, `T_y: diag(+1,−1,+1)`, `T_z: diag(+1,+1,−1)`, and
`THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md` states that those projectors "together with
the induced `C₃[111]` cycle map generate the full operator algebra `M_3(ℂ)` on `H_{hw=1} ≅ ℂ³`."

Theorem 1 identifies the admitted surface: it is `K1 + λ·K0`. Both classes appear in it, and the unforced bit is which of them
is the leading (first-order) term. Everything after that is what each branch does with the corner sector.

## 2. Objects

One particle on the periodic `L^d` torus, `L` even, `N = L^d` sites. With `T_μ = Σ_x |x+μ̂⟩⟨x|` (so `T_μ|p⟩ = e^{−i p_μ}|p⟩`)
and the Kawamoto-Smit signs `η_μ(x) = (−1)^{x_1+…+x_{μ−1}}`:

```text
H_K0  = Σ_μ (T_μ + T_μ^+)                 K0, t ≡ 1,     flux +1
H_K1r = Σ_μ η_μ (T_μ + T_μ^+)             K1, t = η,     flux −1   (real frame)
H_K1  = i Σ_μ η_μ (T_μ − T_μ^+)           K1, t = i η,   flux −1   (staggered frame)
M_W   = Σ_μ (1 − (T_μ + T_μ^+)/2)         Wilson operator, M_W(p) = Σ_μ (1 − cos p_μ)
```

Corners are the momenta `p ∈ {0,π}^d`, i.e. grid labels `n ∈ {0, L/2}^d`; `hw(n)` is the number of slots equal to `L/2`. All
statements below use `H_K1` (the `t = iη` frame), in which the corners lie on the periodic grid for every even `L`; Theorem 5
records why the real frame is not interchangeable with it at `L ≡ 2 (mod 4)`. `λ ≥ 0` is a free coefficient, not a derived one.

## 3. Theorem 1 — the Wilson operator is the K0 operator

**Conclusion.** On the surface (1), exactly `M_W = d·I − H_K0/2`.

**Proof.** `M_W = Σ_μ (1 − (T_μ + T_μ^+)/2) = d·I − (1/2) Σ_μ (T_μ + T_μ^+)`, and the second sum is `H_K0` by definition. ∎

The runner forms both sides as dense matrices for `d = 2, 3, 4` at every `L` used and reports maximum entry difference `0.0`.
Consequently `[H_K0, M_W] = 0` exactly (norm `0.0`), while `‖[H_K1, M_W]‖ = 27.71` at `d = 3, L = 4`. So the Wilson term is not
a new object added to the kinetic term: on the licensed nearest-neighbour surface it is the K0 representative, shifted and
scaled. The admitted "staggered-Dirac/Wilson" operator is `H_K1 + λ(d·I − H_K0/2)`.

## 4. Theorem 2 — the K1 branch: exact corner levels, count `d`, algebra `M_d(C)`

Periodic boundaries, even `L`, `d = 3` unless stated.

**(a) Kernel.** `H_K1` has exactly `2^d` zero modes — `8, 8, 8` at `L = 4, 6, 8` — and the kernel is the span of the `2^d`
corner plane waves (maximum residual `8.0e-15`).

**(b) Exact corner eigenvectors.** For every corner `c` and every `λ`,

```text
H_K1 |c⟩ = 0,     M_W |c⟩ = 2·hw(c) |c⟩,     (H_K1 + λ M_W)|c⟩ = 2 λ hw(c) |c⟩.
```

Maximum residual `6.0e-15` for the two kinetic identities at `d = 3`, and `1.3e-14` for the combined eigenvalue over
`λ ∈ {0.1, 0.25, 0.5, 1, 2}` and `d = 2, 3, 4`. The eigenvalue is exact in `λ`; no expansion in `λ` is used anywhere.

**(c) Degeneracies.** At `d = 3, λ = 0.1` the levels `0, 0.2, 0.4, 0.6` carry multiplicities `(1, 3, 3, 1) = C(3,k)` at
`L = 4, 6, 8`. The lightest nonzero level is threefold: three in three dimensions, two in two, four in four (Theorem 6).

**(d) Isolation window.** At `λ = 0.1` the nearest bulk eigenvalue to any corner level sits at distance `1.500 / 1.182 / 0.844`
for `L = 4 / 6 / 8`. The pattern `(1, 3, 3, 1)` is exact at `λ = 0.1, 0.25, 0.5` for all three `L`. At `λ = 1` the two
*singlets* meet bulk states at `L = 4` and `L = 8`, giving `(5, 3, 3, 5)`, while `L = 6` stays `(1, 3, 3, 1)`; at `λ = 2` the
*triplets* meet bulk states at `L = 4` and `L = 8`, giving `(2, 10, 10, 2)` and `(2, 18, 18, 2)`, with `L = 6` again clean. The
honest statement is therefore: the whole corner set is separated from the bulk for `λ` below about `1`, and the `hw = 1`
triplet is exactly threefold through `λ = 1` at every `L` tested. It is not separated for all `λ`. The finite-volume scale
behind this is the smallest nonzero `|E|` of `H_K1`, equal to `2 sin(2π/L)` = `2.0000 / 1.7321 / 1.4142` at `L = 4 / 6 / 8`.

**(e) Observables on the `hw = 1` level.** At `d = 3, λ = 0.1` the eigenspace at `E = 0.2` has dimension `3` at `L = 4, 6, 8`;
the three plain translations restricted to it are Hermitian and commute (residual `9.3e-15`); their joint characters are
`(−1,1,1), (1,−1,1), (1,1,−1)` — `−1` in exactly one slot. The axis 3-cycle `R` restricted to the level is unitary with
`R^3 = I` and trace `0`, a fixed-point-free cycle acting with one orbit on the three characters. The algebra generated by the
three character projectors and `R` has dimension `9 = dim M_3(C)`, is closed, and has commutant dimension `1`: it is
irreducible, so no proper invariant subspace and no proper quotient survives the characters and the cycle together.

## 5. Theorem 3 — the K0 branch: no corner zero mode, no separated multiplet

Same boundaries, `d = 3`, `L = 4, 6, 8`.

**(a) The kernel is a surface, and no corner is in it.** `H_K0` has `20 / 24 / 68` zero modes, matching
`#{p : Σ_μ cos p_μ = 0}` exactly. The number of Brillouin corners in that set is `0` at each `L`. Under the 24 proper rotations
the zero set breaks into orbits of sizes `[8, 12]`, `[12, 12]`, `[8, 12, 24, 24]` — never into a triple.

**(b) The Wilson term lifts nothing there.** By Theorem 1, on `ker H_K0` the operator `M_W` is identically `3` (residual
`4.0e-14`), and globally `H_K0 + λ M_W = 3λ + (1 − λ/2) H_K0` with maximum entry difference `0.0`. Adding the Wilson term to K0
rescales and shifts one operator; it introduces no new eigenvector and no new level structure. At the band extrema `E = +6`
(`p = 0`) and `E = −6` (`p = (π,π,π)`) the multiplicity is `1` at each `L`: one species at each extremum, and no multiplet.

**(c) The `hw = 1` corners are not a level.** At `λ = 0.1` the eigenspace containing them (`Σ_μ cos p_μ = 1`, `E = 2.2`) has
dimension `15 / 27 / 39` at `L = 4 / 6 / 8` (plane-wave residual `1.9e-14`). `R` acts on it with `5 / 9 / 13` orbits, all of
size `3`, one of which is the corner triple. The algebra generated by the momentum projectors and `R` has dimension
`45 / 81 / 117` against a full `M_n` dimension of `225 / 729 / 1521`, with commutant dimension `5 / 9 / 13`: it is
`M_3(C)^{⊕5}, M_3(C)^{⊕9}, M_3(C)^{⊕13}`, reducible. The corner triple is one summand among `5 / 9 / 13` mutually isomorphic
ones, and nothing spectral or algebraic separates it. The Hamming counting `1+3+3+1` still holds as combinatorics of
`{0,1}^3`, but on K0 it is combinatorics of a label set, not the multiplicity structure of an operator.

## 6. Theorem 4 — the combined hopping is outside the two-class family

Read `H_K1 + λ M_W` as a single nearest-neighbour hopping system, `t = iη − λ/2`. At `d = 3, L = 4` the plaquette flux of
`t ≡ 1` is the single value `+1`, of `t = η` and of `t = iη` the single value `−1`, and of `t = iη − λ/2` at `λ = 0.1` the two
values `−0.995012 ∓ 0.099751 i`. Non-uniform, and complex, so the combined operator is not one of the two covariant classes and
is not covariant up to a single site-local frame. It is a K1 term plus a K0 term with a free relative coefficient. `λ` is an
admitted parameter of the surface, not a quantity this note or the notes it cites produce.

## 7. Theorem 5 — boundary witnesses

**(a) Antiperiodic wrap.** With antiperiodic boundaries `H_K1` has `0` zero modes at `L = 4, 6, 8`; the smallest `|E|` is
`2√3 sin(π/L) = 2.4495 / 1.7321 / 1.3257`, attained on `64 = 4^3` near-corner momenta. `H_K0` has `0 / 56 / 0` zero modes. The
exact corner structure of Theorem 2 is a periodic-torus statement; under antiperiodic wrap it holds only as `L → ∞`.

**(b) Frame.** The real-frame representative `t = η` has `8 / 0 / 8` zero modes at `L = 4 / 6 / 8` — none at `L = 6`. The
site-local `U(1)` map `U = diag(i^{|x|})` carries `H_K1r` to `−H_K1` at `L = 4` and `L = 8` and not at `L = 6`, because it is
single-valued on the torus only for `L ≡ 0 (mod 4)`. Corner statements need the `t = iη` frame, or `L ≡ 0 (mod 4)`.

## 8. Theorem 6 — the count is the dimension

Same construction in `d = 2` (`L = 4, 6, 8`) and `d = 4` (`L = 4, 6`).

| `d` | K1 zero modes | corner multiplicities at `λ=0.1` | lightest nonzero count | `hw=1` algebra | K0 zero modes | corners in K0 kernel | K0 level holding the `hw=1` corners |
|---|---|---|---|---|---|---|---|
| 2 | `4 = 2^2` | `1+2+1` | **2** | `M_2(C)`, dim 4, commutant 1 | `6 / 10 / 14` | 2 | dim `6 / 10 / 14`, algebra `20 / 36 / 52` |
| 3 | `8 = 2^3` | `1+3+3+1` | **3** | `M_3(C)`, dim 9, commutant 1 | `20 / 24 / 68` | 0 | dim `15 / 27 / 39`, algebra `45 / 81 / 117` |
| 4 | `16 = 2^4` | `1+4+6+4+1` | **4** | `M_4(C)`, dim 16, commutant 1 | `70 / 198` | 6 | dim `28 / 68`, algebra `208 / 528` |

In every `d` the `hw = 1` characters carry `−1` in exactly one slot, the axis `d`-cycle is transitive on them, and the
generated algebra is the full `M_d(C)` with commutant dimension `1`. In every `d` the K0 level holding those same corners has
algebra dimension strictly below `n^2` and is reducible. Where the corners do lie on the K0 kernel (`d = 2` at `hw = 1`,
`d = 4` at `hw = 2`, from `d − 2·hw = 0`), that only places them inside the extensive kernel; it never separates them.

## 9. Corollary — what the number three is here

The count is contingent on the unforced bit, and the two branches are not two values of one quantity.

On K1 the count is exact and equals `d`: the lightest nonzero Wilson-lifted corner multiplet has `C(d,1) = d` members, with
irreducible observable algebra `M_d(C)`. In three dimensions that is three. So "three generations", on this surface, is a
consistency statement between the Lattice axiom's spatial dimension and the doubler count of the first-order kinetic class. It
is not an independent explanation of three: the three is the dimension, read twice.

On K0 there is no count. The zero set is extensive, no corner lies in it (in `d = 3`), the Wilson term is constant on it, and
the corner triple sits inside a `15 / 27 / 39` dimensional level with reducible algebra. Read at the band extremum, K0 has one
species; read at zero energy, an extensive surface. Neither is a generation count.

The bit's content is therefore sharper than "flux `−1`". Because `M_W = d·I − H_K0/2`, both classes are already present in the
admitted operator, and the bit selects which of them is the leading order: K1-leading gives Dirac doublers and the count `d`;
K0-leading gives a scalar band and one species at the extremum.

**Untouched by all of the above.** Labelling the triplet e/μ/τ: the cyclic action on labels is free and the `hw = 1` triplet
carries exactly one orbit (Theorem 2e). That is the situation scoped by
`CHARGED_LEPTON_SELECTED_LINE_GENERATION_SELECTOR_NO_GO_NOTE_2026-04-27.md`, whose scoped claim is that "the support data
determine at most a sorted heavy/middle/light ratio profile on an unbased orbit. They do not identify which physical
charged-lepton generation/source slot carries the tau-scale support." Nothing here supplies a basepoint. The masses: the Wilson
splitting is `2λ·hw`, exactly degenerate within a Hamming weight, so it orders the weights and says nothing inside one. The
bridge to the 3+1D two-taste census is a different census and is not computed here.

## 10. Reading, not theorem

In plain words: the framework's "three generations" comes out of a lattice with three directions, through a construction whose
corner set is `{0,π}^3` and whose lightest nonzero corner multiplet has one member per direction. If the lattice had four
directions the same construction would give four. That is worth saying out loud, because it means the number three here is
carried by the Lattice axiom's dimension rather than added to it. It also means the interesting question is not "why three" but
"why the first-order class", since the second-order class — which the same construction already contains as its Wilson term —
gives a single band with nothing to count. None of that is proved by the theorems above; the theorems prove the arithmetic, and
this paragraph is a reading of it.

## 11. Interfaces

- `THREE_GENERATION_STRUCTURE_NOTE.md` could add: on the admitted surface the corner Hamming structure is the multiplicity
  structure of an actual lattice operator only on the K1 branch, where `H_K1 + λ M_W` has the corner plane waves as exact
  eigenvectors with eigenvalue `2λ·hw` for every `λ`, and the triplet count there is `C(d,1) = d`.
- `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md` could add to B-BIT: the Wilson operator of the
  admitted three-generation surface is the K0 representative, `M_W = d·I − H_K0/2`, so the bit chooses the leading order
  between two operators that both already appear there; and a spectral principle demanding a point-like zero set would be
  exactly a principle demanding a finite species count, since K0 supplies none.
- `STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md` could add: its Step-3 characters and `M_3(C)` are realised on
  the eigenspace of a lattice operator, not only on the abstract corner label set, and on the K0 branch the same label set
  gives `M_3(C)^{⊕5/9/13}` instead.

## Executable claim block

```text
surface: one-particle nearest-neighbour operators on the periodic L^d torus, L even
sizes: d=3 at L=4,6,8; d=2 at L=4,6,8; d=4 at L=4,6
T1_identity: M_W = d*I - H_K0/2; max entry difference 0.0 for d=2,3,4 at every L
T1_commutators: ||[H_K0,M_W]|| = 0.0 exactly; ||[H_K1,M_W]|| = 27.71 at d=3,L=4
T2_kernel: H_K1 zero modes = 2^d (8,8,8 at d=3); kernel = span of the corner plane waves
T2_corner_eigenvalue: (H_K1 + lam*M_W)|c> = 2*lam*hw(c)|c> exactly, every lam
T2_degeneracies: C(d,k); (1,3,3,1) at d=3 for lam = 0.1, 0.25, 0.5 at L=4,6,8
T2_isolation_window: bulk clearance 1.500/1.182/0.844 at lam=0.1, L=4/6/8;
  lam=1 gives (5,3,3,5),(1,3,3,1),(5,3,3,5); lam=2 gives (2,10,10,2),(1,3,3,1),(2,18,18,2)
T2_bulk_floor: smallest nonzero |E| of H_K1 = 2 sin(2 pi/L) = 2.0000/1.7321/1.4142
T2_characters: (-1,1,1), (1,-1,1), (1,1,-1); R unitary, R^3 = I, trace 0, one orbit
T2_algebra: dim 9 = dim M_3(C), closed, commutant dim 1
T3_k0_kernel: 20/24/68 = #{p : sum cos p = 0}; corners in it 0; orbit sizes [8,12],[12,12],[8,12,24,24]
T3_wilson_constant: M_W = 3 on ker H_K0; H_K0 + lam*M_W = 3*lam + (1 - lam/2)*H_K0 exactly
T3_band_extrema: multiplicity 1 at E = +6 and E = -6 at every L
T3_hw1_level: dim 15/27/39; R-orbits 5/9/13 of size 3; algebra dim 45/81/117; commutant 5/9/13
T4_flux: K0 {+1}; K1 t=eta {-1}; K1 t=i*eta {-1}; t = i*eta - lam/2 gives -0.995012 -/+ 0.099751i
T5_apbc: H_K1 zero modes 0 at L=4,6,8; min |E| = 2 sqrt(3) sin(pi/L) on 64 momenta; H_K0 0/56/0
T5_frame: t=eta zero modes 8/0/8; U = diag(i^|x|) conjugates to -H_K1 only at L = 0 mod 4
T6_counts: lightest nonzero K1 corner multiplet = C(d,1) = d; {d=2: 2, d=3: 3, d=4: 4}
T6_k0_reducible: K0 level algebra dim < n^2 in d = 2, 3, 4
runner_result_required: zero failed checks
```

## Proof boundary

Every theorem is stated for periodic boundaries, even `L`, `L ∈ {4, 6, 8}` and `d ∈ {2, 3, 4}`, on the one-particle
nearest-neighbour surface; no many-body space is formed anywhere. The translations used are the plain ones. On the
one-component K1 surface the gauged translations that commute with `H_K1` are a different set, they mix Hamming weights, and
their characters on the corner sector are not computed here; the corner statements are unaffected because the corner plane
waves are exact eigenvectors of `H_K1 + λ M_W` regardless of which translations one uses to label them. Separation of the
corner levels from the bulk is claimed only for `λ` below about `1`; the finite-`λ` crossings at `λ = 1` (singlets, `L = 4, 8`)
and `λ = 2` (triplets, `L = 4, 8`) are bulk states arriving at fixed corner eigenvalues, not corner eigenvalues, and they are
named rather than smoothed. The `L = 6` column stays clean at both, which is itself a finite-volume accident and not evidence
of a wider window. Not computed: the antiperiodic finite-`L` Wilson splitting beyond the zero-mode statement of Theorem 5,
gauged-translation characters on the corner sector, and the bridge to the 3+1D two-taste census. Species semantics, generation
labelling, mass hierarchy, and any continuum limit are outside this note.

## Honest-auditor read

- The result that could most easily be self-confirming is Theorem 2b, since a corner plane wave is an eigenvector of `M_W` by
  inspection. It is not left there: the runner diagonalises the full dense `H_K1 + λ M_W` and reads multiplicities off the
  spectrum, then separately checks the residual of the predicted eigenvector. The two routes could disagree and do not.
- The K0 result is the load-bearing negative one, so its numbers are produced twice by unrelated means: `20 / 24 / 68` comes
  from counting eigenvalues of a dense matrix at zero and, independently, from counting grid momenta with `Σ cos p = 0`. The
  gate requires the two to agree. The same double count gates `15 / 27 / 39`.
- "Reducible" is computed, not asserted. The algebra dimension comes from the rank of the span of the words, and the commutant
  dimension is computed by solving the commutation equation — `5 / 9 / 13`, matching the orbit count. A single number would not
  have distinguished a reducible algebra from an artefact of the basis; two do.
- The separation claim is the softest thing here and is stated at its true strength. The corner eigenvalues are exact for every
  `λ`; their distance from the bulk is not, and the note gives the `λ` values where it fails and at which `L`. A reader should
  not carry "separated from the bulk" past `λ ≈ 1`.
- The `d = 2` and `d = 4` rows are not decoration. They are what makes the corollary a statement about the dimension rather
  than about the number three: the same code path with `d` changed returns `2` and `4`, and the K0 comparison stays reducible
  in both. If the count were an accident of three dimensions those rows would show it.
- What a reader should weigh against the note: `L ∈ {4, 6, 8}` is three sizes, the algebra statements are checked at those
  sizes and by an argument that is dimension-blind but not size-blind, and the whole thing lives on the one-particle surface.
  Nothing here shows that a many-body or gauged version keeps the same corner sector.

## Review record

The scope of this note ends at the finite operator statements above and at the corollary that reads them. Withdrawn rather than
refuted during drafting: any title or claim asserting the count is defined on both kinetic branches, which Theorem 3
contradicts; any statement that the corner levels are separated from the bulk for all `λ`; and any species, labelling, or mass
reading of the `hw = 1` multiplet. Hard landing conditions are a fresh runner/cache pair with zero failed checks and bounded
invocation stdout, a current citation-graph manifest entry for this node, and clean pipeline, strict-lint, and changed-evidence
gates. Independent audit is a separate lane and owns every audit status or verdict.
