---
claim_id: spin_half_cubic_ice_source_receipt_diagnostic_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Deterministic consistency and fixed-protocol arithmetic for six exactly preserved historical cubic-ice receipts, conditional on the supplied source convention and literal recorded rows. The historical replay fails, its two detuned primary spans exceed 0.05, the magnetic source is checkerboard Cartesian, and the electric benchmark borrows another estimator's uncertainty. No producer validation, calibrated confidence coverage, thermodynamic law, physical UK certificate or exclusion of other routes."
upstream_dependencies:
  - spin_half_cartesian_plaquette_source_note_2026-09-07
runner: scripts/spin_half_cubic_ice_source_receipt_diagnostic_2026_09_07.py
---

# A bounded diagnostic for the historical cubic-ice source and receipts

The six historical receipts do not supply a physical static–dynamic Maxwell
certificate. The implemented magnetic source is checkerboard Cartesian under
the stated electric convention; the preserved replay exits with failure and
misses its genealogy and relative-span requirements; the benchmark electric
central value and uncertainty refer to different estimators. This note records
those specific obstructions to that comparison. It makes no claim that other
sources, estimators, states, carriers or continuum limits cannot work.

The new runner checks deterministic consistency of exact historical data and
recomputes the stated arithmetic. Its own successful receipt means those
checks worked. It cannot issue a physical certificate. It does not execute,
import, repair or validate the old production tower, and no new large-volume
sampling is performed.

## What is preserved and what is assumed

The controlled [fixture](../data/field/spin_half_cubic_ice_historical_receipts_2026_09_07.json)
contains six complete UTF-8 payloads from the frozen successor #7966 at
`369f785003f19c1ec5e8c4a6f1155c2827a7986b`. Each has its original constituent
PR/head/base provenance, capture path/mode/blob/SHA-256, producer identity and
available declared-input identities at that successor. These are historical
captures, including their failed status, stdout, stderr and later scope
annotations; they are not fresh caches for the corrected source.

| Receipt | Historical exit / check counts | Role here |
| --- | --- | --- |
| Projector stiffness | 0 / 12 passed | Unvalidated electric-flux production provenance |
| Charge/Coulomb join | 0 / 15 passed | Literal U_flux and U_charge estimator extraction |
| Magnetic response | 0 / 13 passed | Literal checkerboard-source response extraction |
| Late-time spectrum | 0 / 11 passed | Complete historical spectral payload |
| Infrared ladder | 1 / 2 passed, 1 failed | Preserved failed genealogy evidence |
| Paired-forward replay | 1 / 3 passed, 1 failed | Eight paired rows and fixed-protocol diagnostic |

A green historical header does not establish valid producer code or physics.
Only available declared inputs are inventoried: undeclared scientific helpers
and their proof premises remain unreviewed by this unit. A snapshot input
fingerprint is compared with the historical header and its match flag is
reported, without treating a match as closure of undeclared inputs. The
infrared capture's elapsed 26,040.72 seconds exceeds its declared 21,600-second
timeout; this historical anomaly is retained and reported, not normalized.
The replay's recorded elapsed time is 20,807.00 seconds. Neither run is repeated.

The 57 original field-chain sources remain at #7966 with their review
obligations intact: 11 notes, 23 runners and 23 caches originating in
#7941/#7943/#7945/#7946/#7952/#7953/#7955/#7963/#7966. The earlier constituent
closures consolidate those obligations at the successor; this small unit
neither lands their production source nor grants it a scientific disposition.
The generated original manifest and all reserved #6379/#6858/#6859 content are
outside this selection.

## Source convention and the electric benchmark

The [independent source note](SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07.md)
uses the supplied observable
`E_i(r)=epsilon(r)(n_i(r)-1/2)`, with `epsilon(r)=(-1)^sum(r)`.
A ring move changes the oriented electric field by
`Delta E=-epsilon(r)*s_p(n)*boundary(p)`. Therefore a uniform Cartesian
plaquette source requires `exp(i theta epsilon(r) s_p(n))`, up to a common
orientation sign. The historical real-angle and imaginary-source magnetic
implementations omit epsilon. Their numbers describe a checkerboard Cartesian
source in these fixed electric coordinates.

The source note proves a local identity, a finite source-family discriminator
and finite covariance/endpoint identities conditional on the supplied carrier,
Hamiltonian, ground-state prescription and component. It also exhibits a
nonzero infinitesimal uniform-source curvature alongside a whole-flux endpoint
unitary. A relaxed source curvature is not automatically an energy in a
specified magnetic-flux sector. No thermodynamic uniform-source coefficient or
physical electromagnetic identification is supplied here.

The V=0.95 charge row contains `U_charge=0.160609 +/- 0.015345` and
`U_flux=0.162638`. The magnetic summary contains checkerboard
`K=0.075561 +/- 0.000915`. The old comparison calculates

\[
U_{\rm flux}K=0.012289089918,\qquad
\sigma_{\rm hybrid}=\sqrt{(U_{\rm flux}\,0.000915)^2+
                         (K\,0.015345)^2}
=0.0011689942811097837.
\]

