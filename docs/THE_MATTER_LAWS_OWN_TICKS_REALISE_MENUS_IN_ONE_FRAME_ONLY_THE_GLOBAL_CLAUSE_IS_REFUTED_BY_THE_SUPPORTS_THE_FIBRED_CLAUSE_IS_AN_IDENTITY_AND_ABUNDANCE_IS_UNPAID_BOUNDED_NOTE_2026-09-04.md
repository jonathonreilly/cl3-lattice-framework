---
claim_id: matter_law_ticks_realise_menus_in_one_frame_only_abundance_unpaid_2026_09_04
claim_type: bounded_theorem
claim_scope: "Supplied finite static conditional Born record laws on the cube, slab and declared 4^3 torus families; exact supports, odds-vector classes and cross-state incidence systems. Full reduced-state grouping is a separate tolerance-tested calculation. A dynamic tick interpretation requires the stated eigenvector condition at every reached prefix, or zero dwell. Historical full-family quotations are unverified here."
upstream_dependencies: []
runner: scripts/matter_law_ticks_realise_menus_in_one_frame_only_check_2026_09_04.py
---

# Static conditional readout in one record frame and its finite menu systems

**Type:** bounded_theorem

Original date: 2026-09-04. Correction: 2026-09-09.
**Author status:** conditional finite support; no audit grade.
**Audit:** formal audit deferred by the owner.
[Primary runner](../scripts/matter_law_ticks_realise_menus_in_one_frame_only_check_2026_09_04.py) · [current cache](../logs/runner-cache/matter_law_ticks_realise_menus_in_one_frame_only_check_2026_09_04.txt)

