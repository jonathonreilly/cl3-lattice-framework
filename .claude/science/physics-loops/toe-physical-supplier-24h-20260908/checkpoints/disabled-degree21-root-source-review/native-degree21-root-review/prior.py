"""Independent saved-input mapping and quartic certificate arithmetic."""
from pathlib import Path
from fractions import Fraction as F
import json,math,hashlib
import independent as I
P=Path(__file__).resolve().parent.parent/'native-quartic-spectral-estimator-design'
def guard(x):
 if type(x)is not F or max(abs(x.numerator).bit_length(),x.denominator.bit_length())>32768:raise ValueError("rational cap")
 return x
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def norm(x):
 if type(x)is F:return str(x)
 if type(x)is bool:return('BOOL',x)
 if type(x)is int:return('INT',x)
 if isinstance(x,(list,tuple)):return tuple(norm(v)for v in x)
 if isinstance(x,dict):return tuple(sorted((str(k),norm(v))for k,v in x.items()))
 return x
def eq(x,y,m):need(norm(x)==norm(y),m)
def rat(x):
 need(type(x)is str and len(x)<=20000,'scalar string');v=guard(F(x));need(str(v)==x,'canonical');return v
def box(x):
 need(type(x)is list and len(x)==2,'box');a,b=map(rat,x);need(a<=b,'order');return a,b
def source_packet(b):
 def read(spec,lines=False):
  need(sha(spec['path'])==spec['sha256'],'input hash');text=Path(spec['path']).read_text();return[json.loads(x)for x in text.splitlines()]if lines else json.loads(text)
 ev=read(b['degree20']['files']['events'],True);need(len(ev)==255,'source255')
 for i,e in enumerate(ev,1):need(type(e['sequence'])is int and e['sequence']==i,'source sequence')
 high=read(b['high']['files']['result']);post=read(b['posterior20']['files']['result']);old=read(b['degree20']['files']['result']);tables=read(b['high']['tables']);hm={r['kind']:r for r in high['rows']}
 def select(stage,mode,kind=None):
  a=[e['data']for e in ev if e['stage']==stage and e['choice']==mode and(kind is None or e['data'].get('kind')==kind)];need(len(a)==1,'unique '+stage);return a[0]
 moments={}
 for kind in['P','O']:
  copies=[]
  for mode in['residual','variational']:copies.append([e['data']for e in ev if e['stage']=='vacuum_moment_raw'and e['choice']==mode and e['data'].get('kind')==kind])
  eq(copies[0],copies[1],'same lower moments');need(len(copies[0])==7,'seven lower');m=[]
  for j,r in enumerate(copies[0]):
   eq(r['index'],j,'index');v=box(r['real']);im=box(r['imaginary']);need(im[0]<=0<=im[1],'reality');m.append(v);Q=1<<256;lo=v[0].numerator*Q//v[0].denominator;hi=-((-v[1].numerator*Q)//v[1].denominator);eq(tables['classes'][kind]['accepted_m'][str(j)],[[lo,hi],[0,0]],'high lower mapping')
  eq(hm[kind]['orders'],[7,8,9,10],'high orders')
  for j in range(7,11):
   v=hm[kind]['moments'][str(j)];need(type(v)is list and len(v)==2,'high box')
   for z in v:need(type(z)is list and len(z)==2 and all(type(x)is int and abs(x).bit_length()<=4096 for x in z)and z[0]<=z[1],'high endpoints')
   need(v[1][0]<=0<=v[1][1],'high reality');m.append((F(v[0][0],1<<256),F(v[0][1],1<<256)))
  moments[kind]=m
 out={}
 for index,mode in enumerate(['residual','variational']):
  gate=select('gate_inputs',mode);prior=post['rows'][index];eq(prior['mode'],mode,'prior mode');eq(prior['nominal'],gate['nominal'],'nominal');eq(old['rows'][index]['nominal'],gate['nominal'],'original nominal');rows={}
  for kind in['P','O']:
   pol=select('first_polynomial',mode,kind)['coefficients'];r=select('residual_raw',mode,kind);g=gate['rows'][kind];eq(pol,g['p'],'same p');eq(r['q'],g['q'],'same q');eq(r['r2'],g['r2'],'same r2');eq(r['t2'],g['t2'],'same t2');v=box(r['r2']);rows[kind]={'moments':moments[kind],'p':list(map(rat,pol)),'r2':v,'t2':box(r['t2']),'old_first_squared_upper':guard(16*v[1])}
  out[mode]={'rows':rows,'nominal':box(gate['nominal']),'old_alpha':box(prior['alpha_interval']),'trial_a2':(rat(prior['a_squared_upper']),)*2,'trial_b2':(rat(prior['b_squared_upper']),)*2}
 return out

