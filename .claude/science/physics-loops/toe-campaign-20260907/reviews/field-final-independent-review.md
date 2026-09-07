# Final independent source check — Cartesian plaquette source

**Disposition: clean within the explicitly conditional scope of the three files bound below.** I found no blocking mathematical, source-identification, or provenance defect. The package correctly preserves the independently established source correction and the distinction between continuous-source curvature and magnetic-flux-sector energy. This is a focused scientific source check, not a formal audit, retained-grade decision, or authorization to land.

Reviewed worktree: `/Users/jonreilly/Projects/Physics-worktrees/toe-campaign-20260907`; base `HEAD=f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`. The three reviewed files were untracked candidate files at review time. This confirmation applies to their exact content hashes, independently of later branch changes.

| File | SHA-256 |
|---|---|
| `docs/SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07.md` | `c51fd68a14992017101f6b4f4aca4dc4ce78e0ad7731be404fa587d3e9f6ddd3` |
| `scripts/spin_half_cartesian_plaquette_source_2026_09_07.py` | `935553580b57a2ab1d5e0dd89f8bcc419e2a005b5c089e04b42ed13baf1445d5` |
| `scripts/spin_half_cartesian_plaquette_source_independent_check_2026_09_07.py` | `2b21ba485d696599af74d5fed7077997a202423a800fee0d21cd24c96cdf0a62` |

## Scientific confirmation

The note's definitions are sufficient to reproduce its algebra without importing an unlanded claim as a premise. The supplied objects are the link-occupation carrier, allowed ring moves, Hamiltonian with `J>0`, finite connected move component, electric-field map, and source. The note correctly states that the minimal framework axioms and approved primitives do not derive these objects.

For the ordered square links, the local relation `Δn=(-s,+s,-s,+s)` and parities `(epsilon,-epsilon,-epsilon,epsilon)` give `ΔE=-epsilon*s*(+,+,-,-)`. This establishes the claimed local domain: infinite cubic lattice, compatible open squares, and periodic rectangular lattices with every periodic extent even. It needs no infinite-volume operator. Reversing a move and reversing the ordered axes give the correct conjugation and orientation behavior. Numerical checks on cubic even tori supplement the local proof; they are not offered as a numerical proof for every rectangular or infinite carrier. The odd-periodic control is correctly identified as outside the supported extension.

In the declared row convention, `E(n)-E(n^p)=epsilon*s*∂p` proves

`H[b+da]=D(a) H[b] D(a)†`, with `D(a)|n>=exp(i<a,E(n)>)|n>`.

The frozen `theta*s` exponent is therefore a checkerboard plaquette source when physical `E` is held fixed. The `theta*epsilon*s` exponent is the uniform Cartesian source. The note correctly allows global sign and orientation conventions without using them to erase a spatial parity pattern. The cube-sum argument and finite trace invariant rule out the relevant equivalence; the note does not turn this source distinction into a physical-phase no-go.

The exact integer Laurent polynomials remain those of my independent construction:

- `tr H_s(theta)^4 = 8975616`;
- `tr H_epsilon_s(theta)^4 = 8973184 + 2432*cos(4*theta)`.

The primary independently computes the second derivatives `0` and `-38912` from integer matrix products. I checked its product-rule formula: for `H'=iB`, the terms are `4 tr(CH^3)-4 tr(BBH^2+BHBH+BH^2B)`, agreeing with the differentiated trace. Matrix sizes and integer magnitudes are safely within the implemented arithmetic range for this fixture.

The finite response formula uses the actual derivatives of the two Hamiltonian families. The primary sums over a full dense eigendecomposition; the preserved independent code solves the projected derivative equation with a bordered sparse system. The note properly calls the resulting values numerical derivatives of finite eigenvalues. It supplies the hypotheses for a simple lowest eigenvalue at zero source: finite connected component and strictly negative ring couplings at zero source. The scalar shift in its Perron argument can always make every diagonal positive for finite real `V`; singleton components are explicitly accommodated. This establishes local finite eigenvalue analyticity, not a thermodynamic gap.

The full-flux seam construction is correct on every even cubic torus for integer `theta*L^2/(2*pi)`. Its other curls vanish, and the exceptional seam changes the plaquette angle by an integer multiple of `2*pi`. The diagonal rotation preserves each occupation component. The note consequently states the correct endpoint equality for the fully relaxed finite spectrum, while leaving a followed branch, magnetic-flux sector, and uniform limiting remainder as separate obligations. It does not label the tabulated `chi_2` as an established thermodynamic or physical sector stiffness.

