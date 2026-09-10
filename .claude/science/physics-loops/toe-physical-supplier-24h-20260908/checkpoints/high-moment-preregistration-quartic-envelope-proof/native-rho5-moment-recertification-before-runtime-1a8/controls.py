import core as c
from fractions import Fraction as F
import json
checks=0
def ok(x):
 global checks
 assert x;checks+=1
for n,v in enumerate([1,6,42,324]):ok(c.moment(n)==v)
# Explicit synthetic high-tail replacement: no native moments beyond n=3.
c.tail=lambda kind:(F(1,100),F(1,10**40))
pi=c.machin()
for kind in c.RAD5:
 panels=[];total=(F(0),F(0))
 for j in range(67):
  v=(F(1,1000),F(1,1000)+F(1,10**40));total=c.add(total,v);panels.append({'panel':j-64,'value':v,'cumulative':total})
 first=((F(3,2**65),F(7,2**66)),(F(1,5),F(1,5)))
 lo=c.low(kind,first);hi=c.tail(kind);old=c.finish(total,lo,hi,pi,c.RAD4[kind])
 saved={'middle':total,'low':lo,'high':hi,'radius':c.RAD4[kind],'interval':old}
 out=c.recertify(kind,panels,saved,pi,first);ok(old[0]<=out['interval'][0]<=out['interval'][1]<=old[1]);ok(c.RAD5[kind]<c.RAD4[kind])
 for field,bad in [('radius',F(0)),('interval',(F(0),F(1))),('middle',(F(0),F(0))),('high',(F(0),F(0)))]:
  x=dict(saved);x[field]=bad
  try:c.recertify(kind,panels,x,pi,first)
  except ValueError:ok(True)
  else:raise AssertionError(field)
try:c.load_actual()
except RuntimeError:ok(True)
print(json.dumps({'status':'PASS','checks':checks,'scope':'synthetic panels and synthetic tail; moments only 0..3; no accepted results/catalog/node loads'}))
