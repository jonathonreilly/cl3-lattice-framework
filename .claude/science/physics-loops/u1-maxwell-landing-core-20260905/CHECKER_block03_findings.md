# CHECKER block 03 — independent refuting check of the Gauss-rows-as-support-forcing note

**Verdict: FIX FIRST**

Every mathematical claim in the note survives a from-scratch attack. I rebuilt the
compilation with my own sign conventions and my own state layout, classified the
covariant nearest-neighbour generator class by a completely different route (signed
orbit counting under the generated symmetry group, no pattern basis assumed),
re-derived both Gauss rate functionals as a *solve* rather than a check, recomputed
the collapse, the maximal invariant subspaces, the branch multiplicities (against an
independent Fourier prediction), the charged-surface statements, the coin class, its
conservative cut, its Gauss cut and both coin witnesses, and the hidden-time identity.
**Seventy-four independent checks, seventy-three pass and the one non-pass is a defect
in my own assertion (below), not in the note: no verdict in the four-row obligation
table is refuted.** The collapse theorem and the coin residual
both stand. Three mutations planted in the primary's runner were all caught, and a
fourth probe reproduces one row of the primary's own mutation table exactly.

What must be fixed before the PR:

- **CK-01** the note repeatedly attributes *both* Gauss rows to "the class's own fifth
  item"; #7917's item 5 declares only the **magnetic** row (plus gauge invariance of
  the edge-to-face map). The electric row — the one that does the vertex half of the
  work — is not an item of the declared class. The headline consequence ("not an
  independent supply … inside the class's own other items") is therefore true of the
  cube half and overstated for the vertex half.
- **CK-02** the audited `claim_scope` and the EC premise say "translation-covariant"
  and "the 24 proper cubic rotations". Read literally, that names a **five**-dimensional
  class, not the ten-dimensional one (executed below): the theorem needs *even*
  translations and rotations about *even-parity centres*. Sections 2–3 say this; the
  audited sentences do not.
- **CK-03** the no-go gate's N1 preamble claims every closed route is "executed in this
  block's runner or excluded by an approved premise node". Route R7 is excluded by an
  unlanded PR's execution (block 02's eight-component bound), which this runner never
  performs and which section 11 says is "not used as a premise".

Object under attack, all read complete:
`docs/U1_GAUSS_SUPPORT_FORCING_EXTENDED_PAYLOAD_CLASS_BOUNDED_NOTE_2026-09-05.md` (806
lines), `scripts/u1_gauss_support_forcing_extended_class_2026_09_05.py` (1,301 lines),
`logs/runner-cache/u1_gauss_support_forcing_extended_class_2026_09_05.txt` (89/0, pin
`119500b2…7080`, re-verified by `shasum` against the file on this branch),
`GOAL_block03.md`, `RESULTS_block03.md`. Block 02's note is context only.

Framework refresher read first, complete: `docs/MINIMAL_AXIOMS_2026-06-29.md` (233
lines: the four named axioms Lattice / Qubit / Admissibility / Record, the
Qualification with the law sentence, the "Admissibility is not a dynamics axiom"
boundary, the open-gates list, and — the reading the note leans on — reading note (3),
`"available"/"admissible" denotes its support -- on finite menus, exactly the
possibilities of nonzero probability`, together with the 2026-08-05 history paragraph
"availability became the distribution's support");
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (do not classify a registered
primitive as an axiom, an import, a wall or a source of bounded status; grant no more
than the source note declares); `docs/audit/data/axiom_premise_nodes.json` (four
canonical nodes: `minimal_axioms`, `scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`). None of the three primitives
supplies a Gauss row, a payload clause or a constraint-preservation principle — the
note's registry check is correct.

