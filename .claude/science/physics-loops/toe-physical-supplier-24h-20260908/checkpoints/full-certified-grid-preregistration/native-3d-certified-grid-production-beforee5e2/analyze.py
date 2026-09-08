import sys
if not sys.flags.isolated:raise RuntimeError('Python -I required')
from pathlib import Path
import runpy,json,signal,time,resource
B=Path(__file__).resolve().parent
if len(sys.argv)!=2:raise ValueError('one output directory')
signal.alarm(170);start=time.monotonic();freeze=runpy.run_path(str(B/'verify.py'))['verify']();out=Path(sys.argv[1]);a=runpy.run_path(str(B/'aggregate.py'))['analyze'](out,B,freeze)
a['analysis_seconds']=time.monotonic()-start;a['analysis_peak_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if a['analysis_seconds']>170 or a['analysis_peak_bytes']>384*1048576:raise ValueError('analysis resource')
if (out/'ANALYSIS.json').exists():raise ValueError('no analysis overwrite')
(out/'ANALYSIS.json').write_text(json.dumps(a,indent=2)+'\n')
