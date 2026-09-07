# Exact first relative ground coefficient for the actual cube slab

This separate preregistered calculation keeps the actual 22 ordered Wilson face words, adapted literal-source tree and trace-orthonormal SU(3) convention. It imports the structural nonlinear Hilbert-Schmidt theorem and the two-source cubic-cancellation argument. No finite-beta onset or beta=6 accuracy is supplied.

## Analytic coefficient interface

Set epsilon=beta^-1/2 and expand the exact action and product Haar in the 136 adapted logarithm coordinates:

    beta E(epsilon z)=E2(z)+epsilon E3(z)+epsilon² E4(z)+O(epsilon³ |z|^5),
    product_e j(epsilon z_e)=j0^17[1-epsilon² sum_e Tr(z_e²)/4+O(epsilon³ P(|z|))].

Here E2=sum_color z_color^T H z_color/6. The Haar coefficient follows from the exponential Jacobian product over positive roots: log j(X)=-sum_positive_roots alpha(X)^2/12+O(|X|^4)=-Tr(X²)/4+O(|X|^4). The density correction before normalization is

    R(z)=E3(z)^2/2-E4(z)-sum_e Tr(z_e²)/4.

The weighted Taylor argument of the cubic-cancellation proof extends by one derivative: bounded action derivatives through order five and Haar/cutoff derivatives through order three give a polynomial-Gaussian bound on the third epsilon derivative. Thus the displayed second-order expansion has remainder O(epsilon³) in the weighted marginal L2 norm after nuisance integration. Compact chart complements remain exponentially small. The first-order marginal vanishes identically. The same expansion passes through the positive partition normalization and source square-root Jacobians. Therefore the common-space central kernel has K_beta=K0+beta^-1 K2+o(beta^-1) in Hilbert-Schmidt norm. This is not an expansion on the original undilated group space.

Let phi(X) be the normalized Gaussian ground state proportional to exp(-omega |X|²/2), omega=sqrt55/90. The simple isolated ground eigenvalue obeys

    beta^-4 lambda0(A_beta)=lambda0(K0)[1+k0/beta+o(beta^-1)].

Indeed standard elementary simple-eigenvalue perturbation applied to the norm expansion gives coefficient <phi,K2 phi>; corrections to the eigenvector contribute only at higher order. The off-chart full-operator remainder is exponentially small, so this is the actual slab eigenvalue, not only the chart compression.

## Gaussian expectations giving k0

For the partition, the per-color covariance is G0=3H^-1. In the ground matrix element, multiplication by phi(X)phi(Y) changes precision to H/3+omega P_source, so Gg is its inverse. The two source variables are literal distinct chords; no nonlinear source substitution occurs.

The normalized-kernel factor 1/sqrt(j(X)j(Y)) returns half of the source Haar correction. Since E Tr z_e²=8G_ee, define

    Z1 = E_G0[E3²/2-E4] - 2 Tr G0,
    Ng1 = E_Gg[E3²/2-E4] - 2 Tr Gg + Gg_uu+Gg_vv,
    k0 = Ng1-Z1.

The ground Gaussian integral's leading normalization cancels against lambda0. Thus these are normalized Gaussian expectations, not unnormalized insertions.

## Exact color and word contractions

For independent color-isotropic Gaussian edge variables,

    E Tr(Xa Xb Xc Xd)
      = (64/3)(Gab Gcd+Gad Gbc) - (8/3)Gac Gbd.

This follows from trace-orthonormal SU(3) completeness; the separate explicit eight-generator matrix check verifies all three contractions. Write [Ta,Tb]=i f'_abc Tc; then sum(f'_abc)^2=48 and Im Tr(Ta Tb Tc)=f'_abc/2. Expanding each original plaquette product through order three gives

    E3=sum_{u<v<w} C_uvw f'_abc z_u^a z_v^b z_w^c,

where each ordered three-factor choice contributes -weight times its orientation signs and sorting parity divided by6. Repeated-edge cubic terms vanish. Wick contraction, including all six cross-pairings and the vanishing within-triple contractions, gives

    E E3² = 48 sum_{I,J} C_I C_J det G[I,J].

Every fourth-order ordered word is retained with coefficient -weight/3 times its orientation sign product divided by the exponential factorials. In particular the calculation does not commute the face factors or replace the action by its Hessian.

The one-group Wilson control has G=3, E E4=-5 and Haar=-6, hence Z1=-(-5)-6=-1. The explicit generator matrix checks also verify an ordered noncommuting cubic and a cyclic four-factor cancellation.

## Frozen exact result

The actual adapted tree has 19 nonzero canonical cubic triples and 204 quartic ordered words. Exact rational arithmetic and a rank-two Woodbury update over Q(sqrt55) give

    Z1=1444313/38720,
    Ng1=1012365/23276 + (27961081/27931200)sqrt55,
    k0=126839623/20482880 + (27961081/27931200)sqrt55.

Both coefficients of k0 are positive, so k0>0 exactly. The approximate value13.6166025406 is a diagnostic only. The primary exact calculation's raw result retains every face word, orientation, weight, cubic/quartic coefficient and the separate E4, E3², Haar and source-half-back contributions. Six initial geometry/covariance/one-group checks and ten independent explicit color-matrix/Jacobian checks pass. This is not a fitted eigenvalue.

The value is provisional pending independent coefficient reproduction and cold review of the analytic interface. A positive asymptotic coefficient does not provide a finite-beta sign theorem at a specified beta, a spectral-ratio correction, physical coupling selection or a thermodynamic statement.
