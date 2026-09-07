# RESULTS — block 03 (primary seat, Fable), 2026-09-06

## Headline

The one-neighbor interdependence coefficient `c_1(p, q, r)` of the covariant product rule on the six-neighbor shell is computed exactly, is direction-independent, `p ↔ q` symmetric and zero exactly at the constant rule, and the crossing `6c_1 = 1` along each of the three lines `(t,1,1)`, `(t,t,1)`, `(1,1,t)` is the unique positive root of an explicit irreducible degree-7 polynomial, isolated to width `10^-20` with the maximizing shell pattern re-executed at both isolating endpoints. The finite-window comparison bound is re-proved by a random-scan coupling (every step written in the note) and executed on the plaquette (`223,616` configuration pairs, four triples) and on the `3×3` planar window (`D_Λ` exact over the rationals, `200` damped iterates, the exact center-site total variation against `(D_Λ b)_center` at the three region triples). Hence the specification on `Z^3` has exactly one infinite-volume static law at `(2,1,2)`, `(3,2,2)`, `(5,4,4)`, `(11,10,10)` and at the ten executed rational line points; at `(3,1,2)` and `(5,2,4)` the criterion is silent and nothing is stated about one law or several.

## Run record

- Runner `scripts/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.py` (807 lines): `TOTAL: PASS=36 FAIL=0`, 26 declared mutations, unmutated stdout 5,962 characters, baseline 19.10 s (the cache run).
- Cache: `logs/runner-cache/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.txt`, runner sha256 `b20b895254b915b05ce1ebd4f262b62d639ca1651ad731cd8828833d0f25470c`, input fingerprint `ce06982009fcead609fe22ce95fb887aed358076c94a1cb8f42f52f5690ccfdd`, exit 0, elapsed 19.10 s, written by `runner_cache.execute_and_write_cache` after the last runner and note edits (re-pinned once, after the guard below).
- Note `docs/ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md`: 650 lines (cap 650); `vocab_lint --report-only` 0 violations.
- Timing decision (contract: time the grid and the plaquette family first and cut to what fits 400 s): in scratch, one coefficient evaluation costs 0.06 s with the integer hot loop (the contract expected 0.7 s with Fractions), the `1..8` grid 4.4 s, the plaquette family 1.6 s per triple, the `3×3` row transfer 0.01 s; so the grid was EXTENDED to `1..12` (144 points, 9 s) and nothing was cut.
- Control reproduction before any theorem sentence (own code, `scratchpad/primary03/control03.py`): `c_1(3,1,2) = 270/989`, `c_1(2,1,2) = 2/13`, the `(t,1,1)` crossing between `3/2` and `13/8` with pattern three `+x` two `−x` and pair `+x ↔ −x`, the `3×3` TV at `(2,1,2)` `= 691410442136477999520/76730168638463067377251` against `1/56`; also `8650000/40615109`, `2079/15566`, `4000000/61385721`, `98241110000/4544062780611` and the four-neighbor coefficients `1/8`, `1404/11431`, `10000/175641`. All equal to the supervisor's controls; nothing differed.

## Defects fixed while executing

- The decimal label strings `"0.0090109"` etc. tripped the textual float scan (F4); stored as digit strings and compared to `"0." + label`.
- Unmutated stdout was 7,879 characters on the first run; check messages, info lines and the N5 lines were compressed in four passes to 5,962.
- The note was 684 lines after the first draft; six compression passes brought it to 650 without removing any proof step (deletions: repeated sentences in N-gate intros, the Falsifiers list, the `Further` paragraph, the Review record, two obligation rows merged, one N8 row).
- The author-name section rule (F3) caught the full `WILSON_STAGGERED_..._DOBRUSHIN_...` filename inside the N4 table; the table now uses the short name and the full name stays under Prior art.
- First census: `sign_pattern_not_fixed` crashed (IndexError: with one sign flipped the numerator has no positive root and the isolating-interval list is empty) instead of failing in family C; guarded (`have_root`), the mutation now fails C5–C9, the runner was recommitted, the cache re-pinned at the final sha and the census re-run in full.

## Could-not list

