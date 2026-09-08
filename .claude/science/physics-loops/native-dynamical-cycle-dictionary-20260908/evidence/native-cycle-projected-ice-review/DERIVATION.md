# Independent projected-cycle bridge review

The proposed operator bridge is valid under explicit new supplied-Hamiltonian/constraint premises. It is not a native-hopping derivation. General proof below; finite phase controls incheck.py are supporting checks only.

## Phase flatness

For connected even periodic cubicL≥4, letX_b be the computational strings with allB_v=−1. The incidence equations have solutions because the numberofvertices iseven, and X_b is an affine binarycycle-space torsor. Native parent Eq2 and Theorem1 supply commuting canonical cycle checksS_C withXsupportC and a consistent all+1 code. Within each admissibleBfiber that complete-cycle code has rankone. Letφ=Σ_x c_x|x> be its nonzero normalizedvector. Cycle-space transitivity and monomialunitarity imply all|c_x| equal and nonzero. DefineD|x>=c_x/|c_x| |x>. FromS_Cφ=φ, the monomial phaseα_C(x) obeysα_C(x)c_x=c_(x+C), henceD†S_CD|x>=|x+C>. This works simultaneously for everycanonicalcycle, not just a locally chosen face. No phaseholonomy remains because existenceofφ establishes globalconsistency. Without consistent canonical cycle signs this argument fails; arbitraryfrustrated signassignments are not covered. D is a generallynonlocal diagonal changeofbasis, NOT a supplied efficientlocalphysicalgate.

IndependentL4 construction uses192edgequbits and129fundamentalcycles represented as Pauli bitmasks, never a2^192matrix. Eachof192canonical square operators exactly equals its unique fundamentalcycle product, with fullcomplexphase included; allsquarechecks commute and squaretoI. This directly tests the potential phase obstruction. No numeric ice enumeration or giantmatrix was used.

## Exact ice compression

Define ice literally by degree3 of n_e=(1−Z_e)/2 on the sameedgequbits. At eachcorner of a square, togglingits twoincidentfaceedges preservesdegree3 iff exactlyone isoccupied. Thus bothinitialandfinalstrings areice iff the fourfacebits alternate. LetF_p be the diagonal projector onto patterns0101 or1010 aroundthecycle, andX_p the unsigned fourbit toggle. F_p commutesX_p andthemonomialS_p. Onicespace,

D† Pice S_p Pice D = F_p X_p restrictedtoice.

D commutesPice andF_p becauseit isdiagonal. Therefore the finite restricted Hamiltonian−JΣPiceS_pPice+VcouplingΣF_p is unitarilyequivalent to theordinary suppliediceHamiltonian−JΣF_pX_p+VcouplingΣF_p. Thisincludes fulloperator/spectrum correspondence ontheentire ice span, not onlyoneclassicalstate. Connectedcomponents andwindingsectors remain; it doesnotselectone orjustifyanensemble. J,Vcoupling remain new suppliedcouplings.

The restriction can be written with local gatedcycletermsF_pS_p ontheinvarianticespace. It must notbe replaced by the ungated ambientΣS_p evolution: Pice generallydoesnotcommuteS_p, so barecycleevolution leaks. A hardconstraint orsuchgating isadditionalphysicalinput. NativeT_ij=iA_ij(B_i−B_j)/2 stillannihilates the entireallBminusfiber. Nothinghere turns that zerohopping intoicekinetics. Droppingfixedcyclecode also forfeits theoriginal faithfulfixed-sector evenCAR interpretation as the selectedphysicalstates; the ambientPaulioperators continuewell-defined.

## Local frustration cost

WriteN_v fornumberofvertices toavoiddimension/couplingVconfusion. Thereare3N_v positivelyrootedfaces. Foranynormalizedψ supportedonice, |<S_p>|≤<F_p>: the compressedselfadjointpartialtoggle has squareF_p andspectralvalues0,±1. At arootvertex, its threeoutgoingbits contain anequalpair; at mosttwoofthree rootedfacescanalternate. ConsequentlyΣ_p F_p≤2N_v onicespace and

Σ_p <(I−S_p)/2> ≥ (3N_v−Σ_p<F_p>)/2 ≥ N_v/2.

This is a state-independent lowerbound for the specifiedsumofcyclepenalties, not a tightminimum claim, not a nativeenergyLedger bound andnot a universalno-go. It explains why theprojectedbridge cannot simultaneously keepalllocalS_p=+1. It is strongerthan merelyexhibitingonebadicebasisstring but has a differentrole from thepositiveHamiltonianbridge.

## Placement and duplication check

Read currentmain native matter/instrument Eqs1–4 andcodeTheorem1, andtargeted localcycletransport source searches. Existing scratch native-ice-overlap and local-cycle-escape establish incompatible simultaneousfixedcycle+literalice constraints, includingexponentialprojectionbounds; theydonotestablish this compressedcycleHamiltonian equivalence. Targeted searches didnotlocatethis particularpositivebridge inthosemainparents; noexhaustive repository/openPRnoveltyclaim.

The sameabstractedge assignment isexplicit. Nativephysicaledgecenters are2v+e_a; neighboring graph-edgecenters are generallynotnearestneighbors oftheoriginalfinecubicphysicalsite lattice. A wholeS_p contains orderedZdressings beyonditsfourXedges. F_p isfour-edge diagonal; F_pS_p hasbounded localstar support but isnot thereby anaxiom-admitted one-site or nearest-neighborinteraction. ThediagonalD neednotbelocal. Thus exactalgebraic equivalence doesnot supplyphysicalactionselection, dynamics/readout or a newprimitive. AllphysicalHamiltonian/iceconstraint/placement/probabilitypremises remainvisible.

Disposition: positive exact conditionaloperatorbridge passes; native-hopping orfixedcode identification remainsfalse. No formalN1/audit verdict or claimofphysicalunification.
