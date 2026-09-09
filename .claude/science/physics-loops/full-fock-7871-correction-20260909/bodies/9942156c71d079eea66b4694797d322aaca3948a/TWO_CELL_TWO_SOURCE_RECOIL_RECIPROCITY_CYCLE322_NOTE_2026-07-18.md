# Two-cell two-source recoil reciprocity — Cycle 322

Date: 2026-07-18
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.

## Result up front

Cycle 322 places two matter-controlled source vertices on the complete
Cycle-315 `M64 tensor M64` physical edge code. Each endpoint source is the
second-quantized coefficient-two direction-reversing vertex from Cycle 318.
The two vertices coexist with the Cycle-315 coin-FSWAP-contact update, preserve
both endpoint matter numbers locally at the source factors, preserve total
matter number through the complete update, and retain the nontrivial Cycle-230
contact block.

On the declared code space, in both endpoint roles,

```text
E_two-source G_two-source = G_physical,two-source E_two-source.
```

The maximum forward residual is `1.40923e-15`; the maximum conjugate inverse
residual is `2.55102e-15`. The 4,096-column seam remains isometric at `L=3,4`
and held `L=6`. The construction occupies 36 physical M2 per matter cell and a
97-M2 two-cell patch union: the inherited 29 M2 per cell, one endpoint
reservoir M2, and six mediator M2.

The shared source/field sector has global Q=1. Its basis consists of reservoir
`R_A`, reservoir `R_B`, or one directional mediator at one lattice cell. Thus
this cycle tests one response column at a time. It does not yet construct a
global-Q2 state in which both sources emit simultaneously.

With a symmetric one-one matter preparation and two update depths, the finite
occupation off-diagonal response matrix is identical for `L=3,4,6`:

```text
[[0.7712291018346235,    0.0006446410419510052],
 [0.0006446410419510054, 0.7712291018346235   ]].
```

The off-diagonal response is nonzero and its reciprocity residual is
`2.16840e-19`. Deleting the receiving source or mediator stream makes the
tested `A -> B` entry exactly zero. Unequal endpoint couplings leave the two
off-diagonal entries reciprocal but split the diagonal entries by
`0.07190144893576245`; this is the correct source-exchange asymmetry witness.

This is a common-code two-source reciprocity proxy. It is not energy, not
stress, not gravity, not metric response, and not time. Two update depths are
not a physical duration or rate. No Green function, force law, source tensor,
or metric equation is derived.

## Declared source law and exact local ledgers

For endpoint `X` in `{A,B}`, direction `d`, and its opposite `reverse(d)`, let
`c_X,d` be the local fermion annihilation operator. The exchange is

```text
T_X = sum_d (
        c^dagger_X,reverse(d) c_X,d tensor |F_X,d><R_X|
      + c^dagger_X,d c_X,reverse(d) tensor |R_X><F_X,d|
      ),

V_X(theta) = exp(+i theta T_X).
```

The endpoint active space has dimension `64 * 7 = 448`: every local fermion
occupation mask times one reservoir/mediator label. Pauli signs are evaluated
directly for all local Fock masks. The exchange has rank 112. The local checks
give

| control | residual |
|---|---:|
| `V_X^dagger V_X - I` | `1.44129e-15` |
| `[V_X,Q]` | `0` |
| `[V_X,N_X]` | `0` |
| `[V_X,P_x]` | `0` |
| `[V_X,P_y]` | `0` |
| `[V_X,P_z]` | `0` |
| maximum proper-cubic source covariance | `8.80775e-16` |

The coefficient-two vector ledger is

```text
P = P_matter + 2 P_mediator.
```

An active channel changes matter direction from `d` to `reverse(d)`, a vector
change `-2 e_d`, while its mediator branch carries `+2 e_d`. For every one of
the six direction inputs the emitted weight is
`0.1258992161287137...`, the matter response magnitude is
`0.2517984322574274...`, the weighted mediator response is the same, and the
balance residual is literal zero.

The coefficient is supplied. This cycle neither calibrates that diagonal
vector operator as physical momentum nor derives the coefficient from a
physical source law.

## Full-Fock seam and number structure

The matter code is the complete Cycle-315 `M64 tensor M64` seam with all local
occupation numbers `0,...,6` and total number `0,...,12`. The source factors
preserve both endpoint matter numbers individually:

```text
[V_A,N_A] = [V_A,N_B] = [V_B,N_A] = [V_B,N_B] = 0.
```