- None of the contracted computations was cut; the grid was extended to `1..12`.
- The region is stated at the executed rational points only, not on the open interval below the threshold: monotonicity of `c_1` along a line is not proved (contract sentence "for every rational t strictly between 1 and the isolating interval's lower endpoint" is not claimed in the note).
- Whether the displayed pattern attains the supremum at every interior point of the `10^-20` isolating interval is not executed; the executed content is the sign change and the endpoint suprema (stated in G5 and Boundaries).
- The `3×3` window bound at `(3,1,2)` is not asserted (row sum `3672/3431 ≥ 1`); the TV `0.0346753` is recorded only.
- No sharper criterion attempted (five routes named with obligations in N1).
- The monotone decrease of the damped iterates needs `C_Λ 1 + b ≤ 1` in addition to the contraction; stated in H2 (the contract's H2 sentence omitted it).

## Modelling choices (declared, not physics)

- Menu order `P(+e_x), P(−e_x), P(+e_y), P(−e_y), P(+e_z), P(−e_z)`; patterns are printed as the other five slot values (digits in this order) and the flipped pair; the maximizer is the lexicographically first over the `7776 × 15` choices, ties not excluded.
- Rational triples are scaled to integers by the common denominator (the conditional is homogeneous of degree zero in `φ`).
- Lines: scan `t = 1 + k/8` on `(t,1,1)` and `(t,t,1)`, `t = k/8` on `(1,1,t)`, `k = 1..8`; the pattern at the upper bracket point; the sign pattern from the exact conditionals at both bracket points; isolation width `10^-20` (`sympy` `Poly.intervals`); the endpoint checks use the exact rational endpoints scaled to integers.
- Plaquette: sites `0-1-2-3-0`; base exterior all `P(e_x)`; flipped exterior: slot (site 0, left) `= P(−e_x)`; family = all ordered pairs differing at ≤ 2 sites (`221,616`) + `2,000` LCG pairs (seed `20260906`, multiplier `1103515245`, increment `12345`, modulus `2^31`, eight draws per pair, `(state >> 16) mod 6`); coefficient `c_1^{(4)}` for every slot; `b_x = c_1^{(4)}[x = 0]`; executed at `(2,1,2)`, `(3,2,2)`, `(5,4,4)`, `(3,1,2)`.
- `3×3` window: sites `(i,j)`, twelve exterior slots `L/R/B/T`; base all `P(e_x)`; flipped `(1,0,'L') = P(−e_x)`; `C_Λ = c_1^{(4)} ·` adjacency; `b = c_1^{(4)}` at `(1,0)`; `D_Λ` by `sympy` `Matrix.inv` over `QQ`, verified `D(I − C) = I`; damped map `u ↦ (8/9)u + (1/9)(Cu + b)`, `200` iterations, tolerance `10^-4`.
- Corollary arithmetic: path counts by enumerating all `6^n` direction sequences, `n ≤ 4`; the table `α^L/(1−α)` for `L = 1..12`; the least `L` with the bound below `10^-3` by an exact loop.
- Region points: `(t,1,1)`: `9/8, 5/4, 11/8, 3/2`; `(t,t,1)`: `9/8, 5/4, 11/8`; `(1,1,t)`: `3/4, 7/8, 1`.

## Exact coefficients, patterns, polynomials and thresholds (runner `--exact` and unmutated stdout, verbatim lines)

```text
info c_1(3, 1, 2)=270/989 6c_1=1.638018 max eta=00023 pair=01
info c_1(5, 2, 4)=8650000/40615109 6c_1=1.277849 max eta=00000 pair=01
info c_1(2, 1, 2)=2/13 6c_1=0.923076 max eta=00123 pair=45
info c_1(3, 2, 2)=2079/15566 6c_1=0.801361 max eta=00011 pair=01
info c_1(5, 4, 4)=4000000/61385721 6c_1=0.390970 max eta=00000 pair=01
info c_1(11, 10, 10)=98241110000/4544062780611 6c_1=0.129717 max eta=00000 pair=01
info line (t,1,1): crossing 3/2..13/8; eta=00011 pair=01; t* in [1.60970232778584910813, 1.60970232778584910814]
info line (t,t,1): crossing 11/8..3/2; eta=00022 pair=02; t* in [1.47753945492134830313, 1.47753945492134830314]
info line (1,1,t): crossing 5/8..3/4; eta=00022 pair=02; t* in [0.67680087774930621901, 0.67680087774930621903]
info 3x3 (2, 1, 2): c_1^(4)=1/8 TV(center)=0.0090109 <= (D b)_c=1/56=0.0178571
info 3x3 (3, 2, 2): c_1^(4)=1404/11431 TV(center)=0.0073929 <= (D b)_c=1971216/114898033=0.0171562
info 3x3 (5, 4, 4): c_1^(4)=10000/175641 TV(center)=0.0016901 <= (D b)_c=100000000/30049760881=0.0033278
info 3x3 (3, 1, 2): 4c_1^(4)=3672/3431 >= 1; bound not asserted; TV(center)=0.0346753 recorded only
info tbl(2, 1, 2): a=0.923076 L1=12.000000 L12=4.975057 <10^-3 from L=119
info tbl(3, 2, 2): a=0.801361 L1=4.034282 L12=0.353087 <10^-3 from L=39
info tbl(5, 4, 4): a=0.390970 L1=0.641956 L12=0.000020 <10^-3 from L=8
info tbl(11, 10, 10): a=0.129717 L1=0.149052 L12=0.000000 <10^-3 from L=4
info pts (t,1,1): 9/8:0.17005 5/4:0.39097 11/8:0.59997 3/2:0.80136
info pts (t,t,1): 9/8:0.26820 5/4:0.53886 11/8:0.80125
info pts (1,1,t): 3/4:0.71592 7/8:0.30715 1:0.00000
```

Grid map `r = 4`, `p` rows and `q` columns `1..12` (`U` = `6c_1 < 1`):

```text
exact grid p= 1: . . . . . . . . . . . .
exact grid p= 2: . . . U . . . . . . . .
exact grid p= 3: . . U U U . . . . . . .
exact grid p= 4: . U U U U U . . . . . .
exact grid p= 5: . . U U U U . . . . . .
exact grid p= 6: . . . U U . . . . . . .
exact grid p= 7: . . . . . . . . . . . .
exact grid p= 8: . . . . . . . . . . . .
exact grid p= 9: . . . . . . . . . . . .
exact grid p=10: . . . . . . . . . . . .
exact grid p=11: . . . . . . . . . . . .
exact grid p=12: . . . . . . . . . . . .
```

Lines (numerator of `6TV − 1` at the displayed pattern, sign pattern, exact isolating interval, Sturm counts):

```text
exact line (t,1,1): numerator of 6TV-1 = 2*(t**7 - 2*t**5 + 5*t**4 - 8*t**3 - t**2 - 4); signs (1, -1, -1, -1, -1, -1); interval [49164167869/30542397200, 47982574521/29808352571]; real roots 3, positive 1
exact line (t,t,1): numerator of 6TV-1 = 4*t**7 - 8*t**5 + 5*t**4 - 8*t**3 - t**2 - 1; signs (1, 1, -1, -1, -1, -1); interval [39169651467/26510054494, 8570324974/5800403465]; real roots 3, positive 1
exact line (1,1,t): numerator of 6TV-1 = -t**7 - t**5 - 8*t**4 + 5*t**3 - 8*t**2 + 4; signs (1, 1, -1, -1, -1, -1); interval [5800403465/8570324974, 9108844099/13458676545]; real roots 3, positive 1
```

Thresholds as decimal labels (the exact endpoints are above): `(t,1,1)`: `t* ∈ [1.60970232778584910813, 1.60970232778584910814]`; `(t,t,1)`: `t* ∈ [1.47753945492134830313, 1.47753945492134830314]`; `(1,1,t)`: `t* ∈ [0.67680087774930621901, 0.67680087774930621903]`. Each polynomial is irreducible over `Q` with three real roots and exactly one positive root.

## Window bounds (`3×3`, exact; `u*` indexed by site `3i + j`, center index 4; `D_Λ` center row)

```text
exact 3x3 (2, 1, 2): TV = 691410442136477999520/76730168638463067377251; u* = ['59/3472', '1/224', '3/3472', '913/6944', '1/56', '17/6944', '59/3472', '1/224', '3/3472']; D center row = ['1/28', '1/7', '1/28', '1/7', '15/14', '1/7', '1/28', '1/7', '1/28']
exact 3x3 (3, 2, 2): TV = 33371823530478793013606992/4514027923287489693489918949; u* = ['238145918574096/14560491033377857', '5535174528/1313399415223', '11657077555968/14560491033377857', '21462366556785182652/166440973002542283367', '1971216/114898033', '383456480343768000/166440973002542283367', '238145918574096/14560491033377857', '5535174528/1313399415223', '11657077555968/14560491033377857']; D center row = ['3942432/114898033', '16049124/114898033', '3942432/114898033', '16049124/114898033', '122782897/114898033', '16049124/114898033', '3942432/114898033', '16049124/114898033', '3942432/114898033']
exact 3x3 (5, 4, 4): TV = 1731753640209702882755284603119966790400/1024620776654359492500695152066016873791443; u* = ['3034976088100000000/921017985533877896161', '2000000000000/5277970050899721', '30000000000000000/921017985533877896161', '9301529137981778961610000/161768519997155847559614201', '100000000/30049760881', '31249760881000000000000/161768519997155847559614201', '3034976088100000000/921017985533877896161', '2000000000000/5277970050899721', '30000000000000000/921017985533877896161']; D center row = ['200000000/30049760881', '1756410000/30049760881', '200000000/30049760881', '1756410000/30049760881', '30449760881/30049760881', '1756410000/30049760881', '200000000/30049760881', '1756410000/30049760881', '200000000/30049760881']
```

## The table `α^L/(1 − α)` and the region points (exact)

```text
exact table (2, 1, 2): alpha = 12/13; L=1 12; L=2 144/13; L=3 1728/169; L=4 20736/2197; L=5 248832/28561; L=6 2985984/371293; L=7 35831808/4826809; L=8 429981696/62748517; L=9 5159780352/815730721; L=10 61917364224/10604499373; L=11 743008370688/137858491849; L=12 8916100448256/1792160394037
exact table (3, 2, 2): alpha = 6237/7783; L=1 6237/1546; L=2 38900169/12032518; L=3 242620354053/93649087594; L=4 1513223148228561/728870848744102; L=5 9437972775501534957/5672801815775345866; L=6 58864636200803073526809/44151416532179516875078; L=7 367138735984408769586707733/343630474869953179838732074; L=8 2289844296334757495912296130721/2674475985912845598684851731942; L=9 14281758876239882502004990967306877/20815446598359677294564201029704586; L=10 89075330111108147165005128663092991849/162006620875033368383593176614190792838; L=11 555562833902981513868136987471710990162213/1260897530270384706129505693588246940658154; L=12 3465045395052895701995570390861061445641722481/9813565478094404167805942813197325939142412582
exact table (5, 4, 4): alpha = 8000000/20461907; L=1 8000000/12461907; L=2 64000000000000/254994382076649; L=3 512000000000000000000/5217671331574858709643; L=4 4096000000000000000000000000/106763505543250922454855069201; L=5 32768000000000000000000000000000000/2184584921419984852935456124469426307; L=6 262144000000000000000000000000000000000000/44700773495698038002173980221473825437187449; L=7 2097152000000000000000000000000000000000000000000/914663070097038153682949781111636819029963923005243; L=8 16777216000000000000000000000000000000000000000000000000/18715750676660075676112225906776669208766952005888442778401; L=9 134217728000000000000000000000000000000000000000000000000000000/382959949781005539097570488067454875119552956617952768506462870707; L=10 1073741824000000000000000000000000000000000000000000000000000000000000/7836090877143605707499351252780871381392906479891584079571772159359658249; L=11 8589934592000000000000000000000000000000000000000000000000000000000000000000/160341362771660885631520927894735681585023182851238963518878201750006506642820843; L=12 68719476736000000000000000000000000000000000000000000000000000000000000000000000000/3280890053286987277329817495135787306174356960346046506299678508535870388320282307127601
exact table (11, 10, 10): alpha = 196482220000/1514687593537; L=1 196482220000/1318205373537; L=2 38605262776128400000000/1996669325030300712030369; L=3 7585247733937071037048000000000000/3024330255019292265112737245872125153; L=4 1490366314013925057656893286560000000000000000/4580915516036313316552489798957038334825657936161; L=5 292830481990673106242054391246404963200000000000000000000/6938655899181347950154238082727977327825733479766431062191457; L=6 57535983185197471208734704152842214188554304000000000000000000000000/10509896006312304814974990709509000702867855992969348546425784788889813409; L=7 11304797706110270281478278062993657553482648240474880000000000000000000000000000/15919209090125311941866486718625120497468554368501406140788260884450171046331164337633; L=8 2221191749947453469704876955594293682028039457767598276633600000000000000000000000000000000/24112628507734244094997197207983055403547296916755643580391245099327176805555384643336603336677921; L=9 436424686075360541074316969062008241976843294909773953461143854592000000000000000000000000000000000000/36523099248231645580579057059719669474671599580201825588246497640443025973430808538187924750300204767530196577; L=10 85749691182889926410682983064974697041907359175987086074222228289593354240000000000000000000000000000000000000000/55321085308817005047176773160767397052415362141494362629035276942571195698250298284484060506704258777648647968196684722849; L=11 16848289687928638756807624228828632718621390965235313363194268187686105138321612800000000000000000000000000000000000000000000/83794161578267113863211769694723697861530411935470471023625068276023507361475430710017601034534174582865939754249500892353643608626913; L=12 3310389361087326144515602121406037756119366236337377191996076104791942600730837556924416000000000000000000000000000000000000000000000000/126921976953435960576054606832716103040007372702478070286698543741157367640995624523907147389912330530707841079046197676122474521524839504823061281
exact region points (t,1,1): t=9/8 c_1=11851370496/418142914585, t=5/4 c_1=4000000/61385721, t=11/8 c_1=145238720/1452454739, t=3/2 c_1=2079/15566
exact region points (t,t,1): t=9/8 c_1=419904/9393713, t=5/4 c_1=36125/402234, t=11/8 c_1=1247147/9338966
exact region points (1,1,t): t=3/4 c_1=8896/74555, t=7/8 c_1=200704/3920631, t=1 c_1=0
```

## Certified stdout (the pinned cache, verbatim)

```text
===== runner cache v1 =====
runner: scripts/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.py
runner_sha256: b20b895254b915b05ce1ebd4f262b62d639ca1651ad731cd8828833d0f25470c
input_fingerprint_sha256: ce06982009fcead609fe22ce95fb887aed358076c94a1cb8f42f52f5690ccfdd
timeout_sec: 900
exit_code: 0
elapsed_sec: 19.10
status: ok
----- stdout -----
AUDIT_INPUT_PATHS:
  docs/ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md
  docs/MINIMAL_AXIOMS_2026-06-29.md
  docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md
  docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md
AUDIT_TIMEOUT_SEC: 900
scope: six-projector menu, covariant product rule; c_1 exactly; the coupling bound on two windows; the corollary's arithmetic; uniqueness only where 6c_1 < 1; silent at (3,1,2), (5,2,4)
mutation: none
PASS: A1 the four declared audit inputs exist
PASS: A2 axiom memo: both Admissibility sentences verbatim
PASS: A3 axiom memo: the four Record sentences verbatim
PASS: A4 block 01's note: claim id and the finite-window uniqueness fragment
PASS: A5 block 02's note: claim id and the existence fragment
PASS: A6 this note carries its claim id
PASS: B1 G1: the same coefficient 270/989 with the flipped neighbor in each of the six directions, (3,1,2)
PASS: B2 G2: c_1(3,1,2) = c_1(1,3,2) and c_1(5,2,4) = c_1(2,5,4) exactly
PASS: B3 G2: r_(3,1,2)(-s | eta) = r_(1,3,2)(s | eta) on all 46656 shells and six values
PASS: B4 G3: c_1 = 0 at (2,2,2); c_1 > 0 at the six non-constant triples
PASS: C1 G4: exact c_1 at the seven triples equals the literals
info c_1(3, 1, 2)=270/989 6c_1=1.638018 max eta=00023 pair=01
info c_1(5, 2, 4)=8650000/40615109 6c_1=1.277849 max eta=00000 pair=01
info c_1(2, 1, 2)=2/13 6c_1=0.923076 max eta=00123 pair=45
info c_1(3, 2, 2)=2079/15566 6c_1=0.801361 max eta=00011 pair=01
info c_1(5, 4, 4)=4000000/61385721 6c_1=0.390970 max eta=00000 pair=01
info c_1(11, 10, 10)=98241110000/4544062780611 6c_1=0.129717 max eta=00000 pair=01
PASS: C2 G4: 6c_1 < 1 at the four region triples; >= 1 at (3,1,2), (5,2,4)
PASS: C3 G2/G4: c_1(p,q,4) = c_1(q,p,4) on all 144 grid points, p, q in 1..12
PASS: C4 G4: the r = 4 grid's 6c_1 < 1 cells are the diamond (15 cells)
info line (t,1,1): crossing 3/2..13/8; eta=00011 pair=01; t* in [1.60970232778584910813, 1.60970232778584910814]
info line (t,t,1): crossing 11/8..3/2; eta=00022 pair=02; t* in [1.47753945492134830313, 1.47753945492134830314]
info line (1,1,t): crossing 5/8..3/4; eta=00022 pair=02; t* in [0.67680087774930621901, 0.67680087774930621903]
PASS: C5 G5: crossings at the declared brackets; sign pattern of the six differences fixed at both
PASS: C6 G5: numerator of 6TV(t) - 1 at the pattern = the contract's degree-7 polynomial up to a constant
PASS: C7 G5: Sturm: one positive root each, isolated to width < 10^-20, sign change at the rational endpoints
PASS: C8 G5: at both endpoints the sup over all 7776 x 15 choices is the displayed pattern's value
PASS: C9 G5: 6c_1 - 1 negative below, positive above t* on (t,1,1), (t,t,1); reversed on (1,1,t)
PASS: D1 H1: plaquette one-step inequality TV <= c_1^(4) sum[differ] + b_x, 223616 pairs x 4 sites
PASS: D2 H1: maximal coupling: sum_s min(a_s, b_s) = 1 - TV on all 5184 distinct instances, four triples
PASS: D3 H2: c_1^(4) = 1/8, 1404/11431, 10000/175641, 918/3431; 3x3 row sums < 1 at region triples, >= 1 at (3,1,2)
PASS: D4 H2: D = (I - C)^{-1} exact: D(I - C) = I, D >= 0, three region triples
PASS: D5 H2: damped iterates from u^0 = 1 nonincreasing, >= u* = D b, within 10^-4 at step 200
PASS: D6 H2: fixed-point identity u* = (8/9) u* + (1/9)(C u* + b) exact
info 3x3 (2, 1, 2): c_1^(4)=1/8 TV(center)=0.0090109 <= (D b)_c=1/56=0.0178571
info 3x3 (3, 2, 2): c_1^(4)=1404/11431 TV(center)=0.0073929 <= (D b)_c=1971216/114898033=0.0171562
info 3x3 (5, 4, 4): c_1^(4)=10000/175641 TV(center)=0.0016901 <= (D b)_c=100000000/30049760881=0.0033278
PASS: D7 H3: center-site TV <= (D b)_center at the three region triples; values equal the contract's literals
info 3x3 (3, 1, 2): 4c_1^(4)=3672/3431 >= 1; bound not asserted; TV(center)=0.0346753 recorded only
PASS: D8 H3: (3,1,2): row sum > 1; TV printed, window bound not asserted
PASS: E1 I: sum_y N_n(0,y) = 6^n on Z^3, n = 1..4, by path enumeration
info tbl(2, 1, 2): a=0.923076 L1=12.000000 L12=4.975057 <10^-3 from L=119
info tbl(3, 2, 2): a=0.801361 L1=4.034282 L12=0.353087 <10^-3 from L=39
info tbl(5, 4, 4): a=0.390970 L1=0.641956 L12=0.000020 <10^-3 from L=8
info tbl(11, 10, 10): a=0.129717 L1=0.149052 L12=0.000000 <10^-3 from L=4
PASS: E2 I: table alpha^L/(1-alpha), L = 1..12, exact at the four region triples
PASS: E3 I: least L with alpha^L/(1-alpha) < 10^-3 (>= at L-1): L=119, L=39, L=8, L=4
info pts (t,1,1): 9/8:0.17005 5/4:0.39097 11/8:0.59997 3/2:0.80136
info pts (t,t,1): 9/8:0.26820 5/4:0.53886 11/8:0.80125
info pts (1,1,t): 3/4:0.71592 7/8:0.30715 1:0.00000
PASS: E4 region: 6c_1 < 1 at the four region triples and the declared line points; >= 1 at (3,1,2), (5,2,4)
PASS: F1 the note carries the four fence sentences verbatim
PASS: F2 the note contains no forbidden phrase (hits: [])
PASS: F3 the criterion's author is named only in the Prior art and Imports sections (violations: [])
PASS: F4 runner source: no floating-point literal or conversion call (0 hits)
per_element: executed — all 7776 x 15 pattern-and-pair choices at every triple, grid point, scan point and endpoint; every plaquette pair
per_site: executed — the flipped neighbor in each of six directions; the plaquette inequality at each site; the 3x3 window's row sums and center marginals
per_mode: executed — D = (I - C)^{-1} exactly with the damped fixed-point iterates; Sturm isolation of each threshold as the unique positive root
per_block: executed — the 3x3 window by integer row transfer under two exterior assignments; path counts n <= 4; the table alpha^L/(1-alpha)
lattice_wide: proved, not executed — uniqueness on Z^3 where 6c_1 < 1 is the corollary of the window bound and the path-count bound; the silent triples are named, not decided
PASS: G1 the five N5 resolution lines are printed (each >= 40 chars)
TOTAL: PASS=36 FAIL=0

----- stderr -----
```

## Mutation census (26 mutations, one helper invocation each, 4 in parallel; expected/observed read from raw stdout at the final runner sha)

census: 26 mutations; runner sha256 b20b895254b915b05ce1ebd4f262b62d639ca1651ad731cd8828833d0f25470c

| mutation | expected | observed | total | failing checks | exit |
|---|---|---|---|---|---|
| `coefficient_direction_dependent` | B | B | TOTAL: PASS=35 FAIL=1 | B1 | 1 |
| `relabeling_identity_broken` | B | B | TOTAL: PASS=35 FAIL=1 | B3 | 1 |
| `constant_rule_nonzero` | B | B | TOTAL: PASS=35 FAIL=1 | B4 | 1 |
| `c1_literal_off` | C | C | TOTAL: PASS=35 FAIL=1 | C1 | 1 |
| `region_triple_misclassified` | C | C | TOTAL: PASS=35 FAIL=1 | C2 | 1 |
| `grid_symmetry_broken` | C | C | TOTAL: PASS=35 FAIL=1 | C3 | 1 |
| `grid_region_cells_wrong` | C | C | TOTAL: PASS=35 FAIL=1 | C4 | 1 |
| `sign_pattern_not_fixed` | C | C | TOTAL: PASS=31 FAIL=5 | C5 C6 C7 C8 C9 | 1 |
| `line_polynomial_wrong_coefficient` | C | C | TOTAL: PASS=35 FAIL=1 | C6 | 1 |
| `threshold_wrong_root` | C | C | TOTAL: PASS=34 FAIL=2 | C7 C9 | 1 |
| `endpoint_sup_pattern_forged` | C | C | TOTAL: PASS=35 FAIL=1 | C8 | 1 |
| `one_step_inequality_drops_b` | D | D | TOTAL: PASS=35 FAIL=1 | D1 | 1 |
| `one_step_inequality_wrong_coefficient` | D | D | TOTAL: PASS=35 FAIL=1 | D1 | 1 |
| `maximal_coupling_identity_broken` | D | D | TOTAL: PASS=35 FAIL=1 | D2 | 1 |
| `row_sum_ignored` | D | D | TOTAL: PASS=35 FAIL=1 | D3 | 1 |
| `D_matrix_wrong_inverse` | D | D | TOTAL: PASS=32 FAIL=4 | D4 D5 D6 D7 | 1 |
| `fixed_point_not_fixed` | D | D | TOTAL: PASS=35 FAIL=1 | D6 | 1 |
| `center_tv_exceeds_bound_forged` | D | D | TOTAL: PASS=35 FAIL=1 | D7 | 1 |
| `path_count_wrong` | E | E | TOTAL: PASS=35 FAIL=1 | E1 | 1 |
| `alpha_table_wrong_exponent` | E | E | TOTAL: PASS=35 FAIL=1 | E2 | 1 |
| `line_points_misclassified` | E | E | TOTAL: PASS=35 FAIL=1 | E4 | 1 |
| `claim_nonunique_at_silent` | F | F | TOTAL: PASS=35 FAIL=1 | F2 | 1 |
| `claim_unique_at_silent` | F | F | TOTAL: PASS=35 FAIL=1 | F2 | 1 |
| `claim_phase_transition` | F | F | TOTAL: PASS=35 FAIL=1 | F2 | 1 |
| `claim_physical_rule` | F | F | TOTAL: PASS=35 FAIL=1 | F2 | 1 |
| `claim_author_in_theorem` | F | F | TOTAL: PASS=35 FAIL=1 | F3 | 1 |

all in-family and exit 1: True

Every mutation fails in exactly its declared family and no other; the unmutated runner passes 36/36. Family sizes: A 6, B 4, C 9, D 8, E 4, F 4, G 1. Per-mutation raw stdout kept in the seat's scratch directory (`primary03/census2/<mutation>.txt`).

## Supervisor fold after the contract refuter lens (2026-09-06) — supersedes the run record above

- Lens (`scratchpad/panel3/L4_block03_refuter.md`, Opus 5, twelve exact scripts): every control number reproduced; seven contract defects, three false as written (the "second real root"; "the crossing" — each line crosses `6c_1 = 1` twice; `b` declared with `c_1` where the executed windows use `c_1^{(4)}`, and `c_1^{(4)}(2,5,3) > c_1(2,5,3)`), plus the iterate-decrease hypothesis (the primary had already stated it), endpoint-only dominance, the continuum line statement, "paths" for "walks", the full-DLR definition (already in the note), the non-unique maximizer, the π–λ clause (already in the note), the `(7,3,5)` silent triple. Recorded as the addendum of `GOAL_block03.md` (A1–A11) with the supervisor's controls `specs/supervisor_control_block03_after_lens.py` (the lens's counterexamples confirmed; the second crossings; a crude-Lipschitz sweep) and `specs/supervisor_control_block03_certificates.py` (the `6/t` lemma prototype: isolating-interval sweeps 0.2 s each; region certificates 27, 20, 18 s).
- Runner fold (960 lines): `coefficient_multiset` (252 multisets × 15 pairs; agrees with the 7776-shell supremum at the eight triples); `LINES2` (the second crossings: `t^2 + 10t − 5`, `t^5 + 7t − 5`, `5t^5 − 7t^4 − 1`); `region_certificate` (bisection on `c_1` itself with the Lipschitz constant `6/u`, dyadic midpoints); `competitor_sweep` (each choice verified below on the isolating interval or identical to the displayed maximizer); `reciprocal`/`proportional`; checks C10–C14; mutations `second_crossing_wrong_root`, `competitor_identity_forged`, `region_certificate_forged`, `reciprocity_broken`, `c4_c1_inversion_denied`; E1 wording "walk enumeration"; stdout compacted (the `tbl` and `pts` info lines moved under `--exact`; the six `c_1` info lines merged into two; 14-digit interval labels in stdout, 20 digits under `--exact`).
- Note fold (739 lines; lint 0): claim_scope, Result up front, machine status, declared triples (`(7,3,5)`), the coefficient definition (`(2,5,3)` inversion), G4 (ties recorded: `12, 6, 60, 30, 30, 30, 24`), G5 tail, G5′ (second crossings), G6 (the Lipschitz lemma with proof; the two certificates; scale invariance and reciprocity), the obligation table, Theorem I ("walks"), The region stated (open intervals between the two thresholds, the executed points inside), Falsifiers, Boundaries, Imports, Review record, Verification. The lane's forbidden word "certified" was avoided ("verified"); "uncertified" likewise.
- Final certificate: `TOTAL: PASS=41 FAIL=0`; runner sha256 `953de23b62c6388103db089cb3b49da12adf2607119166319bd02ec1655e06d5`; input fingerprint `19543425c15e3b6662b5d805877a51f304578089fd95dd6884a0a92a7d131d83`; exit 0; elapsed 86.38 s; unmutated stdout 5,959 characters; 31 mutations.
- The second thresholds (runner `--exact`): `(t,1,1)`: numerator `−t^2 − 10t + 5`, signs `(1,1,1,1,−1,1)`, interval `[10527439114/22059670865, 2351330961/4927084976]` (`0.47722557505166113456…458`), real roots 2, positive 1; `(t,t,1)`: `−t^5 − 7t + 5`, signs `(1,1,−1,−1,1,1)`, interval `[6864156352/9924024879, 10832308623/15661079783]` (`0.69167061103656469380…382`), real roots 1; `(1,1,t)`: `5t^5 − 7t^4 − 1`, same signs, interval `[15661079783/10832308623, 25585104662/17696464975]` (`1.44577488770465582773…774`), real roots 1. Copies at the six thresholds: `30, 288, 288, 60, 72, 72`; region-certificate subintervals `2395, 1782, 1715`.
- Fold census: below (re-run at the final sha, 31 mutations, 4 in parallel, one helper invocation each).

