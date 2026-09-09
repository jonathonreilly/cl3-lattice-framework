# Nonadjacent L6 sixth-order proper-prefix census

Status: exact geometry complete; gap scans unlaunched. The supplied full native U=0 dictionary and electric perturbation are the same as the adjacent calculation. No coefficient or gap positivity is asserted for the new masks.

## Insertion families, not arbitrary matchings

The electric perturbation contains pairs Z_e Z_f with distinct edges incident to one vertex, coefficient 1/2 in the dimensionless convention. Six insertions toggle at most twelve edges. For a nonadjacent target pair (0,w), its cut has twelve distinct edges. A sixth-order word ending at this cut must therefore use each cut edge exactly once: repeated edges, edges outside the cut and insertions involving fewer toggles cannot produce twelve odd edges in twelve available occurrences.

For representatives003,012,023,122,223, the two centers have odd distance at least three. Two cut edges from different stars cannot share a vertex: such a shared vertex would make the centers distance two. Within a star every pair is allowed. Thus each star's six edges must be partitioned into three pairs, giving15 perfect pairings per star and225 six-insertion sets per target. Every ordering is allowed as an operator word; whether its matrix element vanishes is left to the actual Gaussian calculation. There are225*720=162000 ordered words per target,810000 total. This derivation uses the actual perturbation's incident-edge rule; no arbitrary perfect matching import is made.

A proper prefix uses an even subset from each star. Each star has32 even subsets, so there are32^2-2=1022 proper edge-usage keys. Every such subset can be paired internally and completed, proving completeness in both directions. The DP state is its twelve-edge usage mask. Different pairings reaching the same key must have their vectors summed; their multiplicity must not be discarded. The resolvent depends only on that key's changed link mask. Final closure and spectator signs are not calculated by this census.

The literal geometry checker enumerates all pairings and every proper insertion subset. It stores all5110 keys and4986 distinct full648-bit masks. Overlap with the old adjacent certificate is31 masks, leaving4955 new masks; reuse is optional and would require exact source/certificate binding. Six distinct singleton-star masks occur across this census.

## Gauge cuts and parity

For each target, the exact216-vertex graph with both centers removed is connected (literal BFS certificate). If a cut has support inside the two stars, its vertex indicator must be constant on this connected complement. Up to complement its vertex set is therefore empty, either singleton center, or both centers. Empty and full target are endpoints, not proper prefixes. The only proper gauge cuts are consequently the two singleton stars.

Each singleton gauge changes active parity. Its proper resolvent in the fixed initial parity has gap2sqrt3, as in the canonical L6 dispersion; the zero unrestricted vacuum difference must not be used. All other proper masks require a genuine positive lower bound. Failure of the proposed Newton bound is to be retained as indeterminate, even though finite flux isolation gives qualitative strictness.

## Rank-four Woodbury certificate

Write K=2[[0,B],[-B^T,0]] with black center0 and white centerw. Every changed edge lies in the row of0 or column ofw. Since the centers are nonadjacent, their intersection entry vanishes. Put deltaB=e_0 z^T+u e_w^T=F G^T with F=[e_0,u], G=[z,e_w]. This is exact for every prefix, with rank at most two. Hence

    BB^T-A0 = U C U^T,
    U=[F,B0G], C=[[G^TG,I2],[I2,0]].

Only a4x4 rational inverse is needed, improving the adjacent external-bridge rank-six update. With R=(A0+25I/4)^(-1),

    Tr(A+25I/4)^(-1)
      = Tr R - Tr[(I4+C U^T R U)^(-1) C U^T R^2 U].

The inverse exists because A+25I/4 is positive definite; redundant update columns do not invalidate the identity. R is the exact degree-three interpolation polynomial on A0 eigenvalues3,6,9,12, with multiplicities32,48,24,4. Thus the unchanged baseline can be built once per process with exact integer/rational arithmetic. No new spectrum or floating diagonalization is required.

For c=5/2, the existing Newton majorant gives

    Tr sqrt(A) <= (648+108c^2)/(4c)+c[108-c^2 Tr(A+c^2 I)^(-1)].

Subtract this from72+40sqrt3+48sqrt6, using outward rational lower roots, to obtain an exact gap lower bound. Positivity must be tested on the Fraction itself. The update formula does not imply that all bounds will succeed. The active unaffected-vacuum offset is already included because the trace is the full108-dimensional bipartite problem.

## Controls and limits

The one geometry execution took0.12 external seconds and29,261,824bytes maximum RSS. RESULT's7320 'exact_checks' counts inspected pairing/key/connectivity objects plus grouped checks, not7320 separately raised assertions. All computations used standard-library integer/set operations. No spectral, LDL, gap or Gaussian residual calculation was run. The stored exact geometry is independent of author floating frame implementations. A future gap implementation must bind the prior baseline source and verify literal update and inverse residuals; that implementation is not yet provided here.
