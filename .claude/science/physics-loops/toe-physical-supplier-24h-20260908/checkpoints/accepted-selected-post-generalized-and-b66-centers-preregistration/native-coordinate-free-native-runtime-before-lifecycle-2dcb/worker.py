"""Unactivated same-span orchestration; caller-supplied authenticated DATA only."""
import json,os,time
from pathlib import Path
from fractions import Fraction as F
import adapter,binder

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encode(v)for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [encode(v)for v in x]
 return x

def save(p,x):
 t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(encode(x),separators=(',',':'))+'\n');os.replace(t,p)

def acquire(indices,entry,emit):
 """entry.raw supplies existing192 physical boxes, including selector inflation."""
 R,_=adapter.seeds(indices);U=tuple(sorted(set(R)|set(adapter.Q)))
 raw=sorted({r for r,g in U});table={};count=0
 for ii,r in enumerate(raw):
  for s in raw[ii:]:
   emit('acquisition_current',{'raw_i':r,'raw_j':s,'completed':count})
   G,J=entry.raw(r,s)
   for box in(G,J):
    if len(box)!=2 or any(type(x)is not int or abs(x).bit_length()>4096-64 for x in box)or box[0]>box[1]:raise ValueError('raw192 physical interval')
   # Exact change of dyadic representation: no reduced old physical radius.
   G=tuple(x<<64 for x in G);J=tuple(x<<64 for x in J)
   if r==s:
    if not J[0]<=0<=J[1]:raise ValueError('J diagonal contradiction')
    J=(0,0)
   table[r,s]=(G,J);count+=1;emit('acquired_raw',{'i':r,'j':s,'G':G,'J':J,'count':count})
 if count>1378:raise ValueError('raw acquisition cap')
 M=[]
 for r,g in U:
  row=[]
  for s,h in U:
   G,J=table[min(r,s),max(r,s)]
   if r>s:J=(-J[1],-J[0])
   row.append(G if g==h else ((-J[1],-J[0])if g else J))
  M.append(row)
 emit('physical_principal',{'U':U,'M':M,'raw_pairs':count});return M

def compute(prepared,out):
 """Not called by dispatcher. Future binder returns records/entries/family/descriptors."""
 out=Path(out);out.mkdir(exist_ok=False);rows=[];current={'stage':'start'};start=time.monotonic();opened=prepared['descriptors']
 save(out/'PARTIAL.json',current)
 try:
  if len(prepared['records'])!=5 or len(prepared['entries'])!=5:raise ValueError('five orbit')
  for oi,record in enumerate(prepared['records']):
   od=out/('ORBIT_'+str(oi));od.mkdir();serial=0
   def emit(stage,data):
    nonlocal current,serial
    current={'orbit':oi,'stage':stage,'serial':serial}
    # Current context precedes serialization; full stage data precedes next gate.
    save(out/'PARTIAL.json',{**current,'completed_orbits':rows})
    save(od/('%05d_%s.json'%(serial,stage)),data);serial+=1
    if serial>4096:raise ValueError('stage file cap')
   indices,T=binder.selected_record(record,oi);emit('selected_candidate',record)
   M=acquire(indices,prepared['entries'][oi],emit)
   try:
    result=adapter.run(indices,T,M,prepared['poles'],prepared['alpha'],emit)
   except adapter.l.Refused as exc:
    result={'status':'INDETERMINATE_CERTIFICATE','error':repr(exc),'current':current,'leakage_pass':False};emit('indeterminate',result)
   save(od/'RESULT.json',result);rows.append({'orbit':oi,'status':result['status'],'stage_files':serial})
   del M,T
  result={'status':'COMPLETE_SAME_SPAN_LEAKAGE_ATTEMPT','orbits':rows,'h':1,'target_squared':'1/1000000000000','C_width_gate_required':False,'new_scalar_recenter':False,'seconds':time.monotonic()-start}
  save(out/'RESULT.json',result);save(out/'PARTIAL.json',{'stage':'complete','completed_orbits':rows});return result
 except BaseException as exc:
  save(out/'FAILURE.json',{'current':current,'completed_orbits':rows,'error':repr(exc),'seconds':time.monotonic()-start});raise
 finally:
  errors=[]
  for d in opened:
   try:d.verify()
   except BaseException as exc:errors.append('verify '+repr(exc))
   finally:
    try:d.close()
    except BaseException as exc:errors.append('close '+repr(exc))
  if errors:
   save(out/'IMMUTABILITY_FAILURE.json',{'errors':errors,'current':current});raise ValueError('immutable DATA descriptors')
