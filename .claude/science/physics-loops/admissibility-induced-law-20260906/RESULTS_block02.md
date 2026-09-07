# Results — block 02 (primary seat, Fable, 2026-09-06)

## Headline

On the infinite strips `S_2` and `S_3` of the lattice, the row-sweep formation
law of the product rule has the path static chain `p_0` on every row and the
single-edge law `(1/6) K` on every horizontal and vertical nearest-neighbor
pair (pair-parallel probability exactly `p/(p+q+4r)`: `1/4`, `5/23`), proved
by an exact telescoping identity for every width and length and executed at
widths 2, 3 and 4. The static law of the same strip has a center-row
pair-parallel probability `s_∞` that is an algebraic number (degree 3 at
`(3,1,2)`, degree 8 at `(5,2,4)` for `W = 3`) enclosed in exact rational
intervals of width below `10^-30` that exclude `1/4` and `5/23`. The
finite-window static laws with exterior records form a specification (executed
on the cube and plaquette) and an infinite-volume static law exists on `Z^3`
for the finite menu (native compactness proof; nothing about uniqueness).

## Run record

- Launch (system clock) 19:30 UTC; the supervisor's control numbers reproduced
  in the seat's own scratch code at 19:34 (`p_0 P = p_0` at width 3 both
  triples; `1/4` and `5/23` vertically and horizontally; 8 orbits with sizes
  `6, 12, 48, 6, 48, 24, 24, 48`; the width-3 characteristic polynomial at
  `(3,1,2)` verbatim; the degree-8 polynomial at `(5,2,4)` verbatim and
  irreducible). No control number differed.
- Timing in scratch before building: width-4 `p_0 P = p_0` with integer
  numerators 0.5 s per triple (executed, not cut); the exhaustive `6^8` cube
  static table 2.5 s per triple; the sympy steps (charpoly, factor, Sturm
  intervals to `10^-30`, the `Q(λ_1)` elimination, the 216-row lift check,
  the resultant, the finite-`n` products) under 1 s at `(3,1,2)` and about 5 s
  at `(5,2,4)`. Nothing was cut for budget.
- Runner: `scripts/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.py`,
  951 lines, seven families, 37 checks, 28 declared mutations, `--exact`
  flag for the exact rationals and polynomials. Unmutated stdout 5,798
  characters; baseline 26.9 s alone (36.8 s while the census ran alongside).
- Note: `docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md`,
  650 lines, `vocab_lint --report-only` 0 violations.
- Cache: `logs/runner-cache/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.txt`
  written by `execute_and_write_cache(<runner>, 900)` after the final note
  edit (the sha lines are in the certified-stdout section below).

## Defects found and fixed while executing

- Runner B2 (E1 symbolic identity): `sp.expand` of the difference does not
  cancel the common denominator `Z_1^2`; replaced by `sp.cancel` (the identity
  holds; the first form was a false negative).
- Runner C6: the seat's expected count of non-adjacent complement sites for
  the cube single-site sub-window was 3; the complement has 7 sites, 3
  adjacent, so 4. Corrected to the executed value.
- Note: the F2 (Wielandt) paragraph had a dangling fragment; rewritten. The
  first draft was 672 lines; trimmed to 650 without dropping any executed
  statement.
- Contract conflict resolved: `specs/primary_block02.md` asks
  `next_trace_action` to name the uniqueness region by the proper name that
  the same spec's F fence list forbids in the note. The fence wins: the region
  is described as "the contraction region of the one-site conditional's
  dependence on its six neighbors". The N8 table likewise says
  "contraction-coefficient bounds".
- Contract expectation refined: the contract left the second-eigenvalue ratio
  numeric at `(5,2,4)` pending complex-root handling. Every root of the octic
  is real (Sturm count 8), so the bound is exact by real-root isolation at both
  triples; no Fujiwara-type bound was needed.

## Could-not list

- None of the contracted computations was cut. Not attempted by contract:
  the static law at width 4 (only the sweep was contracted at width 4); the
  plane's static law; uniqueness on `Z^3`; any three-neighbor sweep beyond the
  cube witness.