They commute with each other exactly. Their commutator with the Cycle-230
contact is `7.86448e-17`. Coin, edge FSWAP, and contact commute with total
matter number exactly. FSWAP can move matter across the endpoint split, so the
full update need not preserve `N_A` and `N_B` separately; it does preserve
their sum.

This distinction is load-bearing. The naive 36-dimensional product of two
one-particle local sectors has FSWAP leakage operator norm `1`. That route is
not closed under the actual Cycle-315 seam. Extending the source vertex over
all 64 local Fock states removes that leakage without changing the local
source formula.

The retained contact is nontrivial on 4,047 logical columns. Deleting it has
operator norm `1.9911500883709052`. A coarse one-one truncation would hide the
very higher-number sectors needed for the seam/contact theorem.

## Physical common-code lift

Cycle 315 supplies two physical edge-role encodings, `E_AB` and `E_BA`, and
their bounded matrix-unit completions. Cycle 322 attaches a local reservoir
and six local mediator M2 to each matter cell. Every global-Q1 label carries a
full 4,096-component matter seam vector. The physical source factor is the
same second-quantized endpoint matrix on each matching physical column and is
identity-completed off the declared code.

The logical factor order is

```text
matter coin
field coin
source A
source B
edge FSWAP
field stream
contact.
```

The physical lift uses the same order and the Cycle-315 local matter factors.
No global parity service, host-side occupation query, or global ordering is
added. Fermionic signs remain the bounded six-mode local signs already exposed
inside each M64 cell.

| edge role | Gram residual | forward EG | inverse EG | encoded norm | output norm |
|---|---:|---:|---:|---:|---:|
| `AB` | `0` | `1.40923e-15` | `2.55102e-15` | `0.9999999999999994` | `0.9999999999999999` |
| `BA` | `0` | `1.40923e-15` | `2.55102e-15` | `0.9999999999999994` | `0.9999999999999999` |

The physical completion remains a dense bounded edge matrix-unit lift. This
is an exact physical-code intertwiner, not a synthesis from a smaller named
primitive gate set.

## Size and support controls

| L | role | columns | physical rays | nonzeros | raw Gram max | minimum Gram eigenvalue |
|---:|---|---:|---:|---:|---:|---:|
| 3 | training | 4,096 | 63,488 | 65,536 | `1.77636e-15` | `0.9999999999999977` |
| 4 | training | 4,096 | 63,488 | 65,536 | `1.77636e-15` | `0.9999999999999982` |
| 6 | held | 4,096 | 63,488 | 65,536 | `1.77636e-15` | `0.9999999999999978` |

The Cycle-315 code uses 29 homogeneous M2 per cell and an 83-M2 two-cell patch
union. The source extension adds one reservoir plus six mediator M2 per cell,
for 36 installed M2 per cell and a 97-M2 patch union. The overhead is bounded
and constant per matter cell. At lattice size `L`, the source/field sector has
dimension `2 + 6 L^3` because global Q=1 is supplied.

## Emission, transport, and absorption

Every endpoint contains six matched source channels. Direct basis tests cover
emission, transport, and absorption at both endpoints, for 12 channels total.
Minimum and maximum emission weights are
`0.1258992161287137` and `0.12589921612871374`; conjugate absorption gives the
same interval.

The complete two-update response adds matter coin, mediator coin, both source
vertices, edge FSWAP, mediator stream, and contact. For source column `Y` and
reservoir observable `X`, define

```text
R_XY = <N_R_X> after two complete updates
```

from the symmetric one-one matter input and reservoir `R_Y`. The exact finite
matrices are:

| L | role | `R_AA` | `R_AB` | `R_BA` | `R_BB` | reciprocity residual | norm drift |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | training | `0.7712291018346235` | `0.0006446410419510052` | `0.0006446410419510054` | `0.7712291018346235` | `2.16840e-19` | `3.55271e-15` |
| 4 | training | same | same | same | same | `2.16840e-19` | `3.55271e-15` |
| 6 | held | same | same | same | same | `2.16840e-19` | `3.55271e-15` |

This off-diagonal response matrix is an occupation response after a supplied
two-update protocol. It is not an energy response, susceptibility, propagator,
or continuum source equation.

## Reciprocity, asymmetry, and deletions

Three independent interventions distinguish the measured response:

| intervention | observed discriminator |
|---|---:|
| delete receiving source `B` | `A -> B = 0` |
| delete mediator stream | `A -> B = 0` |
| set `theta_B = 1.17 theta_A` | diagonal source-exchange residual `0.07190144893576245` |

