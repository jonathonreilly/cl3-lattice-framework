# Conditional pair moments, Ward completion and reference scores

**Date:** 2026-08-31; correction 2026-09-09.
**Campaign block:** Source/Eta 34.
**Type:** bounded_theorem
**Standing:** conditional mathematical result; physical suppliers remain open.

Descriptions below of exhaustive runner checks refer to the archived original
controller unless named in the current evidence section. The displayed proofs
remain; the current entrypoint does not relabel old executions as fresh.

**Primary runner:** [`admissibility_d4_normalized_record_pair_source_gravity_pincer_gate_2026_08_31.py`](../scripts/admissibility_d4_normalized_record_pair_source_gravity_pincer_gate_2026_08_31.py).
**Current bounded cache:** [execution](../logs/runner-cache/admissibility_d4_normalized_record_pair_source_gravity_pincer_gate_2026_08_31.txt).

Current framework boundary: [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
[32 conditional theorem](ADMISSIBILITY_D4_SYMBOLIC_LAMBDA_GUARDED_FINITE_SUCCESSOR_TRANSACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-31.md).
[Exact original bodies, versions and earlier evidence](../.claude/science/physics-loops/eta-pair-process-correction-20260909/HISTORY.md).

## Result in one paragraph

For the actual Block32 fixed-front four-lateral-exit law, the ordered pair
moment is exactly

\[
C_\lambda=\mathbb E_\lambda[gh^T]
=\frac{\lambda}{2}(I-ff^T).
\]

It is transverse to the fixed front, but not to generic spatial momentum.
The self-contained conditional nonzero-frequency continuum completion below
restores both Ward contractions for every `lambda`, while all
components remain proportional to `lambda`.  Homogeneous conservation, linear
response with a free coupling, normalized shape, and count-once Blank
bookkeeping therefore do not choose a positive amplitude.  A fixed statistic
normalized at the uniform family member has the exact equal-variance recurrence
`{0,2/3}`, but this is a reference-dependent Bernoulli complement mirror, not a
Fisher-information, action-unit, source-unit, or physical-selection law.  The
shortest remaining positive bridge must identify the branchwise Record source
and supply an absolute source/response/unit law consumed by the same gravity
carrier.

## Imported conditional family and actual geometry

The Block32 family is

\[
q_\lambda(g,h)=
\begin{cases}
(1+3\lambda)/16,&g=h,\\
(1-\lambda)/16,&g\ne h,
\end{cases}
\qquad 0\leq\lambda<1,
\]

with uniform left and right marginals.  This note uses the actual lateral
directions for a fixed axial front `f=e_x`,

\[
g,h\in\{-e_y,+e_y,-e_z,+e_z\},
\qquad P_f^\perp=I-ff^T,
\]

not a tetrahedral label surrogate.  Direct summation gives

\[
\mathbb E[g]=\mathbb E[h]=0,
\qquad
\mathbb E[gg^T]=\mathbb E[hh^T]=\frac12P_f^\perp,
\]

\[
C_\lambda=\mathbb E[gh^T]=\frac\lambda2P_f^\perp,
\quad
\operatorname{tr}C_\lambda=\lambda,
\quad
\lVert C_\lambda\rVert_F^2=\frac{\lambda^2}{2},
\quad
C_\lambda^2=\frac\lambda2C_\lambda.
\]

The runner repeats this calculation in all 24 proper-cubic frames.  It proves
geometric covariance of the family, not a momentum-space conservation law.

## Three distinct notions of transversality

Label centering, front transversality, and physical-momentum transversality are
not interchangeable:

1. uniform marginals give `E[g]=E[h]=0`;
2. the lateral embedding gives `f^T C_lambda=0`;
3. for generic spatial momentum `p`,

\[
p^TC_\lambda
=\frac\lambda2\bigl(p-(p\cdot f)f\bigr)^T,
\]

which is not zero generically.  The bare spatial tensor therefore satisfies a
generic momentum Ward condition only at `lambda=0`; front-parallel momentum is
a special geometry, not the full law.

## Conditional nonzero-frequency Ward completion

For any supplied symmetric spatial tensor `S`, define the following
completion at nonzero frequency. Applying it to
`S=C_lambda` gives

\[
T^{ij}=C_\lambda^{ij},\qquad
T^{0i}=\frac{C_\lambda^{ij}p_j}{\omega},\qquad
T^{00}=\frac{p_iC_\lambda^{ij}p_j}{\omega^2},
\qquad \omega\ne0.
\]

Then, in the displayed sign convention,

\[
-\omega T^{0j}+p_iT^{ij}=0,
\qquad
-\omega T^{00}+p_iT^{i0}=0.
\]

This is real progress in route confidence: the actual anisotropic pair tensor
is not algebraically incompatible with a conserved continuum source.  It is
not yet a physical lattice source theorem.  The formula divides by `omega`,
is proved by substitution here, and does not supply source-event
typing, birth, cadence, the zero mode, boundary treatment, coupling, or
nonlinear gravity.  Moreover, every displayed component scales with `lambda`,
so the completion preserves the full amplitude ray.

## Homogeneous-ray theorem and free coupling

Write

\[
C_\lambda=\lambda C_1,
\qquad C_1=P_f^\perp/2.
\]

For any collection of homogeneous linear source constraints `L_a(C)=0`,

\[
L_a(C_\lambda)=\lambda L_a(C_1).
\]

If the unit shape obeys all constraints, every `lambda` in the supplied family
obeys them.  If it fails at least one, only `lambda=0` obeys the collection.
Thus no homogeneous linear constraint selects a unique positive amplitude on
this ray.

Likewise a linear consumer with free coupling sees only

\[
g C_\lambda=(g\lambda)C_1.
\]

For every nonzero scale `t`, the replacement
`(g,lambda)->(g/t,t lambda)` leaves the response unchanged wherever both
parameters stay in their declared domains.  Finally,

\[
\frac{C_\lambda}{\operatorname{tr}C_\lambda}=C_1,
\qquad \lambda>0,
\]

so trace normalization deliberately erases the quantity to be selected.

## Count-once source composition and the 12-Blank boundary

For an unordered pair `g<=h`, use probability

\[
p_{gg}=q_\lambda(g,g),\qquad
p_{gh}=2q_\lambda(g,h)\quad(g<h),
\]

and symmetrized dyad

\[
S_{gg}=gg^T,\qquad
S_{gh}=\frac12(gh^T+hg^T)\quad(g<h).
\]

The ten unordered events have total probability one and reproduce the ordered
moment exactly once:

\[
\sum_{g\leq h}p_{gh}S_{gh}=C_\lambda.
\]

Re-doubling the already doubled off-diagonal events gives the hostile control

\[
C_{\rm bad}=\frac{5\lambda-1}{8}P_f^\perp,
\]

which is nonzero even at `lambda=0` and is rejected by the runner.

The supplied Block32 carrier starts with 2 Locked plus 158 Blank centers and ends
with 14 Locked plus 146 Blank centers.  The bounded check applies the actual finite transaction to a route-derived
carrier and checks that both differences are twelve.  That is finite storage/no-refire
bookkeeping.  A symbolic conversion coefficient can map the count into any
chosen source amplitude; Block32 supplies no Blank-to-energy, Blank-to-action,
or Blank-to-stress conversion.  Pairing a tensor with its algebraic negative is
therefore called opposite bookkeeping here, not physical recoil.

## The fixed-`q0` score recurrence

Let `D=1` for `g=h` and zero otherwise.  Restrict first to functions constant
on the equality/off-diagonal partition.  Requiring uniform-`q0` mean zero,
uniform-`q0` second moment one, and positive diagonal orientation gives

\[
\frac{a+3b}{4}=0,
\qquad
\frac{a^2+3b^2}{4}=1,
\qquad a>0,
\]

with the unique solution in that restricted grammar

\[
O=\frac{4D-1}{\sqrt3},
\qquad (a,b)=(\sqrt3,-1/\sqrt3).
\]

The qualifier is essential.  The actual fixed-front `D4` orbit grammar has
three classes: 4 same, 4 opposite, and 8 perpendicular ordered pairs.  The
different orbit function `(sqrt(2),-sqrt(2),0)` is also uniform-centered and
unit-second-moment.  Therefore `O` is the equality/off family-score direction,
not the unique `D4`-invariant observable.

For the supplied family,

\[
\mathbb E_\lambda O=\sqrt3\lambda,
\qquad
\mathbb E_\lambda O^2=1+2\lambda,
\qquad
v(\lambda)=\operatorname{Var}_\lambda(O)
=(1-\lambda)(1+3\lambda).
\]

The actual score and Fisher information are

\[
s_\lambda(g,h)
=\partial_\lambda\log q_\lambda(g,h)
=\frac{\sqrt3\,[O(g,h)-\sqrt3\lambda]}{v(\lambda)},
\qquad
I(\lambda)=\mathbb E_\lambda[s_\lambda^2]=\frac3{v(\lambda)}.
\]

Only at `lambda=0` is `s_0=sqrt(3) O`.  Consequently the equation

\[
\operatorname{Var}_\lambda(O)=
\operatorname{Var}_0(O)=1
\]

is not a unit-Fisher equation.  Its exact roots are

\[
\lambda\in\{0,2/3\}.
\]

The diagonal-event probability is

\[
P_\lambda(D=1)=\frac{1+3\lambda}{4},
\]

so the two roots are the elementary complement pair `1/4` and `3/4`.  More
generally,

\[
v(\lambda)-v(\lambda_0)
=(\lambda-\lambda_0)\,[2-3(\lambda+\lambda_0)],
\]

and the second root moves to `2/3-lambda0`.  This exposes reference dependence
rather than a universal constant.

The generic Fisher-information machinery is prior art, including the repo's
[sharp Record Fisher tangent-space note](SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md)
and
[pre-Record reference-state/tracial note](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md).
The exact Block32 specialization and its complement interpretation are the
narrow new calculation.  On the commutative classical outcome algebra,
traciality alone does not select the uniform state: every probability state is
tracial.  Equal weighting would need a separately justified
permutation/equal-minimal-projection convention and still would not identify
`O` with a physical source or impose its actual-state variance as an action
unit.

## What an absolute selector would require

An inhomogeneous target can select.  For example, if a retained physical bridge
identifies `T=kappa C_lambda` with fixed nonzero `kappa`, then

\[
\operatorname{tr}T=N\ne0
\quad\Longrightarrow\quad
\lambda=N/\kappa,
\]

or

\[
\lVert T\rVert_F=R>0
\quad\Longrightarrow\quad
|\kappa\lambda|=\sqrt2R.
\]

These are conditional solutions, not derivations of `N`, `R`, or `kappa`.
The minimum physical bridge has three logically separate pieces:

1. a branchwise Record-local event tensor whose expectation is the displayed
   `C_lambda` (or a declared alternative source functional);
2. a local lattice conservation/attachment law, including cadence and zero
   mode, that consumes that same tensor;
3. an independently fixed nonzero response, susceptibility, equation-of-state,
   action-unit, or coupling condition that breaks the homogeneous rescaling.

A reference-state program additionally must derive why `q0` is physically
privileged and why this exact contrast's actual-state response is required to
equal its reference value.  Without those suppliers, declaring `lambda=2/3`
would restate a chosen normalization convention.

## Current premises and historical context

The current minimal-axiom memo and premise registry remain authoritative and
unchanged. This calculation consumes the explicitly supplied probability
family, spatial embedding and nonzero-frequency completion above. It adds no
physical source identity, cadence, zero-mode rule, privileged measure, action
unit or fixed coupling to the framework.

The earlier eleven Git/ledger/status inspections at `aa7338d1` are historical
custody. Their exact bodies remain in recovery; they are not current premises.
In particular, the former RN/source-measure note and ledger are not restored.
The old #6269 completion is historical prior art; the local substitution proof
supplies the complete algebra used here. No inference is made from present PR
status or from the absence of a historical file.

## Physical and TOE boundary

This block improves route confidence but does not retire a TOE obligation:

- gravity can conditionally conserve the actual pair tensor at nonzero
  frequency, so the anisotropic tensor is not killed algebraically;
- the entire conditional stress still carries a free common amplitude;
- the 12-Blank debit supplies bookkeeping, not a physical unit;
- the apparent nonzero `2/3` shortcut is rejected as a reference mirror;
- no physical Record-source identity, local lattice four-stress, cadence,
  zero-mode completion, fixed coupling, or nonlinear gravity law is derived;
- no axiom amendment, approved-primitive amendment, audit verdict, retained
  claim, obligation retirement, or TOE percentage movement is claimed.

The result therefore localizes the blocker rather than closing the lane.  The
next campaign should be chosen by a fresh portfolio panel between (a) deriving
the missing source/absolute-response law on the same carrier and (b) the
independent predictive-reset/source-production route.  More homogeneous Ward
algebra or compiler depth is lower leverage unless it supplies one of those
missing physical inputs.

## Evidence scope after correction

Current named science checks:

- `actual_lateral_moments`
- `homogeneous_ray`
- `actual_debit_and_count_once`
- `nonzero_Ward_and_changed_sign`
- `reference_score_Fisher_orbits`
- `conditional_absolute_target`


The original Block34 numerical definitions and conditional argument are
preserved. The current entrypoint executes the checks it names, with current
source, own-note and actual input identities. Its terminal covers those
bounded checks only. It does not replay or newly certify the original long
controller, original mutation census, or historical custody/status checks.
The complete original execution output and all earlier source versions remain
in the linked recovery inventory, including any earlier failures. Mathematical
claims beyond the named fresh checks retain their displayed proof and the
explicitly historical computation; old outputs are not presented as fresh.
No formal audit verdict or physical TOE closure is asserted.
