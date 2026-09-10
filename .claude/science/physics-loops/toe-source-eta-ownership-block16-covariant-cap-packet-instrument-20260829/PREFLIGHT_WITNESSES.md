# Preflight Witnesses

No Block-16 target runner, independent checker, result cache, or target mutation
was written or executed before this freeze.  These are analytic witnesses and
falsifiers; post-registration code must rederive them.

## Common-block witness

The branch-specific geometry uses axial sites at distances one, two, and three
plus four sites of type `2f+e` with `e` perpendicular to `f`.  Taking the union
over all six signed axes gives

```text
1 center + 18 nonzero axial sites + 24 off-axis sites = 43 sites.
```

Every proper cubic rotation permutes this set.  No branch needs a site outside
it.  The same no-Record projector therefore serves all branches; there is no
branch-specific precursor sector.

## Record and packet witness

With `a(f)=f`, the frozen Record code is

```text
r_f = -(9/16)f + (1/256)f = -(143/256)f.
```

Its Bloch norm is `143/256<1`, so `rho(r_f)` is strictly positive and
normalized.  `a(Qf)=Qa(f)` and `r_(Qf)=Q r_f` for every proper cubic rotation.

At candidate `2f`, the predecessor neighbor `f` and forward packet source
`3f` both carry `r_f`; the four transverse sources carry zero Bloch vector.
This is exactly `hybrid_shell(0,f,a(f))`.  The Record mask
`{-2f,0,f}` leaves the required gap `-f` and candidate `2f` empty.  Sites at
`-2f,0,f,3f,2f+e` are pairwise distinct, and branch masks differ for every
pair of signed axes.

## CP and trace witness

For a positive normalized target state `sigma_f`, the map

```text
X -> Tr(Pi_blank X) sigma_f / 6
```

has positive Choi operator `Pi_blank^T tensor sigma_f / 6` and effect
`Pi_blank/6`.  Six branches sum to effect `Pi_blank`.  The identity map on the
orthogonal nonblank direct-sum sectors has effect `Pi_nonblank`; therefore the
complete instrument is trace preserving.  Uniform weights and
`U_Q sigma_f U_Q^dagger=sigma_(Qf)` give proper-cubic covariance.

This witness proves only an effective finite-block channel.  The trace-and-
prepare step discards blank-sector quantum information into an environment and
the Record mask is a declared classical sector.  No finite-depth nearest-
neighbor unitary or physical blank detector is inferred.

## Flag-front composition witness

For the output Record set `{-2f,0,f}`, the candidate `2f` has unique nearest
Record `f` and grand-predecessor `0`.  The rear gap `-f` has two nearest
Records, `-2f` and `0`; the cap exterior `-3f` lacks a grand-predecessor at
`-f`; cap and trail laterals lack collinear predecessor pairs.  Hence the
Block-15 flag predicate returns exactly `f` at `2f`.

The generated six-neighbor content is the frozen `M=0` shell, so the
fourteen-way next-outcome distribution is the exact positive normalized
baseline.  The existing clear/blocked controller theorem is expected to
compose, but all 2,688 branch/outcome/mask maps and 2,976 blocked components
must be freshly checked.

## Joint-law model-pair witness

Treat each local possibility label as Record presence plus exact Bloch content.
In the correlated law, a branch `f` has four labels unique to that branch:

- center Record content `r_f`;
- Record at tip `f`;
- Record at cap `-2f`;
- non-Record live content `r_f` at `3f`.

For each of the other five directions, the branch carries the common blank
label at that direction's tip, cap, and live-front site.  Therefore the product
of the correlated law's one-site marginals assigns one valid branch

```text
(1/6)^4 (5/6)^15,
```

and the six disjoint valid branches total

```text
6 (1/6)^4 (5/6)^15 = 5^15/6^18 < 1.
```

The transverse `M=0` sources equal the common blank possibility and contribute
unit factors.  The product coupling is not offered as a physical dynamics; it
is a finite countermodel to uniqueness from one-site marginals alone.

## Occupied-sector witness

Because the declared effective algebra is a direct sum over complete Record
masks, `Pi_nonblank` covers every one of the `2^43-1` nonempty masks exactly.
Identity/STOP on that full complement preserves every Record and content.  The
runner should prove this symbolically and use the 43 single-site occupations
plus every branch-footprint site as executable falsifiers; enumerating all
trillions of masks would add cost without strengthening the projector proof.

## Principal risks frozen before execution

1. The construction may merely replace a supplied oriented cap with a supplied
   atomic block channel; this is the explicit positive boundary.
2. A trace-and-prepare map on the effective direct-sum Record algebra may not
   compile to the one-site `M_2` nearest-neighbor substrate.
3. An implementation may accidentally construct six branch-specific channels
   instead of one common-input covariant instrument.
4. The output Record code or live source may fail positivity, covariance, or
   exact equality with the Block-15 shell.
5. The occupied complement or blank/nonblank sector treatment may leave a
   trace-preservation or overwrite loophole.
6. Overlapping centers, formation occurrence, rate, and time remain absent even
   if the finite-block instrument succeeds.
7. The model pair establishes nonuniqueness only for the frozen finite one-site
   marginals; it cannot support a global dynamics or axiom no-go.

Any risk may bound interpretation.  None permits a same-cycle change to the
frozen block, branch outputs, weights, parent law/controller, or axioms.
