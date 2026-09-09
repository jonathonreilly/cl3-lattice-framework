# L1: fixed Wilson words and their conditional boundary

**Date:** 2026-06-04; source correction 2026-09-09
**Type:** bounded_theorem
**Scope:** supplied finite mathematics; no physical selection or audit verdict.
**Primary runner:** [diagonal_l1_wilson_line_composite_demonstration.py](../scripts/diagonal_l1_wilson_line_composite_demonstration.py)
**Cached output:** [diagonal_l1_wilson_line_composite_demonstration.txt](../logs/runner-cache/diagonal_l1_wilson_line_composite_demonstration.txt)
**Original history:** [exact original and correction record](../.claude/science/physics-loops/diagonal-adjacency-7870-correction-20260909/CORRECTION_HISTORY.md).

Supply invertible NN link matrices and a specified path. Define its diagonal
transporter to be the ordered product along that path, with the first step
on the right. It is then fully determined by the NN connection variables and
the path. The fixed Wilson word adds no independent connection variable.
This is a statement about a definition, not an exclusion of new dynamics.
Before any gauge quotient, four independent SU(2) matrices on the edges of
a face have 12 real parameters. Appending a fixed word gives the graph of a
function of those variables, with no extra free coordinate. This dimension
count is distinct from the uniform example's shared link matrices.

## Uniform SU(2) example

In the runner's uniform background, `U_x`, `U_y`, `U_z` are 2×2 SU(2)
matrices. For a face displacement, set

```
W_A = U_y U_x,    W_B = U_x U_y,
P_xy = U_x U_y U_x^{-1} U_y^{-1}.
```

Associativity gives `W_B W_A^{-1}=P_xy`. Products and inverses remain in
SU(2). Noncommuting sample links yield unequal path products; commuting
links give the same products and identity plaquettes. The sample angles
are unchanged: `(0.7,1.1,0.9)` about the x,y,z axes, and
`(0.5,1.3,0.2)` about a common z axis for the commuting comparison.

For bounded fixed Hermitian `A_x,A_y` and small real `a`, expansion of the
four exponentials gives
`P_xy=I-a^2[A_x,A_y]+O(a^3)`. The logarithm near identity has the same
leading term. The runner checks one numerical representative at `a=10^-3`,
with residual below `50 a^3`; that single sample is a diagnostic, while the
local expansion supplies the asymptotic statement. “Curvature” here labels
the chosen discrete plaquette, not spacetime or a field equation.

There are `3!=6` shortest positive-axis paths to a body-diagonal endpoint.
For `W_xy=U_z U_y U_x` and `W_yx=U_z U_x U_y`,

```
W_xy W_yx^{-1} = U_z P_yx U_z^{-1}.
```

Adjacent swaps generate all permutations, so every ratio can be expressed
using conjugated plaquettes. The runner checks this displayed swap and all
six path products: the chosen noncommuting sample has six distinct products,
and the commuting sample has one. The six-distinct observation is not a
statement about every noncommuting background.

## Scope of the negative statement

For a nonuniform connection, link matrices must be evaluated at the actual
vertices and oriented fibers along each path. The uniform formulas above do
not suppress those endpoint arguments in a general model. A unitary map
between fibers is also different from a simultaneous tensor action on two
site factors; the L2 note chooses its own matrices explicitly.

A fixed word introduces no freely variable transporter beyond its inputs.
It can nevertheless appear in an additional term `kappa Re Tr(W)` with a
new supplied coupling `kappa`, changing an action while leaving the word
fixed. The old phrase “zero new content” is therefore withdrawn. The result
does not exclude independently chosen diagonal variables, weights, longer
paths, carriers or dynamical laws. It does not change axioms and supplies
no physical gauge group, clock, carrier or Record formation law.
The [current four-axiom memo](MINIMAL_AXIOMS_2026-06-29.md) is a scope boundary only.
