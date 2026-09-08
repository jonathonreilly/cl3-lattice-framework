---
claim_id: admissibility_periodic_flat_ec_connection_negative_mode_axiom_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "For the unchanged Block-38--40 Euclidean ten-label Record/coframe/SO(4)-link law, every proper-cubic homogeneous flat stationary Gram on every finite periodic L>=3 cubic carrier has a physical zero-momentum connection direction A_i=J_(i,3)/sqrt(3) whose complete gauge-quotiented action Hessian is strictly negative. The stationary equations contract the Block-40 Gram ellipse to x in (0.89,1.03), y in (1.40,1.66). A Jensen--Holder six-neighbor bound forces total spatial-ray marginal above 0.18. The EC commutator Hessian is 8sqrt(x)/3 on the four spatial rays and 8sqrt(x)/9 on the six tick rays, while every Record contact is bounded below by -2 beta and connected covariance is nonnegative. Thus the normalized full directional Hessian is at most -0.0304634968. An explicit L=3 joint coframe/link tangent-rank test proves the direction is not internal-frame gauge. This is a bounded instability theorem for one supplied flat branch and a downstream law-repair localization, not a gravity no-go for modified or relational laws, nonflat phases, continuous joint geometry, physical selection, Lorentzian updates, axiom necessity, or axiom adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_two_cube_record_ec_overlap_gibbs_connection_boundary_bounded_theorem_note_2026-08-11
  - admissibility_periodic_record_ec_dobrushin_flat_connection_source_boundary_bounded_theorem_note_2026-08-11
  - admissibility_periodic_gram_well_nondegenerate_flat_vacuum_local_frame_hessian_boundary_bounded_theorem_note_2026-08-11
  - admissibility_periodic_gram_well_spin_two_mass_gap_connection_schur_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_periodic_flat_ec_connection_negative_mode_boundary_2026_08_11.py
---

# Periodic Flat EC Connection Negative Mode / Axiom Boundary

**Date:** 2026-08-11
**Type:** `bounded_theorem`
**Role:** resolve the highest-priority connection-quotient discriminator left
by Block 41 before investing in a full Bloch-symbol census.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_periodic_flat_ec_connection_negative_mode_boundary_2026_08_11.py](../scripts/admissibility_periodic_flat_ec_connection_negative_mode_boundary_2026_08_11.py)

## Result Up Front

The unchanged supplied flat branch is not connection-stable. Its physical
connection block is neither a regular positive auxiliary block nor merely a
massless singular escape. It has a strictly negative direction.

Let the Block-40 proper-cubic stationary Gram be

```text
G_L=diag(x_L,x_L,x_L,y_L).
```

The stationary equations sharpen the earlier energy ellipse to

```text
0.89 < x_L < 1.03,
1.40 < y_L < 1.66.                                           (1)
```

For the three positive base axes use the unit coefficient-norm connection
variation

```text
B_i = J_(i,3)/sqrt(3),       i=0,1,2,                       (2)
```

where `J_(i,3)` is the internal `SO(4)` generator mixing spatial axis `i`
with the internal tick direction. This is the proper-cubic isotropic
time--spatial connection channel. Direct joint tangent rank on the `L=3`
carrier gives

```text
rank(local-frame tangent)              162/162,
rank(tangent augmented by (0,B))       163,
least-squares distance from gauge      5.196152423.           (3)
```

Thus `(delta e=0,delta A=B)` is not an internal-frame gauge tangent.

The complete directional action Hessian includes geometry, all Record bond
contacts, the connected Record score covariance, and the quadratic
Einstein--Cartan load. A volume-uniform local conditional bound proves that
the four purely spatial Record rays carry total marginal probability

```text
p_S > 0.18.                                                   (4)
```

The separate contributions obey

```text
K_geometry(B,B) = eta(x+y+1),
K_EC(B,B)       = sqrt(x)[8/9+(16/9)p_S],
K_Record(B,B)   >= -2 beta = -0.4.                            (5)
```

Here `K_Record` is the Record pressure Hessian: its connected covariance is
nonnegative, and `-0.4` is the strongest possible stabilizing lower bound on
its contact part in the declared normalization. Since the action is geometry
minus Record-plus-EC pressure, equations (1), (4), and (5) give

```text
K_action(B,B)
 <= (1/5)(0.89+1.66+1) + 0.4
    -sqrt(0.89)[8/9+(16/9)(0.18)]
  = -0.0304634968 < 0.                                      (6)
```

