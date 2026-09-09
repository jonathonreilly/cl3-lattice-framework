"""Exact small abstract source tests; no physical history or entry reader."""
from fractions import Fraction as F
import core,interval as iv,json
n=0
def req(x):
 global n
 if not x:raise ValueError('check '+str(n))
 n+=1
one=iv.ONE;zero=iv.ZERO
seeds={0:{(396,0):one},1:{(397,0):one,(396,1):one}}
history=[{'index':0,'r':one,'g':[one,zero],'j':[zero,iv.neg(one)]},{'index':1,'r':one,'g':[zero,one],'j':[zero,zero]}]
events=[];cols,R=core.coefficients(history,events.append,seed_map=seeds,label_count=2)
req(cols==[{(396,0):one},{(396,1):one},{(397,0):one},{(397,1):one}])
# Wrong recurrence sign genuinely leaves an unwanted two-e1 coefficient.
wrong=core.combine(seeds[1],core.gamma(seeds[0]),one);req(wrong!={(397,0):one})
for col in cols:req(core.gamma(core.gamma(col))=={key:iv.neg(x) for key,x in col.items()})
req(core.seed(0)=={(3,0):iv.rational(F(1,2)),(0,0):iv.rational(F(1,2))})
req(core.seed(1)=={(3,0):iv.rational(F(1,2)),(0,0):iv.rational(F(-1,2))})
req(core.seed(2)=={(4,0):iv.rational(F(1,2)),(1,0):iv.rational(F(-1,2))})
for bad in [(0,iv.S),(-1,iv.S)]:
 try:core.coefficients([{'index':0,'r':bad,'g':[one],'j':[zero]}],events.append,seed_map={0:seeds[0]},label_count=1)
 except core.Indeterminate:req(True)
 else:req(False)
# Abstract10-dimensional identity Gram on needed support; no native covariance.
r=core.action(cols,R,lambda i,j:one if i==j else zero,[one]*66,[one]*66,events.append,leakage_target=F(1))
req(len(r['U'])<=24 and not r['midpoint_isometry_claim'])
for row in r['results']:
 req(all(x==zero for t in row['T'] for x in t));req(row['delta_squared_upper_numerator']==73*iv.S);req(not row['leakage_pass'])
# Free action on original pole: sigma coefficient and same-Gamma source.
req(core.free({(0,0):one},[one]*66,[one]*66)=={(0,0):iv.neg(one),(396,0):iv.rational(-2)})
try:core.free({(399,0):one},[one]*66,[one]*66)
except ValueError:req(True)
else:req(False)
try:core.native()
except ValueError:req(True)
else:req(False)
print(json.dumps({'status':'PASS_SMALL_SYNTHETIC','checks':n,'native_calls':0,'actual_history_loaded':False}))
