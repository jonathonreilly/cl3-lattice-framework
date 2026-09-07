#!/usr/bin/env python3
"""Independent physical Pauli witness for a supplied irreversible jump law.

Four edge qubits, four live fuel bits (gap one), four degenerate head positions,
legal Record/code sectors, and a retained integer battery 0..33. Sector labels
are an orthogonal direct sum, never a tensor allocation of illegal states.
This commensurate finite example is not the continuous cube proof, a local
physical implementation, or a closed unitary realization.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import itertools
import resource
import signal
import sys
import time
import numpy as np
from scipy.linalg import eigh

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('180 second limit')))
signal.alarm(180)
EDGES = ((0,1),(1,2),(2,3),(0,3))
I = np.eye(16, dtype=complex)
x = np.array([[0,1],[1,0]], complex)
z = np.diag([1.,-1.])
CAP = 34
TOL = 2e-9
MUTATION = ''
checks = 0
worst = 0.

def check(a, b, label):
    global checks, worst
    err = float(np.max(np.abs(np.asarray(a)-np.asarray(b)), initial=0))
    if err > TOL:
        raise AssertionError(f'{label}: residual={err:.9g}')
    checks += 1
    worst = max(worst, err)

def word(ops):
    out = np.ones((1,1), complex)
    for e in range(4):
        out = np.kron(out, ops.get(e,np.eye(2)))
    return out

Z = [word({e:z}) for e in range(4)]
B = [word({e:z for e,pair in enumerate(EDGES) if v in pair}) for v in range(4)]

def A(i,j):
    e = EDGES.index(tuple(sorted((i,j))))
    ops = {e:x}
    for k,pair in enumerate(EDGES):
        if k != e and ((i in pair and next(v for v in pair if v != i)<j) or
                       (j in pair and next(v for v in pair if v != j)<i)):
            ops[k]=z
    return (1 if i<j else -1)*word(ops)

HOPS = [0.5j*A(i,j)@(B[i]-B[j]) for i,j in EDGES]
N = sum((I-b)/2 for b in B)
S = A(0,1)@A(1,2)@A(2,3)@A(3,0)

def sector(records):
    p = (I+S)/2 if not records else I.copy()
    for e,sign in records.items():
        p = p@((I+sign*Z[e])/2)
    vals,vec = eigh(p)
    q = vec[:,vals>0.5]
    live = [e for e in range(4) if e not in records]
    # Actual fuel Hamiltonian is the sum of four latch occupations.
    fuel = sum(int(e in live) for e in range(4))
    h = q.conj().T@(sum((HOPS[e] for e in live if e in (0,2)), np.zeros((16,16),complex)))@q + fuel*np.eye(q.shape[1])
    return q,h,live

def component(live, removed):
    reached = {EDGES[removed][0]}
    while True:
        new = reached | {v for e in live if e!=removed for v in EDGES[e] if any(w in reached for w in EDGES[e])}
        if new==reached: return reached
        reached=new

def branches(records,e):
    q,h,live = sector(records)
    comp = component(live,e)
    bridge = EDGES[e][1] not in comp
    result=[]
    for sign in (1,-1):
        out=dict(records); out[e]=sign
        r,g,_=sector(out)
        k=r.conj().T@((I+sign*Z[e])/2)@q
        if MUTATION=='fair_bridge' and bridge: k=k/np.sqrt(2)
        physical=r@k
        if MUTATION=='old_record' and records:
            physical=word({next(iter(records)):x})@physical
        for old,value in records.items():
            check(Z[old]@physical,value*physical,'physical old Record preservation')
        nout=r.conj().T@N@r
        if MUTATION=='number': nout=nout+np.eye(len(nout))
        check(nout@k,k@(q.conj().T@N@q),'native N intertwining')
        for old,value in records.items():
            check(r.conj().T@Z[old]@r@k,value*k,'old Record preservation')
        if bridge:
            parity=I.copy(); oldsign=1
            for v in comp: parity=parity@B[v]
            for old,value in records.items():
                if sum(v in comp for v in EDGES[old])==1: oldsign*=value
            check(k.conj().T@k,q.conj().T@(I+sign*oldsign*parity)@q/2,'signed component parity projector')
        else: check(k.conj().T@k,np.eye(len(h))/2,'nonbridge fair isometry')
        result.append((r,g,k))
    check(sum(k.conj().T@k for _,_,k in result),np.eye(len(h)),'native sign completeness')
    return q,h,live,result

def translation(shift):
    out=np.zeros((CAP,CAP))
    for n in range(CAP):
        dest=n+shift
        if 0<=dest<CAP: out[dest,n]=1
    return out

def total(h):
    # Construct independently in code coordinates, not from lift eigenvalues.
    return np.kron(h,np.eye(CAP))+np.kron(np.eye(len(h)),np.diag(np.arange(CAP)))

def lift(h,g,k):
    a,u=eigh(h); b,v=eigh(g)
    check(a,np.rint(a),'input integer spectrum'); check(b,np.rint(b),'output integer spectrum')
    out=np.zeros((len(g)*CAP,len(h)*CAP),complex)
    for ia,ea in enumerate(a):
        for ib,eb in enumerate(b):
            amp=v[:,ib].conj()@k@u[:,ia]
            if abs(amp)<1e-12: continue
            shift=int(round(ea-eb))
            if MUTATION=='omit_fuel': shift-=1
            if MUTATION=='double_fuel': shift+=1
            if MUTATION=='reverse_shift': shift=-shift
            out += np.kron(amp*np.outer(v[:,ib],u[:,ia].conj()),translation(shift))
    check(total(g)@out,out@total(h),'actual matrix energy intertwining')
    return out

def completed(records,e):
    q,h,live,bs=branches(records,e)
    lifts=[lift(h,g,k) for _,g,k in bs]
    effect=sum(l.conj().T@l for l in lifts)
    defect=np.eye(len(effect))-effect
    vals,u=eigh((defect+defect.conj().T)/2)
    if vals.min() < -TOL: raise AssertionError('joint cap is not a contraction')
    f=(u*np.sqrt(np.where(vals>TOL,vals,0)))@u.conj().T
    if MUTATION=='separate_refusal':
        # Two individual complements add 2I-effect instead of I-effect.
        refusal_effect=2*np.eye(len(effect))-effect
    else: refusal_effect=f.conj().T@f
    check(effect+refusal_effect,np.eye(len(effect)),'ONE joint refusal completeness')
    ht=total(h)
    check(ht@f,f@ht,'same-H absorbing refusal commutation')
    ev,w=eigh(ht)
    safe=w[:,abs(ev-20)<TOL]
    check(f@safe,0,'safe total-energy-20 refusal')
    check(safe.conj().T@effect@safe,np.eye(safe.shape[1]),'safe rate one per incident edge')
    # Distribution conservation tests every spectral indicator, not just mean.
    for energy in np.unique(np.rint(ev)):
        pin=w[:,abs(ev-energy)<TOL]; pin=pin@pin.conj().T
        pull=f.conj().T@pin@f
        for l,(_,g,_) in zip(lifts,bs):
            eo,wo=eigh(total(g)); po=wo[:,abs(eo-energy)<TOL]; po=po@po.conj().T
            pull+=l.conj().T@po@l
        check(pull,pin,'full total-energy distribution invariance')
    refusal_max=float(vals.max())
    if refusal_max<0.1: raise AssertionError('unsafe boundary refusal witness absent')
    idx=int(np.argmax(vals)); unsafe=u[:,idx]
    check(unsafe.conj()@defect@unsafe,refusal_max,'actual unsafe input refusal probability')
    return safe,effect,f,refusal_max

def main():
    global MUTATION
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutation',default='',choices=['','omit_fuel','double_fuel','reverse_shift','fair_bridge','separate_refusal','old_record','number','wrong_head_degree'])
    MUTATION=parser.parse_args().mutation
    start=time.monotonic()
    check(S,S.conj().T,'native cycle Hermiticity'); check(S@S,I,'native cycle square')
    for e,(i,j) in enumerate(EDGES):
        check(A(i,j)@A(i,j),I,'native edge involution')
        check(HOPS[e]@N,N@HOPS[e],'native hopping N')
        check(HOPS[e]@HOPS[e],(I-B[i]@B[j])/2,'native hopping normalization')
    count=0
    for values in itertools.product((0,1,-1),repeat=4):
        records={e:s for e,s in enumerate(values) if s}
        for e in range(4):
            if e not in records: branches(records,e); count+=1
    print(f'PASS native Pauli/code instrument: {count} legal mask/sign/edge cases, full even-N dictionary')
    # Head 0 starts on the square; edge 01 moves it to head 1. Edge 12 is
    # then a reachable bridge. Both first signs and all live head incidences
    # are covered by the algebraic census above; actual lifts below.
    maxima=[]
    for records,head in (({},0),({0:1},1),({0:-1},1)):
        _,h,live=sector(records)
        incident=[e for e in live if head in EDGES[e]]
        accumulated=None
        for e in incident:
            safe,effect,f,m=completed(records,e); maxima.append(m)
            value=safe.conj().T@effect@safe
            accumulated=value if accumulated is None else accumulated+value
        claimed_degree=len(incident)+(1 if MUTATION=='wrong_head_degree' else 0)
        check(accumulated,claimed_degree*np.eye(len(accumulated)),'head live-degree generator rate')
    # Deterministic bridge parity input, reachable after nonbridge 01=+.
    q,h,live,bs=branches({0:1},1)
    effect=bs[0][2].conj().T@bs[0][2]
    vals,u=eigh(effect); psi=u[:,np.argmax(vals)]
    check(np.linalg.norm(bs[0][2]@psi)**2,1,'deterministic bridge positive outcome')
    check(np.linalg.norm(bs[1][2]@psi)**2,0,'deterministic bridge negative outcome')
    # Nonbridge onto isometry supplies an explicit antecedent in initial code.
    _,_,_,first=branches({},0)
    antecedent=2*first[0][2].conj().T@psi
    check(first[0][2]@antecedent,psi,'bridge input reachable from nonbridge')
    # Use the same finite ladder through both actual events at total energy 20.
    q0,h0,_=sector({})
    r1,h1,k1=first[0]
    a0=lift(h0,h1,k1)
    energies,vec=eigh(h1)
    target=np.zeros(len(h1)*CAP,complex)
    for j,energy in enumerate(energies):
        battery=int(round(20-energy))
        target += np.kron(vec[:,j]*(vec[:,j].conj()@psi),np.eye(CAP)[:,battery])
    initial=2*a0.conj().T@target
    check(a0@initial,target,'actual safe ladder nonbridge reachability')
    check(total(h0)@initial,20*initial,'actual antecedent total-energy fiber')
    for sign,(_,g,k) in zip((1,-1),bs):
        outcome=lift(h1,g,k)@target
        check(np.linalg.norm(outcome)**2,1 if sign==1 else 0,'actual lifted deterministic bridge')
    # Head has four positions, with incidence enforced at every legal mask.
    for values in itertools.product((0,1,-1),repeat=4):
        records={e:s for e,s in enumerate(values) if s}
        _,h,live=sector(records)
        for head in range(4):
            effect=np.zeros_like(h)
            for e in live:
                if head in EDGES[e]:
                    _,_,_,out=branches(records,e)
                    effect+=sum(k.conj().T@k for _,_,k in out)
            check(effect,sum(head in EDGES[e] for e in live)*np.eye(len(h)),'all four head positions legal incidence')
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
    if rss>=180: raise AssertionError(f'RSS envelope exceeded: {rss:.1f} MiB')
    print(f'PASS retained 0..33 ladder: safe Etotal=20, boundary refusal max={max(maxima):.6f}; matrix commutation, joint completion, every energy indicator, head rates')
    print('PASS nonbridge then reachable deterministic bridge; refusal sectors absorbing with unchanged H')
    print(f'PASS checks={checks} worst={worst:.3e} elapsed={time.monotonic()-start:.3f}s RSS={rss:.1f}MiB')
    print('SCOPE supplied irreversible generator; no local physical or closed-unitary implementation claim')
    print('SOURCE_SHA256',hashlib.sha256(open(__file__,'rb').read()).hexdigest())

if __name__=='__main__':
    main()
