# Independent signed native reduced-dual covariance bank

Source-only PASS of the bank in625f027c, h=1. No native scalar or covariance was evaluated. This checks the vector closure and all two-point inputs, not yet the new runtime or its eventual signed estimator.

## Recover the signed elementary forms

The reviewed Ward-source orientation is K=[0,B;-B^T,0], center row negative on positive neighbors and positive on negative neighbors. Set b_j=epsilon_j e_j with epsilon positive/negative1 accordingly. Then Ka=k=sum_j b_j, and skew-symmetry gives a·K b_j=-(Ka)·b_j=-1. It is not an unsigned adjacency convention. The d in this note is the signed pair sum, so a·Kd=-2; the source perturbation is i gamma(a)gamma(d).

Let N(f,h)=sum f_j h_j and O(f,h)=sum f_j h_(j xor1) for real linear combinations of the six b_j. Since the b_j are orthonormal, f·h=N. The literal free lattice measure has each ||Kb_j||²=6. The reviewed pair identities ||Kd_P||²=12 and ||Kd_O||²=14 then polarize pair by pair to

 (Kb_j)·(Kb_l)=6 delta_jl+delta_(j,l xor1).

Consequently (Kf)·(Kh)=6N+O. This derives the signed opposite entry +1 from the native pair identities and fixed K orientation; a bare unsigned two-step adjacency guess would not fix it.

The diagonal local |h0| measure is mu=3c. Reviewed signed pair measures are <d_P,|h0|d_P>=2mu and <d_O,|h0|d_O>=nu/3. Polarization gives

 <b_j,|h0|b_l>=3c delta_jl+(nu/6-3c)delta_(j,l xor1).

For kappa=K/|h0|, skew K and -K²=|h0|² imply

 kappa(Kf,h)=f^T K^T K |h0|^-1 h=<f,|h0|h>
             =3c N+(nu/6-3c)O.

The sign is POSITIVE. Also kappa(a,d_A)=-c for each of all15 signed pairs. These15 pair-sum equations imply each kappa(a,b_j)=-c/2, hence kappa(a,f)=-(c/2)sum f_j. This is fixed by the Gaussian reference convention; it is opposite to the Gamma0=i sign(h0) real matrix convention. Confusing those two antisymmetric matrices would reverse every displayed covariance sign.

The bipartite coloring puts a,Kd,Kk,Ke white and d,k,e black. Cross-color real dots and same-color kappa vanish. Ordinary Gram is symmetric and kappa skew. These statements use the native chiral symmetry, not an arbitrary isotropic Gaussian covariance.

## Explicit perpendicular bank

Choose d=b0+b2 and the unused-axis opposite pair e=b4+b5; k=sum six b_j. Any signed native perpendicular pair is related by the already supplied lattice symmetries. In white order(a,Kd,Kk,Ke) and black order(d,k,e), the real dot blocks are

 Dw=[[1,-2,-6,-2],[-2,12,14,0],[-6,14,42,14],[-2,0,14,14]],
 Db=[[2,2,0],[2,6,2],[0,2,2]].

The white-to-black antisymmetric covariance block is

 Kappa_wb=[[-c,-3c,-c],
           [6c,nu/3,0],
           [nu/3,nu,nu/3],
           [0,nu/3,nu/3]].

In the author's interleaved order(a,d,k,e,Kd,Kk,Ke), insert these blocks at white indices(0,4,5,6), black(1,2,3). Reverse kappa is negative transpose; the physical two-point function is dot+i*kappa, so reversing a word conjugates its covariance. In particular <Kd,Ke>_real=0 and kappa(Kd,e)=0, but <Kk,Ke>=14 and kappa(Kk,e)=nu/3. The untouched-axis source is not orthogonal to the whole bank.

## Explicit opposite bank

Set d=b0+b1 and omit e,Ke. White order(a,Kd,Kk), black(d,k) gives

 Dw=[[1,-2,-6],[-2,14,14],[-6,14,42]], Db=[[2,2],[2,6]],
 Kappa_wb=[[-c,-3c],[nu/3,nu/3],[nu/3,nu]].

Use white indices(0,3,4), black(1,2) in order(a,d,k,Kd,Kk). These are exactly the corresponding subblocks of the independently reviewed degree11 six-vector table; no omega5 entry survives. The extra Ke in the P bank uses only the elementary opposite-pair polarization above and likewise adds no higher moment.

## Closure and limits

The disjoint-pair sums W and R in625f lie in span(d,k,e); applying K puts their images in span(Kd,Kk,Ke). The reduced actions therefore require only this seven/five-vector bank. All contractions have dot+i*kappa with scalar symbols c,nu; the accepted spectral E,F still inherit their separate omega5 dependence. No claim is made that E/F or actual interval contractions are narrow enough. This table supplies no actual scalar values and authorizes no native call.

Independent controls enumerate every15 possible A, use the literal six disjoint pairs to test the W decomposition for symbolic P/O weights, and polarize the elementary N/O matrices into both displayed banks. Signed rational coefficient probes check the disjoint-sum linearity; skew completion is specified analytically. These are finite synthetic integer/rational identities only, not replacement proofs of native dispersion or source measures.
