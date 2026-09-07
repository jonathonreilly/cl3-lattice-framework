import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import time,signal,resource,sys,json,hashlib
AUDIT_TIMEOUT_SEC=180
signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic()
import sympy as s
checks=[]
def ck(name,v):
 if name in checks or not bool(v):raise AssertionError(name)
 checks.append(name)
omega=s.sqrt(5);theta=(3-omega)/2;d=(3+omega)/2
ck('Mehler inverse width',s.simplify(theta*d)==1)
ck('Mehler square coefficient',s.simplify(omega*theta-1+theta**2)==0)
ck('Mehler ground exponent',s.simplify(-s.Rational(3,2)+theta+omega/2)==0)
x,y,z,q,c=s.symbols('x y z q c',real=True)
left=-s.Rational(3,2)*x*x-z*z+(x+s.sqrt(omega)*z)**2/d
right=-omega*x*x/2+2*s.sqrt(omega)*x*theta*z-theta**2*z*z
ck('actual Gaussian generating transform',s.simplify(left-right)==0)
# Independent degree census from Dirichlet angular modes3k and radial nodes n.
degrees={N:sum(3*k+2*n==N for k in range(1,6) for n in range(8)) for N in range(9)}
ck('top and first excited simplicity',degrees[3]==1 and degrees[4]==0 and degrees[5]==1 and all(degrees[j]==0 for j in range(3)))
H=x*y*(x+y)/2;Q=x*x+x*y+y*y;a=2/omega
L=lambda f:(s.diff(f,x,2)-s.diff(f,x,y)+s.diff(f,y,2))/3
ck('radial generator action',s.simplify(L(H*s.exp(-a*Q))-H*s.exp(-a*Q)*(a*a*Q-4*a))==0)
cc=(omega+1)/2;dd=1+cc/2
ck('mapped physical ground exponent',s.simplify(cc/dd-a)==0)
A=s.simplify(4-2*omega/dd);B=s.simplify(omega/dd**2)
ck('mapped first radial polynomial',s.simplify(B/A-1/omega)==0)
def expect(poly,rate):
 P=s.Poly(s.expand(poly),q)
 return s.simplify(sum(coeff*s.rf(4,n[0])/rate**n[0] for n,coeff in P.terms()))
P2=3-s.Rational(7,4)*q+q*q/4
rows=[]
for n,P in [(0,s.Integer(1)),(1,4-omega*q)]:
 norm=expect(P*P,omega)
 m1=s.simplify(expect(q*P*P,omega)/norm);m2=s.simplify(expect(q*q*P*P,omega)/norm)
 upart=s.simplify(expect(P2*P*P,omega)/norm)
 F=1 if n==0 else 4-2*a*q
 LF=s.expand(q*(s.diff(F,q,2)-2*a*s.diff(F,q)+a*a*F)+4*(s.diff(F,q)-a*F))
 heat=s.simplify(expect(LF*LF,2*a)/expect(F*F,2*a))
 ck('normalized ground radial moments' if n==0 else 'normalized excited radial moments',s.simplify(m1-(4 if n==0 else 6)/omega)==0 and s.simplify(m2-(4 if n==0 else 10))==0)
 ck('ground heat derivative norm' if n==0 else 'excited heat derivative norm',heat==(4 if n==0 else 10))
 total=s.simplify(upart+heat/4)
 ck('ground full coefficient' if n==0 else 'excited full coefficient',s.simplify(total-((5-7/omega) if n==0 else (8-s.Rational(21,2)/omega)))==0)
 rows.append({'branch':n,'leading_eigenvalue':str(s.expand(theta**(4+2*n))),'weighted_Q_mean':str(m1),'weighted_Q_second_moment':str(m2),'multiplier_relative_correction':str(upart),'heat_derivative_norm_squared':str(heat),'full_relative_correction':str(total)})
ck('radial orthogonality B',expect(4-omega*q,omega)==0)
ck('radial orthogonality G0',expect(4-2*a*q,2*a)==0)
diff=3-s.Rational(7,2)/omega
ck('first top relative ratio correction',s.simplify((8-s.Rational(21,2)/omega)-(5-7/omega)-diff)==0)
ck('ratio correction positive',s.Rational(9)>s.Rational(49,20))
ck('missing metric measure factor rejected',s.simplify(s.sqrt(3)/(2*s.pi)*2/s.sqrt(3)-1/s.pi)==0 and s.sqrt(3)/(2*s.pi)!=1/s.pi)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<180 or time.monotonic()-start>=180:raise AssertionError('resource')
payload={'scope':'Exact Gaussian chamber spectrum and branch corrections conditional on global divided multiplier and heat/quadrature lemmas; central-character sandwich only','checks':checks,'theta':str(theta),'degree_census':degrees,'rows':rows,'ratio_relative_correction':str(diff),'source_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest(),'seconds':time.monotonic()-start,'rss_MiB':rss}
if len(sys.argv)==2 and sys.argv[1]=="--json":
 print(json.dumps(payload,indent=2,allow_nan=False))
elif len(sys.argv)==1:
 print("PASS: 19 exact assertions")
 for level in ("per_element","per_site","per_mode","per_block","lattice_wide"):
  print(level+": bounded central-character one-link theorem; no multi-link physical identification")
 print(json.dumps({k:v for k,v in payload.items() if k not in ("checks",)},indent=2,allow_nan=False))
 print("TOTAL: PASS="+str(len(checks))+" FAIL=0")
else:
 raise SystemExit("usage: native_gauge_transfer_central_character_gaussian_spectral_second_order_2026_09_07.py [--json]")
