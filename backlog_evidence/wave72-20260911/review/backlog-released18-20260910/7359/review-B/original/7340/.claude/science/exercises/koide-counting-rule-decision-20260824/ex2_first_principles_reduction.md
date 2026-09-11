# EX2 — First-Principles Reduction of the Slot-Count Wall (2026-08-24)

Exercise agent, read-only. Refresher surfaces read: `docs/MINIMAL_AXIOMS_2026-06-29.md`;
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`; all four registered nodes in
`docs/audit/data/axiom_premise_nodes.json`; `CAMPAIGN_20260823_COMPLEX_STRUCTURE.md`
from THE FIBER THEOREM to end; plus `b181_reality_check_findings.md` (exact sector data)
and `origin/main:scripts/berezin_detc_detr_fork_2026_06_04.py` (the arbiter, loaded and called).
Status: exercise analysis only — nothing here is a claim, registration, or adoption.

## 0. The wall, in its exact minimal data

Record-slice sector (12x6 bench, s_x=3/5, s_t=0): a=43/35, d=a*s_x=129/175; per chart
k=1,2 the c-block is aI+dJ; eigenlines g_+/-, h_+/- with lam_+/- = a +/- di; Theta g_+=h_-,
Theta g_-=h_+ (orbits O_+={g_+,h_-}, O_-={g_-,h_+}, each Theta-closed); X0 g_+=-g_-,
X0 h_-=-h_+ (X0 swaps the orbits and maps Q(+s_x) to Q(-s_x); joint-flip identity landed).
Additive count: n=2 slots -> r=1 -> Q=1. Quotient count: n=1 -> r=1/2 -> Q=2/3.
Given as landed for this exercise: the orbit structure, the joint-flip identity, the
no-registration theorem (no record readout registers the orbit label), three checker
rounds finding no landed principle entails either count.

## (a) WEAKEN — what actually consumes r

Enumeration of downstream consumers of r in landed structure:
1. The Koide lever Q=(1+2r)/3 (the arbiter + circulant narrow theorem). Sole landed consumer.
2. Nothing else sees the sector at all: the c-fiber is exactly decoupled (no Q/W9 block),
   so every transport-borne window (interference J, dial responses) is c-blind; the B2/b178
   results confine positive transport-sensitive readouts to the rank-one |Z|^2 family; and
   empirical Koide 2/3 is barred as an in-framework tiebreak by the re-prove policy.
3. Candidate consumer the lane has not yet computed: the sector's MULTIPLICATIVE det factor
   in the landed partition function itself. A decoupled block contributes det(c-block)^p with
   p fixed by how many integration variables the landed measure actually carries there —
   p=2 (all four real dims) vs p=1 (a halved carrier). This is not a new observable; it is
   a factor of the already-landed Z.
WEAKENED QUESTION (sufficient to discharge the physics): "what det-power does the c-sector
contribute to the landed Z, relative to a known single-slot sector?" Answering it never
adjudicates an abstract counting rule; it reads the count off the committed measure.

## (b) DELETE — which premise makes the question arise, and the minimal formulation

Assessed candidate deletions:
- REAL-FORM / DROP THE ORIENTATION COORDINATE: works, and is decisive about what the fork
  IS. Invariant data: the real 4-dim sector W_R with real operator Q_R; min poly gives the
  canonical transport complex structure J_can=(Q_R-aI)/d (J_can^2=-I; the sign of d is frame
  and +/-J_can are conjugate — count-stable). Over J_can the sector is E_+ = the lam_+
  eigenspace ~ C^2 with Q = lam_+ * I (scalar). The orientation coordinate is gone, yet the
  fork SURVIVES as dim_C E_+ = 2: the two orbits are not orientation-conjugates inside the
  fixed theory (their exchange needs the dial flip); the fork is about MULTIPLICITY, not
  orientation. This kills the pure frame-argument route to the quotient: frame-invariance
  quotients the orbit ORDERING (the label — consistent with the no-registration theorem),
  not the CARDINALITY. Adjudication (d) of the orientation-bit run: the invariant relative
  sign is count-neutral; no landed invariant reduces 2 to 1.
- BEREZIN/GRASSMANN MEASURE PRESENTATION: does not decide — the arbiter's own landed cells
  prove statistics_not_decisive (real Gaussian = Majorana Berezin; holo Gaussian = holo
  Berezin). The measure re-houses the same bit as "which Grassmann algebra."
- INVARIANT-DATA-ONLY (triple sign): the count persists as invariant multiplicity 2.
THE MINIMAL FORMULATION IN WHICH THE COUNT IS UNAMBIGUOUS: the landed measure itself.
New exact structure (verified in the toy): sigma := -Theta o X0 is an ANTILINEAR INVOLUTION
of E_+ (sigma g_+ = h_+, sigma^2=+1, built only from landed objects) — a real structure on
the sector. The two branches are then EXACTLY a sector-level POLARIZATION-SELECT instance:
  carrier = E_+ (full real form W_R, 4 real integration dims)      -> n=2 -> Q=1
  carrier = Fix(sigma) (sigma-real form, 2 real integration dims)  -> n=1 -> Q=2/3
So the question never arises in a formulation that states the sector's FIELD CONTENT: the
count is whatever the committed integral integrates. "Additive vs quotient counting" was
presentation fog over one physical bit: is sigma-reality imposed on the record-slice
carrier or not. This also sharpens the seventh correction's phrase "orienting the staggered
grading": choosing Fix(sigma) is precisely a joint (X0, conj) discrete commitment — but now
phrased arbiter-natively as supplied field content, not as a counting principle.

## (c) MINIMIZE — the smallest end-to-end object (computed, not sketched)

Toy: C^2 (+) C^2 (charts), Q(d) = (aI+dJ) (+) (aI+dJ) with the committed rationals,
Theta = chart-swap o conj (slice reflection = identity, per b181), X0 = diag(-1,1,-1,1).
Run: scratchpad `toy_run.py` importing the arbiter's own CPair/det_cpair/det_fraction/
r_from_slot_count/q_from_r. Results, all exact:
- 13/13 identity checks PASS: eigenpairs, all four Theta maps (orbit closure), X0 orbit
  swap, the joint flip X0 Q(+d) X0 = Q(-d), and sigma (antilinear, involutive, E_+ -> E_+).
- Arbiter end-to-end: n=2 -> r=1 -> Q=1; n=1 -> r=1/2 -> Q=2/3 (its functions, unmodified).
- Independent quantity (the Z factor of the decoupled block): a^2+d^2 = 62866/30625;
  carrier W_R: det of the realified block = (62866/30625)^2 = 3952133956/937890625;
  carrier Fix(sigma): one holo slot det_C norm = 62866/30625.
  DISCRIMINATOR RATIO = a^2+d^2 = 62866/30625 != 1: the readings differ in a landed-object
  quantity, not only in the Q formula. One of them mis-describes the committed integral.

## (d) THE FASTEST FALSIFIER

Artifact: one exact-rational runner, `c_sector_det_power_probe` (~150 lines), on the landed
b171/b179 machinery at Bench("12x6",12,6), committed dials, constant carrier: build the full
landed quadratic form, use the exact c-fiber decoupling to factor Z, and extract the
c-sector's det EXPONENT relative to two in-Z calibration cells of known slot count (the
level-4 singleton fiber; the b179 accepted doublet cell). Runtime: minutes (exact fractions,
<= 24x24 realifications). Pass/fail, exact rational equality:
- c-factor = (62866/30625)^2 relative to calibration -> the committed measure integrates all
  four real dims: QUOTIENT COUNTING IS FALSE of committed structure (Q=2/3 then requires the
  sigma-reality bit as new physical input — a proposal for Jon's bar, not a derivation).
- c-factor = (62866/30625)^1 -> the committed field content is already the sigma-real form:
  ADDITIVE COUNTING IS FALSE; Q=2/3 closes with no new premise.
- c-factor cancels from every landed normalized window (if absolute Z is nowhere consumed):
  underdetermination is PROVEN by cancellation, not asserted by checker exhaustion.

## Verdict

The wall is not a counting-rule question; committed structure fixes the count as soon as the
record-slice FIELD CONTENT is stated, and the committed measure already states it — read it
off. If (and only if) the probe lands in the third outcome, the decision is genuinely
underdetermined by all committed structure, and the MINIMAL new physical input deciding it
is one bit: whether the record-slice carrier is the sigma-real form Fix(-Theta o X0)
(equivalently, a physical orientation of the staggered grading). That bit is unreadable by
any record (no-registration theorem), which is bar-relevant color — unreadable field
doubling is surplus structure by Record-primacy taste — but decides nothing by itself.
