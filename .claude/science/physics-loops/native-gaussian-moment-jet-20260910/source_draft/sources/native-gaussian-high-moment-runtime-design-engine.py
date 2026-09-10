"""Inert fixed-schema high-jet interface; native binding intentionally absent."""
import json,os
from pathlib import Path
import core as C
S=C.S
class Invalid(ValueError):pass
def need(x,m):
 if not x:raise Invalid(m)
def pair(x):
 need(type(x)is list and len(x)==2,'ordered dyadic pair')
 for a in x:need(type(a)is int and abs(a).bit_length()<=C.CAP,'literal bounded endpoint')
 need(x[0]<=x[1],'ordered endpoints');return tuple(x)
def scalar(x):
 need(type(x)is list and len(x)==2,'complex box');return pair(x[0]),pair(x[1])
def conj(x):return x[0],(-x[1][1],-x[1][0])
def table(x):
 need(type(x)is dict and set(x)=={str(j)for j in range(9)},'powers0..8 only');out={}
 for j in range(9):
  a=x[str(j)];need(type(a)is list and len(a)==2 and all(type(r)is list and len(r)==2 for r in a),'2x2 table');a=[[scalar(v)for v in row]for row in a]
  need(a[0][1]==conj(a[1][0]),'Hermitian interval symmetry')
  need(a[0][0][1]==a[1][1][1]==(0,0),'real diagonal intervals');out[j]=a
 return out
def validate(packet):
 need(type(packet)is dict and set(packet)=={'first_order','classes','units','grid_bits'},'packet fields');need(type(packet['first_order'])is int and packet['first_order']==7,'literal first_order7');need(type(packet['grid_bits'])is int and packet['grid_bits']==256,'fixed grid');need(packet['units']=='dimensionless_h1','units');need(type(packet['classes'])is dict and set(packet['classes'])=={'P','O'},'two classes');out={}
 for kind in ['P','O']:
  row=packet['classes'][kind];need(type(row)is dict and set(row)=={'D','B','accepted_m'},'class fields');m=row['accepted_m'];need(type(m)is dict and set(m)==set(map(str,range(7))),'accepted0..6');m={j:scalar(m[str(j)])for j in range(7)};need(m[0]==C.point(1),'m0 exact1');need(all(x[1]==(0,0)for x in m.values()),'real accepted moments');out[kind]=(table(row['D']),table(row['B']),m)
 return out
def atomic(path,value):
 temp=path.with_suffix(path.suffix+'.tmp')
 with temp.open('w')as f:json.dump(value,f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
 temp.replace(path)
def compute(packet,emit):
 # Pure interface; caller must authenticate containment/provenance before this function.
 data=validate(packet);rows=[]
 for kind in ['P','O']:
  D,B,m=data[kind];emit('accepted_lower_reused',{'kind':kind,'orders':list(range(7))})
  def event(stage,value):emit(stage,{'kind':kind,**value})
  def d(j,a,b):need(type(j)is int and 0<=j<=8,'ordinary degree');return D[j][a][b]
  def b(j,a,b):need(type(j)is int and 0<=j<=8,'projected degree');return B[j][a][b]
  ell,counters=C.logjet(10,d,b,event,first_order=7)
  emit('high_log_complete',{'kind':kind,'ell':ell,'counts':counters})
  # Reconstruct one scalar order at a time with raw sums before division/gates.
  from math import factorial
  low={n:C.divide(C.mul(C.point((-1)**n),x),factorial(n))for n,x in m.items()};logs=C.lower_logs(low);emit('lower_logs_from_accepted',{'kind':kind,'orders':list(range(1,7)),'logs':logs});logs.update(ell);Z=dict(low);new={}
  for n in range(7,11):
   total=C.ZERO
   for k in range(1,n+1):total=C.add(total,C.mul(C.mul(C.point(k),logs[k]),Z[n-k]));emit('scalar_reconstruction_partial',{'kind':kind,'order':n,'term':k,'sum':total})
   Z[n]=C.divide(total,n);value=C.mul(C.point((-1)**n*factorial(n)),Z[n]);emit('new_moment_raw',{'kind':kind,'order':n,'value':value});need(value[1][0]<=0<=value[1][1],'real moment containment');new[n]=value
  rows.append({'kind':kind,'orders':[7,8,9,10],'moments':new,'real_width_grid_units':{n:x[0][1]-x[0][0]for n,x in new.items()},'status':'ENCLOSURES_COMPUTED_NO_WIDTH_TARGET','counts':counters})
 return {'status':'COMPLETE_HIGH_JET_ARITHMETIC_ONLY','rows':rows,'native_lower_moments_recomputed':0,'native_oracle_calls':0,'first_order':7}
def execute_authenticated(packet,out):
 # Future dispatcher only; no input loader or activation authorizes native use now.
 out=Path(out);out.mkdir(exist_ok=False);current={};seq=0
 with(out/'EVENTS.ndjson').open('x')as stream:
  def emit(stage,value):
   nonlocal current,seq
   seq+=1;current={'sequence':seq,'stage':stage,'data':value};stream.write(json.dumps(current,sort_keys=True)+'\n');stream.flush();os.fsync(stream.fileno());atomic(out/'PARTIAL.json',current)
  try:r=compute(packet,emit);atomic(out/'RESULT.json',r);return r
  except BaseException as e:
   try:atomic(out/'FAILURE.json',{'error':repr(e),'current':current})
   except BaseException as err:e.add_note('retention '+repr(err))
   raise
