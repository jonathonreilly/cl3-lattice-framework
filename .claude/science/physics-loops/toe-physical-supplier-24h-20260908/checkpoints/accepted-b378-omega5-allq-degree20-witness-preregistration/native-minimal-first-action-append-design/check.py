"""Small nonphysical algebra controls: no stream66, binder or native data."""
from fractions import Fraction as F
import core,interval as iv,json
count=0
def req(x):
 global count
 if not x:raise ValueError('predicate '+str(count))
 count+=1
def enclosed(i,x):return i[0]<=x*iv.S<=i[1]
for orbit in core.ORBITS:
 old,new=core.geometry(orbit)
 for a in range(3):
  for v in range(3):
   I,O,T,N=core.bilinear(new[a],old[v])
   for sig in(-1,1):
    s=F(3,2);A=F(2,7);B=F(3,8);mu=F(5,2);D=(1-s*s*A)/6
    g,j=core.cross(a,v,s,sig,A,B,mu,orbit,iv.rational(2))
    req(enclosed(g,sig*s*(A*N-D*O)+D*T));req(enclosed(j,B*N-(mu-s*s*B)*O/6-sig*s*B*T/6))
   g,j=core.insertion(a,v,F(1,3),F(5,2),orbit)
   target=-F(5,2)*T/24 if v==0 else-F(1,3)*N/4+F(5,2)*O/24
   req(g==iv.ZERO and enclosed(j,target))
   if v==0:req(not enclosed(j,-target))
  for c in range(a,3):
   g,j=core.self_entry(a,c,orbit);req(enclosed(g,F(sum(x*y for x,y in zip(new[a],new[c])),4)) and j==iv.ZERO)
print(json.dumps({'status':'PASS_SMALL_SYNTHETIC','checks':count,'native_calls':0,'full_stream_calls':0}))
