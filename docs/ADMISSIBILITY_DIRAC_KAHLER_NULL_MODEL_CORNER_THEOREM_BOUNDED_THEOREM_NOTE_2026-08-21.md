# Block 167 corrected bounded note: null-model corner identities

**Type:** `bounded_theorem`

**Primary runner:** [Corrected finite producer](../scripts/admissibility_dirac_kahler_null_model_corner_theorem_2026_08_21.py)

The finite fixture uses the local construction in [Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md), under the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). Only the specified constructor data is used; no broader parent conclusion is adopted.

Status: **corrected bounded source candidate**. Any producer output is separate provisional evidence that requires source-identity review and acceptance. This note replaces the historical universal exclusion with exact block algebra and two named finite fixtures. It adopts no premise, primitive, reflection class, or physical interpretation. Formal audit is deferred.

## Authority and objects

The authority surface is the four axioms in `docs/MINIMAL_AXIOMS_2026-06-29.md` and the three registered primitive nodes in `docs/audit/data/axiom_premise_nodes.json`. None supplies an Osterwalder-Schrader theorem, a Hilbert-space reconstruction, or a reference QCA. The QCA below is imposed for comparison and is not a framework object.

All inertia triples use `(n_positive, n_zero, n_negative)`. The corrected producer imports only the released-7315 C helper, whose sparse fixture is extracted from the frozen Block 165/166 constructor ASTs and whose local cell data comes from the accepted main A helper.

For a site-reflected two-slice restriction write

\[
 P=\begin{pmatrix}B&C\\ C^\dagger&0\end{pmatrix},\qquad B=B^\dagger.
\]

The correct hollow-block statement is

\[
 P\succeq0 \quad\Longleftrightarrow\quad C=0\ \text{and}\ B\succeq0.
\]

If `P` is positive semidefinite, `(0,y)^\dagger P(0,y)=0`. The Cauchy-Schwarz inequality for a positive semidefinite form then makes `(0,y)` orthogonal to every vector, so `Cy=0` for every `y`. Thus `C=0`; the remaining form is `B direct-sum 0`, which is positive semidefinite exactly when `B` is. The matrix with `B=-I` and `C=0` is the missing counterexample to the historical `P PSD iff C=0` wording.

## Decisive QCA counterexample

The imposed step uses Cayley transport and a mass coin. At `m=2` and `s_t=0`, the transport blocks are the identity while the coin is `-i sigma_x`. Hence the slice step `U` is unitary, invertible, and anti-Hermitian:

\[
 U^\dagger U=I,\qquad U^\dagger=-U,\qquad \operatorname{herm}(U)=0.
\]

The historical history constructor places `U` and `U^dagger` on adjacent directed links. Its actual reflected cross block is `C=herm(U)`, not `U`. Therefore `C=0` in this example. On the positive graded carrier, the mass diagonal `B` is positive. The reflected form is consequently `B direct-sum 0`, with inertia `(L_x,L_x,0)`, at both 8x4 and 12x4. The underlying history has nonzero temporal coupling and full-rank inter-slice transport. This is a positive-semidefinite history in the imposed comparison family and refutes the historical claim that real-time unitarity forces failure of this positivity test. No graph-connectivity property is asserted.

An anti-Hermitian cancellation family survives with the proper rank condition. For `V^dagger=-V`, `herm(V)=0`; full-rank inter-slice transport requires `V` to be invertible. The producer exhibits `iI` and `i diag(1,2,3,5)`. Zero and singular anti-Hermitian matrices belong to the cancellation locus but must not be described as full-rank transport witnesses.

## Retained finite measurements

The producer retains the original eight reference-QCA parameter points only as a finite unitarity/full-rank table. Their individual reflected inertias are printed; they do not support a universal exclusion after the `m=2,s_t=0` counterexample.

The named generator table is likewise finite. The hop-free generator `2J3` has cross-map rank zero and remains positive semidefinite at nonzero `s_t`. Conclusions about nonzero cross rank and failure of positivity are restricted to rows that actually carry temporal hops, at the two named carrier specializations. Symbolic and specialized rank counts are properties of those selected maps, not all numerical carriers.

The off-region control trace is recomputed from the outgoing action block and the two neighboring metric blocks. No value copied from the historical Block 166 control table is used as evidence for a different object.

## Disposition of the historical claim families

| Original group | Corrected disposition |
|---|---|
| A, authority and cache pins | Replaced by current literal authority/input hashes; historical cache remains archive-only. |
| B, convention and constructors | Retained with the explicit inertia order and AST provenance. |
| C, imposed-QCA contrast | Narrowed to the eight printed rows and refuted as a universal statement by the anti-Hermitian-unitary control. |
| D, site/link support dictionary | Preserved in the immutable original archive as historical and unreproduced. This reduced producer supplies no current acceptance of the support-dictionary family. |
| E, hollow-block lemma and cancellation | Corrected to require `B PSD`; rank-four language restricted to invertible `V`. |
| F, loophole census | Historical families preserved in the correction archive; no exhaustive classification lands here. |
| G, generator settlement | Retained as a named finite table; the hop-free row is stated explicitly and all-carrier language is removed. |
| H, result and closure prose | Rejected. No incompatibility, physical wall, all-carrier theorem, or TOE movement follows. |

The exact finite identities above do not establish an OS reconstruction, a physical transport interpretation, or a global no-go. Any corrected cache or manifest remains separate evidence subject to exact source binding, review, and acceptance.
