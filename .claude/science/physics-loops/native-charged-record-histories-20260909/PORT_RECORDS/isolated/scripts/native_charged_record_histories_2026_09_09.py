"""Portable exact finite controls; no physical stochastic run."""
AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_CHARGED_RECORD_HISTORIES_NOTE_2026-09-09.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
 'scripts/native_charged_record_history_controls_2026_09_09.py',
 'scripts/native_charged_record_history_car_2026_09_09.py',
)
def main():
 import argparse,json,hashlib,time,signal,resource,sys
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.parse_args();signal.alarm(30);t=time.monotonic();root=Path(__file__).resolve().parents[1]
 hashes={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS};results=[]
 for n in AUDIT_INPUT_PATHS[-2:]:
  p=root/n;data=p.read_bytes()
  if hashlib.sha256(data).hexdigest()!=hashes[n]:raise ValueError('source changed')
  ns={'__name__':'controls','__file__':str(p)};exec(compile(data,str(p),'exec'),ns);results.append(ns['check']())
 if results[0]['status']!='PASS' or results[0]['history_columns']!=736 or results[0]['omitted_phase_mutant_failures']!=80 or results[1]['checks']!=146:raise ValueError('coverage')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if sys.platform!='darwin':rss*=1024
 if rss>384*1048576 or time.monotonic()-t>=30:raise ValueError('resource cap')
 print(json.dumps(dict(status='PASS',actual_current_surface_status='conditional-support',controls=results,input_sha256=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-t,peak_rss_bytes=rss),indent=2))
if __name__=='__main__':main()
