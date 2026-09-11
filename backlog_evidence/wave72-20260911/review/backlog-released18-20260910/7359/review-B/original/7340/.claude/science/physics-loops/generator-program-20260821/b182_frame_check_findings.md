# B182 adversarial frame check: orientation bit

Status: complete; exact-arithmetic audit against the requested committed surfaces.

Scope: C1--C5 only; no worktree edit. Benchmark `(s_x,s_t)=(3/5,1/4)` is
supplied data unless the landed theorem licenses parameter-changing identification.

## Exact fixture and C1

Using `Bench("12x6",12,6)` and `Bench("8x4",8,4)`, I substituted exactly:
`nu=7/5`; `sigma=0` on pinned `{0,1}` and `3/5` elsewhere; `m=1`; supplied
couplings. No float enters; the physical lattices are `6x6` and `4x4`.

For `X_0=diag((-1)^(t+x))`, exact full-matrix subtraction gives, at both
extents, `X_0 Q(+s_x,+s_t) X_0-Q(-s_x,-s_t)=0` (0 nonzero entries).
Against either single flip, `Q(-s_x,+s_t)` or `Q(+s_x,-s_t)`, the residual has
84 nonzero entries at 12x6 and 32 at 8x4. It is not a fixed-point symmetry:
`X_0Q(+,+)X_0-Q(+,+)` has 144/56 nonzeros.

The landed scaling-probe wording says `(-1)^(t+x)` descends through the
antiperiodic quotient iff both *physical* extents are even. That condition is
met (`6x6`, `4x4`), so the joint-flip map exists on both fixtures. Existence
does not decide whether a parameter-changing map is a fixed-theory redundancy.

**Verdict C1: PASS algebraically, with a scope correction.** Joint flip and
single-flip rejection are exact; descent is in-class at these even extents,
but `X_0` is not a symmetry of the supplied-sign benchmark point.

## C4: full diagonal-sign group

Write `K=s_x K_x(sigma)+s_t K_t(sigma)` (zero constant/mixed term exactly).
Both fixtures give the same exact conjugation table:

| map | `H(sigma)` | `K_x(sigma)` | `K_t(sigma)` | sign-point map |
|---|---|---|---|---|
| `X_0=(-1)^(t+x)` | `H(sigma)` | `-K_x(sigma)` | `-K_t(sigma)` | `(sigma,s_x,s_t)->(sigma,-s_x,-s_t)` |
| `X_t=(-1)^t` | `H(-sigma)` | `K_x(-sigma)` | `-K_t(-sigma)` | `->(-sigma,s_x,-s_t)` |
| `X_x=(-1)^x` | `H(-sigma)` | `-K_x(-sigma)` | `K_t(-sigma)` | `->(-sigma,-s_x,s_t)` |

Thus `X_0=X_tX_x`.  The full orbit of `(+,+,+)` is
`{(+,+,+),(+,-,-),(-,+,-),(-,-,+)}` in `(sigma,s_x,s_t)` signs;
the other four points form the orbit with the opposite triple product.
The full-group invariant is `sigma*s_x*s_t`, **not** `s_x*s_t`.
Only in the stabilizer of the fixed `sigma=+3/5` carrier, `{1,X_0}`, are the
two coupling-sign orbits `{(++),(--)}` and `{(+-),(-+)}`, labeled by `s_xs_t`.

**Verdict C4: PARTLY REFUTED.** `s_xs_t` is invariant under the fixed-carrier
stabilizer, but not under the full available diagonal relabeling group: `X_t`
or `X_x` flips it while also flipping the supplied carrier shear orientation.

## C2: the frame license

The sign-channel note uses "jointly frame data" for the horizontal map
`(t,beta)->(t eta,-beta)` between class points, not only at fixed parameters.
Its license is the measure-preserving change and equality of all licensed
gauge-invariant correlators. Suppliedness alone cannot defeat the analogy:
`beta` there is supplied too. Here `X_0` likewise licenses family equivalence
if fields, measure, and observables transform covariantly, but it is not a
vertical symmetry of the fixed `(3/5,1/4)` fiber.

More decisively, the diagonal action has two slot-orbits:
`(p,O_+)<->(-p,O_-)` and `(p,O_-)<->(-p,O_+)`. Quotienting the parameter pair
therefore leaves two fiber slots; it does not identify `O_+` with `O_-` at `p`.
**Verdict C2: FRAME LICENSE ONLY AT FAMILY LEVEL; COUNTING CLAIM REFUTED.**

## C3: invariants, registration, and counting

The landed note reports `beta_P=beta Phi_P(t)` as invariant; it never says an
orbit has unit slot weight and explicitly selects neither K0 nor K1. Its odd-#P
2D registration is `Z(-beta)!=Z(beta)`; its zero-set discriminator is instead
the frozen 3D background comparison. Both register the invariant B-BIT, not two
representatives of one relabeling orbit. The main-branch Koide no-go is explicit:
orbit count is not a weighting rule; the orbit-quotient sharpening excludes
phase-resolved readout but still does not select slot degree.

No analogous channel registers the *overall* orientation here: `X_0` commutes
with the committed `r`, so `Q`, `herm(Q^-1)`, the reflected form, determinant,
spectrum, and zero-set data are conjugate across `(++)<->(--)`. There is an
exact channel for the surviving relative-sign class: `tr(Q^2)` is
`47794293/896000` versus `82268811/1792000` at 12x6 and
`378637341/17920000` versus `335627241/17920000` at 8x4; determinants also differ.
This registers `s_xs_t` at fixed carrier (or `sigma s_xs_t` for the full group),
but changes no vector-space multiplicity. **Verdict C3: COUNTING ENTAILMENT FAILS.**

## C5: consequence

**Verdict C5: `Q=2/3` is conditional on an additional one-orbit/slot-weighting
principle.** Frame equivalence supports invariant reporting, not dimensional
quotienting. Without that principle the two slots remain and the prior arbiter
gives `r=1`, `Q=1`; no committed orientation-registration channel changes this.

## Eight-line summary
1. C1 passes exactly: joint flip residual 0; either single flip has 84/32 defects.
2. Even physical extents `6x6` and `4x4` satisfy the landed descent requirement.
3. C2: the sign note licenses horizontal equivalence between class points, not a fixed-point symmetry.
4. The horizontal quotient still has two slot-orbits, so it cannot turn two slots into one.
5. C3: the sign note entails invariant reporting, not orbit slot-weighting; its own Koide notes say so.
6. No invariant channel registers overall orientation; relative/triple sign is spectrally registered and count-neutral.
7. C4: `s_xs_t` is fixed-carrier invariant only; the full group preserves `sigma s_xs_t`.
8. C5: strongest honest result is conditional `Q=2/3`; absent the new counting rule, `Q=1`.
