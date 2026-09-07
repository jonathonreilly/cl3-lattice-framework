import sys, pathlib
p = pathlib.Path(sys.argv[1]); t = p.read_text(encoding="utf-8"); orig = t
def rep(old, new, count=1):
    global t
    assert t.count(old) == count, (old[:80], t.count(old))
    t = t.replace(old, new)
# fence 1 (must match the runner's FENCES[0] verbatim)
rep("This note selects no physical formation order; the row sweep is a declared order whose exact solvability is a property of two-recorded-neighbor sweeps on two-dimensional windows.",
    "This note selects no physical formation order; the row sweep is a declared order whose exact solvability is a property of sweeps in which each site forms with one in-row predecessor and the site below it as its recorded neighbors, on two-dimensional windows with an unrecorded exterior.")
# strips: exterior unrecorded on both sides; rows indexed by N
rep("**Strips and the sweep.** `S_{W,n}` is the `W × n` grid (rows `i = 0..n−1`,\ncolumns `j = 0..W−1`, nearest-neighbor edges, open boundary); `S_W` is the\ninfinite strip (rows indexed by `N`);",
    "**Strips and the sweep.** `S_{W,n}` is the `W × n` grid (rows `i = 0..n−1`,\ncolumns `j = 0..W−1`, nearest-neighbor edges, open boundary: as a window of\n`Z^3` every strip site also has out-of-plane and out-of-strip neighbors, and\nthey carry no records on either side of the comparison — under the\nrecords-only reading they contribute nothing to the formation law, and the\nstatic law is the open-boundary one); `S_W` is the infinite strip (rows\nindexed by `N`; a two-sided strip is not needed, see F5);")
# E3: the width restriction lemma made explicit
rep("On the quadrant (the half-plane swept row by row\nfrom the left end), the law of the first `J + 1` sites of row `i` depends\nonly on the first `J + 1` sites of row `i − 1`, so it is the width-`(J + 1)`\nstatement: every finite-width marginal of every row is the path chain. ∎",
    "On the quadrant (the half-plane swept row by row\nfrom the left end), the restriction lemma holds: every site's recorded\nneighbors lie in its own column or to its left, so the formation law of width\n`W` restricted to the first `W'` columns is the width-`W'` formation law\n(executed at `3 → 2` on the two-row joint, D9), the finite-width marginals are\nconsistent, and the Kolmogorov extension on the countable product gives the\nquadrant's law, whose every finite-width row marginal is the path chain. ∎")
# E4 hypothesis: transitivity sufficient, not necessary
rep("Theorem E is proved here\nfrom transitivity and `Z_2 = Z_1^2 K^2`.",
    "Theorem E is proved here\nfrom the symmetry of `φ` and the constancy of `Z_1` (on this menu a consequence\nof transitivity; a symmetric pair weight with constant row sums on a\nnon-transitive menu satisfies the same two hypotheses), through `Z_2 = Z_1^2 K^2`.")
rep("One classical\nobservation is referenced only, as `classical: certain sequential lattice\nprocesses have product-form or Markov-chain invariant row measures`; no\nauthor claim is made and nothing is taken from it",
    "One classical\nobservation is referenced only, as `classical: certain sequential lattice\nprocesses have product-form or Markov-chain invariant row measures — the\nPickard / Markov-mesh construction`; no author claim is made and nothing is\ntaken from it")
# F3: boundary independence licenses "the" static law; the one-sided strip's deep rows
rep("and the center-row law converges to `w(ρ) ∝ A(ρ) ρ_1(ρ)^2`, geometrically\nwith ratio `|λ_2/λ_1|`.",
    "and the center-row law converges to `w(ρ) ∝ A(ρ) ρ_1(ρ)^2`, geometrically\nwith ratio `|λ_2/λ_1|` taken in `Q`'s spectrum. The limit does not depend on\nthe records at the two ends of the strip: for any nonnegative nonzero boundary\nvectors `b_L`, `b_R` (any exterior records on the first and last rows),\n`b_L T^c / λ_1^c` and `T^{n−1−c} b_R / λ_1^{n−1−c}` converge in direction to\n`A ρ_1` and `ρ_1` because their Perron components `b_L · ρ_1` and\n`(A ρ_1) · b_R` are positive, so the deep-row law is `w` whatever the end\nrecords (executed with `P(e_y)` records on both end rows at `n = 13`, E11);\nthe same argument gives `w` as the law of row `i` of the one-sided strip\n(rows indexed by `N`) as `i → ∞`, which is the object F5 compares with.")
