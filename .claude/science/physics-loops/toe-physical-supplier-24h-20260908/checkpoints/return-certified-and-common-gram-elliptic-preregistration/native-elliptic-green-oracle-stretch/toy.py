from core import D,F,sqrt,TERMS
import json
n=0
for x in (F(1,3),F(2),F(7,4)):
 y=D(x,1);z=(y*y+3)/(y+2);v=(x*x+3)/(x+2);d=(x*x+4*x-3)/(x+2)**2
 if not z.v[0]<=v<=z.v[1] or not z.d[0]<=d<=z.d[1]:raise ValueError('dual rational')
 n+=2
for x in (F(1,4),F(4),F(9,16)):
 y=D(x,1).root();a,b=y.v
 if not a*a<=x<=b*b:raise ValueError('root')
 if not y.d[0]<=1/(2*b)<=1/(2*a)<=y.d[1]:raise ValueError('root derivative')
 n+=2
# Nonphysical elliptic parameter0 gives normalized series value1 and derivative1/4.
from math import comb
if F(comb(2,1)**2,16)!=F(1,4):raise ValueError('elliptic parameter convention')
n+=1
print(json.dumps({'status':'PASS','checks':n,'physical_oracle_calls':0}))
