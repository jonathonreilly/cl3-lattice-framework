# Exact target contract

## Same-carrier incompatibility

Let `A=M_2(C)`. For `j in {x,y,z}` and `b in {+1,-1}`, let

```text
P_{j,b} = (I + b sigma_j)/2.
```

Prove that these six projectors span `A`. Hence a linear involutive
`*-automorphism gamma` satisfying `gamma(P_{j,b})=P_{j,b}` for all six is
the identity. A fortiori, no fixed nontrivial grading can make all rank-one
Bloch projectors even/readable on the same carrier.

For `gamma=Ad(Z)`, execute the parity decomposition of the literal Block-38
effects and outputs. Only the `Z`-axis rank-one projectors are even; generic
random-axis projectors are not.

Separately compute the commutant of the full matter algebra `M_2(C)` in its
defining two-dimensional representation. It must be `C I`, ruling out an
independent commuting full `M_2(C)` Record algebra on that carrier.

## Two-mode even repair

On `C^2 tensor C^2`, define total parity `Pi=Z tensor Z`, code projector

```text
P_C = |00><00| + |11><11|,
```

and logical Pauli operators on `C=span{|00>,|11>}`:

```text
X_L = |00><11| + |11><00|,
Y_L = -i|00><11| + i|11><00|,
Z_L = |00><00| - |11><11|.
```

Prove exact Pauli multiplication on `C`, `Pi`-evenness, and for every unit
real axis `a` the rank-one code projectors

```text
P_L(a,b) = (P_C + b a.sigma_L)/2.
```

For `|lambda|<=1`, execute the full-space effects

```text
F_L(a,b;lambda)
  = (P_C + b lambda a.sigma_L)/2 + P_Cperp/2.
```

Show positivity, `F_+ + F_- = I`, exact code restriction, and covariance
under logical rotations. Construct and Choi-test the even
measure-and-prepare instrument

```text
J_b(rho) = Tr(F_L(a,b;lambda) rho) P_L(a,b),
```

whose branch traces sum to `Tr(rho)`. Do not call its complement action a
faithful logical measurement; it is the declared fair completion.

## Typed matter/Record composition

Execute two matter factors with `Ad(Z)` grading and separate Record factors
with the trivial grading. Under the supplied graded product:

- odd matter generators at distinct sites obey CAR;
- every full Record matrix is even;
- distinct Record algebras and even matter observables commute; and
- the vector-space dimension equals the ordinary tensor-product dimension.

Then execute an ungraded twin containing the same one-site algebras,
gradings, Record projectors, and local writer probabilities but commuting
odd matter generators. This is the residual selection wall.

## Decision accounting

- `COMPATIBLE_SAME_CARRIER`: all three PR surfaces coexist literally.
- `REPAIR_DERIVED`: the four governing axioms select one repair.
- `AXIOM_DECISION_READY`: same-carrier coexistence fails, viable repairs
  exist, and current premises do not select among them.
- `BACKLOG_NO_PR`: no advance beyond the three input PRs.

Audit status, axiom adoption, obligation retirement, and TOE score remain
separate events.
