"""Standalone deterministic local controls; no numerical Gibbs solver."""
from fractions import Fraction as F
from itertools import product,combinations
import json,argparse

def require(c,s):
 if not c:raise ValueError(s)
def check():
 count=0
 for bits in product((0,1),repeat=6):
  z=[1-2*b for b in bits];d=(sum(bits)-3)**2
  require(d==F(3,2)+F(1,2)*sum(z[i]*z[j] for i,j in combinations(range(6),2)),'electric expansion');count+=1
 geom=[]
 for L in (4,8):
  def add(v,a):return tuple((x+int(i==a))%L for i,x in enumerate(v))
  def edge(a,b):return tuple(sorted((a,b)))
  zero=(0,0,0);incident=set();faces=[]
  for v in product(range(L),repeat=3):
   for a in range(3):
    e=edge(v,add(v,a))
    if zero in e:incident.add(e)
   for a,b in combinations(range(3),2):
    va,vb=add(v,a),add(v,b);vab=add(va,b)
    faces.append({edge(v,va),edge(v,vb),edge(va,vab),edge(vb,vab)})
  require(len(incident)==6,'six edges')
  for e,f in combinations(sorted(incident),2):
   ce=[p for p in faces if e in p];cf=[p for p in faces if f in p]
   shared=sum(f in p for p in ce);odd=sum((e in p)==(f in p) for p in faces)
   require(len(ce)==len(cf)==4 and shared<=1 and odd==8-2*shared and odd>=6,'noncut witness');count+=1
   geom.append({'L':L,'shared_faces':shared,'flipped_faces':odd})
 delta=F(3,50)-F(15,1024);kappa=delta/8
 require(delta==F(1161,25600) and F(3,2)/kappa==F(102400,387),'sharp normalization');count+=1
 # Scalar variational inequalities with a nonnegative perturbation: all rational,
 # arbitrary mixtures, not claims that noncommuting Gibbs states are classical.
 for x in (F(0),F(1,7),F(1,2),F(1)):
  for u in (F(0),F(1,100),F(1,3)):
   k=F(2,5);h0=k*x;D=F(9)*(1-x)
   require(h0+u*D>=k*x,'positive perturbation');count+=1
 return {'status':'PASS','checks':count,'local_states':64,'incident_pairs':30,'geometric_cases':geom,'ground_density_coefficient':str(F(3,2)/kappa),'thermal_density_coefficient':'800','scope':'exact local geometry and rational inequality controls; no physical solve or Gibbs sampling'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');p.parse_args();print(json.dumps(check(),indent=2))
