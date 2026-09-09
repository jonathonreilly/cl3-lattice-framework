---
claim_id: records_register_colour_only_through_triality_and_singlets_the_su3_case_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "Conditional finite SU(3) one-rishon tensor model: diagonal gauge-invariant algebra, charge/orientation generators, singlet and commutant dimensions, joint Gauss eigenbasis resolution, necessary triality, and specified colour-rotation comparisons. A support proof gives the diagonal-intersection formula on finite abstract graphs for the stated N=2,3 representations. No arbitrary-state tomography, physical Record realization, confinement, general-N monotonicity or parent-campaign acceptance."
upstream_dependencies: [minimal_axioms_2026-06-29]
runner: scripts/records_register_colour_through_triality_su3_check_2026_09_04.py
---

# Diagonal gauge-invariant data in the supplied finite SU(3) model

Original date: 2026-09-04. Corrected source: 2026-09-08.

**Type:** bounded_theorem
This is conditional supplied-model mathematics, with no scientific audit grade.
Formal audit is deferred by the owner until a solid TOE. Historical audit scheduling
and historical claim labels do not direct current landing cadence.

Primary: [finite checker](../scripts/records_register_colour_through_triality_su3_check_2026_09_04.py).
Evidence: [genuine runner cache](../logs/runner-cache/records_register_colour_through_triality_su3_check_2026_09_04.txt).
The exact original note, runner and cache remain in the outside-docs correction packet
`.claude/science/physics-loops/su3-7933-correction-20260908/originals/`.
The original 22 checks and numerical rows remain; B3 and C7 now assert the previously
unguarded quantities. Additional controls state the limits of the positive results.

## Premises and interpretation

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) govern interpretation:
physical sites have an M2 local algebra on the nearest-neighbour cubic lattice, and
readout is determined by permanent Record content. They do not supply this tensor
carrier, a preferred measured basis, Born probabilities, a dephasing channel, gauge
invariance or a physical process forming the proposed readouts. Here these are
explicitly supplied mathematical structures. No new axiom or physical bridge follows.

A corner has N Jordan-Wigner fermion modes. A link has the one-rishon space
`L_e = span{|i,a>, |j,a>} = C^2 (endpoint) tensor C^N (colour)`. For N=3 this is
six-dimensional, not one physical M2 site or two physical qubit Records. Multi-site
encoding would require its own construction. The dimer and open three-chain are
abstract incidence graphs; the three-edge triangle is also abstract. A direct triangle
cannot be a nearest-neighbour cubic-lattice subgraph, because each edge reverses
lattice parity. A subdivided graph or encoded realization is not excluded, but is not
specified. All composition here is an explicitly supplied tensor product.

The original #7908/#7914 construction, proposed Record outcome map, different unitary
U2 connection and archived colour campaign are dated context only. The corrected
#7908/#7914 sources now on main likewise distinguish basis populations from arbitrary
states, and supplied tensor algebra from physical Record realization. This unit
recomputes its own quantities and uses neither those parent proofs nor their cached
results; agreement of selected counts does not restore the historical overclaims. In particular the local channel below is supplied, not derived
from the proposed map or from the current Record memo.

```text
psi_(v,a): Jordan-Wigner annihilator, mode N*v+a
U_e^(ab) = -|j,b><i,a|; products U U = 0 on the one-rishon factor
E_(e,v)^a = P_v tensor T^a; rho_v^a = psi_v^dag T^a psi_v
G_v^a = rho_v^a + sum_(e at v) E_(e,v)^a; Q_v = n_v^f + n_v^r
R = diagonal operators in the supplied fine basis
I = commutant of all G_v^a; P_G = their joint-kernel projector
D(M) = sum_r P_r M P_r: supplied dephasing onto R
H_hop = -t sum_(e,ab) eta_e (psi_(i,a)^dag psi_(j,b) U_e^(ab) + h.c.)
```

The particular nilpotent U is nonunitary; this does not exclude other unitaries on
the Hilbert space. H_hop is only an example in I. No ground state or evolution is used.
The fine-basis probabilities below use the separately supplied Born rule.

