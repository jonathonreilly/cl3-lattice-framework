"""Fixed tiny exact coordinate/PSD refusal controls; no native input."""
from fractions import Fraction as F
import pivot,interval as iv,json
count=0
def ck(x):
 global count
 if not x:raise ValueError('tiny control')
 count+=1
lab=(('pole',0,0,1,2),('pole',0,0,-1,2),('append',0,0,1,1))
# Literal R2 vectors e0,e1,e0/2; Gamma e0=e1, Gamma e1=-e0.
v=((F(1),F(0)),(F(0),F(1)),(F(1,2),F(0)))
def fetch(i,j):
 a,b=v[i],v[j];return iv.rational(a[0]*b[0]+a[1]*b[1]),iv.rational(-a[0]*b[1]+a[1]*b[0])
log=[];r=pivot.run(fetch,lab,log.append,native=False);ck(r['status']=='PASS_BOTH');ck(r['pairs']==1)
checkpoints=[x for x in log if x['stage']=='checkpoint'];ck(F(checkpoints[0]['raw_residual_upper'])==F(17,4));ck(F(checkpoints[-1]['raw_residual_upper'])==0)
coords=checkpoints[-1]['coordinate_intervals'][0]
for row,exact in zip(coords,((1,0,F(1,2)),(0,1,0))):
 for (m,rad),x in zip(row,exact):ck(F(m-rad,iv.S)<=x<=F(m+rad,iv.S))
# Dropping the required minus J sign produces the wrong second coordinate.
ck(r['history'][0]['j'][1]==iv.rational(-1));ck(coords[1][1][0]==iv.S)
ck(pivot.run(fetch,lab,lambda _:None,native=False,max_pairs=0)['status']=='PAIR_CAP')
# A broad uncertain diagonal fails the residual but supplies no positive pivot.
ck(pivot.run(lambda i,j:((-iv.S,iv.S),iv.ZERO),(('append',0,0,1,1),),lambda _:None,native=False)['status']=='PRECISION_STALL')
for fn in (lambda:pivot.divide(iv.ONE,(-1,1)),lambda:pivot.intersection((-4,-2),(0,1)),lambda:pivot.run(lambda i,j:((-2,-1),iv.ZERO),(('append',0,0,1,1),),lambda _:None,native=False),lambda:pivot.validate((('append',0,0,-1,1),),False),lambda:pivot.validate(lab,True)):
 try:fn()
 except ValueError:ck(True)
 else:ck(False)
ck(pivot.square((-3,2))[0]==0);ck(len(pivot.labels())==399);ck(sum(x[4] for x in pivot.labels())==795)
print(json.dumps({'status':'PASS_TINY_EXACT','predicates':count,'native_calls':0,'full_mock_calls':0}))