For unequal couplings the response is

```text
[[0.7712291018346235, 0.0008681390409184706],
 [0.0008681390409184706, 0.699327652898861 ]].
```

Its off-diagonal reciprocity residual remains zero. The intervention breaks
endpoint exchange in the diagonal responses, while reciprocal transport still
contains the product of the two endpoint amplitudes. Treating unequal coupling
as an off-diagonal nonreciprocity deletion would reject the actual finite
unitary result for the wrong reason.

Other destructive controls pass:

- zero source angle gives identity exactly;
- retaining only one conjugate half of the source exchange gives unitarity
  residual `5.268203128804968`;
- malformed `L<3`, `Q != 1`, missing-source, and invalid-edge declarations are
  all rejected;
- the naive one-one seam restriction leaks with norm `1`.

## Covariance and translation audit

The full Cycle-315 seam covers all 24 proper-cubic frames. Twelve preserve the
endpoint role and twelve implement endpoint reversal. The inherited complete
update covariance has processed residual zero and raw maximum
`2.16778e-16`; the local source factor maximum is `8.80775e-16`.

The edge-role group law passes 93,312 tests. The inherited `L=3` translated
edge-role census passes 4,374 tests. The full source family, with both source
cells translated together and the mediator labels translated on the torus,
commutes with all L=3 translations: 27 tests and maximum residual zero.

These are covariance tests of a family indexed by translated cells and proper
frames. The cell pair and response column are supplied test preparation, not
an autonomous source-selection result.

## Mass firewall and contact firewall

The Cycle-219 one-particle rest-mass fixture is unchanged:

| fixture | value |
|---|---:|
| Cycle-219 analytic mass | `0.4534056541748851` |
| two-cell seam mass | `0.4534056541748851` |
| uniform eigenvector residual | `3.85718e-16` |

This is the mass firewall. The source extension does not alter the matter coin
or its one-particle eigenfixture.

The contact firewall retains 4,047 nontrivial columns and contact-deletion norm
`1.9911500883709052`. The joint EG test includes the same contact factor.
Neither firewall promotes the response proxy to physical energy or gravity.

## Supplied structure, derived results, and open work

Supplied structure:

- the complete Cycle-315 `M64 tensor M64` AB/BA physical seam;
- the Cycle-219 matter coin, literal edge FSWAP, and Cycle-230 contact;
- shared global Q=1 over reservoirs `R_A`, `R_B`, and one directional mediator;
- two second-quantized coefficient-two matter-controlled source vertices;
- source angle, mediator coin/stream, factor order, and identity completion;
- symmetric one-one matter preparation, reservoir response column, and two
  update depths;
- periodic sizes `L=3,4,6`, with `L=6` held;
- dense bounded physical matrix-unit completion and response observable.

Derived here:

- exact local Q, coefficient-two vector, and endpoint matter-number identities;
- full-Fock coexistence with the coin-FSWAP-contact seam;
- exact AB and BA physical intertwiners;
- matched emission and conjugate absorption at both endpoints;
- nonzero same-code off-diagonal transfer and reciprocity;
- frame, endpoint-reversal, translation, held-size, deletion, mass, and contact
  controls.

Open:

- a global-Q2 simultaneous-emission sector;
- a full-Fock Cycle-320 unit-weight auxiliary source lift;
- a multi-edge source network and overlapping source recurrence;
- autonomous preparation or selection of source sites and response columns;
- an alternate mediator, paired mediator, or matter-rest branch;
- operational calibration to physical momentum, energy, stress, a source
  tensor, gravity, metric response, or time.

## TOE dependency ledger and maturity

| wall | Cycle-322 effect | remaining import |
|---|---|---|
| `C_ref` | two source columns and two receiver observables now share one physical edge code | symmetric matter state, reservoir column, two-update depth, and readout remain supplied |
| `C_num` | complete two-cell matter Fock space is combined with one reservoir-or-mediator excitation | global Q2, local source-sector preparation, and multi-edge higher-Q closure remain open |
| `C_wrap` | unchanged | factor schedule and update count do not provide physical clock time or rate |
| `C_int` | both coefficient-two source vertices coexist with coin-FSWAP-contact and preserve the exact operator ledgers | coefficient, coupling, source law, and unit-weight/full-Q alternatives remain supplied or open |
| `C_local` | two bounded physical source blocks now act on the same 97-M2 edge patch in both endpoint roles | primitive synthesis and overlapping multi-edge source recurrence remain open |
| `C_source` | a nonzero reciprocal two-source occupation response is derived on the common code | global Q2, autonomous source preparation, physical calibration, source tensor, and metric response remain open |

