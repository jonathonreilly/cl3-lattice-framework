# Independent all-positive-coupling reflection analysis

Candidate verdict: the proposed reflection route works for the frozen bare-Haar cube-slab compression, provided all s,t>0. This derivation is scratch and awaits independent review. It does not change the source map or the frozen small-coupling result.

## Reinsertion and cut fixing are exact Haar changes of variables

Start with the original24spatial links on two slices. Reinsert an independent temporal link T_v at each of the eight spatial vertices. The temporal plaquette is the gauge-invariant four-link product, rather than the already gauge-fixed V_e U_e^-1. For each fixed T, transform only the upper-slice spatial links by endpoint multiplication with T_v and T_w^-1. Their product Haar measure is unchanged; spatial plaquette traces are unchanged by gauge covariance, and the lower-slice source trace is unchanged. The transformed temporal links are identity. The now-unused eight normalized Haar integrals are1, so the32-link gauge-invariant integral equals the original24-link temporal-gauge integral exactly. No orbit quotient, determinant or Gauss-law projection is inserted.

Reflect across the middle of the x direction. The eight x-directed links are a matching: each connects a different left vertex to a different right vertex. They are a forest, NOT a connected spanning tree. Fix the left endpoint gauge to identity and the right gauge to the matching-link value so that each matching link becomes identity. For each fixed set of matching values, the right-half y,z,time links undergo left/right Haar translations. The integrand is gauge invariant, including the source-loop trace. Thus the right-half variable change has Jacobian1, the matching variables disappear, and their eight Haar integrals give1. There is no need to fix a residual gauge or divide by a gauge volume.

The remaining graph is two independent12-link half-cubes with coordinates(y,z,time), sharing no variables. This proves the legality of changing from temporal gauge to cut-link gauge on this open temporal slab.

## Face counts, weights and source orientation

The full tesseract has24square faces. The two marked xy faces at z0, one per time, are stripped, leaving22. Internal half-cube faces are, per half, two yz spatial faces with weight w_(s/2), and four temporal faces(y-time and z-time) with weight w_t. There are12internal faces total.

Across the cut there would be12faces, one for each of the12half-cube links. Removing the two marked faces deletes precisely the cross terms for the bottom y links at z0, time0 and time1. The remaining10cross factors are six spatial factors w_(s/2)(R_e L_e^-1) and four temporal factors w_t(R_e L_e^-1). Their exact orientation may be inverted or conjugated without changing w because w is central and inversion symmetric. No spatial halfweight is accidentally doubled into w_s.

After cut links are identity, the input source holonomy is R_U L_U^-1, or its inverse according to the frozen loop orientation, where U is the bottom y link at time0. Hence its fundamental character is Tr(R_U L_U†)=sum_ij (R_U)_ij conjugate((L_U)_ij). This is the required complex Hilbert–Schmidt pairing, not a product of traces. Reversing the source replaces the pairing by its conjugate and will give the same real positive result.

## Reflection quadratic form

Let z denote the10coupled half-links and U,V the two uncoupled bottom y links at times0,1. Define the real positive internal halfweight
F(z,U,V)=product_(2spatial half-faces) w_(s/2) times product_(4temporal faces) w_t.
Both halves have exactly this same F. For each matrix slot set
G_ij(z)=integral F(z,U,V) U_ij dU dV.

The full unnormalized off-diagonal equals
sum_ij integral conjugate(G_ij(z_L)) [product_(10links) w_(b_e)(z_R,e z_L,e^-1)] G_ij(z_R) dz_L dz_R,
with b_e=s/2 on six links and t on four. The scalar kernel is real symmetric, so swapping L,R if needed identifies this exactly with sum_ij<G_ij,C G_ij>. All Haar integrations are finite and F bounded on a compact group product, so Fubini applies without qualifications. This equality is for the actual trivial/fundamental source entry, not a newly chosen test state.

Every w_b, b>0, has strictly positive coefficient in every SU(3) irrep: its representation-ring exponential has nonnegative multiplicities, and every(p,q) occurs in a tensor product of fundamental and dual fundamentals. Thus its central convolution has eigenvalue c_lambda(b)/d_lambda>0 on every Peter–Weyl matrix slot. The finite10-link tensor product C is positive and injective on L². No positive uniform spectral lower bound is asserted: eigenvalues can tend to0. Nevertheless <G,C G>>0 for every nonzero G, by its complete positive spectral expansion.

## The averaged half amplitude is not zero

Strictness is not inferred merely from reflection positivity. Evaluate G at z=identity. The two spatial half-faces give w_a(U)w_a(V), a=s/2. The bottom y-time face gives w_t(VU^-1); the other three internal temporal faces have identity holonomy and contribute e^(3t), because J(I)=1. Therefore

G(I)=e^(3t) integral U w_a(U)w_a(V)w_t(VU^-1) dU dV.

Simultaneous conjugation makes this matrix a scalar multiple of identity. Its trace is

e^(3t) integral chi3(U) w_a(U) [C_t w_a](U) dU.

The character coefficients of C_t w_a are c_lambda(t)c_lambda(a)/d_lambda, all nonnegative. Products of characters have nonnegative tensor multiplicities. In the trace integral, retain the trivial coefficient of C_t w_a and the dual-fundamental coefficient of w_a. This gives

Tr G(I)>=e^(3t)c0(t)c0(a)c3(a)>0.

Uniform convergence of the representation-ring expansions follows from their identity-value sums, so retaining this term is rigorous. Inversion of U or V yields the same result by dual symmetry. Since G is continuous in z, a nonzero matrix at identity is nonzero on a positive-Haar-measure neighborhood. At least one G_ij is a nonzero L² function. Injectivity of C then proves the off-diagonal is strictly positive for every s,t>0.

## Normalizations and scope

This is the unnormalized numerator defined by the frozen Wilson source compression. Dividing by c0(t)^12 or another positive partition scalar preserves strict positivity. Finite character-row division by a positive local diagonal also preserves the particular off-diagonal, but no bounded all-weight inverse is used. The result does not require gauge-noninvariant external states: the original source trace and all action factors are gauge invariant, and each gauge step was a Haar-preserving change of variables before integrating.

The conclusion is all positive couplings for this explicitly supplied finite bare-Haar source map, including isotropic s=t and the mathematical value6 if those parameters are substituted. It does NOT identify a framework-selected physical beta6 environment, a dressed-environment source map, an infinite-volume limit or a continuum theory. Such an identification remains a separate physical premise. The source character is not replaced by an arbitrary abstract D or a fitted reflection amplitude.
