"""Exact scalar and parity components of the separately proved remainder bound."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md',)
import argparse,itertools,json,resource,signal,sys,time
from fractions import Fraction as F
start=time.monotonic()
if __name__=='__main__':
    signal.alarm(AUDIT_TIMEOUT_SEC)
    parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');parser.parse_args()
checks=0
def require(value,message):
    global checks
    checks+=1
    if not value:raise RuntimeError(message)
r=F(1,8)
terms=[1/(1-r)**2,3/(1-r),r*r/(1-r)**3,1/((1-r)**3*(1-r)),F(2)]
expected=[F(64,49),F(24,7),F(8,343),F(2048,1029),F(2)]
for actual,wanted in zip(terms,expected):require(actual==wanted,'exact endpoint term')
require(sum(terms)==F(1286,147),'exact endpoint sum')
require(sum(terms)<9,'conservative constant')
require(F(9,32)<1,'U scaling')
require(r/(1-r)==F(1,7),'Neumann radius')
words={}
expected_words={0:[''],1:['E'],2:['VV','EE'],3:['VVE','VEV','EVV','EEE']}
for n in range(4):
    words[n]=[''.join(w) for w in itertools.product('VE',repeat=n) if w.count('V')%2==0]
    require(words[n]==expected_words[n],'parity word enumeration')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
require(0<rss<384 and time.monotonic()-start<180,'resources')
print(json.dumps(dict(checks=checks,constant_terms=list(map(str,terms)),sum=str(sum(terms)),surviving_inner_words=words,seconds=time.monotonic()-start,rss_MiB=rss,scope='Exact finite algebraic components only; operator proof is separate.'),indent=2))