The result advances source integration without producing a physical gravity
law. A conservative planning update is:

| lane | integrated | strict floor | conditional | maturity |
|---|---:|---:|---:|---:|
| operational quantum / Records | 62% | 28% | 89% | 3.3/5 |
| causal time / clock | 34% | 17% | 62% | 1.8/5 |
| inertia / matter | 74% | 35% | 95% | 4.1/5 |
| gravity / source / resource | 40% | 16% | 67% | 2.1/5 |
| Born / probability / realized history | 34% | 14% | 85% | 2.0/5 |

The gravity/source change is limited to one percentage point integrated, two
conditional points, and one tenth maturity because the response is still a
dimensionless global-Q1 occupation proxy with supplied preparation.

## No-Go Discipline Gate

The broad candidate negative is that two recoil-balanced sources cannot share
the full Cycle-315 physical contact seam with a nonzero reciprocal response.
Cycle 322 is a bounded constructive counterexample on global Q=1. Stronger
negatives about global Q2, unit-weight auxiliaries, multi-edge recurrence,
preparation, or physical calibration have open routes.

Gate status: **FAIL / DO NOT SHIP** the broad negative. There is no shared
obstruction and no axiom pressure.

### N1 — alternative routes

| route | marker | actual disposition |
|---|---|---|
| two fixed matter-number reservoir sources | **ATTEMPTED** | earlier fixed-source response separates two endpoints but does not carry recoil through the complete Fock seam |
| naive one-one product of carried sources | **ATTEMPTED** | the 36-dimensional matter restriction has Cycle-315 FSWAP leakage norm `1` |
| full-Fock coefficient-two endpoint sources | **ATTEMPTED** | succeeds on the 4,096-state seam with AB/BA EG residual `1.40923e-15` and nonzero reciprocal response |
| full-Fock Cycle-320 unit-weight auxiliary sources | **OPEN / UNTESTED** | Cycle 320 gives a one-carrier 40-M2 auxiliary compiler, but no full-Fock two-source lift is implemented here |
| global-Q2 simultaneous emission sector | **OPEN / UNTESTED** | the tested response uses one shared reservoir-or-mediator excitation |
| asymmetric endpoint coupling | **ATTEMPTED** | diagonal exchange splits by `0.07190144893576245` while off-diagonal reciprocity remains exact |
| multi-edge source network | **OPEN / UNTESTED** | no overlapping source-edge recurrence or network response is compiled |
| alternate mediator or rest branch | **OPEN / UNTESTED** | no paired mediator, rest species, or altered stream law is implemented |

The successful route is sufficient for a common-code global-Q1 response
theorem. Four materially different stronger routes remain open.

### N2 — wall-independence audit

The collapsed walls for a stronger source theorem are:

- `W_Q2`: compile simultaneous source-sector occupation beyond global Q=1;
- `W_aux`: compile or retire the Cycle-320 unit-weight auxiliary on full Fock;
- `W_multiedge`: extend the source seam to overlapping edges;
- `W_prepare`: derive local source placement and response preparation;
- `W_energy`: calibrate an operational energy/stress/source law.

| pair | closing first automatically closes second? | closing second automatically closes first? | independent? |
|---|---|---|---|
| `w_q2`, `w_aux` | no | no | yes |
| `w_q2`, `w_multiedge` | no | no | yes |
| `w_q2`, `w_prepare` | no | no | yes |
| `w_q2`, `w_energy` | no | no | yes |
| `w_aux`, `w_multiedge` | no | no | yes |
| `w_aux`, `w_prepare` | no | no | yes |
| `w_aux`, `w_energy` | no | no | yes |
| `w_multiedge`, `w_prepare` | no | no | yes |
| `w_multiedge`, `w_energy` | no | no | yes |
| `w_prepare`, `w_energy` | no | no | yes |

Global Q2 does not choose the auxiliary law. A full-Fock auxiliary does not
build overlapping edge recurrence. Multi-edge recurrence does not derive
source preparation. Preparation does not calibrate energy. No directed
implication collapses another wall.

### N3 — hidden-wall scan

