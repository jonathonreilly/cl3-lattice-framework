# Ward-augmented common Gram: sufficient prospective ledger

Source-only, h=1 dimensionless units. Import the reviewed Ward insertion proof222f (cold6ade), common five-orbit c61c, and symmetric compression3d774 (freeze2987), without modifying them. This is an enlarged mathematical error budget, not an actual Gram evaluation or an accepted finite time generator.

## Scaling and actual dimensions

Append x0=e0/2,xA=wA/2,xC=wC/2 to the396 raw pole columns. The raw dimension is399, covariance-closed dimension n=798. Here omega=1/4 exactly: no irrational new scaling or balancing error. Extend BOTH pair coefficient matrices by zero on these columns and their Gamma partners. Their norm bound remains1 and their physical Q operators are unchanged.

All three appended real vectors have positive chiral sign; Gamma partners have negative chiral sign. The prior paired chiral pivot/dilation construction applies verbatim. There is one common frame and one common covariance. The exact small appended block is G00=1/4,G0A=G0C=1/12,GAA=||wA||²/4,GCC=||wC||²/4,GAC=k(1/6-a0)/4 and J=0. These entries must not be replaced by independent orthogonal insertions. In particular the center contribution in each w has norm1/3 and is retained; numerical small eigenvalues are not licenses to drop these dependencies.

Using ||w||²<=17/30, the added closed trace is at most

 2 omega (1+17/30+17/30)=16/15.

Thus T=Tr M<529+16/15<531. Raw trace<531/2. Appending unscaled W=6gamma(w) would waste this trace budget; recover W as12gamma(xA), and gamma(e0)=2gamma(x0) after compression. This makes the physical insertion error explicit rather than hiding it in the operator coefficient matrix.

## Scalar entry errors with all append inflation

All eta below are radii, not full widths. Assume existing A,A' radii<=1e-30, B,B' radii<=1e-19, new c_minus radius<=1e-19 and a0 radius<=1e-30. The actual precise a0 certificate can be used only after binding its accepted physical normalization; the looser target is sufficient here. No c_minus outcome is assumed.

The existing pole block B/B' operator error is <=48166272 eta_B. The append-pole J formulas at s>=1/128,s<=16 give unbalanced B multiplier<=257 and c multiplier<=256. Since sqrt(alpha)<sqrt12<4 and sqrt(omega)=1/2, the appended balanced multipliers are <=514 and512. Center append entries obey these same loose bounds. In the full798 matrix each new error entry is therefore <=514 eta_B+512 eta_c. The maximum row-sum bound, deliberately charging all798 entries even though only six rows/columns are new, gives

 epsilon_Bc <=48166272 eta_B+798(514 eta_B+512 eta_c)
             <=48985020*1e-19 <5e-12.

This adds a perturbation supported on new rows/columns to the original embedded pole error; it does not incorrectly rescale the old block as if every entry were new. Closed covariance blocks preserve the same entry bounds.

For A append entries, the unbalanced neighbor multiplier is <=2+s²/3<88 and center multiplier<=s/3<6. Balancing contributes at most2, so use176. Ward-Ward a0 multiplier<=1/2. Consequently old2^38 eta_A plus798*176 eta_A+399 eta_a0 is <2^40*1e-30. This also covers the center append A dependence. These are conservative actual entry sensitivities; no inverse Gram conditioning is used.

The equivariant factor theorem in dimension798 yields, for each impurity,

 E(epsilon)=2 sqrt(531*1596*epsilon)+1596 epsilon.

E(5e-12)<.00412. E(2^40*1e-30)<.000002. A separate final arithmetic spectral error epsilon_num<=2^-60 contributes <.000002. Signed coefficient error<=2^-40 contributes less than(531+1596 epsilon_num)2^-40<1e-9. Reserve1e-6 for the existing pole/weight/pi displacement and coefficient-input errors (these are vastly smaller under their frozen targets, but must still be bound). Their sum is below.0042<.005. This is a sufficient prospective ledger, not a claim those arithmetic residual gates have run.

The new source scaling is rational, so it introduces no root-rounding uncertainty. Old balancing/root/pi arithmetic still belongs in epsilon_num and the imported geometry budget. Chiral change of basis is orthogonal; it cannot amplify these spectral bounds.

## Compression and insertion errors stay separate

For a subsequent common projection Q commuting Gamma/chirality, let r=Tr[(I-Q)Yaug]^T[(I-Q)Yaug] be the actual RAW residual. Each impurity compression error is at most2sqrt((531/2)r)=sqrt(1062r). To allocate .001 to compression, it suffices r<=1/1062000000; this is separate from the .005 physical-input/factor ledger.

Each physical e0,wA,wC has projection error <=2sqrt(r), and W has error<=12sqrt(r). A tighter per-column residual can replace r. Under a common equivariant Gram dilation with spectral input radius epsilon, additional vector errors are <=2sqrt(2epsilon) for e0,w, and12sqrt(2epsilon) for W. Both terms must be propagated into the mixed-kernel insertion contractions; the .005 operator ledger alone does not certify inserted kernels.

No time generator has been represented or its propagation error bounded by this append. That remains the next constructive blocker.

## API scope

append_api.py supplies exact rational midpoint formulas for ordered (0,wA,wC) versus the three original source columns, and the appended block, including the physical signs and fixed1/2 scaling. It performs no native input loading, assembly or pivot. A future interval adapter must reproduce the displayed radius ledger and actual source binding. The native_append entry point is disabled. Tiny synthetic checks can test source algebra without pretending to test the bath or acceptance of c_minus.
