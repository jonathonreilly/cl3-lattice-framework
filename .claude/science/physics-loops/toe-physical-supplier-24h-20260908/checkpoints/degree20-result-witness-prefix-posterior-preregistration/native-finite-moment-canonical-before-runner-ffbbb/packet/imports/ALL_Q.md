# A rigorous all-q screening condition for the unchanged first polynomial

SOURCE ONLY. No accepted gate values or scalar inputs have been read/evaluated. This is a restriction of the reported e858 residual certificate, NOT a nonvanishing/no-go theorem about alpha.

Let x_A=R_A Omega and xhat_A=-p_A(D_A)Omega for the fixed first polynomials. Write a=||xhat|| in the15-fold direct sum. Let e_A bound ||x_A-xhat_A|| and E=||e||. Set delta=h/4, j=2sqrt2 h, X=sqrt15/delta, V=j sqrt15/delta²; then a<=X+E. The inner source is b_A=J_A p_A(D_A)Omega and satisfies ||b||=j a EXACTLY, since J_A*J_A=j²I for every pair.

For any proposed second polynomial, or indeed any domain vector vhat_A, let t_A bound ||b_A-D_A vhat_A|| and T=||t||. Gap coercivity and the triangle inequality give

 ||vhat|| <= (j a+T)/delta.

The nominal Ward number W=<xhat,T_KG xhat>-Re<xhat,T_KG g vhat>, where ||T_KG||=6, therefore obeys

 |W| <=6[a²(1+j/delta)+a T/delta].                              (1)

The unchanged e858 reported error uses F=||j e+t||/delta and

 Error=6[E(2X+E)+E V+(X+E)F].

All entries of e,t are nonnegative, so F>=T/delta. Put C=E(2X+E+V). Subtracting gives

 |W|-Error <=6[a²(1+j/delta)-C+(a-X-E)T/delta]
            <=6[a²(1+j/delta)-C].                              (2)

Consequently

 C >= a²(1+j/delta)                                             (3)

prevents either strict sign gate for EVERY second polynomial with the same first polynomial and the same residual error estimator. Equality also prevents the strict sign predicate. Increasing q from degree0 to1, or any larger degree, cannot fix this particular certificate if(3) is verified. Changing p or tightening the error estimator is a distinct route and is not ruled out. This says nothing about the true sign or size of alpha.

## Exact saved inputs for a bounded diagnostic

The completed degree10 event ledger already retained E and the class source norm intervals s0(P),s0(O). The source is b=J p(D)Omega, so

 a²=[12 s0(P)+3 s0(O)]/(8h²).

This identity needs no new moment or source-state approximation. A sufficient interval screening gate is

 E_lower(2X_lower+E_lower+V_lower)
 >= ([12 s0P_upper+3 s0O_upper]/(8h²))*(1+j_upper/delta).

It uses only directed roots of integer constants, rational arithmetic on three already retained intervals per mode, and exact fixed multiplicities. Original source/root acceptance and the exact event identities must be authenticated by a NEW bounded saved-metadata protocol before evaluation; merely reading an approximate printed E or nominal is not a certificate. No such evaluation has occurred in this source preparation.

The screen is one-sided: a failed inequality is inconclusive. It does not assert that the unchanged first-polynomial E term alone always prevents progress. It explicitly incorporates the maximal possible nominal benefit from the second polynomial and cancels its T-dependent contribution using the same gap and Kneser norm used in the error proof.
