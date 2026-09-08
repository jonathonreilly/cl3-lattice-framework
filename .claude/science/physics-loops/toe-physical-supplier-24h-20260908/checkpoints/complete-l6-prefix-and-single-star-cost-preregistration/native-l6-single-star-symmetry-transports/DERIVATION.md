# L6 signed magnetic transports for one-star sources

The construction uses the actual canonical K and42-dimensional W basis frozen by the one-star design. No spectral or resolvent evaluation is performed. All48 signed coordinate permutations fix the center. For a coordinate map phi, solve s0=1 and s_j=s_i K_phi(i),phi(j)/K_i,j along the graph. The exact cycle checks in the control establish consistency for every edge of this finite L6 carrier. Thus T e_i=s_i e_phi(i) is orthogonal and TK=KT; it fixes gamma0. The edge masks transform by the actual site map, including seams. This is a signed magnetic symmetry, not an unsigned coordinate permutation.

The full graph is connected, so the gauge with s0=1 is unique. Consequently these normalized maps compose as a group, rather than up to a residual global minus sign. W is the minimal K-invariant space containing the seven star endpoints. T permutes those endpoints and commutes with K, hence maps W onto itself. The helper independently verifies exact projection containment of all42 basis columns for every symmetry, and records their rational coordinates.

Let r_j,Kr_j be the stored orthogonal paired basis, with K²r_j=-lambda_j r_j and norm d_j. Define the positive-energy complex structure J=K/sqrt(-K²). Since T commutes with K, it commutes with J and mixes no annihilators with creators. In the design's nonnormalized convention b_j=[gamma(r_j)-i gamma(Kr_j)/sqrt(lambda_j)]/2, expand

T r_j = sum_i (a_ij r_i + b_ij Kr_i).

Only equal-lambda terms occur. The induced annihilator map is b_j -> sum_i (a_ij+i sqrt(lambda_j)b_ij)b_i. These coefficients are read directly from the recorded even/odd real basis rows. The d-weighted CAR metric is preserved. Normalizing by sqrt(d_i) yields an ordinary unitary matrix. It is not necessary to introduce a full Fock vector to define its exterior-power action.

Choose its number-preserving second quantization Gamma(T) with Gamma(T)|Omega>=|Omega>. This explicitly fixes the otherwise arbitrary implementing phase; it is a genuine representation and preserves parity. Any physical implementer differing by a scalar phase represents the same CAR automorphism; using the vacuum-fixed convention prevents that phase from corrupting transported source vectors. No claim that a supplied native pulse prepares these transformations is made: they are exact computational symmetry identities.

If T sends the pair mask A0 to A, then H_A=Gamma(T) H_A0 Gamma(T)†, and the same energy reference E0 is unchanged. Therefore for either consistent resolvent sign convention,

R_A(E0)|Omega> = Gamma(T) R_A0(E0)|Omega>.

The15 pair masks have precisely two orbits:12 perpendicular and3 opposite. TRANSPORTS records a chosen symmetry from each representative to every target. Thus two exact first-source vectors suffice to reconstruct all15, provided their actual exterior-power transports are applied; they are not identical coordinate vectors. For approximate first-source vectors, unitary transport preserves each residual/norm error.

For each last pair C the odd source is gamma0 sum_(A disjoint C) Gamma(T_A)x_rep(A). There are exactly six predecessors, listed explicitly for all15 C, hence90 terms in total. Since gamma0 is fixed, the same symmetry can also reduce complete second-source sums to the two last-pair orbit representatives: the stabilizer merely permutes the six predecessors. That optional reduction still requires the complete transported sum and an odd resolvent; it is not a numerical cancellation or proof of vacuum linearity. A later solver must retain CAR exterior signs and the vacuum-fixed phase.

The finite exact geometry controls prove this particular L6 symmetry/containment ledger, not a spectral assertion. The42 real modes have unequal frequencies, so no L4 flat-frequency simplification is used. No spectrum, physical inverse, Gaussian overlap, or full-state evaluation was run.
