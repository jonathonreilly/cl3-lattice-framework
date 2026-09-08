---
claim_id: admissibility_counterpropagating_scalar_bianchi_trace_shear_energy_current_exchange_boundary_bounded_theorem_note_2026-08-14
claim_status: unretained
claim_type: bounded_theorem
claim_scope: "For the actual Block95 nearest-neighbour massless scalar, one explicit site energy and oriented bond current satisfy an off-shell local continuity identity and equal the Block95 Ttt/Tti coefficients on all 247 exact L=3 through L=8 shell modes. An equal-amplitude L=5 counterpropagating pair has q=0 density and longitudinal stress plus compulsory q=plus/minus 4pi/5 density interference; the latter have exact Block78 inhomogeneous Hamiltonian-constraint solutions. The q=0 stress decomposes into one trace and one axisymmetric shear under the actual Block78 DeWitt map. For fixed positive coupling g, the Block95 interaction gradient supplies a reduced trace-shear Hamiltonian jet with exact constrained continuous flow whose half-tick momentum impulse equals the Block78 front kick. On both real volume-momentum branches, at fixed g, that same matter-energy jet cancels the complete order-A^3 frozen-source endpoint defect and leaves an exact order-A^4 residual. The result does not construct S_g3, S_phi2, R1, D1, the full order-h phi^2 Ward identity, a common nonlinear lattice action, a total discrete Noether energy, full-Z3 control, a Record compiler, law selection, audit retention, obligation retirement, or TOE percentage movement. Block78 does not select the sign or value of g. No gravity no-go or axiom amendment is inferred."
depends_on:
  - admissibility_boundary_dressed_joint_stage_homogeneous_nonlinear_zero_mode_boundary_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14.py
---

# Counterpropagating Scalar Bianchi Target: Trace–Shear, Energy Current, and Leading Exchange Cancellation

Date: 2026-08-14

Campaign block: 97

Status: positive bounded theorem plus a sharply named quartic construction wall

Retention status: proposed only; no audit verdict

## 1. Result

This block executes the one coupled gravity viability experiment required
after Block 96.  It obtains four positive results on the actual Block 95/78
carrier:

1. the Block 95 density and current of every exact free scalar plane wave are
   exactly the density and bond flux of one local discrete energy continuity
   law;
2. an equal-amplitude counterpropagating L=5 pair has a positive homogeneous
   density and longitudinal stress, while its two compulsory
   q=plus/minus 4pi/5 density components remain present and solve the
   inhomogeneous Block 78 Hamiltonian constraints;
3. the homogeneous source fits one trace pair and one axisymmetric shear pair
   under the actual Block 78 DeWitt map, and the Block 95 interaction gradient
   gives a common reduced constrained Hamiltonian flow;
4. on both volume-momentum branches, the matter-energy jet cancels the entire
   order-A^3 defect produced by treating the source as frozen during one
   Block 78 front step.  The remaining residual is exactly order A^4.

This is material route progress.  It says the first nonlinear exchange
coefficient has the right sign and magnitude on a source that includes genuine
background-to-inhomogeneous mixing.  It does not retire a TOE obligation.  The
quartic residual still has to be derived from one common bounded-local joint
action, not assigned to a bookkeeping reservoir.

The exact local energy/current theorem is for the free scalar.  The reduced
trace–shear Hamiltonian jet is not the full joint lattice action.  Full
order-h phi^2 Ward completion remains open.  Total discrete Noether energy
remains open.  The Record compiler, law selection, and independent retention
remain open.

## 2. Authority and dependency chain

The current authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
origin/main eee6ab5874e2fc207db5526dc82d9f71ae550c7c and axiom blob
bc23300becfe4e4db57153c0e94cfcdf2338da71.

The immediate parent is
[Block 96](ADMISSIBILITY_BOUNDARY_DRESSED_JOINT_STAGE_HOMOGENEOUS_NONLINEAR_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md),
which supplies the endpoint-dressed interpretation of the Block 78 front
cadence and the positive nonlinear homogeneous volume-momentum branch.

