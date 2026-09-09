import argparse,json,hashlib,signal,time
from pathlib import Path

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');args=ap.parse_args();signal.alarm(180);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 pins=json.loads((root/'outputs/native_pair_vacuum_chart_2026_09_09_inputs.json').read_text())
 for rel,h in pins.items():
  if hashlib.sha256((root/rel).read_bytes()).hexdigest()!=h:raise ValueError('input '+rel)
 helper=root/'scripts/native_pair_vacuum_chart_controls_2026_09_09.py';ns={'__file__':str(helper),'__name__':'controls'};exec(compile(helper.read_bytes(),str(helper),'exec'),ns);result=ns['result'];result.update({'input_hashes':pins,'actual_current_surface_status':'conditional-support','assembled_review':'pending','elapsed_seconds':time.monotonic()-start});print(json.dumps(result,indent=2))
if __name__=='__main__':main()