## Fold census (31 mutations, one helper invocation each, 4 in parallel; expected/observed read from raw stdout at the final runner sha 953de23b…)

| mutation | expected | observed | FAIL count | failing checks | exit | in-family |
|---|---|---|---|---|---|---|
| `coefficient_direction_dependent` | B | B | 1 | B1 G1: | 1 | yes |
| `relabeling_identity_broken` | B | B | 1 | B3 G2: | 1 | yes |
| `constant_rule_nonzero` | B | B | 1 | B4 G3: | 1 | yes |
| `c1_literal_off` | C | C | 1 | C1 G4: | 1 | yes |
| `region_triple_misclassified` | C | C | 1 | C2 G4: | 1 | yes |
| `grid_symmetry_broken` | C | C | 1 | C3 G2/ | 1 | yes |
| `grid_region_cells_wrong` | C | C | 1 | C4 G4: | 1 | yes |
| `sign_pattern_not_fixed` | C | C | 7 | C5 G5: C6 G5: C7 G5: C8 G5: C9 G5: C11 G5 C12 G6 | 1 | yes |
| `line_polynomial_wrong_coefficient` | C | C | 1 | C6 G5: | 1 | yes |
| `threshold_wrong_root` | C | C | 4 | C7 G5: C9 G5: C11 G5 C12 G6 | 1 | yes |
| `endpoint_sup_pattern_forged` | C | C | 1 | C8 G5: | 1 | yes |
| `second_crossing_wrong_root` | C | C | 3 | C10 G5 C11 G5 C12 G6 | 1 | yes |
| `competitor_identity_forged` | C | C | 1 | C11 G5 | 1 | yes |
| `region_certificate_forged` | C | C | 1 | C12 G6 | 1 | yes |
| `reciprocity_broken` | C | C | 1 | C13 G2 | 1 | yes |
| `c4_c1_inversion_denied` | C | C | 1 | C14 c_ | 1 | yes |
| `one_step_inequality_drops_b` | D | D | 1 | D1 H1: | 1 | yes |
| `one_step_inequality_wrong_coefficient` | D | D | 1 | D1 H1: | 1 | yes |
| `maximal_coupling_identity_broken` | D | D | 1 | D2 H1: | 1 | yes |
| `row_sum_ignored` | D | D | 1 | D3 H2: | 1 | yes |
| `D_matrix_wrong_inverse` | D | D | 4 | D4 H2: D5 H2: D6 H2: D7 H3: | 1 | yes |
| `fixed_point_not_fixed` | D | D | 1 | D6 H2: | 1 | yes |
| `center_tv_exceeds_bound_forged` | D | D | 1 | D7 H3: | 1 | yes |
| `path_count_wrong` | E | E | 1 | E1 I: | 1 | yes |
| `alpha_table_wrong_exponent` | E | E | 1 | E2 I: | 1 | yes |
| `line_points_misclassified` | E | E | 1 | E4 reg | 1 | yes |
| `claim_nonunique_at_silent` | F | F | 1 | F2 the | 1 | yes |
| `claim_unique_at_silent` | F | F | 1 | F2 the | 1 | yes |
| `claim_phase_transition` | F | F | 1 | F2 the | 1 | yes |
| `claim_physical_rule` | F | F | 1 | F2 the | 1 | yes |
| `claim_author_in_theorem` | F | F | 1 | F3 the | 1 | yes |
in-family: 31/31

