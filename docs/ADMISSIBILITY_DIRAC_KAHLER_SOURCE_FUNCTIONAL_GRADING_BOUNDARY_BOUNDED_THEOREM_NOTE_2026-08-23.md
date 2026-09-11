---
claim_id: admissibility_dirac_kahler_source_functional_grading_boundary_bounded_theorem_note_2026-08-23
claim_type: bounded_theorem
claim_scope: "Formal Gaussian source differentiation and exact finite measurements on four supplied Dirac-Kahler cells: two cover extents and two transport-dial values. The ordinary complex Gaussian interpretation is conditional on, and here accompanied by, an exact positive-Hermitian-part certificate. The full selected historical displayed-order kernel is non-Hermitian on these cells, while one imposed rank-two restriction is positive. No physical source/event selector, universal reflection-positivity theorem, parent theorem, probability law, continuum result, axiom, premise, obligation, audit verdict, or TOE status is supplied or adopted."
depends_on:
  - admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_bounded_theorem_note_2026-08-23
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_source_functional_grading_boundary_2026_08_23.py
---

# Source-functional grading boundary — corrected finite note

**Historical block:** 179

**Repair date:** 2026-09-10

**Claim type:** `bounded_theorem`

**Claim status:** finite exact calculation; audit status is unset and deferred

**Primary runner:**
[`scripts/admissibility_dirac_kahler_source_functional_grading_boundary_2026_08_23.py`](../scripts/admissibility_dirac_kahler_source_functional_grading_boundary_2026_08_23.py)

**Finite helper:**
[`scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py`](../scripts/admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10.py)

**Finite rank-two dependency:**
[corrected Block 178 note](ADMISSIBILITY_DIRAC_KAHLER_RANK_TWO_SCALAR_TRANSPORT_COUNTEREXAMPLE_BOUNDED_THEOREM_NOTE_2026-08-23.md)

The helper uses the fixed matrices from the
[current Block 105 finite construction](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md).
That citation and the corrected Block 178 citation identify finite inputs only;
neither broader theorem scope is imported. The
[current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) remain the authority
boundary. This note adds no axiom or premise.

## Formal source algebra

For any supplied matrix `G`, define the formal normalized series

\[
 \widehat Z[\bar J,J]=\exp(\bar J^\top GJ).
\]

Formal differentiation at zero gives

\[
 {\partial^2\widehat Z\over\partial\bar J_a\partial J_b}\bigg|_0
 =G_{ab},
\]

and equal-degree higher derivatives give the corresponding permanent Wick
sum. Unequal source degrees vanish. These are algebraic power-series
identities; they require no convergence hypothesis.

The degree-zero coefficients of three different conventions are

\[
 [\widehat Z]_0=1,\qquad
 [Z_Q\widehat Z]_0=Z_Q,\qquad
 [Z_Q\overline{Z_Q}\widehat Z]_0=|Z_Q|^2.
\]

Multiplying by either scalar rescales every degree. A genuine doubled
independent-source functional has a larger bigrading. Algebra alone does not
identify any one convention as a physical readout or identify `|Z_Q|^2` with
the one-copy degree-zero sector.

## Convergence certificate for the supplied fixtures

Writing `Z_Q=pi^N/det(Q)` as an ordinary complex Gaussian integral requires

\[
 \operatorname{Herm}(Q)>0.
\]

A positive determinant alone is insufficient. For example, `Q=-I` in even
dimension has positive determinant but does not define the ordinary convergent
Gaussian integral.

The live finite helper supplies an exact certificate on the two extents. At
each cover cell the volume is positive and the shear is either `0` or `3/5`.
Up to the common positive local assembly factor, the Hodge-cell eigenvalues are

\[
 v,\qquad {1\over v},\qquad {v\over1-s},\qquad {v\over1+s},
\]

so every cell contribution is positive for `v>0` and `|s|<1`. The assembled
cover Hodge form is positive. If `J_AP=(-I,I)^T` is the full-column-rank
antiperiodic injection, the helper checks the exact identity

\[
 H_q={1\over2}J_{AP}^\dagger HJ_{AP}.
\]

Therefore `H_q>0`. The connection contribution has the form

\[
 K_q=i(Hd+d^\dagger H),
\]

which is anti-Hermitian. At the supplied mass `m=1`,

\[
 Q=H_q+K_q,\qquad \operatorname{Herm}(Q)=H_q>0.
\]

The runner checks the restriction identity, carrier inequalities,
full-column-rank injection, anti-Hermiticity of `K_q`, and
`Herm(Q)=H_q` exactly at both extents and both dials. Only after those checks is
`pi^N/det(Q)` described as the convergent one-copy Gaussian coefficient.

## Four finite raw-kernel measurements

The disclosed fixtures use cover extents `8x4` and `12x4`, transport dial
`s_t` in `{0,1/4}`, selected rows `(4,5,6,7,8,9,10,11)`, the supplied graded
carrier and reflection, mass `1`, and the rank-two isometry from the corrected
Block 178 calculation.

For historical comparison, the archived original107 body implemented

\[
 K^{\rm code}_{ab}=\overline{G(a,\theta b)},
\]

while its displayed equation used

\[
 K^{\rm disp}_{ab}=\overline{G(b,\theta a)}.
\]

On a generic matrix the two are transposes. There is no canonical original107
primary on the repair base, and the current Block 109 interface is different.
This note preserves a dated comparison between the two exact original107
surfaces; it does not report a current-main defect or substitute Block 109 for
Block 107.

