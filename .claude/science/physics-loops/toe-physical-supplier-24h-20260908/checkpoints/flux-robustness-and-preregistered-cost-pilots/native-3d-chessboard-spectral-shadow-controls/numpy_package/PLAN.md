# Frozen spectral comparison design — UNLAUNCHED

This packet prepares the next calculation for the independently reviewed compatible-block dissemination theorem. No eigensolver, spectral integration or physical spectrum scan has run. The only execution is the integer geometry checker. The supplied model and the auxiliary objective identity remain premises.

## Exact Bloch matrix

Use a 4x4x4 cell, lexicographic sites r, and the frozen real link tiling from native-3d-chessboard-dissemination/DERIVATION.md (44877b2cd9733af18357c34ba4793453afe3bbecfb70083b9ca90320eaa3c6e7). INPUTS.json retains all 32 cube representatives and every directed Laurent term. Unit hopping is used throughout this design.

For a positive-axis bond from r to r+e_a, reduce the endpoint modulo four. Enter s_a(r) exp(i k_a) if r_a=3, and s_a(r) otherwise; enter its Hermitian conjugate in the reversed entry. This convention follows a Bloch function exp(i k dot cell_index). There are 192 undirected bonds and 384 distinct directed entries, including 96 directed wrapped entries. No seam multiplier is silently incorporated into the Bloch matrix: global twists belong in the allowed momenta.

The exact matrix is Hermitian for real k and anticommutes with the cell bipartite parity. At unit hopping Tr h(k)^2=384 for every k. With q_pi (representative15), h(0)^2=6I; changing the x Bloch phase to -1 destroys that identity. This is a sensitive normalization and seam control, not a floating eigenvalue fixture. Representative0 has every INTERNAL cube face +1 but retains canonical crossing faces; it is NOT the globally flux-free cubic hopping model.

For L_a=4M_a the finite allowed momenta are k_a=2pi(n_a+alpha_a)/M_a. A global seam multiplier zeta_a=exp(2pi i alpha_a) gives real straight winding (-1)^M_a zeta_a. Thus canonical real winding -1 requires zeta_a=(-1)^(M_a+1). The eight alternatives are all retained when minimizing finite comparison energies. Setting every alpha to zero independently of M would be wrong.

## Energy normalization

For unit hopping let angular brackets denote the normalized integral over [0,2pi)^3. Bipartite symmetry gives the filled negative-band auxiliary energy density

    e_aux(q) = - <Tr |h_q(k)|> / (2*64).

The physical native density is one half of this objective. To restore the native coupling multiply unit auxiliary densities by h0=2|g lambda| before taking that half. No physical observable identification follows from the equality of objectives.

If d_aux(q)=e_aux(q)-e_aux(q_pi), the thermodynamic candidate comparison number is

    delta_infty = min_{m(q)>0} 8 d_aux(q)/m(q).

This is the normalization in the dissemination theorem, since B=N/8. Its auxiliary defect inequality has coefficient delta/4 and native coefficient delta/8. None of these density differences or their signs have yet been computed. A finite-size/winding remainder is required in addition to positive limiting differences.

## Why six density classes suffice, and where they do not

Cube face labels have even numbers of + faces. Signed coordinate permutations act as arbitrary permutations of the three opposite-face pairs and independent swaps within each pair. The 32 labels form six orbits: m=0 (one); m=2 adjacent (twelve) or opposite (three); m=4 complementary adjacent (twelve) or complementary opposite (three); m=6 (one). The frozen representative IDs are15,3,5,1,10,0 respectively. This is an exact finite label classification.

Under a coordinate symmetry preserving the cube at {0,1}^3, the infinite disseminated face field maps to that of the transformed cube label: internal face positions reflect/permutate, and every crossing face remains -1. The two resulting period-four link fields therefore differ by a flat Z2 link ratio. On the period-four cell, a flat ratio is a site gauge times three seam signs. Thus the corresponding Bloch matrices are unitarily related after permuting/reversing momentum coordinates and possibly shifting some momenta by pi. The permutation can include cell-dependent phases from translated cell representatives; these are unitary and do not affect the spectrum. Normalized full-zone integration is invariant under all these changes. Hence the six classes give exactly six INFINITE-VOLUME density integrals, including the canonical baseline.

