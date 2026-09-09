---
claim_id: regge_4d_cubic_coxeter_native_linearised_graviton_dispersion
claim_type: bounded_theorem
claim_scope: "On the 4D cubic-Coxeter (Kuhn/Freudenthal) path complex T(Z^3 x Z_tau) with flat Euclidean/OS0 background and supplied 0/1-vector edge lengths (l^2 in {1,2,3,4}), the second variation of the Regge action S_R = sum_t A_t delta_t about flat has, at every declared momentum: dim ker Q(k) = 5, namely 4 discrete diffeomorphisms coinciding exactly with the continuum family h_munu = i(k_mu xi_nu + k_nu xi_mu) plus 1 identically flat non-metric branch, with metric-sector kernel exactly 4; exactly 2 propagating modes, doubly degenerate, with no further branch in omega in (0,8] out to the zone boundary; the exact on-shell locus 4 sinh^2(omega/2) = sum_i 4 sin^2(k_i/2) under the holomorphic continuation k_tau = i omega, to worst relative residual 3.2e-13 over 32 declared zone points in five directions; the small-momentum expansion omega^2 = k^2 - (k^4/12)(1 + sum_i n_i^4) + O(k^6) with the exact rationals -1/6, -1/8, -1/9, -7/50 on the axis, face, body and (2,1,0) directions; zero lapse and shift kinetic weight on shell; and both propagating polarisations transverse-traceless up to gauge in the small-momentum limit, degrading at the zone corner. The edge-length variables, the selection of S_R, its overall orientation, the Lorentzian signature, the nonlinear completion and the record-to-geometry link are supplied and are not derived here."
upstream_dependencies:
  - docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md
  - docs/CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md
  - docs/CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md
  - docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md
  - docs/POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md
runner: scripts/regge_4d_complex_native_linearised_graviton_dispersion_check_2026_09_03.py
---

# The Regge second variation on the 4D cubic-Coxeter complex carries a native linearised graviton

**Date:** 2026-09-03

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source note writes no audit
verdict and retags no ledger row.

**Primary runner:**
[`scripts/regge_4d_complex_native_linearised_graviton_dispersion_check_2026_09_03.py`](../scripts/regge_4d_complex_native_linearised_graviton_dispersion_check_2026_09_03.py)
(PASS=11 FAIL=0)

**Runner cache:**
[`logs/runner-cache/regge_4d_complex_native_linearised_graviton_dispersion_check_2026_09_03.txt`](../logs/runner-cache/regge_4d_complex_native_linearised_graviton_dispersion_check_2026_09_03.txt)

**Parents:** the 3D equality row, the 3+1 tick-extension row, and the retained
spatial complex they both stand on; listed in *Load-bearing inputs* below.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Machine-exact linear-order spectral theorem on one declared complex at declared momenta; the geometric variables and the action remain supplied."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit; the runner re-executes both landed parent runners in-process."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Setting

The Lattice axiom is quoted verbatim from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic rotations
> about each site.
>
> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

