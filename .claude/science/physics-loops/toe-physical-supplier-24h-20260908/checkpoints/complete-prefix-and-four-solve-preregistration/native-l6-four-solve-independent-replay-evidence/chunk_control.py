import json,struct

def parity(x):return x.bit_count()&1
def calc(x,p,rows,kind,corrected):
 n=len(x);top=n.bit_length()-1;chunk=8;scatter=[0.]*n;gather=[0.]*n
 for lo in range(0,n,chunk):
  for j,c in rows:
   for src in range(lo,lo+chunk):
    bits=src|((parity(src)^p)<<top);sg=(-1)**parity(bits&((1<<j)-1))
    if kind=='B':sg*=2*((bits>>j)&1)-1
    dst=src^(1<<j) if j<top else src
    scatter[dst]+=(x[src]*c)*sg
 for lo in range(0,n,chunk):
  order=sorted(enumerate(rows),key=lambda row:(((lo^(1<<row[1][0])) if row[1][0]<top else lo)//chunk,row[0])) if corrected else list(enumerate(rows))
  for _,(j,c) in order:
   for dst in range(lo,lo+chunk):
    src=dst^(1<<j) if j<top else dst;bits=src|((parity(src)^p)<<top);sg=(-1)**parity(bits&((1<<j)-1))
    if kind=='B':sg*=2*((bits>>j)&1)-1
    gather[dst]+=(x[src]*c)*sg
 return sum(struct.pack('d',a)!=struct.pack('d',b) for a,b in zip(scatter,gather))
rows=[(0,.1),(2,-.3),(4,.7),(5,-.2)];x=[(-1.)**i*(1e16 if i%5==0 else (i-30)/7) for i in range(64)]
old=[];new=[]
for p in (0,1):
 for kind in ('A','B'):
  old.append(calc(x,p,rows,kind,False));new.append(calc(x,p,rows,kind,True))
if not any(old) or any(new):raise ValueError('chunk-order witness')
print(json.dumps({'old_mismatches':old,'corrected_mismatches':new,'largest_vector':64,'physical_calls':0}))
