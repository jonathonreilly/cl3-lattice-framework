"""Explicit finite Cycle885/887/893 fixtures and mathematical walk definitions.

Coordinates, content bits, depth labels, scalar weights and kernel are supplied
finite inputs. No physical Record, formation, measure or barrier is selected.
Copied definitions are identified in the outside-docs correction history.
"""
from fractions import Fraction
from itertools import product, permutations, combinations
from functools import lru_cache

NEIGHBOURS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def _lcg(seed: int, n: int, modulus: int):
    """Deterministic integer stream; no randomness enters any certified value."""
    x = seed
    out = []
    for _ in range(n):
        x = (1103515245 * x + 12345) % (1 << 31)
        out.append(x % modulus)
    return out


def make_config(name: str, sites) -> dict:
    """A supplied labelled configuration: support, per-record content bit, formation depth.

    Content is a supplied two-state label.  The depth label is assigned
    by an EQUIVARIANT rule -- the rank of the record's squared radius about the
    configuration's own barycentre -- so the filtration transports under G.
    """
    sites = tuple(sorted(set(tuple(int(c) for c in s) for s in sites)))
    n = len(sites)
    cx = tuple(Fraction(sum(s[i] for s in sites), n) for i in range(3))
    r2 = {s: sum((Fraction(s[i]) - cx[i]) ** 2 for i in range(3)) for s in sites}
    shells = sorted(set(r2.values()))
    depth = {s: 1 + shells.index(r2[s]) for s in sites}
    content = {s: (s[0] + s[1] + s[2]) % 2 for s in sites}
    return {
        "name": name,
        "sites": sites,
        "content": tuple((s, content[s]) for s in sites),
        "depth": tuple((s, depth[s]) for s in sites),
    }


def build_family() -> list:
    fam = []
    fam.append(make_config("single", [(0, 0, 0)]))
    fam.append(make_config("pair", [(0, 0, 0), (1, 0, 0)]))
    fam.append(make_config("shell1", list(NEIGHBOURS)))
    fam.append(make_config("ball1", [(0, 0, 0)] + list(NEIGHBOURS)))
    ann = [x for x in product(range(-2, 3), repeat=3)
           if 1 <= sum(c * c for c in x) <= 4]
    fam.append(make_config("annulus_1_4", ann))
    fam.append(make_config("hollow_annulus", [x for x in ann if x != (2, 0, 0)]))
    fam.append(make_config(
        "Lshape", [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (0, 2, 0)]))
    fam.append(make_config(
        "plane_square", [(i, j, 0) for i in range(3) for j in range(3)]))
    fam.append(make_config("chain", [(k, 0, 0) for k in range(5)]))
    box = [x for x in product(range(-2, 3), repeat=3)]
    for seed, tag in ((7, "a"), (2909, "b")):
        idx = sorted(set(_lcg(seed, 24, len(box))))[:9]
        fam.append(make_config(f"sparse_{tag}", [box[i] for i in idx]))
    fam.append(make_config(
        "offcentre_ball",
        [(s[0] + 2, s[1] - 1, s[2] + 1) for s in [(0, 0, 0)] + list(NEIGHBOURS)]))
    return fam


def det3(m) -> int:
    (a, b, c), (d, e, f), (g, h, i) = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def proper_cubic_rotations():
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            m = tuple(
                tuple(signs[r] if perm[r] == col else 0 for col in range(3))
                for r in range(3))
            if det3(m) == 1:
                out.append(m)
    return sorted(out)


ROT24 = proper_cubic_rotations()


