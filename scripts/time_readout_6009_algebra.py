"""Supplied exact finite algebra for corrected time-family unit C.
No physical Record, readout scale, action, clock or framework selector is inferred.
Copied original definitions are mapped in the correction evidence, outside runtime.
"""
from fractions import Fraction
from itertools import product, permutations, combinations
from functools import lru_cache
from math import isqrt, gcd
I3=((1,0,0),(0,1,0),(0,0,1))
NEIGHBOURS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def q(x):return str(x) if x is not None else None
C883_FORMS = (
    ("w1 / (w0 + w1)^2", lambda w0, w1, n: Fraction(w1, (w0 + w1) ** 2)),
    ("w0 * w1 / n^2",    lambda w0, w1, n: Fraction(w0 * w1, n ** 2)),
    ("w1 / n^2",         lambda w0, w1, n: Fraction(w1, n ** 2)),
    ("(n - 1) / n^2",    lambda w0, w1, n: Fraction(n - 1, n ** 2)),
    ("w1 / (w0 * n^2)",  lambda w0, w1, n: Fraction(w1, w0 * n ** 2)),
    ("w0 / n",           lambda w0, w1, n: Fraction(w0, n)),
    ("(w0 + w1) / n^2",  lambda w0, w1, n: Fraction(w0 + w1, n ** 2)),
)


def rref(rows: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    A = [r[:] for r in rows]
    width = len(A[0]) if A else 0
    piv: list[int] = []
    r = 0
    for c in range(width):
        p = None
        for i in range(r, len(A)):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(width)]
        piv.append(c)
        r += 1
        if r == len(A):
            break
    return A, piv


def nullspace(rows: list[list[Fraction]], width: int) -> list[list[Fraction]]:
    if not rows:
        return [[Fraction(1) if j == k else Fraction(0) for j in range(width)]
                for k in range(width)]
    A, piv = rref(rows)
    free = [c for c in range(width) if c not in piv]
    basis = []
    for fc in free:
        v = [Fraction(0)] * width
        v[fc] = Fraction(1)
        for ri, pc in enumerate(piv):
            v[pc] = -A[ri][fc]
        basis.append(v)
    return basis


