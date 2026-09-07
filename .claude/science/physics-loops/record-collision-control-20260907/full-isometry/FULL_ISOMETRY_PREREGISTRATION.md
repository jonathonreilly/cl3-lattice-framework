# Block07 full native isometry: preregistration before execution

2026-09-07. Same reduced nine-qubit carrier, K, source head10/fuel1/label00/old Record0, all TWO matter states and FOUR battery levels, complete interaction graph and expanded workspace. This is all8 input columns, not a selected normalized outcome. No extra ancillas are needed beyond the existing two collision-label qubits. Globally K-commuting controls of Pauli weight at most3 and supplied pulse timing/coherent typing are explicit assumptions.

Let q=n_f, p+=(I+Y_x)/2, p-=(I-Y_x)/2, a=1-q, n=n_b1, z-=(I-Z_x)/2. Define exact controlled flip C(P,l)=exp[-i(pi/2)P(X_l-I)]; when P is a projector commuting with X_l this equals (I-P)+P X_l, including its phase.

Freeze these NINE pulses, in order:
1. C(p+ n,l0).
2. C(p+ n,l1). These mark bright upper-half inputs as refusal11 while leaving accepted ready labels00.
3. exp[-i(pi/2) p+ (|0><1|_f |1><0|_b1+h.c.)].
4. exp[-i(pi/2) p- X_f]. Accepted bright-low and all dark branches now have fuel0, correct battery shift2 or0, and common phase -i. Overflow bright-upper branches stay fuel1 with phase1.
5. C(a,l1).
6. C(a z-,l0).
7. C(a z-,l1). These write coherent native signs: edgeZ+ maps ready00 to01, edgeZ- to10. Edge amplitudes are preserved rather than measured or normalized.
8. exp[-i(pi/2) a (|01><10|_head+h.c.)]. Accepted branches move head with another -i.
9. exp[-i pi a]. This cancels the common accepted phase -1; refusal phase remains1.

Each generator has Pauli weight at most3. All controls commute with K, old Record Z_r and total head number as FULL Pauli sums. The q0-conditioned edge-Z controls commute with K because the matter-energy term vanishes in that fuel sector. Pulse3 transfers bright energy2; pulse4 changes fuel only in zero-active-energy dark sector. Controls1/2 depend only on conserved Y_x and n_b1. No statement is made about nearest-neighbor routing, formation/permanence of the fresh label before decoupling, or arbitrary gate controllability.

Frozen target isometry on source matter/battery input psi:
    V psi = sum_z |head01,f0,label z> [P_z p+ tensor T2 + P_z p- tensor I] psi
            + |head10,f1,label11> [p+ tensor n_b1] psi.
Here P_z=(I+zZ_x)/2, labels +=01,-=10, and T2 raises battery by2 with hard cap4. The refused branch retains its source matter/battery state. F=p+ n_b1 is the ONE combined-sign refusal square root because sum_z S_z†S_z=I-F. Relative phases and interference between initial bright/dark components must match this exact isometry, not just probabilities.

Checks: expand all9 generators as exact Pauli dictionaries; maximum weight3; exact global commutators and Hermiticity; exact analytic exponential/unitarity identities. Apply sequentially to all8 source basis columns, preferably computational edge basis so coherent Y± cross terms are present. Independently construct the target above by exact matrix/projector action; compare every amplitude exactly. Verify V†V=I8, full energy intertwining, old Record/head conservation, and exact cap refusal on every column. Include one coherent mixed bright/dark battery input and sign-relative-phase/drop-refusal adverse mutations, while all-column equality remains the primary test. No parameter changes after results. 180seconds/180MiB, one BLAS thread; no full dense512-unitary required. Preserve this preregistration and source/output hashes.
