# Prospective same-carrier .95 versus zero comparison — no execution

This is a staged research proposal, not a frozen production contract or a claim that the two endpoints share a phase. No new numerical calculation or microbenchmark was run. The running L8 .95 protocol, its seeds, coverage and gates remain unchanged. Root supplied the endpoint question and the fourth-order/winding warning before this proposal.

## Exact operator to be studied

Let e=(r,a) be a positive-coordinate cubic edge, x_e its occupation, E_a(r)=epsilon(r)(x_e−1/2), epsilon(r)=(-1)^(r_x+r_y+r_z). The ice carrier has three occupied edges per vertex (twenty local configurations). Write T_C=F_C S_C for an alternating ring. For equal positive canonical native edge couplings the reviewed fourth-order operator, after its scalar is subtracted and time units rescaled, is

  K_native4 = sum_elementary T_p − sum_straight-length4-winding T_C.

This formula uses the lexicographic native orientation and the reviewed eta_C signs. Define sigma_x(r)=(-1)^(r_y+r_z), sigma_y(r)=(-1)^r_z, sigma_z(r)=1 and the explicit diagonal physical unitary Z_pi=product_{e:sigma_e=-1} Z_e. Conjugation multiplies each ring by product_C sigma_e. This product is −1 on each elementary square, including seams on even periods. On each straight winding length-four cycle it is +1: its transverse coordinates are constant and the fixed sign is raised to the fourth power. Thus

  Z_pi K_native4 Z_pi = −sum_elementary T_p −sum_length4-winding T_C.

No new sign pattern is selected physically by this basis change. Diagonal E, flippability and Fourier-intensity observables commute with Z_pi. An off-diagonal observable or a trial state must be transformed too; in particular the positive uniform trial in the transformed basis corresponds to Z_pi times that trial in the original positive-canonical-A basis.

For isotropic L4 there are 3 L²=48 straight winding four-cycles, in addition to 3 L³=192 elementary squares. Their presence is an operator change, not a statistical correction. Each alternating straight winding flip changes the corresponding electric flux by one unit (with sign), since it reverses one oriented E=±1/2 link through every transverse cut. Hence flux sectors are NOT invariant for the full native L4 fourth-order operator. A fixed-flux L4 run of elementary squares cannot be called that native effective model. Integer Gauss charge remains zero under those winding flips.

When every extent is at least six, there are no length-four winding cycles. The leading native operator is then the conventional elementary pure-kinetic H(0)=−sum_p T_p, after Z_pi. This is only the reviewed finite-volume fourth-order correspondence; omitted higher orders, the supplied low projection and perturbative scale remain separate obligations.

Decision: the first endpoint study should deliberately use the elementary-plaquette family H(V)=V N_f−sum_p T_p at L8, with V=.95 and V=0. It matches the leading native effective operator at V=0 for that size, but does not study the full native H(g). L4 may be a separately labeled two-operator control (plaquette-only versus all-four-cycles), never silently pooled as a native size point. L2 is only an exact algorithm oracle for its geometric-move model, not a simple degree-six native perturbation example.

## Minimal staged design, before any production

Stage 0, deterministic implementation review only: parameterize V explicitly in the local kernel, endpoint h=(V−1)N_f, row sum b=1+(1−V)N_f/M and acceptance b(old head)/b(old second tail). At V=0 the aggregated self weight is one, not zero; Q has self probability 1/b. Preserve geometric labels and multiplicities. Enumerated L2 transition and finite-G oracle comparisons at V0 must precede use, along with literal local-path replay. A separate sign/winding control should check Z_pi products, full ice support and flux changes on explicit L4 loops and absence of nongeometric four-cycles for L≥6. No such control has been executed here.

Stage 1, resource profile only after review: one L8 V0 end-to-end profile ≤30s/384MiB with both spectral harmonics and the proposed diagonal order observables. Its purpose is timing and state/cache drift, not physics. Existing .95 throughput does not establish V0 autocorrelation cost. Keep 180s/384MiB segment caps and exact resumable RNG/path state if needed. Forecast ≤80% of an explicitly authorized aggregate envelope; otherwise stop before production. Do not reduce independent chains after outcomes.

Stage 2, smallest informative production proposal after that forecast: two new V0 arms at L8, equal independent-chain coverage, tau12 and tau36, RK2048 propagated initialization and burn32n, matching the already frozen .95 A/C projection settings. The new seeds are prospectively disjoint. This is an endpoint comparison only, not a continuity/phase diagram test. A fixed additional initialization family is more informative than adding many intermediate V points: construct an explicitly distinct, high-order seed in the SAME declared flux/component only if reachability is proved or a recorded legal path is supplied. Otherwise label it a different component and do not treat agreement/disagreement as an initialization test. Coverage and runtime cannot yet be frozen without the new measurement profile; no production is authorized by this document.

