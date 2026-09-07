import sympy as s,json
from fractions import Fraction as F
x,y,t=s.symbols('x y t',positive=True);Q=x*x+x*y+y*y;H=x*y*(x+y)/2
u=H*(1+t)**-4*s.exp(-Q/(1+t));L=lambda f:(s.diff(f,x,2)-s.diff(f,x,y)+s.diff(f,y,2))/3
assert s.simplify(s.diff(u,t)-L(u))==0
assert s.simplify(u.subs(t,0)-H*s.exp(-Q))==0
th=s.symbols('th',real=True)
assert s.integrate(s.cos(3*th),(th,-s.pi/6,s.pi/6))==s.Rational(2,3)
assert s.integrate(s.cos(3*th)**2,(th,-s.pi/6,s.pi/6))==s.pi/6
mu=s.simplify((s.pi/(27*s.sqrt(3))*s.Rational(2,3)**4/16)/(s.sqrt(s.pi)/18))
assert mu==2*s.sqrt(s.pi)/(243*s.sqrt(3))
assert F(4,35)**2*F(2,3)**5<F(1,24)**2
term=F(1);e6=term
for j in range(1,20):term*=F(6,j);e6+=term
assert e6>400
assert F(6)<F(5,2)**2
assert F(7,324)*(F(1,24)+F(1,8))==F(7,1944)
assert -1+F(7,1944)/F(2,243)==-F(9,16)
print(json.dumps({'heat_PDE_identity':True,'radial_H_coefficient':'2/27','radial_H2_integrated':'pi/(27sqrt3)*a^-4','mu_trial':str(mu),'exp6_lower_19terms_exceeds400':True,'J_bound':'7/1944','relative_sign_bound':'-9/16'},indent=2))
