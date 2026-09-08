# Native Record response: a mixed-variation identity and a static-action identification failure

## Status and source-bound question

Conditional finite native construction, not a gravity theorem or an action-selection principle. Repository pin: 2b42ebe4b6b4ee76b0fa1b8e668ad7775e946307. This probe uses the actual native edge/CAR interaction and physical Z Record instrument, with supplied preparation, phase sources, pulse ordering, Born/Lueders formation and ordinary tensor composition. No Poisson quadratic functional is selected or differentiated, and no logarithm of a chosen statistical weight is promoted to an action.

The current weak-field source-response note proves its response only after specifying a symmetric quadratic action, source term and density/test dictionary. Its corrected SELF_CONSISTENCY_FORCES_POISSON parent explicitly does not derive the solver from the axioms; its matched density-response columns fail the inverse-Laplacian comparison. GATE_B leaves the finite-core scalar, normalization and readout supplied. The concrete question here is whether a native source operation and actual Record test response automatically provide the symmetric response required for such a static-action identification. They do not. A complete native finite-history characteristic function instead supplies an exact mixed source/counting derivative. Its derivative types matter.

This is not a refutation of the conditional Poisson variational theorem, an equilibrium reciprocity theorem, or a general time-dependent action. It is a new native operational counterexample to identifying an arbitrary sourced Record response with a static scalar Hessian or symmetric inverse Hessian in the same source/test coordinates.

## Declared apparatus and chronology

Use virtual path 0--1--2--3 at positions (2i,0,0), with three physical edge qubits at (1,0,0),(3,0,0),(5,0,0). The tree code is its full eight-dimensional physical space, faithfully the even four-mode CAR sector. The native dictionary is B0=Z01, B1=Z01 Z12, B2=Z12 Z23, B3=Z23, with n_i=(1-B_i)/2 and T_ij=c_i†c_j+c_j†c_i. This is inherited from the native matter-instrument theorem, not a new tensor decomposition assumption.

Prepare occupations n0=n3=1,n1=n2=0. Let U_ij(c,r)=I-i r T_ij+(c-1)T_ij² with c²+r²=1. Freeze

    U=U01(3/5,4/5), W=U12(7/25,24/25),
    V=U01(5/13,12/13) W.

The readout evolution is V; edge23 has zero hopping coefficient. The physical source is the supplied diagonal pulse J(s)=exp(i sum_j s_j n_j), equivalently an integrated Hamiltonian source -sum_j s_j n_j. The sign is fixed here, not normalized after observation. The test observable uses the same occupation dictionary. After V, form all three edge-Z Records in fixed order, with no intervening dwell; all outcomes are retained. Their commuting product projectors Q_z give the exact joint occupation readout through the displayed B dictionary. Deleting each measured hopping and preserving each old Z is consistent; no restoration or postselection is used.

The initial preregistered preparation was U|1001>. Its first response is identically zero, a failed nonreciprocity candidate. Both source and raw result remain unchanged. Before further calculation a separate supplement specified the phase-enabled preparation

    |psi> = exp(i pi n0/2) W U |1001>.

This deliberately escapes the real-control symmetry and uses the already supplied occupation-phase resource. It does not claim that the first experiment produced a nonzero response. There was no parameter scan or subsequent retuning.

All support statements are physical: adjacent virtual edges have midpoint distance two. The whole T12 control can touch the three physical sites with diameter four. Occupation-phase controls on interior vertices likewise are two-site products at distance two. No nearest-neighbor physical two-qubit synthesis, source-selection rule, energy apparatus or autonomous scheduler is derived.

## General complete-history response identity

For this experiment, K_z(s)=Q_z V J(s), acting on its specified prepared input rho. Completeness gives sum_z K_z(s)†K_z(s)=I. The complete probabilities are

    p_z(s)=Tr[K_z(s) rho K_z(s)†].

Let o_i(z) be the occupation decoded from the three physical Records. Then

    m_i(s)=sum_z o_i(z) p_z(s)
          =Tr[n_i V J(s) rho J(s)† V†],
    R_ij=partial_sj m_i(0)
        =i Tr[rho [V† n_i V,n_j]].                 (1)

