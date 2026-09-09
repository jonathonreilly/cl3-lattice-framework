# Full128 local M64 × seam-M2 bare-frame intertwiner

**Date:** 2026-07-24

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Framework substrate:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Exact abstract encoder:**
[`scripts/frontier_full128_cycle_encoder_2026_07_24.py`](../scripts/frontier_full128_cycle_encoder_2026_07_24.py)

**25-site nearest-neighbor supplied-schedule runner:**
[`scripts/frontier_full128_25site_nn_supplied_schedule_2026_07_24.py`](../scripts/frontier_full128_25site_nn_supplied_schedule_2026_07_24.py)

**Bare-frame pair-cocycle runner:**
[`scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py`](../scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py)

**Primary runner:**
[`scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py`](../scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py)

**Receipt:**
[`outputs/frontier_full128_local_m64_seam_m2_bare_frame_intertwiner_receipt_2026_07_24.json`](../outputs/frontier_full128_local_m64_seam_m2_bare_frame_intertwiner_receipt_2026_07_24.json)

**Runner caches:**
[`abstract encoder`](../logs/runner-cache/frontier_full128_cycle_encoder_2026_07_24.txt),
[`25-site circuit`](../logs/runner-cache/frontier_full128_25site_nn_supplied_schedule_2026_07_24.txt),
[`pair cocycle`](../logs/runner-cache/frontier_full128_bare_frame_pair_cocycle_2026_07_24.txt), and
[`integrated intertwiner`](../logs/runner-cache/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.txt).

## Controlled claim

For the supplied finite mode labels, couplings, factor order, code reference,
pair-register preparation, Manhattan routing convention, and rotated seam-word
family listed below, there is a bounded physical-M2 encoding and circuit for
one local six-mode `M64` cell tensored with one seam-port `M2`:

```text
E_full = D U W_A (I_7 tensor |+>^15 tensor |0>^39),

G_physical
  = D U R_contact W_A G_free+seam W_A^dag U^dag D^dag,

E_full G_coarse = G_physical E_full.
```

The executable checks all 128 decoded columns. The maximum intertwiner
residual is `8.40686768501364e-15`. The local cell, seam, conditional pair
sector, contact action, and proper-cubic frame action are part of one
dependency-tracked construction rather than separately asserted objects.

The semantic code occupies 61 named physical `M2` sites: 25 cycle/repetition
shell sites, 30 ordered-pair register sites, and six corridor/returned-work
sites. A radius-four carrier cube contains 729 `M2` sites. The displayed
nearest-neighbor word touches 115 of them, has 3,907 gates, and returns every
routing wire. These are constant finite resources per isolated coarse cell.

The result is covariant on its declared code under bare coordinate
permutations for all 24 proper-cubic frames and all 576 ordered frame products.
The frame-conjugated circuit family is nearest-neighbor and preserves the
matrix/order word. Only the identity frame gives the same canonical off-code
coordinate word and support. Thus the theorem is code-space covariance of the
rotated seam family, not canonical off-code word invariance.

## Exact construction

The first stage uses 22 edge `M2` factors: the 21 edges of `K7`, whose seven
vertices are the six local modes and the seam port, plus one
port-to-reference bridge. A rank-22 binary
map `U` sends seven decoded occupation bits and 15 cycle auxiliaries to those
sites. Its circuit has 20 SWAPs and 36 CNOTs. The 15 independent triangle-X
checks have rank 15, so the cycle code has dimension 128. The abstract runner
checks the original vacuum/one/two-particle 29-column seam fixture; the
nearest-neighbor successor proves the same encoder is bijective on all
`128 × 2^15` decoded/auxiliary bit points and checks the full128 operator
blocks.

Three repetition mirrors give the 25-site shell and make the reverse-pair
layout proper-cubic. The seven-mode free-plus-seam update is decomposed into
38 one- or two-qubit CAR factors: ten coin Givens, one coin phase, three
reverse FSWAPs, nine adjacent seam FSWAPs, and 15 contact phases. Decode,
route, apply, and re-encode gives a 504-gate nearest-neighbor data word. The
separate one-hot schedule is supplied finite circuit structure; its substep
index is not physical time or a transition rate. That optional supporting
controller is not composed into `E_full` or `G_physical`: its 504 clock sites,
radius-11 12,167-site cube, and 564,333-gate macro are excluded from the
61-site/115-touched-site/3,907-gate primary theorem census. The primary theorem
requires only the explicitly supplied finite word order.

For every unordered local pair `(i,j)`, `W_A` prepares the two corresponding
ordered register sites in

```text
|00>,                         unless q_i q_j = 11,
(|1_(j,i)>-|1_(i,j)>)/sqrt(2), when q_i q_j = 11.
```

The product over occupied pairs supplies exactly the exterior/Fock inversion
sign under bare coordinate permutation. Applying the same onsite phase to all
30 ordered sites gives `exp(i g k(k-1)/2)` in every local-number sector
`k=0,...,6`. The preparation and inverse return the shared flag.