The central value uses U_flux; the electric error comes from U_charge. No
uncertainty for U_flux is provided by that line, and any covariance between the
chosen estimators is also unspecified. The runner preserves this exact named
historical prescription as unresolved arithmetic. It does not substitute the
charge central value or invent a flux error bar.

## Paired diagnostic and exact scope of its thresholds

The replay has six replicas at each of `(V,L)=(1,16),(1,18),(.95,16),(.95,18)`.
Its forward endpoints are `(6,12,20)` and fit windows `(2,6)` and `(8,14)`.
For each of the eight printed rows, let `g=(g6,g12,g20)` and let Sigma be its
printed 3-by-3 covariance. The inverse expressions below apply only to the
detuned rows; the RK identity case is treated separately. Use the paired contrasts

\[
C=\begin{pmatrix}-1&1&0\\-1&0&1\end{pmatrix},\quad
 d=Cg,\quad S=C\Sigma C^T,\quad
 H=d^TS^{-1}d,\quad T=\max_i |d_i|/\sqrt{S_{ii}},\quad
 R=(\max g-\min g)/\operatorname{mean}(g).
\]

The inherited strict diagnostic limits are `H<17.361`, `T<2.571` and `R<0.05`.
The covariance is constructed from six leave-one-replica-out **nonlinear fitted
gap vectors**, with `(n-1)/n` times their centered jackknife Gram matrix. It is
not an exact sample covariance of six independent Gaussian vectors. The fixed
numbers 17.361 and 2.571 remain predeclared protocol cutoffs; no exact Hotelling,
Student or calibrated 95% coverage is claimed. The diagnostic retains the full
paired covariance; it does not replace it with a diagonal independence model.

At the primary window 8–14 the detuned relative spans are:

| L | Relative span | Span rule | Significance cutoffs |
| --- | --- | --- | --- |
| 16 | 0.05809271167933884 | Fails | Pass |
| 18 | 0.13497596323427857 | Fails | Pass |

The fixed health requirements are `min_ess>0.85`, `min_origin_count>=40` and
`min_forward_count>=40`. At detuned L=18 the recorded values are 0.943968,
57 and 36. The forward genealogy floor fails. Significance arithmetic does not
override either the span rule or this failure, and the original producer exit
remains 1.

The four RK rows have exactly identical endpoint means and common-mode,
rank-one covariances. Their contrast covariance is zero. They are explicitly
checked as identity controls and are never inverted. They do not establish
detuned convergence. Detuned contrast covariances must be positive definite at
the declared numerical tolerance before evaluating the two statistics.

Errors are printed to eight decimals and covariances to `.12e`. The declared
standard-deviation comparison allows absolute rounding error 5.001e-9.
Covariance symmetry/positive-semidefinite checks use
`1e-18 + 2e-12*max(abs(Sigma))`; detuned contrast eigenvalues must exceed four
times that tolerance. Tiny roundoff eigenvalues of the exact rank-one RK
covariance are allowed. These tolerances handle printing and floating-point
arithmetic; they do not weaken the original acceptance thresholds.

## Canonical parser, controls and actual inputs

The parser requires one ordered cache header, one stdout/stderr envelope,
one stdout total, and header/exit/check-count consistency. It rejects header
or status tokens appended elsewhere rather than searching for success
substrings. Complete paired rows, replica endpoints, health rows and the
certificate are unique and fixed. Exact payload and whole-fixture SHA-256
identities bind all remaining historical text, producer/input provenance and
source-family metadata. Post-total recovery annotations remain exact inert
text and cannot replace the canonical status. This is consistency checking
against a known fixture, not an authenticator of arbitrary live logs.

Validation exercises actual adverse fixture files: appended forged success;
duplicate/conflicting headers, totals, paired rows, forward endpoints and
replica endpoints; stale producer, input, payload and fixture identities;
wrong source family; malformed, nonfinite, asymmetric, inconsistent-diagonal
and singular detuned covariance. The genuine singular RK rows are accepted.
Structural and covariance checks run before the final immutable fixture pin,
so those controls exercise the corresponding parser rather than only a hash.
Source matching and fixed-protocol statistics are separate guards: changing a
source label cannot turn a failed genealogy or span into a pass.

The primary and independent source runners each read and hash their source
note and the current axiom memo. The diagnostic reads and hashes this note,
the source note and the fixture, then checks those identities again before
finishing. Each fresh cache also binds its own runner source. There are no
local scientific imports; the independent source checker is registered as a
packet sibling in both actual helper consumers and is executed separately.
Passing these deterministic checks applies no audit verdict.

## Current claim status and trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: >-
  No reviewed downstream consumer is selected. A physical static-dynamic
  Maxwell comparison still requires matched sources, valid producer/helper
  closure, converged sampling and justified uncertainties.
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: >-
  Review all original field producer and proof obligations at the preserved
  successor; specify and independently calibrate a uniform-source measurement
  and a bounded genealogy/runtime plan before any expensive sampling.
conditional_surface_status: >-
  Literal frozen receipt data and supplied source conventions only; failed
  replay and unresolved electric uncertainty remain; physical_certificate=false.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: >-
  Conditional finite source interpretation and deterministic data-consistency
  statements are explicitly scoped; author labels do not grant retention.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
