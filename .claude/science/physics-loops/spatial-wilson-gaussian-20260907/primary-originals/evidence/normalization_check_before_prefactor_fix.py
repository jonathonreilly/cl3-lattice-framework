import sympy as s,json
checks=[]
def ck(n,b):
 assert bool(b),n
 checks.append(n)
pi=s.pi;a=s.Rational(8,135);b=s.Rational(23,270);omega=s.sqrt(55)/90;theta=(32-3*s.sqrt(55))/23
Sigma=s.Matrix([[192,138],[138,192]])/11
ck('source Gaussian precision',Sigma.inv()==s.Matrix([[2*a,-b],[-b,2*a]]))
ck('oscillator frequency',s.simplify(4*a*a-b*b-omega*omega)==0)
ck('Mehler ratio',s.simplify(theta-b/(2*a+omega))==0)
# x=u-y/2 makes Q=u²+3y²/4. Normalized independent Gaussian moments.
expect=s.Rational(4)*s.Rational(15,8)-18*s.Rational(3,4)*s.Rational(2,3)+s.Rational(81,4)*s.Rational(1,2)*s.Rational(4,3)
ck('Weyl Vandermonde Gaussian moment',expect==12)
weyl_integral=expect*2*pi/s.sqrt(3)
j0=s.simplify(weyl_integral/(6*(2*pi)**2)/(2*pi)**4)
ck('normalized Haar tangent density',j0==1/(16*s.sqrt(3)*pi**5))
joint=(2*pi)**-8*Sigma.det()**-4
lambda0=s.simplify(joint/j0*(pi/(a+omega/2))**4)
candidate=s.sqrt(3)*pi*((32-3*s.sqrt(55))/270)**4
ck('absolute Gaussian ground eigenvalue',s.simplify(lambda0-candidate)==0)
ck('eight versus radial ground power',8*s.Rational(1,2)==3+2*s.Rational(1,2))
degrees={n:sum(2*i+3*j==n for i in range(5) for j in range(4)) for n in range(7)}
ck('invariant first degree is two',degrees[0]==1 and degrees[1]==0 and degrees[2]==1 and degrees[3]==1 and degrees[6]==2)
print(json.dumps({'checks':checks,'j0':str(j0),'joint_density_prefactor':str(joint),'omega':str(omega),'theta':str(theta),'ground_eigenvalue':str(candidate),'first_top_ratio':str(s.expand(theta**2)),'invariant_degree_census':degrees},indent=2))
