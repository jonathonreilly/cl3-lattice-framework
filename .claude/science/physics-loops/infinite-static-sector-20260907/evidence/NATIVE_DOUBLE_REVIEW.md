# Independent cold review: selected infinite charged GNS sector

Verdict: PASS for both frozen proofs in their explicit fixed-interaction, selected full-local-algebra GNS scope. No repository edits and no finite check was rerun. This review relies on the already independently checked block38 bound and directly inspected Yarotsky0411042 Theorems2–3/equation6; it is not an independent reproof of the general neutral thermodynamic-limit theorem.

Bound targets:

- Root ROOT_DERIVATION.md SHA868eed1df8dbee74957f5ad0a5afc880de921847400cfc6ca61ad4c7255dcac3.
- Primary DERIVATION.md SHAd82ddb5165688622c3d6e7a110274f61b0fa3db4a9b1a386bbb8ba07c187b98b.

Both were frozen before this review. The source is https://arxiv.org/pdf/math-ph/0411042 . Its equation6 is a local-vector weak-resolvent statement, not convergence of finite charged minima; the proofs use exactly the former.

## Local normality and implementation

In scaled units, removing one cell h_z and at most four grouped terms of norm delta gives the two variational inequalities E<=E_rest+4delta and E>=E_rest+<h_z>−4delta. Thus <h_z><=8delta. The remaining operator acts on the other cells and has a bottom, so the product-vacuum trial is legitimate. This uses the fixed whole-range finite restriction; no volume-dependent interaction is substituted.

On each fixed finite union S of cells, sum_S h_z has compact resolvent. The uniform energy estimate bounds the mass above cutoff R by8delta|S|/R. To make the compactness step explicit, for its finite-rank spectral projector P, positivity and the gentle-projection estimate give ||rho−P rho P||_1<=2sqrt(Tr((I−P)rho)). The finite-dimensional compressions form a compact bounded set. This proves trace-norm precompactness, and the prescribed local weak-star state identifies all subsequential limits. Hence the limiting state is locally normal.

Normality of the local GNS representation, rather than just its vacuum functional, follows by testing matrix elements between pi(A)Omega and pi(B)Omega on a larger finite normal algebra and then taking density limits. Primary states this explicitly; it supplies the detail behind root's statement that operator integrals agree in GNS by local normality. Strong-star continuity of finite-link gauge conjugations and local normality imply norm continuity of their action on each local GNS vector. Density gives strong continuity on the full representation. No norm continuity of gauge conjugation on all bounded operators is required.

The finite gauge commutation identity passes through equation6 on the dense local-vector domain. Boundedness of nonreal resolvents then gives commutation everywhere. Therefore the common fixed space of the combined gauge/source representation is closed and reducing, so its Hamiltonian restriction is genuinely selfadjoint, not merely a formal compression.

## Local charged density

For a local operator tuple only the finite set of incident gauge vertices and the two source vertices acts nontrivially. Its finite Haar average remains a bounded local tuple: the finite-dimensional source matrix mixing and ultraweak bounded-operator integral are well defined, and normality identifies this with the vector integral. All other vertex factors commute with the averaged ones and already fix the tuple applied to the invariant vacuum. Thus the average is invariant under the full finite-support gauge group.

For a fixed charged vector xi, approximate by a local tuple zeta and average over zeta's finite support group. This average fixes xi and is contractive, so the approximation error cannot increase. Equivalently it agrees with the full fixed-space orthogonal projection on zeta. Hence exactly covariant local tuples are dense in the charged space. Their defining operator identities hold also in sufficiently large finite volumes, where the vacuum is invariant; there is no merely asymptotic Gauss constraint or false assertion that arbitrary reduced states are boundary singlets.

## Spectral support and upper form bound

Each finite charged tuple has positive spectral measure supported above b=(4/a)(1−kappa)d by block38. The actual finite graph distance eventually equals the fixed Manhattan distance, since a fixed shortest path is included and no subgraph path is shorter. Equation6 and convergence of local tuple norms imply convergence against C_0 spectral functions. One may justify the resolvent-algebra step using the resolvent identity and difference quotients for repeated poles, with the uniform total-mass bound. Every nonnegative compact test function below b has zero limiting integral. The limiting spectral projection below b therefore annihilates a dense set of charged vectors and hence the entire charged space. This step does not require any uniform condition number for the finite dressed similarity.

The local path tuple is normalized exactly by sum_ab A_ab* A_ab=I. It is nonzero and charged by its endpoint covariance. Its finite spectral measures all have mass one and first moment4d/a. The limiting GNS spectral measure also has mass one, independently of energy convergence. Vague convergence of these probabilities to a probability measure is weak convergence; alternatively the uniform first moment supplies tightness. Applying weak convergence to bounded continuous truncations of the nonnegative energy and monotone convergence gives the limiting first moment at most4d/a. Thus the vector lies in the quadratic-form domain and yields the upper variational bound. Equality of first moments, an operator-domain claim, or convergence of minimizing vectors is neither needed nor asserted.

## Scope clarification worth retaining canonically

The GNS representation is that of the FULL local bounded-operator (field/link) algebra with the neutral invariant state. It is not merely the GNS representation of the gauge-invariant observable subalgebra; the latter does not automatically contain the covariant path matrix coefficients used here. Primary explicitly names the full algebra, and root's use of the full Theorem2–3 local-vector domain has the same meaning. State that convention explicitly in the canonical lead to avoid a physical-identification ambiguity. This is a scope clarification, not a defect in either proof.

The result is a selected charged sector and its spectral bottom with linear bounds. It does not establish convergence of finite charged lowest energies, a charged bottom eigenvector, boundary-independent charged representations, a temporal Wilson-loop potential, a large-distance string-tension limit, a continuum theorem or axiom selection. Those exclusions are mathematically substantive and correctly preserved. No blocking correction found.
