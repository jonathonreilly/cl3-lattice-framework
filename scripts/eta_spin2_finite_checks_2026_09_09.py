"""Exact finite checks for the five conditional Eta spin-2 theorems.

The large historical Laurent/Schur/history controllers are never invoked.
Each check reports its actual scope; scalar finite results are not physical selection.
"""
from __future__ import annotations
import itertools
from functools import cache
import sympy as s
import eta_spin2_affine_model_2026_09_09 as a
import eta_spin2_native_model_2026_09_09 as n
import eta_spin2_quadrupole_model_2026_09_09 as q
import eta_spin2_joint_model_2026_09_09 as j
import eta_spin2_nondisturbance_model_2026_09_09 as d
R=s.Rational

def equal(x,y):
    return x.shape==y.shape and all(s.simplify(v)==0 for v in x-y)

def rank(columns):
    return s.Matrix.hstack(*[s.Matrix(list(c)) for c in columns]).rank()

@cache
def fixtures():
    return {name:q.coeff_to_tensor(n.tt_source_coefficients(name)) for name in ('H1','H2')}

@cache
def source_rank():
    vertices=n.centered_objects((0,)*4,(0,)*4)[2]
    return rank(vertices)

@cache
def representation():
    Q=fixtures(); rots=a.rotations()
    orbits={name:tuple(r*t*r.T for r in rots) for name,t in Q.items()}
    basis=(s.diag(1,-1,0),s.diag(1,1,-2),s.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
           s.Matrix([[0,0,1],[0,0,0],[1,0,0]]),s.Matrix([[0,0,0],[0,0,1],[0,1,0]]))
    B=s.Matrix.hstack(*[s.Matrix(list(t)) for t in basis])
    reps=tuple(s.Matrix.hstack(*[B.gauss_jordan_solve(s.Matrix(list(r*t*r.T)))[0] for t in basis]) for r in rots)
    classes={}
    for r,rep in zip(rots,reps):
        power=s.eye(3)
        for order in range(1,13):
            power=power*r
            if power==s.eye(3): break
        key=(order,int(s.trace(r)),sum(r[i,i]!=0 for i in range(3)))
        classes.setdefault(key,[]).append((s.trace(rep[:2,:2]),s.trace(rep[2:,2:]),s.trace(rep)))
    return orbits,reps,classes

@cache
def orbit_census():
    action=a.selected_action(); reps=representation()[1]; unseen=set(range(64)); rows=[]
    while unseen:
        m=min(unseen); orbit={action(g,m) for g in range(24)}; unseen-=orbit
        stab=[g for g in range(24) if action(g,m)==m]
        fixed=s.Matrix.vstack(*[reps[g]-s.eye(5) for g in stab])
        parity=None
        if (m^63) in orbit:
            g=next(g for g in range(24) if action(g,m)==(m^63))
            parity=(5-s.Matrix.vstack(fixed,reps[g]-s.eye(5)).rank(),5-s.Matrix.vstack(fixed,reps[g]+s.eye(5)).rank())
        rows.append((m,len(orbit),len(stab),5-fixed.rank(),parity))
    return rows

def exact_box(dim):
    """Same 32/512 vertices using integer numerators; no fixture substitution."""
    nm=cm=0
    for v in itertools.product((-1,1),repeat=dim):
        aa,bb,dd,ee,ff=v[:5]
        Q=((aa,dd,ee),(dd,bb,ff),(ee,ff,-aa-bb))
        if dim==9:
            x,y,z,t=v[5:]; U=((0,-z,y),(z,0,-x),(-y,x,0))
            A=tuple(tuple(-4*Q[r][c]+U[r][c]+(t if r==c else 0) for c in range(3)) for r in range(3)); denom=32
        else:
            A=tuple(tuple(-3*Q[r][c] for c in range(3)) for r in range(3)); denom=16
        nm=max(nm,max(sum(A[r][c]**2 for r in range(3)) for c in range(3)))
        cm=max(cm,max(sum(sum(A[r][c]*corner[c] for c in range(3))**2 for r in range(3)) for corner in itertools.product((-1,1),repeat=3)))
    return R(nm,denom**2),R(cm,9*denom**2)

