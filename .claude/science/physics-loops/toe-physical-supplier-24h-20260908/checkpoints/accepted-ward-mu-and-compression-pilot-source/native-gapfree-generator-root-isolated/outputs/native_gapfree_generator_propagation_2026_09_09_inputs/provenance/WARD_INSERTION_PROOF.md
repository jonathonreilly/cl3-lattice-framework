# Actual Ward sources in the shared star frame

Source-only derivation; no native Gram, integral, pivot or propagation evaluated. The previously frozen symmetric-compression2987 is unchanged. Read CORRECTED_WARD_IDENTITY.md and NATIVE_WARD_ROUTE.md in native-node-analytic-sign-stretch, the canonical finite-excitation Ward note, and native-star-local-green-gram-stretch/DERIVATION.md. Retain their infinite-volume Fourier inverse and h=2|t_hop|>0 conventions.

## 1. The actual vector, including its sign

K=[0,B;-B^T,0], h0=iK, center in the first sublattice. The center row is -h on positive neighbors and +h on negative neighbors. For d_A=sum_(j in A) epsilon_j e_j, epsilon_(+a)=1,epsilon_(-a)=-1, the actual restricted row column is b_A=-h d_A. Thus

 w_A=(B^T)^-1 b_A=i h h0^-1 d_A,
 h0 w_A=i h d_A,  (w_A)_0=1/3,  W_A=6 gamma(w_A).

These are real l2 vectors. The inverse is only applied to the specified local source, not asserted bounded on the full one-particle Hilbert space. Three-dimensional Dirac integrability proves its l2 domain. In particular {W_A,gamma(e0)}=4. Replacing d_A by an unsigned two-site vector changes the operator.

## 2. Closed cross-Grams

Use seven-site matrices O,T,N=I+O from the local-Green proof. Let

 a0=E[X^-1], c=E[X^-1/2], D0=1/(6h^2),
 E_s=A(s)N-D(s)O, D(s)=(1-s^2 A(s))/(6h^2),
 L_s=(c-B(s))/s^2,
 M_s=L_s N-B(s)O/(6h^2).

For any real local star column v, let y_(sigma,s,v)=-i(h0-i sigma s)^-1 v. It is a real CAR vector. With Gamma0=i sign(h0), Gamma0^2=-I, the exact real bilinear entries are

 <w_A,y> = -h d_A^T E_s v + sigma s A(s) d_A^T T v/6,             (G)
 <w_A,Gamma0 y> = B(s)d_A^T T v/6 + h sigma s d_A^T M_s v.       (J)

All balanced-column entries multiply by the existing sqrt(alpha_j); no new matrix normalization is introduced.

Proof: h0^-1 R_z=(R_z-h0^-1)/z, and the local h0^-1 matrix is i h D0 T. Multiplying w_A^*=-i h d_A^T h0^-1 and y=-i R_z v gives (G). For (J), h0^-1 Gamma0=i|h0|^-1, and

 U^* |h0|^-1 R_z U=i B(s)T/(6h)+i sigma s M_s.

The even part follows from 1/[sqrt(X)(X+s^2)]=(X^-1/2-sqrt(X)/(X+s^2))/s^2. The oriented odd part is the same local parity calculation as the Green proof. This establishes the sign of J without a choice of an impurity vacuum.

Between Ward sources,

 <w_A,w_C>=h^2 d_A^T[a0 N-D0 O]d_C,
 <w_A,Gamma0 w_C>=0.                                         (W)

The second equality is exact sublattice parity: both w's are first-sublattice vectors, Gamma0 exchanges sublattices. For a perpendicular pair ||w||^2=2h^2 a0; for an opposite pair ||w||^2=1/3. For disjoint pairs with k cross-opposite incidences, <w_A,w_C>=k h^2(D0-a0). Consequently the five orbit types have cross entries 0,0,0,2h^2(D0-a0),h^2(D0-a0). Their possibly negative sign is not to be clipped.

The only bare insertion required by the Ward identity is e0:

 <e0,w_A>=1/3, <e0,Gamma0 w_A>=0, ||e0||=1.

The e0 versus nonzero-pole columns is already supplied by the local Green functions; the projected resolvent's constant mu O has zero center row. Thus adding e0,w_A,w_C and their Gamma partners to the common frame closes ALL insertion geometry with precisely the nonzero-pole A,B catalog plus a0 and c. Derivatives A',B' remain needed for the existing pole Gram, not for (G),(J),(W).

For completeness, if additional bare neighbor vectors are requested, then

 <w_A,Gamma0 e_j>=h d_A^T[c N-mu O/(6h^2)]e_j,
 mu=E sqrt(X).

That enlarged optional problem needs mu; it must not be charged to the present Ward-only scope. The source w_A is supported on the first sublattice, so its bare-neighbor Euclidean overlaps vanish.

## 3. What is and is not already closed numerically

Nonzero A/B66 values alone do not specify a0,c exactly. Existing analytic bounds a0<=17/(60h^2), c<7/(15h) suffice for finite interval inclusion, but may be far too wide for a useful pivot/compression certificate. An accepted scalar certificate for c_minus supplies c directly. A certified zero-argument A oracle supplies a0 only if its physical normalization and acceptance are actually bound; this note does not substitute a speculative value or infer acceptance from a file name. No mu evaluation is required here.

The Ward vectors are legitimate infinite l2 sources, not positive-pole columns with s set formally to zero. Their exact insertion into a common Gram is permissible once these scalar intervals are available. The joint Gamma/chiral closure uses w first-sublattice and Gamma w second-sublattice. Append all three real sources once, using a common dilation and common pivot projector. This adds at most six real dimensions to the coefficient closure; dependencies may reduce rank. Do not construct separate impurity frames or regard numerical null directions as occupied physical modes.

## 4. Explicit conditioning and error accounting

Equations (G),(J) avoid a divided difference between a tiny pole and zero in A. However the c input in J has coefficient h sigma/s times d_A^T N v. Thus small s does amplify c uncertainty. For common v in {e0,d_A,d_C}, |d_A^T N v|<=2 and |d_A^T O v|<=2. At h=1, s>=1/128, radius eta_c contributes at most256 eta_c to an unbalanced J entry. The B radius contributes at most (2/s+s/3)eta_B for neighbor v; the center term is eta_B/3. Weighted entries acquire sqrt(alpha_j), whose interval/error is separately accounted.

The Ward-Ward Gram a0 sensitivity is at most2h^2 eta_a0 per entry. Center identities and the vanishing J(W,W) are exact structural equalities. These estimates are actual entry bounds, not yet the total enlarged-matrix/operator budget: dimension, source scaling and factor norms must be propagated through the existing common-dilation/compression theorem. In particular a0 merely bounded by17/60 is not a claim of successful compression.

The singularity is physical: h0^-1 is unbounded and w has a Dirac 1/|k| Fourier tail. The finite l2 norm does not supply a uniform bounded inverse or fast spatial decay. A zero-pole approximation requires its own error proof; exact scalar append avoids that approximation but does not remove possible small pivots. The parent protocol may now choose certified a0/c inputs and an insertion-weight ledger before any actual augmented Gram job.

Alpha and its sign remain unresolved. These formulas close the actual bounded Ward insertions needed by the mixed Gaussian contraction formulas, not the full time evolution or a positivity proof.
