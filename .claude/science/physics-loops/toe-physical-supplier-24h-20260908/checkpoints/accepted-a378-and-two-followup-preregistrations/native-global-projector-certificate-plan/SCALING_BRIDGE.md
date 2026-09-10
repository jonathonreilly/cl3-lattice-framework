# Exact source convention bridge: projector versus CAR action

Source-only matching of the actual displayed identities. Imported source: native-weighted-impurity-projector-stretch/DERIVATION.md and native-minimal-first-action-gram-stretch/DERIVATION.md. No numerical values are evaluated.

Let h=2|t_hop|, K_phys=h Kbar with real skew Kbar, and H_phys=iK_phys=h Hbar. The action proof explicitly uses h=1. Its selected signed neighbor vector d has normsqrt2. Define unnormalized U=[e0,d]. Then

 Delta K_phys=2h(e0 d^T-d e0^T),
 Delta H_phys=U (2ih [[0,1],[-1,0]]) U*.

This is exactly the projector source's V matrix in its unnormalized U convention. Replacing d by d/sqrt2 changes the coefficient matrix to2sqrt2 ih J2. Its operator norm is2sqrt2h and its trace norm is4sqrt2h, as used in the low/high proofs. There is no factor8 physical hopping: the action proof defines x0=e0/2 and q=d/2, so

 8[x0<q,f>-q<x0,f>]=2[e0<d,f>-d<e0,f>].

The literal8 is entirely the two half-column factors. Restoring h multiplies this action byh. The six absolute physical hoppings remainh after the link-sign flips, hence the common Schur bound6h.

For physical frequency z=i sigma h sbar and real source v,

 ybar_sigma(v)=-i (Hbar-i sigma sbar)^-1 v,
 Kbar ybar_sigma=sigma sbar ybar_sigma-v.

This matches the freepole action exactly. Physical -i(H_phys-z)^-1v equals ybar/h. A physical quadrature weight is h times its dimensionless weight and the Woodbury T matrix is h times its dimensionless value; the product w X T X* is dimensionless. Thus projector quadrature and its tails are scale-invariant after all factors are restored. If balanced columns are used, the balancing coefficient scales likeh² and cancels the h^-1 resolvent column. Do not transfer individual unbalanced coefficients without this accounting.

The reference covariance in the action source is Gamma0=i sign(Hbar). Therefore the projector represented there as(I+i Gamma0)/2 is the NEGATIVE projector. Our occupation proof uses positive P0,PA, for which P+=(I-i Gamma0)/2. Accordingly the actual negative-projector source candidate must be NEGATED before using it as Dhat for PA,+-P0,+. The range, singular values, S1 error and occupation trace bounds are unchanged; the finite coefficient matrix and low/high correction signs are not. A future binder must record this sign explicitly rather than infer it from a label.

For the low correction, physical F0=h^-1 Fbar0 and epsilon_phys=h*2^-Jlo, so epsilon_phys F0/pi=2^-Jlo Fbar0/pi. The positive-projector correction is +epsilon F0/pi; the low proof's displayed negative correction has the opposite sign. For the high correction each H^(2n+1)/S^(2n+1) is dimensionless, and the sign is again the chosen polarization sign.

Finally physical compressedH=h times the dimensionless compressedH, and physical leakage-square=h² times the action proof's L. A dimensionless target1e-12 corresponds to physical squared leakageh²*1e-12. Occupation-weighted propagation uses dimensionless time h*t_phys; an unlabelled time or squared residual cannot be mixed across these conventions. This source bridge supplies no new physical certificate or span containment.
