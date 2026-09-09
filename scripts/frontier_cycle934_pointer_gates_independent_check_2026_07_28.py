#!/usr/bin/env python3
"""Literal-bit, partial-trace and actual interval-counter controls.
Shares supplied definitions and NumPy/SciPy libraries, not Dicke coefficients.
"""
import json
import math
from hashlib import sha256
from pathlib import Path
import numpy as np
import pointer_6005_model as model
AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS = ('docs/POINTER_SYMMETRY_AND_SAMPLED_STAR_PROTOCOL_CYCLE934_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/pointer_6005_model.py')
INPUT_SHA256 = {'docs/POINTER_SYMMETRY_AND_SAMPLED_STAR_PROTOCOL_CYCLE934_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'e2fbb30f4ca053f4c1364d65ad9b3337a8e4f7bead00ebd051bc78ac9ba9cbba', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/pointer_6005_model.py': '5416b71a71bdb03843f752b03b696f07fe3158e0a3dc8a3eb0782f201102cd46'}


def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,want in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=want:raise RuntimeError('missing or changed input: '+path)


def full_stats(d,lp,la,t):
    if not 1<=d<=6:raise ValueError('full-bit control cap is seven spins')
    N=2**(d+1);H=np.zeros((N,N))
    for a in range(N):
        H[a,a]=-sum((1-2*(a&1))*(1-2*((a>>j)&1)) for j in range(1,d+1))
        for j in range(d+1):H[a,a^(1<<j)]-=lp if j==0 else la
    w,V=np.linalg.eigh(H);psi=V@(np.exp(-1j*w*t)*(V.T@np.full(N,1/math.sqrt(N))))
    def entropy(rho):
        return float(-sum(x*math.log2(x) for x in np.linalg.eigvalsh(rho) if x>1e-15))
    branches=[]
    for z in [0,1]:
        v=psi[z::2];p=float(np.vdot(v,v).real);v=v/math.sqrt(p);density={}
        for k in range(1,min(2,d)+1):
            D=2**k;R=np.zeros((D,D),complex)
            for a in range(D):
                for b in range(D):R[a,b]=sum(v[(rest<<k)|a]*v[(rest<<k)|b].conjugate() for rest in range(2**(d-k)))
            density[k]=R
        branches.append((p,density))
    s={k:sum(p*entropy(r[k]) for p,r in branches) for k in range(1,min(d,2)+1)}
    mix=sum(p*r[1] for p,r in branches)
    return {'chi1':entropy(mix)-s[1],'H_Z':-sum(p*math.log2(p) for p,r in branches),
            'C_ab':2*s[1]-s[2] if d>=2 else None,'s1':s[1],
            'global_flip_commutator_max':float(np.max(abs(H-H[::-1,::-1])))}


def controls():
    input_guard();rows=[]
    for d,l,t in [(2,.1,.7),(3,.1,.7),(3,0.,.7),(2,2.,.7)]:
        full=full_stats(d,l,l,t);s=model.StarCollective(d,l).stats(t)
        rows.append({'d':d,'field':l,'t':t,'full':full,'max_difference':max(abs(full[k]-s[k]) for k in ['chi1','H_Z','C_ab','s1'])})
    periods=[]
    for field in [0.,.1]:
        cell=model.StarCollective(3,field);a=cell.stats(.7)['chi1'];b=cell.stats(.7+math.pi/2)['chi1']
        periods.append({'field':field,'chi_t':a,'chi_t_plus_pi_over_2':b,'difference':abs(a-b)})
    good,blocks=model.revival_control(model.edges_by_brentq)
    bad,_=model.revival_control(lambda *args,**kwargs:[])
    windows=[{'lo':.2,'hi':.31},{'lo':.39,'hi':.51}];times=[round(.1*i,10) for i in range(13)]
    flags=model.sampled_union(windows,times)
    kwargs={'x_control_ok':True,'commutator_ordering_ok':True,'drift_ok':True}
    run=model.sampled_verdict(flags,times,**kwargs)
    removed={key:model.sampled_verdict(flags,times,**(kwargs|{key:False})) for key in kwargs}
    checks={'actual_full_bit_partial_trace_agreement':all(r['max_difference']<1e-11 and r['full']['global_flip_commutator_max']==0 for r in rows),
            'period_exact_only_zero_field_in_control':periods[0]['difference']<1e-11 and periods[1]['difference']>1e-3,
            'actual_C5_two_blocks_detected_and_counter_fault_rejected':good and not bad,
            'union_grid_counter_keeps_four_consecutive_samples':run['run']==4 and run['verdict']=='YES',
            'full_protocol_control_clauses_are_required':all(r['verdict']=='NO' for r in removed.values())}
    path=next(iter(INPUT_SHA256));prior=INPUT_SHA256[path];INPUT_SHA256[path]='0'*64
    try:input_guard();caught=False
    except RuntimeError:caught=True
    finally:INPUT_SHA256[path]=prior
    checks['actual_wrong_input_rejected']=caught
    return checks,{'full_bit_rows':rows,'periods':periods,'C5_actual_blocks':blocks,'counter_fault_was_rejected':not bad,'abstract_two_interval_run':run,'missing_control_results':removed}


def main():
    checks,result=controls();print(json.dumps(result,sort_keys=True))
    for name,ok in checks.items():print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"TOTAL: PASS={sum(checks.values())} FAIL={len(checks)-sum(checks.values())}")
    return int(not model.accepted(checks,[]))

if __name__=='__main__':raise SystemExit(main())
