---
claim_id: admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "For the supplied repaired flat four-dimensional Kuhn/Coxeter Regge edge action at alpha=1/1024 and the conditional analytic continuation q=(k,0,0,-i omega), the raw 99-term Laurent symbol retains its four exact vertex-displacement Ward columns. After exact bordered gauge quotient and y/z-reflection decomposition, one isolated physical pole is resolved in each parity sector at all 36 declared positive-axis wave numbers k in {0.05,0.10,0.20,0.40} union {pi*j/32:1<=j<=32}. Across the 72 solves the five-direction nonmetric Schur block has singular gap above 1.28, the gauge-removed metric-coordinate overlap with the corresponding TT direction exceeds 0.93, and the pole nulls belong to the complete fifteen-edge symbol rather than the border multipliers. Both branches approach the common infrared light cone with sampled cubic real corrections and fifth-order pole phase. On the finite lattice the single-orientation raw continuation has small parity-odd complex phases and a small polarization split; momentum reversal gives the conjugate pole. This is sampled finite-frequency survival, not an all-momentum theorem, selected causal Record update, physical transfer or inner product, unitarity or stability theorem, nonlinear/nonflat completion, axiom amendment, or TOE closure."
upstream_dependencies:
  - minimal_axioms
  - admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_bounded_theorem_note_2026-08-11
  - admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_axiom_boundary_bounded_theorem_note_2026-08-11
  - admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py
---

# Repaired Regge Full-Edge Finite-Frequency Pole Survival Boundary

**Date:** 2026-08-11

**Type:** bounded theorem

**Role:** decide whether the two conditional infrared tensor modes survive in
the actual repaired fifteen-edge lattice symbol before investing in a
physical transfer/inner-product reconstruction.

**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py](../scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py)

## Result Up Front

The supplied repaired edge law passes the finite-frequency survival gate on
the declared axis sample.

The test keeps all fifteen edge coordinates and uses the raw analytic Laurent
symbol of the repaired `alpha=1/1024` action. It does not project to the ten
metric coordinates, and it does not Hermitian-symmetrize the symbol after the
temporal momentum becomes complex. Along

~~~text
q = (k,0,0,-i omega),                                      (1)
~~~

the four exact vertex-displacement Ward columns remain present. After an
exact bordered gauge quotient, reflection across the two transverse axes
splits the problem into an eleven-edge/three-gauge even sector and a
four-edge/one-gauge odd sector. One isolated physical pole is found in each
sector at all `36` declared positive wave numbers,

~~~text
k in {0.05,0.10,0.20,0.40}
     union {pi*j/32 : 1 <= j <= 32}.                        (2)
~~~

The two branches are the finite-lattice continuations of the two infrared
transverse-traceless directions. Across all `72` pole solves:

- the complete analytic Ward residual is below `4.4e-16` in relative norm;
- the metric Schur Ward residual is below `8.2e-12` in relative norm;
- the five-direction nonmetric block has minimum singular value
  `1.28838745`;
- the gauge-removed metric-coordinate TT overlap is at least `0.93191359`;
- the next bordered singular-value ratio is at least `1.6947e-5`;
- the border-multiplier/edge norm ratio is below `5.1e-13`; and
- the nonmetric/metric coordinate ratio is at most `0.56138735`.

Thus the poles are nulls of the complete fifteen-edge symbol, not gauge
zeros, metric-only projection artifacts, or zeros manufactured by the
bordering variables. The nonmetric dressing becomes appreciable near the
zone edge, but its own block never approaches a zero on the sample.

For the four low momenta, the real dispersion correction and polarization
split scale empirically as `k^3`, while the small pole phase scales as `k^5`.
The two modes therefore converge to the common real light cone derived in the
infrared parent.

At finite lattice momentum, however, this particular single-orientation raw
continuation is not exactly polarization-degenerate or exactly real. Over
(2), the maximum relative departure of `Re(omega)` from

