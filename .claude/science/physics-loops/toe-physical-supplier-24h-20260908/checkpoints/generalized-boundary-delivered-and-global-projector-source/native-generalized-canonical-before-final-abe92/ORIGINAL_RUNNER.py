#!/usr/bin/env python3
"""Compact exact checks only; not archived native matrix replay."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parents[1]/'.claude/science/physics-loops/native-generalized-action-boundary-20260909'
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--json',action='store_true');args=ap.parse_args();d=json.loads((P/'EXACT_SUMMARY.json').read_text());n=0
 def check(x):
  nonlocal n
  if not x:raise ValueError('compact predicate '+str(n))
  n+=1
 check(len(d['selected'])==5);check(len(d['generalized'])==10)
 for i,r in enumerate(d['selected']):
  check(type(r['orbit'])is int and r['orbit']==i);check(0<=F(r['e'])<F(8,10**6));check(r['width_pass']is False);check(r['l1_pass']is True)
 for j,r in enumerate(d['generalized']):
  check((r['orbit'],r['impurity'])==(j//2,(399,400)[j%2]));check(r['status']=='CERTIFIED_GENERALIZED_LEAKAGE_BOUND');check(F(r['delta_squared_lower'])>F(53,100));check(F(r['delta_squared_upper'])>=F(r['delta_squared_lower']));check(r['target_excluded']is True);check(r['leakage_pass']is False);check(F(r['target_squared'])==F(1,10**12))
 # W=(2,0), K=[[0,-3],[3,0]]. H=4,A=0,Z=36; normalized leakage9.
 H,A,Z=F(4),F(0),F(36);N=Z+A*A/H;check(N/H==9);check(N>=0)
 print(json.dumps({'status':'PASS_COMPACT_EXACT_SUPPORT','predicates':n,'native_matrix_replay':False,'generalized_saved_post':d['generalized_saved_post']},indent=2))
if __name__=='__main__':main()
