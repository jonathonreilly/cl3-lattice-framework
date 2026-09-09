#!/usr/bin/env python3
"""Portable supporting proof checks, standard library only."""
import argparse,hashlib,json,signal,time,resource
from pathlib import Path

def main():
 start=time.monotonic();p=argparse.ArgumentParser(description=__doc__);p.add_argument('--json',action='store_true');a=p.parse_args()
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('30s support cap')));signal.alarm(30)
 root=Path(__file__).resolve().parents[1];manifest=root/'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/SOURCE_MANIFEST.json';pins=json.loads(manifest.read_text())['inputs']
 for rel,h in pins.items():
  if hashlib.sha256((root/rel).read_bytes()).hexdigest()!=h:raise ValueError('input identity '+rel)
 helper=root/'scripts/native_gapfree_generator_propagation_2026_09_09_controls.py';data=helper.read_bytes();ns={'__file__':str(helper),'__name__':'supporting_controls'};exec(compile(data,str(helper),'exec'),ns);r=ns['controls']()
 if time.monotonic()-start>=30 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('support resources')
 r.update(claim_status='conditional-support',input_hashes=pins)
 if a.json:print(json.dumps(r,sort_keys=True,indent=2))
 else:print('TOTAL: PASS=%d FAIL=0'%r['predicates'])
if __name__=='__main__':main()
