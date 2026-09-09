---
claim_id: vortex_two_dimensional_record_time_single_weyl_interior_real_mass_none
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied finite Wilson-Dirac matrices: Clifford identities; pointwise cancellation of the signed full-cutoff density for real mass; complete-SVD finite vortex counts and localization; exact squared-dispersion identity with nonzero splitting; zero global index for the balanced square chiral block. Masked and heat-weighted local traces are noninteger and scale dependent. Numerical chiral subspaces need not be energy eigenspaces. The pair has nonzero unsigned boundary support but no boundary-localized direction within its specified two-dimensional cutoff under the declared 0.5 threshold. No physical Record history, global winding-index theorem, exact Weyl species or minimal supplier count is established."
upstream_dependencies: []
runner: scripts/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.py
---

# Finite vortex localization and signed chirality cancellation on a supplied two-coordinate square

**Date:** 2026-09-04; corrected 2026-09-09
**Type:** bounded_theorem
**Status:** bounded - bounded or caveated result note
**Audit:** unset; formal audit is deferred until a solid TOE is ready.
**Primary runner:** [scripts/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.py](../scripts/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.py)
**Current cache:** [logs/runner-cache/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.txt](../logs/runner-cache/vortex_two_dimensional_record_time_single_weyl_check_2026_09_04.txt)

