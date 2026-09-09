#!/usr/bin/env python3
"""Independent signed-star check of the actual finite model; no primary import.

The primary uses a dense matrix exponential. This checker constructs the exact
star exponential from independent occupied-list fermion signs and compares all
448-square entries of the actual model, including all number-sector zeros.
It reads primary declarations as AST data, and runs no parent campaign.
"""
from __future__ import annotations
import ast
import hashlib
import math
from pathlib import Path
import numpy as np
import full_fock_local_model_7871_2026_09_09 as model

AUDIT_TIMEOUT_SEC = 30
NOTE_PATH = "docs/FULL_FOCK_UNIT_WEIGHT_SOURCE_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = ("docs/FULL_FOCK_UNIT_WEIGHT_SOURCE_SUPPORT_NOTE_2026-07-28.md", "scripts/full_fock_local_model_7871_2026_09_09.py", "scripts/frontier_full_fock_unit_weight_source_2026_07_28.py")
DIRECT_HASHES = {'docs/FULL_FOCK_UNIT_WEIGHT_SOURCE_SUPPORT_NOTE_2026-07-28.md': 'f84db2d9ceb677bf542cb095307529c4d3a24967ced836482e9470249ec0c1aa', 'scripts/full_fock_local_model_7871_2026_09_09.py': '46f98210bf215a1998905baadc339237e8dbc0b704f4ad0875766e12ef69e5c5', 'scripts/frontier_full_fock_unit_weight_source_2026_07_28.py': '9695f2834ba1d589d78e112200c8e0761e27a7a80996c9ab0d47fdf051a9648c'}
ROOT = Path(__file__).resolve().parents[1]
TOLERANCE = 3e-10


def own_hop(mask, direction):
    occupied = [d for d in range(6) if mask & (1 << d)]
    opposite = direction ^ 1
    if direction not in occupied or opposite in occupied:
        return None
    sign = (-1) ** occupied.index(direction)
    occupied.remove(direction)
    sign *= (-1) ** sum(d < opposite for d in occupied)
    occupied.append(opposite)
    return sum(1 << d for d in occupied), sign


def star_operators(angle):
    # Independent construction in the same explicitly checked ordered basis.
    masks = sorted(range(64), key=lambda m: (m.bit_count(), tuple(d for d in range(6) if m & (1 << d))))
    index = {m:i for i,m in enumerate(masks)}
    exchange = np.zeros((448,448), complex)
    vertex = np.eye(448, dtype=complex)
    counts = [0,0,0]
    channels = []
    for mask in masks:
        center = 7*index[mask]
        leaves = []
        signs = []
        for d in range(6):
            hop = own_hop(mask,d)
            if hop is None:
                continue
            target, sign = hop
            leaf = 7*index[target]+1+d
            leaves.append(leaf); signs.append(sign)
            exchange[center,leaf] = exchange[leaf,center] = sign
            channels.append((mask,target,d,center,leaf))
            if mask.bit_count() <= 2:
                counts[mask.bit_count()] += 1
        k = len(leaves)
        if not k:
            continue
        bright = np.asarray(signs)/math.sqrt(k)
        c,s = math.cos(math.sqrt(k)*angle), math.sin(math.sqrt(k)*angle)
        vertex[center,center] = c
        vertex[center,leaves] = vertex[leaves,center] = 1j*s*bright
        vertex[np.ix_(leaves,leaves)] += (c-1)*np.outer(bright,bright)
    return masks,exchange,vertex,channels,counts