## Rerun evidence

Both exact packaged runners were rerun from the reviewed worktree, directing all new outputs into the permitted external scratch directory. Results:

| Check | Fresh result |
|---|---:|
| Primary runner | `TOTAL: PASS=19 FAIL=0`, exit 0 |
| Independent helper | `TOTAL: PASS=55 FAIL=0`, exit 0 |
| Maximum difference across six response derivatives | `6.6058269965196814e-15` |
| Arbitrary-source rephasing matrix residual | `1.729642994972255e-14` |
| Full-flux matrix conjugation residual | `5.878304635907301e-15` |

The new results preserve the independent curvature values at `V=1,.95,.90`, the exact trace polynomial, every tested even-root update, reverse-move consistency, all reached-state ice/flux conditions, and real/imaginary finite-difference convergence. The primary also checks arbitrary-source covariance, unwrapped negative roots, both ordered-axis conventions, and the seam phases at L2/L4/L6. These are genuinely different controls: neither a fixed-state expectation nor a test of Hermiticity alone would detect the source error.

Fresh receipts are in [final-review scratch](/Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/field-independent-check/final-review/review-binding.json), alongside `primary.json`, `primary.log`, `independent.json`, and `independent.log`.

## Downstream scope and provenance

The downstream table matches the frozen PR-head snapshot. In addition to the four original targets, I read the relevant raw note passages at the stated heads of #7955, #7963, #7966, and #7976 using `git show`. Those passages do carry the magnetic-twist-derived `UK` target, its regression comparisons, or the synthesis of that sequence. The package confines its correction to that identification and the dependent interpretations. It explicitly preserves unrelated spectra, electric `U`, raw correlations, conditional quadratic-kernel algebra, and the separate genealogy/forward failures, subject to their own validation. It does not claim those sources have been newly validated or rejected by association.

The packaged independent helper was directly diffed against my original script, whose verified SHA-256 is `128657c428c5ecf9b9a7350955211924a31148c60e88bde1df0ca650fdbff100`. Its scientific construction, exact Laurent calculation, response solve, boundary checks, and full-flux test are unchanged. Packaging adds the optional output path, counted checks, provenance declarations, and explicit assertions of the already-derived polynomial. The original independent derivation remains the one completed without reading the scout/discriminator. This final pass is a review of the integrated package and does not claim to be a second newly blind derivation.

The campaign's `INDEPENDENT_PROVENANCE.json` correctly binds that original script. Its `verification.json` binds the exact two packaged runner hashes above and reports the same cross-method discrepancy. I read the mutation driver and its seven recorded scientific-failure results. The target substitutions, failure-label requirement, and source hashes support the note's account. I did not rerun those seven mutations in this final pass; I reran both unmodified packaged baselines and inspected the existing mutation receipts. No production Monte Carlo, audit pipeline, or grade operation was run.

## Commands and boundary

Actual fresh execution commands, with the reviewed worktree as the current directory:

```bash
OPENBLAS_NUM_THREADS=1 python3 scripts/spin_half_cartesian_plaquette_source_2026_09_07.py --json /Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/field-independent-check/final-review/primary.json > /Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/field-independent-check/final-review/primary.log 2>&1
OPENBLAS_NUM_THREADS=1 python3 scripts/spin_half_cartesian_plaquette_source_independent_check_2026_09_07.py --json /Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/field-independent-check/final-review/independent.json > /Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/field-independent-check/final-review/independent.log 2>&1
```

Read-only commands were `git status --short`, `git rev-parse HEAD`, full `cat` reads of the three candidate files, `nl -ba`/`sed` for the primary construction, `rg --files` for the campaign field receipts, `diff -u` against my original script, and exact `git show <frozen-head>:<note-path>` reads. Python `hashlib.sha256` bound the files and verified receipt identities; a Python comparison recomputed the maximum response discrepancy from the fresh JSON outputs. The helper diff returned exit 1 because the declared packaging changes exist, not because execution failed.

No candidate source was edited. Only this external report and its allowed scratch evidence were written. No commit, push, PR comment, formal audit, grade action, or status promotion was performed. Further content changes require checking the changed content; the clean confirmation is bounded by the hashes above.
