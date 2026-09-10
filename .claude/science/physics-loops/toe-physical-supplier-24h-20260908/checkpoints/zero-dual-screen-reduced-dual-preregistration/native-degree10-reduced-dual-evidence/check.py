from pathlib import Path
from fractions import Fraction as F
import sys,json
sys.dont_write_bytecode=True
P=Path('/private/tmp/toe-24h-probes-20260908/native-degree10-reduced-dual-design');sys.path.insert(0,str(P));import dual,interval as I
rows={'P':(F(1,3),F(2,5),F(1,7)),'O':(F(2,3),F(1,6),F(1,4))};keys={};saved={};n=0
for label in dual.LABELS:
 G,ops,key,raw=dual.prepare(label,rows,I.point(0),I.point(0));cl=dual.kind(label)
 if cl in keys:assert keys[cl]==key
 else:keys[cl]=key;saved[cl]=(G,ops)
 n+=1
assert len(set(keys.values()))==2;n+=1
for cl,(G,ops)in saved.items():
 events=[];M=dual.acquire(G,ops,lambda s,d:events.append(s));assert M['words']==171 and events.count('dual_entry')==16;n+=1
 t,s,why=dual.proposal(M);assert 0<=t<=4 and 0<=s<=4 and (t*(1<<64)).denominator==(s*(1<<64)).denominator==1;n+=1
 a,b,c=dual.certify(M,t,s);assert a[1]>=0 and b[1]>=0;n+=1
 a,b,c=dual.certify(M,F(0),F(0));assert a==M['A'][0][0]and b==M['B'][0][0]and c==I.point(0);n+=1
# Explicit P table entries, independent bank construction.
f=lambda b=None,k=None,a=0:dual.vector(a,b,k)
d=[F(1),F(0),F(1),F(0),F(0),F(0)];k=[F(1)]*6;e=[F(0)]*4+[F(1)]*2
bank=[f(a=1),f(k=d),f(k=k),f(k=e),f(b=d),f(b=k),f(b=e)]
white=[[1,-2,-6,-2],[-2,12,14,0],[-6,14,42,14],[-2,0,14,14]];black=[[2,2,0],[2,6,2],[0,2,2]]
c=F(2,7);nu=F(9,5);kap=[[-c,-3*c,-c],[6*c,nu/3,0],[nu/3,nu,nu/3],[0,nu/3,nu/3]]
for i in range(7):
 for j in range(7):
  v=dual.covariance(bank[i],bank[j],I.point(c),I.point(nu))
  if i<4 and j<4:want=(F(white[i][j]),F(0))
  elif i>=4 and j>=4:want=(F(black[i-4][j-4]),F(0))
  elif i<4:want=(F(0),F(kap[i][j-4]))
  else:want=(F(0),F(-kap[j][i-4]))
  assert v==(I.point(want[0]),I.point(want[1]));n+=1
print(json.dumps({'status':'PASS','predicates':n,'synthetic_gram_sets':2,'actual_saved_values':0,'full_native_or_mode_run':0}))
