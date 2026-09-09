# Unit-weight carried-link recoil — Cycle 320

Date: 2026-07-18
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.

## Result up front

Cycle 320 compiles a direction-changing carried-link source through the full
Cycle-316 recurrent physical schedule. It adds six auxiliary direction M2 per
cell, bringing the installed total from 34 to 40 M2 per cell. The local source
channels are

```text
|E,d>  <->  |G,reverse(d); F,d; A,d>.
```

Here `F` is the mediator direction and `A` is a locally constrained auxiliary
direction carried on the matter cell. The source vertex exactly conserves

```text
Q = N_source + N_field,
P = P_matter + P_mediator + P_aux,
[V,Q] = [V,P_x] = [V,P_y] = [V,P_z] = 0.
```

Every direction contribution has unit weight. The local 222-dimensional
vertex has exact unitarity, exact operator commutators, and exact covariance
under all 24 proper-cubic frames. On every incoming direction eigenstate the
matter recoil magnitude is `0.2517984322574276`; mediator and auxiliary each
carry `0.1258992161287137` in the opposite balance, with literal zero residual.

The recurrent physical code satisfies

```text
E_link G_link = G_physical,link E_link.
```

The maximum intertwining residual is `8.79e-16` on `L=3,4` and held `L=6`.
The same bounded matter blocks transport the matter port, source tag, and
auxiliary direction together. Emission, transport, and absorption, overlapping
translated source blocks, all frames, all translations, held sizes, deletion
controls, and mass/contact firewalls pass.

This removes Cycle 318’s supplied relative coefficient two from the retained
kinematic ledger, but replaces it with supplied auxiliary content: six M2 per
cell, an identity auxiliary coin, unit auxiliary direction weight, and a
matter-carried catch-up law. The result is dimensionless direction/flux
transfer. It is not physical momentum, not work, not energy, not stress, not
source selection, and not gravity or metric response.

## Exact unit-weight vertex

Let `e_d` denote a proper-cubic unit direction. Define the three vector
operators on the ground-plus-field-plus-auxiliary branch by

```text
P_matter |G,m;F,f;A,a> = e_m |G,m;F,f;A,a>,
P_mediator |G,m;F,f;A,a> = e_f |G,m;F,f;A,a>,
P_aux |G,m;F,f;A,a> = e_a |G,m;F,f;A,a>.
```

On the excited branch `P_matter|E,d> = e_d|E,d>` and the other two terms
vanish. For the active channel,

```text
e_reverse(d) + e_d + e_d = -e_d + e_d + e_d = e_d.
```

Thus the coefficient-two mediator term in Cycle 318 is resolved into one
mediator direction plus one independent auxiliary direction, each with unit
weight. The exchange and vertex are

```text
T_link = sum_d ( |G,reverse(d);F,d;A,d><E,d| + h.c. ),
V_link(theta) = exp(+i theta T_link).
```

The executed local controls are:

| control | residual |
|---|---:|
| local active dimension | `222` |
| unitarity | `0` |
| `[V_link,Q]` | `0` |
| `[V_link,P_x]` | `0` |
| `[V_link,P_y]` | `0` |
| `[V_link,P_z]` | `0` |
| maximum 24-frame covariance | `0` |

For a basis input `d`, the expectation response is

```text
Delta P_matter = -2 sin(theta)^2 e_d,
P_mediator     =    sin(theta)^2 e_d,
P_aux          =    sin(theta)^2 e_d.
```

At the selected angle, these magnitudes are `-0.2517984322574276`,
`0.1258992161287137`, and `0.1258992161287137`. The balance residual is zero
for all six directions. This is nonzero matter recoil and exact unit-weight
operator balance, not an isotropic expectation cancellation.

## Why the previous link comparator was insufficient

Cycle 318 also tested a direction-preserving link vertex. That route couples
an excited direction `d` to matter direction `d`, mediator `f`, and auxiliary
`reverse(f)`. It has exact unit-weight P because mediator and auxiliary cancel,
but the matter-direction commutators are all zero. It balances an auxiliary
ledger without recoiling matter.

