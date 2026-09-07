# Exact target contract

## Frozen mathematical objects

On the seven-site star, let `0` be the center, `d=1,...,6` the leaves, and

```text
h(t) = sum_d (t_d |0><d| + conjugate(t_d) |d><0|),   |t_d|=1.
```

Let `H_F(t)=dGamma(h(t))` on the strict number-conserving fermion Fock space,
`L(t)=exp(-beta h(t))`, and use the standard grand-canonical Gibbs state
`Gamma(L)/det(I+L)` at zero chemical potential. Condition on the complete
leaf occupation Record `S subset {1,...,6}` and ask for the center occupation.

On the unit cube `x in {0,1}^3`, define

```text
H0 = X1 + X2 + X3,
H1 = X1 + Z1 X2 + Z1 Z2 X3,
```

in the one-particle corner basis. The common protocol prepares `|000>`, evolves
by `Uj(z)=exp(-i z Hj)`, measures the common target effect
`E*=|111><111|`, and feeds target/complement into one common two-outcome
pointer writer.

## Required certificates

1. **Source binding.** Current minimal axioms, primitive registry, closest
   July prior art, open PR heads `#7828-#7832`, and the preregistration commit
   are pinned.
2. **Strict-free typing.** `H_F(t)` is quadratic and number conserving; no
   density-density, twisted-SWAP, hard-core interaction, or fitted target term
   enters the star result.
3. **Star exponential.** With `q=beta sqrt(6)`, `C=cosh(q)`, derive the exact
   center/leaf blocks of `L(t)` and show every principal minor used below is
   invariant under arbitrary link phases. More generally, exhibit the diagonal
   leaf gauge `D` with `h(t)=D h(1) D*`; hence every positive spectral
   preparation `f(h)` followed by occupation effects is phase blind on a tree.
4. **Exact full conditional.** If `m=|S|`, derive from Fock Gibbs weights

   ```text
   p(center=1 | S) = [C - (C-1)m/6] / (C+1).
   ```

   It is normalized, strictly between zero and one, depends only on the six
   nearest-neighbor occupations, is strictly varying for `beta>0`, and is
   proper-cubic invariant.
5. **Partial-Record extension.** If `a,z,u` are the numbers of leaf Records
   equal to one, equal to zero, and still blank, with `a+z+u=6`, summing over
   the unrecorded leaves gives

   ```text
   p(center=1 | a,z,u) = [1 + (C-1)(z+u/2)/6] / (C+1).
   ```

   This covers all `3^6=729` neighboring Record conditions without assigning
   a value to a blank site. At `C=5/4` the exact value is
   `(48+2z+u)/108`.
6. **Common K0/K1 law.** Substitution of uniform `K0` phases and staggered
   `K1` phases gives exactly the same seven probabilities for every `beta`.
   At `beta=log(2)/sqrt(6)`, the exact fixture is
   `(30-m)/54`, `m=0,...,6`; this fixture is a certificate, not a fitted input.
7. **Literal local writer.** One fixed occupation PVM and one common
   target/complement pointer writer give those weights and lock one supported
   rank-one Record outcome. Formation cadence and later decoupling/gating stay
   supplied.
8. **Global-consistency diagnostic.** With `r_m` the complete-shell star odds,

   ```text
   r_m = [6+(6-m)(C-1)] / [6+m(C-1)].
   ```

   Test the pairwise nearest-neighbor Markov compatibility identity
   `r_m r_(m+2)=r_(m+1)^2`. It fails for `C>1`, so translating the star
   conditional is not called a global DLR/equilibrium Gibbs specification.
9. **Globally consistent escape route.** The diagonal two-site Gibbs weights
   give an edge-factor law

   ```text
   p_edge(center=1 | a,z,u) = C^z / (C^a + C^z),
   ```

   where blank-edge factors cancel. This is the exact conditional of the
   positive classical measure proportional to `C^(number of disagreeing
   edges)`, but it is described as an edgewise diagonal functional, not as
   `exp(-beta sum_e H_e)` for the noncommuting quantum hoppings.
10. **Cube flux.** The three summands of `H0` commute, those of `H1`
   anticommute, `H1^2=3I`, and every elementary face has flux `+1` for `K0`
   and `-1` for `K1`.
11. **Common Record discriminator.** For all real `z`,

   ```text
   |<111|U0(z)|000>|^2 = sin(z)^6,
   |<111|U1(z)|000>|^2 = 0.
   ```

   In particular the common cadence `z=pi/2` gives target probabilities
   `1` and `0`. The same writer produces disjoint literal pointer Records and
   later pointer-only dynamics preserves them.
12. **Full-global-Gibbs control.** The global cube quantum Gibbs diagonals are
    not branch equal:

    ```text
    (exp(-beta H0))_xx = cosh(beta)^3,
    (exp(-beta H1))_xx = cosh(sqrt(3) beta).
    ```

    Their first mismatch is at order `beta^4`. This kills any inference from
    the star gauge theorem to a loop-bearing global thermal equality.
13. **Cubic family covariance.** All 24 proper cubic rotations map the
   corner-to-opposite-corner protocol and the face-flux statements into the
   same protocol family. A single asymmetric prepared instance is not called
   invariant.
14. **Resolution certificate.** Runner stdout includes substantive
    `per_element:`, `per_site:`, `per_mode:`, `per_block:`, and
    `lattice_wide:` lines before the final `TOTAL` line.
15. **Scope firewall.** The result is a conditional operational separator
    and a star-local blindness theorem, not an axiom derivation, an empirical
    observation, a physical clock, a selection of `K1`, an obligation
    retirement, or a TOE-score change.

## Hard kills

The block is killed if the star conditional uses only a mean-field expectation
instead of the full strict-free Gibbs state; if a nonlinear interaction is
inserted; if link phases enter a diagonal star probability; if the cube test
uses different preparations, cadence, effects, or writers by branch; if the
target is not a literal Record outcome; if strict prior-art search finds the
same star/cube joint statement; or if the conclusion is sold as action
selection rather than operational distinguishability. It is also killed if
the translated star law is called a global equilibrium specification, the
edge-factor escape is called the full quantum Gibbs state, or the full cube
quantum Gibbs state is claimed branch blind.