This is a conditional finite matrix construction. Every operator, graph,
profile, coefficient, embedding, cutoff and boundary condition below is supplied.
The mathematical results do not derive a physical Hamiltonian, state-selection
rule, species realization, Record-production process or gauge coupling.
The [minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the framework
boundary: permanent single records and nearest-neighbour physical adjacency
supply neither these operators nor their physical interpretation. No approved
primitive is invoked by the dimensionless calculations.

The exact original note, runner and cache are preserved in
`archive/backlog/vortex-7935-7949/originals/7935/` at their original PR head.
Those historical bodies include superseded claims; they are recovery evidence,
not current scientific authority. Current source and actual declared input
identities are checked before execution and bound into the cache. The runner
imports no local scientific helper or external data.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact conditional finite algebra with explicitly finite numerical diagnostics. No general index or physical species theorem."
trace_class: frontier_discovery
artifact_role: theorem
next_trace_action: "Resolve the stated physical realization and generalization obligations; formal audit remains deferred."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Definitions and declared domain

The two transverse coordinates are auxiliary vertices of an open square graph,
not demonstrated physical time directions. In the following original notation,
“record time” names this supplied mathematical coordinate only. Labels called
chirality and handedness refer to matrices and compressed spatial generators;
they are not physical species identifications.

```text
alpha_1..4    t1 (x) o1, t1 (x) o2, t1 (x) o3, t2 (x) I           Cl(4) on C^4
B             alpha_1 alpha_2 alpha_3 alpha_4 = -t3 (x) I         Hermitian, B^2 = 1
embedding     Gamma_i = s_i (x) B  (i = 1,2,3)                    supplied spatial
              Gamma_4 = I (x) alpha_1, Gamma_5 = I (x) alpha_2    record time      SUPPLIED
              Gamma_6 = I (x) alpha_3, Gamma_7 = I (x) alpha_4    the complex mass SUPPLIED
chirality     CHI = Gamma_4 Gamma_5 Gamma_6 Gamma_7 = -i G_1 G_2 G_3   A MATRIX LABEL
handedness    Tr(V_1 V_2 V_3) / 2i on the projected spatial velocities  COMPRESSED CLIFFORD SIGN
H(p)          sum_i sin(p_i) Gamma_i + K_1 (x) Gamma_4 + K_2 (x) Gamma_5
              + [ diag(m_1) + r_s (L_1+L_2) + r sum_i (1 - cos p_i) ] (x) Gamma_6
              + diag(m_2) (x) Gamma_7
D_4           the 4-component transverse operator; H(0) = I_2 (x) D_4
K_1, K_2      hermitian nearest-neighbour momenta on the two open chains   SUPPLIED
L_1, L_2      Wilson Laplacians; 'hard' ends hold the diagonal at 1.0,
              'free' ends at 0.5                                           SUPPLIED
m_1 + i m_2   the record-time mass field on the N x N square               SUPPLIED
vortex n      m = M e^{i n theta}, constant modulus, or M tanh(r/a) e^{i n theta}
pair          m = M e^{i(theta_L - theta_R)}: winding +1 and -1 inside, 0 at the boundary
chi(x)        the basis-free chirality density on the light subspace, summed over it
interior      the square with a pad of N/6 removed; edge is the complement
core          the disc r < max(3, N/6) about the vortex core
```

Sizes: `M = 0.8`, `r = r_s = 1`, light cut `|E| < 0.30`, hard ends unless stated. `N_s = 64` for the one-dimensional control; `N = 24` for the profile table and the robustness checks; `N = 16` for
the light-state growth; `N = 32` for the size row, the cumulative radial profile and the heat-kernel density; `N = 20` for the eight-component checks; `N = 12` and `N = 8` for the operator
identities. Because `{D_4, CHI} = 0` exactly, `D_4` is off-diagonal in the `CHI` eigenbasis with a **square** block `A`, and one singular value decomposition of `A` gives the whole spectrum and
the whole chirality density; the largest dense matrix is therefore `2048 x 2048` for the transverse work and `3200 x 3200` for the eight-component work, both inside the declared bound.

## Clifford algebra and rebuilt one-dimensional control

The seven Hermitian matrices square to identity and anticommute in pairs;
their explicit Pauli products prove the identities checked at zero residual.
An eighth anticommuting generator would give a complex Cl(8) representation,
whose irreducible dimension is 16; this eight-dimensional representation is
therefore saturated. Equivalently, the linear anticommutator map on all 64
Pauli strings has nullity zero. `CHI = I tensor B = -i G1 G2 G3`, with
`CHI^2=1`, commutes with the three spatial generators and anticommutes with
all four transverse ones. This is an enlarged algebra, not one physical qubit.

The runner reconstructs the one-dimensional N=64 hard-wall control:
`d=K sigma2 + [diag(m)+L] sigma3`, `chi=-sigma1`, M=.8 and cutoff .30.
It finds two transverse light states, max|E| approximately 5.3e-16, next
|E|=.801213, wall [24,40) signed weight .999975296343, left-end weight -1,
right-end weight approximately 0 and zero total. Doubling the spin multiplicity
reproduces the historical 1.999950592685428 comparison value. That agreement
checks one fixture, not an arbitrary transition-count theorem. The corrected
[open-interval note](THE_RECORD_TIME_DOMAIN_WALL_ON_AN_OPEN_INTERVAL_WHERE_THE_PARTNER_WEYL_MODE_LIVES_BOUNDED_THEOREM_NOTE_2026-09-03.md)
likewise distinguishes finite paired subspaces from an exact Weyl eigenmode.
Its science is context only; the present matrices are reconstructed here.

## Real mass: signed cancellation with both chiral subspaces present

When m2=0 the unused site-diagonal alpha4 anticommutes with D and CHI.
For the complete symmetric cutoff P=1_{|D|<cut}, alpha4 commutes with P and
each site projector Pi_x. Cyclicity of the trace gives
`Tr(P Pi_x CHI) = -Tr(P Pi_x CHI) = 0`. This proves pointwise cancellation
for this algebra, arbitrary real profiles and the declared endpoint operators.
It pairs opposite chiral sectors with the same spatial probability; it does
not remove those sectors. At nonzero energy alpha4 reverses energy, while the
full symmetric cutoff remains invariant. It preserves the kernel at zero.

At N24 the wall, quadrant, radial and uniform-negative profiles give respectively
16,16,8,20 cutoff states, maximum |E| .2992,.2213,.2128,.2898 and next
|E| .382635,.305534,.352697,.352601. Maximum absolute signed density is below
1.2e-15. The N16 wall has 8 cutoff states compared with 16 at N24; this
is a finite-size comparison, not a proved asymptotic dispersing band.
A focused N12 wall control exhibits 8 light states and four chiral directions
of each sign while its signed density vanishes. Thus “no handed species at
all” was not supported by the original cancellation test.

## Complex profiles: finite census and nonstationary chiral subspaces

One complete SVD of the square A gives all transverse energies and vectors.
For each singular value delta, the two energy eigenvectors are `(u,+v)/sqrt(2)`
and `(u,-v)/sqrt(2)` at +delta and -delta. Their chiral combinations `(u,0)`
and `(0,v)` are CHI eigenvectors, but for delta>0 they mix the two energies.
Their energy expectation is zero and energy residual is delta. At N12 the
focused control finds delta=.001558354565; this excludes exact stationarity.

At N24 the named winding fixtures give:

| Winding | Cutoff count | Interior signed weight | Maximum absolute energy | Next absolute energy |
|---|---:|---:|---:|---:|
| -1 | 2 | -.999951866 | 2.727e-7 | .35586 |
| +1 | 2 | +.999951866 | 2.727e-7 | .35586 |
| +2 | 4 | +1.999642307 | 1.186e-5 | .49390 |
| +3 | 6 | +2.998444682 | 1.249e-4 | .51465 |

Counts are `2|n|` on these fixtures. Signed masked weights approximate n but
are not integer indices. The wider winding-three distribution has a larger
mask deficit; no mask-independent equality follows. At N32, n=1, cutoff
count is 2, maximum |E|=5.714e-10 and next |E|=.31023. The radial cumulative
weights at radii 2,4,8,12 are .818503353,.990842714,.999939457,.999994126;
the outer two-site ring has -.997255950. These are different masks.

The tested hard/free ends give radius-four core weights .990842962/.990842449;
the tanh-core interior is .999933139 compared with .999951866 for constant
modulus. Offsets 0,2,4 retain two cutoff states, while the origin-centred disc
weights become .990842962,.960656303,.717660942. These observations test the
specified variations, not all end conditions, positions or profiles.

At N20 the full eight-component low space has four energy eigenstates with
maximum |E|=5.362e-6 and next |E|=.387679. CHI compression splits it into exact
+1 and -1 doublets; their core weights are .997352 and 7.6e-7. The compressed
spatial generators obey the Clifford relations, with triple-product signs
+1 and -1. This proves the compressed algebra, not invariance of either
chiral doublet under H. The nonzero splitting couples them.

Anticommutation proves exactly
`H(p)^2=sum_i sin(p_i)^2 I + lift(D(p)^2)`, including the spatial Wilson
shift in D(p). Thus a paired branch has
`|E(q)|=sqrt(sin(q)^2+delta(q)^2)` and is approximately Weyl-like only when
the splitting is negligible for the comparison made. At q/pi=0,.05,.10,.20,.40,
the N20 deltas are approximately 5.362e-6,8.034e-6,2.422e-5,6.417e-4,.1392.
Direct diagonalization at .10 pi agrees with .309016995324; the identity
residuals on N12/N20 fixtures are below 7e-17. It is not an exact gapless Weyl cone.

## Local heat traces and the balanced global index

For the square chiral block, rank(A)=rank(A†) and both domains have the same
dimension 2N². Therefore `dim ker A-dim ker A†=0`. The full signed trace of
any symmetric spectral cutoff vanishes, as does the heat supertrace
`Tr(CHI exp(-D²/lambda²))`. A rectangular finite chiral block can instead
have unequal nullities: a rank-two 2x3 block has nullities one and zero.
Equal chiral dimensions, not finiteness alone, are essential.

The local heat density replaces the hard cutoff by a chosen positive lambda.
At N32, radius-eight core values at lambda .1,.2,.4 are
.999939457240,.999938991630,.969581572523; corresponding ring values are
-.997255709,-.996845485,-.964732156 and full traces are approximately zero.
Only the first small-lambda values closely match the cutoff core weight.
A focused N12 vortex control at lambda .1,1,10 gives local core weights near
.9680685,.2534633,0 with zero full trace. Heat weighting removes a sharp
energy boundary, but does not remove scale or mask dependence and does not
prove local index equals winding.

## Constant-symbol gap and the actual pair boundary test

The sampled constant-modulus vortex has |m|=.8. Separately, a translation-
invariant symbol with constant phase theta has square
`sin(k1)^2+sin(k2)^2+[M cos(theta)+2-cos(k1)-cos(k2)]^2+M² sin(theta)^2`.
For x=1-cos(k1), y=1-cos(k2), r_s=1 and 0<M<=1, its value minus M² is
`2(x+y)+2xy+2M cos(theta)(x+y)` and is at least
`2(1-M)(x+y)+2xy >= 0`. Hence the uniform symbol has gap at least M for
all phases and momenta in that range. Corner values at M=.8 are .8,
at least 1.2 and at least 3.2. This proof does not identify the inhomogeneous
open-boundary spectrum or exclude interfaces or topological boundary states.

For the N24 vortex/antivortex pair, signed weights in the two radius-four
core masks are +.987455583 and -.987455583, while the signed edge sum is
about 1.1e-17. The original signed test allowed cancellation. The actual
unsigned cutoff-projector edge trace is .003710367936; maximum pointwise
absolute signed edge density is .000278696211. The compressed boundary
projector on the complete two-dimensional cutoff space has two eigenvalues
about .001855183968. Therefore every normalized vector in that particular
space has boundary weight below the declared .5 boundary-localization
threshold (pad four). This supports no separately boundary-localized direction
under that definition; it does not imply zero boundary support, absence of
higher-energy boundary states, or a general zero-winding boundary theorem.

## Supplied structure and open physical obligations

The reconstruction uses a finite square graph, its two momentum matrices,
Wilson Laplacians and end convention, Clifford embedding, two mass coefficient
fields, finite size and spatial Bloch comparison. Deleting each displayed
transverse term changes the operator by norms 33.226,33.226,110.278,27.153
at N24. Those norms do not prove independent necessity or a minimal supplier count.
No unbounded extent is consumed. No family of nested Record configurations
is constructed. Indexing square vertices by one integer preserves the grid
edges; replacing them with a nearest-neighbour chain changes the graph.
Thus the model does not force a branching physical history.

The original reference to an occupancy-front proposal concerned an archived
historical proposal, not a current derived formation law. No physical
occupancy-to-phase bridge is supplied here. The time-axis discussion’s
sequence definition and the single-clock comparator’s additional premise do
not classify this unembedded auxiliary graph as a realized history. Those
physical realization questions remain open; no repository-wide absence
search or impossibility theorem is claimed. Gauge inflow, many-body effects,
anomalies, other windings, continuum limits and asymptotic decoupling are open.

## Validation and scope recovery

Run the paired runner; its original 25 numerical predicates remain unchanged.
The former unconditional E2 statement is uncounted scope information, and
six focused scientific controls supplement the numerical suite. Source/input
binding runs before science. See the current cache for the actual total and
all numerical output. Historical source/check labels and overclaims remain
recoverable only in the exact archive. Independent review and the combined
integration checks supply landing readiness; neither supplies an audit verdict.
