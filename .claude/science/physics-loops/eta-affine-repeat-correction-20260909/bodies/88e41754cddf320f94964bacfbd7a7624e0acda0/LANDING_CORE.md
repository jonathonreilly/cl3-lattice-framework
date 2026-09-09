# LANDING CORE — the campaign's core landable science

**Distilled 2026-08-31 from `POSITIVE_PATH.md` (R1–R202, ~16,000 lines).** This
document contains only (a) the positive results the campaign can stand behind,
stated with their current numbers only, and (b) the negative/forcing results
that shape the theory's content. Superseded values do not appear here at all —
they are marked at their source in the research log. Every claim below was verified by at least two
independent routes in the full log; result numbers (R#) index into
the campaign's research log (`POSITIVE_PATH.md`, unlanded archive), which maps
each to its scripts and controls. Nothing here
is landed, ledgered, or audited; statuses are author-proposed.

---

## 1. The theory

Four axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`): **Lattice** (`Z³`, NN
adjacency, proper cubic rotations, no site privileged), **Qubit** (site
possibility domain `M₂(C)`, no possibility privileged), **Admissibility** (one
fixed covariant NN rule determining the local probability distribution),
**Record** (records form; a record locks exactly one admissible possibility;
permanent; one per site; only records readable).

One enlargement is repeatedly pointed at but **not derived**:
`Z³+M₂(C) → Z⁴+M₄(C)`. It is a proposal and the owner's call (§7).

## 2. Kinematics — derived from the axioms

- **The master identity** (R16): `det Q(q) = (m² + s·g⁻¹·s)^(2^(d−1))`. All
  kinematics are corollaries: relativistic dispersion (R2), real positive
  energy with `arcsinh` form (R5), two structurally distinct branches (R12/R14),
  and the 3+1D light cone as the symbol of the rule (R15).
- **The site algebra is the Lorentz algebra** (R97/R143): `M₂(C) ≅ Cl(3,0) ≅
  Cl(1,3)⁺`. The site state is a Minkowski 4-vector; **records are null**
  (R98). The Born weight is light-cone geometry (R100).
- **Complete positivity** imposes a speed limit and makes propagation cost
  purity (R99); no finite-dimensional unitary Lorentz representation exists,
  which is exactly why normalisation and boosts conflict (R107).
- The axioms **disclaim dynamics** (R112, confirmed by the axioms text): only
  the ground-state measure and the rule's form are fixed; the rate function is
  the one genuine freedom (R138).

## 3. The rule — form forced, value not

- **Form forced** (R92/R94/R136): covariance + Markov + triangle-freeness of
  `Z^d` + Hammersley–Clifford + Record consistency give
  `P(v_x|ne) ∝ Π_{y~x} φ(v_x·v_y)`, `φ = a + λ(v·v')` — one parameter at
  `M₂(C)`, six at `M₄(C)` (R147).
- **A continuum limit requires `|λ| > λ_c ≈ 0.68`** (R137): the record field
  has two phases (Binder-verified against both 3-component limits); only the
  ordered phase is massless (structure factor `1/k²`).
- **The Born point** `λ = 1`, where `φ = 2 Tr(ρρ')` exactly: the unique member
  vanishing on orthogonal pairs (R148), and the **apex of the positivity
  region** — the region pinches to a point there, linearly (R190).
- **NOT derived — the forcing negatives** (R192/R193/R194):
  - positivity admits `λ ∈ [−1,1]`; the region is a **bicone** with a second
    apex at the anti-Born point `φ ∝ 1 − Tr(ρρ')`;
  - at `M₂(C)` the two endpoints share a partition function (bipartite
    sublattice map, Binder `|ΔU| = 0.0000` at L=10) yet make **opposite**
    predictions for the nearest-neighbour readout correlation (±0.5545) — a
    physically consequential choice the axioms do not make;
  - the site-algebra enlargement breaks the `±λ` degeneracy (anti-Born fails to
    order at `M₄(C)`, ground-manifold entropy — verified from an exact Néel
    start) but the 6-parameter family has ≥5 conical points of which **four
    order** — the continuum-limit criterion selects an open *neighbourhood* of
    the Born direction, not a point.
  - **Open problem, precisely posed:** the Born weight needs an axiom clause
    neither positivity nor the continuum limit encodes. The Record axiom's
    readout sentences are the only clauses the campaign never used, and the two
    branches differ exactly in what adjacent records say (R192).

## 4. Gravity

- **Arena**: the naive lattice effective action is *not* diffeomorphism
  invariant (R19/R20, gate controlled); the **cell-complex construction passes
  the refinement gate** the lattice fails (R23, three routes; d-dimensional
  lift R24). On it: `S_Regge = ½∫R√g` (four routes, one exact — R63), a
  graviton with positive energy (R64/R74), and working Lorentzian Regge
  calculus (R70).
- **Induced Einstein–Hilbert = 1.00000 ± 0.00003** on the framework's own Kuhn
  simplicial operator, two harnesses, conformal and TT channels (R132/R135).
  The coefficient is confirmed **analytically**: `b₁ = (d−1)/(3d)` in symbolic
  `d` (R189) reproduces the independently measured `1/4` at `d=4` and `2/9` at
  `d=3` (verified against an exact continuum operator to ~1e-4; R188/R198).
- **Newton's constant, closed form** (R195/R196):
  `τ₀ = a²/(16π²W₄)`, `W₄ = ∫₀^∞[e^{−2t}I₀(2t)]⁴dt = 0.154933390` (8 digits,
  three routes). The `U(1)` phase is exact redundancy (site-dependent phase
  invariance to 5.7e-14; phase Hessian exactly 0), so `N = 6` and

  ```
  G = 2πτ₀ = 0.2568119 a²      ℓ_P = 0.506766 a      a = 1.9733 ℓ_P
  ```

  The natural unit is **not** the Planck length, and the inequality runs the
  self-consistent way (`ℓ_P < a`). (R196.)
- **Partial records** (R179–R183, R191): the Record axiom's "when present"
  clause admits diluted configurations. The arena appears before the physics
  (thresholds: connectivity `p ≈ 0.32`; diffusive structure 0.5–0.7; order
  `≈ 0.6`). **The induced EH coefficient survives dilution:** at `p = 0.85` it
  is `1.017 ± 0.021` × the complete-lattice value (5 disorder realisations,
  three calibrated `D` estimators agreeing to 1%). At `p = 0.70` no single `D`
  exists (runs ~2.8× across scales) and no coefficient is quoted.
- **The induced vacuum energy is Planck-density** (R201):
  `ρ_vac·ℓ_P⁴ = 9/(4N) = 3/8`, two routes (one cutoff-free; they agree to
  5.5%), and `G·ρ_vac = 3/(16πτ₀)` is **N-independent** — no field content
  changes it. Against observation this is the cosmological-constant problem
  stated exactly: **122 orders of magnitude**, with no dial to turn. (No
  instability claim: the metric is not dynamical in the framework — R138.)

## 5. Electromagnetism

- The rule uses `|⟨ψ_x|ψ_y⟩|²`; the discarded phase is a **local `U(1)`
  already in the axioms** — "possibilities are states" makes the phase
  unphysical per site (R154/R155). Its flux is quantised into integer Chern
  numbers (machine precision).
- The matter is **minimally coupled to its own Berry connection**, exactly
  (9.1e-16; R158) — so the gauge field is the framework's own, not imposed.
- **The same regulator induces Maxwell at the continuum coefficient**:
  `a₂ = −0.0830` vs `−1/12 = −0.08333`, independently re-derived and confirmed
  to 0.4%, honest uncertainty `~1e-3` (R157/R197).
- The induced gauge coupling is **marginal only at `d = 4`** (R157).

## 6. Matter and spectrum — the decisive negatives

- **Complete low-energy spectrum** (R177): six exactly massless scalars +
  gravity + at most one `U(1)`. Nothing else. The fluctuation operator is
  **exactly** `2·(graph Laplacian) ⊗ I₆` (2.3e-07; R195); the masslessness is
  an identity, protected by the Qubit axiom's non-privileging clause via
  Goldstone's theorem (R178).
- **No fermions — three independent legs**: the axioms introduce no
  anticommuting variables (R163); the measure is real and non-negative, so no
  WZ/Hopf phase (R171); and the charge–monopole route (`n = 1` defect,
  `J = qg/4π = 1/2` measured to 4e-4 — R199) closes because **the monopoles
  are confined into neutral pairs** in the Higgsed phase (opposite-sign pair
  excess 5.6×; R200). The route would need the un-Higgsed phase, which has no
  continuum limit (R137/R169) — a structural conflict, not an open end.
- **Gauge group exactly `U(1)`** (R167/R169/R170/R173): the Record axiom's
  "exactly one" makes it abelian; rank `k > 1` never orders because the Born
  weight's coupling is exactly `1/k`; the internal `u(k)` is global, not
  gauged. Non-abelian gauge symmetry is unreachable by any mechanism found.
- **One particle** (R164/R165): a topological monopole, localised to ~2a,
  action ≈ 4.35, abundance `≈ e^{−S}` — and never light (heavier toward
  criticality).
- **One scale** (R202): the correlation length is infinite (`ξ ∝ L`, two
  channels); every dimensionful output is a power of `a`. **A mass hierarchy
  is inexpressible** — every mass-generating mechanism is separately blocked
  (no potential for a vev; no vector to Higgs; no fermions; no asymptotic
  freedom for transmutation).
- **Generations** (R128–R131, R145/R146): the minimal site algebra carrying
  spacetime + Standard-Model content is `M₁₂(C)`, giving exactly 48 Weyl =
  **3 generations** — *compatible, not forced*; the taste algebra cannot carry
  a gauge charge.

> **The framework is a complete, internally consistent theory of gravity and
> electromagnetism with six massless scalars and no matter. It is not our
> universe, and it now says exactly why at each point.** (R172/R177)

## 7. Dimension, and the single addition (the proposal)

- On `Z³` the record field is **not relativistic**: `η = 0`, `z = 1.94`,
  two independent measures (R140). For **odd d the chirality space is exactly
  `{0}`** (R133/R134); `d = 2, 3` are also excluded by direct measurement
  (R174).
- **`Z⁴` forces `M₄(C)`** (R142): the fourth lattice direction forces the
  fourth Clifford direction — relativity and chirality are **one change**, not
  two (R141/R143). The same change removes the dynamics freedom (R144). The
  proposal simulated as stated is relativistic, with a pre-registered failing
  control that fired correctly (R149/R150); ordering breaks no spatial
  isotropy (R151); the Born point sits ~15% above `t_c` for `CP³` on `Z⁴`
  (R175).
- **Four independent pointers at `d = 4`, none a proof**: (i) chirality parity
  excludes odd `d`; (ii) the framework's two curvatures — Regge on hinges,
  Berry on plaquettes — are objects on the same cells only at `d = 4` (R42/
  R154); (iii) the induced gauge coupling is marginal only at `d = 4` (R157);
  (iv) only the enlarged algebra breaks the rule's `±λ` degeneracy (R193).
- **`Z⁴` is not derived. It is the owner's call.**

## 8. Standards of evidence

**Numbers.** Every number above is the campaign's current value; superseded
values are banner-marked at their source in `POSITIVE_PATH.md` and none are
carried here.

**Error bars** (R198): when candidate values are alternative fits of one
dataset, the spread across fits is the uncertainty; when they are a nested
sequence converging in lattice size, the last step is. Quoting the best
member's agreement is defensible only in the second case, with the convergence
demonstrated.

**Method** (R187/R188 lesson, held to for the rest of the campaign): progress
came from constructing objects with known answers — exact Bloch operators,
closed forms, calibrated controls — never from re-interrogating a failing
measurement. Every positive claim has two independent routes.

## 9. Open problems, in order

1. **The Born-weight selector** — needs a clause beyond positivity + continuum
   limit; the Record readout sentences are the only unused candidates (R192/R194).
2. **`Z⁴ + M₄(C)`** — not derived; four pointers; owner's call.
3. **The dynamics gap** — the rate function is genuinely free (R138); the
   axioms disclaim dynamics (R112).
4. **The cosmological constant** — Planck-density, N-independent, no
   counterterm available in pure induced gravity (R201).

---

*Provenance: the full research log (`POSITIVE_PATH.md`, ~16,000 lines,
R1–R202, ~370 scripts alongside) is retained as an **unlanded archive** with
the campaign worktree — every number above cites its result ID there, and
anything superseded is banner-marked in that log at its source, so it contains
no unmarked stale claims. Only this file is landed.*
