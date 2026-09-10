# Tiny nonphysical root/worker arithmetic comparison; no loaders/Wick.
import pathlib,sys,importlib.util,json
from fractions import Fraction as F
B=pathlib.Path('/private/tmp/toe-24h-probes-20260908');sys.path.insert(0,str(B/'native-degree10-reduced-dual-design'));import dual as d
sp=importlib.util.spec_from_file_location('rs',B/'native-reduced-dual-root-review/schema.py');r=importlib.util.module_from_spec(sp);sp.loader.exec_module(r)
p=d.P;M={'A':[[p(3 if i==j else 1)for j in range(4)]for i in range(4)],'B':[[p(2),p(1)],[p(1),p(4)]],'correction':[p(-1),p(2),p(3)]};t,s,_=d.proposal(M);assert r.propose(M)==(t,s,False);n=1
for lam in d.SCALES:
 logs=[];d.certify(M,t,s,lam,lambda *x:logs.append(x));a,b,c=r.channel(M,t,s,lam);assert (a,b,c)==tuple(logs[0][1][x]for x in ['a2','b2','correction']);n+=1
for x in [F(0),F(1,3),F(7),F(1,2**256)]:assert r.upperroot(x)==d.I.root(p(x))[1];n+=1
for e,f in [(1,1),(1,3),(1,5),(0,1)]:assert r.lower(F(e),F(f))==d.remainder(F(e),F(f));n+=1
print(json.dumps({'checks':n,'native_calls':0}))
