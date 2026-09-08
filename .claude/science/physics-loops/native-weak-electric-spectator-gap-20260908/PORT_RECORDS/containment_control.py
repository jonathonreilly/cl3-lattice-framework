from pathlib import Path
import sys,json,copy,time
P=Path(__file__).resolve().parent
ROOT=next(p for p in P.parents if (p/'scripts/native_weak_electric_rational_core_2026_09_08.py').exists())
sys.path.insert(0,str(ROOT/'scripts'))
from native_weak_electric_rational_core_2026_09_08 import ExactModel
D=ROOT/'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs';f=json.loads((D/'FRAME_RESULT.json').read_text());p=json.loads((D/'PREFIXES.json').read_text());t=time.monotonic();m=ExactModel(f,p)
# Fixed far canonical edge191 is additional valid geometric support, but the
# frozen twenty-dimensional frame does not contain its endpoints.
bad=copy.deepcopy(p);bad['rows'].append({'bridge_edge':191})
try:ExactModel(f,bad)
except ValueError as e:
 if str(e)!='active frame endpoint containment':raise
else:raise RuntimeError('wrong support survived')
print(json.dumps({'baseline_reduction_guards':'pass','actual_wrong_support_mutant':'active frame endpoint containment','fixed_added_edge':191,'seconds':time.monotonic()-t},indent=2))
