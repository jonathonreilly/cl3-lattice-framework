import pathlib,json,time,signal,resource,sys,itertools
import numpy as np
from observables import OrderMenu
signal.alarm(180);start=time.monotonic();P=pathlib.Path(__file__).parent;checks=0
def req(c,m):
 global checks
 checks+=1
 if not c:raise RuntimeError(m)
def literal(menu,x):
 m=[];f=[]
 for b in menu.corners:
  mm=[];ff=[]
  for a in range(3):mm.append(sum((-1)**(sum(r)+sum(bi*ri for bi,ri in zip(b,r)))*(int(x[menu.index[r,a]])-.5) for r in menu.rs)/menu.N)
  for a,c in menu.planes:
   total=0
   for r in menu.rs:
    ra=list(r);rc=list(r);ra[a]=(ra[a]+1)%menu.L;rc[c]=(rc[c]+1)%menu.L
    z=[int(x[menu.index[r,a]]),int(x[menu.index[tuple(ra),c]]),int(x[menu.index[tuple(rc),a]]),int(x[menu.index[r,c]])]
    total+=(-1)**sum(bi*ri for bi,ri in zip(b,r))*int(z[0]==z[2] and z[1]==z[3] and z[0]!=z[1])
   ff.append(total/menu.N)
  m.append(mm);f.append(ff)
 return np.array(m),np.array(f)
def gauss(menu,x):
 q=[]
 for r in menu.rs:
  n=0
  for a in range(3):
   s=list(r);s[a]=(s[a]-1)%menu.L;n+=x[menu.index[r,a]]+x[menu.index[tuple(s),a]]
  q.append(int(n)-3)
 return q
rows=[]
for L in (2,4,6):
 menu=OrderMenu(L);x=np.array([r[a]%2 for r,a in menu.links],np.uint8);fixtures=[x.copy()]
 for j in range(len(menu.faces)):
  z=x[menu.faces[j]]
  if z[0]==z[2] and z[1]==z[3] and z[0]!=z[1]:x[menu.faces[j]]^=1
  if j in (0,3,11):fixtures.append(x.copy())
 for x in fixtures:
  req(not any(gauss(menu,x)),'ice fixtures');z=menu.measure(x);m,f=literal(menu,x);req(np.max(abs(z['electric']-m))<1e-14 and np.max(abs(z['flippability']-f))<1e-14,'literal normalization')
  req(np.max(abs(m))<=.5+1e-14 and np.max(abs(f))<=1+1e-14,'absolute bounds');req(menu.vector(x).shape==(145,) and np.all(np.isfinite(menu.vector(x))),'vector schema')
  conjugate=menu.measure(1-x);req(np.max(abs(conjugate['electric']+m))<1e-14 and np.max(abs(conjugate['flippability']-f))<1e-14,'charge conjugation')
  for s in itertools.product(range(2),repeat=3):
   y=np.array([x[menu.index[tuple((r[i]-s[i])%L for i in range(3)),a]] for r,a in menu.links],np.uint8);v=menu.measure(y)
   for k,b in enumerate(menu.corners):
    phase=(-1)**sum(bi*si for bi,si in zip(b,s));req(np.max(abs(v['electric'][k]-(-1)**sum(s)*phase*m[k]))<1e-14,'translation electric');req(np.max(abs(v['flippability'][k]-phase*f[k]))<1e-14,'translation face')
  # Cyclic coordinate permutation new=(old z,old x,old y).
  perm=(2,0,1);y=np.array([x[menu.index[tuple(r[perm.index(i)] for i in range(3)),perm[a]]] for r,a in menu.links],np.uint8);v=menu.measure(y)
  for k,b in enumerate(menu.corners):
   oldb=tuple(b[perm.index(i)] for i in range(3));kk=menu.corners.index(oldb)
   for a in range(3):req(abs(v['electric'][k,a]-m[kk,perm[a]])<1e-14,'rotation electric')
   for j,(a,c) in enumerate(menu.planes):req(abs(v['flippability'][k,j]-f[kk,menu.planes.index(tuple(sorted((perm[a],perm[c]))))])<1e-14,'rotation face')
  flux=[]
  for a in range(3):
   planes=[sum((-1)**sum(r)*(int(x[menu.index[r,a]])-.5) for r in menu.rs if r[a]==t) for t in range(L)];req(max(planes)==min(planes),'flux cut independence');req(abs(m[0,a]-planes[0]/L**2)<1e-14,'q0 normalization');flux.append(planes[0])
  rows.append(dict(L=L,flux=flux,anisotropy=z['plane_anisotropy'],max_electric=float(np.max(abs(m))),max_face=float(np.max(abs(f)))))
for bad in (np.zeros(24,float),np.full(24,2,dtype=int),np.zeros(23,dtype=int)):
 try:OrderMenu(2).measure(bad)
 except ValueError:pass
 else:raise RuntimeError('invalid carrier accepted')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(rss<384 and time.monotonic()-start<180,'resources');out=dict(predicates=checks,rows=rows,seconds=time.monotonic()-start,rss_mib=rss,scope='deterministic diagonal measurement checks, not sampled order');(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
