"""Supporting finite controls for the analytic full odd-star infrared theorem."""
AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS=('docs/NATIVE_FULL_STAR_INFRARED_RESPONSE_NOTE_2026-09-09.md', 'docs/NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md', 'docs/NATIVE_UNIFORM_QUASILOCAL_STAR_VERTEX_NOTE_2026-09-09.md', 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md', 'scripts/native_full_star_infrared_controls_2026_09_09.py')
def main():
 import argparse,json,hashlib,signal,time,resource
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.parse_args();signal.alarm(30);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
 helper=root/AUDIT_INPUT_PATHS[-1];data=helper.read_bytes();ns={'__name__':'controls','__file__':str(helper)};exec(compile(data,str(helper),'exec'),ns);out=ns['record']
 if out['FAIL'] or out['PASS']!=748:raise ValueError('supporting control count')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if rss>384*1048576:raise ValueError('memory cap')
 out.update(status='PASS',input_sha256=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start,peak_rss_bytes=rss,actual_current_surface_status='conditional-support')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