## Theorem 1 -- the construction: the `SU(3)` carrier and its Gauss algebra

**Conclusion.** (1) The `6` Jordan-Wigner matter modes of the dimer satisfy the canonical anticommutation relations exactly; the one-rishon `U(3)` link has `DL = 2N = 6` with `U U = 0`, giving `dim R = dim H = 2^6 x 6 = 384`; every generator entry is dyadic of magnitude `<= 4`; and `G_v^3`, `G_v^8` and `Q_v` are diagonal, hence in `R`. (2) The Gauss generators **close on `su(3)`**: with `f^{abc} = -2i tr([T^a,T^b]T^c)` read off the generators themselves -- `f_123 = 1`, `f_458 = 0.866025 = sqrt(3)/2`, `f_147 = 0.5`, `f_156 = -0.5` -- `[G_v^a, G_w^b] = i f^{abc} delta_vw G_v^c` holds for all `2 x 2 x 8 x 8` pairs to `4.44e-16`, and different corners commute. (3) The covariant hop is gauge-invariant **exactly**: `[G_v^a, H_hop] = 0` with `nnz = 0` and no tolerance for all sixteen dyadic generators, `0.0` with the true `lambda^8/2`, and `[Q_v, H_hop] = 0` as well. (4) The corner Casimir `C_v = sum_a (G_v^a)^2` commutes with the whole gauge algebra and has spectrum `{0, 4/3, 3, 10/3}` -- the `1`, the `3/3bar`, the `8` and the `6/6bar`, exactly the corner colour representations produced by tensoring the corner matter Fock space `Lambda(C^3) = 1 + 3 + 3bar + 1` with its link end (`1` or `3`). (5) The carriers actually built are the dimer (`384`, densely), the 3-chain (`18432`) and the triangle (`110592`, sparsely). The **`SU(3)` plaquette is rejected and never built**: `2^12 x 6^4 = 5308416`, whose twelve fermion modes alone would need a `4096 x 4096` factor and whose component graph would need `~2 x 10^8` edges.

**Proof.** Item 1 is exact anticommutator and nonzero-entry counting on dense `384 x 384` matrices. Item 2 evaluates the structure constants by trace and compares `256` commutators entrywise, `[numerical, 1e-13]` because the true `lambda^8/2` carries `1/(2 sqrt 3)`. Item 3 is sixteen sparse commutators tested by `nnz == 0` on dyadic operators, plus a floating-point cross-check. Item 4 is a dense `384 x 384` eigen-decomposition. Item 5 is integer dimension arithmetic. Exact except where tagged.


Arithmetic boundary: dyadic rescaled generators permit the reported exact zero
comparisons in these bounded computations. True normalized T8, Casimir spectra,
exponentials and compressed Gauss ranks use floating arithmetic at the stated
runner tolerances. A numerical eigensolver does not become an exact-arithmetic
certificate by printing an expected rational spectrum.

## Theorem 2 -- diagonal intersection and its measured scope

For diagonal D, `[D,G]_(rs)=(d_r-d_s)G_(rs)`. Thus R intersect I consists of functions
constant on the graph of off-diagonal generator support. In this model its components
are exactly the fibres of `(n_v^f; o_e)`. Therefore
`dim(R intersect I)=(N+1)^V 2^E` for N=2,3 on any finite abstract graph of these factors.

Proof of the extension beyond the nine direct censuses: at fixed matter number k,
all k-subsets of colours connect by root operators replacing an occupied colour by
an empty one. Every occupied link endpoint has the connected fundamental colour
graph. A sum of local generator actions cannot cancel such a move: moves on different
tensor factors produce different target basis states. Taking their real/imaginary
Hermitian generators gives the same union of support. Each fibre is therefore
connected, and particle numbers and endpoint orientations are unchanged by all
moves. This proves both directions, not merely that each edge stays inside a fibre.
For N=1 the empty-generator comparator has one basis vector per fibre; it is not a
full U(1) commutant. Its dimer full Q-commutant dimension is 10, rather than the
empty-generator dimension 64, although both diagonal intersections have dimension 8.

