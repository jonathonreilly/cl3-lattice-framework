import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import itertools,json,hashlib,time,resource,signal,sys
from fractions import Fraction as F
signal.alarm(180);start=time.monotonic();N=9
import sympy as s
checks=0
def ck(condition):
 global checks
 checks+=1
 if not condition:raise AssertionError("exact control assertion "+str(checks))
AUDIT_TIMEOUT_SEC=180
I='I'*N
def word(**kw):
 s=list(I)
 for k,v in kw.items():s[int(k)]=v
 return ''.join(s)
def w(i,a):return I[:i]+a+I[i+1:]
def mul(a,b):
 out=[];phase=1
 for x,y in zip(a,b):
  if x=='I':out.append(y)
  elif y=='I':out.append(x)
  elif x==y:out.append('I')
  else:
   out.append(({'X','Y','Z'}-{x,y}).pop());phase*=1j if (x,y) in [('X','Y'),('Y','Z'),('Z','X')] else -1j
 return ''.join(out),phase
def add(d,k,v):
 d[k]=d.get(k,F(0))+v
 if d[k]==0:del d[k]
def comm(a,b):
 # [a,b]/(2i), real coefficients for Hermitian Pauli inputs
 out={}
 for x,c in a.items():
  for y,d in b.items():
   z,p=mul(x,y)
   if p.imag:add(out,z,c*d*int(p.imag))
 return out
Zf=w(4,'Z');Yx=w(3,'Y');ZfYx=mul(Zf,Yx)[0]
Qa={I:F(1,2),Yx:F(1,2),Zf:F(-1,2),ZfYx:F(-1,2)}
K=dict(Qa)
for a,c in {I:F(2),w(5,'Z'):F(-1,2),w(6,'Z'):F(-1)}.items():add(K,a,c)
Zr={w(0,'Z'):F(1)};Nh={I:F(1),w(1,'Z'):F(-1,2),w(2,'Z'):F(-1,2)}
def solve(graph,strict=False):
 basis=[] if strict else [I]+[w(i,a) for i in range(N) for a in 'XYZ']
 basis += [mul(w(i,a),w(j,b))[0] for i,j in graph for a in 'XYZ' for b in 'XYZ']
 rows={}
 for col,x in enumerate(basis):
  for family,op in enumerate((K,Zr,Nh)):
   for key,v in comm({x:F(1)},op).items():rows.setdefault((family,key),{})[col]=v
 piv={}
 for row in rows.values():
  row=dict(row)
  while row:
   p=min(row)
   if p not in piv:
    v=row[p];piv[p]={k:x/v for k,x in row.items()};break
   v=row[p]
   for k,x in piv[p].items():add(row,k,-v*x)
 gens=[]
 for free in range(len(basis)):
  if free in piv:continue
  vec={free:F(1)}
  for p,row in sorted(piv.items(),reverse=True):
   v=-sum((x*vec.get(k,0) for k,x in row.items() if k!=p),F(0))
   if v:vec[p]=v
  g={basis[k]:v for k,v in vec.items()}
  ck(all(not comm(g,op) for op in (K,Zr,Nh)))
  gens.append(g)
 return {'columns':len(basis),'rank':len(piv),'nullity':len(gens),'all_commute_active_energy':all(not comm(g,Qa) for g in gens),'fuel_noncommuting_generators':sum(bool(comm(g,{Zf:F(1)})) for g in gens),'basis':[{k:str(v) for k,v in g.items()} for g in gens]}
complete=list(itertools.combinations(range(N),2));path=[(i,i+1) for i in range(N-1)]
results={name:solve(graph,strict) for name,graph,strict in [('complete_at_most_two',complete,False),('path_at_most_two',path,False),('complete_exactly_two',complete,True),('path_exactly_two',path,True)]}
for family in results.values():
 ck(family['all_commute_active_energy'])
Xf=w(4,'X');cancel={Xf:F(1),mul(Xf,Yx)[0]:F(-1)}
ck(not comm(cancel,K) and not comm(cancel,Zr) and not comm(cancel,Nh))
ck(comm({Xf:F(1)},K))
ck(not comm(K,K) and not comm({I:F(1)},K))
ck(comm({w(0,'X'):F(1)},Zr))
# Every path generator is exactly in the complete allowed span because its support is a subset and its constraints vanish.
for gen in results['path_at_most_two']['basis']:
 ck(all(sum(c!='I' for c in p)<=2 for p in gen))
 ck(all(not comm({k:F(v) for k,v in gen.items()},op) for op in (K,Zr,Nh)))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