~~~text
omega_lat(k) = 2 asinh(sin(k/2))                            (3)
~~~

is `0.00934417`, the maximum real polarization split is `0.00666505`, and the
maximum `|Im(omega)|` is `0.00139269`. Reversing `k` gives the conjugate pole,
so the phase is parity-odd rather than a same-sign growth rate across both
orientations.

This is positive gravity progress: the complete finite-frequency edge system
does not kill the two infrared tensor branches. It is not yet TOE progress.
The raw complex poles cannot be called unitary, unstable, or physical until a
physical transfer or inner product and its Record clock are supplied.

This is **not a gravity no-go** and **not a global instability**. It is a
bounded survival theorem plus a sharply localized reconstruction question.
No canonical axiom is edited, and no TOE percentage moves.

## Inputs And Non-Imports

| input | used | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | the current dynamics, time-metric, and source/action boundary | a selected action, analytic continuation, transfer operator, physical norm, or Record clock |
| [complete-edge Ward/Green parent](ADMISSIBILITY_REGGE_FIXED_AVERAGE_TICK_SOURCE_INCREASING_TORUS_WARD_GREEN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the repaired real-space kernel, fifteen edge classes, exact displacement columns, and warning against metric-only poles | physical action selection, finite-frequency Lorentzian dynamics, or an all-volume theorem |
| [infrared Einstein/TT parent](ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the complete stationary Schur construction, conditional standard continuation, and two infrared TT directions | a finite-lattice pole theorem, positive Hilbert space, causal update, or nonlinear constraints |
| [joint-law cut gate](ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the distinction between a conditional gravity completion and an exact selected Record/geometry law | an extensional `L*`, axiom adoption, or license to interpret raw poles as observations |

The tick direction, analytic continuation (1), Euclidean coordinate norms
used for diagnostics, and single Kuhn/Coxeter orientation are supplied
conditional choices. None is promoted into the foundation.

## Raw Analytic Symbol

Let `Q_s` denote the `15`-by-`15` real-space Hessian coefficient at shift `s`.
The combined repaired kernel has `99` distinct shifts and temporal-shift
inventory

~~~text
s_t  = -2  -1   0  +1  +2
count=  4  29  33  29   4.                              (4)
~~~

It obeys

~~~text
Q_(-s) = Q_s^T                                             (5)
~~~

to maximum coefficient error below `4.5e-16`. The analytic symbol is

~~~text
Q(q) = sum_s exp(i s dot q) Q_s.                           (6)
~~~

For real `q`, (5) makes (6) Hermitian. For complex temporal momentum it does
not license replacing (6) by `(Q+Q^dagger)/2`; that replacement changes the
analytic problem. The runner therefore uses (6) directly.

For an edge direction `d`, the exact displacement and line-averaged metric
maps are

~~~text
G_d,mu(q) = [exp(i d dot q)-1] d_mu/|d|,

M_d,A(q)  = exp(i x_d) sin(x_d)/x_d M_d,A(0),
x_d       = d dot q/2.                                     (7)
~~~

The raw symbol retains the two-sided analytic Ward identities

~~~text
Q(q) G(q)       = 0,
G(-q)^T Q(q)    = 0.                                       (8)
~~~

At four representative complex momenta through the zone edge, the absolute
residual in (8) is below `3e-13` and `G(q)` has rank four.

## Exact Sector Gauge Quotient

Let `P_15` swap the transverse `y` and `z` coordinates of every edge and let
`P_4` do the same to a displacement parameter. On the axis (1),

~~~text
[P_15,Q(q)] = 0,
P_15 G(q)   = G(q) P_4.                                    (9)
~~~

The `+1` eigenspaces of `(P_15,P_4)` have dimensions `(11,3)`; the `-1`
eigenspaces have dimensions `(4,1)`. Write their orthonormal bases as
`(U_sigma,V_sigma)`. The even metric tensor direction is the cross mode
`h_yz`; the odd direction is the plus mode `h_yy-h_zz`.

The physical poles are located with the analytic bordered operator

~~~text
B_sigma(k,omega) =
  [ U_sigma^T Q(q) U_sigma       U_sigma^T G(-q) V_sigma ]
  [ V_sigma^T G(q)^T U_sigma                   0          ]. (10)
~~~

This construction removes the exact gauge kernel without choosing a gauge
penalty or dropping an edge equation. A zero of `det B_sigma` is accepted as
a physical edge pole only if its right null vector `(x,lambda)` also has
`lambda/x` negligible and `Q(q)U_sigma x` negligible. Both controls pass for
all `72` roots. The maximum multiplier ratio is `5.1e-13`; the maximum
normalized complete-edge null residual is below `7e-16`.

The smallest singular value of (10) is below `1.7e-16` relative to its largest
at every solved root. The next singular-value ratio stays above `1.69e-5`, so
the sample resolves one isolated quotient pole in each sector rather than an
uncontrolled multi-zero collision.

## Pole Inventory

Representative double-precision roots are:

| `k` | even / cross `omega` | odd / plus `omega` |
|---:|---:|---:|
| `0.05` | `0.04998985243 - 4.52e-11 i` | `0.04998994348 - 9.47e-13 i` |
| `0.10` | `0.09991889345 - 1.443e-9 i` | `0.09991962051 - 3.144e-11 i` |
| `0.20` | `0.19935349943 - 4.573e-8 i` | `0.19935927414 - 9.971e-10 i` |
| `0.40` | `0.39490120293 - 1.407e-6 i` | `0.39494612839 - 3.069e-8 i` |
| `pi/2` | `1.32170978304 - 6.137e-4 i` | `1.32361361166 - 1.303e-5 i` |
| `pi` | `1.77255352896` | `1.77921857106` |

The table is illustrative; the claim inventory is the complete set (2), not
only these six rows. The solver starts each sector at (3) and solves the real
and imaginary parts of the scaled determinant independently. No target root,
dispersion coefficient, phase, or polarization split is hard-coded.

## Complete-Edge Character Of The Poles

Let `N` be the constant orthonormal five-direction complement to the ten
constant-metric tangents. At complex momentum, the analytic stationary Schur
operator is

~~~text
C(q) = N^T Q(q) N,

E(q) = M(-q)^T Q(q) M(q)
     - M(-q)^T Q(q) N C(q)^(-1) N^T Q(q) M(q).             (11)
~~~

The transpose and `-q` in (11) are essential. A conjugate transpose would
replace the analytic pole problem by a different Hermitian one.

Across the root inventory, `sigma_min(C)` is at least `1.28838745`. Thus none
of the roots is a zero of the discarded complement. Solving

~~~text
edge pole vector = M(q) h + N n                             (12)
~~~

gives `||n||/||h|| <= 0.56138735`. The high-momentum modes are genuinely
dressed complete-edge excitations; calling them purely metric would be too
strong.

For a coordinate diagnostic only, the runner removes from `h` the Hermitian
least-squares span of the exact metric gauge columns and compares the result
with the corresponding plus or cross vector after the same removal. The
absolute normalized overlap is at least `0.93191359`, reaching its minimum in
the even sector at `k=pi`. This is strong TT character, but it is not called a
physical probability or norm because no physical inner product has been
selected.

## Infrared Survival And Finite-Lattice Artifacts

For `k=0.05,0.10,0.20,0.40`, define

~~~text
delta_disp(k) = max_sigma |Re omega_sigma(k)-omega_lat(k)|,
delta_pol(k)  = |Re omega_even(k)-Re omega_odd(k)|,
delta_phase(k)= max_sigma |Im omega_sigma(k)|.              (13)
~~~

Under each doubling of `k`, the observed base-two orders are approximately

~~~text
delta_disp : 2.997, 2.989, 2.958,
delta_pol  : 2.997, 2.990, 2.960,
delta_phase: 4.997, 4.985, 4.944.                           (14)
~~~

This sampled scaling is consistent with cubic real lattice corrections and a
fifth-order orientation phase. It is not an analytic asymptotic proof beyond
the four declared points.

At `k=0.4,0.8,1.6,2.4`, substituting `(-k,omega(k)^*)` into the corresponding
bordered operator leaves a normalized smallest singular value below `9e-17`.
The raw real-space law therefore supplies the conjugate partner under momentum
reversal. A small negative imaginary part on the chosen positive orientation
is not, by itself, a global instability or a nonunitarity theorem.

What fails on the displayed single-orientation representation is the stronger
statement that both finite-lattice polarizations share one exactly real pole
at each `k`. That stronger statement was not supplied by the infrared parent
and is not required for the positive survival result.

## Physical Reconstruction Gate

The result retires one candidate failure mode: complete-edge mixing and the
exact lattice Ward quotient do not destroy the two tensor branches before the
zone edge. It does not retire the physical gravity obligation.

The next decisive test is no longer another frequency grid. It is whether an
actual physical reconstruction turns the paired analytic information into a
positive causal propagator. The highest-leverage constructions are:

1. a reflected-orientation or alternating-orientation block whose transfer
   spectrum can be compared with the conjugate pole pair;
2. an Osterwalder-Schrader/reflection-positive transfer reconstruction with an
   explicit physical inner product;
3. a unitary dilation or gauge-invariant observable transfer whose eigenphases
   reproduce the same infrared residue and two-mode quotient; and
4. an exact Record-clock map showing which analytic frequency is operational.

The stop criterion is sharp. If one construction yields a positive physical
two-mode transfer, it can retire part of the physical gravity lane. If every
construction requires an independently chosen clock, norm, or orientation
completion, that choice belongs in the exact joint-law contract identified by
the parent cut gate. More pole sampling cannot decide between those outcomes.

## Axiom And TOE Boundary

The current axioms do not choose a Hamiltonian or transfer operator, a time
metric, an update law, a source/action dictionary, or a physical state
inner product. The present computation therefore cannot select its own
conditional continuation as the world law.

It also does not remove any of the five independent controls in the joint-law
cut. In particular, exact Ward survival for the supplied candidate is not a
proof that every admissible Record law fixes its Lorentzian constraint map.
The extensional `L*` or exact record-faithful physical-equivalence class is
still absent.

No canonical axiom is edited. No TOE percentage moves. The scientific gain
is narrower but real: gravity remains viable at complete-edge
finite-frequency level, and the remaining high-value question has moved from
"do the modes survive?" to "what physical reconstruction and joint law select
their norm, clock, and causal meaning?"

## Portfolio Re-Rank

This block closes the already-computed finite-frequency diagnostic and ends
that search direction. The campaign order is now:

| rank | seam | lane-moving condition | stop condition |
|---:|---|---|---|
| 1 | physical transfer or inner product for the paired pole branches | a positive two-mode physical quotient tied to the static residue and constraints | stop after the first exact construction or exact obstruction; do not add grids |
| 2 | exact joint Record/geometry law `L*` | an extensional law or exact operational-equivalence class binds clock, constraints, source, and Record composition | stop treating structural existence clauses as progress |
| 3 | stable nonflat phase and nonlinear constraint propagation | one selected law preserves constraints away from the flat linear sector | defer until ranks 1-2 produce the law being propagated |
| 4 | full-`Z^3`/boundary and realized-history completion | the selected local law has a projectively consistent global process and actual-history semantics | pursue only against a concrete selected law |

Additional precision, denser axial samples, alternate metric projections, and
new Record counterkernels are demoted. They cannot move a lane unless they
reverse one of the decisions above.

## Fresh No-Go-Discipline Packet

The scoped negative is only this: **the displayed single-orientation raw
analytic continuation does not numerically supply one exactly real,
polarization-degenerate finite-lattice pole on the declared sample.** It is
not a claim that gravity, a positive transfer, or a unitary completion is
impossible.

### N1 — Alternative Routes

Live routes include a reflected-orientation block, alternating simplex
orientation, temporal blocking, an Osterwalder-Schrader reconstruction, a
physical similarity transform, a gauge-invariant observable transfer, a
unitary dilation, and an exact Record-clock law. Off-axis and nonperturbative
constructions also remain open.

### N2 — Wall Independence

The phase and split are read from zeros of the exact bordered determinant
after all four gauge columns are removed. The five nonmetric directions stay
gapped, the border multipliers vanish, and both parity sectors are resolved.
Thus they are not produced by the known metric-only truncation or a gauge
penalty. Their physical significance remains dependent on the unsupplied norm
and clock.

### N3 — Hidden-Wall Scan

The repaired action, `alpha=1/1024`, tick axis, continuation (1), orientation,
and Euclidean coordinate diagnostic are supplied. The action is not selected
by the axioms. The calculation is double precision and samples one momentum
axis at `36` points. No all-axis continuity, full Brillouin zone, positive
measure, transfer matrix, nonlinear phase, or realized history is imported.

### N4 — Residual Matching

The residual is a small parity-odd finite-lattice pole phase and a small real
polarization split, not loss of the Ward identities, disappearance of the two
tensor modes, closure of the nonmetric gap, or reversal of the positive static
source residue. The missing TOE content is the physical reconstruction and
exact joint-law selection, not more root precision.

### N5 — Resolution And Scope Certificate

The runner resolves all `99` Laurent shifts and their transpose partners, all
`15` edge coordinates, all four exact gauge columns, the fixed five-direction
nonmetric complement, both reflection sectors, `36` positive wave numbers,
`72` pole solves, four infrared doublings, and eight momentum-reversal sector
checks. It does not infer a continuum of momenta or an infinite-volume causal
process.

### N6 — Partial-Closure Scan

The positive theorem is preserved: both complete-edge branches survive,
remain isolated from the nonmetric block, are strongly TT-like after gauge
removal, converge to the common infrared cone, and possess conjugate reversal
partners. This is the part that should guide the next construction.

### N7 — Steelman

The strongest counterposition is that the phase is a representation artifact
of looking at one oriented analytic kernel before the correct reflection
pairing or physical norm is imposed. That is plausible and is now the first
route to test. Conversely, its success is not assumed: it must reproduce the
same Ward quotient, static residue, and two-mode count without fitting a
frequency-dependent correction.

### N8 — Cross-Cycle Echo

Earlier reflection-positive and orientation-repair seams warn that a raw
single-orientation phase need not be a physical decay rate. The Block-43
metric-only false pole likewise warns against interpreting a reduced
determinant before the complete edge equations are solved. This block honors
both lessons: it uses the complete edge quotient and leaves the
reflected-orientation physical reconstruction open.

**Status: PASS.** The narrow sampled artifact statement survives N1-N8. A
gravity no-go, a global instability, nonunitarity, exact all-zone splitting,
and the necessity of any axiom change are not proved. A physical reconstruction
is not proved necessary as an axiom rather than a downstream theorem.

## Reproduction

Run from the repository root:

~~~bash
python3 scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py
~~~

Expected final line:

~~~text
TOTAL: PASS=12 FAIL=0
~~~

The runner computes every quoted root and bound from the real-space kernel. It
does not hard-code a target dispersion or load a pole table.

## Conclusion

The complete repaired Regge law has crossed a meaningful physics gate: its
two conditional infrared tensor modes survive as isolated, strongly TT-like
full-edge poles throughout the declared positive-axis sample, with exact
complex-momentum Ward identities and a uniformly gapped nonmetric remainder.

That is significant science progress but not lane closure. The small
single-orientation phase and polarization split now make the next experiment
unambiguous: construct the physical transfer/inner product or show exactly
why no current-foundation reconstruction chooses one. Only that result—or an
exact joint `L*` resolving it—can justify moving the gravity percentage.
