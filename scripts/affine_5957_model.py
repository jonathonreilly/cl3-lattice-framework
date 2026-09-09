"""Finite supplied affine support model; no repository scan or physical selector."""
from fractions import Fraction as F
from itertools import product
from collections import Counter

DIRECTIONS = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))


def records():
    rows=[]
    for d,m,f,a in product(range(6),repeat=4):
        A=tuple(DIRECTIONS[m][i]+DIRECTIONS[f][i]+DIRECTIONS[a][i]-DIRECTIONS[d][i] for i in range(3))
        B=tuple(DIRECTIONS[f][i]-DIRECTIONS[a][i] for i in range(3))
        if not any(B): root='all' if not any(A) else None
        else:
            roots={F(-x,y) for x,y in zip(A,B) if y}
            root=next(iter(roots)) if len(roots)==1 and all(y or x==0 for x,y in zip(A,B)) else None
        rows.append({'support':(d,m,f,a),'A':A,'B':B,'root':root})
    return rows


def partition(rows):
    out={'all':[],'never':[],'roots':{}}
    for r in rows:
        key=r['support'];root=r['root']
        if root=='all':out['all'].append(key)
        elif root is None:out['never'].append(key)
        else:out['roots'].setdefault(str(root),[]).append(key)
    return out


def lawful(rows,t):
    return [r for r in rows if all(F(a)+t*b==0 for a,b in zip(r['A'],r['B']))]


def ledger(support,weight=1):
    d,m,f,a=support
    return tuple(tuple(weight*(DIRECTIONS[j][i]-(DIRECTIONS[d][i] if s==0 else 0)) for i in range(3)) for s,j in enumerate((m,f,a)))


def trace(block):return tuple(sum(row[i] for row in block) for i in range(3))


def grade(block,sigma):
    C=trace(block)
    return tuple(tuple(F(v)+(sigma-1)*F(C[i],3) for i,v in enumerate(row)) for row in block)


def response(array,sigma):
    g=tuple(grade(b,sigma) for b in array);pushed=g[::-1]
    pulled=tuple(grade(b,sigma) for b in g) # R twice is identity; G is applied twice.
    o1=tuple(v for b in pushed for row in b for v in row)
    o2=tuple(v for b in pulled for row in b for v in row)
    o3=tuple(v for b in pushed for v in trace(b))
    o4=(sum(v*v for v in o1),)
    o5=tuple(sum(b[s][i]*b[s][j] for s in range(3)) for b in pushed for i in range(3) for j in range(3))
    o6=(sum(g[0][s][i]*g[1][s][i] for s in range(3) for i in range(3)),)
    return (o1,o2,o3,o4,o5,o6)


def fibre_size(n,weights=6):return 2*n*weights+(n*weights)**2


