# Exact target contract

## Common action object

For a unit Bloch direction `n`, write

```text
P_n = (I + n.sigma)/2,
int P_n dnu(n) = I/2.
```

For a frozen neighboring Record condition `eta`, define

```text
m_eta = (1/6) sum_(y~x) n_y       (blank neighbors contribute zero),
A_eta = -h m_eta.sigma,
W_eta = exp(-A_eta) > 0.
```

The target marked weight is

```text
q_eta(n) = Gamma_0 Tr(P_n W_eta),
Gamma_eta = int q_eta(n)dnu(n) = Gamma_0 Tr(W_eta)/2.
```

Writing `x_eta=h|m_eta|` and
`r_eta=tanh(x_eta) m_hat_eta`, the conditional mark law should be

```text
p_eta(dn) = [1 + r_eta.n] dnu(n),
Gamma_eta/Gamma_0 = cosh(x_eta) = 1/sqrt(1-|r_eta|^2).
```

Before specializing to the exponential, prove the invariant classification.
For every positive qubit transfer write uniquely

```text
W_eta = alpha_eta (I + r_eta.sigma),  alpha_eta>0, |r_eta|<1.
```

Under the same marked-intensity rule,
`Gamma_eta=Gamma_scale alpha_eta` and
`det W_eta=alpha_eta^2(1-|r_eta|^2)`. Relative to an isotropic baseline
`W_0=alpha_0 I`, test the exact equivalence

```text
det W_eta = det W_0
  iff Gamma_eta/Gamma_0 = 1/sqrt(1-|r_eta|^2).
```

The exponential of a traceless action is one sufficient realization because
`det exp(-A)=exp(-Tr A)=1`; it is not to be called the unique realization.

## Route Q: same-qubit survival filter

At step `dt`, test

```text
K_n = sqrt(2 dt Gamma_0) P_n W^(1/2),
K_0 = sqrt(I-dt Gamma_0 W).
```

The route must include the exact completeness domain, the unique blank input
needed to recover `q_eta`, the no-jump state update, the continuous-time
survival law, and the time-integrated Record content. Reusing the original
conditional law after a no-jump result is forbidden unless a reset is explicit.

## Route B: orthogonal blank and Record sectors

On `H_dyn = C|B> direct_sum C^2_Record`, construct a basis-independent Kraus
family using `W^(1/2)` whose total effect on `|B>` is
`Gamma_eta |B><B|`, whose every resolved output is `P_n`, whose no-jump branch
leaves `|B>` unchanged after conditioning, and whose complete Record sector is
absorbing. Prove the exact finite-time instrument and composition law.

Test the minimum carrier dimension for simultaneous nonzero autonomous
formation and absorption of the full pure-qubit Record orbit.

## Record-only two-site discriminator

For two simultaneously eligible sites with frozen conditions and common
`Gamma_0`, derive the winner probability and winner-conditioned Record content
for both routes. For Route B the target is

```text
Pr(1 wins)/Pr(2 wins)
  = sqrt[(1-|r_2|^2)/(1-|r_1|^2)],
r_i = 3 E[n | i wins].
```

At the exact witness `x_1=0`, `x_2=log 2`, Route B should predict `4/9`.
Route Q must be independently integrated and compared at the same witness.

Only pre-race conditions, eligibility, winner identity, ordering, and formed
Record content may enter the observable discriminator. No absolute time or
unread absence may be treated as a measurement.

## Hard positive gates

1. Exact Kraus completeness and positivity for both candidate routes.
2. Exact branch output and action-dependent marked weights.
3. Exact no-jump/backaction accounting with no silent reset.
4. Exact finite-time absorption and semigroup composition for Route B.
5. A proved minimal-carrier statement at the exact stated resolution.
6. Exact covariance and null-action limits.
7. Exact constant-determinant/rate-polarization biconditional and converse.
8. Exact two-site winner/content laws and a separating rational witness.
9. A Record-ancestry inventory for every empirical variable.
10. Explicit scalar-action-shift and free-hazard counterfamilies.
11. Exact separation of proved mathematics, candidate physical law, current
    axiom content, and owner decision.

## Hard kill gates

- kill `axiom-derived` if action, exponentiation, event-flux identification,
  clock normalization, aligned writer, reset, or carrier enlargement is supplied;
- kill `memoryless` if no-jump filtering changes the blank or makes survival a
  non-exponential mixture;
- kill `same-carrier` if absorption of the full pure orbit forces every jump to
  vanish;
- kill `Record-only` if duration, unread absence, uncertified eligibility, or an
  unrecorded context is used;
- kill `unique` if a scalar action shift or independent positive hazard factor
  preserves content while changing races;
- kill `exponential-specific` if the relation is actually characterized by a
  broader constant-determinant positive-transfer class;
- kill `grading-compatible one-site` if generic pure projectors are not in the
  declared even readable algebra;
- kill `new science` if the complete architecture comparison and discriminator
  already exist on main or an open PR;
- kill `TOE movement` unless the exact registered obligation and authority path
  are named.