All nine direct component counts are retained:

| Graph | Empty-generator N=1 | SU(2) | SU(3) |
|---|---:|---:|---:|
| dimer | 8/8 | 18/64 | 32/384 |
| three-chain | 32/32 | 108/1024 | 256/18432 |
| triangle | 64/64 | 216/4096 | 512/110592 |

Entries are `dim(R intersect I)/dim H`. The dimer support has 3840 edges; the largest
computed graph has 110592 nodes and 2322432 edges. No SU(3) plaquette graph is built.
Its diagonal-intersection dimension 4096 follows from the support proof; the SU(2)
plaquette value is 1296. The corresponding Hilbert dimensions are 5308416 and 65536.

For N=2,3, the endpoint Casimir is `C_F P_end`, with `C_F=(N^2-1)/(2N)`.
It recovers orientation, and Q minus endpoint occupancy recovers matter number.
Thus `{Q_v,E^2_(e,end)}` generates the intersection. On the SU(3) dimer these give
32 levels; Q alone gives 23, E2 alone 2, and Q mod 3 alone 9. The actual sum of
squared electric generators now must match `(4/3)P_end` within 1e-12 (original
residual 2.2e-16); the original B3 omitted this acceptance condition. Five declared
projectors and all charge/endpoint generators have the reported zero commutators.

All six tested single-colour occupations/projectors fail to commute. Only two of
eight local Pauli-Z strings survive, giving eight tested string products rather
than 32 dimensions. This statement is about that string class; arbitrary polynomials
of the joint charge/orientation data do span the whole finite algebra. All 32
component projectors commute with all generators. Gauge-conjugating the fine basis
leaves the intersection fixed; arbitrary basis changes are not asserted.

Integer Weyl/Dyson character arithmetic retains the SU(3) Gauss/commutant rows
`4/146, 10/4692, 14/31412, 34/991584` for dimer, chain, triangle and plaquette.
It separately reproduces SU(2) plaquette `82/356306`; this numerical agreement does
not import the old parent claim. Character checks retain SU(3)
`M00=1, M10=0, M11=1, M30=1, M22=2, M33=6`, SU(2) `M20=1, M40=2`.
The dimer Gauss hull has 12 fine patterns in four readable classes; the chain hull
has 78 in ten classes. No individual fine pattern solves the Gauss law in either
case. Numerical compression gives four and ten orthogonal rank-one projectors
respectively, resolving a joint eigenbasis and a maximal commuting algebra on the
Gauss subspace. It does not distinguish every quantum state.

For an explicit counterexample in the dimer's lexicographic JW basis followed by
link index, let u have amplitudes `(1,-1,1)/sqrt(3)` at indices `(144,241,290)`;
let w have the same amplitudes at `(186,283,332)`. These are orthogonal epsilon
singlets. Then `(u+w)/sqrt(2)` and `(u-w)/sqrt(2)` are orthogonal singlets with
identical probabilities for all 384 fine outcomes, hence all 32 readable atoms.
Dephasing u preserves those probabilities but changes the total Gauss Casimir
expectation from 0 to 2. Neither tomography nor singlet certification follows
from the diagonal outcomes alone.

## Theorem 3 -- necessary triality and specified rotations

`omega^Q_v`, with `omega=exp(2 pi i/3)`, belongs to R intersect I. Singlets must
have triality zero at every corner, since the center acts trivially on a singlet.
The converse fails: the dimer triality-zero subspace has dimension 36 while the
Gauss sector has dimension 4. Fine basis state 21 has Q=(0,3), triality zero, and
total Gauss Casimir 2. The singlets u,w above have Q=(3,0) and (3,3): triality is
only one coarsening of readable charge/orientation data.

