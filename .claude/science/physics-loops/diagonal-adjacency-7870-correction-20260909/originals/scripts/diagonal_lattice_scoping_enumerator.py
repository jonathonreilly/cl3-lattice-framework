#!/usr/bin/env python3
"""Enumeration / orbit checks for the diagonal-lattice scoping note.

This runner exhibits the diagonal enumeration of one unit cube and of the
per-site Moore neighborhood on Z^3, and verifies the cubic-symmetry (O_h)
orbit/stabilizer arithmetic. It is a combinatorial/group-theoretic enumerator
only. It makes no physics claim, changes no axiom, and asserts no closure.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs" / "DIAGONAL_LATTICE_SCOPING_NOTE_2026-06-04.md"

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


# --- cube vertices {0,1}^3 -------------------------------------------------
VERTS = list(product((0, 1), repeat=3))


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


# --- cubic symmetry group O_h as S_3 (x) (Z_2)^3, order 48 -----------------
# element (perm, flip): acts on a bit-string b by permuting coords then XOR flip.
def oh_elements():
    elems = []
    for perm in permutations(range(3)):
        for flip in product((0, 1), repeat=3):
            elems.append((perm, flip))
    return elems


def act_vertex(elem, b):
    perm, flip = elem
    permuted = tuple(b[perm[i]] for i in range(3))
    return tuple(permuted[i] ^ flip[i] for i in range(3))


def act_pair(elem, pair):
    a, b = pair
    return frozenset((act_vertex(elem, a), act_vertex(elem, b)))


def orbit_and_stab(elems, obj, action):
    orbit = set()
    stab = 0
    for e in elems:
        img = action(e, obj)
        orbit.add(img)
        if img == (obj if not isinstance(obj, frozenset) else obj):
            stab += 1
    return orbit, stab


# --- per-site Moore displacement families ----------------------------------
DISPLACEMENTS = [d for d in product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]


def sqlen(d):
    return sum(c * c for c in d)


# signed-permutation realization of O_h acting on Z^3 displacement vectors
def signed_perm_elements():
    elems = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            elems.append((perm, signs))
    return elems


def act_vec(elem, v):
    perm, signs = elem
    return tuple(signs[i] * v[perm[i]] for i in range(3))


def main() -> int:
    print("=" * 72)
    print("Diagonal-lattice scoping enumerator")
    print("=" * 72)

    # ---- per-unit-cube segment enumeration --------------------------------
    record("cube {0,1}^3 has 8 vertices", len(VERTS) == 8)
    pairs = list(combinations(VERTS, 2))
    record("cube has C(8,2)=28 undirected vertex pairs", len(pairs) == 28)

    by_h = {1: [], 2: [], 3: []}
    for a, b in pairs:
        by_h[hamming(a, b)].append((a, b))
    record("cube edges (Hamming 1) count = 12", len(by_h[1]) == 12, str(len(by_h[1])))
    record("face-diagonals (Hamming 2) count = 12", len(by_h[2]) == 12, str(len(by_h[2])))
    record("body-diagonals (Hamming 3) count = 4", len(by_h[3]) == 4, str(len(by_h[3])))
    record(
        "edge+face-diag+body-diag = 28 partition",
        len(by_h[1]) + len(by_h[2]) + len(by_h[3]) == 28,
    )

    # ---- per-site Moore displacement families -----------------------------
    record("Moore neighborhood (3^3 - 1) = 26 displacements", len(DISPLACEMENTS) == 26)
    fam = {1: [], 2: [], 3: []}
    for d in DISPLACEMENTS:
        fam[sqlen(d)].append(d)
    record("<100> NN family size = 6 (sq-length 1)", len(fam[1]) == 6, str(len(fam[1])))
    record("<110> face-diagonal family size = 12 (sq-length 2)", len(fam[2]) == 12, str(len(fam[2])))
    record("<111> body-diagonal family size = 8 (sq-length 3)", len(fam[3]) == 8, str(len(fam[3])))
    record("6+12+8 = 26 displacement partition", len(fam[1]) + len(fam[2]) + len(fam[3]) == 26)
    record(
        "coordination numbers 6 -> 18 -> 26",
        (len(fam[1]), len(fam[1]) + len(fam[2]), len(fam[1]) + len(fam[2]) + len(fam[3]))
        == (6, 18, 26),
    )

    # ---- O_h group on the cube --------------------------------------------
    cube_g = oh_elements()
    record("cubic symmetry group |O_h| = 48 (S_3 x Z_2^3)", len(cube_g) == 48)
    # closure spot-check: composition stays in the realized set as a permutation of vertices
    perms_on_verts = set()
    for e in cube_g:
        perms_on_verts.add(tuple(act_vertex(e, v) for v in VERTS))
    record("O_h acts as 48 distinct vertex permutations (faithful)", len(perms_on_verts) == 48)

    # segment orbits under cube symmetry
    for name, h, exp_size, exp_stab in [
        ("edge", 1, 12, 4),
        ("face-diagonal", 2, 12, 4),
        ("body-diagonal", 3, 4, 12),
    ]:
        rep = frozenset(by_h[h][0])
        orbit = {act_pair(e, by_h[h][0]) for e in cube_g}
        stab = sum(1 for e in cube_g if act_pair(e, by_h[h][0]) == rep)
        ok = (len(orbit) == exp_size) and (stab == exp_stab) and (len(orbit) * stab == 48)
        record(
            f"cube {name}s: single O_h orbit size {exp_size}, stabilizer {exp_stab}",
            ok,
            f"orbit={len(orbit)} stab={stab}",
        )

    # ---- O_h orbits on displacement families ------------------------------
    sp_g = signed_perm_elements()
    record("signed-permutation O_h realization order 48", len(sp_g) == 48)
    for name, sl, exp_size, exp_stab in [
        ("<100>", 1, 6, 8),
        ("<110>", 2, 12, 4),
        ("<111>", 3, 8, 6),
    ]:
        rep = fam[sl][0]
        orbit = {act_vec(e, rep) for e in sp_g}
        stab = sum(1 for e in sp_g if act_vec(e, rep) == rep)
        ok = (len(orbit) == exp_size) and (stab == exp_stab) and (len(orbit) * stab == 48)
        record(
            f"displacement {name}: single O_h orbit size {exp_size}, stabilizer {exp_stab}",
            ok,
            f"orbit={len(orbit)} stab={stab}",
        )

    # ---- explicit named lists match computed sets -------------------------
    face_named = {
        frozenset([(0, 0, 0), (1, 1, 0)]), frozenset([(1, 0, 0), (0, 1, 0)]),
        frozenset([(0, 0, 1), (1, 1, 1)]), frozenset([(1, 0, 1), (0, 1, 1)]),
        frozenset([(0, 0, 0), (1, 0, 1)]), frozenset([(1, 0, 0), (0, 0, 1)]),
        frozenset([(0, 1, 0), (1, 1, 1)]), frozenset([(1, 1, 0), (0, 1, 1)]),
        frozenset([(0, 0, 0), (0, 1, 1)]), frozenset([(0, 1, 0), (0, 0, 1)]),
        frozenset([(1, 0, 0), (1, 1, 1)]), frozenset([(1, 1, 0), (1, 0, 1)]),
    }
    face_computed = {frozenset(p) for p in by_h[2]}
    record("explicit 12 face-diagonals match Hamming-2 set", face_named == face_computed)

    body_named = {
        frozenset([(0, 0, 0), (1, 1, 1)]), frozenset([(1, 0, 0), (0, 1, 1)]),
        frozenset([(0, 1, 0), (1, 0, 1)]), frozenset([(0, 0, 1), (1, 1, 0)]),
    }
    body_computed = {frozenset(p) for p in by_h[3]}
    record("explicit 4 body-diagonals match Hamming-3 set", body_named == body_computed)
    record("face-diagonal and body-diagonal sets are disjoint", face_computed.isdisjoint(body_computed))

    # ---- hw=1 generation triplet ------------------------------------------
    hw1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    pairwise = [hamming(a, b) for a, b in combinations(hw1, 2)]
    record("hw=1 generation triplet pairwise Hamming distance 2 (face-diagonal)", pairwise == [2, 2, 2])
    # S_3 acts transitively on the triplet; C_3 cyclic shift is transitive
    s3_orbit = set()
    for perm in permutations(range(3)):
        s3_orbit.add(tuple(sorted(tuple(v[perm[i]] for i in range(3)) for v in hw1)))
    record("hw=1 triplet is a single S_3 orbit (closed under coordinate perms)", len(s3_orbit) == 1)
    c3 = [(1, 2, 0), (2, 0, 1), (0, 1, 2)]  # cyclic shifts
    cyc_images = {tuple(tuple(v[c[i]] for i in range(3)) for v in hw1) for c in c3}
    # each cyclic shift maps the triplet onto itself (a permutation of it)
    record(
        "C_3 cyclic shift permutes the hw=1 triplet onto itself",
        all(set(img) == set(hw1) for img in cyc_images),
    )

    # ---- source-note firewalls --------------------------------------------
    text = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "This note does not change axioms",
        "thought-experiment surface, not a derived theorem",
        "independent audit lane only",
    ]:
        record(f"source-note firewall present: {phrase!r}", phrase in text)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
