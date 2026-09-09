from pathlib import Path
from math import isqrt
from fractions import Fraction as F
import argparse,json,hashlib
P=Path(__file__).resolve().parent;S=1<<192

def scalar(l,u,half=True):
 if type(l)is not int or type(u)is not int or not 0<l<=u:raise ValueError('positive integer pivot')
 a=isqrt(l*S);b=isqrt(u*S);b+=b*b<u*S
 if not a:return {'divisor_failure':True}
 factor=2 if half else 1;n=S*S
 lo=n//(factor*b);hi=-((-n)//(factor*a))
 lower=F(u-l,S)/(4*F(u,S)*F(b,S))*(1 if half else 2)
 return {'divisor_failure':False,'forced_lower':lo,'forced_upper':hi,'width':hi-lo,'threshold':S//2**39,'must_fail_width':hi-lo>S//2**39,'exact_image_width_lower_bound':str(lower),'exact_image_lower_exceeds_threshold':lower>F(1,2**39)}
def support(i):
 if type(i)is not int or not 0<=i<399:raise ValueError('index')
 if i>=396:return {i},False
 n,t=divmod(i,6);v=t//2;return {6*n+v,6*n+3+v},True

def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['tiny','verify']);ap.add_argument('--output');a=ap.parse_args()
 if a.mode=='tiny':
  z=scalar(S,4*S)
  if z['forced_lower']!=S//4 or z['forced_upper']!=S//2 or not z['must_fail_width']:raise ValueError('toy')
  if support(267)[0]!=support(266)[0] or support(193)[0]==support(267)[0]:raise ValueError('support')
  print(json.dumps({'status':'PASS_TINY','checks':3,'saved_data_read':False}));return
 if not a.output:raise ValueError('output required')
 out=Path(a.output);out.mkdir(exist_ok=False);state={'stage':'pins','orbit':None,'row':None};write=lambda n,x:(out/n).write_text(json.dumps(x,indent=2)+'\n')
 try:
  cfg=json.loads((P/'INPUTS.json').read_text())
  for p,h in cfg['files'].items():
   if hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h:raise ValueError('pin '+p)
  allrows=[]
  for oi,path in enumerate(cfg['histories']):
   state={'stage':'history','orbit':oi,'row':None};write('PARTIAL.json',state);doc=json.loads(Path(path).read_text());hist=doc['history']
   if doc['orbit']!=oi or len(hist)!=24:raise ValueError('fixed24 history')
   seen=set();indices=set()
   for j,row in enumerate(hist):
    state={'stage':'scalar','orbit':oi,'row':j};write('PARTIAL.json',state);idx=row['index'];raw,half=support(idx)
    if idx in indices:raise ValueError('duplicate');
    indices.add(idx);fresh=sorted(raw-seen);seen.update(raw)
    if fresh:allrows.append({'orbit':oi,'row':j,'index':idx,'fresh_raw':fresh,'half':half,**scalar(*row['r'],half=half)})
  write('RESULT.json',{'status':'COMPLETE_SAVED_SCALAR_DIAGNOSTIC','rows':allrows,'forced_blockers':[x for x in allrows if x.get('must_fail_width') or x['divisor_failure']],'scope':'specific interval coefficient algorithm; no fullC/native replay'})
 except BaseException as e:write('FAILURE.json',{'state':state,'error':repr(e)});raise
if __name__=='__main__':main()
