AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_ZERO_PENALTY_L6_FLUX_ISOLATION_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'scripts/native_zero_penalty_l6_flux_exact_2026_09_08.py',
)
import argparse,hashlib,json,os,resource,runpy,signal,time
from pathlib import Path

def main():
 start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
 p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
 root=Path(__file__).resolve().parents[1];sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();inputs={n:sha(root/n) for n in AUDIT_INPUT_PATHS}
 part=runpy.run_path(str(root/'scripts/native_zero_penalty_l6_flux_exact_2026_09_08.py'))['out']
 if part['rank']!=108 or part['det_mod_prime']!=88:raise RuntimeError('live faithful-cut certificate')
 seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
 if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
 out={'executed_predicates':part['checks']+2,'modular_certificate':part,'source_sha256':sha(Path(__file__)),'input_sha256':inputs,'elapsed_seconds':seconds,'peak_rss_mib':rss,'scope':'Supplied uniform finite L6 unique minimizing flux orbit through linked proof; existential wrong-orbit separation only, no numerical gap or native ground uniqueness.'}
 (root/'outputs/native_zero_penalty_l6_flux_isolation_2026_09_08.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
 if not args.json:
  print('per_element: exact canonical skew edge signs and magnitudes.')
  print('per_site: all216 sites and the108-site coordinate half.')
  print('per_mode: linked exact spectrum and valid modular root images.')
  print('per_block: all108 pivots and nonzero cross-correlation determinant.')
  print('lattice_wide: supplied L6 reflection equality and faithful-child proof premises.')
  print(f"TOTAL: PASS={out['executed_predicates']} FAIL=0")
  print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
if __name__=='__main__':main()
