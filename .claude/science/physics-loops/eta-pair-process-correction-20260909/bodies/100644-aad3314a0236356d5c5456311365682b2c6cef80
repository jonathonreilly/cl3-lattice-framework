# Block28 preflight witnesses

No Block28 target source has been executed.

One feasibility-only diagnostic imported the abandoned Block27 source without
running its main classifier.  It returned `True` for the fixed geometry in
`0.006` seconds and for all `1,568` isolated local turn branches in `6.506`
seconds.  This is not Block28 evidence and will not be cited by the terminal;
it only shows that a small reconstruction is computationally plausible.

## Physical carrier

Use current centers `Y_L=9 e1` and `Y_R=18 e1`, with inward fronts `e1` and
`-e1`.  Each has four perpendicular exits.  The two current blocks and eight
lateral target blocks are pairwise disjoint.  For each source-label pair
`x=(s,t)`, the active control `P_x` is the product of the two exact Locked
pointer projectors and the eight exact Blank-block projectors.  Distinct
`P_x` must be orthogonal; their sum is an active projector and its complement
is the common no-write STOP control.

## Local turn module

For each side, source `s`, perpendicular exit `g`, and target `c`, reconstruct
one literal turn factor list.  It keeps the current Locked word fixed, prepares
the selected lateral Blank block with the Block23 source state, applies the
literal target root, writes `Locked(g,c)`, and is identity on spectators and
outside the finite carrier.  Its Gram coefficient must be the derived
transition `T(c|s)` and every target row must sum to one.

## Tensor coupling

Because the left and right turn supports are disjoint, their products have
Gram

\[
V_{xghcd}^\dagger V_{xghcd}=T(c|s)T(d|t)P_x.
\]

Multiplying by `sqrt(q_lambda(g,h))` and summing over exits and targets must
give `P_x`.  Summing the orthogonal controls and the common STOP gives the
identity, including after tensoring every Kraus operator with an arbitrary
untouched reference identity.

## Readable discriminator

The two new Locked words decode the exits at distinct physical centers.  The
coarse Record event `D={g=h}` is therefore readable.  The source must derive

```text
lambda=0:   P(D)=1/4
lambda=1/2: P(D)=5/8
```

without embedding those values as expected terminal constants.