@cache
def target_bounds(joint):
    out={}
    for name,Q in fixtures().items():
        if joint:
            p,k=n.POINTS[name]; end=tuple(p[i]+k[i] for i in range(4))
            shells=[j.joint_vectors(Q,*j.normalized_action(x)) for x in (p,end)]
            decoded=[j.decoded_point(v) for v in shells]
            identity=decoded==[p,end]
        else:
            shells=[q.prepare_target(Q)]; identity=True
        ns=[s.simplify(q.norm_squared(v)) for shell in shells for v in shell]
        cs=[s.simplify(q.norm_squared(q.composite_corner(shell,c))) for shell in shells for c in q.CORNERS]
        nm=j.maximum_exact(tuple(ns)); cm=j.maximum_exact(tuple(cs))
        # Floating comparison only proposes a candidate; exact symbolic signs certify every bound.
        if not all(s.simplify(nm-v).is_nonnegative for v in ns):raise ArithmeticError('uncertified neighbor maximum')
        if not all(s.simplify(cm-v).is_nonnegative for v in cs):raise ArithmeticError('uncertified mixture maximum')
        out[name]=(nm,cm,identity,
                   all(equal((-48 if joint else -32)*q.distribution_moment(q.local_distribution(shell)),Q) for shell in shells))
    return out

