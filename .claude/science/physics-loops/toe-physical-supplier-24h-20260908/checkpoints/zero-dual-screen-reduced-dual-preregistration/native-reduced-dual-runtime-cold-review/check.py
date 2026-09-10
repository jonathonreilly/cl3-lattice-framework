# Tiny synthetic proposal and scale tests; no production loader or Wick calls.
import pathlib,sys,json
from fractions import Fraction as F
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-degree10-reduced-dual-design');sys.path.insert(0,str(P));import dual as d
p=d.P;M={'A':[[p(int(i==j))for j in range(4)]for i in range(4)],'B':[[p(2),p(1)],[p(1),p(4)]],'correction':[p(2),p(3),p(4)]};t,s,reason=d.proposal(M);assert t==F(1,4) and s==0 and reason is None;n=1
for lam in d.SCALES:
 logs=[];a,b,c=d.certify(M,F(1,2),F(1,3),lam,lambda *x:logs.append(x));v=[1,-lam/3,-lam/2,lam/6];z=[-1,lam/2]
 assert a==p(sum(x*x for x in v));assert b==p(2*z[0]**2+2*z[0]*z[1]+4*z[1]**2);assert c==p(lam*(F(2,3)-F(1,2)-2));assert logs[0][0]=='raw_channel_forms';n+=4
bad={**M,'A':[[p(-1 if i==j==0 else 0)for j in range(4)]for i in range(4)]};logs=[]
try:d.certify(bad,F(0),F(0),F(0),lambda *x:logs.append(x))
except ValueError:assert logs[0][1]['a2']==p(-1);n+=1
else:raise AssertionError('negative norm accepted')
M['B'][1][1]=p(-1);assert d.proposal(M)[0]==0;n+=1
print(json.dumps({'checks':n,'native_calls':0,'Wick_calls':0}))
