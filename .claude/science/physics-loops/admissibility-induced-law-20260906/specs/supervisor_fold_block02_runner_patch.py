import sys, pathlib
p = pathlib.Path(sys.argv[1]); t = p.read_text(encoding="utf-8"); orig = t
def rep(old, new, count=1):
    global t
    assert t.count(old) == count, (old[:70], t.count(old))
    t = t.replace(old, new)
# (i) fence 1: the order class stated precisely
rep('"This note selects no physical formation order; the row sweep is a declared order whose exact solvability is a property of two-recorded-neighbor sweeps on two-dimensional windows.",',
    '"This note selects no physical formation order; the row sweep is a declared order whose exact solvability is a property of sweeps in which each site forms with one in-row predecessor and the site below it as its recorded neighbors, on two-dimensional windows with an unrecorded exterior.",')
# (ii) mutations
rep('    "second_eigenvalue_bound_too_small": "E",\n',
    '    "second_eigenvalue_bound_too_small": "E",\n    "boundary_dependence_forged": "E",\n    "restriction_lemma_broken": "D",\n')
# (iii) restriction lemma in family D: the width-3 two-row joint restricted to columns {0,1} equals the width-2 two-row joint
rep('''    checks.check("D1", d1, "E2 row kernel from the formula equals the kernel from the definition entrywise, W = 2, 3, both triples; rows sum to one")''',
'''    d9 = True
    for triple in TRIPLES:
        rows3, p03, P3 = report[("P", triple, 3)]
        rows2, p02, P2 = report[("P", triple, 2)]
        cols = (0, 2) if mut("restriction_lemma_broken") else (0, 1)
        restricted: dict = {}
        for i, b in enumerate(rows3):
            for k, a in enumerate(rows3):
                key = (tuple(b[c] for c in cols), tuple(a[c] for c in cols))
                restricted[key] = restricted.get(key, Fraction(0)) + p03[i] * P3[i][k]
        idx2 = {r: i for i, r in enumerate(rows2)}
        d9 = d9 and all(restricted[(b, a)] == p02[idx2[b]] * P2[idx2[b]][idx2[a]] for b in rows2 for a in rows2)
    checks.check("D9", d9, "restriction lemma: the width-3 two-row formation joint restricted to columns 0,1 equals the width-2 two-row joint, both triples")
    checks.check("D1", d1, "E2 row kernel from the formula equals the kernel from the definition entrywise, W = 2, 3, both triples; rows sum to one")''')
# (iv) boundary independence of the deep-row limit: general boundary vectors in center_row_value
rep('''def center_row_value(rows, T, Avec, n: int) -> Fraction:
    """Center-row pair-parallel probability of the n-row static strip: w = (A T^c)(rho) (T^(n-1-c) 1)(rho)."""
    R = len(rows)
    c = n // 2
    left = list(Avec)
    for _ in range(c):
        left = [sum(left[i] * T[i][k] for i in range(R)) for k in range(R)]
    right = [1] * R''',
'''def center_row_value(rows, T, Avec, n: int, left0=None, right0=None) -> Fraction:
    """Center-row pair-parallel probability of the n-row static strip: w = (b_L T^c)(rho) (T^(n-1-c) b_R)(rho); default b_L = A, b_R = 1 (open ends)."""
    R = len(rows)
    c = n // 2
    left = list(Avec) if left0 is None else list(left0)
    for _ in range(c):
        left = [sum(left[i] * T[i][k] for i in range(R)) for k in range(R)]
    right = [1] * R if right0 is None else list(right0)''')
rep('''    out["finite_n"] = seq
    out["finite_n_ok"] = all(dist[i + 1] < dist[i] for i in range(len(dist) - 1)) and dist[-1] < Fraction(1, 10 ** 6)''',
'''    out["finite_n"] = seq
    out["finite_n_ok"] = all(dist[i + 1] < dist[i] for i in range(len(dist) - 1)) and dist[-1] < Fraction(1, 10 ** 6)
    # boundary independence of the deep-row limit: exterior records P(e_y) on the first and last rows (a positive boundary vector h)
    hvec = [prod(phi[r[j]][2] for j in range(W)) for r in rows]
    bval = center_row_value(rows, T, Avec, 13, left0=[Avec[k] * hvec[k] for k in range(R)], right0=hvec)
    if mut("boundary_dependence_forged"):
        bval = bval + Fraction(1, 100)
    out["boundary_ok"] = max(glo - bval, bval - ghi, Fraction(0)) < Fraction(1, 10 ** 6)
    out["boundary_value"] = bval''')
rep('''    checks.check("E10", all(r["second_ok"] for r in res.values()), "second eigenvalue: all charpoly roots real; every non-Perron root in [-m, m] with rational m < lam_1 (Sturm)")''',
'''    checks.check("E10", all(r["second_ok"] for r in res.values()), "second eigenvalue: all charpoly roots real; every non-Perron root in [-m, m] with rational m < lam_1 (Sturm)")
    checks.check("E11", all(r["boundary_ok"] for r in res.values()), "boundary independence: with exterior records P(e_y) on both end rows the n = 13 center-row value lies within 10^-6 of the enclosure, W = 2, 3, both triples")''')
assert t != orig
p.write_text(t, encoding="utf-8"); print("patched")
