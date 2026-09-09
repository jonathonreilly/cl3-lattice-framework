---
claim_id: admissibility_dirac_kahler_cutting_strata_completion_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "Supplied corner-simplex dissections of one unit four-box with integer pair-count coordinates C4, TC and MC: seven explicit constructions, finite boundary trace catalogue, same-cost differences and counterexamples to two specific local arguments. Higher-stratum censuses, exact minima and physical interpretation remain unestablished by this package."
upstream_dependencies: []
runner: scripts/admissibility_dirac_kahler_cutting_strata_completion_2026_08_20.py
---

# Finite corner-simplex constructions and boundary traces

Type: bounded_theorem

Original date: 2026-08-20. Correction: 2026-09-09.
**Author status:** conditional finite mathematics; no audit grade.
[Primary runner](../scripts/admissibility_dirac_kahler_cutting_strata_completion_2026_08_20.py) · [current cache](../logs/runner-cache/admissibility_dirac_kahler_cutting_strata_completion_2026_08_20.txt) · [historical recovery](../archive/backlog/cutting-7028/HISTORY.md)

Can the supplied corner-simplex model realize the displayed charge pairs?
Yes: the seven explicit constructions below certify existence at their
listed costs. They give upper bounds on minimum cost. They do not prove
those upper bounds optimal. The corrected result also keeps a boundary-trace
theorem and two finite counterexamples, with their actual domains stated.

## 1. Supplied finite domain and coordinates

The box is [0,1]^4 with coordinates (x0,x1,x2,t). Corner k has the four binary
digits of k in that order, for 0<=k<16. A piece is the convex hull of five
corners whose 4-by-4 edge matrix has determinant +1 or -1. Its Euclidean
volume is 1/24. A dissection has 24 distinct such pieces, pairwise disjoint
interiors, and union equal to the box. Face-to-face compatibility is not
required: boundaries may carry incompatible subdivisions.

These are supplied combinatorial/geometric choices. The word “charge” below
means the specified integer pair count. It does not identify electric charge,
physical ticks, Records, momentum, a gravity action or a selected physical
cell. This note supplies no new framework axiom or primitive.

For a piece P, C4(P) counts unordered pairs of its vertices whose four-coordinate
Manhattan distance exceeds one. A boundary facet is x_i=s, i=0,1,2,3,
s=0,1. It contributes only when exactly four vertices of P lie in it.
On each contributing facet, count pairs whose distance in the spatial
coordinates other than the fixed coordinate exceeds one. The two t facets
contribute TC(P); the six spatial facets contribute MC(P). Add piece values
to obtain C4(D),TC(D),MC(D) for a dissection D. These definitions retain the
original runner's coordinates and ordering.

The finite enumeration of all 4,368 five-corner subsets gives determinant
absolute-value counts

| Absolute determinant | Number |
| --- | ---: |
| 0 | 1,360 |
| 1 | 2,672 |
| 2 | 320 |
| 3 | 16 |

Among the 2,672 allowed pieces, C4 takes values 6,7,8,9 with multiplicities
400,1216,864,192. Therefore every dissection in this domain has C4>=144.
This bound does not establish the minimum at any specified (TC,MC).

## 2. Seven explicit dissections, with existence bounds

The runner carries the exact original WITNESS and PARTNER tuples. Their
entries index the lexicographically ordered determinant-one five-corner
subsets defined above. Every row has 24 distinct allowed cells and 276/276
piece pairs certified by nonzero integer separating normals.

| Construction | C4 | TC | MC | Mathematical conclusion |
| --- | ---: | ---: | ---: | --- |
| Target (36,55) | 149 | 36 | 55 | Minimum at this pair is at most 149 |
| Target (41,53) | 156 | 41 | 53 | Minimum at this pair is at most 156 |
| Target (37,53) | 152 | 37 | 53 | Minimum at this pair is at most 152 |
| Target (41,48) | 163 | 41 | 48 | Minimum at this pair is at most 163 |
| Target (37,48) | 165 | 37 | 48 | Minimum at this pair is at most 165 |
| Partner at 156 | 156 | 36 | 60 | Same-cost comparison with (41,53) |
| Partner at 152 | 152 | 36 | 60 | Same-cost comparison with (37,53) |

