from fractions import Fraction as F
from seed import seed
S=1<<192
def assemble(selected,entry,persist):
 if len(selected)!=24 or any(type(i)is not int or not 0<=i<399 for i in selected)or len(set(selected))!=24:raise ValueError('ordered24')
 n=48;boxes=[[None]*n for _ in range(n)]
 def put(i,j,x):
  if len(x)!=2 or any(type(v)is not int for v in x)or x[0]>x[1]:raise ValueError('entry interval')
  boxes[i][j]=boxes[j][i]=x
 for a,i in enumerate(selected):
  for b in range(a,24):
   g,z=entry(i,selected[b]);persist('selected_entry',{'a':a,'b':b,'g':g,'j':z})
   if a==b:
    if not z[0]<=0<=z[1]:raise ValueError('J diagonal')
    z=(0,0)
   put(2*a,2*b,g);put(2*a+1,2*b+1,g);put(2*a,2*b+1,z);put(2*a+1,2*b,(-z[1],-z[0]))
 center=[[F(x[0]+x[1],2*S)for x in row]for row in boxes];radius=[[F(x[1]-x[0],2*S)for x in row]for row in boxes]
 cols=[seed(i,g)for i in selected for g in (0,1)];labels=sorted(set().union(*(set(c)for c in cols)));E=[[c.get(label,F(0))for c in cols]for label in labels]
 persist('selected_gram',{'center':center,'radii':radius,'labels':labels,'E':E})
 return center,radius,E
