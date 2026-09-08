---
claim_id: admissibility_dirac_signature_gravity_replacement_shortest_route_gate_boundary_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the supplied twenty-two-edge reflected carrier, the natural one-cell four-edge multi-affine Ward row is unique up to scale and translation and is exactly the Block-49 curvature row.  The unique exact common-line-metric compatibility row on that support is obtained by dividing its zero-momentum row by the line-average factor F(v dot q)=(exp(i v dot q)-1)/(i v dot q); it annihilates both the exact line-metric and displacement images and lifts all three relative shifts, but is non-Laurent, infinite-range, and singular where a diagonal v dot q reaches plus or minus 2 pi.  It also leaves the Block-75 constant-complement Dirac failure unchanged.  A scalar coefficient tuned to restore one Hamiltonian row at k=.4 loses it at k=.8 and has 318/728 negative static and 174/728 negative kinetic L=9 TT modes.  A shared three-section connection is gauge invariant but has axial TT rank one for every coefficient choice.  The smallest displayed six-section extension has TT rank two on all 728 nonzero L=9 modes, but equal connection norm is infrared anisotropic, its positive-face carrier is not signed proper-cubic complete, and flattening it supplies the existing ADM law in connection coordinates.  These results stop the tested same-support scalar and three-connection fitting routes and rank an exact local incidence-derivative ADM/Fierz--Pauli law, with Block-67 source and Block-53 TT quotient, as the next positive target.  This is partial-narrowing only: larger-support Laurent syzygies, changed carriers, non-Gram terms, genuine constraint/Palatini or Pachner laws remain live.  No selected gravity law, universal gravity no-go, axiom amendment, audit verdict, retention, obligation retirement, or TOE percentage movement is claimed."
upstream_dependencies:
  - minimal_axioms
  - admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_bounded_theorem_note_2026-08-11
  - admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_bounded_theorem_note_2026-08-11
  - admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_bounded_theorem_note_2026-08-13
  - admissibility_reflected_curvature_gravity_physical_reconstruction_cut_gate_boundary_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_dirac_signature_gravity_replacement_shortest_route_gate_boundary_2026_08_14.py
---

# Dirac-Signature Gravity Replacement Shortest-Route Gate Boundary

Status: partial-narrowing candidate; unaudited and unretained.

TOE accounting: zero TOE percentage movement and zero obligation retirement.
This packet changes the gravity portfolio ranking.  It does not promote a
parent, select a physical action, or amend the axioms.

## Result up front

The shortest repair is no longer another coefficient on the Block-74/75
raw-edge action.

Three exact facts force that decision.

1. On the natural four-edge cell, the local Ward row is unique and is already
   Block 49's row.  The exact row that instead annihilates the complete
   momentum-dependent line-metric image requires an inverse line-average form
   factor.  It is nonlocal and becomes singular at diagonal zone corners.
2. A coefficient can restore the missing Hamiltonian row at one momentum, but
   not at a held-out momentum or across the full TT zone.  The defect is a law
   and carrier problem, not a remaining one-number calibration.
3. Three shared connection sections cannot see the axial cross polarization.
   Six sections repair kinematic coverage, but then require an independently
   supplied constraint surface, connection metric, potential, signed cubic
   completion, source law, and cadence.  The natural exact flattening is just
   canonical ADM in connection coordinates.

The positive next target is therefore a local staggered/cochain
incidence-derivative ADM/Fierz--Pauli law.  It should accept Block 67's exact
incidence current directly, reduce to Block 53 on its TT quotient, and agree
with Block 44 in the infrared without demanding an exact all-zone inverse
line-metric dictionary.

## Inputs and non-imports

