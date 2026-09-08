# Native low-projected A edge includes gauge-invariant pair channels

## Frozen premises and orientation

Use the actual full native dictionary W A_ij W†=-i gamma_i gamma_j X_e (i<j), and the corrected signed-defect U1 map of native-low-charge-u1-dictionary/DERIVATION.md a70724ba. The latter uses site-major species CAR f_{v,+},f_{v,-}, no double occupancy, spin-half links E=x-1/2 and exact Gauss divE=rho=n_+-n_-. Its unitary phase is d(x)s0(I)b_D, where s0=(-1)^sumI is the correct increasing-hole basis phase and b_D=(-1)^[D(D-1)/2] is an explicitly optional block phase. The graph is the stated even cubic torus, all extents>=4, full low-charge domain and relaxed cycle constraints. This note keeps b_D exactly as previously tested; off-D signs therefore require a new derivation.

Orient a physical edge from black b to white w. L^+=|1><0| raises E and L^-=|0><1| lowers it. Define A_bw by the native antisymmetric convention; for the physical ascending edge i<j, A_ij=kappa A_bw, with kappa=+1 if b<w and -1 otherwise. This orientation factor must not be silently dropped.

## Complete projected operator

Let P_nd impose no-double occupancy and define the ordered bilinear

    B_bw = f†_{b,+} f_{w,+} + f_{b,-} f†_{w,-}
           - f†_{b,+} f†_{w,-} - f_{b,-} f_{w,+}.

Then on the exact Gauss/no-double subspace,

    mathcal W (P_low A_bw P_low) mathcal W†
       = -i P_nd [B_bw L^+ - B_bw† L^-] P_nd.

Multiply by kappa for the ascending native edge operator. This is manifestly Hermitian since link and matter operators commute. Products of different-site fermion operators retain their displayed order. P_nd can be replaced by its two endpoint factors on the constrained domain. Projected flavor operators themselves are not asserted to satisfy full CAR.

For comparison, without the optional b_D phase the plus-ladder bilinear would be

    B0_bw = (f†_{b,+}+f_{b,-})(f_{w,+}+f†_{w,-}),

with all four expansion signs positive. The full operator is again -i(B0 L^+ - B0† L^-). The change is exactly the minus on both pair terms, not an adjustable hopping sign.

## Derivation and support table

In hole variables h†=c, h=c†, gamma=h+h†. In the site-major no-double encoding, an allowed change of signed charge by+1 at b is represented by f†_{b,+}+f_{b,-}; a change by-1 at w is represented by f_{w,+}+f†_{w,-}. The source factor -i gamma_b gamma_w fixes operator order. The ladder L^+ changes Qb by+1 and Qw by-1. Its complete allowed input/output table is

    (Qb,Qw)=(0,+1)  ->(+1,0): positive hole hops w->b;
    (-1,0)         ->(0,-1): negative hole hops b->w;
    (0,0)          ->(+1,-1): opposite pair creation;
    (-1,+1)        ->(0,0): opposite pair annihilation.

It requires x_e=0. The L^- table is its reversed transitions and requires x_e=1. Every other endpoint/bit combination either has zero ladder/CAR support, is killed by no-double projection, or would have |Q|>1 and is absent from the source low-projected column. These are all possibilities, because each toggle shifts the two signed charges oppositely by exactly one.

The electron-to-hole basis conversion is the corrected s0, not the earlier erroneous absolute phase formula. The extra b_D contributes b_{D±2}/b_D=-1 to pair creation or annihilation and contributes+1 to the hopping channels. That gives B_bw above. This matters even though all global physical D are even. It was invisible to the prior D-conserving hopping/ring tests and is independently checked here.

The Gauss transformation multiplies B_bw by exp[-i(theta_b-theta_w)] and L^+ by the inverse. Both hopping and pair monomials therefore commute with every Gauss generator. Pair creation has opposite charges, so gauge invariance does not require defect-number conservation. This is not gauge breaking of the old magnetic code: that code constraint is already relaxed, and the exact integer Gauss condition belongs to the redundant representation.

## Sector and Hamiltonian implications

The operator has nonzero D0->D2, D2->D0 and D2->D4 matrix elements on the actual carrier, with Hermitian reverses. Hence D and each species number are not conserved under a general supplied nonzero A coupling; pair terms change N+ and N- together. Their difference and all exact Gauss constraints remain conserved. This contrasts with the earlier T-only Hamiltonian, which preserves each signed species separately. Existing D-sector energy and connectivity theorems must not be transferred to a Hamiltonian containing these pair terms without a new argument.

P_low A P_low is not generally an involution on the low domain: forbidden toggles are killed by the intermediate projection, even though ambient A²=I. It connects the exhibited D sectors, but this note alone does not establish connectivity of the entire low domain. Adding real coefficients times these Hermitian operators is a new supplied Hamiltonian choice, not a derivation of occurrence, pair-production dynamics, coupling strength, relativistic particles or physical preparation.

## Exact bounded controls

The preregistered standalone checker directly evaluates native Pauli-string phases and compares them with the four-term species-CAR/ladders after the full d*s0*b_D map. It does not import the old executable or rely on its D-conserving outcomes. Twenty-four actual L4 initial configurations span D0 through16 and64; all192 initial edge columns are considered. Five hundred four forbidden initial columns are zero. Allowed columns are also checked at fixed non-backtracking second-edge selections, giving24596 composed two-edge paths including0->2->4 and2->0->2. The source phase and mapped phase agree at every tested step, not just after squaring one edge. Counts including repeated composition columns are disclosed in RESULT.json.

The deliberate omission of the b_D pair signs fails26918 tested pair-channel comparisons; conserving columns are not falsely expected to fail it. The run used9.58s and18.39MiB, below180s/384MiB. This is a selected-column/full-bit physical control, not an exhaustive L4 Hilbert-space census. The exact operator proof, rather than the finite count, supplies the general identity.
