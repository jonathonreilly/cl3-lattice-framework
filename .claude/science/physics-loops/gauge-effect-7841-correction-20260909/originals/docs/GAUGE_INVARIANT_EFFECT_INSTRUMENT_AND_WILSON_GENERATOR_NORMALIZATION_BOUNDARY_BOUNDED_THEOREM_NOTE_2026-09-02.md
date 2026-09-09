# Gauge-Invariant Effect, Instrument, and Wilson-Generator Normalization Boundary

**Date:** 2026-09-02
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This note sets no audit verdict,
retires no obligation, and changes no TOE percentage.
**Primary runner:**
[`scripts/gauge_invariant_effect_instrument_generator_boundary_2026_09_02.py`](../scripts/gauge_invariant_effect_instrument_generator_boundary_2026_09_02.py)
**Cached receipt:**
[`logs/runner-cache/gauge_invariant_effect_instrument_generator_boundary_2026_09_02.txt`](../logs/runner-cache/gauge_invariant_effect_instrument_generator_boundary_2026_09_02.txt)

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
3. On a supplied finite Wilson gauge Hilbert space, the positive same-carrier
   Hamiltonians `H_g=g^2 H_E+g^-2 H_B`, `g>0`, preserve the enumerated
   gauge, positivity, isotropy, and coefficient-product properties while
   retaining a free relative coefficient. Moreover, an exact unitary or
   antiunitary exchange of raw `H_E` and `H_B` on this carrier is impossible:
   `H_E` is unbounded and `H_B` is bounded.
4. For the supplied Wilson plane weight, the identity-tangent negative
   log-Hessian is exactly `(beta/(2 N_c)) g_can`. Therefore the separately
   supplied one-tick fluctuation law
   `-Hess_e log K_tick=g_can` selects `beta=2 N_c`, hence `beta=6` for
   `N_c=3`.

The fourth item is a sufficient conditional law, not a derivation from the
current axioms. The first three items show why the structural inputs tested in
this campaign do not themselves supply that law.

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

On a finite lattice with edge set `E` and plaquette set `P`, take

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

Boundary conditions and the finite cell complex are fixed. The electric and
magnetic operators are supplied Wilson/Kogut--Susskind objects, not outputs of
Admissibility or Record.

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

Every `H_g` is nonnegative, gauge invariant, and self-adjoint on the domain of
`H_E`. If the edge and plaquette sums use the same coefficient on symmetry
related cells, each is spatially isotropic on the fixed lattice. The product
of the displayed electric and magnetic coefficients is one for every `g`,
while their ratio is `g^4` and they are equal only at `g=1`.

A common clock rescaling `H_g -> c H_g`, `c>0`, multiplies both coefficients
and leaves their ratio unchanged. Thus positivity, gauge invariance, spatial
isotropy, the coefficient-product constraint, and a common clock choice do not
select `g=1` on this supplied family.

### Proof

`H_E` is a nonnegative self-adjoint finite sum of commuting edge Casimirs.
`H_B` is a bounded nonnegative multiplication operator on a finite lattice.
The bounded-perturbation theorem therefore makes `H_g` self-adjoint on
`Dom(H_E)` for every `g>0`. Gauge invariance and lattice isotropy hold term by
term. The coefficient statements are exact scalar algebra.

This is a counterfamily only to the enumerated premises. A separately derived
electric/magnetic equality, fluctuation law, calibrated tick, or other physical
condition could select one member.

## 5. Exact same-carrier exchange obstruction

### Theorem D1

There is no unitary or antiunitary operator on the supplied finite-lattice
Hilbert space that exactly exchanges the raw electric Casimir operator `H_E`
with a finite nonzero affine rescaling of the Wilson multiplication operator
`H_B`.

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

> The enumerated current structural premises do not select the Wilson
> same-slot point on the supplied carrier.

Alternative routes remain live: derive an independent physical tick and its
fluctuation law; derive another action or kernel; calibrate a supplied law and
make held-out predictions; construct a duality on a different carrier with an
exact Wilson reduction; or adopt explicit convention-level bookkeeping.

## 8. Boundaries and falsifiers

This packet does not:

- derive the `3+1` representation carrier, Wilson action, Wilson plane weight,
  electric Hamiltonian, Record instrument, or occurrence law from the minimal
  axioms;
- claim a complete classification of repeatable instruments;
- rule out all electric/magnetic dualities;
- derive the one-tick Hessian law or recommend silently adding it to the
  minimal axioms;
- establish same-slot physical identification, continuum Yang--Mills, a mass
  gap, confinement, Standard Model identification, or TOE closure;
- apply an audit verdict or move a retained score.

The packet is falsified if the commutant contains another independent block,
an invariant effect lies outside the displayed square, one of the instrument
maps loses complete positivity/completeness/repeatability/covariance, all
`lambda` produce the same channel, a tested structural premise fixes the
relative coefficient in the displayed operator family, `H_E` is bounded,
`H_B` is unbounded on a finite carrier, or the Wilson negative log-Hessian
differs from `beta/(2N_c)` in the named normalization.

The current N1--N8 stress test is preserved in the committed
[No-Go Discipline checklist](../.claude/science/physics-loops/toe-gauge-instrument-generator-closure-block54-20260902/NO_GO_DISCIPLINE_CHECKLIST.md).
The earlier prose pass remains in the campaign directory as historical state.

## 9. Recovery provenance

The original scratch runner survived at `/private/tmp/gauge54_probe.py` with
SHA-256
`2f80aa2cd4eafacc2d25dcb0848a61649514294b1a183cd751c1d1f77bb920e1`.
The repository runner preserves its scientific body. Repository-facing
metadata and final `TOTAL:` punctuation were normalized, and the Wilson
Hessian and center-bound checks were strengthened to derive their tested
matrices independently. It was executed again after recovery and reports
`TOTAL: PASS=81 FAIL=0`.
