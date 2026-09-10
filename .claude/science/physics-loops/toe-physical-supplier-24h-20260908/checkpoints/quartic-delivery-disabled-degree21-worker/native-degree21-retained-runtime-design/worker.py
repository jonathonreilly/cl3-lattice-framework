import json,os,time
from pathlib import Path
from fractions import Fraction as F
import loader,core,assembly as A,tables,certificate
MAX_TOTAL=512*1048576;MAX_EVENT=4*1048576

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return[encode(v)for v in x]
 if isinstance(x,dict):return{str(k):encode(v)for k,v in x.items()}
 return x
def atomic(p,x):
 t=p.with_suffix(p.suffix+'.tmp')
 with t.open('w')as f:json.dump(encode(x),f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
 t.replace(p)
def run(binding,out):
 start=time.monotonic();seq=0;current={};mode=None;jet_id=None;total=0;rows=[]
 with(out/'EVENTS.ndjson').open('x')as log:
  def emit(stage,data):
   nonlocal seq,current,total
   current={'sequence':seq+1,'choice':mode,'jet':jet_id,'stage':stage};atomic(out/'PARTIAL.json',{'current':current,'completed':len(rows),'seconds':time.monotonic()-start})
   raw=json.dumps(encode(dict(current,data=data)),separators=(',',':'))+'\n';size=len(raw.encode());
   if size>MAX_EVENT or total+size>MAX_TOTAL:raise ValueError('bounded event serialization')
   log.write(raw);log.flush();os.fsync(log.fileno());seq+=1;total+=size;current['sequence']=seq
  try:
   R,inputs=loader.load(binding,emit);atomic(out/'INPUTS.json',{'radials':R,'modes':inputs});jets={};inner={};counts={}
   for kind in('P','O'):
    jet_id='inner_'+kind;D,B=tables.inner(lambda n:R[n],kind);emit('jet_start',{'profile':'inner21','source_width':3,'mask':[2,2,4],'D':{n:[[D(n,i,j)for j in range(3)]for i in range(3)]for n in range(7)},'B':{n:[[B(n,i,j)for j in range(3)]for i in range(3)]for n in range(7)}})
    Z,c=core.jet('inner21',A.defects('inner21'),D,B,emit);inner[kind]=Z;counts[jet_id]=c;atomic(out/(jet_id+'.json'),{'coefficients':[[list(k),v]for k,v in Z.items()],'counts':c});emit('jet_complete',{'counts':c})
   for left,right,o,_ in A.SIGNATURES:
    jet_id='nominal_'+left+right+'_'+str(o);D,B=tables.nominal(lambda n:R[n],left,right,o);emit('jet_start',{'profile':'nominal21','source_width':4,'mask':[2,2,1,1],'signature':[left,right,o],'D':{n:[[D(n,i,j)for j in range(4)]for i in range(4)]for n in range(5)},'B':{n:[[B(n,i,j)for j in range(4)]for i in range(4)]for n in range(5)}})
    Z,c=core.jet('nominal21',A.defects('nominal21'),D,B,emit);jets[left,right,o]=Z;counts[jet_id]=c;atomic(out/(jet_id+'.json'),{'coefficients':[[list(k),v]for k,v in Z.items()],'counts':c});emit('jet_complete',{'counts':c})
   jet_id=None
   for mode in('residual','variational'):
    row=inputs[mode];emit('choice_start',{'mode':mode});trials={}
    for kind in('P','O'):
     def tagged(stage,data):emit(stage,dict(data,kind=kind))
     s=A.new_inner(inner[kind],row['p'][kind],row['s0_s2'][kind],tagged);trials[kind]=A.choose(s,row['old_q'][kind],tagged)
    result=certificate.finish(row['p'],trials,jets,row['first_squared'],row['a_squared'],row['old_alpha'],emit);result['mode']=mode;atomic(out/(mode+'.json'),result);rows.append(result);emit('choice_complete',result)
   if {x['status']for x in rows}>={'POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'}:raise ValueError('contradictory signs')
   mode=None;emit('complete',{'rows':rows});atomic(out/'RESULT.json',{'status':'COMPLETE_NEW_DEGREE21_JET_CERTIFICATE','rows':rows,'choices':2,'jets':7,'events':seq,'serialized_event_bytes':total,'counts':counts,'native_oracle_calls':0,'old_native_moments_recomputed':0,'seconds':time.monotonic()-start})
  except BaseException as e:
   try:atomic(out/'FAILURE.json',{'error':repr(e),'current':current,'completed':rows,'seconds':time.monotonic()-start})
   except BaseException as err:e.add_note('retention '+repr(err))
   raise
