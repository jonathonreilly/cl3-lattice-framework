# Goal

Source/Eta Block 11 classifies the strict causal-past preparation route left
open by Block 10.  It asks whether the same six noncommuting `M2` contents can
be earlier permanent Records and, without changing those Records, drive a
normalized physical channel that prepares a new six-condition shell carrying
the full `A1+T1+E+T2` data.  The target is the entire nine-parameter open
family, not only H1 and H2.

This is deliberately narrower than a claim about all causal dynamics.  A
negative answer closes only the **permanent quantum-Record shell as its own
nondisturbing program**.  Consumable live conditions, orthogonal classical
Record codes, larger blocks, approximate channels, a supplied external
program, and a formation/history law remain counterroutes unless separately
tested.

## Exact target contract

Let `theta=(q0,q1,q2,q3,q4,ux,uy,uz,s)` and let Block 10's frozen preparation
give the six Bloch vectors

```text
v_n(theta) = -Q(theta)n/2 + (s n + u cross n)/8,
rho_n(theta) = (I + v_n(theta).sigma)/2.
```

The prior permanent-Record configuration is the product state

```text
R(theta) = tensor_n rho_n(theta)
```

on the six signed neighbors.  The box `|theta_i|<1/4` contains the maximally
mixed point and is strictly inside every Bloch ball by Block 10.

Classify CPTP maps

```text
Gamma: B(H_R) -> B(H_R tensor H_C)
```

subject to both conditions for every `theta` in the open box:

1. **Record prefix safety:** `Tr_C Gamma(R(theta)) = R(theta)`; the complete
   six-site Record configuration, not merely selected expectations, remains
   unchanged.
2. **Full carrier preparation:** the six one-site marginals on `H_C` equal
   the frozen `rho_n(theta)`, or more generally have a decoded
   `A1+T1+E+T2` Jacobian of rank nine while preserving Block 09's probability
   rule and zero action leakage.

The class includes arbitrary fixed ancillas and correlations in the output.
It is therefore stronger than a radius-one/product-Kraus search.  If the
class is empty without using locality or covariance, every strict-radius-one,
translation/proper-cubic-covariant subclass is empty as well.

## Prospective adjudication

Exactly one terminal must be reported:

- `UNIQUE-CAUSAL`: one physical channel class survives after quotienting
  Kraus/Stinespring gauge;
- `PLURAL-CAUSAL`: at least two gauge-inequivalent physical channel classes
  survive;
- `EMPTY`: the displayed permanent-Record program class is proved empty;
- `CAPACITY-ONLY`: only a destructive/live-condition relay or another route
  outside the displayed Record-preserving class survives, or the exhaustive
  classification is not proved.

`EMPTY` must never be shortened to “causal preparation is impossible.”  It
cannot justify an axiom update by itself.

## Stage A: shell and tangent algebra

Recompute Block 10's nine-coordinate map from `theta` to the three positive-
direction Bloch vectors.  Require exact determinant `3/16384`, rank nine,
`v_-n=-v_n`, and strict positivity on the registered box.

Differentiate `R(theta)` at `theta=0`.  After the invertible coordinate
change, the nine tangent operators must be the three Pauli differences

```text
D_(i,a) = sigma_a on (+e_i) - sigma_a on (-e_i),
i=1,2,3,  a=x,y,z.
```

Prove exactly that each pair's three differences generates both local Pauli
algebras and that all nine differences generate the complete six-qubit matrix
algebra.  A dimension count alone is not a proof.

## Stage B: exhaustive nondisturbing-channel classification

For a candidate `Gamma`, put `N=Tr_C o Gamma`.  Prefix safety fixes
`R(theta)`, hence the maximally mixed state and all nine tangent operators.
Because `N` is then bistochastic, its fixed points form the commutant algebra
of its Kraus operators.  Stage A must force that algebra to be all of
`B(H_R)`, so `N` is the identity channel.

Use the Choi extension directly: the `H_R` marginal of `J(Gamma)` is the
rank-one identity-channel Choi matrix.  Positivity then forces

