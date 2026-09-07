# Assembled full leading correction to the normalized native top eigenvalue

The heat input formerly left conditional in DERIVATION.md is now supplied by the separately derived orbital reflected-kernel lemma and its independent cold review in HEAT_LEMMA_REVIEW.md. The result remains conditional on the exact parent native recurrence/reflection identity and its established continuum Perron framework, not on an assumed full operator expansion.

Set h=beta^-1/2 and let A_beta=e^-beta beta^-3/2 T_beta be the exact normalized native packet. Let mu,phi be the top eigenpair of T0=S M_W S. Define d0=<phi,S M_(W2-3W)Sphi> as before. Then

    lambda_top(A_beta)=mu+beta^-1 c_full+o(beta^-1),
    c_full=d0+3mu+(mu/4)||Lphi||²,
    c_full/mu >=7/16.

No O(beta^-2) remainder or explicit onset follows from this proof.

## Proof through the positive weighted heat carrier

The exact shifted saddle has the same nonzero spectrum as

    e^(3h²) M_sqrtW exp[beta(J-I)] M_sqrtW.

On the lattice, let B_h sample the continuum kernel sqrtW(x)s_1^C(x,y)sqrtW(y) with the usual h² matrix-entry factor. Let C_h sample sqrtW(x)L_x²s_1^C(x,y)sqrtW(y)/4. The reviewed uniform18h4 reflected heat error and h²sumW<1 yield

    M_sqrtW exp[beta(J-I)]M_sqrtW=B_h+h²C_h+R_h,
    ||R_h||<=||R_h||HS<18h4.

The quadrature lemma in DERIVATION.md proves lambda_top(B_h)=mu+O(h4). Its proof applies Euler–Maclaurin to the smooth cubic-wall products, not to the nonsmooth bare vector sqrtW psi. It also establishes qualitative HS convergence of B_h to B=M_sqrtW e^L M_sqrtW, while C_h converges qualitatively in HS to C=M_sqrtW L²e^L M_sqrtW/4. The top branch remains uniformly isolated. Consequently the bounded simple-gap perturbation estimate gives

    lambda_top(B_h+h²C_h+R_h)
       =mu+h²<u,Cu>+o(h²),

where u=sqrtW Sphi/sqrtmu. The domain/smoothing calculation in DERIVATION.md gives <u,Cu>=mu||Lphi||²/4. Expanding only the scalar e^(3h²) adds3mu to the coefficient.

Independently, the already proved exact-native versus exact-discrete-saddle comparison gives their top-eigenvalue difference h²d0+o(h²). Adding the two differences proves the displayed c_full. This argument does not require a square-root expansion of the native multiplier or a convergence rate for the sampled correction C_h.

## Relative sign and retained limitations

Using the proved cone-dilation identity E_nuQ=3/2+kappa with kappa=-<phi,Lphi>,

    c_full/mu
      =[Var_nu(Q)+kappa²-4kappa+15/4+||Lphi||²]/4
      >=[2(kappa-1)²+7/4]/4 >=7/16.

The negative d0 from the earlier trace certificate is therefore compatible with a positive full coefficient: the exact discrete saddle has its own positive heat/scalar correction. These are different comparisons, not contradictory signs.

It follows that the exact normalized native top approaches mu from above eventually, but no explicit finite-beta threshold is extracted here. There is no individual excited-branch coefficient, ground/excited gap-ratio sign or physical mass-gap consequence. The parent step-function embedding still has its unavoidable Omega(h) projection error; no false operator-norm T0+h²T2 expansion is asserted. T2 remains a useful bounded quadratic-form expression for c_full, not an established expansion of that embedded operator family.
