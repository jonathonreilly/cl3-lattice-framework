"""Portable primary occupation-feedback calculation.
The primary agent independently froze the grouped70d prototype and raw results
before comparison with the orbital checker; the orbital agent packaged this port.

Importing defines functions only; main executes live independent validation. Post-event
states are unnormalized until conditioning on the complete edge path.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[key]='1'
import sys,json,hashlib,time,resource,signal,math,copy,subprocess,tempfile
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import numpy as np
import native_edge_record_autonomous_head_shared_battery_2026_09_07 as p


def hop(bits,v,w):
    removed=p.parent.ladder_action(bits,v,False)
    if removed is None: return None
    added=p.parent.ladder_action(removed[0],w,True)
    if added is None: return None
    return added[0],removed[1]*added[1]


def allowed(bits,head,mask):
    return [(edge,w,hop(bits,head,w)) for edge,w in p.choices(head,mask)
            if hop(bits,head,w) is not None]


def configuration_census(calc):
    """Enumerate every occupation-conditioned trail to traps with rational mass.

    Results contain all initial70 configurations, not just favorable ones.
    Tuple rows: initial_index,final_bits,head,mask,rate_tuple,fermion_sign,weight.
    Prefix and terminal probabilities are weighted by q_x only subsequently.
    """
    prefixes=defaultdict(list);traps=defaultdict(list)
    for x,bits in enumerate(calc.basis):
        def walk(path,bits,head,mask,rates,sign,weight):
            row=(x,bits,head,mask,rates,sign,weight)
            prefixes[path].append(row)
            options=allowed(bits,head,mask)
            if not options:
                traps[path].append(row)
                return
            for edge,w,(newbits,phase) in options:
                walk(path+(edge,),newbits,w,mask^(1<<edge),rates+(len(options),),sign*phase,weight/Fraction(len(options)))
        walk((),bits,0,p.FULL,(),1+0j,Fraction(1))
    # Independent exact per-initial-configuration mass accounting.
    for x in range(70):
        assert sum((r[-1] for rows in traps.values() for r in rows if r[0]==x),Fraction())==1
    return prefixes,traps


def initial_Q_moments(calc):
    K=p.parent.sine_overlap(calc.a[:,None]-calc.a[None,:])
    M=(p.MEAN+12*p.DELTA+(calc.a[:,None]+calc.a[None,:])/2)*K
    C=calc.sources
    q=np.einsum('xa,ab,xb->x',C,K,C.conj()).real
    energy=np.einsum('xa,ab,xb->x',C,M,C.conj()).real
    assert abs(sum(q)-1)<2e-9
    assert abs(sum(energy)-(calc.initial_energy+p.MEAN+12*p.DELTA))<2e-9
    return q,energy


def post_event(calc,path,records,q,qenergy,mutation=None):
    """All sign branches summed; normalized first-four signs each weigh2^-k.

    Uses complete occupation-dependent rate tuples. Direct EB is contracted
    independently of the Q ledger. Returns conditional density and EB plus
    unnormalized mass and direct conditioned Q mean.
    """
    assert 1<=len(path)<=4 and records
    k=len(path);mask=records[0][3]
    assert p.parent.component_count(mask)==1
    h,b,V,_,_=calc.endpoint(mask)
    index={bits:i for i,bits in enumerate(calc.basis)}
    groups={}
    for x,bits,head,rowmask,rates,sign,weight in records:
        assert rowmask==mask and all(r>0 for r in rates)
        if rates not in groups: groups[rates]=np.zeros_like(calc.sources)
        groups[rates][index[bits]]+=sign*calc.sources[x]
    amplitudes={rates:V.conj().T@vectors for rates,vectors in groups.items()}
    reduced=np.zeros((70,70),complex);EB=0j
    gap=b[:,None]-b[None,:]
    K0=p.parent.sine_overlap(calc.a[:,None]-calc.a[None,:])
    rates=list(amplitudes);A=np.array([amplitudes[g] for g in rates])
    L=np.ones((len(rates),len(rates),70,70),complex)
    for g,r in enumerate(rates):
        for other,t in enumerate(rates):
            for event,(rx,ry) in enumerate(zip(r,t)):
                rate=(rx+ry)/2
                if mutation=='constant_rates': rate=3 if event==0 else 2
                sign=-1 if mutation=='gap_sign' else 1
                L[g,other]*=p.GAMMA/(p.GAMMA*rate+sign*1j*gap)
            if mutation=='drop_cross_rate' and g!=other: L[g,other]=0
    for i in range(70):
        for j in range(70):
            K=p.parent.sine_overlap(calc.a[:,None]-calc.a[None,:]-b[i]+b[j])
            contraction=A[:,i,:]@K@A[:,j,:].conj().T
            reduced[i,j]=np.sum(L[:,:,i,j]*contraction)
        shift=0 if mutation=='omit_fuel' else k*p.DELTA
        M=(p.MEAN+(calc.a[:,None]+calc.a[None,:])/2-b[i]+shift)*K0
        EB+=np.sum(L[:,:,i,i]*(A[:,i,:]@M@A[:,i,:].conj().T))
    rho=V@reduced@V.conj().T
    mass=float(np.trace(rho).real)
    census_mass=sum(q[r[0]]*float(r[-1]) for r in records)
    total_Q=sum(qenergy[r[0]]*float(r[-1]) for r in records)
    if mutation is None: assert abs(mass-census_mass)<2e-9 and mass>0
    assert abs(EB.imag)<2e-9
    rho/=mass;EB=float(EB.real)/mass;total_Q/=mass
    Em=float(np.trace(rho@h).real)
    if mutation is None: assert abs(Em+EB+(12-k)*p.DELTA-total_Q)<2e-8
    return dict(density=rho,battery_energy=EB,matter_energy=Em,
                probability=mass,total_energy=total_Q,rate_tuples=list(groups),
                live_mask=mask,spent_fuel=k,sign_branch_probability=mass/2**k)

AUDIT_INPUT_PATHS=('scripts/native_edge_record_autonomous_head_shared_battery_2026_09_07.py','scripts/native_edge_record_shared_battery_transport_2026_09_07.py','scripts/native_edge_record_occupation_feedback_orbital_check_2026_09_07.py')

AUDIT_TIMEOUT_SEC=180
RSS_LIMIT_MIB=180
SCHEMA='occupation-feedback-shared-battery-v1'
ROOT=Path(__file__).resolve().parents[1]
SCOPE='Post-event conditional states; all reach/dark/trap mass retained. Headempty dark refers to the TOTAL-ENERGY-FIBER occupation dictionary, not bare physical occupation. Supplied changed law, no optimization or nonnegative battery drift theorem.'
def finite(x):
    if isinstance(x,float):return math.isfinite(x)
    if isinstance(x,dict):return all(finite(v) for v in x.values())
    if isinstance(x,(list,tuple)):return all(finite(v) for v in x)
    return True
def emit(result,started):
    elapsed=time.monotonic()-started
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
    assert elapsed<180 and rss<180
    result.update(schema=SCHEMA,validation_ok=True,scope=SCOPE,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},resources=dict(seconds=elapsed,peak_rss_MiB=rss,timeout_seconds=180,blas_threads=1,rss_limit_MiB=180))
    assert finite(result)
    if '--json' in sys.argv:print(json.dumps(result,allow_nan=False))
    else:
        print('OCCUPATION FEEDBACK: '+SCOPE)
        for j in range(1,5):
            rr=[r for r in result['rows'] if r.get('event',r.get('step'))==j]
            print('DATA post'+str(j)+' prefixes='+str(len(rr))+' mass='+str(sum(r['probability'] for r in rr)))
        print('VALIDATION '+json.dumps(result.get('comparison',{})))
        print('per_element: checked all live-edge currents on all45 post-event conditioned prefixes.')
        print('per_site: checked all eight densities and fixedN4 on every positive-probability prefix.')
        print('per_mode: checked full fixedN occupation/spectral coherences and all zero-gap rate-tuple terms.')
        print('per_block: checked conditioned totalQ and direct battery energy, all292 exact configuration-prefix records and complete dark/trap census.')
        print('lattice_wide: checked and not executed -- finite supplied feedback law does not resolve infinite-lattice formation, locality, entropy or renewal.')
        print('SOURCE_SHA256 '+result['source_sha256'])
        print('TIMING '+json.dumps(result['resources']))
        print('TOTAL: PASS FAIL=0')

def calculate():
    started=time.monotonic();c=p.Calculation();prefixes,traps=configuration_census(c);q,Q=initial_Q_moments(c)
    levels,_=p.enumerate_trails();rows=[];worst=defaultdict(float)
    q_wrong=abs(c.psi)**2
    law_census=[]
    for depth in range(max(map(len,prefixes))+1):
        reached=sum(q[r[0]]*float(r[-1]) for path,rs in prefixes.items() if len(path)==depth for r in rs)
        earlier_traps=sum(q[r[0]]*float(r[-1]) for path,rs in traps.items() if len(path)<depth for r in rs)
        assert abs(reached+earlier_traps-1)<2e-12
        law_census.append(dict(events=depth,reached_mass=reached,earlier_trapped_mass=earlier_traps,total=reached+earlier_traps,
            edge_prefixes=sum(len(path)==depth for path in prefixes),configuration_prefixes=sum(len(rs) for path,rs in prefixes.items() if len(path)==depth)))
    trap_rows=[]
    for path,rs in sorted(traps.items(),key=lambda x:(len(x[0]),x[0])):
        classes=defaultdict(float)
        for r in rs:
            x,bits,head,mask,rates,phase,w=r
            label='head_empty' if not bits&(1<<head) else ('graph_trap' if not p.choices(head,mask) else 'occupied_head_no_vacant_neighbor')
            classes[label]+=q[x]*float(w)
        trap_rows.append(dict(path=list(path),mass=sum(classes.values()),classes=dict(classes),configuration_count=len(rs)))
    assert abs(sum(r['mass'] for r in trap_rows)-1)<2e-12
    for depth in range(1,5):
        for graph in levels[depth]:
            path=graph['path'];rs=prefixes.get(path,[])
            if not rs:
                rows.append(dict(path=list(path),step=depth,probability=0.,zero_probability=True))
                continue
            out=post_event(c,path,rs,q,Q);rho=out.pop('density')
            obs=p.parent.measure(rho,c.endpoint(graph['mask'])[0],graph['mask'],c.currents,c.numbers)
            herm,trace,mineig=p.parent.density_numerics(rho)
            worst['hermiticity']=max(worst['hermiticity'],herm);worst['trace']=max(worst['trace'],trace)
            worst['negative_eigenvalue']=max(worst['negative_eigenvalue'],-mineig);worst['N']=max(worst['N'],abs(obs['number']-4))
            worst['conditional_ledger']=max(worst['conditional_ledger'],abs(out['matter_energy']+out['battery_energy']+12-depth-out['total_energy']))
            mass_direct=sum(q[r[0]]*float(r[-1]) for r in rs)
            worst['census_vs_spectral_mass']=max(worst['census_vs_spectral_mass'],abs(mass_direct-out['probability']))
            rows.append(dict(path=list(path),step=depth,head=graph['head'],zero_probability=False,**out,
                densities=list(obs['densities']),currents={str(e):v for e,v in obs['currents'].items()},support=obs['support'],
                density_window_ok=min(obs['densities'])>=.1 and max(obs['densities'])<=.9,
                allowed_configurations=len(rs),group_counts={','.join(map(str,g)):sum(r[4]==g for r in rs) for g in out['rate_tuples']},
                wrong_initial_weight_probability=sum(q_wrong[r[0]]*float(r[-1]) for r in rs)))
    # Targeted mutants on an early prefix with multiple nontrivial rate groups.
    pth=(0,3);rs=prefixes[pth];baseline=post_event(c,pth,rs,q,Q);mutations={}
    for name in ('constant_rates','drop_cross_rate','gap_sign','omit_fuel'):
        wrong=post_event(c,pth,rs,q,Q,name)
        mutations[name]=dict(density_difference=float(np.max(abs(wrong['density']-baseline['density']))),mass_difference=abs(wrong['probability']-baseline['probability']),battery_difference=abs(wrong['battery_energy']-baseline['battery_energy']))
        assert max(mutations[name].values())>1e-7
    mutations['wrong_initial_weights']=dict(difference=max(abs(r['probability']-r['wrong_initial_weight_probability']) for r in rows if not r['zero_probability']))
    mutations['lost_dark_mass']=dict(difference=1-law_census[1]['reached_mass'])
    mutations['incorrect_global_conditional_energy']=dict(difference=max(abs(r['total_energy']-(c.initial_energy+p.MEAN+12)) for r in rows if not r['zero_probability']))
    assert all(max(v.values())>1e-7 for v in mutations.values())
    assert len(rows)==45 and max(worst.values())<2e-8
    summary=[]
    for depth in range(1,5):
        rr=[r for r in rows if r['step']==depth and not r['zero_probability']]
        summary.append(dict(step=depth,positive_paths=len(rr),reached_mass=sum(r['probability'] for r in rr),support_min=min(r['support'] for r in rr),support_max=max(r['support'] for r in rr),support_pass=sum(r['support']>=4 for r in rr),density_pass=sum(r['density_window_ok'] for r in rr)))
    base=Path(__file__).parent
    result=dict(law='B_ez=K_ez c_w^dagger c_v; rate gamma sum n_v(1-n_w); supplied changed conditional formation law',fixture=dict(N=4,gamma=1,t=1,Delta=1,head=0,packet=[48,49],cap=[0,97]),rows=rows,summary=summary,census=law_census,traps=trap_rows,
        initial_occupation_Q_weights=list(q),initial_occupation_Q_first_moments=list(Q),basis=list(c.basis),
        exact_configuration_paths=[dict(path=list(path),records=[dict(initial_index=r[0],final_bits=r[1],head=r[2],mask=r[3],rates=list(r[4]),fermion_sign=float(r[5].real),weight=str(r[6])) for r in rs]) for path,rs in sorted(prefixes.items(),key=lambda x:(len(x[0]),x[0]))],
        controls=dict(worst=worst,mutations=mutations),resources=dict(seconds=time.monotonic()-started,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)),
        scope='Post-event conditional states only. Full reach+dark+trap mass retained. No pre instrument, no optimization, no axiomatic derivation or fuel monotonicity clai')
    return result

def compare(expected,got):
    if not isinstance(got,dict) or not finite(got):raise ValueError('nonfinite/malformed checker')
    top={'schema','source_sha256','initial_energy_groups','initial_Q_mean','initial_q','initial_Q_first_moments','basis','initial_Q_quadrature_convergence','rows','event_mass','census','time_density_checks','adaptive_family_max_difference','max_time_convergence','max_battery_convergence','max_ledger_residual','max_battery_norm_residual','resources','validation_ok','scope','dependencies'}
    if set(got)!=top or got['schema']!=SCHEMA or got['validation_ok'] is not True:raise ValueError('checker schema')
    if type(got['scope']) is not str or got['scope']!=SCOPE:raise ValueError('scope mismatch')
    if got['dependencies']!={}:raise ValueError('unexpected orbital dependency')
    checker=ROOT/'scripts/native_edge_record_occupation_feedback_orbital_check_2026_09_07.py'
    if got['source_sha256']!=hashlib.sha256(checker.read_bytes()).hexdigest():raise ValueError('checker source identity')
    rr=got['resources']
    if set(rr)!={'seconds','peak_rss_MiB','timeout_seconds','blas_threads','rss_limit_MiB'}:raise ValueError('resource schema')
    if any(type(rr[k]) not in (int,float) for k in ('seconds','peak_rss_MiB')) or any(type(rr[k]) is not int for k in ('timeout_seconds','blas_threads','rss_limit_MiB')):raise ValueError('resource types')
    if not (0<=rr['seconds']<180 and 0<rr['peak_rss_MiB']<180 and rr['timeout_seconds']==180 and rr['blas_threads']==1 and rr['rss_limit_MiB']==180):raise ValueError('resource envelope')
    if not isinstance(got['initial_energy_groups'],list) or len(got['initial_energy_groups'])!=5 or any(type(e) not in (int,float) for e in got['initial_energy_groups']):raise ValueError('spectral group count/types')
    if not isinstance(got['time_density_checks'],list):raise ValueError('time certificate list')
    certificate_keys=set()
    for certificate in got['time_density_checks']:
        if not isinstance(certificate,dict) or set(certificate)!={'rates','tail','norm_error','mean_error','variance_error','min_density'}:raise ValueError('time certificate schema')
        if not isinstance(certificate['rates'],list) or not 1<=len(certificate['rates'])<=4 or any(type(r) not in (int,float) or r not in (1.,1.5,2.,2.5,3.) for r in certificate['rates']):raise ValueError('time rates')
        key=tuple(certificate['rates'])
        if key in certificate_keys:raise ValueError('duplicate time certificate')
        certificate_keys.add(key)
        if any(type(certificate[k]) not in (int,float) for k in ('tail','norm_error','mean_error','variance_error','min_density')):raise ValueError('certificate numeric types')
        if not (0<=certificate['tail']<1e-18 and 0<=certificate['norm_error']<2e-12 and 0<=certificate['mean_error']<1e-10 and 0<=certificate['variance_error']<1e-10 and certificate['min_density']>-1e-12):raise ValueError('time certificate failure')
    if any(type(got[k]) not in (int,float) for k in ('adaptive_family_max_difference','initial_Q_quadrature_convergence')):raise ValueError('family numeric types')
    if not got['time_density_checks'] or not 0<=got['adaptive_family_max_difference']<=2e-11 or not 0<=got['initial_Q_quadrature_convergence']<=2e-10:raise ValueError('quadrature family failure')
    def numeric(v):
        if type(v) not in (float,int):raise ValueError('nonnumeric observable')
        return v
    maxdiff=0.
    def close(a,b,tol=2e-9):
        nonlocal maxdiff
        diff=abs(numeric(a)-numeric(b));maxdiff=max(maxdiff,diff)
        if diff>tol:raise ValueError('numeric mismatch')
    def pathkey(path):
        if not isinstance(path,list) or any(type(e) is not int or not 0<=e<12 for e in path):raise ValueError('path type')
        return tuple(path)
    rows=got['rows']
    if not isinstance(rows,list) or len(rows)!=45:raise ValueError('45 rows required')
    rowkeys={'path','event','mask','probability','densities','currents','N','matter_energy','battery_energy','conditional_totalQ','ledger_residual','battery_norm_residual','time_convergence','battery_convergence','active_occupations','rate_groups','battery_support','head','zero_probability'}
    mapped={}
    for r in rows:
        if not isinstance(r,dict) or set(r)!=rowkeys:raise ValueError('row schema')
        key=pathkey(r['path'])
        if key in mapped or not 1<=len(key)<=4:raise ValueError('duplicate/invalid prefix')
        mapped[key]=r
        if any(type(r[k]) is not int for k in ('event','mask','head','active_occupations')) or type(r['zero_probability']) is not bool:raise ValueError('discrete types')
        if len(r['densities'])!=8 or len(r['currents'])!=12 or len(r['battery_support'])!=2:raise ValueError('observable dimension')
        if not isinstance(r['rate_groups'],list) or any(not isinstance(g,list) or len(g)!=len(key) or any(type(v) is not int or not 1<=v<=3 for v in g) for g in r['rate_groups']):raise ValueError('rate group types')
        if r['event']!=len(key):raise ValueError('event indexing')
        if r['zero_probability'] or r['probability']<=0:raise ValueError('frozen positive path replaced by zero')
        if any(type(r[k]) not in (int,float) for k in ('probability','ledger_residual','battery_norm_residual','time_convergence','battery_convergence')):raise ValueError('row certificate numeric types')
        if any(type(v) not in (int,float) for v in r['battery_support']):raise ValueError('support numeric types')
        if any(not 0<=r[k]<=2e-9 for k in ('time_convergence','battery_convergence')):raise ValueError('quadrature convergence')
        if abs(r['ledger_residual'])>2e-8 or abs(r['battery_norm_residual'])>2e-9:raise ValueError('independent ledger/norm')
        if not 0<=r['battery_support'][0]<=r['battery_support'][1]<=97:raise ValueError('cap support')
    required_certificates={tuple((a+b)/2 for a,b in zip(g,h)) for r in rows for g in r['rate_groups'] for h in r['rate_groups']}
    if certificate_keys!=required_certificates:raise ValueError('complete time certificate coverage')
    for aggregate,field in (('max_time_convergence','time_convergence'),('max_battery_convergence','battery_convergence'),('max_ledger_residual','ledger_residual'),('max_battery_norm_residual','battery_norm_residual')):
        if type(got[aggregate]) not in (int,float) or got[aggregate]!=max(abs(r[field]) for r in rows):raise ValueError('aggregate row binding '+aggregate)
    for r in expected['rows']:
        key=tuple(r['path'])
        if key not in mapped:raise ValueError('missing keyed prefix')
        q=mapped[key]
        if (q['head'],q['mask'],q['active_occupations'],q['event'],q['zero_probability'])!=(r['head'],r['live_mask'],r['allowed_configurations'],r['step'],r['zero_probability']):raise ValueError('path discrete mismatch')
        if sorted(map(tuple,q['rate_groups']))!=sorted(map(tuple,r['rate_tuples'])):raise ValueError('rate tuple mismatch')
        for k in ('probability','matter_energy','battery_energy'):close(q[k],r[k])
        close(q['conditional_totalQ'],r['total_energy']);close(q['N'],4)
        for a,b in zip(q['densities'],r['densities']):close(a,b)
        if set(r['currents'])!={str(e) for e in range(12) if q['mask']>>e&1}:raise ValueError('primary live currents')
        for e,a in enumerate(q['currents']):close(a,r['currents'].get(str(e),0.))
        if sum(abs(v)>=.02 for e,v in enumerate(q['currents']) if q['mask']>>e&1)!=r['support']:raise ValueError('support count')
        if (min(q['densities'])>=.1 and max(q['densities'])<=.9)!=r['density_window_ok']:raise ValueError('density comparator')
    basis=got['basis']
    if not isinstance(basis,list) or any(type(bits) is not int for bits in basis) or len(basis)!=70 or len(set(basis))!=70 or set(basis)!=set(expected['basis']):raise ValueError('basis coverage')
    if len(got['initial_q'])!=70 or len(got['initial_Q_first_moments'])!=70:raise ValueError('Q dimensions')
    initial={bits:(got['initial_q'][i],got['initial_Q_first_moments'][i]) for i,bits in enumerate(basis)}
    for i,bits in enumerate(expected['basis']):
        close(initial[bits][0],expected['initial_occupation_Q_weights'][i]);close(initial[bits][1],expected['initial_occupation_Q_first_moments'][i])
    close(sum(got['initial_q']),1);close(sum(got['initial_Q_first_moments']),got['initial_Q_mean'])
    census=got['census']
    if set(census)!={'configuration_paths','trap_prefixes','reach','terminal','occupations'}:raise ValueError('census schema')
    if len(census['reach'])!=13 or len(got['event_mass'])!=4:raise ValueError('reach dimensions')
    for j in range(13):
        reference=next((r['reached_mass'] for r in expected['census'] if r['events']==j),0.)
        close(census['reach'][j],reference)
        if 1<=j<=4:close(got['event_mass'][j-1],reference)
    configs={}
    for block in census['configuration_paths']:
        if set(block)!={'path','records'}:raise ValueError('configuration block schema')
        path=pathkey(block['path'])
        for record in block['records']:
            if set(record)!={'initial_bits','final_bits','head','mask','rates','fermion_sign','weight'}:raise ValueError('configuration record schema')
            if any(type(record[k]) is not int for k in ('initial_bits','final_bits','head','mask','fermion_sign')) or record['fermion_sign'] not in (-1,1) or type(record['weight']) is not str:raise ValueError('configuration discrete types')
            if not isinstance(record['rates'],list) or len(record['rates'])!=len(path) or any(type(v) is not int or not 1<=v<=3 for v in record['rates']):raise ValueError('configuration rate types')
            key=(path,record['initial_bits'])
            if key in configs:raise ValueError('duplicate configuration record')
            configs[key]={k:v for k,v in record.items() if k!='initial_bits'}
    reference={}
    for block in expected['exact_configuration_paths']:
        for record in block['records']:
            key=(tuple(block['path']),expected['basis'][record['initial_index']])
            reference[key]={k:v for k,v in record.items() if k!='initial_index'}
    if len(configs)!=292 or configs!=reference:raise ValueError('exact full configuration census')
    tmap={}
    labels={'headempty_dark':'head_empty','graph_trap':'graph_trap','exclusion_block':'occupied_head_no_vacant_neighbor'}
    for t in census['trap_prefixes']:
        if set(t)!={'path','mass','classes','configuration_count'}:raise ValueError('trap schema')
        key=pathkey(t['path'])
        if key in tmap:raise ValueError('duplicate trap')
        if any(k not in labels for k in t['classes']):raise ValueError('trap class')
        tmap[key]=t
    if len(tmap)!=46 or tmap.keys()!={tuple(t['path']) for t in expected['traps']}:raise ValueError('complete trap prefix coverage')
    for t in expected['traps']:
        q=tmap[tuple(t['path'])];classes={labels[k]:v for k,v in q['classes'].items()}
        if type(q['configuration_count']) is not int or q['configuration_count']!=t['configuration_count'] or classes.keys()!=t['classes'].keys():raise ValueError('trap discrete mismatch')
        close(q['mass'],t['mass'])
        for k,v in classes.items():close(v,t['classes'][k])
    close(sum(t['mass'] for t in tmap.values()),1)
    if 'headempty_dark' not in tmap[()]['classes']:raise ValueError('dark mass missing')
    close(tmap[()]['classes']['headempty_dark'],.5)
    # Independently retain zero/tiny terminal rows and per-initial exact mass.
    aggregate={}
    for path,t in tmap.items():
        for kind,mass in t['classes'].items():aggregate[len(path),kind]=aggregate.get((len(path),kind),0.)+mass
    terminal={}
    for t in census['terminal']:
        if set(t)!={'events','kind','mass'} or type(t['events']) is not int or t['kind'] not in labels:raise ValueError('terminal schema')
        key=t['events'],t['kind']
        if key in terminal:raise ValueError('duplicate terminal')
        terminal[key]=t['mass']
    if terminal.keys()!=aggregate.keys():raise ValueError('terminal coverage')
    for key in terminal:close(terminal[key],aggregate[key])
    exact_terminals={bits:{} for bits in basis}
    for (path,bits),record in reference.items():
        if not allowed(record['final_bits'],record['head'],record['mask']):
            kind='headempty_dark' if not record['final_bits']>>record['head']&1 else ('graph_trap' if not p.choices(record['head'],record['mask']) else 'exclusion_block')
            key=(len(path),kind)
            exact_terminals[bits][key]=exact_terminals[bits].get(key,Fraction())+Fraction(record['weight'])
    occupations=census['occupations']
    if len(occupations)!=70 or {x['bits'] for x in occupations}!=set(basis):raise ValueError('occupation terminal coverage')
    for occ in occupations:
        if set(occ)!={'bits','q','terminal'} or type(occ['bits']) is not int:raise ValueError('occupation schema')
        close(occ['q'],initial[occ['bits']][0])
        actual_terminals={}
        for t in occ['terminal']:
            if not isinstance(t,dict) or set(t)!={'events','kind','conditional_weight'} or type(t['events']) is not int or t['kind'] not in labels or type(t['conditional_weight']) is not str:raise ValueError('occupation terminal schema')
            key=(t['events'],t['kind'])
            if key in actual_terminals:raise ValueError('duplicate occupation terminal')
            actual_terminals[key]=Fraction(t['conditional_weight'])
        if actual_terminals!=exact_terminals[occ['bits']]:raise ValueError('exact occupation terminal distribution')
        if sum(actual_terminals.values(),Fraction())!=1:raise ValueError('exact terminal occupation mass')
    return maxdiff

def main():
    started=time.monotonic();signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('180 seconds')));signal.alarm(180)
    result=json.loads(json.dumps(calculate(),allow_nan=False));checker=ROOT/'scripts/native_edge_record_occupation_feedback_orbital_check_2026_09_07.py'
    with tempfile.TemporaryFile() as out,tempfile.TemporaryFile() as err:
        cp=subprocess.run([sys.executable,str(checker),'--json'],cwd=ROOT,stdout=out,stderr=err,timeout=max(1,180-(time.monotonic()-started)))
        if cp.returncode:
            err.seek(0);raise RuntimeError('live checker failed '+str(cp.returncode)+': '+err.read(4000).decode(errors='replace'))
        out.seek(0,2)
        if out.tell()>2_000_000:raise ValueError('checker output over2MB')
        out.seek(0);raw=out.read().decode()
    def unique(pairs):
        d={}
        for k,v in pairs:
            if k in d:raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    got=json.loads(raw,object_pairs_hook=unique,parse_constant=lambda s: (_ for _ in ()).throw(ValueError('nonfinite JSON')))
    residual=compare(result,got);mutations={}
    for name in ('missing_row','NaN','wrong_conditionalQ','current_difference','lost_dark_mass','wrong_CAR_sign','wrong_scope','bool_threads','float_basis','missing_time_certificates','duplicate_time_certificate','invented_time_rate','untrue_max_residual','terminal_depth12','duplicate_terminal','omitted_terminal'):
        bad=copy.deepcopy(got)
        if name=='missing_row':bad['rows'].pop()
        elif name=='NaN':bad['rows'][0]['battery_energy']=float('nan')
        elif name=='wrong_conditionalQ':bad['rows'][0]['conditional_totalQ']=bad['initial_Q_mean']
        elif name=='current_difference':bad['rows'][0]['currents'][1]+=.01
        elif name=='lost_dark_mass':bad['census']['trap_prefixes'][0]['classes'].pop('headempty_dark')
        elif name=='wrong_CAR_sign':bad['census']['configuration_paths'][0]['records'][0]['fermion_sign']*=-1
        elif name=='wrong_scope':bad['scope']='Head-empty means bare occupation; battery cannot decrease'
        elif name=='bool_threads':bad['resources']['blas_threads']=True
        elif name=='float_basis':bad['basis'][0]=float(bad['basis'][0])
        elif name=='missing_time_certificates':bad['time_density_checks']=bad['time_density_checks'][:1]
        elif name=='duplicate_time_certificate':bad['time_density_checks'].append(copy.deepcopy(bad['time_density_checks'][0]))
        elif name=='invented_time_rate':bad['time_density_checks'][0]['rates']=[3.,3.,3.,3.]
        elif name=='untrue_max_residual':bad['max_ledger_residual']=99.
        elif name=='terminal_depth12':bad['census']['occupations'][0]['terminal'][0]['events']=12
        elif name=='duplicate_terminal':bad['census']['occupations'][0]['terminal'].append(copy.deepcopy(bad['census']['occupations'][0]['terminal'][0]))
        elif name=='omitted_terminal':bad['census']['occupations'][0]['terminal'].pop()
        try:compare(result,bad)
        except (ValueError,TypeError,KeyError):mutations[name]=True
        else:mutations[name]=False
    assert all(mutations.values())
    margin=min(abs(abs(v)-.02) for r in result['rows'] if not r['zero_probability'] for v in r['currents'].values())
    result['comparison']=dict(rows=45,configuration_records=292,trap_prefixes=46,maximum_residual=residual,minimum_current_threshold_margin=margin,mutations=mutations,live_checker_sha256=got['source_sha256'])
    emit(result,started)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        if '--json' not in sys.argv:print('TOTAL: FAIL '+str(exc))
        raise
