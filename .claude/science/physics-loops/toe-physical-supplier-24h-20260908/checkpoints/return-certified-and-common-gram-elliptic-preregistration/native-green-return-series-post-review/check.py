import time,signal,resource,json,hashlib,math,re
from pathlib import Path
from fractions import Fraction as F
from math import comb
start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('25s independent replay')));signal.alarm(25)
B=Path('/private/tmp/toe-24h-probes-20260908');P=B/'native-green-return-series-stretch';R=B/'native-green-return-series-root-review';O=B/'native-green-return-series-run-4ec20';D=Path(__file__).resolve().parent
count=0;stage='pins';completed=[]
def need(ok,msg):
 global count
 count+=1
 if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(n,d):(D/n).write_text(json.dumps(d,indent=2)+'\n')
try:
 pf='4ec2098e333aed49e74f99d7fe247c116774ecad6c66360dd0bed13f1102dcac';need(sha(P/'FREEZE.json')==pf,'freeze')
 pins=json.loads((P/'FREEZE.json').read_text())['inputs']
 for k,v in pins.items():need(sha(k)==v,k)
 data=json.loads((O/'RESULT.json').read_text());done=json.loads((O/'WORKER_COMPLETE.json').read_text());receipt=json.loads((R/'RECEIPT.json').read_text())
 need(done['freeze_sha256']==pf and done['result_sha256']==sha(O/'RESULT.json'),'completion')
 expected=[('1','1/1000000',55),('1','1/1000000000000',101),('2','1/1000000',15),('2','1/1000000000000',29),('1/2','1/1000000',232),('1/2','1/1000000000000',408)]
 need([(r['s'],r['target'],r['terms']) for r in data['rows']]==expected,'coverage')
 # Separate one axis: T_j=(2n)!(2n-2j)!/[j!²(n-j)!⁴].
 # T_0=binom(2n,n)^2; T_(j+1)/T_j=(n-j)^4/[(j+1)^2(2n-2j)(2n-2j-1)].
 stage='coefficient recurrence';cs=[]
 for n in range(408):
  term=comb(2*n,n)**2;c=term
  for j in range(n):
   l=n-j;num=term*l**4;den=(j+1)**2*(2*l)*(2*l-1)
   term,rem=divmod(num,den);need(rem==0,'integer axis allocation');c+=term
  cs.append(c)
 # Fixed finite sums only: independent Horner evaluation in q^-2.
 for row in data['rows']:
  stage='row '+row['s']+':'+row['target'];s=F(row['s']);q=s*s+6;r=36/q**2;m=row['terms'];x=1/q**2
  a=d=F(0)
  for n in range(m-1,-1,-1):a=a*x+cs[n];d=d*x+(2*n+1)*cs[n]
  a/=q;d*=2*s/q**2
  ta=r**m/(q*(1-r));td=2*s/q**2*r**m*((2*m+1)-(2*m-1)*r)/(1-r)**2
  need(list(map(F,row['A']))==[a,a+ta],'A');need(list(map(F,row['Aprime']))==[-d-td,-d],'Aprime')
  need(list(map(F,row['widths']))==[ta,td] and max(ta,td)<=F(row['target']),'tail and target')
  need(row['status']=='CERTIFIED_TARGET','row status');completed.append(stage);write('PARTIAL_REVIEW.json',{'stage':stage,'completed':completed})
 need(json.loads((O/'PARTIAL.json').read_text())['rows']==data['rows'],'saved final partial')
 need(receipt['pass'] and receipt['returncode']==0 and receipt['failure'] is None,'root')
 ts=[v['seconds'] for v in data['rows']]+[data['seconds'],done['seconds'],receipt['seconds']]
 need(all(math.isfinite(t) and t>0 for t in ts),'times');need(sum(ts[:6])<=ts[6]<=ts[7]<=ts[8],'nested')
 shell=(R/'ROOT.stderr').read_text();wall=float(re.search(r'([0-9.]+) real',shell).group(1));rss=int(re.search(r'(\d+)  maximum resident set size',shell).group(1))
 need(receipt['seconds']<=wall+.01 and wall+.01<30,'shell');need(0<rss<=384*1048576 and 0<receipt['sampled_whole_tree_peak']<=384*1048576,'memory')
 need(data['alpha_computed'] is False and data['physical_Gram_computed'] is False,'scope')
 elapsed=time.monotonic()-start;need(elapsed<25 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<384*1048576,'review resources')
 reads={str(p):sha(p) for folder in [O,R] for p in folder.iterdir() if p.is_file()};reads[str(P/'FREEZE.json')]=pf
 write('READ_HASHES.json',reads);write('RESULT.json',{'status':'PASS','predicates':count,'rows':len(completed),'coefficient_count':408,'seconds':elapsed,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'new_worker_or_integral_calls':0,'method':'independent axis-allocation integer recurrence and exact Horner finite-certificate replay'})
 print('PASS',count,elapsed)
except BaseException as e:write('FAILURE.json',{'stage':stage,'completed':completed,'error':repr(e)});raise
