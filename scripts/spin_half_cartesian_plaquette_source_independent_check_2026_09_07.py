#!/usr/bin/env python3
"""Independent Cartesian-source check, preserved from the fresh checker seat.

Original author: independent field-check agent, 2026-09-07, who read frozen
PR sources but neither the scout report nor its discriminator before deriving
and running this construction. Axis-major state order, exact Laurent trace,
and bordered sparse response solve differ from the primary runner.

Packaging by the field scout changes CLI/output handling and assertion
reporting only. Root arranges independent confirmation of the final files.
Imports no repository science code; no Monte Carlo production is performed.
"""
from collections import deque, Counter, defaultdict
from itertools import product, combinations
from pathlib import Path
import json
import argparse
import hashlib
import os
# Bound the small finite calculation before NumPy initializes its BLAS runtime.
for _thread_env in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_thread_env] = "1"

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh, eigs, spsolve

AUDIT_INPUT_PATHS = ('docs/SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 120

def input_identity():
    """Read and bind the premises used to interpret this conditional calculation."""
    root = Path(__file__).resolve().parents[1]
    return {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
            for p in AUDIT_INPUT_PATHS}

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--json', type=Path, help='Optional structured receipt path')
args = parser.parse_args()
bound_inputs = input_identity()
checks_passed = 0
checks_failed = 0

def check(condition, label):
 global checks_passed, checks_failed
 if condition:
  checks_passed += 1
 else:
  checks_failed += 1
  print('[FAIL]', label)

L=2
coords=list(product(range(L),repeat=3))
# Axis-major ordering is deliberately different from the frozen root-major code.
links=[(a,r) for a in range(3) for r in coords]
ix={e:i for i,e in enumerate(links)}
def shift(r,a):
 t=list(r);t[a]=(t[a]+1)%L;return tuple(t)
def eps(r): return (-1)**sum(r)
plaquettes=[]
for a,b in combinations(range(3),2):
 for r in coords:
  es=[(a,r),(b,shift(r,a)),(a,shift(r,b)),(b,r)]
  ids=tuple(ix[e] for e in es)
  plaquettes.append((a,b,r,ids,sum(1<<k for k in ids)))
def moves(x):
 for p,(a,b,r,ids,mask) in enumerate(plaquettes):
  ns=[(x>>k)&1 for k in ids]
  if ns[0]==ns[2] and ns[1]==ns[3] and ns[0]!=ns[1]:
   yield x^mask,p,2*ns[0]-1
start=sum((r[a]%2)<<k for k,(a,r) in enumerate(links))
seen={start};q=deque([start]);xs=[]
while q:
 x=q.popleft();xs.append(x)
 for y,p,s in moves(x):
  if y not in seen:seen.add(y);q.append(y)
xs.sort();lookup={x:k for k,x in enumerate(xs)};N=len(xs)
rows=[];cols=[];legacy=[];cartesian=[];degrees=[]
max_error=0;reverse_errors=0;gauss_errors=0;flux_errors=0
for i,x in enumerate(xs):
 for r in coords:
  inc=[]
  for a in range(3):inc += [ix[(a,r)],ix[(a,shift(r,a))]]
  gauss_errors += (sum((x>>k)&1 for k in inc)!=3)
 for a in range(3):
  flux=sum(eps(r)*(((x>>ix[(a,r)])&1)-.5) for r in coords if r[a]==0)
  flux_errors += (flux!=0)
 m=list(moves(x));degrees.append(len(m))
 for y,p,s in m:
  a,b,r,ids,_=plaquettes[p]
  delta=np.array([eps(links[k][1])*(((y>>k)&1)-((x>>k)&1)) for k in ids])
  expected=-eps(r)*s*np.array([1,1,-1,-1])
  max_error=max(max_error,float(np.max(abs(delta-expected))))
  rev=[ss for yy,pp,ss in moves(y) if yy==x and pp==p]
  reverse_errors += (rev != [-s])
  rows.append(i);cols.append(lookup[y])
  legacy.append(s if (a,b)==(0,1) else 0)
  cartesian.append(eps(r)*s if (a,b)==(0,1) else 0)
rows=np.array(rows);cols=np.array(cols);degrees=np.array(degrees)
phases={'occupation_sign':np.array(legacy),'cartesian_curl':np.array(cartesian)}
def H(V,theta,kind):
 data=-np.exp(1j*theta*phases[kind])
 return sparse.coo_matrix((data,(rows,cols)),shape=(N,N)).tocsr()+sparse.diags(V*degrees,dtype=float)
def e0(V,theta,kind):
 h=H(V,theta,kind)
 if abs(complex(theta).imag)<1e-15:
  val=eigsh(h,k=1,which='SA',tol=1e-12,v0=np.ones(N),return_eigenvectors=False)[0]
 else:
  val=eigs(h,k=1,which='SR',tol=1e-12,v0=np.ones(N),return_eigenvectors=False)[0]
 check(abs(complex(val).imag)<1e-9, 'abs(complex(val).imag)<1e-9')
 return float(np.real(val))
def curvature(V,kind):
 h=H(V,0,kind).real
 es,vs=eigsh(h,k=2,which='SA',tol=1e-13,v0=np.linspace(1,2,N))
 order=np.argsort(es);e=float(es[order[0]]);psi=vs[:,order[0]]
 p=phases[kind]
 h1=sparse.coo_matrix((-1j*p,(rows,cols)),shape=(N,N)).tocsr()
 h2=sparse.coo_matrix((p*p,(rows,cols)),shape=(N,N)).tocsr()
 rhs=h1@psi;projected=rhs-psi*np.vdot(psi,rhs)
 augmented=sparse.bmat([[h-e*sparse.eye(N),sparse.csr_matrix(psi[:,None])],
                        [sparse.csr_matrix(psi[None,:]),sparse.csr_matrix((1,1))]],format='csc')
 sol=spsolve(augmented,np.r_[projected,0])[:N]
 direct=float(np.real(np.vdot(psi,h2@psi)))
 relaxation=float(2*np.real(np.vdot(projected,sol)))
 return {'E0':e,'sampled_ritz_separation':float(es[order[1]]-e),'K':(direct-relaxation)/L**3,
         'direct_over_volume':direct/L**3,'relaxation_over_volume':relaxation/L**3,
         'ground_residual':float(np.linalg.norm(h@psi-e*psi)),
         'solve_residual':float(np.linalg.norm((h-e*sparse.eye(N))@sol-projected)),
         'FD':[{'theta':t,'K_real':2*(e0(V,t,kind)-e)/t**2/L**3,
                'K_imag':-2*(e0(V,1j*t,kind)-e)/t**2/L**3} for t in (.02,.01)]}
# Exact Laurent polynomial trace H(theta)^4 at V=1. Every coefficient integer.
def trace4_poly(kind):
 adj=[[] for _ in range(N)]
 for i,j,p in zip(rows,cols,phases[kind]):adj[int(i)].append((int(j),int(p),-1))
 for i,d in enumerate(degrees):adj[i].append((i,0,int(d)))
 total=Counter()
 for i in range(N):
  two=defaultdict(Counter)
  for j,p,c in adj[i]:
   for k,q,d in adj[j]:two[k][p+q]+=c*d
  for exps in two.values():
   for p,c in exps.items():
    for q,d in exps.items():total[p-q]+=c*d
 return {str(k):int(v) for k,v in sorted(total.items()) if v}
result={'independence':'No imports from frozen or author code; axis-major edge indexing; BFS on bits.',
        'N':N,'directed_moves':len(rows),'mean_degree':float(degrees.mean()),
        'min_degree':int(degrees.min()),'max_degree':int(degrees.max()),
        'electric_update_max_error':max_error,'reverse_move_errors':reverse_errors,
        'gauss_errors':int(gauss_errors),'flux_errors':int(flux_errors),
        'trace_H4_V1':{},'matrix_checks':{},'curvatures':{}}
for kind in phases:
 result['trace_H4_V1'][kind]=trace4_poly(kind)
 h=H(.95,.37,kind);him=H(.95,.37j,kind)
 result['matrix_checks'][kind]={'hermitian_residual':float(sparse.linalg.norm(h-h.conj().T)),
  'imaginary_transpose_residual':float(sparse.linalg.norm(him.T-H(.95,-.37j,kind))),
  'trace_H4_at_theta_0p37_V1':float((H(1,.37,kind)@H(1,.37,kind)).multiply((H(1,.37,kind)@H(1,.37,kind)).T).sum().real)}
 for V in (1.,.95,.90):
  result['curvatures'][f'{kind}_V{V:.2f}']=curvature(V,kind)
  print(kind,V,result['curvatures'][f'{kind}_V{V:.2f}'],flush=True)
# Boundary/orientation algebra checked independently at every root and both signs,
# without needing to enumerate all larger-volume configurations.
result['all_root_orientation_algebra']={}
for ll in (2,4,6,8,10,12,3):
 fail=0;checked=0
 for r in product(range(ll),repeat=3):
  for a,b in combinations(range(3),2):
   ra=list(r);ra[a]=(ra[a]+1)%ll
   rb=list(r);rb[b]=(rb[b]+1)%ll
   for s in (-1,1):
    dn=np.array([-s,s,-s,s]);er=np.array([eps(r),eps(ra),eps(rb),eps(r)])
    fail+=not np.array_equal(er*dn,-eps(r)*s*np.array([1,1,-1,-1]))
    checked+=1
 result['all_root_orientation_algebra'][str(ll)]={'checked':checked,'failures':fail}
# A full source-flux quantum admits a periodic link-phase construction modulo
# 2*pi. This checks the endpoint, separately from the infinitesimal curvature.
tquant=2*np.pi/L**2
link_a=np.zeros(len(links))
for k,(a,r) in enumerate(links):
 if a==1:link_a[k]=tquant*r[0]
 if a==0 and r[0]==L-1:link_a[k]=-tquant*L*r[1]
state_f=np.array([sum(link_a[k]*eps(r)*(((x>>k)&1)-.5)
                         for k,(a,r) in enumerate(links)) for x in xs])
d=sparse.diags(np.exp(1j*state_f))
result['quantized_uniform_source']={
 'theta':tquant,
 'matrix_rotation_residual':float(sparse.linalg.norm(
     H(.95,tquant,'cartesian_curl')-d@H(.95,0,'cartesian_curl')@d.conj().T)),
 'energy_difference':e0(.95,tquant,'cartesian_curl')-e0(.95,0,'cartesian_curl')}
check(N==864 and len(rows)==6912, 'N==864 and len(rows)==6912')
check(max_error==reverse_errors==gauss_errors==flux_errors==0, 'max_error==reverse_errors==gauss_errors==flux_errors==0')
check(all(v['failures']==0 for k,v in result['all_root_orientation_algebra'].items() if int(k)%2==0), "all(v['failures']==0 for k,v in result['all_root_orientation_algebra'].items() if int(k)%2==0)")
check(result['all_root_orientation_algebra']['3']['failures']>0, "result['all_root_orientation_algebra']['3']['failures']>0")
check(result['quantized_uniform_source']['matrix_rotation_residual']<1e-11, "result['quantized_uniform_source']['matrix_rotation_residual']<1e-11")
for kind in phases:
 check(result['matrix_checks'][kind]['hermitian_residual']==0, "result['matrix_checks'][kind]['hermitian_residual']==0")
 check(result['matrix_checks'][kind]['imaginary_transpose_residual']==0, "result['matrix_checks'][kind]['imaginary_transpose_residual']==0")
 for V in (1.,.95,.90):
  c=result['curvatures'][f'{kind}_V{V:.2f}']
  check(c['ground_residual']<1e-11 and c['solve_residual']<1e-11, "c['ground_residual']<1e-11 and c['solve_residual']<1e-11")
  for typ in ('K_real','K_imag'):
   errors=[abs(fd[typ]-c['K']) for fd in c['FD']]
   check(3.9<errors[0]/errors[1]<4.1, '3.9<errors[0]/errors[1]<4.1')
# Packaging check of the already-derived independent Laurent polynomial.
check(result['trace_H4_V1']['occupation_sign'] == {'0': 8975616},
      'exact legacy fourth-trace Laurent polynomial')
check(result['trace_H4_V1']['cartesian_curl'] == {'-4': 1216, '0': 8973184, '4': 1216},
      'exact Cartesian fourth-trace Laurent polynomial')
# This sparse two-Ritz-value separation is not certified as the first gap.
result['ritz_separation_scope'] = 'sampled pair only; no minimum-gap certification'
result['bound_inputs_sha256'] = bound_inputs
if input_identity() != bound_inputs:
 raise RuntimeError('declared input changed during calculation')
result['checks_passed'] = checks_passed
result['checks_failed'] = checks_failed
if args.json:
 args.json.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='curvatures'},indent=2))
print(f'TOTAL: PASS={checks_passed} FAIL={checks_failed}')
raise SystemExit(int(checks_failed != 0))
