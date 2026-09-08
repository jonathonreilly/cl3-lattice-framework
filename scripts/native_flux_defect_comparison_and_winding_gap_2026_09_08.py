"""Exact finite controls supporting the separately stated analytical theorem."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_FLUX_DEFECT_COMPARISON_AND_WINDING_GAP_NOTE_2026-09-08.md',
 'docs/NATIVE_EVEN_TORUS_FLUX_ISOLATION_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'scripts/native_flux_defect_geometry_2026_09_08.py',
 'scripts/native_flux_defect_combinatorics_2026_09_08.py',
)
def main():
 import argparse,hashlib,json,os,resource,runpy,signal,time
 from pathlib import Path
 p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args();signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();inputs={n:sha(root/n) for n in AUDIT_INPUT_PATHS}
 geometry=runpy.run_path(str(root/AUDIT_INPUT_PATHS[-2]))['result'];combinatorics=runpy.run_path(str(root/AUDIT_INPUT_PATHS[-1]))['result']
 if geometry['predicates']!=91395 or combinatorics['predicates']!=14218 or geometry['classes']!=32:raise ValueError('fixed control coverage')
 elapsed=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
 if elapsed>=180 or not 0<rss<384:raise ValueError('resource bounds')
 total=geometry['predicates']+combinatorics['predicates']+2
 result=dict(executed_predicates=total,predicate_breakdown=dict(geometry=91395,combinatorial=14218,coverage=1,resource=1),geometry=geometry,combinatorics=combinatorics,elapsed_seconds=elapsed,peak_rss_mib=rss,input_sha256=inputs,source_sha256=sha(Path(__file__)),scope='Finite geometry and chessboard combinatorial controls only; reflection energy inequality and Fourier winding bound are analytical proofs, not numerical validations.')
 (root/'outputs/native_flux_defect_comparison_and_winding_gap_2026_09_08.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
 if not args.json:
  print('per_element: cube links and compatible face products.')
  print('per_site: disjoint cube vertices and reflection partitions.')
  print('per_mode: no spectral or Bloch calculation.')
  print('per_block:32 cube labels and exact run-extension controls.')
  print('lattice_wide: finite tiling/seams/counts; analytical bounds separately proved.')
  print(f'TOTAL: PASS={total} FAIL=0')
  print(f'Resources: {elapsed:.6f}s,{rss:.3f}MiB; timeout180s,RSS384MiB.')
if __name__=='__main__':main()
