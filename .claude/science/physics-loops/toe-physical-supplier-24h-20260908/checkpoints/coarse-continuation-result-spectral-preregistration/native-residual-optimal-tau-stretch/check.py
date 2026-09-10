from fractions import Fraction as F
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent))
from proposal import propose,coefficients,upper,DELTA
n=0
def Q(l,t):return (3*t-2*l)/t**3+(t+2*DELTA)/(DELTA**2*t**3)*(l-t)**2
for l in map(F,[F(1,4),F(1,3),F(1,2),1,2,7,100]):
 for t in map(F,[F(1,8),F(1,4),F(1,2),1,3,16]):
  gap=(l-DELTA)*(l-t)**2*((t+2*DELTA)*l+DELTA*t)/(DELTA**2*t**3*l**2)
  assert Q(l,t)-1/l**2==gap>=0;n+=1
  r=(F(1),l,l*l);B,C,D=coefficients(r);assert Q(l,t)==r[0]/DELTA**2+B/t+C/t**2+D/t**3;n+=1
for ls in [(F(1,4),),(F(1,2),),(F(3,4),),(F(3),),(F(1,4),F(2)),(F(1,2),F(3),F(7))]:
 rho=tuple(sum((l**j for l in ls),F(0))for j in range(3));B,C,D=coefficients(rho)
 assert B<=0 and D>=0;n+=1
 if B<0:
  assert D>0 and B+2*C/DELTA+3*D/DELTA**2==8/DELTA**3*sum((l-DELTA)**2 for l in ls)>0;n+=1
 else:assert C==D==0;n+=1
 t=propose(rho);assert DELTA<t<=1<<22 and ((t/DELTA)*(1<<32)).denominator==1;n+=1
 exact=sum(1/l**2 for l in ls);box=[(x-F(1,10**12),x+F(1,10**12))for x in rho]
 value=min([box[0][1]/DELTA**2]+[upper(box,v)for v in(1,2,4,8,16,t)])
 assert value>=exact;n+=1
 if len(ls)==1 and ls[0]>DELTA:assert abs(t-ls[0])<=F(1,1<<32);n+=1
assert propose((1,0,0))==1;n+=1
assert propose((1,2,0))==1;n+=1
assert propose((1,F(1,4),F(1,16)))==1;n+=1
assert propose((1,F(1,2),F(1,4)))<1;n+=1
print(json.dumps({'status':'PASS','predicates':n,'actual_moments':0,'physical_calls':0}))