Machinery, disjoint by construction (`/private/tmp/claude-502/b03check/`, the primary's
runner never imported): `lib.py` + `c1_class.py`, `c2_collapse.py`, `c3_sector_coin.py`,
`c4_coin.py`. Differences that make it a real second opinion: one state vector in
**lexicographic site order** (the primary groups by role); incidence maps as full
`n x n` matrices; **sign conventions flipped** (`D0 = -d0`, `D2 = -d2`, `CURL` built
from Levi-Civita symbols and negated); the class obtained by **signed orbit counting**
(union-find with parity over the 448 / 1512 nearest-neighbour coordinate pairs) instead
of a 56-pattern nullspace; the conservation cut read off the **assembled** matrices
rather than a hand-written block list; ranks over two primes with exact rational RREF
where the answer is load-bearing.

---

## Findings

### CK-01 — "item 5's Gauss rows": item 5 declares only the magnetic row (MEDIUM, fix before PR)

**Attacked sentences.** Section 1: "This note asks whether the class's own fifth item —
the Gauss rows — buys any of it." Result-up-front: "Its vertex/cube half is not an
independent supply once item 5's Gauss rows are read as support forcing (all-charge
reading) inside the class's own other items." `next_trace_action`:
"DERIVED-CONDITIONAL-ON(item 5's Gauss rows read as support forcing, the class's other
items, conservation)". Imports: "Provenance: the light lane's members (the open PRs
`#7893`, `#7903`, `#7917` item 5)".

**Independent evidence.** `git show FETCH_HEAD:docs/U1_MINIMAL_PHYSICAL_NEIGHBOR_
CONSERVATIVE_GAUGE_DYNAMICS_UNIQUELY_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-03.md` on
`physics-loop/u1-maxwell-generator-uniqueness-classification-20260903` (the head branch
named by `gh pr view 7917`), item 5 verbatim: "5. the edge-to-face map is invariant
under `A -> A+d_0 lambda` and preserves the magnetic Gauss row;". One row, the magnetic
one, plus a gauge-invariance clause on the block `L`. The electric row occurs in that
note only twice, in the section-6 mode count ("After the electric and magnetic Gauss
rows remove the two longitudinal zero directions") and in a runner-coverage line — it is
used there, never declared as a class item, and no background charge `rho_V` appears.
The note under check knows this: its section 9 opens "Block 02 read item 5's 'preserves
the magnetic Gauss row' …".

**Why it matters.** The vertex half of item 7 is derived from SF-all on the *electric*
row. If that row is not one of the class's own items, the vertex half does not "fold
into the class's other items": it folds into an **externally supplied** row (from
`#7893`/`#7903`, transported to this compilation — itself a supplied identification the
Imports section already flags). The verdict line is unaffected (it names SF-all on the
electric row explicitly), and the cube half is unaffected (item 5 does declare the
magnetic row). Only the two "splits inside the class" sentences overstate.

**Narrowest fix.** In the consequence bullet, the `next_trace_action` and the Imports
row, write "item 5's magnetic row together with the electric row supplied by `#7893`/
`#7903` (used by `#7917`'s section-6 mode count, not declared among its seven items)".
One clause, three places; no runner change.

### CK-02 — the audited scope sentence names a five-dimensional class (MEDIUM, fix before PR)

**Attacked sentences.** `claim_scope`: "the translation- and proper-cubic-covariant real
linear nearest-neighbor generator class under the oriented four-role transformation law
in the compilation's sign basis is exactly the ten-dimensional span". Premise EC: "the
law is covariant under lattice translations and the 24 proper cubic rotations acting on
the four-role payload".

**Independent evidence (executed).** Under the group generated by the two 90-degree
rotations about a vertex and the three even translations, the covariant
nearest-neighbour class has dimension **10** — 10 sign-consistent orbits out of 448
coordinate pairs on side 4 and 1512 on side 6, computed by union-find with parity, with
no pattern basis assumed (`c1_class.py`). Adding the translation by `(1,1,1)` — a
"standard translation" of the Lattice axiom, and the very translation the note uses for
its own self-duality lever — cuts the class to **dimension 5** (side 4). Separately, a
90-degree rotation about an *edge-role* site does not preserve the role labels at all,
so "proper cubic rotations about each site" (Lattice) is not what EC can mean either;
only rotations about even-parity centres are available.

The theorem is not wrong — sections 2 and 3 say "even translations" and "about a
vertex", and I reproduce ten dimensions under exactly that group — but the two sentences
an auditor reads as the scope and the premise say something else, and the something else
is a different class.

**Narrowest fix.** `claim_scope`: "even-translation- and proper-cubic-covariant (rotations
about vertex-role centres)". EC: "covariant under the even lattice translations that
preserve the sector and the 24 proper cubic rotations about a vertex-role site". Two
sentences; no runner change (the runner already tests only even translations —
`translation4` asserts it).

