---
claim_id: spin_half_cartesian_plaquette_source_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional on the explicitly supplied cubic-ice occupation carrier, ring Hamiltonian and E_i(r)=(-1)^sum(r)(n_i(r)-1/2): local oriented electric-update and plaquette-source covariance identities on the infinite cubic lattice, compatible open subcomplexes, and tori with every periodic extent even; finite-source operator identities on any finite ring-move component; an exact source-family inequality and numerical infinitesimal uniform Cartesian source curvatures on the stated 864-state L=2 component; a constructive full-background-flux endpoint unitary on even periodic cubic tori. No thermodynamic magnetic stiffness, magnetic-flux-sector energy, physical electromagnetic identification or static-dynamic Maxwell equality is established."
upstream_dependencies:
  - minimal_axioms
runner: scripts/spin_half_cartesian_plaquette_source_2026_09_07.py
packet_helper_runner:
  - scripts/spin_half_cartesian_plaquette_source_independent_check_2026_09_07.py
---

# Cartesian plaquette sources for the supplied spin-half cubic-ice carrier

The magnetic source must use the same electric-field convention as the electric
flux and spectrum to which it is compared. For the supplied observable
`E_i(r)=ε(r)(n_i(r)-1/2)`, a ring flip has

\[
\Delta E=-\epsilon(r)s_p(n)\,\partial p,
\qquad \epsilon(r)=(-1)^{r_x+r_y+r_z},\quad s_p(n)=2n_i(r)-1.
\]

Consequently, a uniform Cartesian plaquette source has phase
`exp(i θε(r)s_p(n))`, up to a common orientation sign. The phase
`exp(i θs_p(n))` implemented by frozen historical PR #7946 is a checkerboard source
in those same electric coordinates. An exact finite trace polynomial proves
that these are different matrix families at generic angle. The original
matrix's response numbers remain meaningful for its implemented source.
Their use as the independently measured uniform coefficient in `c²=UK`
requires a source-identification correction.

There is a second, distinct issue: the minimum energy of the fully relaxed
uniformly sourced matrix returns to the zero-source spectrum at a whole
background flux quantum. Its infinitesimal curvature is therefore not, by
itself, the energy of a specified magnetic-flux sector. This note constructs
both identities and keeps those observables separate.

## Supplied objects and quantified domain

