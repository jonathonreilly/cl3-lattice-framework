"""Future saved-only B66 panel/tail reconciliation; no integrand or oracle import."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
import json,hashlib,argparse
S=2**192

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def iv(x):return tuple(map(F,x))
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
 cfg=json.loads(Path(args.post_binding).read_text());checks=0
 def ck(x,m):
  nonlocal checks
  if not x:raise ValueError(m)
  checks+=1
 for p,h in cfg['files'].items():ck(sha(p)==h,'post-bound input '+p)
 study=Path(cfg['study']);bind=json.loads(Path(cfg['worker_binding_path']).read_text());summary=json.loads((study/'SUMMARY.json').read_text());complete=json.loads((study/'COMPLETE.json').read_text());ck(complete['summary_sha256']==sha(study/'SUMMARY.json'),'complete summary binding');ck(complete['worker_freeze']==cfg['worker_freeze'] and complete['binding_sha256']==sha(cfg['worker_binding_path']),'complete worker binding')
 required={str(study/'SUMMARY.json'),str(study/'COMPLETE.json'),str(Path(cfg['worker_binding_path'])),str(Path(bind['a66']['directory'])/'RESULT.json')}
 for j in range(11):
  d=study/f'SHARD_{j:02d}';required|={str(d/'RESULT.json'),str(d/'WORKER_COMPLETE.json')}|{str(d/f'PANELS/{k:02d}.json') for k in range(67)}
 ck(required<=set(cfg['files']),'complete read-input membership')
 arows=json.loads((Path(bind['a66']['directory'])/'RESULT.json').read_text())['rows'];M=[moment(n) for n in range(27)];allrows=[]
 # Same exact Machin32/10-term enclosure used by the frozen pi provider.
 def atan(q,n):
  x=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0));return(x,x+F(1,(2*n+1)*q**(2*n+1)))
 p5=atan(5,32);p239=atan(239,10);pi=(16*p5[0]-4*p239[1],16*p5[1]-4*p239[0]);factor=(2/pi[1],2/pi[0])
 for shard in range(11):
  d=study/f'SHARD_{shard:02d}';r=json.loads((d/'RESULT.json').read_text());w=json.loads((d/'WORKER_COMPLETE.json').read_text());ids=list(range(shard*6,shard*6+6));ck(r['selected_ids']==ids,'shard ids');ck(w['result_sha256']==sha(d/'RESULT.json'),'worker result')
  acc={i:[(F(0),F(0)),(F(0),F(0))] for i in ids}
  for j in range(-64,3):
   panel=json.loads((d/f'PANELS/{j+64:02d}.json').read_text());ck(panel['panel']==j,'panel index')
   for i in ids:
    for k in (0,1):
     x=iv(panel['values'][str(i)][k]);ck(x[0]<=x[1],'panel interval');acc[i][k]=add(acc[i][k],x);ck(acc[i][k]==iv(panel['cumulative'][str(i)][k]),'cumulative interval')
  for row,i in zip(r['rows'],ids):
   raw=arows[i]['oracle'];s=F(raw['s']);si=(s,s);ss=mul(si,si);a=iv(raw['A']);da=iv(raw['Aprime']);c=add((F(1),F(1)),neg(mul(a,ss)));e=add(scale(mul(si,a),2),mul(da,ss));tails=[(F(0),F(0)),(F(0),F(0))]
   for n in range(26):
    wt=F((-1)**n,(2*n+1)*8**(2*n+1));tails=[add(tails[0],scale(c,wt)),add(tails[1],scale(e,wt))];c,e=add((M[n+1],M[n+1]),neg(mul(c,ss))),add(scale(mul(si,c),2),neg(mul(e,ss)))
   rem=F(12**26,53*8**53);tails=[add(tails[0],(F(0),rem)),add(tails[1],(F(0),rem/3))];rad=F(400,27)*F(4,25)**26;low=F(1,3*2**64);answers=[]
   for k in (0,1):
    x=mul(add(add(acc[i][k],tails[k]),(-rad,rad+low)),factor);answers.append(neg(x) if k else x)
   ck(answers[0]==iv(row['B']) and answers[1]==iv(row['Bprime']),'saved final endpoints');widths=[x[1]-x[0] for x in answers];ck(widths==list(map(F,row['widths'])),'saved widths');ck(row['status']==('CERTIFIED_TARGET' if max(widths)<=F(2,10**19) else 'INDETERMINATE'),'fixed classification');allrows.append(row)
 ck(summary['rows']==allrows and len(allrows)==66,'all66 summary')
 out.write_text(json.dumps({'status':'PASS_SAVED_PANEL_TAIL_RECONCILIATION','checks':checks,'integrand_calls':0,'oracle_calls':0,'scope':'saved panel sums and final tail arithmetic only; individual panel integrands not recomputed','summary_sha256':sha(study/'SUMMARY.json')},indent=2)+'\n')
if __name__=='__main__':main()
