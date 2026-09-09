# Exact Record-law domain and tensor-order bridge: original #6275

Type: bounded_theorem

Status: corrected supplied finite construction, awaiting independent review.
No retained grade, formal audit or TOE closure is claimed.

**Primary runner:** `scripts/law_tournament_6275_finite_2026_09_09.py`

**Independent checker:** `scripts/law_tournament_6266_6275_independent_check_2026_09_09.py`

The shared model is `scripts/law_tournament_6266_6275_model.py`.
The [signed carrier note](SIGNED_RECORD_FINITE_REFINEMENT_AND_CONDITIONAL_SOURCE_6266_BOUNDED_THEOREM_NOTE_2026-09-09.md)
defines the exact menus, transported carriers and local continuation rule.
[History and recovery](../.claude/science/physics-loops/law-tournament-6266-6275-correction-20260909/HISTORY.md)
preserve every original endpoint and intermediate version. Existing current
helper functions and archival note paths remain untouched.

## Exact domain and total supplied kernel

The canonical input basis is `a=2P+M`, ordered 00,01,10,11. Omega is an
exact 4 by 4 Gaussian-rational matrix, Hermitian, trace one and positive
semidefinite. The implementation admits only int/Fraction real and imaginary
components, excluding floats and bools. A valid matrix must pass all 15
nonempty principal minors, computed by exact determinant expansion. For a
Hermitian matrix nonnegative principal minors are equivalent to PSD: the
coefficients of det(tI+Omega) are sums of principal minors. If all are
nonnegative, that polynomial is positive for t>0, ruling out a negative
real eigenvalue; necessity follows from PSD of every principal submatrix.
The test includes nonleading minors and singular boundary densities.

The original tolerant `qdensity` predicate is not used. For
`epsilon=1/10^13`, diag(1+epsilon,0,-epsilon,0) gave negative exact
weights despite passing the old floating predicate. The excess-trace
matrix diag(1+epsilon,0,0,0) likewise did not normalize. Both are now
rejected, without clipping, renormalization or changing their values.

A typed patch also supplies one of the two named dictionaries, a proper
cubic frame, a finite dictionary of integer sites to exact 2 by 2 carriers,
boolean context/output readiness and a boolean spent marker. Malformed
Record dictionaries raise ValueError at this typed API boundary. Invalid
matrix/frame/name, false readiness, spent state, or any occupied candidate
target returns the single refusal of weight one, preserving the old
Records. Readiness bits are supplied interface metadata; they do not prove
a physical preparation or establish a physical Record formation law.

For a valid ready patch the effects are

```
F_empty = P0 tensor I
F_hs = P1 tensor (P_s^R E_h^R),  (h,s) in
       ((0,-1),(1,-1),(1,+1),(2,+1)).
```

Sharp refinement ensures positivity. Their sum is I4, so
`w_i=tr(Omega F_i)` are exactly nonnegative and sum to one on the declared
domain. Both candidates use these same five weights. A no-record outcome
keeps Records unchanged; each formed branch appends its specified two
carriers. All outcomes mark this attempt spent, a supplied protocol rule.
Zero weights are valid entries and stay in the distribution. A requested
realized member must have strictly positive weight; a zero-weight request
raises ValueError. There is no independent random generator claim.

## Explicit channel composition in one basis

The parent five-qubit analytic isometry uses bit index
`p+2m+4b+8r+16a_env`, with input columns `b_input=P+2M`. Its nonzero
column entries, expressed as (output bit tuple; amplitude), are

```
b_input=0: (0,0,0,0,0); 1
b_input=2: (0,1,0,0,0); 1
b_input=1: (1,0,0,0,0); sqrt(1/2)
           (1,0,1,0,0); sqrt(5/14)
           (1,0,1,1,1); sqrt(1/7)
b_input=3: (1,1,0,0,0); sqrt(1/7)
           (1,1,0,1,1); sqrt(2/35)
           (1,1,1,1,0); sqrt(4/5)
```

Each column has unit norm and their supports are disjoint. Let S have
`S[b_input,a]=1` for `b_input=P+2M`, `a=2P+M`; thus its column indices
are the permutation (0,2,1,3). The actual canonical-input isometry is
**W=V S**, and input transport is `X_b=S X_a S^dagger`. The no-record
output is also transported back by `S^dagger Y_b S`. This output-side
bridge matters as well as the input bridge.

For every canonical X, projection to P=0 followed by environment trace
therefore returns `(P0 tensor I) X (P0 tensor I)`. For a fine pair (h,s),
set m=(s+1)/2 and b=h-m, project to P=1,M=m,B=b and trace the environment.
The two-dimensional R output is

