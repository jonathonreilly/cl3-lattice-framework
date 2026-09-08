from pathlib import Path
import subprocess,sys,json,difflib,shutil
p=Path(__file__).resolve().parent;s=(p/'tilted_kernel.py').read_text();v=(p/'verify_kernel.py').read_text();rows=[]
for name,a,b in [('bad_cache','O[m]+=delta','O[m]+=0.'),('bad_tilt','return 1.0-delta_v*count/M+(shift-lam*xvalue)/M','return 1.0-delta_v*count/M')]:
 assert s.count(a)==1;t=s.replace(a,b);(p/(name+'.py')).write_text(t);(p/(name+'.diff')).write_text(''.join(difflib.unified_diff(s.splitlines(True),t.splitlines(True))));f=p/('verify_'+name+'.py');f.write_text(v.replace('from tilted_kernel import','from '+name+' import'));r=subprocess.run([sys.executable,str(f)],capture_output=True,text=True,timeout=180);(p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr);rows.append({'case':name,'exit':r.returncode,'actual_assertion':'AssertionError' in r.stderr})
q=p/'synthetic_zero_source_response';q.mkdir(exist_ok=True);shutil.copyfile(p/'analyze_production.py',q/'analyze_production.py');shutil.copyfile(p/'RESULT.json',q/'RESULT.json')
cases=[(.93,0.),(.95,0.),(.97,0.),(.95,-.02),(.95,.02),(.95,-.01),(.95,.01)]
for pi,pop in enumerate([1024,2048]):
 for c,(V,lam) in enumerate(cases):
  E=(V-1)*8;reps=[{'replica':r,'seed':3400000+10000*pi+r,'postconditions':True,'Nf_window':[8]*40,'X_window':[0]*40,'energy_window':[E]*40,'physical_energy':E,'shifted_energy':E-12*abs(lam),'cache_drift':0} for r in range(16)];(q/f'production_p{pop}_c{c}.json').write_text(json.dumps({'V':V,'lambda':lam,'population':pop,'shift':12*abs(lam),'seconds':1,'rss_mib':1,'replicas':reps}))
r=subprocess.run([sys.executable,str(q/'analyze_production.py')],capture_output=True,text=True);(q/'stdout').write_text(r.stdout);(q/'stderr').write_text(r.stderr);assert r.returncode==0;x=json.loads((q/'PRODUCTION_ANALYSIS.json').read_text());assert not x['population_comparison']['valid'];assert all(not z['valid'] for y in x['populations'].values() for z in y['moments']);rows.append({'case':'synthetic_zero_source_response','exit':0,'explicit_invalid':True})
(p/'IMPLEMENTATION_ADVERSE_RESULT.json').write_text(json.dumps(rows,indent=2)+'\n')
