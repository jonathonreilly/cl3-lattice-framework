"""Saved-only postcheck; never imports any oracle or physical worker."""
import argparse,json,hashlib,math,re,signal
from pathlib import Path
from fractions import Fraction as F

def pi_bounds():
 def atan(q):
  a=sum((F((-1)**n,(2*n+1)*q**(2*n+1)) for n in range(64)),F(0));return a,a+F(1,129*q**129)
 a,b=atan(5);c,d=atan(239);return 16*a-4*d,16*b-4*c

def consistency(s,A,Ap,A0,pi):
 l,u=pi;lo,hi=A;dl,du=Ap
 ordinary=max(lo,1/(s*s+6))<=min(hi,F(17,60),1/(s*s))
 if s>1:return ordinary,None
 ir=(A0[0]-s/(4*l)-(1+1/(12*l*l))*s*s,A0[1]-s/(4*u)+s*s/(2*l*l))
 e=(2+F(7,6)/(l*l))*s;dip=(-1/(4*l)-e,-1/(4*u)+e)
 return ordinary,(max(lo,ir[0])<=min(hi,ir[1]),max(dl,dip[0])<=min(du,dip[1]))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--result-sha256',required=True);args=ap.parse_args();signal.alarm(25)
 s=Path('/private/tmp/toe-24h-probes-20260908');p=s/'native-highprecision-b-catalog-design';o=s/'native-highprecision-b-catalog-run-c6430';r=s/'native-highprecision-b-catalog-root-review';checks=0
 def req(x,label):
  nonlocal checks
  if not x:raise ValueError(label)
  checks+=1
 def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
 local=Path(__file__).parent;inputs=json.loads((local/'INPUT_PINS.json').read_text())
 for name,h in inputs.items():req(sha(Path(name))==h,'review input '+name)
 req(sha(o/'RESULT.json')==args.result_sha256,'authorized result hash')
 f=json.loads((p/'FREEZE.json').read_text())
 for name,h in f['inputs'].items():req(sha(Path(name))==h,'source pin '+name)
 d=json.loads((o/'RESULT.json').read_text());w=json.loads((o/'WORKER_COMPLETE.json').read_text());root=json.loads((r/'RECEIPT.json').read_text());g=json.loads((p/'CATALOG_GEOMETRY.json').read_text());ps=json.loads((s/'native-stationary-pole-scalar-batch-design/POLES.json').read_text())['rows']
 req(w['status']=='COMPLETE' and w['result_sha256']==args.result_sha256 and w['freeze_sha256']==sha(p/'FREEZE.json'),'worker complete binding')
 req(d['status']=='COMPLETE_FIXED_3484_CATALOG' and d['oracle_count']==3484 and all(d[k] is False for k in ('B_computed','matrix_computed','alpha_computed','A66_results_bound')),'scope')
 req(len(d['rows'])==len(g['endpoints'])==3484 and len(g['nodes'])==1742,'census')
 a0path=s/'native-elliptic-green-run-6d85f/RESULT.json';a0result=json.loads(a0path.read_text());a0root=json.loads((s/'native-elliptic-green-root-review/ROOT_ACCEPTANCE.json').read_text());req(a0root['result_sha256']==sha(a0path),'A0 acceptance');a0rows=[x for x in a0result['rows'] if x['s']=='0'];req(len(a0rows)==1,'unique A0');A0=tuple(map(F,a0rows[0]['A']));pi=pi_bounds();small=0;names=set();rowtime=0
 for n,node in enumerate(g['nodes']):
  req((node['id'],node['panel'],node['root'])==(n,n//26-64,n%26),'geometry order');lo,hi=map(F,node['t_interval']);req(0<lo<hi and node['endpoint_ids']==[2*n,2*n+1],'node bracket')
  distances=[max(lo-F(pp['s_interval'][1]),F(pp['s_interval'][0])-hi) for pp in ps];req(min(distances)>0 and min(distances)==F(node['minimum_stationary_separation']),'all66 separation')
 for i,(row,end) in enumerate(zip(d['rows'],g['endpoints'])):
  name=f'ORACLES/{i:04d}.json';names.add(f'{i:04d}.json');req(row['id']==i and row['path']==name and row['gate']=='PASS','row identity');req(sha(o/name)==row['sha256'],'raw hash');a=json.loads((o/name).read_text());req(a['catalog_endpoint']==end and a['s']==end['s'] and end['id']==i and end['node_id']==i//2 and end['side']==('lower' if i%2==0 else 'upper'),'endpoint identity');req(F(end['s'])==F(g['nodes'][i//2]['t_interval'][i%2]),'endpoint bracket side')
  req(a['status']=='CERTIFIED_TARGET' and a['terms']==160 and a['derivative_side']=='ordinary' and len(a['widths'])==2,'oracle schema')
  vals=[]
  for key,width in zip(('A','Aprime'),a['widths']):
   req(len(a[key])==2,'interval shape');l,u=map(F,a[key]);req(0<=u-l==F(width)<=F(1,10**30),'fixed precision');req(l>0 if key=='A' else u<0,'sign');vals.append((l,u))
  ok,ir=consistency(F(a['s']),vals[0],vals[1],A0,pi);req(ok,'native Jensen/upper consistency')
  if ir is not None:small+=1;req(ir[0],'native IR A consistency');req(ir[1],'native IR derivative consistency')
  t=row['seconds'];req(isinstance(t,(int,float)) and math.isfinite(t) and 0<t<=d['seconds'] and t==a['seconds'],'actual time');rowtime+=t
 req({x.name for x in (o/'ORACLES').iterdir()}==names,'raw file membership');partial=json.loads((o/'PARTIAL.json').read_text());req(partial['stage']=='complete' and partial['completed_rows']==3484 and partial['current']==g['endpoints'][-1] and partial['last_retained_row']==d['rows'][-1],'last partial retention')
 req(root['pass'] is True and root['failure'] is None and root['returncode']==0 and root['worker_freeze']==sha(p/'FREEZE.json'),'root completion')
 for t in [d['seconds'],w['seconds'],root['seconds']]:req(isinstance(t,(int,float)) and math.isfinite(t) and 0<t<180,'finite positive totals')
 req(rowtime<=d['seconds']<=w['seconds']<=root['seconds'],'nested accounting')
 text=(r/'ROOT.stderr').read_text();times=re.findall(r'^real\s+(\d+(?:\.\d+)?)$',text,re.M);rss=re.findall(r'^\s*(\d+)\s+maximum resident set size$',text,re.M);req(len(times)==len(rss)==1,'external receipt schema');sec=F(times[0])+F(1,100);req(0<sec<=180 and root['seconds']<=float(sec),'whole external time')
 for mem in [int(rss[0]),w['rss_bytes'],root['sampled_whole_tree_peak']]:req(isinstance(mem,int) and 0<mem<=384*1048576,'RSS')
 print(json.dumps({'status':'PASS_SAVED_CATALOG_AND_NATIVE_CONSISTENCY','checks':checks,'rows':3484,'small_s_rows':small,'result_sha256':args.result_sha256,'external_conservative_seconds':str(sec),'sampled_tree_peak':root['sampled_whole_tree_peak'],'oracle_calls':0,'scope':'containment consistency, not an independent elliptic containment proof; original method proof remains load-bearing'},indent=2))
if __name__=='__main__':main()
