"""Literal native path/leaf Gibbs-preparation probe; numerical support for the analytic proposal."""
from pathlib import Path
import hashlib,json,os
import numpy as np
from functools import reduce

m=4
vertices=[(j,0,0) for j in range(m)]+[(j,1,0) for j in range(m)]+[(0,0,1)]
edges=[(j,j+1) for j in range(m-1)]+[(j,m+j) for j in range(m)]+[(0,2*m)]
L=len(edges);dim=2**L;I=np.eye(dim,dtype=complex);X=np.array([[0,1],[1,0]],complex);Z=np.diag([1.,-1.]);i2=np.eye(2)
def site(op,k):return reduce(np.kron,[op if j==k else i2 for j in range(L)])
z=[site(Z,k) for k in range(L)];x=[site(X,k) for k in range(L)]
B=[reduce(np.matmul,[z[k] for k,e in enumerate(edges) if j in e],I) for j in range(2*m+1)]
n=[(I-b)/2 for b in B];T=[]
for k,(a,b) in enumerate(edges):
 A=x[k].copy()
 for u,v in ((a,b),(b,a)):
  for q,e in enumerate(edges):
   if u in e and q!=k:
    other=e[1] if e[0]==u else e[0]
    if other<v:A=A@z[q]
 T.append(.5j*A@(B[a]-B[b]))
checks={};residuals={}
def check(name,condition):
 checks[name]=bool(condition)
 if not condition:raise AssertionError(name)
def close(name,a,b,tol=2e-10):
 err=float(np.linalg.norm(a-b));residuals[name]=err;check(name,err<tol)
def pulse(t,c,s):return I+(c-1)*(t@t)-1j*s*t
for k,t in enumerate(T):
 close(f'T{k}_Hermitian',t,t.conj().T);close(f'T{k}_cubic',t@t@t,t)
