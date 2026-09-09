import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
S=1<<192

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def req(x,m):
 if not x:raise ValueError(m)
def integer(x):return type(x)is int
def interval(x):return isinstance(x,(list,tuple)) and len(x)==2 and all(integer(v) for v in x) and x[0]<=x[1] and all(abs(v).bit_length()<=320 for v in x)
def coord(k):return isinstance(k,(list,tuple)) and len(k)==2 and all(integer(v) for v in k) and 0<=k[0]<402 and k[1]in(0,1)
def vector(v):
 req(isinstance(v,list),'encoded vector');seen=set()
 for row in v:
  req(len(row)==4 and coord(row[:2]) and interval(row[2:]),'encoded entry');k=tuple(row[:2]);req(k not in seen,'unique coordinate');seen.add(k)
 return seen
def matrix(a):req(len(a)==8 and all(len(row)==8 and all(interval(x) for x in row) for row in a),'8matrix')
def read(p):return json.loads(Path(p).read_text())
def check(out,rf,elapsed):
 out=Path(out);r=read(out/'RESULT.json');w=read(out/'WORKER_COMPLETE.json');part=read(out/'PARTIAL.json')
 req(not any((out/n).exists() for n in('FAILURE.json','DISPATCH_FAILURE.json','IMMUTABILITY_FAILURE.json')),'no failure files')
 req(read(out/'STARTED.json')==rf['authorization'],'startup')
 req(w['status']=='COMPLETE_SPARSE_ACTION_ONLY' and w['freeze_sha256']==rf['worker_freeze'] and w['binding_sha256']==rf['authorization']['binding_sha256'] and w['result_sha256']==sha(out/'RESULT.json'),'worker/result')
 req(all(type(t)in(int,float) and math.isfinite(t) and t>0 for t in(r['seconds'],w['seconds'],elapsed)) and r['seconds']<=w['seconds']<119 and w['seconds']<=elapsed<=120,'time')
 req(integer(w['rss_bytes']) and 0<w['rss_bytes']<=384*1048576 and w['continuation_used'] is False,'resources/scope')
 req(r['status']=='COMPLETE_FIXED_FOUR_PAIR_SPARSE_ACTION' and integer(r['original_pairs']) and r['original_pairs']==4 and r['continuation_used'] is False and r['midpoint_isometry_claim'] is False and len(r['orbits'])==5,'fixed scope')
 req(part=={'stage':'complete','completed_orbits':r['orbits']},'complete partial')
 plan=read(rf['binding_path']);restore=read(plan['restore_binding']);old=Path(restore['pilot_output']);summaries=[]
 for oi,row in enumerate(r['orbits']):
  req(integer(row['orbit']) and row['orbit']==oi,'orbit order');d=out/f'ORBIT_{oi}';v=read(d/'RESULT.json');state=read(d/'RESTORED_STATE.json')
  req(sha(d/'RESULT.json')==row['result_sha256'] and sha(d/'EVENTS.ndjson')==row['events_sha256'],'saved digests')
  oldhist=read(old/f'ORBIT_{oi}/HISTORY.json');req(state['history']==oldhist['history'] and len(state['history'])==4 and state['original_context']==oldhist['context'] and state['history_sha256']==sha(old/f'ORBIT_{oi}/HISTORY.json'),'original four history')
  events=[]
  with(d/'EVENTS.ndjson').open() as f:
   for line in f:
    e=json.loads(line);req(integer(e['orbit']) and e['orbit']==oi,'event orbit');events.append(e)
  req(events and row['status']==v['status'],'result status')
  if v['status']=='INDETERMINATE_CONDITIONING':
   req(v['leakage_pass'] is False and isinstance(v['error'],str) and events[-1]['stage']=='indeterminate' and events[-1]['error']==v['error'],'retained indeterminate');summaries.append({'orbit':oi,'status':v['status']});continue
  req(v['status']=='COMPLETE_CONDITIONAL_ACTION_ENCLOSURE' and v['midpoint_isometry_claim'] is False,'enclosure scope')
  R=v['R'];U=v['U'];req(all(coord(k) and k[0]<399 for k in R) and len(R)<=16 and len(set(map(tuple,R)))==len(R),'original R');req(all(coord(k) for k in U) and len(U)<=24 and len(set(map(tuple,U)))==len(U) and set(map(tuple,R))<=set(map(tuple,U)),'DATA U')
  saved=read(d/'COEFFICIENTS.json');req(saved['R']==R and len(saved['columns'])==8,'saved coefficients')
  for c in saved['columns']:req(vector(c)<=set(map(tuple,R)),'original C support')
  ce=[e for e in events if e['stage']=='coefficient_enclosed'];req(len(ce)==4 and [e['pair'] for e in ce]==list(range(4)),'four coefficient records')
  pe=[e for e in events if e['stage']=='principal_gram_complete'];req(len(pe)==1 and pe[0]['U']==U and len(pe[0]['entries'])==len(U)*(len(U)+1)//2,'retained principal Gram')
  expected=[(a,b) for ii,a in enumerate(U) for b in U[ii:]]
  for entry,(a,b) in zip(pe[0]['entries'],expected):req(len(entry)==6 and entry[:2]==a and entry[2:4]==b and interval(entry[4:]),'principal entry shape/order')
  ae=[e for e in events if e['stage']=='action_enclosed'];req(len(ae)==2 and len(v['results'])==2,'two impurities');flags=[]
  for q,z,e in zip((399,400),v['results'],ae):
   req(z=={k:t for k,t in e.items() if k not in('stage','orbit')} and z['impurity_bare_index']==q,'retained TGL')
   req(z['columns']==saved['columns'] and len(z['action_columns'])==8,'same columns')
   for col in z['action_columns']:req(vector(col)<=set(map(tuple,U)),'action support')
   for name in('T','G','L'):matrix(z[name])
   T,L=z['T'],z['L']
   for i in range(8):
    req(T[i][i]==[0,0] and L[i][i][0]>=0,'proved diagonals')
    for j in range(8):req(T[i][j]==[-T[j][i][1],-T[j][i][0]] and L[i][j]==L[j][i],'proved symmetry')
   bound=max(sum(max(abs(x[0]),abs(x[1])) for x in rr) for rr in L)
   req(integer(z['delta_squared_upper_numerator']) and bound==z['delta_squared_upper_numerator'] and integer(z['denominator']) and z['denominator']==S,'row bound')
   req(F(z['leakage_target'])==F(1,10**6) and type(z['leakage_pass'])is bool and z['leakage_pass']==(F(bound,S)<=F(1,10**12)),'optional target')
   flags.append(z['leakage_pass'])
  summaries.append({'orbit':oi,'status':v['status'],'leakage_pass':flags})
 return {'status':'PASS_SPARSE_ACTION_SAVED_SCHEMA','orbits':summaries,'result_sha256':sha(out/'RESULT.json'),'native_arithmetic_replayed':False,'midpoint_isometry_claim':False,'external_pending':True}
