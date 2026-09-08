import time,json,resource,signal
from pathlib import Path
import core,postcheck
signal.alarm(30)
t=time.monotonic();tim={}
def mark(name):
 global t
 now=time.monotonic();tim[name]=now-t;t=now
p=postcheck.P
f=json.loads((p/'FRAME_RESULT.json').read_text());r=json.loads((p/'PREFIXES.json').read_text());z,row,saved=postcheck.load(p/'COEFFICIENT_OUTPUT/bridge_0.json',r);mark('input_load')
m=core.ExactModel(f,r);mark('model')
# Frozen first proper prefix: bridge0, boundary-used2, bridge-count1, mask3.
k,mask,words,x=saved[(2,1)]
if (k,mask,words)!=(1,3,1):raise ValueError('fixed identity')
c=core.candidate(x,1,m.W);mark('candidate')
a=m.matrix(3);mark('matrix')
g=core.gap(m,3);mark('gap')
v=core.residual(m,a,c,[([1]+[0]*511,1)]);mark('residual')
print(json.dumps({'scope':'fixed first-prefix cost only; no coefficient interval','timers':tim,'candidate_denominator_bits':c[1].bit_length(),'rss_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,'input_sha':postcheck.sha(p/'COEFFICIENT_OUTPUT/bridge_0.json')},indent=2))
