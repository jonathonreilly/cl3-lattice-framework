# A possible stronger infrared input: nine-power tail after one-particle subtraction

New analytical derivation for independent review; no physical computation. Uses8062/8063 and the full-odd infrared theorem. Let Z=Y-L be the uniformly rapidly quasi-local odd creator whose vacuum image has quasiparticle number at least3. The subtraction L is the ACTUAL extracted linear creator, not an unsupported number projection of an operator.

Write N_epsilon=sum_{omega_l<=epsilon} a_l* a_l. On occupation vectors with particle number>=3 and total energy in(0,epsilon], every occupied mode is soft. Thus

 1_(0,epsilon](H) P_(>=3) <= N_epsilon(N_epsilon-1)(N_epsilon-2)/6.

This remains a diagonal positive operator inequality on the entire Fock basis, with the left side understood to include P_(>=3). Consequently, using CAR,

 ||1_(0,epsilon](H) Z Omega||²
 <= (1/6) sum_{i,j,k soft, distinct} ||a_k a_j a_i Z Omega||².

For a local parity-homogeneous D supported on m real Majoranas, move each annihilator through D using the GRADED commutator. Since annihilators kill Omega, the triple action equals a triple nested graded commutator applied to Omega. Each commutator flips parity, remains supported on D's sites, and has norm at most (2 C_B m/sqrt(Ncell)) times the preceding operator norm. The commutator types alternate anticommutator/ordinary commutator/anticommutator for initially odd D. Therefore

 ||a_k a_j a_i D Omega|| <= (2 C_B m)^3 ||D|| / Ncell^(3/2).

Decompose the uniformly quasi-local Z into odd dyadic shells D_n of support m_n=O(2^(3n)). The constant

 K_3=sum_n (2 C_B m_n)^3 ||D_n||

is uniform using any tail exponent p>9. Triangle inequality bounds every triple action of Z by K_3/Ncell^(3/2). The conical mode count #soft/Ncell<=C_D epsilon³ then gives

 mu_Z((0,epsilon]) <= K_3² C_D³ epsilon^9 /6.

No independence assumption on the three created particles enters. Shells individually need not have zero one-particle vacuum component: the number>=3 condition is used only for the FULL Z vector before shellwise bounds on triple annihilation. This avoids an invalid per-shell number assumption.

Stieltjes integration yields inverse moments for0<s<9 and inverse-vector powers q<9/2, with uniform low-energy remainder9C/(9-s) epsilon^(9-s). Existing local spectral convergence then gives the corresponding thermodynamic inverse moments. This is strictly stronger than merely reapplying the generic cubic tail to Z.

The argument generalizes to any uniformly quasi-local parity-homogeneous creator whose vacuum image has particle number at least r: factorial soft-number moment of order r, nested graded commutators, and p>3r give epsilon^(3r). It does NOT claim the required subtraction creator exists for every r without a separate construction. For r=3, existence is already supplied by linear subtraction.

Consequence for the fixed-U program: the higher-odd vacuum transition has much stronger infrared integrability, leaving the linear return as the lowest soft channel. This still does not control the interacting reference, mixed-flux histories, operator action on excited states, or all-u relative susceptibility. It is an exact candidate improvement to an input, not an interacting resummation proof.
