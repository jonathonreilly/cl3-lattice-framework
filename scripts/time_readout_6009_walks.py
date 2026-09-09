"""Original supplied finite walks: C903 nearest seeds and distinct C941 rounded seed.
Zero-step conventions are explicit. No physical source or controller is loaded.
"""
from fractions import Fraction
from itertools import product, combinations
from functools import lru_cache
NEIGHBOURS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
RBOX=4
MAX_STEPS=4
THETAS=tuple(map(Fraction,['1/2','1/3','2/5','1/7','3/8','5/6']))
def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cabs2(a):
    return a[0] * a[0] + a[1] * a[1]


def unit_point(t: Fraction):
    """Exact rational point on the unit circle (Cycle 885 parameterisation)."""
    s = Fraction(t)
    return (Fraction(1 - s * s) / (1 + s * s), Fraction(2 * s) / (1 + s * s))


def _lcg(seed: int, n: int, modulus: int):
    x = seed
    out = []
    for _ in range(n):
        x = (1103515245 * x + 12345) % (1 << 31)
        out.append(x % modulus)
    return out


def make_config(name: str, sites) -> dict:
    sites = tuple(sorted(set(tuple(int(c) for c in s) for s in sites)))
    n = len(sites)
    content = {s: (s[0] + s[1] + s[2]) % 2 for s in sites}
    return {"name": name, "sites": sites,
            "content": tuple((s, content[s]) for s in sites)}


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
        [(s[0] + 2, s[1] - 1, s[2] + 1)
         for s in [(0, 0, 0)] + list(NEIGHBOURS)]))
    return fam


def barycentre(cfg) -> tuple:
    sites = cfg["sites"]
    n = len(sites)
    return tuple(Fraction(sum(s[i] for s in sites), n) for i in range(3))


def shell_of(S) -> set:
    """Sites adjacent to S but not in S: the equivariant outer shell."""
    out = set()
    for s in S:
        for nb in NEIGHBOURS:
            t = (s[0] + nb[0], s[1] + nb[1], s[2] + nb[2])
            if t not in S:
                out.add(t)
    return out


def dilate(S, k: int) -> set:
    S = set(S)
    for _ in range(k):
        S = S | shell_of(S)
    return S


def erode(S, k: int) -> set:
    S = set(S)
    for _ in range(k):
        S = {s for s in S
             if all((s[0] + n[0], s[1] + n[1], s[2] + n[2]) in S
                    for n in NEIGHBOURS)}
    return S


def source_set(cfg) -> list:
    """Supplied source: all box sites closest to the barycentre."""
    c = barycentre(cfg)
    best, src = None, []
    for x in product(range(-RBOX, RBOX + 1), repeat=3):
        r2 = sum((Fraction(x[i]) - c[i]) ** 2 for i in range(3))
        if best is None or r2 < best:
            best, src = r2, [x]
        elif r2 == best:
            src.append(x)
    return src


FAMILY=build_family()

@lru_cache(None)
def counts(seeds,barrier,radius=4,depth=4):
    layers=[dict.fromkeys(seeds,1)]
    for _ in range(depth):
        nxt={}
        for x,c in layers[-1].items():
            for e in NEIGHBOURS:
                y=tuple(x[i]+e[i] for i in range(3))
                if max(map(abs,y))<=radius and y not in barrier:nxt[y]=nxt.get(y,0)+c
        layers.append(nxt)
    return layers

def mass(layers,seeds,window,t,include_zero=True):
    u=unit_point(t);powers=[(Fraction(1),Fraction(0))]
    for _ in range(len(layers)-1):powers.append(cmul(powers[-1],u))
    total=Fraction(0)
    for x in window:
        a=(Fraction(0),Fraction(0))
        for l,layer in enumerate(layers):
            if l==0 and not include_zero:continue
            c=Fraction(layer.get(x,0),len(seeds));a=cadd(a,(c*powers[l][0],c*powers[l][1]))
        total+=cabs2(a)
    return total

def spectrum(layers,seeds,window,include_zero=True):
    ds=[Fraction(0)]*len(layers)
    for x in window:
        cs=[Fraction(layer.get(x,0),len(seeds)) if include_zero or i else Fraction(0) for i,layer in enumerate(layers)]
        for i,a in enumerate(cs):
            for j,b in enumerate(cs):ds[abs(i-j)]+=a*b
    return tuple(ds)

def barriers():
    result=[('dilate_k0',lambda c:set(c['sites'])),('dilate_k1',lambda c:dilate(c['sites'],1)),('dilate_k2',lambda c:dilate(c['sites'],2)),('closing_1',lambda c:erode(dilate(c['sites'],1),1)),('opening_1',lambda c:dilate(erode(c['sites'],1),1))]
    for rank in range(3):
        def slit(c,rank=rank):
            sh=sorted(shell_of(c['sites']),key=lambda x:(sum((Fraction(x[i])-barycentre(c)[i])**2 for i in range(3)),x))
            return dilate(c['sites'],1)-{sh[rank]} if len(sh)>rank else dilate(c['sites'],1)
        result.append((f'slit_rank{rank}',slit))
    result.append(('halfspace_dilate',lambda c:set(c['sites'])|{x for x in dilate(c['sites'],1) if x[0]>=0}))
    result.append(('far_site',lambda c:set(c['sites'])|{(4,4,4)}))
    for seed in [11,97,313]:
        def inter(c,seed=seed):
            sh=sorted(shell_of(c['sites']));keep=_lcg(seed,len(sh),2)
            return set(c['sites'])|{x for x,k in zip(sh,keep) if k}
        result.append((f'intermediate_seed{seed}',inter))
    return result