IDENTITY3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def apply_mat(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


TEST_SHIFTS = ((0, 0, 0), (1, 0, 0), (0, -2, 0), (3, 1, -2), (-1, -1, -1))


def barycentre(cfg) -> tuple:
    sites = cfg["sites"]
    n = len(sites)
    if n == 0:
        return (Fraction(0), Fraction(0), Fraction(0))
    return tuple(Fraction(sum(s[i] for s in sites), n) for i in range(3))


def minkowski(sites, S):
    return set((s[0] + v[0], s[1] + v[1], s[2] + v[2]) for s in sites for v in S)


def erosion(sites, S):
    ss = set(sites)
    return set(x for x in ss
               if all((x[0] + v[0], x[1] + v[1], x[2] + v[2]) in ss for v in S))


def bounding_box(sites):
    if not sites:
        return set()
    lo = [min(x[i] for x in sites) for i in range(3)]
    hi = [max(x[i] for x in sites) for i in range(3)]
    return set(product(*[range(lo[i], hi[i] + 1) for i in range(3)]))


def axis_segment_closure(sites):
    """Add every lattice point on an axis-aligned segment between two records.

    Equivariant (the 24 rotations permute the axes with signs) and monotone.
    A non-Minkowski, hull-like closure.
    """
    ss = set(sites)
    out = set(ss)
    pts = sorted(ss)
    for i, p in enumerate(pts):
        for r in pts[i + 1:]:
            diff = [p[k] != r[k] for k in range(3)]
            if sum(diff) != 1:
                continue
            ax = diff.index(True)
            lo, hi = sorted((p[ax], r[ax]))
            for v in range(lo, hi + 1):
                y = list(p)
                y[ax] = v
                out.add(tuple(y))
    return out


def rotation_orbits(box_radius: int):
    pts = set(product(range(-box_radius, box_radius + 1), repeat=3))
    seen = set()
    orbs = []
    for p in sorted(pts):
        if p in seen:
            continue
        o = frozenset(apply_mat(m, p) for m in ROT24)
        assert o <= pts, "orbit escapes the box -- box is not rotation-closed"
        orbs.append(o)
        seen |= o
    return sorted(orbs, key=lambda o: (len(o), sorted(o)[0]))


S_ZERO = ((0, 0, 0),)


S_N6 = tuple(sorted(NEIGHBOURS))


S_BALL1 = tuple(sorted(set(NEIGHBOURS) | {(0, 0, 0)}))


S_BALL2 = tuple(sorted(
    x for x in product(range(-2, 3), repeat=3)
    if sum(abs(c) for c in x) <= 2))


S_FAR = tuple(sorted({(0, 0, 0)} | set(apply_mat(m, (2, 0, 0)) for m in ROT24)))


S_NOT_ROT_INV = ((0, 0, 0), (1, 0, 0))     # deliberately not rotation-invariant


CONST_CUBE = tuple(sorted(product((-1, 0, 1), repeat=3)))


def transform(cfg: dict, mat, shift) -> dict:
    content = dict(cfg["content"])
    depth = dict(cfg["depth"])
    back = {}
    for s in cfg["sites"]:
        t = apply_mat(mat, s)
        back[(t[0] + shift[0], t[1] + shift[1], t[2] + shift[2])] = s
    sites = tuple(sorted(back))
    return {"name": cfg["name"] + "|g", "sites": sites,
            "content": tuple((t, content[back[t]]) for t in sites),
            "depth": tuple((t, depth[back[t]]) for t in sites)}


_TRUNC_CACHE: dict = {}


def truncations(cfg):
    key = cfg["name"]
    if key not in _TRUNC_CACHE:
        levels = sorted(set(d for _, d in cfg["depth"]))
        _TRUNC_CACHE[key] = [
            make_config(f"{key}@{lv}", [s for s, d in cfg["depth"] if d <= lv])
            for lv in levels]
    return _TRUNC_CACHE[key]


def site_boundary(cfg) -> set:
    """885's W1b locus: sites adjacent to the support but not in it."""
    supp = set(cfg["sites"])
    out = set()
    for s in supp:
        for nb in NEIGHBOURS:
            t = (s[0] + nb[0], s[1] + nb[1], s[2] + nb[2])
            if t not in supp:
                out.add(t)
    return out


def b_supp(cfg):
    return set(cfg["sites"])


def b_empty(cfg):
    return set()


def mk_dilation(S):
    S = tuple(sorted(S))

    def f(cfg):
        return minkowski(cfg["sites"], S)
    return f


def mk_erosion(S):
    S = tuple(sorted(S))

    def f(cfg):
        return erosion(cfg["sites"], S)
    return f


def _nbr_counts(cfg) -> dict:
    cnt: dict = {}
    for s in cfg["sites"]:
        for nb in NEIGHBOURS:
            t = (s[0] + nb[0], s[1] + nb[1], s[2] + nb[2])
            cnt[t] = cnt.get(t, 0) + 1
    return cnt


def mk_threshold(k: int):
    """THRESHOLD family: block every site with at least `k` record neighbours.

    This family is NOT in 887's window catalogue.  It is the barrier analogue of
    the rank/threshold filters 887's own checker found the window enumeration had
    missed, and it is included here for exactly that reason: the 887 lesson is
    that the first enumeration is always short.
    """
    def f(cfg):
        return {x for x, c in _nbr_counts(cfg).items() if c >= k}
    return f


def mk_threshold_union(k: int):
    """supp(R) union the k-threshold set: a family straddling the identification."""
    def f(cfg):
        return set(cfg["sites"]) | {
            x for x, c in _nbr_counts(cfg).items() if c >= k}
    return f


def b_box(cfg):
    return bounding_box(cfg["sites"])


def b_segment(cfg):
    return axis_segment_closure(cfg["sites"])


def b_box_union_dil1(cfg):
    return bounding_box(cfg["sites"]) | minkowski(cfg["sites"], S_BALL1)


def b_size_keyed(cfg):
    S = S_ZERO if len(cfg["sites"]) <= 3 else S_BALL1
    return minkowski(cfg["sites"], S)


def readout(cfg):
    return sum((1, 2)[b] for _, b in cfg["content"])


def b_readout_keyed(cfg):
    S = S_ZERO if readout(cfg) <= 6 else S_BALL1
    return minkowski(cfg["sites"], S)


def b_depth_keyed(cfg):
    md = max([d for _, d in cfg["depth"]], default=0)
    S = S_ZERO if md <= 2 else S_BALL1
    return minkowski(cfg["sites"], S)


def b_boundary_shell(cfg):
    """885's refuted W1b locus, now offered as a BARRIER.  The brief asks
    whether the same computation that refuted it as a window refutes it here."""
    return site_boundary(cfg)


def b_extremal_shell(cfg):
    c = barycentre(cfg)
    r2 = {s: sum((Fraction(s[i]) - c[i]) ** 2 for i in range(3))
          for s in cfg["sites"]}
    top = max(r2.values())
    return {s for s in cfg["sites"] if r2[s] == top}


def b_constant_cube(cfg):
    return set(CONST_CUBE)


def b_nonequivariant(cfg):
    return minkowski(cfg["sites"], S_NOT_ROT_INV)


BARRIER_FAMILIES = {
    "DILATION": [
        ("B_supp__THE_IDENTIFICATION", b_supp),
        ("B_dilation_S_N6", mk_dilation(S_N6)),
        ("B_dilation_S_ball1__THICK", mk_dilation(S_BALL1)),
        ("B_dilation_S_ball2", mk_dilation(S_BALL2)),
        ("B_dilation_S_far_shell", mk_dilation(S_FAR)),
    ],
    "EROSION": [
        ("B_erosion_S_N6", mk_erosion(S_N6)),
        ("B_erosion_S_ball1", mk_erosion(S_BALL1)),
        ("B_erosion_S_ball2", mk_erosion(S_BALL2)),
    ],
    "THRESHOLD": [(f"B_threshold_k{k}", mk_threshold(k)) for k in range(1, 7)],
    "THRESHOLD_UNION": [
        (f"B_supp_union_threshold_k{k}", mk_threshold_union(k))
        for k in range(1, 7)],
    "HULL": [
        ("B_bounding_box", b_box),
        ("B_axis_segment_closure", b_segment),
        ("B_box_union_dilation1", b_box_union_dil1),
    ],
    "KEYED": [
        ("B_size_keyed", b_size_keyed),
        ("B_readout_keyed", b_readout_keyed),
        ("B_depth_keyed", b_depth_keyed),
    ],
    "CONTROL": [
        ("B_empty__NO_BARRIER_free_walk", b_empty),
        ("B_boundary_shell__885_refuted_W1b", b_boundary_shell),
        ("B_extremal_shell", b_extremal_shell),
        ("B_constant_cube__record_blind", b_constant_cube),
        ("B_nonequivariant_dilation", b_nonequivariant),
    ],
}


BARRIERS = [(n, f) for fam in BARRIER_FAMILIES.values() for n, f in fam]


S_BALL3 = tuple(sorted(x for x in product(range(-3, 4), repeat=3)
                       if sum(abs(c) for c in x) <= 3))


def mk_closing(S):
    """MORPHOLOGICAL CLOSING: erosion(dilation(supp, S), S).

    A family the primary's seven declared families do not contain.  Closing is a
    composition of two monotone equivariant maps, so it is a genuine admissible
    candidate and NOT a dilation: it fills concavities without growing the
    outer envelope the way a dilation does.
    """
    S = tuple(sorted(S))

    def f(cfg):
        return erosion(minkowski(cfg["sites"], S), S)
    return f


def mk_opening(S):
    """MORPHOLOGICAL OPENING: dilation(erosion(supp, S), S)."""
    S = tuple(sorted(S))

    def f(cfg):
        return minkowski(erosion(cfg["sites"], S), S)
    return f


def b_adaptive(cfg):
    """PER-SITE ADAPTIVE DILATION: each record dilates by a ball whose radius
    grows with its own local record density.  Not a fixed-S dilation, so not in
    the primary's DILATION family, and not keyed on a global statistic, so not
    in its KEYED family either."""
    supp = set(cfg["sites"])
    out = set()
    for s in supp:
        local = sum(1 for nb in NEIGHBOURS
                    if (s[0] + nb[0], s[1] + nb[1], s[2] + nb[2]) in supp)
        S = S_BALL1 if local >= 3 else S_ZERO
        for v in S:
            out.add((s[0] + v[0], s[1] + v[1], s[2] + v[2]))
    return out


def b_rank_nearest(cfg):
    """RANK FILTER: block the records nearest the barycentre (the half closest
    in squared radius).  887's checker found the window enumeration had missed
    rank filters; this is the barrier analogue and its admissibility is an open
    question until computed."""
    c = barycentre(cfg)
    r2 = sorted(((sum((Fraction(s[i]) - c[i]) ** 2 for i in range(3)), s)
                 for s in cfg["sites"]), key=lambda p: (p[0], p[1]))
    k = max(1, len(r2) // 2)
    return {s for _, s in r2[:k]}


NEW_BARRIERS = [
    ("NEW_closing_S_ball1", mk_closing(S_BALL1)),
    ("NEW_closing_S_ball2", mk_closing(S_BALL2)),
    ("NEW_opening_S_ball1", mk_opening(S_BALL1)),
    ("NEW_adaptive_local_density_dilation", b_adaptive),
    ("NEW_dilation_S_ball3", mk_dilation(S_BALL3)),
    ("NEW_rank_filter_nearest_half", b_rank_nearest),
]


FAMILY = build_family()
RBOX = 4
D = 4
BOX = frozenset(product(range(-RBOX, RBOX + 1), repeat=3))
THETAS = tuple(Fraction(a,b) for a,b in [(1,2),(1,3),(2,5),(1,7),(3,8),(5,6)])
WINDOWS = {
 'minkowski_S_zero__the_885_support_window': b_supp,
 'minkowski_S_ball1__885_checker_dilation_k1': mk_dilation(S_BALL1),
 'minkowski_S_ball2__885_checker_dilation_k2': mk_dilation(S_BALL2),
 'minkowski_S_far_shell__origin_present': mk_dilation(S_FAR),
 'bounding_box': b_box, 'axis_segment_closure': b_segment,
 'size_keyed_inflation': b_size_keyed, 'readout_keyed_inflation': b_readout_keyed,
 'union_box_with_dilation': b_box_union_dil1,
}

@lru_cache(None)
def sources(sites):
    centre = tuple(Fraction(sum(s[i] for s in sites),len(sites)) for i in range(3))
    distances = {x: sum((x[i]-centre[i])**2 for i in range(3)) for x in BOX}
    best = min(distances.values())
    return tuple(sorted(x for x in BOX if distances[x] == best))

@lru_cache(None)
def layers(sites, barrier):
    src = sources(sites)
    out = [{x: 1 for x in src}]
    for _ in range(D):
        nxt = {}
        for x,count in out[-1].items():
            for step in NEIGHBOURS:
                y = tuple(x[i]+step[i] for i in range(3))
                if y in BOX and y not in barrier:
                    nxt[y] = nxt.get(y,0)+count
        out.append(nxt)
    return out

@lru_cache(None)
def site_spectra(sites, barrier):
    ls = layers(sites,barrier)
    out = {}
    # Integer numerators; common denominator is |sources|^2.
    for x in set().union(*ls):
        c = [row.get(x,0) for row in ls]
        out[x] = tuple(sum(c[i]*c[j] for i in range(D+1) for j in range(D+1) if abs(i-j)==d) for d in range(D+1))
    return out


def spectrum(cfg, window, barrier=None):
    sites = tuple(cfg['sites']);barrier = frozenset(sites) if barrier is None else frozenset(barrier)
    ss = site_spectra(sites,barrier);den = len(sources(sites))**2
    return tuple(Fraction(sum(ss.get(x,(0,)*5)[d] for x in set(window)&BOX),den) for d in range(D+1))


def cheb_values(p):
    out = [Fraction(1),p]
    for _ in range(2,D+1):out.append(2*p*out[-1]-out[-2])
    return out


def evaluate(spectrum, theta):
    p = (1-theta*theta)/(1+theta*theta)
    return sum(a*b for a,b in zip(spectrum,cheb_values(p)))


def direct_masses(cfg, theta, barrier=None):
    sites = tuple(cfg['sites']);barrier=frozenset(sites) if barrier is None else frozenset(barrier)
    ls=layers(sites,barrier);n=len(sources(sites));den=1+theta*theta
    u=((1-theta*theta)/den,2*theta/den);up=(Fraction(1),Fraction(0));amp={}
    for row in ls:
        for x,c in row.items():
            a,b=amp.get(x,(Fraction(0),Fraction(0)));amp[x]=(a+up[0]*c/n,b+up[1]*c/n)
        up=(up[0]*u[0]-up[1]*u[1],up[0]*u[1]+up[1]*u[0])
    return {x:a*a+b*b for x,(a,b) in amp.items()}


def partition(signatures):
    buckets={}
    for label,signature in signatures.items():buckets.setdefault(signature,[]).append(label)
    return sorted(sorted(v) for v in buckets.values())


def refines(p,q):
    return all(any(set(a)<=set(b) for b in q) for a in p)


def partition_relation(p,q):
    pq,qp=refines(p,q),refines(q,p)
    return 'same' if pq and qp else 'finer' if pq else 'coarser' if qp else 'incomparable'


def finite_map_checks(fn):
    eq=rot=checks=mono=mpairs=0
    for cfg in FAMILY:
        initial=set(fn(cfg))
        for mat in ROT24:
            for shift in TEST_SHIFTS:
                checks+=1
                expected={tuple(apply_mat(mat,x)[i]+shift[i] for i in range(3)) for x in initial}
                if set(fn(transform(cfg,mat,shift)))!=expected:
                    eq+=1;rot+=int(shift==(0,0,0))
        chain=[set(fn(sub)) for sub in truncations(cfg)]
        mono+=sum(not a<=b for a,b in zip(chain,chain[1:]));mpairs+=max(0,len(chain)-1)
    distinct=len({frozenset(fn(c)) for c in FAMILY})
    return dict(equivariance_checks=checks,equivariance_failures=eq,rotation_only_failures=rot,monotonicity_pairs=mpairs,monotonicity_failures=mono,distinct=distinct,finite_filter=(eq==0 and mono==0 and distinct>1))


def alternate_centre(cfg):
    centre=barycentre(cfg)
    dist={x:sum((x[i]-centre[i])**2 for i in range(3)) for x in cfg['sites']}
    return barycentre({'sites':tuple(x for x in cfg['sites'] if dist[x]==max(dist.values()))})


def window_results():
    checks={name:finite_map_checks(fn) for name,fn in [('support',b_supp),('boundary_shell',site_boundary),('constant_cube',b_constant_cube),('dilation1',mk_dilation(S_BALL1)),('dilation2',mk_dilation(S_BALL2))]}
    centres=[c['name'] for c in FAMILY if barycentre(c)!=alternate_centre(c)]
    theta=[c['name'] for c in FAMILY if any(spectrum(c,site_boundary(c))[1:])]
    seed_rows=[]
    for c in FAMILY:
        support=set(c['sites']);ls=layers(c['sites'],frozenset(support));src=set(sources(c['sites']))
        seed_rows.append({'configuration':c['name'],'support_mass':str(spectrum(c,support)[0]),'seed_mass_on_support':str(Fraction(len(src&support),len(src)**2)),'positive_length_landings_on_support':len(support&set().union(*ls[1:]))})
    return {'finite_map_checks':checks,'centre_disagreement_configurations':centres,'boundary_theta_moving':theta,'support_seed_rows':seed_rows,'orbit_counts':{r:len(rotation_orbits(r)) for r in [1,2,3]}}


def barrier_fate(name,fn):
    sigs={w:[] for w in WINDOWS};rows=[]
    for c in FAMILY:
        barrier=frozenset(fn(c));ls=layers(c['sites'],barrier);reach=set().union(*ls[1:]);src=set(sources(c['sites']));supp=set(c['sites'])
        for w,wfn in WINDOWS.items():sigs[w].extend(spectrum(c,wfn(c),barrier))
        rows.append({'configuration':c['name'],'contains_support':supp<=barrier,'positive_length_support_landings':len(reach&supp),'frozen':not reach,'potential_support_on_records':len((reach|src)&supp),'boundary_theta_moving':any(spectrum(c,site_boundary(c),barrier)[1:])})
    return {'barrier':name,'partition':partition({w:tuple(v) for w,v in sigs.items()}),'configurations':rows}


def barrier_results():
    # Original31 named maps and six explicitly listed original checker additions.
    out={name:{'finite_map_checks':finite_map_checks(fn),**barrier_fate(name,fn)} for name,fn in BARRIERS+NEW_BARRIERS}
    reference=out['B_supp__THE_IDENTIFICATION']['partition']
    for row in out.values():row['partition_relation_to_support']=partition_relation(row['partition'],reference)
    return out


def bridge_results():
    profiles={};allvalues=[]
    for c in FAMILY:
        s={n:spectrum(c,fn(c)) for n,fn in WINDOWS.items()}
        vals={n:tuple(evaluate(v,t) for t in THETAS) for n,v in s.items()};pairs=[]
        for a,b in combinations(sorted(WINDOWS),2):
            valid=[i for i in range(len(THETAS)) if vals[b][i]>0]
            ratios={vals[a][i]/vals[b][i] for i in valid}
            if len(ratios)>1:pairs.append({'numerator':a,'denominator':b,'positive_denominator_indices':valid,'ratios':[str(vals[a][i]/vals[b][i]) for i in valid]})
        profiles[c['name']]={'varying_ratio_pairs':pairs,'total_pairs':36,'window_values':{n:list(map(str,v)) for n,v in vals.items()}}
        allvalues.extend(v for row in vals.values() for v in row)
    a=next(c for c in FAMILY if c['name']=='shell1');b=next(c for c in FAMILY if c['name']=='offcentre_ball');fixed=frozenset(a['sites'])|frozenset(b['sites'])
    witness={'target_sites':sorted(fixed),'configurations':[a['name'],b['name']],'contains_both_supports':set(a['sites'])<=fixed and set(b['sites'])<=fixed,'masses':[str(evaluate(spectrum(c,fixed),THETAS[0])) for c in [a,b]],'theta':str(THETAS[0])}
    return {'fixed_set_witness':witness,'per_configuration':profiles,'zero_cells':sum(x==0 for x in allvalues),'grid_cells':len(allvalues),'restricted_bridge_rejected_configurations':[n for n,row in profiles.items() if row['varying_ratio_pairs']]}


def rref(rows,ncols):
    matrix=[[Fraction(x) for x in row] for row in rows];r=0;piv=[]
    for col in range(ncols):
        p=next((i for i in range(r,len(matrix)) if matrix[i][col]),None)
        if p is None:continue
        matrix[r],matrix[p]=matrix[p],matrix[r];v=matrix[r][col];matrix[r]=[x/v for x in matrix[r]]
        for i in range(len(matrix)):
            if i!=r and matrix[i][col]:
                v=matrix[i][col];matrix[i]=[x-v*y for x,y in zip(matrix[i],matrix[r])]
        piv.append(col);r+=1
        if r==len(matrix):break
    return matrix,piv,r


def atoms(cfg):
    windows=[set(fn(cfg))&BOX for fn in WINDOWS.values()];supp=set(cfg['sites'])&BOX;universe=set().union(*windows,supp);buckets={}
    for x in sorted(universe):buckets.setdefault(tuple(x in w for w in windows)+(x in supp,),[]).append(x)
    return [tuple(v) for _,v in sorted(buckets.items())]


def canonical_coefficients(cfg):
    return [spectrum(cfg,a) for a in atoms(cfg)]


def linear_system(cfg,restrictions):
    ats=atoms(cfg);n=len(ats)*5;rows=[]
    for fn in WINDOWS.values():
        w=set(fn(cfg))&BOX;sp=spectrum(cfg,w)
        for d in range(5):
            row=[Fraction(0)]*(n+1)
            for i,a in enumerate(ats):
                if set(a)<=w:row[5*i+d]=1
            row[-1]=sp[d];rows.append(row)
    if 'content_identification' in restrictions:
        content=dict(cfg['content'])
        for i,a in enumerate(ats):
            if not set(a)&set(cfg['sites']):continue
            for d in range(5):
                row=[Fraction(0)]*(n+1);row[5*i+d]=1;row[-1]=sum((1,2)[content[x]] for x in a) if d==0 else 0;rows.append(row)
    if 'theta_free' in restrictions:
        for i in range(len(ats)):
            for d in range(1,5):
                row=[Fraction(0)]*(n+1);row[5*i+d]=1;rows.append(row)
    if 'null_windows' in restrictions:
        for fn in WINDOWS.values():
            w=set(fn(cfg))&BOX
            if any(spectrum(cfg,w)):continue
            for i,a in enumerate(ats):
                if set(a)<=w:
                    for d in range(5):
                        row=[Fraction(0)]*(n+1);row[5*i+d]=1;rows.append(row)
    rank=rref([r[:-1] for r in rows],n)[2];aug=rref(rows,n+1)[2]
    return {'rank':rank,'augmented_rank':aug,'consistent':rank==aug,'unknowns':n,'nullity':n-rank,'equations':len(rows)},rows


def spectrum_results():
    rows=[spectrum(c,fn(c)) for fn in WINDOWS.values() for c in FAMILY]
    rank=rref(rows,5)[2];evalrows=[cheb_values((1-t*t)/(1+t*t)) for t in THETAS]
    per={};grid=0;violations=0
    for c in FAMILY:
        canonical=canonical_coefficients(c);ats=atoms(c);systems={}
        for name,rules in [('bridge',set()),('bridge_content',{'content_identification'}),('bridge_null',{'null_windows'}),('all',{'content_identification','null_windows'}),('theta_free',{'theta_free'})]:
            st,eqs=linear_system(c,rules);st['canonical_residual_nonzero']=sum(sum(a*b for a,b in zip(row[:-1],[x for atom in canonical for x in atom]))!=row[-1] for row in eqs);systems[name]=st
        for t in THETAS:
            direct=direct_masses(c,t)
            for fn in WINDOWS.values():
                w=set(fn(c))&BOX;fromatoms=sum(evaluate(v,t) for a,v in zip(ats,canonical) if set(a)<=w);actual=sum(direct.get(x,0) for x in w);grid+=1;violations+=fromatoms!=actual
        per[c['name']]={'spectrum_rank':rref([spectrum(c,fn(c)) for fn in WINDOWS.values()],5)[2],'atoms':[{'sites':a,'coefficients':list(map(str,v))} for a,v in zip(ats,canonical)],'systems':systems,'linear_content':readout(c),'seed_support_mass':str(spectrum(c,c['sites'])[0])}
    return {'realized_span_rank':rank,'spectrum_rows':len(rows),'evaluation_rank':rref(evalrows,5)[2],'five_point_evaluation_rank':rref(evalrows[:5],5)[2],'per_configuration':per,'canonical_grid_cells':grid,'canonical_grid_violations':violations,'continuum_nonnegativity':'proved by the actual squared-amplitude construction in note; grid is a consistency check'}

def synthetic_weighting_profile():
    """Exact aggregation of the original894 synthetic fixture, not actual878 events."""
    n_worlds,n_formed,total,unformed_events,moment0_events=748,164,92260,73088,3096
    n_unformed=n_worlds-n_formed;first,rem=divmod(unformed_events,n_unformed)
    counts=[first+1]*rem+[first]*(n_unformed-rem)
    n_m0=moment0_events//129;counts += [129]*n_m0
    first,rem=divmod(total-unformed_events-moment0_events,n_formed-n_m0)
    counts += [first+1]*rem+[first]*(n_formed-n_m0-rem)
    formation={w:0 if w<n_unformed+n_m0 else w-n_unformed-n_m0+1 for w in range(n_unformed,n_worlds)}
    worldweights={
      'M2_PER_WORLD_UNIFORM':[1]*n_worlds,
      'M3_OCCUPATION_WEIGHTED':[0 if w<n_unformed else 1+w%7 for w in range(n_worlds)],
      'M4_FORMATION_LIFETIME':[0 if w not in formation else 16384-formation[w]+1 for w in range(n_worlds)],
      'M5_FORMATION_MOMENT':[formation.get(w,0) for w in range(n_worlds)],
    }
    out={'M1_COUNTING':{'zero_atoms':0,'total_mass':str(total),'on_formed_fraction':str(Fraction(total-unformed_events,total))}}
    for name,weights in worldweights.items():
        norm=sum(weights)
        out[name]={'zero_atoms':sum(counts[w] for w in range(n_worlds) if weights[w]==0),'total_mass':'1','on_formed_fraction':str(Fraction(sum(weights[n_unformed:]),norm))}
    return {'fixture':'synthetic original894 aggregate construction; no878 input identity or physical covariance','world_count':len(counts),'event_count':sum(counts),'event_counts_by_world':counts,'formation_times':formation,'weightings':out}