The actual matter stress, interaction gradient, recoil, and first-order Ward
cochain come from
[Block 95](ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md).
The canonical constraints and two-half-step update come from
[Block 78](ADMISSIBILITY_INCIDENCE_ADM_DEPTH_TWO_SOURCED_CONSTRAINT_RECORD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md).
The distinction between a field-work shadow and a total joint energy is kept
from
[Block 79](ADMISSIBILITY_CYCLE713_RECORD_HEAD_ADM_WORK_ARCHIVE_STATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md).

The executable certificate is
[admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14.py](../scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14.py).
It recursively content-binds the complete Block 96 parent authority chain.

## 3. Exact free-scalar local energy/current cochain

Let the positive spatial lattice Laplacian be

\[
 (L_s\phi)_x=\sum_i(2\phi_x-\phi_{x+e_i}-\phi_{x-e_i}),
\]

and let the free scalar equation at integer time n be

\[
 {\cal E}_{n,x}=
 \phi_{n+1,x}-2\phi_{n,x}+\phi_{n-1,x}+(L_s\phi_n)_x=0.
\]

Define the forward spatial difference and centered temporal velocity by

\[
 d_i\phi_{n,x}=\phi_{n,x+e_i}-\phi_{n,x},
 \qquad
 u_{n,x}={\phi_{n+1,x}-\phi_{n-1,x}\over2}.
\]

The site energy assigned to the interval from n to n+1 is

\[
 e_{n,x}={1\over2}|\phi_{n+1,x}-\phi_{n,x}|^2+
 {1\over2}\sum_i
 {\rm Re}\!\left[
   \overline{d_i\phi_{n,x}}\,d_i\phi_{n+1,x}
 \right],
\]

and the oriented bond current is

\[
 j_{n,i}(x+\tfrac12e_i)=-
 {\rm Re}\!\left[
   \overline{d_i\phi_{n,x}}\,u_{n,x+e_i}
 \right].
\]

Direct expansion and a single nearest-neighbour summation-by-parts identity
give the off-shell pointwise relation

\[
 e_{n,x}-e_{n-1,x}
 +\sum_i\left[j_{n,i}(x+\tfrac12e_i)
              -j_{n,i}(x-\tfrac12e_i)\right]
 ={\rm Re}\!\left[\overline{u_{n,x}}\,{\cal E}_{n,x}\right].
 \tag{1}
\]

Thus the spatial sum of e is exactly conserved on shell on every periodic
finite lattice.  This is stronger than a plane-wave comparator: it is a
local off-shell cochain identity for arbitrary complex fields.

For the repo convention

\[
 \phi_{n,x}=A\exp[-i(k\mathbin{\cdot}x+\omega n)]
\]

on the exact massless shell

\[
 4\sin^2(\omega/2)=4\sum_i\sin^2(k_i/2),
\]

equation (1) gives

\[
 {e\over |A|^2}=\sin^2\omega,\qquad
 {j_i\over |A|^2}=-\sin\omega\,\sin k_i.             \tag{2}
\]

At zero transfer, the Block 95 centered derivative is

\[
 d_\mu=(\sin k_1,\sin k_2,\sin k_3,-\sin\omega),
\qquad T_{\mu\nu}=d_\mu d_\nu.
\]

Therefore equation (2) is exactly

\[
 e/|A|^2=T_{tt},\qquad j_i/|A|^2=T_{ti}.
\]

The runner checks the local off-shell identity on 48 random complex fields,
global on-shell conservation, and the equality to Block 95 Ttt and Tti on all
247 exact shell modes:

| L | exact shell modes |
|---:|---:|
| 3 | 13 |
| 4 | 28 |
| 5 | 25 |
| 6 | 68 |
| 7 | 37 |
| 8 | 76 |

This closes the free scalar energy-current bridge only.  It does not yet
provide the time-translation Noether charge of a dynamical geometry–matter
action.