```yaml
actual_current_surface_status: conditional-support
trace_class: frontier_discovery
artifact_role: theorem
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Supplied state and law

The finite graphs are the open 2x2x2 cube, open 2x2x3 slab and periodic 4^3 torus
with twist(1,1,1). Qubits live on their edges. The superfast Pauli encoding,
corner parity B_v=product of Z_e on star(v), n_v=(1-B_v)/2, pi-flux signs
eta_x=1, eta_y=(-1)^x, eta_z=(-1)^(x+y), Hamiltonian H=-sum eta_e T_e,
and half-filled code-space sea are supplied mathematics. The independent
record alphabet is the Z basis on every edge. None of these choices is a
physical carrier, vacuum or formation law derived from the minimal axioms.

Let A be the corner-edge incidence matrix over F2, g=|E|-rank(A), and
K the occupied one-particle spectral projector. The supplied static law is

    p(n)=det(diag(n)K+diag(1-n)(I-K)),  P(w)=2^-g p(Aw).

For unrecorded unit U, prior edge records(R0,w0), remaining edges
F=E minus(U union R0), n0=A_R0 w0 and L_F=image(A_F), define

    q_F(n)=sum_(l in L_F) p(n+l),
    p_U(w|w0)=q_F(n0+A_U w)/sum_(w') q_F(n0+A_U w').

Only positive-probability conditions enter. The runner enumerates coset
classes with their multiplicities using integer Walsh-Hadamard convolution;
Q(sqrt(m)) arithmetic and canonical integer keys distinguish exact odds.
Menu M is the support of this vector. Its possibilities are the rank-one
computational-basis projectors on C^(2^|U|). A proper support resolves P_M,
not the identity on the full unit. Coarse readings may sum those projectors,
but no additional coarse formation event is supplied.

For the specified conditioned sea sigma_U, Born conditioning gives exactly
p_U=diag(sigma_U) and M=support(diag(sigma_U)). At fixed U, equal **full**
states therefore give one menu. This is a property of the specified map;
an arbitrary law could give two menus to the same externally supplied label.
The identity does not derive Born weights from a clause about labels.

## Static law versus an iterated tick

Everything generally computed here is static conditional readout. Its value
also describes zero-dwell successive Born projections. With nonzero dwell
exp(-i tau H_R), a sufficient condition is that at **every reached prefix**
each nonzero projected sea branch is an H_R eigenvector. Each dwell then adds
only a branch phase, so induction recovers the static law. No necessity,
minimal-unit classification, or preservation for all schedules follows.
The class-prefix tables below count static conditions; a dynamic interpretation
must separately discharge this per-prefix condition. Larger tori supply closure
combinatorics only. This runner performs no dynamic evolution of those tori.

A small control explicitly separates the two readings: under H=X and tau=pi/4,
sigma=diag(1/4,3/4) changes its Z diagonal to(1/2,1/2), whereas an X-eigenstate
stays fixed. This supplied two-dimensional example is a boundary control, not
a surrogate execution of the cube's tick schedules. The current corrected
tick sources give sufficient prefix conditions and named finite schedules,
not an all-policy theorem; no result from them is imported as a premise here.

## Framework text boundary

These quotations from the current [minimal-axiom memo](MINIMAL_AXIOMS_2026-06-29.md)
constrain the physical interpretation, not the finite model's derivation:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.
> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.
> When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent.
> Only records are readable. A readout value is determined by record content alone.

No physical Record overwrite, clock, formation rate or iterated nearest-neighbour
probability law is established. The actual static global-conditioning contrast
below is a limitation of this supplied carrier, not a replacement axiom.

## T1 — The exact record laws

On the `2x2x2` cube `h^2 = 3I`, so `K = (I - h/sqrt3)/2` is exact in `Q(sqrt3)` and nearest-neighbour, with `K = K^T = K^2`, `tr K = 4` and `[h, K] =
0` exactly. The corner law has `62` nonzero patterns of `256`, all at `|n| = 4`, summing to `1`, **rational** with common denominator `D = 144` and
values `{1/144, 1/48, 1/36, 1/16}`; its eight cancellation zeros are exactly the eight closed corner stars `{v} u N(v)`. The record law `P(w) = 2^-5
p(A w)` has support `1984 = 32 x 62` on the `4096` labels and agrees with the many-body sea of the superfast encoding — code dimension `128`, `E = -4
sqrt3` — to `3.5e-18` in the original reproduced run; the current check requires deviation below `4e-18`.

On the `2x2x3` slab `spec(h^2) = {2,4}` and `K` is exact in `Q(sqrt2)`; the corner law has `804` nonzero patterns of `4096`, all at `|n| = 6`, `D =
8192`, `23` distinct values and `392` patterns with a `sqrt2` part, and the record law `P(w) = 2^-9 p(A w)` has support `411648 = 512 x 804`. On the
`4^3` torus in its supplied twist sector `(1,1,1)`, `h^2 = 6I` exactly, so `K = (I - h/sqrt6)/2` in `Q(sqrt6)` with `tr K = 32`.

> **`K_AA = K_BB = I/2` exactly on all three objects.** This holds because `sgn(h)` is off-diagonal in the sublattice decomposition when `h` is, and it
> is why the even corners' occupations are independent fair coins: the even-sublattice marginal is `2^-|A|` on every pattern. It is the hinge of Lemma
> 4, and it removes the matrix inversion from the torus computation, since a set `T` of formed even corners has `K_TT = I/2` and so `M_TT = I/2`.

## T2 — Single-site formation: one binary menu and two forced singletons

On the cube the census is complete: all `12` sites and all `3^11` conditions on the other eleven edges, `2105028` valid conditions in all, `12 / 264 /
2640 / 15840 / 63360 / 177408 / 354816 / 506880 / 506880 / 336384 / 122880 / 17664` by the number `k` of prior records. Over every site and every
condition there are exactly **three** menus — `{P0,P1}`, `{P0}`, `{P1}` — and **129** distinct odds vectors. No singleton menu occurs through `k = 7`;
the first forced record is at `k = 8`.

PR #7919's control reproduces exactly: nonzero record blocks `1 / 24 / 264 / 1760` at `k = 0..3`, the odds at a free edge `1/2` for `k <= 2` and the
five values `{5/18, 1/3, 1/2, 2/3, 13/18}` at `k = 3`, and its witness — records `0` on edges `0..6` and `8` lock edge `9` — giving support `{P1}` and
odds `[0, 1]`.

Two facts about this static conditional model follow. Nearest-neighbour records never move a site's odds off `1/2`: every condition whose records lie on the four edges
sharing a corner with the site gives the single odds vector `[1/2, 1/2]`, by particle-hole symmetry `p(n) = p(1-n)`, invariance of the record law
under a perfect matching, and `p(00) = p(11)` on an adjacent pair. Yet fixing the whole nearest-neighbour pattern and letting the far records vary,
**all `192` (site, NN pattern) pairs carry several odds values**, with spread `1` — the same NN pattern completes to conditions whose odds are
`[0,1]`, `[1,0]` and other attained intermediate values. These static conditional odds are a function of records at distance two and beyond, and are not a
nearest-neighbour function on the edge-site lattice at all.

On the slab, over all conditions with `k <= 4` at every site, all nearest-neighbour conditions and all whole-class conditions, there is one menu
`{P0,P1}` everywhere with `73` odds vectors and no forcing.

## T3: declared joint units and closure

Cube stars contain three edges and have an eight-label domain. Complete
enumeration of 3^9 conditions at all eight corners gives 69 menus and 1329
odds vectors. Sizes are{4:8,5:24,6:28,7:8,8:1};37 menus carry multiple odds,
with 849 vectors on the full basis. The size 4 menus form four complementary
pairs. Nearest-neighbour-only conditions give 5 menus, sizes{6:4,8:1}, and 27 odds.

The four even-corner units on the cube, over 24 orders, have per-prefix menu
counts 1/1/13/32, odds-vector counts 1/1/18/32 and uniform-vector counts 1/1/0/0.
For the declared slab even classes{4},{7},{0,2},{9,11}, use the union of each
class's stars as U. The column-pair unit has 421 menus and 423 odds vectors,
with sizes{19:32,25:32,31:192,32:96,44:16,56:36,60:16,64:1}; one vector is
uniform. The degree 4 star has 285 menus and 501 odds vectors, with
sizes{5:16,7:112,8:8,9:112,10:16,12:12,14:8,16:1}; one is uniform.
These are the class-prefix condition families, not all slab conditions.
Across 24 orders the slab counts are menus 2/2/166/960, odds 2/2/192/1152,
uniform 2/2/0/0. A class is a declared unit, not a proved globally minimal one.

On all 32 distinct(prior classes,next unit) steps for each cube and slab,
full uniform support is equivalent to closing no other-sublattice corner.
The tested alternative criterion, all unit columns lying in L_F, fails at
every step. K_AA=I/2 makes same-sublattice marginals uniform; when no other
corner closes, the only relevant parity marginal is that independent one.
Particle-hole symmetry and matching invariance are checked on cube/slab
(three/two matchings). On 6^3/8^3 the supplied classes have162/384 edges and
closure counts 0,0,27,108 /0,0,64,256. Those are combinatorics, without a new
state or nonzero-dwell execution. No all-unit/all-policy uniformity is inferred.

## T4: exact declared torus families

The unit is the six-edge star of v0=(0,0,0), with 64 labels. Let T be the
formed even corners and C the closed odd neighbours of v0. Each declared
T is contained in the 15 even second neighbours. K_TT=I/2, so on R={v0} union C
the conditioned kernel is K_RR-2 K_RT D K_TR, D_aa=+1 for occupied and-1
for empty formed corners. Every n_T and closure parity is enumerated in the
named family. Tj closes j indicated odd neighbours, with T their other neighbours.

| family | closes | condition classes | menus | sizes | odds vectors | full basis |
|---|---|---|---|---|---|---|
| T0: none | — | 1 | 1 | 64 | 1 (`1/64` each) | 1 |
| T1: `N(+x)` formed | 1 | 64 | 5 | 48, 64 | 12 | 1 |
| T2: `N(+x), N(-x)` | 2 | 2048 | 25 | 32, 48, 56, 64 | 200 | 1 |
| T2: `N(+x), N(+y)` | 2 | 2048 | 25 | 32, 48, 56, 64 | 200 | 1 |
| T3: `N(+x), N(+y), N(+z)` | 3 | 32768 | 141 | 20, 32, 40, 48, 56, 60, 64 | 4096 | 1 |
| T6 sub-family, exact | 6 | 312 | 193 | 7, 20, 23, 63 | 257, all rational | 0 |


T0–T3 retain their entire named families. T6 uses n_T of Hamming weight<=2
with closure parity 0, plus four named bit patterns (zero,all-one,alternating,
complementary alternating) at all 64 parities. This is 312 classes,193 menus,
257 rational odds vectors. No float-source comparison is executed or claimed.

## T5: three distinct questions

**Cross-state incidence system.** Stipulate one vector g over all unit labels
and require sum_(w in M)g_w=1 for every support across different conditioned
states. Exact integer elimination gives rank/augmented-rank:
site 2/3, cube star 8/9, slab pair 64/65, slab star 16/17;
torus T1 4/5, T2o8/9, T3 16/17, T6 64/65, pooled 353 menus 64/65.
Single-menu cases(T0 and binary site through k7) are consistent rank 1/1.
These are conditional linear-system results. Ordinary frame normalization
on complete identity resolutions does not require this cross-state system
on proper P_M resolutions, so its failure does not refute frame functions.

The displayed disjoint-menu proof is restricted to the cube: two actual
size 4 star menus partition its full basis, and all three supports occur.
The runner computes that witness from its actual menu set. It is not a universal
explanation of the other rank gaps. T1 has only 48/64-element menus, so pairs
intersect in at least 32 labels. Its actual four size 48 incidence rows sum to
three copies of the full-basis row: the imposed right sides would give 4=3.
The runner checks this actual dependency. T6 has no full-basis menu.
The other exact rank gaps are retained without inventing disjoint witnesses.

**Fixed prescribed sea versus Born form.** Uniform-on-support grades differ
from the specified nonuniform sea vector for 126/129 site odds classes,
1324/1329 star odds classes and 4765 distinct pooled torus odds classes.
They nonetheless are Born probabilities of the valid density P_M/|M|.
The runner checks this with an actually encountered nonuniform site odds
vector. Once the grade is required to equal diag(sigma_U), that prescribed
vector is fixed. A simplex of alternative supported grades of dimension|M|-1
exists only after dropping that equality. This is not a non-Born counterexample.

**Full states versus grouping keys.** At k<=4 the numerical cube control
has 9969 conditions,82116 condition-site pairs and 164232 scalar comparisons.
The key(site,rho00,rho11,abs(rho01)), rounded to 9 decimals, gives 172 groups;
omitting site gives 21. These keys discard the phase of rho01 and are not
full density equality. Complete fixed-unit conditioning gives 175419 conditions
at site 0 and 19619 at star(0), with 635/1499 rounded full reduced-state keys
respectively and 3/69 menus. No such full key has two menus. Full matrices
are rounded to 9 decimals; branches below 1e-14 are excluded and diagonal
magnitudes below 1e-13 are treated as zero. The exact analytic support-map
identity is separate from this tolerance-tested grouping. The diagonal/odds
numerical deviation is checked below 8e-15, not assumed exact from rounding.

**Effect census.** All computed possibilities are unscaled rank-one projectors
in one fixed record frame; supports cover the basis and each odds vector sums
to 1. The computed families have no size 3 menu. Minimum sizes are 4/19/5/7
for cube star/slab pair/slab star/T6 torus star. Binary site menus are
{P0},{P1},{P0,P1}; cube size 4 menus pair complementarily. These statements
refer to actual computed families, not quoted full censuses or arbitrary units.

## Historical quotations, unverified here

The original note quoted full slab-pair counts 11405 menus/95631 odds,
slab-star 1093/358125, and a full float T6 census of 2097152 classes,
2097088 valid,21656 menus,2093568 odds vectors, no full basis. It also
quoted 312/312 exact/float agreement to 3.9e-16, full-family multi-odds counts
5437/949 and maximum 266133, and 95630/95631 nonuniform pair odds.
Those source data are not input to this runner; **none of those quotations is
verified by the current execution**. The old mixed-parity torus row of 32
outcomes with values 5/192,7/192 likewise is historical only here. All exact
original text and caches remain recoverable in the archive. The text-only
quote gate checks disclosure, not any quoted number's scientific truth.

## Current conclusion and input closure

A fixed Z readout supplies one frame; it does not establish the full eligible
family needed for a frame-function theorem. The smaller homogeneous ternary
Born result additionally assumes scale homogeneity; neither that assumption
nor its full family is supplied by these supports. A second frame alone is
not a sufficient abundance theorem. Born probabilities are stipulated in this
model, not derived or disproved. Its physical carrier, law and clock remain open.

The runner retains all 54 original scientific predicates, with corrected labels,
and four explicitly text-only gates. It adds actual-support/state/dwell controls.
All scientific functions are inline. The runtime file inputs are this exact
note and the current minimal-axiom memo, both declared and hash-verified.
Sibling papers, historical code names and quotations are provenance, not inputs
or accepted suppliers. No physical or reserved supplier is consumed.
Independent audit remains required before any retained grade; the owner has
deferred formal audit. [Recovery and disposition](../archive/backlog/readout-7901-7969/HISTORY.md).
