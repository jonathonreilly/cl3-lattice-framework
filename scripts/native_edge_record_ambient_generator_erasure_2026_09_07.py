#!/usr/bin/env python3
"""Independent native ambient/history-erasure matrix witness on a square carrier."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import time,json,resource,sys,signal,hashlib
import numpy as np
from scipy.linalg import eigh,expm
import scipy.sparse as sp
from pathlib import Path
AUDIT_INPUT_PATHS = ("scripts/native_edge_record_autonomous_head_native_ladder_check_2026_09_07.py",)
import native_edge_record_autonomous_head_native_ladder_check_2026_09_07 as n
signal.alarm(180)
start=time.monotonic();checks=0;worst=0.
I=n.I;D=n.CAP

def check(a,b,label,tol=3e-9):
 global checks,worst
 aa,bb=np.asarray(a),np.asarray(b)
 if aa.ndim==2 and bb.shape==aa.shape:
  error=0.
  for j in range(0,aa.shape[1],32):
   part=float(np.max(abs(aa[:,j:j+32]-bb[:,j:j+32]),initial=0))
   if not np.isfinite(part):raise AssertionError(label+': nonfinite column residual')
   error=max(error,part)
 else:error=float(np.max(abs(aa-bb),initial=0))
 if not np.isfinite(error) or error>tol:raise AssertionError(label+': '+str(error))
 checks+=1;worst=max(worst,error)

def H(live):
 return sum((n.HOPS[e] for e in live if e in (0,2)),np.zeros((16,16),complex))+len(live)*I

def total(h):return np.kron(h,np.eye(D))+np.kron(np.eye(len(h)),np.diag(np.arange(D)))
def sparse_total(h):return sp.kron(sp.csr_matrix(h),sp.eye(D),format="csr")+sp.kron(sp.eye(len(h)),sp.diags(np.arange(D),dtype=float),format="csr")

def spectral(h):
 a,V=eigh(h);check(a,np.rint(a),'commensurate ambient spectrum')
 return [(int(energy),V[:,abs(a-energy)<1e-9]@V[:,abs(a-energy)<1e-9].conj().T) for energy in np.unique(np.rint(a))]

_ambient_lift_workspace=np.zeros((16,D,16,D),complex)
def lift(h,g,B):
 # Independent grouped-projector assembly with literal battery index writes.
 assert len(g)==16 and len(h)==16
 out=_ambient_lift_workspace
 out.fill(0)
 for a,Pa in spectral(h):
  for b,Pb in spectral(g):
   block=Pb@B@Pa;shift=a-b
   for battery in range(D):
    if 0<=battery+shift<D:out[:,battery+shift,:,battery]+=block
 result=out.reshape(len(g)*D,len(h)*D)
 target_total=sparse_total(g);source_total=sparse_total(h)
 for column in range(0,result.shape[1],32):
  sl=slice(column,column+32)
  check(target_total@result[:,sl],result@source_total[:,sl],'actual ambient energy intertwining all-column block')
 return result

def Q(e,z):return (I+z*n.Z[e])/2

def embed(h,E):
 result=np.zeros((len(h)*D,len(h)),complex)
 for a,Pa in spectral(h):
  assert 0<=E-a<D
  result+=np.kron(Pa,np.eye(D)[:,E-a:E-a+1])
 return result

# Native directed identity checked on the entire edge-qubit Hilbert space.
for e,(u,v) in enumerate(n.EDGES):
 for source,target in ((u,v),(v,u)):
  nv=(I-n.B[source])/2;nw=(I-n.B[target])/2
  J=n.HOPS[e]@nv@(I-nw)
  other=(n.HOPS[e]+nw@n.HOPS[e]-n.HOPS[e]@nw)/2
  check(J,other,'native directed J independent formula')
  check(J.conj().T@J,nv@(I-nw),'ambient J effect')
  check(J@n.N,n.N@J,'ambient directed N')
  check(n.Z[e]@J,-J@n.Z[e],'new Record flips across directed hop')

# Exact sign-summed loss preserves source code; individual signs need not.
individual_leak=0.;summed_leak=0.;restriction_cases=0
for records,edge,feedback in (({},0,False),({},0,True),({0:1},1,False),({0:1},1,True)):
 qs,hs,live=n.sector(records);Us=np.kron(qs,np.eye(D))
 ha=H(live);ga=H([e for e in live if e!=edge])
 head=0 if not records else 1
 source_n=(I-n.B[head])/2
 dest=next(v for v in n.EDGES[edge] if v!=head)
 J=n.HOPS[edge]@source_n@((I+n.B[dest])/2) if feedback else I
 loss_us=np.zeros_like(Us)
 # Two differently prepared histories in copies of this same present sector.
 rng=np.random.default_rng(201)
 psi=rng.normal(size=Us.shape[1])+1j*rng.normal(size=Us.shape[1]);psi/=np.linalg.norm(psi)
 rho_code=np.outer(psi,psi.conj())
 ambient_psi=Us@psi
 recycle_difference=[];code_loss=np.zeros((len(psi),len(psi)),complex)
 for z in (1,-1):
  out=dict(records);out[edge]=z;qt,gt,_=n.sector(out);Ut=np.kron(qt,np.eye(D))
  ambient=lift(ha,ga,Q(edge,z)@J)
  ambient_sparse=sp.csr_matrix(ambient)
  K=qt.conj().T@Q(edge,z)@J@qs
  sector=n.lift(hs,gt,K)
  branch_error=0.
  for column in range(0,Us.shape[1],32):
   sl=slice(column,column+32)
   part=float(np.max(abs(ambient_sparse@Us[:,sl]-Ut@sector[:,sl])))
   if not np.isfinite(part):raise AssertionError('nonfinite branch column residual')
   branch_error=max(branch_error,part)
  check(branch_error,0.,'ambient branch equals erased history branch')
  effect_us=np.empty_like(Us)
  ambient_adjoint=ambient_sparse.conj().T
  for column in range(0,Us.shape[1],32):
   sl=slice(column,column+32)
   effect_us[:,sl]=ambient_adjoint@(ambient_sparse@Us[:,sl])
  del ambient_adjoint
  loss_us+=effect_us
  for column in range(0,Us.shape[1],32):
   sl=slice(column,column+32)
   individual_leak=max(individual_leak,float(np.max(abs(effect_us[:,sl]-Us@(Us.conj().T@effect_us[:,sl])))))
  code_loss+=sector.conj().T@sector
  check(ambient@ambient_psi,Ut@sector@psi,'recycling amplitude intertwines erasure')
  restriction_cases+=1
 leak=float(np.max(abs(loss_us-Us@(Us.conj().T@loss_us))));summed_leak=max(summed_leak,leak)
 check(loss_us,Us@code_loss,'capped sign-summed loss intertwines code embedding')
 check(sparse_total(ha)@Us,Us@total(hs),'ambient free term intertwines history embedding')
 restricted_loss=Us.conj().T@loss_us
 check(-(restricted_loss@rho_code+rho_code@restricted_loss)/2,-(code_loss@rho_code+rho_code@code_loss)/2,'anticommutator erasure equality')
 if not feedback:
  check(Us-loss_us,Us@(np.eye(len(psi))-code_loss),'one eligibility-refusal effect restriction')
 del ambient_sparse,Us,ambient_psi,rho_code,ambient,sector,Ut,code_loss,loss_us,effect_us,restricted_loss
assert individual_leak>.01

# Two actual square trails merge after four events, with fixed physical signs.
signs={0:1,1:-1,2:1,3:1};paths=((0,1,2,3),(3,2,1,0))
q0,h0,_=n.sector({});U0=np.kron(q0,np.eye(D))
# A native N2 initial occupation vector, with a superposition of total energies.
P=I.copy()
for v,occ in enumerate((0,1,1,0)):P=P@((I+(1-2*occ)*n.B[v])/2)
a,v=eigh(q0.conj().T@P@q0);chi=v[:,np.argmax(a)];check(a.max(),1,'native initial occupancy sector')
W19=embed(h0,19);W20=embed(h0,20)
safe=np.column_stack([W19,W20]);initial=(W19@chi+W20@chi)/np.sqrt(2)
check(np.linalg.norm(initial),1,'two-energy safe input normalization')
resultpaths=[];ambientpaths=[]
for path in paths:
 records={};head=0;sector_amplitudes=safe.copy();ambient_amplitudes=U0@safe;degrees=[]
 for edge in path:
  qs,hs,live=n.sector(records)
  degrees.append(sum(head in n.EDGES[e] for e in live))
  assert head in n.EDGES[edge]
  newrecords=dict(records);newrecords[edge]=signs[edge]
  qt,gt,_=n.sector(newrecords)
  K=qt.conj().T@Q(edge,signs[edge])@qs
  sector_amplitudes=n.lift(hs,gt,K)@sector_amplitudes
  ambient_amplitudes=lift(H(live),H([e for e in live if e!=edge]),Q(edge,signs[edge]))@ambient_amplitudes
  head=next(v for v in n.EDGES[edge] if v!=head);records=newrecords
 check(head,0,'head returns on merging trail')
 check(degrees,[2,1,1,1],'square trail rate sequence')
 Uf=np.kron(qt,np.eye(D))
 check(ambient_amplitudes,Uf@sector_amplitudes,'full merging history ambient equality')
 resultpaths.append(sector_amplitudes);ambientpaths.append(ambient_amplitudes)
check(resultpaths[0],resultpaths[1],'same-sign zero-dwell retained path columns coincide on safe domain')
check(ambientpaths[0],ambientpaths[1],'physical merging paths coincide')
del U0, W19, W20, safe, ambient_amplitudes, sector_amplitudes, ambientpaths
# Independent bare product plus FINAL full total-energy phase.
bare=I.copy()
for e in range(4):bare=Q(e,signs[e])@bare
Kall=qt.conj().T@bare@q0
expected=np.column_stack([embed(gt,19)@Kall,embed(gt,20)@Kall])
check(resultpaths[0],expected,'retained lift telescopes to physical commuting Q product')
column=np.r_[chi,chi]/np.sqrt(2)
y=resultpaths[0]@column
Hf=total(gt)
def free(t):
 a,V=eigh(Hf);return (V*np.exp(-1j*a*t))@V.conj().T
# Same total time, different first wait: states equal, timed norms differ.
times_a=np.array([.1,.2,.3,.4]);times_b=np.array([.4,.3,.2,.1]);rates=np.array([2,1,1,1])
Ta=float(times_a.sum());Tb=float(times_b.sum());check(Ta,Tb,'same accumulated dwell')
def actual_timed_path(path,times):
 records={};head=0;amplitude=initial.copy()
 for edge,dwell in zip(path,times):
  qs,hs,live=n.sector(records)
  degree=sum(head in n.EDGES[e] for e in live)
  unitary=np.kron(expm(-1j*hs*dwell),np.diag(np.exp(-1j*np.arange(D)*dwell)))
  amplitude=unitary@amplitude*np.exp(-degree*dwell/2)
  newrecords=dict(records);newrecords[edge]=signs[edge]
  qt,gt,_=n.sector(newrecords)
  K=qt.conj().T@Q(edge,signs[edge])@qs
  amplitude=n.lift(hs,gt,K)@amplitude
  head=next(v for v in n.EDGES[edge] if v!=head);records=newrecords
 return amplitude
state_a=actual_timed_path(paths[0],times_a)
state_b=actual_timed_path(paths[1],times_b)
check(state_a,free(Ta)@y*np.exp(-rates@times_a/2),'actual stagewise free-plus-jump path A retains final total phase')
check(state_b,free(Tb)@y*np.exp(-rates@times_b/2),'actual stagewise free-plus-jump path B retains final total phase')
check(state_a/np.linalg.norm(state_a),state_b/np.linalg.norm(state_b),'same-time normalized physical path states coincide')
ratio=float(np.linalg.norm(state_b)**2/np.linalg.norm(state_a)**2)
check(ratio,np.exp(-.3),'same total time does not fix timed path probability')
assert np.linalg.norm(state_a-state_b)>1e-3
# Preserve the physical final relative phase between Q19 and Q20.
u=y/np.linalg.norm(y);v=free(1.)@u
phase_distance=float(np.linalg.eigvalsh(np.outer(u,u.conj())-np.outer(v,v.conj())).__abs__().sum())
check(phase_distance,2*np.sin(.5),'different accumulated dwell retains actual relative total-energy phase')
# CPTP erasure: density alternatives add, not amplitudes.
physical_a=Uf@state_a;physical_b=Uf@state_b
# Same complete density-matrix Frobenius comparison, accumulated by columns.
# Avoid retaining three full ambient density matrices simultaneously.
coherent_error_squared=0.
physical_sum=physical_a+physical_b
for column in range(0,len(physical_a),32):
 sl=slice(column,column+32)
 difference=np.outer(physical_sum,physical_sum[sl].conj())
 difference-=np.outer(physical_a,physical_a[sl].conj())
 difference-=np.outer(physical_b,physical_b[sl].conj())
 coherent_error_squared+=float(np.vdot(difference,difference).real)
coherent_error=float(np.sqrt(coherent_error_squared))
del difference
assert coherent_error>.01
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert rss<180 and time.monotonic()-start<180, f'RSS={rss}'
result=dict(checks=checks,carrier_checks=n.checks,worst=max(worst,n.worst),branch_restriction_cases=restriction_cases,individual_loss_code_leak=individual_leak,sign_summed_loss_code_leak=summed_leak,merging_paths=[list(p) for p in paths],record_signs=signs,rate_tuple=rates.tolist(),safe_total_energies=[19,20],same_total_time=Ta,times_a=times_a.tolist(),times_b=times_b.tolist(),timed_probability_ratio=ratio,distinct_time_state_trace_norm=phase_distance,coherent_history_addition_error=coherent_error,seconds=time.monotonic()-start,rss_MiB=rss,scope='Actual native square with opposite dimers, fixed N2 merging paths; ambient block matrices vs separate history-code lifts. No full cube computation.',source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest())
result["dependencies"]={p:hashlib.sha256((Path(__file__).resolve().parents[1]/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
result["resources"]={"timeout_seconds":180,"rss_limit_MiB":180,"blas_threads":1}
if "--json" in sys.argv:
 print(json.dumps(result,indent=2,allow_nan=False))
else:
 print("PASS native ambient/history erasure: all-column energy lifts, sign-summed code loss and actual merging trajectories")
 print("RESULT",json.dumps(result,sort_keys=True,allow_nan=False))
 print("COUNTER_SCOPE On-demand imported carrier assertions only; the parent main/full census is not rerun.")
 print("per_element: checked all native directed edges and both sign branches in the declared capped restriction cases.")
 print("per_site: checked all four native occupations, head routing and old/new Record roles on the square.")
 print("per_mode: checked grouped energy projectors and every column of total-energy intertwiners, including safe Q19/Q20 coherence.")
 print("per_block: checked initial and bridge source codes, summed loss/refusal effects and two complete merging histories.")
 print("lattice_wide: checked and not executed -- finite witness does not prove local bath, infinite-lattice formation or renewal.")
 print("SOURCE_SHA256",result["source_sha256"])
 print("DEPENDENCIES",json.dumps(result["dependencies"],sort_keys=True))
 print("TOTAL: PASS FAIL=0")
