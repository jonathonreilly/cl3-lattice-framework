# Five-event native flux Record escape: bounded conditional construction

## Frozen scope and carrier

This follows POSITIVE_ESCAPE_PREREGISTRATION.md and native_escape_check.py, executed before this explanatory proof. It is a positive escape from the earlier one-event and direct-two-event obstructions, on a larger prepared carrier with a supplied finite controller. It is not an axiomatic gate compiler, a minimal flux Lüders instrument, or a finite-battery realization.

The CAR path has twelve vertices in the fixed order
(a0,b0,c0,d0,a1,b1,c1,d1,q,qbar,r,anchor).
There are eleven native BKSF physical edge qubits e0,...,e10. Use the even fermion-parity code, dimension 2048. This tree has no cycle stabilizers. In its occupation dictionary the physical bit xj is the prefix parity n0 xor ... xor nj; consequently B0=Z0, Bj=Z(j-1)Zj internally, and B11=Z10. The 256 inputs have arbitrary eight data occupations, q=0, qbar=1, r=parity(data), anchor=1. Thus every input has even total parity, and the physical computational codewords are orthogonal. Preparing the correlated reference r is an input preparation assumption, not supplied by an arbitrary set injection.

Define the four oriented Z4 labels ai=a0+2a1, etc., and flux F=(a+b-c-d) mod4. The boundary labels are prepared occupation data, not already permanent Record signs. All eleven edges start live; their native coefficients and controlled pulse sign are taken in the displayed positive path convention.

## Actual event and pulse instrument

Record e0,e1,e2,e3 in that order with no intervening matter dwell. Their outcomes are the actual physical bits x0,x1,x2,x3 (Z sign (-1)^x). Every selected edge is a bridge. After each deletion its left endpoint has become isolated; after four deletions the low four vertices are isolated and modes4,...,11 still form a path. The native ready-input projectors are Qj,x=(I+(-1)^x Zj)/2. No generic Boolean quantum gate is used.

Let z=(x0,x1,x2,x3). A supplied classical controller with sixteen possible history states reconstructs li=xi xor x(i-1), with x(-1)=0, and computes
  L=(l0+l1-l2-l3) mod4,
  c=x3 xor floor(L/2).
The event schedule/pulse clock is additional supplied control; sixteen counts the stored history, not a complete autonomous controller implementation.

If c=1 apply U=exp[-i(pi/2)T8]; if c=0 apply identity. Then Record e8. Here T8 is the actual native whole hopping term joining adjacent CAR vertices q and qbar. With the path edge ordering,
  A8=X8 Z7, B8=Z7 Z8, B9=Z8 Z9,
  T8=(i/2) A8(B8-B9)=Y8(I-Z7Z9)/2.
This identity was checked on all eight physical three-bit basis states, including its complex phase. On the prepared subspace q xor qbar=1, so Z7Z9=-1 and T8=Y8. Therefore the pulse flips x8 and leaves every other physical bit fixed. Its phase is (-1)^(old x8). It swaps the q,qbar occupations, leaves all eight data occupations fixed, and does not act on any old Record site e0,...,e3. e8 is still a live bridge when recorded. Its removal disconnects the remaining path, so the final Record is permanent under the surviving native hopping terms.

For history z and final bit b the ideal branch map on the prepared carrier is
  M(z,b)=Q8,b U^c Q3,x3 Q2,x2 Q1,x1 Q0,x0.
Sum M(z,b)^*M(z,b)=I on the whole even-code space, since U^c is unitary and each event is a complete projective instrument. An outcome-register isometry is Vpsi=sum_(z,b) M(z,b)psi tensor |z,b>. This is an explicit finite isometry, not a relabeling of observed outcomes as a new physical measurement. The final Q8 is essential.

## Exact truth table and coherence scope

Let H=(a1+b1+c1+d1) mod2. Before the controlled pulse x8=x3 xor H, since q=0. Afterwards
  x8=x3 xor H xor c=H xor floor(L/2).
But F=(L+2(a1+b1-c1-d1)) mod4, whose high bit is exactly H xor floor(L/2). Hence e3 stores F mod2 and e8 stores floor(F/2), both as physical native Z Records. The checker exhausts all 256 labels, verifies every recovered data occupation, every old Record, the pulse guard and phase, and uniqueness of all 256 output physical codewords.

For fixed low history the conditional pulse phase depends only on H and therefore only on the final high Record bit. It does not resolve individual high occupations. Nevertheless the first four Records reveal the low occupations separately: superpositions with equal flux but distinct low data generally decohere when histories are discarded. The claim is nondemolition preservation of the orthogonal input basis and an isometry retaining complete history, not coherent Lüders measurement of flux alone. The output retains data as well as the two flux Record sites; it does not compress 256 states into four states.

## Load-bearing control, locality and energy imports

This is a controlled native instrument sequence. It does not evolve under an unmodified fixed H_R. Generic surviving hopping terms would move the high data and references. Setting the dwell to zero during the first four events, activating only T8 for the conditional pulse, and suspending the pulse interaction for the final sharp event are supplied bond selection and switching assumptions. No prior result is imported as proving that this selective control is available. With selected Hamiltonian g T8, g>0, the active duration is pi/(2g). Its physical Pauli support is the three consecutive edge sites e7,e8,e9, not a two-site physical nearest-neighbor gate. CAR adjacency and bounded whole-hop support are explicit; a two-site bounded-strength hardware synthesis is not proved.

The controller reads four already formed permanent signs and chooses one of two pulse actions. It contains a nonlinear sixteen-entry rule and a timed schedule. This is an explicit finite classical control resource, not a native Toffoli or an autonomous computation derived from the axioms. Initial preparation, ready Record apparatus, prescribed event occurrence and controller coupling are likewise premises.

The ideal selective unitary/projector calculation is not an energy ledger. Switching a Hamiltonian is generally work; the energy change of forming/deleting a Record edge requires its modeled battery apparatus. If a nonzero incoming hopping remains active at the final event, the usual independent-ready normalizable battery lift averages rotated effects and does not inherit this exact sharp truth table. The earlier battery obstruction cannot simply be bypassed by naming the pulse a control. This construction therefore isolates a positive information-processing bridge and identifies selective native hopping plus compatible work/Record apparatus as the remaining physical import. No exact finite-battery success probability or energy-conservation claim is made.
