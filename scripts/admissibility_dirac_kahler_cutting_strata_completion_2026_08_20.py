#!/usr/bin/env python3
"""Exact finite corner-simplex witnesses and boundary traces.

The original explicit witnesses, integer cell construction and point-free
3D facet enumeration are retained. Historical large-search assertions are
archived, not measured by this program. No historical module is executed.
The current cycle-726 source is parsed only for its literal WIT dictionary.
"""
from __future__ import annotations
import ast
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_CUTTING_STRATA_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md"
SUPPLIER = "scripts/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04.py"
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CUTTING_STRATA_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04.py",
)
INPUT_SHA256 = {
    NOTE: "3fcb5864a8a7f0fa183d9ce5ba17a5e31c385b632126e62c799ea332a16bb57b",
    SUPPLIER: "f30f37ff214db7bf6e003c5aa8ebfe0f0275c62554f38797c03940e87f31c0b5",
}

# Original finite definitions and explicit constructions, unchanged in logic.
CORNERS = 16

PIECES = 2672

CUTTING_SIZE = 24

COST_SPECTRUM = ((6, 400), (7, 1216), (8, 864), (9, 192))

VOLUME_SPECTRUM = ((0, 1360), (1, 2672), (2, 320), (3, 16))

FACET_DISSECTIONS = 180

TICK_SPECTRUM = ((18, 16), (19, 72), (20, 84), (21, 8))

MIXED_SPECTRUM = ((8, 12), (9, 64), (10, 104))

SLICE_INCIDENCES = 3584

WITNESS = {
    (36, 55): (22, 42, 102, 124, 194, 200, 845, 1056, 1142, 1182, 1292, 1390,
               1423, 1488, 1684, 1699, 1787, 2015, 2290, 2376, 2463, 2501,
               2519, 2611),                                   # C4 = 149
    (41, 53): (18, 100, 168, 172, 192, 216, 845, 1056, 1142, 1182, 1292, 1390,
               1423, 1488, 1684, 1699, 1787, 2017, 2045, 2290, 2376, 2503,
               2506, 2611),                                   # C4 = 156
    (37, 53): (22, 42, 102, 114, 194, 848, 872, 1142, 1182, 1217, 1390, 1423,
               1491, 1541, 1559, 1573, 1684, 1699, 1779, 1857, 2290, 2376,
               2598, 2615),                                   # C4 = 152
    (41, 48): (54, 82, 114, 242, 410, 500, 1020, 1109, 1148, 1164, 1217, 1223,
               1394, 1922, 1932, 1934, 2150, 2157, 2221, 2290, 2334, 2376,
               2598, 2615),                                   # C4 = 163
    (37, 48): (49, 242, 410, 417, 418, 507, 784, 1030, 1046, 1142, 1925, 1937,
               1964, 1981, 1991, 2022, 2078, 2081, 2128, 2151, 2154, 2158,
               2160, 2667),                                   # C4 = 165
}

WITNESS_COST = {(36, 55): 149, (41, 53): 156, (37, 53): 152,
                (41, 48): 163, (37, 48): 165}

PARTNER = {
    156: (22, 42, 96, 206, 781, 845, 1056, 1137, 1248, 1292, 1488, 1679, 2015,
          2209, 2256, 2312, 2441, 2538, 2543, 2584, 2595, 2626, 2647, 2659),
    152: (22, 42, 96, 194, 845, 1056, 1137, 1248, 1292, 1392, 1488, 1679, 2015,
          2208, 2256, 2441, 2448, 2538, 2547, 2584, 2591, 2595, 2626, 2659),
}

PER_PIECE_HISTOGRAM = ((3, 48), (4, 304), (5, 192), (6, 304), (7, 48),
                       (8, 336), (9, 672), (10, 624), (11, 96), (12, 48))

COUNTEREXAMPLE_SQUARE = (0, 0, 1, 1)

COUNTEREXAMPLE_CORNERS = (4, 5, 6, 7)

COUNTEREXAMPLE_PIECES = {
    (0, 0): ((1, 4, 5, 6, 9), (2, 5, 6, 7, 10)),
    (1, 1): ((4, 5, 7, 11, 15), (4, 6, 7, 11, 15)),
}

