# Independent cold review of fixed safe-cap finite-ladder proof

Read SAFE_CAP_FINITE_LADDER.md and UNIFORMIZATION_ERRATUM.md on2026-09-07. This is a proof review after my earlier arithmetic-only certificate review; the latter did not certify this argument. No repo edits.

## Verdict

No blocking defect found in the stated complete-law, fixed-initial-sector theorem. The48-storage-qubit conditional finite GKSL model description is justified with its declared apparatus and input restrictions. It is not a48-qubit simulation, nearest-neighbor implementation, or full physical realization. Two wording qualifications below would improve precision but do not invalidate the stated certificate.

## Proof checks

The norm bound ||A_s||<=24 gives initial total Q support[24,73] and subsequent battery support[0,97]. Endpoints are harmless for the continuum cap projection. Energy-intertwining accepted branches and free propagation preserve this support; exact refusal amplitude is zero. This is a support argument for the exact reference, not a claim that projected or approximate inputs inherit that support.

The full-line rounded TWO-sign column is an isometry on each eligible source block. Capping its output is a contraction, so the complement exists. On the ambient space it must be formed from E_e-S_e†S_e rather than I-S_e†S_e, as the memo explicitly says. Both exact and approximate completed columns have the same effect E_e, so their anticommutators cancel. The refusal copy carries the matched source energy. Using one complement per accepted sign-column is essential; independent complements per sign would change the law.

For the exact safe state, acceptance error and refusal norm are each bounded by alpha. The enlarged isometry-vector error is at most sqrt(2)alpha, and the density trace-norm estimate2sqrt(2)sqrt(p)alpha follows, also with a reference. Its use does not require the approximate flow to be safe. Summing over at mostD outgoing columns gives the stated2sqrt(2)Lambda coefficient.

The Duhamel orientation is correct: approximate propagation acts after the generator difference, while exact safe propagation acts before it. Only the exact reference Fourier marginal must translate. Cap compression of the approximate process therefore does not invalidate the Fourier second-moment estimate. The battery derivative norm pi/w gives the stated moment pi^2/w^2+t^2. The free Hamiltonians in this first comparison are identical.

The finite-cell step is ordered correctly. Integer shifts reduce the cell-constant subspace, and a cap made of whole cells commutes with its projection. Hence S†S and its square-root complement reduce that subspace too. Original matter A acts only on matter and preserves it. Replacing battery multiplication by centers first gives a bounded commutator perturbation of size at mostdelta in trace norm per unit time; only then is the normalized projected packet substituted. The Poincare estimate ||(I-P_delta)beta||<=delta/w and exact normalized-projection pure-state trace distance2||(I-P_delta)beta|| justify the2delta/w preparation cost. No false Q-safety assertion for that packet is needed.

The whole-cube rounded operator A_delta is a spectral function of A. Thus the ACTUAL free F=A+EB_delta commutes with conserved K=A_delta+EB_delta although it need not commute with individual rounded jumps. Capped integer shifts and matched refusal commute with K. Rounded-energy conservation and the bounded discrepancy from embedded original energy support the mean-error argument; the aligned packet has exactly matching mean by reflection symmetry, so the conservative quoted bound is safe. This reasoning cannot be transferred to a locally truncated A_R_delta with unchanged global free A.

The fixed-battery diamond statement is properly limited to arbitrary matter/reference input inside the prescribed legal initial source sector, or the stated classical mixtures satisfying the same support bound. It does not promote the proof to arbitrary coherent source-sector or arbitrary battery inputs.

## Uniformization erratum

The counterexample is correct: for the two-sector dephasing jump, adding the proposed null column doubles the off-diagonal damping. Scalar-rate uniformization is valid on the invariant source-block-diagonal class but not as a superoperator identity on arbitrary cross-sector coherences. The new safe-cap proof does not use that construction and carries an explicit restricted domain. I find no remaining dependence on the invalid identity in the reviewed new proof.

## Precision qualifications and storage interpretation

“Finite-dimensional GKSL” applies to the final cell-restricted model. The exact capped comparison space remains infinite dimensional in its battery coordinate, even though its Hamiltonian and GKSL generator are bounded. The proof does distinguish these stages; keep that distinction explicit when summarizing it.

The final unused1728 battery code states require an inert or otherwise specified trace-preserving extension if the advertised physical storage space is literally15 qubits rather than an abstract31040-level system. Such an extension exists and does not increase storage, but it is a supplied implementation convention. Similarly the one-head subspace and absorbing flag must use the stated invariant embedding.

The count12 native edge+12 fuel+8 physical one-hot head+15 battery+1 refusal=48 is consequently an honest conditional storage upper bound for the specified finite matrices, using the proved ambient erasure to avoid extra physical history memory. It excludes reservoir/ancilla, clock/control, preparation and jump-synthesis costs. The fixed-horizon collision construction adds its own ancilla inventory and approximation error; it is not contained in these48 qubits.
