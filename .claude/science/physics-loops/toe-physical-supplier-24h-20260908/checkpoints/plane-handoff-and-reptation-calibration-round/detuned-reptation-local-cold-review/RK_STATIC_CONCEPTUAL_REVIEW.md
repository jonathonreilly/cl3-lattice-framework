# RK static support: concise conceptual review

Read complete native-rk-static-charge-support/DERIVATION.md, bound by SHA below. No conceptual blocker found. The source explicitly assumes J>=0,U>0,t=0, a finite connected even periodic cubic graph with extents>=4, all electric windings and the full ambient native cycle space with an imposed low-charge constraint.

After the phase-correct W dictionary, each alternating ring term is a graph edge Laplacian with eigenvalues0,2. In any nonempty fixed-charge component the uniform coordinate vector is a common null vector, including isolated frozen components; in native coordinates its conjugate d(x) phase is necessary and retained. No component connectivity beyond the selected component or uniqueness is asserted. Hence the sector minimum U sum q² is attained.

The missing-support obligation is actually closed: any ice orientation is balanced3-in/3-out; a source SCC in its condensation DAG has zero net degree and thus no outgoing edges, forcing a single SCC by underlying connectivity. A simple directed path from u to v therefore exists. Reversal changes path-directed E by minus1, yields Q_u=-1,Q_v=+1 and cancels at all internal vertices. Every prefix stays low-charge. This is a combinatorial existence construction, not evolution under t=0 or native hopping; changing the native number by two is stated.

Thus E_pair-E0=2U for every ordered distinct pair under unrestricted winding choice is justified. Prescribing an additional electric winding could obstruct the construction and is excluded. Neither a temporal Wilson potential, mobile-particle deconfinement, infinite-volume charged vector nor detuned continuation follows. The separation-normalized cost tends to zero only under the stated fixed-U sequence, a direct finite-sector consequence. Negative J is outside the positivity proof, and its local adverse example is not misrepresented as the full cubic negative-J ground calculation.

This is a conceptual source review using the already reviewed dictionary, not an independent execution of all author finite controls or a formal audit.

Reviewed proof SHA: 5f43318608efff7467ec97aaaa8dcd586f152d39c6b11b3543ad208f902483b9
