"""Exact local controls for the supplied-model weak-electric density theorem."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_WEAK_ELECTRIC_DEFECT_DENSITY_NOTE_2026-09-08.md',
 'docs/NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'scripts/native_weak_electric_defect_density_controls_2026_09_08.py',
)
def main():
 import argparse,json,hashlib,runpy,signal,time,resource
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.parse_args();signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 inputs={x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in AUDIT_INPUT_PATHS}
 result=runpy.run_path(str(root/AUDIT_INPUT_PATHS[-1]))['check']()
 if result['checks']!=107 or result['ground_density_coefficient']!='102400/387' or result['thermal_density_coefficient']!='800':raise ValueError('claim-local controls')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if rss>384*1048576:raise RuntimeError('384MiB RSS')
 result.update(input_sha256=inputs,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start,peak_rss_bytes=rss,scope='Exact local controls supporting the separate full analytical theorem; no perturbed-state solve or phase claim.')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
