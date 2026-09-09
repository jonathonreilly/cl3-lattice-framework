# Gauge-Invariant Effect, Instrument, and Wilson-Generator Normalization Boundary

**Date:** 2026-09-02; corrected 2026-09-09
**Type:** bounded_theorem
**Status:** proposed_retained
**Status authority:** independent audit only. This note sets no audit verdict,
retires no obligation, and changes no TOE percentage.
**Primary runner:**
[`scripts/gauge_invariant_effect_instrument_generator_boundary_2026_09_02.py`](../scripts/gauge_invariant_effect_instrument_generator_boundary_2026_09_02.py)
**Cached receipt:**
[`logs/runner-cache/gauge_invariant_effect_instrument_generator_boundary_2026_09_02.txt`](../logs/runner-cache/gauge_invariant_effect_instrument_generator_boundary_2026_09_02.txt)

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-carrier effect and instrument results, plus conditional full-L2 Wilson operator and plane-weight results on explicitly supplied structures."
conditional_surface_status: conditional-support
trace_class: negative_route_pruning
target_claim_id: g_bare_parent_finite_link_wilson_beta6_bridge_note_2026-06-18
target_blocker_text: "Derive, rather than assign, the same-slot electric/magnetic normalization."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Derive an independently fixed physical tick and fluctuation law, or keep the Wilson normalization conditional."
negative_assertion_classes: [derived_no_go_boundary]
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply neither the
representation carrier nor the Wilson action, Hamiltonian, instrument, update
law, or tick normalization used below. Those objects are explicit mathematical
inputs to this note. The exact original note, runner, cache, campaign files, and
three raw commit patches are preserved under
`.claude/science/physics-loops/gauge-effect-7841-correction-20260909/originals/`.

## Claim scope

This packet proves four finite-carrier statements and locates one exact
sufficient-law cut.

1. On the supplied `3+1` representation carrier
   `H=C^3 direct_sum C`, the complete `SU(3)`-invariant binary-effect cone is
   `E=a P_3+b P_1`, with `0<=a,b<=1`.
2. If sharpness is separately supplied, the only nontrivial invariant binary
   PVM is `{P_3,P_1}`, up to exchanging outcome labels. Even then, covariance,
   trace completeness, and repeatability do not select the Lueders update: an
   explicit continuous non-Lueders family has those same effects.
3. On the supplied full Wilson Hilbert space with at least one edge and with a
   nonzero Wilson plaquette multiplication operator, the positive same-carrier
   Hamiltonians `H_g=g^2 H_E+g^-2 H_B`, `g>0`, preserve the enumerated gauge,
   positivity, isotropy, and coefficient-product properties while retaining a
   free operator-level relative coefficient. On any such full space with at
   least one edge, an exact unitary or antiunitary exchange of raw `H_E` and
   `H_B` is impossible: `H_E` is unbounded and `H_B` is bounded.
4. For the supplied Wilson plane weight, the identity-tangent negative
   log-Hessian is exactly `(beta/(2 N_c)) g_can`. Therefore the separately
   supplied one-tick fluctuation law
   `-Hess_e log K_tick=g_can` selects `beta=2 N_c`, hence `beta=6` for
   `N_c=3`.

The fourth item is a sufficient conditional law, not a derivation from the
current axioms. The first three items establish only the stated finite
mathematical boundaries. They do not construct two full framework models or
prove that the displayed law is physically unique or minimal.

## Exact target and obligation graph

The target proved here is the conjunction of the four statements above on
their stated supplied carriers and domains. Schur decomposition proves the
effect cone. Explicit Choi and support calculations prove the instrument
family. Peter--Weyl growth, bounded multiplication, and the bounded-perturbation
theorem prove the full-`L^2` Wilson statements after the nondegenerate domain
hypotheses are imposed. A second-order exponential expansion proves the plane
weight Hessian. The physical selection of the carriers, Wilson action,
Hamiltonian, tick, and unit-Hessian law remains open; no lemma here supplies
those bridges.

## 1. Supplied carriers and notation

### 1.1 Registration carrier

Let

```text
H = C^3 direct_sum C,
R(U) = U direct_sum 1,       U in SU(3),
P_3 = diag(1,1,1,0),
P_1 = diag(0,0,0,1).
```