For a coherent superposition, the site representative e in equation (1) is
not pointwise identical to the inverse-metric source density reconstructed
from all Block 95 Ttt transfer coefficients.  Their spatial sums, hence their
q=0 charges, agree for the standing-wave fixture, but an improvement term
redistributes the nonzero-q density.  Standing-wave local energy improvement
and interference matching remain open and belong in the joint Noether
construction.  The runner independently requires both the equal spatial
charges and a nonzero pointwise improvement.

## 4. Full L=5 counterpropagating source

Take the two exact massless modes

\[
 k_+=(2\pi/5,0,0,2\pi/5),\qquad
 k_-=(-2\pi/5,0,0,2\pi/5)
\]

with equal complex amplitude A.  Put s=sin(2pi/5).  The source coefficient at
transfer q is computed from the actual Block 95 vertex,

\[
 T_{\mu\nu}(q)=
 \sum_{k_{\rm out}-k_{\rm in}=q}
 \overline{A_{k_{\rm out}}}A_{k_{\rm in}}\,
 t_{\mu\nu}(q,k_{\rm in}).
 \tag{3}
\]

No cross term is discarded.  Equation (3) has exactly three nonzero Fourier
components:

| transfer | density rho | current j | spatial stress tau |
|---|---:|---:|---:|
| q=0 | 2 times |A| squared times s squared | 0 | 2 times |A| squared times s squared times e_x e_x |
| q=+4pi/5 e_x | |A| squared times s squared | 0 | 0 |
| q=-4pi/5 e_x | |A| squared times s squared | 0 | 0 |

The two cross components are compulsory background-to-inhomogeneous mixing.
In position space,

\[
 \rho_x=4|A|^2s^2\cos^2(2\pi x/5)\geq0.              \tag{4}
\]

The q and minus-q coefficients are conjugates.  Their current vanishes and
their spatial stress vanishes, so their exact source Ward equations hold.

The special L=4 quadrature-phase fixture used in the earlier search is
intentionally not used here: its cross transfer aliases to the self-inverse
q=pi sector and its chosen relative phase cancels that coefficient, making
that particular source homogeneous.  An equal-phase L=4 pair instead leaves
one real q=pi density sector and is not homogeneous, but it collapses the
distinct plus-q and minus-q checks.  L=5 avoids both the phase cancellation
and the self-inverse alias.

## 5. Constraint embedding: trace, shear, and interference density

Define the normalized axisymmetric traceless tensor

\[
 Q={1\over\sqrt6}{\rm diag}(2,-1,-1),\qquad
 Q:Q=1,\qquad {\rm tr}\,Q=0.
\]

Use homogeneous canonical coordinates

\[
 h=\alpha I+\sigma Q,\qquad
 \pi={p_\alpha\over3}I+p_\sigma Q.
\]

The actual Block 78 DeWitt map gives

\[
 {1\over2}\pi:G\pi=-{p_\alpha^2\over12}
                   +{p_\sigma^2\over2}.             \tag{5}
\]

The q=0 source decomposes exactly as

\[
 \tau=\rho\left({I\over3}+\sqrt{2\over3}Q\right).
 \tag{6}
\]

A trace-only model misses

\[
 \tau_{\rm TF}=\rho\,{\rm diag}(2/3,-1/3,-1/3),
 \qquad \|\tau_{\rm TF}\|_F=\rho\sqrt{2/3}.           \tag{7}
\]

One shear pair is sufficient for this source.  Extra independent shear
coordinates are not needed for the axisymmetric fixture.  Shear is an
evolution equation here, not an additional ADM constraint.

For each cross transfer q=plus/minus 4pi/5 e_x, the lattice momentum obeys

\[
 p(q)^2=4s^2.
\]

The exact Block 78 inhomogeneous solution is

\[
 h_{yy}(q)=h_{zz}(q)={g|A|^2\over8},\qquad
 \pi(q)=0.                                           \tag{8}
\]

Indeed,