COUNTEREXAMPLE_DIAGONALS = {(0, 0): (5, 6), (1, 1): (4, 7)}

def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    total = 0
    for column in range(n):
        if matrix[0][column] == 0:
            continue
        minor = [
            [row[x] for x in range(n) if x != column] for row in matrix[1:]
        ]
        total += ((-1) ** column) * matrix[0][column] * det(minor)
    return total

COR = [tuple((k >> (3 - j)) & 1 for j in range(4)) for k in range(CORNERS)]

FACETS = [(i, c) for i in range(4) for c in (0, 1)]

TICK_FACETS = [f for f in FACETS if f[0] == 3]

SPAT_FACETS = [f for f in FACETS if f[0] != 3]

SQUARES = [(i, ci, j, cj) for i, j in itertools.combinations(range(4), 2)
           for ci in (0, 1) for cj in (0, 1)]

def rebuild_fixture():
    """The 2,672 unimodular cells and their C4/TC/MC charges, from scratch."""
    volumes: Counter = Counter()
    cells = []
    for combination in itertools.combinations(range(CORNERS), 5):
        edges = [
            [COR[combination[r + 1]][c] - COR[combination[0]][c]
             for c in range(4)]
            for r in range(4)
        ]
        volume = abs(det(edges))
        volumes[volume] += 1
        if volume == 1:
            cells.append(combination)
    c4, tc, mc = [], [], []
    for piece in cells:
        vertices = [COR[k] for k in piece]
        c4.append(sum(
            1 for a, b in itertools.combinations(range(5), 2)
            if sum(abs(vertices[a][c] - vertices[b][c]) for c in range(4)) > 1
        ))
        tick = mixed = 0
        for axis, side in FACETS:
            slab = [a for a in range(5) if vertices[a][axis] == side]
            if len(slab) != 4:
                continue
            others = [j for j in range(3) if j != axis]
            count = sum(
                1 for a, b in itertools.combinations(slab, 2)
                if sum(abs(vertices[a][x] - vertices[b][x]) for x in others) > 1
            )
            if axis == 3:
                tick += count
            else:
                mixed += count
        tc.append(tick)
        mc.append(mixed)
    return cells, tuple(sorted(volumes.items())), c4, tc, mc

def det3(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2]
                            - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2]
                              - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1]
                              - matrix[1][1] * matrix[2][0]))

def adj3(matrix):
    out = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            minor = [[matrix[r][c] for c in range(3) if c != i]
                     for r in range(3) if r != j]
            out[i][j] = ((-1) ** (i + j)) * (
                minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
            )
    return out

def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])

def square_corners(square):
    i, ci, j, cj = square
    return sorted(k for k in range(CORNERS)
                  if COR[k][i] == ci and COR[k][j] == cj)

def facet_squares(facet):
    axis, side = facet
    return [square for square in SQUARES
            if (square[0] == axis and square[1] == side)
            or (square[2] == axis and square[3] == side)]

