from pathlib import Path
import subprocess,sys,difflib,json
p=Path(__file__).resolve().parent;text=(p/'pilot.py').read_text();out=[]
for name,old,new in [('omit_stagger','(-1)**sum(r)*np.exp','np.exp'),('wrong_plane','planes.append(orient.index(tuple(sorted((a,b)))))','planes.append(0)')]:
 assert text.count(old)==1;s=text.replace(old,new);f=p/(name+'.py');f.write_text(s);(p/(name+'.diff')).write_text(''.join(difflib.unified_diff(text.splitlines(True),s.splitlines(True),fromfile='pilot.py',tofile=f.name)))
 r=subprocess.run([sys.executable,str(f),'--micro'],capture_output=True,text=True,timeout=30);(p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr)
 out.append({'name':name,'exit':r.returncode,'last_error':r.stderr.strip().splitlines()[-1]if r.stderr else None})
(p/'mutations.json').write_text(json.dumps(out,indent=2)+'\n')
