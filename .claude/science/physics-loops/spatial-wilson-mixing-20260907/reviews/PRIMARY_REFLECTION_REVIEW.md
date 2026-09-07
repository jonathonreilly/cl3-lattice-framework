# Cold review: all-positive-coupling cube-slab reflection

Verdict: PASS for the precise finite bare-Haar source compression. I checked the two proposed derivations against the earlier spatial-wilson-seam PREREGISTRATION and DERIVATION, reconstructed the reflection geometry independently, and checked the strictness argument. This is a cold review, not authorship of either proposed proof. No repository files were changed.

## Exact model and Haar changes

The old operator is D=I* Menv C_t Menv I, with I f=f(W_bottom), C_t the product of twelve unnormalized link Wilson kernels, and Menv the five spatial face halfweights. Thus the matrix entry against trivial output and fundamental input is exactly the 24-spatial-link open-slab integral used in both proofs. The marked spatial weight is absent on BOTH slices. The source remains the trace of the input loop, with no factor 1/3.

For any fixed eight temporal links, endpoint translations of the upper spatial link variables set the temporal transport to identity. Product Haar is unchanged. Upper spatial loop traces are conjugated, and the lower source is untouched. More generally this works for both separately gauge-invariant boundary functions; it would not work for arbitrary gauge-noninvariant boundary states. Consequently inserting normalized temporal Haar integrations is an identity on the stated matrix element, not a Gauss-law projection. The open matching has no cycle or residual holonomy. The second gauge change, fixing the eight x links, is likewise an endpoint change of variables on the right half for each fixed matching-link configuration. No gauge-volume factor is introduced, and a residual gauge need not be fixed.

## Independent geometry count

I enumerated the 24 faces of the binary four-cube, with axes x,y,z,time, and removed exactly xy at z=0 on each time. The remaining cross-x faces consist of six spatial halfweights a=s/2 and four temporal weights t. Each x half has twelve links and six internal faces: two yz faces and four time-containing faces. The uncoupled halfedges are precisely y at z=0,time=0 and y at z=0,time=1. At all ten other halfedges equal to identity, the six internal face dependencies are U, V, (U,V), and three empty sets. This independently verifies the factor e^(3t) w_a(U) w_a(V) w_t(UV^-1). The exact enumeration is check.py/result.json here. No face is restored accidentally, and no halfweight is doubled.

## Pairing and positive operator

With cross links fixed, the source is Tr(R_U L_U^-1)=sum R_ij conjugate(L_ij), possibly conjugated by the original orientation. Since both internal weights are identical real functions, integrating the two uncoupled links leaves exactly sum_ij <G_ij,C_cross G_ij>. Centrality and inversion symmetry identify either orientation with the same real symmetric kernel. This requires matrix-entry pairing, not a product of two separate traces.

For b>0, expand exp[b(chi3+chibar3)/6] in tensor characters. Every coefficient is nonnegative. Every (p,q) occurs in a finite tensor product of 3 and bar3 (for example through its highest-weight component), so every coefficient is strictly positive. Central convolution has eigenvalue c_lambda(b)/d_lambda on the full matrix-coefficient sector. The finite ten-link tensor convolution is consequently positive and injective. Its quadratic form is strictly positive on every nonzero vector by the complete Peter-Weyl expansion, even though its eigenvalues have no uniform positive lower bound. Compactness/coercivity is not confused with injectivity.

## Strictness after partial Haar averaging

At the coupled identity configuration, simultaneous conjugation forces the projected matrix G(I) to be scalar. Its trace is e^(3t) times

    integral chi3(U) w_a(U) (w_a*w_t)(U) dU.

Convolution contributes coefficients c_lambda(a)c_lambda(t)/d_lambda. Character products have nonnegative integral multiplicities; retaining lambda=0 and the bar3 term of w_a gives the lower bound c0(a)c0(t)cbar3(a)>0. There is no unproved pointwise positivity of the trace integrand here: positivity is obtained after the representation expansion and Haar integration. Dual symmetry identifies cbar3 with c3 if that notation is used.

The expansion exchanges are justified: sum d_lambda c_lambda(b)=w_b(I)=e^b, obtainable by the positive representation-ring exponential itself; |chi_lambda|<=d_lambda gives absolute uniform convergence. Products and the convolution expansion are therefore integrable termwise. The nonzero identity value is promoted to a nonzero L2 function by continuity on the compact group product and full support of Haar measure. This closes the essential gap that mere reflection positivity would leave.

## Scope and conclusion

It follows that the original unnormalized D03 is strictly positive for every s,t>0, hence also at the mathematical substitution s=t=6. Positive temporal normalization c0(t)^12 or a positive scalar partition normalization cannot change this conclusion. No uniform quantitative lower bound at 6 is supplied. There is no change of I, environment dressing, thermodynamic limit, framework-selected physical coupling, periodic time closure, or universal statement over source maps. The boundary values s=0 or t=0 are not covered by the strict ten-link injectivity proof. I found no actionable mathematical correction in either reviewed version.
