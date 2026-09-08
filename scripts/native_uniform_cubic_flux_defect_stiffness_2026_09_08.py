"""Portable exact replay of the complete supplied dyadic spectral certificate."""
AUDIT_TIMEOUT_SEC=180
PACK='.claude/science/physics-loops/native-uniform-cubic-flux-defect-stiffness-20260908'
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'docs/NATIVE_FLUX_DEFECT_COMPARISON_AND_WINDING_GAP_NOTE_2026-09-08.md',
 'docs/NATIVE_EVEN_TORUS_FLUX_ISOLATION_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md',
 'scripts/native_uniform_cubic_flux_matrix_2026_09_08.py',
 'scripts/native_uniform_cubic_flux_certificate_2026_09_08.py',
 PACK+'/RAW_CANDIDATES/MANIFEST.json',
 PACK+'/RAW_CANDIDATES/CUBE_INPUTS.json',
 PACK+'/RAW_CANDIDATES/TRIG_INPUTS.json',
 PACK+'/RAW_CANDIDATES/ACCEPTED_ANALYSIS.json',
)+tuple(PACK+f'/RAW_CANDIDATES/job{j:02d}.jsonl.gz' for j in range(24))

def main():
 import argparse,json,hashlib,gzip,runpy,signal,time,resource,os,math
 from pathlib import Path
 from fractions import Fraction as F
 from itertools import product
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');args=ap.parse_args();signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 def require(ok,msg):
  if not ok:raise ValueError(msg)
 def sha(path):
  h=hashlib.sha256()
  with path.open('rb') as f:
   for part in iter(lambda:f.read(1<<20),b''):h.update(part)
  return h.hexdigest()
 inputs={name:sha(root/name) for name in AUDIT_INPUT_PATHS};raw=root/PACK/'RAW_CANDIDATES';manifest=json.loads((raw/'MANIFEST.json').read_text());cubes=json.loads((raw/'CUBE_INPUTS.json').read_text());trig=json.loads((raw/'TRIG_INPUTS.json').read_text())
 require(trig['grid_n']==32 and [r['j'] for r in trig['rows']]==list(range(32)),'trig coverage')
 require(manifest['source_freeze']=='09bc556a79a4a64488bfa1a59caef7b97afee37f298273d97fb4a2d817dda636' and len(manifest['jobs'])==24,'accepted source/job manifest')
 require(manifest['cube_sha']==sha(raw/'CUBE_INPUTS.json') and manifest['trig_sha']==sha(raw/'TRIG_INPUTS.json'),'input bindings')
 build=runpy.run_path(str(root/'scripts/native_uniform_cubic_flux_matrix_2026_09_08.py'))['build'];certify=runpy.run_path(str(root/'scripts/native_uniform_cubic_flux_certificate_2026_09_08.py'))['certificate'];reps=(0,1,3,5,10,15);sums={r:[F(0),F(0)] for r in reps};counts={r:0 for r in reps};ledger=[];predicates=0
 for job,m in enumerate(manifest['jobs']):
  rep=reps[job//4];name=f'job{job:02d}.jsonl.gz';require((m['job'],m['rep'],m['block'],m['nodes'],m['file'])==(job,rep,job%4,1024,name),'job identity');p=raw/name;require(p.stat().st_size==m['compressed_bytes'] and sha(p)==m['compressed_sha'],'compressed binding');h=hashlib.sha256();size=0;count=0;expected=iter(product(range(4*(job%4),4*(job%4)+4),range(16),range(16)))
  with gzip.open(p,'rb') as file:
   for line in file:
    h.update(line);size+=len(line)
    try:index=next(expected)
    except StopIteration:raise ValueError('extra node') from None
    row=json.loads(line);require((row['job'],row['rep'],tuple(row['index']))==(job,rep,index),'node identity');predicates+=1
    ev=[float.fromhex(x) for x in row['eigenvalues_hex']];Q=[[complex(float.fromhex(a),float.fromhex(b)) for a,b in line] for line in row['vectors_hex']];require(len(ev)==16 and ev==sorted(ev) and all(math.isfinite(x) for x in ev),'eigenvalue schema')
    D,radius=build(cubes['rows'][rep],[trig['rows'][j] for j in index]);actual=certify(D,Q,ev,radius);require(actual==row['certificate'],'complete exact certificate mismatch');predicates+=1
    sums[rep][0]+=F(actual['density_lower']);sums[rep][1]+=F(actual['density_upper']);counts[rep]+=1;count+=1
  require(count==1024 and size==m['decompressed_bytes'] and h.hexdigest()==m['decompressed_sha'],'decompressed coverage/hash');predicates+=1;ledger.append(dict(job=job,nodes=count,compressed_sha=m['compressed_sha'],decompressed_sha=m['decompressed_sha']))
 require(set(counts.values())=={4096},'complete folded grid');predicates+=1;densities={r:[a/4096,b/4096] for r,(a,b) in sums.items()};pi=F(trig['pi_upper_numerator'],trig['pi_denominator']);error=3*pi*pi/(8*32**2);comparison=[]
 for rep in reps[:-1]:
  m=cubes['rows'][rep]['defects'];require(m in (2,4,6),'defect count');a=densities[rep][0]-densities[15][1]-error;b=densities[rep][1]-densities[15][0]+error;comparison.append(dict(rep=rep,defects=m,lower=str(a),upper=str(b),positive=a>0,limiting_delta_lower=str(8*a/m),auxiliary_defect_coefficient_lower=str(2*a/m),native_half_objective_defect_coefficient_lower=str(a/m)));predicates+=1
 accepted=json.loads((raw/'ACCEPTED_ANALYSIS.json').read_text());require(len(accepted['costs'])==5 and accepted['freeze']==manifest['source_freeze'] and accepted['node_count']==24576,'accepted analysis identity');require(accepted['grid_density_intervals']=={str(r):[str(a),str(b)] for r,(a,b) in densities.items()},'accepted exact grid sums');require(F(accepted['quadrature_difference_radius'])==error,'accepted quadrature');predicates+=2
 for c,old in zip(comparison,accepted['costs']):
  require(c['rep']==old['rep'] and c['lower']==old['density_lower'] and c['upper']==old['density_upper'] and c['positive']==old['strictly_positive'] and c['limiting_delta_lower']==old['limiting_delta_lower'] and c['auxiliary_defect_coefficient_lower']==old['auxiliary_defect_coefficient_lower'] and c['native_half_objective_defect_coefficient_lower']==old['native_half_objective_defect_coefficient_lower'],'accepted comparison');predicates+=1
 common_lower=min(F(c['lower']) for c in comparison);delta_lower=min(F(c['limiting_delta_lower']) for c in comparison)
 require(common_lower>=F(17,1000),'derived common density floor17/1000');require(delta_lower>=F(3,50),'derived limiting delta floor3/50');predicates+=2
 elapsed=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024);require(elapsed<180 and 0<rss<=384,'canonical resource cap');predicates+=1
 result=dict(executed_predicates=predicates,predicate_breakdown=dict(node_identity=24576,complete_exact_certificate=24576,decompressed_job_binding=24,folded_coverage=1,defect_domain=5,accepted_analysis_binding=2,accepted_comparison_binding=5,derived_theorem_floors=2,resource=1),node_count=sum(counts.values()),original_node_count=8*sum(counts.values()),grid_n=32,folded_n=16,grid_density_intervals={r:[str(a),str(b)] for r,(a,b) in densities.items()},quadrature_difference_radius=str(error),comparisons=comparison,all_five_positive=all(c['positive'] for c in comparison),common_density_lower=str(common_lower),common_limiting_delta_lower=str(delta_lower),derived_rounded_bounds=dict(common_density_lower='17/1000',limiting_delta_lower='3/50',scope='derived after independently accepted full grid; not initial-run acceptance thresholds'),job_ledger=ledger,input_sha256=inputs,source_sha256=sha(Path(__file__)),elapsed_seconds=elapsed,peak_rss_mib=rss,scope='Full exact finite dyadic arithmetic replay; analytical Clifford/quadrature/flux proofs and rational sine enclosures5a86 remain separately imported proof inputs; this runner does not regenerate sine intervals.')
 output=root/'outputs/native_uniform_cubic_flux_defect_stiffness_2026_09_08.json';output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));require(result['all_five_positive'],'positive density comparisons not certified')
 if not args.json:print(f'TOTAL: PASS={predicates} FAIL=0; exact nodes={sum(counts.values())}')
if __name__=='__main__':main()
