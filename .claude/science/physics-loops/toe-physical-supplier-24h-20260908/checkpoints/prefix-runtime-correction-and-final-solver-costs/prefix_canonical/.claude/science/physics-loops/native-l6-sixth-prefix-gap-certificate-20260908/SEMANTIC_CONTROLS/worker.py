import sys,json,runpy,signal,resource
from pathlib import Path
from fractions import Fraction as F
signal.alarm(8)
d=Path(__file__).resolve().parent
case=json.loads((d/'CASES.json').read_text())['noncut']
core=runpy.run_path(str(d/(sys.argv[1]+'.py')))
root=Path(sys.argv[2]);p=root/'.claude/science/physics-loops/native-l6-sixth-prefix-gap-certificate-20260908'
adj=json.loads((p/'live_inputs/ADJACENT_CENSUS.json').read_text())
B,R,bi,wi=core['baseline'](adj)
gap,bits=core['gap'](int(case['mask']),case['center'],adj,B,R,bi,wi)
print(json.dumps(dict(case=case,actual=str(gap),bits=bits)),flush=True)
if gap!=F(case['gap_lower']):raise ValueError('actual arithmetic disagrees with exact source row')
if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise RuntimeError('RSS')