For fixed rectangular dimensions, an axis permutation also permutes the finite momentum grid. Do not use this as a six-class reduction on an unequal fixed rectangle without tracking that permutation. On a cubic torus, minimizing all eight seam twists is invariant and the six-class reduction applies. All 32 inputs remain frozen for independent checks and any later rectangular study.

## Prospective single cost pilot, not authorized to run yet

The pilot source evaluates all six fixed representatives at the same fixed 4x2x2 midpoint grid: 96 Hermitian64 eigvalsh calls. It retains the complete spectra, momenta, input hashes, timings and memory. It does not label the grid average a rigorous integral or a positivity certificate. No adaptivity, replacement grid or additional profile is allowed. Run only after root review/authorization and a remote checkpoint. The pilot requires an external wall watchdog at30seconds and a384MiB RSS guard; its internal30second alarm and reported RSS are secondary. A failure ends this contract rather than increasing it.

There is no measured cost forecast yet. The proposed30second ceiling is a prospective bounded measurement, not a claim it will pass. The later grid forecast will scale the actually measured per-matrix and setup costs, with explicit headroom, and requires a new contract. NumPy/interpreter hashes and version must be bound before launching; their availability/version has not been probed by a spectral call.

## Route to a certificate and a useful falsifier

Exploratory quadrature can reveal whether one of the five noncanonical density costs is small or negative and identify the hardest band geometry. It cannot prove all-positive costs. A rigorous fallback uses interval Hermitian spectral bounds at fixed cells plus an operator-norm variation bound. Each Bloch derivative is a signed boundary matching of norm one; hence ||h(k)-h(k0)|| <= sum_a |k_a-k0_a|. The trace absolute-value inequality gives an energy-density variation at most half this sum. On an n^3 midpoint partition this implies an individual density integration error <=3pi/(2n), and a two-density difference error <=3pi/n. This coarse bound is rigorous but may be computationally useless for a small cost; it is not a promised practical certificate.

A practical improvement would require analytic block reduction or higher-order certified quadrature away from explicitly controlled band zeros/crossings, with a separate bound on neighborhoods where those hypotheses fail. No smoothness of |h(k)| across zero modes is assumed. Finite-size sums and minimizing seam twists remain a further step. A vanishing or nonpositive certified limiting comparison would refute this proposed positive-density route, not the already established finite strictness or the supplied Hamiltonian.

## Runtime-binding completion (still no spectral execution)

The earlier source freeze939ac370 is preserved as BEFORE_RUNTIME_FREEZE.json, with the prior pilot and plan. RUNTIME.json now binds the actual Python3.12 interpreter, NumPy2.4.1 installed Python/extensions including linalg, imported file-backed modules and readable loaded non-system libraries. Its otool receipts identify the Accelerate linkage. macOS System/usr-lib images and shared-cache backend code are explicitly outside file-hash coverage; their names and the OS identity are recorded, not represented as hashed binaries. No eigvalsh was called during this census.

The pilot now verifies source/runtime bytes before the fixed calculation, inside its30second alarm. The root external watchdog remains REQUIRED: elapsed wall time at most30seconds and RSS at most384MiB, including verification/import/setup/output. Set OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS and VECLIB_MAXIMUM_THREADS all to1 before starting the interpreter. The validator requires those settings, the pinned interpreter and an absent output. No self-launch or authorization is included. The whole census is a deterministic environment read, not the requested cost pilot.

## Import-shadow repair, before any spectral data

The prior d73ba684 freeze and its pilot/validator/plan are preserved. Both pilot and validator now require Python -I. The validator rejects unlisted local executable modules and any local package directory; only ignored __pycache__ is allowed, which is outside the isolated import path. After importing NumPy the pilot checks its version, resolved origin and every loaded NumPy module against RUNTIME.json. A copied-package negative test adds an actual numpy.py and must fail membership before any eigensolver call. Root must launch the exact pinned interpreter with -I. This changes integrity guards only, not the96 matrices, grid or normalization.