This is direct differentiation of the actual source unitary and the complete native instrument; the sign follows from J(s)=exp(+i s.n). It holds on arbitrary reference-correlated inputs after tracing a passive reference. It is a finite impulse-response identity, not a thermodynamic susceptibility.

More generally one can replace K_z by complete finite adaptive native history words K_h(s), retaining the full labels and the actual source placements. The derivative differentiates every source-bearing factor in its time order. A source inserted strictly after a prefix cannot change that prefix's outcome probabilities, since summing all its continuations gives the identity. This is the finite causal normalization statement; it does not assume a formation rate or continuous-time bath.

Define the operational characteristic function of the recorded data,

    F(s,lambda)=sum_h exp(i lambda.o(h)) p_h(s).

It is known from the full Record law, F(s,0)=1, and

    m_i(s)=-i partial_lambdai F(s,0),
    R_ij=-i partial_sj partial_lambdai F(0,0).     (2)

Equation (2) is the positive conditional response bridge delivered here. Source s and counting variable lambda have different roles: s is a native physical phase perturbation, whereas lambda weights readable output data. They cannot be identified just because both are coordinates in one scalar function. Symmetry of the entire Hessian in (s,lambda) pairs R with its transpose in the opposite mixed block, and does not force R=R^T. Locally taking a logarithm would not change (2), because F(s,0)=1; that optional cumulant convention supplies no physical action or source selection.

## Initial zero-response control

In physical edge-Z coordinates, hopping pulses and the initial occupation projector are real, while J(s)*=J(-s). Every Q_z is real. Therefore p_z(s)=p_z(-s) for the first preparation. All first derivatives vanish, including on nonconstant source directions. This is not an inverse Laplacian with the constant zero mode removed: every direction vanishes. The result does not say finite sources have no effect, since interference gives nonzero second-order response. It shows why a zero-source response extracted from this real preparation cannot itself supply a nondegenerate static field operator.

## Exact phase-enabled discrimination on two neutral sources

In the direct occupation basis, retaining the inert occupied mode3, the active initial amplitudes are

    (i 3/5, -i 28/125, -96/125).

After the sources and V the active output amplitudes are

    a0= i(3/13)e^(is0) -(2352/40625)e^(is1)+(27648/40625)e^(is2),
    a1= (36/65)e^(is0) -i(196/8125)e^(is1)+i(2304/8125)e^(is2),
    a2= -(672/3125)[e^(is1)+e^(is2)].

The three nonzero histories have exactly the occupations of the active particle at0,1,2 plus the inert particle at3; the other five histories have zero probability. Their probabilities are |a_i|², summing to one for every real source. At zero source they are

    727778241/1650390625,
    24693664/66015625,
    1806336/9765625.

The full occupation response is

    R = 1/528125 *
        [[-151776, -14112,  165888, 0],
         [ 151776,  14112, -165888, 0],
         [      0,      0,       0, 0],
         [      0,      0,       0, 0]].          (3)

This was obtained independently from even-Fock hopping and physical three-qubit native Pauli matrices, and again from the explicit amplitudes. Both row and column sums vanish: a uniform source is a fixed-total-number phase and cannot affect outcomes, while total output number is conserved. The inert mode produces another zero direction. These extra degeneracies are disclosed rather than removed by a fitted inverse.

Use two genuine neutral source directions u=e0-e2 and v=e1-e2, and the dual tests n0-n2,n1-n2. If C has these columns, the correctly paired neutral response is

    C^T R C = 1/528125 *
              [[-317664,-180000],
               [ 317664, 180000]].              (4)

Its antisymmetric component is nonzero: Rneutral_21-Rneutral_12=497664/528125. The determinant of its symmetric part is -61917364224/278916015625<0. Thus changing the overall sign cannot make this response symmetric or positive definite. A common invertible change of source coordinates with dual observable transformation is a congruence and cannot remove the nonzero antisymmetric bilinear form.

If m were the gradient of any real C² scalar source potential on this neutral plane, its Jacobian would be symmetric. Equivalently, for the response one-form m_u dx+m_v dy, the circulation around a small positively oriented rectangle equals (497664/528125) times its area plus higher-order terms. The finite coefficient proves failure of local integrability in this experiment. In particular this response is not either sign of the inverse of a symmetric Hessian on that plane. This is not merely a bad treatment of the constant mode or mismatched source/test normalization.

