#!/usr/bin/env python3
"""Exact support; analytical supplied-slab proof remains load bearing."""
AUDIT_TIMEOUT_SEC = 180
import time,signal
start=time.monotonic();signal.alarm(180)
import resource,sys,json,hashlib
from fractions import Fraction as F
from pathlib import Path
checks=[]
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
# Remove the S side constraint in each temporal slice, keep identical links.
sub={'A':[],'B':[],'C':[],'D':[],'U':[('g',1)]}
def subst(word):
 out=[]
 for a,sign in word:out+=sub[a] if sign==1 else inv(sub[a])
 return reduce(out)
ck('adverse all retained spatial faces flat',all(subst(w)==[] for w in (A,B,D,T)))
ck('adverse missing face remains nonidentity',subst(U)==[('g',1)] and subst(side)==[('g',1)])
ck('actual SU3 adverse diagonal determinant',(-1)*(-1)*1==1)
ck('actual adverse missing deviation',sum((1-z)**2 for z in (-1,-1,1))==8)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert 0<rss<180 and time.monotonic()-start<180
assert len(checks)==16
result=dict(status='PASS',per_word_checks=2,per_arithmetic_checks=10,per_adverse_checks=4,TOTAL=16,runtime_input_files=[],checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),fiveface_words={'top':T,'side':side,'reconstruction':word,'reduced':reduce(word)},seconds=time.monotonic()-start,rss_MiB=rss,scope='Exact freegroup and rational support for analytical finitewindow weakcoupling theorem; no Haar saddle or numerical spectral fit.')
if '--json' in sys.argv:print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS: TOTAL16 exact checks (word2, arithmetic10, adverse4).')
 print('N5: Fixed finite-character windows of the actual bare-Haar cube slab.')
 print('N5: Exact word/arithmetic support; analytical concentration and character proof remain load bearing.')
 print('N5: Side-removal control changes both slice copies, not the theorem fixture.')
 print('N5: No high-label uniformity, spectral-gap or physical coupling selection.')
 print('N5: No runtime file inputs; source SHA '+result['source_sha256'])

if '--json' not in sys.argv:
 print('Resources: %.6fs; %.3f MiB; limits 180s/180MiB.' % (result['seconds'], result['rss_MiB']))
