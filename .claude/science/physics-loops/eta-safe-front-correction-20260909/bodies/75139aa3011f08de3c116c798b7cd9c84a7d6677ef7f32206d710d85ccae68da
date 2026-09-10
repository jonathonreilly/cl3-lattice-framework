---
claim_id: admissibility_d4_h1_port_free_neighbor_phase_m2_context_descent_boundary_bounded_theorem_note_2026-08-26
claim_type: bounded_theorem
claim_scope: "On the fixed Block-205 H1 L24 two-sector right-Schur family and the fixed Block-194 pointer orientation, summing all four coarse ports before readout gives a positive binary M2 law whose linear source response vanishes but whose exact cubic off-diagonal overlap is iC with C>0. For a source at the six nearest spatial displacements, the normalized cubic probability contrasts are (sqrt(3)kappa,-sqrt(3)kappa,2kappa,-2kappa,0,0), with kappa>0, so the phase-tagged port-free law varies on a finite positive analytic germ. The full 24-frame source, detector, and phase family is covariant. However, exact inverse-Fourier reconstruction has 110 forward and 110 actual-reverse Laurent terms with spatial matter and geometry support reaching L1 radius three, and the source depends on incoming p as well as transfer q. The proper-cubic Hom from six scalar neighbor contents to the required T2 shear is zero; only after conditionally assigning the Pauli-adjoint Bloch action does the Hom have dimension two, with no axiom-selected decoder. This is a positive phase-law theorem and a sharply localized context boundary, not a complete eta-to-M2 law, formation/history, an axiom amendment, obligation retirement, retained status, or TOE percentage movement."
claim_type_reason: "The cubic coefficient, positivity sign, six phase values, Laurent support, source collision, proper-cubic covariance, and Hom dimensions are exact finite-dimensional calculations. Analyticity and inherited strict Schur positivity give a nonzero positive germ. Standing remains bounded because actual neighboring M2 Record contents are not mapped to the source, the conditional internal/external action has two inequivalent decoder classes, the literal source is not a radius-one scalar shell, H2 remains sealed, and no formation or history law is supplied."
parent_commit: 8e6706c6077b718e5d424f8db8c0d6cc9143f17c
preregistration_commit: 725f490afe1f55e1fc2655784a29b9a1833ecbad
origin_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
fixture: H1
tt_column_zero_based: 1
port_free_neighbor_phase_germ: exact_positive_nonconstant_at_cubic_order
scalar_neighbor_to_t2_hom_dimension: 0
conditional_adjoint_m2_neighbor_to_t2_hom_dimension: 2
complete_nearest_neighbor_eta_law: false
axiom_amendment: none
obligation_retirement: 0
toe_percentage_movement: 0
independent_audit: unset
---

# H1 Port-Free Neighbor-Phase Law And M2 Context Boundary

**Date:** 2026-08-26

**Campaign block:** 206

**Type:** `bounded_theorem`

**Standing:** proposed bounded theorem; independent audit unset

Primary runner:
[`admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py`](../scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py).

Independent checker:
[`independent_admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py`](../scripts/independent_admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py).

## 1. Result Up Front

Block 206 finds a stronger positive law than Block 205.  The four coarse
detector ports can be summed **before** the pointer is read.  The resulting
binary law has no linear H1 response, but it is not constant: its first
surviving exact response is cubic in the source strength and is carried by
the source--detector phase.

Put the source at one of the detector's six nearest spatial neighbors.  In
direction order

```text
(+x,-x,+y,-y,+z,-z),
```

the exact cubic coefficients of `r_+ - r_-` are

```text
(sqrt(3) kappa, -sqrt(3) kappa,
 2 kappa,       -2 kappa,
 0,              0),                    kappa > 0.
```

Thus four conditions give nonzero response and the six conditions give five
distinct binary laws on one sufficiently small positive analytic germ.  No
coarse port is conditioned upon.  This is real campaign-local progress on
the probability/context seam.

