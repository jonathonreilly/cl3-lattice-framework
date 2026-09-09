from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
Q=1<<256
def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def budgets(s,aa,ap,total):
 ea=(F(aa[1])-F(aa[0]))/2;ep=(F(ap[1])-F(ap[0]))/2;k=kp=F(0)
 for n in range(40):
  d=(2*n+1)*8**(2*n+1);k+=s**(2*n+2)/d;kp+=(2*n+2)*s**(2*n+1)/d
 eps=F(1,2**64);a0=F(17,60);low=(eps*ea+eps**3*a0/(6*s*s),eps*ep+eps**3*a0/(3*s**3));high=(k*ea,kp*ea+k*ep);rem=F(12**40,81*8**81);quad=F(128,4**52)
 widths=[F(200,157)*(total[i]+low[i]+high[i]+rem/2+quad+F(1,10**35))+F(1,10**35)for i in range(2)]
 return low,high,widths
def check(out,rf,elapsed):
 out=Path(out);read=lambda n:json.loads((out/n).read_text());r=read('RESULT.json');w=read('WORKER_COMPLETE.json');p=read('PARTIAL.json')
 req(read('STARTED.json')==rf['authorization'],'start')
 req(w['status']=='COMPLETE_WIDTH_ONLY_DIAGNOSTIC'and w['runtime_sha256']==rf['worker_freeze']and w['result_sha256']==sha(out/'RESULT.json'),'worker')
 req(all(type(x)in(int,float)and math.isfinite(x)and x>0 for x in(r['seconds'],p['seconds'],w['seconds'],elapsed))and r['seconds']<=p['seconds']<=w['seconds']<119 and w['seconds']<=elapsed<120,'timing')
 req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 req(r['status']=='COMPLETE_REMAINING65_WIDTH_DIAGNOSTIC'and len(r['poles'])==66,'diagnostic')
 for k,v in(('new_node_checks',113230),('recovered_node_records',1742),('node_checks',114972),('moments_evaluated',0),('integral_centers_evaluated',0),('oracle_calls',0)):req(type(r[k])is int and r[k]==v,'counts')
 binding=json.loads(Path(rf['binding_path']).read_text());b=binding['physical'];prior=binding['prior']
 req(sha(prior['nodes'])==prior['inputs'][prior['nodes']]and sha(out/'RECOVERED_NODES_00.ndjson')==prior['inputs'][prior['nodes']],'original pole0 exact copy')
 poles=json.loads(Path(b['poles_path']).read_text())['rows'];a66=json.loads((Path(b['a66']['directory'])/'RESULT.json').read_text())['rows'];req(len(poles)==len(a66)==66,'input66')
 expected={'STARTED.json','PARTIAL.json','RESULT.json','WORKER_COMPLETE.json'}|{f'{kind}_{i:02d}.{ext}'for i in range(66)for kind,ext in(('NODES','ndjson'),('POLE','json'))};expected.remove('NODES_00.ndjson');expected.add('RECOVERED_NODES_00.ndjson');req(set(x.name for x in out.iterdir())==expected,'outputmembership/failures')
 count=0;flags=[]
 for i in range(66):
  total=[0,0];sep=True;j=0
  with(out/('RECOVERED_NODES_00.ndjson'if i==0 else f'NODES_{i:02d}.ndjson')).open()as f:
   for line in f:
    row=json.loads(line);req(type(row['node'])is int and row['node']==j and type(row['panel'])is int and row['panel']==j//26-64,'fixednodeorder');rr=list(map(F,row['radii']));req(len(rr)==2 and all(x>=0 and (x*Q).denominator==1 for x in rr),'256radii');info=row['info']
    if 'separation_failure'in info:req(info['separation_failure']=='denominator does not separate'and rr==[0,0],'separationfailure');sep=False
    else:req(F(info['denominator_lower_abs'])>0 and len(info['node_radii'])==2,'separation')
    total=[total[k]+int(rr[k]*Q)for k in range(2)];req(list(map(F,row['cumulative_radii']))==[F(x,Q)for x in total],'retainedcumulative');j+=1
  req(j==1742,'nodecensus');count+=j;z=read(f'POLE_{i:02d}.json');s=F(poles[i]['s_midpoint']);req(F(1,128)<=s<=16 and F(z['s'])==s and z['pole']==i,'fixedpole');raw=a66[i]['oracle'];low,high,width=budgets(s,raw['A'],raw['Aprime'],[F(x,Q)for x in total]);passes=[width[0]<=F(2,10**28),width[1]<=F(2,10**27)]
  req(list(map(F,z['low_radii']))==list(low)and list(map(F,z['high_input_radii']))==list(high)and list(map(F,z['widths']))==width,'low/high/totalledger')
  req(z['passes']==passes and all(type(x)is bool for x in z['passes'])and z['separated']is sep,'flags');status='FEASIBLE_UNDER_DECLARED_ARITHMETIC_RESERVE'if sep and all(passes)else'INDETERMINATE_WIDTH_OR_SEPARATION';req(z['status']==status and r['poles'][i]=={'pole':i,'status':status,'separated':sep,'passes':passes},'classification');flags.append(status.startswith('FEASIBLE'))
 req(count==114972 and type(r['all_feasible'])is bool and r['all_feasible']==all(flags),'allflags')
 req(p['current']=={'stage':'complete'}and p['poles']==r['poles']and p['node_checks']==114972,'lastpartial')
 return {'status':'PASS_WIDTH_LEDGER_SCHEMA','all_feasible':all(flags),'node_error_formulas_recomputed':False,'node_records':count,'new_node_records':113230,'recovered_node_records':1742,'poles':66,'high_amplification_terms':2640,'integral_centers_evaluated':0,'result_sha256':sha(out/'RESULT.json')}
