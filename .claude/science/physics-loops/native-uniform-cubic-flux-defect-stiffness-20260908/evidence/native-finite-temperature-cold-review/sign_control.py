from itertools import product
import json,time
start=time.monotonic();h=6;dimension=2**(h//2);full=(1<<h)-1;oddmask=sum(1<<j for j in range(1,h,2))
def product_cliff(a,b):
 ma,ca=a;mb,cb=b;inversions=sum((mb&((1<<j)-1)).bit_count() for j in range(h) if ma>>j&1)
 return ma^mb,ca*cb*(-1)**inversions
def conjugate(a):m,c=a;return m,complex(c).conjugate()*(-1)**((m&oddmask).bit_count())
def trace(a):return dimension*a[1] if a[0]==0 else 0
P=(full,(-1j)**(h//2));even=[m for m in range(1<<h) if m.bit_count()%2==0];n=0;kills={'wrong_i':0,'missing_parity':0,'missing_right_conjugation':0}
for length in range(9):
 for seed in range(32):
  L=[(even[(seed+7*k)%32],1j**((seed+3*k)%4)) for k in range(length+1)]
  R=[(even[(3*seed+5*k)%32],1j**((2*seed+k)%4)) for k in range(length+1)]
  js=[(seed+5*k)%h for k in range(length)]
  if length%2==0 and length:
   x=L[0];y=R[0]
   for k,j in enumerate(js):
    x=product_cliff(x,(1<<j,1));y=product_cliff(y,(1<<j,1))
    if k<length-1:x=product_cliff(x,L[k+1]);y=product_cliff(y,R[k+1])
   L[-1]=(x[0],1j);R[-1]=(y[0],1j)
  wl=L[0];wr=R[0]
  left=L[0];right=conjugate(R[0]);bad_i=left;bad_p=left;bad_r=R[0]
  for k,j in enumerate(js):
   a=(1<<j,1);ap=product_cliff(a,P);left=product_cliff(product_cliff(left,(ap[0],1j*ap[1])),L[k+1]);right=product_cliff(product_cliff(right,conjugate(a)),conjugate(R[k+1]))
   bad_i=product_cliff(product_cliff(bad_i,ap),L[k+1]);bad_p=product_cliff(product_cliff(bad_p,(a[0],1j)),L[k+1]);bad_r=product_cliff(product_cliff(bad_r,a),R[k+1])
   wl=product_cliff(product_cliff(wl,a),L[k+1]);wr=product_cliff(product_cliff(wr,a),R[k+1])
  expected=0 if length%2 else trace(wl)*complex(trace(wr)).conjugate();actual=trace(left)*trace(right)
  if actual!=expected:raise ValueError(('history sign',length,seed,actual,expected))
  n+=1
  for name,z in [('wrong_i',trace(bad_i)*trace(right)),('missing_parity',trace(bad_p)*trace(right)),('missing_right_conjugation',trace(left)*trace(bad_r))]:
   kills[name]+=int(z!=expected)
if not all(kills.values()):raise ValueError(('adverse controls not discriminating',kills))
print(json.dumps(dict(history_cases=n,half_majoranas=h,actual_adverse_mismatches=kills,seconds=time.monotonic()-start,scope='abstract Clifford exact signs only, no thermal scan'),indent=2))
