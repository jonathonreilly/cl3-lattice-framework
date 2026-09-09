# Block 35 independent static attack — final

Status: `PASS TO PIN`

Reviewed artifacts:

- runner SHA-256:
  `a6a0c0c297d090bec925d9895568083bbf159e4713e8a33e9b19f261c37bdb08`;
- theorem SHA-256:
  `ba5d5f026ffd5ef882c7eef401d3c5aac9db7cb60f89efa79132bd6e06ee71f7`;
- N1--N8 sidecar SHA-256:
  `c1aaa0c54ea0ecfa2d207ca8afa499b90201810017cd2ab2bc26b5a1841c06d0`;
- TOE update SHA-256:
  `155961ed6d1e9de78c37f30c6cefe6e686994ab93b42bab81b0fca77d94a8c22`;
- canonical cache SHA-256:
  `0b3110720e0c98582b1be2bb8f2516519007a1f06ce751495554c73ac95e9979`.

Three independent reviewers attacked the mathematics/autonomy boundary, the
tensorization and executable-certificate boundary, and the authority/prior-art
portfolio boundary. Reviewers made no file edits.

## Attack history

The attacks rejected earlier candidates until all of these issues were fixed:

1. Endpoint exclusion and normalization were initially too weakly tested. The
   final packet includes the monotone nonlinear family
   `(1+u)[1+epsilon(1-u^2)]`, which has the Born endpoints but is not affine.
2. The first mixture test compared raw pair weights. The final gate compares
   normalized six-outcome probabilities and proves the exact positive gap
   `[cosh(k)-1]/[3 cosh(k)+6]`.
3. The first C4 Markov fixture had zero exponent change and reduced to `1=1`.
   The final fixture has exact local change `delta=2` and verifies cancellation
   of nonincident edges.
4. The first N5 certificate overstated finite controls as executable
   lattice-wide proof. The cache now says lattice-wide execution did not run;
   the general `Z^3` and bipartite statements rest on displayed analytic
   proofs.
5. Operational randomization was initially allowed to imply affinity of the
   unnormalized edge factor silently. The final theorem separates affinity of
   normalized operational probabilities (`W_A`) from the typed
   probability-to-factor or normalizer bridge (`W_E`) and audits all ten pairs
   among the five independent walls.
6. The first portfolio wording treated preparation affinity as newly found.
   The final N8 pins #6326, #6184, #6347, and #6275, credits the July theorem
   and #6326 as direct prior art, and assigns Block 35 only its actual new
   contribution.
7. The no-go certificate initially promised a cache that did not exist. The
   final source-bound cache is present, fresh, and contains all five required
   resolution lines.
8. The first hostile-mutation gate counted fourteen literal `False` constants
   as rejected tests. The final gate recomputes every one of its 21 predicates
   from algebra, pinned evidence, or pinned result state, and an AST control
   enforces zero literal Boolean verdicts.

## Final mathematical grading

| surface | independent result |
|---|---|
| nonlinear public-premise controls | exact; exponential and polynomial positive families survive, and the endpoint-normalized monotone control defeats endpoint-only affinity |
| local probability comparison | exact after normalization; event addition and physical-preparation affinity are distinct |
| affine representation lemma | exact; the 15-coefficient proper-cubic invariant solve has rank 14 and leaves only `c+b r dot s` plus the free constant |
| C4 Markov control | exact and nondegenerate at `delta=2`; triangle-freeness does not restrict edge-potential harmonic degree |
| bipartite sign map | exact on all 1,296 C4 six-axis configurations at three rational parameters; analytic generalization is clearly distinguished from execution |
| Born/anti-Born scope | exact inside the affine cone; no sign selector is promoted from the stagger map |
| operational predecessor | exact rerun at `PASS=118 FAIL=1`; the sole failure is the deliberately removed scalar-Record-additivity needle |
| gravity arithmetic | numerical formulas reproduce conditionally; operator, source, dynamics, and parameter identification remain unproved |
| no-go discipline | complete N1--N8 public-premise boundary; five independent walls and ten wall pairs are explicit |

## Execution and scope grading

- Fresh independent replays return `PASS=15 FAIL=0`.
- Hostile promotions rejected: `21/21`.
- Content-identity mutations rejected: `14/14`, with seven exact public,
  canonical, and result-state evidence hashes matched.
- The cache envelope pins the reviewed runner hash and reproduces the same
  substantive stdout and N5 lines.
- Current main, PR #7814 state, and every N8 Git blob/SHA identity were
  independently rechecked.
- The intentional zero of the endpoint nonlinear control is support/limit
  qualified and is not presented as a strict-positive Hammersley--Clifford
  witness.

## Verdict boundary

`PASS TO PIN` applies to the public-premise boundary, countermodels, normalized
discriminator, affine sufficiency lemma, conditional arithmetic, and route
classification. It is not an audit verdict, axiom decision, autonomous
randomizer/reset theorem, typed factor bridge, Born sign selection, gravity
derivation, obligation retirement, or TOE-score movement.