## Refuting checker and the second fold (2026-09-06) — final certificate

- Checker (Opus 5, disjoint machinery; `CHECKER_block03_findings.md`, spec `scratchpad/checker03/checker_spec_block03.md`): **PASS-NO-BLOCKER, nothing refuted**. CK-01..CK-08 and CK-02a all CONFIRM on its own integer/Fraction brute force, own row transfer and Gauss–Jordan inverse, own walk counts and a re-implementation of the cache hash: the eight coefficients, the tie counts, the five maximizing patterns, direction independence by full ordered enumeration at each slot, the fifteen-cell diamond, all six thresholds with polynomials, root counts and endpoint sign changes, the copy counts, the four-neighbor coefficients, the 21-digit centre total variation and the three window bounds, `L = 119, 39, 8, 4`, every decimal label, the cache sha and the input fingerprint. Attacks without a hit: 1,344 rationals strictly between the thresholds (none with `6c_1 ≥ 1`), 1,110 outside (none with `6c_1 < 1`), 1,080 window site-checks over all twelve exterior slots × five flipped values × two triples plus a two-slot flip and a two-site observable (no bound violation; worst ratio 0.809). Theorems H and I: no missing lemma. Runner: `41/41`, twelve mutations run, all in family. Findings: F1 (low) the copy test of C11 verified only the signed rational function, which certifies `TV ≥ f`, not `TV = f`, on `[a, b]`; F2 (low) the region certificate's `[u, v]` omits the two slivers inside the isolating intervals, which need one sentence joining G6(i) and G6(ii); F3/F4 informational (the title's "exact region" readable as sharpness; H3's citation of Theorem A is a proved step). Checker's own gaps: the plaquette family and the LCG draws not re-executed; the copy and sliver checks finite-sample.
- Second fold: C11's copy test now also requires the sign pattern to be constant on `[a, b]` (no numerator of `a_s − b_s` has a root there, by Sturm; `sign_constant`, `difference_numerators`), so a copy's total variation equals the displayed function on the whole interval — the copy counts are unchanged (`30, 288, 288, 60, 72, 72`); G6 gains the sentence that (i) covers the region side of each isolating interval and (ii) the interval between, so the whole open interval between the thresholds carries `6c_1 < 1`; Boundaries states that "the exact region" is the exact locus of the criterion, not a sharp boundary of uniqueness; the Review record carries the checker's verdict and the independence class.
- Final certificate: `TOTAL: PASS=41 FAIL=0`; runner sha256 `a2da7fbeb2cda37efd444da11c4c2e0f18798a91296478844185f44b48e87843`; input fingerprint `be51d2ec3a054cd1a81d6ad9579422123a8f55c842168cd3a5926b2259941ce6`; exit 0; elapsed 87.65 s; unmutated stdout 5,963 characters; note 756 lines, vocab lint 0; 31 mutations, census re-run at this sha (table below).

