# Quadratic weak-electric ground-state defect-density bound

Status: new exact support derivation, conditional on supplied native model and accepted U0 uniform stiffness. Independent review pending. This strengthens the previously derived linear mean-density estimate; it does not give a nonzero-U phase or contour bound.

Let K=sum_f P_f count bad elementary plaquettes and H0>=E0+κK on the full physical carrier. Let HU=H0+UD, U>=0, D=3N/2+V, V=(1/2)sum_j W_j. There are15N incident-edge pairs j, with W_j Hermitian unitary and with each term flipping its affected plaquette signs. The canonical-flux trial state has <V>=0, so EU<=E0+3UN/2.

For any state ρ, including a mixed ground state, and any face f flipped by j, W_j anticommutes with S_f=I−2P_f. Hence P_f W_j P_f=Q_f W_j Q_f=0, Q_f=I−P_f. Hilbert–Schmidt Cauchy–Schwarz gives |TrρW_j|<=2sqrt(p_f(1−p_f))<=2sqrt(p_f), p_f=TrρP_f. Explicitly the cross term Tr(sqrtρ P_f W_j Q_f sqrtρ) has the two squared norms TrρP_f and TrρQ_f. This does not assume a product state, flux diagonality, or a spectral gap.

Each vertex has12 perpendicular incident pairs and3 opposite pairs. A perpendicular pair flips6 faces, because each edge belongs to4 faces and the two edges share exactly1; an opposite pair flips8. These statements include the L=4 periodic seams: opposite lattice neighbors remain distinct, two adjacent collinear edges share no elementary face, and perpendicular incident edges share exactly one face for every L>=4.

A fixed elementary face has4 edges and4 corner vertices. Counting incident pairs containing exactly one of its edges gives24 perpendicular pairs and8 opposite pairs: at each corner each of the two face edges pairs with three nonparallel edges other than its partner in that face, giving6 perpendicular pairs per corner; it pairs with its single opposite edge, giving2 opposite pairs per corner. Such a pair has a unique common endpoint, so no further multiplicity occurs.

Average the bound for W_j over its m_j affected faces before summing:

 |<V>| <= sum_j (1/m_j) sum_(f flipped by j) sqrt(p_f)
       = (24/6+8/8) sum_f sqrt(p_f)
       = 5 sum_f sqrt(p_f)
       <= sqrt(75 N <K>).

The lattice has3N elementary faces. This is a state-independent expectation estimate, not an operator inequality with a nonlinear function of K.

For any HU ground-state density operator, the trial bound and H0 stiffness yield

 κ<K> + U<V> <= 0,
 κ<K> <= U sqrt(75N<K>).

If <K>=0 there is nothing to divide; otherwise division and squaring give

 <K>/N <= 75 (U/κ)^2.

Combine with the independent positivity-based linear bound and the exact maximum K<=3N:

 <K>/N <= min(3, 3U/(2κ), 75(U/κ)^2).

For cubic L=4M, M>=32, the accepted density certificate and π²<10 give κ=1161h/204800, hence the explicit quadratic coefficient is75(204800/1161)^2 multiplying(U/h)^2; the linear coefficient is102400/387. For all cubic sizes a positive existential κ exists by the earlier small-size argument. Neither a unique ground state nor a uniform active/winding gap is required.

The same nonlinear estimate controls <V> in thermal states, but this note does not claim that the ground-state variational cancellation transfers without an entropy remainder. The already established finite-temperature relative-entropy linear bound remains separate. A local contour or phase theorem is not inferred from small mean density.
