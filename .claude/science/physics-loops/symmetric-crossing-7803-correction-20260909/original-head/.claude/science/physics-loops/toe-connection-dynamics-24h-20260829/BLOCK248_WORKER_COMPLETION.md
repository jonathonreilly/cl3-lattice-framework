# Block248 worker completion

## Disposition

Block248 packages one coherent exact science block. The unique highest-spin
branch of the complete two-order response reinforces, rather than cancels, on
each fixed fine-plaquette placement in the supplied `r=3, q=2` local geometry.
The result is a `bounded_theorem` on the supplied action, crossing, and physical
conditional-Haar stack. It is not an audit verdict.

## Exact result

The parent response is

```text
L_epsilon=-(epsilon/2)(B C_c+C B).
```

For the selected defining-vector component on placement `p_i`, put
`A_i=(I-Q)M_(chi_V(p_i))`. The parent identities `C J_3=J_3 C_c` and
`[C,Q]=0` transport both orders to

```text
B_i C_c+C B_i=alpha_i(A_i C+C A_i)J_3.
```

Let `rho_n=(n,(-1)^n)` and let `r_n` be its supplied central multiplier. On
the two placements disjoint from the neighboring merged loop `C1`, the current
top network has four spin-`n` links and eight vector links. Therefore

```text
d_n^D=r_n^4 r_1^8,
s_n^D=d_n^D+d_(n+1)^D
     =r_1^8(r_n^4+r_(n+1)^4).
```

The boundary placement `p2` shares exactly the oppositely oriented rung `h3`
with `C1`. Its unique highest-coupled network has three spin-`n` links, seven
vector links, and one spin-`n+1` shared link. Therefore

```text
d_n^S=r_n^3 r_1^7 r_(n+1),
s_n^S=d_n^S+d_(n+1)^S
     =r_1^7[r_n^3r_(n+1)+r_(n+1)^3r_(n+2)].
```

Both order contributions reach the same normalized top network with fusion
coefficient one. Every relevant multiplier is strictly positive at supplied
finite positive exterior coupling, so `s_n^D>0` and `s_n^S>0` for every finite
layer. The pure-placement selected spin-`N` coefficient is the product of
`s_j` from `j=1` through `N-1`, multiplied by
`(-epsilon alpha_i/2)^(N-1)` when the common parent scalar is restored.

## Physical-Q and cancellation boundaries

Physical `Q` is `J_3J_3^*`, not a static cup. The coarse merged first-cell loop
contains neither internal rung `h1` nor `h2`, while every selected top network
carries a nontrivial irrep on at least one of them. Linkwise Peter--Weyl
orthogonality therefore puts the top network and its raised output in `ker Q`,
including the shared-rung placement.

For real nonzero `r_1`, a disjoint factor can vanish only when
`r_n=r_(n+1)=0`. The shared factor has the exact wider locus

```text
r_(n+1)[r_n^3+r_(n+1)^2r_(n+2)]=0.
```

The hostile signed assignment `r_n=r_(n+1)=1`, `r_(n+2)=-1` cancels the shared
factor exactly. It lies outside the supplied positive multiplier domain. At
identity crossing every symmetric factor is two; at the Haar endpoint or when
the vector spectator multiplier vanishes, every displayed factor vanishes.

## Artifacts

- Source note:
  `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SYMMETRIC_ACTION_CROSSING_TOP_SPIN_BOUNDED_THEOREM_NOTE_2026-08-29.md`
- Primary runner:
  `scripts/admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_2026_08_29.py`
- Independent checker:
  `scripts/admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_independent_2026_08_29.py`
- Source-bound cache:
  `logs/runner-cache/admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_2026_08_29.txt`
- Approach registry and updated campaign governance in this directory.
- Citation manifest with exactly one new node and five dependency edges.

The positive theorem does not invoke the N1--N8 negative-claim gate. The
primary cache nevertheless carries substantive `per_element`, `per_site`,
`per_mode`, `per_block`, and `lattice_wide` lines as a conservative N5 rhetoric
certificate.

## Verification

- Primary exact runner: `TOTAL: PASS=21 FAIL=0`.
- Independent oriented-link/maximal-torus checker:
  `TOTAL: PASS=12 FAIL=0`.
- Hostile formula and scope mutations: `TOTAL: PASS=14 FAIL=0`.
- Both Python files compile.
- Cache freshness: runner SHA and all declared-input fingerprints match;
  timeout 30 seconds, exit code zero, status `ok`.
- Vocabulary lint: zero violations.
- Strict audit lint: no errors; inherited warnings and notices remain.
- Repository invariants: zero link violations, zero Class-F violations, and
  graph delta acknowledged.
- Full audit pipeline: axiom purity, graph build, ledger seed, runner
  classification, and effective-status computation pass; the run then stops at
  the inherited dependency-policy epoch-manifest mismatch on the open parent
  stack. Generated ledger/status churn was removed and no audit verdict was
  applied.
- Exact-commit changed-evidence readiness: one row checked, zero failures and
  zero control failures, `forensic_evidence_ready: true`, with the independent
  checker present in `changed_surfaces` and `helper_runner_paths`.
- The staged/cold diff and author review-loop preflight were read against the
  Block247 parent. All required links resolve.

## Limitations

“Complete” here means both parent operator orders for one fixed placement of
the selected defining-vector action component. It does not mean all Fourier
irreps of the supplied action. Mixed-placement words are not enumerated. The
formal fine-packet iteration is not identified with powers of the actual
coarse-to-residual response. The result supplies no full action-exponential,
invariant-closure, nonlinear-memory, global minimal-memory, arbitrary-`r/q`,
dynamics, gravity, or TOE conclusion. Every parent PR is treated as open.

No axiom or approved primitive was edited. No merge, push, PR creation, or
audit-verdict application was performed.

## Commit and next falsifier

The science packet is committed locally on
`physics-loop/toe-connection-dynamics-block248-symmetric-action-crossing-20260829`
as `2a5588bb0cf08ff805b8c29d1ce4f35a9cb84e84`.

The best next falsifier is the shortest mixed word containing one disjoint
placement and one `p2` placement. Enumerate every maximum-external-label spin
network, apply physical conditional Haar at each typed domain transition, and
compare exact recoupling signs at the supplied positive multipliers. That test
decides whether different placements can meet on a common top basis vector; a
pure-placement coefficient cannot decide it.
