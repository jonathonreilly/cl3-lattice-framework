from pathlib import Path
from fractions import Fraction as F
import tempfile,json,hashlib
r=Path('/private/tmp/toe-24h-probes-20260908/native-global-projector-coefficient-root-review');e={};exec(compile((r/'schema.py').read_text(),'<schema>','exec'),e)
# Fixture deliberately repeats one nonnative atomic scalar; not a Gauss rule or acquisition.
with tempfile.TemporaryDirectory() as td:
 p=Path(td);source=p/'source';source.mkdir();o=p/'out';o.mkdir();dump=lambda x:json.dumps(x,default=str);put=lambda path,x:path.write_text(dump(x));sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest();identity={'synthetic':True};b=p/'BINDING.json';put(b,{'identity':identity,'output':str(source)});rf={'binding_path':str(b),'binding_sha256':sha(b),'worker_freeze':'synthetic'};events=[]
 def emit(stage,payload):events.append({'seq':len(events),'stage':stage,'payload':payload})
 n={'s_interval':['1','1'],'weight_interval':['1/378','1/378']};nodes=[dict(n,id=i)for i in range(378)];put(source/'NODES.json',{'rows':nodes});put(source/'RESULT.json',{'synthetic':True})
 emit('start',{'scope':'NEW_A_ONLY_PHYSICAL_COLUMN_COEFFICIENTS','acquisition_binding':identity})
 for i,node in enumerate(nodes):emit('input_row_before_check',{'id':i,'node':node});put(source/f'RAW_{i:03d}.json',{'raw':{'A':['1/7','1/7'],'s':'1'}})
 emit('accepted_inputs_loaded',{'count':378,'acquisition_result_sha256':sha(source/'RESULT.json')});pb=e['pi_box']();pm=sum(pb)/2;emit('reciprocal_pi',{'interval':pb,'terms':[40,12]});g=2**192;wl=F(g//378,g);wh=F(-(-g//378),g);w=(wl+wh)/2;A=F(1,7);D=F(1,7);a=F(3,7);maxerr=0
 for i in range(378):
  emit('weight_recentered',{'index':i,'original':[F(1,378)]*2,'rounded':[wl,wh]});emit('node_start',{'index':i,'row':{'id':i,'root':[F(1)]*2,'weight':[F(1,378)]*2,'A':[A]*2}})
  for kind in('P','O'):
   B=A;det=a*a+8*A*B;emit('coefficient_inputs',{'s':F(1),'A':A,'A_box':[A]*2,'D':D,'Bgeo':B,'a':a,'determinant':det,'kind':kind});Q=[[-8*B/det,2*a/det],[-2*a/det,-4*A/det]];qh=[[e['rounded'](v)for v in row]for row in Q];err=2*max(abs(Q[j][k]-qh[j][k])for j in range(2)for k in range(2));maxerr=max(maxerr,err);emit('coefficient_exact_and_rounded',{'Q':Q,'Qhat':qh,'operator_rounding':err});C=[[F(0)]*4 for _ in range(4)]
   for j in range(2):
    for k in range(2):C[j][k+2]=-w*pm*qh[j][k]/2;C[k+2][j]=-C[j][k+2]
   emit('node_operator',{'index':i,'kind':kind,'columns':'R0(+is)[e0,d], R0(-is)[e0,d]','positive_imaginary':C})
 analytic={'low':F(2,9)*F(5439,160)/2**48+F(867,192)/2**64,'high':F(1,8)*F(9,64)**15*(1+F(18,64*33)),'quadrature':6139*F(4,25)**21};rad={'A':F(0),'pole':F(0),'weight':(wh-wl)/2,'coefficient':maxerr,'reciprocal_pi':(pb[1]-pb[0])/2};fac={'A':2**27,'pole':2**42,'weight':2**13,'coefficient':5,'reciprocal_pi':2**12};terms={k:rad[k]*fac[k]for k in rad};ledger={'analytic':analytic,'input_radii':rad,'input_terms':terms,'input_error':sum(terms.values()),'total_error':sum(terms.values())+sum(analytic.values()),'midpoint_weight_sum':378*w,'physical_columns_exact':True,'gram_or_consumer_certified':False,'low_columns':'H0^-1 [e0,d]','high_operator':'sum coefficient*(HA^power-H0^power)','low_imaginary':[[0,-6*pm/2**32],[6*pm/2**32,0]],'high':[{'n':n,'power':2*n+1,'coefficient':pm*F((-1)**n,(2*n+1)*16**(2*n+1))}for n in range(15)]};ledger['low_imaginary'][0][0]=ledger['low_imaginary'][1][1]=F(0);emit('ledger_before_gate',ledger);result={'status':'CERTIFIED_DESCRIPTOR_OPERATOR_INPUT_BOUND','scope':'physical-column operator only; no Gram or Gaussian consumer','binding':identity,'ledger':ledger,'events':3407,'nodes':378,'classes':['P','O'],'coefficient_blocks':756,'native_oracle_calls':0,'physical_columns_evaluated':False,'gaussian_consumer_certified':False,'seconds':1};emit('complete',result)
 def writeevents():(o/'EVENTS.ndjson').write_text(''.join(dump(x)+'\n'for x in events))
 writeevents();put(o/'RESULT.json',result);put(o/'PARTIAL.json',{'current':{'stage':'complete','seq':3406},'events':3407,'coefficient_blocks':756,'seconds':2});put(o/'STARTED.json',{'freeze_sha256':'synthetic','output':str(o.resolve()),'once':True});c={'status':'COMPLETE','scope':'NEW_A_ONLY_DESCRIPTOR_COEFFICIENTS','freeze_sha256':'synthetic','binding':identity,'seconds':3,'rss_bytes':100,'result_sha256':sha(o/'RESULT.json'),'events_sha256':sha(o/'EVENTS.ndjson'),'partial_sha256':sha(o/'PARTIAL.json')};put(o/'WORKER_COMPLETE.json',c)
 def check():return e['check'](o,rf,4,lambda _:None)
 check();cases=['full3407 synthetic events accepted']
 # Rehash a corrupted coefficient stream so rejection is arithmetic, not stale digest.
 idx=next(i for i,x in enumerate(events)if x['stage']=='node_operator');old=events[idx]['payload']['positive_imaginary'][0][2];events[idx]['payload']['positive_imaginary'][0][2]=-old;writeevents();c['events_sha256']=sha(o/'EVENTS.ndjson');put(o/'WORKER_COMPLETE.json',c)
 try:check()
 except ValueError:cases.append('rehashed wrong positive sign rejected')
 else:raise AssertionError
 events[idx]['payload']['positive_imaginary'][0][2]=old;writeevents();c['events_sha256']=sha(o/'EVENTS.ndjson');c['rss_bytes']=True;put(o/'WORKER_COMPLETE.json',c)
 try:check()
 except ValueError:cases.append('boolean RSS rejected')
 else:raise AssertionError
print(json.dumps({'scope':'3407 fabricated repeated non-Gauss atomic metadata events; no producer assemble, actual A or native geometry','cases':cases},indent=2))