**Why this is a geometric certificate.** For each pair A,B, the runner finds
n!=0 with max(n·A)<=min(n·B), or the reverse. The candidates are the 80
nonzero {-1,0,1}^4 normals and exact cofactor normals of simplex faces.
A successful separator proves their interiors disjoint. A failed search in
this candidate family would be inconclusive, not a proof of overlap.
Containment in the unit box and 24 volumes of 1/24 give total volume one.
The union of finitely many closed simplices is closed; any omitted interior
point would have an open neighborhood of positive missing volume, and the
boundary is in the closure of the interior. Thus the union equals the box.
An exact cover of finitely many generic sample points alone would not prove
this assertion. The corrected runner does not use a sample cover as its
sufficiency argument.

Subtracting the partners gives charge differences (5,-7) at cost 156 and
(1,-7) at cost 152; reversing the ordered comparison negates the difference.
These are pairs of whole dissections of equal cost. No bound on the number
of changed pieces, reversible local move, full frame-map antecedent, or
physical transition follows.

## 3. Boundary traces and finite facet catalogue

Every boundary facet of a dissection in this domain is partitioned into
six unimodular corner tetrahedra. To see this, intersect a four-simplex
with a supporting hyperplane of the box. A full-dimensional facet trace
has four corners in that hyperplane and the fifth corner at height one.
The determinant-one condition therefore gives normalized three-volume one,
or Euclidean volume 1/6, for that tetrahedron. Distinct traces cannot overlap
in their relative interiors: near an interior point of an overlap, both
incident four-simplices would contain overlapping thin inward neighborhoods.
The traces cover the boundary facet, and their volumes consequently force
six of them. Lower-dimensional intersections do not change this measure
argument.

The runner retains the original point-free enumeration on each three-cube
facet. It lists all determinant-one corner tetrahedra and enumerates their
six-member cliques of pairwise interior-disjoint tetrahedra. In three
dimensions the separating-axis test using face normals and cross-products
of edge directions decides convex-polytope separation; all comparisons here
are integer comparisons. Every six-clique fills its cube by the same
volume argument. The catalogue has 180 dissections on each of the eight
facets. The supplied facet costs have distributions

| Facet kind | Cost: multiplicity |
| --- | --- |
| t fixed | 18:16, 19:72, 20:84, 21:8 |
| spatial coordinate fixed | 8:12, 9:64, 10:104 |

There are 3,584 allowed-piece/boundary-facet incidences across all 2,672
pieces. The runner verifies each exhibited dissection's eight traces
against the catalogue and compares their summed costs to its direct
piece-charge computation.

The trace theorem and this finite catalogue imply the global necessary
bounds 36<=TC<=42 and 48<=MC<=60 for this supplied domain. They do not make
independently chosen facet dissections extendible to one bulk dissection.
They also do not impose agreement of the two boundary subdivisions on a
codimension-two square.

## 4. An explicit diagonal disagreement

The already certified cost 156 partner in section 2 supplies the original
counterexample's square x0=0,x1=1, with corner indices {4,5,6,7}.
Its trace from facet x0=0 has triangles {4,5,6} and {5,6,7}, meeting along
diagonal(5,6). Its trace from facet x1=1 has triangles {4,5,7} and {4,6,7},
meeting along diagonal(4,7). The runner derives these triangles from the
same full 24-piece witness; it does not assume the two-dimensional pieces
are themselves four-simplices.

Both facet traces and the bulk dissection are valid. Their incompatible
square diagonals refute the specific assertion that every such bulk
dissection has matching boundary-square diagonals. The original floor
corpus histogram and 86/91 constraint-satisfaction count are separate
historical assertions, not consequences of this one counterexample.

## 5. The proposed cost law and a local obstruction

Write delta=(TC-36)+(60-MC). The historical proposed inequality is
C4>=144+delta. The displayed target witnesses satisfy it; that finite
observation is not a proof for all dissections. In particular a witness
whose cost exceeds 144+delta does not disprove equality of the *minimum*
with that expression. Exact minima and the general law remain open here.

The direct uniform per-piece strategy would require C4(P)-TC(P)+MC(P)>=7,
since summing 24 such bounds gives C4-TC+MC>=168. The complete allowed-piece
enumeration instead has minimum 3 and distribution

| Value | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Multiplicity | 48 | 304 | 192 | 304 | 48 | 336 | 672 | 624 | 96 | 48 |

