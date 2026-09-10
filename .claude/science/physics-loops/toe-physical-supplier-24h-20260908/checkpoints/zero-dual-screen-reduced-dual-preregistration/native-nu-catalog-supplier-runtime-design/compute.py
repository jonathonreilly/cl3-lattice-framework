import json,time
from fractions import Fraction as F
from math import factorial,comb
from interval import add,mul,neg
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
   for node in nodes:
    tt=mul(node['t_interval'],node['t_interval']);q=add(add((F(6),F(6)),neg(tt)),mul(mul(tt,tt),node['A_interval']));val=add(val,mul(node['weight_interval'],q))
   total=add(total,val);name=f'PANELS/{j+64:02d}.json';save(name,{'panel':j,'value':list(map(str,val)),'cumulative':list(map(str,total))});panels.append(name);partial()
  stage='tail';partial()
  middle_width_ok=total[1]-total[0]<=F(2,10**25)
  moments={k:moment(k) for k in range(2,42)}
  tail=sum((F((-1)**n)*moments[n+2]/((2*n+1)*8**(2*n+1)) for n in range(40)),F(0))
  rem=F(12**42,81*8**81);radius=F(256,4**52);eps=F(1,2**64)
  low=6*eps-eps**3/3;low_width=F(17,60)*eps**5/5
  save('TAIL.json',{'moments':{str(k):str(v) for k,v in moments.items()},'high_partial':str(tail),'high_remainder':str(rem),'low_interval':[str(low),str(low+low_width)],'quadrature_radius':str(radius)})
  pl,pu=pi_bounds();ans=mul(add(add(total,(tail,tail+rem)),(low-radius,low+low_width+radius)),(2/pu,2/pl));width=ans[1]-ans[0]
  result={'observable':'nu=E_X_power_3_over_2','status':'CERTIFIED_TARGET' if middle_width_ok and width<=F(2,10**19) else 'INDETERMINATE','interval':list(map(str,ans)),'width':str(width),'target':str(F(2,10**19)),'middle':list(map(str,total)),'middle_width_gate':middle_width_ok,'high_partial':str(tail),'high_remainder':str(rem),'low_interval':[str(low),str(low+low_width)],'tail_terms':40,'quadrature_radius':str(radius),'panels':67,'nodes':1742,'oracle_calls':0,'new_catalog_only_integral':True,'seconds':time.monotonic()-start}
  stage='complete';save('RESULT.json',result);partial()
 except BaseException as e:partial();save('FAILURE.json',{'error':repr(e),'stage':stage,'current':current,'panels':panels});raise
