from pathlib import Path
import subprocess,json,hashlib
w=Path('/private/tmp/toe-admissibility-plane-formation-20260908');p=w/'.claude/science/physics-loops/admissibility-plane-formation-20260908'
n=w/'docs/ADMISSIBILITY_PLANE_FORMATION_DIAGONAL_INTERACTION_NOTE_2026-09-08.md'
s=n.read_text().replace('These references were supplied as prior-art pointers; their full papers were not read for this proof,','The 1998 paper’s abstract and introductory definitions were inspected; the DOI lookup failed. Their full papers were not read for this proof,')
insert='''## Corner-mixture comparison

Any convex mixture of the two plane laws retains the same all-equal eight-site conditional displayed above: reflection fixes this boundary configuration and the center, so both component laws give identical joint and boundary probabilities there. Their mixture therefore gives the same conditional. For nonconstant weights it still differs from the original axial specification. This statement concerns only these two laws, not arbitrary formation orders. The equal mixture is invariant under square-lattice rotations and reflections because those transformations either preserve or exchange the two diagonal classes; that restored spatial symmetry does not remove the conditional discrepancy.

'''
s=s.replace('## No-Go Discipline Gate',insert+'## No-Go Discipline Gate');n.write_text(s)
r=w/'scripts/admissibility_plane_formation_diagonal_interaction_2026_09_08.py'
mut=p/'mutations';mut.mkdir(exist_ok=True)
code=r.read_text();reports=[]
for name,old,new in [('omit_normalizer','if i and j:n*=l//h[x[i*W+j-1]][x[(i-1)*W+j]]','if i and j:n*=l'),('one_center_normalizer','F(phi[s][0]**4,h[s][0]**2)','F(phi[s][0]**4,h[s][0])')]:
 if code.count(old)!=1:raise RuntimeError('mutation anchor')
 m=mut/(name+'.py');m.write_text(code.replace(old,new))
 driver="import sys; sys.argv=['runner','--json']; exec(compile(open(%r).read(),%r,'exec'),{'__file__':%r,'__name__':'__main__'})"%(str(m),str(m),str(r))
 x=subprocess.run(['python3','-O','-c',driver],capture_output=True,text=True,timeout=180)
 (mut/(name+'.stdout')).write_text(x.stdout);(mut/(name+'.stderr')).write_text(x.stderr)
 if x.returncode==0 or 'control failed' not in x.stderr:raise RuntimeError('mutant survived or unrelated failure')
 reports.append(dict(name=name,returncode=x.returncode,sha256=hashlib.sha256(m.read_bytes()).hexdigest()))
(p/'MUTATION_RECORD.json').write_text(json.dumps(reports,indent=2)+'\n')
x=subprocess.run(['python3','-O',str(r),'--json'],capture_output=True,text=True,timeout=180,check=True)
(p/'LIVE_RESULT.json').write_text(x.stdout);(p/'LIVE_STDERR.txt').write_text(x.stderr)
y=subprocess.run(['python3',str(r)],capture_output=True,text=True,timeout=180,check=True)
(p/'LIVE_STDOUT.txt').write_text(y.stdout)
orig=json.loads((p/'evidence/original/result.json').read_text());now=json.loads(x.stdout)
for k in ('fixtures','checks','elimination_schedules','scope'):
 if orig[k]!=now[k]:raise RuntimeError('scientific drift')
(p/'PORT_RECEIPT.json').write_text(json.dumps(dict(scientific_fields_unchanged=['fixtures','checks','elimination_schedules','scope'],checks=now['checks'],source_sha256=hashlib.sha256(n.read_bytes()).hexdigest(),runner_sha256=hashlib.sha256(r.read_bytes()).hexdigest(),mathematical_scope='Proof plus finite controls, not full plane census; parent opposite-corner theorem unchanged'),indent=2)+'\n')
