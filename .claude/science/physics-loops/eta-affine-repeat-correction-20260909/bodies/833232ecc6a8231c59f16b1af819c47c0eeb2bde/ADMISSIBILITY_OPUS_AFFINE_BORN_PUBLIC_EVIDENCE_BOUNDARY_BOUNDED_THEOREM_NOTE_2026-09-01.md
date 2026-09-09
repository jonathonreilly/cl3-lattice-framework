---
claim_id: admissibility_opus_affine_born_public_evidence_boundary_bounded_theorem_note_2026-09-01
final_path: docs/ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md
claim_type: bounded_theorem
claim_scope: "At PR #7814 head 9b5dbb97455a1c26783ad5b4c154d5edea123fdf, whose sole reachable campaign file is LANDING_CORE.md blob 88e41754cddf320f94964bacfbd7a7624e0acda0, the publicly named covariance, nearest-neighbor Markov, triangle-free, Hammersley--Clifford and current-Record premises do not force an affine pure-qubit edge kernel: exp(k n dot m), k nonzero, is a strictly positive simultaneous-rotation-invariant nonlinear edge potential, gives a positive triangle-free Markov edge-product law, and gives a normalized full-support Z3 local conditional specification; 1+epsilon(n dot m)^2 supplies a distinct positive nonlinear family. The exact positive repair is that separate preparation affinity in both Bloch arguments plus simultaneous proper-cubic covariance forces q(n,m)=c+b n dot m. That affinity is not current axiom content and ordinary additivity of measurable Record events at a fixed neighbor condition does not imply it. Within the affine positive cone, orthogonal exclusion selects the Born ray 1+n dot m, same-state exclusion selects the anti-Born ray 1-n dot m, and common positive scaling cancels from the normalized six-neighbor conditional. On every bipartite graph, flipping one sublattice maps lambda to -lambda, so the partition functions agree and nearest-neighbor correlations reverse; this is an exact discriminator and not a sign selector. The displayed W4, tau0, G, lP and b1 arithmetic in #7814 reproduces conditional on the displayed formulas, but no unlanded operator, simulation, source, metric dynamics or archive derivation is reproduced. The unavailable archive may contain a stronger formal meaning of Record consistency, so this result is a public-premise boundary and not a refutation of that unseen claim. No axiom edit, audit verdict, obligation retirement or TOE percentage movement is made."
runner: scripts/admissibility_opus_affine_born_public_evidence_gate_2026_09_01.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The public affine/Born gate: the missing operation is mixture affinity, not event addition

**Date:** 2026-09-01
**Runner:** `scripts/admissibility_opus_affine_born_public_evidence_gate_2026_09_01.py`
**No-go discipline:**
`.claude/science/physics-loops/toe-source-eta-ownership-block35-opus-affine-born-evidence-gate-20260901/POSTEXECUTION_NO_GO_DISCIPLINE_CHECKLIST.md`

## Result up front

The one-file public surface of PR #7814 does not establish its statement that

```text
covariance + Markov + triangle-freeness + Hammersley--Clifford
+ Record consistency
=> phi(n,m) = a + lambda n dot m.
```

On the ordinary reading of those named conditions, the exact counterkernel

```text
phi_k(n,m) = exp(k n dot m),       k != 0,
```

survives every condition and is nonlinear. A second independent family,

```text
psi_epsilon(n,m) = 1 + epsilon (n dot m)^2,
                   0 < epsilon < 1,
```

survives as well. Even adding orthogonal-pair exclusion and the Born endpoint
normalization does not force affinity: a monotone nonlinear deformation with
those same endpoints survives.

The constructive result is sharper than that boundary. If a real pair weight,
or a normalized one-neighbor transition density, is separately affine under
physical mixtures of either preparation, then simultaneous qubit covariance
forces

```text
q(n,m) = c + b n dot m.
```

That is the exact missing rung. Ordinary additivity of probabilities across
disjoint Record events does not supply it: event additivity concerns subsets
of outcomes at one fixed neighboring condition; preparation affinity concerns
how the whole probability law changes when the neighboring condition itself is
a physical mixture.