Cycle 320 changes the channel rather than relabeling that result. Matter flips,
while mediator and auxiliary both take direction `d`. The direction-preserving
link remains a useful deletion/control route, not the recurrent theorem.

## Recurrent logical code

The declared logical sector contains exactly one matter carrier and prepared
`Q=1`. Its branches are

```text
excited/no-field/no-auxiliary:
    amplitude psi_e(x,d),

ground/one-field/one-auxiliary:
    amplitude psi_gfa(x,y;m,f,a).
```

The matter and mediator receive the inherited Cycle-219 and Cycle-214 coins.
The auxiliary direction receives an identity coin. Matter streams by `m`, the
mediator streams by `f`, and the auxiliary direction label moves with the
matter body rather than streaming independently. The onsite source vertex acts
only on the correlated `m=reverse(d), f=d, a=d` channels and identity-completes
the remaining 210 local active states.

The auxiliary conditions are local on the declared code:

- no auxiliary M2 is occupied on the excited branch;
- exactly one auxiliary direction M2 is occupied on the ground/field branch;
- its cell equals the matter carrier cell;
- the bounded matter block carries its direction label to the output cell;
- the source vertex creates or removes it together with the mediator.

These conditions and the global one-carrier/Q1 sector are supplied code
structure, not autonomous preparation results.

## Physical 40-M2 encoding

Cycle 320 extends the Cycle-316 physical columns:

```text
excited:
    E_312 |x,d> tensor |port=x,d> tensor |source=x>
                    tensor |field vacuum> tensor |aux vacuum>,

ground/field/auxiliary:
    E_312 |x,m> tensor |port=x,m> tensor |source vacuum>
                    tensor |field=y,f> tensor |aux=x,a>.
```

The last factor uses six new physical M2 per cell. Each source factor is

```text
L_x(V_link) = I + Phi_x (V_link-I) Phi_x^dagger,
```

with six excited columns and 216 ground/field/auxiliary columns. The source
factor is applied homogeneously at every cell. No state-dependent selection and
no host carrier query occurs.

Matter coin, reverse, and outer-edge block lifts preserve the field direction
and auxiliary direction while changing the matter port. Their output columns
relocate the auxiliary M2 to the new matter cell. The mediator coin and stream
act on the mediator M2 only. This gives literal source/tag/auxiliary catch-up
inside the same bounded physical grammar.

The cold recurrent table is:

| L | status | matter Gram | `E_link G_link - G_physical,link E_link` | largest local P residual |
|---:|---|---:|---:|---:|
| 3 | training | `4.45e-16` | `8.49e-16` | `1.22e-16` |
| 4 | training | `4.45e-16` | `8.79e-16` | `7.08e-17` |
| 6 | held | `4.45e-16` | `8.34e-16` | `8.10e-17` |

The maximum encoded-output norm drift is `9.55e-15` at held `L=6`. The test
states contain coherent excited amplitudes, onsite 216-component link
amplitudes, and separated 216-component link amplitudes.

## Emission, transport, and absorption

An excited scalar input emits total mediator/link occupation
`0.1258992161287138`. The mediator moves one edge along `d`; recoiling matter
and its auxiliary direction label move one edge along `reverse(d)`. Each of the
six mediator target cells receives `sin(theta)^2/6`, and each corresponding
matter-target/auxiliary-direction pair receives the same weight. Both maximum
errors are `6.94e-18`.

The physical source plus matter and mediator streams agree with the encoded
logical result to `5.43e-16` on `L=3,4,6`. The conjugate onsite input

```text
sum_d |G,reverse(d);F,d;A,d> / sqrt(6)
```

restores source weight `0.1258992161287138` and leaves link-sector weight
`0.8741007838712865`. This is the conjugate absorption channel, not a claim
that every freely propagated packet returns.

If a translated matter column and port are placed at the target cell while the
auxiliary M2 is left at the origin, measured code leakage is one. The full
source/tag/auxiliary catch-up residual is `5.43e-16`; deletion shows the
auxiliary transport is operational.

## Overlap, covariance, translations, and support

Adjacent translated 222-state source blocks inherit the overlapping
Cycle-312 coefficient patches:

