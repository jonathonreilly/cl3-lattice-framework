import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import json,pathlib,math
import numpy as np
from producer import P,ARMS,config,req,sha,verify_freeze,finalrow
from checkpoint import load
from analysis_core import validate_history,stats

def collect(out):
 freeze=verify_freeze();out=pathlib.Path(out);arms=[]
 for arm in range(3):
  rows=[]
  for cid in range(16):
   c=config(arm,cid);total=c['burn']+c['updates'];prev=None;last=None
   for seg in range((total+c['cap']-1)//c['cap']):
    file=out/f'arm{arm}_chain{cid}_segment{seg}.json';z=json.loads(file.read_text());state=out/f'arm{arm}_chain{cid}_segment{seg}.npz'
    req(z['config']==c and z['freeze']==freeze and z['segment']==seg,'identity');req(z['previous_receipt_sha']==prev and z['state_sha']==sha(state),'hash chain');req(z['begin']==seg*c['cap'] and z['stop']==min(total,(seg+1)*c['cap']) and z['final']==(z['stop']==total),'interval');req(0<z['seconds']<180 and 0<z['rss_mib']<384,'resource')
    a,r,s=load(state,expected=c);req(a.n==c['n'] and len(a.faces)==1536 and s['step']==z['stop'],'saved dimensions');req(type(s['runs'])is list and all(type(v)is int and v>=0 for v in s['runs']+[s['run']]) and sum(s['runs'])+len(s['runs'])+s['run']==s['step'],'saved runs')
    req(np.array(s['batch']).shape==(16,9) and np.isfinite(s['batch']).all(),'partial moments');prev=sha(file);last=z
   row=last['row'];req(row==finalrow(s,c),'final accumulator');req(row['cid']==cid and row['seed']==c['seed'] and row['initseed']==c['initseed'],'seeds');validate_history(row,c['n'],c['rk'],c['burn'],c['updates'])
   b=np.array(row['batch_means']);m=np.array(row['mean']);req(b.shape==(16,9) and m.shape==(9,) and np.isfinite(b).all() and np.isfinite(m).all() and np.max(abs(b.mean(0)-m))<1e-8,'means');rows.append(row)
  a=np.array([r['mean'] for r in rows]);z=stats(a);z.update(arm=arm,parameters=ARMS[arm],chain_vectors=a.tolist(),tag_fractions=[r['memory']['fraction'] for r in rows]);z['memory_flag']=max(z['tag_fractions'])>.01;arms.append(z)
 comparisons=[]
 for i,j in [(0,2),(1,2)]:
  for a,b in zip(arms[i]['rows'],arms[j]['rows']):
   if a['valid'] and b['valid']:
    for k in ['D','R','correction']:
     d=a[k]-b[k];se=math.hypot(a[k+'_SE'],b[k+'_SE']);comparisons.append(dict(arms=[i,j],harmonic=a['harmonic'],quantity=k,difference=d,SE=se,flag=abs(d)>4*se))
 status='fails_diagnostics' if any(a['memory_flag'] or any(not r.get('D_precision',False) for r in a['rows']) for a in arms) or any(c['flag'] for c in comparisons) else 'passes_limited_diagnostics_not_convergence'
 baseline=json.loads((P/'L4_BASELINE_ANALYSIS.json').read_text());pin=json.loads((P/'L4_BASELINE.json').read_text());membership=json.loads((P/'L4_BASELINE_RAW_MEMBERSHIP.json').read_text())
 req(sha(P/'L4_BASELINE_ANALYSIS.json')==pin['analysis_sha']==membership['ANALYSIS.json'] and sha(P/'L4_BASELINE_POST_REVIEW.md')==pin['post_review_sha'],'baseline pins')
 req(len(baseline['arms'])==4 and baseline['arms'][1]['parameters']==[12,512,32] and baseline['arms'][3]['parameters']==[36,512,32],'baseline parameters')
 size=[]
 for i,j in [(0,1),(2,3)]:
  a=arms[i]['rows'][1];b=baseline['arms'][j]['rows'][0];req(a['harmonic']==2 and b['harmonic']==1,'matched momentum')
  for k in ['D','R','correction']:
   valid=a['valid'] and b['valid'];size.append(dict(L8_arm=i,L4_arm=j,quantity=k,valid=bool(valid),difference=a[k]-b[k] if valid else None,SE=math.hypot(a[k+'_SE'],b[k+'_SE']) if valid else None,scope='size contrast; not a pass gate'))
 return dict(arms=arms,comparisons=comparisons,matched_L4_size_contrasts=size,status=status,segments_are_not_independent=True)
if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);v=ap.parse_args();d=pathlib.Path(v.out);result=collect(d)
 with (d/'ANALYSIS.json').open('x') as f:json.dump(result,f,indent=2,allow_nan=False)