Even the affine theorem does not choose the sign. Once affinity is established,
orthogonal exclusion selects the Born ray and same-state exclusion selects
anti-Born. Without affinity, endpoint exclusion alone still permits nonlinear
kernels. A common positive scale still cancels from a normalized local
conditional law.

This is significant route progress and zero TOE-score progress. It converts a
vague “Record consistency” decision into four explicit physical obligations:

1. an autonomous recorded randomizer/coarse-graining operation that proves
   affinity of normalized operational probabilities;
2. a typed identification of that normalized probability with the claimed
   one-neighbor transition density, or with the pair factor through a proved
   mixture-independent normalization; and
3. a repeatability or matching experiment that orients Born rather than
   anti-Born; and
4. an autonomous reset/repeat process if one-shot weights are to become stable
   Record frequencies.

## 1. Evidence and authority boundary

The exact public target is PR #7814 at
`9b5dbb97455a1c26783ad5b4c154d5edea123fdf`. Its sole reachable file under
`.claude/science/opus-direct-20260827` is `LANDING_CORE.md`, Git blob
`88e41754cddf320f94964bacfbd7a7624e0acda0`.

The referenced `POSITIVE_PATH.md` research log and the approximately 370 cited
scripts are absent from the PR tree, every reachable Git object, and the local
worktree census performed at preregistration. Their absence is an evidence
limit, not a falsifier of their contents.

The premise source is canonical main
`aa7338d1fbc34a4b92205182b26793194e4727b6`, not the older registry copy
inherited by this stacked branch. The current minimal-axiom source states all
three load-bearing boundaries explicitly:

- Admissibility names a neighbor-conditioned probability distribution;
- its extensional form and values remain unspecified; and
- scalar finite Record additivity was removed and is not current Record
  content.

Record currently says that a record locks one supported possibility and that
readout is determined by record content. It does not relate two neighboring
records, identify a mixed preparation, or require affine dependence on a
neighboring density matrix.

## 2. Exact nonlinear counterkernel

Let `G=(V,E)` be any finite triangle-free graph and let each `n_x` lie on the
Bloch sphere `S^2`. For real `k`, define

```text
p_k({n_x}) = Z_k^-1 product_{(x,y) in E} exp(k n_x dot n_y).
```

For every finite graph this density is strictly positive and normalizable.
It has the following exact properties.

### Simultaneous covariance

For every `R in SO(3)`,

```text
(R n_x) dot (R n_y) = n_x dot n_y.
```

The runner checks the complete 24-element proper-cubic subgroup. The kernel in
fact respects the larger simultaneous rotation group.

### Markov locality and Hammersley--Clifford scope

Changing `n_x` cancels every edge factor not incident on `x`. Therefore the
conditional distribution at `x` depends only on its neighbors. On a
triangle-free graph the maximal nontrivial cliques are edges, so
Hammersley--Clifford gives edge factorization. It does not say that an edge
potential is a degree-one polynomial.

The runner verifies this cancellation exactly on the triangle-free four-cycle.
The same edge potential gives the actual local `Z^3` specification

```text
p_k(dn_x | {m_y : y~x})
  = Z(H)^-1 exp(k n_x dot H) dOmega(n_x),
H = sum_{y~x} m_y.
```

For `H != 0`,

```text
Z(H) = 4 pi sinh(|k H|) / |k H|,
```

with the continuous `H=0` limit `4 pi`. It has full support and varies with the
neighbor condition. Thus current Record can lock any supported draw without
adding a restriction on the kernel shape.

### Non-affinity

For `k != 0`,

```text
d^2/du^2 exp(k u) = k^2 exp(k u) > 0.
```

So no constants `a,b` satisfy `exp(k u)=a+b u` throughout `[-1,1]`. The
midpoint gap at the runner's exact `k=2/3` is

```text
exp(-2/3) + exp(2/3) - 2 > 0.
```

The polynomial kernel `1+u^2/2` gives a second strictly positive counterfamily
with constant second derivative `1`. The result therefore does not rest on a
special analytic feature of the exponential.

