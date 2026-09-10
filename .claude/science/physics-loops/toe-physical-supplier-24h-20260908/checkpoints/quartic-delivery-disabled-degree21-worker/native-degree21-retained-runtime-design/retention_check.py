"""Affected output-only controls; zero synthetic Gram, no native values."""
import json
from fractions import Fraction as F
import core,arithmetic as a,assembly as A,certificate
out={};checks=0
for kind,target in [('nominal21',286),('inner21',448)]:
 events=[];Z,c=core.jet(kind,A.defects(kind),lambda *_:a.ZERO,lambda *_:a.ZERO,lambda s,d:events.append({'stage':s,'data':d}))
 assert len(events)==target and all(v==a.ZERO for k,v in Z.items()if sum(k));checks+=1
 for i,e in enumerate(events):
  if e['stage']=='operator_matrices':assert events[i+1]['stage']=='operator_coefficient';checks+=1
  if e['stage']=='log_power_matrix':assert events[i+1]['stage']=='log_power_trace';checks+=1
 raw=json.dumps(events,separators=(',',':'));out[kind]={'events':len(events),'zero_fixture_json_bytes':len(raw)}
 if kind=='nominal21':nom=Z
p={k:[F(0)]*3 for k in('P','O')};t={k:{'q':(F(0),F(0)),'eta':a.ZERO,'trial_norm':a.ZERO}for k in p};jets={(x,y,z):nom for x,y,z,_ in A.SIGNATURES};first={k:F(0)for k in p};ev=[]
r=certificate.finish(p,t,jets,first,(F(0),F(0)),(F(-1),F(1)),lambda s,d:ev.append((s,d)));assert r['intersection']==(F(0),F(0));checks+=1
try:certificate.finish(p,t,jets,first,(F(0),F(0)),(F(1),F(2)),lambda s,d:ev.append((s,d)))
except ValueError:assert ev[-1][0]=='new_q_posterior_raw';checks+=1
else:raise AssertionError('empty intersection accepted')
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':checks,'profiles':out,'native_values':0},indent=2))
