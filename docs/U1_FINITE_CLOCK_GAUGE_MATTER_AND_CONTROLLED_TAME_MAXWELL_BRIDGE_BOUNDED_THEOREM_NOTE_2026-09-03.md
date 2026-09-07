# Finite Clock Gauge-Matter Carrier and Controlled Tame-Maxwell Bridge

**Status:** proposed_retained
**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct finite-step parent:**
[`U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Hard-cutoff backreaction parent:**
[`U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Reversible-photon parent:**
[`U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Maxwell-generator parent:**
[`U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Kinetic normalization boundary:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)

**Runner:**
[`scripts/u1_finite_clock_gauge_matter_tame_maxwell_bridge_2026_09_03.py`](../scripts/u1_finite_clock_gauge_matter_tame_maxwell_bridge_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/u1_finite_clock_gauge_matter_tame_maxwell_bridge_2026_09_03.txt`](../logs/runner-cache/u1_finite_clock_gauge_matter_tame_maxwell_bridge_2026_09_03.txt)

## Result up front

A genuinely finite qubit payload can carry an exact gauge-matter law whose
controlled small-field tangent is three-dimensional Maxwell theory.

Put a `K`-state Weyl clock on each oriented link,

```text
Z X=omega X Z,               omega=exp(2 pi i/K),
X^K=Z^K=I.
```

Unlike the hard-cutoff raising operator, both `X` and `Z` are exactly unitary
and cyclic. For `K=2^q`, the complete link Hilbert space is exactly `q` qubits;
the clock phase factorizes over their binary digits and modular increment is a
reversible permutation of their basis states.

On a square carrying one charged hop, the finite Hamiltonian

```text
H_K
 =g^2/[2(dA)^2] sum_e (2-X_e-X_e^dag)
  +1/(2g^2) sum_f (2-W_f-W_f^dag)
  -t(Z_e |head><tail|+Z_e^dag |tail><head|),
dA=2 pi/K
```

is exact. Its electric, Wilson-face, and matter terms separately commute with
all modular Gauss generators for every tested `K=2,3,4,5,8`. On one bond,
exact finite-step evolution preserves both endpoint Gauss generators and
total charge while electric and hopping energies change by equal and opposite
amounts for `K=3,4,5,8,16`. On the complete `K=3` face, the joint
matter-electric-magnetic exponential is unitary, preserves all four Gauss
operators, and conserves its full energy.

The finite law has a controlled no-wrap sector. For electric modes `|m|<=2`,
the electric cosine approaches `E^2` with relative errors

```text
K=16      5.03587964e-2
K=32      1.27851692e-2
K=64      3.20863596e-3
K=128     8.02932461e-4,
```

falling as `K^-2`. The Wilson magnetic cosine has the usual quartic remainder
about `(curl A)^2`. With the convention `X=exp(-i dA E)`, a fixed
Gauss sector `G_v=omega^(-b_v)` imposes `div E-rho=b_v mod K`.
Only when the full residual `div E-rho-b_v` cannot wrap does this become
the additive equation `div E=rho+b_v`. The charged and wrap controls below
keep sector conservation distinct from the neutral constraint.

The quadratic tangent on a three-dimensional cubic torus is

```text
H_tame=(g^2/2)||E||^2+(1/(2g^2))||curl A||^2.
```

At every nonzero momentum on `L=3,4,5,7`, its curl kernel has one gauge-null
direction and exactly two degenerate transverse branches,

```text
omega(k)^2=4 sum_i sin^2(k_i/2).
```

They have unit-speed linear infrared dispersion, no Brillouin-corner doubler,
and covariance under all 48 signed cubic permutations. Reciprocal electric
and magnetic coefficients cancel `g` from the frequency.

Finally, a separately supplied finite-clock comparison oscillator uses the
quadratic stiffness at three representative transverse momenta. It is not
an established invariant sector or spectral reduction of the many-link clock.
Across `K=128,256,512,1024`, its discrepancy from the harmonic frequency
decreases. At `K=1024` the relative discrepancies for `L=8,16,32` are respectively

```text
0.159%, 0.166%, 0.256%,
```

and the ground-state probability near the angular branch edge is below
`1e-12`. At fixed `g=0.06`, further clock refinement leaves a nonzero
anharmonic discrepancy: the cosine-rotor comparison has gaps
`0.764916599742, 0.389730123464, 0.195583241400`, respectively.
Exact convergence to the harmonic frequencies is not claimed.

This is a positive finite-payload bridge. It removes the false choice between
“a finite local Hilbert space” and “a Maxwell tangent.” It does not yet prove
that the complete interacting many-link clock Hamiltonian is in its tame
Coulomb phase in the thermodynamic limit.

## 1. Exact finite link algebra

Use the clock basis `|a>`, `a=0,...,K-1`, and define

```text
Z|a>=omega^a|a>,             X|a>=|a+1 mod K>.
```

Then

```text
Z X=omega X Z,
Z^dag Z=X^dag X=I,
Z^K=X^K=I.
```

The runner verifies these matrix identities for `K=2,3,4,5,8,16`. This
carrier pays a different price from the hard-cutoff integer flux in the
parent: electric flux is modular rather than unbounded. It gains exact
unitarity of both link generators and has no top-flux state annihilated by a
raising operation.

For `K=2^q`, write `a=sum_j 2^j a_j`. The phase is

```text
omega^a=product_j exp(2 pi i 2^j a_j/K),
```

so `Z` factorizes into one-qubit phases. `X` is reversible modular binary
increment. The runner exhausts every basis value for `q=2,...,10` and checks
the phase factorization and increment/decrement inverse. This is an exact
register representation, not yet a homogeneous physical nearest-neighbor
compiler for the ripple/carry operation.

## 2. Exact modular Gauss symmetry with matter and magnetism

On the oriented square

```text
e_0: 0 -> 1,   e_1: 1 -> 2,   e_2: 3 -> 2,   e_3: 0 -> 3,
```

put

```text
W=Z_0 Z_1 Z_2^dag Z_3^dag.
```

The two-state matter factor carries one charge at either endpoint of `e_0`.
Let `M_0=diag(omega,1)` and `M_1=diag(1,omega)`. The modular Gauss generators
are

```text
G_0=X_0^dag X_3^dag M_0,
G_1=X_0 X_1^dag M_1,
G_2=X_1 X_2,
G_3=X_2^dag X_3.
```

They are commuting unitaries. In the oriented convention below,

```text
G_v=exp[-i dA (div E-rho)_v].
```

A chosen joint sector has eigenvalues `omega^(-b_v)`, for fixed integers
`b_v` modulo `K`. Their product is `omega I` on this one-particle closed
face, so `sum_v b_v=-1 mod K`; the sector with every `G_v=1` is absent.
For example, zero link flux with the particle at vertex 0 has
`b=(-1,0,0,0)`. A forward hop along edge 0 raises its oriented flux and moves
the particle to vertex 1, preserving that same sector. The background labels
are supplied sector data; they are not a derived physical background charge.
Commuting with `G_v` conserves each chosen sector and does not impose a
neutral Gauss constraint.

The charged forward hop is

```text
Z_0 tensor |1><0|.
```

The link Weyl phase from either endpoint Gauss operation cancels the matter
phase. The plaquette phases cancel corner by corner because the boundary of a
boundary is zero. Therefore each of

```text
H_E, H_B, H_hop
```

commutes with every `G_v`. The runner checks all `12` component/generator
commutators at each of `K=2,3,4,5,8`, on face Hilbert spaces up to dimension
`2*8^4=8192`.

The exact one-bond exponentials additionally verify real-time backreaction:
the modular Gauss operators and total matter number are invariant and

```text
Delta H_E=-Delta H_hop.
```

The current is group-valued at finite `K`; no globally additive Hermitian
electric operator is silently assigned to the full cyclic space. The additive
current/flux reading belongs only to the no-wrap sector below.

## 3. The controlled no-wrap sector

Choose centered integer representatives and the Fourier vectors

```text
|e> = K^(-1/2) sum_a exp(+i dA e a)|a>,
X|e> = exp(-i dA e)|e>,        Z|e> = |e+1 mod K>.
```

Thus `X=exp(-i dA E)`. Away from the wrap, the actual charged hop increases
both `E` and head number by one, in the parent's orientation. At `K=9`,
the runner tests `e=0, tail -> e=1, head` and both unchanged endpoint sector
phases `(omega,1)`. It rejects the opposite electric convention. The actual
`e=4, tail -> e=-4, head` wrap changes the centered electric representative
by `-8`, while head number changes by `+1`: modular Gauss survives, but a
globally additive flux/current identity does not.

The exact electric energy per link is

```text
g^2/(dA)^2 [1-cos(dA E)].
```

For a fixed bounded mode `m`, it approaches

```text
(g^2/2)m^2
```

with relative error `O((dA m)^2)=O(K^-2)`. The measured four-step ladder in
the result verifies that rate rather than merely displaying the Taylor
series.

Similarly,

```text
1/g^2 [1-cos(curl A)]
 =(1/(2g^2))(curl A)^2+O((curl A)^4).
```

The runner halves the face angle four times and observes the factor-16
quartic remainder.

For a chosen sector, the relevant integer residual is
`r_v=(div E)_v-rho_v-b_v`, not just the divergence. A sufficient bound is
`6 M+|rho_v|+|b_v|<K` when six incident links obey `|e|<=M`. Under it,

```text
r_v=0 mod K     iff     r_v=0.
```

The runner exhausts `5^6` electric assignments at `K=32,M=2`, each with
`rho_v in {0,1}` and `b_v in {-1,0,1}`. Thus `|r_v|<=14<32` for all
93,750 local charged/sector assignments. These local tests do not assert that
every combination assembles into a global one-particle sector. The separate
charged Fourier hop checks a consistent sector. Outside the bound, an
explicit assignment with divergence 32, charge 1 and background -1 has
residual 32 and zero modular residue; it is rejected as an additive solution.

## 4. The three-dimensional Maxwell tangent

For forward difference symbol

```text
q_i(k)=exp(i k_i)-1,
```

the three-dimensional curl symbol is cross product with `q`. Its positive
kernel is

```text
C(k)^dag C(k).
```

At every nonzero `k`, the runner obtains eigenvalues

```text
0, |q|^2, |q|^2,
|q|^2=4 sum_i sin^2(k_i/2).
```

The null vector is longitudinal gauge motion. The two positive vectors are
the two photon polarizations. Hamilton's equations from the quadratic tangent
give

```text
A_dot=g^2 E,
E_dot=-(1/g^2) C^dag C A,
A_double_dot=-C^dag C A,
```

so the frequency is independent of the supplied coupling `g`.

The complete momentum census on `L=3,4,5,7`, five independent controls, the
infrared ladder through `L=256`, and all 48 signed coordinate permutations
agree with the parent Maxwell generator. The new content is the controlled
map from an exact finite clock Hamiltonian to that tangent.

## 5. Separately supplied clock/rotor spectral comparison

A Taylor tangent need not describe low-energy states of the interacting
many-link carrier. To test a narrower comparison, the runner diagonalizes
the separately supplied `K`-state oscillator

```text
H_mode
 =g^2/[2(dA)^2](2-X-X^dag)
  +lambda/(2g^2)(2-Z-Z^dag),
lambda=4 sin^2(pi/L),
```

for `L=8,16,32`, `g=0.06`, and `K=128,256,512,1024`. Its harmonic target is

```text
omega=sqrt(lambda)=2 sin(pi/L).
```

The discrepancies from the harmonic comparison decrease across the named
four-point ladder, reaching the stated sub-percent values. This finite
observation is not exact harmonic convergence. At fixed positive `g`, the
angular continuum comparison is the periodic cosine rotor

```text
H_rotor=-(g^2/2) d^2/dA^2 + lambda/g^2 (1-cos A).
```

Its anharmonic potential remains under clock refinement. A separate Fourier
tridiagonal calculation on integer electric modes `-M,...,M`, at `M=100,200`,
changes each computed gap by less than `2e-10`. The rotor gaps quoted above
remain below the harmonic frequencies by approximately `0.05883%`,
`0.11546%`, and `0.23008%`. The finite-clock ladder's discrepancy from these
rotor gaps also decreases. This is a numerical cutoff-stability control,
not a rigorous eigenvalue error bound.

The harmonic width estimates distinguish two requirements:
`g^2/sqrt(lambda)` must be small for angular localization and
`2 pi/K << g/lambda^(1/4)` for angular grid resolution. Raising `K` alone
addresses neither the fixed-g anharmonic correction nor a physical many-link
phase. A separate small-g or joint-limit theorem remains open.

The `K=1024` ground states have angle second moments below `0.01`, now
checked and printed, and probability below `1e-12` for `|A|>3 pi/4`.
This comparison does not derive an invariant Fourier sector of the
interacting many-link model, its spectral reduction, or a thermodynamic phase.

## 6. What this changes and what remains

The payload question is materially improved:

```text
finite qubit register
    -> exact cyclic gauge link
    -> exact charge and plaquette symmetry
    -> controlled additive no-wrap sector
    -> two-polarization Maxwell tangent
    -> a separate finite-clock/rotor comparison with a fixed-g harmonic gap floor.
```

The hard-cutoff construction remains useful because it has an exact additive
flux operator throughout its finite window. The clock construction instead
has exact cyclic unitarity throughout the full finite space and recovers
additive flux only without modular wrap. They are complementary regulators,
not claims that one invalidates the other.

The next decisive target is the full microscopic phase: demonstrate, by a
controlled many-link bound or sign-free three-dimensional calculation, that a
nonempty low-energy sector of the exact finite clock Hamiltonian stays tame
and carries the two transverse gaps under volume and payload refinement. If
positive, that would promote this tangent bridge into a finite-payload photon
phase. If negative for one parameter window, other `K`, coupling, and quantum
spin-ice routes remain open.

The exact `q`-qubit register also still needs compilation into the framework's
homogeneous physical nearest-neighbor law. The user-approved scale reading
allows a collective link to occupy many smallest sites; this note counts the
qubits but does not build the local incrementer scaffold.

No axiom edit follows. The clock order, link role, Hamiltonian, couplings,
tame restriction, matter representation, and register layout are supplied.
Admissibility selection and permanent Record realization are untouched.

## 7. Program and prior-art boundary

The finite-clock Hamiltonian and tame Maxwell construction are standard
methodology, developed in detail by D. Radičević,
[“The Ultraviolet Structure of Quantum Field Theories. Part 3: Gauge
Theories”](https://arxiv.org/abs/2105.12751) (2021). That work explicitly uses
finite-dimensional `Z_K` links, obtains the tame Maxwell Hamiltonian, and
identifies `d-1` photon oscillators at each nonzero momentum. The Hamiltonian
lattice-gauge ancestor is J. Kogut and L. Susskind,
[“Hamiltonian formulation of Wilson's lattice gauge
theories”](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.395)
(1975).

The repo-specific contribution is not invention of clock gauge theory. It is
the executable junction to the current program: exact charged-hop and
Wilson-face Gauss symmetry on the same finite register, exact finite-step
component exchange, quantified no-wrap reduction, the complete three-
dimensional mode census in the parent's convention, and a payload-refined
exact reduced-mode spectral witness.

Open PR #7903 uses an integer-flux hard cutoff and studies static compact-link
matter blocks. It is context only and not imported. Open PR #7911 finds a
spin-half ring gapped but explicitly leaves the three-dimensional transverse
question open. This source uses a distinct finite-clock route and makes no
claim about that ring.

## 8. Executable evidence

The runner reports `TOTAL: PASS=27 FAIL=0`. It checks:

- exact Weyl algebra, cyclic unitarity, and absence of dark boundary states;
- exact binary phase and increment maps for `q=2,...,10`;
- face dimensions through `K=8`, Hermiticity, and nontrivial components;
- all component/Gauss commutators, commuting unitary generators, and their
  total-charge product phase;
- five exact one-bond finite-step Gauss, charge, and opposite-energy cases;
- complete `K=3` matter-electric-magnetic face unitarity, energy, and Gauss;
- the `K^-2` electric tame ladder and quartic magnetic ladder;
- exhaustive no-wrap Gauss equivalence and a modular-alias control;
- all momentum blocks on `L=3,4,5,7`, coupling cancellation, corner control,
  infrared refinement, and 48 cubic transformations; and
- twelve exact reduced-clock spectral solves plus final wavefunction
  localization.

## No-Go Discipline Gate

This is a positive finite-payload theorem with one deliberately unexecuted
many-link phase question. The gate prevents a controlled tangent from being
called a complete microscopic photon and prevents the open phase test from
being called a no-go.

### N1 — Alternative route enumeration

| Honesty | Route family | Outcome |
|---|---|---|
| **ATTEMPTED** | hard-cutoff integer-flux carrier | Parent route closes exact additive local work but has explicit boundary dark states. |
| **ATTEMPTED** | exact cyclic `Z_K` Weyl carrier | **Positive:** removes dark states and supports exact electric, magnetic, and matter gauge symmetry. |
| **ATTEMPTED** | charged no-wrap modular-to-additive reduction | **Positive in scope:** actual `K=9` charged sector/hop/wrap and exhaustive full residual at `K=32, |m|<=2`; no global additive reading. |
| **ATTEMPTED** | three-dimensional quadratic tangent | **Positive:** exactly two transverse branches at every nonzero tested momentum. |
| **ATTEMPTED** | supplied clock/rotor spectral comparison | **Bounded numerical witness:** harmonic discrepancies decrease below `0.26%` at `K=1024`, but fixed-g rotor gaps leave a nonzero anharmonic floor. |
| **ATTEMPTED** | binary qubit-register realization | **Positive algebraically:** exact phase and increment maps; physical local compiler not attempted. |
| **OPEN** | sign-free full 3D clock calculation | Could test the thermodynamic Coulomb phase directly; not executed here. |
| **OPEN** | quantum-spin-ice carrier | A distinct finite-qubit route to an emergent photon; not ruled out by any clock result. |
| **OPEN** | higher-order/local register compiler | Could realize modular increment through a larger physical scaffold; not tested here. |

The families differ in carrier algebra, terminal obligation, or spectral
object; they are not multiple wordings of one calculation.

### N2 — Wall-independence and collapse audit

“Tameness of the full low-energy lattice” and “the thermodynamic photon phase”
are not counted as two independent walls: the former is the proposed
mechanism for the latter and they collapse into `W1`.

```text
W1 = full many-link low-energy phase and volume/payload scaling,
W2 = homogeneous nearest-neighbor compiler for the q-qubit link register,
W3 = Admissibility selection and Record realization,
W4 = empirical electromagnetic identification and coupling normalization.
```

The following motivations do not prove both directions of every pairwise
non-implication. Those logical relations remain unresolved; no independent
wall count or stronger exclusion follows. The positive constructions and
partial witnesses elsewhere in this note retain their stated domains.

| Pair | Implication proved? | Independence proved? |
|---|---:|---:|
| W1, W2 | unresolved | unresolved |
| W1, W3 | unresolved | unresolved |
| W1, W4 | unresolved | unresolved |
| W2, W3 | unresolved | unresolved |
| W2, W4 | unresolved | unresolved |
| W3, W4 | unresolved | unresolved |

No impossibility is inferred from the collapsed set.

### N3 — Hidden-condition scan

The clock order, couplings, charge representation, square/cubic complexes,
tame mode window, reduced oscillator, and binary register are declared. The
full law's low-energy tameness is not assumed as a proved result. “Standard”
appears only in the non-load-bearing prior-art classification. The framework
is not said to provide the Hamiltonian or compiler. The fixed modular
sector/background labels are explicit supplied data; no physical background
field or charge law is derived. The word “exact” is confined to finite matrices,
exhaustive assignments, or algebraic momentum kernels actually checked.

### N4 — Residual matching

| Surface | Exact residual there | Match here |
|---|---|---|
| hard-cutoff backreaction parent | finite raising boundary | **alternative closure:** cyclic clock removes it but makes flux modular |
| magnetic-junction parent | one face joins matter and magnetism | **same local residual, new carrier:** repeated with exact clock links |
| reversible-photon parent | finite-depth noncompact field amplitudes | **tangent match:** finite clock supplies their quadratic curl/electric form |
| compact quadratic-basin PR #7884 | supplied classical compact action | **partial match:** exact quantum clock Hamiltonian and tame expansion supplied here |
| spin-half ring PR #7911 | no transverse geometry | **different residual:** no evidence for or against the 3D clock phase |
| compact matter PR #7903 | no quantum photon spectrum | **different regulator:** context only, no result imported |

No ring or one-face result is cited against the three-dimensional phase.

### N5 — Rhetoric and resolution audit

“Finite payload carries Maxwell” means an exact finite carrier plus its
conditional quadratic tangent and separately supplied clock/rotor comparison. It does not mean
the full many-link spectrum has been solved. “No dark boundary” is an exact
per-link clock statement. “Two transverse branches” is an exact per-mode
statement about the quadratic tangent. No thermodynamic conclusion is made.

The cached runner contains the five-resolution execution certificate:

```text
per_element: exact finite Weyl links, cyclic unitaries, and tame cosine errors are checked
per_site: modular Gauss generators, charged transport, and the no-wrap additive limit are checked
per_mode: two transverse branches, infrared speed, cubic covariance, and reduced clock spectra are checked
per_block: exact bond exchange and the complete K=3 matter-electric-magnetic face are checked
lattice_wide: the 3D quadratic tame tangent is resolved; the exact clock law's thermodynamic Coulomb phase is not executed
```

### N6 — Partial-closure paths and primitive boundary

No new axiom is required or proposed. `W1` is an ordinary supplied-model phase
calculation, approachable by a gauge-reduced exact diagonalization, controlled
bound, or sign-free Monte Carlo. `W2` is a physical compiler construction,
not new physics. The approved kinetic-isotropy primitive supplies only the
normalization boundary already used by the parent; it does not select this
clock law, its coupling, or its low-energy phase.

### N7 — Steelman

A hostile reviewer should reject the headline if it is read as proof that the
full microscopic clock lattice has a photon. The tame Hamiltonian is a
controlled restriction, and twelve reduced oscillator spectra do not prove a
many-body Coulomb phase. This objection is correct and fixes the next terminal
obligation: show volume- and payload-stable transverse gaps and tame weight in
the exact three-dimensional Gauss sector. It does not overturn the exact
carrier, gauge, component-energy, error-bound, or tangent results.

The reviewer should also point out that dimension matching to `q` qubits is
not a nearest-neighbor implementation of modular carry. Correct. A larger
scaffold or local auxiliary clock is still required, and the program's
zoomed-out object reading keeps that route open.

### N8 — Cross-cycle echo

The hard-cutoff campaigns repeatedly found that a finite link can close local
Gauss and work while leaving a payload boundary. This cycle changes the
carrier rather than rephrasing that wall: cyclic Weyl links remove the boundary
and expose modular aliasing as the replacement cost. The earlier role compiler
showed that collective edge/face roles can be embedded in physical neighbor
geometry; it does not automatically compile binary carry, so that step remains
named. The gapped spin-half ring is not echoed into three dimensions because
its own source explicitly lacks a transverse direction.

**Gate result:** PASS. Six distinct route families are executed, three remain
open, the dependent phase/tameness questions are collapsed, and no
thermodynamic or axiom no-go is shipped.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- the finite `X,Z` pair violates the Weyl or cyclic-unitarity identities;
- the qubit phase/increment maps fail for any tested register basis state;
- any displayed Hamiltonian component violates any modular Gauss generator;
- the Gauss generators fail to commute or carry the stated total-charge phase;
- one-bond evolution changes charge/Gauss or fails opposite component energy;
- the complete `K=3` face changes Gauss or full energy;
- electric or magnetic errors fail the stated refinement order;
- modular and additive Gauss differ inside the exhaustive no-wrap window;
- the three-dimensional tangent fails its mode count, dispersion, coupling
  cancellation, corner control, infrared limit, or cubic covariance;
- the named clock-comparison discrepancies fail their reported refinement
  ladder, or the rotor cutoff-stability/anharmonic-floor control fails; or
- the final reduced ground states have material angular branch-edge weight.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_finite_clock_gauge_matter_tame_maxwell_bridge_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=27 FAIL=0
```

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A selected electromagnetic law, physical matter/field identification and Record preparation/readout remain open."
source_of_blocker_text: "review_loop"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Review the corrected conditional source and establish the missing physical consumer before claiming framework closure."
conditional_surface_status: "Supplied finite Weyl links, one-particle Hamiltonian, reciprocal electric/magnetic coefficients, chosen modular sector/background and bounded no-wrap representatives; formal quadratic Maxwell kernel and separate fixed-coupling clock/rotor comparison, with harmonic convergence and the many-link tame phase open."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The result is a conditional mathematical theorem on supplied laws and finite domains; author status and a green runner grant no audit retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original source and receipts remain recoverable at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. The oriented Fourier convention is
corrected to X=exp(-i dA E), with explicit charged Gauss sectors and an actual
nonzero-charge no-wrap/wrap control. Fixed-g refinement is compared with the
cosine rotor and no longer claimed to converge exactly to a harmonic photon
gap. All runner timeouts and final input-bound receipts describe this
corrected source. The source status and trace above state the supplied
premises and open physical bridge. Independent review confirmation and
integration validation remain separate; no audit verdict or effective retained
status is asserted.
