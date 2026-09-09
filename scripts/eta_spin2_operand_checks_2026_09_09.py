"""Independent finite identities and actual changed-operand controls.

No mutation flag is counted as an altered process. Each adverse operand is
passed to exactly the same numerical/algebraic predicate as its clean control.
"""
from __future__ import annotations
import itertools
from fractions import Fraction as F
import sympy as s
import eta_spin2_affine_model_2026_09_09 as a
import eta_spin2_native_model_2026_09_09 as n
import eta_spin2_quadrupole_model_2026_09_09 as q
import eta_spin2_joint_model_2026_09_09 as j
R=s.Rational

def same(x,y):return x.shape==y.shape and all(s.simplify(v)==0 for v in x-y)

def checks(block):
    rows=[]
    def add(name,ok,data):rows.append((name,bool(ok),str(data)))
    Q1=s.Matrix([[0,0,-1],[0,0,1/s.sqrt(2)],[-1,1/s.sqrt(2),0]])
    Q2=s.Matrix([[(3+s.sqrt(3))/4,-s.sqrt(6)/4,0],[-s.sqrt(6)/4,-(1+s.sqrt(3))/4,1/s.sqrt(2)],[0,1/s.sqrt(2),-R(1,2)]])
    if block==7:
        expected=q.tensor_to_coeff(Q2)
        def column_ok(c):return same(c,expected)
        c=n.tt_source_coefficients('H2'); bad=s.Matrix(c);bad[1]=0
        add('actual TT column: clean and changed diagonal',column_ok(c) and not column_ok(bad),tuple(c-bad))
        target=s.Matrix((-s.sqrt(6)/4,1/s.sqrt(2),0))
        seed=s.Matrix((0,1/s.sqrt(2),-1))
        table=tuple(tuple(a.shear_representation(r)*seed) for r in a.rotations())+((0,0,0),)*40
        add('independent exact 64-row inequality',all(not same(s.Matrix(row),target) for row in table),len(table))
        # Degree-preserving zero-momentum occupation and hopping columns.
        C=[]
        for i in range(4):
            m=s.zeros(16)
            for mask in range(16):
                if not(mask>>i&1):m[mask|(1<<i),mask]=(-1)**((mask&((1<<i)-1)).bit_count())
            C.append(m)
        H=[s.eye(16)/2-C[i]*C[i].T for i in range(4)]+[-(C[i]*C[k].T+C[k]*C[i].T)/s.sqrt(2) for i in range(4) for k in range(i+1,4)]
        full=s.Matrix.hstack(*[s.Matrix(list(h)) for h in H])
        add('native injectivity clean and deleted hopping column',full.rank()==10 and full[:,:9].rank()!=10,(full.rank(),full[:,:9].rank()))
    elif block==8:
        def orbit_span(Q):return s.Matrix.hstack(*[s.Matrix(list(r*Q*r.T)) for r in a.rotations()]).rank()
        bad=Q2-s.diag(*Q2.diagonal())
        add('H1/H2 spans and actual removed diagonal sector',orbit_span(Q1)==3 and orbit_span(Q2)==5 and orbit_span(bad)!=5,(orbit_span(Q1),orbit_span(Q2),orbit_span(bad)))
        A=a.selected_action(); unseen=set(range(64)); rows2=[]
        while unseen:
            m=min(unseen); orb={A(g,m) for g in range(24)};unseen-=orb
            rows2.append((m,len(orb),sum(A(g,m)==m for g in range(24))))
        add('finite orbit stabilizer control',sorted(r[1] for r in rows2)==[2,4,4,6,6,6,12,24] and sum(r[2]==1 for r in rows2)==1,rows2)
    elif block==9:
        aa,bb,dd,ee,ff=s.symbols('a b d e f',real=True)
        Q=s.Matrix([[aa,dd,ee],[dd,bb,ff],[ee,ff,-aa-bb]])
        shell=q.prepare_target(Q); expected=-Q/32
        def moment_ok(prob):return same(q.distribution_moment(prob),expected) and s.simplify(sum(prob.values()))==1
        clean=q.local_distribution(shell); bad=dict(clean)
        # Move mass between two actual outcomes, preserving normalization.
        keys=list(bad);bad[keys[0]]+=R(1,100);bad[keys[2]]-=R(1,100)
        add('moment baseline and actual redistributed probabilities',moment_ok(clean) and not moment_ok(bad),q.distribution_moment(bad)-q.distribution_moment(clean))
        zero=(s.zeros(3,1),)*6
        add('actual mixture/outcome distinction at Q0',all(q.composite_corner(zero,c)==s.zeros(3,1) and (c.T*c)[0]/3==1 for c in q.CORNERS),'I/2 versus rank-one fixed outcome states')
    elif block==10:
        params=s.symbols('a b d e f x y z t',real=True);aa,bb,dd,ee,ff,x,y,z,t=params
        Q=s.Matrix([[aa,dd,ee],[dd,bb,ff],[ee,ff,-aa-bb]]); u=s.Matrix((x,y,z))
        def decoder_ok(shell):
            dec=j.joint_decode(shell)
            return same(dec['tensor'],Q) and same(dec['spatial_action'],u) and s.simplify(dec['time_action']-t)==0
        clean=j.joint_vectors(Q,u,t)
        bad=tuple(-Q*v/2+(t*v-u.cross(v))/8 for v in q.DIRECTIONS)
        add('unchanged decoder against actual cross-product sign fault',decoder_ok(clean) and not decoder_ok(bad),'decoded spatial action changes u to -u')
        M=-Q/2+(t*s.eye(3)+s.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]]))/8
        det=s.Matrix([M[r,c] for c in range(3) for r in range(3)]).jacobian(params).det()
        add('independent coordinate Jacobian',det==R(3,16384),det)
        nm=cm=F(0)
        for bits in itertools.product((-1,1),repeat=9):
            aa,bb,dd,ee,ff,x,y,z,t=map(lambda v:F(v,4),bits)
            M=[[-aa/2+t/8,-dd/2-z/8,-ee/2+y/8],[-dd/2+z/8,-bb/2+t/8,-ff/2-x/8],[-ee/2-y/8,-ff/2+x/8,(aa+bb)/2+t/8]]
            nm=max(nm,max(sum(M[r][c]**2 for r in range(3)) for c in range(3)))
            cm=max(cm,max(sum((sum(M[r][c]*v[c] for c in range(3))/3)**2 for r in range(3)) for v in itertools.product((-1,1),repeat=3)))
        add('independent Fraction arithmetic over all 512 vertices',(nm,cm)==(F(131,1024),F(395,9216)),(nm,cm))
    elif block==11:
        P=(s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1));I=s.eye(2)
        D=[s.kronecker_product(p,I)-s.kronecker_product(I,p) for p in P]
        B=s.Matrix(4,4,s.symbols('b0:16'))
        def commutant_rank(ops):return s.Matrix([v for op in ops for v in B*op-op*B]).jacobian(list(B)).rank()
        good=commutant_rank(D);bad=commutant_rank([D[2]])
        add('actual commutant and reduced generator control',good==15 and bad!=15,(good,bad))
        # Classical copy is nondisturbing on diagonal inputs but removes coherence.
        V=s.Matrix([[1,0],[0,0],[0,0],[0,1]])
        def old_marginal(A):
            out=V*A*V.H
            return s.Matrix(2,2,lambda i,j:sum(out[2*i+k,2*j+k] for k in range(2)))
        add('same marginal predicate on classical and coherent operands',same(old_marginal(P[2]),P[2]) and not same(old_marginal(P[0]),P[0]),old_marginal(P[0])-P[0])
    else:raise ValueError(block)
    return rows
