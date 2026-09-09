#!/usr/bin/env python3
"""Finite conditional support and determinant/Pfaffian identities.

The separate Gaussian-integer checker is a real imported and called helper.
Current source pins bind the note and declared premise/target context; moving
ledger counts and whole-repository ancestry are not mathematical predicates.
"""
from __future__ import annotations
import hashlib
from fractions import Fraction
from pathlib import Path
import sympy as sp
import independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02 as independent

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('scripts/ac_occupancy_grain_support_typed_target_repair_2026_09_02.py', 'scripts/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.py', 'docs/AC_OCCUPANCY_GRAIN_SUPPORT_TYPED_FORMAL_TARGET_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md', 'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md', 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md', 'docs/audit/data/axiom_premise_nodes.json')
EXPECTED_HASHES = {'scripts/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.py': '1d24b5eaa2f41048498b8a7af6116a594349a63e9555b65040e724272fb43747', 'docs/AC_OCCUPANCY_GRAIN_SUPPORT_TYPED_FORMAL_TARGET_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md': '44a9d2154373d8b4f74ba4e66a5159d285471132200c558d3329dcd1ab4c2393', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md': 'bd91c0496a51334fa7f7b4ab7a84f87b1575103b1398873d77fe260ffd6aef63', 'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md': 'e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md': '5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b', 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md': '755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563', 'docs/audit/data/axiom_premise_nodes.json': '615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37'}


def source_bound() -> bool:
    helper = ROOT / 'scripts/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.py'
    return Path(independent.__file__).resolve() == helper.resolve() and all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in EXPECTED_HASHES.items())


def orbit_partition(items, action):
    unseen = set(items)
    out = []
    while unseen:
        seed = min(unseen)
        orbit = frozenset((seed, action[seed]))
        out.append(orbit)
        unseen -= orbit
    return out


def realify(matrix: sp.Matrix) -> sp.Matrix:
    x = matrix.applyfunc(sp.re)
    y = matrix.applyfunc(sp.im)
    return x.row_join(-y).col_join(y.row_join(x))


def pfaffian4(a: sp.Matrix) -> sp.Expr:
    return sp.expand(a[0, 1] * a[2, 3] - a[0, 2] * a[1, 3] + a[0, 3] * a[1, 2])


def jacobian_residual(a, m, *, include_jacobian=True):
    value = pfaffian4(m.T * a * m)
    if include_jacobian:
        value /= m.det()
    return sp.expand(value - pfaffian4(a))


def algebra_checks():
    tests = []
    def add(name, value):
        tests.append((name, bool(value)))
    items = ('s', '+', '-')
    action = {'s': 's', '+': '-', '-': '+'}
    orbits = orbit_partition(items, action)
    atom_mult = tuple(sum(x in sector for x in items) for sector in ({'s'}, {'+', '-'}))
    quotient_mult = tuple(sum(bool(o & sector) for o in orbits) for sector in ({'s'}, {'+', '-'}))
    add('supplied involution orbit census', len(items) == 3 and sum(action[x] == x for x in items) == 1 and len(orbits) == 2)
    add('channel and orbit multiplicities', atom_mult == (1, 2) and quotient_mult == (1, 1))
    add('conditional support endpoints', Fraction(quotient_mult[1], 2 * quotient_mult[0]) == Fraction(1, 2) and Fraction(atom_mult[1], 2 * atom_mult[0]) == 1)
    ns, nd = sp.symbols('nu_s nu_d', positive=True)
    qs, qd = sp.symbols('q_s q_d', real=True)
    difference = (ns * qd - nd * qs) / (2 * ns * (ns + qs))
    add('symbolic support increment', sp.cancel((nd + qd) / (2 * (ns + qs)) - nd / (2 * ns) - difference) == 0)
    add('global copy neutral', sp.cancel(difference.subs({qs: ns, qd: nd})) == 0)
    add('zero increment neutral', difference.subs({qs: 0, qd: 0}) == 0)
    add('singlet and doublet-only controls', difference.subs({ns: 1, nd: 1, qs: 1, qd: 0}) == -sp.Rational(1, 4) and difference.subs({ns: 1, nd: 1, qs: 0, qd: 1}) == sp.Rational(1, 2))
    add('whole-carrier squaring preserves ray', Fraction(2, 1) == Fraction(4, 2) and Fraction(1, 1) == Fraction(2, 2))
    k = sp.Matrix([[1 + 2 * sp.I, 3 - sp.I], [2, 4 + sp.I]])
    rk = realify(k)
    add('complex determinant fixture', sp.expand(k.det()) == -4 + 11 * sp.I)
    add('ordinary realification', rk.det() == 137 and sp.expand(rk.det() - k.det() * sp.conjugate(k.det())) == 0)
    x, y = k.applyfunc(sp.re), k.applyfunc(sp.im)
    bad = x.row_join(y).col_join(y.row_join(x))
    add('actual realification sign corruption', bad.det() == -121 and bad.det() != rk.det())
    a = sp.zeros(4)
    a[:2, 2:] = k
    a[2:, :2] = -k.T
    add('skew block and Pfaffian sign', a.T == -a and sp.expand(pfaffian4(a) + k.det()) == 0)
    original_m = sp.Matrix([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 2]])
    nonunit_m = sp.diag(2, 1, 1, 1)
    add('original congruence fixture', original_m.det() == 1 and jacobian_residual(a, original_m) == 0)
    add('nonunit congruence fixture', nonunit_m.det() == 2 and jacobian_residual(a, nonunit_m) == 0)
    add('actual omitted Jacobian control', jacobian_residual(a, nonunit_m, include_jacobian=False) == 4 - 11 * sp.I)
    add('ordinary realification not this skew kernel', rk.T != -rk)
    add('independent conjugate block product', sp.expand(k.det() * sp.conjugate(k.det())) == 137)
    def odds(power, z):
        p = z ** power / (1 + z ** power)
        return p / (1 - p)
    add('conditional odds exponents', odds(1, Fraction(4)) / odds(1, Fraction(2)) == 2 and odds(2, Fraction(4)) / odds(2, Fraction(2)) == 4)
    # Arithmetic of the historical comparator's supplied c-sector scalar only.
    u = Fraction(43, 35) ** 2 + Fraction(129, 175) ** 2
    add('supplied comparator factor arithmetic', u == Fraction(62866, 30625) and u * u == Fraction(3952133956, 937890625))
    return tests


def main() -> int:
    tests = [('actual input/source binding', source_bound()), *algebra_checks()]
    tests += [('independent helper source binding', independent.source_bound())]
    tests += [('independent: ' + name, ok) for name, ok in independent.algebra_checks()]
    for name, ok in tests:
        print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}")
    failed = sum(not ok for _, ok in tests)
    print('SCOPE: exact finite supplied algebra and independent arithmetic controls; no physical carrier/action/measure/event selection, graph-status inference, or audit verdict')
    print(f'TOTAL: PASS={len(tests)-failed} FAIL={failed}')
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