### CK-03 — N1's preamble is false as written: R7 is excluded by an unlanded PR's execution (MEDIUM, fix before PR)

**Attacked sentences.** N1: "every closed route is executed in this block's runner or
excluded by an approved premise node." Row R7: "RULED OUT BY PRIOR (block 02's executed
bound; the open PR `#7980` at its scope, an evidence address)". Section 11: "The
eight-component capacity bound is block 02's and is cited as context, not used as a
premise."

**Independent evidence.** `#7980` is open and unlanded, has no ledger row (N4 says so),
and is not one of the four canonical nodes in `axiom_premise_nodes.json`. The runner
performs no check of the real dimension of `M_2(C)`: the 89 checks in the cached receipt
contain no capacity computation (grep of the runner for `M_2`/`eight`/`capacity`: only
the memo-sentence needle). So R7 is excluded neither by this runner nor by an approved
premise node — the third possibility, an unlanded PR's execution, is exactly what
section 11 says is not used as a premise. The same pattern recurs in N2, whose
`W_G`/`W_EC`, `W_C`/`W_coin` and `W_EC`/`W_coin` rows use block 02's improved-curl and
damped laws as witnesses; there the provenance is at least named in the cell.

**Why it matters.** N1 is the alternative-route enumeration of a family-level negative
claim. A route excluded by content that the note itself declares non-premise is an open
route on the note's own accounting.

**Narrowest fix (cheapest).** Add one exact check to the runner — the real dimension of
`M_2(C)` is 8, one line, no dependency on block 02 — and mark R7 "ATTEMPTED (executed
here)". Alternatively, reword the N1 preamble to "…executed in this block's runner,
excluded by an approved premise node, or excluded by an evidence address quoted at
scope, marked as such", and drop "not used as a premise" from section 11 in favour of
"used only to exclude route R7 in N1, at that PR's scope".

### CK-04 — the doubled ("coin") transformation law is a load-bearing premise, named only in passing (LOW-MEDIUM)

**Attacked sentence.** Section 7: "the 120 translation-covariant nearest-neighbor
patterns … have covariance nullspace of dimension sixteen under the rotation group …
`span{onsite E, onsite B, C, C^T} (x) M_2(R)` — the coin index is inert under
rotations." The parenthetical reads as a finding; it is a stipulation.

**Independent evidence (executed).** With the coin index inert I reproduce dimension
**16** on sides 4 and 6 (orbit counting, 960 and 3240 coordinates). With the second
component carrying the sign character of the rotation group — `rho (x) diag(1, chi)`,
an equally genuine real representation of the same group, and no less "oriented" than
the chosen one — the class has dimension **12**, and the mixing witness `K = [[1,1],[0,1]]`
is *not* covariant there (the coin-off-diagonal blocks are cut). The GENUINE SUPPLY
verdict survives the alternative (a conservative, both-rows-preserving law with two real
components per site still exists, e.g. `K = diag(1,2)`), but "sixteen-dimensional",
"six-parameter", "six to four" and the covariance of witness two are all relative to the
inert-coin law, which is not in the section-1 premise list (SF-all, SF-0, EC, CONS,
CONN).

**Narrowest fix.** Add the doubled law to the EC bullet ("…and, for the coin class, the
doubled law in which the coin index carries the trivial representation — a supply of the
same kind as OL"), and add to the falsifier list "a different real representation of the
rotation group on the coin index changes the class dimension (12 for the sign
character); the sixteen is relative to the declared doubled law".

### CK-05 — under SF-all every surviving coin member is, over the reals, two decoupled copies (LOW)

**Attacked sentence.** Result table row 3: "the rows cut only the two onsite mixings (six
to four) and cannot cut the coupling `K (x) C`"; section 7: "In neither reading does the
second component disappear."