The bound holds for every finite periodic `L>=3` carrier. It passes to the
unique fixed-background infinite Record phase from Block 39 because all
quantities in the proof are bounded local expectations and the inequality is
volume independent.

This is significant for the TOE stack. The singular-connection escape named
in Block 41 does not rescue this unchanged flat branch: a negative direction
is not a massless physical zero mode. A full small-`k` census of this same
unstable saddle is therefore low leverage. The next high-value target is a
modified or relational law that first restores a semibounded physical phase
and then derives a base-displacement Ward identity capable of removing the
Block-41 spin-two intercept.

This is **not a gravity no-go**. A modified law, a relational/derivative
completion, a nonflat phase, or a different joint geometry phase can evade
equation (6). No canonical axiom is edited, and no fixed TOE percentage moves
in this block.

## Inputs And Non-Imports

| input | used | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | `Z^3`, translations, proper cubic rotations, one fixed nearest-neighbor Admissibility distribution, and permanent Records | coframes, `SO(4)` links, EC curvature, Euclidean action, flat stability, gravity, or time |
| [Block 38](ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the fixed elementary `sigma/3` EC face-incidence factor and overlap-consistent local law | periodic stability, a selected phase, or a physical coefficient |
| [Block 39](ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the periodic fixed-background Record phase and vanishing flat first variation | a second-order connection stability theorem or joint geometry measure |
| [Block 40](ADMISSIBILITY_PERIODIC_GRAM_WELL_NONDEGENERATE_FLAT_VACUUM_LOCAL_FRAME_HESSIAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the `alpha=16` stationary proper-cubic flat Gram, its ellipse, and local-frame quotient | a positive physical Hessian or realized vacuum |
| [Block 41](ADMISSIBILITY_PERIODIC_GRAM_WELL_SPIN_TWO_MASS_GAP_CONNECTION_SCHUR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the zero uniform Gram/link mixed block and the explicit regular-versus-singular connection discriminator | connection regularity, singularity, or stability |

No observed gravitational datum, graviton mass bound, Newton coefficient,
cosmological coefficient, continuum target, fitted cancellation, canonical
axiom edit, audit verdict, or `review-loop` is used. The only transcendental
inequalities are elementary finite-label exponential bounds evaluated with
more than a factor-six margin over their printed rounding error.

## 1. Stationarity Contracts The Gram Domain

Block 40 proves

```text
3(x-1)^2+(y-25/16)^2 <= 21/40.                               (7)
```

Hence

```text
x >= x_0=0.5816699867,
y >= y_0=0.8379311627.                                       (8)
```

For a ray `r`, let

```text
u(x,y;r)=diag(sqrt(x),sqrt(x),sqrt(x),sqrt(y)) r /
         ||diag(sqrt(x),sqrt(x),sqrt(x),sqrt(y)) r||,
C_ab=(u_a.u_b)^2.                                             (9)
```

Under `d/d log x`,

```text
u'=(1/2)(Pi_S-<Pi_S>)u,
||u'||^2=(1/4)s(1-s) <=1/16.                                 (10)
```

The same statement holds with the complementary tick projector under
`d/d log y`. Therefore

```text
|dC_ab/d log x| <=1,
|dC_ab/d log y| <=1.                                         (11)
```

This is a continuum bound for every ray pair, not a grid over the stationary
domain. At identity links the proper-cubic pressure derivatives contain one
site score plus three bonds per site. The site score ranges are

```text
d_x log q_a in [-3/2,-1/2],
d_y log q_a in [-1/2,0].                                     (12)
```

Stationarity of the `alpha=16` well gives

```text
24(x-1)=d_x p,
 8(y-25/16)=d_y p.                                           (13)
```

Using (8), (11), and `beta=1/5` in (12)--(13) yields the unrounded enclosure

```text
0.8945203026 < x < 1.0221463641,
1.4104938409 < y < 1.6520061592.                             (14)
```

Equation (1) is (14) rounded outward. This contraction is why a generic
ellipse-wide covariance campaign would have been inefficient: stationarity
removes the extreme low-geometry corner before any connection estimate.

## 2. Geometry And Physical Quotient Of The Isotropic Mode

The coefficient norm in (2) is

```text
sum_i ||J_(i,3)/sqrt(3)||_coeff^2=1.                         (15)
```

For compatibility, each `J_(i,3)` rotates one coframe column of squared norm
`x` into the tick column of squared norm `y`, and conversely. The unit normal
is rotated with squared norm one. For a face in axes `i,j`,

```text
J_(i,3)e_j=J_(j,3)e_i=0,                                    (16)
```

so the linear torsion residual vanishes. Thus

```text
K_geometry(B,B)=eta(x+y)+eta=eta(x+y+1).                     (17)
```

The direction is physical. A local-frame tangent has

```text
delta e_v=Omega_v e,
delta A_(v,i)=Omega_v-Omega_(v+i).                            (18)
```

Since `e` is invertible, `delta e_v=0` forces every `Omega_v=0`; a nonzero
uniform `B_i` cannot then occur. The runner independently builds the complete
`L=3` tangent matrix and obtains (3), rather than relying only on this
one-line argument. A negative value on this non-gauge vector descends to a
negative value of the gauge-quotiented quadratic form even if other coframe
directions are retained.

## 3. A Uniform Spatial-Ray Marginal Floor

At the flat link, write `S={0,1,2,3}` for the four spatial rays and
`T={4,...,9}` for the six time-bearing rays. Their site weights are

```text
w_S=3 exp(-3x/2),
w_T=4 exp(-(x+y)/2).                                         (19)
```

For six neighboring labels `b_1,...,b_6`, the conditional orbit weights are

```text
A=w_S sum_(a in S) product_j K_(a b_j),
B=w_T sum_(a in T) product_j K_(a b_j),
p_S=A/(A+B),                                                  (20)
```

where `K_ab=exp[-beta(1-C_ab)]`. Jensen on the four-term denominator of
`B/A` and Holder on its six-term numerator give

```text
B_kernel/A_kernel
 <= (1/4) product_j r_(b_j),
r_b=[sum_(a in T) K_ab^6]^(1/6) /
    exp[(1/4)sum_(a in S)log K_ab].                           (21)
```

Only two neighbor orbits exist. Put `t=y/x`. For a spatial neighbor and a
tick neighbor respectively, direct ten-ray contraction gives

```text
r_S^6=6 exp[-2/5+(6/5)/(3(1+t))],                            (22)

r_T^6={1+exp[-(6/5)(1-((t-1)/(t+1))^2)]
         +4exp[-(6/5)(1-(t/(t+1))^2)]}
       exp[(6/5)(1-1/(3(1+t)))].                             (23)
```

On (1), `1.40/1.03 <=t<=1.66/0.89`, with `t>1`. Equation (22) decreases
with `t`, while every nonconstant factor in (23) increases. Endpoint
evaluation gives

```text
r_S^6 <4.77,
r_T^6 <9.65.                                                  (24)
```

Also

```text
w_T/w_S=(4/3)exp(x-y/2)
       <=(4/3)exp(1.03-1.40/2).                              (25)
```

Equations (21), (24), and (25) imply

```text
B/A <4.474280814,
p_S >0.1826723973 >0.18.                                     (26)
```

The bound holds in every exterior configuration. Averaging the conditional
therefore proves (4) for every finite-volume marginal without an independence
or mean-field assumption.

## 4. Exact Einstein--Cartan Quadratic Load

For the based loop in an `ij` face, uniform links in direction (2) give

```text
U_i U_j U_i^-1 U_j^-1
 =I+(t_link^2/3)[J_(i,3),J_(j,3)]+O(t_link^3).                (27)
```

The sine-holonomy coordinate has the same quadratic commutator. Its first
derivative is zero configurationwise, so it contributes no first-score
covariance or mixed covariance at the flat point.

Each site is the base of four oriented loops in each of the three spatial
face planes. Summing the fixed `sigma/3` incidence factor over all twelve
based loops gives

```text
q_EC''(a)=8sqrt(x)/3,    a in S,
q_EC''(a)=8sqrt(x)/9,    a in T.                              (28)
```

The primary runner derives (28) from the generator commutators, Hodge dual,
ray incidences, and all twelve step pairs. It also exponentiates the finite
`SO(4)` links and recovers the same second derivatives. Taking the marginal
expectation and using (4) gives the second equation in (5).

## 5. Complete Record Bound

For one Record bond and one skew generator combination `D`, the overlap term
is

```text
f(t)=beta [u.exp(tD)v]^2.                                    (29)
```

Its second derivative is

```text
f''(0)=2beta{[u.Dv]^2+(u.v)[u.D^2v]}
      >=-2beta ||D||_op^2.                                   (30)
```

For a four-dimensional skew matrix written in the runner's six-generator
coefficient basis,

```text
||D||_op^2 <= ||D||_coeff^2.                                 (31)
```

There is one bond per site in each positive axis. The three blocks of (2)
have total coefficient norm one, so the sum of every contact expectation is
at least `-2beta=-0.4`. The runner reconstructs all 100 ordered projector-pair
contact matrices at every safe-box corner and reaches this lower bound.

Let `S_B` be the total first Record score. Direct finite-volume
differentiation gives

```text
p_Record''=<Q_B>+Var(S_B).                                   (32)
```

The variance is nonnegative. It can only make the pressure curvature larger
and the Euclidean action curvature more negative. Consequently (30)--(32)
already grant the Record sector its strongest possible stabilizing effect;
no susceptibility estimate is needed to prove (6).

## 6. Strict Negative Bound And Its Scope

Combining (17), (28), and (32),

```text
K_action(B,B)
 <= eta(x+y+1)+2beta
    -sqrt(x)[8/9+(16/9)p_S].                                 (33)
```

At `p_S=0.18`, the right side increases with `y` and decreases with `x` over
the safe box because

```text
eta-[8/9+(16/9)(0.18)]/(2sqrt(1.03)) <0.                     (34)
```

Its maximum is therefore the corner used in (6). The strict margin is more
than thirty thousand times the runner's floating comparison tolerance.

This proves one negative physical `k=0` connection direction. It does not
classify the other seventeen uniform connection coordinates, compute the
small-`k` Bloch spectrum, or locate a stable nonflat saddle. None of those
tasks can make the current flat Hessian semibounded: one negative quotient
direction is decisive for flat stability.

## 7. Gravity And Axiom Consequence

The gravity priority stack changes materially:

- **Closed:** the physical connection quotient on the unchanged flat branch
  is unstable; it is not the regular-positive or massless-singular escape
  left open by Block 41.
- **Deprioritized:** a full Bloch census of the same unstable saddle and
  tighter generic susceptibility constants. They cannot restore
  semiboundedness.
- **Highest priority:** construct a modified or relational finite-range law
  with an exact local displacement Ward identity; prove a stable joint phase;
  then test its tensor residue and source coupling.
- **Still live:** a stable nonflat phase of a modified or separately proved
  law, continuous joint geometry, physical law selection, and Lorentzian
  permanent-Record dynamics.

The four canonical axioms do not select the supplied `sigma/3` EC coefficient,
the absolute Gram well, a stable geometry phase, or a massless displacement
Ward sector. Equation (6) therefore identifies a downstream law-selection
issue, not a contradiction among the axioms. A sufficient but unadopted
interface clause would require a selected geometry-bearing Admissibility law
to have a semibounded physical quotient and a derived displacement Ward/source
identity with no forbidden `O(k^0)` spatial spin-two term. Necessity,
minimality, and canonical adoption are not proved. **No canonical axiom is
edited.**

Fixed TOE percentages remain
`95/92/50/99`, `76/72/41/99`, `95/96/75/99`, `70/45/29/94`, and
`84/63/34/99` for operational Records, causal time, inertia, gravity, and
Born/history respectively. This block changes the route diagnosis, not a
closure gate.

## No-Go Discipline Gate

The eligible negative is deliberately narrow:

> The unchanged supplied Block-38--40 homogeneous flat stationary branch has
> at least one negative physical zero-momentum connection Hessian direction.

It is not a statement that gravity, EC/BF/Regge/teleparallel mechanisms,
nonflat phases, modified Record laws, relational geometry, or Lorentzian
dynamics are impossible.

### N1 — Alternative Route Enumeration

The approach families are normalized by mathematical object, mechanism, and
terminal obligation rather than by artifact or worker.

| route | honesty | attack on the scoped negative | result |
|---|---|---|---|
| stationary-domain escape | `ATTEMPTED` | move the actual stationary Gram to a corner where geometry dominates EC | equations (7)--(14) put every Block-40 stationary Gram inside the safe box, and the negative bound is uniform there |
| complete Record stabilization | `ATTEMPTED` | use bond contacts or connected susceptibility to lift the mode | equations (29)--(32) grant the contact its optimal `+0.4` action effect, while covariance has the destabilizing sign; (6) stays negative |
| internal-frame gauge removal | `ATTEMPTED` | identify `(0,B)` with a local `SO(4)` orbit tangent | invertibility plus the independent `162 ->163` rank increase in (3) rules this out |
| finite-boundary artifact | `ATTEMPTED` | make the sign disappear with volume or a boundary message | the conditional bound is exterior-uniform and the periodic local counts are exactly `3/3/12` edges/faces/based loops per site for every `L>=3` |
| massless singular connection | `ATTEMPTED` | reinterpret the Block-41 singular escape as the current mode | a strict negative Rayleigh value is not a zero eigenvalue; this flat branch is unstable before residue or polarization questions arise |
| other positive connection sectors | `ATTEMPTED` | hope positive eigenvalues elsewhere make the quotient semibounded | one non-gauge negative vector is sufficient to make the quadratic form indefinite; a full eighteen-mode census cannot reverse it |
| modified coefficient, relational law, or nonflat phase | `ATTEMPTED` | change the law or phase so equation (33) no longer applies | this is a genuine live escape, but it changes the scoped premise; deleting or modifying the EC load removes this certificate and is queued as the next repair target |

The first six routes fail against the scoped theorem. The seventh defeats any
broad gravity no-go and is why the claim remains a bounded supplied-law
instability.

### N2 — Wall-Independence Audit

The negative theorem itself has one collapsed condition: the unchanged
supplied flat branch. The following are independent downstream TOE
obligations, not extra premises used to obtain (6):

`W1` stable semibounded selected geometry law/phase; `W2` massless
base-displacement Ward sector; `W3` physical law/source identification; `W4`
Lorentzian causal permanent-Record update.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| `W1,W2` | no: stability permits a massive tensor | no: a formal Ward identity need not select a stable phase | yes |
| `W1,W3` | no: a stable supplied law can remain unselected | no: selection does not prove stability | yes |
| `W1,W4` | no: Euclidean semiboundedness is not causal evolution | no: a causal update need not select this geometry law | yes |
| `W2,W3` | no: a Ward identity does not identify the physical source law | no: source identification need not make the tensor massless | yes |
| `W2,W4` | no: spatial Ward structure is not Lorentzian closure | no: causality alone does not derive the Einstein tensor | yes |
| `W3,W4` | no: physical selection is not an update theorem | no: an update rule does not identify the gravity source/action | yes |

No wall is collapsed into another, and none is described as a newly required
ontology axiom.

### N3 — Hidden-Wall Scan

| phrase class | occurrence/classification |
|---|---|
| “background” / “flat branch” | cited bounded object supplied by Block 40; not called a realized physical vacuum |
| “the framework provides” | absent; the law is repeatedly typed as supplied and downstream |
| “by construction”, “naturally”, “obviously”, “standard QFT” | absent from the load-bearing proof |
| “registered” / “canonical” | governance-only statement that no canonical axiom is edited; it supplies no physics step |
| “we assume” | absent; every quantitative premise is displayed in Inputs And Non-Imports |

No hidden condition is promoted to a wall.

### N4 — Residual Matching

| cited witness | witness residual | current residual | match? |
|---|---|---|---|
| `ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:62` | fixes `sigma/3` as an elementary face coefficient | identify the exact EC factor differentiated here | yes, as a premise; not a prior negative witness |
| `ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:281,311` | closes flat first variation and queues the quotient Hessian | decide second-order physical connection stability | yes; this is the queued residual |
| `ADMISSIBILITY_PERIODIC_GRAM_WELL_NONDEGENERATE_FLAT_VACUUM_LOCAL_FRAME_HESSIAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:63,318` | proves stationary Gram confinement but excludes nonuniform/Lorentzian stability | sharpen that Gram and test one uniform physical connection mode | yes for the stationary input; no stability conclusion is borrowed |
| `ADMISSIBILITY_PERIODIC_GRAM_WELL_SPIN_TWO_MASS_GAP_CONNECTION_SCHUR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md:327,359` | leaves regularity versus singular connection open | classify the unchanged flat physical block | yes; equation (6) resolves it as unstable rather than regular or merely singular |
| older Regge/continuum response notes | test different supplied actions and source projections | current Record/EC flat-branch Hessian | no; dropped from proof support |

No mismatched prior no-go is used as evidence.

### N5 — Rhetoric Audit

| resolution | executed statement | untested boundary |
|---|---|---|
| per element | all ten EC ray labels and all 100 ordered Record bond contacts | no arbitrary continuous label carrier |
| per site | every six-neighbor conditional environment through the two-orbit Jensen--Holder bound | no fluctuating coframe conditional |
| per mode | the one normalized isotropic `B_i=J_(i,3)/sqrt(3)` zero-momentum mode | not all eighteen uniform modes or nonzero momenta |
| per block | complete geometry, Record-contact, covariance-sign, and EC contributions in that directional Hessian | not a full matrix spectrum or stable nonflat Hessian |
| lattice wide | every finite periodic `L>=3` carrier and the unique fixed-background Record phase | no continuous joint coframe/link Gibbs phase |

The note says “one negative physical zero-momentum direction,” never “all
connection modes are negative” or “gravity is impossible.” The runner cache
prints one substantive certificate line for each resolution.

### N6 — Partial-Closure Path Scan

The following escape/repair paths are preserved:

| path | current status | what it could close |
|---|---|---|
| modify or relationalize the fixed EC/Gram law | live next target | remove the negative flat mode and the Block-41 absolute spin-two intercept |
| derive an exact displacement Ward identity from a derivative-only geometry action | live | force the required `O(k^2)` tensor order without tuning an `O(k^0)` cancellation |
| locate and prove a stable nonflat joint phase | live but costlier | evade the flat-branch quantifier while retaining curvature coupling |
| explicit supplied-law import -> bounded theorem -> retirement audit | live governance path | license a successful geometry law without misclassifying a convention or selected model as a new ontology axiom |
| Lorentzian causal update after Euclidean repair | queued separately | close causal stability and permanent-Record evolution, which (6) does not address |

Existing scale and kinetic-isotropy primitives do not select an EC coefficient,
stable phase, or displacement Ward law. This note does not say “no retained
primitive supplies this” and does not say “a new axiom is required.” A model
law repair can close the immediate wall without changing ontology.

### N7 — Steelman

The strongest hostile counterargument is that the flat branch is the wrong
phase: the nonabelian EC term that destabilizes (2) may drive the joint law to
a stable nonflat stationary connection, and relaxing the coframes there could
produce a massless mixed metric/connection residue that no flat Hessian can
see. Block 38 already keeps nonflat translation-compatible carriers alive,
and Block 41 explicitly warned that nonflat and modified-law routes were not
closed. The actionable terminal obligation is therefore to construct such a
periodic/infinite-volume stationary phase, quotient its full Hessian, and
show the correct source residue, two tensor polarizations, absence of extra
unstable modes, and Lorentzian continuation. This steelman defeats a broad
law- or gravity-level no-go. It does not change the sign of the explicitly
evaluated flat-branch vector, so the present claim stays narrow and the
nonflat route is promoted to a live repair family rather than silently closed.

### N8 — Cross-Cycle Echo

Three similar lessons were checked.

1. Block 36's positive transported-ray escape defeated a broad finite-carrier
   no-go by changing the connection-aware law. The same mechanism class is
   preserved here as the modified/relational-law route.
2. Block 38 found that reduced homogeneous extrema need not solve full
   boundary-resolved equations and kept periodic/nonflat phases open. The
   present proof uses a periodic full local factor and makes no inference from
   reduced stationarity alone.
3. Block 41 left a singular connection quotient as a named escape rather than
   overclaiming regularity. The present calculation resolves only its unchanged
   flat branch; it does not transfer that resolution to modified or nonflat
   phases.

The prior broad-wall failures were retired by narrowing the carrier/law and
executing the missing connection terms. This note applies the same mechanism:
it narrows to one supplied branch, includes the complete directional contact
and covariance sign, and queues law repair rather than asserting axiom
necessity.

**Status: PASS.** N1 has seven normalized routes, N2 uses the collapsed
condition set, N3 finds no hidden wall, N4 drops mismatched witnesses, N5 is
resolution-scoped, N6 preserves non-axiom repair paths, N7 defeats the broad
claim and leaves the narrow theorem intact, and N8 imports the earlier
narrowing lesson. The primary runner cache is the landing N5 execution
certificate.

## Reproduction

```bash
python3 scripts/admissibility_periodic_flat_ec_connection_negative_mode_boundary_2026_08_11.py
```

Expected terminal summary:

```text
primary_pass=14
primary_fail=0
```

## Claim Boundary

Retained claim: every Block-40 proper-cubic homogeneous flat stationary Gram
of the unchanged supplied Block-38--40 law has the explicit physical
zero-momentum negative connection direction (2), with the uniform upper bound
(6), on every finite periodic `L>=3` carrier and in the Block-39 unique
fixed-background Record phase.

Not claimed: a full connection eigenvalue table, small-`k` dispersion,
stable nonflat phase, continuous joint geometry measure, Einstein tensor,
physical law selection, observed coefficient, Lorentzian update, gravity
no-go, axiom necessity, or axiom adoption.
