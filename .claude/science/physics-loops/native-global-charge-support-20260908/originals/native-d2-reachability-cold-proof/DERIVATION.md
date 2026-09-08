# Independent D2 position reachability

Fixed domain: Cartesian product C_L1 square C_L2 square C_L3, each Li even and >=4, simple physical edges; arbitrary full low-charge configuration with precisely Qx=+1,Qy=-1. Fixed cycle constraints are relaxed. Claim: the positive charge can be carried by a finite sequence of nonzero legal native hops to every vertex other than y, leaving the negative charge at y. The reversed-orientation argument gives the analogous negative-charge statement. This is existential position reachability, not full configuration connectivity, an implemented control schedule or quantum transport.

Orient each electric edge i->j when epsilon_i(2n_e-1)=+1. Then outdegree=3+Q, indegree=3-Q. Thus x has outdegree4, y has outdegree2, and neutral vertices have3. Positive charge moves along the initial arrows; negative charge moves against them. Along a simple directed path, previously flipped edges never include the next edge, so every next prescribed arrow is still eligible. A path avoiding y preserves its charge, has only the two endpoint defects after each prefix, and its native amplitudes are nonzero with modulus one. Phases need not be positive and are not discarded.

## Small edge-cut lemma

For the stated three-dimensional torus, every nonempty proper vertex set has at least six boundary edges; a cut of size six isolates a single vertex on one side.

Here is an elementary proof also covering extent-four wraparound. For each coordinate, every nonconstant cyclic line contributes at least two cut edges. If a direction has no cut edges, the set is constant along every line in that direction. Any cut in another direction is then replicated Li>=4 times, yielding at least eight cut edges. Therefore a cut of size at most six in a nontrivial set must have exactly two edges in each direction, on exactly one nonconstant line per direction.

Slice perpendicular to coordinate1. Within each slice the coordinate2/3 torus has any nontrivial cut of size at least four: if both directions have cuts, each contributes two; if one has none, the other repeats at least four times. Since the total cut in directions2/3 is four, at most one slice can be nonconstant. There must be such a slice: otherwise all slices are constant and a transition between full and empty slices contributes L2*L3>=16 coordinate1 edges. All remaining slices are constant. Their constants must agree, because the cycle of slices with the exceptional slice removed is connected, and a full/empty adjacent pair would again cost at least16 edges. The exceptional slice therefore differs from the common constant on exactly one site: each differing site contributes two coordinate1 cut edges, and only two are available. The entire set or its complement is consequently a singleton. This proves both the lower bound and equality classification without an imported connectivity theorem.

## Reachability cut

Delete y and let R be the vertices reachable from x in the resulting directed graph. Suppose some other vertex is outside R. No directed edge exits R except possibly an edge into y. Write a for outgoing cut edges and b for incoming cut edges. Summing outdegree-minus-indegree over R gives a-b=2, because R contains x but not y. The vertex y has indegree4, hence a<=4, and |boundary R|=a+b=2a-2<=6.

The cut lemma forces size six and either R or its complement to be a singleton. If the complement is a singleton, it must be y, contrary to the assumed other unreachable vertex. If R is a singleton, it is x; but the simple graph permits at most one outgoing edge from x into y, contrary to a=4. Thus R contains every vertex except y.

A directed shortest path from x to any requested vertex in R is simple. Its successive native hops give the required legal sequence. For moving the negative charge instead, reverse all arrows: it becomes the outdegree4 source and the fixed positive charge the indegree4 excluded sink; the same argument applies.

The proof fails without the graph hypotheses used in the cut lemma and simple-edge bound. It does not assert a universal statement on other bipartite graphs. It makes no claim that the two prescribed positions can be reached with an unchanged electric configuration, winding data, native phases or spectator path history. Intermediate and final electric bits generally differ. A nonzero product of directed hopping matrix elements is a support witness, not evidence that the fixed Hamiltonian alone performs that controlled path with probability one.