def interference_results():
    rows=[];srcs={c['name']:tuple(source_set(c)) for c in FAMILY}
    for name,fn in barriers():
        per=[]
        for cfg in FAMILY:
            B=frozenset(fn(cfg));W=shell_of(B);seeds=srcs[cfg['name']];layers=counts(seeds,B)
            M=spectrum(layers,seeds,W);zs=[mass(layers,seeds,W,t) for t in THETAS]
            lengths={x:[l for l,L in enumerate(layers) if L.get(x,0)] for x in W}
            per.append({'configuration':cfg['name'],'seeds':seeds,'same_seed_parity':len({sum(x)%2 for x in seeds})==1,
                        'contains_support':set(cfg['sites'])<=B,'window_size':len(W),'mass_samples':list(map(str,zs)),
                        'spectrum':list(map(str,M)),'theta_dependent':any(M[1:]),'sample_moves':len(set(zs))>1,
                        'two_lengths_in_window':any(len(v)>=2 for v in lengths.values()),
                        'no_positive_length_motion':not any(layers[l] for l in range(1,5))})
        rows.append({'barrier':name,'contains_every_support':all(r['contains_support'] for r in per),
                     'theta_moving':[r['configuration'] for r in per if r['theta_dependent']],
                     'no_motion':[r['configuration'] for r in per if r['no_positive_length_motion']], 'rows':per})
    seeds=((-1,0,0),(0,0,0));target={(3,0,0)};L=counts(seeds,frozenset(),3,4)
    mixed={'seeds':seeds,'target':sorted(target),'radius':3,'depth':4,'lengths':[l for l,lay in enumerate(L) if lay.get((3,0,0))],
           'counts':[lay.get((3,0,0),0) for lay in L],'mass_theta0':str(mass(L,seeds,target,Fraction(0))), 'mass_theta1':str(mass(L,seeds,target,Fraction(1)))}
    return {'barriers':rows,'mixed_seed_control':mixed,'measured_core':sorted(set.intersection(*(set(r['theta_moving']) for r in rows if r['contains_every_support'])))}

def rounded_seed(cfg):
    ss=cfg['sites'];n=len(ss)
    return tuple((2*sum(s[i] for s in ss)+n)//(2*n) for i in range(3))

def structuring_sets(radius,rotations,apply):
    rem=set(product(range(-radius,radius+1),repeat=3));orbs=[]
    while rem:
        v=min(rem);orb=frozenset(apply(g,v) for g in rotations);orbs.append(orb);rem-=orb
    other=[o for o in orbs if (0,0,0) not in o]
    return [frozenset({(0,0,0)}.union(*(other[j] for j in range(len(other)) if bits>>j&1))) for bits in range(1<<len(other))]

def minkowski(S,T):return {tuple(x[i]+y[i] for i in range(3)) for x in S for y in T}

def statistics_results(rotations,apply):
    wins1=structuring_sets(1,rotations,apply);wins2=structuring_sets(2,rotations,apply)
    linear=[];profiles=[];window_signatures=[[] for _ in wins1];separated=0;seed_difference=[]
    for cfg in FAMILY:
        S=set(cfg['sites']);seed=rounded_seed(cfg);seeds=(seed,);layers=counts(seeds,frozenset(S))
        if set(seeds)!=set(source_set(cfg)):seed_difference.append(cfg['name'])
        linear.append({'configuration':cfg['name'],'support_size':len(S),'window_counts':[len(S&minkowski(S,T)) for T in wins2], 'drop_one_count':len(S-{min(S)})})
        profile=[]
        for i,T in enumerate(wins1):
            W=minkowski(S,T)
            # Preserve C941's own positive-length, theta-free statistic exactly.
            diag=sum(sum(layers[l].get(x,0)**2 for l in range(1,5)) for x in W)
            profile.append(diag)
            # Distinct full-mass statistic on C941's own single-seed, zero-step-included protocol.
            window_signatures[i].extend(spectrum(layers,seeds,W,True))
        profiles.append({'configuration':cfg['name'],'positive_length_diagonal_profile':profile})
        separated+=sum(profile[i]!=profile[j] for i in range(8) for j in range(i+1,8))
    return {'radius1_structuring_sets':[sorted(T) for T in wins1],'radius2_window_count':len(wins2),'linear_rows':linear,
            'linear_cells':len(FAMILY)*len(wins2),'configuration_profiles':profiles,
            'configuration_diagonal_classes':len({tuple(r['positive_length_diagonal_profile']) for r in profiles}),
            'diagonal_pair_separations':separated,'diagonal_pair_cells':12*28,
            'full_window_spectrum_signatures':[list(map(str,x)) for x in window_signatures],
            'full_window_classes_own_protocol':len(set(map(tuple,window_signatures))),
            'rounded_versus_all_nearest_seed_difference':seed_difference,
            'protocol_warning':'Neither statistic reproduces current892: distinct grouping, radius1 catalogue and rounded seed convention are explicit.'}
