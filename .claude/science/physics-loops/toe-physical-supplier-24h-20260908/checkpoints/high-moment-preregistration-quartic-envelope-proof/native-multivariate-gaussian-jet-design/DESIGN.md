# Masked multivariate Gaussian jets, source-only core

This is an inert implementation proposal under the independently reviewed Gaussian determinant germ and native source-table identities pinned in SOURCE_PINS.json. It has no loader, accepted-input binding, runtime dispatcher, authorization, or execution proposal. It computes neither native moments nor a Ward sign. The copied arithmetic.py is byte-identical to the reviewed one-variable core; only its bounded complex interval primitives are used.

## Exact ordered interfaces

The pair mask is `(3,3,1)` in `(t,s,z)`, including its constant: 32 coefficients. It represents the branch-one square root of the determinant of `I+P(U-I)`, where

`U = exp((t+s)h) exp(-t(h+V_A)) exp(2z V_C) exp(-s(h+V_C))`.

Its vacuum series is `<Omega, exp(-t D_A) exp(2z B_C) exp(-s D_C) Omega>`. Multiply its coefficient `(i,j,k)` by `i!j!k!(-1)^(i+j)` to recover the requested ordered derivative with the marker already normalized as `2 B_C`. Source order is `(a,d_A,d_C)`; the two defects have entries `J_A[0,1]=2i`, `J_C[0,2]=2i`, and Hermitian conjugates. Reversing source order without the corresponding matrix change is invalid.

The reflected mask is `(3,3,2)`: 48 coefficients, for

`U = exp((t+s+z)h) exp(-t(h+V)) exp(-z(h+V')) exp(-s(h+V))`.

Its scalar series is `<Omega,exp(-tD)exp(-zD')exp(-sD)Omega>`, with exactly the same vacuum-energy subtraction in D and D'. In source order `(a,d,hd)`, `J_1[0,1]=2i`; the reflected coefficient matrix is

```
[ 0  -2i   0 ]
[ 2i   0  -1 ]
[ 0   -1   0 ]
```

The physical `J* D^k J` insertion has an additional factor 8, not incorporated in this normalized scalar jet. The squared inner-residual combinations are assembled separately from these coefficients. Full F-error propagation also remains separate.

## Cancellation before acquisition

Formal relative-product coefficients are exact rational dictionaries of words in `h,V_1,V_2`. Coefficients are collected before converting to intervals. Every nonconstant pure-h word must cancel exactly; otherwise the implementation refuses. A word with at least one defect factors as `h^p F J_1 (F*h^q F) J_2 ... F*h^r` with no inverse Gram matrix.

For any coefficient of total degree at least two, the trace of its complete one-defect sector is analytically zero because `[P,h]=0`. The code retains these one-defect matrices for products with other relative coefficients, but never passes their linear trace to the projected table. Only the nonlinear sector is passed to the first log term. This is not cancellation of uncertain high-power interval data.

For m>=2, the degree-alpha coefficient C(alpha,m) of the mth relative power is formed by masked convolution of A(beta) and C(alpha-beta,m-1), joining them through the projected Gram. The log coefficient is the nonlinear first trace divided by 2, plus `(-1)^(m+1) Tr C(alpha,m)/(2m)`. Euler's formal-series identity gives

`|alpha| Z_alpha = sum_(0<beta<=alpha) |beta| ell_beta Z_(alpha-beta)`.

All mask operations discard only coefficients that cannot influence the requested rectangular mask. The endpoint support invariant is p+r<=|alpha|-m for an m-defect/log-product term. Thus every projected or ordinary contraction has intervening degree at most N-2: 5 in the pair case, 6 in the reflected case. The code checks supports and these query bounds.

## Native table interface; no supplied scalar values

The inert tables.py expresses signed radial entries from a callback R(j). For pairs A,C the neighbor block is

`T_AC(j) = shared * R(j) + opposite_cross * (R(j+2)/6 - R(j))`.

The opposite contribution has the signed-source minus R(j). Ordinary odd center-to-edge entry is `-i R(j+1)/3`; negative-band projected even center-to-edge entry is `+i R(j+1)/6`. The adapter forms `(ordinary - signed-absolute block)/2` with the parity appropriate to each order. A physical caller must authenticate the pair labels and these integer overlap counts; no binder is provided here.

