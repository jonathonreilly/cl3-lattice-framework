# Prospective actual R1 matrix witness

Before execution, fix the full Peter–Weyl R1 basis [1, sqrt3 U_kl, sqrt3 conjugate U_kl], dimension19, and the color basis dimension3. The57-dimensional multiplication compression is constructed from exact Haar coefficients:
U_ij 1 -> F_ij/sqrt3;
U_ij F_kl -> (1/2)Σ_ab epsilon_aik epsilon_bjl A_ab;
U_ij A_kl -> delta_ik delta_jl/sqrt3 times vacuum.
These coefficients are analytic Haar inputs, not conclusions from matrix arithmetic. Independently derive literal U_R*U_R, its defect, and the Cartan covariance for T=diag(1,-1,0), Qvac=0,QF_kl=-Tkk,QA_kl=Tkk.

Prospective checks: exact covariance; contraction via idempotent Gram; rank/traceGram15 and defect42; shell support annihilates vacuum-color3; highest-weight F11 tensor e1 kernel; defectnorm1; exact interior isometry; trace-square obstruction offset38; R0 zero transporter. Reverse the covariance sign as adverse. Using identity as fake finiteunitary fails covariance. Resource180s/180MiB, oneBLASthread, no numerical eigenspectrum or imported-theorem claim. Preserve every failed run; no parameter changes.