There is also a stronger endpoint control. For `0<epsilon<1/4`, define

```text
phi_epsilon,+ (u) = (1+u)[1+epsilon(1-u^2)].
```

It has

```text
phi_epsilon,+(-1)=0,       phi_epsilon,+(1)=2,
d phi_epsilon,+/du = 1+epsilon(1-2u-3u^2) > 0
```

on `[-1,1]`, yet its second derivative

```text
-2 epsilon (3u+1)
```

is not zero. It is Born-oriented, monotone, zero only at the orthogonal
endpoint, endpoint-normalized, and nonlinear. Its reflected partner gives the
anti-oriented family. Exact zeros require the same support or limiting
qualification that PR #7814's Born and anti-Born endpoint kernels already
require when invoking the strictly-positive Hammersley--Clifford theorem.

Therefore “unique member vanishing on orthogonal pairs” is true only after the
affine family has been established independently.

## 3. The exact positive repair: physical-mixture affinity

Write density matrices in Bloch form,

```text
rho(r) = (I + r dot sigma)/2,       |r| <= 1.
```

A real function separately affine in `r` and `s` has the general form

```text
q(r,s) = c + a dot r + d dot s + r^T M s.
```

Require simultaneous proper-cubic covariance,

```text
q(Rr,Rs)=q(r,s)
```

for all 24 proper-cubic rotations. No nonzero vector is fixed by all those
rotations, so `a=d=0`. The commutant of their three-dimensional vector
representation is scalar, so `M=bI`. Hence

```text
q(r,s)=c+b r dot s.
```

The runner solves all coefficient constraints exactly. The 15 nonconstant
coefficients have constraint rank 14; their one-dimensional nullspace is the
dot product. The free constant gives the expected two-dimensional affine
family.

This theorem shows precisely why the nonlinear counterkernel works: it violates
preparation affinity. At a 50/50 mixture of opposite neighbor Bloch vectors,

```text
exp(k n dot 0) = 1,
```

whereas mixing the two responses gives

```text
[exp(k)+exp(-k)]/2 = cosh(k) > 1.
```

That raw-weight comparison is not yet an operational probability statement.
For a six-axis one-neighbor conditional, however, the pure-preparation
normalizer is `2 cosh(k)+4`, while the zero-Bloch conditional is uniform. For
the `+z` outcome the normalized mixture gap is therefore

```text
cosh(k)/(2 cosh(k)+4) - 1/6
  = [cosh(k)-1]/[3 cosh(k)+6] > 0.
```

Thus the normalized operational law is also non-affine in this controlled
one-neighbor setting. On a general six-neighbor product, a physical-randomizer
theorem constrains normalized operational probabilities; it does not by itself
make each unnormalized factor `phi` affine. That further inference requires a
typed identification of `phi` with a normalized one-neighbor transition
density, or a proof that its normalizer is independent of the preparation
mixture in the required comparison.

## 4. Why Record-event addition does not close the bridge

For every fixed neighbor condition, the exponential kernel is a positive
normalized probability density. It therefore obeys ordinary addition on
disjoint measurable events:

```text
mu_eta(A union B) = mu_eta(A)+mu_eta(B),       A intersect B = empty.
```

This says nothing about comparing `mu_eta` with `mu_eta'`, or with the law at a
mixed condition. The runner exhibits the separation on a six-outcome cubic
menu: event addition holds identically, while the normalized 50/50
preparation-affinity equation fails at `k=2/3` by

```text
[cosh(2/3)-1]/[3 cosh(2/3)+6].
```

This resolves the ambiguity in the recent axiom discussion. A possibility is
an alternative of the quantum state, and Record gives access to realized
outcomes. Reconstructing probabilities from many records can estimate a law,
but neither realization nor event addition determines how two physically
equivalent preparation mixtures must be represented. That equivalence needs an
operational randomizer/coarse-graining theorem, together with the typed
transition-density/pair-factor bridge just named, or an explicit additional law
condition.