| input | used here | not imported |
|---|---|---|
| [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | the explicit boundary that Admissibility is not a dynamics axiom | gravity action, field carrier, signature, coupling, cadence, or selection |
| [Block 49](ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | exact reflected carrier, displacement map, line-metric map, and three curvature rows | a selected physical marginal or compatibility law |
| [Block 53](ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | lattice TT constraint and positive depth-two control | full Einstein constraints, source work, or a selected gravity law |
| [Block 67](ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md) | exact signed Record-incidence current and full `T00/T0i/Tij` target | physical source typing, cadence, normalization, or Bianchi intertwiner |
| [Block 75](ADMISSIBILITY_REFLECTED_CURVATURE_GRAVITY_PHYSICAL_RECONSTRUCTION_CUT_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md) | complete-edge Dirac, pole, canonical, and connection residuals | a universal canonical/connection no-go |

The current packet is a route discriminator.  Every new action discussed below
remains a candidate law rather than axiom authority.

## 1. Unique minimal Ward row

Fix one spatial axis `i`, write

\[
 z_i=e^{iq_i},\qquad z_t=e^{iq_t},
\]

and use the four stored directions

\[
 S_i=\{e_i+e_t,e_i-e_t,e_i,e_t\}.
\]

The natural one-cell ansatz has row coefficients

\[
 [\sqrt2 a,\ \sqrt2 z_t b,\ c_0+c_tz_t,\ d_0+d_iz_i].
\]

Exact annihilation of the `xi_i` and `xi_t` displacement columns gives

\[
 a(z_iz_t-1)+b(z_i-z_t)+(c_0+c_tz_t)(z_i-1)=0,
\]

\[
 a(z_iz_t-1)-b(z_i-z_t)+(d_0+d_iz_i)(z_t-1)=0.
\]

Coefficient matching in `1,z_i,z_t,z_iz_t` has a one-dimensional kernel,

\[
 (a,b,c_0,c_t,d_0,d_i)=(1,1,-1,-1,-1,-1).
\]

Thus, up to translation and scale,

\[
 D_i(q)=
 [\sqrt2,\sqrt2 z_t,-(1+z_t),-(1+z_i)].
\]

After the common cell-center phase this is precisely Block 49's row.  There is
no unused coefficient at the same support and range.

## 2. Exact compatibility exists, but is not a local replacement

For a stored edge direction `v`, the exact line-average metric map factors as

\[
 M_v(q)=F(v\cdot q)A_v,
 \qquad
 F(x)=\frac{e^{ix}-1}{ix},
\]

where `A_v` is the constant metric contraction.  Let `R=D(0)`.  Since
`RA=0`, the unique row in the same four-edge kernel is

\[
 C(q)=R\,\operatorname{diag}_v F(v\cdot q)^{-1}.
\]

For row `i`, its four coefficients are

\[
 \left[
 \frac{\sqrt2}{F(q_i+q_t)},
 \frac{\sqrt2}{F(q_i-q_t)},
 -\frac2{F(q_i)},
 -\frac2{F(q_t)}
 \right].
\]

The runner verifies at generic, axial, and mixed probes that

\[
 C(q)M(q)=0,\qquad C(q)G(q)=0,
\]

to below `5e-15`, and that `C(0)` maps the three relative shifts with singular
values `(2,2,2)`.

This exact result is not a finite-range rescue.  On `q_t=0`, the coefficient
ratio `C_t/C_+` contains `F(q_i)`.  A finite-range row would make such a ratio
rational and periodic in `z_i`; `F(q_i+2pi)` is not equal to `F(q_i)` on an
open set.  Moreover, diagonal directions can reach `v dot q=plus or minus
2pi`, where `F=0` and the inverse row has a pole.  This proof is limited to the
declared four-edge kernel.  Larger supports may combine factors differently.

## 3. Compatibility does not supply a Hamiltonian constraint

At `q=(.4,0,0,0)` and `mu=1/1024`, the complete Block-75 constant-complement
Dirac reduction remains

\[
 \operatorname{rank}(Q,N^TQN,E,E_{aa},K)=(18,12,6,3,3).
\]

Its inertias are

\[
 E:(4-,2+,4\,0),\quad
 E_{aa}:(2-,1+,1\,0),\quad
 K:(2-,1+,3\,0).
\]

There is only the gauge temporal null and no Hamiltonian-constraint row.
Replacing a kinematic coordinate dictionary does not change this action
result.

A hostile scalar foil makes the distinction concrete.  The runner derives the
root of the `k=.4` lapse-entry equation on `[-.20,-.15]`; it is

\[
 \mu=-0.1765289805547723
\]

It gives `rank Eaa=2` and one nonzero Hamiltonian row at `k=.4`, with constraint
norm `0.0567693`.  At `k=.8`, the third temporal eigenvalue is
`-0.00408197237`, `rank Eaa=3`, and the constraint disappears.  Its complete
nonzero `L=9` TT census has

\[
 318/728\ \text{negative static modes},\qquad
 174/728\ \text{negative kinetic modes},
\]

with minima below `-40` and `-1000`.  This is a one-mode hostile foil, not a
physical fit and not a theorem about momentum-dependent, matrix-valued, or
larger-support actions.

## 4. Shared three-section connection obstruction

For a spatial direction `v` and time direction `t`, define

\[
 T_v^+=\sqrt{|v|^2+1}\,\ell_{v+t}
 -|v|\ell_v-e^{ik\cdot v}\ell_t,
\]

\[
 T_v^-=\sqrt{|v|^2+1}e^{iq_t}\ell_{v-t}
 -|v|e^{iq_t}\ell_v-\ell_t.
\]

After their common center phase,

\[
 T_v^+G=-T_v^-G.
\]

A shared compensator with that gauge variation therefore makes
`A_v^+=T_v^+ ell-c_v` and `A_v^-=T_v^- ell+c_v` gauge invariant.  Their sum
returns the existing `D_v` marginal; their difference is the natural
connection-velocity channel.

For only `v=x,y,z`, every one of these rows annihilates the cross tensor
`h_yz` on an `x`-axis momentum.  The runner obtains axial TT singular values
`(.25,0)`.  No coefficient or connection norm can create a missing carrier
representation.  A genuinely first-order law would additionally need a
newly supplied symplectic term.

## 5. Six sections repair coverage, not law selection

The smallest displayed coverage extension is

\[
 V_6=\{x,y,z,x+y,x+z,y+z\}.
\]

Its metric-velocity map is

\[
 W_v(k)h=w(k\cdot v)v^Thv,
\]

\[
 w(a)=\frac14\operatorname{sinc}(a/2)
 +\frac1{4i}\operatorname{sinc}'(a/2).
\]

In Frobenius coordinates `(xx,yy,zz,sqrt2 xy,sqrt2 xz,sqrt2 yz)`, the
directional-contraction matrix is

\[
 R=\begin{pmatrix}
1&0&0&0&0&0\\
0&1&0&0&0&0\\
0&0&1&0&0&0\\
1&1&0&\sqrt2&0&0\\
1&0&1&0&\sqrt2&0\\
0&1&1&0&0&\sqrt2
\end{pmatrix},
\qquad \det R=2\sqrt2.
\]

The scalar `w(a)` has no real zero.  The runner verifies two nonzero TT
singular values on every one of the 728 nonzero `L=9` modes, with minimum
`0.129271995`.

This is kinematic coverage only.  Equal connection norm gives the infrared TT
mass eigenvalues

| ray | eigenvalues |
|---|---|
| axis | `(1/8,1/8)` |
| face diagonal | `(1/16,1/8)` |
| body diagonal | `(1/24,1/24)` |

The six positive face directions are permutation-covariant but not complete
under signed proper-cubic rotations at finite momentum.  Adding the missing
negative face diagonals or averaging frames is another carrier/action input.

Choosing a dense connection metric to flatten `W_6`, together with the
Block-53 trace/divergence surface and `V=kappa^2 I`, reduces through
`pi=W_6^dagger c` to the existing canonical ADM Hamiltonian.  It is a useful
coordinate construction, but does not derive a new law.  Keeping the
Block-74/75 static potential instead preserves its `276/728` negative modes.

## 6. Positive route selected for the next experiment

The next runner should use coordinate incidence derivatives

\[
 D_mu(q)=e^{iq_mu}-1
 =i e^{iq_mu/2}\,2\sin(q_mu/2),
\]

with fields placed on the corresponding half-cells.  This avoids an inverse
diagonal-edge line factor.  Its hard gates are:

1. real Hermitian finite-range action and proper-cubic/time-reflection maps;
2. exact Ward and contracted-Bianchi identities at every finite-grid mode,
   including UV corners;
3. nondynamical lapse/shift, four constraints/gauge directions, and exactly
   two positive TT pairs;
4. exact acceptance of all six Block-67 signed axial source rays, including
   the odd `T0i` and even `T00/Tij` sectors;
5. a TT quotient equal to Block 53, including its positive depth-two update;
6. sourced-constraint propagation, a positive Newton sign, and explicit
   failure of nonconserved/deletion mutants;
7. no inverse form factor or pseudoinverse in the law or source assembly.

A pass would retire a scoped *existence* seam only after independent retention.
Selection, state ontology, source energy debit, cadence, coupling, nonlinear
closure, and full TOE composition would remain.

## No-Go Discipline Gate

### N1 -- Alternative Route Enumeration

| route | status |
|---|---|
| same four-edge scalar Ward repair | attempted; exact uniqueness returns Block 49 |
| exact common-metric compatibility | attempted; exists, but inverse-line-factor nonlocal/singular and does not repair Dirac |
| scalar momentum-dependent weights | untested beyond the displayed constant one-mode foil; broad fitting is stopped, not excluded |
| three-section shared Palatini connection | attempted; exact axial cross-TT coverage obstruction |
| six-section connection | attempted positively; covers TT but imports metric, constraints, potential, cubic completion, and law selection |
| larger-support Laurent syzygy | untested and live |
| changed local metric interpolation/carrier | untested and live; incidence ADM is the next target |
| non-Gram cross terms | untested and live |
| genuine Lagrange-multiplier/Palatini compatibility | untested beyond the displayed shared algebraic connection |
| Pachner/tent canonical constraint evolution | untested and live |

### N2 -- Wall-Independence Audit

Locality and Dirac signature are independent.  The exact nonlocal `C(q)`
closes `CM=0`, yet the `Eaa` rank and Hamiltonian row still fail.  TT coverage
and physical law selection are also independent: `W6` closes the former while
leaving the latter open.

### N3 -- Hidden-Wall Scan

The uniqueness theorem assumes the displayed four-edge support and
one-cell/multi-affine coefficient class.  The compatibility result assumes the
Block-49 line metric.  The Dirac comparison uses Block 75's constant
complement.  The scalar negative covers only the displayed constant and
quadratic weights.  The six-section coverage uses its stated positive face
directions and Block-53 lattice TT rows.

### N4 -- Residual Matching

Block 75 witnesses only the identical constant-complement Dirac and static
residuals used here.  Its broader canonical and connection cuts are not
relabelled as proofs of the present minimal-support statements.  Block 53 is
used only as the positive TT control, and Block 67 only types the next source
target.

### N5 -- Rhetoric And Resolution Audit

The Ward and compatibility identities are exact per row.  The connection
coverage and scalar signs are complete only on the declared 728-mode `L=9`
census.  No continuum, arbitrary-lattice, nonlinear, or universal no-go is
inferred.

### N6 -- Partial-Closure Path Scan

A larger-support local syzygy could retire the inverse-factor wall.  A changed
carrier could retire the line-average ownership entirely.  A supplied
constraint law could make a first-order connection physical.  These are live
import-retirement paths, not automatic reasons to amend an axiom.

### N7 -- Steelman

The strongest escape is a larger-support Laurent compatibility row whose
several edge directions cancel the nonperiodic line factors.  It is actionable
and untested.  Independently, a direct incidence-derivative Fierz--Pauli law
can be local without ever inverting the line map.  Therefore this result is
partial-narrowing, never a gravity no-go.

### N8 -- Cross-Cycle Echo

Block 75 found that exact-marginal auxiliary rewriting inherited the same bad
transfer.  The current connection coverage problem is different: it asks
whether the carrier sees both TT polarizations before a marginal is chosen.
Neither result retires the other.  The repeated lesson is to gate carrier,
constraint, positivity, source, and selection separately.

No-Go Discipline Gate status: PASS for the narrow family cut and portfolio
decision.  It does not authorize a global negative.

## Reproduction

```bash
python3 scripts/admissibility_dirac_signature_gravity_replacement_shortest_route_gate_boundary_2026_08_14.py
```

The runner ends with the canonical `TOTAL: PASS=n FAIL=n` line.  Nine named
mutations target uniqueness, compatibility locality, the inverse-factor pole,
the Dirac gate, one-mode fitting, shared-connection gauge signs, six-section
coverage, connection-law promotion, and scope promotion.

Source-identity-pinned evidence: [cached runner stdout](../logs/runner-cache/admissibility_dirac_signature_gravity_replacement_shortest_route_gate_boundary_2026_08_14.txt).
