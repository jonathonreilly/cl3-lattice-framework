# Finite autonomous native clock: proof and parameter certificate

The preregistered static Hamiltonian realizes the full ready-input native isometry exactly at time1, with original free evolution retained, and within trace-norm error1/20 throughout[0.99,1.01] when the clock is retained with an appropriate universal completed-clock target. It is an autonomous finite-window implementation under supplied static multi-site couplings and pure clock preparation, not permanent Record formation.

## Gauge and exact solution

Let U1,...,U9 be the actual native all-input pulse unitaries, U10,...,U17=I, and Wj=Uj...U1. Define D=sum_j |j><j| tensor Wj. D is unitary and gauges the clock hopping:

    Hc = D(Hpath tensor I)D†,
    Hpath_(j+1,j) = g sqrt((j+1)(17-j)).

All native Uj commute with K as full operators, so [D,K]=[Hc,K]=0. Therefore evolution under K+Hc from clock0 is

    sum_j a_j(t)|j> tensor exp(-itK)Wj psi.

This identity holds for every input, including reference entanglement, not only a selected native state.

For an elementary derivation of a_j, take17 virtual spins with Hamiltonian g sum X. In the normalized permutation-symmetric state with j ones, its matrix element to j+1 is g sqrt((j+1)(17-j)). The product rotation of all-zero spins gives

    a_j(t)=sqrt(binomial(17,j))cos(gt)^(17-j)(-i sin(gt))^j.

The virtual spins are a derivation of the18-dimensional clock matrix, not additional physical resources. At g=pi/2,t=1 only j=17 remains, with phase(-i)^17. Since W17=W9 and W9 restricted to ready inputs is V, the output is exactly |17> tensor exp(-iK)V psi up to global phase. The free evolution is not compensated or silently removed.

## Full-input retained and discarded clock bounds

Let eta(t)=sum_(j<9)|a_j|² and p=1-eta. For p>0 define the normalized completed-clock vector chi_t=p^(-1/2)sum_(j>=9)a_j|j>. It depends on time and the clock couplings, not on the input. The actual pure output has overlap sqrt(p) with chi_t tensor exp(-itK)V psi for every normalized ready-input psi and arbitrary reference. Orthogonality of clock positions proves this without a bound on individual native prefixes. Thus the joint trace-norm distance is exactly2sqrt(eta) for every pure input; purification/contractivity gives the same upper bound on the ready-input channel diamond norm. This is not an unrestricted initial-clock diamond norm.

After tracing the clock, the channel is a mixture of prefix channels. The completed terms sum to p times the target; remaining terms have total weight eta. Hence the system-only diamond error is at most2eta. No postselection or normalization of a native outcome is used. The normalized chi_t is only the comparison state's clock factor; the actual clock is retained unmeasured.

Missing steps17-j have binomial mean17cos²(gt). Unfinished j<9 implies17-j>=9, so

    eta <= (17/9)cos²(gt)
        = (17/9)sin²(g(t-1))
        <= 17pi²/360000 < 1/2000

for |t-1|<=1/100. With pi<22/7, the displayed upper bound is exact rational arithmetic. Consequently2sqrt(eta)<1/20 and2eta<1/1000. These are conservative sufficient bounds, not optimized clock length or window.

## Resources, energy and locality

There are18 one-hot clock registers plus the9 reduced native registers, total27 qubits, initially with one clock excitation at0. The natural static Hamiltonian is a sum of clock-exchange terms tensor the specific native Uj and their adjoints. Each Uj has support on at most3 native sites, so each Hermitian term has support at most5 sites including two clock sites. This is a supplied multi-site complete-connectivity interaction, not a nearest-neighbor primitive or a compiled two-site realization.

On the invariant one-hot clock sector, ||Hc||=17pi/2<27, maximum coupling=9pi/2<15, and ||K+Hc||<=17pi/2+11/2<33. These are legal-sector bounds. On the full27-qubit register space the natural sum of clock exchanges remains a well-defined local-support Hermitian extension, conserves clock excitation and K, and has the coarse bound ||Hc||<=sum g_j<255, hence ||K+Hc||<261. It does not require a global one-hot projector or an inert extension to exist. Its behavior on unused clock sectors is not the claimed computation.

Both K and total energy K+Hc are conserved. The interaction Hamiltonian is part of the actual autonomous model; no energy-cost or formation derivation follows from giving its norm. Static engineered position-dependent couplings, the exact Uj coefficients, supplied roles, pure ready clock and native preparation remain physical inputs. Observation within the stated window is still a supplied timing condition, though no external sequence of nine switching pulses occurs.

## Recurrence and numerical scope

At t=2 the clock returns0 with phase(-1)^17 and W0=I; the circuit has coherently undone its completed native operation up to free evolution. Thus the completed label is not permanently locked in this closed model. Padding supplies a finite retention window, not irreversibility or renewal.

The runner revalidates the actual native163 exact assertions, then independently exponentiates the18x18 path and compares amplitudes/spectrum to the analytic construction, including both window endpoints and recurrence. It checks the exact rational inequalities and resource bounds. It does not allocate or simulate the full2^27 apparatus. Native all-input equality plus the gauge proof supplies the arbitrary-input/reference statement; small-matrix agreement alone is not a numerical diamond-norm certificate.
