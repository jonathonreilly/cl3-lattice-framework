#!/usr/bin/env python3
"""Preregistered native noncommensurate positive-cell ladder witness."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.linalg import eigh,expm
import scipy.sparse as sp
from numpy.polynomial.legendre import leggauss
import time,signal,resource,sys,json,hashlib,argparse
from pathlib import Path
import native_edge_record_autonomous_head_native_ladder_check_2026_09_07 as n
AUDIT_INPUT_PATHS = ('scripts/native_edge_record_autonomous_head_native_ladder_check_2026_09_07.py',)
AUDIT_TIMEOUT_SEC = 180
RSS_LIMIT_MIB = 180
DELTA=.25;M=48;CAP=12.;BLOW=4.;WIDTH=1.;ALPHA=np.sqrt(2)/3
EB=(np.arange(M)+.5)*DELTA;PATH=(0,1,2);DWELLS=(.2,.3,.4)
checks=0;worst=0.;original_defect=0.;rounding_error=0.
def check(a,b,label,tol=2e-9):
 global checks,worst
 error=float(np.max(abs(np.asarray(a)-np.asarray(b)),initial=0))
 if not np.isfinite(error) or error>tol:raise AssertionError(label+': '+str(error))
 checks+=1;worst=max(worst,error)
def sector(records):
 q,_,live=n.sector(records)
 h=sum((n.HOPS[e]*(1 if e==0 else ALPHA) for e in live if e in (0,2)),np.zeros((16,16),complex))
 return q,q.conj().T@h@q+len(live)*np.eye(q.shape[1]),live

def groups(h,rounded=False):
 a,V=eigh(h)
 labels=np.floor(a/DELTA+.5).astype(int) if rounded else np.round(a,11)
 return [(int(label) if rounded else float(a[labels==label].mean()),V[:,labels==label]@V[:,labels==label].conj().T) for label in np.unique(labels)]

def rounded(h):
 global rounding_error
 result=sum((DELTA*k*P for k,P in groups(h,True)),np.zeros_like(h))
 rounding_error=max(rounding_error,float(np.linalg.norm(h-result,2)))
 check(h@result,result@h,'original free A commutes spectral rounding')
 return result

def total(h):return sp.kron(sp.csr_matrix(h),sp.eye(M),format='csr')+sp.kron(sp.eye(len(h)),sp.diags(EB,dtype=float),format='csr')

def lift(h,g,K,extra_shift=0):
 out=np.zeros((len(g),M,len(h),M),complex)
 for a,Pa in groups(h,True):
  for b,Pb in groups(g,True):
   block=Pb@K@Pa;shift=a-b+extra_shift
   for j in range(M):
    if 0<=j+shift<M:out[:,j+shift,:,j]+=block
 return out.reshape(len(g)*M,len(h)*M)

def intertwine(left,L,right,label):
 for col in range(0,L.shape[1],32):
  sl=slice(col,col+32);check(left@L[:,sl],L@right[:,sl],label)

def complete(records,e):
 global original_defect
 q,h,live=sector(records);hr=rounded(h);Ls=[];targets=[];bare_effect=np.zeros_like(h)
 for z in (1,-1):
  rec=dict(records);rec[e]=z;r,g,_=sector(rec);gr=rounded(g)
  K=r.conj().T@((n.I+z*n.Z[e])/2)@q
  bare_effect+=K.conj().T@K
  check(r.conj().T@n.N@r@K,K@q.conj().T@n.N@q,'native N')
  for old,value in records.items():check(n.Z[old]@r@K,value*r@K,'native old Record')
  L=lift(h,g,K)
  intertwine(total(gr),L,total(hr),'literal rounded energy intertwining')
  for col in range(0,L.shape[1],32):
   sl=slice(col,col+32);original_defect=max(original_defect,float(np.max(abs(total(g)@L[:,sl]-L@total(h)[:,sl]))))
  Ls.append(L);targets.append((rec,r,g,gr,K))
 check(bare_effect,np.eye(len(h)),'native full sign instrument')
 effect=sum(L.conj().T@L for L in Ls);defect=np.eye(len(effect))-effect
 vals,V=eigh((defect+defect.conj().T)/2)
 if vals.min() < -1e-9:raise AssertionError('capped column not contraction')
 F=(V*np.sqrt(np.where(vals>1e-10,vals,0)))@V.conj().T
 check(effect+F.conj().T@F,np.eye(len(effect)),'ONE refusal completeness')
 intertwine(total(hr),F,total(hr),'refusal preserves rounded energy')
 return h,hr,Ls,F,targets

def evolve(h,state,t):
 # ORIGINAL system free A, rounded battery center energy.
 shape=state.shape
 matrix=state.reshape(len(h),M,-1)
 out=np.einsum('ab,bjk,j->ajk',expm(-1j*h*t),matrix,np.exp(-1j*EB*t))
 return out.reshape(shape)

def distribution(h,vec):
 data={};mat=vec.reshape(len(h),M,-1)
 for k,P in groups(h,True):
  prob=np.sum(abs(np.einsum('ab,bjk->ajk',P,mat))**2,axis=(0,2))
  for j,p in enumerate(prob):data[k+j]=data.get(k+j,0)+float(p)
 return data

def sum_distribution(rows):
 result={}
 for row in rows:
  for e,p in distribution(row['h'],row['vec']).items():result[e]=result.get(e,0)+p
 return result

def dist_check(a,b,label):
 check([a.get(k,0) for k in sorted(a.keys()|b.keys())],[b.get(k,0) for k in sorted(a.keys()|b.keys())],label)

def moments(rows):
 prob=energy=battery=0.
 for r in rows:
  v=r['vec'];prob+=float(np.vdot(v,v).real)
  energy+=float(np.vdot(v,total(r['h'])@v).real)
  mat=v.reshape(len(r['h']),M,-1);battery+=float(np.einsum('ajk,j,ajk->',mat.conj(),EB,mat).real)
 return dict(probability=prob,total_original=energy,battery=battery)

def main():
 global checks,worst,original_defect,rounding_error
 signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic()
 q0,h0,_=sector({});a,V=eigh(h0);psi=V[:,0]
 occupations=[(n.I-B)/2 for B in n.B]
 phase=.37*(occupations[0]-occupations[1])+.23*(occupations[2]-occupations[3])
 psi=q0.conj().T@(np.exp(-1j*np.diag(phase))*(q0@psi));psi/=np.linalg.norm(psi)
 check(q0.conj().T@n.N@q0@psi,2*psi,'prepared native N2')
 beta=np.zeros(M)
 for j in range(M):
  lo=max(j*DELTA,BLOW);hi=min((j+1)*DELTA,BLOW+WIDTH)
  if hi>lo:beta[j]=np.sqrt(2)/(np.sqrt(DELTA)*np.pi)*(np.cos(np.pi*(lo-BLOW))-np.cos(np.pi*(hi-BLOW)))
 projection_norm=float(np.linalg.norm(beta));prep_distance=2*np.sqrt(max(0,1-projection_norm**2))
 if prep_distance>2*DELTA/WIDTH+1e-12:raise AssertionError('cell Poincare bound')
 beta/=projection_norm;initial=np.kron(psi,beta)
 initial_rows=[dict(records={},h=h0,vec=initial,K=np.eye(len(h0)),head=0)]
 initial_dist=sum_distribution(initial_rows);initial_mom=moments(initial_rows)
 accepted=initial_rows;refused=[];prefixes=[];saved_first=None
 for step,(e,dwell) in enumerate(zip(PATH,DWELLS),1):
  for r in refused:r['vec']=evolve(r['h'],r['vec'],dwell)
  following=[]
  for r in accepted:
   h,hr,Ls,F,targets=complete(r['records'],e)
   assert r['head'] in n.EDGES[e]
   v=evolve(h,r['vec'],dwell)
   refused.append(dict(records=r['records'],h=h,vec=F@v))
   for L,(rec,q,g,gr,K) in zip(Ls,targets):
    following.append(dict(records=rec,h=g,vec=L@v,K=K@r['K'],head=next(x for x in n.EDGES[e] if x!=r['head'])))
  accepted=following
  dist_check(sum_distribution(accepted+refused),initial_dist,'retained prefix rounded energy distribution')
  mom=moments(accepted+refused);check(mom['probability'],1,'accepted plus absorbing refusal mass')
  check(sum(float(np.linalg.norm(r['vec'])**2) for r in refused),0,'prepared three-prefix refusal zero')
  prefixes.append(dict(step=step,**mom,original_drift=mom['total_original']-initial_mom['total_original']))
  if step==1:saved_first=[dict(r,vec=r['vec'].copy()) for r in accepted]
 if original_defect<1e-4:raise AssertionError('unrounded energy defect not detected')
 if abs(prefixes[-1]['original_drift'])<1e-4:raise AssertionError('unrounded mean drift absent')
 assert abs(prefixes[-1]['original_drift'])<=2*DELTA+1e-9

 # Direct continuous reference integration, every final Record sign retained.
 def continuous_comparison(order):
  x,w=leggauss(order);total_norm=total_energy=battery=distance=0.
  T=sum(DWELLS)
  for row in accepted:
   g=row['h'];K=row['K'];ags=groups(h0);bgs=groups(g)
   shifts=[a-b for a,_ in ags for b,_ in bgs]
   knots=np.unique(np.r_[np.arange(M+1)*DELTA,[BLOW+s for s in shifts],[BLOW+WIDTH+s for s in shifts]])
   lo=knots[:-1];hi=knots[1:]
   E=((lo+hi)[:,None]/2+(hi-lo)[:,None]/2*x).ravel();weights=((hi-lo)[:,None]/2*w).ravel()
   exact=np.zeros((len(g),len(E)),complex)
   for a,Pa in ags:
    for b,Pb in bgs:
     u=E-(a-b)-BLOW;packet=np.where((u>=0)&(u<=WIDTH),np.sqrt(2)*np.sin(np.pi*u),0)
     exact+=np.outer(Pb@K@Pa@psi,packet*np.exp(-1j*(b+E)*T))
   finite=np.zeros_like(exact);indices=np.floor(E/DELTA).astype(int);inside=(indices>=0)&(indices<M)
   finite[:,inside]=row['vec'].reshape(len(g),M)[:,indices[inside]]/np.sqrt(DELTA)
   pn=float(weights@np.sum(abs(exact)**2,axis=0));pf=float(np.linalg.norm(row['vec'])**2)
   overlap=np.einsum('aj,aj,j->',exact.conj(),finite,weights)
   distance+=np.sqrt(max(0,(pn+pf)**2-4*abs(overlap)**2))
   total_norm+=pn;battery+=float(weights@(E*np.sum(abs(exact)**2,axis=0)))
   total_energy+=float(weights@np.einsum('aj,aj->j',exact.conj(),g@exact).real)+float(weights@(E*np.sum(abs(exact)**2,axis=0)))
  return dict(norm=total_norm,total_original=total_energy,battery=battery,retained_trace_norm_error=distance)
 c16=continuous_comparison(16);c32=continuous_comparison(32)
 check(list(c16.values()),list(c32.values()),'direct continuous energy quadrature refinement')
 check(c32['norm'],1,'continuous full sign mass')
 check(c32['total_original'],initial_mom['total_original'],'continuous reference original energy conservation')

 # Unsafe boundary input, genuine completed refusal, still exact rounded energy.
 h,hr,Ls,F,targets=complete({},0);unsafe=np.kron(psi,np.eye(M)[:,-1])
 unsafe_rows=[dict(h=targets[i][2],vec=L@unsafe) for i,L in enumerate(Ls)]+[dict(h=h,vec=F@unsafe)]
 unsafe_refusal=float(np.linalg.norm(F@unsafe)**2)
 if unsafe_refusal<.01:raise AssertionError('unsafe refusal absent')
 dist_check(sum_distribution(unsafe_rows),distribution(h,unsafe),'unsafe rounded energy distribution with refusal')
 check(moments(unsafe_rows)['probability'],1,'unsafe complete mass')
 mutations={}
 def reject(label,a,b):
  try:check(a,b,label)
  except AssertionError as exc:mutations[label]=str(exc)
  else:raise AssertionError('undetected '+label)
 for label,shift in [('omit_fuel',-4),('double_fuel',4)]:
  rec,q,g,gr,K=targets[0];bad=lift(h,g,K,shift)
  reject(label,total(gr)@bad,bad@total(hr))
 effect=sum(L.conj().T@L for L in Ls)
 reject('separate_sign_refusals',effect+2*np.eye(len(effect))-effect,np.eye(len(effect)))
 reject('claim_original_energy_invariance',prefixes[-1]['original_drift'],0.)
 # Actual replacement channel after first event, retaining system marginal only.
 reset=[]
 for r in saved_first:
  mat=r['vec'].reshape(len(r['h']),M)
  columns=np.stack([np.kron(mat[:,j],beta) for j in range(M)],axis=1)
  reset.append(dict(r,vec=columns))
 for e,dwell in zip(PATH[1:],DWELLS[1:]):
  follow=[]
  for r in reset:
   h,hr,Ls,F,targets=complete(r['records'],e);v=evolve(h,r['vec'],dwell)
   check(F@v,0,'reset control also cap safe')
   for L,(rec,q,g,gr,K) in zip(Ls,targets):follow.append(dict(h=g,records=rec,vec=L@v))
  reset=follow
 reset_mom=moments(reset);reject('reset_retained_battery',reset_mom['total_original'],prefixes[-1]['total_original'])
 # Actual two-sector counterexample to unrestricted scalar Poisson uniformization.
 rate=np.diag([0.,1.]);rho=np.ones((2,2))/2;L=np.diag([0.,1.]);null=np.diag([1.,0.])
 true_derivative=L@rho@L-(rate@rho+rho@rate)/2
 false_derivative=L@rho@L+null@rho@null-rho
 reject('unrestricted_two_rate_uniformization',false_derivative,true_derivative)
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
 assert rss<180 and time.monotonic()-start<180,(rss,time.monotonic()-start)
 result=dict(checks=checks,worst=worst,parameters=dict(alpha=ALPHA,delta=DELTA,cap=CAP,packet=[4,5],levels=M,path=list(PATH),dwells=list(DWELLS),free='original A plus center EB'),rounding_operator_error=rounding_error,cell_projection_trace_norm_error=prep_distance,original_intertwining_defect=original_defect,prefixes=prefixes,continuous_reference=c32,unsafe_refusal=unsafe_refusal,reset_moments=reset_mom,uniformization_control=dict(true_derivative=true_derivative.tolist(),false_derivative=false_derivative.tolist()),mutations=mutations,seconds=time.monotonic()-start,rss_MiB=rss,scope='N2 native square, noncommensurate opposite dimers, retained positive-cell ladder; three-event complete instrument sequence, not a full finite-time path-summed GKSL computation',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 result['dependency_sha256']={AUDIT_INPUT_PATHS[0]:hashlib.sha256(Path(n.__file__).read_bytes()).hexdigest()}
 result['resources']={'timeout_seconds':180,'rss_limit_MiB':180,'blas_threads':1}
 result['distance_convention']='trace norm ||rho-sigma||_1; conventional trace distance is half these errors'
 result['N5_scope']='Fixed three-event complete Record sequence on a native N2 square, not all-path finite-time GKSL, not the cube, not a local physical implementation; one retained battery and one combined-sign refusal.'
 return result

if __name__ == '__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--json',action='store_true',help='Emit only the full JSON result')
 args=parser.parse_args();result=main()
 if args.json:print(json.dumps(result,indent=2,allow_nan=False))
 else:
  print('PASS: native noncommensurate finite-ladder complete Record witness')
  print(f"{result['checks']} checks; worst residual {result['worst']:.3g}; {result['seconds']:.3f} s; {result['rss_MiB']:.2f} MiB")
  print('N5 scope: '+result['N5_scope'])
  print('Parameters: '+json.dumps(result['parameters']))
  print('Original free A is retained; rounded total-energy distribution is invariant.')
  print(f"Original energy drift: {result['prefixes'][-1]['original_drift']:.12g}; unsafe refusal: {result['unsafe_refusal']:.12g}")
  print(f"Retained trace NORM error: {result['continuous_reference']['retained_trace_norm_error']:.12g}; conventional trace distance is half this value.")
  print('Detected mutations: '+', '.join(result['mutations']))
  print('Source SHA256: '+result['source_sha256'])
  print('Dependency SHA256: '+json.dumps(result['dependency_sha256']))
  print('per_element: both native Record signs, finite translated-battery matrix columns and one combined refusal are checked.')
  print('per_site: four native square vertices, old Records and directed head path01,12,23 are explicit.')
  print('per_mode: noncommensurate sector spectra, rounded total-energy indicators and direct continuous-energy quadrature are checked.')
  print('per_block: all three prescribed event prefixes retain the battery; unsafe completion and six adverse controls are executed.')
  print('lattice_wide: checked and not executed -- no all-path GKSL cube simulation, infinite-volume claim or physical bath realization.')
  print('RESOURCES '+json.dumps(result['resources'],sort_keys=True))
  print('TOTAL: PASS FAIL=0')