\[
 {\cal H}h=p(q)^2(h_{yy}+h_{zz})
           =g|A|^2s^2=g\rho(q),
\]

and all three momentum constraints vanish with j(q)=0.  Equations (6)–(8)
show why neither the homogeneous shear nor the interference density may be
silently removed.

## 6. Common reduced Hamiltonian jet

For the q=0 source, the spatial part of the actual Block 95 interaction is

\[
 H:T=2h:\tau.
\]

Consequently its Hamiltonian energy jet in the trace–shear chart is

\[
 E_{\rm lin}(\alpha,\sigma)
 =1-{2h:\tau\over\rho}
 =1-2\alpha-2\sqrt{2/3}\,\sigma.                    \tag{9}
\]

The runner obtains both derivatives of equation (9) by complex-step
differentiation through the Block 95 interaction-metric function.  They are
not inserted as a separate source rule.

Fix a positive coupling g, and let

\[
 r=g\rho,\qquad q_s=\sqrt{2/3}.
\]

The reduced common constraint is

\[
 C_B=-{p_\alpha^2\over12}+{p_\sigma^2\over2}
       +r(1-2\alpha-2q_s\sigma).                    \tag{10}
\]

At alpha=sigma=p_sigma=0, both branches

\[
 p_{\alpha0}=\pm\sqrt{12r}
\]

solve C_B=0.  Hamilton's equations have the exact solution

\[
 p_\alpha(t)=p_{\alpha0}+2rt,\qquad
 p_\sigma(t)=2rq_st,
\]

\[
 \alpha(t)=-{p_{\alpha0}t\over6}-{rt^2\over6},
 \qquad
 \sigma(t)=rq_st^2.                                 \tag{11}
\]

Substitution gives C_B(t)=0 identically.  The runner independently integrates
the Hamilton vector field derived from equation (10), checks both signs over
64 logarithmically distributed source scales, and recovers equation (11).

At the Block 78 half-step duration delta=1/2,

\[
 \Delta p_\alpha=r,\qquad
 \Delta p_\sigma=rq_s,                              \tag{12}
\]

which is exactly the decomposition of the actual front kick
\(\Delta\pi=g\tau\).  The coordinate path in equation (11) is not the same as
the Block 78 symplectic-Euler coordinate path.  The runner measures and
requires this nonzero chart gap; only the momentum impulse is identified.

## 7. Leading discrete exchange cancellation

Start the Block 78 front step at

\[
 \alpha_0=\sigma_0=p_{\sigma0}=0,\qquad
 p_{\alpha0}=\pm\sqrt{12r}.
\]

After the front momentum kick and one half-step drift,

\[
 p_{\alpha1}=p_{\alpha0}+r,\qquad
 p_{\sigma1}=rq_s,
\]

\[
 \alpha_1=-{p_{\alpha0}+r\over12},\qquad
 \sigma_1={rq_s\over2}.                             \tag{13}
\]

If the matter energy is frozen at r, the endpoint constraint defect is

\[
 \Delta C_{\rm frozen}
 =-{p_{\alpha0}r\over6}+{r^2\over4}.                \tag{14}
\]

At fixed positive g, r is proportional to A squared and p_alpha0 is
proportional to A, so equation (14) starts at order A^3.  Block 78 does not
select the sign or value of g; the real two-branch theorem here assumes g>0.

The Block 95 matter-energy jet changes the source contribution by

\[
 r[E_{\rm lin}(\alpha_1,\sigma_1)-1]
 ={p_{\alpha0}r\over6}-{r^2\over2}.                 \tag{15}
\]

Adding equations (14) and (15) gives

\[
 \Delta C_{\rm joint\ jet}=-{r^2\over4}.            \tag{16}
\]

Thus the complete branch-dependent order-A^3 coefficient cancels on both
signs of p_alpha0.  The remaining defect is order A^4.  The runner checks 128
random amplitudes and couplings and independently fits the amplitude orders:
the frozen residual has order 3 and the joint-jet residual has order 4.

