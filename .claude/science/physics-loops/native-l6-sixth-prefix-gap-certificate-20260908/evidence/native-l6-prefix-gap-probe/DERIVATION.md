# L6 adjacent-word census and inexpensive exact gap pilot

This is a bounded pilot, not an all-prefix certificate or coefficient calculation. The first rank-two proposal failed an explicit assertion on an external bridge and is preserved. The corrected result uses rank-three changes of B and rank-six changes of BB^T.

## Exact L6 support, independent of L4 counts

Literal lexicographic6^3 geometry has648 edges. For adjacent centers0 and36, the ten boundary edges occur once and one bridge occurs twice. Enumerating incident-edge perfect matchings with indistinguishable repeated bridge copies gives exactly five families: internal edge0 has225 pair sets; external edges3,15,18,90 each have9. The L4 sixth bridge is absent: the two outer collinear endpoints cease to be adjacent at extent6. There are187920 ordered words,2038 proper DP keys and1534 distinct proper masks. The only proper masks that are gauge cuts are the two singleton stars. CENSUS.json saves every key, mask and edge; no floating computation is involved. This does not enumerate unrelated sixth operators or straight winding-six transitions.

## Rank-six shifted inverse

Write K in bipartite form2[[0,B],[-B^T,0]], with canonical B0. For a prefix in one bridge family, deltaB consists of changes in the black center row, the white center column, and possibly the single external bridge entry. Thus deltaB=F G^T with at most three columns, exactly. For A0=B0B0^T,

A−A0 = U C U^T,
U=[F,B0G], C=[[G^TG,I],[I,0]].

The matrices may have redundant columns; the identity remains valid. For s=25/4 let R=(A0+sI)^−1. Positive definiteness ensures the Woodbury denominator I+C U^T R U is invertible. Then

Tr(A+sI)^−1 = Tr R−Tr[(I+C U^T R U)^−1 C U^T R² U].

Only a6x6 rational inverse is needed. Canonical A0 has eigenvalues3,6,9,12 with multiplicities32,48,24,4. Consequently R is exactly a cubic rational polynomial in the integer A0, obtained by interpolation. Its trace is the corresponding four-term rational sum. No diagonalization or approximate singular values enter the certificate.

## Fixed Newton upper bound

For every x>=0 and fixed c=5/2, the second Newton iterate is an upper bound to sqrt(x), including zero. Its trace form is

Tr sqrt(A) <= (Tr A+108c²)/(4c)+c[108−c² Tr(A+c²I)^−1].

Tr A=648 for every sign pattern. The canonical native energy is minus Tr sqrt(A0), with Tr sqrt(A0)=72+40sqrt3+48sqrt6. Bound these two radicals from below by exact integer-square-root rationals. Subtracting the prefix trace upper bound gives a rigorous unrestricted active ground-energy difference. A positive result also bounds every state in the fixed initial parity. No ordinary floating eigenvalue is used as evidence.

The five prospectively chosen degree-one rows (four distinct masks) all certify gap>=0.3945478578742174 in displayed units |t|=1; exact lower rationals are in PILOT_RESULT.json. They have symmetry-equal values but were not chosen for success. Corrected entire pilot costs0.23986s37.0625MiB. This is not a forecast for all1534 masks: exact rational denominator sizes and shifted-inverse costs may vary. No c retuning, prefix scan or integration was performed.

Singleton cuts are different: their unrestricted ground energy equals the canonical energy in the opposite initial active parity. Their fixed-initial-parity gap is the minimum active frequency. On L6 this is sqrt12=2sqrt3, using the canonical dispersion and odd singleton gauge implementer. The Newton vacuum-difference formula must not replace that separate parity bound. Other proper prefixes might yield negative Newton lower bounds; those must remain failures/indeterminate and require a prospectively specified stronger majorant rather than invoking positivity without a number.

The exact rank-six route removes the full108-dimensional rational inverse bottleneck. A future bounded all-prefix contract could cache equal masks and classify symmetries, but no such run is authorized by this pilot. The existing strictness proof remains untouched and is not treated as already reviewed numerical-gap evidence.
