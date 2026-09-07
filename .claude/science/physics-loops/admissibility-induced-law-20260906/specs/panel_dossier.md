# Panel dossier — "What the nearest-neighbor rule induces on a finite window" (2026-09-06)

You are one lens of a four-lens physics panel convened at a direction-setting
juncture. Read this whole dossier, then read the COMPLETE axioms file from the
repository worktree (never truncate it):

    /Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/sync-science-task-0c8fac/docs/MINIMAL_AXIOMS_2026-06-29.md

You have read-only tools. Do NOT edit any repository file, do not run git
commands that change state, do not use `rm -rf`, and write your deliverable
ONLY to the path named at the bottom. You may run scratch Python in the
scratchpad directory. Time budget: 25 minutes. Deliver even if incomplete.

## 1. The framework in one paragraph

Four axioms. Lattice: sites are Z^3 with nearest-neighbor adjacency,
translations, proper cubic rotations; no site privileged. Qubit: each site has
a domain of local possibilities with algebraic presentation M_2(C); no
possibility privileged. Admissibility: "There is one fixed nearest-neighbor
admissibility rule, covariant under lattice translations and proper cubic
rotations. For each site, the probability distribution over the possibilities
is determined by, and varies with, the nearest-neighbor conditions." Reading
note (non-governing): "Read with Record, the distribution concerns which
possibility a forming record locks, conditional on formation at that site; it
does not supply the formation site, probability, or rate." Record: "Records
form. When present, a record locks exactly one admissible local possibility.
A site never carries more than one record; records are permanent. Only records
are readable. ... A site with no record cannot be read." The axioms explicitly
disclaim dynamics, a time metric, formation site/rate, and "source/action and
physical-observable identification" (listed as an open gate outside the
axioms).

The owner's standing sequencing rule (2026-08-26): identify the
framework-level action — "what the Admissibility rule induces on the infinite
lattice" — BEFORE any statistical bridge/Born postulate is considered; the
gravity lane's finite quadratic forms Q are measuring instruments, not the
framework action. Axioms are updated only for a layman-expressible physical
insight. Nothing is adopted or registered by a physics block.

## 2. Prior art that this block must reckon with

An archived, never-refereed Opus campaign (archive/campaigns/opus-direct-
20260827/POSITIVE_PATH.md, result R136, scripts opus_t210-213.py; floating
point) claimed: "Record consistency fixes the FORM of the admissibility rule."
Its chain: (i) permanence + one-per-site => a configuration of records is a
random field; (ii) "each site's distribution is determined by its neighbours
=> Markov"; (iii) Z^3 NN adjacency is triangle-free => cliques are edges;
(iv) positivity + Hammersley-Clifford => the joint factorises over edges;
(v) covariance => the edge potential is isotropic; hence
P(v_x | ne) ∝ Π_{y~x} φ(v_x·v_y). It also showed (floating point) that the
campaign's earlier "sum rule" P(v_x|ne) ∝ 1 + λ v_x·Σ_y v_y is the
conditional of NO joint law (compatibility nullspace empty, obstruction
O(λ^2)), and that requiring the normalized conditional to be affine in each
neighbour ("convex-consistency") forces the two-neighbour normaliser
Z(b,c) = Σ_s φ(s,b)φ(s,c) to be constant, which forces rank(F)=1, i.e. no
coupling. On the continuous sphere it verified by Funk-Hecke that Z is
constant iff φ is constant.