ck(rss<180 and time.monotonic()-start<180)
for family in results.values():
 family['basis_sha256']=hashlib.sha256(json.dumps(family['basis'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
payload={'schema':'native-reduced-cell-two-site-exact-commutant-v1','qubit_order':['r','head_v','head_w','edge','fuel','battery_low','battery_high','label0','label1'],'coordinates':[[j,0,0] for j in range(9)],'scope':'Reduced square-boundary odd carrier; expanded workspace; supplied energy-preserving controls; complete graph versus fixed NN path; no full collision implementation','constraints':['[H,K]=0','[H,Z_r]=0','[H,N_head]=0'],'dependencies':{},'resources':{'timeout_seconds':180,'rss_limit_MiB':180,'blas_threads':1},'results':results,'controls':{'sum_cancellation_allowed':True,'fuel_flip_rejected':True,'old_record_flip_rejected':True,'identity_and_energy_allowed':True,'path_subset':True},'source_active_energy':2,'target_active_energy':0,'source_target_total_energy':'5/2','source_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest(),'seconds':time.monotonic()-start,'rss_MiB':rss}
def sadd(a,b):
 out=dict(a)
 for k,v in b.items():out[k]=s.simplify(out.get(k,0)+v)
 return {k:v for k,v in out.items() if v!=0}
def scale(a,c):return {k:s.simplify(v*c) for k,v in a.items() if v*c!=0}
def product(a,b):
 out={}
 for x,c in a.items():
  for y,e in b.items():
   z,p=mul(x,y);p=s.Integer(int(p.real))+s.I*int(p.imag)
   out=sadd(out,{z:c*e*p})
 return out
def minus(a,b):return sadd(a,scale(b,-1))
def adj(a):return {k:s.conjugate(v) for k,v in a.items()}
ident={I:s.Integer(1)}
Pi={I:s.Rational(1,2),w(3,'Y'):s.Rational(1,2)}
exchange=sadd({mul(w(4,'X'),w(6,'X'))[0]:s.Rational(1,2)},{mul(w(4,'Y'),w(6,'Y'))[0]:s.Rational(1,2)})
H1=product(Pi,exchange)
H2=product({I:s.Rational(1,2),w(4,'Z'):s.Rational(1,2)},{w(3,'X'):s.Integer(1)})
H3={mul(w(1,'X'),w(2,'X'))[0]:s.Rational(1,2),mul(w(1,'Y'),w(2,'Y'))[0]:s.Rational(1,2)}
H4={w(8,'X'):s.Integer(1)}
Hs=[H1,H2,H3,H4];angles=[s.pi/2,s.pi/4,s.pi/2,s.pi/2]
Us=[]
for h,theta in zip(Hs,angles):
 ck(not minus(product(h,h),adj(product(h,h))))
 ck(not minus(product(product(h,h),h),h))
 for op in (K,Zr,Nh):ck(not comm(h,op))
 u=sadd(sadd(ident,scale(product(h,h),s.cos(theta)-1)),scale(h,-s.I*s.sin(theta)))
 ck(not minus(product(adj(u),u),ident))
 Us.append(u)
ck(comm(exchange,K))
def apply(op,state):
 out={}
 for word,c in op.items():
  for bits,amp in state.items():
   dst=list(bits);phase=s.Integer(1)
   for j,p in enumerate(word):
    if p=='X':dst[j]=1-dst[j]
    elif p=='Y':phase*=s.I if dst[j]==0 else -s.I;dst[j]=1-dst[j]
    elif p=='Z':phase*=1 if dst[j]==0 else -1
   out=sadd(out,{tuple(dst):c*amp*phase})
 return out
def state(edge, fuel, head, battery, label,phase=1):
 bits=[0,int(head[0]),int(head[1]),0,fuel,int(battery[1]),int(battery[0]),int(label[0]),int(label[1])]
 if edge in ('Y+','Y-'):
  a=tuple(bits);bits[3]=1;return {a:phase/s.sqrt(2),tuple(bits):phase*s.I*(1 if edge=='Y+' else -1)/s.sqrt(2)}
 return {tuple(bits):phase}
x=state('Y+',1,'10','00','00');expect=[state('Y+',0,'10','10','00',-s.I),state('Z+',0,'10','10','00',-s.I),state('Z+',0,'01','10','00',-1),state('Z+',0,'01','10','01',s.I)]
rows=[]
for j,(u,h,y) in enumerate(zip(Us,Hs,expect)):
 x=apply(u,x);ck(not minus(x,y))
 ck(not minus(apply(K,x),scale(x,s.Rational(5,2))))
 rows.append({'pulse':j+1,'hamiltonian':{k:str(v) for k,v in h.items()},'angle':str(angles[j]),'max_pauli_weight':max(sum(c!='I' for c in k) for k in h),'state':{''.join(map(str,k)):str(v) for k,v in x.items()}})
ck(rows[0]['max_pauli_weight']==3)

# Separately preregistered fixed-input two-site sequence. It is NOT in the
# globally energy-commuting family, since its first control fails that test.
B1={mul(w(3,'Z'),w(6,'X'))[0]:s.Rational(1,2),mul(w(3,'X'),w(6,'Y'))[0]:s.Rational(-1,2)}
B2=product({w(4,'X'):s.Integer(1)},{I:s.Rational(1,2),w(3,'Y'):s.Rational(-1,2)})
Bs=[B1,B2,H2,H3,H4];betas=[s.pi/2,s.pi/2,-s.pi/4,s.pi/2,s.pi/2]
charged={I:s.Rational(1,2),w(4,'Z'):s.Rational(-1,2)}
ck(bool(comm(B1,K)))
ck(not comm(B1,charged))
# Exact full subspace identity, stronger than a sampled state expectation:
# [B1,K]P_q1=0 and [B1,P_q1]=0 keep the whole first orbit in energy5/2.
ck(not product(comm(B1,K),charged))
specific_expected=[state('Y-',1,'10','10','00',-s.I),state('Y-',0,'10','10','00',-1),state('Z+',0,'10','10','00',-1),state('Z+',0,'01','10','00',s.I),state('Z+',0,'01','10','01',1)]
specific_x=state('Y+',1,'10','00','00');specific_rows=[]
for j,(h,theta,y) in enumerate(zip(Bs,betas,specific_expected)):
 ck(not minus(product(product(h,h),h),h))
 ck(max(sum(c!='I' for c in k) for k in h)<=2)
 ck(not comm(h,Zr));ck(not comm(h,Nh))
 if j:ck(not comm(h,K))
 u=sadd(sadd(ident,scale(product(h,h),s.cos(theta)-1)),scale(h,-s.I*s.sin(theta)))
 ck(not minus(product(adj(u),u),ident))
 specific_x=apply(u,specific_x);ck(not minus(specific_x,y))
 ck(not minus(apply(K,specific_x),scale(specific_x,s.Rational(5,2))))
 specific_rows.append({'pulse':j+1,'hamiltonian':{k:str(v) for k,v in h.items()},'angle':str(theta),'max_pauli_weight':max(sum(c!='I' for c in k) for k in h),'state':{''.join(map(str,k)):str(v) for k,v in specific_x.items()}})
# Original combined-workspace discriminator, all source/refusal versus accepted strings.
source_controls=['11000','11011'] # f,hv,hw,l0,l1
accepted_controls=['00101','00110']
distances=[sum(a!=b for a,b in zip(x,y)) for x in source_controls for y in accepted_controls]
ck(distances==[4,4,4,4])
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
ck(0<rss<180);ck(0<=time.monotonic()-start<180)
payload['schema']='native-reduced-cell-control-v1'
payload['scope']='Exact conditional reduced native cell: two-site energy-preserving commutants and complete-graph three-site state transfer; no NN pulse implementation or full instrument'
payload['three_site']={'rows':rows,'final_phase':'I','uncontrolled_exchange_rejected':True}
payload['state_specific_two_site']={'rows':specific_rows,'final_phase':'1','first_global_energy_commutator_nonzero':True,'first_charged_subspace_commutator_zero':True,'scope':'Fixed input and complete graph only; first control does not globally conserve K; not a counterexample to globally commuting obstruction'}
payload['workspace_cross_hamming_distances']=distances
payload['exact_assertion_calls']=checks
payload['seconds']=time.monotonic()-start;payload['rss_MiB']=rss
payload['source_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
if '--json' in sys.argv:print(json.dumps(payload,indent=2,allow_nan=False))
else:
 print('PASS exact reduced native cell controls:',checks,'actual exact assertion calls')
 for name,row in results.items():print(name,'rank',row['rank'],'nullity',row['nullity'],'basis_sha256',row['basis_sha256'])
 print('THREE_SITE exact final phase I; pulse supports 3,2,2,1; modeled energy preserved')
 print('STATE_SPECIFIC_TWO_SITE exact final phase 1; first pulse conserves energy only on charged subspace')
 print('per_element: exact Pauli-sum commutators and pulse polynomials, not termwise conservation')
 print('per_site: nine explicitly placed reduced-cell qubits; old Record and head number preserved')
 print('per_mode: fixed active N=1 odd carrier with supplied parent boundary, no ambient square simulation')
 print('per_block: four complete/path support bases; four exact pulse states; four workspace cross distances')
 print('lattice_wide: checked and not executed -- no general lattice controllability or NN three-site synthesis')
 print('SOURCE_SHA256',payload['source_sha256'])
