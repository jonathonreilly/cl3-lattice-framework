# Supplied circulant weights: coefficient powers and signed ratios

**Date:** 2026-06-04; source correction 2026-09-09
**Type:** bounded_theorem
**Scope:** supplied finite mathematics; no physical selection or audit verdict.
**Primary runner:** [diagonal_gate_r_half_weighted_path_test.py](../scripts/diagonal_gate_r_half_weighted_path_test.py)
**Cached output:** [diagonal_gate_r_half_weighted_path_test.txt](../logs/runner-cache/diagonal_gate_r_half_weighted_path_test.txt)
**Original history:** [exact original and correction record](../.claude/science/physics-loops/diagonal-adjacency-7870-correction-20260909/CORRECTION_HISTORY.md).

Supply `H=aI+bC+conj(b)C^2`, with real `a`, complex `b` and a cyclic 3×3
shift C. H is Hermitian. The labels “stay” and “shift” describe its coefficient
basis, without identifying spatial links, BZ corners or physical particles.
For `a!=0`, define `r=|b|^2/a^2`.

## Coefficient-space identity

The three powers `I,C,C^2` are Hilbert–Schmidt orthogonal and each has
squared norm 3. Thus

```
||aI||_HS^2 = 3a^2,     ||bC+conj(b)C^2||_HS^2 = 6|b|^2.
```

Choosing equality of these two coefficient powers is equivalent to `r=1/2`.
It is a supplied balance rule, not forced by the triangle's one stay and two
neighbors. In particular, this is not equal power in the minimal central
blocks of the real cyclic group algebra.

The latter projectors are `P_s=J/3` and `P_d=I-P_s`. At `a=1,b=1/sqrt(2)`
real, coefficient powers are `3,3`, whereas

```
||P_s H||_HS^2 = (1+sqrt(2))^2,
||P_d H||_HS^2 = 2(1-1/sqrt(2))^2.
```

These are approximately `5.828427` and `0.171573`. The coefficient summands
are linear coordinate spaces, not the two central ideals. The former K0,
central-block and determinant-measure identification is withdrawn. No
current measure is derived from this example.

## Signed ratio and positive square-root convention

Since `Tr H=3a` and `Tr H^2=3a^2+6|b|^2`,

```
Q_H = Tr(H^2)/(Tr H)^2 = 1/3+(2/3)r,       a != 0.
```

If one separately defines nonnegative numbers `m_j=lambda_j^2` from the
eigenvalues, their positive-square-root ratio is
`Q_+=sum lambda_j^2/(sum |lambda_j|)^2`. It agrees with Q_H when the nonzero
eigenvalues have a common sign. For a nonzero spectrum with mixed signs,
`|sum lambda_j| < sum |lambda_j|`, so the ratios differ when Q_H is defined.
Neither formula assigns physical masses.

The historical positive examples at `a=1`, real nonnegative b and
`r=0,1/2,1` give Q_H=`1/3,2/3,1`; the latter has eigenvalues `3,0,0`.
At `a=1,b=2`, the valid mixed-sign spectrum is `5,-1,-1` and Q_H=3,
but Q_+=27/49. Calling this matrix or abstract squared spectrum “unphysical”
was unjustified. At `a=0`, r and Q_H are undefined; Q_+ can still be defined
if H is nonzero. The zero spectrum has no normalized ratio.

## Eight supplied arithmetic conventions

All rows retain the original numerical ratios with `a=1`. The table is not
an exhaustive search or a list of framework-selected laws.

| supplied rule | abs(b)/a | r | Q_H |
|---|---:|---:|---:|
| inverse face-diagonal length, with stay normalized to 1 | 1/sqrt(2) | 1/2 | 2/3 |
| inverse squared face-diagonal length | 1/2 | 1/4 | 1/2 |
| number of shortest NN paths | 2 | 4 | 3 |
| inverse path count | 1/2 | 1/4 | 1/2 |
| displacement orbit-size ratio 12/6 | 2 | 4 | 3 |
| displacement stabilizer ratio 4/8 | 1/2 | 1/4 | 1/2 |
| coefficient HS balance | 1/sqrt(2) | 1/2 | 2/3 |
| equal amplitudes a=abs(b) | 1 | 1 | 1 |

The inverse-length and coefficient-balance rows are precisely the two r=1/2
rows in this finite list. They do not derive a normalization of “stay.”
Equal amplitudes are a chosen rule, not a deduction of Born probabilities.

## Current premise boundary

The [current custody note](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
leaves the physical r selector open; the former AC_phi_lambda admission has
zero premise weight. We consume that open-boundary statement only, not its
whole ancestry or any historical selector rhetoric. The present independent
coefficient/projector calculation controls the distinction made above.
The [current four-axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies no value of r, mass assignment,
clock, dynamics or permanent Record formation in this calculation. This note
does not change axioms and does not close the physical selector.