A full claim about absence of a transition between .95 and0 would require additional couplings and size scaling. No interpolation from endpoints is permitted. An intermediate V=.5 could become a separately preregistered follow-up after endpoint analysis, not an outcome-selected rescue point in this study.

## Observables that distinguish order, sectors and spectral centroids

Retain the nine same-time moments NF, S1,S2,Eavg,hLhR,S1Eavg,S2Eavg,S1²,S2². At stationarity for the product-G path law, they give D, the endpoint covariance correction, R relative to E_psi, and signed VarH/VarS; all finite-projection qualifiers remain. L8 h2 matches L4 h1, while L8 h1 is a lower momentum. A centroid or corrected Rayleigh ratio does not identify a pole or dispersion exponent.

Add explicitly diagonal order probes rather than relying on a zero mean in a symmetry-invariant finite state. Define m_a(k)=L^-3 sum_r E_a(r) exp(i k.r) and f_ab(k)=L^-3 sum_r F_ab(r) exp(i k.r), with the eight reciprocal-corner momenta k in {0,pi}³ fixed prospectively. Record squared amplitudes, their cross-covariance, and fourth moments for a Binder-style diagnostic only where denominators are resolved. Also record orientation anisotropy sum_ab (mean_r F_ab−N_f/(3L³))². These are a finite candidate ordering menu, not an exhaustive detector of all possible crystals; an incommensurate or more complicated order may escape it. Specify the transformation of this menu under cubic rotations before using symmetry pooling. Do not substitute six separate channel standard errors for their joint covariance.

The original .95 raw data do not contain this complete order menu. Therefore a matched .95 order reference requires fresh, separately authorized measurement; it cannot be reconstructed from S1/S2. Existing raw .95 is usable only for its explicitly stored quantities. This missing reference is a reason to keep Stage2 a spectral endpoint pilot, or to budget a new paired .95/V0 order study prospectively, not to claim a complete phase comparison from old data.

For the plaquette-only model, define Phi_a=sum_{r_a=0}E_a(r). Each elementary flip preserves Phi exactly. A flux-response extension would require separately declared, explicitly legal Phi=(0,0,0) and one-unit-flux initial components, with plane-independence/Gauss checks. Finite projected energies in two components can be compared, but their difference is not a certified difference of sector ground minima: both energies have projection errors and the selected components may not minimize their whole sectors. The full L4 native operator cannot use this fixed-flux protocol because its winding rings mix Phi. For it, flux distribution/mixing is an observable instead.

## Predeclared outcomes and failure boundaries

Use independent whole-chain means as statistical units. Batches and resumable segments are diagnostics only. Keep the existing 4SE nominal contrasts and ten-percent 4SE/D precision criterion for positive D; retain negative variance and unresolved correction estimates without clipping. Record original-tag survival, run-length/roundtrip data, burn split diagnostics and acceptance. Nonzero retained initial memory, failed burn/projection contrasts, unresolved residuals or inadequate precision yield failure/indeterminate for the relevant interpretation. Unflagged contrasts are not equilibration proofs. Expected V0 failures include slow ordered-domain tunneling, persistent lifted-path memory, poor overlap of the RK-derived start with the V0 ground vector, and symmetry/component trapping. A favorable acceptance fraction alone does not refute these.

No order threshold or Binder crossing can be certified from one L8 point. A phase or photon conclusion needs isotropic size behavior, competing-order diagnostics, sector control and spectral information beyond these centroids. The immediate useful result would be a controlled finite-projector endpoint difference or a precisely isolated sampling/initialization failure, not a renamed V0 Coulomb claim.

## Literature and source boundary

The reviewed comparison 8e8a56ca identifies the matching cubic twenty-vertex carrier and the limits of the near-RK literature. Hermele–Fisher–Balents, Sec II B and Fig1, gives the cubic family and leaves the lower edge of the adjacent liquid interval unknown: https://arxiv.org/pdf/cond-mat/0305401 . The finite-tube study uses the relevant bosonic link model but is not an isotropic bulk phase certificate: https://arxiv.org/pdf/2201.07171 . This proposal imports neither paper as proof that exactly V0 or .95 is in a phase. The native fourth-order source supplies the signed coefficient/winding bookkeeping, not a convergence-to-H(0) theorem at finite coupling.