It is not yet the Admissibility axiom's complete local law.  The calculation
still receives the H1 incoming momentum, transfer, TT shear, and relative
source phase as Fourier data.  Exact inverse Fourier and representation
checks show that the scalar six-neighbor shell cannot supply the shear, while
a conditional Bloch-`M2` shell supplies two possible decoder classes rather
than one physically selected decoder.

## 2. Frozen Construction

The immutable registration at `725f490afe` keeps:

- the Block-205 mass `2/7`, periodic `L=24` carrier, `12|12` cut, and
  ordinary-transpose right-Schur state;
- the literal forward and actual-reverse H1 second-TT source;
- incoming momentum
  `p=(pi/6,pi/3,0,pi/6)` and transfer
  `q=(pi/3,pi/2,0,0)`;
- the four Block-194 coarse events `E_st` and classified orientation `J`;
- the complete eight-effect PVM and its nonidentity pointer pullback; and
- the phase `phi=q.(x-x_src)` without effect fitting or a favorable port.

For unit phase `u=exp(i phi)`, summing over the four ports gives

\[
 P_\sigma(\phi)={1\over2}
 \begin{pmatrix}I&\sigma u^{-1}J\\
                 \sigma uJ&I\end{pmatrix},
 \qquad \sigma\in\{+1,-1\}.                    \tag{1}
\]

Because `J` is a Hermitian involution, `(P_+,P_-)` is a complete orthogonal
binary PVM for every tested phase.  It is exactly the sum of the four fixed
joint effects at that phase; no port selector remains in (1).

Let `G(e)` be the full reflected Schur Gram and `Z(e)=Tr G(e)`.  Its normalized
pointer probabilities and contrast are

\[
 r_\sigma(e,\phi)={\operatorname{Tr}(G(e)P_\sigma(\phi))\over Z(e)},
 \qquad
 \Delta(e,\phi)=r_+(e,\phi)-r_-(e,\phi).         \tag{2}
\]

## 3. Exact Cubic Coefficient

The runner derives the inverse and graph series directly from

\[
 A(e)Y(e)=I,
 \qquad
 P^T A(e)R(e)=0,                                  \tag{3}
\]

then forms every ordinary-transpose half-Gram term

\[
 H_n=\sum_{a+b+c=n}R_a^T Y_b R_c,
 \qquad G_n=H_n+H_n^\dagger.                     \tag{4}
\]

Write

\[
 a_n=\operatorname{Tr}((G_n)_{01}J).             \tag{5}
\]

The exact linear coefficient is `a_1=0`.  The cubic coefficient is

\[
 a_3=iC,\qquad
 C={343(A-B\sqrt3)\over D},                       \tag{6}
\]

where

```text
A = 39614194410521886011258608271189426608989637314061903595310837311299128766179775614039384849224874802424309955547840537519444031415731
B = 20088236778144933307422375844774848466973250848745230478668770773683346878595585928475405853707189945489158937323659388473013648683423
D = 14630373132760996204705386039773889549383195117366765668241345031835670611592246823650335399786716111445599465516368081316673691027954400
```

All three integers are positive, and the runner checks
`A^2 > 3 B^2`; hence `C>0` without a floating tolerance.  Numerically,
`C` is approximately `0.11301005367176628` only as a readability control.

The exact zero-source normalizer is positive.  Define

\[
 \kappa={C\over Z(0)}>0.                          \tag{7}
\]

Its readability value is approximately `0.000889700861213663`.  Since the
linear overlap vanishes, normalization cannot change the first nonzero term:

\[
 [e^3]\Delta(e,\phi)
 =2\operatorname{Re}(e^{i\phi}iC)/Z(0)
 =-2\kappa\sin\phi.                              \tag{8}
\]

For `x_src=x+delta`, `phi=-q.delta`.  Equation (8) gives exactly the six-entry
pattern in section 1.  Inherited strict positivity of `G(0)`, analytic finite
matrix inversion, and the nonzero rank-16 projectors (1) imply a sufficiently
small interval on which both probabilities remain strictly positive and sum
to one.  The nonzero cubic coefficient proves that the finite law, rather
than merely its tangent, varies with neighboring source direction.

