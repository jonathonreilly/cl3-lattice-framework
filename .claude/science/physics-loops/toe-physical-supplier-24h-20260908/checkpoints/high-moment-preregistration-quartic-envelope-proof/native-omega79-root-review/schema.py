"""Independent directed dual-integrand replay; raw A truth inherited."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,isfinite
import json,hashlib
S=1<<192;LIMIT=384*1048576

def req(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def eq(a,b,m):req(type(a)is type(b)and(a.keys()==b.keys()and all(equal(a[k],b[k])for k in a)if type(a)is dict else len(a)==len(b)and all(equal(x,y)for x,y in zip(a,b))if type(a)is list else a==b),m)
def equal(a,b):
 try:eq(a,b,'equality');return True
 except ValueError:return False

def integer(x,n):req(type(x)is int and x==n,'literal integer')
def rat(x):
 req(type(x)is str and len(x)<=40000,'rational token');v=F(x);req(str(v)==x and max(v.numerator.bit_length(),v.denominator.bit_length())<=65536,'rational cap');return v

def box(x):
 req(type(x)is list and len(x)==2,'box shape');a,b=map(rat,x);req(a<=b,'box order');return a,b

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(tuple,list)):return[encode(y)for y in x]
 if isinstance(x,dict):return{str(k):encode(v)for k,v in x.items()}
 return x

def rounding(x):return F(x[0].numerator*S//x[0].denominator,S),F(-((-x[1].numerator*S)//x[1].denominator),S)
def add(a,b):return rounding((a[0]+b[0],a[1]+b[1]))
def mul(a,b):
 v=[x*y for x in a for y in b];return rounding((min(v),max(v)))
def neg(a):return -a[1],-a[0]
def node(t,a,w,r,m):
 square=mul(t,t);power=(F(1),F(1));q=(F(0),F(0))
 for j in range(r+1):
  term=mul((m[r-j],m[r-j]),power);q=add(q,neg(term)if j%2 else term);power=mul(power,square)
 correction=mul(power,a);q=add(q,neg(correction)if(r+1)%2 else correction)
 return q,mul(w,q),mul(w,power)

def convolution_moment(n):
 # Central-binomial recurrence, then two successive binomial convolutions.
 req(type(n)is int and 0<=n<=45,'fixed convolution index');c=[1]
 for k in range(n):
  num=2*(2*k+1)*c[-1];req(num%(k+1)==0,'central integer recurrence');c.append(num//(k+1))
 two=[sum(comb(k,j)*c[j]*c[k-j]for j in range(k+1))for k in range(n+1)]
 return F(sum(comb(n,j)*two[j]*c[n-j]for j in range(n+1)))
def new_moments():return{k:convolution_moment(k)for k in(44,45)}
def pi_bounds():
 bounds=[]
 for q,n in [(5,32),(239,10)]:
  total=F(0)
  for k in range(n):total+=F((-1)**k,(2*k+1)*q**(2*k+1))
  rem=F(1,(2*n+1)*q**(2*n+1));bounds.append((total,total+rem))
 return 16*bounds[0][0]-4*bounds[1][1],16*bounds[0][1]-4*bounds[1][0]
def tails(r,m):
 terms=[F((-1)**j)*m[r+1+j]/((2*j+1)*8**(2*j+1))for j in range(40)];e=F(1,2**64);lo=sum(((-1)**j*m[r-j]*e**(2*j+1)/F(2*j+1)for j in range(r+1)),F(0));width=F(17,60)*e**(2*r+3)/F(2*r+3)
 return{'r':r,'high_terms':terms,'high_partial':sum(terms,F(0)),'high_remainder':m[r+41]/(81*8**81),'low_interval':(lo-width,lo)if(r+1)%2 else(lo,lo+width),'quadrature_radius':F(136,3)*m[r]/4**52,'tail_terms':40}
def final(total,t):
 pl,pu=pi_bounds();low=t['low_interval'];rad=t['quadrature_radius'];v=add(add(total,(t['high_partial'],t['high_partial']+t['high_remainder'])),(low[0]-rad,low[1]+rad));return mul(v,(2/pu,2/pl)),(pl,pu)

def inputs(b):
 def bound(p):req(sha(p['path'])==p['sha256'],'bound source');return read(p['path'])
 tail=bound(b['omega5']['tail']);req(set(tail['moments'])=={str(k)for k in range(3,44)},'inherited41moments');m={0:F(1),1:F(6),2:F(42)}
 for k in range(3,44):m[k]=rat(tail['moments'][str(k)]);req(m[k].denominator==1 and 0<m[k]<=12**k,'inherited moment integer')
 req(sha(b['catalog_geometry_path'])==b['catalog_geometry_sha256'],'geometry hash');geo=read(b['catalog_geometry_path']);cat=b['catalog'];req(sha(Path(cat['directory'])/'RESULT.json')==cat['result_sha256'],'catalog result');rr=read(Path(cat['directory'])/'RESULT.json')['rows'];req(len(rr)==3484 and len(geo['nodes'])==1742 and len(geo['endpoints'])==3484,'catalog census');aa=[]
 for i,(row,e)in enumerate(zip(rr,geo['endpoints'])):
  integer(row['id'],i);integer(e['id'],i);req(row['path']==f'ORACLES/{i:04d}.json'and row['gate']=='PASS','endpoint row');p=Path(cat['directory'])/row['path'];req(sha(p)==row['sha256'],'endpoint hash');x=read(p);eq(x['catalog_endpoint'],e,'endpoint metadata');eq(x['s'],e['s'],'endpoint argument');v=box(x['A']);req(all(max(t.numerator.bit_length(),t.denominator.bit_length())<=512 for t in v),'A component cap');ap=box(x['Aprime']);eq(x['widths'],encode([v[1]-v[0],ap[1]-ap[0]]),'raw width identity');req(max(v[1]-v[0],ap[1]-ap[0])<=F(1,10**30),'raw width bound');aa.append(v)
 mapped=[]
 for i,g in enumerate(geo['nodes']):
  integer(g['id'],i);integer(g['panel'],i//26-64);eq(g['endpoint_ids'],[2*i,2*i+1],'endpoint links');t=box(g['t_interval']);req(all(max(x.numerator.bit_length(),x.denominator.bit_length())<=512 for x in t),'t component cap');original_weight=box(g['weight']);req(original_weight[1]-original_weight[0]<=F(1,10**38),'weight width');a=(aa[2*i+1][0],aa[2*i][1]);w=rounding(box(g['weight']));req(0<t[0]<t[1]<=8 and t[1]-t[0]<=F(1,2**140),'t bound');req(0<=a[0]<=a[1]<F(1,3)and a[1]-a[0]<=F(3,10**30),'A bound');req(0<w[0]<=w[1],'positive weight');mapped.append({'id':i,'panel':i//26-64,'t_interval':t,'A_interval':a,'weight_interval':w})
 req(sum(x['weight_interval'][1]for x in mapped)<=9,'weight sum');return m,mapped

def check(O,rf,elapsed,progress):
 O=Path(O);files={p.relative_to(O).as_posix():sha(p)for p in O.rglob('*')if p.is_file()};base={'STARTED.json','WORKER_COMPLETE.json','RESULT.json','PARTIAL.json','REUSED_MOMENTS.json','M44.json','M45.json','CURRENT_ARITHMETIC.json','TAIL7.json','TAIL9.json','FINAL7.json','FINAL9.json'};expected=base|{f'NODES/{i:04d}.json'for i in range(1742)}|{f'PANELS/{i:02d}.json'for i in range(67)};req(set(files)==expected and len(files)==1821,'exact1821files');req({p.relative_to(O).as_posix()for p in O.rglob('*')if p.is_dir()}=={'NODES','PANELS'},'exact directories')
 P=Path(rf['worker_path']);r=read(O/'RESULT.json');w=read(O/'WORKER_COMPLETE.json');part=read(O/'PARTIAL.json');eq(read(O/'STARTED.json'),{'runtime_sha256':rf['worker_freeze'],'binding_sha256':sha(P/'BINDING.json'),'output':str(O.resolve()),'no_retry':True},'started auth');req(w['status']=='COMPLETE_NEW_OMEGA79_ONLY'and r['status']=='COMPLETE_NEW_OMEGA79','completion');req(w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==sha(P/'BINDING.json')and w['result_sha256']==files['RESULT.json'],'worker receipt')
 for x,cap in[(r['seconds'],29),(w['seconds'],29),(part['seconds'],29),(elapsed,29.5)]:req(type(x)in(int,float)and isfinite(x)and 0<x<cap,'time')
 req(r['seconds']<=part['seconds']<=w['seconds']<=elapsed,'time order');req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=LIMIT,'worker RSS')
 for k,n in [('nodes',1742),('panels',67),('endpoint_oracles_reused',3484),('oracle_calls',0),('reused_moments',41),('tail_terms_each',40)]:integer(r[k],n)
 eq(r['new_moments'],[44,45],'new indices');b=read(P/'BINDING.json');m,catalog=inputs(b);eq(read(O/'REUSED_MOMENTS.json'),encode(m),'inherited moments copy');new=new_moments()
 for k in(44,45):m[k]=new[k];eq(read(O/f'M{k}.json'),encode({'index':k,'value':m[k]}),'independent new convolution')
 totals={k:(F(0),F(0))for k in(3,4)};powers={k:(F(0),F(0))for k in(3,4)};lastvals=None
 for panel in range(-64,3):
  subtotal={k:(F(0),F(0))for k in(3,4)}
  for nid in range((panel+64)*26,(panel+65)*26):
   inp=catalog[nid];d=read(O/f'NODES/{nid:04d}.json');integer(d['id'],nid);integer(d['panel'],panel);eq(d['input'],encode(inp),'mapped input source');vals={}
   for k in(3,4):
    q,v,p=node(inp['t_interval'],inp['A_interval'],inp['weight_interval'],k,m);subtotal[k]=add(subtotal[k],v);powers[k]=add(powers[k],p);vals[k]={'integrand':q,'weighted':v,'panel_cumulative':subtotal[k],'weighted_power_cumulative':powers[k]}
   eq(d['values'],encode(vals),'all dual node arithmetic');lastvals=vals
  for k in(3,4):totals[k]=add(totals[k],subtotal[k])
  eq(read(O/f'PANELS/{panel+64:02d}.json'),encode({'panel':panel,'value':subtotal,'cumulative':totals}),'panel cumulative');progress({'stage':'panel_checked','panel':panel})
 eq(read(O/'CURRENT_ARITHMETIC.json'),encode({'id':1741,'r':4,'values':lastvals}),'last arithmetic');rows=[]
 for k,target,cap in[(3,F(1,10**22),15000000),(4,F(1,10**20),800000000)]:
  t=tails(k,m);eq(read(O/f'TAIL{2*k+1}.json'),encode(t),'independent tails');ans,pib=final(totals[k],t);width=ans[1]-ans[0];eq(read(O/f'FINAL{2*k+1}.json'),encode({'r':k,'interval':ans,'width':width,'middle':totals[k],'weighted_power':powers[k],'pi_interval':pib}),'final pi scaling');mg=totals[k][1]-totals[k][0]<=target;pg=powers[k][1]<=cap;rows.append(encode({'observable':f'omega{2*k+1}','status':'CERTIFIED_TARGET'if mg and pg and width<=target else'INDETERMINATE','target':target,'interval':ans,'width':width,'middle_width_gate':mg,'weighted_power_gate':pg,'quadrature_radius':t['quadrature_radius']}))
 eq(r['rows'],rows,'exact target flags');eq(part['stage'],'complete','partial complete');eq(part['current'],{'result':r},'partial result');integer(part['completed_nodes'],1742);eq(part['panels'],list(range(-64,3)),'partial panels');eq(part['middle'],encode(totals),'partial totals');eq(part['weighted_power'],encode(powers),'partial powers');req(files=={p.relative_to(O).as_posix():sha(p)for p in O.rglob('*')if p.is_file()},'output immutable final census')
 return{'status':'ACCEPTED_NEW_OMEGA79_SCHEMA','count':2,'nodes':1742,'dual_integrands':3484,'panels':67,'new_moments':[44,45],'inherited_moments':41,'result_sha256':files['RESULT.json'],'output_sha256':files,'independent_node_tail_final_arithmetic':True,'raw_A_oracle_truth_inherited':True}