def checks(block):
    rows=[]
    def check(name,ok,value): rows.append((name,bool(ok),str(value)))
    if block==7:
        c=n.tt_source_coefficients('H2'); target=tuple(s.simplify(c[i]/s.sqrt(2)) for i in (7,9,8))
        table=a.supplied_shear_table()
        anf=tuple(a.anf_coefficients(tuple(row[i] for row in table)) for i in range(3))
        reconstructed=tuple(tuple(a.evaluate_anf(anf[i],mask) for i in range(3)) for mask in range(64))
        check('actual Boolean interpolation and all64 evaluations',reconstructed==table,len(reconstructed))
        expected=s.Matrix((0,(s.sqrt(3)+3)/4,-(s.sqrt(3)+1)/4,-R(1,2),0,0,0,-s.sqrt(3)/2,0,1))
        check('actual TT nullspace column',equal(c,expected),tuple(c))
        check('all 64 supplied affine masks',not any(all(s.simplify(x-y)==0 for x,y in zip(row,target)) for row in table),len(table))
        h1=s.zeros(10,3)
        for col,slot in enumerate((7,9,8)):h1[slot,col]=s.sqrt(2)
        check('source subspace separation',h1.rank()==3 and h1.row_join(c).rank()==4,(3,4))
        check('native mass/occupation witness',source_rank()==10,source_rank())
        transformed=[]
        for r in a.rotations():
            for sign in (1,-1):
                T=s.eye(4);T[:3,:3]=sign*r; rep=n.tensor_representation(T)
                transformed.append((rep*h1).rank()==3 and (rep*h1).row_join(rep*c).rank()==4)
        check('all 48 invertible cubic/reflection images',all(transformed),len(transformed))
    elif block==8:
        orbits,reps,classes=representation()
        sizes=tuple(len(set(map(tuple,orbits[k]))) for k in ('H1','H2'))
        ranks=tuple(rank(orbits[k]) for k in ('H1','H2'))
        check('proper cubic tensor orbit spans',sizes==(24,24) and ranks==(3,5),(sizes,ranks))
        expected={(1,3,3):(1,(2,3,5)),(2,-1,1):(6,(0,1,1)),(2,-1,3):(3,(2,-1,1)),(3,0,0):(8,(-1,0,-1)),(4,1,1):(6,(0,-1,-1))}
        check('exact E plus T2 character table',all(len(classes[k])==v[0] and set(classes[k])=={v[1]} for k,v in expected.items()),classes)
        rows2=orbit_census(); expectedrows=[(0,6,4,2,(1,1)),(1,6,4,2,None),(4,12,2,3,(1,2)),(5,24,1,5,(3,2)),(7,6,4,2,None),(12,2,12,0,(0,0)),(21,4,6,1,None),(22,4,6,1,None)]
        check('all 64 affine masks and stabilizer spaces',rows2==expectedrows,rows2)
        check('equivariant function dimension and free orbit count',sum(r[3] for r in rows2)==16 and sum(r[2]==1 for r in rows2)==1,(16,1))
        check('native source rank on full and common spaces',source_rank()==10,(source_rank(),5))
    elif block==9:
        u=q.universal_facts()
        check('normalized rank-five moment identity',u['normalization']==1 and equal(u['moment_residual'],s.zeros(3)) and u['condition_rank']==u['probability_rank']==5,(u['normalization'],u['condition_rank'],u['probability_rank']))
        check('uniform Bloch-domain probability floors',u['axis_floor']==R(1,18) and u['corner_floor']==R(1,64),(u['diagonal_l1'],u['off_diagonal_l1'],u['axis_floor'],u['corner_floor']))
        cov=q.covariance_facts();check('all 24 simultaneous address/Bloch frames',not any(any(v) for v in cov['failures']),cov['rotation_count'])
        bounds=target_bounds(False)
        check('exact H1 and H2 preparations and source moment',all(x[0]<1 and x[1]<1 and x[2] and x[3] for x in bounds.values()),bounds)
        box=exact_box(5);check('all 32 vertices of the five-parameter box',box==(R(27,128),R(9,128)),box)
        zero=(s.zeros(3,1),)*6
        check('mixtures differ from fixed pure outcome menu',all(q.composite_corner(zero,c)==s.zeros(3,1) and q.norm_squared(c/s.sqrt(3))==1 for c in q.CORNERS),'Q=0: auxiliary mixtures I/2; fixed outcomes pure')
    elif block==10:
        f=j.decomposition_facts()
        check('exact joint scalar/vector/STF decoder',f['decode_identity'] and f['matrix_identity'] and (f['scalar_rank'],f['vector_rank'],f['spin2_rank'],f['sum_rank'],f['prepared_rank'])==(1,3,5,9,9),f)
        f=j.orthogonality_and_law_facts();check('conditional law excludes action scalar and skew sectors',f['probability_independence'] and f['source_identity'] and f['normalization']==1,f)
        f=j.covariance_facts();check('all 24 joint rotation identities',not any(f['failures']),f['rotation_count'])
        bounds=target_bounds(True);check('exact H1/H2 incoming and outgoing coordinates',all(x[0]<1 and x[1]<1 and x[2] and x[3] for x in bounds.values()),bounds)
        box=exact_box(9);check('all 512 original box vertices',box==(R(131,1024),R(395,9216)),box)
        f=d.shell_facts();check('actual positive-direction Jacobian',f['rank']==9 and f['determinant']==R(3,16384),(f['rank'],f['determinant']))
    elif block==11:
        f=d.shell_facts();check('open nine-parameter maximally mixed anchor',f['rank']==9 and f['maximally_mixed'] and f['antipodal'],(f['rank'],f['determinant']))
        f=d.pair_algebra_facts();check('pair differences generate full six-site algebra',f['commutator_sums'] and f['first_local'] and f['second_local'] and f['basis_rank']==16,(f['basis_rank'],f['full_six_qubit_dimension']))
        f=d.fixed_point_and_choi_facts();check('rank-one identity Choi support forces constant complement',f['pure_marginal_forces_product'] and f['identity_choi_rank']==1 and f['constant_complement_rank']==0,f)
        f=d.even_shell_facts();check('even shell cannot remove variable odd target',f['odd_decoder_unchanged'] and f['target_rank']==9 and f['full_rank']==18,f)
        f=d.classical_record_control_facts();check('orthogonal classical CNOT escape',f['unitary'] and f['zero_copy'] and f['one_copy'],f)
        f=d.approximate_clone_control_facts();check('actual approximate clone relaxed-premise channel',f['tp'] and f['marginal_shrink'] and f['identity'],f)
    else:raise ValueError(block)
    return rows
