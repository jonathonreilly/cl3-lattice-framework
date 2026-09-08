# Exact L4 vacuum vertex and a nonlinear-operator witness

Post-data analytical derivation, pending cold review. The observed exact chi_0=315/64 times the first odd coordinate motivated this simplification; this is not a preregistered prediction. No new physical resolvent or operator-basis solve was performed. All coefficients below follow from two-by-two analytical algebra on the actual one-star L4 invariant space. Unit |t|=1 unless restored through omega=sqrt24|t|.

## Paired star frame

The six white neighbors of black vertex0 span an orthonormal white space. Pair it through J=K0/omega with a black space. Absorb the six canonical link signs into the neighbor vectors, and choose paired active Majoranas a_j,b_j so H0,W=(i omega/2)sum a_j b_j. Then f_j=(a_j+i b_j)/2 has the empty vacuum. The center Majorana is a_u with u=(1,...,1)/sqrt6. Reversing a two-edge subset A changes the black-to-white matrix by -2omega u v_A^T, where v_A is u restricted to the two coordinates in A. Consequently c=u dot v_A=1/3, ||v_A||²=1/3, and v_A=c u+s w_A with s=sqrt2/3 and w_A unit perpendicular to u.

The four orthogonal modes remain unexcited during a single pair-defect inverse from vacuum. Subtract E0,W=-3omega. On its even two-mode basis(|vac>,f_u† f_w†|vac>), the dimensionless denominator is

    M_even=[[c,s],[s,2-c]].

On the odd basis(f_u†|vac>,f_w†|vac>) it is

    M_odd=[[1-c,-s],[-s,1+c]].

These signs follow directly from -i a_u b_v: it creates the ordered u,w pair with coefficient+s and exchanges the one-particle states with coefficient-s. Thus they retain the native CAR sign, rather than replacing a link operation by an unsigned bit flip. The reduced bath offset is included in E0,W.

## Grouping proves cancellation before taking a norm

The first positive denominator inverse is

    (H_A-E0)^(-1)|vac> = (1/omega)[5|vac>-3 f_u† f_vA†|vac>].

For a fixed last pair C, there are six disjoint first pairs A, and sum_A v_A=3(u-v_C). Therefore their sum is

    (1/omega)[30|vac>+9 f_u† f_vC†|vac>].

Applying gamma_0=a_u gives (1/omega)(27u+9v_C) as a one-particle vector. Applying the second inverse using M_odd gives exactly

    (1/omega²)(45u+54v_C).

In particular each grouped last-pair term already has no three- or five-particle component. Summing all15 C uses sum_C v_C=5u, giving945u/omega². The vertex's electric factor1/8 yields

    chi_0 = [945/(8omega²)] gamma_0|Omega>
          = +(315/64) gamma_0|Omega>   at |t|=1.

The sign is positive: the two negative Feshbach resolvents cancel. The actual saved grouped vectors independently agree: every grouped gamma-coordinate is63/4 in the rational A^-1 normalization, and all their higher-particle coordinates vanish. Those saved-vector observations are corroboration, not the derivation.

There is also a symmetry explanation. Permuting the six paired modes preserves H0, gamma_0 and the complete family of15 pair defects. The vacuum is invariant. The only invariant odd vector in the exterior algebra of the six-dimensional permutation representation is its one-particle uniform vector; exterior powers3 and5 contain no trivial S6 representation. The explicit two-mode calculation above establishes the cancellation without importing that representation-theoretic fact.

## Singleton-middle sixth coefficient

Magnetic covariance gives the same alpha=315/64 at every vertex. The singleton vertex is -i alpha sum gamma_v beta_v. On the one-particle active space the reduced inverse is -1/omega, and <gamma_v gamma_w>=delta_vw+i K_vw/omega. Thus the two ordered cross terms produce spectator coefficient

    b_vw(singleton)=-2 alpha² K_vw/omega²

in front of i beta_v beta_w for v<w. With K_0,16=-2 and omega²=24,

    b_0,16(singleton)=33075/8192.

This is approximately4.03748, whereas the complete separately certified coefficient is in[370.7628915198,370.7628915199]. The difference belongs to the mixed-middle contribution under the already reviewed nonscalar raw-chain/folded analysis. The vertex does not reproduce the full result. For each fixed pair set the72 singleton-middle orders are only part of720; the648 mixed orders are not optional. The scalar diagonal contribution is separate and is not being identified with the full sixth scalar energy.

## Analytic test of the full operator: it is not linear

A full32-column physical solve is unnecessary to find an operator-level falsifier. Introduce a spectral shift x through denominators M_even+xI and M_odd+xI. Repeating the same two-mode grouping gives the vacuum coefficient

    alpha(x)=15(6x²+18x+14) /
      [8omega² (x²+2x+1/3)(x²+2x+2/3)].                         (1)

For clarity, the first inverse coefficients are a=(x+5/3)/(x²+2x+1/3), b=-1/(x²+2x+1/3) multiplying vacuum and u-wedge-v. For fixed C the post-gamma vector is6a u-3b s w_C. Its second inverse's u-component is[6(x+4/3)a-3b s²]/(x²+2x+2/3). The perpendicular components cancel in the15-pair sum, proving (1).

Particle-hole conjugation of all six active complex modes fixes every a_j and reverses every b_j, hence sends H_F,W to -H_F,W and maps the vacuum to the filled six-mode state. It is implementable as a unitary CAR transformation because six sign reversals have even determinant. At the fixed original energy E0,W=-3omega, conjugating E0,W-H_F,W gives E0,W+H_F,W=omega(M-6I). Two inverses remove their common overall sign, so (1) with x=-6 gives

    O_0(E0)|filled> = alpha(-6) gamma_0|filled>,
    alpha(-6)=2745/172864 at |t|=1,

which differs from alpha(0)=315/64. The filled state has even active parity and is an allowed canonical-sector active excitation with the appropriate spectator parity; it is not claimed to lie in the low-energy window.

A Hermitian linear active Majorana operator is uniquely determined by its vacuum transition: the map from its real coefficients to the one-particle complex vector is an isomorphism. Thus the observed vacuum action fixes the only possible linear operator to alpha(0)gamma_0. Its different action on the filled state disproves that full-operator identity. This is a fixed-frame operator statement, not an obstruction to a dressed low-energy description. Energy-dependent Feshbach operators may be evaluated on the full retained active space even when those vectors are excited; no assertion of an all-active SW spectral gap is used.

## Next checks and cost scope

The zero-solve analytical filled-state witness should receive independent sign/frame review before being used as a theorem. If a literal finite-source check is desired, a new frozen run can replace the vacuum source by the filled even basis vector and reuse the same30 solves; compare to2745/172864 only after fixing that contract. The prior1.74-second whole run suggests similar cost, but opposite source fill can change rational elimination bit sizes; a conservative30s384MiB one-run contract suffices prospectively, not an already executed test. No operator-basis scan has been launched or required.

For physics beyond the singleton channel, the lowest useful next calculation remains the certified mixed-prefix L6 Gaussian route. L4 vacuum linearity explains one special exact cancellation and does not remove those prefixes or establish a bulk quadratic hybridization.
