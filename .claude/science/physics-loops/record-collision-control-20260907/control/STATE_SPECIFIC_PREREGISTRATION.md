# Preregistered state-specific two-site escape, before matrix execution

Same nine-site order r,hv,hw,x,f,b0,b1,l0,l1 and K=q(1+Yx)+1/2+nb0+2nb1. Source r0,head10,Yx+,f1,b1b0=00,label00; target r0,head01,Zx+,f0,b1b0=10,label01. Complete interaction graph; no assertion of nearest-neighbor path placement. At most two-site Hermitian sums, supplied coherent typing and pulse clock, fixed pure input only.

Let Lx=|Y-><Y+|=(Zx-iXx)/2 and Rb=|1><0|b1=(Xb1-iYb1)/2. Pulse1 H1=Lx Rb+Lx† Rb†=(Zx Xb1-Xx Yb1)/2, duration pi/2. It maps bright/b0 to -i dark/b1, with q fixed1: K is exactly5/2 across the whole occupied pulse orbit. H1 does NOT commute with K globally on q0.

Pulse2 H2=Xf(1-Yx)/2, duration pi/2. It flips fuel in the dark sector with -i phase and commutes K globally. Pulse3 H3=(1-q)Xx, signed duration -pi/4, maps Y- to Z+ with no added scalar phase, at q0. Pulse4 H4=(Xhv Xhw+Yhv Yhw)/2, duration pi/2, swaps head10 to01 with -i. Pulse5 H5=Xl1, duration pi/2, writes workspace label01 with -i. Predicted final phase (-i)^4=+1 times target.

Check every Hamiltonian is at most two-site; full [H1,K] nonzero but [H1,K]psi along pulse1 zero; all later full commutators zero. Verify exact projector invariance of the occupied pulse subspace, and sampled fractions0,1/8,...,1 in each pulse for norm, full energy distribution, mean5/2, variance0, old Record and one-head conservation. Use sparse512 matrices and analytic H^3=H exponentials (rotation has projector square), no parameter fitting. This is fixed-input state-transfer, not a full instrument or arbitrary-input energy-preserving control family. It does not contradict the globally commuting two-site obstruction. Source/target workspace is not new permanent Record formation. Preserve phase prediction failure if any.
