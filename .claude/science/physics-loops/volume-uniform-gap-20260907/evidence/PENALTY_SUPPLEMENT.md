# A supplied penalty extends the gap to the full finite qubit register

This is an additional mathematical hardware encoding, not a native control implementation. The root supplied the penalty candidate after the finite-PW supplement. Keep R>=1 and q_R=ceil(log2 D_R). Let W_R embed the full finite link carrier in C^(2^q_R), P_e be its code projector, and Q_e=I-P_e. Supply a penalty Delta>=4/a and define

 K_e^hardware=W_R K_(e,R) W_R*+Delta Q_e.

It has a unique zero vector, the embedded constant, and all other energies are at least4/a; a fundamental code state attains4/a. Regrouping three outgoing links therefore again gives an onsite gap1 after multiplication by a/4, independently of R, volume, or how many unused states the qubit register contains.

For each actual plaquette take its compressed Hermitian real-trace operator J_(f,R), and extend it by zero whenever any of its four link registers is outside its code. Denote that operator J_f^hardware. It has norm at most1, commutes with each local code projector, and acts only on the same four link registers. The centered grouped interaction -(av/4)sum_(three pairs)J_f^hardware thus has the unchanged common range and norm bound3av/4. Extend each finite link gauge representation trivially on Q_e. This is a genuine direct-sum representation of both endpoint groups; the penalty and every extended plaquette commute with it.

The same imported c1,c2 therefore imply a unique finite-volume ground and full-register gap at least2/a in the same small-av regime. To prove that this ground actually lies in the product code, rather than merely presume the penalty suffices against all interactions, interpolate

 H(s)=sum_e K_e^hardware+s V^hardware,  0<=s<=1,

where V^hardware is the supplied deficit potential or its centered version; their scalar difference is irrelevant. At each s the perturbation norm satisfies the same smallness condition, so the finite-dimensional ground projection is rank one and separated by a positive gap. It depends continuously on s by the resolvent spectral projection. Every P_e commutes with H(s), hence its expectation in that rank-one ground is exactly0 or1. The expectation is continuous and equals1 at s=0, where the ground is the product of encoded constants. It is therefore1 for every s and every e. This proves exact product-code membership at s=1 without an additional numeric inequality involving v and Delta.

On the product code H(1) is precisely the finite-PW Hamiltonian. Consequently its ground energy and ground vector agree with those of that carrier, while the full register—not just the code—has the stated lower gap. The unique ground is a physical singlet by the finite-product SU3 character argument; the physical reducing restriction retains the lower gap. The finite open-graph padding argument still works because the added register factors are decoupled penalized electric operators with gap4/a.

For each fixed R and supplied Delta, the fixed whole-group lattice family also meets the imported GNS theorem on finite-dimensional onsite registers. Its thermodynamic ground satisfies omega(P_e)=1 at every fixed link, by the finite ground-code identity. It inherits the full-register GNS gap and the physical fixed-space restriction. This is not an interchange of R and thermodynamic limits, and no convergence as R tends to infinity is asserted.

The penalty and zero-off-code operator extension are additional specified operators. Their existence preserves four-register support but does not provide a gate compiler, a native two-qubit interaction construction, a bounded switching schedule, or a preparation algorithm. The original inert-complement counterexample remains valid when this penalty is absent.