The `C^3` fundamental representation and the trivial representation are
irreducible and inequivalent. This is the supplied `3+1` carrier used here;
the theorem does not derive that carrier from the minimal axioms.

### 1.2 Finite Wilson gauge carrier

On a finite lattice with edge set `E` and plaquette set `P`, take the full,
unreduced Hilbert space

```text
K = L^2(SU(3)^E),
H_E = sum_edges Delta_edge,
H_B = sum_plaquettes [1-(1/3) Re Tr U_p],
```

where `Delta_edge` is the nonnegative canonical Casimir/Laplacian in the
half-trace normalization

```text
Tr(T_a T_b)=delta_ab/2.
```

Boundary conditions and the finite cell complex are fixed. For the operator
independence statement below, require `|E|>=1` and require `H_B` to be a nonzero
multiplication operator; a standard lattice with at least one nondegenerate
plaquette has this property because the Wilson deficit takes both zero and
nonzero values. For the exchange obstruction, `|E|>=1` suffices. The electric
and magnetic operators are supplied Wilson/Kogut--Susskind objects, not outputs
of Admissibility or Record. A separately reduced or truncated physical Hilbert
space is outside the proof.

### 1.3 Wilson plane weight

For `SU(N_c)`, define the supplied one-plane weight

```text
K_beta(U)=Z_beta^-1 exp[(beta/N_c) Re Tr U],       beta>0.
```

The scalar `Z_beta` is independent of the tangent coordinate and therefore
drops out of its log-Hessian.

## 2. Complete invariant binary-effect cone

### Theorem E1

An operator commutes with every `R(U)` if and only if it has the form

```text
X=x_3 P_3+x_1 P_1.
```

Consequently, every invariant binary POVM is `{E,I-E}` with

```text
E=a P_3+b P_1,       0<=a,b<=1.
```

The invariant effect set is therefore a square, not a single point. Its
projection-valued corners are `0`, `P_3`, `P_1`, and `I`; after the two trivial
effects are removed, `{P_3,P_1}` is the unique nontrivial invariant sharp
binary PVM up to outcome labels.

### Proof

Schur's lemma makes the commutant scalar on each irreducible summand. The
summands are inequivalent, so no off-diagonal intertwiner survives. Hermiticity
makes the two coefficients real, and `0<=E<=I` is exactly
`0<=a,b<=1`. Idempotence imposes `a,b in {0,1}`. The runner independently
computes the commutant nullity from all eight embedded Gell-Mann generators and
checks the effect and projection conditions.

Sharpness is load-bearing. Gauge invariance alone permits every interior point
of the square, including the completely uninformative `E=I/2`.

## 3. Repeatability does not select the update map

### Theorem I1

For every `lambda in [0,1]`, define the two outcome operations

```text
I_3^lambda(rho)
  = lambda P_3 rho P_3
    +(1-lambda) Tr(P_3 rho) P_3/3,

I_1(rho)=P_1 rho P_1.
```

Then:

- both maps are completely positive;
- `Tr[I_3^lambda(rho)+I_1(rho)]=Tr rho`;
- their effects are exactly `P_3` and `P_1`;
- each outcome is repeatable under the same sharp PVM;
- the instrument is `SU(3)`-covariant; and
- different `lambda` give different post-measurement states.

Only `lambda=1` is the Lueders instrument. Thus even supplied sharpness,
covariance, effect identity, trace completeness, and outcome repeatability do
not uniquely select the state-update law.

### Proof

Compression by `P_3` and `P_1` is completely positive. The map
`rho -> Tr(P_3 rho)P_3/3` is a prepare-after-effect channel and is completely
positive; convexity proves complete positivity for the full interval. The
trace identity follows from `P_3+P_1=I`. Both outputs lie entirely in their
named sectors, which proves repeatability. Since `P_3/3` is invariant under
the fundamental `SU(3)` action, covariance is immediate.

For a pure state in the triplet sector, output purity varies from `1/3` at
`lambda=0` to `1` at `lambda=1`, so the family is not an alternative Kraus
description of one channel. The runner checks Choi positivity, trace
completeness, repeatability, covariance, and this purity witness at four
values of `lambda`.