The zero-phase cubic contrast vanishes because (6) is the orthogonal phase
quadrature.  No all-order zero claim is made or needed.

## 4. Translation And Proper-Cubic Covariance

The ordered H1 `(p,q)` pair has a 24-element proper-cubic orbit and trivial
stabilizer.  On all 24 frames the runner checks exactly:

- the transformed forward source equals the exterior-form conjugate of the
  original forward source;
- the actual-reverse source obeys the same covariance equation;
- simultaneous rotation preserves `q.delta` for every signed neighbor;
- the detector orientation and four-event context transform as their fixed
  families; and
- common translation of detector and source preserves `x-x_src`.

This is simultaneous source--detector covariance, not a free lookup between
two 24-element orbits.

## 5. Exact Inverse-Fourier Support And Collision

The parent centered action has an exact integer Laurent representation in
incoming matter variables `z=exp(ip)` and transfer variables `u=exp(iq)`.
Combining the frozen H1 TT coefficients before evaluation gives:

| object | Laurent terms | distinct spatial `(p,q)` supports | matter supports | geometry supports | max spatial matter L1 | max spatial geometry L1 |
|---|---:|---:|---:|---:|---:|---:|
| forward source | 110 | 78 | 38 | 26 | 3 | 3 |
| actual reverse `V(p+q,-q)` | 110 | 78 | 38 | 26 | 3 | 3 |

Every exponent is integral and lies inside the no-alias window on `Z_12^3`.
The geometry support is neither the six signed units nor radius-one-only.
This does not prove nonlocality of every factorized realization: a composition
of radius-one operations can have a wider effective stencil.  It does prove
that the literal source cannot simply be renamed as six scalar neighboring
values.

There is also an exact `q`-only collision.  Keep the H1 transfer fixed and
compare

```text
p  = (pi/6,pi/3,0,pi/6),
p' = (0,0,0,pi/6).
```

The two combined source vertices are different.  Therefore the six phase
values determined by `q` and `delta` do not reconstruct the action source;
incoming-mode information or its local real-space equivalent is required.

## 6. What Six M2 Neighbors Can Represent

The frozen TT polarization is the nonzero off-diagonal shear

\[
 h_{T2}=\begin{pmatrix}
 0&0&-1\\0&0&1/\sqrt2\\-1&1/\sqrt2&0
 \end{pmatrix},                                  \tag{9}
\]

with `(xy,yz,xz)` coordinates `(0,1/sqrt(2),-1)`.  It transforms in the
proper-cubic `T2` representation.

For six scalar or central neighbor contents, the exact intertwiner space is

\[
 \operatorname{Hom}_{O}(\mathbb R^{\{\pm x,\pm y,\pm z\}},T2)=0. \tag{10}
\]

So a scalar phase shell cannot linearly manufacture (9).

Conditionally let each neighboring traceless `M2` content transform as a
Bloch vector under the **same** spatial cubic rotation.  The domain is then
the signed shell tensored with the vector representation, and

\[
 \dim\operatorname{Hom}_{O}(\mathbb R^6\otimes T1,T2)=2.       \tag{11}
\]

The runner constructs two independent rank-three intertwiners.  If
`w_i=v_{+i}-v_{-i}` and `u_i=v_{+i}+v_{-i}`, one is the odd-shell symmetric
shear

```text
xy = -(w_x)_y -(w_y)_x
yz = -(w_y)_z -(w_z)_y
xz = -(w_x)_z -(w_z)_x,
```

and the other is the even-shell axis-difference shear

```text
xy = (u_x)_z -(u_y)_z
yz = (u_y)_x -(u_z)_x
xz = (u_z)_y -(u_x)_y.
```

