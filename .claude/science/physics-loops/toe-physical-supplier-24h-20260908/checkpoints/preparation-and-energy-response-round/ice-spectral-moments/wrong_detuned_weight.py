import os,sys,time,signal,resource,json,hashlib
for k in['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
signal.alarm(180);start=time.monotonic()
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy import sparse
from scipy.linalg import eigh
p=Path(__file__).resolve().parent;data=np.load(p.parent/'ice-estimator-calibration/exact_data.npz');states=data['states'];faces=data['faces'];idx={int(x):i for i,x in enumerate(states)};n=len(states)
O=np.rint(data['O']*np.sqrt(32)).astype(np.int64);rows=[];cols=[];faceids=[]
for i,x in enumerate(states):
 for fi,f in enumerate(faces):
  bits=[(int(x)>>int(k))&1 for k in f]
  if bits[0]==bits[2] and bits[1]==bits[3] and bits[0]!=bits[1]:rows.append(i);cols.append(idx[int(x)^sum(1<<int(k)for k in f)]);faceids.append(fi)
A=sparse.coo_matrix((np.ones(len(rows),dtype=np.int64),(rows,cols)),shape=(n,n)).tocsr();deg=np.asarray(A.sum(1)).ravel();L=sparse.diags(deg,dtype=np.int64)-A
checks={}
def ck(k,b):checks[k]=bool(b);assert b,k
ck('component',n==864 and len(rows)==6912);ck('zero_mean',sum(O)==0);ck('integer_observable',max(abs(O/np.sqrt(32)-data['O']))<1e-14)
powers=[O]
for j in range(8):powers.append(L@powers[-1])
z=int(O@O);mom=[F(int(O@v),z)for v in powers];mu=float(mom[1]);variance=mom[2]-mom[1]**2
sq=(O[np.array(rows)]-O[np.array(cols)])**2;local=np.bincount(rows,weights=sq,minlength=n)/2
ck('dirichlet_form',F(int(sum(sq)),2*z)==mom[1]);ck('local_second_moment',F(int(powers[1]@powers[1]),z)==mom[2]);ck('positive_spectral_variance',variance>0)
# Proposed face is uniform among24, including nonflippable zero contributions.
Y=np.zeros((n,24));Y[rows,faceids]=12*sq
ck('conditioning_identity',np.array_equal(Y.mean(1),local))
var_all=F(int(np.sum(Y**2)),n*24)-F(int(np.sum(Y)),n*24)**2;var_local=F(int(np.sum(local**2)),n)-F(int(np.sum(local)),n)**2
# Centered ratio influence, common denominator O², exactly compare no independent-denominator fiction.
infl_all=Y-mu*O[:,None]**2;infl_local=local-mu*O**2
var_ratio_all=float(np.mean(infl_all**2)/(z/n)**2);var_ratio_local=float(np.mean(infl_local**2)/(z/n)**2)
ck('variance_reduction',var_local<var_all and var_ratio_local<var_ratio_all)
ritz=[]
for k in[1,2,3]:
 S=np.array([[float(mom[i+j])for j in range(k)]for i in range(k)]);B=np.array([[float(mom[i+j+1])for j in range(k)]for i in range(k)])
 vals,vec=eigh(B,S);weights=(S[0]@vec)**2
 held={str(j):float(weights@(vals**j)-float(mom[j]))for j in range(2*k,9)}
 ritz.append({'dimension':k,'nodes':vals.tolist(),'quadrature_weights':weights.tolist(),'held_out_moment_errors':held})
# Now reveal full finite spectral measure, held out of moment/Ritz construction.
e,U=eigh(L.toarray());amp=U.T@O;w=amp**2/z;support=np.flatnonzero(w>1e-10);gap=float(e[support[0]])
for k,row in enumerate(ritz):ck('Ritz_upper_'+str(k),row['nodes'][0]>=gap-1e-10)
ck('not_lower_bound',ritz[0]['nodes'][0]>gap+1e-3)
ck('spectral_moments',max(abs(sum(w*e**j)-float(mom[j]))/(1+abs(float(mom[j])))for j in range(9))<1e-10)
closure=np.linalg.matrix_rank(np.column_stack(powers[:4]).astype(float),tol=1e-8)
# Derive known full support envelope from graph degrees, not exact extreme eigenvalue.
cap=2*int(max(deg));center=mu;radius=.25;denbound=max(center**2,(cap-center)**2)-radius**2
outside_lower=max(0.,(float(variance)-radius**2)/denbound)
# Held-out detuned diagnostic: exact ground weighting is expressly imported here.
H=.95*np.diag(deg)-A.toarray();ed,Ud=eigh(H);psi=Ud[:,0];psi*=np.sign(sum(psi));prob=psi**2;delta=ed[0];v=(H-delta*np.eye(n))@(O*psi);ell=v/psi;Zd=sum(prob*O**2)
correct1=float(mom[1]);correct2=float(sum(prob*ell**2)/Zd);naive1=float(mom[1]);naive2=float(mom[2]);mixed1=float(sum(psi*O*ell)/sum(psi*O**2))
weighted_local=np.zeros(n)
for i,j,d in zip(rows,cols,sq):weighted_local[i]+=.5*psi[j]/psi[i]*d
ck('detuned_weighted_dirichlet',abs(sum(prob*weighted_local)/Zd-correct1)<1e-12)
ck('detuned_wrong_uniform_rejected',abs(naive1-correct1)>1e-5 and abs(naive2-correct2)>1e-5)
ck('detuned_mixed_not_pure',abs(mixed1-correct1)>1e-5)
maxmult=int(A.data.max());Ad=A.copy();Ad.data[:]=1;Ld=sparse.diags(np.asarray(Ad.sum(1)).ravel())-Ad
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);ck('resources',0<rss<384)
out={'checks':checks,'count':len(checks),'moments':[str(x)for x in mom],'spectral_variance':str(variance),'variance':{'single_face':str(var_all),'all_faces':str(var_local),'factor':float(var_all/var_local),'ratio_influence_single_face':var_ratio_all,'ratio_influence_all_faces':var_ratio_local,'ratio_influence_factor':var_ratio_all/var_ratio_local},'ritz':ritz,'krylov_rank_four_vectors':int(closure),'exact_supported_gap':gap,'lowest_level_weight':float(sum(w[abs(e-gap)<1e-9])),'full_component_gap':float(e[1]),'support_cap':cap,'outside_mean_plusminus_quarter_lowerbound':outside_lower,'outside_actual_mass':float(sum(w[abs(e-center)>.25])),'multiplicity_control':{'maximum':maxmult,'collapsed_changes_operator':bool((Ld-L).nnz)},'detuned':{'E0':float(delta),'mu1':correct1,'mu2':correct2,'RK_wrong_mu1':naive1,'RK_wrong_mu2':naive2,'mixed_wrong_mu1':mixed1},'seconds':time.monotonic()-start,'rss_mib':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2,allow_nan=False))
