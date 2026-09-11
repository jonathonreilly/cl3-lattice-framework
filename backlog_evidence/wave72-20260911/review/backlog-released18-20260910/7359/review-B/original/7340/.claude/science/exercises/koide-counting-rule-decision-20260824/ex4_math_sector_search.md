# EX4 — Broad Mathematics Sector Search + Reframing (Koide counting-rule decision)

Date 2026-08-24. Max-reasoning exercise agent, read-only. Refresher read:
`docs/MINIMAL_AXIOMS_2026-06-29.md`; all four registered nodes in
`docs/audit/data/axiom_premise_nodes.json`; `CAMPAIGN_20260823_COMPLEX_
STRUCTURE.md` from THE FIBER THEOREM to end (seven corrections incl. C2
supplied-polarization, C3 grading-convention, C4 theta-closes-within-orbit;
orientation-bit run: joint flip X0 Q(+,+) X0 = Q(-,-) exact, single flips fail).

THE WALL, NEUTRAL. Two X0-exchanged theta-stable slot-orbits O_+ = {g_+, h_-},
O_- = {g_-, h_+} at the record-slice sector of the committed fixtures
(`build_fixture()` in `scripts/admissibility_dirac_kahler_embedding_residues_
campaign_close_2026_08_23.py`; sign variants in `scripts/admissibility_dirac_
kahler_sign_layer_comparison_2026_08_20.py`). Additive counting: two orbits =
two slots, r = 1, Q = 1. Quotient counting: orbit-pair quotient = one slot,
r = 1/2, Q = 2/3. No landed principle entails either; the orientation is
unregistrable in-class; the invariant physical datum is the triple sign
sigma*s_x*s_t (count-neutral).

## PART A — MATHEMATICS SECTOR SEARCH

### A1. Representation theory over R vs C (Wigner corepresentation types / Frobenius-Schur)
GROUP ENUMERATION FIRST (on the 4-dim orbit-pair space; all from landed data):
z = the chart translation generating Z_3 (unitary linear; omega on k=1, conj on
k=2 — `chart_translation()` in the campaign-close script); theta = the record-
slice reflection (linear, maps chart k=1 <-> k=2, theta-stable orbits, theta^2
to be computed); C = complex conjugation in the committed real basis (antilinear;
the fixture Q is real, so C is a POINT symmetry); X0 = (-1)^(t+x) (real unitary
involution; CLASS morphism only: X0 Q(+,+) X0 = Q(-,-)); plus any landed slice-
stabilizing lattice reflections. Two groups: G_pt (omits X0) and G_cl (adjoins X0).
OBJECT: the orbit pair as a corepresentation of G_pt and of G_cl (antiunitary
elements included). TOOL: Wigner corep types a/b/c = Frobenius-Schur machinery
over R; type decides mechanically whether the R-irreducible constituent is one
orbit (no doubling — additive count stands) or the pair (forced pairing — one slot).
FIRST ARTIFACT: exact sympy on `build_fixture()`: assemble {z, theta, C} (+ X0),
verify the multiplication table, compute the corep type of the pair under G_pt
and under G_cl. DECISIVE branch: C4 proved theta closes WITHIN each orbit, so
each orbit is separately self-conjugate — if the type computation makes the pair
a single R-irreducible ALREADY UNDER G_pt (no X0, no frame question touched),
quotient counting follows from committed point symmetry alone; if the pair is
G_cl-reducible, additive counting survives even the frame reading.

### A2. K-theory / index theory (mod-2 index, Pfaffian line)
OBJECT: the record-slice projector with the theta-odd (antisymmetric) part
a*s_x*J of the c-block Q_c = (43/35)(I + s_x J); candidate mod-2 datum =
sign(Pf) of the theta-odd block. TOOL: Pfaffian line / KR-index; a genuine index
must be invariant under the always-existing in-class relabeling group. FIRST
ARTIFACT: exact Pf at the four sign points (+-s_x, +-s_t) of the sign-layer
script, then the invariance sweep. EXPECTED: the only invariant is the known
triple sign sigma*s_x*s_t — a decisive NEGATIVE artifact: no mod-2 index pairs
the orbits, so the count is not index-shaped and index language cannot rescue
additive counting. SECONDARY DATUM: determine whether the arbiter's landed b179
one-slot cell computed a KU-rank (C-lines) or a KR-rank (R-forms) — a functor-
identification fact about an already-landed cell, sharpening C2 without new rules.

### A3. Equivariant structures (Z_2-equivariant object over the class)
OBJECT: the orbit pair as a Z_2-equivariant bundle over the two-point class base
{(+s_x,+s_t), (-s_x,-s_t)} with X0 the deck exchange (free on the pair). TOOL:
for a free action, equivariant K-theory = K-theory of the quotient — ranks halve
— and this is FORCED exactly when the physical algebra is the X0-invariant
subalgebra (superselection criterion), not a convention. FIRST ARTIFACT: the
OBSERVABLE-SEPARATION SWEEP — enumerate every landed readable functional on the
fixture (record-slice readout, W9 Gram data, Q spectral data) and test X0-
invariance exactly; X0 is site-diagonal, hence fixes the record-slice fiber
setwise, so the sweep is finite and exact. If NOTHING separates O_+ from O_-,
every readable functional factors through the quotient; if something does,
additive counting has named its reader and the wall breaks the other way.

