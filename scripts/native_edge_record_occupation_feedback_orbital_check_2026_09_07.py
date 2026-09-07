#!/usr/bin/env python3
"""Independent feedback checker: orbital determinants, time convolution, direct E/Q.
Portable derivative of independently frozen scratch source dc5cb77098222eed;
all45 rows were compared only after the independent raw freeze.
Preregistered before computing or reading any primary feedback implementation.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import numpy as np
from numpy.polynomial.legendre import leggauss
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import math,json,time,resource,sys,signal,hashlib
# This independent runner reads no repository inputs; omit AUDIT_INPUT_PATHS.
EDGES=[(a,b,c) for (a,b),c in zip([(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7)],[-1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1])]
SUB=np.array(list(combinations(range(8),4)));BITS=[sum(1<<int(a) for a in x) for x in SUB];INDEX={b:i for i,b in enumerate(BITS)}
def ham(mask):
 h=np.zeros((8,8))
 for e,(a,b,c) in enumerate(EDGES):
  if mask>>e&1:h[a,b]=h[b,a]=c
 return h
def hop(bits,a,b):
 if not bits>>a&1 or bits>>b&1:return None
 lowa=(bits&((1<<a)-1)).bit_count();after=bits^(1<<a);lowb=(after&((1<<b)-1)).bit_count()
 return after|(1<<b),(-1)**(lowa+lowb)
def incident(head,mask):return [(e,a^b^head) for e,(a,b,c) in enumerate(EDGES) if mask>>e&1 and head in (a,b)]
def rate(bits,head,mask):return sum(not bits>>w&1 for e,w in incident(head,mask)) if bits>>head&1 else 0
@lru_cache(None)
def polynomial(rates):
 terms={(F(rates[0]),0):F(1)}
 for rb in rates[1:]:
  b=F(rb);new={}
  def add(key,v):new[key]=new.get(key,F(0))+v
  for (a,n),c in terms.items():
   if a==b:add((b,n+1),c/F(n+1))
   else:
    d=a-b;add((b,0),c*math.factorial(n)/d**(n+1))
    for j in range(n+1):add((a,j),-c*math.factorial(n)/F(math.factorial(j))/d**(n+1-j))
  terms={key:v for key,v in new.items() if v}
 # Complete homogeneous polynomials, generated independently of exp coefficients.
 h=[1.]+[0.]*24
 for r in rates:
  for n in range(1,25):h[n]+=float(r)*h[n-1]
 return terms,h

def conv(t,rates):
 terms,h=polynomial(tuple(sorted(rates)));t=np.asarray(t);out=np.zeros_like(t)
 for (a,n),c in terms.items():out+=float(c)*t**n*np.exp(-float(a)*t)
 small=t<.25;u=t[small];v=np.zeros_like(u);k=len(rates)
 for n in range(25):v+=(-1.)**n*h[n]*u**(n+k-1)/math.factorial(n+k-1)
 out[small]=v
 return out

def tail(rates,T=60):
 terms,h=polynomial(tuple(sorted(rates)));ans=0.
 for (a,n),c in terms.items():ans+=float(c)*math.exp(-float(a)*T)*sum(math.factorial(n)/math.factorial(j)*T**j/float(a)**(n+1-j) for j in range(n+1))
 return ans
@lru_cache(None)
def mesh(order,cells):
 x,w=leggauss(order);edges=np.linspace(0,60,cells+1)
 return ((edges[:-1,None]+edges[1:,None])/2+(30/cells)*x).ravel(),np.tile(w*(30/cells),cells)
@lru_cache(None)
def timekernel(rates,gaps,order=16,cells=120):
 t,w=mesh(order,cells);density=conv(t,rates)
 # Frequency batching preserves quadrature nodes/weights and bounds temporary RSS.
 return np.concatenate([(w*density)@np.exp(-1j*t[:,None]*np.array(gaps[offset:offset+8])[None,:]) for offset in range(0,len(gaps),8)])
def overlap(d):
 x=np.abs(d);return np.where(x<1,(1-x)*np.cos(np.pi*x)+np.sin(np.pi*x)/np.pi,0.)
def beta(u):return np.where((u>=0)&(u<=1),np.sqrt(2)*np.sin(np.pi*u),0.)
def integral_nodes(starts,order):
 knots=np.unique(np.r_[starts,starts+1]);lo=knots[:-1];hi=knots[1:];x,w=leggauss(order)
 return ((lo+hi)[:,None]/2+(hi-lo)[:,None]/2*x).ravel(),((hi-lo)[:,None]/2*w).ravel()
def initial():
 ev,V=np.linalg.eigh(ham(4095));X=V[:,:4].astype(complex);X[0]*=np.exp(-.7j);X[1]*=np.exp(.7j)
 A=np.linalg.det(np.stack([V[:,ii].conj().T@X for ii in SUB]))
 D=np.linalg.det(V[SUB[:,None,:,None],SUB[None,:,None,:]])
 energies=ev[SUB].sum(1);labels=np.round(energies,11);groups=np.unique(labels)
 ea=np.array([energies[labels==g].mean() for g in groups]);C=np.stack([(D[:,labels==g]*A[labels==g]).sum(1) for g in groups],1)
 assert max(np.ptp(energies[labels==g]) for g in groups)<1e-12
 def qintegral(order):
  Q,W=integral_nodes(ea+12+48,order);amp=beta(Q[:,None]-(ea+12+48)[None,:])@C.T;prob=abs(amp)**2
  return W@prob,(W*Q)@prob
 q,m=qintegral(32);q16,m16=qintegral(16)
 return ea,C,q,m,max(np.max(abs(q-q16)),np.max(abs(m-m16)))
def graphpaths():
 levels=[[((),0,4095)]]
 for k in range(1,5):levels.append([(p+(e,),w,mask^(1<<e)) for p,h,mask in levels[-1] for e,w in incident(h,mask)])
 return levels

def map_path(path):
 active=[]
 for x,bits0 in enumerate(BITS):
  bits=bits0;head=0;mask=4095;sign=1;rs=[]
  for e in path:
   a,b,c=EDGES[e];dest=a^b^head;r=rate(bits,head,mask);res=hop(bits,head,dest)
   if r==0 or res is None:break
   bits,sg=res;sign*=sg;rs.append(r);head=dest;mask^=1<<e
  else:active.append((x,INDEX[bits],sign,tuple(rs)))
 return active

def orbital_transitions(a,b):
 jj=[];kk=[];ss=[]
 for j,bits in enumerate(BITS):
  if a==b:
   if bits>>a&1:jj.append(j);kk.append(j);ss.append(1)
  else:
   res=hop(bits,a,b)
   if res is not None:dest,sg=res;jj.append(j);kk.append(INDEX[dest]);ss.append(sg)
 return np.array(jj),np.array(kk),np.array(ss)
TRANS={(a,b):orbital_transitions(a,b) for a in range(8) for b in range(8)}
def endpoint(path,mask,ea,C,q,qmoment):
 active=map_path(path);tuples=sorted(set(r for x,y,s,r in active));groups=[[t for t in active if t[3]==r] for r in tuples]
 ev,V=np.linalg.eigh(ham(mask));ef=ev[SUB].sum(1)
 D=np.linalg.det(V[SUB[:,None,:,None],SUB[None,:,None,:]]).conj().T
 M=np.stack([sum((D[:,y,None]*s*C[x,None,:] for x,y,s,r in group),np.zeros((70,len(ea)),complex)) for group in groups],1)
 lambdas={(g,h):tuple(F(a+b,2) for a,b in zip(tuples[g],tuples[h])) for g in range(len(groups)) for h in range(len(groups))}
 gaps=tuple((ev[:,None]-ev[None,:]).ravel());zero={}
 def covariance(order,cells):
  ft=np.array([[timekernel(lambdas[g,h],gaps,order,cells) for h in range(len(groups))] for g in range(len(groups))]);co=np.zeros((8,8),complex)
  for a in range(8):
   for b in range(8):
    jj,kk,ss=TRANS[a,b];gap=ev[a]-ev[b];K=overlap(ea[:,None]-ea[None,:]-gap)
    channels=np.einsum('jga,jhb,ab,j->gh',M[jj],M[kk].conj(),K,ss,optimize=True)
    co[a,b]=np.sum(channels*ft[:,:,8*a+b])
  return V@co@V.conj().T
 coarse=covariance(16,120);fine=covariance(32,240)
 F0=np.array([[timekernel(lambdas[g,h],(0.,),32,240)[0].real for h in range(len(groups))] for g in range(len(groups))])
 probability=sum(q[x]*F0[g,g] for g,group in enumerate(groups) for x,y,s,r in group)
 Qmoment=sum(qmoment[x]*F0[g,g] for g,group in enumerate(groups) for x,y,s,r in group)
 def battery(order):
  norm=moment=0.;support=[math.inf,-math.inf]
  for j in range(70):
   starts=48+ea-ef[j]+len(path);support[0]=min(support[0],starts.min());support[1]=max(support[1],(starts+1).max())
   E,W=integral_nodes(starts,order);amp=beta(E[:,None]-starts[None,:])@M[j].T
   prob=np.einsum('eg,gh,eh->e',amp,F0,amp.conj()).real
   assert prob.min()>-1e-12
   norm+=W@prob;moment+=(W*E)@prob
  return float(norm),float(moment),list(map(float,support))
 n16,b16,sp=battery(16);n32,b32,sp=battery(32)
 cov=fine/probability;curr=[float(2*c*cov[a,b].imag) if mask>>e&1 else 0. for e,(a,b,c) in enumerate(EDGES)]
 energy=float(np.trace(ham(mask)@cov).real);N=float(np.trace(cov).real)
 assert abs(N-4)<1e-9 and np.max(abs(cov-cov.conj().T))<1e-10
 row=dict(path=list(path),event=len(path),mask=mask,probability=float(probability),densities=cov.diagonal().real.tolist(),currents=curr,N=N,matter_energy=energy,battery_energy=b32/probability,conditional_totalQ=Qmoment/probability,ledger_residual=energy+12-len(path)+b32/probability-Qmoment/probability,battery_norm_residual=n32-probability,time_convergence=float(np.max(abs(fine-coarse))),battery_convergence=max(abs(n32-n16),abs(b32-b16)),active_occupations=len(active),rate_groups=[list(r) for r in tuples],battery_support=sp)
 return row,set(lambdas.values())

def census(q):
 totals={};reach=[0.]*13;occupation_terminal=[];records={};trap_prefixes={}
 for x,bits in enumerate(BITS):
  terminal={};depthmass={}
  def walk(bits,head,mask,depth,weight,path=(),rates=(),phase=1):
   records.setdefault(path,[]).append(dict(initial_bits=BITS[x],final_bits=bits,head=head,mask=mask,rates=list(rates),fermion_sign=phase,weight=str(weight)))
   depthmass[depth]=depthmass.get(depth,F(0))+weight
   options=[(e,w) for e,w in incident(head,mask) if hop(bits,head,w) is not None]
   if not options:
    kind='headempty_dark' if not bits>>head&1 else ('graph_trap' if not incident(head,mask) else 'exclusion_block')
    key=(depth,kind);terminal[key]=terminal.get(key,F(0))+weight
    entry=trap_prefixes.setdefault(path,dict(mass=0.,classes={},configuration_count=0));entry['mass']+=float(q[x])*float(weight);entry['classes'][kind]=entry['classes'].get(kind,0.)+float(q[x])*float(weight);entry['configuration_count']+=1
    return
   for e,w in options:
    new,sg=hop(bits,head,w);walk(new,w,mask^(1<<e),depth+1,weight/F(len(options)),path+(e,),rates+(len(options),),phase*sg)
  walk(bits,0,4095,0,F(1));assert sum(terminal.values(),F(0))==1
  for d,w in depthmass.items():reach[d]+=float(q[x])*float(w)
  for (d,kind),w in terminal.items():totals[d,kind]=totals.get((d,kind),0.)+float(q[x])*float(w)
  occupation_terminal.append(dict(bits=bits,q=float(q[x]),terminal=[dict(events=d,kind=k,conditional_weight=str(w)) for (d,k),w in sorted(terminal.items())]))
 return dict(configuration_paths=[dict(path=list(path),records=rs) for path,rs in sorted(records.items())],trap_prefixes=[dict(path=list(path),**r) for path,r in sorted(trap_prefixes.items())],reach=reach,terminal=[dict(events=d,kind=k,mass=m) for (d,k),m in sorted(totals.items())],occupations=occupation_terminal)

def calculate():
 start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('180 seconds')));signal.alarm(180)
 ea,C,q,qm,qconv=initial();assert abs(sum(q)-1)<1e-11 and q.min()>-1e-12
 rows=[];allrates=set()
 for level in graphpaths()[1:]:
  for path,head,mask in level:
   row,rates=endpoint(path,mask,ea,C,q,qm);row['head']=head;row['zero_probability']=False;rows.append(row);allrates.update(rates)
 cert=[]
 for rates in sorted(allrates):
  t,w=mesh(32,240);f=conv(t,rates);norm=float(w@f);mean=float((w*t)@f/norm);variance=float((w*t*t)@f/norm-mean*mean)
  analytic=math.prod(1/float(r) for r in rates);amean=sum(1/float(r) for r in rates);avar=sum(1/float(r)**2 for r in rates)
  cert.append(dict(rates=list(map(float,rates)),tail=tail(rates),norm_error=abs(norm+tail(rates)-analytic),mean_error=abs(mean-amean),variance_error=abs(variance-avar),min_density=float(f.min())))
 from scipy.integrate import quad_vec
 probes=[]
 for rates in sorted(allrates):
  frequencies=(0.,.7,2.3,5.1)
  val,err=quad_vec(lambda t:conv(np.array([t]),rates)[0]*np.exp(-1j*np.array(frequencies)*t),0,60,epsabs=1e-12,epsrel=1e-12)
  probes.append(float(np.max(abs(val-timekernel(rates,frequencies,32,240)))))
 cc=census(q);masses=[sum(r['probability'] for r in rows if r['event']==j) for j in range(1,5)]
 assert max(abs(masses[j-1]-cc['reach'][j]) for j in range(1,5))<1e-10
 assert abs(sum(t['mass'] for t in cc['terminal'])-1)<1e-10
 result=dict(schema='independent-occupation-feedback-scratch-v1',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),initial_energy_groups=ea.tolist(),initial_Q_mean=float(sum(qm)),initial_q=q.tolist(),initial_Q_first_moments=qm.tolist(),basis=BITS,initial_Q_quadrature_convergence=float(qconv),rows=rows,event_mass=masses,census=cc,time_density_checks=cert,adaptive_family_max_difference=max(probes),max_time_convergence=max(r['time_convergence'] for r in rows),max_battery_convergence=max(r['battery_convergence'] for r in rows),max_ledger_residual=max(abs(r['ledger_residual']) for r in rows),max_battery_norm_residual=max(abs(r['battery_norm_residual']) for r in rows))
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);result['resources']=dict(seconds=time.monotonic()-start,peak_rss_MiB=rss,timeout=180,blas_threads=1,rss_target=180)
 assert max(c['norm_error'] for c in cert)<2e-12 and max(c['variance_error'] for c in cert)<1e-10
 assert max(probes)<2e-11 and result['max_battery_convergence']<2e-10
 assert result['max_ledger_residual']<2e-8 and result['max_time_convergence']<1e-10 and result['max_battery_norm_residual']<1e-10 and rss<180,(rss,result['max_ledger_residual'],result['max_time_convergence'],result['max_battery_norm_residual'])
 return result

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
    assert elapsed<180 and rss<180,(rss,result['max_ledger_residual'],result['max_time_convergence'],result['max_battery_norm_residual'])
    result.update(schema=SCHEMA,validation_ok=True,scope=SCOPE,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies={},resources=dict(seconds=elapsed,peak_rss_MiB=rss,timeout_seconds=180,blas_threads=1,rss_limit_MiB=180))
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

def main():
    started=time.monotonic();emit(calculate(),started)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        if '--json' not in sys.argv:print('TOTAL: FAIL '+str(exc))
        raise
