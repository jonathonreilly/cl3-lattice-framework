# Post-execution tensor-type audit

## Exact finding

Let `G_AB=<Theta F_A F_B>` be the occupation-basis OS Gram extracted from the
declared two-slice action, and let `C_AB` be the ordered Grassmann coefficient
array of its sole cross-boundary factor.  Direct exact extraction gives

```text
G_AB = det K[A,B] = C_AB,
G = C = Gamma(K),
G^-1 C = I_16.
```

`C` is nontrivial, positive, normalized in the vacuum sector, and obeys the
exterior composition law.  Those facts do not change its index type.  On this
two-slice surface it pairs a reflected boundary argument with a boundary
argument; it does not compare a boundary state with its translated image.

## Minimal translated extension

For a four-slice link-reflected chain with outer link `L` and central link
`K`, exact block inversion gives

```text
G = Gamma(K),
C_1 = Gamma(K L) = G Gamma(L),
T = G^-1 C_1 = Gamma(L).
```

The homogeneous choice `L=K` yields `T=Gamma(K)`.  But homogeneity or any
other outer-link choice is additional temporal-extension data: `L=I` is an
exact symmetric counterexample to selection by the original two-slice action.
This is why a genuine translation requires more data than the frozen source.

The result is a local tensor-type boundary only.  It does not say that OS
translation, action-to-Fock reconstruction, or CAR dynamics are impossible.
