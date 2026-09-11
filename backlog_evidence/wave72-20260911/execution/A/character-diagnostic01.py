import sympy as s
w=(-1+s.sqrt(3)*s.I)/2
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
f1=s.Matrix([w**(-j)/s.sqrt(3) for j in range(3)])
f2=s.Matrix([w**(-2*j)/s.sqrt(3) for j in range(3)])
for name,v in [('conjugacy',f2-f1.conjugate()),('first',P*f1-w*f1),('second',P*f2-w**2*f2)]:
 print(name,'expanded=',[s.expand(x)==0 for x in v],'exact=',[s.simplify(s.expand_complex(x)) for x in v])
print('cyclotomic',s.expand(w*w+w+1),'norm',s.expand(w*s.conjugate(w)))