For reflected sources, `shifted_table` maps `(a,d,hd)` to fundamental `(a,d)` with endpoint shifts `(0,0,1)` on both sides. The maximum fundamental power is therefore 8. Pair radial data require odd moments through omega7 and even R6; reflected data require odd moments through omega9 and exact even R10. The maximum underlying radial degree 10 is not a demand for an omega11 oracle. These are source formulas, not numerical inputs or verified supplier widths.

The determinant bridge, source signs, one-variable degree cancellation, and reflected identity are imported only from the pinned reviewed proofs. A finite synthetic determinant/Fock match does not by itself prove the infinite-lattice bridge.

## Finite work and bit limits

After exact collection there are 566 pair words and 2,219 reflected words including the constant, with maximum lengths 7 and 8. These are source-only combinatorial counts. The implementation's formal dictionary cap is 200,000 entries. Each formal rational is capped at 2,048 bits in each numerator/denominator; multiplying and adding two such coefficients before checking requires less than 16,384 transient bits. All generated factorial/binomial constants in these fixed masks are substantially smaller.

A sparse endpoint matrix with endpoint degree at most d has at most `E(d)=9(d+1)(d+2)/2` complex entries. Summing E(|alpha|-1) over the masks bounds one full family of coefficient matrices by 2,664 pair entries and 5,004 reflected entries. Keeping A, previous and current log powers plus a temporary matrix is bounded by three such families plus 648 entries: at most 15,660 complex boxes in the reflected case. The exact formal dictionary is released before log powers are built. A complex box has four integer endpoints, each capped at 4,096 bits; packed endpoint payload is under 33 MB, but Python objects, retained callbacks, and formal dictionaries require additional memory. This is not a measured process-RSS bound or a promise to fit an existing runtime contract.

A conservative summand count from mask convolution is 1,175,310 pair or 4,037,040 reflected complex multiplications in log products. Bounding each formal factor chain by 162(N-1)+9 products per word, adding all trace terms (5,940/12,060), and at most three products per ordered scalar convolution pair gives fewer than 1.75 million pair or 6.60 million reflected complex products per jet. The global product counter refuses above 100 million; no performance claim relies on reaching that cap. Each copied complex multiplication performs 16 real endpoint multiplications. Stored integer cap is 4,096 bits; endpoint multiplication requires at most 8,192 bits and outward-ceiling increments at most 8,193 bits. Input/table boxes are checked and memoized, with at most 2*(N-1)*9 distinct queries.

There is no denominator growth in interval contraction: all intervals use the same 2^-256 grid. Exact formal word coefficients are converted outward once. Numerical width success is not guaranteed, and no target or conditioning gate is installed. A future runtime must persist intermediate data, bound process resources, and authenticate the exact original source family before any native use.

## Synthetic scope and retained failures

check.py uses four explicit Majorana matrices over exact rational complex numbers, two distinct free block energies, a finite vacuum, two distinct neighbor sources, and the exact reflected Fock Hamiltonian. Direct products of 4x4 Fock powers are independent of the core's logarithm/determinant recurrence. All 32 pair and 48 reflected scalar coefficients are checked for containment, including mixed insertion coefficients. Additional controls check endpoint shifts, degree refusal, pure-word census, and malformed/oversized interval rejection. No native scalar, covariance, saved trial, or accepted output is read.

The first fixture had a syntax error, preserved verbatim. The next fixture was deliberately interrupted because it rebuilt exact toy Gram powers on every query; its uncached source is preserved. Caching fabricated table entries changes neither the proposed mathematics nor the tested inputs. Final source guards and support checks justified the final complete synthetic comparison.

## Separate possible degree2/degree1 option

The suggested `(p degree2,q degree1)` route is not implemented here. A reflected inner mask `(2,2,4)` again has total degree 8 and the same +2 endpoint shift, suggesting the same omega9 ceiling. A nominal center-conjugated defect on `(a,d_A,d_C,ha)` needs a separate signed scalar/defect proof and a four-source implementation. No sufficiency, cost, or error improvement is claimed by this note; the current masks are unchanged.