Using the historical displayed order on the four real fixtures, the full
selected eight-source kernel is non-Hermitian. Its anti-Hermitian part has rank
`8`. The inertia of its Hermitian part, in `(positive,negative,zero)` order, is

| cover | `s_t=0` | `s_t=1/4` |
|---|---:|---:|
| `8x4` | `(6,2,0)` | `(6,2,0)` |
| `12x4` | `(4,4,0)` | `(4,4,0)` |

The exact action-side reflection-covariance defect has `(0,0)` entry
`-997/27456` at `8x4` and `3167/10560` at `12x4`.

These are four finite measurements of one selected historical convention. They
do not prove that all source kernels, reflections, actions, or physical event
domains have the same boundary.

## Preserved positive route

For the imposed isometry

\[
 X=\left[{4e_0+3e_4\over5},{4e_2+3e_6\over5}\right],
\]

`X^dag K X` is exactly Hermitian and positive at all four cells, and the two
historical row/column orders agree after this restriction. The exact half-trace
change from `s_t=0` to `1/4` is

\[
 {73977924244224\over1492124486100431}
\]

at `8x4`, and

\[
 {150346029799280479942166602650413136160
  \over2455275247171512614379752553769527826469}
\]

at `12x4`; both are positive.

Shift by two intertwines every weight pair `(u,v)`, so it does not select the
specific weights `(4/5,3/5)`. The imposed subspace also leaks under the
reflection, local action, and selected action form. Thus the positive
restriction is a real finite existence route, not a derived physical selector.

Because `Herm(Q)>0` is certified, the ordinary one-copy Gaussian is convergent
on these fixtures. The runner also finds `det(Q)>0` at both dials on each
extent, with distinct determinant values. Hence `Z_Q=pi^N/det(Q)` is positive
and dial-sensitive here. This closes only the earlier finite one-copy vacuum
question. It does not Hermitianize the raw higher-sector kernel or choose a
physical one-copy or doubled source law.

## Runtime closure and historical disposition

The repaired primary imports only the dedicated pair helper. That helper binds
the already reviewed finite supplier and current Block 105 bytes, and extracts
only the historical formulas needed for the reflection bench, graded carrier,
rank-two effect, exact inertia, and original107 convention comparison. The
runner binds every live filesystem input with literal SHA-256 values.

All eight original pair bodies are preserved byte-for-byte in the recovery
packet: five science sources, two historical caches, and the historical
manifest occurrence. The recovery map also records all 51 historical static
source occurrences and identifies the five corrected current-main sources that
were preserved rather than overwritten. Historical parent theorem prose,
status tables, campaign routing, and claims of universal closure remain
archive-only.

## Scope and disposition

Preserved results are the formal covariance and permanent identities, the
vacuum-category distinction, the exact positive-Hermitian-part proof on the
four fixtures, the four raw-kernel measurements, the positive imposed
restriction, and the convergent one-copy determinant response.

The package does not identify a physical source/event algebra, choose a field
reflection, derive a Record-to-source map, select one-copy or doubled
normalization, derive the Born rule, prove a universal OS theorem, establish a
continuum limit, or adopt any parent theorem. It predicts no audit result and
directs no campaign budget. Any continuation is optional work under current
shared planning.

## N1 — alternative routes

Live routes include a derived physical event/source algebra, a different field
reflection, a separately justified Hermitianized kernel, an explicit doubled
functional with a sewing map, a full effect-refinement/additivity theorem, and
other fixtures or continuum controls. The present calculation excludes none of
those families.

## N2 — separate obligations

Choosing the physical event/source domain, choosing its reflection/positivity
rule, and choosing a one-copy or doubled normalization are separate missing
supplies in this scope. Their distinction helps route future work; no
countermodel family here proves logical independence in both implication
directions.

## N3 — hidden assumptions

The Gaussian action, carrier, finite Hodge data, reflection, support, dials,
rank-two `X`, and historical row/column convention are supplied inputs. The
formal series and ordinary integral are explicitly separated. No supplied
construction is promoted to an axiom, premise, or physical law.

## N4 — residual matching

Formal differentiation supports only the Wick identities. The positive-Hodge
certificate supports convergence only on the supplied fixtures. The
original107 comparison supports only the dated transpose statement. The full
kernel and restricted kernel are recomputed separately; neither substitutes
for a physical selector theorem.

## N5 — rhetoric and resolution

The runner prints the resolution boundary: per element it distinguishes formal
and convergent Gaussian statements; per site it checks four finite cells; per
mode it compares two supplied dial values; per block it preserves the algebraic
and finite boundary results; lattice-wide and whole-TOE conclusions are not
executed.

## N6 — partial closure

A derived event/source algebra plus field reflection could turn the positive
finite route into a conditional representation theorem. An explicit one-copy
or doubled sewing law could settle bookkeeping. Those are constructive paths,
and their absence does not imply that a new axiom is required.

## N7 — hostile-reviewer steelman

The strongest positive reading is that a physical source map may select a
positive subspace like the displayed `X`, while the convergent one-copy
Gaussian already supplies a positive dial-sensitive vacuum. This mechanism
defeats any universal negative claim. What remains is to derive the selector
and show that its probabilities agree with the intended physical event law.

## N8 — cross-cycle echo

Earlier source/readout work repeatedly separated finite positive matrices from
a physical event selector and separated algebraic normalization from a
probability rule. The present convergence repair closes a real algebraic gap,
but the same distinction remains: finite positivity and a source series do not
by themselves choose Nature's event domain or weighting law.
