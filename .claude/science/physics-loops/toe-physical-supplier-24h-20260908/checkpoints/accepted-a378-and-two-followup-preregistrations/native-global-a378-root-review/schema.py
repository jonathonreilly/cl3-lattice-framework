"""Independent structural/interval checks for a new378 A acquisition; import is inert."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math,re

def req(x,m):
 if not x:raise ValueError(m)
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def integer(x,m):req(type(x)is int,m);return x
def scalar(x):
 req(type(x)is str and len(x)<=40000 and re.fullmatch(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?',x) is not None,'rational encoding')
 v=F(x);req(str(v)==x,'canonical rational');req(max(v.numerator.bit_length(),v.denominator.bit_length())<=50000,'rational bits');return v
def interval(x):
 req(type(x)is list and len(x)==2,'interval shape');a,b=map(scalar,x);req(a<=b,'interval ordering');return a,b
def seconds(x):req(type(x)in(int,float) and math.isfinite(x) and 0<x<179,'finite seconds');return x

def check(out,root,elapsed,progress):
 out=Path(out);nodes=json.loads((out/'NODES.json').read_text());req(integer(nodes['count'],'node count')==378 and len(nodes['rows'])==378,'378 nodes')
 refs=[];previous=None;weight_sum=[F(0),F(0)];panels={};rule={}
 for i,n in enumerate(nodes['rows']):
  j,k=divmod(i,21);j-=16;req(integer(n['id'],'node id')==i and integer(n['panel'],'panel')==j and integer(n['root'],'root')==k,'fixed ordering')
  sl,sh=interval(n['s_interval']);wl,wh=interval(n['weight_interval']);sm=scalar(n['s']);wm=scalar(n['weight']);a=F(4)**j
  req(a<sl<=sh<4*a and 0<wl<=wh,'positive geometry');req(sm==(sl+sh)/2 and wm==(wl+wh)/2,'midpoints');req(sh-sl<=F(1,2**160) and wh-wl<=F(1,2**160),'geometry width')
  if previous is not None:req(previous<sl,'disjoint ordered poles')
  previous=sh;weight_sum[0]+=wl;weight_sum[1]+=wh;panels.setdefault(j,[F(0),F(0)]);panels[j][0]+=wl;panels[j][1]+=wh
  x=(F(2)*sl/(3*a)-F(5,3),F(2)*sh/(3*a)-F(5,3));w=(F(2)*wl/(3*a),F(2)*wh/(3*a))
  if k in rule:req(rule[k]==(x,w),'same exact mapped rule')
  else:rule[k]=(x,w)
  refs.append(n)
 for j,(l,h)in panels.items():req(l<=3*F(4)**j<=h,'panel weight sum')
 req(weight_sum[0]<=16-F(1,2**32)<=weight_sum[1],'total weight sum')
 req(rule[10][0]==(F(0),F(0)),'central zero')
 for k in range(10):req(rule[k][0]==tuple(-v for v in reversed(rule[20-k][0])) and rule[k][1]==rule[20-k][1],'symmetric rule')
 events=[json.loads(l)for l in(out/'ROOT_PROGRESS.jsonl').read_text().splitlines()];req(len(events)==37 and events[0]=={'stage':'scan_start','grid_intervals':2048},'full geometry events');
 for i,j in enumerate(range(128,2049,128),1):req(events[i]=={'stage':'scan','grid_index':j},'scan schedule')
 for i in range(10):
  pre,post=events[17+2*i:19+2*i];req(pre['stage']=='before_root' and post['stage']=='root' and integer(pre['index'],'before root index')==i and integer(post['index'],'root index')==i,'root event schedule');lo,hi=interval(pre['bracket']);a,b=interval(post['bracket']);req(0<lo<=a<=b<=hi<1 and hi-lo==F(1,2048),'initial bracket contains final')
 completed=[x for x in events if x.get('stage')=='root'];req(len(completed)==10,'ten completed positive roots')
 for i,e in enumerate(completed):req(integer(e['index'],'root index')==i and interval(e['bracket'])==rule[11+i][0],'progress root binding')
 result=json.loads((out/'RESULT.json').read_text());req(result['status']=='COMPLETE' and result['scope']=='A-only378scalar acquisition','result scope');req(integer(result['count'],'result count')==378 and len(result['rows'])==378,'result census');seconds(result['seconds']);flags=[]
 for i,n in enumerate(refs):
  raw=json.loads((out/f'RAW_{i:03d}.json').read_text());req(integer(raw['id'],'raw id')==i,'raw order');seconds(raw['seconds']);r=raw['raw'];al,ah=interval(r['A']);dl,dh=interval(r['Aprime']);req(0<al<=ah and dl<=dh<=0,'scalar signs');req(scalar(r['s'])==scalar(n['s']) and integer(r['terms'],'terms')==160,'oracle point and terms');req(list(map(scalar,r['widths']))==[ah-al,dh-dl],'declared widths')
  target=ah-al<=F(1,10**30);flag=result['rows'][i]['target_met'];req(type(flag)is bool and flag==target,'target truth');expected=dict(raw,target_met=target);req(result['rows'][i]==expected,'original raw copy');flags.append(target)
  if i%21==20:progress({'stage':'schema_scalar','completed':i+1})
 req(type(result['all_targets_met'])is bool and result['all_targets_met']==all(flags),'all target flag')
 partial=json.loads((out/'PARTIAL.json').read_text());req(partial['current']=={'stage':'retained','id':377} and type(partial['completed'])is int and partial['completed']==378 and partial['target_met']is flags[-1],'final partial')
 expected={f'RAW_{i:03d}.json'for i in range(378)};req({p.name for p in out.iterdir()}==expected|{'NODES.json','RESULT.json','PARTIAL.json','WORKER_COMPLETE.json','ROOT_PROGRESS.jsonl'},'exact output membership');req({p.name for p in out.glob('RAW_*.json')}==expected,'exact raw membership')
 complete=json.loads((out/'WORKER_COMPLETE.json').read_text());req(complete['status']=='COMPLETE','completion status');req(result['seconds']<=complete['seconds'],'result within worker time');req(sum(x['seconds'] for x in result['rows'])<=result['seconds'],'scalar times within result');req(complete['result_sha256']==digest(out/'RESULT.json') and complete['nodes_sha256']==digest(out/'NODES.json'),'worker final bindings')
 req(complete['freeze_sha256']==root['worker_freeze'],'worker runtime binding');seconds(complete['seconds']);req(type(complete['rss_bytes'])is int and 0<complete['rss_bytes']<=384*1048576,'worker final RSS')
 return {'status':'ACCEPTED_NEW_A378_SCHEMA','all_targets_met':all(flags),'count':378,'scope':'New geometry and A scalar acquisition; native scalar containment inherits reviewed oracle; operator T/pi assembly and consumer remain open','result_sha256':digest(out/'RESULT.json'),'nodes_sha256':digest(out/'NODES.json'),'raw_sha256':{f'RAW_{i:03d}.json':digest(out/f'RAW_{i:03d}.json')for i in range(378)},'seconds_before_schema':elapsed,'independent_native_oracle_replay':False}