The executable literal scan covers the note and runner and reports zero hits.
Every load-bearing choice is listed in the supplied inventory: matter code,
reservoirs, mediator field and vacuum, global Q=1, source angle, coefficient,
factor order, source cells, two-update preparation, physical completion,
periodic sizes, and response observable.

### N4 — residual matching

| exact witness | inherited residual or boundary | Cycle-322 use | match? |
|---|---|---|---|
| `PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md:26` | complete `M64 tensor M64` Fock space | declared matter code | yes |
| same file, line 172 | covariant coin-FSWAP-contact update | retained seam factor | yes |
| same file, line 169 | 12 preserved and 12 reversed endpoint roles | source family covariance target | yes |
| `PROPER_CUBIC_RECOIL_BALANCED_CARRIED_SOURCE_CYCLE318_NOTE_2026-07-18.md:57` | relative mediator coefficient supplied | exact coefficient-two endpoint ledger | yes |
| `UNIT_WEIGHT_CARRIED_LINK_RECOIL_CYCLE320_NOTE_2026-07-18.md:38` | every direction contribution has unit weight | open alternate full-Fock route | yes |

The one-one leakage is used only against the naive restricted product. It is
not used against a different higher-number source-sector encoding. The
global-Q1 result is not used against global Q2, and the coefficient-two success
does not rule out the unit-weight auxiliary route.

### N5 — rhetoric audit

“Not energy,” “not gravity,” and the other interpretation boundaries state
what the executed observables do not establish. They are not impossibility
claims. The runner computes occupation weights, diagonal direction ledgers,
and finite update responses. It does not test a translation generator,
continuum tensor, physical calibration, or metric equation.

The naive one-one failure is route-specific FSWAP leakage. It is not evidence
against the complete Fock construction, which succeeds, or against a future
global-Q2 code. The full-Fock Cycle-320 route is open because no such code was
built, not because its auxiliary mechanism failed.

### N6 — partial-closure paths

Live constructive paths include:

- form a global-Q2 reservoir/field sector and retest simultaneous emissions;
- second-quantize the Cycle-320 unit-weight auxiliary vertex over local Fock;
- tile the source-edge lift over adjacent edges and test overlap commutators;
- replace the mediator by a paired branch or independent matter-rest column;
- derive a source preparation/readout protocol from retained operational
  resources;
- add an independently calibrated physical response observable.

Each path could retire a distinct import without axiom language.

### N7 — hostile steelman

A hostile reviewer should reject any claim that coefficient two, 36 M2 per
cell, 97 M2 per edge patch, or global Q=1 is necessary. Cycle 320 supplies a
different one-carrier unit-weight mechanism, and its full-Fock lift remains
open. A global-Q2 sector can add simultaneous emission content. A paired
mediator or rest branch can alter the vector ledger. Multi-edge completions can
change the physical support accounting. Cycle 322 proves one sufficient
common-code response construction, not uniqueness or minimality.

The reviewer should also reject a gravity interpretation. Reciprocal finite
occupation transfer can arise in a unitary lattice model without an energy
calibration, stress/source tensor, force law, or metric response.

### N8 — cross-cycle echo

The recent constructive sequence repeatedly closes the residual at its actual
code level:

- Cycle 312 extended bounded matter blocks over local Fock;
- Cycle 315 joined two complete Fock cells with FSWAP and contact;
- Cycle 318 obtained a proper-cubic coefficient-two recoil ledger;
- Cycle 320 exhibited a unit-weight one-carrier alternative with local
  auxiliary support;
- Cycle 322 second-quantizes the coefficient-two source at both endpoints of
  the complete seam and measures common-code reciprocity.

That sequence leaves live paths for global Q2, unit-weight full Fock,
multi-edge recurrence, and operational calibration. The broad gate remains
**FAIL / DO NOT SHIP**.

## Optimal next campaign

The sharpest next test is a full-Fock Cycle-320 unit-weight two-source lift on
the same Cycle-315 seam. It should demand exact local Q/vector/number
commutators, AB/BA physical intertwining, contact preservation, nonzero
two-source response, all frames, endpoint reversal, translations, held sizes,
deletions, and the same interpretation firewalls. That experiment directly
tests whether coefficient two can be retired without losing the newly closed
common-code response.

In parallel priority, a global-Q2 source/field sector should test genuine
simultaneous two-source emission. Neither campaign is an axiom request.

## Verification

```text
python3 scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py
```

Final local result: `20 PASS / 0 FAIL`,
`RESULT TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CERTIFIED`.
