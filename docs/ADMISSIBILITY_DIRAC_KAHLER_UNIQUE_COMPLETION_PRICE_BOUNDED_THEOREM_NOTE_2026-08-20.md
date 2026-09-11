---
claim_id: admissibility_dirac_kahler_unique_completion_price_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "the supplied 8x4 antiperiodic-cover matrices, sixteen healed edge differentials, theta-prime formal half pairing, and explicitly stated completion spaces"
depends_on:
  - admissibility_dirac_kahler_bare_character_bounded_theorem_note_2026-08-20
runner: scripts/admissibility_dirac_kahler_unique_completion_price_2026_08_20.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A Support-Restricted Completion on the Supplied Finite Fixture

**Type:** `bounded_theorem`

**Campaign block:** 154. **Status:** corrected bounded theorem; formal audit is
deferred. Exact versions of the original note, primary, cache, ledger, and
generated manifest are preserved in the released-7315-A recovery packet.

The [primary](../scripts/admissibility_dirac_kahler_unique_completion_price_2026_08_20.py)
uses the corrected [Block 153 character](ADMISSIBILITY_DIRAC_KAHLER_BARE_CHARACTER_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the finite cover assembly from [Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). These citations identify
constructors and declared premises; they do not import the historical gates.

## The three blocks and the coefficient map

On the eight half-carrier slots, the staggered grading gives

\[
D=\{1,3,4,6\},\qquad L=\{0,2,5,7\}.
\]

For the displayed theta-prime pairing, the dead-dead and live-live blocks are
pure mass while the dead-live block is pure connection. The live-live block is
diagonal. A generic real antisymmetric, grading-odd 16-by-16 residue increment
has 64 coefficients. Its Hermitian theta-prime half block reaches all 32
oriented dead-live slots, and the resulting coefficient map onto the sixteen
independent dead-live targets has rank 16. This is a coefficient-map rank. An
invertible change of basis cannot change it.

The clean single-monomial form of the connection block occurs on the four
chart-0/1 edges. The other twelve edges contain larger carrier expressions.
That distinction is retained rather than promoted to an atlas-wide formula.

## Exact support-restricted completion

For each of the sixteen healed edge differentials, assign one real multiplier
to each nonzero hop and solve the identity

\[
\operatorname{Herm}[\theta' K(d+\Delta d)]_{++}|_{D\times L}=0
\]

in all 64 carrier moduli and the two connection symbols. The solve is feasible
on all sixteen edges. Six edge differentials have 32 hops and ten have 48.
Exactly 16 or 24 coefficients, respectively, are forced to \(-1\); the other
half are invisible free directions. Setting those free coefficients to zero
gives a selected minimal-support representative that deletes the forced hops.
It kills the complete theta-prime half block of the connection residue, not
only its dead-live part.

The support counts must be read as 16 deleted out of 32 atlas hops on the six
small edges and 24 out of 48 on the ten large edges. “16 of 32” is not an
atlas-wide count. The selected representative also loses antisymmetry: the
connection survives outside the half pairing, while the completed pairing has
no connection term.

The wider nearest-neighbor coefficient system is different from this
support-restricted system. At the probe edge it assigns two coefficients to
each of 128 ordered nearest-neighbor hops and has coefficient-map rank 104.
Restricting it to the 32 hops whose endpoint time residues cross
\(\{1,2\}\) or \(\{3,0\}\) has rank 32 and is infeasible at that probe. This
is a crossing-hop result, not a statement about every hop touching slices 3 or
4. Dropping one time slice at the same probe makes slices
\(0,4,5,6,7\) individually necessary; the per-slice statement is explicitly
a probe-edge certificate.

## Positivity and formal compression

Because the connection half block vanishes for the selected completion, its
Hermitian pairing is the mass Gram alone. For positive mass, positivity is a
codimension-two semialgebraic condition: the two hyperbolic dead blocks must
vanish and the four live diagonal entries must have the required signs. The
supplied exact escape carrier gives

\[
G'=\frac{15}{64}\operatorname{diag}(1,0,1,0,0,1,0,1),
\]

so the inertia is \((4,4,0)\). The flat carrier gives the zero Gram. This is a
finite carrier calculation and does not repair the flat-limit calibration
gap.

The historical map called `quotient` is the algebraic compression
\(q=\mathrm{SELECT}\,M\,\mathrm{LIFT}\). A genuine quotient descent also
requires

\[
M\,\mathrm{LIFT}=\mathrm{LIFT}\,q.
\]

The primary evaluates this residual separately. It therefore calls the former
map a *formal compression* unless the intertwining identity is proved for the
particular matrix. No physical quotient action or carrier-independent
congruence is inferred from the compression.

## Disposition

The finite character split, support-restricted deletion, probe crossing-hop
infeasibility, and exact mass-Gram witness are retained at their stated matrix
scope. Basis-dependent rank rhetoric, an overbroad seam class, atlas-wide
“16 of 32,” and automatic quotient/action language are withdrawn. No
completion or reflection is adopted as physical input.
