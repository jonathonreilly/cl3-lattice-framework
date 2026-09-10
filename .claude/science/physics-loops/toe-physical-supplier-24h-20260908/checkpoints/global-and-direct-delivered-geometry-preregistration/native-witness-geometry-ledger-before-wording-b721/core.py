from fractions import Fraction as F
S=1<<192;G=1<<64

def ceildiv(a,b):
 if a<0 or b<=0:raise ValueError('positive quotient')
 return (a+b-1)//b

def interval(xs):
 if not isinstance(xs,list) or len(xs)!=2 or any(type(x)is not str for x in xs):raise ValueError('interval strings')
 a,b=map(F,xs)
 if not 0<a<=b:raise ValueError('positive interval')
 if max(abs(q.numerator).bit_length() for q in (a,b))>65536 or max(q.denominator.bit_length() for q in(a,b))>65536:raise ValueError('input bits')
 return a.numerator*S//a.denominator,ceildiv(b.numerator*S,b.denominator)

def gap(a,b):
 d=max(a[0]-b[1],b[0]-a[1])
 if d<=0:raise ValueError('unresolved coincidence')
 return d

def square(a):return a[0]*a[0],a[1]*a[1]
def point(s):return interval([s,s])
def kernel_gain(weight,den):return ceildiv(weight[1]*G,den)

def ledger(new,old,outer,emit):
 if len(new)!=378 or len(old)!=66 or len(outer)!=1742:raise ValueError('fixed census')
 ns=[];os=[];ts=[]
 for role,rows in [('new',new),('old',old),('outer',outer)]:
  for i,r in enumerate(rows):
   emit({'stage':'before_normalize','role':role,'row':i})
   if role=='new':ns.append((interval(r['s_interval']),interval(r['weight_interval'])))
   elif role=='old':os.append(interval(r['s_interval']))
   else:ts.append((interval(r['t_interval']),interval(r['weight'])))
 oldgain=[0]*66;c_gain=0;rows=[];counts=[0,0]
 for i,(s,w) in enumerate(ns):
  emit({'stage':'before_node','id':i,'counts':counts.copy()})
  local=0
  for k,t in enumerate(os):
   d=gap(s,t);v=128*kernel_gain(w,d);oldgain[k]+=v;local=max(local,v);counts[0]+=1
  ward=ceildiv(6*w[1]*G,S)+2*ceildiv(w[1]*G,s[0]);c_gain+=2*ceildiv(w[1]*G,s[0])
  # Allocate every new-B term separately; max old-column <=sum of maxima.
  b_gain=local+ward
  ag=0;tg=0
  ss=square(s)
  for t,wt in ts:
   tt=square(t);d=gap(ss,tt)
   ag+=ceildiv(wt[1]*ss[1]*G,d*S)
   tg+=ceildiv(wt[1]*tt[1]*G,d*S);counts[1]+=1
  # 2/pi<1. Each integral input coefficient uses this safe upper bound.
  eta_b=F(1,10**5)/((7*(1<<40))*378*F(b_gain,G))
  eta_a=eta_b/(4*max(F(ag,G),F(1)))
  row={'id':i,'weighted_B_gain_units':b_gain,'As_integral_gain_units':ag,'catalog_integral_gain_units':tg,'gain_scale':G,'required_B_radius':str(eta_b),'required_As_radius_quarter_B_budget':str(eta_a),'catalog_radius_reserve':str(F(tg,G)*F(1,10**49))}
  emit({'stage':'node_complete','data':row});rows.append(row)
 oldbud=[str(F(1,10**5)/((7*(1<<40))*66*F(x,G))) for x in oldgain]
 out={'rows':rows,'old_B_required_radii':oldbud,'c_required_radius':str(F(1,10**5)/((7*(1<<40))*F(c_gain,G))),'counts':counts,'status':'COMPLETE_GEOMETRY_GAIN_LEDGER','scope':'conditional weighted B/c allocation only; no scalar containment or witness value'}
 emit({'stage':'complete','counts':counts});return out
