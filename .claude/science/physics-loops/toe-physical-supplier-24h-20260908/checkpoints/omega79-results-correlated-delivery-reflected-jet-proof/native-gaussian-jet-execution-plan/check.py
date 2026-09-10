import loader as L
from fractions import Fraction as F
import json
n=0
for x in ['1/3','-1/7','1','0']:
 a=L.dyadic([x,x]);v=F(x);assert F(a[0][0],L.S)<=v<=F(a[0][1],L.S);n+=1
for fn in [lambda:L.dyadic(['2','1']),lambda:L.dyadic([True,'1']),lambda:L.load('/path/not/read')]:
 try:fn()
 except(ValueError,TypeError):n+=1
 else:raise AssertionError('missing refusal')
print(json.dumps({'checks':n,'native_values':0,'status':'PASS_SOURCE_HELPERS'}))
