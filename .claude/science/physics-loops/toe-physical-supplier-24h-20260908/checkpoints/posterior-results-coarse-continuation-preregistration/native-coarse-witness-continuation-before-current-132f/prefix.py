"""Saved-prefix authentication only; original native adapter truth is inherited."""
from pathlib import Path
from fractions import Fraction as F
import json,math
from binder import sha

def req(x,m):
 if not x:raise ValueError(m)
def q(x):
 req(type(x)is str and len(x)<20000,'rational type/size');v=F(x)
 req(str(v)==x and max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=32768,'canonical rational cap');return v
def matrix(a,n,m):
 req(type(a)is list and len(a)==n,'matrix rows');out=[]
 for row in a:
  req(type(row)is list and len(row)==m,'matrix columns');r=[]
  for p in row:
   req(type(p)is list and len(p)==2,'interval shape');lo,hi=map(q,p);req(lo<=hi,'interval order');r.append((lo,hi))
  out.append(r)
 return out
def case(row,block,i):
 req(type(row)is dict and set(row)=={'squared_block_lower','excludes_tau_1e9','status','stored_operator','metric_and_tail_charged','orbit','impurity'},'case keys')
 req(type(row['orbit'])is int and row['orbit']==i//2 and type(row['impurity'])is int and row['impurity']==i%2+1,'case labels')
 req(type(row['excludes_tau_1e9'])is bool and row['metric_and_tail_charged']is True and row['stored_operator']=='minus_i_times_positive_projector_difference','case scope')
 n=sum((lo if lo>0 else hi if hi<0 else F(0))**2 for r in block for lo,hi in r)
 rad=sum(((hi-lo)/2)**2 for r in block for lo,hi in r);flag=rad<=F(11,10**5)**2 and n>=F(11,500)**2
 req(q(row['squared_block_lower'])==n and row['excludes_tau_1e9']is flag,'case gates')
 req(row['status']==('EXCLUDED_BY_COARSE_WITNESS'if flag else'INDETERMINATE_COARSE_WITNESS'),'case status')
def grammar(events,cases,plan,emit):
 req(len(events)==76 and len(cases)==3,'fixed prefix census');ts=[];j=0;resume={}
 def take(stage,ci):
  nonlocal j
  emit('before_prefix_record',{'index':j});e=events[j];j+=1
  req(type(e)is dict and set(e)=={'current','data'},'event keys');cur=e['current']
  req(type(cur)is dict and set(cur)=={'stage','case'} and cur['stage']==stage and type(cur['case'])is int and cur['case']==ci,'prefix chronology')
  req(type(e['data'])is dict,'event data');return e['data']
 for oi in range(5):
  d=take('mapped_T',0);req(set(d)=={'orbit','source_sha256','mapped','operator_squared_upper'},'mapped keys')
  req(type(d['orbit'])is int and d['orbit']==oi and d['source_sha256']==plan['files']['T_'+str(oi)]['sha256'],'mapped source')
  req(0<q(d['operator_squared_upper'])<=10**8,'inherited norm premise');ts.append(matrix(d['mapped'],48,48))
 for ci in range(4):
  d=take('factorization',ci);req(set(d)=={'local','projector_columns'},'factor keys')
  local=matrix(d['local'],7,48);pc=matrix(d['projector_columns'],48,7)
  for completed in range(21,379 if ci<3 else 211,21):
   d=take('witness_panel',ci);req(set(d)=={'completed','direct','mixed'} and type(d['completed'])is int and d['completed']==completed,'panel census')
   direct=matrix(d['direct'],7,7);mixed=matrix(d['mixed'],7,7)
  if ci<3:
   d=take('witness_block',ci);req(set(d)=={'block'},'block keys');case(cases[ci],matrix(d['block'],7,7),ci)
  else:resume={'local':local,'projector_columns':pc,'direct':direct,'mixed':mixed}
 req(j==76,'prefix exhaustion');return ts,resume

def load(plan,emit):
 p=plan['prefix'];receipt=Path(p['receipt']['path']);req(sha(receipt)==p['receipt']['sha256'],'failure receipt hash');a=json.loads(receipt.read_text())
 req(a['status']=='FAILED_ONCE_TIME_CAP_PRESERVED' and a['worker_freeze']==p['worker_freeze'] and a['root_freeze']==p['root_freeze'],'failed source binding')
 req(type(a['returncode'])is int and a['returncode']==-9 and 'root deadline'in a['root_failure'],'failed cap disposition')
 req(type(a['external_seconds'])in(int,float)and math.isfinite(a['external_seconds'])and 0<a['external_seconds']<=300,'failed time')
 for key in ('external_rss_bytes','sampled_whole_tree_peak'):req(type(a[key])is int and 0<a[key]<=384*1048576,'failed RSS')
 req(a['whole_witness_certified']is False and a['partial_cases_independently_accepted']is False,'no old success')
 req(type(a['completed_case_files'])is int and a['completed_case_files']==3 and type(a['retained_event_lines'])is int and a['retained_event_lines']==76 and a['last_panel_metadata']==['witness_panel','3','210'],'receipt prefix')
 req(a['outputs']==p['outputs'],'receipt outputs');folder=Path(p['output'])
 req(sorted(x.name for x in folder.iterdir())==sorted(p['outputs']),'old output membership')
 for name,h in p['outputs'].items():req(sha(folder/name)==h,'prefix file hash '+name)
 # Parse only after all receipt/source hashes; keep source files immutable.
 data=(folder/'BLOCKS.jsonl').read_bytes();events=[json.loads(x)for x in data.splitlines()]
 cases=[json.loads((folder/('CASE_%02d.json'%i)).read_text())for i in range(3)]
 ts,resume=grammar(events,cases,plan,emit)
 for name,h in p['outputs'].items():req(sha(folder/name)==h,'post-prefix file hash '+name)
 return cases,ts,resume,data
