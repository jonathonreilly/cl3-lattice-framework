"""Exact finite Gauss/no-double domain controls; no new physical claim."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md',)
import argparse,itertools,json,resource,signal,sys,time
_started=time.monotonic()
if __name__=='__main__':
    signal.alarm(AUDIT_TIMEOUT_SEC)
    parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');parser.parse_args()
checks=0
def require(value):
    global checks
    checks+=1
    if not value:raise RuntimeError('Gauss/no-double domain')
def gauss(div,plus,minus):
    return div+(plus-minus)
def admitted(div,plus,minus):
    return plus*minus==0 and gauss(div,plus,minus)==0
rows=[]
for bits in itertools.product((0,1),repeat=6):
    degree=sum(bits)
    for epsilon in (-1,1):
        div=epsilon*(sum(2*x-1 for x in bits))//2
        require(div==epsilon*(degree-3))
        labels=[(p,m) for p,m in itertools.product((0,1),repeat=2) if admitted(div,p,m)]
        expected=[] if abs(div)>1 else [(int(div==1),int(div==-1))]
        require(labels==expected)
        if labels:
            require(2*(labels[0][0]+labels[0][1])-1==(-1)**degree)
        rows.append(dict(bits=bits,epsilon=epsilon,divergence=div,labels=labels))
unrestricted=[(p,m) for p,m in itertools.product((0,1),repeat=2) if gauss(0,p,m)==0]
require(unrestricted==[(0,0),(1,1)])
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
require(0<rss<384 and time.monotonic()-_started<180)
print(json.dumps(dict(executed_predicates=checks,star_rows=rows,neutral_without_no_double=unrestricted,portable_seconds=time.monotonic()-_started,portable_rss_mib=rss),indent=2))
