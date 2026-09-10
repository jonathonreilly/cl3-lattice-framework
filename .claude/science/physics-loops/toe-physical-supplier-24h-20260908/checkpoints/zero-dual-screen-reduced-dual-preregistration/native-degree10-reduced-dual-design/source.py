from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time,os,math
import interval as I


def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return[encode(v)for v in x]
 if isinstance(x,dict):return{k:encode(v)for k,v in x.items()}
 return x
def atomic(p,x):
 tmp=p.with_suffix(p.suffix+'.tmp')
 with tmp.open('w')as f:json.dump(encode(x),f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
 tmp.replace(p)
def schedule(count):
 from itertools import combinations
 labels=list(combinations(range(6),2));kind=lambda a:'O'if a[0]//2==a[1]//2 else'P'
 local=['vacuum_inputs']+['vacuum_moment_raw']*7+['first_polynomial','source_inputs']+['source_moment_raw']*3+['residual_raw']
 if count==205:local=['moments','polynomial','source_moments','residual_raw']
 elif count!=255:raise ValueError('fixed source count')
 stages=local*2;seen=set()
 for C in labels:
  for A in labels:
   if set(C)&set(A):continue
   kc,ka=kind(C),kind(A);ell=sum((2*k in C and 2*k+1 in A)or(2*k+1 in C and 2*k in A)for k in range(3));tag='PP'+str(ell)if kc==ka=='P'else kc+ka
   if count==255 and tag not in seen:stages.append('cross_wick_raw');seen.add(tag)
   stages.append('ordered_word')
 stages.append('gate_inputs');out=[('binding',None),('scalar_inputs',None)]
 for mode in ['residual','variational']:out += [('choice_start',mode)]+[(s,mode)for s in stages]+[('choice_complete',mode)]
 return out+[('complete',None)]

def load_family(spec,emit):
 def read(k):
  f=spec[k];emit('before_input',{'role':k});need(sha(f['path'])==f['sha256'],'input hash');return json.loads(Path(f['path']).read_text())
 a=read('acceptance');w=read('worker');rr=read('receipt');rf=read('root_freeze');r=read('result')
 need(a['status']==spec['accepted_status']and a['once']is True,'accepted status')
 need(a['result_sha256']==spec['result']['sha256']==w['result_sha256']and a['worker_freeze']==spec['worker_freeze']==w['runtime_sha256']==rr['worker_freeze']==rf['worker_freeze'],'producer chain')
 need(a['root_freeze']==spec['root_freeze']['sha256']and w['status']==spec['worker_status'],'producer freeze')
 need(rr['pass']is True and type(rr['returncode'])is int and rr['returncode']==0,'original completion')
 for v,cap in [(w['seconds'],19),(rr['seconds'],19.5),(a['external_seconds'],20)]:need(type(v)in(int,float)and math.isfinite(v)and 0<v<cap,'original timing')
 for v in [w['rss_bytes'],rr['sampled_whole_tree_peak'],a['external_rss_bytes'],a['sampled_whole_tree_peak']]:need(type(v)is int and 0<v<=384*1048576,'original RSS')
 need(r['status']==spec['result_status']and type(r['events'])is int and r['events']==spec['count']and type(r['choices'])is int and r['choices']==2,'original full completion')
 p=spec['events'];need(sha(p['path'])==p['sha256'],'events hash');ev=[]
 with Path(p['path']).open()as stream:
  for i,line in enumerate(stream,1):
   emit('before_source_event',{'index':i});e=json.loads(line);need(type(e['sequence'])is int and e['sequence']==i,'sequence');ev.append(e)
 need(len(ev)==spec['count'],'event census');need([(e['stage'],e['choice'])for e in ev]==schedule(spec['count']),'exact source chronology');return r,ev

def selected(events,stage,mode,kind=None):
 rows=[e['data']for e in events if e['stage']==stage and e['choice']==mode and(kind is None or e['data'].get('kind')==kind)]
 need(len(rows)==1,'unique '+stage);return rows[0]

