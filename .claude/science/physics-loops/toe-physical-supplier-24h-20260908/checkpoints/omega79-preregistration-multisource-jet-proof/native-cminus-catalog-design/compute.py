import json,time
from fractions import Fraction as F
from math import factorial,comb
from interval import add,mul
from interval_base import pi_bounds

def moment(n):return sum((F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1) for b in range(n-a+1)),F(0))
def run(out,catalog):
 start=time.monotonic();stage='initial';panels=[];total=(F(0),F(0));current=None
 def save(name,x):(out/name).write_text(json.dumps(x,indent=2)+'\n')
 def partial():save('PARTIAL.json',{'stage':stage,'current':current,'panels':panels,'sum':list(map(str,total)),'seconds':time.monotonic()-start})
 (out/'PANELS').mkdir();partial()
 try:
  if len(catalog)!=1742:raise ValueError('catalog count')
  for j in range(-64,3):
   stage='panel';current=j;nodes=[x for x in catalog if x['panel']==j]
   if len(nodes)!=26:raise ValueError('panel count')
   val=(F(0),F(0))
   for node in nodes:val=add(val,mul(node['weight_interval'],node['A_interval']))
   total=add(total,val);name=f'PANELS/{j+64:02d}.json';save(name,{'panel':j,'value':list(map(str,val)),'cumulative':list(map(str,total))});panels.append(name);partial()
  stage='tail';partial();tail=sum((F((-1)**n)*moment(n)/((2*n+1)*8**(2*n+1)) for n in range(26)),F(0));rem=F(12**26,53*8**53);radius=F(400,27)*F(4,25)**26;low=F(1,3*2**64);pl,pu=pi_bounds();ans=mul(add(add(total,(tail,tail+rem)),(-radius,radius+low)),(2/pu,2/pl));width=ans[1]-ans[0]
  result={'status':'CERTIFIED_TARGET' if width<=F(2,10**19) else 'INDETERMINATE','interval':list(map(str,ans)),'width':str(width),'target':str(F(2,10**19)),'middle':list(map(str,total)),'high_partial':str(tail),'high_remainder':str(rem),'low_bound':str(low),'quadrature_radius':str(radius),'panels':67,'nodes':1742,'oracle_calls':0,'new_catalog_only_integral':True,'seconds':time.monotonic()-start}
  stage='complete';save('RESULT.json',result);partial()
 except BaseException as e:partial();save('FAILURE.json',{'error':repr(e),'stage':stage,'current':current,'panels':panels});raise
