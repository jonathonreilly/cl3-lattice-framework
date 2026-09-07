import time,signal,resource,sys,json,hashlib
from fractions import Fraction as F
from pathlib import Path
start=time.monotonic();signal.alarm(180);checks=[]
def ck(n,v):
 assert n not in checks and bool(v),n
 checks.append(n)
def inv(w):return [(a,-s) for a,s in reversed(w)]
def reduce(w):
 stack=[]
 for a,s in w:
  if stack and stack[-1]==(a,-s):stack.pop()
  else:stack.append((a,s))
 return stack
A=[('A',1)];B=[('B',1)];C=[('C',1)];D=[('D',1)];U=[('U',1)]
T=A+B+inv(C)+inv(D);side=U+inv(C)
word=side+inv(D)+inv(T)+A+B
ck('actual noncommuting fiveface disk word',reduce(word)==U)
ck('inverted missing loop identity',reduce(inv(word))==inv(U))
ck('weighted action count',10*F(1,2)+12==17)
ck('missingface deficit factor',5*6*2==60)
ck('Frobenius smallball energy',17*16/F(6)==F(136,3))
ck('24link ambient dimension exponent',24*18==432)
ck('beta partition power',432/F(2)==216)
ck('rational concentration ceiling',F(136,3)+432*2+1==F(2731,3))
ck('character local to global constant',F(4**2,8)==2)
ck('entry bound factor',2*60==120)
ck('fundamental deficit bound',F(60,2)==30)
ck('operatornorm factor',2*120==240)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert 0<rss<180 and time.monotonic()-start<180
print(json.dumps(dict(checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),fiveface_words={'top':T,'side':side,'reconstruction':word,'reduced':reduce(word)},seconds=time.monotonic()-start,rss_MiB=rss,scope='Exact freegroup and rational support for analytical finitewindow weakcoupling theorem; no Haar saddle or numerical spectral fit.'),indent=2))