Supervisor's assessment of R136 (this is what the panel should stress):
step (ii) is a READING, not axiom content. It equates the Admissibility
conditional (the law of the record forming at x given its neighbours'
conditions at formation) with the full conditional μ(v_x | v_{all others}) of
a static joint law over complete configurations. The Record axiom describes
permanent records forming one site at a time; the law of the final
configuration is the product of the rule's conditionals along the formation
order, conditioning only on neighbours already recorded (unrecorded
neighbours are unreadable). That sequential object exists for ANY rule and is
in general order-dependent and different from the static law. So "the form
is forced" holds only under the static reading. Nobody has stated this
distinction as a theorem in the repository (searched: no front-of-house note
mentions formation order, Brook's lemma, or a growth/sequential law; the
Hammersley-Clifford step appears only in the archived Opus packet). The
repo's separate 2026-08-26 "statistical bridge" exercise measured, on the
gravity lane's Gaussian fixture, that the "sliding-frontier process"
marginals differ from the static Gram weights W9 = herm(Q^{-1}) by an
extent-stable gap of 5e-2..1.2e-1 — a numerical fixture-level cousin of the
same distinction, never stated at the axiom level.

## 3. The proposed block (exact finite theorems; one note, one exact runner, one PR off main)

Declared objects. A finite window W of Z^3 (or a small finite graph used as
a declared model: 3-path, 4-star, 4-cycle = one plaquette, open 2x2x2 cube
with its 12 edges); a finite proper-cubic-invariant menu M inside M_2(C) —
primary: the six Bloch-axis pure-state projectors P(±e_a) = (I ± σ_a)/2,
whose ordered pairs fall into three rotation orbits (parallel 6,
antiparallel 6, orthogonal 24). A nearest-neighbour rule r assigns to a site
and to any assignment η of menu values on a SUBSET of its neighbours (the
recorded ones) a probability vector r(· | η) on M; covariance means r depends
on η only through rotation-orbit data. Rule classes: (P) product rules
r(s|η) ∝ ψ(s) Π_{y recorded} φ(s, η_y), φ symmetric isotropic positive, with
three orbit values (p, q, r) on the menu; (S) the sum rule
r(s|η) ∝ 1 + λ Σ_y ⟨s, η_y⟩ with ⟨P,P'⟩ = 2Tr(PP') − 1 (positive for |λ|
small); (D) a deterministic parity rule as a non-positive control.

Definitions. The STATIC law of a rule on W: a probability law μ on M^W whose
full conditionals exist and equal the rule with all neighbours recorded,
μ(v_x = s | v_{W\x}) = r(s | v_{N(x)}), for every configuration and site. A
rule is "consistent" iff such μ exists. The FORMATION law for a formation
order σ (a total order on W, which the axioms do not supply):
μ_σ(v) = Π_k r(v_{x_k} | v restricted to N(x_k) ∩ {x_1..x_{k-1}}).

T1 (static law exists iff product form; the action). For a positive rule on
a finite graph: a static law exists iff the rule has product form with a
symmetric pair weight; then μ is unique, μ = Z^{-1} Π_x ψ(v_x) Π_{xy} φ(v_x,v_y),
and its finite-window action S_W = −Σ log ψ − Σ log φ is the object the rule
induces statically. Native proof: (⇐) direct; (⇒) Brook's lemma (uniqueness
and the ratio formula) + Möbius-inversion canonical potential + the Markov
property killing non-clique terms + triangle-freeness (cliques are vertices
and edges). Exact runner: full-conditional identity checked exhaustively on
the small windows; the sum rule's inconsistency by an EXACT Brook-cycle
certificate (a closed loop of single-site changes whose product of
conditional ratios is a rational function of λ not identically 1) plus the
exact compatibility-system rank on the 3-path; positivity necessity by a
finite witness (an eight-configuration Markov law on the 4-cycle with local
full conditionals and no pair factorisation — the classical example,
re-proved by a finite argument: every edge pair value occurs in a supported
configuration so all pair factors would be positive, contradicting the zeros).

