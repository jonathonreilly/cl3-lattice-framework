# Conditional spectator spectrum cold review

PASS for the stated conditional finite-volume conclusion. Complete DERIVATION.md and EXACT_LEVELS.json read; exact hashes are in READ_HASHES.json. Also read complete magnetic-symmetry and full-operator-support root derivations to identify the imported scope. This review does not independently rerun their signed-orbit certificate or promote its coefficient hypothesis into a calculated result.

The normalization is correct: Q=sum b_ij i beta_i beta_j has standard skew matrix 2b. With b=(-c/2)K0 the matrix is -cK0, so each excitation frequency is |c|sqrt24, not half that value. The physical total parity is active chirality times spectator chirality for 64 matter modes. Using the same orthogonal frame matters: each chirality acquires the same determinant. Reversing all 32 occupations for the opposite sign of c preserves chirality. Thus the unconstrained spectator vacuum is physically allowed for either nonzero sign, and the first allowed excitation has two occupations. Exact leading multiplicities sum to 2^31, with unique ground and gap 2|c|sqrt24.

Independent check.py derives the Clifford reordering with literal bit operators on a four-mode analogue, checks the 64-mode phase factors, and computes the exact 32-mode even-occupation levels (31 predicates). It does not call author functions or evaluate c.

The finite-u inference is sound: the canonical isolated-cluster effective matrix is analytic; subtracting its scalar Taylor polynomial through degree six and dividing by u^6 leaves Q+O(u). Weyl's norm estimate preserves its simple bottom for sufficiently small nonzero real u. Other clusters remain separated by the original finite gap. This proves a unique full ground and gap 2|c|sqrt24 u^6+O(|u|^7), conditional on nonzero c and the imported full coefficient reduction. It supplies no numerical radius. Excited binomial multiplicities apply only to the leading coefficient. In particular, an adjacent coefficient alone cannot establish this spectrum without the additional full-operator/magnetic-symmetry premises.

No blocker or source correction requested. No numerical production or CT data were read.
