import json
import conditional as c
from check import build_fixtures,masses,near,legal
N=0
def need(v,msg):
 global N
 N+=1
 if not v:raise ValueError(msg)
g=c.Geometry(4);p=next(p for p in range(g.M) if legal(g,g.seed,p));q=next(q for q in range(g.M) if legal(g,g.seed,q) and c.strict_distant(g,p,q))
obj=c.Conditional(c.Trajectory(g,g.seed,[(.4,q)],1.,[]),p,.95)
need(obj.C==[[[1,0],[0,1]]],'native transported identity')
D=[obj.D[0],[[obj.D[1][1-i][1-j] for j in range(2)] for i in range(2)]]
C=[[[obj.C[0][i][1-j] for j in range(2)] for i in range(2)]]
need(C==[[[0,1],[1,0]]],'coordinate reversal gives swap')
a=masses(obj.D,obj.C);b=masses(D,C)
for ids,w in a.items():need(near(w,b[(ids[0],ids[1],1-ids[2],1-ids[3])]),'physical boundary probability unchanged')
changed=[]
for L in (2,4):
 for path,p in build_fixtures(c.Geometry(L)):
  original=c.Conditional(path,p,.95);wrong=c.Conditional(path,p,0.)
  aa=masses(original.D,original.C);bb=masses(wrong.D,wrong.C)
  if any(not near(v,bb.get(k,0)) for k,v in aa.items()):changed.append(dict(L=L,p=p,initial=path.initial,events=path.events))
need(bool(changed),'native diagonal-potential omission actually biases')
print(json.dumps(dict(checks=N,native_potential_counterexamples=changed,scope='deterministic coordinate/invariance supplement'),indent=2))