Equation (16) is positive route evidence, not conservation of a finished
joint step.  It tells us exactly where the next coefficient must live.

## 8. The quartic construction wall

The minimal target remains one joint bounded-local action of the schematic
form

\[
 S=S_{g2}+S_{g3}+S_{\phi0}+gS_{\phi1}+gS_{\phi2}
   +\sum_n(F_{n+1}-F_n).                             \tag{17}
\]

Blocks 77/78 supply the quadratic gravity sector S_g2.  Block 95 supplies
S_phi0 and S_phi1.  Block 96 supplies the boundary generator F.  The missing
order-A^4 terms are:

- the seagull S_phi2;
- cubic gravity S_g3;
- the compulsory q=plus/minus 2k interference-sector energy;
- the order-h gauge and matter generators conventionally denoted R1 and D1;
- the exact temporal Noether terms of the same discrete action.

The next Ward coefficient equations are

\[
 \delta_0S_{g3}+\delta_1S_{g2}=0,
\]

\[
 \delta_0^hS_{\phi2}+\delta_1^hS_{\phi1}
 +\delta_0^\phi S_{\phi1}+\delta_1^\phi S_{\phi0}=0.
 \tag{18}
\]

They must be solved on a declared finite support ladder.  The Hamiltonian and
momentum constraints and the energy law must then be variations of that same
action.

For a time-node or lapse-varying discrete action, the defensible total energy
has the form

\[
 E_{{\rm tot},n}=-\partial_{\Delta_n}L_{{\rm joint},n}.
 \tag{19}
\]

It requires all discrete Euler–Lagrange equations, lapse and shift
constraints, and the time-node equation relating adjacent step-duration
derivatives.  The Block 79 field shadow plus a formal battery is not equation
(19).  Total discrete Noether energy remains open.

## 9. Decisive next experiment and stop rule

The highest-leverage next gravity experiment is now narrower:

1. enumerate the smallest proper-cubic finite support for S_g3, S_phi2, R1,
   and D1 that contains the Block 95 support;
2. form the exact Laurent coefficient system for equations (18);
3. include q=0 and both q=plus/minus 4pi/5 source sectors in the same solve;
4. derive, rather than append, the time-node Noether equation;
5. run rank, consistency, covariance, and hostile-deletion checks.

A consistent solution is the shortest current route to a first same-carrier
nonlinear-order viability witness.  It would remain a candidate deformation,
not all-order constraint closure or a selected gravity law.  An inconsistent
coefficient system rejects only that declared support and carrier.  It does
not reject gravity.

The portfolio stop rule is explicit: if the next block produces only another
comparator, census, or prescribed-source identity without solving or
falsifying one complete coefficient system, stop the gravity seam and pivot
to the broader typed-event/Record-law confluence seam.

## 10. Scope and TOE accounting

This block has zero obligation retirement.  No TOE percentage moves.  The
retained-positive end-to-end theory count remains zero.

It does not establish:

- the full order-h phi^2 Ward identity;
- a nonlinear lattice constraint algebra;
- the total joint discrete Noether energy;
- full-Z3 or increasing-region control;
- a Lorentzian causal Record update selected by the axioms;
- a Record compiler or law-selection theorem;
- independent retained status.

The Record compiler, law selection, and independent retention remain open.
No axiom amendment is forced.  The result positively localizes a missing
construction; it does not show that the present axioms are insufficient.

## 11. No-go discipline N1–N8

The normalized negative target is:

> The order-A^4 residual in equation (16) proves that no admissible
> bounded-local gravity completion can conserve the joint energy or satisfy
> the nonlinear Ward identity.

That target is not established.

### N1 — alternative-route enumeration

| normalized route | status in this block | retained-authority failure citation |
|---|---|---|
| finite-support metric seagull and cubic-action solve | ATTEMPTED only through the reduced order-A^3 jet; the full coefficient solve is not executed | none |
| expanded bounded-support metric action | not attempted | none |
| tetrad, Palatini, or BF carrier | not attempted | none |
| Regge or dynamical-source discretization | not attempted | none |
| refinement or perfect-action route | not attempted | none |
| alternative variational cadence | not attempted beyond the Block 96 boundary chart | none |
| scalar-clock deparameterization | not attempted | none |