The framework authority is the current [four-axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
Its neighbor-dependent probability-distribution clause supplies neither this
Hamiltonian nor a ground-state probability rule. The approved scale reference,
kinetic-form isotropy and pointwise realized-state interface likewise supply
neither the following carrier nor its observable map.

All scientific statements here are conditional on these explicit definitions:

- A two-state occupation `n_i(r)∈{0,1}` on each positive-coordinate link of
  the cubic cell complex, with three occupied incident links at each vertex
  where the ice constraint is imposed. The identification of link qubits with
  the framework's one-qubit-per-site possibilities is not derived here.
- Complete elementary square flips of the alternating patterns described
  below. On a finite carrier, `Ω` denotes any connected component of this
  move graph; frozen configurations are allowed as singleton components.
- In the occupation basis, diagonal energy `V N_f(n)` and off-diagonal
  contribution `-J` for each geometric allowed ring move, with real `V` and
  `J>0`. Here `N_f` counts flippable squares. Distinct geometric moves are
  summed even when they share endpoints. Numerical tables use `J=1`.
- The electric observable `E_i(r)=ε(r)(n_i(r)-1/2)`, the oriented cell
  incidence maps, the external plaquette source defined below, and, for the
  finite response, the lowest eigenvalue of this supplied Hermitian matrix.

The local identities hold on the infinite cubic lattice and any open
subcomplex containing the square in question. On a periodic rectangular
carrier they require **every periodic extent to be even**, so that root
parity flips across every nearest-neighbor edge. Odd periodic extensions are
outside the claim. Finite-component unitary identities need no positivity
or uniqueness assumption beyond their stated matrix definitions. The
infinite-lattice statement is local algebra; it does not assert an infinite
Hamiltonian, global Hilbert-space unitary, or thermodynamic state.

## Local source construction

For ordered axes `(i,j)` and root `r`, list the links as

\[
(r,i),\ (r+e_i,j),\ (r+e_j,i),\ (r,j),
\qquad \partial p=(+1,+1,-1,-1).
\]

An allowed occupation pattern is `(a,1-a,a,1-a)`. With `s=2a-1`, its flip
changes occupation by `(-s,+s,-s,+s)`. The four link-root parities are
`(ε,-ε,-ε,ε)`. Multiplication gives `ΔE=-εs∂p` exactly. The electric
divergence is preserved because the boundary of a square has zero boundary.
This proof uses only the four affected links; no finite-volume sampling or
continuum approximation enters it.

For arbitrary real plaquette cochain `b`, define the matrix in the convention
that row `n` and column `n^p` are the old and flipped configurations:

\[
H_V[b]_{n,n^p}=-J\exp\{i\epsilon(r)s_p(n)b_p\},\qquad
H_V[b]_{n,n}=V N_f(n).
\]

Every contributing geometric move is summed. Reversal changes `s` to `-s`,
so the matrix is Hermitian for real `b`. For any real link cochain `a`, set

\[
D(a)|n\rangle=\exp(i\langle a,E(n)\rangle)|n\rangle.
\]

Since `E(n)-E(n^p)=εs∂p`, direct multiplication proves

\[
\boxed{H_V[b+da]=D(a)H_V[b]D(a)^\dagger.}
\]

Thus an exact-curl source is a basis rotation of zero source, on every finite
component. Closed source cochains modulo exact ones form the harmonic source
classes on a torus. Arbitrary nonclosed sources also define matrices, but
are different response channels. No canonical rotor or infinite-dimensional
on-link algebra is assumed: `D(a)` is a diagonal rotation of finite-spin
occupation states.

Fixing `b_ij(r)=θ` is the uniform Cartesian source in this electric
convention. The old exponent `θs` instead fixes `b_ij(r)=ε(r)θ`, at root
wavevector `(π,π,π)`. This distinction also appears in the cube sum: the
uniform source contributes zero, while a checkerboard source on one plane
contributes `-2ε(r)θ` along its transverse direction. Exact curls have zero
cube sum by cancellation of edges. The two sources therefore cannot differ
only by an ordinary link rephasing near zero.

Reversing the ordered square orientation, transposing the matrix convention,
or reversing θ consistently changes a global sign and leaves the curvature
unchanged. Redefining the electric field can rename a source, but its Fourier
observables and electric normalization then change too. That is not an
identification of the two sources while keeping the parents' E fixed.

## Exact finite separation and continuous-source curvature

The finite discriminator uses the periodic `L=2` component reached from
`n_i(r)=r_i mod 2`: 864 states and 6,912 directed geometric ring moves. Both
independent constructions verify the local update; the independent helper
also checks every state's ice constraint and zero electric flux.

At `V=J=1`, exact integer Laurent-polynomial calculation gives

\[
\begin{aligned}
\operatorname{tr}H_s(\theta)^4&=8{,}975{,}616,\\
\operatorname{tr}H_{\epsilon s}(\theta)^4
 &=8{,}973{,}184+2{,}432\cos(4\theta).
\end{aligned}
\]

The primary independently differentiates integer matrix products and obtains
fourth-trace second derivatives `0` and `-38,912`, respectively. Similarity
preserves traces of powers, so the families are not unitarily equivalent on
this component at generic θ with the same source parameter. This is a finite
source distinction, not an infrared phase statement or a universal physical
no-go.

Define the **uniform Cartesian source curvature** on this finite component by

\[
\chi_L=L^{-3}\left.\frac{d^2E_{0,L}(\theta)}{d\theta^2}\right|_{\theta=0}.
\]

A connected component with `J>0` has a unique lowest eigenvector: shifting
`-H(0)` by a sufficiently large scalar produces an irreducible nonnegative
matrix with a positive diagonal, and Perron–Frobenius applies. Finite
simplicity supplies an analytic eigenvalue near zero and, on a nonsingleton
component, a positive gap to the next eigenvalue.
Differentiating the finite eigenvalue equation gives

\[
L^3\chi_L=\langle0|H''|0\rangle
 -2\sum_{m>0}\frac{|\langle m|H'|0\rangle|^2}{E_m-E_0}.
\]

The sum is empty on a singleton. This formula is used only on the declared
finite matrices. A dense full spectral sum and an independently constructed
bordered sparse solve agree as follows:

| V, J=1 | Occupation-sign source curvature | Uniform Cartesian source curvature χ₂ |
|---:|---:|---:|
| 1.00 | 0.105121402155 | 0.285050028242 |
| 0.95 | 0.107539111729 | 0.286566088925 |
| 0.90 | 0.109734422219 | 0.287751063895 |

Their maximum absolute disagreement across all six values is below `7e-15`.
These are numerical derivatives of finite eigenvalues, not exact closed-form
constants. Ground and response-solve residuals are below `1e-11`. Hermitian
finite differences at `.02` and `.01` converge quadratically; the independent
helper also checks imaginary-source continuation. The independent legacy
`.02` values reproduce frozen #7946's displayed continuation values. Neither
implementation runs that PR's production Monte Carlo.

The direct terms coincide because both sign prescriptions have the same
square. At RK, the direct term divided by volume is `1/3`; the relaxation
terms differ. A fixed-state flippability expectation therefore cannot identify
which relaxed source response is being measured. None of these L2 values
replaces the larger-volume response ladder or establishes thermodynamic K.

## A full background flux quantum is a different question

On any even cubic torus, for a uniform xy source let `θL²=2πm`, `m∈Z`, and
choose the periodic link phases

\[
a_y(x,y,z)=\theta x,\qquad
a_x(L-1,y,z)=-\theta L y,
\]

with other `a_x` and every `a_z` zero. Its xy curl equals θ except at the
corner seam, where it equals `θ-θL²`; the other curls vanish. Since `εs` is
integer, the two plaquette phases are identical modulo `2π`. The source
identity therefore proves

\[
H_V[\theta\,dx\wedge dy]=D(a)H_V[0]D(a)^\dagger
\quad\text{when}\quad\theta L^2\in2\pi\mathbb Z.
\]

`D(a)` preserves each occupation move component. Thus the **fully relaxed**
minimum at this endpoint equals the zero-source minimum on that component.
The L2 `V=.95`, `θ=π/2` matrix identity is independently checked; the helper
also compares the lowest energies. Local seam-phase checks run at L2/L4/L6.

A positive derivative at zero is compatible with this endpoint equality.
Determining the energy of a followed flux branch or a specified magnetic-flux
sector requires a branch/sector definition and control of the limiting
procedure. Substituting `θ=2π/L²` into a local quadratic expansion without a
uniform remainder bound does not establish that energy. This note derives
neither a magnetic-flux-sector stiffness nor a thermodynamic helicity modulus.

## Frozen provenance and narrow consequences

Main premise snapshot: `f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`.
All open-PR scientific objects needed here are defined above; the following
addresses record their provenance, rather than assuming their review status.

| PR | Frozen head | Relevant source |
|---|---|---|
| [#7937](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7937) | `2814c6768e4d7b38048f70ad7883b4951cb12da3` | Electric-flux/stiffness carrier |
| [#7945](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7945) | `ecbea1587cf8c29e94caf8eaa3eb28fab2558b5f` | Staggered transverse-electric spectrum |
| [#7946](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7946) | `4b4919dc58cb35d51ed675ba69ec9431e319d338` | `spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py`, `flip_weight` and `exact_small_hamiltonian` omit root ε in the source |
| [#7952](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7952) | `48790c92bec9287e4a30f1e6595afa1d076b8998` | Late-time UK fit; separate quadratic-kernel theorem |
| [#7955](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7955) | `3cd24f9ea3a962088cd285b85a862c591d97b374` | Off-axis UK localization |
| [#7963](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7963) | `0b63aebcf9df437a95ac23f56b2981ea80e2be6c` | Infrared UK comparisons and estimator failure |
| [#7966](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7966) | `369f785003f19c1ec5e8c4a6f1155c2827a7986b` | Forward-replay diagnostic UK comparisons |
| [#7976](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7976) | `d2dd83da37f6ebe03c7075a218f9cbdff8a3efe9` | Landing-core synthesis |

The original #7946 response numbers survive as estimates for its implemented
checkerboard source, subject to their original finite-population limitations.
Their identification as uniform magnetic K, and the UK-based interpretations
in the listed descendants, need correction. Regressions against the original
fixed number remain arithmetic statements, not tests of the newly matched
uniform-source coefficient. Their separate genealogy and forward-stability
failures remain separate.

The source correction does not alter the electric field, measured transverse
correlators, raw spectra, electric U, or the conditional cubic/gauge quadratic
kernel classification. It also does not refute their results by association.
Independent production validation of those quantities is outside this block.
The next measurement is the matched **continuous-source curvature** with an
explicit source convention. A magnetic-flux-sector or thermodynamic stiffness
claim requires the additional obligation above before a physical UK join.

## Reproduction, independence and mutation checks

Run from the repository root:

```bash
OPENBLAS_NUM_THREADS=1 python3 scripts/spin_half_cartesian_plaquette_source_2026_09_07.py
OPENBLAS_NUM_THREADS=1 python3 scripts/spin_half_cartesian_plaquette_source_independent_check_2026_09_07.py
```

Both take optional `--json PATH` and otherwise write only stdout. NumPy and
SciPy are mathematical tools; neither runner imports repository science code
or reads a moving PR. The primary reports `TOTAL: PASS=19 FAIL=0`; the
independent helper reports `TOTAL: PASS=55 FAIL=0` on the packaged revision.

The primary's original root-major bit construction and dense spectral-sum
check were authored before the scout read the fresh checker's work. The
independent helper preserves that checker's axis-major construction, exact
Laurent trace enumeration and bordered sparse solve. Packaging changed its
CLI/output and check reporting, and added assertions of its already-derived
trace polynomial. This preserves the provenance of the independent derivation;
final-file review remains a separate coordinator-arranged check.

The campaign field pack preserves JSON/log receipts, source hashes,
`INDEPENDENT_PROVENANCE.json`, and `verify_and_mutate.py`. The latter reproduces
both runners, compares their results, and mutates only scratch copies. All
seven executed mutations produce nonzero exit and a scientific check failure:

| Scratch mutation | Detecting content |
|---|---|
| Remove ε from the primary uniform-source family | Exact fourth-trace derivative |
| Remove ε from the primary arbitrary-source family | General-source and exact-curl rephasing identities |
| Reverse one boundary edge | Local electric update and source covariance |
| Omit the primary full-flux seam | Full-flux matrix identity |
| Add rather than subtract spectral relaxation | Finite-difference convergence |
| Remove ε from the independent source | Laurent trace and full-flux identity |
| Omit the independent full-flux seam | Full-flux matrix identity |

Local even-periodic tests cover every root and both signs at L2/L4/L6 in the
primary, and through L12 in the helper. The primary also checks unwrapped
negative roots and both ordered-axis orientations. The L3 periodic control
fails the bipartite identity as expected; it is not a supported extension.
These checks supplement the local proof, not a numerical proof of its
infinite domain. No large-volume Monte Carlo, formal audit, source-branch
mutation, or status promotion is part of this block.


## Source and receipt repair — 2026-09-07

The original three-file checkpoint is preserved at
`e3d28020b5fbe5f8c7c00bd030aba991abb364d3`. This repair binds the two separately
executed constructions to this note and the actual current four-axiom memo on
landed main `94e90cbf928cb35fa1b50e894cd897c94b73077f`; each runner reads and emits
their SHA-256 identities and checks those identities again before finishing.
Its receipt also binds its own source. Neither runner imports the other.
The historical main snapshot above remains provenance for the original work.
The checkpoint declared identifier `spin_half_cartesian_plaquette_source_2026_09_07` is
historical metadata. The current claim ID follows the actual graph consumer's
canonical note-filename rule.

The independent sparse solve reports `sampled_ritz_separation`, not a certified
first spectral gap. Its deterministic two-vector Ritz call at V=0.95 gives
1.2244543292624046 whereas the complete dense spectrum gives a first gap of
1.0305400919127556. Residuals near 1e-14 do not exclude a missed lower sector.
No assertion or response denominator uses the reported Ritz separation: the
independent curvature uses the bordered solve; the primary curvature uses the
complete dense spectral sum. The finite connected-component Perron–Frobenius
argument above supplies simplicity of the ground state independently of this
sampled separation.

The historical receipt diagnostic
`spin_half_cubic_ice_source_receipt_diagnostic_note_2026-09-07`
preserves the old source response and failed replay as inert evidence. The
magnetic label correction does not repair the detuned genealogy or relative-span
failures, and the old U_flux central estimate has no supplied U_flux uncertainty.
No original field-chain source or review obligation is retired by this note.

## Current claim status and trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: spin_half_cubic_ice_source_receipt_diagnostic_note_2026-09-07
target_blocker_text: >-
  A physical UK comparison lacks a matched uniform Cartesian source, converged
  detuned replay and an uncertainty for the chosen electric estimator.
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: >-
  Review this source correction and the bounded receipt diagnostic, then specify
  an independently calibrated uniform-source producer before new sampling.
conditional_surface_status: >-
  Supplied occupation carrier, ring Hamiltonian, electric convention, component
  and finite ground-state rule; no thermodynamic or physical Maxwell result.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: >-
  The local identities and finite calculations are conditional mathematics.
  Author classification and passing checks do not apply a scientific grade.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