| control | result |
|---|---:|
| shared physical pair rows | `14` |
| opposite-order source-block residual | `0` |
| measured lawful-code leakage | `2.97e-16` |

The full link-source, coin, matter-stream, and mediator-stream update passes
all 24 proper-cubic frames with maximum residual `1.93e-16`. All L=3
translations (27 origins) have zero residual. `L=6` is held out.

The overhead inventory is:

| item | count/envelope |
|---|---:|
| inherited Cycle-316 M2 per cell | `34` |
| added auxiliary direction M2 per cell | `6` |
| installed M2 per cell | `40` |
| source active dimension | `222` |
| maximum inherited physical pair rows per block | `36` |
| two-cell patch envelope | `254 M2` |

The 254-M2 envelope is the Cycle-316 242-M2 two-cell envelope plus twelve
auxiliary M2 on two cells. It is an observed constant support bound, not a
minimum theorem.

## Matter-rest comparator

The bounded rest candidate tested here is the proper-cubic scalar
superposition of the six existing matter direction columns at one cell:

```text
|rest_x?> = sum_d E_312 |x,d> / sqrt(6).
```

The actual Cycle-312 matter stream sends its six components to six neighboring
cells. Its logical stationarity residual is exactly `sqrt(2)` at `L=3,4,6`,
and the encoded physical residual matches to floating precision. Thus this
specific six-port column is not a stationary rest output.

This does not rule out an independent physical rest column, a multi-cell
stationary dressing, or a paired-mediator branch. Those remain open. The
failure is a route-specific comparator, not minimum-content evidence.

## Mass firewall, contact firewall, deletions, and domain

The mass firewall remains source-off. At zero coupling the 222-state source
vertex is identity, the auxiliary sector does not fire, and the inherited
Cycle-219 mass fixture remains:

| L | source-off fixture |
|---:|---:|
| 3 | `0.4534056541748850` |
| 4 | `0.4534056541748858` |
| 6 held | `0.4534056541748896` |

No interacting mass shift is inferred from the direction/flux ledger.

The contact firewall is one-carrier exact. The lawful code has one matter
carrier, performs zero Cycle-230 contact calls, and cannot exercise recurrent
multiparticle contact.

Executed controls:

- coupling removed: identity residual `0`;
- conjugate source half removed: unitarity residual `1.297185990748149`;
- auxiliary term removed from P: commutator `0.709645590780958`;
- auxiliary catch-up removed: leakage `1`;
- direction-preserving link route: exact P but matter recoil commutator `0`;
- malformed `L`, matter number, Q, source/port tag, and auxiliary-cell tag:
  five rejections.

## Supplied, derived, and open inventory

Supplied structure:

- the Cycle-316 one-carrier physical matter/source/mediator code;
- six auxiliary direction M2 per cell and their one-hot lawful branch;
- the direction-changing link source vertex and coupling;
- unit direction weights for matter, mediator, and auxiliary;
- identity auxiliary coin and matter-carried auxiliary catch-up;
- prepared one-carrier/Q1 sector, factor schedule, identity completion, and
  finite periodic test volumes.

Derived here:

- exact unit-weight local operator Q/P identities;
- nonzero matter recoil balanced separately by mediator and auxiliary flux;
- exact 40-M2 recurrent physical intertwiner through held `L=6`;
- emission, mediator transport, auxiliary catch-up, and absorption;
- overlap compatibility, covariance, held-size behavior, and deletion
  residuals.

Open:

- independent physical matter-rest or paired-mediator completion;
- derivation or operational selection of the auxiliary field and its law;
- simultaneous matter carriers, recurrent contact, and full Fock;
- two matter sources and same-code reciprocity;
- physical calibration as momentum, work, energy, stress, gravity, or metric.

## TOE dependency ledger and maturity