**Independent evidence (executed).** Solving the SF-all condition inside the
six-parameter conservative coin family, the survivors are exactly `theta_E = theta_B = 0`
(rank of the surviving `K` block 4, of the onsite mixings 0 — `c4_coin.py`), i.e. exactly
`K (x) C` with `R = -W_E^{-1} K^T W_B`. Every such member is orthogonally equivalent to
**two independent copies of the one-speed law** at the two singular values of
`W_B^{1/2} K W_E^{-1/2}`: I verified the real SVD `U^T K V` diagonal exactly over
`Q(sqrt 5)` for the note's own witness. So the SF-all residue is never a *coupled* coin —
a genuinely coupled coin (kernel dimension 0) survives only the zero-charge reading. The
note has both halves of this (section 7's paragraph on witness two, N6's second bullet)
but states it only of the witness; the headline row can be read as leaving a coupled coin
at the all-charge reading, which is false.

**Narrowest fix.** One sentence in section 7: "Under SF-all the residue is exactly
`K (x) C`, and every member of it is orthogonally equivalent to two decoupled one-speed
copies at the singular values of `W_B^{1/2} K W_E^{-1/2}`; two components per site and
two speeds remain, a coupled coin does not." The verdict is unaffected — a direct sum of
two one-component laws still violates item 7's one-component clause and the terminal's
"one speed".

### CK-06 — SF-0 is used in two inequivalent senses, and a third reading exists (LOW)