Removing readout propagation makes the phase-source response zero. Reversing the physical source sign negates R but preserves the reciprocity failure. Omitting the preparation phase restores the real-control zero-response result. These controls locate the nonreciprocity in the actual prepared interference and ordered dynamics.

## Separate amplitude sources and what Records cannot determine

The known microscopic history words define the forward/backward extension

    Gamma(s+,s-;lambda)
      =sum_h exp(i lambda.o(h)) Tr[K_h(s+) rho K_h(s-)†].

At lambda=0 it is a positive kernel in the source labels (a Hilbert-Schmidt Gram kernel), and Gamma(s,s;lambda)=F(s,lambda). On its equal-source, zero-counting diagonal it is one. Differentiating both source arguments together on that diagonal gives the commutator in (1), and differentiating lambda gives (2). The two terms have their origin in the ket and bra amplitudes, not an assumed scalar Poisson action.

The off-diagonal Gamma is not recoverable from complete classical Record probabilities alone. Replace each history word by K'_h(s)=exp(i chi_h(s))K_h(s). Every conditional completely positive map K_h rho K_h†, hence every Record probability and conditional matter state, is unchanged for every input. But Gamma obtains the factor exp(i[chi_h(s+)-chi_h(s-)]). For the actual h0 history choose chi_h0(s)=t s0 and all other phases zero. At zero sources the forward-only derivative changes by i t p_h0(0), with p_h0(0)=727778241/1650390625>0, while all physical Record statistics are identical. This is an exact phase-convention ambiguity of the source-controlled instrument dilation, not a claim that arbitrary controlled phase hardware has already been supplied.

A coherent comparison between source settings would require additional reference/control/readout and a fixed dilation. It could operationalize the off-diagonal functional, but that is another physical premise. Permanent classical Records by themselves do not fix it. Thus the full-history functional provides the correct causal mixed response without supplying a unique amplitude action, a static field equation, or a gravitational interpretation.

## Current-source consequence and prior art

The source-response bridge's symmetric H and same source/test coupling remain conditions. Native locality, number conservation and actual Record readout do not imply those conditions: (3)-(4) give an exact finite counterexample. An equilibrium preparation/relaxation principle or some other independently derived mechanism must explain why the relevant sourced physical response has the required reciprocity and positivity, and why that response is the same operator used for propagation. Neither choosing a quadratic functional nor assembling a finite metric-shaped matrix answers this identification.

The live PR7997 source at774374271180405d5c2522010511adbd2c906236 was retrieved; its N0, interpretation fence and N6 explicitly keep source/physical meaning and assembly selection open. I inspected those scope sections, not its full 599-line algebra or all inherited scripts. It is not used as a mathematical premise here.

The response-commutator and doubled-source techniques are established. See Kubo, Statistical-Mechanical Theory of Irreversible Processes I (1957), https://doi.org/10.1143/JPSJ.12.570, and Haehl, Loganayagam and Rangamani, Schwinger-Keldysh formalism I, https://arxiv.org/abs/1610.01940 (standard doubled evolution and source distinctions). The finite equations above are proved directly and do not import a thermal Onsager hypothesis. The contribution claimed is the actual native Record/phase-source typing, exact neutral-plane discriminator, and amplitude-functional identifiability boundary on this carrier, not invention of Kubo or Schwinger-Keldysh theory.

## Evidence and remaining obligation

The original zero-response and separate supplement preregistrations and outputs are retained. physical_check.py has20 exact controls; functional_check.py has23 additional controls and explicitly reuses the physical result through runpy. The independent even-Fock route supplies the raw response comparison. All eight histories are retained per preparation. Two actual scratch mutants fail assertions (omit preparation phase; change the physical Record-to-occupation dictionary). Counts are finite evidence, not proofs of the general statements. No numerical fitting, random samples or continuum approximation is used.

Hardest remaining obligation: derive the physical preparation/source/readout principle that selects a reciprocal equilibrium response and identifies it with the same action/propagation operator. This work supplies a conditional operational response identity and a precise failure of one proposed identification; it does not close the gravity or native probability supplier.
