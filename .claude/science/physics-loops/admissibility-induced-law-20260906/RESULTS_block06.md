# RESULTS — block 06 (Fable primary seat; Opus contract lens before the build; Opus refuting checker pending), 2026-09-07

## Headline

On the open-boundary static strips of widths 4 and 5 (1296 and 7776 row states; 38 and 178 orbits under the row symmetry group of order 48), the deep-row pair-parallel probabilities of the edge pair and of the innermost pair are enclosed in exact rational intervals of width below `10^-50`, at both declared triples, by an elementary route that needs no algebraic field: the orbit quotient `Q` is self-adjoint for the weights `|O| A_O` (S2, proved from block 02's F1 and the symmetry of `φ`; executed on every orbit pair), so the two-sided ratio bounds enclose the Perron root, the trace bound `λ_2^2 ≤ tr(Q^2) − lo^2` controls every other eigenvalue, the residual–gap bound controls the angle between `Q^40 1` and the Perron vector, and one Cauchy–Schwarz step encloses the statistic (S3). Every enclosure excludes the formation value `f = p/(p+q+4r)` by more than `10^-3` (widths 2, 3, 4, 5; S5), and the innermost pair is strictly more often parallel than the edge pair at widths 4, 5. The Krylov dimension of `Q` on `1` is `8, 30, 16, 111`, with the integer dependency `m_1(Q) 1 = 0` verified exactly on every orbit at all four cases by the runner itself (the degree-111 polynomial with 526-digit coefficients in about ten seconds by a multi-modular search plus integer verification); `m_1` is irreducible at degrees 8, 30, 16, and at degrees 8 and 16 the statistics are identified as algebraic numbers by their minimal polynomials (S4). Nothing about wider strips, the plane, monotonicity in the width, or a physical order.

## Run record

- Runner `scripts/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.py`: 34 checks in families A (5), B (5), C (7), D (7), E (4), F (5), G (1); 26 declared mutations (4 B, 6 C, 9 D, 3 E, 4 F). Baseline about 60 s uncontended (the largest items: the width-5 quotient builds, the degree-111 modular solve, the `n = 33` full-state boundary check at width 5 through the tensor structure of `V`, the degree-30 Sturm counts).
- Cache: runner sha256 `57a840346f74b10ae5e9f5a518c62f358d4767034144c860dd389280adc04997`, input fingerprint `b5a5caa473ef094e41da23da07a4ac5a7a057d7d277da668f5f6c9e18aa7565c`, exit 0, elapsed 64.33 s, `TOTAL: PASS=34 FAIL=0` (written by `execute_and_write_cache(<runner>, 900)` after the final note edit and after the census had finished; uncontended).
- Control reproduction before any theorem sentence (own code, scratch `control_repro.py`, 23 s): orbit counts 38/178; Krylov dimensions 8/30/16/111 with the exact dependency verified on all orbits at every case; `λ_1` to 18 digits at all four cases; `tr(Q^2)` at all four; the 22-digit enclosures of `s_edge` and `s_inner` at all four; the ratio bounds `0.05538, 0.03301, 0.06932, 0.04150`; the innermost sector values at `W = 5`, `(3,1,2)`, `n = 3, 5, 9, 17, 33, 65` (`n = 33`: `0.2562896288160817584176711…`, `1.49 × 10^-25` from the enclosure). All equal to the supervisor's controls.
- Note `docs/ADMISSIBILITY_RULE_STATIC_STRIP_WIDTHS_4_5_RIGOROUS_ENCLOSURE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`: 546 lines (reflowed from 634 after the census, whitespace only); `vocab_lint --report-only` 0 violations; the classical names appear only in Prior art, Imports and the verbatim third fence in Boundaries (runner F4 strips that fence before scanning Boundaries).

## Defects fixed while executing

- First full run: the `--exact` printing of the field image crashed on Python's 4300-digit integer-to-string limit; the limit is lifted at import and the image is printed as 40-digit outward labels with the coefficient counts and digit sizes instead of the raw rationals.
- The E3 literal check first demanded `floor = 54437` for the width-4/width-5 difference of `s_inner`; the exact interval difference is `[5.4436…, 5.4437…] × 10^-6` (and `[1.8169…, 1.8170…] × 10^-7` for `s_edge`), so the contract's `5.4437`, `1.8170` are the upper (rounded-up) labels; the check and the note's S5 say so.
- The E4 detail string carried the four ratio labels as literals, which the runner's own F3 (float-literal scan) and F5 (every decimal from `dec()`) flagged; the labels are now produced by `dec(…, 5, up=True)` from the exact rationals. The F3 scan's own lines named the array library and matched themselves; the word is assembled from parts on marker lines.
- The note used "certificate" twice ("the rank certificate", "the resolution certificate"); the lane's forbidden scan is a substring match on the family of that word, so both were reworded.

## Could-not list

- The identification of the statistics as algebraic numbers is executed at Krylov degrees 8 and 16 only; at degree 30 (width 4, `(5,2,4)`) it was not attempted (the contract scopes it to `d ≤ 16`), and at degree 111 neither factorization nor root isolation is attempted; the S3 enclosure stands alone there.
- Irreducibility of `m_1` at degree 111 is not claimed; the polynomial is verified exactly and nothing else.
- `s_inner` is a distinct statistic at two widths only; the width-4/width-5 differences are two numbers, not a law.
- The boundary check with the single record `P(e_y)` on both end rows is executed on the full state through the tensor structure of `V` (not in the sector, where a single record is not `G`-invariant); the sector version uses the orbit-averaged record. Both are within `10^-6` of the enclosures at `n = 33`; the contract's "(sector)" wording is read as the latter.
- The refuting checker seat has not yet run.

## Modelling choices (declared, not physics)

- Menu order, orbit weights, `A`, `V`, `T` as in block 02; the group as the 24 signed axis permutations of determinant `+1` (computed by the Leibniz formula) times the row reversal; orbits by the images of each row.
- The power `k = 40`; the square-root scale `10^80` (integer square root plus one, over the scale) for `λ_2bound`, `r` and `√2`; enclosures `[s(y) − 2ε, s(y) + 2ε]` with `ε = √2 r/δ`.
- The Krylov dimension by an incremental reduced echelon form modulo `2^61 − 1` and `2^89 − 1` (both must agree at each step); the integer coefficients of `m_1` by a multi-modular Gauss–Jordan solve on `d` rows independent modulo `2^61 − 1` with primes of 512 bits (enough that their product exceeds `2 (1 + ⌈hi⌉)^d`), symmetric CRT, then the exact integer verification of `m_1(Q) 1 = 0` on every orbit — the verification is the proof, the search is not.
- The resultant `Res_λ(m_1, y D − N)` by exact evaluation at `y = 0, …, d` (univariate integer resultants) and Lagrange interpolation over `Q`; `N`, `D` scaled to integer coefficients by their common denominator (the ratio is unchanged).
- The full-state transfer as `T v = φ^{⊗W} (A ∘ v)` and `a T = A ∘ (φ^{⊗W} a)` (mode-by-mode application; checked against the explicit `T` at width 4 on three vectors).
- The finite-`n` sequence `n = 3, 5, 9, 17, 33, 65` in the sector; the end-record check at `n = 33`.

## Exact polynomials and enclosures (`--exact`)

The runner's `--exact` output (139 kB) carries every rational endpoint, the Krylov polynomials and the minimal polynomials; the items below are copied from it, the longest ones summarized by size.

- `W=4 (3, 1, 2)`: `lo` and `hi` are rationals with numerators of 154 and 154 digits; `lambda_2bound = 9252156550117622340549561250885119672389…` (166 characters); `eps` has a numerator of 403 digits and a denominator of 462 digits.
- `W=4 (5, 2, 4)`: `lo` and `hi` are rationals with numerators of 295 and 296 digits; `lambda_2bound = 6520460104507972001938329454854852930731…` (166 characters); `eps` has a numerator of 677 digits and a denominator of 746 digits.
- `W=5 (3, 1, 2)`: `lo` and `hi` are rationals with numerators of 197 and 198 digits; `lambda_2bound = 6965913608746311750577245376703845282281…` (166 characters); `eps` has a numerator of 493 digits and a denominator of 550 digits.
- `W=5 (5, 2, 4)`: `lo` and `hi` are rationals with numerators of 374 and 375 digits; `lambda_2bound = 5788325937310705677965247667602858633557…` (170 characters); `eps` has a numerator of 837 digits and a denominator of 905 digits.
- `W=4 (3, 1, 2)` `s_edge` exact endpoints: numerators of 759 and 759 digits over denominators of 760 and 760 digits; lower endpoint begins `815377579855216765925967923962970826407199544400466566937083…`.
- `W=4 (3, 1, 2)` `s_inner` exact endpoints: numerators of 759 and 759 digits over denominators of 760 and 760 digits; lower endpoint begins `815912228701878964373898774462237436309230072719747837152315…`.
- `W=4 (5, 2, 4)` `s_edge` exact endpoints: numerators of 1325 and 1325 digits over denominators of 1326 and 1326 digits; lower endpoint begins `501375959323205928663749294163091088121844242810666919340138…`.
- `W=4 (5, 2, 4)` `s_inner` exact endpoints: numerators of 1325 and 1325 digits over denominators of 1326 and 1326 digits; lower endpoint begins `501469238376366226610836280946278455771119791841390118786040…`.
- `W=5 (3, 1, 2)` `s_edge` exact endpoints: numerators of 933 and 933 digits over denominators of 934 and 934 digits; lower endpoint begins `312370394208059324556203037056376361414998726517688179136844…`.
- `W=5 (3, 1, 2)` `s_inner` exact endpoints: numerators of 933 and 933 digits over denominators of 934 and 934 digits; lower endpoint begins `312581635272004493507284137436037046948196854440513373002020…`.
- `W=5 (5, 2, 4)` `s_edge` exact endpoints: numerators of 1641 and 1641 digits over denominators of 1642 and 1642 digits; lower endpoint begins `475133158249488917769093422621066759371419893304560704118872…`.
- `W=5 (5, 2, 4)` `s_inner` exact endpoints: numerators of 1641 and 1641 digits over denominators of 1642 and 1642 digits; lower endpoint begins `475223065180482597443298749619390458826639759904965777164068…`.
- `W=4 (3, 1, 2)` finite-n exact values: n=3: s_inner numerator 9 digits, s_edge numerator 9 digits; n=5: s_inner numerator 16 digits, s_edge numerator 16 digits … (n = 3: s_inner = `107714193/420597956…`).
- `W=4 (5, 2, 4)` finite-n exact values: n=3: s_inner numerator 18 digits, s_edge numerator 18 digits; n=5: s_inner numerator 33 digits, s_edge numerator 33 digits … (n = 3: s_inner = `222799818274226215/1013126379051875359…`).
- `W=5 (3, 1, 2)` finite-n exact values: n=3: s_inner numerator 11 digits, s_edge numerator 11 digits; n=5: s_inner numerator 19 digits, s_edge numerator 20 digits … (n = 3: s_inner = `40913020773/159752845180…`).
- `W=5 (5, 2, 4)` finite-n exact values: n=3: s_inner numerator 24 digits, s_edge numerator 24 digits; n=5: s_inner numerator 42 digits, s_edge numerator 42 digits … (n = 3: s_inner = `119715640502298039013185/544375382349486764567177…`).
- `W=4 (3, 1, 2)` minimal polynomial of `s_inner` (degree 8):

  `1596512138085954177217195333829992847318622983394023515577326321659152685839985882374068762341152695541438763008*y**8 - 4458330695748456797950296417609507335145417909394338635135879695904845501210569490673983679467552887727252003840*y**7 + 5356107581624239935652280897278830818321837833684891040885504808602281158640560317123958582703229926115549003712*y**6 - 3614463712241632629009872644815197027983975784389477568075803247679093843341255590905709522548173226179872431456*y**5 + 1498153233861410979723083796486437970500957535554137131324861835099391782341988872294533787879241291594845532533*y**4 - 390482691996646337665679835338417833903599499981641682257744992538214165019073860153144349524811563134999610622*y**3 + 62492572067008059919735026034508178268089246264967789207571650549794668630541187233175643350001413857463764141*y**2 - 5614177642099541636299765804332977761903373105080423728182210399580726444699555154261919707221429683414309232*y + 216750374423727790441535258059281039810131770277934922316910824737769729826015059931982727383694092643822163`

- W=4 (3, 1, 2): image of N/D for s_inner on the refined isolating interval: [0.2562841851395883553318126802890931412871, 0.2562841851395883553318126802890931412872]; N, D have 8 integer coefficients of up to 62 digits
- `W=4 (3, 1, 2)` minimal polynomial of `s_edge` (degree 8):

  `772711874833601821773122541573716538102213523962707381539425939683029899946553167069049280973117904642056361295872*y**8 - 2015026899511992107063033469000465397062996454525526472284808551185280928851208419785651552723901663796634797174784*y**7 + 2215508318553560537171752101834400831891193520588342766198084953406087908556021367269876580172775741386519343540992*y**6 - 1335363876274739635003516100729470248325025460320997841257378594492061870515152524795603135663142903801632092993024*y**5 + 479559712919180736828946017469188380921014511730164044205084233800791570473133799188481232147128493995964547932692*y**4 - 104048585046906780889979996288919960675880167673817231113366251892687541474420451417421079282856662144861086587744*y**3 + 13088546836560310875599119338064695241128809230163492645720680207946583939370198300606149213512254767805793648865*y**2 - 841463447790639490443585117764179047908076995941632096964093185533288100960749293612678591951485038160642986409*y + 19177854626052947650636187827342194866174334685793710058937506103378486252194970484561781286095044048809159111`

- W=4 (3, 1, 2): image of N/D for s_edge on the refined isolating interval: [0.2561162479042062541091894487266876417699, 0.2561162479042062541091894487266876417700]; N, D have 8 integer coefficients of up to 62 digits
- `W=5 (3, 1, 2)` minimal polynomial of `s_inner` (degree 16): integer coefficients of up to 538 digits; leading coefficient `38288879280768251791163251500405398319074686613155…`; printed in full under `--exact`.
- W=5 (3, 1, 2): image of N/D for s_inner on the refined isolating interval: [0.2562896288160817584176713359161367180141, 0.2562896288160817584176713359161367180142]; N, D have 16 integer coefficients of up to 166 digits
- `W=5 (3, 1, 2)` minimal polynomial of `s_edge` (degree 16): integer coefficients of up to 538 digits; leading coefficient `63814798801280419651938752500675663865124477688593…`; printed in full under `--exact`.
- W=5 (3, 1, 2): image of N/D for s_edge on the refined isolating interval: [0.2561164296010283514028361313868890496719, 0.2561164296010283514028361313868890496720]; N, D have 16 integer coefficients of up to 166 digits
- `W=4 (3, 1, 2)` `m_1` of degree 8, coefficients low to high (monic): `90219989988109256849620992, -2412275093353715386548224, 22193931315681941258240, -76784493914501414912, 62001017490767872, -20736995753984, 3149745152, -185216`
- `W=4 (5, 2, 4)` `m_1` of degree 30, coefficients low to high (monic): `58981624059611320715844752608071591504684645054467014280580454080034651260516700300247040000000000000000000000, -5336763628220616892349733664952656548500842826949631677618876345124617742895751978150789120000000000000000000, 186345837733311917222045812207025334330626752736903270423678343229193636468163509006578483200000000000000000, -3229359605448559226969646626040837003913701502401772123758503341669653695562159254981836800000000000000000, 30261324615573629300634933431201297705082871387111874875968382496411297360248550370941337600000000000000, -160664230064467377322846079054539251909601834521678963551790019537579389569177487157493760000000000000, 478519473713772244577049894362907075193899866875120676606647741349191941351645589064908800000000000, -680671147408024642580008906120503255408906532116474764182320477297666473255259812659200000000000, -39879143059875992082315067831769140586152388559260396912867882208490788234003166003200000000, 1426639237822982711401714978947667849243178119391227318185406587662746075870632345600000000, -1345142700236733688707363341996591686488647463064874166290903608572841163684315136000000, -412765699357456547414650576842466789886735741595684174778747686563272878509260800000, 985486895624058107806749356152485566532736634376980408281026776871884543754240000, -166531873532746874305184393552720076641568577415421092781590786350327529472000, -103861766376642143725767066219438252587701558380231398945999946128975462400, 16774227896634322750087333424917428620563506324931126465173914438860800, 5144840638454721301710628426955645126851586258697270292890330857472, -429905799025265257151405753196966255646860012994625880302026752, -122868939921241161400361971427422340223099898689192374304768, 921076552845447878670268551446327631909831124080132096, 858248226307113720676819568798544816066532864950272, -3764551156351493028479470834626323118787002368, -2711671905725963661951642873243368019984384, 46454304180747747122169185358577615872, 3093232969314389304161086780793344, -113976942210321766182250102784, 1319016775580747701958368, -6943865085059439252, 17293143577680, -16872201`
- `W=5 (3, 1, 2)` `m_1` of degree 16, coefficients low to high (monic): `54300750807023017100985063838587641511898876115983680846379440144384, -182713577206556711676057278082266311054929377712900287455138152448, 272495171422624773826987067468124360548986748859141023799967744, -236843699528570460559804816826143257722150589488484723982336, 132612703975555404113497738145446784248226353949058269184, -49867216153339744775995915592646188131357344252559360, 12720840284178132976302591049953331732046380269568, -2168859286809094496388513519874103074717958144, 236946119339270745991926370398463829475328, -15345030056384549782021084503399727104, 529513003502231142663821386055680, -10304226701536044782991704064, 117909227128787124092928, -790639441027792896, 2902100475904, -4694848`
- `W=5 (5, 2, 4)` `m_1` of degree 111: 111 integer coefficients of up to 526 digits (constant term `1193885195544829142494617460258820799032…`, `526` digits); printed in full under `--exact`; the dependency is verified on all 178 orbits.

## Verified stdout (final runner, unmutated; run 4, 63 s uncontended, 5,926 characters)

```
AUDIT_INPUT_PATHS:
  docs/ADMISSIBILITY_RULE_STATIC_STRIP_WIDTHS_4_5_RIGOROUS_ENCLOSURE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-09-07.md
  docs/MINIMAL_AXIOMS_2026-06-29.md
  docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md
AUDIT_TIMEOUT_SEC: 900
scope: the six-projector menu, the product rule at two exact triples; the static strips of widths 4 and 5 (widths 2, 3 as controls); exact arithmetic; no plane, no wider strip, no monotonicity in the width, no order selected
mutation: none
PASS: A1 the three declared inputs exist (this note, the axiom memo, block 02)
PASS: A2 the six axiom sentences used are present verbatim in the axiom memo
PASS: A3 block 02's claim id and deep-row fragment present
PASS: A4 this note carries its claim id and names this runner
PASS: A5 blocks 03-05 are not inputs
PASS: B1 row orbits under G (order 48): 3, 8, 38, 178 at widths 2-5, both triples
PASS: B2 T(g rho, g rho') = T(rho, rho'), all 48 maps: every representative x all 1296 rows (W=4); two representatives x 7776 rows (W=5)
PASS: B3 Q representative-independent (second representative of every orbit); R_OO' |O'| = |O| Q_OO'; sizes sum to 6^W, parallel counts to 6^(W-1)
PASS: B4 the tensor-structured full-state transfer equals the explicit T on three vectors, both actions, W=4
PASS: B5 sector center-row statistics = full-state ones: W=4 at n = 3, 5, 7; W=5 at n = 3, 5; both pairs, both triples (20 equalities)
PASS: C1 w_O Q_OO' = w_O' Q_O'O on every orbit pair (38^2, 178^2), both triples: Q self-adjoint for w = |O| A
PASS: C2 tr(Q^2) = 28006524928, 250087391159985, 16238809878528, 1948759036672266913
PASS: C3 ratio bounds after 40 powers: 0 < lo <= mu <= hi; 18-digit outward labels of lambda_1 are the contract's, four cases
PASS: C4 Krylov dimension of Q on 1 = 8, 30, 16, 111 (ranks mod 2^61-1, 2^89-1; integer dependency m_1(Q) 1 = 0 verified on every orbit, four cases)
PASS: C5 W=4: charpoly factor degrees [1, 1, 2, 8] and [1, 1, 1, 5, 30]; m_1 is the factor of degree d
PASS: C6 m_1 irreducible over Q at d = 8, 30, 16; at d = 111 factorization not attempted, nothing claimed
PASS: C7 d = 8, 30, 16: exactly one real root of m_1 in [lo, hi], none above hi (Sturm counts)
PASS: D1 four cases: y > 0, delta = mu - lambda_2bound > 0, lo > lambda_2bound, square-root bounds are upper bounds, residual recomputed
PASS: D2 enclosures [s(y) - 2 eps, s(y) + 2 eps] of width < 10^-50; 22-digit outward labels are the contract's (four cases, both pairs)
PASS: D3 no enclosure contains f = 1/4 or 5/23 (eight enclosures)
PASS: D4 sector center-row statistics at n = 3, 5, 9, 17, 33, 65: strictly decreasing distances to the enclosure, both pairs, four cases
PASS: D5 end records P(e_y) on both end rows at n = 33 (full state via the tensor structure; orbit-averaged in the sector): within 10^-6 of the enclosures
PASS: D6 widths 2, 3 by the same route: block 02's F4 digits (18 and 22) reproduced, f excluded, innermost pair = edge pair
PASS: D7 d <= 16: Q x = lambda_1 x in Q[lam]/(m_1) on every orbit, x one-signed; one irreducible factor of the resultant with one root in the enclosure for s_inner, s_edge; field image meets the enclosure
W=2 (3, 1, 2): s_edge 0.2559430889.. s_inner 0.2559430889.. minus f: 0.00594308.. 0.00594308..
W=2 (5, 2, 4): s_edge 0.2198741761.. s_inner 0.2198741761.. minus f: 0.00248287.. 0.00248287..
W=3 (3, 1, 2): s_edge 0.2561109872.. s_inner 0.2561109872.. minus f: 0.00611098.. 0.00611098..
W=3 (5, 2, 4): s_edge 0.2199151616.. s_inner 0.2199151616.. minus f: 0.00252385.. 0.00252385..
W=4 (3, 1, 2): s_edge 0.2561162479.. s_inner 0.2562841851.. minus f: 0.00611624.. 0.00628418..
W=4 (5, 2, 4): s_edge 0.2199158620.. s_inner 0.2199567765.. minus f: 0.00252455.. 0.00256547..
W=5 (3, 1, 2): s_edge 0.2561164296.. s_inner 0.2562896288.. minus f: 0.00611642.. 0.00628962..
W=5 (5, 2, 4): s_edge 0.2199158748.. s_inner 0.2199574883.. minus f: 0.00252457.. 0.00256618..
PASS: E1 s - f > 10^-3 at widths 2, 3, 4, 5, both pairs, both triples; 8-digit labels at widths 4, 5 are the contract's
PASS: E2 s_inner > s_edge strictly at widths 4, 5, both triples (lower endpoint above the upper endpoint)
PASS: E3 the width-4 and width-5 values differ at (3,1,2) by s_inner: [0.0000054436, 0.0000054437] and s_edge: [0.00000018169, 0.00000018170] (outward labels; two data points)
PASS: E4 lambda_2bound/lo <= 0.05538, 0.03301, 0.06932, 0.04150 (rounded up; bounds the executed ratio, not the true lambda_2/lambda_1)
PASS: F1 the note carries the three fence sentences verbatim
PASS: F2 the note contains no forbidden phrase (hits: [])
PASS: F3 runner source: no floating-point literal, conversion, evaluation call or array library (0 hits)
PASS: F4 classical names only in Prior art, Imports and the verbatim fence (offenders: [])
PASS: F5 every decimal label in this stdout came from the integer-arithmetic dec() (32 labels; stray: [])
per_element: executed — every row state of the width-2, 3, 4, 5 strips enters the orbit reduction, the quotients and the full-state checks, both triples, exact
per_site: executed — the edge pair (0, 1) and the innermost pair of every row; the end-row records on every site of both end rows in the boundary check
per_mode: executed — the Perron root by the ratio bounds, every other eigenvalue by the trace bound, the Perron vector by the residual-gap bound, the Krylov degree exactly; minimal polynomials where the degree allows
per_block: executed — the finite-n center rows for n = 3 to 65 in the sector and n = 3 to 7 (width 4) and 3 to 5 (width 5) on the full state; the characteristic polynomial at width 4
lattice_wide: checked and not executed — strips of widths 2 to 5 only; the plane and wider strips are named, not computed, and no monotonicity in the width is stated
PASS: G1 the five N5 resolution lines are printed (each >= 40 characters)
elapsed_s: 63
TOTAL: PASS=34 FAIL=0
```

## Mutation census (26 mutations, one helper invocation each, 4 in parallel; expected/observed read from raw stdout at the final runner sha256 57a840346f74b10a…; the note reflowed to 546 lines afterwards with byte-identical normalized text, which the F-family checks normalize before comparing)

| mutation | expected | observed | PASS | FAIL | failing checks | single family |
|---|---|---|---|---|---|---|
| `boundary_dependence_forged` | D | D | 33 | 1 | D5 | yes |
| `charpoly_factor_mismatch` | C | C | 33 | 1 | C5 | yes |
| `claim_classical_name_in_theorem` | F | F | 33 | 1 | F4 | yes |
| `claim_monotone_in_W` | F | F | 33 | 1 | F2 | yes |
| `claim_plane_limit` | F | F | 33 | 1 | F2 | yes |
| `claim_washes_out` | F | F | 33 | 1 | F2 | yes |
| `commutation_broken` | B | B | 33 | 1 | B2 | yes |
| `cw_interval_forged` | C | C | 33 | 1 | C3 | yes |
| `dependency_not_verified` | C | C | 33 | 1 | C4 | yes |
| `field_vector_not_eigen` | D | D | 33 | 1 | D7 | yes |
| `finite_n_sequence_shuffled` | D | D | 33 | 1 | D4 | yes |
| `inner_edge_order_flipped` | E | E | 33 | 1 | E2 | yes |
| `krylov_dimension_off` | C | C | 33 | 1 | C4 | yes |
| `largest_root_outside_interval` | C | C | 33 | 1 | C7 | yes |
| `orbit_count_wrong` | B | B | 33 | 1 | B1 | yes |
| `quotient_row_identity_broken` | B | B | 33 | 1 | B3 | yes |
| `ratio_bound_too_small` | E | E | 33 | 1 | E4 | yes |
| `residual_forged` | D | D | 33 | 1 | D1 | yes |
| `residual_gap_ignored` | D | D | 33 | 1 | D1 | yes |
| `resultant_factor_wrong` | D | D | 33 | 1 | D7 | yes |
| `s_enclosure_contains_formation_value` | D | D | 33 | 1 | D3 | yes |
| `sector_full_mismatch` | B | B | 33 | 1 | B5 | yes |
| `self_adjointness_broken` | C | C | 33 | 1 | C1 | yes |
| `separation_sign_flipped` | E | E | 33 | 1 | E1 | yes |
| `trace_bound_forged` | D | D | 33 | 1 | D1 | yes |
| `w2_w3_literals_off` | D | D | 33 | 1 | D6 | yes |

26 of 26 mutations fail in exactly their declared family

Each mutated run reports `TOTAL: PASS=33 FAIL=1` with the single failing check in the declared family; the mutation `field_vector_not_eigen` is the slowest (the perturbed field vector defeats the cancellation in the resultant's interpolation), about four minutes four-wide; every other run about 60–100 s four-wide.

## Supervisor folds, the refuting checker, and the final certificate (2026-09-07)

- Contract lens (Opus 5, before the build; `scratchpad/panel6/L4_block06_refuter.md`): fifteen findings on the supervisor's contract, no theorem refuted — float-printed decimals in the table (D1, blocking), upper bounds rounded the wrong way (D2), S2's hypotheses (D3), the upper ratio bound's justification (D4), unstated side conditions (D5), S3(d) underived (D6), S1 not covered by a control (D7), the residual-gap control's output unrecorded (D8), the identification order (D9), "agree to 5e-6" false (D10), limit language in the title and V4 (D11), the forbidden list (D12), a dangling premise (D13), a theorem marked executed (D14), "middle pair" (D15); all folded into the contract before the primary ran; the late exact degree-111 construction reproduced by the supervisor in 795 s (`specs/supervisor_control_block06_krylov_d111_exact.out.txt`).
- Supervisor line-by-line review of the primary's runner (1148 lines) and note (546 lines): the enclosure code read against the contract's four steps (the weighted quotient, the upward-rounded square roots at scale 10^80, `δ = μ − λ_2bound`, `ε = √2·r/δ`, the 2ε bound on both statistics), the decimal-label scan (F5), the classical-name placement (F4). Fold 1: the third fence reworded without the classical names (the runner's constant and its F4 exception removed), the degree-111 control attribution, "about the same size".
- Refuting checker (Opus 5, disjoint machinery; `CHECKER_block06_findings.md`): PASS-NO-BLOCKER, nothing refuted; every quantitative literal reproduced, including all eight enclosures to 22 digits from an independent full-state route at width 4; three wording findings folded (fold 2: the orbit-sum justification of the innermost pair, the width-4 factor multiplicities, one lay phrase; the mirror-count verification attributed to the checker).
- Final certificate: `TOTAL: PASS=34 FAIL=0`; runner sha256 `9b05b6d8b81fdf529885ac1e0a31922557889e255260ac6e9f17e600c875d315` (unchanged by the note-only folds); input fingerprint `48aebbe9db08ce9d78d0373eeda8f381d035594ab280c4bb46f7520f4c4bbc39`; exit 0; elapsed 79.6 s; unmutated stdout 5,945 characters; note 551 lines, vocab lint 0; 26 mutations, census at this runner sha (table below). Gates on the final tree: pipeline PASS (`graph_delta=acknowledged`, two passes), changed-evidence `checked=6 failures=0`, audit_lint strict OK, diff --check clean, manifest 4766 nodes, 11870 edges (+1 node).

## Final census (26 mutations, one helper invocation each, 4 in parallel; expected/observed read from raw stdout at the final runner sha 9b05b6d8…)

| mutation | expected | observed | FAIL count | failing checks | exit | in-family |
|---|---|---|---|---|---|---|
| `orbit_count_wrong` | B | B | 1 | B1 row | 1 | yes |
| `commutation_broken` | B | B | 1 | B2 T(g | 1 | yes |
| `sector_full_mismatch` | B | B | 1 | B5 sec | 1 | yes |
| `quotient_row_identity_broken` | B | B | 1 | B3 Q r | 1 | yes |
| `self_adjointness_broken` | C | C | 1 | C1 w_O | 1 | yes |
| `krylov_dimension_off` | C | C | 1 | C4 Kry | 1 | yes |
| `dependency_not_verified` | C | C | 1 | C4 Kry | 1 | yes |
| `cw_interval_forged` | C | C | 1 | C3 rat | 1 | yes |
| `charpoly_factor_mismatch` | C | C | 1 | C5 W=4 | 1 | yes |
| `largest_root_outside_interval` | C | C | 1 | C7 d = | 1 | yes |
| `trace_bound_forged` | D | D | 1 | D1 fou | 1 | yes |
| `residual_gap_ignored` | D | D | 1 | D1 fou | 1 | yes |
| `residual_forged` | D | D | 1 | D1 fou | 1 | yes |
| `s_enclosure_contains_formation_value` | D | D | 1 | D3 no | 1 | yes |
| `finite_n_sequence_shuffled` | D | D | 1 | D4 sec | 1 | yes |
| `boundary_dependence_forged` | D | D | 1 | D5 end | 1 | yes |
| `resultant_factor_wrong` | D | D | 1 | D7 d < | 1 | yes |
| `w2_w3_literals_off` | D | D | 1 | D6 wid | 1 | yes |
| `field_vector_not_eigen` | D | D | 1 | D7 d < | 1 | yes |
| `separation_sign_flipped` | E | E | 1 | E1 s - | 1 | yes |
| `ratio_bound_too_small` | E | E | 1 | E4 lam | 1 | yes |
| `inner_edge_order_flipped` | E | E | 1 | E2 s_i | 1 | yes |
| `claim_plane_limit` | F | F | 1 | F2 the | 1 | yes |
| `claim_monotone_in_W` | F | F | 1 | F2 the | 1 | yes |
| `claim_washes_out` | F | F | 1 | F2 the | 1 | yes |
| `claim_classical_name_in_theorem` | F | F | 1 | F4 cla | 1 | yes |
in-family: 26/26
