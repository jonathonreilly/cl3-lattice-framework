# Exact redundant signed-defect U(1) quantum-link dictionary

## Scope and prior-source distinction

This is a constructive conditional operator dictionary, not a physical action or role-selection theorem. The source is the actual native full-carrier dictionary in NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md (3d61dfac), restricted to its supplied six-valent bipartite low-charge domain. The old September3 THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS... note was read completely. It supplies an independent additional physical link role and couples the earlier fermion-number charge. The present construction instead redundantly represents signed defects Q, with no new independent physical register. These are different charge/model surfaces: this does not retire the old role-supplier obligation or identify Q with that old Noether charge.

Fix a finite even cubic torus with each extent>=4, the source vertex/neighbor orders and relaxed magnetic-cycle constraints. Physical edge bits are x_e=(1-Z_e)/2. Let epsilon_v=+1 on black and -1 on white vertices, G_v=sum_incident x_e-3, Q_v=epsilon_v G_v. The physical Hilbert space is the span of all bit configurations with |Q_v|<=1. No further winding restriction is imposed. Its dimension is the number of those configurations; no giant census is needed.

## Enlarged representation and exact dimension

Introduce two mathematical CAR modes f_{v,+},f_{v,-} per vertex, in the fixed site-major order (0,+),(0,-),(1,+),(1,-),... . They act on a full ordinary Fock space. Add one mathematical spin-half link for each existing physical edge, with the same electric-bit basis. This is an enlarged redundant representation, not an additional physical role assignment.

Orient every edge from black i to white j. Define

    E_e = x_e-1/2 = -Z_e/2,
    L_e^+ = |1><0|,   L_e^- = |0><1|,
    [E_e,L_e^±] = ±L_e^±.

In conventional Pauli notation L^+=(X-iY)/2 and L^-=(X+iY)/2. Explicit ket definitions fix the otherwise reversed sigma naming. These are spin-half ladders, not unitary rotors: (L^±)^2=0 and E²=I/4.

Impose no double occupancy n_{v,+}n_{v,-}=0 and the simultaneous exact Gauss equations

    mathcal G_v = (div E)_v - rho_v = 0,
    rho_v = n_{v,+}-n_{v,-}.

All six incident edges are outward at black vertices and inward at white vertices, so divE=epsilon_v(sum x_e-3)=Q_v. For a fixed link string, the Gauss/no-double conditions have exactly one matter assignment when Q is0,+1,-1 (vacant,+,- respectively), and none when |Q|>1. Thus the constrained enlarged space has exactly the same basis cardinality as the physical low-charge space. Without no-double, neutral links would permit both vacancy and double occupation, and dimension equality would fail. On a closed torus sumQ=0, hence N+=N- and total defect numberD=N++N- is even. No extra parity projection is missing.

## Explicit all-sector phase map

Use the exact source W with

    W|x> = d(x)|n_c(x)> tensor |x>,
    n_{c,v}=sum_incident x_e mod2=1-Q_v²,

where d(x) is its source-defined quadratic native phase. Set h_v†=c_v, h_v=c_v† and use the filled electron state |F> as the hole vacuum. For an increasing list I of hole sites define |I>_h=product_{v in I increasing} c_v |F>. Relative to the ordinary electron occupation basis,

    |I>_h = s0(I)|n_c>,
    s0(I)=(-1)^(sum_{v in I}v).

The finite ordered product acts rightmost first: each removed larger index leaves the lower occupied indices intact, so its annihilation sign is (-1)^v. Map this hole basis to the species basis by replacing each occupied hole site v with the unique species sign Q_v, retaining site-major order. One may additionally choose an arbitrary constant phase on each D block. To preserve the originally tested map, choose b_D=(-1)^{D(D-1)/2}. This is an optional block phase, not the hole-basis identity. Therefore an explicit unitary onto the constrained enlarged space is

    mathcal W|x> = d(x)s0(I(x))b_D |{n_{v,+}=1_{Q_v=+1},
                                     n_{v,-}=1_{Q_v=-1}}> tensor |x>.

This is an all-D formula. It does not use the exceptional D2 charge-first ordering and does not erase same-species fermionic exchange signs. Diagonal identities include physical Z_e=-2E_e, Q_v=rho_v, D=sum rho_v²=N++N-, B_v=2rho_v²-1 and original native number N_c=|V|-D.

## Exact native hopping

Let P_nd be the no-double projector. For a black-to-white edge i->j put

    K_e = -P_nd [ f†_{j,+} f_{i,+} L_e^-
                 + f†_{j,-} f_{i,-} L_e^+ + h.c. ] P_nd.

