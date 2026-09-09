#!/usr/bin/env python3
"""Independent full-spin/orbit checks of the bounded Cycle937 construction.
Shared model definitions and NumPy eigensolver are disclosed; full matrix,
preparation, orbit projection and branch reshaping are separately constructed.
"""
import itertools
import json
import math
from hashlib import sha256
from pathlib import Path
import numpy as np
import spider_6008_model as model
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/SPIDER_SYMMETRY_REDUCTION_AND_FINITE_COMPARISONS_CYCLE937_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/spider_6008_model.py')
INPUT_SHA256 = {'docs/SPIDER_SYMMETRY_REDUCTION_AND_FINITE_COMPARISONS_CYCLE937_BOUNDED_THEOREM_NOTE_2026-07-28.md': '761cab9b3d1bb2d85d949fb0a7c42d839daa38913c85c61679e9684feb3d6195', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/spider_6008_model.py': '898c8acd3f07c07b33b5a06726884bf2e923502e857caa47307747745903b95e'}


def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,expected in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=expected:
            raise RuntimeError('missing or changed input: '+path)


def full_system(arms, arm_field, pointer_field, broken=0.0):
    """Little-endian sites: pointer0, then each root and its deeper sites."""
    sizes=[L for L,edges in arms];n=1+sum(sizes)
    if n>9:
        raise ValueError('bounded full-space fixture exceeds nine spins')
    bonds=[];roots=[];start=1
    for L,edges in arms:
        roots.append(start);bonds.append((0,start));bonds += [(start+u,start+v) for u,v in edges];start+=L
    N=2**n;H=np.zeros((N,N));initial=np.zeros(N)
    active=[0,*roots]
    for a in range(N):
        z=[1-2*((a>>i)&1) for i in range(n)]
        H[a,a]=-sum(z[u]*z[v] for u,v in bonds)
        for i in range(n):H[a,a^(1<<i)]-=pointer_field if i==0 else arm_field+(broken if i==roots[0] else 0)
        if all(not ((a>>i)&1) for i in range(n) if i not in active):initial[a]=2**(-len(active)/2)
    return H,initial


def orbit_projection(d,L,basis):
    D=2**L;N=len(basis);pos={n:i for i,n in enumerate(basis)}
    groups={}
    for a in range(2**(1+d*L)):
        arms=[(a>>(1+j*L))&(D-1) for j in range(d)]
        occ=tuple(arms.count(b) for b in range(D));key=(a&1,occ)
        groups.setdefault(key,[]).append(a)
    P=np.zeros((2**(1+d*L),2*N))
    for (z,occ),rows in groups.items():P[rows,z*N+pos[occ]]=1/math.sqrt(len(rows))
    return P


def full_profile(psi, sizes):
    """Direct tensor Schmidt matrices, no occupation/Hankel coefficients."""
    # pointer is low bit; C reshape puts it last, hence branch psi[z::2].
    out=[];d=len(sizes)
    for k in range(d+1):
        dim=2**sum(sizes[:k]);value=0.0
        for z in [0,1]:
            branch=psi[z::2];p=float(np.vdot(branch,branch).real)
            if p:
                sv=np.linalg.svd(branch.reshape(-1,dim),compute_uv=False)**2/p
                value+=p*float(-sum(x*math.log2(x) for x in sv if x>0))
        out.append(value/float(np.vdot(psi,psi).real))
    return out


def compare(d,L,edges,field,t,pointer=None):
    pointer=field if pointer is None else pointer
    H,c0,basis=model.reduced(d,L,edges,field,pointer)
    F,f0=full_system([(L,edges)]*d,field,pointer);P=orbit_projection(d,L,basis)
    c=model.evolve(H,c0,t);f=model.evolve(F,f0,t)
    sk=model.profile(c,basis,d,L);sf=full_profile(f,[L]*d)
    return {'d':d,'L':L,'edges':edges,'field':field,'pointer_field':pointer,'t':t,
            'full_dim':len(F),'reduced_dim':len(H),'isometry_residual':float(np.max(abs(P.T@P-np.eye(len(H))))),
            'projection_residual':float(np.max(abs(P.T@F@P-H))),
            'intertwining_residual':float(np.max(abs(F@P-P@H))),
            'initial_residual':float(np.max(abs(P@c0-f0))),
            'state_residual':float(np.max(abs(P@c-f))),
            'entropy_residual':float(np.max(abs(np.array(sk)-sf))),
            's_reduced':sk,'s_full':sf,'C_pair':2*sk[1]-sk[2],
            'complement_residual':max(abs(sk[k]-sk[d-k]) for k in range(d+1))}


def controls():
    input_guard()
    H,c0,basis=model.reduced(2,2,[(0,1)],.13,.13)
    F,f0=full_system([(2,[(0,1)])]*2,.13,.13,broken=.2);P=orbit_projection(2,2,basis)
    projected=P.T@F@P;lift=P@model.evolve(projected,c0,.7);actual=model.evolve(F,f0,.7)
    leakage=float(np.max(abs(F@P-P@projected)));difference=float(np.linalg.norm(actual-lift));norm=float(np.linalg.norm(lift))
    # Actual source perturbation has leakage and wrong evolution yet stays normalized.
    broken_ok=leakage>1e-3 and difference>1e-3 and abs(norm-1)<1e-12
    good=compare(2,2,[(0,1)],.13,.7)
    checks={'symmetric_matrix_and_evolution':all(good[k]<1e-11 for k in ['isometry_residual','projection_residual','intertwining_residual','initial_residual','state_residual','entropy_residual']),
            'broken_arm_leakage_and_state_difference':broken_ok}
    # Exercise the real terminal rule with refutation and required-result failures.
    checks['terminal_rejects_refutation']=not model.accepted({'clean':True},['actual planted disagreement'])
    checks['terminal_rejects_missing_or_failed_science']=not model.accepted({},[]) and not model.accepted({'Q1':True,'Q2':False},[]) and model.accepted({'Q1':True,'Q2':True},[])
    path=next(iter(INPUT_SHA256));prior=INPUT_SHA256[path];INPUT_SHA256[path]='0'*64
    try:
        input_guard();caught=False
    except RuntimeError:caught=True
    finally:INPUT_SHA256[path]=prior
    checks['actual_input_guard_rejects_wrong_expected_hash']=caught
    return checks,{'clean_baseline':good,'broken_arm':{'leakage':leakage,'full_evolution_difference':difference,'projected_lift_norm':norm}}


def main():
    checks,result=controls();print(json.dumps(result,sort_keys=True))
    for name,ok in checks.items():print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"TOTAL: PASS={sum(checks.values())} FAIL={len(checks)-sum(checks.values())}")
    return int(not model.accepted(checks,[]))

if __name__=='__main__':raise SystemExit(main())
