from pathlib import Path
import json,hashlib
S=Path('/private/tmp/toe-24h-probes-20260908');R=S/'native-coarse-witness-continuation-root-review';R.mkdir(exist_ok=True);O=S/'native-coarse-witness-root-review';P=S/'native-coarse-witness-continuation-design'
s=(O/'run_once.py').read_text().replace("native-coarse-occupied-witness-runtime-design","native-coarse-witness-continuation-design").replace("'new_certificate_only':True","'new_continuation_only':True").replace('new coarse witness attempt failed','new coarse continuation attempt failed')
(R/'run_once.py').write_text(s)
s=(O/'schema.py').read_text().replace("'BLOCKS.jsonl'}","'BLOCKS.jsonl','CONTINUATION.json'}").replace('COMPLETE_FIXED_COARSE_WITNESS','COMPLETE_COMPOSITE_COARSE_WITNESS')
s=s.replace(" summaries=[];events=0", """ req(type(result['inherited_cases'])is int and result['inherited_cases']==3 and type(result['new_nodes'])is int and result['new_nodes']==2436 and result['original_run_status']=='FAILED_ONCE_TIME_CAP_PRESERVED','continuation scope')
 pre=binding['prefix'];a=read(Path(pre['receipt']['path']));req(sha(pre['receipt']['path'])==pre['receipt']['sha256'],'failed receipt pin')
 req(a['status']=='FAILED_ONCE_TIME_CAP_PRESERVED'and a['worker_freeze']==pre['worker_freeze']and a['root_freeze']==pre['root_freeze']and a['whole_witness_certified']is False and a['partial_cases_independently_accepted']is False,'old failure remains failed')
 req(type(a['external_seconds'])in(int,float)and isfinite(a['external_seconds'])and 0<a['external_seconds']<300 and type(a['returncode'])is int and a['returncode']==-9,'old failed time/code')
 for key in ('external_rss_bytes','sampled_whole_tree_peak'):req(type(a[key])is int and 0<a[key]<=384*1048576,'old failed resources')
 req(type(a['completed_case_files'])is int and a['completed_case_files']==3 and type(a['retained_event_lines'])is int and a['retained_event_lines']==76 and a['last_panel_metadata']==['witness_panel','3','210']and a['outputs']==pre['outputs'],'old prefix relation')
 old=Path(pre['output']);req(set(x.name for x in old.iterdir())==set(pre['outputs']),'old membership')
 for name,h in pre['outputs'].items():req(sha(old/name)==h,'old retained hash')
 for i in range(3):req(sha(O/f'CASE_{i:02d}.json')==pre['outputs'][f'CASE_{i:02d}.json'],'verbatim completed case')
 with (O/'BLOCKS.jsonl').open('rb')as f:prefix_bytes=b''.join(f.readline()for _ in range(76))
 req(hashlib.sha256(prefix_bytes).hexdigest()==pre['outputs']['BLOCKS.jsonl'],'verbatim76 prefix')
 con=read(O/'CONTINUATION.json');req(same(con,{'old_status':'FAILED_ONCE_TIME_CAP_PRESERVED','prefix_outputs':pre['outputs'],'inherited_cases':3,'inherited_nodes':1344,'remaining_nodes':2436,'start_case':3,'start_node':210,'adapter_truth':'inherited reviewed original adapter; prefix grammar and final block gates checked; no prefix native recomputation'}),'continuation receipt')
 cp=binding['files']['coefficient_events'];req(sha(cp['path'])==cp['sha256'],'pi input pin');pi=None;pi_count=0
 with Path(cp['path']).open()as f:
  for line in f:
   event=json.loads(line)
   if event['stage']=='reciprocal_pi':
    pi_count+=1;pi=mat([[event['payload']['interval']]],1,1)[0][0];pi=round_box(*pi)
 req(pi_count==1 and pi[0]>0,'unique reciprocal pi')
 summaries=[];events=0""")
