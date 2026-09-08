from pathlib import Path
import shutil,json,hashlib
w=Path('/private/tmp/toe-native-dynamical-cycle-dictionary-20260908');base=Path('/private/tmp/toe-24h-probes-20260908')
pack=w/'.claude/science/physics-loops/native-dynamical-cycle-dictionary-20260908';ev=pack/'evidence';ev.mkdir(parents=True,exist_ok=True)
for name in ['native-dynamical-cycle-dictionary','native-charged-cycle-bridge','native-cycle-projected-ice-review','native-common-carrier-cold-review']:
 dest=ev/name;dest.mkdir(exist_ok=True)
 for f in (base/name).iterdir():
  if f.is_file() and f.name!='package.py':shutil.copy2(f,dest/f.name)
# Portable helpers preserve original mathematical bodies and payload fields.
header='''AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
import os,time,signal,resource,argparse,json,hashlib
_PORT_START=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[_key]='1'
'''
footer='''
if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');parser.parse_args()
    _seconds=time.monotonic()-_PORT_START
    _rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if os.uname().sysname=='Darwin' else 1024)
    if not 0<_rss<384 or _seconds>=180:raise RuntimeError('resource contract')
    print(json.dumps(result,indent=2,allow_nan=False))
'''
s=(base/'native-dynamical-cycle-dictionary/check.py').read_text()
s=s.replace("print(json.dumps({'checks':len(checks)","result={'checks':len(checks)")
s=s.replace(".hexdigest()},indent=2,allow_nan=False))",".hexdigest()}")
(w/'scripts/native_dynamical_cycle_dictionary_author_2026_09_08.py').write_text(header+s+footer)
s=(base/'native-common-carrier-cold-review/dictionary_check.py').read_text()
s=s[:s.index("Path(__file__).with_name('DICTIONARY_RESULT.json')")]+"result=out\n"
(w/'scripts/native_dynamical_cycle_dictionary_independent_2026_09_08.py').write_text(header+s+footer)
s=(base/'native-common-carrier-cold-review/check.py').read_text()
s=s[:s.index("Path(__file__).with_name('RESULT.json')")]+"result=out\n"
s=s.replace('assert active>0 and wrong==active',"if not (active>0 and wrong==active):raise RuntimeError('active unsigned adverse')")
s=s.replace('assert nonalternating==14',"if nonalternating!=14:raise RuntimeError('nonalternating adverse')")
(w/'scripts/native_dynamical_cycle_dictionary_exchange_2026_09_08.py').write_text(header+s+footer)
