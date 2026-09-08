from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,hashlib,time
B=Path(__file__).resolve().parent

def atan_bounds(inv,N=48):
 x=F(1,inv);s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(N)),F(0));nextterm=(-1)**N*x**(2*N+1)/F(2*N+1)
 return min(s,s+nextterm),max(s,s+nextterm)
def floor_dyadic(x,bits=100):return (x.numerator*(1<<bits))//x.denominator
def ceil_dyadic(x,bits=100):return -floor_dyadic(-x,bits)
def build():
 a,b=atan_bounds(5);c,d=atan_bounds(239);plo=16*a-4*d;phi=16*b-4*c;pm=(plo+phi)/2;pe=(phi-plo)/2
 if not F(3)<plo<phi<F(22,7):raise ValueError('pi enclosure sanity')
 rows=[]
 for j in range(32):
  x=pm*F(2*j+1,64);xe=pe*F(2*j+1,64)
  s=sum(((-1)**k*x**(2*k+1)/factorial(2*k+1) for k in range(40)),F(0));err=abs(x)**81/factorial(81)+xe
  lo=2*(s-err);hi=2*(s+err);ln=floor_dyadic(lo);un=ceil_dyadic(hi);v=float((lo+hi)/2);vf=F.from_float(v);rad=F(1,1<<48)
  if not vf-rad<=F(ln,1<<100)<=lo<=hi<=F(un,1<<100)<=vf+rad:raise ValueError('binary64 radius')
  if not F(0)<lo<hi<F(2):raise ValueError('q range')
  rows.append(dict(j=j,q_hex=v.hex(),lower_numerator=ln,upper_numerator=un,denominator=1<<100,center_error_numerator=1,center_error_denominator=1<<48))
 for j in range(32):
  r,t=rows[j],rows[31-j]
  if max(r['lower_numerator'],t['lower_numerator'])>min(r['upper_numerator'],t['upper_numerator']):raise ValueError('reflection symmetry')
 return dict(grid_n=32,formula='q_j=2sin(pi(2j+1)/64)',pi_lower_numerator=floor_dyadic(plo),pi_upper_numerator=ceil_dyadic(phi),pi_denominator=1<<100,rows=rows,method='Exact rational Machin alternating arctan48 terms; sine Taylor through79 with degree80 remainder; dyadic outward rounding100bits; exact binary64-center radius check')
if __name__=='__main__':
 start=time.monotonic();r=build();(B/'INPUTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(dict(rows=len(r['rows']),seconds=time.monotonic()-start,input_sha256=hashlib.sha256((B/'INPUTS.json').read_bytes()).hexdigest())))
