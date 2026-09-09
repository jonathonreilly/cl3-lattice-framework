"""Four exact historical fixture definitions, used only as AST data.

The assigned bits/depths are finite test data, not a physical formation rule.
No other Cycle-885 function or campaign result is imported by this fixture.
"""
from fractions import Fraction
from itertools import product
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/multiplicity-correction-20260908/historical-inputs/scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py.txt',)
AUDIT_TIMEOUT_SEC = 30

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
    """A record configuration: support, per-record content bit, formation depth.

    Content is the Qubit axiom's two-state label.  Formation depth is assigned
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



if __name__ == "__main__":
    import ast
    import hashlib
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    original = root / AUDIT_INPUT_PATHS[0]
    if not original.is_file() or hashlib.sha256(original.read_bytes()).hexdigest() != 'daee8bbfefde80a351bf82a3028d96baf447493d3add8cdc85f4eb63fc114f32':
        raise SystemExit("historical fixture source is missing or changed")
    names = {"NEIGHBOURS", "_lcg", "make_config", "build_family"}
    def selected(text):
        result = {}
        for node in ast.parse(text).body:
            name = node.name if isinstance(node, ast.FunctionDef) else node.targets[0].id if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) else None
            if name in names:
                result[name] = ast.dump(node, include_attributes=False)
        return result
    expected = selected(original.read_text())
    actual = selected(Path(__file__).read_text())
    if set(actual) != names or actual != expected:
        raise SystemExit("fixture AST differs from the four exact historical definitions")
    print("four exact configuration fixture definitions: verified")
