import tables,assembly,arithmetic as a,json
seen=set()
def R(n):seen.add(n);return a.point(n+1)
for left,right,o,_ in assembly.SIGNATURES:
 for M in tables.nominal(R,left,right,o):
  for n in range(5):
   for i in range(4):
    for j in range(4):M(n,i,j)
assert max(seen)==6 and max(n for n in seen if n%2)==5
nom=sorted(seen);seen.clear()
for kind in('P','O'):
 for M in tables.inner(R,kind):
  for n in range(7):
   for i in range(3):
    for j in range(3):M(n,i,j)
assert max(seen)==10 and max(n for n in seen if n%2)==9
print(json.dumps({'status':'PASS_FORMAL_LOOKUP_ONLY','nominal_radial_orders':nom,'inner_radial_orders':sorted(seen),'native_values':0},indent=2))