s=s.replace("mat(x['local'],7,48);mat(x['projector_columns'],48,7)","local=mat(x['local'],7,48);mat(x['projector_columns'],48,7)")
s=s.replace("mat(x['direct'],7,7);mat(x['mixed'],7,7)","direct=mat(x['direct'],7,7);mixed=mat(x['mixed'],7,7)")
s=s.replace("block=mat(x['block'],7,7)","block=mat(x['block'],7,7);req(block==assemble(local,direct,mixed,pi,case),'independent high/mixed final assembly')")
s=s.replace("'ACCEPTED_FIXED_COARSE_WITNESS_SCHEMA'","'ACCEPTED_COMPOSITE_COARSE_WITNESS_SCHEMA'")
s=s.replace("'raw_adapter_contractions_replayed':False", "'raw_adapter_contractions_replayed':False,'independent_final_high_mixed_assembly':True,'old_failed_protocol_relabelled':False,'inherited_cases':3,'new_nodes':2436")
s+='''
# Independent scalar Fraction dyadic evaluator; no producer modules imported.
def round_box(a,b):
 Q=1<<192
 return F((a.numerator*Q)//a.denominator,Q),F(-((-b.numerator*Q)//b.denominator),Q)
def plus(x,y):return round_box(x[0]+y[0],x[1]+y[1])
def times(x,y):
 a,b=x;c,d=y
 if a>=0:
  lo,hi=(a*c,b*d)if c>=0 else (b*c,a*d)if d<=0 else(b*c,b*d)
 elif b<=0:
  lo,hi=(a*d,b*c)if c>=0 else(b*d,a*c)if d<=0 else(a*d,a*c)
 else:
  lo,hi=(a*d,b*d)if c>=0 else(b*c,a*c)if d<=0 else(min(a*d,b*c),max(a*c,b*d))
 return round_box(lo,hi)
def product(A,B):
 C=[]
 for row in A:
  out=[]
  for j in range(len(B[0])):
   z=(F(0),F(0))
   for k,x in enumerate(row):z=plus(z,times(x,B[k][j]))
   out.append(z)
  C.append(out)
 return C
def assemble(local,direct,mixed,pi,case):
 pairs=(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)))
 pair=pairs[case//2][case%2];high=[[(F(0),F(0))for _ in range(7)]for _ in range(7)]
 for j in pair:
  v=2*((-1)**(j+1));high[0][j]=times((F(v,16),F(v,16)),pi);high[j][0]=times((F(-v,16),F(-v,16)),pi)
 projected=product(high,product(local,list(map(list,zip(*local)))))
 out=[]
 for i in range(7):
  row=[]
  for j in range(7):
   x=plus(direct[i][j],high[i][j]);y=plus(mixed[i][j],projected[i][j]);row.append(plus(x,(-y[1],-y[0])))
  out.append(row)
 return out
'''
(R/'schema.py').write_text(s)
(R/'PROTOCOL.md').write_text('''# Disabled independent continuation root

Author: Orbital, also author of the continuation worker; independent implementation of final scalar checks does not replace external source review. Reuses the original reviewed300/299.5/299 second,384MiB root lifecycle with full source hashes in precheck and final closure, current-child cleanup, inclusive schema RSS/time guards and once marker. Execution disabled pending independent review and preregistration.

Success requires exactly15 files,205 events, the original76-event prefix verbatim and three byte-identical completed cases. It preserves the failed original receipt and verifies its time/resource/source relation. All ten final49-entry lower norms and radii are independently evaluated. The high correction and mixed final subtraction are independently rebuilt with Fraction sign-case multiplication and dyadic rounding using saved local/direct/mixed and the authenticated reciprocal-pi interval. Raw native contractions, mappedT truth and the partial panel accumulations remain inherited reviewed interfaces, not independently replayed. The complete second run certifies a composite result, never success of the old failed run.

Synthetic tests and readiness do not read actual scientific arrays. Launch mode requires a separately installed exact worker authorization and enabled freeze. Fixed output native-coarse-witness-continuation-run-prospective. External /usr/bin/time receipt remains required for acceptance.
''')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
h=sha(P/'FREEZE.json');out=str(S/'native-coarse-witness-continuation-run-prospective');auth={'worker_freeze':h,'output':out,'once':True,'external_seconds':300,'rss_bytes':384*1048576}
(R/'AUTHORIZATION.json').write_text(json.dumps(auth,indent=2)+'\n');(R/'WORKER_AUTHORIZATION.json').write_text(json.dumps({'freeze_sha256':h,'output':out,'once':True},indent=2)+'\n')
f={'execution_enabled':False,'worker_path':str(P),'worker_freeze':h,'worker_authorization_sha256':sha(R/'WORKER_AUTHORIZATION.json'),'authorization':auth,'authorization_sha256':sha(R/'AUTHORIZATION.json'),'membership':['run_once.py','schema.py'],'files':{n:sha(R/n)for n in ['run_once.py','schema.py','PROTOCOL.md']}}
(R/'ROOT_FREEZE.json').write_text(json.dumps(f,indent=2)+'\n');print(sha(R/'ROOT_FREEZE.json'))