def build_facets():
    """Per facet: its unimodular tetrahedra, its six-clique dissections, each
    one's charge cost, and the diagonal it induces on each of its six squares.

    The route is POINT-FREE: interior disjointness is decided by an EXHIBITED
    integer separating plane drawn from the two tetrahedra's facet normals and
    the cross products of their edge vectors, and a six-clique of pairwise
    interior-disjoint unimodular cells has total volume one, so it IS a
    dissection.  No sample lattice is involved anywhere.
    """
    info = {}
    for facet in FACETS:
        axis, side = facet
        keys = [k for k in range(CORNERS) if COR[k][axis] == side]
        kept = [j for j in range(4) if j != axis]
        points = {k: tuple(COR[k][j] for j in kept) for k in keys}
        cells = [
            combination for combination in itertools.combinations(keys, 4)
            if abs(det3([
                [points[combination[r + 1]][x] - points[combination[0]][x]
                 for x in range(3)]
                for r in range(3)
            ])) == 1
        ]
        edge_pairs = list(itertools.combinations(range(4), 2))

        def normals(cell):
            matrix = [
                [points[cell[j + 1]][r] - points[cell[0]][r] for j in range(3)]
                for r in range(3)
            ]
            rows = adj3(matrix)
            if det3(matrix) < 0:
                rows = [[-value for value in row] for row in rows]
            out = [tuple(rows[k]) for k in range(3)]
            out.append(tuple(-sum(rows[k][r] for k in range(3))
                             for r in range(3)))
            return out

        def separated(left, right):
            pa = [points[k] for k in left]
            pb = [points[k] for k in right]
            ea = [tuple(pa[y][r] - pa[x][r] for r in range(3))
                  for x, y in edge_pairs]
            eb = [tuple(pb[y][r] - pb[x][r] for r in range(3))
                  for x, y in edge_pairs]
            candidates = normals(left) + normals(right)
            for u in ea:
                for v in eb:
                    normal = cross(u, v)
                    if any(normal):
                        candidates.append(normal)
            for normal in candidates:
                va = [sum(a * b for a, b in zip(normal, p)) for p in pa]
                vb = [sum(a * b for a, b in zip(normal, p)) for p in pb]
                if max(va) <= min(vb) or max(vb) <= min(va):
                    return True
            return False

        size = len(cells)
        disjoint = [[False] * size for _ in range(size)]
        for a in range(size):
            for b in range(a + 1, size):
                value = separated(cells[a], cells[b])
                disjoint[a][b] = disjoint[b][a] = value
        cliques = []

        def grow(start, chosen):
            if len(chosen) == 6:
                cliques.append(tuple(chosen))
                return
            for a in range(start, size):
                if all(disjoint[a][j] for j in chosen):
                    chosen.append(a)
                    grow(a + 1, chosen)
                    chosen.pop()

        grow(0, [])
        live_axes = ([0, 1, 2] if axis == 3
                     else [p for p, j in enumerate(kept) if j != 3])

        def cost(cell):
            return sum(
                1 for a, b in itertools.combinations(cell, 2)
                if sum(abs(points[a][x] - points[b][x]) for x in live_axes) > 1
            )

        cell_cost = [cost(cells[a]) for a in range(size)]
        squares = facet_squares(facet)
        signatures, costs = [], []
        for clique in cliques:
            bits = []
            for square in squares:
                corners = set(square_corners(square))
                triangles = {
                    tuple(sorted(set(cells[a]) & corners)) for a in clique
                    if len(set(cells[a]) & corners) == 3
                }
                if len(triangles) != 2:
                    raise AssertionError(("square not split in two", facet,
                                          square))
                first, second = sorted(triangles)
                diagonal = tuple(sorted(set(first) & set(second)))
                listed = square_corners(square)
                bits.append(0 if diagonal == (listed[0], listed[3]) else 1)
            signatures.append(tuple(bits))
            costs.append(sum(cell_cost[a] for a in clique))
        info[facet] = dict(
            cells=cells,
            cliques=cliques,
            squares=squares,
            sigs=signatures,
            costs=costs,
            spec=tuple(sorted(Counter(costs).items())),
            pos={tuple(sorted(x)): n for n, x in enumerate(cells)},
            key={tuple(sorted(clique)): n for n, clique in enumerate(cliques)},
        )
    return info


# Exact 4D separation is a sufficient certificate here. This small family is
# not asserted to decide arbitrary polytope intersection: failure is inconclusive.
def separating_normal(left, right):
    candidates = [n for n in itertools.product((-1, 0, 1), repeat=4) if any(n)]
    for piece in (left, right):
        for face in itertools.combinations(piece, 4):
            edges = [[COR[k][j] - COR[face[0]][j] for j in range(4)] for k in face[1:]]
            candidates.append(tuple((-1)**j * det3([
                [row[k] for k in range(4) if k != j] for row in edges
            ]) for j in range(4)))
    for normal in candidates:
        if not any(normal):
            continue
        a = [sum(normal[j] * COR[k][j] for j in range(4)) for k in left]
        b = [sum(normal[j] * COR[k][j] for j in range(4)) for k in right]
        if max(a) <= min(b) or max(b) <= min(a):
            return normal
    return None


