# Strict cube-slab mixing for all positive couplings

This is a separate extension of the frozen actual two-slice cube model. Write a=s/2, w_b(G)=exp[b ReTr(G)/3], s,t>0. D03 denotes the UNNORMALIZED matrix element <χ0,I* Menv C_t Menv I χ3> from the existing source. The claim is D03>0 for every s,t>0, including s=t=6, for this precise finite open slab and constant-spectator Haar embedding. It does not identify that finite matrix element with a thermodynamic or dressed-source target.

## Gauge restoration and change of reflection plane

Restore one temporal link at each of the8spatial vertices. The resulting full open four-dimensional hypercube has16vertices and32links. Its24plaquette faces are weighted except the2marked xy faces at z=0, at the input and output times. Spatial faces carry a and temporal faces carry t. Sourceχ3 is the input marked loop; its action weight remains absent.

Integrate every link against normalized Haar. Gauge-transform the upper-time vertices, leaving lower-time vertices fixed, to set the8temporal links to identity. These links form a matching forest, so there is no periodic holonomy constraint. The remaining spatial variables change by left/right Haar translations with unit Jacobian, and every face weight and the source trace is gauge invariant. The8temporal Haar integrations contribute1. The integral is exactly the original temporal-gauge D03, not a new measure or transfer model.

Instead fix the8links parallel to spatial x to identity, by gauge-transforming the x=1vertices with x=0vertices fixed. These links are another matching forest. The same normalized-Haar argument is exact. Remaining variables form two identical12link halfcubes in(y,z,time), one at each x. Each half has six internal face factors: two yz spatial faces with a and four temporal faces with t. Let their common real positive product be M(H).

Every crossface with axes(x,j) reduces to H_j,right H_j,left^-1, up to inversion/conjugation which does not change w. There are12potential matching halfedges. The two missing source face weights remove exactly the crosscouplings on the yedges at z=0 at the two times. Of the10remaining crosscouplings, six carry a and four carry t. Thus their kernel is a tensor product of10actual central Wilson convolutions. There is no added coupling on an omitted face.

## Exact reflection quadratic form

Let U be the omitted yedge at input time and V the omitted yedge at output time within either halfcube. The source trace after x gaugefix is

Tr(U_right U_left^-1)=Σ_(i,j) (U_right)_(i,j) conjugate((U_left)_(i,j)).

The two half-actions are identical, since x reflection does not exchange space and time. Define F_ij(H)=M(H) U_ij. Let P integrate U and V against independent normalized Haar, leaving a function of the10coupled halfedges. Fubini's theorem (all functions continuous on compact groups) gives exactly

D03=Σ_(i,j) <P F_ij, C_cross P F_ij>,

where C_cross is the tensor product of six C_(w_a) and four C_(w_t). Depending on the initial source-loop orientation the displayed scalar is conjugated; the real positive quadratic form proves the same value. No factor1/3 appears in the character source: it is an unnormalized trace.

Each Wilson convolution has strictly positive Peter–Weyl eigenvalues c_lambda(b)/d_lambda for b>0. Strict coefficient positivity follows from the actual representation-ring expansion: every SU3 irrep occurs in a tensor product of fundamental and antifundamental representations, whose exponential coefficients are positive. Thus C_cross is a bounded positive injective operator. It need not have a positive uniform spectral lower bound. Nevertheless <f,C_cross f>>0 for every nonzero L² function f, by its full orthogonal Peter–Weyl expansion.

## Nonzero projected half-function

It remains essential to prove PF is nonzero; reflection positivity alone would only give nonnegativity. Set the10coupled halfedges to identity. Of the six half-faces, the two spatial ones reduce to w_a(U),w_a(V), one temporal face reduces to w_t(UV^-1), and the other three temporal faces give e^(3t). Hence

(PF_ij)(identity)=e^(3t)∫∫ U_ij w_a(U)w_a(V)w_t(UV^-1)dU dV.

The matrix integral is scalar by simultaneous conjugation. Let

I(a,t)=∫ χ3(U)w_a(U)(w_a*w_t)(U)dU.

Then (PF_ij)(identity)=δ_ij e^(3t) I(a,t)/3. Central convolution gives

(w_a*w_t)(U)=Σλ [c_lambda(a)c_lambda(t)/d_lambda]χ_lambda(U).

All coefficients are nonnegative. Expand the other w_a and use the nonnegative integer multiplicities in character products. The trivial convolution term and the antifundamental coefficient of w_a alone give

I(a,t)≥c0(a)c0(t)cbar3(a)>0.

Absolute uniform convergence is justified by Σλ d_lambda c_lambda(b)=e^b and standard character bounds; alternatively expand finite positive representation sums and pass to the uniform Wilson limit. Thus at least the diagonal PF_ii is nonzero at identity. PF_ii is continuous, so it remains nonzero on an open set of positive product Haar measure. It is genuinely nonzero in L², not merely at a measure-zero configuration.

Combining this with the strictly positive quadratic form proves D03>0 for ALL s,t>0.

## Normalization, controls and limits

Dividing the temporal kernel by c0(t)^12, or dividing the complete finite integral by any positive partition scalar, preserves strict nonzero mixing. The proof supplies no useful uniform numerical lower bound at6; injectivity is not a coercivity estimate. An algebraic finite-character residual obtained by left multiplying by a positive invertible diagonal also retains this off-diagonal entry.

The matching-forest gauges rely on open two-slice geometry. Periodic temporal boundary conditions would introduce a holonomy constraint and are not included. The five-face cap geometry is inherited from the previous construction; the new ingredient is reflection across spatial x and the strict projected-amplitude argument. The source map remains f↦f(Wbottom) with constant spectators, and no generic source embedding or physical infinite-volume environment is substituted.

At t=0 or s=0 the strict coefficient argument changes; the already proved t=0 positive-s result and untouched-edge vanishing families are separate controls. No claim of all-parameter positivity is made outside s,t>0. The existing small-coupling isotropic series remains an independent check, not an input to this proof.