Both are proper-cubic equivariant and surjective onto `T2`; they lie in
different shell-parity classes.  This is a constructive escape from the
scalar obstruction, not closure.  The minimal axioms supply the abstract
`M2(C)` domain but do not select a spatial action on its traceless part, one
of these two decoder classes, actual neighbor values, or a collision-free map
to the full forward/actual-reverse source.

## 7. Context And Axiom Decision

The campaign decision is now sharper:

```text
positive port-free phase law                 CLOSED on the H1 germ
proper-cubic/translation covariance          CLOSED on all 24 H1 frames
scalar six-neighbor source decoder           EXACTLY ABSENT in the linear class
conditional Bloch-M2 decoder existence       POSITIVE, two-dimensional
physical action-selected decoder             OPEN
literal radius-one eta source reconstruction OPEN
formation, permanence, and history           OPEN
```

No axiom amendment is justified yet.  The Admissibility axiom asserts that
one fixed nearest-neighbor rule exists; it does not promise that every chosen
Fourier action candidate realizes that rule.  A missing decoder is downstream
law content unless all factorized, nonlinear, and noncentral `M2` routes fail.
Nor do two conditional Hom classes establish two complete same-input physical
laws: neither has actual Record contents or a formation/history attachment.

If the next action-derived factorization cannot select a class and cannot
reduce the effective radius-three support to nearest-neighbor data, the exact
fork will be explicit: reject this H1 action family as the axiom's local law,
or propose an owner-approved enlargement of the supplied local context.  This
block does not cross that threshold.

## 8. No-Go Discipline N1--N8

### N1 -- alternative-route enumeration

| route | mechanism | status after Block 206 |
|---|---|---|
| port-free neighbor phase | cubic Schur quadrature | `POSITIVE` |
| action-selected Bloch decoder | odd/even Hom class fixed by source factorization | `OPEN` |
| nonlinear/noncentral M2 decoder | full six-record algebra rather than linear center | `OPEN` |
| multistep nearest-neighbor factorization | compose radius-one action factors to reproduce radius-three effective support | `OPEN` |
| wider finite local context | amend realization or, only if necessary, the supplied context radius | `OPEN` |
| alternative detector/event family | different source quadrature | `OPEN` |
| periodic `C32` type/Hom | typed positive periodic state/operator | `OPEN`, panel rank 2 |
| formation/history | action-derived instrument and permanent process | `OPEN` |
| gravity pincer | independent geometry--Record law | `OPEN`, separate PR stack |

No bounded negative absorbs these alternatives.

### N2 -- wall independence

The cubic probability result does not select a decoder.  The scalar Hom-zero
result does not constrain the conditional adjoint or nonlinear domains.  The
effective radius-three support does not rule out a factorization into
radius-one steps.  A decoder does not supply formation, and a one-shot law
does not supply history.  These walls remain independent.

### N3 -- hidden-wall scan

- `neighbor phase` means the supplied exact `q.delta`, not an inferred Record
  content.
- `M2` means the one-site algebra; the spatial action on its Bloch sphere is
  conditional here.
- `port-free` means the four coarse ports are summed before binary readout;
  it does not mean `p`, `q`, TT polarization, or source location were derived.
- `positive germ` uses the finite state family and openness, not a tangent
  treated as a state.
- `radius three` is inverse-Fourier support of the combined effective vertex,
  not a broad proof against composed local dynamics.

### N4 -- residual matching

| source | inherited result | use here |
|---|---|---|
| [Block 190 action/TT note](ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md) | centered action vertices and integer raw Laurent placement | exact source support and covariance |
| [Block 193 discriminator](ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) | literal two-sector source and Schur recurrence | exact cubic state coefficient |
| [Block 194 detector](ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) | fixed orientation, PVM, pointer, cubic family action | port-free phase effects and covariance |
| [Block 205 positive germ](ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_BOUNDED_THEOREM_NOTE_2026-08-26.md) | strict state positivity and analytic finite family | finite positive binary germ |
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | nearest-neighbor distribution and abstract M2 domain | exact closure criterion only |