## 5. The affine cone still contains Born and anti-Born

For pure states,

```text
Tr[rho(n) rho(m)] = (1+n dot m)/2.
```

Thus

```text
K_+(n,m) = 1+n dot m = 2 Tr[rho(n)rho(m)],
K_-(n,m) = 1-n dot m = 2[1-Tr(rho(n)rho(m))].
```

An affine kernel `c+b u` is nonnegative on `u in [-1,1]` exactly when
`c>=|b|`. Positivity alone gives a cone, not one ray.

- `q(-1)=0` gives `c=b>=0`: orthogonal alternatives have zero pair weight and
  the Born ray is selected.
- `q(1)=0` gives `c=-b>=0`: identical alternatives have zero pair weight and
  the anti-Born ray is selected.

Those are physically different endpoint conditions. Current Record supplies
neither adjacent-record condition. The nonlinear endpoint control in Section 2
shows that endpoint exclusion must not be used to smuggle in affinity.

Multiplying every pair kernel by `alpha>0` contributes the same `alpha^6` to
every candidate local state on `Z^3`; local probability normalization cancels
it. Endpoint orientation therefore fixes a ray, not an absolute event rate,
source unit, or coupling.

## 6. Exact bipartite sign equivalence

Let `G=A union B` be bipartite and transform

```text
n_x -> -n_x  for x in A,
n_x ->  n_x  for x in B.
```

Every edge has one endpoint in `A`, so its dot product changes sign. The
rotation-invariant one-site measure is unchanged. Therefore, for every
`|lambda|<=1`,

```text
Z(lambda)=Z(-lambda),
<n_x dot n_y>_lambda = -<n_x dot n_y>_-lambda.
```

The runner verifies the change of variables pointwise on all `6^4=1296`
configurations of a four-cycle and the exact partition/correlation identities
at `lambda=1,2/3,1/5`.

Triangle-free alone does not imply bipartite; the transformation uses the
stronger bipartiteness of actual `Z^3`. It holds on open boxes and even-period
tori, while odd-period tori, antipode-breaking unary weights, and fixed boundary
conditions not transformed with the spins require separate treatment. At the
Born/anti-Born endpoints, zeros again require support or limiting language.

This proves that adjacent-record correlation is a sign discriminator. Equal
partition functions do not choose which sign Nature uses, and the quoted
thermodynamic magnitude `0.5545` is not reproduced without its missing lattice
data and scripts.

## 7. The existing operational route and the axiom choice

The authority-free July review-feedback note
`docs/work_history/repo/review_feedback/OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md`
already contains the right operational mechanism:

1. a physically recorded randomizer chooses preparations with law-supplied
   probabilities;
2. conditional control runs the corresponding preparation;
3. forgetting the randomizer branch by physical coarse-graining gives the law
   of total probability; and
4. the resulting normalized operational probability is affine.

Its companion runner was rerun in this campaign. The operational algebra,
randomizer-affinity, nonlinear clause-delete, reset, and frequency controls
passed, while its old authority needle for scalar Record additivity failed as
it must after the current axiom revision: `PASS=118 FAIL=1`. The predecessor is
not authority and is not imported as a premise. Its surviving conditional
construction identifies the next positive experiment, but it does not itself
identify the PR's unnormalized edge factor `phi` with that operational
probability.

This route is not newly discovered in Block 35. Closed-unmerged PR #6326 at
`b37d487dac778c11e7a9a0e3d1772e39cef0d343` already placed a linear response
beside a cubic nonlinear twin and identified a physical preparation-affinity
diagnostic as the shortest selector route. Open PR #6347 supplies a
current-authority finite-state process scaffold while leaving physical draw and
reset open; PR #6275 supplies an exact coarse-graining fixture but carries a
stale authority copy and likewise does not autonomously realize the draw or
reset. Block 35 contributes the PR-#7814-specific countermodel, normalized
six-outcome discriminator, and general affine representation lemma. The next
campaign should reuse those carriers rather than build another static law.

