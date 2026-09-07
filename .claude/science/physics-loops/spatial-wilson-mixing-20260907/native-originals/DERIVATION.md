# Actual cube-slab stripped source mixing

This develops the frozen model c55d2234, not a supplied diagonal packet. Spatial Wilson action and anisotropy are explicit inputs. No beta6, isotropic, thermodynamic or continuum identification follows.

## Actual operator and source map

Let E be the twelve edges of one cube and H=L²(SU(3)^E,dU). Let W0 be its bottom loop. I:L²central(SU3)→H sends f to f(W0). Product Haar makes I isometric. This image is gauge invariant; all Wilson factors and temporal convolution commute with local gauge transformations, so restricting to the gauge-invariant Hilbert space makes no change to the matrix elements below.

Write J(G)=(χ3+χbar3)/6=ReTr(G)/3, w_b=e^(bJ). Let C_t have kernel ∏_(e∈E) w_t(V_e U_e^-1). Let M0 be multiplication by w_(s/2)(W0), and Menv by the product of the other five face halfweights. The true two-slice transfer is M0 Menv C_t Menv M0. Since M0 I=I m0, its source compression is m0 D_(s,t) m0, where

D_(s,t)=I* Menv C_t Menv I.

Thus multiplication by m0^-1 strips the marked faces EXACTLY on the full source class space. No finite-section exponential or prescribed D enters. C_t is positive semidefinite by the nonnegative Wilson character expansion, and D is positive self-adjoint. Positivity does not imply character diagonality.

## Five-face disk Haar integration

Fix the bottom boundary holonomy W. Conditional integration over the other eight links gives g_s(W)=I* Menv 1. The five environment faces form a disk with boundary the marked loop. Gauge-fix a tree consisting of three bottom edges and four vertical edges. Seven normalized Haar gauge integrations give one; the remaining four top edges are independent Haar variables, while the fourth bottom edge is W (or its inverse). The five face words now form the usual disk gluing integral.

The exact elementary identity, from matrix-index Schur orthogonality, is

∫ χλ(A X) χμ(X^-1 B) dX = δλμ χλ(AB)/dλ.

Successive gluing of five disk faces gives four factors1/dλ. Equivalently, after the above tree gauge, integrate the four free top links successively. Orientation reversals are harmless since w_b(G^-1)=w_b(G). If w_(s/2)=Σλ cλ(s/2)χλ, then

g_s(W)=Σλ cλ(s/2)^5/dλ^4 χλ(W).

All steps can first be made for finite character polynomials and then passed to the Wilson exponential: its representation-ring expansion has nonnegative coefficients and Σλ dλ cλ=e^(s/2), ensuring absolute uniform convergence and permitting the Haar integrations. This is actual disk integration, not a definition of a coefficient vector.

The cube geometry itself is old: docs/GAUGE_VACUUM_PLAQUETTE_DISTINCT_SHELL_EXACT_CORE_NARROW_THEOREM_NOTE_2026-05-29.md proves the distinct five-face cap. It does not prove this two-slice off-diagonal. The old tensor-transfer Perron source lines12–13,73–74,450–451 explicitly leave static-to-two-slice operator identification open. Here the static marginal is used only through the exactly rank-one temporal kernel at t=0.

## Exact off-diagonal at zero temporal coupling

C_0=|1><1| on the full link space. Consequently D_(s,0)=|g_s><g_s|, and conjugation symmetry gives

<χ0,D_(s,0)χ3>=c0(s/2)^5 c3(s/2)^5/81.

For s>0 this is strictly positive. More explicitly, positivity of representation-ring coefficients in exp[(s/12)(χ3+χbar3)] gives c0≥1 and c3≥s/12, so

<χ0,D_(s,0)χ3>≥s^5/(12^5·81).

This is not a claim about an inverse local convolution at t=0, where nontrivial local eigenvalues vanish.

## Explicit strictly positive temporal coupling

Because |J|≤1, the product temporal kernel satisfies pointwise

|∏_(12edges)w_t(V_eU_e^-1)−1|≤e^(12t)−1.

The ten environment halfweights in the two-slice integrand have product at most e^(5s); |χ3|≤3. Product Haar has mass1. Therefore

|<χ0,[D_(s,t)−D_(s,0)]χ3>|≤3e^(5s)(e^(12t)−1).

This is a direct integral estimate, not a numerical continuity inference. As a derived explicit member of the preregistered positive-t interval, choose s=1 and t=10^-12. Since e5<149 and e^x−1≤2x for0≤x≤1/2,

|difference|<10728/10^12 < 1/(12^5·81)=1/20155392.

Thus this actual finite Wilson slab has a strictly nonzero character off-diagonal at strictly positive spatial AND temporal couplings. The extreme anisotropy is disclosed; it proves existence and does not approximate a physical beta6 or isotropic slab. The rational choice is made after deriving the analytic bound, not presented as the original preregistered numeric fixture.

For t>0 the normalized one-link convolution eigenvalues aλ(t)=cλ(t)/(dλ c0(t)) are strictly positive. If one further defines the historical algebraic residual R=(Dloc)^-1D with Dloc=diag(aλ^4), its 0,3 entry remains nonzero (a0=1). Multiplying by any positive normalization scalar likewise cannot restore diagonality. This is a statement on finite character matrix elements; no bounded all-weight inverse is asserted.

## Controls and boundaries

With Menv=I, direct linkwise Schur integration gives diagonal compression c0(t)^8 [cλ(t)/dλ]^4, or aλ(t)^4 after dividing by c0(t)^12. This derives the four-link packet for the explicitly constant spectator embedding in the no-spatial-environment model. It does not derive the same form after five spatial faces are inserted.

If a source edge is absent from every remaining spatial factor at both slices, its Peter–Weyl isotypic projectors commute with Menv and C_t. Iχλ belongs to the λ (or dual, depending orientation) sector on that edge. Orthogonality then forces off-diagonal source entries to vanish for different labels. This explains why a two-plaquette toy is an inadequate falsifier. The five-face cap avoids that condition on every source edge.

The new result rejects universal diagonality for this explicit actual Wilson/Haar source compression. It does not claim that every physically chosen environment embedding, boundary state, geometry or parameter is non-diagonal. In particular an environment-dressed embedding is a different map and would need its own definition and proof.