This theorem exhibits a nonunique family; it does not claim to classify every
repeatable covariant instrument.

## 4. Same-carrier coefficient counterfamily

### Theorem H1

For each `g>0`, let

```text
H_g=g^2 H_E+g^-2 H_B.
```

Assume `|E|>=1` and `H_B!=0` on the full `L^2` carrier. Every `H_g` is
nonnegative, gauge invariant, and self-adjoint on the domain of `H_E`. If the
edge and plaquette sums use the same coefficient on symmetry-related cells,
each is spatially isotropic on the fixed lattice. The product of the displayed
electric and magnetic coefficients is one for every `g`, while their ratio is
`g^4` and they are equal only at `g=1`.

A common clock rescaling `H_g -> c H_g`, `c>0`, multiplies both coefficients
and leaves their ratio unchanged. Thus positivity, gauge invariance, spatial
isotropy, the coefficient-product constraint, and a common clock choice do not
select `g=1` on this supplied family.

### Proof

`H_E` is a nonnegative self-adjoint finite sum of commuting edge Casimirs.
Because at least one edge is present, it is unbounded on the full `L^2`
carrier. `H_B` is a bounded nonnegative multiplication operator on a finite
lattice. The bounded-perturbation theorem therefore makes `H_g` self-adjoint
on `Dom(H_E)` for every `g>0`. Gauge invariance and lattice isotropy hold term
by term.

The coefficients are genuine operator coordinates on this domain. If

```text
a H_E+b H_B=c(a' H_E+b' H_B),       c>0,
```

then `(a-ca')H_E=-(b-cb')H_B`. The left side is unbounded unless `a=ca'`,
whereas the right side is bounded. Thus `a=ca'`; since `H_B!=0`, also
`b=cb'`. If `ab=a'b'=1`, then `c^2=1`, so positivity gives `c=1`. Distinct
members of the displayed family therefore cannot be identified by a common
clock rescaling.

Both domain conditions matter. With no edges, `H_E=H_B=0` and the exchange
obstruction is false. With edges but `H_B=0`, every `H_g=g^2H_E` is related to
every other member by a common clock rescaling, so the formal coefficient
ratio has no operator meaning.

This is a counterfamily only to the enumerated premises. A separately derived
electric/magnetic equality, fluctuation law, calibrated tick, or other physical
condition could select one member.

## 5. Exact same-carrier exchange obstruction

### Theorem D1

If `|E|>=1`, there is no unitary or antiunitary operator on the supplied full
finite-lattice `L^2` Hilbert space that exactly exchanges the raw electric
Casimir operator `H_E` with a finite nonzero affine rescaling of the Wilson
multiplication operator `H_B`.

### Proof

The `SU(3)` irreducible representations `(p,0)` have

```text
C_2(p,0)=(p^2+3p)/3,
```

which is unbounded as `p` grows. Peter--Weyl sectors carrying this sequence
occur in `L^2(SU(3))`, so `H_E` is unbounded.

For every `U in SU(3)`,

```text
-3/2 <= Re Tr U <= 3,
0 <= 1-(1/3)Re Tr U <= 3/2.
```

On a finite lattice, `0<=H_B<=3|P|/2`; it is bounded. Unitary and antiunitary
conjugation preserve boundedness. An unbounded operator therefore cannot be
conjugate to a finite affine rescaling of `H_B`.

This excludes only a raw exact electric/magnetic exchange on this Hilbert
space. It does not exclude dual formulations on enlarged or different
carriers, representation/spin-foam transforms, continuum or infrared
dualities, or a new theory that reduces back to Wilson observables by a proved
bridge.

## 6. Exact Wilson tangent Hessian and the sufficient law

### Theorem W1

Write `U(x)=exp(i x^a T_a)` near the identity. Canonical half-trace
normalization gives

```text
Re Tr U(x)
  = N_c-(1/4) delta_ab x^a x^b+O(|x|^4).
```

Hence

```text
-Hess_e log K_beta
  = [beta/(2N_c)] g_can.
```

This is an exact tangent-Hessian identity for every positive `beta`, not the
large-`beta` heat-kernel generator asymptotic.

Therefore, inside the supplied Wilson family, the one-scalar physical law

```text
-Hess_e log K_tick=g_can
```

