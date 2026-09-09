"""Saved center accumulation and independent tails. Never recomputes a node formula."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb,isfinite
import json,hashlib
S=1<<256;EPS=F(1,2**64);A0=F(17,60);TARGETS=(F(2,10**28),F(2,10**27))
def need(x,msg):
 if not x:raise ValueError(msg)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def literal(d,k,n):need(type(d[k])is int and d[k]==n,'literal '+k)
def pair(x):
 need(type(x)is list and len(x)==2 and all(type(v)is str for v in x),'fraction pair');return tuple(map(F,x))
def floor(x):return F((x*S).numerator//(x*S).denominator,S)
def moments():
 return [sum(F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b)for a in range(n+1)for b in range(n-a+1))for n in range(41)]
def pi_bounds():
 def atan(q,n):
  v=sum((F((-1)**k,(2*k+1)*q**(2*k+1))for k in range(n)),F(0));e=F(1,(2*n+1)*q**(2*n+1));return(v,v+e)if n%2==0 else(v-e,v)
 a,b=atan(5,32),atan(239,10);return 16*a[0]-4*b[1],16*a[1]-4*b[0]
def check(out,rf,elapsed,progress=lambda d:None):
 out=Path(out);rd=lambda p:json.loads(p.read_text());r=rd(out/'RESULT.json');w=rd(out/'WORKER_COMPLETE.json');partial=rd(out/'PARTIAL.json')
 need(r['status']=='COMPLETE_NEW_RHO4_B66_CERTIFICATES','complete result');need(w['status']=='COMPLETE_NEW_CENTER_CERTIFICATES_ONLY','worker status')
 need(w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==rf['binding_sha256']and w['result_sha256']==sha(out/'RESULT.json'),'worker binding')
 for d,k,n in [(r,'poles',66),(r,'node_center_pairs',114972),(r,'panels_per_pole',67),(r,'tail_terms',40),(r,'moments',41),(r,'oracle_calls',0),(r,'old_protocol_replays',0)]:literal(d,k,n)
 need(r['matrix_computed']is False and r['alpha_computed']is False,'scope');need(type(r['rows'])is list and len(r['rows'])==66,'rows66')
 for x,cap in [(r['seconds'],119),(w['seconds'],119),(elapsed,120)]:need(type(x)in(int,float)and isfinite(x)and 0<x<=cap,'time')
 need(r['seconds']<=w['seconds']<=elapsed,'nested timing');need(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 need(rd(out/'CURRENT.json')=={'stage':'complete'},'final CURRENT');need(partial['current']=={'stage':'complete'}and partial['rows']==r['rows'],'final partial');literal(partial,'node_centers',114972)
 need(r['seconds']<=partial['seconds']<=w['seconds'],'partial timing')
 expected={'STARTED.json','RESULT.json','PARTIAL.json','WORKER_COMPLETE.json','MOMENTS.json','PI.json','CURRENT.json'}|{f'POLE_{i:02d}'for i in range(66)}
 need({x.name for x in out.iterdir()}==expected,'exact output membership')
 M=moments();md=rd(out/'MOMENTS.json');need(md['moment_indices']==list(range(41))and list(map(F,md['values']))==M,'independent multinomial moments')
 pi=pi_bounds();need(pair(rd(out/'PI.json')['interval'])==pi,'independent Machin interval')
 b=rd(Path(rf['binding_path']));total=0;flags=[]
 physical=b['physical'];pole_source=rd(Path(physical['poles_path']))['rows'];a_source=rd(Path(physical['a66']['directory'])/'RESULT.json')['rows'];need(len(pole_source)==len(a_source)==66,'source scalar census')
 for i,row in enumerate(r['rows']):
  progress({'stage':'schema_pole','pole':i,'records':total});literal(row,'pole',i);od=out/f'POLE_{i:02d}';need(rd(od/'RESULT.json')==row,'per-pole result')
  need({x.name for x in od.iterdir()}=={'CENTERS.ndjson','TAILS_AND_BUDGET.json','RESULT.json'}|{f'PANEL_{j:02d}.json'for j in range(67)},'pole output membership')
  sums=[F(0),F(0)];panel=[F(0),F(0)];err=[F(0),F(0)];n=0
  with(od/'CENTERS.ndjson').open()as fp,Path(b['node_files'][i]).open()as oldfp:
   for line in fp:
    d=json.loads(line);original=json.loads(next(oldfp));literal(original,'node',n);literal(original,'panel',n//26-64);need(pair(d['accepted_radii'])==pair(original['radii']),'bound original node radii');literal(d,'node',n);literal(d,'panel',n//26-64);need(n<1742,'extra node');centers=pair(d['centers']);rr=pair(d['accepted_radii'])
    need(all((v*S).denominator==1 for v in centers+rr)and all(v>=0 for v in rr),'fixed grid radii')
    panel=[panel[k]+centers[k]for k in range(2)];err=[err[k]+rr[k]for k in range(2)];need(pair(d['panel_cumulative'])==tuple(panel),'node cumulative');n+=1;total+=1
    if n%26==0:
     sums=[sums[k]+panel[k]for k in range(2)];p=rd(od/f'PANEL_{n//26-1:02d}.json');literal(p,'panel',n//26-65)
     need(pair(p['centers'])==tuple(panel)and pair(p['cumulative'])==tuple(sums)and pair(p['accepted_radius_cumulative'])==tuple(err),'panel cumulative');panel=[F(0),F(0)]
   need(not oldfp.readline(),'extra bound old node')
  need(n==1742,'missing nodes');t=rd(od/'TAILS_AND_BUDGET.json');s=F(row['s_midpoint']);need(F(t['s'])==s and F(1,128)<=s<=16,'fixed s');A=pair(t['A']);Ap=pair(t['Aprime']);source=a_source[i];literal(source,'id',i);need(source['gate']=='PASS'and F(pole_source[i]['s_midpoint'])==s and F(source['oracle']['s'])==s and pair(source['oracle']['A'])==A and pair(source['oracle']['Aprime'])==Ap,'bound original pole A/Aprime');a=sum(A)/2;ap=sum(Ap)/2
  # Independent explicit polynomial expansion of J_n rather than producer recurrence.
  def J(k):return sum(((-s*s)**j*M[k-1-j]for j in range(k)),F(0))+(-s*s)**k*a
  def Jp(k):return sum((2*j*(-1)**j*s**(2*j-1)*M[k-1-j]for j in range(1,k)),F(0))+2*k*(-1)**k*s**(2*k-1)*a+(-s*s)**k*ap
  gp=sum((F((-1)**j,(2*j+1)*8**(2*j+1))*J(j+1)for j in range(40)),F(0));hp=-sum((F((-1)**j,(2*j+1)*8**(2*j+1))*Jp(j+1)for j in range(40)),F(0));rem=F(12**40,81*8**81);quad=F(128,4**52)
  high=(floor(gp+rem/2),floor(hp+rem/2));low=(floor(EPS*a-EPS**3*A0/(6*s*s)),floor(-EPS*ap-EPS**3*A0/(3*s**3)))
  need(pair(t['high_centers_with_half_remainder'])==high and pair(t['low_centers'])==low,'independent high/low centers');need(pair(t['middle'])==tuple(sums)and pair(t['node_radii'])==tuple(err),'middle/radii')
  accepted=rd(Path(b['pole_files'][i]));lr=pair(accepted['low_radii']);hr=pair(accepted['high_input_radii']);need(pair(t['low_radii'])==lr and pair(t['high_input_radii'])==hr,'accepted input radii')
  need(F(t['positive_remainder'])==rem and F(t['quadrature_radius'])==quad and F(t['arithmetic_reserve'])==F(1,10**35),'analytic radii')
  radii=tuple(err[k]+lr[k]+hr[k]+rem/2+quad+F(1,10**35)for k in range(2));c=tuple(sums[k]+low[k]+high[k]for k in range(2));need(pair(accepted['widths'])==tuple(F(200,157)*x+F(1,10**35)for x in radii),'accepted total width budget');need(pair(t['total_centers'])==c and pair(t['total_radii'])==radii,'final inputs')
  answers=[]
  for k in range(2):
   vals=[x*y for x in(c[k]-radii[k],c[k]+radii[k])for y in(2/pi[1],2/pi[0])];x=(floor(min(vals)),-floor(-max(vals)));answers.append(x if k==0 else(-x[1],-x[0]))
  need(pair(row['B'])==answers[0]and pair(row['Bprime'])==answers[1],'final directed enclosure');widths=tuple(x[1]-x[0]for x in answers);need(pair(row['widths'])==widths and pair(row['targets'])==TARGETS,'fixed widths/targets')
  ok=all(widths[k]<=TARGETS[k]for k in range(2));need(row['status']==('CERTIFIED_TARGET'if ok else'INDETERMINATE_TARGET'),'actual target status');flags.append(ok)
 need(total==114972 and type(r['all_targets_met'])is bool and r['all_targets_met']==all(flags)and w['all_targets_met']is r['all_targets_met'],'all flags')
 return {'status':'PASS_SAVED_STRUCTURE_AND_TAILS','node_records':total,'poles':66,'independent_moments':41,'node_center_formulas_recomputed':0,'all_targets_met':all(flags),'scope':'accepted radius reuse and saved accumulation/tails; future independent node-center replay still required'}