| wall | Cycle-320 effect | remaining import |
|---|---|---|
| `C_ref` | unchanged | fixed reference, prepared one-carrier/Q1 sector, and response readout supplied |
| `C_num` | unchanged | simultaneous carriers, higher Fock, cross-number reference, and local preparation |
| `C_wrap` | unchanged | factor schedule and update count are not clock time or rate |
| `C_int` | Cycle-318 coefficient two is replaced by a unit-weight three-part operator ledger on the recurrent code | auxiliary identity/law, coupling, recurrent contact, and multiparticle extension supplied/open |
| `C_local` | a six-M2 local auxiliary constraint and catch-up are compiled through overlapping translated blocks | primitive factor synthesis, multiparticle overlap/contact, and full Fock |
| `C_source` | exact unit-weight dimensionless matter/mediator/auxiliary recoil transfer | auxiliary/source selection, physical calibration, energy/stress/tensor, and metric response |

Removing the coefficient two is a genuine kinematic cleanup, but the auxiliary
law is new supplied candidate content. Scores therefore stay at the current
post-Cycle-315/Cycle-318 planning baseline:

| lane | integrated | strict floor | conditional | maturity |
|---|---:|---:|---:|---:|
| operational quantum / Records | 61% | 27% | 87% | 3.2/5 |
| causal time / clock | 34% | 17% | 62% | 1.8/5 |
| inertia / matter | 73% | 34% | 94% | 4.0/5 |
| gravity / source / resource | 39% | 16% | 65% | 2.0/5 |
| Born / probability / realized history | 33% | 14% | 82% | 1.8/5 |

## No-Go Discipline Gate

The broad candidate negative is that unit direction weights cannot support a
proper-cubic recoil-balanced source on the recurrent physical code. Cycle 320
is a bounded 40-M2 counterexample. Broader claims about auxiliary necessity,
minimum overhead, rest modes, paired mediators, multiparticle sources, or
physical calibration remain premature.

Gate status: **FAIL / DO NOT SHIP** the broad negative. There is no shared
obstruction and no axiom pressure.

### N1 — alternative routes

| route | marker | actual disposition |
|---|---|---|
| Cycle-316 direction-preserving source | **ATTEMPTED** | exact Q but unit-weight matter-plus-mediator P commutator `0.721479` |
| Cycle-318 coefficient-two recoil source | **ATTEMPTED** | exact recurrent recoil balance with no added M2, but relative coefficient two supplied |
| direction-preserving link reservoir | **ATTEMPTED** | exact local unit-weight P with six auxiliary M2 but zero matter recoil |
| direction-changing carried-link source | **ATTEMPTED** | exact unit-weight Q/P, nonzero recoil, and full 40-M2 recurrent compiler |
| uniform six-port rest-column candidate | **ATTEMPTED** | bounded scalar column has actual stream stationarity residual `sqrt(2)` through held `L=6` |
| independent physical matter-rest column | **OPEN / UNTESTED** | no extra stationary physical rest species is constructed |
| paired-mediator unit-weight branch | **OPEN / UNTESTED** | no two-mediator source sector or transport compiler is built |
| simultaneous-carrier recoil/contact splice | **OPEN / UNTESTED** | the retained code has one matter carrier and cannot fire contact |

Eight distinct routes are exposed. The principal carried-link route succeeds,
and three materially different extensions remain open.

### N2 — wall-independence audit

The collapsed walls for a stronger physical-source theorem are:

- `W_aux`: derive or operationally select the auxiliary field and its law;
- `W_rest`: construct an independent recurrent rest/paired alternative;
- `W_multi`: compile simultaneous matter carriers;
- `W_contact`: compile recurrent contact on that code;
- `W_energy`: calibrate an operational energy/stress/source law.

| pair | closing first automatically closes second? | closing second automatically closes first? | independent? |
|---|---|---|---|
| `W_aux`, `W_rest` | no | no | yes |
| `W_aux`, `W_multi` | no | no | yes |
| `W_aux`, `W_contact` | no | no | yes |
| `W_aux`, `W_energy` | no | no | yes |
| `W_rest`, `W_multi` | no | no | yes |
| `W_rest`, `W_contact` | no | no | yes |
| `W_rest`, `W_energy` | no | no | yes |
| `W_multi`, `W_contact` | no | no | yes |
| `W_multi`, `W_energy` | no | no | yes |
| `W_contact`, `W_energy` | no | no | yes |

Removing auxiliary content via a rest mode need not compile multiple carriers.
A multiparticle code need not choose contact, and contact need not calibrate
energy. No directed implication collapses another wall.