On the simultaneous Gauss/no-double subspace,

    mathcal W (P_low T_e P_low) mathcal W† = K_e.

Proof: the source W gives electron hopping (c_i†c_j+c_j†c_i)X_e. Electron-to-hole conversion gives c_i†c_j=-h_j†h_i for i!=j. A legal low-charge hop moves one hole from charged source to neutral target and preserves its signed Q. On no-double site-major states, the f-species hopping sign is exactly the one-hole CAR sign: every intervening occupied site contributes one fermion, independent of species; the unused species slot at each endpoint is empty. Thus the bilinear replaces h_j†h_i with f†_{j,s}f_{i,s} without a new sign. Moving charge s from black to white changes E by -s, selecting L^- for positive and L^+ for negative. The reverse is the Hermitian adjoint. This proves every nonzero column and support refusal; both charged endpoints or a doubly occupied target are excluded by fermion/no-double support and Gauss. Phases are retained in d*s0*b_D and in ordinary species CAR. The optional b_D cancels because every listed hop and gated ring preserves D.

Unprojected f operators obey CAR on the enlarged Fock space. Their projections into no-double or Gauss space do not themselves obey full CAR and are not claimed to. K_e is an even projected bilinear with local endpoint no-double factors; a global projector notation can be replaced by endpoint factors on the restricted domain. This does not imply a fine-lattice admissible native circuit for the redundant representation.

## Rings and gauge invariance

For an oriented simple even cycle define R_C as the product of L^+ on edges traversed along black-to-white orientation and L^- on edges traversed against it. Then R_C+R_C† is the alternating link ring toggle. For an elementary plaquette p,

    mathcal W (F_p S_p) mathcal W† = R_p+R_p†,

with F_p the source alternating projector. It preserves all Q and matter labels; the source W already maps S to the positive X product and the extra hole/species phase stays constant. Ungated ambient S_p is not asserted to equal this partial ladder ring: it can change signed low-charge labels or leave the low domain. The statement concerns the actual gated RK ring.

The commuting mathcal G_v generate a local U(1) action exp(i sum theta_v mathcal G_v). Their spectra are integers on this six-valent spin-half-link domain, so each angle is2pi-periodic. Under this action f_{v,s} transforms by exp(i s theta_v); L^+ on i->j transforms by exp(i(theta_i-theta_j)). Each displayed hopping monomial and each closed ring has zero total gauge charge. P_nd commutes with all generators. Consequently K_e and R_p+R_p† commute with every mathcal G_v, also as ambient operators with no-double projection. Gauge transformations act trivially on the constrained physical states, as a redundancy should.

This is an exact compact U(1) gauge-invariant quantum-link presentation of these native restricted operators. It is not a rotor representation, a new independent U(1) matter/link factorization of the physical carrier, electromagnetism, a continuum limit or an axiom-selected charge/action. The signed defect charge differs from total hole number; native hopping happens to preserve both species separately, but that is not identification of their generators.

## Finite controls and boundaries

The preregistered checker independently computes direct native Pauli-string phases and compares them to the proposed species-CAR/link-ladder operator with the full d*s0*b_D map. It checks24 actual L4 configurations across D=0,2,4,6,8,10,12,14,16,64, including the delivered globally supported same-sign exchange witness;256 allowed hop columns and2348 alternating ring columns agree exactly. A missing electron-to-hole minus fails all256 hop comparisons. An independent complete six-site three-label enumeration checks4860 species hopping columns against single-hole CAR signs. These are selected physical columns, not a full L4 census or proof by enumeration. The general basis and operator argument supplies the all-sector statement.

No new stochastic production, physical preparation, occurrence law, local schedule or coupling selection is supplied. Existing low-charge/projector, graph placement, ordinary composition and Hamiltonian use remain conditional premises. Exact state encoding is not an implementation of arbitrary classical injection: it is a specified unitary between the source physical subspace and a redundant constrained basis, with its intertwining algebra proved above.

## Preserved absolute-phase correction

Root independent review found that the original prose incorrectly assigned the D-dependent block factor to the increasing-order hole-basis identity. The earlier bytes are preserved. The correct identity is s0=(-1)^sumI; for I={0,1}, c0c1|11>=-|00>. The tested operator map is unchanged by explicitly retaining its extra b_D as an optional sector phase. Original hop/ring controls could not detect this absolute-basis error because they preserve D. A separate direct hole-vacuum control now tests all subsets for one through eight modes. No off-diagonal-in-D operator identity is claimed from the old controls.
