"""Exact supplied A/B programs and carrier words, without parent campaigns.

These are the actual Block3 Bloch triples used through Block7, and the final
Block8 word correction. They specify finite fixtures, not a selected law.
The independent checker separately reconstructs their explicit matrix entries.
"""
import sympy as sp

I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Z = sp.diag(1, -1)
R = sp.Rational
BLOCH = {
    'A': ((R(1,2), 0, 1), (R(9,10), 4*sp.sqrt(2)/9, -R(7,9)),
          (R(3,5), -2*sp.sqrt(2)/3, R(1,3))),
    'B': ((R(1,2), 0, 1), (R(3,4), 2*sp.sqrt(2)/3, -R(1,3)),
          (R(3,4), -2*sp.sqrt(2)/3, -R(1,3))),
}
EFFECTS = {name: tuple(sp.simplify(w*(I2+x*X+z*Z)/2) for w,x,z in rows)
           for name,rows in BLOCH.items()}
PROGRAMS = {name: tuple(sp.simplify(e/sp.sqrt(sp.trace(e))) for e in menu)
            for name,menu in EFFECTS.items()}
BLANK = '000'
PENDING = '100'
TERMINALS = ('010', '110', '111')
