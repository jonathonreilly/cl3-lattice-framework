import os,sys,time,json,hashlib,pathlib
import numpy as np
from scipy.optimize import brentq
R=pathlib.Path('/Users/jonreilly/Projects/Physics-worktrees/review-backlog-schur-poles-7338-20260909')
sys.path.insert(0,str(R/'scripts'))
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as b48
import admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11 as b49
U=b48.build_reflection_union();D=np.asarray(U.directions);idx={tuple(d):i for i,d in enumerate(D)}
def Q(q):
 c=b49.centered_curvature_intertwiner(U,q)
 return b48.union_symbol(U,q)+b49.centered_curvature_intertwiner(U,-q).T@c/1024

def M(q):
 v=D@q/2
 return (np.exp(1j*v)*np.sinc(v/np.pi))[:,None]*b48.metric_coefficients(D)
def N(m): return np.linalg.qr(m,mode='complete')[0][:,10:]
n0=N(M(np.zeros(4)));out={}
for moving,e,k in [(True,(-2,0,1,0),9),(False,(-4,-4,1,0),10)]:
 a=np.array((.4,0,0,0));z=np.array(e)*2*np.pi/9
 def matrices(t):
  q=a*(1-t)+z*t;m=M(q);n=N(m) if moving else n0;op=Q(q);return q,m,n,op,n.conj().T@op@n
 def ev(t):return np.linalg.eigvalsh(matrices(t)[-1])[k]
 t=brentq(ev,0,1,xtol=1e-14);q,m,n,op,c=matrices(t);v,w=np.linalg.eigh(c);j=np.argmin(abs(v));mix=np.linalg.norm(w[:,j].conj()@n.conj().T@op@m);s=np.linalg.svd(op,compute_uv=False)
 out[str(moving)]={'t':t,'q':q.tolist(),'zero':float(v[j]),'mix':float(mix),'full_rank':int(np.sum(s>1e-9)),'ward':float(np.linalg.norm(op@b48.union_gauge_map(U,q)))}
 assert mix>1e-3 and np.sum(s>1e-9)==18 and abs(v[j])<1e-10
print('SECTIONS',json.dumps(out),flush=True)
obs=np.zeros(22);obs[idx[(0,1,0,0)]]=1;obs[idx[(0,0,1,0)]]=-1
for ns in [256,512]:
 cs=[];tt=np.arange(ns)*2*np.pi/ns
 for t in tt:
  q=np.array([np.pi/2,0,0,t]);op=-Q(q);g=b48.union_gauge_map(U,q);basis=np.linalg.qr(g,mode='complete')[0][:,4:];oo=basis.conj().T@obs;cs.append(float(np.real(oo.conj()@np.linalg.solve(basis.conj().T@op@basis,oo))))
 mm=np.array([np.mean(np.array(cs)*np.cos(n*tt)) for n in range(13)])
 h1=np.array([[mm[i+j+1] for j in range(2)] for i in range(2)]);h2=np.array([[mm[2*(i+j)] for j in range(3)] for i in range(3)])
 vals=(float(np.linalg.eigvalsh(h1)[0]),float(np.linalg.eigvalsh(h2)[0]));print('MOMENTS',ns,mm.tolist(),'HANKEL',vals,flush=True)
 assert vals[0]<-1e-13 and vals[1]<-1e-8
# Deliberately discard the hostile branches: positive single root control must be PSD.
mm=.581884812*.266171727**np.arange(13)
for step,order,shift in [(1,2,1),(2,3,0)]:
 h=np.array([[mm[step*(i+j+shift)] for j in range(order)] for i in range(order)])
 assert np.linalg.eigvalsh(h)[0]>-1e-14
print('CONTROL positive dominant root alone is PSD; direct quotient differs',flush=True)
inputs={}
for mod in list(sys.modules.values()):
 p=getattr(mod,'__file__',None)
 if p and str(p).startswith(str(R)) and str(p).endswith('.py'):
  inputs[str(pathlib.Path(p).relative_to(R))]=hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
print('ACTUAL_INPUTS',json.dumps(inputs,sort_keys=True),flush=True)
print('INDEPENDENT_CHECK_PASS',flush=True)