This refutes that uniform per-piece bound. It does not exclude compensated,
weighted, facet-coupled or other global arguments.

## 6. Existing constructions correct the novelty claim

The exact current cycle726 supplier already contains the following literal
witnesses, whose coordinates are parsed and rechecked by the corrected runner:

| Supplier key | C4 | TC | MC |
| --- | ---: | ---: | ---: |
| W1 | 165 | 37 | 48 |
| W3 | 168 | 39 | 49 |
| W4 | 168 | 42 | 60 |
| W5 | 159 | 36 | 55 |
| W6 | 169 | 41 | 48 |

Thus MC=48 was already witnessed, and TC=42 was already realized. The
original claim that these boundaries were unwitnessed/open was false for
the supplied corpus. The current target constructions improve the shown
cost at (36,55) from 159 to 149 and at (41,48) from 169 to 163. These are
comparisons with the specified supplier witnesses, not claims of global
novelty or optimality. A point realized at some cost is not thereby realized
at every cost.

## 7. Historical claims kept outside the active result

The [exact original note](../archive/backlog/cutting-7028/originals/docs/ADMISSIBILITY_DIRAC_KAHLER_CUTTING_STRATA_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md),
runner, cached output and ledger are preserved without edits. Their older
labels are historical assertions and confer no acceptance. Specifically:

- The original default-run budget0/1 counts, cost9 allocation test, complete
  15,800-member floor-corpus trace/histogram, and supplier comparison are
  historical executed reports; this corrected runner does not replay them.
- The budget2/stratum146 and budget3/stratum147 censuses and multiplicities,
  four-route and allocation narratives, higher-stratum geometric censuses,
  fifteen stratum148 witnesses, all five exact minima and lower exclusions,
  27-point law sweep, 86/91 constraint-satisfaction result, checker engines,
  timing and independence claims remain historical and unverified here.
  No genuine responsible search packet was recovered. Arithmetic agreement
  between literal tables is not exhaustive evidence.
- The historical “none excluded” language is retained only in that archive.
  The current positive conclusion is existence for the explicit witnesses.
  No universal cost-level existence or general minimum-cost law is asserted.

These dispositions preserve all original information and state which
claims remain unresolved. They do not substitute a shorter check for a
still-active exhaustive claim.

## 8. Reproduction and actual input boundary

Run `python3 scripts/admissibility_dirac_kahler_cutting_strata_completion_2026_08_20.py`
from a checkout containing this note and its declared supplier. The runner
hashes its own note and the exact current cycle726 source before using them.
It parses only that source's literal WIT dictionary with ast.literal_eval.
It imports no historical science module and executes no cycle726/cycle734
producer, b151/b152 loader, carrier helper, or old receipt gate. The note and
cycle726 source are the complete file-read inputs; standard-library code
and inline exact finite definitions perform the calculations. Its cache
binds the final runner and both declared inputs.

The original execution did consume a floating inverse/rotation construction
inside the cycle734 prefix before checking integer identities; its blanket
“no float constructed” statement was false. The corrected finite runner
uses integer determinants, cofactors and comparisons throughout, without
that prefix. The current cycle734 source remains unchanged on main. The
old cycle725 comparison receipt and b156 stack-parent hashes are not
inputs to the corrected result and supply it no authority. Reserved carrier
science under the other successor scopes remains excluded.

The declared final-run cap is 60 seconds and 2 GiB peak RSS. The actual stdout
and resource receipt report the run outcome; the note's formulas alone do
not certify execution. Formal audit is deferred.

## No-Go Discipline Gate

The two negative statements are narrow counterexamples, not broad no-go
claims. N1: the uniform per-piece bound 7 and mandatory square-diagonal
agreement are the two exact target statements. N2: their witnesses use the
same supplied domain as those statements. N3: the only extra choices are
explicit corner coordinates and pair-count rules. N4: general cost-law and
minimum questions remain open. N5: physical, exhaustive-search and local-move
conclusions are excluded. N6: compensated/global cost arguments and other
subdivision rules remain possible. N7: each positive finite dissection is
checked before it is used as a counterexample. N8: historical censuses and
previous favorable narratives are not reused as proof. This is a focused
scope disposition; it claims no exhaustive catalogue of alternative theories.
