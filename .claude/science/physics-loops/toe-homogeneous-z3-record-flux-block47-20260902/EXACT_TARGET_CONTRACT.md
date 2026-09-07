# Exact target contract

## Frozen objects

On `ell^2(Z^3)`, use translations and coordinate parities

```text
T_j |x> = |x+e_j>,       D_j = T_j + T_j^-1,
P_j |x> = (-1)^x_j |x>.
```

Define two bounded self-adjoint nearest-neighbor signed adjacencies

```text
H0 = D_1 + D_2 + D_3,
A_1 = D_1,  A_2 = P_1 D_2,  A_3 = P_1 P_2 D_3,
H1 = A_1 + A_2 + A_3.
```

The displayed Pauli/parity notation is a coordinate representation of a
one-particle signed adjacency. The physical strict-free lift, when invoked,
is `dGamma(Hj)` on one CAR mode per lattice site; the coordinate parities are
not three physical onsite qubits.

## Required certificates

1. **Source binding and novelty.** Pin `origin/main`, the current minimal
   axioms blob, the Block 46 parent, the closest uniform-walk and staggered
   kernel prior art, and open PR heads `#7828-#7832`. No exact prior source may
   already own the joined homogeneous pi-flux darkness plus common local
   Record protocol.
2. **Signed-adjacency typing.** Construct matrix elements directly from link
   signs as well as from the displayed shift/parity algebra. Verify
   self-adjointness, nearest-neighbor support, and face flux `+1` for `H0`,
   `-1` for `H1` in every coordinate plane.
3. **Clifford cancellation.** Derive `A_i A_j + A_j A_i = 0` for `i != j`,
   `A_j^2=D_j^2`, and

   ```text
   H1^2 = Q := D_1^2 + D_2^2 + D_3^2
          = 6 I + sum_j (T_j^2 + T_j^-2).
   ```

   No mixed-coordinate shifts may survive.
4. **All-time parity theorem.** `Q` preserves each of the eight coordinate-
   parity sectors and `H1` maps a sector only to the three sectors at Hamming
   distance one. From the norm-convergent exponential series, prove

   ```text
   <x+r|exp(-it H1)|x> = 0
   ```

   for every real `t` whenever `r mod 2` has Hamming weight two or three.
   This is an operator theorem, not a finite-power numerical inference.
5. **Uniform positive comparator.** Because the `D_j` commute,

   ```text
   <x+r|exp(-it H0)|x>
     = product_j [(-i)^r_j J_(r_j)(2t)]
   ```

   for nonnegative coordinate displacement, with the usual extension to
   signed displacement. At `r=(1,1,1)` the amplitude is
   `i J_1(2t)^3`. Independently derive its leading Taylor coefficient from
   `<111|H0^3|000>=6`.
6. **Fixed common cadence.** At `t=1/2`, certify by the alternating Bessel
   series that `7/16 < J_1(1) < 1/2`. Hence the common target occupation
   probability obeys

   ```text
   (7/16)^6 < p0 = J_1(1)^6 < (1/2)^6,    p1 = 0.
   ```

   The result is probabilistic, not perfect transfer.
7. **Literal local Record protocol.** In the one-particle sector the target
   effect is the local occupation `n_(x+(1,1,1))`. Use the same supplied
   unrecorded source, cadence, two-outcome target/complement PVM, writer, and
   branch-blind post-write incident-edge gate for both candidates. Only the
   resulting Records are read; the unrecorded amplitudes are inferred through
   repeated Record frequencies under supplied repeatability/stationarity.
8. **No isolation.** Every homogeneous exterior bond remains active. The
   theorem may not use a finite open cube or silently suppress links leaving
   the source/target cell.
9. **Covariant family.** Translations and all 24 proper cubic rotations carry
   source-target protocols into the same family; `H0` is strictly covariant
   and the `H1` link field is covariant only up to a diagonal site gauge. In
   the displayed gauge the bare one-step translations in directions 1 and 2
   do not commute with `H1`; explicitly certify the corresponding magnetic
   translations. No single localized preparation is called invariant and no
   ordinary one-site translation invariance is claimed for the displayed
   staggered gauge.
10. **Sequential-pulse sharpness.** The cancellation is for static
    simultaneous evolution under `H1`. The ordered pulse
    `exp(-it A3) exp(-it A2) exp(-it A1)` has a generically nonzero all-odd
    amplitude and must be retained as a counterexample to a broader claim.
11. **Resolution certificate.** Runner output includes substantive
    `per_element:`, `per_site:`, `per_mode:`, `per_block:`, and
    `lattice_wide:` lines and terminates with `TOTAL: PASS=N FAIL=0`.
12. **Scope firewall.** No action choice, physical state, Born rule, clock,
    formation site/rate, permanence dynamics, `I-4`, `P-KIN`, B-BIT, audit
    grade, obligation retirement, or TOE-percentage movement is claimed.

## Hard kills

Kill the block if any mixed term survives in `H1^2`; if any parity-Hamming-two
or -three target has nonzero static-`H1` amplitude; if `H0` is identically
dark at the body diagonal; if the two branches use different sources, times,
effects, writers, or gates; if a finite boundary is isolated; if the
coordinate representation is mistyped as three physical qubits; if prior art
already owns the joined result; or if the result is sold as selecting a
physical law or moving a TOE lane.
