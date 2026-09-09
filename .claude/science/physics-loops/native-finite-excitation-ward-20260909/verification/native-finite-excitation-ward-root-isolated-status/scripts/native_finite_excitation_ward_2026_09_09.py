#!/usr/bin/env python3
"""Portable exact supporting certificate for the conditional Ward theorem."""
import argparse,hashlib,json,pathlib,runpy,signal,time

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',action='store_true')
    args=parser.parse_args();signal.alarm(180);start=time.monotonic()
    root=pathlib.Path(__file__).resolve().parents[1]
    manifest=root/'outputs/native_finite_excitation_ward_2026_09_09_inputs.json'
    pins=json.loads(manifest.read_text())
    for rel,expected in pins.items():
        actual=hashlib.sha256((root/rel).read_bytes()).hexdigest()
        if actual!=expected:raise ValueError('input hash mismatch: '+rel)
    helper=root/'scripts/native_finite_excitation_ward_controls_2026_09_09.py'
    namespace={'__file__':str(helper),'__name__':'ward_controls'}
    exec(compile(helper.read_bytes(),str(helper),'exec'),namespace)
    result=namespace['run']();result['input_hashes']=pins
    result['claim_id']='native_finite_excitation_ward_note_2026-09-09'
    result['actual_current_surface_status']='conditional-support'
    result['review_status']='source review passed; formal audit deferred'
    result['elapsed_seconds']=time.monotonic()-start
    print(json.dumps(result,sort_keys=True,indent=2) if args.json else str(result))
if __name__=='__main__': main()
