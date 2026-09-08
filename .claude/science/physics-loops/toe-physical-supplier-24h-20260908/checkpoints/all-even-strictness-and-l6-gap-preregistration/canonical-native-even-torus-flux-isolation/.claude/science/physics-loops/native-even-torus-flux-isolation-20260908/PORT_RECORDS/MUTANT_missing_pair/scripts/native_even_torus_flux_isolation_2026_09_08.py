"""Exact finite lemma controls supporting the analytical all-even flux theorem."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_EVEN_TORUS_FLUX_ISOLATION_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'scripts/native_even_torus_flux_isolation_controls_2026_09_08.py')
EXPECTED_INPUT_SHA256={'docs/NATIVE_EVEN_TORUS_FLUX_ISOLATION_NOTE_2026-09-08.md': '7cf79e48fd3bc070a95b1f81b52e6c21ae0ca212225b25a5713ca5598f6928e0', 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md': '1a61b1c79b351343c88b619a454d2f2c03565e64d1c738f198fa90586831e042', 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md': 'c689445a96134275fe75190ca3858fc61cc59d323393182ad549044a8c3c4c04', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md': '3d61dfac1a844364b98c731efca34b27b3c8dac1a3049d519f26d97b1db12715', 'scripts/native_even_torus_flux_isolation_controls_2026_09_08.py': '705b0c585b31ad4ae2850871b3319fc7813d3b90c971b53235d742c759e00b1f'}
import argparse,hashlib,json,os,resource,runpy,signal,time
from pathlib import Path

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args();signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic()
 root=Path(__file__).resolve().parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();inputs={n:sha(root/n) for n in AUDIT_INPUT_PATHS}
 if inputs!=EXPECTED_INPUT_SHA256:raise RuntimeError('declared input hash changed')
 mod=runpy.run_path(str(root/'scripts/native_even_torus_flux_isolation_controls_2026_09_08.py'));checks=mod['run']()
 if checks!=5955:raise RuntimeError('control coverage')
 seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
 if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
 result={'executed_predicates':checks+2,'lemma_predicates':checks,'coverage_guard':1,'resource_guard':1,'half_widths':list(range(2,9)),'transverse_extents':[4,6],'elapsed_seconds':seconds,'peak_rss_mib':rss,'source_sha256':sha(Path(__file__)),'input_sha256':inputs,'scope':'Exact finite controls for complex SVD equality, paired-channel kernel positivity and structural layer/gauge induction. The linked analytical proof establishes all even sizes; finite tested widths do not prove the theorem by extrapolation.'}
 (root/'outputs/native_even_torus_flux_isolation_2026_09_08.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
 if not args.json:
  print('per_element: exact complex rational channels and phases.')
  print('per_site: boundary and inward-frontier mode propagation.')
  print('per_mode: CAR kernel and reflected-matrix identities.')
  print('per_block: fixed rectangular half-slab controls.')
  print('lattice_wide: analytical induction in the linked note; finite controls only.')
  print(f'TOTAL: PASS={checks+2} FAIL=0')
  print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
if __name__=='__main__':main()