def row_values(rows,t):
    """The original 23 selected rows, rewritten on explicit supplied definitions.

    The only t-dependence is the finite lawful support set and t=0/1 atoms.
    Other facts are independent of t by the proved identities in the note.
    These rows are not a census of external predicates or physical observables.
    """
    L=lawful(rows,t);blind=[r for r in L if not any(r['A'])]
    U={r['support'] for r in rows if r['root']=='all'}
    always={ (d,d^1,d,d) for d in range(6) }
    L0=lawful(rows,F(0));tb=sum(any(r['A']) for r in L)
    facts={
      'C873_TRACE_IS_THE_CONSERVATION_DEFECT':all(trace(ledger(r['support']))==r['A'] for r in rows),
      'C873_EVERY_LAWFUL_SUPPORT_IS_TRACELESS':tb==0,
      'C873_LAWFUL_GRADINGS_ARE_A_SEGMENT':U==always and (1+t)+(1-t)==2,
      'C873_WITNESS_IS_TRACE_BEARING':sum((-2,1,0))!=0,
      'C873_SIGN_WALL_UNQUALIFIED':all(not any(trace(grade(ledger(r['support']),1))[i]-trace(grade(ledger(r['support']),-1))[i] for i in range(3)) for r in L),
      'C876_RESIDUE_IS_ONE_RATIONAL':(1+t)+(1-t)==2,
      'C876_SIGMA_ONSET_IS_EXACTLY_PLUS_MINUS_ONE':(tb>0)==(t in (F(-1),F(1))),
      'C876_UNIT_IS_THE_UNIQUE_MAXIMISER':len(L0)>len(L) or t==0,
      'C876_TRACE_IS_GRADING_INDEPENDENT':all(trace(ledger(r['support']))==r['A'] for r in rows),
      'C876_LAWFUL_COUNT_IS_NINETY':len(L)==len(L0),
      'C876_SIGMA_VISIBILITY_TRACKS_THE_TRACE':all((grade(ledger(r['support']),1)!=grade(ledger(r['support']),-1))==bool(any(r['A'])) for r in rows),
      'C876_O3_IS_SIGMA_TIMES_THE_CONFORMAL_CHANNEL':all(trace(grade(ledger(r['support']),F(2)))==tuple(2*v for v in r['A']) for r in rows),
      'C880_LANDED_FAMILY_SIZE':fibre_size(len(U))==1368,
      'C880_LANDED_FAMILY_HAS_ZERO_CONFORMAL_CHANNEL':all(not any(trace(ledger(x))) for x in U),
      'C880_ALL_SIX_OBJECTS_BLIND_ON_THE_LANDED_FAMILY':all(grade(ledger(x),F(2))==ledger(x) for x in U),
      'C880_RESPONSE_SURFACE_CANNOT_SEE_SIGMA_UNQUALIFIED':tb==0,
      'C880_BLIND_LOCUS_IS_EXACTLY_THE_LANDED_FAMILY':{r['support'] for r in blind}==U,
      'C880_LANDED_320_IDENTITIES':all(x in {r['support'] for r in L} and not any(trace(ledger(x))) and any(ledger(x)[0]) for x in U),
      'C880_318_TWO_SECTOR_SUPPORT_LAWFUL':all(-DIRECTIONS[d][i]+(1+t)*DIRECTIONS[d][i]==DIRECTIONS[d][i] for d in range(6) for i in range(3)),
      'C880_873_WITNESS_ON_SHELL':-2+(1+t)==0,
      'C880_LOCUS_IS_A_SEGMENT_NOT_A_POINT':all(r['root'] is None or r['root']=='all' or r['root'] in (F(-1),F(0),F(1)) for r in rows),
      'C880_TOP_SIGMA_DEGREE':all(grade(ledger(r['support']),F(2))==tuple(tuple(2*x-y for x,y in zip(u,v)) for u,v in zip(grade(ledger(r['support']),F(1)),grade(ledger(r['support']),F(0)))) for r in rows),
      'C880_BLIND_LOCUS_SIZE_MATCHES_THE_LANDED_FAMILY':fibre_size(len(blind))==fibre_size(len(U))}
    return facts


def classify(tables):
    # Completeness is conditional on the factored Boolean rows above, not inferred by sampling.
    keys=list(tables['2']);out={}
    for key in keys:
        generic=tables['2'][key]
        out[key]={'generic':generic,'exceptions':{t:tables[t][key] for t in ['-1','0','1'] if tables[t][key]!=generic},
                  'classification':'T_UNIFORM' if generic and all(tables[t][key] for t in ['-1','0','1']) else 'T_SENSITIVE'}
    return out


def summary(table):
    return {'scope':'selected_23_affine_rows','row_count':len(table),
            'uniform_count':sum(r['classification']=='T_UNIFORM' for r in table.values()),
            'sensitive_count':sum(r['classification']=='T_SENSITIVE' for r in table.values()),
            'decision_surface_state':'SELECTED_CONDITIONAL_TABLE_ONLY'}


def validate_receipt(receipt,table):
    want=summary(table)
    return bool(table) and set(receipt)==set(want) and all(type(receipt[k]) is type(v) and receipt[k]==v for k,v in want.items())


def accepted(checks,refutations):return bool(checks) and all(v is True for v in checks.values()) and not refutations
