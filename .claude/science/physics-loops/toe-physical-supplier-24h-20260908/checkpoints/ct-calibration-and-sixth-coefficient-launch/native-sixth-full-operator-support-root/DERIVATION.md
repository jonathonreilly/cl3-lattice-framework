# Sixth-order full-operator support: root extension in progress

Premises are the supplied uniform finiteL4 endpoint and its isolated single-flux full-rank active vacuum, plus the cut/spectator word selection already proved through five. This extension does not evaluate a coefficient or identify a phase. The checker is calculating one adjacent pair; that quantity alone must not be called the entire sixth-order spectator Hamiltonian.

## Cuts through twelve edges

For every nonempty proper vertex subset S of an even cubic torus with extents>=4, let m_a count mixed coordinate-a lines. If |delta S|<=12 then sum m_a<=6. No m_a is zero: descending to the other two-coordinate torus and lifting produces at least eight mixed lines, as in the earlier arbitrary-subset proof.

If some m_a=1, choose b with the largest of the other two counts, leaving m_c<=2. A nonconstant(a,c) slice perpendicular to b must contain a mixed a-line; otherwise c variation along all at least four a coordinates contradicts m_c<=2. Thus exactly one slice is nonconstant. All constant slices have the same value, else every b-line is mixed. The differing sites T in the exceptional slice have |T|=m_b<=4. S or its complement is T.

The only remaining positive integer triple with sum<=6 and no1 is(2,2,2). Choose any b. At most two perpendicular slices are nonconstant, since each uses a mixed a-line. At least two slices are constant; they share a value, else all b-lines would be mixed. At most m_b=2 b-lines contain sites different from that value, and each has at most two such sites, hence |T|<=4 again.

A three-vertex subset of the simple triangle-free cubic graph has at most two internal edges and boundary>=14. A four-vertex subset has at most four internal edges (triangle-free on four vertices) and boundary>=16. Therefore T has at most two vertices. The complete nontrivial cut classification through12 is singleton/complement (size6), adjacent pair/complement(size10), or nonadjacent pair/complement(size12).

## Consequence and missing supports

At sixth order the returning spectator operator can only be scalar or a bilinear, since odd singleton cuts vanish in the active vacuum and the even cuts are exactly vertex pairs. Adjacent pairs have ten boundary edges and two extra occurrences; their complete six-bridge support has been separately enumerated. Nonadjacent pairs have twelve boundary edges, each occurring once. Six allowed incident-pair insertions can always pair the six edges at each center into three pairs, so they are support-allowed too. Shared outer vertices may permit additional cross-pair matchings; these must be counted rather than silently omitted.

## Same-sublattice vanishing argument, awaiting independent review

In a bipartite active Fock representation choose black active Majoranas real and white active Majoranas purely imaginary. Every real-sign bipartite quadratic active Hamiltonian is then a real matrix, as are its resolvents and spectral projectors. The unique initial active vacuum can be chosen real. Electric-pair insertions change only link signs in an unreduced representative and carry real coefficients. Closing a pair cut introduces gamma_v gamma_w times the spectator product bar-gamma_v bar-gamma_w, up to the fixed real convention sign.

For v,w on the same sublattice the active closing product is real. Therefore its full perturbative coefficient multiplying the spectator product is real. But the spectator product is anti-Hermitian, and the canonical effective Hamiltonian is Hermitian. Distinct spectator bilinears are linearly independent on the allowed spectator-parity space for N=64. Hence that coefficient must also be purely imaginary, forcing it to vanish. Opposite-sublattice closing products are imaginary and have no such obstruction. This applies to the full coefficient after all ordered words/folded terms, not to individual paths.

This uses reality, parity and Hermiticity, not an assertion that each word is symmetric. Exact finite controls and independent review remain pending. The argument must retain the spectator basis convention and global parity restriction explicitly.

## Further connectedness conjecture, NOT proved here

For two separated star supports S_v={v and its neighbors}, let W_v=span{e_s,J e_s:s in S_v}, where J=K0/sqrt24. If graph distance(v,w)>3, then W_v and W_w are orthogonal: endpoint inner products vanish beyond distance2, and cross-J entries require an edge between the two stars, possible only through distance3. Their defect Hamiltonians therefore act on disjoint active Clifford factors. An exact linked-cluster/canonical factorization argument may force the cross spectator coefficient to vanish. This last inference has NOT been established, and no truncation to nearest/third neighbors is claimed.