The integrated physical order is

```text
D^dag U^dag ; W_A^dag ; G_free+seam ; W_A ; R_contact ; U ; D.
```

It contains 205 decode gates, 1,704 unprepare gates, 59 free-plus-seam gates,
1,704 prepare gates, 30 onsite contact gates, and 205 re-encode gates. Of the
3,907 total gates, 601 are one-site, 3,306 are two-site, and 2,716 are route
SWAPs. Every two-site factor is nearest-neighbor.

## Static commuting-projector code certificate

The conditional pair sector is not merely a prepared-state convention. On
decoded `q_i,q_j` and their two ordered register bits define

```text
Pi_ij = sum_(q != 11) |q><q| tensor |00><00|
        + |11><11| tensor |psi_minus><psi_minus|.
```

Each `Pi_ij` is Hermitian, idempotent to residual
`2.220446049250313e-16`, and has rank four. All 15 commute. Conjugating the
decoded conditional-pair and cycle-auxiliary projectors by the bounded `D U`
circuit gives projectors on physical sites.

For covariance, the certificate uses all 35 `K7` triangle-X projectors. This
family is closed under the 24 frames and has independent rank 15. The original
15 anchored triangles remain an encoder basis but are only span-covariant.
The remaining physical projectors are three repetition-Z projectors, 15
conditional-pair projectors, and six corridor-blank projectors. The total is
59 commuting projectors.

The cross-commutation test is physical and explicit. `D` lifts each triangle
X onto its primary-plus-mirror support. A decoded logical-q Z control becomes
exactly the corresponding row of `U^-1` on the 22 primary sites because the
outer CNOT leaves control-Z unchanged. The runner computes all
`35 × 15 × 2 = 1,050` triangle-X versus conditional-control symplectic
products and all `35 × 3 = 105` triangle-X versus repetition-Z products; all
are zero. It also exhausts all 105 pair-projector pairs on their complete
reduced Hilbert spaces; every commutator is zero.

The exact `D U`-conjugated conditional-pair operator support is the union of
the two distinct logical-Z Pauli rows and the two pair-register sites. The
certificate checks the rows are distinct and that the nonzero individual
Pauli terms make every site in that union actual operator support. There are
zero support-exactness failures. The maximum support is 13 physical sites with
fine-lattice L1 diameter 7.

In the 61-site semantic block, the 15 cycle auxiliaries, three mirrors, 30 pair
register bits, and six corridor/work bits are fixed, leaving exactly seven
free logical bits. The joint code dimension is therefore `2^7 = 128`, equal
to the column space of `E_full`. Deleting one conditional-pair projector
increases the dimension to 512; deleting one independent outer or corridor
projector increases it to 256. Deleting one anchored independent triangle
lowers its basis rank from 15 to 14. Deleting one row from the redundant
35-triangle symmetry family leaves rank 15, as it must.

For the static penalty

```text
H_code = sum_alpha (I - Pi_alpha),
```

the joint code is the zero eigenspace and the finite-cell penalty gap is
exactly one: flipping a single corridor blank violates exactly one projector.
This is a static code certificate. It is not physical energy and does not
provide dynamical enforcement, cooling, preparation, admissibility selection,
or genesis.

## The 13 integrated checks

| # | Executed check | Exact result |
|---:|---|---|
| 1 | ordinary source closure | five unique repo-relative inputs; no campaign fallback |
| 2 | 25-site/61-site geometry | zero shell/register/corridor collisions |
| 3 | decoded control coordinates | logical coordinates differ from signed-direction carrier sites; wrong-coordinate residual `sqrt(2)` |
| 4 | complete circuit word | 3,907 gates; zero non-NN, outside-carrier, or route-return failures |
| 5 | `W_A` reversibility | prepare residual `0`; inverse residual `8.92674853442885e-16`; flag failures `0` |
| 6 | full128 intertwiner | free-plus-seam residual `8.290102484032882e-15`; contact residual `0`; `E G` residual `8.40686768501364e-15` |
| 7 | commuting-projector code | 59 projectors; joint dimension 128; all `1,050 + 105 + 105` commutator checks pass; penalty gap 1 |
| 8 | all-column bare frames | 3,072 frame-columns; register residual `0`; update covariance residual `3.010942510752124e-15` |
| 9 | rotated word family | 24 × 3,907 gates; zero NN, support, order, or roundtrip failures; canonical equality in one frame only |
| 10 | frame products | all 576; zero cycle, cocycle, or carrier-coordinate failures |
| 11 | active deletions | pair-Z `2`; `W_A^dag` reset `sqrt(2)`; early-contact `0.36789306705608243`; one-site leakage `0.1839465335280422`; seam `16` |
| 12 | held domain | `L=3` train and `L=4` held/no-refit; zero collisions; four unlawful inputs rejected |
| 13 | resources | 61 semantic sites; 115 touched sites; radius 4; 729-site cube; exact 601/3,306 gate split |