**Attacked sentences.** Section 1 defines SF-0 as the *sector* reading ("the law is only
required to have a consistent restriction to the admissible set"). Section 7 uses
"Under SF-0 every zero-charge surface is preserved by every member and nothing is cut",
which is the *zero-charge-surface-invariance* reading.

**Independent evidence (executed).** For the four-role class the two are not equivalent.
Requiring the zero-charge surface itself to be invariant cuts the ten-parameter class to
**9** (`a2 = 0`, `u_E` free) on both sides — a coefficient statement — whereas the sector
reading cuts nothing (the three-speed member keeps a 112-dimensional sector). For the
record the three readings cut the class to 8 (SF-all: `a2 = u_E = 0`), 9
(zero-charge surface invariance) and 10 (sector). Under CONS the first two coincide,
which is why the note's verdict does not depend on the choice — but the naming does.

**Narrowest fix.** Name the middle reading, or rename section 7's use: "on every
zero-charge surface the rate vanishes identically, so neither reading cuts anything".

### CK-07 — branch-count sentence miscounts its own branches (LOW, cosmetic)

Section 5: "Off the sector there are three branches at each of the 26 nonzero coarse
momenta: two transverse at speed one (52 modes) and one longitudinal at speed two
(26 = 6 + 12 + 8); the cube coupling adds a third branch at speed three on the face
side." Two transverse plus one longitudinal is already three; the cube branch is a
fourth. The multiplicities themselves are right (I reproduce `{0:3, 3:12, 6:24, 9:16,
12:6, 24:12, 36:8}` on the E side and the face-side `{…, 27:6, 54:12, 81:8}`). Fix: "a
further branch". The same wording is in the runner's check label for the B-block.

---

## What I could not break — the attacks that failed

Every one of these was an attempt to refute, executed on my own machinery; all confirmed
the note.

| attacked claim | independent route | result |
|---|---|---|
| the class is exactly ten-dimensional | signed orbit counting over all 448 / 1512 NN coordinate pairs, no pattern basis, sides 4 and 6 | 10 sign-consistent orbits, exactly the four onsite terms and `d0, d0^T, C, C^T, d2, d2^T`; no missed member |
| chain identities, row patterns, distance-1 incidence, connectedness lever, zero-sum charge, dipole solvable / monopole not | my flipped-sign compilation | all reproduce |
| odd-shift self-duality `(d0, C, d2) -> (-d2^T, C^T, -d0^T)` | rebuilt in the primary's stated sign basis *and* in mine, entry by entry, sides 4 and 6 | exact both ways |
| conservation cut = three speeds | symbolic `M G + G^T M = 0` read off the **assembled** matrix (not a hand-written block list), side 4 | identical solution set (`sympy` solves for `a, q, b` instead of `a2, r, b2`; the ratios agree) |
| `d/dt(d0^T E) = a2 d0^T d0 phi + u_E d0^T E`, `d/dt(d2 B) = b d2 d2^T psi + u_B d2 B` | computed each unit member's rate matrix and *solved* for which coefficients can contribute | exactly `{a2, u_E}` and `{b, u_B}`; `r` and `q` contribute the zero matrix (the chain identity); sides 4 and 6 |
| the invariance "iff" | solved the invariance condition as a linear system on the ten coefficients — no assumed rate form | SF-all cuts to dim 8 (`a2 = u_E = 0`), zero-charge surface to dim 9 (`a2 = 0`); magnetic mirror `{b, u_B}`; no member with `a2 != 0` preserves any electric surface |
| the collapse: CONS + both rows = the one-speed law | joint nullspace of the conservation and invariance systems, weights `(1,1,1,1)` and `(2,3,5,7)` | exactly one parameter, `w_E r = -w_B q`, all eight other coefficients zero; also one parameter under the zero-charge reading |
| maximal invariant subspace = `{d0^T E = 0, d2 B = 0, phi const, psi const}`, dim 112 (side 6), 36 (side 4) | own observability iteration, two-prime ranks, plus exact verification that the claimed subspace is invariant, that the two members agree on it, and that `phi, psi` have zero rate there | dims 50/164 (electric only) and 36/112 (both rows), row spaces identical, stabilises in 2 steps |
| `C^T C` on `ker d0^T`: `{0:3, 3:12, 6:24, 9:16}` | exact restricted ranks **and** an independent coarse-momentum Fourier prediction (`3 x #nonzero components`, two transverse modes per momentum) | both give the same table; sum 55; `C C^T` on `ker d2` the same; `-G^2` block diagonal |
| charged surface: `a a2 != 0` conservative member has no invariant subset; `a2 = 0, a = 3/2` drifts `phi` linearly | own affine-consistency test on the unobservable subspace, sides 4 and 6 | reproduced; and CONS with `a2 = 0` does force `a = 0` (positive weights), so the drifting member is necessarily non-conservative — the note says so |
| coin class 16-dimensional, conservative cut 6, Gauss cut 6 -> 4 killing exactly the onsite mixings, SF-0 cutting nothing | orbit counting for the class; assembled 324x324 matrices for the cut; solved Gauss cut inside the conservative family | 16 / 6 (two weight choices) / 4 with `K` rank 4 and onsite rank 0 / 6 |
| complex law: preserves both zero-charge rows, antisymmetric, radius 1, covariant, kernel 0 against 116, fails a charged row | rebuilt from scratch on my layout | all reproduce, including `ker G_theta = 0` vs `116` over two primes |
| `K (x) C` law: preserves every charged surface, mixes components, `K^T K` char. poly `lambda^2 - 3 lambda + 1`, discriminant 5 | rebuilt; exact SVD over `Q(sqrt 5)` | all reproduce (see CK-05 for the sharpening) |
| `z1'' = 2 G z1' - (G^2 + theta^2) z1`, `z2 = (G z1 - z1')/theta`, `G^2` radius 2 | own derivation and exact rational evaluation | reproduce |
| every axiom sentence quoted in the note | 15 quotations normalised and matched against the memo | all present; two cosmetic renderings only — single quotes for the memo's `"available"/"admissible"`, and the memo's soft hyphen `approved-\nprimitive` joined |
| PR quotations | matched against live bodies (`gh pr view`, 2026-09-05) and the `#7917` head-branch note | `#7917`'s result sentence and "Split-step and enlarged-state exact ticks remain live", `#7893`'s two sentences, `#7913`'s sector sentence, and item 7 "no vertex, cube, extra coin, or hidden time payload participates" — all verbatim |
| the primary's own quote-fidelity flag | searched `#7893`'s body and its head-branch note for "order-independent site-level support forcing among corner records" | absent from both — the primary's finding is correct; the note itself quotes only the body's own sentence |
| N4 ledger statuses | read `docs/audit/data/ledger/*/<id>.json` for all seven cited ids | 7/7 match: five `bounded_theorem`, two `no_go`, all `unaudited`; the `energy_gauss_constraint_obstruction_route_b` note's docs surface is indeed absent (the note says "archived") |
| N3 hidden-wall scan | grepped every scanned phrase | "by construction", "naturally", "obviously", "standard QFT", "bridge context" occur only inside the N3 sentence itself; "background" occurs only in "background charge"/"charges" (14 times); the scan claim is accurate |
| hidden "no route" sentence in N1–N8 | grepped for absolute negatives | none: the only "no route" strings are the gate's own disclaimers |
| the cached receipt | `shasum -a 256` of the runner against `runner_sha256`; runner re-run with `ROOT` repointed | pin matches, 89/0 reproduced, exit 0 |
| circularity | traced every use of block 02 and `#7917` | EC and CONS are *restated* in section 1, not imported as results; `#7917`'s classification is never a premise; the only leak is the capacity bound in N1/N7 (CK-03) |

---

## Mutation table

Scratch copies of the primary's runner under `/private/tmp/claude-502/b03check/mut/`
(`ROOT` repointed at the worktree by placing the copy in `mut/scripts/` with `mut/docs`
symlinked to the worktree; the repo copy untouched). Baseline: `PASS=89 FAIL=0`, exit 0.

| probe | defect planted | result | caught by |
|---|---|---|---|
| CKM-1 | sign flipped in the magnetic rate functional (`P = -comp.d2` in `gauss_rate_matrix`) | exit 1, `PASS=86 FAIL=3` | section F both rate identities, section L's minimal-payload identity |
| CKM-2 | invariance test made to accept `a2 != 0` (the "every other coefficient nonzero" member given `a2 = 1/7`) | exit 1, `PASS=88 FAIL=1` | section G's "invariance needs only `a2 = 0` / `b = 0`" check |
| CKM-3 | coin cut count broken (the coupling equations `W_E R + K^T W_B = 0` dropped from the conservative system) | exit 1, `PASS=87 FAIL=2` | both weight choices in section J (`free=10`, not 6) |
| CKM-4 (fidelity spot-check of the primary's own table) | second-order coefficient `2 -> 1` (their M13) | exit 1, `PASS=88 FAIL=1` | section K's `z1''` identity — exactly the row `RESULTS_block03.md` claims |

A defect that removes the `d0^T d0 != 0` hypothesis by disconnecting the torus is not
reachable: the compilation requires an even side, and every even torus is
nearest-neighbour connected (I re-verified `ker(d0^T d0) = ker(d2 d2^T) = constants` on
both sides), so the hypothesis cannot be falsified from inside the object.

---

## Reproduction

```text
python3 /private/tmp/claude-502/b03check/c1_class.py     # 22/22  compilation, duality, class = 10 (orbits)
python3 /private/tmp/claude-502/b03check/c2_collapse.py  # 14/15  conservation, rates, the iff, the collapse
python3 /private/tmp/claude-502/b03check/c3_sector_coin.py # 18/18 sectors, multiplicities, charged surfaces
python3 /private/tmp/claude-502/b03check/c4_coin.py      # 19/19  coin class, cuts, witnesses, hidden time
```

The single non-`ok` line in `c2_collapse.py` is my own assertion being over-specific:
`sympy` returns the conservation solution solved for `a, q, b` (`a = -a2 w_E/w_V`, …)
rather than for `a2, r, b2`; the two solution sets are identical and the note's form is
correct.

Independence class: no shared code with the primary's runner; different state layout,
different sign conventions, different classification algorithm, different rank strategy.
Same session family as the primary is *not* the case for the machinery; the note and
runner were read complete before any check was written.