# N1 route 1: monotone row orders only; the panel survey as leads
rep("row sweeps with any per-row direction and any row order are covered by Theorem E (each row is still a path swept from an end with one recorded neighbor below; `p_0` is reversal-invariant since `K` is symmetric); diagonal or random sweeps in which some site forms with two recorded neighbors that have no common earlier neighbor are not covered by E and are not executed — their obligation is a separate solvability argument",
    "row sweeps with the rows formed in increasing or decreasing order, each row swept from either end, are covered by Theorem E (the strip reflection maps a right-to-left row onto a left-to-right one and `p_0` is reflection-invariant since `K` is symmetric), and column sweeps by the transposed argument; orders in which some site forms with recorded neighbors above and below, or with two recorded neighbors that have no common earlier neighbor, are not covered by E and are not executed here — the panel's exact grid survey (pack `REVIEW_HISTORY.md`) found the row law kept by diagonal sweeps and by the snake order and broken by a scrambled order and by the ends-inward path order; those are leads for the next block, not claims of this note")
# Boundaries: rows in N; the order class
rep("Further: Theorem C2 is existence only, along a subsequence, for the finite\nmenu;",
    "Further: the infinite strip and the quadrant have rows indexed by `N` (a\nfirst row exists; the formation law is defined without any limit); the\nexactly solvable order class is the one in the first fence, not every order\nwith at most two recorded neighbors (the ends-inward path order of block 01\nhas two recorded neighbors at its last site and its formation law is not the\npath chain); Theorem C2 is existence only, along a subsequence, for the finite\nmenu;")
# C2 wording: choice principle
rep("(bounded sequences of rationals in\n`[0, 1]` have convergent subsequences by bisection — no choice principle is\nused beyond countable selection along an explicit rule)",
    "(bounded sequences of rationals in\n`[0, 1]` have convergent subsequences by bisection; the countable diagonal\nextraction uses only dependent choice along an explicit rule, never the full\naxiom of choice)")
# translation average: name the two facts
rep("a diagonal\nsubsequence in `L` converges on every cylinder to a measure `μ̄` that is\ntranslation invariant and satisfies the identity by the same passage to the\nlimit. ∎",
    "a diagonal\nsubsequence in `L` converges on every cylinder to a measure `μ̄` that is\ntranslation invariant and satisfies the identity by the same passage to the\nlimit (the identity is preserved under convex combinations and under\ncylinder-wise limits, and the boxes `B_L` have boundary-to-volume ratio\n`2L^2/L^3 → 0`). ∎")
# obligation table rows for D9/E11
rep("| `p_0 P = p_0` (E3) by telescoping; the pair laws (E4) | proved here for every `W`; executed `W = 2, 3, 4` (D2, D5) and (D3) |",
    "| `p_0 P = p_0` (E3) by telescoping; the pair laws (E4); the width restriction lemma | proved here for every `W`; executed `W = 2, 3, 4` (D2, D5), (D3) and (D9) |")
rep("| the center-row law formula and its limit (F3) | proved here; executed for `n ≤ 13` (E9) |",
    "| the center-row law formula, its limit and its boundary independence (F3) | proved here; executed for `n ≤ 13` (E9) and with end records (E11) |")
# review record: fill in
rep("Fable primary seat (own 28-mutation census, read from raw per-mutation\nstdout); refuting checker: pending; independence class: to be filled by the\nsupervisor.",
    "Fable primary seat (own 28-mutation census, read from raw per-mutation\nstdout; two checks and two mutations added by the supervisor at the fold, D9\nand E11, census re-run at 30); a hostile refuter lens on the contract before\nthe build (Opus 5; exact order survey on finite grids; the fence's order class\nand the transitivity sentence corrected on its findings); refuting checker\n(Opus 5, disjoint machinery): __CHECKER__; supervisor line-by-line review of\nthe runner and the note with three exact control scripts. Independence class:\nsingle family (Claude), cross-model.")
# "37 checks, 28 mutations" in Result up front
rep("Executed with exact arithmetic: 37 checks, 28 mutations.", "Executed with exact arithmetic: 39 checks, 30 mutations.")
rep("Each of the 28 declared mutations", "Each of the 30 declared mutations")
rep("Expected final line:\n`TOTAL: PASS=37 FAIL=0`.", "Expected final line:\n`TOTAL: PASS=39 FAIL=0`.")
assert t != orig
p.write_text(t, encoding="utf-8"); print("note patched:", len(t.splitlines()), "lines")
