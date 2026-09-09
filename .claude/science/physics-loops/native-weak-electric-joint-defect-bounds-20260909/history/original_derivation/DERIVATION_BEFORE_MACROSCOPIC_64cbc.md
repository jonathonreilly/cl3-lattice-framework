# From mean density to a conditional local-defect theorem

Scope: a new bounded analytic design on the supplied full native carrier, not a proof of nonzero-U stability. No numerical physical action, sampling, or new model is used. The actual 8056 and 8057 sources supply zero-penalty flux stiffness and weak-electric mean-density bounds. The missing premise below is explicitly stronger than either result.

## Inputs and the precise obstruction

Write H_U=H_0+UD, D=3N/2+V, V=(1/2) sum_j W_j. Each W_j=Z_e Z_f is a Hermitian unitary on two distinct incident edges. Let P_f=(1-S_f)/2 count a defective elementary face, with the canonical magnetic sign convention absorbed, and K=sum_f P_f. The P_f commute mutually and with H_0, but generally not with H_U. Prior results give H_0>=E_0+κK and, for every H_U ground-state density operator,

    <K>/N <= min(3,3U/(2κ),75(U/κ)^2).

A small mean, even uniform small one-face marginals, cannot by itself imply a joint-event or contour estimate. Here is an exact counterexample on this same full carrier. On an even cubic torus both the canonical all-π elementary-flux orbit and the all-zero elementary-flux orbit exist: canonical staggered signs and uniform link signs are explicit representatives. In the relative-defect convention the latter has every one of the 3N faces bad. Choose normalized physical states ρ_good,ρ_bad supported respectively in these two nonempty flux subspaces, and set

    ρ_p=(1-p)ρ_good+pρ_bad.

Then <P_f>=p for every f, <K>/N=3p, and for every nonempty prescribed face set C,

    Tr ρ_p product_(f in C) P_f=p.

No bound exp(-c|C|), with c>0 uniform in volume and fixed p>0, follows. Averaging each state under translations makes the state translation invariant without changing these identities. A pure coherent superposition of one vector from each flux subspace gives the same flux probabilities. Taking p=min(1,25(U/κ)^2) can satisfy the quadratic mean bound while preserving the obstruction. These states are NOT claimed to be H_U ground or Gibbs states. They refute the inference from the stated mean-density conclusion alone, not stability of the actual Hamiltonian. The ground-state equation contains extra information, used next.

## A concrete missing premise

For a finite nonempty set C of elementary faces define Q_C=product_(f in C)P_f and R_C=I-Q_C. Let E_U be the actual finite-volume ground energy. Suppose one can prove, uniformly in volume and in all nonempty C under consideration,

    Q_C(H_U-E_U)Q_C >= κ_* |C| Q_C,                 (LC)

with κ_*>0 independent of C and volume. Empty Q_C causes no problem. This is a lower bound on the compression with all prescribed defects enforced. It is not a claim that Q_C commutes with H_U, nor a global spectral gap, active-particle gap, or winding gap. It permits arbitrarily low excitations in the complementary block. The reference energy is E_U, not E_0+3UN/2.

LC is the specific unproved local coercivity obligation. The known U=0 operator bound alone yields only Q_C(H_U-E_U)Q_C >= (κ|C|-3UN/2)Q_C using D>=0 and the trial energy. That becomes useless at fixed |C| as N grows. Replacing E_U by E_0, dropping the extensive shift, or applying a defect-sector resolvent estimate to the full noncommuting H_U would be invalid. A proof of LC needs cancellation of the exterior ground-energy response or another truly local comparison. No such cancellation is assumed proved here.

## Exact projected ground-state recursion

Let ψ be any normalized H_U ground vector and p(C)=||Q_Cψ||². Project its eigen-equation:

    Q_C(H_U-E_U)Q_C Q_Cψ = -U Q_C V R_Cψ.

Under LC the inverse on ran Q_C has norm at most1/(κ_*|C|). Only electric terms whose flipped-face set F_j intersects C can contribute: H_0 and all other W_j commute with Q_C, hence their off-block terms vanish. Each |F_j| is6 for a perpendicular pair or8 for an opposite pair. A fixed face is flipped by24 perpendicular and8 opposite pairs, including periodic L=4 seams. Therefore the number n_C of contributing terms is at most32|C|.

For each contributing j, conjugation by W_j reverses P_f precisely for f in F_j. Since untouched faces of C remain required bad,

    ||Q_C W_j R_C ψ|| <= ||Q_(C\F_j) ψ||.

