#!/usr/bin/env python3
"""Portable frozen A/B/C/D diagnosis; no width/rate/pulse sweeps.
A finite packet + waits; B finite packet + zero waits; C ideal + waits;
D ideal + zero waits. Ideal means overlap kernel one, not a normalized
finite-energy battery. Thresholds concern currents of averaged states.
Primary many-body route was independently implemented by the primary agent in
scratch before this portable packaging by the orbital-checker agent. The orbital
route was independently frozen before primary results were read; all360 rows
were then independently reproduced before this port.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import sys,json,hashlib,time,resource,signal,math,copy,subprocess,tempfile
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

AUDIT_INPUT_PATHS=('scripts/native_edge_record_autonomous_head_shared_battery_2026_09_07.py','scripts/native_edge_record_shared_battery_transport_2026_09_07.py','scripts/native_edge_record_autonomous_head_ablation_orbital_check_2026_09_07.py','scripts/native_edge_record_autonomous_head_orbital_check_2026_09_07.py')
import numpy as np
import native_edge_record_autonomous_head_shared_battery_2026_09_07 as p
def calculate():
    calc=p.Calculation();levels,terminal=p.enumerate_trails();rows=[];summaries=[];trajectories=[]
    worst=0.
    for label,finite,waits in [('A',True,True),('B',True,False),('C',False,True),('D',False,False)]:
        for j in range(1,5):
            for path in levels[j]:
                for side in ('pre','post'):
                    k=j-1 if side=='pre' else j
                    mask=path['mask'] | (1<<path['path'][-1]) if side=='pre' else path['mask']
                    h,b,V,rho0,_=calc.endpoint(mask)
                    if not finite:
                        x=V.conj().T@calc.psi
                        rho0=np.outer(x,x.conj())
                    rho=V@(rho0*(p.laplace(b,path['rates']) if waits else 1))@V.conj().T
                    herm,trace,mineig=p.parent.density_numerics(rho)
                    obs=p.parent.measure(rho,h,mask,calc.currents,calc.numbers)
                    worst=max(worst,herm,trace,-mineig,abs(obs['number']-4))
                    rows.append(dict(ablation=label,path=list(path['path']),side=side,step=j,mask=mask,
                        weight=str(path['weight']),rates=list(path['rates']),
                        densities=list(obs['densities']),currents=[obs['currents'].get(e,0.) for e in range(12)],number=obs['number'],
                        support=obs['support'],matter_energy=obs['energy'],front_current=obs['currents'].get(path['path'][-1]),
                        density_pass=min(obs['densities'])>=.1 and max(obs['densities'])<=.9))
        sub=[r for r in rows if r['ablation']==label]
        for j in range(1,5):
            for side in ('pre','post'):
                sel=[r for r in sub if r['step']==j and r['side']==side]
                assert sum((Fraction(r['weight']) for r in sel),Fraction())==1
                summaries.append(dict(ablation=label,step=j,side=side,support_min=min(r['support'] for r in sel),support_max=max(r['support'] for r in sel),support_pass=sum(r['support']>=4 for r in sel),density_pass=sum(r['density_pass'] for r in sel),density_min=min(min(r['densities']) for r in sel),density_max=max(max(r['densities']) for r in sel)))
        for path in levels[4]:
            pre=[next(r for r in sub if r['path']==list(path['path'][:j]) and r['side']=='pre') for j in range(1,5)]
            trajectories.append(dict(ablation=label,path=list(path['path']),front_max=max(abs(r['front_current']) for r in pre),front_pass=max(abs(r['front_current']) for r in pre)>=.05,pre_support_pass=all(r['support']>=4 for r in pre)))
    assert worst<2e-9 and len(rows)==360
    margin=min(abs(abs(x)-.02) for r in rows for x in r['currents'] if x!=0)
    return dict(rows=rows,totals=summaries,trajectories=trajectories,maximum_state_residual=worst,minimum_support_threshold_margin=margin)

def compare(expected,received):
    if not isinstance(received,dict) or not finite(received):raise ValueError('nonfinite or malformed payload')
    if set(received)!={'rows','totals','trajectories','schema','validation_ok','scope','source_sha256','dependencies','resources'}:raise ValueError('payload schema')
    if received['schema']!=SCHEMA or received['validation_ok'] is not True:raise ValueError('schema or validation failure')
    if type(received['scope']) is not str or received['scope']!=SCOPE:raise ValueError('scope mismatch')
    checker=ROOT/'scripts/native_edge_record_autonomous_head_ablation_orbital_check_2026_09_07.py'
    if received['source_sha256']!=hashlib.sha256(checker.read_bytes()).hexdigest():raise ValueError('checker hash mismatch')
    dep='scripts/native_edge_record_autonomous_head_orbital_check_2026_09_07.py'
    if received['dependencies']!={dep:hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()}:raise ValueError('dependency mismatch')
    resources=received['resources']
    if set(resources)!={'seconds','peak_rss_MiB','timeout_seconds','blas_threads','rss_limit_MiB'}:raise ValueError('resources schema')
    if any(type(resources[k]) not in (int,float) for k in ('seconds','peak_rss_MiB')):raise ValueError('resource numeric types')
    if any(type(resources[k]) is not int for k in ('timeout_seconds','blas_threads','rss_limit_MiB')):raise ValueError('resource integer types')
    if not (0<=resources['seconds']<180 and 0<resources['peak_rss_MiB']<180 and resources['timeout_seconds']==180 and resources['blas_threads']==1 and resources['rss_limit_MiB']==180):raise ValueError('execution envelope')
    rows=received['rows'];trajectories=received['trajectories']
    if not isinstance(rows,list) or len(rows)!=360 or not isinstance(trajectories,list) or len(trajectories)!=96:raise ValueError('exact counts')
    keys={'ablation','path','side','step','mask','weight','rates','densities','currents','number','support','matter_energy','front_current','density_pass'}
    mapped={};maximum=0.
    for r in rows:
        if not isinstance(r,dict) or set(r)!=keys:raise ValueError('row schema')
        if r['ablation'] not in 'ABCD' or len(r['ablation'])!=1 or r['side'] not in ('pre','post'):raise ValueError('labels')
        if type(r['step']) is not int or r['step'] not in (1,2,3,4) or not isinstance(r['path'],list) or len(r['path'])!=r['step']:raise ValueError('path timing')
        if any(type(e) is not int or not 0<=e<12 for e in r['path']):raise ValueError('path edge')
        if not isinstance(r['rates'],list) or len(r['rates'])!=r['step'] or any(type(rate) is not int or rate<=0 for rate in r['rates']):raise ValueError('rate tuple types')
        if type(r['mask']) is not int or type(r['support']) is not int or type(r['density_pass']) is not bool:raise ValueError('exact field types')
        if not isinstance(r['currents'],list) or len(r['currents'])!=12 or not isinstance(r['densities'],list) or len(r['densities'])!=8:raise ValueError('observable dimensions')
        if any(type(x) not in (int,float) for x in r['currents']+r['densities']+[r['number'],r['matter_energy']]):raise ValueError('numeric types')
        if r['side']=='post' and r['front_current'] is not None:raise ValueError('post front not applicable')
        if r['side']=='pre' and type(r['front_current']) not in (int,float):raise ValueError('pre front missing')
        key=(r['ablation'],r['step'],r['side'],tuple(r['path']))
        if key in mapped:raise ValueError('duplicate row')
        mapped[key]=r
    for r in expected['rows']:
        key=(r['ablation'],r['step'],r['side'],tuple(r['path']))
        if key not in mapped:raise ValueError('missing keyed row')
        q=mapped[key]
        for field in ('mask','weight','rates','support','density_pass'):
            if r[field]!=q[field]:raise ValueError('exact mismatch '+field)
        values=[abs(r['number']-q['number']),abs(r['matter_energy']-q['matter_energy'])]
        values.extend(abs(a-b) for field in ('currents','densities') for a,b in zip(r[field],q[field]))
        if r['side']=='pre':values.append(abs(r['front_current']-q['front_current']))
        maximum=max(maximum,max(values))
        if max(values)>2e-9:raise ValueError('observable mismatch')
    totals=received['totals']
    if not isinstance(totals,list) or len(totals)!=32:raise ValueError('total counts')
    totalkeys={'ablation','event','surface','rows','support4','support_min','support_max','live_current_max','live_current_max_min','density_min','density_max','density_pass','selected005'}
    seen=set()
    for total in totals:
        if not isinstance(total,dict) or set(total)!=totalkeys:raise ValueError('total schema')
        if any(type(total[k]) is not int for k in ('event','rows','support4','support_min','support_max','density_pass')):raise ValueError('total integer types')
        if total['selected005'] is not None and type(total['selected005']) is not int:raise ValueError('selected total integer type')
        key=(total['ablation'],total['event'],total['surface'])
        if key in seen:raise ValueError('duplicate total')
        seen.add(key)
        selected=[r for r in rows if (r['ablation'],r['step'],r['side'])==key]
        if not selected:raise ValueError('unknown total')
        exact=dict(rows=len(selected),support4=sum(r['support']>=4 for r in selected),support_min=min(r['support'] for r in selected),support_max=max(r['support'] for r in selected),density_pass=sum(r['density_pass'] for r in selected),selected005=sum(abs(r['front_current'])>=.05 for r in selected) if key[2]=='pre' else None)
        if any(total[k]!=v for k,v in exact.items()):raise ValueError('total exact mismatch')
        maxima=[max(abs(x) for x in r['currents']) for r in selected]
        values=dict(live_current_max=max(maxima),live_current_max_min=min(maxima),density_min=min(min(r['densities']) for r in selected),density_max=max(max(r['densities']) for r in selected))
        if any(type(total[k]) not in (int,float) or abs(total[k]-v)>2e-12 for k,v in values.items()):raise ValueError('total observable mismatch')
    tmap={}
    for t in trajectories:
        if not isinstance(t,dict) or set(t)!={'ablation','path','front_max','front_pass','pre_support_pass'}:raise ValueError('trajectory schema')
        if type(t['ablation']) is not str or t['ablation'] not in ('A','B','C','D'):raise ValueError('trajectory label')
        if not isinstance(t['path'],list) or len(t['path'])!=4 or any(type(e) is not int or not 0<=e<12 for e in t['path']):raise ValueError('trajectory path types')
        if type(t['front_max']) not in (int,float) or type(t['front_pass']) is not bool or type(t['pre_support_pass']) is not bool:raise ValueError('trajectory types')
        key=(t['ablation'],tuple(t['path']))
        if key in tmap:raise ValueError('duplicate trajectory')
        tmap[key]=t
    for t in expected['trajectories']:
        key=(t['ablation'],tuple(t['path']))
        if key not in tmap:raise ValueError('missing trajectory')
        q=tmap[key];difference=abs(t['front_max']-q['front_max']);maximum=max(maximum,difference)
        if difference>2e-9 or t['front_pass']!=q['front_pass'] or t['pre_support_pass']!=q['pre_support_pass']:raise ValueError('trajectory mismatch')
    return maximum

def main():
    started=time.monotonic();signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('audit timeout')));signal.alarm(AUDIT_TIMEOUT_SEC)
    expected=calculate()
    checker=ROOT/'scripts/native_edge_record_autonomous_head_ablation_orbital_check_2026_09_07.py'
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        completed=subprocess.run([sys.executable,str(checker),'--json'],stdout=stdout,stderr=stderr,cwd=ROOT,timeout=max(1,AUDIT_TIMEOUT_SEC-(time.monotonic()-started)))
        if completed.returncode!=0:raise RuntimeError('live checker failed with code '+str(completed.returncode))
        stdout.seek(0,2)
        if stdout.tell()>2_000_000:raise ValueError('checker payload too large')
        stdout.seek(0);raw=stdout.read().decode()
    def unique(pairs):
        result={}
        for key,value in pairs:
            if key in result:raise ValueError('duplicate JSON key')
            result[key]=value
        return result
    received=json.loads(raw,object_pairs_hook=unique,parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite JSON '+x)))
    residual=compare(expected,received)
    mutations={}
    for name in ('dropped_row','NaN','swapped_ablations','current_difference','float_rate','bool_trajectory_edge','wrong_scope','bool_threads','float_total'):
        bad=copy.deepcopy(received)
        if name=='dropped_row':bad['rows'].pop()
        elif name=='NaN':bad['rows'][0]['currents'][0]=float('nan')
        elif name=='swapped_ablations':
            for r in bad['rows']:
                if r['ablation'] in ('A','B'):r['ablation']='B' if r['ablation']=='A' else 'A'
        elif name=='current_difference':bad['rows'][0]['currents'][0]+=.01
        elif name=='float_rate':bad['rows'][0]['rates'][0]=float(bad['rows'][0]['rates'][0])
        elif name=='bool_trajectory_edge':bad['trajectories'][0]['path'][0]=False
        elif name=='wrong_scope':bad['scope']='C/D normalized finite-energy battery realizations'
        elif name=='bool_threads':bad['resources']['blas_threads']=True
        elif name=='float_total':bad['totals'][0]['rows']=float(bad['totals'][0]['rows'])
        try:compare(expected,bad)
        except (ValueError,TypeError,KeyError):mutations[name]=True
        else:mutations[name]=False
    assert all(mutations.values())
    expected['comparison']=dict(rows=360,trajectories=96,maximum_residual=residual,mutations=mutations,live_checker_sha256=received['source_sha256'])
    finish(expected,started)

if __name__=='__main__':
    try:main()
    except Exception as exc:
        if '--json' not in sys.argv:print('TOTAL: FAIL '+str(exc))
        raise
