from fractions import Fraction as F
from itertools import product
import json,pathlib,time
start=time.monotonic();G=[[F(3,4),F(1,4),F(0)],[F(1,4),F(1,2),F(1,4)],[F(0),F(1,4),F(5,4)]];b=list(map(sum,G));Q=[[x/b[i] for x in row] for i,row in enumerate(G)]
paths=[x for x in product(range(3),repeat=3) if G[x[0]][x[1]]*G[x[1]][x[2]]];weights=[G[x[0]][x[1]]*G[x[1]][x[2]] for x in paths];Z=sum(weights);pi=[w/Z for w in weights];index={x:i for i,x in enumerate(paths)};N=len(paths)
def matrix(lift=False,wrong=False):
 size=N*(2 if lift else 1);P=[[F(0) for _ in range(size)] for _ in range(size)]
 for i,x in enumerate(paths):
  for s in [0,1]:
   src=2*i+s if lift else i;factor=F(1) if lift else F(1,2)
   for z in range(3):
    y=x[1:]+(z,) if s==0 else (z,)+x[:-1];prob=Q[x[-1] if s==0 else x[0]][z]
    if not prob:continue
    den=x[0] if wrong and s==0 else x[-1] if wrong else x[1] if s==0 else x[-2]
    ratio=b[x[-1] if s==0 else x[0]]/b[den];acc=min(F(1),ratio);j=index[y]
    P[src][2*j+s if lift else j]+=factor*prob*acc
    P[src][2*i+1-s if lift else i]+=factor*prob*(1-acc)
 return P
out={}
for lift in [False,True]:
 target=[w/2 for w in pi for _ in range(2)] if lift else pi
 for wrong in [False,True]:
  P=matrix(lift,wrong);assert all(sum(row)==1 for row in P)
  residual=max(abs(sum(target[i]*P[i][j] for i in range(len(P)))-target[j]) for j in range(len(P)))
  if wrong:assert residual>0
  else:assert residual==0
  out[str((lift,wrong))]=str(residual)
# endpoint energy versus even-projector Rayleigh, exact rational arithmetic.
M=4;H=[[M*((1 if i==j else 0)-G[i][j]) for j in range(3)] for i in range(3)];psi=list(map(sum,G));norm=sum(z*z for z in psi);ray=sum(psi[i]*H[i][j]*psi[j] for i in range(3) for j in range(3))/norm
endpoint=sum(pi[k]*sum(H[x[0]]) for k,x in enumerate(paths));assert ray==endpoint
out.update(paths=N,endpoint_energy=str(endpoint),rayleigh=str(ray),seconds=time.monotonic()-start,scope='exact rational three-state balance falsifier, not native ice calibration')
pathlib.Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
