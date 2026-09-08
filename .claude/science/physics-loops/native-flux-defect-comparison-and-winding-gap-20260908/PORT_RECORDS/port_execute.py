from pathlib import Path
import ast,shutil,json,hashlib,subprocess,sys,time
W=Path('/private/tmp/toe-native-flux-defect-comparison-and-winding-gap-20260908');O=Path(__file__).parent;P=W/'.claude/science/physics-loops/native-flux-defect-comparison-and-winding-gap-20260908/PORT_RECORDS';D=O/'isolated';D.mkdir(exist_ok=False);primary='scripts/native_flux_defect_comparison_and_winding_gap_2026_09_08.py'
t=ast.parse((W/primary).read_text());inputs=next(ast.literal_eval(n.value) for n in t.body if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='AUDIT_INPUT_PATHS' for x in n.targets));pins={}
for name in (primary,*inputs):
 f=D/name;f.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(W/name,f);pins[name]=hashlib.sha256(f.read_bytes()).hexdigest()
(D/'outputs').mkdir();(P/'ISOLATED_INPUTS.json').write_text(json.dumps(pins,indent=2)+'\n');tick=time.monotonic()
r=subprocess.run(['/usr/bin/time','-lp',sys.executable,'-I','-OO',str(D/primary),'--json'],capture_output=True,text=True,timeout=180,cwd=D)
(P/'ISOLATED.stdout').write_text(r.stdout);(P/'ISOLATED.stderr').write_text(r.stderr)
if r.returncode:raise ValueError(r.stderr)
z=json.loads(r.stdout);out='outputs/native_flux_defect_comparison_and_winding_gap_2026_09_08.json';shutil.copyfile(D/out,W/out)
if z['executed_predicates']!=105615:raise ValueError('counts')
for key in ('geometry','combinatorics'):
 old=json.loads((O/('GEOMETRY.json' if key=='geometry' else 'COMBINATORICS.json')).read_text());a=dict(z[key]);a.pop('seconds');old.pop('seconds')
 if a!=old:raise ValueError('science port')
(P/'ISOLATION_RECEIPT.json').write_text(json.dumps(dict(returncode=0,seconds=time.monotonic()-tick,files=len(pins),exact_science_equal=True,output_sha256=hashlib.sha256((D/out).read_bytes()).hexdigest()),indent=2)+'\n')
r=subprocess.run([sys.executable,'-OO',str(D/primary),'--unknown'],capture_output=True,text=True,timeout=180);(P/'INVALID_CLI.stderr').write_text(r.stderr)
if r.returncode!=2:raise ValueError('strict CLI')
# Actual isolated canonical mutant: source/output input hashes reflect altered helper.
M=O/'canonical_seam_mutant';shutil.copytree(D,M);f=M/'scripts/native_flux_defect_geometry_2026_09_08.py';s=f.read_text();f.write_text(s.replace('ans*=(-1)**(dims[a]//4+1)','ans*=1'));r=subprocess.run([sys.executable,'-I','-OO',str(M/primary),'--json'],capture_output=True,text=True,timeout=180,cwd=M);(P/'CANONICAL_SEAM_MUTANT.stdout').write_text(r.stdout);(P/'CANONICAL_SEAM_MUTANT.stderr').write_text(r.stderr)
if not r.returncode or 'canonical real hopping winding' not in r.stderr:raise ValueError('mutant survives')
(P/'CANONICAL_MUTATION.json').write_text(json.dumps(dict(returncode=r.returncode,helper_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),predicate='canonical real hopping winding',hash_gate=False),indent=2)+'\n')
print(z['executed_predicates'],z['elapsed_seconds'],z['peak_rss_mib'])