Accordingly, this block does not recommend editing the minimal axioms yet. The
higher-value next campaign is to derive an autonomous Record-local randomizer,
conditional preparation, coarse-graining, reset, and the typed normalized
transition-density/pair-factor bridge from the existing law. If that succeeds,
operational mixture affinity becomes a theorem rather than constitutional
prose, and the bridge will say whether it constrains `phi` itself. If it fails
at an exact named wall after the operational routes are exhausted, the owner
can evaluate a narrow axiom or approved-law update with the physical content
visible.

## 8. Conditional gravity arithmetic from PR #7814

The displayed arithmetic is internally reproducible. High-precision quadrature
gives

```text
W4 = integral_0^infinity [exp(-2t) I0(2t)]^4 dt
   = 0.154933390231060214084837208107375...

tau0/a^2 = 1/(16 pi^2 W4)
          = 0.04087288071475112076891920097...

G/a^2 = 2 pi tau0/a^2
      = 0.2568118835690281168264053164...

lP/a = sqrt(G/a^2)
     = 0.5067661034136242589762562403...
```

The displayed symbolic coefficient also gives

```text
b1(d)=(d-1)/(3d),       b1(4)=1/4,       b1(3)=2/9.
```

These checks validate arithmetic conditional on the formulas. They do not
derive the Kuhn operator, its determinant or heat-kernel coefficient, regulator
independence, sign, Einstein--Hilbert interpretation, source attachment, metric
dynamics, dilution result, or vacuum-energy formula. None of those derivations
is present in the one-file PR.

## 9. Relation to Block 34 gravity/source work

Block 34's `lambda` is the amplitude of one specific D4 lateral-pair Record
source tensor. PR #7814's `lambda` is an interaction parameter in a different
kernel family. No marginal, source map, or parameter identification between
them is supplied. They must remain distinct.

The results nevertheless form a useful pincer:

- Block 34 shows a source-tensor shape can be conditionally Ward-completed but
  retains its full amplitude ray.
- Block 35 shows a proposed rule-form shortcut does not select an affine family
  on its public premises, while isolating the operational-affinity and typed
  factor-bridge conditions that would.

Gravity remains downstream of a selected physical law and same-carrier source
identity.

## 10. TOE disposition

The percentage map is unchanged. There is no obligation retirement, axiom
change, audit verdict, or positively retained end-to-end theory.

The significant progress is decision quality:

- **pruned:** Hammersley--Clifford plus current Record as a public affine-form
  proof;
- **proved:** separate physical-mixture affinity is sufficient for the affine
  reduction;
- **proved:** endpoint orientation, not positivity, distinguishes Born and
  anti-Born;
- **proved:** the bipartite sign map is a discriminator, not a selector;
- **localized:** the next highest-value object is an autonomous recorded
  randomizer/reset experiment plus the typed normalized-probability-to-factor
  bridge, not more static gravity arithmetic;
- **deferred deliberately:** an axiom edit until that operational route is run
  to ground.

## 11. Verification and fence

The primary runner recomputes:

- seven content-addressed public/canonical/result-state inputs and fourteen
  identity mutations;
- all 24 proper-cubic rotations;
- two independent positive nonlinear counterfamilies;
- triangle-free Markov cancellation on the four-cycle;
- the local `Z^3` normalizer and neighbor variation;
- the rank-14 invariant affine coefficient solve;
- event addition versus preparation affinity;
- the pure-qubit trace and endpoint orientations;
- all 1296 stagger-map configurations at three exact parameter values;
- common-scale cancellation;
- `W4`, `tau0`, `G`, `lP`, and `b1` arithmetic; and
- twenty-one hostile algebra/evidence/scope/governance mutations.

Canonical result: `TOTAL: PASS=15 FAIL=0`.

Not claimed: a universal no-go for an unavailable archive definition; a global
infinite-volume Gibbs theorem; the quoted critical point or correlation
magnitude; a selected Born sign or rate; a physical preparation/reset process;
a gravity operator/source/dynamics derivation; an axiom amendment; audit status;
obligation retirement; or TOE-score movement.
