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
 start=time.monotonic();current=None;stage='initial';count=0;panels=[];totals={r:(F(0),F(0))for r in(3,4)};powers={r:(F(0),F(0))for r in(3,4)}
 def progress(s,data):
  nonlocal stage,current
  stage=s;current=data;atomic(out/'PARTIAL.json',{'stage':stage,'current':current,'completed_nodes':count,'panels':panels,'middle':totals,'weighted_power':powers,'seconds':time.monotonic()-start})
 try:
  progress('binding',{});m=loader.reused_moments(binding,progress);atomic(out/'REUSED_MOMENTS.json',m)
  for k in(44,45):
   progress('before_new_moment',{'index':k});m[k]=compute.moment(k);atomic(out/f'M{k}.json',{'index':k,'value':m[k]});progress('new_moment_retained',{'index':k})
  catalog=loader.load(binding,progress);(out/'PANELS').mkdir();(out/'NODES').mkdir()
  for panel in range(-64,3):
   subtotal={r:(F(0),F(0))for r in(3,4)};nodes=catalog[(panel+64)*26:(panel+65)*26]
   if len(nodes)!=26:raise ValueError('panel census')
   for node in nodes:
    progress('node_before_arithmetic',{'id':node['id'],'panel':panel,'input':node});vals={}
    for r in(3,4):
     progress('observable_before_arithmetic',{'id':node['id'],'r':r});q,v,p=compute.node_value(node,r,m);subtotal[r]=add(subtotal[r],v);powers[r]=add(powers[r],p);vals[r]={'integrand':q,'weighted':v,'panel_cumulative':subtotal[r],'weighted_power_cumulative':powers[r]}
     atomic(out/'CURRENT_ARITHMETIC.json',{'id':node['id'],'r':r,'values':vals})
    count+=1;atomic(out/f'NODES/{node["id"]:04d}.json',{'id':node['id'],'panel':panel,'input':node,'values':vals});progress('node_retained',{'id':node['id'],'panel':panel})
   for r in(3,4):totals[r]=add(totals[r],subtotal[r])
   record={'panel':panel,'value':subtotal,'cumulative':totals};atomic(out/f'PANELS/{panel+64:02d}.json',record);panels.append(panel);progress('panel_complete',record)
  rows=[]
  for r,target,cap in[(3,F(1,10**22),15000000),(4,F(1,10**20),800000000)]:
   progress('before_tails',{'r':r});tail=compute.tails(r,m,progress);atomic(out/f'TAIL{2*r+1}.json',tail)
   ans,pibox=compute.finish(totals[r],tail);width=ans[1]-ans[0];mg=totals[r][1]-totals[r][0]<=target;pg=powers[r][1]<=cap
   raw={'r':r,'interval':ans,'width':width,'middle':totals[r],'weighted_power':powers[r],'pi_interval':pibox};atomic(out/f'FINAL{2*r+1}.json',raw);progress('final_before_gates',raw)
   rows.append({'observable':f'omega{2*r+1}','status':'CERTIFIED_TARGET'if mg and pg and width<=target else'INDETERMINATE','target':target,'interval':ans,'width':width,'middle_width_gate':mg,'weighted_power_gate':pg,'quadrature_radius':tail['quadrature_radius']})
  if count!=1742:raise ValueError('node census')
  result={'status':'COMPLETE_NEW_OMEGA79','rows':rows,'nodes':1742,'panels':67,'endpoint_oracles_reused':3484,'oracle_calls':0,'reused_moments':41,'new_moments':[44,45],'tail_terms_each':40,'seconds':time.monotonic()-start};progress('complete',{'result':result});atomic(out/'RESULT.json',result)
 except BaseException as e:
  try:atomic(out/'FAILURE.json',{'error':repr(e),'stage':stage,'current':current,'completed_nodes':count,'panels':panels,'seconds':time.monotonic()-start})
  except BaseException as er:e.add_note('retention '+repr(er))
  raise
