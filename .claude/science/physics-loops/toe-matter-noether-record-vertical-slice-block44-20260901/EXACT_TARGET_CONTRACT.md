# Exact target contract

## One law and two product realizations

Use the four vertices of a square, labelled cyclically `0,1,2,3`, and the one
fixed nearest-neighbor hopping expression

```text
H = -t sum_{<xy>} (a_x^dagger a_y + a_y^dagger a_x),  t real.
```

Execute it in two realizations with identical one-site matrices, square graph,
coupling, charge-density projectors, initial occupation Record, and final
occupation writer:

1. CAR/Jordan-Wigner realization `a_x=c_x`;
2. commuting hard-core realization `a_x=b_x`.

No branch may ask whether the product is graded, inspect a Jordan-Wigner
string, or receive a realization-specific router.

## Action-derived current

For local charge `n_x=a_x^dagger a_x`, derive the oriented bond current by
differentiating the same hopping term with respect to an oriented link phase,
and verify exact operator continuity

```text
d n_x / d tau = i[H,n_x] = - div J(x).
```

The sign convention must be stated and checked on every vertex in both
realizations. The final occupation event must therefore be a spectral event of
the same conserved charge density, not an independently invented product
observable.

## Exact statistics-sensitive event

Let the initial two-particle occupation be opposite corners `|1010>` and the
target occupation be the other opposite corners `|0101>`. Prove exact
all-parameter statements, not only floating-point samples:

- CAR transition amplitude is identically zero for every `t tau`;
- commuting hard-core transition amplitude equals the exact analytic function
  obtained from the finite Hamiltonian and is nonzero away from its discrete
  zero set;
- the two realizations agree on the one-particle hopping graph and all declared
  one-site input data, so the discriminator is genuinely two-particle and
  product-sensitive.

## Common permanent Record writer

Attach the same trivially graded two-label pointer cell to both realizations.
Use the target occupation projector `P_T` and its complement to construct one
common even instrument whose pointer records `target` or `not-target`. Verify:

- Kraus completeness and complete positivity at the executed finite size;
- branch traces agree with the target/complement Born form **conditional on the
  scoped calibration premise**;
- pointer labels are correlated with the matching occupation event;
- later controlled evolution fixes all previous pointer Record projectors;
- replacing the pointer labels changes no branch weight.

The pointer construction may demonstrate compatibility and operational
readability. It may not be called uniquely selected or axiom-derived.

## Required comparison and decision

The block must classify one of:

- `NEW_CONDITIONAL_CONNECTOR`: the one-law/action-current-Record conjunction is
  new, exact, and passes the hard value gate;
- `KNOWN_COMPONENT_COMPOSITION`: exact but already contained in cited prior art;
- `ARBITRARY_COUPLING_REQUIRED`: a separate product-sensitive coupling or
  realization-specific writer is necessary;
- `COUNTEREXAMPLE`: one of the asserted exact equalities fails; or
- `BACKLOG_NO_PR`: no dramatic-step value despite a correct finite result.

Audit status, owner adoption, obligation retirement, and TOE percentages remain
separate events.
