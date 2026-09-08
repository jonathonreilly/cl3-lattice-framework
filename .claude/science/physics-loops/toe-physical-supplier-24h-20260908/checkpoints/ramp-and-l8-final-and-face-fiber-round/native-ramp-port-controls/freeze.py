from pathlib import Path
import subprocess,json,hashlib,shutil
p=Path(__file__).parent;s=(p/'check.py').read_text();out=[]
for name,replacement in [('wrong_moving_sign','a,k=solve(-1)'),('omit_derivatives','a,k=solve(derivatives=False)'),('static_generator_grading','a,k=solve();a.pop(2)')]:
 q=p/('mutant_'+name+'.py');q.write_text(s.replace('a,k=solve() # MUTATION_SOLVE',replacement+' # MUTATION_SOLVE'))
 r=subprocess.run(['python3','-OO',str(q),'--json'],capture_output=True,text=True,timeout=180)
 (p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr)
 if r.returncode==0:raise RuntimeError('surviving mutant '+name)
 out.append(dict(name=name,exit_code=r.returncode,source_sha256=hashlib.sha256(q.read_bytes()).hexdigest(),failure=r.stderr.splitlines()[-1]))
(p/'MUTATIONS.json').write_text(json.dumps(out,indent=2)+'\n')
a=p/'originals';a.mkdir(exist_ok=True)
for dirname in ['native-ramp-initial-ice-control','native-same-hamiltonian-ramp-root','native-same-hamiltonian-ramp-cold-proof']:
 source=p.parent/dirname;dest=a/dirname;dest.mkdir(exist_ok=True)
 for name in ['DERIVATION.md','PREREGISTRATION.md','check.py','RESULT.json']:
  f=source/name
  if f.exists():shutil.copy2(f,dest/name)
result=json.loads((p/'RESULT.json').read_text())
(p/'REPORT.md').write_text('''# Exact ramp port controls

Standard-library sparse Fraction polynomial jets reproduce the full arbitrary-profile Pauli moving-frame coefficients through order four. The derivative acts on formal jets, rather than sampling profiles. The fourth scalar is (f0^4 + f0 f2)/8; the derivative-driven second generator is retained.

The corrected physical moving-frame transform independently rejects all three altered recursions: reversed moving-frame sign, omitted derivatives, and static grading that deletes the second generator. These are actual isolated -OO subprocess failures. A blanket odd-ice-coefficient deletion is not advertised as a discriminating control: the tested odd coefficients vanish.

Exact beta14 endpoint flatness, four time exponents, and all 18,336 distinct two-edge supports on the full L4 cubic graph are checked. These finite controls support the reviewed analytical proof; they do not establish a dynamical or thermodynamic result by themselves. No canonical files were edited.

Original SymPy helpers and proofs are archived for provenance only; the live helper imports no third-party algebra package. Root's independent helper was not rerun.

Actual predicates: %s. Runtime %.6f s; peak RSS %.3f MiB. Strict CLI, standalone alarm, positive resource cap, and explicit predicates survive -OO.
'''%(result['checks'],result['seconds'],result['rss_mib']))
files={str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p.rglob('*')) if f.is_file() and f.name!='HASHES.json'}
(p/'HASHES.json').write_text(json.dumps(files,indent=2)+'\n')
print(json.dumps(dict(check=result['source_sha256'],report=files['REPORT.md'],checks=result['checks'],seconds=result['seconds'],rss=result['rss_mib'],mutants=out),indent=2))