is sufficient to imply

```text
beta=2N_c,
beta=6 when N_c=3.
```

At `beta=24` the Hessian coefficient is four, providing an explicit off-target
control. The tick in the law must be fixed independently of gauge diffusion;
otherwise a time or rate convention can insert the desired normalization and
the argument is circular.

### Proof

Expand the exponential to second order. Tracelessness removes the linear term,
and

```text
Re Tr[-(x^a T_a)(x^b T_b)/2]
  =-(1/4) delta_ab x^a x^b.
```

Multiplication by `beta/N_c` and taking the negative Hessian gives the stated
coefficient. Equality with `g_can` is equivalent to
`beta/(2N_c)=1`.

## 7. What the packet decides

The positive decisions are:

- the full invariant binary-effect cone on the supplied `3+1` carrier is
  known exactly;
- sharpness selects the effect partition but not the repeatable covariant
  update;
- raw same-carrier electric/magnetic exchange is not a valid normalization
  selector;
- within the Wilson family, the missing physical input is compressed to the
  exact one-tick Hessian law above.

The bounded negative statement is only:

> On the stated nondegenerate full-`L^2` Wilson domain, gauge invariance,
> positivity, spatial isotropy, the coefficient-product condition, and a
> common clock rescaling do not select `g=1` in the displayed family.

Alternative routes remain live: derive an independent physical tick and its
fluctuation law; derive another action or kernel; calibrate a supplied law and
make held-out predictions; construct a duality on a different carrier with an
exact Wilson reduction; or adopt explicit convention-level bookkeeping.

## 8. Boundaries and falsifiers

This packet does not:

- derive the `3+1` representation carrier, Wilson action, Wilson plane weight,
  electric Hamiltonian, Record instrument, or occurrence law from the current
  minimal axioms;
- claim a complete classification of repeatable instruments;
- rule out all electric/magnetic dualities;
- derive the one-tick Hessian law or recommend silently adding it to the
  minimal axioms;
- establish same-slot physical identification, continuum Yang--Mills, a mass
  gap, confinement, Standard Model identification, or TOE closure;
- classify the full instrument cone, construct two complete framework/Record
  realizations, identify the finite Wilson operator with an exact transfer
  generator, or prove the unit-Hessian law uniquely or minimally physical;
- apply an audit verdict or move a retained score.

The packet is falsified if the commutant contains another independent block,
an invariant effect lies outside the displayed square, one of the instrument
maps loses complete positivity/completeness/repeatability/covariance, all
`lambda` produce the same channel, the nondegenerate operator family is related
by a common positive clock rescaling at distinct `g`, `H_E` is bounded on the
stated full carrier, `H_B` is unbounded on a finite carrier, or the Wilson
negative log-Hessian differs from `beta/(2N_c)` in the named normalization.

The corrected N1--N8 stress test is preserved in the committed
[No-Go Discipline checklist](../.claude/science/physics-loops/gauge-effect-7841-correction-20260909/NO_GO_DISCIPLINE_CHECKLIST.md).
The original campaign directory is attributed historical state; its stronger
framework, minimality, novelty, panel, scratch, and mutation claims are not
current proof.

## 9. Recovery provenance

The original campaign files report a scratch path, a SHA-256, panel returns,
searches, and mutation plans. The scratch file is unavailable, so those claims
remain attributed history and are not used as evidence. What is verifiable is
the repository runner at raw PR head
`c76726c0fbf2df7c628685b74fc6fadacc4009e7`, its authored Git history, and the
original cached output. This correction preserves those bytes exactly and
adds explicit domain controls and source/input binding. The current cache is
generated only after the corrected source and its declared inputs are frozen.

## Review record

Review of the original three-commit boundary found three corrections. The
operator statements now require a nonempty edge set, and coefficient-ratio
independence additionally requires a nonzero Wilson multiplication operator.
Broad campaign statements about every current premise, framework-native
essentiality, smallest-law selection, full model realization, scratch
survival, panel independence, and unexecuted mutation coverage are historical
only. The finite Schur, effect, instrument, Wilson boundedness, and
identity-tangent Hessian calculations remain in scope. Formal audit remains
deferred until a solid TOE; this source record applies no verdict or grade.
