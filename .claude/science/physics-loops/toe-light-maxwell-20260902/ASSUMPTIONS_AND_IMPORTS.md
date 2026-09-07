# Assumptions and imports

## Import ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---:|---:|---|---|
| `Z^3` nearest-neighbor carrier | spatial domain | framework baseline | `MINIMAL_AXIOMS_2026-06-29.md` | yes | yes | none | allowed |
| local complex phase redundancy | motivates compact `U(1)` links | bounded/current-source support | qubit-link and local-frame notes | yes for physical interpretation; no for lattice theorem | yes for physical Maxwell | derive a direct Admissibility-to-link bridge | open |
| compact `U(1)` Wilson action | supplies dynamics | supplied action surface | Wilson plaquette source class | yes | yes | derive from the fixed Admissibility rule or register an explicit non-derivation input through governance | conditional input |
| positive stiffness `beta>0` | energy/transfer positivity | admitted action parameter domain | Wilson action definition | yes | yes | show positivity from Admissibility probabilities | open outside action surface |
| common temporal/spatial coefficient | isotropic light cone | supplied Wilson action surface; adjacent primitive supplies graining form only | Wilson isotropy notes and `kinetic_isotropy_primitive` | yes for speed one | yes | prove gauge coefficient isotropy on the physical action surface | explicit boundary |
| periodic finite carrier | exact Fourier proof | admitted boundary convention | block definition | yes locally | no for continuum-local result | repeat with open boundary or local symbol proof | bounded convention |
| smooth zero-monopole branch | continuum Taylor limit | explicit sector/regularity condition | block definition | yes | yes for classical continuum | retain compact sectors separately; prove sector decoupling only if available | honest scope |
| physical EM identification | names the continuum field as light | unsupported bridge on current four-axiom surface | Lane 8A | yes for physical headline | yes | derive link/curvature/source identification | open |
| Record-readable field strength | observable interface | unsupported bridge | current Record axiom | no for field equations | yes for end-to-end observability | separate record-content composition theorem | excluded from this block |

No observed constant, fitted selector, `alpha(0)`, charge value, or `beta=6`
normalization is allowed as a proof input.

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| Wilson cosine potential is microscopic | another local even plaquette potential is selected | analytic `V(theta)` with `V''(0)>0` | Maxwell universality could remove Wilson-form dependence | live | 3 |
| stiffness is isotropic | temporal and spatial curvatures differ | `beta_t != beta_s` | yields a computed speed ratio and isolates the isotropy obligation | live control | 3 |
| continuum branch has no monopoles | compact defects survive the scaling family | `m_cube != 0` | requires Maxwell with magnetic current or a suppression theorem | live boundary | 2 |
| periodic boundaries are essential | use a finite open box | discrete relative cochains with boundary data | separates local bulk theorem from harmonic torus modes | live follow-on | 2 |
| overall `beta` must equal six | any positive stiffness is allowed | compare `beta=1,6,24` | tests whether Lane 8A is independent of gauge-coupling normalization | live | 3 |
| plaquette curvature is Record-readable | only individual site records are readable | no finite-record observable bridge | exposes the exact observability wall without changing field equations | live boundary | 2 |

The selected route combines the general-positive-stiffness and anisotropy
counterfactuals. The analytic-potential universality route is queued second.
