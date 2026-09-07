import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import signal,time,resource,sys,json,hashlib
from pathlib import Path
signal.alarm(180);start=time.monotonic();AUDIT_TIMEOUT_SEC=180
import sympy as s
checks=[]
def ck(name,value):
 if name in checks or not bool(value):raise AssertionError(name)
 checks.append(name)
x,y,h,k1,k2,r=s.symbols('x y h k1 k2 r',real=True);t=s.symbols('t',positive=True)
Q=x*x+x*y+y*y;H=x*y*(x+y)/2;W=H*s.exp(-Q)
L=lambda f:s.expand((s.diff(f,x,2)-s.diff(f,x,y)+s.diff(f,y,2))/3)
ck('native harmonic cubic',s.simplify(L(H))==0)
ck('diffusion quadratic normalization',s.simplify(L(Q))==1)
ck('Gaussian generator normalization',s.simplify(L(s.exp(-Q))-(Q-1)*s.exp(-Q))==0)
heat=H*(1+t)**-4*s.exp(-Q/(1+t))
ck('actual harmonic Gaussian heat PDE',s.simplify(s.diff(heat,t)-L(heat))==0)
phi=(s.cos(h*k1)+s.cos(h*k2)+s.cos(h*(k1-k2)))/3
symbol=s.series((phi-1)/h**2,h,0,4).removeO().expand();ell=-(k1*k1-k1*k2+k2*k2)/3
ck('six-step leading diffusion symbol',s.simplify(symbol.coeff(h,0)-ell)==0)
ck('six-step quartic heat correction',s.simplify(symbol.coeff(h,2)-ell**2/4)==0)
ck('wrong half heat coefficient rejected',s.simplify(symbol.coeff(h,2)-ell**2/8)!=0)
dilated=W.subs({x:s.exp(-r)*x,y:s.exp(-r)*y},simultaneous=True);derivative=s.diff(dilated,r).subs(r,0)
ck('actual dilated multiplier derivative',s.simplify(derivative-(2*Q-3)*W)==0)
ck('wrong dilation sign rejected',s.simplify(derivative+(2*Q-3)*W)!=0)
W2=(3-s.Rational(7,4)*Q+Q**2/4)*W
ck('shifted saddle subtraction',s.simplify(W2-3*W-Q*(Q-7)*W/4)==0)
kappa,var,ellnorm=s.symbols('kappa variance ellnorm',real=True);mean=kappa+s.Rational(3,2);moment2=var+mean**2
relative=(moment2-7*mean)/4+3+ellnorm/4
expected=(var+kappa**2-4*kappa+s.Rational(15,4)+ellnorm)/4
ck('virial full coefficient substitution',s.expand(relative-expected)==0)
positive=s.Rational(7,16)+(var+(ellnorm-kappa**2)+2*(kappa-1)**2)/4
ck('full coefficient nonnegative decomposition',s.expand(relative-positive)==0)
ck('missing saddle factor rejected',s.expand(relative-3-positive)==-3)
z=s.symbols('z',real=True);B4=s.bernoulli(4,z);critical=[s.Integer(0),s.Rational(1,2),s.Integer(1)]
ck('Bernoulli critical points complete',s.factor(s.diff(B4,z))==2*z*(z-1)*(2*z-1))
ck('Bernoulli fourth remainder supremum',max(abs(B4.subs(z,a)) for a in critical)==s.Rational(1,30))
ck('Euler Maclaurin fourth constant',2*s.Rational(1,30)/s.factorial(4)==s.Rational(1,360))
cellmean=s.integrate(z,(z,-s.Rational(1,2),s.Rational(1,2)));cellvariance=s.integrate(z*z,(z,-s.Rational(1,2),s.Rational(1,2)))
ck('cell projection first moment',cellmean==0)
ck('cell projection variance',cellvariance==s.Rational(1,12))
f=z**3*s.exp(-z*z)
ck('cubic wall first boundary jet',f.subs(z,0)==0 and s.diff(f,z).subs(z,0)==0)
ck('cubic wall fourth order leading term',s.diff(f,z,3).subs(z,0)/720==s.Rational(1,120))
poly=s.simplify(s.diff(f,z,4)*s.exp(z*z))
ck('fourth derivative polynomial Gaussian envelope',s.Poly(poly,z).degree()==7)
ck('nonvanishing wall derivative adverse control',-s.diff(s.exp(-z),z).subs(z,0)/12==s.Rational(1,12))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<180 or time.monotonic()-start>=180:raise AssertionError('resource contract')
payload={'scope':'Exact symbolic support for full normalized native top coefficient; functional analytic heat/quadrature/Perron proof remains in source; no numerical eigenvalue or excited/physical-gap claim','checks':checks,'check_count':len(checks),'relative_coefficient_lower':'7/16','spectral_remainder':'o(beta^-1)','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':{},'resources':{'timeout_seconds':180,'rss_limit_MiB':180,'blas_threads':1},'seconds':time.monotonic()-start,'rss_MiB':rss}
if '--json' in sys.argv:print(json.dumps(payload,indent=2,allow_nan=False))
else:
 print('PASS full-top symbolic certificate:',len(checks),'actual named checks')
 print('per_element: exact six-step symbol, diffusion and heat PDE normalization')
 print('per_site: shifted-grid wall jets and cell projection variance; no false step-operator expansion')
 print('per_mode: actual virial coefficient algebra, no trial Perron vector')
 print('per_block: relative lower bound7/16 and EM remainder identities; analytic theorem supplies quantifiers')
 print('lattice_wide: checked and not executed -- no numerical full spectrum, explicit onset or physical gap')
 print('SOURCE_SHA256',payload['source_sha256'])
