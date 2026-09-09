# Source-only p=Kq DATA append

Use the preserved df39 proof, reviewed in native-second-action-data-cold-review. Its historical UNREVIEWED/source-only nu-unavailable statements are retained as source provenance, not present claims: nu now has accepted3ac execution and full saved-node POST. This implementation adds pA,pC,pD raw indices402,403,404, Gamma closure810. Original399raw trial (including actual24 selected seeds) remains unchanged. A future separately certified trial may admit q399..401, with p supplying its free action; no action on p is claimed.

At h=1, p=Kq; dimensional convention is p=(K/h)q, and multiply action by h. J=<a,Gamma b>, Gamma=i sign(iK); closed Gram is[[G,J],[-J,G]]. Reversed G is even/J odd. K commutes Gamma; actual DeltaK=8(x0qA^T-qAx0^T) does not. New source computes only raw p rows. A later reader applies the stated closure, never commuting the impurity through Gamma.

## Exact construction and scalar family

Core reads each original saved q-to-pole arithmetic pair once through a callback. It does NOT reevaluate q formulas or load an old native entry builder. The exact identities are G(p,z)=-sigma*s G(q,z)+sqrt(alpha)I/2 and J(p,z)=-sigma*s J(q,z)-sqrt(alpha)*mu*T/12. Pole s,alpha and mu are the exact OLD midpoints actually used by accepted3q. Tighter rho4 mu/cminus must not silently replace them. cminus does not occur in the new formulas; old rows keep their existing cminus dependence unchanged. New nu midpoint comes from accepted3ac/fullPOST only.

For Ward x_j, free Kx=(qD,qA,qC): G(p_u,x_j)=-I(u,f_j)/4,J=0. For q_v, G=0,J=-mu*N/4+nu*O/24; in particular J(pD,qD)=-nu/4. p self G=(6I-O)/4,J=0. No new oracle, torus moment evaluation or original cache/3q recomputation is involved. Existing saved arithmetic error is carried through multiplication; it is not dropped because new inputs are sharper.

## Physical versus arithmetic error

Saved q boxes must be the original ARITHMETIC boxes, not physical-inflated reader boxes. For their true-family physical radii use the reviewed3q bounds pg=2800*etaA,pj=176*etaB+eta_mu. Then new pole entry radii are |s|pg for G, and |s|pj+sqrt(alpha)|T|eta_mu/12 for J. Ward entries are exact. New p-to-q J radius is |N|eta_mu/4+|O|eta_nu/24. These are entrywise physical errors relative to the same midpoint-pole family, with no extra pole displacement or balance midpoint change. The binder must authenticate the original radii, use outward upper sqrt(alpha), and save these coefficients/radii separately; that adapter is NOT IMPLEMENTED/NOTREADY here. There is no claimed actual810 physical precision gate until it exists.

New arithmetic is outward192 with4096-bit stored endpoints,8192-bit products,512-bit rational inputs and bounded192-bit scale shifts. A completed row is synchronously persisted before its width gate. To assert combined arithmetic radius<=2^-60, use 4*810*max(old_actual_width,new_width)/2^192, checking authenticated old per-entry arithmetic maximum. Merely reusing an old804 operator bound is insufficient. If the stronger check fails, retain rows and report failure; never shrink widths. Prior strict trace<536 plus extra closed trace<=35 gives strict<571. This is trace of the exact Gram; physical entry inflation is not an added physical trace.

## Counts, runtime proposal and remaining binder

Five orbits:2025 rows,6060 new raw G/J pairs,5940 saved q-pole pair reads,30 p-self pairs,45 p-Ward and45 p-q pairs. No old entry is reevaluated. A bounded saved-row index needs only2010 old3q rows and32-row LRU, not full oldcache/Gram. Each pole pair needs <=12 rational/interval primitives, so <80000 simple interval primitives plus66 roots; local exact geometry per pair is a tiny7-coordinate sum. This is a source count, not timing. No full mock or actual entry was evaluated during source preparation.

Propose one root+one worker,30s/29.5s/29s,384MiB, once, no retry, only after source/binder/root review and preregistration. Reference accepted3q append external2.41s;10*2.41+5=29.1s is only an inferred allowance and may fail. The extra saved indexing/reuse path differs from the prior formula worker. A timeout preserves completed rows; no fit guarantee.

Runtime/binder remains disabled. Final binding must pin accepted3q ROOT/POST/result/stream and original scalar provenance, exact old mu midpoint and its radius, same poles/alpha, acceptednu ROOT/POST/result/worker/source, and actual old maximum arithmetic width/strict trace. It must avoid any four/24-history restoration or oldcache scan. Descriptor final verify and close are required even on setup, serialization, cap or width failure. Persist current row before the read and append row before any arithmetic-width comparison. No authorization file or native execution path is supplied.