The lattice is physical: `Z^3` is the site set, not a computational scaffold or
a chart on something else. Space is `Z^3` only; time is the emergent tick at
which records register. The complex used here is the tick extension
`T(Z^3 x Z_tau)` of the retained spatial chain, exactly as built by the landed
3+1 row: per 4-cell, the 24 path (Kuhn/Freudenthal) 4-simplices sharing the main
diagonal, 15 edge classes (the nonzero `0/1` vectors, flat lengths squared in
`{1,2,3,4}`), 50 triangle (hinge) classes, and 10 metric components against 15
edge classes, hence 5 non-metric edge directions. The tick edge is grained on
the same footing as the spatial edge under the registered
[`kinetic_isotropy_primitive`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
(`c_t = c_s`, a structural grant); the tick **scale** is not derived, and the
[`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md)
boundary is respected.

## The landed rows this one stands on

The 3D row
[`CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md)
establishes, on the retained six-tetrahedra chain, that the metric-sector Regge
form equals the 3D Euclidean linearised Einstein-Hilbert pairing with the single
constant `c = -1/2` in all three directions. The 3+1 row
[`CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION`](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)
extends that to `T(Z^3 x Z_tau)`: the same comparator constant across five
directions including the tick-mixed ones, the `lambda = 1` kinetic fibre metric,
the multiplier structure, and the split of the five non-metric directions into
four massive branches and one identically flat one.

Both rows evaluate `Q(k)` at **real** Euclidean momenta only. Neither extracts a
frequency. There is no `omega(k)`, no pole and no finite-frequency mode count in
either runner. That is what this note supplies at linear order.

## The question

Does the second variation of the Regge action, on the framework's own 4D
complex, carry a propagating spin-two mode with the right dispersion — from the
action itself, with no continuum operator consumed anywhere in the derivation?

The reading is declared. The signature is Euclidean/OS0, so the dispersion is
read as the poles of the lattice propagator by the holomorphic continuation of
the tick momentum, `k_tau = i omega`. `Q(k)` is entire in `k` — every entry is a
finite sum `c_j exp(i k . a_j)` with real coefficients and real anchors — so the
continuation is unique. The landed `bloch_Q` writes `conj(x(k))`, which is
correct only for real `k`; the continuation replaces it by `x(-k)`, and the same
replacement is made in the line-averaged metric map, whose midpoint phase times
sinc is written as the entire function `(exp(2iz) - 1) / (2iz)`. The gauge map is
already entire as landed and is reused verbatim.

**Provenance.** The runner imports
`scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py` as a
library and builds every geometric object from that module's own edge classes,
areas, dihedral derivatives and hinge stars. The complex analysed here is
therefore provably identical to the landed one, not a re-implementation of it.
The landed 3D runner is imported the same way. Both are declared to the audit
lane through `AUDIT_INPUT_PATHS`, so the cache is pinned to their content.

## Theorem (runner-verified; gates named)

**T1 (both parent runners reproduce).** The landed 3D and 3+1 runners, executed
in-process by this runner, both return `TOTAL: PASS=10 FAIL=0`. The 3D
comparator is unchanged: `c = -1/2` in all three directions with direction
spread `7.54e-08`; `TT(yz) = TT(E) = -0.250000` and transverse-trace `+0.250000`
(raw `S_R` orientation), ratio `-1`.

**T2 (kernel census; numerical tolerance `1e-12`).** On `T(Z^3 x Z_tau)`,
`dim ker Q(k) = 5` at every declared momentum. Four of the five are the discrete
diffeomorphisms — one vertex displacement per spacetime direction — annihilated
to `max|Q Gamma| <= 4.5e-15`. They coincide **exactly**, not approximately, with
the continuum family `h_munu = i(k_mu xi_nu + k_nu xi_mu)`: the worst
`max|Q_h Gamma_h| / |Q_h|` over the four declared momenta is `1.8e-13`. The fifth
lies outside the metric sector: it is the identically flat non-metric branch the
3+1 row already reports (`non-metric eigenvalues = [-48, -16, -16, -16, 0.0]`),
and it stays a null direction under continuation, so it never becomes a pole. The
metric-sector kernel is therefore exactly 4 and the metric-sector rank is
`10 - 4 = 6`.

**T3 (propagating-mode count).** Exactly two propagating modes, doubly
degenerate. At the on-shell frequency the null count rises from 5 to 7, with
`sigma_6` and `sigma_7` at machine zero (`~1e-17`) against a `sigma_8` fourteen
orders larger. Over twelve declared momenta — axis and body diagonal at
`|k| = 0.3, 1.0, 2.0, 2.5, 3.0, pi` — a 900-point scan of `omega in (0, 8]` with
refinement of every interior local minimum finds exactly one branch per momentum,
out to the zone boundary. No doubler, no spurious propagating branch, no extra
branch in the window.

**T4 (the exact dispersion).** The on-shell locus is exactly the zero set of the
standard hypercubic nearest-neighbour lattice d'Alembertian `k-hat^2`, continued
to `k_tau = i omega`:

> `4 sinh^2(omega/2) = sum_{i=1}^{3} 4 sin^2(k_i/2)`,
> equivalently `sum_{mu=0}^{3} 4 sin^2(k_mu/2) = 0` at `k_tau = i omega`.

Worst relative residual `3.243e-13` over 32 declared zone points in five
directions (axis, face, body, `(2,1,0)`, `(3,1,2)`); the residual is
root-finder limited, `~1e-15` typical. At small momentum,

> `omega^2 = k^2 - (k^4/12)(1 + sum_i n_i^4) + O(k^6)`,  `n = k/|k|`,

with the computed coefficients matching the exact rationals `-1/6` (axis),
`-1/8` (face), `-1/9` (body), `-7/50` (`(2,1,0)`) — and `(2,1,1)` reproducing
`-1/8` because it shares the same cubic invariant, so the anisotropy is that
invariant and nothing else. The mode is therefore massless with light speed
exactly 1 in tick units (`omega/|k| = 0.999991667` at `|k| = 0.01`), exactly
isotropic at `O(k^2)` — the relative direction spread over axis, face and body
is `0.0278 k^2`, constant to four figures from `|k| = 0.02` to `0.2` — and
anisotropic only at `O(k^4)`. The lapse `h_tautau` and shift `h_i,tau` kinetic
weights vanish on shell (`4.4e-16`, `3.7e-16`) as well as statically: the
multiplier structure holds at the pole, not only at zero frequency.

**T5 (polarisation, and the comparator).** Removing the four gauge directions
from the seven-dimensional on-shell kernel in edge space leaves three; exactly
two of them lie in the metric slice, and both are transverse-traceless up to
gauge. The TT fraction is `0.99999999` at `|k| = 0.05`, `0.999` at `0.8`, and
`0.96 / 0.89` at the zone corner. **This is a small-momentum statement.** TT is a
continuum notion and the exact lattice polarisation deforms at `O(k^2)`; the mode
count and the dispersion do not deform, and are machine-exact across the whole
zone. Separately, `omega = +-k` across the zone is **not** reproduced: `omega* - k`
is `-0.47` at `|k| = 2` and `-1.24` at `|k| = 3` on the axis.

## Corollary

1. **Yes at linear order.** On the framework's own 4D complex, `delta^2 S_R`
   carries exactly the diffeomorphism gauge zeros, exactly two propagating modes,
   no doublers, and the exact lattice dispersion of a massless mode at light
   speed 1, isotropic to quadratic order. That is the textbook
   `10 - 4 - 4 = 2` count, realised exactly on the lattice.
2. **This is a native linearised graviton on supplied edge lengths, not a
   certificate against a supplied operator.** Nothing in the computation consumes
   the continuum Einstein-Hilbert operator; the comparator relations are outputs
   tested against, never inputs.
3. **What stays supplied is named** — see the section below. The result is a
   statement about the dynamics of a supplied action on supplied variables.
4. **The earlier target-operator row's `omega = +-k` across the zone is the same
   polynomial read in Lorentzian signature, and holds only on axis.** The row
   [`UNIVERSAL_GR_3PLUS1_CONSTRAINT_MULTIPLIER_STRUCTURE_DERIVED_FIBER_METRIC`](UNIVERSAL_GR_3PLUS1_CONSTRAINT_MULTIPLIER_STRUCTURE_DERIVED_FIBER_METRIC_BOUNDED_THEOREM_NOTE_2026-06-09.md)
   gives `4 sin^2(omega/2) = 4 sin^2(k/2)`, i.e. `omega = +-k` exactly across the
   zone, for the written-down continuum-transcribed operator. Both relations are
   the same on-shell polynomial `sum_mu 4 sin^2(k_mu/2)`: with a real-time tick
   the timelike slot enters with the opposite sign and one gets
   `4 sin^2(omega/2) = sum_i 4 sin^2(k_i/2)`, which reduces to `omega = +-k` for
   **axis** momentum only — along a body diagonal the same relation gives
   `4 sin^2(omega/2) = 3 * 4 sin^2(k/(2 sqrt 3))`. The geometric complex here is
   Euclidean/OS0, so the same polynomial is continued instead and gives `sinh`.
   The two agree at `O(k)` and differ at `O(k^3)`. This is a signature-reading
   difference, stated both ways; a Lorentzian cubic-Coxeter complex is not built
   here and is the honest next step if `omega = +-k` across the zone is wanted
   from the geometry.
5. **Two superseded gates are recorded.** (a) A first pass gauge-fixed the
   Hessian against a *fixed* metric-sector complement. That complement degenerates
   whenever `k_tau -> 0` — the directions `h_xy`, `h_xz` become pure gauge there —
   and manufactured a spurious `omega/|k| = 4` branch. Mode counting must be
   basis-free; all results above use the singular values of the full `15 x 15`
   `Q(k)`, whose kernel is 5 at every momentum, so `sigma_6 -> 0` is the on-shell
   diagnostic. (b) A metric-slice gate reading `dim ker Q_h = 6` on shell fails,
   because the two physical null directions of the 15-dimensional edge-space
   Hessian are not exactly inside `range M(k)` at finite `k` (their principal
   cosines are `1 - 1e-8` at `|k| = 0.05`). The edge-space polarisation
   reading of T5 is the correct one and supersedes it.

## Reading, not theorem

Take the lattice's own way of building geometry out of edge lengths, disturb it
slightly, and ask what waves it carries. It carries exactly two, moving at the
speed of light with no extra copies, and the four directions of pure relabelling
do not propagate. That is what a graviton looks like at first order. The lengths
themselves, the action, and the link from records to lengths are still given by
hand.

## What stays supplied

| supplied object | status |
|---|---|
| edge lengths as the geometric variables | supplied; not derived from the axioms |
| selection of `S_R` as the action | supplied; the linearised action-selection row narrows the class at quadratic order without selecting |
| overall action orientation (`S_R` vs `-S_R`) | supplied; the single located sign residual, unchanged here |
| Lorentzian signature | supplied; this is the Euclidean/OS0 surface read by holomorphic continuation |
| the nonlinear completion | supplied; every statement here is quadratic order |
| the record-to-geometry link | supplied; nothing here derives edge lengths from what records register |
| the tick scale (`c_t = c_s`) | structural grant of the kinetic-isotropy primitive; not derived |

## Interfaces

- **Nonlinear order.** Cubic and higher terms of `S_R` on this complex,
  including the behaviour of the identically flat non-metric branch beyond
  quadratic order.
- **Lorentzian signature.** A Lorentzian cubic-Coxeter complex, which would
  produce `4 sin^2(omega/2) = sum_i 4 sin^2(k_i/2)` directly rather than by
  continuation.
- **The record-to-geometry link.** What fixes the edge lengths from what records
  register.
- **The tick scale.** The clock-rate interface, untouched.

## Proof boundary

The theorem proposed here is exactly the linear-order spectral statement of
T1–T5 on one complex at declared momenta, in the Euclidean/OS0 reading with the
holomorphic continuation `k_tau = i omega`. Covered: the complete enumeration of
`ker Q(k)` at four declared 4-momenta; the branch census over `omega in (0, 8]`
at twelve declared spatial momenta; the dispersion at 32 declared zone points in
five directions; the small-momentum coefficients in five directions; the
polarisation at five magnitudes. Every momentum is a declared constant of the
runner; there are no seeds. Outside this target: any statement at cubic or higher
order; any other complex; the `O(k^6)` term; the higher-order behaviour of the
flat non-metric branch; `G_Newton`, the attraction sign, and the equivalence
principle, all of which are separate targets with their own premises.

## Honest-auditor read

The strongest thing an auditor can take from this note is: *given* the edge
lengths as the variables and *given* `S_R` as the action, the framework's own 4D
complex has a linearised graviton with the correct mode count, the correct gauge
structure, the correct light cone and the correct lattice dispersion — and the
framework still supplies no reason, from the axioms, for either given. The
weakest link is not numerical: every gate here is machine-exact, and both parent
runners re-execute clean in the same process. It is the pair of supplied objects
named above. An auditor who wants to overturn the note should attack the reading
(`k_tau = i omega` on a Euclidean complex) or the provenance (that the imported
complex is the landed one), not the arithmetic. The `omega = +-k` disagreement
with the target-operator row is stated in the note rather than smoothed over: the
geometric action gives `sinh`, and that is the honest output of the Euclidean
reading.

## Load-bearing inputs

- [`CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md`](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) — the complex, the Bloch Hessian, the metric and gauge maps; its runner is imported as a library and re-executed here.
- [`CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md) — the 3D headline; its runner is re-executed here as the spatial comparator.
- [`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md) — the retained spatial chain that is the constant-tick slice.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the `c_t = c_s` structural grant; nothing beyond its declared grant is consumed.
- [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md) — the tick-scale boundary respected by the framing.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — the Lattice axiom quoted in *Setting*.

Context only, entering no check:
[`UNIVERSAL_GR_3PLUS1_CONSTRAINT_MULTIPLIER_STRUCTURE_DERIVED_FIBER_METRIC_BOUNDED_THEOREM_NOTE_2026-06-09.md`](UNIVERSAL_GR_3PLUS1_CONSTRAINT_MULTIPLIER_STRUCTURE_DERIVED_FIBER_METRIC_BOUNDED_THEOREM_NOTE_2026-06-09.md)
(the target-operator row of corollary 4) and
[`CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md`](CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md)
(the action-selection class).

## Forbidden-imports check

No PDG, fitted or literature value is consumed. The complex, the areas, the
dihedral angles, the deficits, the Hessian, the gauge and metric maps, the
continuation, the null-space census, the branch census, the dispersion and its
small-momentum coefficients are all constructed or derived in-runner. The exact
rationals `-1/6`, `-1/8`, `-1/9`, `-7/50` and the relation
`4 sinh^2(omega/2) = sum_i 4 sin^2(k_i/2)` are outputs tested against, not
inputs. Regge (1961), Rocek–Williams and Cheeger–Müller–Schrader appear as
context only and enter no check.
