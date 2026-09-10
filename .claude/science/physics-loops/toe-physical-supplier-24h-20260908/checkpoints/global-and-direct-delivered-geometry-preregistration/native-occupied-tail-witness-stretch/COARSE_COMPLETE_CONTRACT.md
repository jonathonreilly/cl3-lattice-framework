# Complete coarse occupied-tail pruning contract

This replaces the incomplete full-operator wording in LITERAL_COARSE_CONTRACT6b4d for the proposed cheap witness. Original files and geometry runtime86c4 remain unchanged, unlaunched. The new test deliberately uses a DIFFERENT coarse approximant Dbar, not the accepted high-accuracy Dhat with omitted terms disguised as exact. No actual geometry or matrix is parsed here.

## Operator and rigorously charged tails

Let Qnodes be the accepted378-node Hermitian sum on[epsilon,16], epsilon=2^-32, with the correct projector sign sigma. Define

 Dbar=Qnodes+sigma V/(16pi), V=hA-h0.

The second term is exactly the N=1 high-frequency correction. It is rank2, supported on the original center/pair star sites. Every part of this Dbar is included in the local witness. Higher high corrections and the low endpoint correction are NOT included; their omission is explicitly charged by comparing Dbar directly to the true projector difference D.

The old uniform low-integrand bound C0<1071/25 yields low trace error<357*epsilon/25. The global21-node quadrature error is<6139(4/25)^21. The independently derived N=1 high error is

 (1/8)(9/64)[1+18/(64*5)].

The sum is<19/1000=.019. Thus ||D-Dbar||1<.019, before any separately accounted coefficient/input arithmetic. This is much coarser than the accepted fullDhat error, and it is a valid alternative for a lower witness. The leading local high term cannot be silently dropped: its omission would cost an order.1 upper bound. No new high moments, higher half moments or high-power overlaps are needed for this chosen N=1 term.

The accepted Qnodes coefficient/input approximation error must also be charged. Its already certified full input/coefficient allowance is far below1e-10, so reserve1e-10 here only after its source/acceptance is pinned. Do not use the fullDhat1.7e-13 error as though Dbar included all corrections.

## Exact local high contraction

For X=Z the fixed seven star unit vectors, the high block is

 sigma/(16pi) [Z*V X - Z*V Vsel H^-1 Vsel*X],

where Vsel denotes the selected basis map and is distinct from impurityV. Since impurityV is supported on these seven sites, Z*V Vsel is obtained from the same local-to-selected overlap block Z*Vsel, multiplied by the explicit signed7x7 impurity matrix. Therefore this adds no nonlocal scalar supplier. The literal Ward/resolvent overlaps from the predecessor suffice for both node and high terms; all phases and the positive/negative projector convention must remain consistent.

## Use the old metric honestly

The actual selected certificate gives ||H-I||<=e with e<8e-6. Choose the fixed inverse candidate Y=I; do not pretend H=I. Then ||H^-1-I||<=e/(1-e). Since ||Dbar||1<88 (from||D||1<87 and.019 approximation) and||Vsel||²<=b=1+8e-6, the local block operator error from this substitution is bounded by

 88b*(8e-6)/(1-8e-6)<.00071.

This is a block operator norm bound. To bound Frobenius error of the7x7 block, multiply bysqrt7<3, yielding<.00213. Omitting this dimension factor would understate the witness error. No metric refinement is required for this coarse test; old uncertainty remains visible.

Allocate additional block Frobenius error1e-4 for newly acquired scalar/kernel intervals and1e-5 for all finite arithmetic/coefficient rounding, including the1e-10 accepted node-input reserve. Total block Frobenius uncertainty is then<.00224. The scalar ledger must certify this aggregate budget, not1e-4 per entry. A sufficient uniform per-entry radius is1e-4/7 for the scalar portion, with the actual outward matrix multiplication tracked.

## Fixed exclusion gate and truthful outcomes

Let Wc be a certified center of Z*Dbar(I-Vsel Vsel*)X, using the fixed Y=I. If its certified Frobenius lower bound is at least11/500=.022, then

 ||D(I-P)||HS >= ||Wc||F-.00224-.019 >.00076,
 tau >=(.00076)²/2 >1e-9.

A rational norm-square comparison avoids any floating threshold ambiguity. This is a deterministic allfive-span, seven-site49-entry test with a fixed gate; no sites or impurity are selected after seeing values. If it does not cross, report INDETERMINATE_COARSE_WITNESS. It does not imply tau small or justify a larger adaptive test inside this protocol.

The required visible block signal .022 is larger than the earlier optimistic5e-5 threshold because the actual omitted high tail and metric uncertainties are now charged. Whether it occurs is unknown. The route is mathematically complete as an exclusion certificate even if it is empirically inconclusive.

## Supplier and cost boundary

The geometry gain ledger86c4 is retained as a stricter conditional B-budget tool; it does not by itself implement this complete test. A successor may replace its three1e-8 allocations by a reviewed aggregate1e-4 Frobenius scalar budget and add the explicit local high term. ExistingB/c bounds and newB378 source must pass that actual weighted gate before contraction. No1e-39 metric or1e-37 kernel precision is required merely to attempt this coarse test.

Any newB378 contraction and49-entry evaluation need a separately frozen source/binding/root contract. The prospective300s cap must include input verification, all contractions, output schema and sampled whole-treeRSS384MiB, with fixed once/no retry. A cap bounds an attempt; it does not establish measured completion. No scientific work is authorized by this source document. Full high-accuracy Dhat and all earlier physical results remain immutable.