## Complete authenticated transcript transport (2026-07-29)

The primary runner's complete cached stdout is below the audit packet's current
20,000-character per-section limit.  The authenticated record contains all 13
passing check lines, including the unabridged all-128 intertwiner diagnostic
with maximum residual `8.40686768501364e-15`, followed contiguously by the full
`SUMMARY_JSON` and terminal `RESULT` line.  Re-rendering the current restricted
packet therefore requires no clipped head/tail join.  This transport repair
changes neither the runner nor any calculation, predicate, tolerance, or claim
boundary in this note.

The complete circuit word has SHA-256
`a2e461d4984e4901fa0e8902c289ed2543da7545370891b96f2b50c6ba7f0fbf`.

## Supplied structure

The theorem supplies, rather than derives:

- the signed mode order `(+x,-x,+y,-y,+z,-z)`, one seam-port label, and the
  bounded decoded wire order;
- the `K7`-plus-reference encoder graph, the 25 shell coordinates, 30
  ordered-pair coordinates, six corridor coordinates, and radius-four carrier;
- 15 cycle `|+>` auxiliaries, three repetition blanks, 30 register blanks, six
  corridor blanks, and the local reference-parity completion;
- the spanning-tree/chord encoder basis, pair preparation order, returned flag,
  Clifford+T decompositions, fixed Manhattan axis order, and finite gate word;
- `beta=-0.3`, contact coupling `g=0.37`, the coin/reverse/seam/contact factor
  order, and attachment of the canonical seam to the `-x` mode;
- the one-particle mass fixture `m=3 tan(-beta/2)`, numerical tolerances, and
  deterministic test inputs;
- the standard translation and proper-cubic coordinate actions; and
- the rotated seam-word family used for covariance.

Derived on that supplied finite surface are the exact encoder ranks, full128
intertwiner, returned-work circuit, local contact and seam actions,
commuting-projector code, active deletions, resource census, held-size control,
and all-24/all-576 covariance results listed above.

## Claim boundary

This note does not establish a recurrent or two-cell compiler, overlapping
shared-port consistency, or a complete lattice stream law. It does not make
the supplied schedule into an autonomous microscopic law. It does not derive
the code preparation, dynamical enforcement, cooling, or genesis; derive the
mode labels, couplings, factor order, routing program, or seam attachment from
the framework axioms; or identify one fixed off-code coordinate word as
proper-cubic invariant.

The construction assigns no physical time, transition rate, physical energy,
source, stress, gravity, framework Record, realized-history, or Born/probability
meaning. The static `H_code` penalty is not called physical energy. A circuit
substep is not called time or a rate. No pointer copy is called a Record.

No minimum-content, impossibility, shared-obstruction, no-go, or axiom-pressure
claim is made. The result is a positive bounded construction on its declared
code and supplied finite carrier.

## Prior-art and novelty boundary

Exterior/Fock lifts, reversible binary encoders, CNOT/SWAP synthesis,
nearest-neighbor swap routing, Clifford+T gate decompositions, antisymmetric
pair registers, and commuting-projector penalties are standard finite methods.
This note claims no global literature priority for any of them.

The new campaign result recorded here is their exact combination for this
specific six-mode-plus-seam update: a full128 physical-M2 intertwiner with the
stated local contact/seam block, resources, deletions, static code projectors,
and bare-coordinate proper-cubic code-space covariance. The historical
`Cycle 230 coarse target fixture` is contextual provenance for the supplied
coin/contact target only; no Cycle 230 source object is imported, and the
present source closure supplies and recomputes its exact finite matrices and
constants directly. The archived context path is
`docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md`.
This note does
not turn that historical calculation into a recurrent law or extend an
unrelated prior-art engine.

## Dependency closure and reproducibility

The executable closure is exactly the four primary runners plus two ordinary
repo-local helper modules:

- `scripts/frontier_full128_cycle_encoder_2026_07_24.py`;
- `scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py`;
- `scripts/frontier_full128_25site_nn_supplied_schedule_2026_07_24.py`;
- `scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py`;
- `scripts/frontier_full128_code_projectors_2026_07_24.py`; and
- `scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py`.

The primary runners declare their complete mutable source closure in literal
`AUDIT_INPUT_PATHS` tuples. Imports are ordinary repo-local Python imports.
There are no `/tmp` fallbacks, network calls, archived-object reads, or hidden
campaign inputs. NumPy is the only non-standard-library runtime dependency.
Every audit source is smaller than 40,000 bytes.

The receipt records the final source, note, and cache hashes together with the
four primary check counts and the integrated residual/resource/deletion/domain
inventory. Authority remains `none`; audit remains `unset`. Only the
independent audit lane may set an audit verdict or effective status.
