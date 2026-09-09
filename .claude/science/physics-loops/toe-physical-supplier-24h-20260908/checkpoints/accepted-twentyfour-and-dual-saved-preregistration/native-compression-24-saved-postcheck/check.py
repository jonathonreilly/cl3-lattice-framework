"""Saved-only history/normalization checker; no native reader or pivot import."""
import json,hashlib,math,re
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import schema
S=1<<192

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def normalized(x,r):
 # Independent rational endpoint quotients, with separately proved integer roots.
 lo=isqrt(r[0]*S);hi=isqrt(r[1]*S)
 if hi*hi<r[1]*S:hi+=1
 if lo<=0:raise ValueError('root denominator')
 q=[F(a,b) for a in x for b in (lo,hi)]
 lower=(min(q)*S).__floor__();upper=(max(q)*S).__ceil__()
 mid=(lower+upper)//2
 return [mid,max(mid-lower,upper-mid)]
def run(cfg,out):
 stage='binding';current=None;checks=0;done=[];coordinates=0;histories=0
 def ck(x,msg):
  nonlocal checks
  if not x:raise ValueError(msg)
  checks+=1
 def save():
  tmp=out/'PARTIAL.tmp';tmp.write_text(json.dumps({'stage':stage,'current':current,'predicates':checks,'completed_orbits':done,'coordinates':coordinates,'histories':histories})+'\n');tmp.replace(out/'PARTIAL.json')
 def read(p):
  ck(p in cfg['inputs'] and sha(p)==cfg['inputs'][p],'bound read');return json.loads(Path(p).read_text())
 save()
 try:
  ck(cfg['status']=='ACCEPTED_RESULT_BOUND','binding status')
  for p,h in cfg['inputs'].items():ck(sha(p)==h,'input pin')
  rf=read(cfg['root_freeze']);wf=read(cfg['worker_freeze']);root=Path(cfg['root_freeze']).parent
  ck(sha(cfg['worker_freeze'])==rf['worker_freeze'],'worker identity')
  ck(sha(Path(__file__).with_name('schema.py'))==rf['files']['schema.py'],'exact reused final root schema')
  for n,h in rf['files'].items():ck(cfg['inputs'].get(str(root/n))==h,'root transitive closure')
  for n,h in wf['inputs'].items():ck(cfg['inputs'].get(n)==h,'worker transitive closure')
  ac=read(cfg['acceptance']);rc=read(cfg['receipt']);r=read(cfg['result'])
  ck(ac['status']=='ACCEPTED_COMPLETE_TWELVE_TO24_CONTINUATION' and ac['result_sha256']==sha(cfg['result']),'accepted result')
  ck(ac['root_freeze']==sha(cfg['root_freeze']) and ac['worker_freeze']==sha(cfg['worker_freeze']),'accepted sources')
  ck(rc['pass'] is True and rc['failure'] is None and type(rc['returncode'])is int and rc['returncode']==0,'root completion')
  for t in (rc['seconds'],ac['external_seconds']):ck(type(t)in(int,float) and math.isfinite(t) and 0<t<=120,'positive times')
  for v in (rc['sampled_whole_tree_peak'],ac['sampled_whole_tree_peak'],ac['external_max_rss']):ck(type(v)is int and 0<v<=384*1048576,'positive RSS')
  ck(rc['sampled_whole_tree_peak']==ac['sampled_whole_tree_peak'],'tree receipt')
  sh=Path(cfg['shell']).read_text();reals=re.findall(r'^real\s+([0-9]+(?:\.[0-9]+)?)$',sh,re.M);rss=re.findall(r'^\s*([0-9]+)\s+maximum resident set size$',sh,re.M)
  ck(len(reals)==len(rss)==1 and F(reals[0])==F(str(ac['external_seconds'])) and int(rss[0])==ac['external_max_rss'],'external receipt')
  ck(F(str(ac['external_seconds']))==F('21.25') and F(str(ac['prior_pilot_seconds']))==F('17.94') and F(str(ac['cumulative_physical_seconds']))==F('39.19'),'actual cumulative physical receipt')
  prior=read(cfg['pilot_post']);ck(prior['status']=='ACCEPTED_TWELVE_CONTINUATION_AND_NEW_SAVED_HISTORY_COORDINATES','accepted original prefix POST')
  ck(prior['post_result_sha256']==sha(prior['post_result_path']),'original post result binding');read(prior['post_result_path'])
  base=Path(cfg['result']).parent;stage='reused_fullstream_schema';save()
  verdict=schema.check(base,rf,rc['seconds'])
  ck(verdict['result_sha256']==sha(cfg['result']),'schema source')
  for oi in range(5):
   stage='orbit_events';current={'orbit':oi};save();d=base/f'ORBIT_{oi}'
   saved=read(str(d/'HISTORY.json'))['history'];rest=read(str(d/'RESTORED_STATE.json'));hp=list(rest['history']);ck(len(hp)==12 and saved[:12]==hp,'preserved twelve prefix');selected={h['index'] for h in hp};diag=rest['checkpoint']['diagonals'];diag_indices=[];row=None;row_columns=[];chosen=None;step=12;events=0
   with (d/'EVENTS.ndjson').open() as stream:
    for line in stream:
     e=json.loads(line);events+=1;st=e['stage'];current={'orbit':oi,'event':events,'stage':st,'index':e.get('index'),'column':e.get('column')}
     if st in ('diagonals','pivot_row','pivot_saved','checkpoint'):save()
     if st=='restored_checkpoint':
      ck(events==1 and e['pairs']==12 and e['raw_residual_upper']==rest['checkpoint']['raw_residual_upper'] and e['coordinate_radius_squared']==rest['checkpoint']['coordinate_radius_squared'],'first restored checkpoint no replay')
     elif st=='diagonals':
      step=e['step'];ck(type(step)is int and step==len(hp) and 13<=step<=24,'new diagonal step');diag_indices=[]
     elif st=='diagonal':
      ck(e['step']==step and e['index']==len(diag_indices),'current diagonal order');diag_indices.append(e['index'])
     elif st=='diagonals_complete':
      ck(diag_indices==list(range(399)) and e['step']==step,'complete diagonal chronology');diag=e['diagonals']
      for j in selected:ck(diag[j]==[0,0],'selected diagonal zero')
     elif st=='pivot_row':
      ck(e['step']==step and 12<=step<24 and diag is not None,'pivot chronology')
      eligible=[j for j in range(399) if j not in selected and diag[j][0]>0]
      ck(bool(eligible),'positive candidate');chosen=min(eligible,key=lambda j:(-diag[j][0],j));ck(e['index']==chosen,'max lower with literal tie');row_columns=[]
     elif st=='pivot_entry':
      ck(e['step']==step and e['index']==chosen and e['column']==len(row_columns),'current column chronology');row_columns.append(e['column'])
     elif st=='pivot_row_complete':
      ck(row_columns==list(range(399)) and e['index']==chosen and e['step']==step,'complete row chronology');row=e['row'];ck(len(row)==399,'row length')
     elif st=='pivot_saved':
      h={k:e[k] for k in ('index','chirality','r','g','j')};ck(h==saved[len(hp)],'saved history identity');ck(h['index']==chosen and row is not None,'row before pivot')
      ck(h['g']==[x[0] for x in row] and h['j']==[x[1] for x in row],'history is complete row')
      ck(h['r']==[max(diag[chosen][0],row[chosen][0][0]),min(diag[chosen][1],row[chosen][0][1])] and h['r'][0]>0,'positive intersected pivot')
      for j in range(399):
       chi=1 if j>=396 else(-1 if j%2==0 else 1)
       if chi!=h['chirality'] or j in selected:ck(h['g'][j]==[0,0],'known G zero')
       if chi==h['chirality'] or j in selected or j==chosen:ck(h['j'][j]==[0,0],'known J zero')
      hp.append(h);selected.add(chosen);histories+=1;row=None
     elif st=='checkpoint':
      ck(type(e['pairs'])is int and e['pairs']==len(hp) and 13<=e['pairs']<=24,'NEW checkpoint pairs');raw=F(sum((2 if j<396 else 1)*diag[j][1] for j in range(399)),S);ck(raw==F(e['raw_residual_upper']),'independent weighted trace')
      sq=0;coords=e['coordinate_intervals'];ck(len(coords)==len(hp),'coordinates history size')
      for a,h in enumerate(hp):
       for side in range(2):
        for j in range(399):
         x=h['g'][j] if side==0 else[-h['j'][j][1],-h['j'][j][0]]
         z=normalized(x,h['r']);ck(z==coords[a][side][j],'independent Fraction/isqrt normalized coordinate');coordinates+=1;sq+=(2 if j<396 else 1)*z[1]**2
      dsq=F(sq,S*S);ck(dsq==F(e['coordinate_radius_squared']),'independent weighted coordinate error');ck(e['residual_pass']==(raw<=F(1,1062*10**6)) and e['coordinate_pass']==(dsq<=F(1,40000**2)),'independent gates')
   ck(len(hp)==24 and hp==saved and events==ac['orbits'][oi]['event_count'],'fixed complete history');done.append({'orbit':oi,'histories':len(hp),'events':events});save()
  ck(histories==60 and coordinates==885780,'complete reconciliation count')
  stage='post_hashes';current=None;save()
  for p,h in cfg['inputs'].items():ck(sha(p)==h,'final input pin')
  stage='complete';save();(out/'RESULT.json').write_text(json.dumps({'status':'PASS_NEW_SAVED_HISTORY_COORDINATES','predicates':checks,'histories':histories,'coordinates':coordinates,'orbits':done,'source_result_sha256':sha(cfg['result']),'native_entries_replayed':False,'new_pivots_selected':False,'original_gram_loaded':False,'schema_reuse':'source-bound root fullstream schema','all_scientific_targets_met':all(x['status']=='PASS_BOTH' for x in verdict['orbits']),'prior_pilot_seconds':'17.94','continuation_seconds':'21.25','cumulative_physical_seconds':'39.19'},indent=2)+'\n')
 except BaseException as e:
  save();(out/'FAILURE.json').write_text(json.dumps({'stage':stage,'current':current,'predicates':checks,'completed_orbits':done,'histories':histories,'coordinates':coordinates,'error':repr(e)})+'\n');raise
