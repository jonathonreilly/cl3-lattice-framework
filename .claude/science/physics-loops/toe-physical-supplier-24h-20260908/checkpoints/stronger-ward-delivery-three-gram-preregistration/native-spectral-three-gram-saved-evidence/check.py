from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,json
P=Path('/private/tmp/toe-24h-probes-20260908/native-spectral-three-gram-saved-design');sys.path.insert(0,str(P));import gram,interval as I
nchecks=0
zero=(F(0),F(0))
def ca(a,b):return a[0]+b[0],a[1]+b[1]
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def cj(a):return a[0],-a[1]
def sc(q,a):return q*a[0],q*a[1]
def operator(u,w):return[((),(-u,F(0))),((0,1),(F(0),-w))]
for overlap in (0,1,2):
 c=F(2,7);G=[[(F(1),0),(0,-c),(0,-c)],[(0,c),(F(2),0),(F(overlap),0)],[(0,c),(F(overlap),0),(F(2),0)]]
 @lru_cache(None)
 def mean(word):
  if not word:return F(1),F(0)
  if len(word)%2:return zero
  z=zero
  for j in range(1,len(word)):z=ca(z,sc(1 if j%2 else -1,cm(G[word[0]][word[j]],mean(word[1:j]+word[j+1:]))))
  return z
 def inner(a,b):
  z=zero
  for wa,va in a:
   for wb,vb in b:z=ca(z,cm(cm(cj(va),vb),mean(tuple(reversed(wa))+wb)))
  return z
 for u,w,q in [(F(1),F(2,3),F(3,5)),(F(-2),F(1,7),F(-1,2))]:
  for v,z,t in [(F(3,2),F(-1,4),F(2)),(F(0),F(1),F(1,3))]:
   xc=[((),(-u,F(0))),((0,1),(F(0),-w))];xa=[((),(-v,F(0))),((0,2),(F(0),-z))]
   vc=[((1,),(F(0),2*q*u)),((0,),(4*q*w,F(0)))];va=[((2,),(F(0),2*t*v)),((0,),(4*t*z,F(0)))];gva=[((0,)+word,coef)for word,coef in va]
   exact=[inner(xc,xa)[0],inner(vc,va)[0],inner(xc,gva)[0]];got=gram.kernels(tuple(map(I.point,(u,w,q))),tuple(map(I.point,(v,z,t))),I.point(c),overlap)
   for x,y in zip(got,exact):assert x==(y,y);nchecks+=1
   if overlap==0:
    nominal=u*v+4*t*u*z+c*(u*z+w*v+t*(2*u*v+4*w*z));assert exact[0]-exact[2]==nominal;nchecks+=1
assert sum(6 if a==b else 1 if not(set(a)&set(b))else 3 for a in gram.LABELS for b in gram.LABELS)==540;nchecks+=1
stages=[];ans=gram.evaluate({'c':['0','0'],'nominal':['1','2'],'spectral_alpha_interval':['-100','100'],'E_upper':'1','F_upper':'10','coefficients':{}},lambda s,d:stages.append(s));assert ans['ordered_pairs']==0 and stages==['necessary_screen']and ans['status']=='ZERO_DUAL_POSITIVE_CERTIFICATE_EXCLUDED';nchecks+=1
for E,Fv in [(F(0),F(1)),(F(1),F(2)),(F(1),F(4))]:assert gram.lower(E,Fv)<=0;nchecks+=1
print(json.dumps({'status':'PASS','predicates':nchecks,'actual_saved_values':0,'full_Gram_calls':0,'scope':'independent exact3-Majorana Wick and source-sign identity; necessary-screen skips kernel acquisition'}))