T2 (the formation law versus the static law). For product rules under the
records-only extension (an unrecorded neighbour contributes no factor — a
NAMED premise, the natural reading of "only records are readable"):
μ_σ(v) = μ(v) · Z_W / Π_k Z_k(v_{A_k}), where Z_k(η) = Σ_s ψ(s) Π_{y∈A_k}
φ(s,η_y) is the local normaliser at site x_k given its recorded neighbours
A_k. Consequences, all exact: (a) on a transitive menu with isotropic φ the
ONE-neighbour normaliser is constant, so any order in which every site forms
with at most one recorded neighbour (a tree swept from a root) gives
μ_σ = μ exactly; (b) on any window containing a 4-cycle (every plaquette of
Z^3) every order has a site forming with ≥ 2 recorded neighbours, and the
two-neighbour normaliser Z(b,c) is constant on the menu iff p = q = r, i.e.
iff the rule does not vary with its neighbours — which Admissibility forbids
— so for every rule obeying the variation clause and every order,
μ_σ ≠ μ; (c) μ_σ depends on σ: exhibited exactly on the 4-cycle and 3-path;
(d) the identity Z_W = E_{μ_σ}[Π_k Z_k] (the partition function is the
formation-law expectation of the normaliser history). Layman's version: the
odds at a site depend on which neighbours have already formed, so the pattern
of records depends on the order they formed in; the order is physical, and
the formed pattern is not the equilibrium pattern the same rule defines.

T3 (naming the induced objects; remarks only, no fixture computed). The
static action S_W and the formation action S_W + Σ_k log Z_k(v_{A_k}) (an
order-dependent normaliser-history term). Remark on the gravity lane's
Gaussian Q: a quadratic pair weight is a Gaussian Markov field whose
precision is Q and whose pinned-record conditional marginals are
herm(Q_sub^{-1}) — the object the parked Bridge text calls W9 — i.e. static
conditional marginals, not the rule's formation conditionals; stated as a
remark with the 2026-08-26 gate cited by path as a fixture-level cousin,
NOT as an explanation of it.

Scope fences: finite windows and declared menus only; no infinite-volume
(DLR) existence/uniqueness claim; no selection of the physical rule; no
formation site/rate; no Born/bridge statement; no axiom or primitive change.
Claim type bounded_theorem, status bounded-support, trace class
upstream_support (consumer: the parked statistical-bridge decision's wake
condition "the committed-action identification lands", and the Born-form
lane's "uniqueness of the form from NN-determination + Record consistency").

Negative-shaped sentences ("μ_σ ≠ μ for every order") will be stated as
finite exact theorems on declared objects with the general-window statement
proved; the repo's N1-N8 no-go gate will be answered in the note with five
ATTEMPTED exact routes by which the two laws could still coincide: constant
rule (forbidden by the variation clause), non-constant site weight ψ (breaks
covariance on a transitive menu), absence-dependent extensions φ_abs (exact
test on the plaquette whether any such extension makes two orders coincide),
averaging over all formation orders (exact mixture vs static law on the
plaquette), and non-product rules (no static law exists to compare with).

## 4. Alternatives the panel should weigh against this block

(a) Continue the gravity mainline queue (certify overlap charpolys; a second
covariant witness; a principle for three signed sums) — incremental, owner
stopped the campaign after block 219 yesterday. (b) The U(1)/Maxwell light
lane's next item: the time-selection fork at the linear level (which finite
tick schedules preserve the Gauss rows and a positive modified energy). (c)
The record-matter lane's next item: derive a formation/renewal law from the
carrier. (d) A verbatim exact re-proof of R136 as stated (static reading
only). (e) Something else you would rank higher, stated concretely.

## 5. Deliverable (write ONLY to your named output file)

Sections, in this order, each short and concrete:
1. VERDICT on the proposed block (build as specified / build with changes /
   do not build), one paragraph.
2. STRONGEST ARGUMENT from your lens (what makes this right or wrong).
3. STEELMAN AGAINST your verdict.
4. WHAT EVIDENCE would change your mind.
5. CONCRETE DEFECTS: any false or unproven step in T1/T2/T3 as stated (be
   specific: which claim, why, and a counterexample or the missing lemma).
   If you checked something by computation, say what you ran and the result.
6. NEXT TEST: the single most decisive exact computation to include.
7. RANKING of this block against alternatives (a)-(e), one line each.

Facts only; no praise; no packaging. If you are unsure, say so.