## Final census (31 mutations, one helper invocation each, 4 in parallel; expected/observed read from raw stdout at the final runner sha a2da7fbe…)

| mutation | expected | observed | FAIL count | failing checks | exit | in-family |
|---|---|---|---|---|---|---|
| `coefficient_direction_dependent` | B | B | 1 | B1 G1: | 1 | yes |
| `relabeling_identity_broken` | B | B | 1 | B3 G2: | 1 | yes |
| `constant_rule_nonzero` | B | B | 1 | B4 G3: | 1 | yes |
| `c1_literal_off` | C | C | 1 | C1 G4: | 1 | yes |
| `region_triple_misclassified` | C | C | 1 | C2 G4: | 1 | yes |
| `grid_symmetry_broken` | C | C | 1 | C3 G2/ | 1 | yes |
| `grid_region_cells_wrong` | C | C | 1 | C4 G4: | 1 | yes |
| `sign_pattern_not_fixed` | C | C | 7 | C5 G5: C6 G5: C7 G5: C8 G5: C9 G5: C11 G5 C12 G6 | 1 | yes |
| `line_polynomial_wrong_coefficient` | C | C | 1 | C6 G5: | 1 | yes |
| `threshold_wrong_root` | C | C | 4 | C7 G5: C9 G5: C11 G5 C12 G6 | 1 | yes |
| `endpoint_sup_pattern_forged` | C | C | 1 | C8 G5: | 1 | yes |
| `second_crossing_wrong_root` | C | C | 3 | C10 G5 C11 G5 C12 G6 | 1 | yes |
| `competitor_identity_forged` | C | C | 1 | C11 G5 | 1 | yes |
| `region_certificate_forged` | C | C | 1 | C12 G6 | 1 | yes |
| `reciprocity_broken` | C | C | 1 | C13 G2 | 1 | yes |
| `c4_c1_inversion_denied` | C | C | 1 | C14 c_ | 1 | yes |
| `one_step_inequality_drops_b` | D | D | 1 | D1 H1: | 1 | yes |
| `one_step_inequality_wrong_coefficient` | D | D | 1 | D1 H1: | 1 | yes |
| `maximal_coupling_identity_broken` | D | D | 1 | D2 H1: | 1 | yes |
| `row_sum_ignored` | D | D | 1 | D3 H2: | 1 | yes |
| `D_matrix_wrong_inverse` | D | D | 4 | D4 H2: D5 H2: D6 H2: D7 H3: | 1 | yes |
| `fixed_point_not_fixed` | D | D | 1 | D6 H2: | 1 | yes |
| `center_tv_exceeds_bound_forged` | D | D | 1 | D7 H3: | 1 | yes |
| `path_count_wrong` | E | E | 1 | E1 I: | 1 | yes |
| `alpha_table_wrong_exponent` | E | E | 1 | E2 I: | 1 | yes |
| `line_points_misclassified` | E | E | 1 | E4 reg | 1 | yes |
| `claim_nonunique_at_silent` | F | F | 1 | F2 the | 1 | yes |
| `claim_unique_at_silent` | F | F | 1 | F2 the | 1 | yes |
| `claim_phase_transition` | F | F | 1 | F2 the | 1 | yes |
| `claim_physical_rule` | F | F | 1 | F2 the | 1 | yes |
| `claim_author_in_theorem` | F | F | 1 | F3 the | 1 | yes |
in-family: 31/31