```
Phi_hs(X) = X[2+m,2+m] (E_h)[m,m] tau_h.
```

The displayed amplitudes give this equality: for h=1,m=0 the R diagonal
is (5/14,1/7), and for h=1,m=1 it is (1/7,2/35); these are the respective
effect weights times tau_1=(5/7,2/7). The h=0 and h=2 formulas follow from
the single remaining supports. Distinct environment values kill the
unwanted output coherences. Summing fine outcomes by h gives the coarse
measure-and-prepare channel. Completeness of the effects plus the
no-record effect gives trace preservation on the direct-sum output.
Each formed branch has Choi matrix `F_hs^T tensor tau_h`, positive because
both factors are positive; the no-record branch has a Kraus form. Thus the
channel statement also holds with arbitrary external reference, without
inferring this from density-only sampling.

The fresh primary sends all sixteen matrix units through this same W,
compares the no-record and four fine outputs (80 comparisons) and the
three coarse sums (48 comparisons). Numerical amplitude evaluation is
checked to 1e-12; the displayed exact squared amplitudes give the algebraic
identity. The companion independently reconstructs canonical sparse
columns and then removes S from the actual isometry. The unchanged
channel comparator fails that changed operand. Separate calculations in
the two old basis conventions are no longer treated as a composition.
This is the supplied analytic parent dilation, not a fresh certification
of the old literal gate compiler or a physical five-qubit implementation.

## Two actual dictionaries and their restricted comparison

Let root=0, side=R e_y, direction=R_s e_x and tau=R tau_h. The dictionaries
are exactly

```
output_root:
  0         -> program(tau, R(1,2,3), 40+index(h,s))
  direction -> head(tau, R_s, menu1, phase1)
adjacent_packet:
  0         -> outcome(R E_h, h+1)
  -side     -> head(tau, R_s, menu1, phase1).
```

The first root decoder finds the unique frame-bearing program code 40--43;
the second finds the unique outcome without a compatible relay predecessor.
These definitions read the actual matrix-valued Records, not a label-only
fixture. They are conditional decoders on the supplied isolated family.
Common root alignment, proper rotation/translation and the content-decoded
head frame leave invariant the nearest-head signature
`(Manhattan distance, displacement·forward, displacement·transverse)`.
It is (1,1,0) for output_root and (1,0,1) for adjacent_packet. Hence these
two supplied dictionaries differ under that restricted geometric/common-
decoder equivalence. An unrestricted lookup or dictionary-dependent
coordinate recoding is not excluded; no exhaustive two-law classification
or full-Z3 physical non-entailment theorem follows.

The primary checks all 24 frames and all four fine pairs for both actual
dictionaries (192 packets), together with equality of their mixed-state
weights for every frame. It runs one three-write event for eight canonical
law/pair packets. The isolated-strip continuation proof in the companion
note applies: relative to the initial head the output root lies at (-1,0),
and the adjacent root at (0,+1), while the initial relay is at (0,-1).
The extra roots never become contexts. The adjacent outcome may be an
inert neighbor of a later relay, which the actual rule explicitly permits;
it is not incorrectly required to be absent. New sites then advance in
the positive head direction. The root is preserved and the initially
nearest head remains the unique nearest one. This is conditional
arbitrary-finite-horizon algebra, with a bounded fresh execution check.

## Original scope and evidence disposition

Original #6275's aggregate B fine-channel algebra is retained with the
explicit S bridge. D/E's total-law/weight assertions now have the exact
input domain and actual refusal semantics above. F's covariance follows
from the supplied transport definitions, checked here on the 192 packet
family. G/H/I's permanence, root decoder and restricted geometry argument
remain conditional as stated. Longer N=16/32/128 runs, 4608 frame-composition
comparisons and historical routing/gathering counts remain recoverable
original reports, not new executions. Aggregate A's Git/text authority and
J's old text gates are bookkeeping. Neither establishes scientific
acceptance of the absent or historical parent campaigns.

The old ten-mutation count is retained only as a dated report. In
particular dirty_route incremented a summary failure count and
weight_mismatch altered a local comparison dictionary rather than the
candidate law. Those were not independent physical route or law changes.
The new evidence uses real exact-matrix and basis operands against the
unchanged predicates, plus separate input-integrity guards. The original
physical gatherer, routed environment reset, formation action, innovation,
source-to-gravity map, clock/cadence, global normalization and physical
selection of either dictionary remain unsupplied. No current axiom,
registry, historical #6266 path or shared campaign state is changed.
