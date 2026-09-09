import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F

def check(out,rf,elapsed):
 out=Path(out)
 def req(x,m):
  if not x:raise ValueError(m)
 def read(n):return json.loads((out/n).read_text())
 req({p.name for p in out.iterdir()}=={'STARTED.json','RESULT.json','PARTIAL.json','WORKER_COMPLETE.json','INDEPENDENT.ndjson'},'membership')
 req(read('STARTED.json')==rf['authorization'],'start')
 r,w,p=read('RESULT.json'),read('WORKER_COMPLETE.json'),read('PARTIAL.json')
 req(w['status']=='COMPLETE_SELECTED_SAVED'and w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==rf['authorization']['binding_sha256']and w['result_sha256']==hashlib.sha256((out/'RESULT.json').read_bytes()).hexdigest(),'completion binding')
 for x,cap in ((w['seconds'],119),(r['seconds'],119),(elapsed,120)):
  req(type(x)in(int,float)and math.isfinite(x)and 0<x<cap,'time')
 req(r['seconds']<=w['seconds']<=elapsed and type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'resources')
 req(r['status']=='PASS_INDEPENDENT_SELECTED_SAVED'and r['entry_truth_inherited']is True and len(r['rows'])==5,'result')
 acc=json.loads(Path(rf['acceptance']).read_text())
 for i,row in enumerate(r['rows']):
  req(type(row['orbit'])is int and row['orbit']==i and row['status']=='PASS_SAVED_MATRIX_CERTIFICATE'and row['certificate_replayed']is True,'orbit')
  a=acc['orbits'][i]
  req(F(row['e'])==F(a['e'])and F(row['radius'])==F(a['radius'])and 0<=F(row['e'])<1 and F(row['radius'])>=0,'numeric acceptance')
  for key in ('width_pass','l1_pass'):req(type(row[key])is bool and row[key]==a[key],'flags')
 req(p=={'current':{'stage':'complete','orbit':5},'rows':r['rows']},'final partial')
 events=[json.loads(x)for x in (out/'INDEPENDENT.ndjson').read_text().splitlines()]
 expected=[('initial_pins',0)]
 stages=['before_orbit_parse','before_selected_entries','selected_reconstruction']
 for s in ('dyadic_inputs','H_integer','error','coefficient_box'):stages += ['independent_'+s,'verified_'+s]
 for i in range(5):expected += [(s,i)for s in stages]+[('orbit_complete',i+1)]
 expected += [('final_pins',5),('complete',5)]
 req(len(events)==len(expected),'event count')
 for e,(s,i)in zip(events,expected):req(e['current']=={'stage':s,'orbit':i}and isinstance(e['data'],dict),'stage')
 for i in range(5):
  data={e['current']['stage']:e['data']for e in events if e['current']['orbit']==i}
  d=data['independent_dyadic_inputs'];h=data['independent_H_integer'];err=data['independent_error'];box=data['independent_coefficient_box']
  def matrix(a,n,m):req(len(a)==n and all(len(row)==m for row in a),'matrix')
  for key in ('Gcenter','radius','T'):matrix(d[key],48,48)
  req(d['scale']==2**256 and 0<len(d['E'])<=96,'dyadic');matrix(d['E'],len(d['E']),48)
  matrix(h['H'],48,48);req(h['denominator']==2**768,'denominator')
  matrix(box['center'],len(d['E']),48)
  req(F(err['e'])==F(r['rows'][i]['e'])and F(box['radius'])==F(r['rows'][i]['radius']),'intermediate equality')
 return {'status':'PASS_SELECTED_SAVED_SCHEMA','orbits':5,'native_entries_recomputed':False}