### N5 -- execution resolution

per_element: checked both binary phase projectors, exact linear and cubic overlaps, six phase values, scalar and conditional-adjoint Hom classes, and the H1 shear coordinates.

per_site: checked the six signed source displacements and the distinction between supplied phase labels and actual neighboring M2 Record contents; no formation event is supplied.

per_mode: checked the fixed H1 incoming/transfer pair and a same-q/different-p collision; H2 remains sealed because full H1 eta reconstruction did not pass.

per_block: checked the full two-sector Schur recurrence, port-free C32 effect, raw forward/actual-reverse source, and M2 decoder domain as distinct typed objects.

lattice_wide: checked exact Z12 inverse-Fourier support and the full 24-frame simultaneous orbit; no full-Z3 history, gravity completion, retained theory, axiom edit, or TOE closure is claimed.

### N6 -- partial closure

The reusable positive chain is now

```text
literal H1 action/source
  -> strictly positive analytic right-Schur state
  -> complete eight-effect law and pointer
  -> sum over coarse ports
  -> exact cubic neighbor-phase binary M2 law.
```

The missing link is no longer “find any probability response.”  It is the
specific map from actual six-record contents to the source and one of the two
allowed `T2` decoders.

### N7 -- strongest hostile steelman

> A nearest-source phase is still a Fourier label.  The calculation does not
> show that six neighboring records contain `p`, `q`, or the TT shear.  The
> scalar shell cannot do so linearly, and the conditional Bloch shell has two
> equally covariant maps.  A radius-three effective source also fails the
> literal radius-one test unless it factors through local steps.  H2,
> formation, history, and independent retention are absent.

This objection is correct and fixes the standing.  It does not erase the
exact positive port-free cubic law.

### N8 -- cross-cycle echo

- Blocks 192--194 repaired the state/source/effect typing but left only a
  port-conditioned linear pointer response.
- Block 205 proved that this conditional response belongs to a finite positive
  probability germ.
- Earlier site-law campaigns found conditional M2 decoders without selecting
  their physical internal/external action.
- History blocks independently showed that a pointer instrument does not
  select a permanent process.
- The gravity pincer advances a different carrier and does not supply this
  H1 context map.

**N1--N8 disposition:** PASS for the exact H1 port-free neighbor-phase germ,
the scoped scalar-Hom boundary, and the conditional two-Hom classification;
FAIL for any broad local-law, Record/history, axiom, retained, or TOE closure
claim.

## 9. TOE And Obligation Accounting

| lane | before | after | reason |
|---|---:|---:|---|
| Records | 95 / 92 / 50 | 95 / 92 / 50 | port-free phase law advances the context seam; actual eta decoder and formation remain open |
| causal time | 76 / 72 / 41 | 76 / 72 / 41 | no inter-event process |
| matter | 95 / 96 / 75 | 95 / 96 / 75 | fixed H1 matter fixture, no generality retirement |
| gravity/source | 70 / 45 / 29 | 70 / 45 / 29 | one T2 source and context boundary, not full two-TT gravity |
| Born/history | 84 / 63 / 34 | 84 / 63 / 34 | positive varying binary law, but no complete eta/formation/history chain |

Formal obligation retirement remains zero.  The result is significant
campaign-local science progress, but the scored lanes move only when a named
end-to-end obligation is actually retired.

obligation retirement: 0

TOE percentage movement: 0

## 10. Highest-Leverage Successor

The next campaign should factor the exact 110-term source into its native
radius-one action pieces and push actual six-neighbor `M2` variables through
that factorization.  The decisive gate is whether the action itself selects
the odd-shell or even-shell intertwiner and reconstructs both forward and
actual-reverse sources without collisions.  Only after H1 passes that gate
should H2 be opened as the non-cubic held-out.

This is higher leverage than another detector scan: Block 206 has already
shown that a positive port-free law exists.  What blocks the TOE lane is now
the physical ownership of its context.
