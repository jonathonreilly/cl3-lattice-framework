#!/usr/bin/env python3
"""Portable frozen A/B/C/D diagnosis; no width/rate/pulse sweeps.
A finite packet + waits; B finite packet + zero waits; C ideal + waits;
D ideal + zero waits. Ideal means overlap kernel one, not a normalized
finite-energy battery. Thresholds concern currents of averaged states.
This orbital route was independently implemented and frozen by the orbital
checker before reading primary results. A separate primary agent reproduced
all360 rows before this portable packaging; no primary functions are imported.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import sys,json,hashlib,time,resource,signal,math,copy,subprocess
from pathlib import Path
from fractions import Fraction
AUDIT_TIMEOUT_SEC=180
RSS_LIMIT_MIB=180
SCHEMA='autonomous-head-four-ablation-v1'
ROOT=Path(__file__).resolve().parents[1]
SCOPE='C/D formal ideal coherent-reference limit; no finite-energy claim. B/D zero-wait endpoint comparisons; not a new autonomous realization. Mean-current thresholds, no fitted parameters.'
def finite(x):
    if isinstance(x,float): return math.isfinite(x)
    if isinstance(x,dict): return all(finite(v) for v in x.values())
    if isinstance(x,list): return all(finite(v) for v in x)
    return True
def finish(output,started):
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
    elapsed=time.monotonic()-started
    assert elapsed<AUDIT_TIMEOUT_SEC and rss<RSS_LIMIT_MIB
    output.update(schema=SCHEMA,validation_ok=True,scope=SCOPE,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},resources=dict(seconds=elapsed,peak_rss_MiB=rss,timeout_seconds=AUDIT_TIMEOUT_SEC,blas_threads=1,rss_limit_MiB=RSS_LIMIT_MIB))
    assert finite(output)
    if '--json' in sys.argv:print(json.dumps(output,allow_nan=False))
    else:
        print('FROZEN FOUR-ABLATION DIAGNOSIS: '+SCOPE)
        for name in 'ABCD':
            rr=[r for r in output['rows'] if r['ablation']==name]
            counts=[sum(r['support']>=4 for r in rr if r['side']=='pre' and r['step']==j) for j in range(1,5)]
            print('DATA '+name+' pre-support counts='+str(counts)+' trajectory fronts='+str(sum(t['front_pass'] for t in output['trajectories'] if t['ablation']==name))+'/24')
        print('ROWS '+str(len(output['rows']))+' TRAJECTORIES '+str(len(output['trajectories'])))
        print('VALIDATION '+json.dumps(output.get('comparison',{})))
        print('SOURCE_SHA256 '+output['source_sha256'])
        print('TIMING '+json.dumps(output['resources']))
        print('TOTAL: PASS FAIL=0')

AUDIT_INPUT_PATHS=('scripts/native_edge_record_autonomous_head_orbital_check_2026_09_07.py',)
import native_edge_record_autonomous_head_orbital_check_2026_09_07 as m
np=m.np
def calculate():
    e0,v0=np.linalg.eigh(m.hamiltonian(0));X=v0[:,:4].astype(complex);X[0]*=np.exp(-.7j);X[1]*=np.exp(.7j)
    c0=X@X.conj().T;c0e=v0.conj().T@c0@v0
    result={'rows':[],'totals':[],'trajectories':[]}
    for j,level in enumerate(m.paths()[1:],1):
     for path,head,mask,w,rates in level:
      for surface,k,mask2 in [('pre',j-1,mask^(1<<path[-1])),('post',j,mask)]:
       ev,vr=np.linalg.eigh(m.hamiltonian(mask2));U=vr.conj().T@v0
       gaps=e0[None,None,:,None]-e0[None,None,None,:]-ev[:,None,None,None]+ev[None,:,None,None]
       cr=np.einsum('am,mn,bn,abmn->ab',U,c0e,U.conj(),m.kernel(gaps))
       ideal=vr.conj().T@c0@vr
       covs={'A':m.average(cr,ev,vr,j,32,80),'B':vr@cr@vr.conj().T,'C':m.average(ideal,ev,vr,j,32,80),'D':c0}
       for name,c in covs.items():
        assert abs(np.trace(c).real-4)<1e-10 and np.max(abs(c-c.conj().T))<1e-12
        assert np.linalg.eigvalsh(c).min()>-1e-12 and np.linalg.eigvalsh(c).max()<1+1e-12
        o=m.observables(c,mask2);o.update(ablation=name,event=j,surface=surface,path=list(path),weight=str(w),mask=mask2,selected_current=o['currents'][path[-1]] if surface=='pre' else None)
        result['rows'].append(o)
    for name in 'ABCD':
     for j in range(1,5):
      for surface in ('pre','post'):
       rr=[r for r in result['rows'] if r['ablation']==name and r['event']==j and r['surface']==surface]
       result['totals'].append(dict(ablation=name,event=j,surface=surface,rows=len(rr),support4=sum(r['support_count']>=4 for r in rr),support_min=min(r['support_count'] for r in rr),support_max=max(r['support_count'] for r in rr),live_current_max=max(r['current_max'] for r in rr),live_current_max_min=min(r['current_max'] for r in rr),density_min=min(min(r['density']) for r in rr),density_max=max(max(r['density']) for r in rr),density_pass=sum(r['density_pass'] for r in rr),selected005=sum(abs(r['selected_current'])>=.05 for r in rr) if surface=='pre' else None))
     for path,head,mask,w,rates in m.paths()[4]:
      selected=[next(r['selected_current'] for r in result['rows'] if r['ablation']==name and r['surface']=='pre' and r['event']==j and tuple(r['path'])==path[:j]) for j in range(1,5)]
      result['trajectories'].append(dict(ablation=name,path=list(path),front_max=max(abs(x) for x in selected),front005=max(abs(x) for x in selected)>=.05))
    for r in result['rows']:
        r.update(step=r.pop('event'),side=r.pop('surface'),mask=4095^r['mask'],densities=r.pop('density'),support=r.pop('support_count'),matter_energy=r.pop('energy'),number=r.pop('N'),front_current=r.pop('selected_current'))
        r['rates']=[3]+[2]*(r['step']-1)
        for key in ('eigenvalues','hermiticity','current_max'):r.pop(key)
    for t in result['trajectories']:
        t['front_pass']=t.pop('front005')
        t['pre_support_pass']=all(next(r['support'] for r in result['rows'] if r['ablation']==t['ablation'] and r['side']=='pre' and r['path']==t['path'][:j])>=4 for j in range(1,5))
    assert len(result['rows'])==360 and len(result['trajectories'])==96
    return result

def main():
    started=time.monotonic();signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('audit timeout')));signal.alarm(AUDIT_TIMEOUT_SEC)
    finish(calculate(),started)
if __name__=='__main__':main()
