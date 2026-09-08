from pathlib import Path
import json,subprocess,sys,shutil
p=Path(__file__).resolve().parent;src=p.parent/'detuned-energy-moment';q=p/'zero_denominator_fixture';q.mkdir(exist_ok=True)
shutil.copyfile(src/'analyze_production.py',q/'analyze_production.py');shutil.copyfile(src/'RESULT.json',q/'RESULT.json')
for pop in [1024,2048]:
 for vi,V in enumerate([.93,.94,.95,.96,.97]):
  reps=[]
  for r in range(16):
   reps.append({'replica':r,'mixed_energy':(V-1)*8,'count_samples_last40':[8]*40,'postconditions':[{'fixture':True}],'blocks':([{'F':F,'C0_six':[0]*6} for origin in range(4) for F in [6,12]] if vi==2 else [])})
  (q/f'production_p{pop}_v{vi}.json').write_text(json.dumps({'V':V,'population':pop,'replicas':reps,'rss_mib':1,'seconds':1}))
r=subprocess.run([sys.executable,str(q/'analyze_production.py')],capture_output=True,text=True);(q/'stdout').write_text(r.stdout);(q/'stderr').write_text(r.stderr);assert r.returncode==0
x=json.loads((q/'PRODUCTION_ANALYSIS.json').read_text());assert not x['population_comparison']['valid']
for v in x['populations'].values():
 assert all(not m['valid'] for m in v['moments'])
 assert v['denominator_diagnostics']['6']['nonpositive_origin_count']==64
(p/'ANALYSIS_ADVERSE_RESULT.json').write_text(json.dumps({'synthetic_fixture_not_physics':True,'zero_denominator_retained_invalid':True,'exit':r.returncode},indent=2)+'\n')