### A4. Galois / descent theory (the pair as a conjugate pair over R)
OBJECT: the orbit pair as a Gal(C/R)-conjugate pair inside the complexified
sector, with candidate semilinear descent datum sigma = C o X0 (and variant
C o theta). TOOL: Galois descent + Hilbert 90: if sigma is antilinear, sigma^2 =
+1, and sigma commutes with the retained structure, an R-form exists and is
UNIQUE UP TO ISOMORPHISM — so quotient counting NEVER SELECTS AN ORBIT: the
counted object is the canonical descended R-form, and the "unregistrable
orientation" objection dissolves (there is nothing to register). sigma^2 = -1
instead gives a quaternionic form — a different, equally determinate count.
FIRST ARTIFACT: exact sympy — sigma^2 on the 4-space, commutation of sigma with
Q and W9 at the committed point; if descent holds, exhibit the R-form basis
explicitly. Reshapes the remainder-ledger premise from "select one orbit"
(unregistrable) to "count the canonical R-form" (choice-free).

### A5. von Neumann algebra type / Tomita theory (reflection as modular conjugation)
OBJECT: A_+ = the algebra generated by the committed observables restricted to
O_+, with candidate modular conjugation J = theta (or C o X0) and the record-
slice vector as candidate cyclic-separating vector. TOOL: Tomita: J M J = M' —
if the second orbit's algebra is the COMMUTANT of the first in standard form,
the doubling is GNS/thermal-double bookkeeping, and no vN counting ever counts
the commutant as independent modes. FIRST ARTIFACT: finite-dimensional exact
check X0 A_+ X0 =? (A_+)' on the 4-space and cyclicity/separation of the slice
vector (type I here, so the entire content is the standard-form identification —
a yes/no exact computation).

### A6. Sharper: Hermitian-form / Witt theory + the gauge-vs-global discriminator
(6a) OBJECT: the 4x4 W9 Gram matrix on {g_+, g_-, h_+, h_-} — W9 values are
ALREADY LANDED (fiber-scalar, organized by reflection orbits). TOOL: Witt
decomposition: if each orbit is W9-ISOTROPIC and the pairing couples only ACROSS
orbits, the pair is one hyperbolic cell — a lone orbit carries no norm, an
unnormable mode is not independently readable, ONE slot; if each orbit is
anisotropic (self-paired), each is separately readable, TWO slots. FIRST
ARTIFACT: the one Gram matrix, exact, from `build_fixture()` — the zero-pattern
alone decides which side the committed pairing supports. Sharpest single object
in this search. (6b) DISCRIMINATOR: gauge redundancy forces quotient in every
formalism; global symmetry forbids it (two degenerate species stay two — the
identical-particle caution against inferring halving from indistinguishability).
A global symmetry admits a committed readable order parameter separating the
class points; a redundancy cannot. Its first artifact IS the A3 sweep (convergence).

## PART B — REFRAMINGS ACROSS THE NAMED BOUNDARIES

(i) PRE-RECORD vs RECORDED: the count is being asserted of the pre-record mode
space, but the Record axiom makes only record content readable — if no
admissible record configuration locks orbit identity, r is a READOUT-side
quantity and the recorded world carries the quotient count whatever the
pre-record bookkeeping says; computable object: the A3 sweep restricted to
record-content functionals (does any lockable content differ between orbits).

(ii) SELECTOR vs DIAL: the orientation is a dial the physics never reads (C3:
it orders labels, supplies no projector), which dissolves quotient counting's
alleged need for a registration (A4: the descended object is choice-free) — but
unread-ness alone cannot kill the additive doublet (distinct-but-
indistinguishable is a consistent reading); the residue is exactly the
redundancy-vs-degeneracy question, whose computable object is 6b's order-
parameter search.

(iii) DYNAMICS vs KINEMATICS: kinematics provably cannot orient the pair, but
the Record axiom's own uniqueness clause — records form; A SITE NEVER CARRIES
MORE THAN ONE RECORD — is formation-side landed content: if both orbits' modes
are supported on the SAME record-slice sites, one-record-per-site caps what any
formed record can lock there, so record CAPACITY, not mode bookkeeping, may set
r, and EVERY formation dynamics inherits the cap (no downstream dynamics content
needed); computable object: the exact support/overlap table of the four
eigenlines against record-slice sites from `build_fixture()` — overlap opens the
capacity route, disjoint support closes it. The only route in this search that
could force the count from landed AXIOM content alone.

(iv) CENTRAL-SECTOR vs WITHIN-SECTOR: the chart decomposition (k=1 vs k=2) that
renders "two orbits" visible is itself supplied readout-context — central-sector
decomposition is explicitly downstream, NOT axiom content (minimal-axioms memo,
2026-06-05 relation) — so the wall may be a decomposition artifact: undecomposed,
the object is ONE real 4-dim block, and counting its R-irreducible constituents
requires no orientation; computable object: the real irreducible decomposition
under G_pt — the SAME artifact as A1 (independent motivation, convergent target).

## SYNTHESIS (one line each)
Sharpest sector object: A6a — the W9 Gram zero-pattern on the four eigenlines
(hyperbolic = one slot / anisotropic = two), already-landed structure, one exact
matrix. Sharpest reframing: B(iii) — record-uniqueness capacity, the only
axiom-content route to a forced count; its support table shares fixtures with
A6a and both feed the A1 corep-type computation (three artifacts, one script).
