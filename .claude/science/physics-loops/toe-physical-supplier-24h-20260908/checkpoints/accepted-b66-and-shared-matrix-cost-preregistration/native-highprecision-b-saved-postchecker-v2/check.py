"""Future saved-only B66 panel/tail reconciliation; no integrand or oracle import."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
import json,hashlib,argparse,math
S=2**192

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def iv(x):
 if not isinstance(x,list) or len(x)!=2:raise ValueError('two interval endpoints')
 a,b=map(F,x)
 if a>b:raise ValueError('ordered interval')
 return a,b
def rnd(a,b):return(F((a*S).__floor__(),S),F((b*S).__ceil__(),S))
def add(a,b):return rnd(a[0]+b[0],a[1]+b[1])
def mul(a,b):
 v=[x*y for x in a for y in b];return rnd(min(v),max(v))
def neg(a):return(-a[1],-a[0])
def scale(a,b):return mul(a,(F(b),F(b)))
def moment(n):return sum(F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1) for b in range(n-a+1))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('post_binding');ap.add_argument('output');args=ap.parse_args();out=Path(args.output)
 if out.exists():raise ValueError('fresh post output')
 cfg=json.loads(Path(args.post_binding).read_text());checks=0;stage='inputs';allrows=[]
 def progress(error=None):
  out.with_name('PARTIAL.json').write_text(json.dumps({'stage':stage,'completed_rows':allrows,'checks':checks,'error':error},indent=2)+'\n')
 def ck(x,m):
  nonlocal checks
  if not x:raise ValueError(m)
  checks+=1
 try:
  for p,h in cfg['files'].items():ck(sha(p)==h,'post-bound input '+p)
  def read(p):
   p=str(Path(p));ck(p in cfg['files'],'declared read '+p);ck(sha(p)==cfg['files'][p],'bound read '+p);return json.loads(Path(p).read_text())
  study=Path(cfg['study']);bind=read(cfg['worker_binding_path']);summary=read(study/'SUMMARY.json');complete=read(study/'COMPLETE.json');ck(complete['summary_sha256']==sha(study/'SUMMARY.json'),'complete summary binding');ck(complete['worker_freeze']==cfg['worker_freeze'] and complete['binding_sha256']==sha(cfg['worker_binding_path']),'complete worker binding')
  ck(complete['status']=='COMPLETE_FIXED_11_SHARDS' and summary['status']=='COMPLETE_FIXED_11_SHARDS','study status')
  ck(summary['matrix_computed'] is False and summary['pairs']==114972 and summary['resource_acceptance_not_checked_here'] is True,'summary scope')
  ck(complete['original_scope']=='B66 midpoint scalar contractions only','complete scope')
  acceptance=read(cfg['root_acceptance_path']);ck(acceptance['status']=='ACCEPTED_EXECUTION_COMPLETE' and acceptance['summary_sha256']==sha(study/'SUMMARY.json') and acceptance['worker_freeze']==cfg['worker_freeze'],'root accepted summary')
  ck(acceptance['complete_sha256']==sha(study/'COMPLETE.json') and acceptance['binding_sha256']==sha(cfg['worker_binding_path']) and acceptance['poles']==66 and acceptance['shards']==11 and acceptance['no_retry'] is True,'root complete binding')
  ck(all(math.isfinite(acceptance[k]) and 0<acceptance[k]<=cap for k,cap in [('external_shell_seconds',1200),('external_max_rss',384*1048576),('sampled_whole_tree_peak',384*1048576)]),'root resources')
  ck(sha(Path(bind['a66']['directory'])/'RESULT.json')==bind['a66']['result_sha256'],'original A66 binding')
  required={str(study/'SUMMARY.json'),str(study/'COMPLETE.json'),str(Path(cfg['worker_binding_path'])),str(Path(bind['a66']['directory'])/'RESULT.json')}
  for j in range(11):
   d=study/f'SHARD_{j:02d}';required|={str(d/'RESULT.json'),str(d/'WORKER_COMPLETE.json'),str(d/'PARTIAL.json')}|{str(d/f'POLES/{i:02d}.json') for i in range(6*j,6*j+6)}|{str(d/f'PANELS/{k:02d}.json') for k in range(67)}
  ck(required<=set(cfg['files']),'complete read-input membership')
  arows=read(Path(bind['a66']['directory'])/'RESULT.json')['rows'];ck([a['id'] for a in arows]==list(range(66)),'A66 ids');M=[moment(n) for n in range(27)]
  # Same exact Machin32/10-term enclosure used by the frozen pi provider.
  def atan(q,n):
   x=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0));return(x,x+F(1,(2*n+1)*q**(2*n+1)))
  p5=atan(5,32);p239=atan(239,10);pi=(16*p5[0]-4*p239[1],16*p5[1]-4*p239[0]);factor=(2/pi[1],2/pi[0])
  for shard in range(11):
   d=study/f'SHARD_{shard:02d}';r=read(d/'RESULT.json');w=read(d/'WORKER_COMPLETE.json');ids=list(range(shard*6,shard*6+6));ck(r['selected_ids']==ids,'shard ids');ck(w['result_sha256']==sha(d/'RESULT.json'),'worker result')
   stage='shard_'+str(shard);progress()
   ck(w['status']=='COMPLETE' and w['shard']==shard and w['freeze_sha256']==cfg['worker_freeze'] and w['binding_sha256']==sha(cfg['worker_binding_path']),'worker source/binding')
   ck(r['status']=='COMPLETE_FIXED_CASES' and len(r['rows'])==6 and [x['id'] for x in r['rows']]==ids and r['pairs']==10452,'six fixed rows')
   ck(r['matrix_computed'] is False and r['alpha_computed'] is False and r['exact_gauss_root_values'] is False and r['midpoint_displacement_requires_separate_ledger'] is True,'shard scope')
   ck(all(isinstance(t,(int,float)) and math.isfinite(t) and t>0 for t in [r['seconds'],w['seconds']]) and r['seconds']<=w['seconds']<=180,'worker timings')
   partial=read(d/'PARTIAL.json');ck(partial['rows']==r['rows'] and partial['stage']=='finish' and partial['current']=={'pole':ids[-1]} and partial['completed_panels']==[{'panel':j,'path':f'PANELS/{j+64:02d}.json'} for j in range(-64,3)],'partial retained')
   acc={i:[(F(0),F(0)),(F(0),F(0))] for i in ids}
   for j in range(-64,3):
    panel=read(d/f'PANELS/{j+64:02d}.json');ck(panel['panel']==j,'panel index')
    stage=f'shard_{shard}_panel_{j}';progress();ck(set(panel['values'])==set(panel['cumulative'])==set(map(str,ids)),'panel exact keys')
    for i in ids:
     ck(len(panel['values'][str(i)])==len(panel['cumulative'][str(i)])==2,'two panel observables')
     for k in (0,1):
      x=iv(panel['values'][str(i)][k]);ck(x[0]<=x[1],'panel interval');acc[i][k]=add(acc[i][k],x);ck(acc[i][k]==iv(panel['cumulative'][str(i)][k]),'cumulative interval')
   for row,i in zip(r['rows'],ids):
    stage='pole_'+str(i);progress();ck(F(row['target'])==F(2,10**19) and len(row['widths'])==len(row['B'])==len(row['Bprime'])==2,'fixed target/shape');ck(read(d/f'POLES/{i:02d}.json')==row,'retained pole');raw=arows[i]['oracle'];ck(F(row['s_midpoint'])==F(raw['s']),'row midpoint');s=F(raw['s']);si=(s,s);ss=mul(si,si);a=iv(raw['A']);da=iv(raw['Aprime']);c=add((F(1),F(1)),neg(mul(a,ss)));e=add(scale(mul(si,a),2),mul(da,ss));tails=[(F(0),F(0)),(F(0),F(0))]
    for n in range(26):
     wt=F((-1)**n,(2*n+1)*8**(2*n+1));tails=[add(tails[0],scale(c,wt)),add(tails[1],scale(e,wt))];c,e=add((M[n+1],M[n+1]),neg(mul(c,ss))),add(scale(mul(si,c),2),neg(mul(e,ss)))
    rem=F(12**26,53*8**53);tails=[add(tails[0],(F(0),rem)),add(tails[1],(F(0),rem/3))];rad=F(400,27)*F(4,25)**26;low=F(1,3*2**64);answers=[]
    for k in (0,1):
     x=mul(add(add(acc[i][k],tails[k]),(-rad,rad+low)),factor);answers.append(neg(x) if k else x)
    ck(answers[0]==iv(row['B']) and answers[1]==iv(row['Bprime']),'saved final endpoints');widths=[x[1]-x[0] for x in answers];ck(widths==list(map(F,row['widths'])),'saved widths');ck(row['status']==('CERTIFIED_TARGET' if max(widths)<=F(2,10**19) else 'INDETERMINATE'),'fixed classification');allrows.append(row)
  ck(all([r['status']=='CERTIFIED_TARGET' for r in allrows])==summary['all_targets_met']==complete['all_targets_met'],'target summaries')
  ck(summary['rows']==allrows and len(allrows)==66,'all66 summary')
  out.write_text(json.dumps({'status':'PASS_SAVED_PANEL_TAIL_RECONCILIATION','checks':checks,'integrand_calls':0,'oracle_calls':0,'scope':'saved panel sums and final tail arithmetic only; individual panel integrands not recomputed','summary_sha256':sha(study/'SUMMARY.json')},indent=2)+'\n')
 except BaseException as e:
  progress(repr(e));out.write_text(json.dumps({'status':'FAILED_SAVED_POSTCHECK','stage':stage,'rows':allrows,'checks':checks,'error':repr(e)},indent=2)+'\n');raise
if __name__=='__main__':main()
