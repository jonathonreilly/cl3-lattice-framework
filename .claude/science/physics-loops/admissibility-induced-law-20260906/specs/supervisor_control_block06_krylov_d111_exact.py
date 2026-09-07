"""Supervisor control: the degree-111 relative minimal polynomial of Q on 1 at W=5, (5,2,4), verified exactly on all 178 orbits."""
import sys; sys.argv=['x']
exec(open("supervisor_control_block06_krylov.py").read().split("\nfor W in (4,5):")[0])
import time
t0=time.time(); rows,idx,A,V,reps,orbit_of,Q=build((5,2,4),5); n=len(reps)
d,vecs=krylov(Q,[1]*n,n+1); print(f"W=5 (5,2,4): orbits {n}; Krylov dimension (modular, two Mersenne primes) = {d} [{time.time()-t0:.0f}s]", flush=True)
t0=time.time(); poly,ok=minpoly_rel(vecs,d)
print(f"   exact relative minimal polynomial of degree {d}: solved on {d} independent orbits and verified on all {n} orbits: {ok}; max coefficient digits {max(len(str(c)) for c in poly.all_coeffs())} [{time.time()-t0:.0f}s]", flush=True)
print("   factorization at this degree not attempted; the d real roots follow from S2 (self-adjointness).")
