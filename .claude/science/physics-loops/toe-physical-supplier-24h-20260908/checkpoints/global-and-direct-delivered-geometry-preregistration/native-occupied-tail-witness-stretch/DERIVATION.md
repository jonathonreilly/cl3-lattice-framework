# A particle-hole occupied-tail lower witness

Source-only independent derivation. Let R=P0^+, S=PA^+ be orthogonal projections on the complex one-particle Hilbert space, D=S-R trace class, C=(I-R)S=(I-R)D, and Q=|C|. Let P be the exact selected orthogonal projector and E=I-P. Assume an antiunitary particle-hole conjugation J satisfies JRJ^-1=I-R, JSJ^-1=I-S and JPJ^-1=P. No zero-mode ambiguity in these projection identities is allowed. In the canonical imaginary-hopping realization complex conjugation supplies the first identities; the selected projector must be shown real in that realization. Unitary chirality closure alone is not a substitute for this antiunitary invariance.

Since ||C||<=1, functional calculus gives Q>=Q². Thus

 tau=Tr(EQ)>=Tr(EQ²)=||CE||HS².

All traces exist because C is trace class. This does not require E to commute with Q. Now J C J^-1=R(I-S)=-RD, while JEJ^-1=E. Antiunitary conjugation preserves Hilbert-Schmidt norm, so

 ||CE||HS²=||RDE||HS².

Orthogonality of the two left reference sectors gives

 ||DE||HS²=||(I-R)DE||HS²+||RDE||HS²=2||CE||HS².

Therefore exactly

 tau >= (1/2)||D(I-P)||HS².                              (1)

No principal-angle cosine factor is inserted. Equality in the HS relation is symmetry-based; the first inequality can be strict. If P is not J-invariant, only the generic bound tau>=||CE||HS² survives. For instance R=diag(1,0),S=diag(0,1),J swapping coordinates followed by conjugation and E=diag(0,1) violate that invariance and give||CE||²=||DE||²=1, not the half identity. The correct actual selected-real premise must be pinned before reuse.

If ||D-Dhat||1<=eta, then the ideal property of Schatten norms yields

 tau >=(1/2)[max(0,||Dhat E||HS-eta)]².                   (2)

This remains valid for any finite approximant Dhat; its being a projection difference is unnecessary. The accepted eta bound can be used only with the exact source/operator convention it certifies.

## Finite witnesses need no full new-new Gram

For finite orthonormal column families X,Z, set W=Z*Dhat E X. Then ||W||F<=||Dhat E||HS. Hence a certified lower bound ell on ||W||F proves tau>=max(0,ell-eta)²/2. X and Z may be fixed local site basis columns in the full native one-particle space. Their orthonormality is exact. A single matrix element is enough in principle; it can fail to witness even when the total tail is large.

For a finite block approximation Wc with entry radii r_ij, an explicit lower bound is

 ell=sqrt(sum_ij max(0,|Wc_ij|-r_ij)²).

Exact rational lower square-root bracketing avoids floating threshold decisions. Alternatively ||Wc||F-sqrt(sum r_ij²) is safe. This is a lower witness, not an estimator of the full tail.

Using P=V H^-1 V*,

 W=Z*Dhat X - (Z*Dhat V) H^-1 (V*X).                     (3)

Only these two blocks and selected metric inverse are needed. Equation(3) does not request the full new-new Gram. With candidate inverse Y and certifiedv=||Y-H^-1||, the inverse-substitution error is at most||Z*Dhat V|| v ||V*X||<=M b v for||Dhat||<=M and||V||²<=b. Directly available smaller block norms can improve it. All errors in block acquisition, operator coefficients, and initial physical eta are charged separately.

## A coarse falsifiable contract

Choose a fixed local X,Z block before reading any witness values. A prospective pilot can use, for example, the center and six nearest-neighbor site basis vectors as seven columns each (49 complex entries). This is a proposed full-space local block, not an assertion it catches the missing occupied directions. Both pair geometries and allfive fixed selected spans require their actual dictionary/translation convention; none is evaluated here.

For eta<=2e-13, if the certified block lower bound ell>=1/20000=5e-5, equation(2) yields tau>1e-9. The exact threshold is sqrt(2e-9)+eta, so this rational gate has margin. An entry-error cap1e-7 would give Frobenius uncertainty at most7e-7 for a7x7 block; use the actual lower formula instead of assuming the block norm exceeds the threshold. This coarse cap is radically weaker than1e-37, but its feasibility remains a new acquisition question. The old H uncertainty may or may not meet the inverse error portion; it must be checked against Mbv and cannot be silently recentered.

If the lower bound does not cross the gate, report INDETERMINATE_WITNESS. Do not conclude tau small, enlarge the block adaptively, or switch targets inside the same fixed protocol. A separately preregistered larger/local translated block is a new experiment. If the gate crosses, only the chosen current selected subspace is excluded for the proposed tau target; the native model, a larger span, and other consumer methods remain open.

The suggested49-entry block is not ready for execution: exact block formulas/source authentication, conservative interval input requirements and resource contract must be independently reviewed. No actual local columns, T, Gram, native data, or witness values were read. The previous fine-precision source remains archived; this lower-bound route is a distinct pruning certificate.
