"""Finalize a prevalidated cost receipt using root's /usr/bin/time -lp output.
This small read-only arithmetic/publication step is post-profile bookkeeping,
not another timing experiment or a rerun of the fixture.
"""
import pathlib,json,hashlib,re,math,argparse
from forecast import price
B=pathlib.Path(__file__).resolve().parent

def finish(out,time_file):
 out=pathlib.Path(out);time_file=pathlib.Path(time_file)
 dispatch=json.loads((out/'DISPATCH.json').read_text());raw=(out/'FORECAST_PENDING_OUTER.json').read_bytes()
 if dispatch['exit']!=0 or dispatch['freeze']!=hashlib.sha256((B/'FINAL_FREEZE.json').read_bytes()).hexdigest() or dispatch['forecast_pending_sha']!=hashlib.sha256(raw).hexdigest():raise ValueError('dispatch binding')
 text=time_file.read_text();matches=re.findall(r'^real\s+([0-9]+(?:\.[0-9]+)?)\s*$',text,re.M)
 if len(matches)!=1:raise ValueError('unique POSIX real time')
 seconds=float(matches[0]);charged=seconds+0.01
 if not math.isfinite(seconds) or seconds<=0:raise ValueError('real time')
 result=price(json.loads(raw),charged)
 result.update(outer_time_file=str(time_file.resolve()),outer_time_sha=hashlib.sha256(time_file.read_bytes()).hexdigest(),printed_real_seconds=seconds,rounding_allowance_seconds=.01,within_30_seconds=charged<=30,measurement_boundary='/usr/bin/time wraps Python startup, dispatch, validation and pending-forecast serialization; final scalar receipt bookkeeping is separate')
 (out/'FORECAST.json').write_text(json.dumps(result,indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--time-file',required=True);a=p.parse_args();r=finish(a.out,a.time_file);print(json.dumps(r));raise SystemExit(0 if r['within_30_seconds'] else 1)