def traces(pieces, info):
    rows = {}
    for facet in FACETS:
        corners = {k for k in range(CORNERS) if COR[k][facet[0]] == facet[1]}
        slices = [tuple(sorted(set(piece) & corners)) for piece in pieces
                  if len(set(piece) & corners) == 4]
        if len(slices) != 6 or len(set(slices)) != 6:
            return None
        row = info[facet]
        key = tuple(sorted(row['pos'][s] for s in slices))
        if key not in row['key']:
            return None
        rows[facet] = row['key'][key]
    return rows


def square_trace(pieces, facet, square):
    fset = {k for k in range(CORNERS) if COR[k][facet[0]] == facet[1]}
    corners = set(square_corners(square))
    found = [piece for piece in pieces if len(set(piece) & fset) == 4
             and len(set(piece) & corners) == 3]
    triangles = sorted({tuple(sorted(set(piece) & corners)) for piece in found})
    diagonal = tuple(sorted(set(triangles[0]) & set(triangles[1]))) if len(triangles) == 2 else ()
    return tuple(sorted(found)), tuple(triangles), diagonal


def verify(pieces, cell_index, c4, tc, mc, info):
    ids = [cell_index[tuple(piece)] for piece in pieces]
    apart = sum(separating_normal(a, b) is not None
                for a, b in itertools.combinations(pieces, 2))
    rows = traces(pieces, info)
    charges = (sum(c4[i] for i in ids), sum(tc[i] for i in ids), sum(mc[i] for i in ids))
    traced_charge = None if rows is None else (
        sum(info[f]['costs'][rows[f]] for f in TICK_FACETS),
        sum(info[f]['costs'][rows[f]] for f in SPAT_FACETS))
    return {'distinct_cells': len(set(ids)), 'C4_TC_MC': charges,
            'separated_pairs': apart, 'pairs': len(ids)*(len(ids)-1)//2,
            'eight_valid_facet_traces': rows is not None,
            'charge_trace_agrees': traced_charge == charges[1:]}