```text
J(Gamma) = J(id_R) tensor tau_C,
Gamma(X) = X tensor tau_C
```

for one fixed state `tau_C`.  Thus every prepared condition marginal is
independent of `theta`.  Compare this exact zero Jacobian with the frozen
rank-nine Block 10 target.

Do not rely on a named no-broadcasting theorem without reproducing the
finite-dimensional algebra and Choi argument.

## Stage C: physical target checks

The target-side runner must independently recompute:

- the Block 10 `A1+T1+E+T2` rank-nine decoder;
- all 24 proper-cubic intertwiners;
- unchanged Block 09 fourteen-way normalization and exact action leakage
  zero;
- H1 and held-out H2 incoming/outgoing action decode, forward vertices,
  literal actual reverse, and common quadrupole source;
- strict positivity on all 512 vertices of the registered box.

These checks establish that the contradiction is with a live physical target,
not with an ill-typed or nonpositive fixture.

## Stage D: counterroutes and no-go discipline

At least these distinct route families must be confronted before a negative
artifact can ship:

1. destructive/consumable live-condition unitary relay;
2. the unused even-shell coordinates;
3. orthogonal classical Record codes or a larger Record block;
4. approximate broadcasting rather than exact open-family preparation;
5. an external or pre-correlated program carrying `theta`;
6. preservation of only selected local readouts rather than the complete
   Record configuration;
7. a formation/history law that generates new conditions without using the
   old shell as a nondisturbing quantum program.

The cycle must apply the current N1--N8 no-go discipline.  If any counterroute
breaks the displayed theorem, report `CAPACITY-ONLY`; do not widen or repair
the target after execution.

The positive control is a consumable six-qubit identity/SWAP relay from an old
live shell to a disjoint output shell.  It must be CPTP, have a rank-nine
past-to-output Jacobian, use no same-event or post-event variable, preserve
the frozen target checks, and fail prefix safety explicitly.  This prevents a
narrow Record-only obstruction from being mistaken for a capacity no-go.

## Forbidden inputs and claims

- no runtime `Q,u,s`, target name, momentum, fixture label, role/epoch tag,
  site selector, host clock, or same/post-event state;
- no gain refit after H1/H2 or after the open-family result;
- no non-TP branch, postselection, reset, or hidden radius-two read;
- no claim about all Record semantics, all live conditions, formation site or
  rate, arbitrary histories, gravity, retention, axiom sufficiency, obligation
  retirement, or TOE percentage movement.

## Frozen authorities

- parent Block 10 delivery `dcc4cb211a40eb246153f863d582905f3002ec5c`;
- Block 10 science result `5388552e789b91fa09ac0fdee94daefc867601fb`;
- Block 09 delivery `ac1473f94fd5df2647bda77b22a191987f4aa05f`;
- latest observed `origin/main` `3cc632921c36aa90266c5c62e56816577ce59a0a`;
- minimal-axiom blob `bc23300becfe4e4db57153c0e94cfcdf2338da71`;
- Block 10 runner/note/cache blobs
  `793ec02b9b031e78e9ff5251377d216182ebec99` /
  `b9187637496f6da0682e7bd5aa64388947fd4df6` /
  `6c9b0fe1a79610acefe13b9653007e3a5e2946e6`;
- Block 10 independent-runner blob
  `3f4c548a7ca6300c7fe5497788f1b4d86ced0ea9`.

The open gravity PR #7795 at head
`8ae39901e0340c64da99103031fb154e938a97ed` is read-only concurrency context.
It closes the static column-closed `q=4` O01 permutation kernel but explicitly
leaves temporal multipliers, physical `Q`, full response, observability,
memory, and gravity open; it does not supersede this causal-preparation test.

## Accounting

This block may close one candidate realization or construct a positive causal
channel.  It moves a TOE percentage only if an applicable obligation is
actually retired and independently retained.  No axiom edit is authorized by
this preregistration.
