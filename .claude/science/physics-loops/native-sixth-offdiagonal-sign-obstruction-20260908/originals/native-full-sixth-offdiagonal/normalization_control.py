"""Independent rank-two metric-direction control, not a native coefficient fixture."""
from fractions import Fraction as F
from pathlib import Path
import json

def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(a,c):return [[c*x for x in r] for r in a]
def tr(a):return list(map(list,zip(*a)))
B=[[F(1),F(0)],[F(1),F(1)]];C=tr(B);invD=[[F(1),F(0)],[F(0),F(1,2)]]
chi1=sc(mm(invD,B),-1);HB2=mm(C,chi1)
chi3=mm(invD,mm(chi1,HB2));HB4=mm(C,chi3)
M2=mm(tr(chi1),chi1);comm=add(mm(M2,HB2),sc(mm(HB2,M2),-1))
correct=add(HB4,sc(comm,F(1,2)));reverse=add(HB4,sc(comm,F(-1,2)))
checks=0
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
req(comm!=[[0,0],[0,0]],'noncommuting metric and Bloch coefficient')
req(correct==tr(correct),'forward canonical metric is Hermitian')
req(reverse!=tr(reverse),'reverse metric fails Hermiticity')
# Direct isometric energy expansion to g4: Omega=(P+gchi1+g3chi3), M^-1/2=I−g2M2/2.
# Omega†H Omega=M H_B. Symmetric sandwich gives HB4+(M2HB2−HB2M2)/2.
energy4=add(HB4,mm(M2,HB2))
sandwich=add(energy4,sc(add(mm(M2,HB2),mm(HB2,M2)),F(-1,2)))
req(sandwich==correct,'normalized-column energy matches forward direction')
r=dict(checks=checks,HB2=HB2,HB4=HB4,M2=M2,commutator=comm,forward4=correct,reverse4=reverse,scope='Generic real rank-two finite model, used only to discriminate canonical metric direction; not native H6 evidence.')
Path(__file__).with_name('NORMALIZATION_RESULT.json').write_text(json.dumps(r,default=str,indent=2)+'\n');print(json.dumps(r,default=str))