def main():
    passed = failed = 0
    def check(label, condition, detail):
        nonlocal passed, failed
        ok = bool(condition)
        passed += int(ok)
        failed += int(not ok)
        print(('PASS ' if ok else 'FAIL ') + label + ': ' + detail, flush=True)

    inputs = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    mismatches = [p for p, data in inputs.items()
                  if hashlib.sha256(data).hexdigest() != INPUT_SHA256[p]]
    if mismatches:
        print('INPUT_BINDING_FAIL: ' + repr(mismatches), flush=True)
        return 1
    print('INPUT_BINDING: own note and current c726 literal-witness source verified before parsing', flush=True)
    print('SCOPE: supplied finite corner-simplex/pair-count model; no physical charge identification; no higher-stratum/minimum search', flush=True)
    cells, volumes, c4, tc, mc = rebuild_fixture()
    index = {tuple(cell): i for i, cell in enumerate(cells)}
    check('finite cells', len(cells) == PIECES and volumes == VOLUME_SPECTRUM
          and tuple(sorted(Counter(c4).items())) == COST_SPECTRUM,
          f'{len(cells)} unit-determinant cells; volume spectrum={volumes}; C4 spectrum={sorted(Counter(c4).items())}')
    info = build_facets()
    check('finite facet catalogue', all(len(info[f]['cliques']) == FACET_DISSECTIONS for f in FACETS)
          and all(info[f]['spec'] == TICK_SPECTRUM for f in TICK_FACETS)
          and all(info[f]['spec'] == MIXED_SPECTRUM for f in SPAT_FACETS),
          f'dissection counts={[len(info[f]["cliques"]) for f in FACETS]}; tick={info[(3,0)]["spec"]}; mixed={info[(0,0)]["spec"]}')
    incidence = sum(sum(COR[k][f[0]] == f[1] for k in cell) == 4 for cell in cells for f in FACETS)
    check('boundary incidences', incidence == SLICE_INCIDENCES, str(incidence))
    certificates = {}
    for label, ids in list(WITNESS.items()) + list(PARTNER.items()):
        pieces = [cells[i] for i in ids]
        cert = verify(pieces, index, c4, tc, mc, info)
        expected = ((WITNESS_COST[label], *label) if isinstance(label, tuple) else (label, 36, 60))
        check('original witness ' + str(label), cert['distinct_cells'] == CUTTING_SIZE
              and cert['C4_TC_MC'] == expected and cert['separated_pairs'] == 276
              and cert['pairs'] == 276 and cert['eight_valid_facet_traces'] and cert['charge_trace_agrees'],
              json.dumps(cert, sort_keys=True))
        certificates[label] = cert
    differences = {}
    for label, cost in [((41,53),156), ((37,53),152)]:
        a, b = certificates[label]['C4_TC_MC'], certificates[cost]['C4_TC_MC']
        differences[cost] = (a[1]-b[1], a[2]-b[2])
    check('same-cost differences', differences == {156:(5,-7),152:(1,-7)}, str(differences) + '; no local reversible-move claim')

    # Parse a pinned literal data assignment; never import/execute c726 or read its c725 gate receipt.
    assignments = [n for n in ast.parse(inputs[SUPPLIER]).body
                   if isinstance(n, ast.Assign) and any(isinstance(k, ast.Name) and k.id == 'WIT' for k in n.targets)]
    if len(assignments) != 1:
        raise ValueError('c726 WIT assignment is not unique')
    old = ast.literal_eval(assignments[0].value)
    expected_old = {'W1':(165,37,48), 'W3':(168,39,49), 'W4':(168,42,60),
                    'W5':(159,36,55), 'W6':(169,41,48)}
    if set(old) != set(expected_old):
        raise ValueError('c726 literal witness keys changed')
    for key, encoded in old.items():
        if len(encoded) != 120:
            raise ValueError('c726 witness encoding length')
        pieces = [tuple(ord(k)-ord('a') for k in encoded[i:i+5]) for i in range(0,120,5)]
        cert = verify(pieces, index, c4, tc, mc, info)
        check('existing supplier witness ' + key, cert['distinct_cells'] == 24
              and cert['C4_TC_MC'] == expected_old[key] and cert['separated_pairs'] == 276
              and cert['pairs'] == 276 and cert['eight_valid_facet_traces'] and cert['charge_trace_agrees'],
              json.dumps(cert, sort_keys=True))

    values = [a-b+c for a,b,c in zip(c4,tc,mc)]
    histogram = tuple(sorted(Counter(values).items()))
    minimum = min(values)
    example = cells[values.index(minimum)]
    check('direct per-piece bound counterexample', minimum == 3 and histogram == PER_PIECE_HISTOGRAM,
          f'min(C4-TC+MC)={minimum} at {example}; histogram={histogram}; only the uniform lower bound 7 is refuted')
    partner = [cells[i] for i in PARTNER[156]]
    square_rows = {f:square_trace(partner,f,COUNTEREXAMPLE_SQUARE) for f in ((0,0),(1,1))}
    check('incompatible boundary diagonals', all(square_rows[f][2] == COUNTEREXAMPLE_DIAGONALS[f] for f in square_rows),
          repr(square_rows) + '; cost 156 partner is geometrically verified above')
    # A separator must reject a full-dimensional piece paired with itself.
    check('overlap control', separating_normal(cells[0],cells[0]) is None,
          'identical simplex has no nonzero separating normal')
    print('HISTORICAL_UNVERIFIED: higher-stratum censuses, exact minima/exclusions, law sweep, CSP count and checker narratives are archived; none supplies a passing predicate here', flush=True)
    print('per_element: all 2672 supplied unit-determinant cells enumerated with integer charge formulas', flush=True)
    print('per_site: checked and not executed — physical sites are not defined by this finite corner-simplex model', flush=True)
    print('per_mode: checked and not executed — no physical momentum or mode decomposition is claimed', flush=True)
    print('per_block: seven original and five supplier dissections checked by exact separation and boundary traces', flush=True)
    print('lattice_wide: checked and not executed — no infinite lattice, physical realization or exhaustive higher-stratum search is claimed', flush=True)
    print(f'TOTAL: PASS={passed} FAIL={failed}', flush=True)
    return int(failed != 0)


if __name__ == '__main__':
    raise SystemExit(main())
