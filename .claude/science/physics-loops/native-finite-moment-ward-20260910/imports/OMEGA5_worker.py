import json,time,os
from fractions import Fraction as F
import loader,compute
from interval import add

def encode(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,(list,tuple)):return[encode(x)for x in v]
 if isinstance(v,dict):return{str(k):encode(x)for k,x in v.items()}
 return v
def atomic(path,data):
 temp=path.with_suffix(path.suffix+'.tmp')
 with temp.open('w')as f:json.dump(encode(data),f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
 temp.replace(path)
def run(binding,out):
 start=time.monotonic();current=None;stage='initial';panels=[];total=(F(0),F(0));six=(F(0),F(0));count=0
 def progress(s,data):
  nonlocal current,stage
  stage=s;current=data;atomic(out/'PARTIAL.json',{'stage':stage,'current':current,'completed_nodes':count,'panels':panels,'middle':total,'weighted_t6':six,'seconds':time.monotonic()-start})
 try:
  progress('binding',{});catalog=loader.load(binding,progress);(out/'PANELS').mkdir();(out/'NODES').mkdir()
  for panel in range(-64,3):
   subtotal=(F(0),F(0));nodes=catalog[(panel+64)*26:(panel+65)*26]
   if len(nodes)!=26:raise ValueError('panel census')
   for node in nodes:
    progress('node_before_arithmetic',{'id':node['id'],'panel':panel,'input':node})
    q,value,power=compute.node_value(node);subtotal=add(subtotal,value);six=add(six,power);count+=1
    record={'id':node['id'],'panel':panel,'input':node,'integrand':q,'weighted':value,'panel_cumulative':subtotal,'weighted_t6_cumulative':six}
    atomic(out/f'NODES/{node["id"]:04d}.json',record);progress('node_retained',{'id':node['id'],'panel':panel})
   total=add(total,subtotal);record={'panel':panel,'value':subtotal,'cumulative':total};atomic(out/f'PANELS/{panel+64:02d}.json',record);panels.append(panel);progress('panel_complete',record)
  progress('tails_before_computation',{});tail=compute.tails(progress);atomic(out/'TAIL.json',tail);progress('tails_retained',{'tail_terms':40})
  ans,pibox=compute.finish(total,tail);width=ans[1]-ans[0];middle_gate=total[1]-total[0]<=F(1,10**24);six_gate=six[1]<=300000
  raw={'interval':ans,'width':width,'middle':total,'weighted_t6':six,'pi_interval':pibox};atomic(out/'FINAL_ARITHMETIC.json',raw);progress('final_before_gates',raw)
  result={'observable':'omega5=E_X_power_5_over_2','status':'CERTIFIED_TARGET'if middle_gate and six_gate and width<=F(1,10**24)else'INDETERMINATE','target':F(1,10**24),'interval':ans,'width':width,'middle_width_gate':middle_gate,'weighted_t6_gate':six_gate,'middle':total,'weighted_t6':six,'panels':67,'nodes':1742,'endpoint_oracles_reused':3484,'oracle_calls':0,'new_quantity_integral':True,'tail_terms':40,'moments_count':41,'quadrature_radius':tail['quadrature_radius'],'seconds':time.monotonic()-start}
  if count!=1742:raise ValueError('node census')
  progress('complete',{'result':result});result['seconds']=time.monotonic()-start;atomic(out/'RESULT.json',result)
 except BaseException as e:
  try:atomic(out/'FAILURE.json',{'error':repr(e),'stage':stage,'current':current,'completed_nodes':count,'panels':panels,'middle':total,'seconds':time.monotonic()-start})
  except BaseException as er:e.add_note('retention '+repr(er))
  raise
