"""Small synthetic8D identity carrier; no native histories/Gram."""
import core,interval as iv,coefficients as cf
from math import isqrt
import json
calls=[];events=[];R=((396,0),(396,1));C=[{R[0]:iv.ONE},{R[1]:iv.ONE}]
def entry(a,b):calls.append((a,b));return iv.ONE if a==b else iv.ZERO
r=core.bound(C,R,[iv.ZERO]*399,entry,[iv.ONE]*66,[iv.ONE]*66,events.append)
n=0
def req(x):
 global n
 if not x:raise ValueError(n)
 n+=1
req(r['status']=='COMPLETE_SUFFICIENT_UPPER_BOUND');req(len(calls)==36);req(len(r['results'])==2)
for x in r['results']:
 req(x['a_upper_numerator']==0);req(x['b'][1]**2>=66*iv.S**2);req((x['b'][1]-1)**2<66*iv.S**2);req(x['pass'] is False)
# Raw residuals are half-diagonal sums, never weighted sum twice.
d=[iv.ZERO]*399;d[0]=(2,2);d[1]=(3,3)
req(core.raw_residual_bounds(d,((0,0),(3,1)))=={(0,0):(0,5),(3,1):(0,5)})
for bad in (((399,0),),((0,True),)):
 try:core.raw_residual_bounds(d,bad)
 except ValueError:n+=1
 else:raise ValueError('bad original key')
try:cf.coefficients([{}]*25,events.append)
except ValueError:n+=1
else:raise ValueError('cap')
print(json.dumps({'status':'PASS_TINY_EIGHT_DIMENSION_BOUND','predicates':n,'native_calls':0,'physical_history_loaded':False,'scope':'synthetic8D, no native Gram or full mock'}))