There are not five in-contract failed routes with retained-authority
citations.  N1 status: FAIL.

### N2 — wall-independence audit

The observed wall is not route-independent.  Equation (16) omits precisely
the seagull, cubic-gravity, interference, and time-node terms that several
listed routes introduce differently.  The present residual cannot be lifted
from the metric support used here to any other carrier or cadence.

### N3 — hidden-wall scan

Potential hidden walls still include support width, component staggering,
finite-torus aliasing, gauge-transformation order, time-node placement,
boundary flux, and background choice.  The L=5 choice removes the special
L=4 alias but does not resolve the other walls.

### N4 — residual matching

The residual is not an unnamed mismatch.  Its exact coefficient is minus
r squared over four.  Its amplitude valuation is four.  Its compulsory
Fourier companions are q=plus/minus 2k.  These data map directly to the
missing terms in equations (17)–(18), so they define a constructive target.

### N5 — resolution audit

- per-element: exact site energy, link current, trace projection, shear
  projection, and both momentum branches are checked;
- per-site: equation (1) is local, but the full nonlinear joint density is not
  built;
- per-mode: 247 free shell modes and all three standing-source transfers are
  checked;
- per-block: the reduced flow and one front-step exchange are checked;
- lattice-wide: full-Z3 control, nonlinear Ward gluing, Record compilation,
  selection, and retention are unexecuted.

Failure at lattice-wide resolution cannot be inferred from success or a
remainder at the lower resolutions.

### N6 — rhetoric audit

Permitted language is: the frozen-source splice fails at order A^3, the
Block 95 jet cancels that term, and a named order-A^4 construction remains.
Forbidden language is: gravity cannot work, the axioms exclude gravity, or
the quartic term is impossible.

The residual rejects neither bounded-local gravity nor the current axioms.

### N7 — strongest steelman

The strongest steelman is a same-carrier finite-support solve of equations
(17)–(18), with the exact L=5 interference source and independently varied
time-node durations.  It is concrete, compatible with the current axioms,
and directly targets the remaining coefficient.  It has not failed.

N7 status: FAIL.

### N8 — cross-cycle echo

The cross-cycle echo is cautionary.  Block 95 exposed a positive compact
linear residual; Block 96 showed that a nonlinear homogeneous
volume-momentum branch resolves its broad interpretation.  Block 96 then
left a stage-work wall; this block shows reciprocal matter work removes its
leading order.  Repeating the earlier overreach at order A^4 would ignore two
successive route reopenings.

Overall no-go-discipline status: FAIL — partial-narrowing.

Only these narrow statements survive:

- trace-only homogeneous evolution is insufficient for this source;
- deleting the two L=5 interference densities is incorrect;
- a frozen-source front splice has an order-A^3 defect;
- the common reduced jet leaves a named order-A^4 action/Noether obligation.

No broad gravity no-go and no axiom no-go ships.

## 12. Reproduction and hostile controls

Run:

    python3 scripts/admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14.py

The normal runner has eight gates.  Each hostile control must fail exactly
one intended gate:

| mutation | intended gate |
|---|---|
| stale_axiom_authority | A |
| break_energy_flux | B |
| drop_interference | C |
| trace_only | D |
| wrong_inhomogeneous_normalization | D |
| break_continuous_flow | E |
| wrong_matter_energy_jet | E |
| freeze_matter_energy | F |
| claim_total_noether | G |
| claim_toe_progress | G |
| weaken_no_go_packet | H |

The frozen output is stored at
[runner cache](../logs/runner-cache/admissibility_counterpropagating_scalar_bianchi_energy_current_exchange_2026_08_14.txt).
Negative-claim dispositions are mirrored in the Block 97 no-go ledger.