The original dimer construction has five highest-weight vectors, then three chosen
weight partners of Casimir 4/3, mean Q0=2.2, and other-corner Gauss residual 7.02e-17.
The partners have pairwise fine TV=1 against the first partner. At theta=0.7 about
the declared axis, TV is instead 0.1175789063577555 = sin^2(0.35), with survival
0.882421094 = cos^2(0.35); a Cartan rotation gives TV=0. The triplet-span residual is
1.59e-16. Readable atom deviations are 1.110e-16 for the specified comparisons and
1.665e-16 over eight axes times five declared angles. These are finite checks;
invariance of the algebra proves aggregate equality for any gauge rotation.
The chain has eleven highest-weight vectors, other-corner residual 1.65e-16,
partner TV=1 and a scan maximum TV=1, not TV=1 at every scan point. Its readable
deviations are 6.939e-17 for partners and 1.527e-16 for the scan.

The tested triplets have ordered triality distribution `(0,1,0)` for k=(0,1,2),
meaning triality one. The Gauss examples have `(1,0,0)`. C7 now asserts all four
dimer triplet/rotated distributions, all three chain triplet distributions and
both Gauss distributions. The chain retains 21 of 78 hull patterns at n0f=3,
including the epsilon_abc baryon channel.

For a tensor transforming in a nontrivial irreducible representation, matrix
elements between two invariant states would form an invariant vector in that
representation; they therefore vanish. This proves the selection rule when the
operator really has that transformation type and contains no trivial component.
The numerical checks exercise 41 dimer list entries including eight repeated link
operators, and 42 chain entries; residuals are 1.081e-16 and 4.484e-16. They are not
an enumeration of all such tensors. The invariant examples retain compressed ranks
[3,2,4,4] on the dimer and [7,10,10] on the chain.

## Theorem 4 -- the computed comparisons and Cartan exclusion

The readable fraction of I rises from SU(2) to SU(3) on the four computed graphs:
dimer 0.1957 to 0.2192, chain 0.04751 to 0.05456, triangle 0.01481 to 0.01630,
plaquette 0.003637 to 0.004131. This disproves a decrease between these two N values;
it does not disprove monotonicity generally or establish a trend for other N.
The readable fraction of R falls for the three tested comparator values; on the
plaquette it is 1, 0.019775, 0.000772. Gauss dimensions 82 and 34 are a pairwise
comparison, not a general-N law. SU(3) admits the defining triplet (p,q)=(1,0);
`p-q=0 mod 3` is a zero-center-charge condition, not an irrep-admission rule or a
sufficient singlet condition.

Both Cartan generators are diagonal but fail to commute with the full gauge
algebra. Their compressed Gauss blocks vanish (reported maximum 1.1e-31). The
frame-dependent observable `2 rho_0^3` has expectations
`(0.2,-0.2,0,0.152968437)` on the four displayed states. It is outside the supplied
invariant algebra; the exclusion is not a derived prohibition on physical readout.

## Boundaries and unresolved changes of model

The result is conditional finite algebra, not confinement or a physical Record
formation law. It preserves the supplied Fock, tensor, gauge and Born structures
without inferring them from the memo. Adjoint matter alone need not trivialize
triality when fundamental one-rishon endpoints remain. Larger rishon number is a
new model, with no strict-increase theorem: at full N_e=6 filling on a SU(3) dimer,
the link is one-dimensional, traceless endpoint generators vanish and the matter-only
readable dimension is 16, below the N_e=1 value 32. Other fillings, adjoint designs,
physical encoding and dynamics remain open; no independent-wall or route-quota
claim is made. No continuum, area law, string tension, physical colour identification
or complete parent campaign is established here.

## Execution and correction trace

The 2026-09-04 source/cache remain exact historical provenance, including the old
22/0 output and its incorrect labels and two unguarded conditions. The independent
original review ran it once and demonstrated those false positives. The current
runner retains every original check ID, strengthens B3/C7, and adds explicit phase,
dephasing, triality and rotation boundary controls. All actual results and any
failed attempts are recorded in the correction evidence. The runner declares its
own note and current memo, verifies their hashes before computation, and its cache
binds their complete input union. There are zero local helper modules. Only genuine
execution after the final note/input freeze supplies the current cache; status
labels are not evidence or scientific certification.