def rank_exact(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    _, piv = rref(rows)
    return len(piv)


def det3(m) -> int:
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def apply(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def transpose(m):
    return tuple(tuple(m[j][i] for j in range(3)) for i in range(3))


def element_order(m) -> int:
    k, c = 1, m
    while c != I3:
        c = mul(c, m)
        k += 1
        if k > 12:
            raise AssertionError("not a finite rotation")
    return k


def rotation_group() -> list:
    out = []
    for p in permutations(range(3)):
        for s in product((1, -1), repeat=3):
            m = [[0] * 3 for _ in range(3)]
            for i in range(3):
                m[i][p[i]] = s[i]
            m = tuple(tuple(r) for r in m)
            if det3(m) == 1:
                out.append(m)
    return sorted(out)


def generate(gens) -> frozenset:
    G = {I3}
    frontier = [I3]
    while frontier:
        x = frontier.pop()
        for s in gens:
            y = mul(x, s)
            if y not in G:
                G.add(y)
                frontier.append(y)
    return frozenset(G)


def conjugate(H: frozenset, g) -> frozenset:
    gi = transpose(g)          # orthogonal integer matrix: inverse = transpose
    return frozenset(mul(mul(g, h), gi) for h in H)


def subgroup_class_name(H: frozenset) -> str:
    """Canonical 888 census name, computed from invariants only."""
    n = len(H)
    if n == 1:
        return "E_trivial"
    cyc = any(element_order(h) == n for h in H)
    nrm = len([g for g in O24 if conjugate(H, g) == H])
    abelian = all(mul(x, y) == mul(y, x) for x in H for y in H)
    key = (n, cyc, abelian, nrm)
    table = {
        (2, True, True, 8): "C2_face",
        (2, True, True, 4): "C2_edge",
        (3, True, True, 6): "C3_body",
        (4, False, True, 24): "V_face",
        (4, False, True, 8): "V_edge",
        (4, True, True, 8): "C4_face",
        (6, False, False, 6): "S3_body",
        (8, False, False, 8): "D4_face",
        (12, False, False, 24): "A4_tetrahedral",
        (24, False, False, 24): "O_full",
    }
    return table.get(key, f"UNCLASSIFIED{key}")


def common_fixed_space(H: frozenset) -> list[list[Fraction]]:
    """Basis of {v in Q^3 : h v = v for all h in H}."""
    rows = []
    for h in H:
        for i in range(3):
            rows.append([Fraction(h[i][j] - (1 if i == j else 0))
                         for j in range(3)])
    return nullspace(rows, 3)


def normal_plane_basis(H: frozenset):
    """The GEOMETRIC normal plane: orthogonal complement in R^3 of the common
    fixed axis.  Returns None when the fixed locus is not a line -- the
    embedding-space reading has no normal plane there."""
    ax = common_fixed_space(H)
    if len(ax) != 1:
        return None, ax
    a = ax[0]
    n2 = sum(x * x for x in a)
    cand = []
    for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        v = [Fraction(x) for x in e]
        d = sum(v[i] * a[i] for i in range(3))
        cand.append([v[i] - d / n2 * a[i] for i in range(3)])
    basis: list[list[Fraction]] = []
    for w in cand:
        if rank_exact(basis + [w]) == len(basis) + 1:
            basis.append(w)
    if len(basis) != 2:
        return None, ax
    return basis, ax


def matrix_on_span(h, B: list[list[Fraction]]) -> list[list[Fraction]]:
    """Matrix of (I - h) restricted to span(B), in the basis B."""
    k = len(B)
    C = [[Fraction(0)] * k for _ in range(k)]
    for col in range(k):
        img = [B[col][i] - sum(h[i][j] * B[col][j] for j in range(3))
               for i in range(3)]
        rows = [[B[t][i] for t in range(k)] + [img[i]] for i in range(3)]
        A, piv = rref(rows)
        sol = [Fraction(0)] * k
        for ri, pc in enumerate(piv):
            if pc < k:
                sol[pc] = A[ri][k]
        # verify the solve
        recon = [sum(sol[t] * B[t][i] for t in range(k)) for i in range(3)]
        if recon != img:
            raise AssertionError("normal-plane solve failed")
        for row in range(k):
            C[row][col] = sol[row]
    return C


def det2(C) -> Fraction:
    return C[0][0] * C[1][1] - C[0][1] * C[1][0]


def L_face_geometric(H: frozenset):
    """READING R (embedding-space).  The retained anchor arithmetic:

        L(H) = (1/|H|) sum_{h != e} 1 / det_R(I - h |_N)

    with N the GEOMETRIC normal plane of the rotation axis.  Returns
    (value | None, diagnostic)."""
    B, ax = normal_plane_basis(H)
    if B is None:
        return None, {"reason": "no rotation axis: common fixed locus has "
                                f"dimension {len(ax)}, not 1",
                      "fixed_locus_dimension": len(ax)}
    total = Fraction(0)
    dets = {}
    for h in sorted(H):
        if h == I3:
            continue
        d = det2(matrix_on_span(h, B))
        dets[str(h)] = q(Fraction(d))
        if d == 0:
            return None, {"reason": "singular transverse determinant",
                          "fixed_locus_dimension": len(ax)}
        total += Fraction(1) / d
    return total / len(H), {"reason": "defined",
                            "fixed_locus_dimension": len(ax),
                            "transverse_determinants": dets}


def orbit_decomposition(H: frozenset, points) -> list[list[tuple]]:
    rem = set(points)
    orbits = []
    while rem:
        p = sorted(rem)[0]
        orb = {apply(h, p) for h in H}
        orbits.append(sorted(orb))
        rem -= orb
    return sorted(orbits)


def F_dim(n: int) -> Fraction:
    return Fraction(n - 1, n * n)


def F_res(n: int) -> Fraction:
    return Fraction(n * n - 1, 12 * n)


def harmonic_invariant_dim_by_character(d: int) -> int:
    """dim of O-invariants in the degree-d harmonic space, by an exact character
    sum over the five conjugacy classes of the chiral octahedral group.

    chi_d(phi) = sum_{m=-d}^{d} cos(m phi) for the rotation angle phi.
    Classes: E (1 elt, phi=0), 6C4 (phi=pi/2), 9 elements at phi=pi
    (3C2 + 6C2'), 8C3 (phi=2pi/3).  All character values are integers here.
    """
    def chi(cos_table) -> Fraction:
        # cos_table[m % period] holds 2*cos(m*phi) as an exact Fraction; the
        # m = 0 term is counted once.
        total = Fraction(1)
        for m in range(1, d + 1):
            total += cos_table[m % len(cos_table)]
        return total

    # 2*cos(m*phi) tables, exact
    t_0 = [Fraction(2)]                                   # phi = 0
    t_pi2 = [Fraction(2), Fraction(0), Fraction(-2), Fraction(0)]   # phi = pi/2
    t_pi = [Fraction(2), Fraction(-2)]                    # phi = pi
    t_2pi3 = [Fraction(2), Fraction(-1), Fraction(-1)]    # phi = 2pi/3

    total = (Fraction(1) * chi(t_0)
             + Fraction(6) * chi(t_pi2)
             + Fraction(9) * chi(t_pi)
             + Fraction(8) * chi(t_2pi3))
    val = total / 24
    assert val.denominator == 1 and val >= 0, (d, val)
    return int(val)


def harmonic_invariant_dim_by_algebra(d: int, mats) -> int:
    """Same number by brute linear algebra on degree-d monomials: the kernel of
    the stacked [average - I ; Laplacian] on the space of degree-d forms."""
    mons = [(i, j, d - i - j) for i in range(d + 1) for j in range(d - i + 1)]
    idx = {m: k for k, m in enumerate(mons)}
    n = len(mons)

    def expand(M, mon):
        """(sum_j M[0][j] x_j)^a (sum_j M[1][j] x_j)^b (...)^c as a dict."""
        cur = {(0, 0, 0): Fraction(1)}
        for row, power in zip(M, mon):
            for _ in range(power):
                nxt: dict = {}
                for base, coeff in cur.items():
                    for j in range(3):
                        if row[j] == 0:
                            continue
                        e = list(base)
                        e[j] += 1
                        key = tuple(e)
                        nxt[key] = nxt.get(key, Fraction(0)) + coeff * row[j]
                cur = nxt
        return cur

    avg = [[Fraction(0)] * n for _ in range(n)]
    for M in mats:
        # substitution x -> M^T x acting on monomials
        MT = tuple(tuple(M[r][c] for r in range(3)) for c in range(3))
        for mon in mons:
            for key, coeff in expand(MT, mon).items():
                avg[idx[key]][idx[mon]] += coeff / len(mats)

    rows = []
    for r in range(n):
        row = list(avg[r])
        row[r] -= 1
        rows.append(row)
    # Laplacian rows: map degree d -> degree d-2
    if d >= 2:
        lower = [(i, j, d - 2 - i - j) for i in range(d - 1)
                 for j in range(d - 1 - i)]
        lidx = {m: k for k, m in enumerate(lower)}
        lap = [[Fraction(0)] * n for _ in range(len(lower))]
        for mon in mons:
            for v in range(3):
                if mon[v] >= 2:
                    tgt = list(mon)
                    tgt[v] -= 2
                    lap[lidx[tuple(tgt)]][idx[mon]] += mon[v] * (mon[v] - 1)
        rows.extend(lap)
    return n - rank_exact(rows)


def screened_green(radius, mu2):
    """Exact Dirichlet-cube solve of (Delta - mu^2) G = -delta_0 on
    [-R,R]^3, symmetry-reduced to octahedral orbits.  Returns {orbit: G}."""
    box = [x for x in product(range(-radius, radius + 1), repeat=3)]
    key = lambda v: tuple(sorted(map(abs, v)))
    interior = [v for v in box if max(map(abs, v)) < radius]
    orbs = sorted({key(v) for v in interior})
    oi = {o: i for i, o in enumerate(orbs)}
    n = len(orbs)
    A = [[Fraction(0)] * n for _ in range(n)]
    rhs = [Fraction(0)] * n
    for o in orbs:
        rep = None
        for v in interior:
            if key(v) == o:
                rep = v
                break
        i = oi[o]
        A[i][i] += Fraction(-6) - Fraction(mu2)
        for e in NEIGHBOURS:
            y = (rep[0] + e[0], rep[1] + e[1], rep[2] + e[2])
            if max(map(abs, y)) >= radius:
                continue  # Dirichlet zero
            A[i][oi[key(y)]] += Fraction(1)
        if o == (0, 0, 0):
            rhs[i] = Fraction(-1)
    # solve A g = rhs exactly
    M = [row[:] + [rhs[r]] for r, row in enumerate(A)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return {o: M[oi[o]][n] for o in orbs}


O24=rotation_group()

@lru_cache(None)
def all_subgroups():
    """Close the subgroup lattice by adjoining every group element, no generator bound."""
    idx={m:i for i,m in enumerate(O24)};identity=idx[I3]
    table=[[idx[mul(a,b)] for b in O24] for a in O24]
    start=frozenset([identity]);seen={start};todo=[start]
    while todo:
        H=todo.pop()
        for g in range(24):
            if g in H:continue
            gens=tuple(H)+(g,);K={identity};queue=[identity]
            while queue:
                x=queue.pop()
                for y in gens:
                    z=table[x][y]
                    if z not in K:K.add(z);queue.append(z)
            K=frozenset(K)
            if K not in seen:seen.add(K);todo.append(K)
    return tuple(sorted((frozenset(O24[i] for i in H) for H in seen),key=lambda H:(len(H),sorted(H))))

def rotation_orbits(points):
    remain=set(points);out=[]
    while remain:
        p=min(remain);orb=frozenset(apply(g,p) for g in O24)
        assert orb<=set(points)
        out.append(orb);remain-=orb
    return out

def reconciliation_results():
    angular=[{'degree':d,'character':harmonic_invariant_dim_by_character(d),
              'monomial_laplacian':harmonic_invariant_dim_by_algebra(d,O24)} for d in range(13)]
    shell=[v for v in product(range(-4,5),repeat=3) if 1<=sum(x*x for x in v)<=16]
    orbit_rows=[{'representative':min(o),'size':len(o)} for o in rotation_orbits(shell)]
    components={'operator_ratio':1,'angular_tower_degree_1_to_12':sum(r['character'] for r in angular[1:]),
                'window_orbit_indicators':len(orbit_rows),'phase_and_calibration':2,'normalization':1}
    # These labels describe an explicitly supplied old chart, not physical dimensions.
    old_free=['sigma','theta','a','b','D','barrier','N','g'];additional=['mu','c4']
    rank=rank_exact([[Fraction(1),-1,0],[0,Fraction(1),-1]])
    return {'linear_C3_coefficient_rank':rank,'linear_C3_invariant_dimension':3-rank,
            'angular':angular,'window_orbits':orbit_rows,'declared_chart_free_names':old_free,
            'declared_extra_names':additional,'declared_chart_counts':[len(old_free),len(old_free+additional)],
            'orbit_components':components,'orbit_sum':sum(components.values()),
            'unmapped_old_labels':['sigma','D','barrier'],'augmented_label_sum':sum(components.values())+3,
            'alternative_shared_sigma_label_sum':sum(components.values())+2}

def vp(x,p):
    x=Fraction(x)
    if not x:raise ValueError('zero has no finite valuation')
    a,b=abs(x.numerator),x.denominator;n=0
    while a%p==0:a//=p;n+=1
    while b%p==0:b//=p;n-=1
    return n

def quadratic_solutions(N):
    N=Fraction(N)
    if N<=0:return {'kind':'empty_real','rational_solutions':[]}
    a=Fraction(1,N);x,y=isqrt(a.numerator),isqrt(a.denominator)
    if x*x==a.numerator and y*y==a.denominator:
        root=Fraction(x,y);return {'kind':'rational_pair','rational_solutions':[str(-root),str(root)]}
    return {'kind':'irrational_real_pair','alpha_squared':str(a),'rational_solutions':[]}

def escape_results():
    sigma=((0,0,1),(1,0,0),(0,1,0));s2=mul(sigma,sigma);identity=I3
    combine=lambda a,b,c:tuple(tuple(Fraction(a)*identity[i][j]+b*sigma[i][j]+c*s2[i][j] for j in range(3)) for i in range(3))
    coeffs=[(1,0,0),(-1,0,0),(Fraction(-1,3),Fraction(2,3),Fraction(2,3)),(Fraction(1,3),Fraction(-2,3),Fraction(-2,3))]
    involutions=[]
    for cs in coeffs:
        J=combine(*cs);w=tuple(sum(J[i][j] for i in range(3))-1 for j in range(3))
        involutions.append({'coefficients':list(map(str,cs)),'squared_identity':mul(J,J)==I3,
                            'commutes':mul(J,sigma)==mul(sigma,J),'solution':'all_Q' if not any(w) else 'zero','w':list(map(str,w))})
    grams=[]
    for p,qv in [(1,0),(1,Fraction(-1,2)),(Fraction(1,3),0),(2,1),(Fraction(243,4),0),(-1,0)]:
        G=combine(p,qv,qv);N=sum(map(sum,G));grams.append({'p':str(p),'q':str(qv),'N':str(N),'direct_matches':N==3*p+6*qv,**quadratic_solutions(N)})
    # Eisenstein integer arithmetic verifies the actual three-point Fourier matrix.
    omega=[(1,0),(0,1),(-1,-1)]
    wm=lambda x,y:(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
    wc=lambda x:(x[0]-x[1],-x[1])
    W=tuple(tuple(omega[i*j%3] for j in range(3)) for i in range(3))
    def prod(A,B):return tuple(tuple(tuple(sum(wm(A[i][k],B[k][j])[c] for k in range(3)) for c in range(2)) for j in range(3)) for i in range(3))
    Wstar=tuple(tuple(wc(W[j][i]) for j in range(3)) for i in range(3))
    threeI=tuple(tuple((3 if i==j else 0,0) for j in range(3)) for i in range(3))
    threeInv=tuple(tuple((3 if (i+j)%3==0 else 0,0) for j in range(3)) for i in range(3))
    ideal=[]
    for m in range(1,401):
        odd=m//(2**vp(m,2));formula=Fraction(2,odd)
        brute=next(Fraction(k,m) for k in range(1,2*m+1) if vp(Fraction(k,m),2)==1)
        ideal.append({'m':m,'odd_part':odd,'least_v2_one':str(formula),'brute':str(brute)})
    defect=[];alphas=[Fraction(2,27),Fraction(1,3),Fraction(1),Fraction(0),Fraction(2,9),Fraction(1,108)]
    for values in product(range(-3,4),repeat=3):
        admitted=[str(a) for a in alphas if all((n*a+(n-1)*values[0]).denominator==1 for n in range(1,7))]
        defect.append({'values':values,'admitted_probe_alphas':admitted})
    box=set(product(range(-2,3),repeat=3));edges=[(v,tuple(v[i]+e[i] for i in range(3))) for v in sorted(box) for e in NEIGHBOURS if tuple(v[i]+e[i] for i in range(3)) in box and v<tuple(v[i]+e[i] for i in range(3))]
    return {'involutions':involutions,'grams':grams,'DFT_WWstar':prod(W,Wstar)==threeI,'DFT_W2':prod(W,W)==threeInv,
            'P0_idempotent':mul(combine(Fraction(1,3),Fraction(1,3),Fraction(1,3)),combine(Fraction(1,3),Fraction(1,3),Fraction(1,3)))==combine(Fraction(1,3),Fraction(1,3),Fraction(1,3)),
            'normalizations':{str(n):quadratic_solutions(n) for n in [3,9]},'target_p_plus_2q':str(Fraction(1,3)/Fraction(2,27)**2),
            'ideal_rows':ideal,'defect_rows':defect,'bipartite_edges':len(edges),'all_edges_flip_parity':all((sum(a)-sum(b))%2 for a,b in edges),
            'C3_shell_pair_squared_distances':[sum((x-y)**2 for x,y in zip(u,v)) for u,v in combinations([(1,0,0),(0,1,0),(0,0,1)],2)], 'positive_chain':[str(Fraction(2,27)/2**i) for i in range(8)]}

def scope_results():
    subs=all_subgroups();rows=[]
    for H in subs:
        v,diag=L_face_geometric(H);rows.append({'class':subgroup_class_name(H),'order':len(H),'matrices':sorted(H),'normal_plane_value':q(v),'fixed_dimension':diag['fixed_locus_dimension'],'reason':diag['reason']})
    S=frozenset([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)])
    scopes=[H for H in subs if len(H)>1 and all(apply(h,p) in S for h in H for p in S)]
    ladder=[]
    for H in scopes:
        orb=orbit_decomposition(H,S);value,diag=L_face_geometric(H)
        ladder.append({'class':subgroup_class_name(H),'order':len(H),'orbit_count':len(orb),'simply_transitive':len(H)==len(S) and len(orb)==1,'value':q(value),'F_dim':str(F_dim(4))})
    forms=[]
    for name,fn in C883_FORMS:
        values=[]
        for H in scopes:
            w0=len(orbit_decomposition(H,S));w1=4-w0
            try:v=fn(w0,w1,4)
            except ZeroDivisionError:v=None
            values.append(q(v))
        forms.append({'name':name,'anchor':str(fn(1,2,3)),'values':values,'total':None not in values,'scope_constant':len(set(values))==1})
    return {'subgroups':rows,'collection':sorted(S),'scope_ladder':ladder,'forms':forms,
            'family_collision':[{'n':n,'F_dim':str(F_dim(n)),'F_res':str(F_res(n)),'alternative':str(F_dim(n)+(n-3)**2)} for n in range(2,9)]}

def action_results():
    pairs=[(1,6),(2,3),(3,2),(6,1),(Fraction(1,2),12),(12,Fraction(1,2))];radii=list(map(Fraction,['1','3/2','2','7/2']))
    rows=[{'lambda':str(a),'strength':str(b),'product':str(a*b),'actions':[str(1-Fraction(a*b)/(r+Fraction(1,10))) for r in radii]} for a,b in pairs]
    involutions=[]
    for a,b,c,d in product(range(-2,3),repeat=4):
        if (a*a+b*c,a*b+b*d,c*a+d*c,c*b+d*d)!=(1,0,0,1):continue
        M=((a,b),(c,d));N=[[Fraction(a-1),Fraction(b)],[Fraction(c),Fraction(d-1)]];ker=nullspace(N,2);preserves=a+c==1 and b+d==1
        involutions.append({'M':M,'preserves_sum':preserves,'fixed_directions':[list(map(str,x)) for x in ker], 'sum_constant_on_fixed_set':all(sum(x)==0 for x in ker)})
    return {'product_rows':rows,'off_product5':[str(1-Fraction(5)/(r+Fraction(1,10))) for r in radii],'involutions':involutions}