close('even_global_parity',reduce(np.matmul,B,I),I)
check('physical_site_count_2m',L==2*m)
centers=[tuple(vertices[a][d]+vertices[b][d] for d in range(3)) for a,b in edges]
check('distinct_midpoints',len(set(centers))==L)
check('virtual_NN_edges',all(sum(abs(vertices[a][d]-vertices[b][d]) for d in range(3))==1 for a,b in edges))
rows=[]
for family,couplings in enumerate(((1.,2.,3.),(2.,1.,2.))):
 h=np.zeros((m,m))
 for j,a in enumerate(couplings):h[j,j+1]=h[j+1,j]=a
 eps,O=np.linalg.eigh(h)
 if np.linalg.det(O)<0:O[:,0]*=-1
 check(f'f{family}_eigenbasis_special_orthogonal',abs(np.linalg.det(O)-1)<1e-12)
 check(f'f{family}_nonzero_one_particle_spectrum',min(abs(eps))>0.1)
 H=sum(a*T[j] for j,a in enumerate(couplings))
 # Adjacent row elimination Q = G_k...G_1 O; reconstruct O = G_1^T...G_k^T Q.
 Q=O.copy();givens=[]
 for col in range(m-1):
  for j in range(m-1,col,-1):
   a,b=Q[j-1,col],Q[j,col];r=np.hypot(a,b)
   if r<1e-14:continue
   c,s=a/r,b/r;G=np.eye(m);G[j-1,j-1]=G[j,j]=c;G[j-1,j]=s;G[j,j-1]=-s
   Q=G@Q;givens.append((j-1,c,s,G))
 close(f'f{family}_QR_diagonal',Q,np.diag(np.diag(Q)))
 reconstructed=np.eye(m)
 V=I.copy();V_no_phase=I.copy()
 for step,(j,c,s,G) in enumerate(givens):
  reconstructed=reconstructed@G.T
  D=n[j]-n[j+1];R=pulse(D,np.sqrt(.5),np.sqrt(.5))
  # G inverse = exp(+i theta J), J=-R T R^dagger: actual three-pulse implementation.
  gate=R@pulse(T[j],c,s)@R.conj().T
  J=(T[j]@D-D@T[j])/(2j)
  close(f'f{family}_g{step}_phase_compilation',gate,pulse(J,c,-s))
  V=V@gate;V_no_phase=V_no_phase@pulse(T[j],c,s)
 signs=np.where(np.diag(Q)>=0,1.,-1.)
 reconstructed=reconstructed@np.diag(signs)
 negative_signs=np.flatnonzero(signs<0)
 check(f'f{family}_residual_signs_paired',len(negative_signs)%2==0)
 for a,b in zip(negative_signs[::2],negative_signs[1::2]):
  # exp(i*pi*(n_a-n_b)) is a product of adjacent difference phases.
  sign_gate=I.copy()
  for j in range(a,b):sign_gate=sign_gate@pulse(n[j]-n[j+1],1.,0.)
  close(f'f{family}_paired_sign_{a}_{b}',sign_gate,B[a]@B[b])
  V=V@sign_gate;V_no_phase=V_no_phase@sign_gate
 close(f'f{family}_one_particle_QR_reconstruction',reconstructed,O)
 close(f'f{family}_native_rotation_unitarity',V.conj().T@V,I)
 Hdiag=sum(eps[j]*n[j] for j in range(m))
 close(f'f{family}_actual_native_diagonalization',V@Hdiag@V.conj().T,H)
 ready_values=(eps<0).astype(int)
 P=I.copy()
 for j,ready in enumerate(ready_values):P=P@(n[m+j] if ready else I-n[m+j])
 ready_indices=np.flatnonzero(np.real(np.diag(P))>.5)
 Qready=I[:,ready_indices]
 check(f'f{family}_ready_rank_full_matter_fock',len(ready_indices)==2**m)
 # Initial physical state is a product with fixed leaf Z and every remaining qubit maximally mixed.
 for j,ready in enumerate(ready_values):close(f'f{family}_ready_leaf{j}',n[m+j]@Qready,ready*Qready)
 for beta in (0.,.7,2.):
  tag=f'f{family}_b{beta}'
  r=np.exp(-beta*abs(eps)/2);s=np.sqrt(np.maximum(0.,1-r*r))
  initial=V.conj().T@Qready
  branches={'':initial}
  for j in range(m):
   u=pulse(T[m-1+j],r[j],s[j]);nleaf=n[m+j];new={}
   close(f'{tag}_leaf{j}_unitarity',u.conj().T@u,I)
   for key,cols in branches.items():
    moved=u@cols
    new[key+'0']=(I-nleaf)@moved;new[key+'1']=nleaf@moved
   branches=new
  branches={key:V@cols for key,cols in branches.items()}
  effects=sum(cols.conj().T@cols for cols in branches.values())
  close(f'{tag}_all_outcomes_complete',effects,np.eye(2**m))
  key=''.join(str(q) for q in ready_values);K=branches[key]
  E,S=np.linalg.eigh(H);pref=np.exp(-beta*np.sum(abs(eps[eps<0]))/2)
  target=(S*(pref*np.exp(-beta*E/2)))@S.conj().T@Qready
  close(f'{tag}_actual_Kraus_vs_H_exponential',K,target)
  prob=float(np.real(np.trace(K.conj().T@K))/(2**m))
  predicted=float(np.prod((1+np.exp(-beta*abs(eps)))/2))
  check(f'{tag}_success_probability',abs(prob-predicted)<2e-12)
  check(f'{tag}_success_lower_bound',prob>=2**(-m)-2e-12)
  rho=K@K.conj().T/((2**m)*prob)
  expected_energy=float(np.sum(eps/(1+np.exp(beta*eps))))
  actual_energy=float(np.real(np.trace(H@rho)))
  check(f'{tag}_thermal_energy',abs(actual_energy-expected_energy)<2e-11)
  for j,ready in enumerate(ready_values):close(f'{tag}_Record{j}_preserved',n[m+j]@K,ready*K)
  if beta>0:
   wrong=V_no_phase.conj().T@Qready
   for j,ready in enumerate(ready_values):
    wrong=pulse(T[m-1+j],r[j],s[j])@wrong
    wrong=(n[m+j] if ready else I-n[m+j])@wrong
   wrong=V_no_phase@wrong
   check(f'{tag}_adverse_removed_phase_changes_Kraus',np.linalg.norm(wrong-target)>.01)
   wrongrho=wrong@wrong.conj().T/np.real(np.trace(wrong.conj().T@wrong))
   check(f'{tag}_adverse_real_controls_zero_energy',abs(np.trace(H@wrongrho))<2e-11)
  rows.append({'family':family,'couplings':couplings,'beta':beta,'eigenvalues':eps.tolist(),'givens_count':len(givens),'success_probability':prob,'predicted_success_probability':predicted,'thermal_energy':actual_energy,'all_branch_probabilities':{k:float(np.real(np.trace(c.conj().T@c))/(2**m)) for k,c in branches.items()}})
result={'status':'PASS','checks':checks,'TOTAL':{'PASS':len(checks),'FAIL':0},'residuals':residuals,'rows':rows,'physical_midpoints':centers,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Numerical physical256-dimensional m4 support; analytic general theorem separate; all preparation,phase,hopping,Born controls supplied.'}
Path(__file__).with_name('PATH_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