### N3 — hidden-wall scan

The executable literal scan covers the note and runner and reports zero hits.
Every load-bearing choice appears in the supplied inventory: auxiliary M2,
one-hot sector, vertex, coupling, identity auxiliary coin, carried catch-up,
one-carrier/Q1 sector, factor schedule, and observables.

### N4 — residual matching

| exact witness | witness residual | Cycle-320 use | match? |
|---|---|---|---|
| `PROPER_CUBIC_RECOIL_BALANCED_CARRIED_SOURCE_CYCLE318_NOTE_2026-07-18.md:57` | coefficient two supplied | normalization target | yes |
| same file, line 71 | recurrent auxiliary compiler absent | exact compiler built here | yes |
| same file, line 143 | unit-weight rest route open | six-port rest comparator | yes |
| `CARRIED_SOURCE_RECURRENT_TAGGED_BLOCK_CYCLE316_NOTE_2026-07-18.md:171` | simultaneous carriers outside code | multiparticle boundary | yes |
| `PHYSICAL_CYCLE269_LOCAL_FOCK_EXTENSION_CYCLE312_NOTE_2026-07-18.md:171` | translated simultaneous patches open | higher-number boundary | yes |

The six-port rest residual is not used against an independent rest species or
multi-cell dressing. The direction-preserving link result is not used against
direction-changing link channels.

### N5 — rhetoric audit

“Not physical momentum” is an interpretation firewall: the tested object is a
local diagonal unit-direction operator plus finite-volume currents. No
translation-generator equivalence, scattering calibration, continuum tensor,
or energy relation is tested. The negative phrase does not assert that future
operational calibration is impossible.

The failed rest result is tested for one bounded scalar superposition at the
logical-column and encoded-physical-column resolutions through `L=6`. It is not
tested for an independent rest M2, multi-cell dressing, or altered matter
stream. The note keeps those resolutions open.

The contact boundary is only for the one-carrier Cycle-320 code. It says
nothing negative about the retained fixed-seam Cycle-230 block.

### N6 — partial-closure paths

Live import-retirement paths are:

- replace the auxiliary by an independent stationary matter-rest column;
- replace it with a locally compiled paired-mediator sector;
- derive the auxiliary law from a retained operational symmetry/current;
- extend Cycle-311/312 translated blocks to simultaneous carriers;
- add two carried sources and test same-code reciprocity.

These are constructive physics paths, not automatic axiom requests. No axiom
language is drafted.

### N7 — hostile steelman

A hostile reviewer should reject any claim that six auxiliary M2 or 40 total
M2 are necessary. The tested six-port rest superposition fails because the
existing stream disperses it, but an independent rest species, a multi-cell
stationary dressing, or a paired mediator could close unit normalization with
different content. The coefficient-two Cycle-318 theorem already closes recoil
with no extra M2 if weighting is allowed. Cycle 320 proves one sufficient
unit-weight compiler, not uniqueness or minimality.

### N8 — cross-cycle echo

This campaign repeatedly retired walls by changing content at the exact
residual:

- Cycle 295 carried source capacity with matter;
- Cycle 312 replaced the global one-carrier projector with bounded blocks;
- Cycle 316 compiled carried source response recurrently;
- Cycle 318 changed source channels to obtain operator recoil balance;
- Cycle 320 splits the coefficient-two flux into mediator and auxiliary unit
  contributions and compiles the auxiliary catch-up.

The same mechanism remains available for rest, paired-mediator, and
multiparticle routes. The broad gate remains **FAIL / DO NOT SHIP**.

## Optimal next campaign

The sharpest local discriminator is now auxiliary retirement: construct an
independent physical rest column or paired-mediator branch and demand the same
unit-weight operator ledger, nonzero recoil, recurrent physical intertwiner,
overlap, frame, translation, held-size, deletion, and firewall controls. That
would test whether the six added M2 and identity auxiliary coin are avoidable.

The higher framework priority remains simultaneous carriers. A higher-number
recurrent compiler is required before the recoil/source result can exercise
Cycle-230 contact, two matter sources, or same-code reciprocity.
