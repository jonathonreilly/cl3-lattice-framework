"""Exact finite supporting controls; no physical native evaluation."""
from fractions import Fraction as F

def require(x, label):
    if not x: raise ValueError(label)
def add(a,b): return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def sc(a,s): return [[s*x for x in row] for row in a]
def mul(*args):
    a=args[0]
    for b in args[1:]: a=[[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return a
def comm(a,b): return add(mul(a,b),sc(mul(b,a),-1))
def run():
    n=0; mutants=0
    def check(x,label):
        nonlocal n
        require(x,label);n+=1
    eta=F(357,25)/2**26+F(2)/2**23+429*F(4,25)**12
    check(eta==F(2287839703834313821,4000000000000000000000000),'raw eta')
    k=4*12*(26+23);check(k==2352,'rank');check((k+3)//2==1177,'mode bound')
    check(F(6476,75)<87,'trace constant');check(F(102,5)<F(46,10)**2,'W norm')
    # sqrt2 < 99/70, and delta/h=1/4. Bound only state-compression error.
    err=F(90,8)*F(61,5)*2*F(99,70)*eta*16
    check(F(99,70)**2>2,'sqrt upper');check(err<F(36,10000),'Ward error')
    g=[[F(1),F(0)],[F(0),F(-1)]]
    for a in range(-3,4):
        for c in range(-3,4):
            wa=[[F(2),F(a)],[F(a),F(-2)]];wc=[[F(2),F(c)],[F(c),F(-2)]]
            ra=[[F(-2),F(1,3)],[F(1,3),F(-1)]];rc=[[F(-1),F(1,5)],[F(1,5),F(-3)]]
            old=add(add(mul(rc,ra),sc(mul(comm(wc,rc),g,ra),F(-1,2))),sc(mul(rc,g,comm(wa,ra)),F(1,2)))
            rest=add(add(sc(mul(rc,g,add(wa,sc(wc,-1)),ra),F(1,2)),sc(mul(wc,rc,g,ra),F(-1,2))),sc(mul(rc,g,ra,wa),F(-1,2)))
            new=add(sc(mul(rc,ra),3),rest)
            check(old==new,'actual Ward expansion')
            check(old!=add(sc(mul(rc,ra),2),rest),'wrong onsite factor rejected');mutants+=1
    # Exact rational paired cosines from Pythagorean parametrization.
    for m in range(2,12):
        angles=[(F(j*j-1,j*j+1),F(2*j,j*j+1)) for j in range(2,m+1)]
        for r in range(len(angles)+1):
            overlap=F(1);tail=F(0)
            for c,s in angles[r:]: overlap*=c;tail+=s*s;check(c*c+s*s==1,'pair normalization')
            check(2*(1-overlap)<=2*tail,'Fock fidelity tail')
    # One particle-hole pair: h eigenvalues +/-a. Ground shift =-(a-b)/2.
    for a in range(1,10):
        for b in range(1,10):
            exact=F(b-a,2);relative_abs=2*(a-b)
            check(exact==-F(1,4)*relative_abs,'Majorana energy normalization')
            if a!=b:check(exact!=-F(1,2)*relative_abs,'wrong energy factor rejected');mutants+=1
    return {'status':'PASS','supporting_predicates':n,'adverse_cases':mutants,'raw_eta':str(eta),'rank_bound':k,'fermion_mode_bound':1177,'state_error_coefficient_upper':str(err),'physical_runs':0,'scope':'finite exact supporting controls, not an infinite-proof audit'}