For clarity, Q_C W_j=W_j Q'_C where Q'_C has good projectors on C∩F_j and bad projectors on C\F_j. Q'_C and R_C commute and Q'_C R_C<=Q_(C\F_j). This proves the norm estimate without assuming ψ flux diagonal or discarding interference. Thus

    sqrt(p(C)) <= U/(2κ_*|C|)
                   sum_(j:F_j∩C nonempty) sqrt(p(C\F_j))
                <= 16U/κ_* max_j sqrt(p(C\F_j)).

Every removal deletes between1 and8 faces. With r=(16U/κ_*)²<1, induction on |C|, starting at p(empty)=1, gives

    p(C) <= r^ceil(|C|/8).

The argument applies to every ground vector and hence every ground-state mixture by linearity of event probabilities. Degeneracy and coherent flux mixing are allowed. It is a ground-state result conditional on LC, not a finite-temperature theorem.

## Conditional contour consequence

Identify defective plaquettes with dual edges. A connected dual-edge set of m edges containing a specified dual vertex can be doubled edge by edge to form a connected Eulerian multigraph. A deterministic Euler tour from the specified vertex has length exactly2m and recovers every original edge, including edges closing cycles. Its degree-six direction word gives an injective encoding after a fixed deterministic choice of tour, hence the safe count6^(2m)=36^m. Doubling only a spanning tree would omit cyclic edges and would not justify this bound. Union bounding the joint estimate gives, with

    a=36*(16U/κ_*)^(1/4)<1,

probability of a connected defective set through that vertex with at least ℓ edges at most a^ℓ/(1-a). This sufficient small-coupling condition is deliberately conservative: U/κ_*<1/(16*36^4). The stronger joint-event bound remains useful before using this crude entropy factor. Pure winding changes have no bad faces and are outside this conclusion.

## What to work on next

The high-value target is LC or a weaker recursion-compatible local compression estimate for prescribed connected sets. It should compare the constrained and unconstrained interacting ground energies while controlling exterior response, not appeal to a uniform free-Majorana gap. A connected-set-only estimate would require checking that the recursive C\F_j sets remain in its domain; they can disconnect, so silently restricting LC to connected sets does not license the recursion above. A repaired domain could include all finite unions generated by these removals.

This identifies both an exact limitation of8057's mean-density statement and an explicit sufficient premise converting the actual noncommuting ground-state equation into local joint-defect control. No assertion is made that LC holds uniformly in volume at any fixed nonzero U. The finite-volume corollary below proves a shrinking-window version.


## An actual finite-volume corollary from the existing theorems

A restricted but nonempty supplied-model regime does satisfy LC without any new premise. Retain the exact positivity D>=0 and the actual variational energy bound E_U<=E_0+(3/2)UN. For m=|C|>=1, the previously proved H_0>=E_0+κK and Q_C K Q_C>=m Q_C yield

    Q_C(H_U-E_U)Q_C >= [κm-(3/2)UN]Q_C.

No commuting assumption on H_U and Q_C is used: compression preserves an operator inequality. If

    0<=U<=κ/(3N),

then (3/2)UN<=κ/2<=κm/2, and LC holds for every nonempty C with κ_*=κ/2. Consequently every actual ground-state density operator of the supplied full H_U satisfies

    Prob(all faces in C bad) <= (32U/κ)^(2 ceil(m/8))

whenever32U/κ<1. At U=0 the right side is zero for nonempty C, directly from the stiffness inequality; division-based steps need not be used at that endpoint. The corresponding connected-defect tail through a specified dual vertex is

    Prob(a connected defective set with >=ell edges) <= min(1,a^ell/(1-a)),
    a=36*(32U/κ)^(1/4)<1.

Thus a sufficient nonempty strict interval is U<min(κ/(3N),κ/(32*36^4)); the first inequality may be taken non-strict if the second remains strict. With the explicit8057 constant κ=1161h/204800, this is fully numerical for cubic L=4M, M>=32. It also applies wherever a positive certified κ is available. It assumes no unique ground state, no active gap and no winding gap. The bound is valid for arbitrary prescribed C, including disconnected sets, so the recursion's domain is closed under every removal.

This is a nontrivial finite-volume joint-event and contour consequence of8056/57 plus the exact ground-state equation. It is stronger in event scope than a first-moment estimate. However its sufficient coupling window shrinks as1/N; it establishes neither fixed-nonzero-U thermodynamic contour stability nor a volume-uniform excitation gap. It does not resolve the missing uniform LC premise. The crude positive-D estimate spends the entire extensive electric energy allowance on the prescribed set. Removing that loss remains the meaningful local problem.