def main():
    for path, expected in DIRECT_HASHES.items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest() != expected:
            raise ValueError('source/input mismatch: '+path)
    outcomes=[]
    def check(label,condition,detail):
        outcomes.append(bool(condition)); print('PASS' if condition else 'FAIL',label,'::',detail)
    source=(ROOT/AUDIT_INPUT_PATHS[2]).read_text()
    literals={}
    for node in ast.parse(source).body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            try:literals[node.targets[0].id]=ast.literal_eval(node.value)
            except (ValueError,TypeError):pass
    check('actual bounded primary conventions',literals.get('N_MAX')==2 and literals.get('AUDIT_TIMEOUT_SEC')==30 and literals.get('NOTE_PATH')==NOTE_PATH, {k:literals.get(k) for k in ('N_MAX','AUDIT_TIMEOUT_SEC','NOTE_PATH')})
    masks,E,V,channels,counts=star_operators(model.ANGLE)
    actualE,actualV,_,N,P=model.local_source_blocks(model.ANGLE)
    check('independent occupied-list CAR signs and binomial channels',tuple(masks)==model.LOCAL_MASKS and np.array_equal(E,actualE) and counts==[0,6,24],counts)
    residual=float(np.max(abs(V-actualV)))
    check('all-entry signed-star versus actual dense exponential',residual<TOLERANCE,residual)
    numbers=np.repeat([m.bit_count() for m in masks],7)
    cross=numbers[:,None]!=numbers[None,:]
    leakage=float(np.max(abs(actualV[cross])))
    check('all-entry cross-sector zero and exact generator number law',leakage==0 and np.count_nonzero(actualE[cross])==0,leakage)
    weights={n:[] for n in (1,2)};ledger=[]
    directions=np.asarray(((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)))
    for mask,target,d,center,leaf in channels:
        if mask.bit_count() not in weights:continue
        k=sum(own_hop(mask,e) is not None for e in range(6))
        expected=math.sin(math.sqrt(k)*model.ANGLE)**2/k
        weights[mask.bit_count()].append((float(abs(actualV[leaf,center])**2),expected))
        before=sum((directions[e] for e in range(6) if mask & (1<<e)),start=np.zeros(3,int))
        after=sum((directions[e] for e in range(6) if target & (1<<e)),start=np.zeros(3,int))
        ledger.append(np.array_equal(after-before,-2*directions[d]))
    check('per-channel probabilities and unit-weight recoil',all(ledger) and max(abs(a-b) for rows in weights.values() for a,b in rows)<TOLERANCE,{n:(min(a for a,b in rows),max(a for a,b in rows)) for n,rows in weights.items()})
    # Compare all six actual one-carrier component rows to an independent closed form.
    p=math.sin(model.ANGLE)**2; residuals=[]
    for d in range(6):
        excited=np.zeros(6,complex);excited[d]=1
        out,report=model.vertex_gate(model.LinkState({(0,0,0):excited},{}),model.ANGLE)
        pair=out.pair[((0,0,0),(0,0,0))]
        expected=np.zeros((6,6,6),complex);expected[d^1,d,d]=1j*math.sin(model.ANGLE)
        residuals.extend([float(np.max(abs(pair-expected))),abs(float(np.vdot(pair,pair).real)-p),report['local_Q_residual'],report['local_P_residual']])
    check('six one-carrier link rows and supplied angle anchor',max(residuals)<TOLERANCE and abs(p-0.12589921612871374)<TOLERANCE,{'maximum_residual':max(residuals),'probability':p})
    # Same number-conservation predicate, clean and changed actual edge operands.
    bad=actualE.copy();mask=(1<<0)|(1<<2);target,sign=own_hop(mask,0)
    center=7*masks.index(mask);proper=7*masks.index(target)+1;wrong=7*masks.index(1<<1)+1
    bad[proper,center]=bad[center,proper]=0
    bad[wrong,center]=bad[center,wrong]=sign
    clean=float(np.linalg.norm(actualE@N-N@actualE));dirty=float(np.linalg.norm(bad@N-N@bad))
    check('actual mis-embedding rejected by unchanged number predicate',clean==0 and dirty>TOLERANCE and abs(dirty-math.sqrt(2))<TOLERANCE,{'clean':clean,'changed':dirty})
    print(f'TOTAL: PASS={sum(outcomes)} FAIL={len(outcomes)-sum(outcomes)}')
    return 0 if all(outcomes) else 1

if __name__=='__main__':
    raise SystemExit(main())