- Route 6 of the N-gate (the marginal reading) is marked ATTEMPTED on block
  01's executed evidence and not re-executed in this runner.
- The convergence-rate statement in F3 relies on the executed simplicity of
  `Q`'s nonzero eigenvalues (distinct real roots); a general Jordan-block
  argument was not written because it is not needed at the executed triples.

## Modelling choices (declared, not physics)

- Cube site index `i = x + 2y + 4z`; block 01's exterior assignment (axis `a`
  exterior neighbor carries `P(e_a)`); sub-windows are the leading index sets
  (face `0..3` = the `z = 0` face; edge `0,1`; site `0`); the cube witness uses
  the index order `0..7` so the last site `(1,1,1)` has recorded neighbors
  `3, 5, 6`.
- The asymmetric control adds `[a < b]` to the `(3,1,2)` pair weight and uses
  `K(a → s) = φ(s,a)/Σ_t φ(t,a)` (the rule's own conditional).
- `G` is taken as the 48 maps (24 rotations, with and without reversal); the
  commutation check is exhaustive at `W = 2` and, at `W = 3`, on the 8 orbit
  representatives against all 216 rows and all 48 maps (a declared sample).
- The finite-`n` convergence check asserts strictly decreasing distance to the
  enclosure and a final distance below `10^-6`; both are executed facts.
- Decimal endpoints printed by the runner are exact integer-arithmetic
  truncations (lower) and roundings-up (upper); the exact rationals are under
  `--exact`.

## Exact enclosures and second-eigenvalue bounds (from `--exact`; every value an exact rational or integer polynomial)

### W = 3, triple (3, 1, 2)

- characteristic polynomial of `Q`: `lam**8 - 7312*lam**7 + 2578432*lam**6 - 221134848*lam**5`
- `λ_1` isolating interval (width < 10^-30): `[4402130830853675836634810902112391/633825300114114700748351602688, 8804261661707351673269621804224783/1267650600228229401496703205376]`
- minimal polynomial of `s_∞`: `2647547323586176*y**3 - 2190008305118016*y**2 + 544429860087294*y - 40261879885473`
- `s_∞` enclosure (width < 10^-30): `[6339549008993337177727595300160277139285829246818144949639964171415296412193/24753131742526218110404142519280925221559534044789955936869005382062937473024, 17433759774731677238750887075441353009682400623874825249477932412882125899483/68071112291947099803611391928022544359288718623172378826389764800673078050816]`
- finite-`n` center-row values: `[(3, '578647/2260844'), (5, '20456844081/79876422590'), (7, '770944922609499/3010200239734244'), (9, '60528391297616165323/236336570250352523934'), (11, '6843167550859767489473457/26719539161752512727788658'), (13, '6447241860308787366661273387875/25173624641196824716828215309466')]`
- second eigenvalue: `m`, ratio bound = `4158153097085676161155/18446744073709551616; ratio bound = 142873052509952736177660404695040/4402130830853675836634810902112391`

### W = 3, triple (5, 2, 4)

- characteristic polynomial of `Q`: `lam**8 - 185171*lam**7 + 1095911038*lam**6 - 1772274674784*lam**5 + 469450026668192*lam**4 + 67550038108063488*lam**3 - 17237755848001351680*lam**2 - 1439162188263618969600*lam - 14640126202850181120000`
- `λ_1` isolating interval (width < 10^-30): `[975153596898408371306948920541418138906773751/5444517870735015415413993718908291383296, 3900614387593633485227795682165672555627095005/21778071482940061661655974875633165533184]`
- minimal polynomial of `s_∞`: `32330789225473908021767435802416095357458632401858485927848001740598709841504285100845561527740443226484950508488783396*y**8 - 6466157845094781604353487160483219071491726480371697185569600348119741968 … 0*y + 139379584408240006527345980448879590158926475304754147709832923701600897621207143977329265605673096949058764800000 (degree 8; coefficients of about 120 digits; full text in the runner's `--exact` stdout)`
- `s_∞` enclosure (width < 10^-30): `[182841098503109846891750227620740544701688477342612509960927632489431884675995914528411072359384782327759198354595648877575723506891128289659501149092941817066 … 989730635773061824309768563380438972971860959243762845810137291729145813975894678489125501987564086285741773880927805218436858558114582369857235962513535795200] (exact endpoints of about 400 digits each; full text under `--exact`)`
- finite-`n` center-row values: `[(3, '3731173618465/16969587349457'), (5, '119716037792791450503185/544375382349486764567177'), (7, '768087720257216734305488815630597/3492654863932433332945094107153565'), (9, '123199245064469174430549022556299822630170785/560212603017039311080735986284938319420053273'), (11, '3952166619094536526121991548154992261048171547308338345/17971323981652852115713366066439361099382848697176316001'), (13, '126783414653255134126987072973522021287465394686160346920774885745/576510567442031609025187457013037849941322310423297468406491315177')]`
- second eigenvalue: `m`, ratio bound = `249130764926366412788905/73786976294838206464; ratio bound = 18382605845936708173555296472450222438481920/975153596898408371306948920541418138906773751`

### W = 2, triple (3, 1, 2)

- characteristic polynomial of `Q`: `lam**3 - 296*lam**2 + 2112*lam`
- `λ_1` isolating interval (width < 10^-30): `[182975250294392782176956959985107/633825300114114700748351602688, 365950500588785564353913919970215/1267650600228229401496703205376]`
- minimal polynomial of `s_∞`: `217712*y**2 - 178128*y + 31329`
- `s_∞` enclosure (width < 10^-30): `[6421443352071838104538466989312335/25089340679717116314422749840801792, 35317938436395109574961568441217961/137991373738444139729325124124409856]`
- finite-`n` center-row values: `[(3, '15987/62500'), (5, '20829675/81385228'), (7, '6781010547/26494222396'), (9, '35319956176587/137999258614660'), (11, '45992365235966163/179697625142145004'), (13, '14972397121010384067/58498931091895893868')]`
- second eigenvalue: `m`, ratio bound = `539822333886424224423/73786976294838206464; ratio bound = 4637038539385169244557898940416/182975250294392782176956959985107`

### W = 2, triple (5, 2, 4)

- characteristic polynomial of `Q`: `lam**3 - 2063*lam**2 + 67814*lam - 190440`
- `λ_1` isolating interval (width < 10^-30): `[2572867137924182429878944859920203/1267650600228229401496703205376, 643216784481045607469736214980051/316912650057057350374175801344]`
- minimal polynomial of `s_∞`: `3028734908421617*y**3 - 3028734908421617*y**2 + 846000180274080*y - 71785120563200`
- `s_∞` enclosure (width < 10^-30): `[3520148926335140812700497233200604761532046025609129238183282985401038457/16009833389203833018989545759505177799505687517498866084339776179192987648, 1070125273605882807060951158893165079623999680771385040045951987377354115883/4866989350317965237772821910889574051049729005319655289639291958474668244992]`
- finite-`n` center-row values: `[(3, '20828405/94745341'), (5, '85815657756405/390295414689013'), (7, '353511254231991882005/1607788937699950090037'), (9, '1456259757132936033740669045/6623150492945643386199095189'), (11, '5998938858014064907596491099100245/27283508067271289597261270372239477'), (13, '24712121052273284514159740178011680782645/112392103010449712044703908689732798828373')]`
- second eigenvalue: `m`, ratio bound = `558299531467563922715/18446744073709551616; ratio bound = 38366051664404958925606344458240/2572867137924182429878944859920203`

Decimal forms (rounded outward) as printed by the unmutated runner: `W = 3`: `s_∞ ∈ [0.2561109872857786908612, 0.2561109872857786908613]` vs `1/4`; `s_∞ ∈ [0.2199151616870197815075, 0.2199151616870197815076]` vs `5/23`; `|λ_2/λ_1| ≤ 0.0324554308` and `≤ 0.0188509851`. `W = 2`: `s_∞ ∈ [0.255943088901618766, 0.255943088901618767]`, `[0.219874176124090031, 0.219874176124090032]`; `|λ_2/λ_1| ≤ 0.02534244`, `≤ 0.01491179`. All roots of every characteristic polynomial are real (Sturm), so every bound is exact.

## Certified stdout (the pinned cache, verbatim)

```text
===== runner cache v1 =====
runner: scripts/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.py
runner_sha256: 1cd8762aba6c5582332c6455ca4a70ba84946690849c871abe5b0bec3374817a
input_fingerprint_sha256: 5545a1a6503b235b4e895328d80fa0cea89cb3c22ba81d244d57553fb14240ea
timeout_sec: 900
exit_code: 0
elapsed_sec: 37.14
status: ok
----- stdout -----
AUDIT_INPUT_PATHS:
  docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md
  docs/MINIMAL_AXIOMS_2026-06-29.md
  docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md
AUDIT_TIMEOUT_SEC: 900
scope: the six-projector menu, the product rule at two exact triples; strips of widths 2, 3, 4 (sweep) and 2, 3 (static); exact arithmetic; no plane, no cubic-lattice uniqueness, no order selected
mutation: none
PASS: A1 the three declared audit inputs exist
PASS: A2 axiom memo: both Admissibility sentences verbatim
PASS: A3 axiom memo: the four Record sentences verbatim
PASS: A4 parent note carries its claim id and the parent theorem sentence
PASS: A5 this note carries its claim id
PASS: B1 K = phi/Z_1 symmetric, rows and columns sum to one (symbolic), Z_1 = p+q+4r
PASS: B2 E1: Z_2(a,b) = Z_1^2 (K^2)(a,b) symbolic for all 36 pairs
PASS: B3 the uniform law is K-invariant (symbolic)
PASS: B4 p_0 = (1/6) prod K equals the end-swept path formation law, W = 2, 3, both triples
PASS: C1 cube face (sites 0-3): conditional = mu_Delta^{omega'} for all 6^4 complements, both triples
PASS: C2 cube edge (sites 0,1): all 6^6 complements, both triples
PASS: C3 cube site 0: all 6^7 complements, both triples
PASS: C4 plaquette edge with exterior (P(e_x), P(-e_y)): all 36 complements, both triples
PASS: C5 plaquette site with exterior: all 216 complements, both triples
PASS: C6 finite range: cube edge 1296 adjacent-record classes (2 non-adjacent sites), site 216 classes (4), plaquette site (1)
PASS: D1 E2 row kernel from the formula equals the kernel from the definition entrywise, W = 2, 3, both triples; rows sum to one
PASS: D2 E3: p_0 P = p_0 exactly for W = 2, 3, both triples (all 6^W row states)
PASS: D3 E4: every vertical and horizontal nearest-neighbor pair has law (1/6) K; the diagonal pair (alpha_0, beta_1) has law (1/6) K^2
PASS: D4 direct finite-strip formation law (W=2: n=2,3; W=3: n=2) = p_0 P^(n-1) on every row marginal and row-pair joint
PASS: D5 width 4: p_0 P = p_0 exactly on all 1296 row states (integer numerators), both triples
PASS: D6 constant rule (2,2,2): K uniform, p_0 uniform on 6^W states, p_0 P = p_0, W = 2, 3
PASS: D7 asymmetric-weight control: p_0 P != p_0 on 36/36 (W=2) and 216/216 (W=3) row states
PASS: D8 cube sweep 0..7 at (3,1,2): joint law of the last site's three recorded neighbors is not proportional to Z_3 (210/216 triples off)
PASS: E1 row orbits under G: 8 at W = 3, 3 at W = 2
PASS: E2 T(g rho, g rho') = T(rho, rho') for all 48 g: exhaustive at W = 2, orbit representatives x all rows at W = 3
PASS: E3 charpoly of Q at W = 3, (3,1,2) = lam^5 (lam^3 - 7312 lam^2 + 2578432 lam - 221134848)
PASS: E4 Perron root: minimal polynomial degrees W3 3,8 W2 2,3; isolating widths < 10^-30
PASS: E5 Perron vector of Q over Q(lam_1): Q x = lam_1 x on every row, all entries positive on the interval
PASS: E6 lift: T rho_1 = lam_1 rho_1 and (A rho_1)^T T = lam_1 (A rho_1)^T exactly in Q(lam_1), 216 and 36 rows
PASS: E7 s_inf: one irreducible factor of the resultant has exactly one root in the enclosure; width < 10^-30
info W=3 (3, 1, 2): lam_1 = 6945.337824257111..; s_inf in [0.2561109872857786908612, 0.2561109872857786908613] (rounded outward), formation value 1/4
info W=3 (3, 1, 2): finite n center row: n=3 0.2559429133, n=5 0.2561061627, n=7 0.2561108435, n=9 0.2561109828, n=11 0.2561109871, n=13 0.2561109872
info W=3 (3, 1, 2): |lam_j| <= m = 225.413932 for all non-Perron roots (all roots real); |lam_2/lam_1| <= 0.0324554308
info W=3 (5, 2, 4): lam_1 = 179107.428802830185..; s_inf in [0.2199151616870197815075, 0.2199151616870197815076] (rounded outward), formation value 5/23
info W=3 (5, 2, 4): finite n center row: n=3 0.2198741514, n=5 0.2199144959, n=7 0.2199151505, n=9 0.2199151614, n=11 0.2199151616, n=13 0.2199151616
info W=3 (5, 2, 4): |lam_j| <= m = 3376.351458 for all non-Perron roots (all roots real); |lam_2/lam_1| <= 0.0188509851
info W=2 (3, 1, 2): s_inf in [0.255943088901618766, 0.255943088901618767]; |lam_2/lam_1| <= 0.02534244; min poly degree 2
info W=2 (5, 2, 4): s_inf in [0.219874176124090031, 0.219874176124090032]; |lam_2/lam_1| <= 0.01491179; min poly degree 3
PASS: E8 the enclosure of s_inf excludes the formation value p/(p+q+4r) at W = 2, 3, both triples
PASS: E9 finite-n center-row values n = 3..13: distance to the enclosure strictly decreasing, final < 10^-6
PASS: E10 second eigenvalue: all charpoly roots real; every non-Perron root in [-m, m] with rational m < lam_1 (Sturm)
PASS: F1 the note carries the four fence sentences verbatim
PASS: F2 the note contains no forbidden phrase (hits: [])
PASS: F3 runner source: no floating-point literal, conversion or evaluation call (0 hits)
per_element: executed — every row state of the width-2, 3 and 4 strips, every configuration of the cube and plaquette sub-window checks, both triples, exact
per_site: executed — the sub-window conditional at every site class (face, edge, site) of the cube and the plaquette; every column of every row of the strip pair laws
per_mode: executed — the quotient transfer matrix's characteristic polynomial, its Perron root, eigenvector and second-eigenvalue bound, all exact (Sturm, resultant, Q(lam_1))
per_block: executed — the row-to-row kernel block by block for widths 2, 3, 4; the finite-n center-row values for n = 3..13; the cube's three-neighbor witness
lattice_wide: checked and not executed — strips of widths 2 and 3 only for the static law; the plane and the cubic lattice's infinite-volume law are named, not computed
PASS: G1 the five N5 resolution lines are printed (each >= 40 characters)
TOTAL: PASS=37 FAIL=0

----- stderr -----
```


## Mutation census (28 mutations, one helper invocation each, 4 in parallel; expected/observed read from raw stdout; runner sha 1cd8762aba6c5582332c6455ca4a70ba84946690849c871abe5b0bec3374817a)

| mutation | expected | observed | total | failing checks | verdict |
|---|---|---|---|---|---|
| `kernel_not_doubly_stochastic` | B | B | PASS=34 FAIL=3 | B1 B2 B3 | ok |
| `z2_identity_wrong_power` | B | B | PASS=36 FAIL=1 | B2 | ok |
| `path_law_not_formation` | B | B | PASS=36 FAIL=1 | B4 | ok |
| `spec_conditional_ignores_exterior` | C | C | PASS=31 FAIL=6 | C1 C2 C3 C4 C5 C6 | ok |
| `spec_conditional_two_hop` | C | C | PASS=31 FAIL=6 | C1 C2 C3 C4 C5 C6 | ok |
| `spec_face_wrong_subwindow` | C | C | PASS=36 FAIL=1 | C1 | ok |
| `row_kernel_formula_wrong_denominator` | D | D | PASS=36 FAIL=1 | D1 | ok |
| `row_kernel_drops_left_neighbor` | D | D | PASS=33 FAIL=4 | D1 D2 D3 D4 | ok |
| `invariance_forced_true` | D | D | PASS=36 FAIL=1 | D7 | ok |
| `pair_law_wrong_column` | D | D | PASS=36 FAIL=1 | D3 | ok |
| `direct_strip_law_mismatch` | D | D | PASS=36 FAIL=1 | D4 | ok |
| `asymmetric_control_passes` | D | D | PASS=36 FAIL=1 | D7 | ok |
| `constant_rule_not_uniform` | D | D | PASS=36 FAIL=1 | D6 | ok |
| `three_neighbor_witness_forced` | D | D | PASS=36 FAIL=1 | D8 | ok |
| `orbit_count_wrong` | E | E | PASS=36 FAIL=1 | E1 | ok |
| `quotient_not_commuting` | E | E | PASS=36 FAIL=1 | E2 | ok |
| `charpoly_coefficient_off` | E | E | PASS=36 FAIL=1 | E3 | ok |
| `perron_interval_wrong_root` | E | E | PASS=34 FAIL=3 | E5 E9 E10 | ok |
| `eigvec_residual_nonzero` | E | E | PASS=35 FAIL=2 | E6 E9 | ok |
| `limit_law_uses_rho_not_squared` | E | E | PASS=36 FAIL=1 | E9 | ok |
| `s_inf_enclosure_contains_formation_value` | E | E | PASS=34 FAIL=3 | E7 E8 E9 | ok |
| `finite_n_sequence_shuffled` | E | E | PASS=36 FAIL=1 | E9 | ok |
| `second_eigenvalue_bound_too_small` | E | E | PASS=36 FAIL=1 | E10 | ok |
| `claim_order_selected` | F | F | PASS=36 FAIL=1 | F2 | ok |
| `claim_plane_static` | F | F | PASS=36 FAIL=1 | F2 | ok |
| `claim_z3_uniqueness` | F | F | PASS=36 FAIL=1 | F2 | ok |
| `claim_washout` | F | F | PASS=36 FAIL=1 | F2 | ok |
| `claim_gate_fired` | F | F | PASS=36 FAIL=1 | F2 | ok |

census: 28 mutations; all in-family: True

Every mutation fails in exactly its declared family and no other; the unmutated runner passes 37/37. Family sizes: A 5, B 4, C 6, D 8, E 10, F 3, G 1.

## Supervisor fold (2026-09-06, after the refuting checker)

Two checks and two mutations added at the fold: D9 (the width restriction lemma: the width-3 two-row formation joint on columns 0,1 equals the width-2 two-row joint; mutation `restriction_lemma_broken` restricts to the non-adjacent columns 0,2, whose pair carries `K^2`) and E11 (boundary independence of the deep-row limit: with exterior records `P(e_y)` on both end rows the `n = 13` center-row value lies within `10^-6` of the enclosure; mutation `boundary_dependence_forged`). Observation found while designing the D9 mutation: restricting the width-3 joint to the ADJACENT columns 1,2 also equals the width-2 joint (the restriction property holds on any adjacent column pair; the non-adjacent pair 0,2 does not) — recorded, not claimed. The first fence sentence was rewritten to the staircase-past order class (the checker's counterexample: row order 0,2,1 at width 3 gives row 1 three recorded neighbors and a marginal off `p_0` on all 216 states). Two check messages shortened to keep the unmutated stdout under 6,000 characters (5,994).

Final runner: `TOTAL: PASS=39 FAIL=0` (26.9 s); runner sha `abbd76127f42d3d5e9b895c451d0f2c31899e0afeb949c7a8f812bb1f65f98c2`, input fingerprint `9ac6e0846636b72e1ccb6ab28df2efc123feac25cb978b26010b27fd7418eaf3`. Census re-run at the final sha, 30 mutations, one helper invocation each, 4 in parallel, expected/observed read from raw stdout: 30 of 30 in family.

| mutation | expected | observed | total | failing checks | exit |
|---|---|---|---|---|---|
| `kernel_not_doubly_stochastic` | B | B | TOTAL: PASS=36 FAIL=3 | B1 B2 B3  | 1 |
| `z2_identity_wrong_power` | B | B | TOTAL: PASS=38 FAIL=1 | B2  | 1 |
| `path_law_not_formation` | B | B | TOTAL: PASS=38 FAIL=1 | B4  | 1 |
| `spec_conditional_ignores_exterior` | C | C | TOTAL: PASS=33 FAIL=6 | C1 C2 C3 C4 C5 C6  | 1 |
| `spec_conditional_two_hop` | C | C | TOTAL: PASS=33 FAIL=6 | C1 C2 C3 C4 C5 C6  | 1 |
| `spec_face_wrong_subwindow` | C | C | TOTAL: PASS=38 FAIL=1 | C1  | 1 |
| `row_kernel_formula_wrong_denominator` | D | D | TOTAL: PASS=38 FAIL=1 | D1  | 1 |
| `row_kernel_drops_left_neighbor` | D | D | TOTAL: PASS=35 FAIL=4 | D1 D2 D3 D4  | 1 |
| `invariance_forced_true` | D | D | TOTAL: PASS=38 FAIL=1 | D7  | 1 |
| `pair_law_wrong_column` | D | D | TOTAL: PASS=38 FAIL=1 | D3  | 1 |
| `direct_strip_law_mismatch` | D | D | TOTAL: PASS=38 FAIL=1 | D4  | 1 |
| `asymmetric_control_passes` | D | D | TOTAL: PASS=38 FAIL=1 | D7  | 1 |
| `constant_rule_not_uniform` | D | D | TOTAL: PASS=38 FAIL=1 | D6  | 1 |
| `three_neighbor_witness_forced` | D | D | TOTAL: PASS=38 FAIL=1 | D8  | 1 |
| `orbit_count_wrong` | E | E | TOTAL: PASS=38 FAIL=1 | E1  | 1 |
| `quotient_not_commuting` | E | E | TOTAL: PASS=38 FAIL=1 | E2  | 1 |
| `charpoly_coefficient_off` | E | E | TOTAL: PASS=38 FAIL=1 | E3  | 1 |
| `perron_interval_wrong_root` | E | E | TOTAL: PASS=35 FAIL=4 | E5 E9 E10 E11  | 1 |
| `eigvec_residual_nonzero` | E | E | TOTAL: PASS=36 FAIL=3 | E6 E9 E11  | 1 |
| `limit_law_uses_rho_not_squared` | E | E | TOTAL: PASS=37 FAIL=2 | E9 E11  | 1 |
| `s_inf_enclosure_contains_formation_value` | E | E | TOTAL: PASS=36 FAIL=3 | E7 E8 E9  | 1 |
| `finite_n_sequence_shuffled` | E | E | TOTAL: PASS=38 FAIL=1 | E9  | 1 |
| `second_eigenvalue_bound_too_small` | E | E | TOTAL: PASS=38 FAIL=1 | E10  | 1 |
| `boundary_dependence_forged` | E | E | TOTAL: PASS=38 FAIL=1 | E11  | 1 |
| `restriction_lemma_broken` | D | D | TOTAL: PASS=38 FAIL=1 | D9  | 1 |
| `claim_order_selected` | F | F | TOTAL: PASS=38 FAIL=1 | F2  | 1 |
| `claim_plane_static` | F | F | TOTAL: PASS=38 FAIL=1 | F2  | 1 |
| `claim_z3_uniqueness` | F | F | TOTAL: PASS=38 FAIL=1 | F2  | 1 |
| `claim_washout` | F | F | TOTAL: PASS=38 FAIL=1 | F2  | 1 |
| `claim_gate_fired` | F | F | TOTAL: PASS=38 FAIL=1 | F2  | 1 |
