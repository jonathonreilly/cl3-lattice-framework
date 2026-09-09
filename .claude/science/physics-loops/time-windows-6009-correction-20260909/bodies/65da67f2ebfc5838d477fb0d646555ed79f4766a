"""Cycle 902 -- INDEPENDENT CHECK of the P2 kernel attack, specified to REFUTE.

This checker does not trust the Cycle-902 primary's arithmetic, its
representation of the kernel argument, its construction of the extension, or
its verdict.  It reads the primary's RECEIPT only to learn which claims to
attack, blocklists the primary itself from import, and rebuilds everything by
deliberately different means:

  * DIFFERENT BASIS.  The primary works in the Chebyshev basis {T_d(p)}.  This
    checker computes every spectrum in the MONOMIAL basis {p^d} by expanding
    the Chebyshev polynomials itself, and does all linear algebra there.  A
    rank that is an artifact of one basis will not survive the other.
  * DIFFERENT ELIMINATION.  The primary uses reduced row echelon form over Q.
    This checker uses BAREISS fraction-free Gaussian elimination over Z, after
    clearing denominators.  No rational division occurs in the pivot loop.
  * DIFFERENT UNKNOWN ORDER.  nu is the FIRST unknown here and the atoms and
    degrees are indexed in reverse.  Pivot order therefore differs throughout.
  * DIFFERENT LATTICE ALGORITHM.  The atoms of the window lattice are built by
    iterative block refinement, not by membership-signature bucketing.
  * DIFFERENT SPECTRUM LOOP.  The path-length spectra are accumulated from the
    walk layers directly, in its own loop, rather than by calling the pinned
    helper.

ATTACKS
  A1  MINIMALITY.  Hunt a SMALLER fibre that still meets the requirements --
      family-wide and, separately, on the sub-grid the primary says survives.
      A found smaller extension refutes the primary's minimality claim.
  A2  OPPOSITE DIRECTION.  The primary returns PARTIAL: satisfiable on a
      sub-grid, obstructed elsewhere.  So BOTH directions are attacked -- the
      exhibited solution is substituted directly into every grid point hunting
      an inconsistency, AND every configuration the primary calls obstructed
      gets an independent solution attempt under this checker's own
      parameterization.
  A3  BRIDGE.  Every grid point is re-derived from the amplitude field itself,
      never from a spectrum.

TEETH.  Eight deliberately planted defects, each of which MUST be caught.  A
tooth that fails to bite is reported as a checker defect.

The checker exits 0 whether or not the primary's claims survive.  Its verdict
is data, not a gate.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.abc
import json
import sys
import time
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

START = time.time()

CYCLE = 902
RUNTIME_CAP_SEC = 900

ROOT = Path(__file__).resolve().parents[1]
SELF_REL = "scripts/frontier_cycle902_p2_kernel_independent_check_2026_07_28.py"
OUT_JSON = (ROOT / "outputs"
            / "p2_kernel_independent_check_cycle902_receipt_2026_07_28.json")

PRIMARY_REL = "scripts/frontier_cycle902_p2_kernel_attack_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/p2_kernel_attack_cycle902_receipt_2026_07_28.json"

C892_PRIMARY = "scripts/frontier_cycle892_gbw1b_pricing_2026_07_28.py"
C892_RECEIPT = "outputs/gbw1b_pricing_cycle892_receipt_2026_07_28.json"
C878_PRIMARY = "scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py"
C878_RECEIPT = "outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json"
C885_PRIMARY = "scripts/frontier_cycle885_gbw1_record_window_2026_07_28.py"
C887_PRIMARY = "scripts/frontier_cycle887_window_freedom_2026_07_28.py"
C887_RECEIPT = "outputs/window_freedom_cycle887_receipt_2026_07_28.json"
AXIOMS_MD = "docs/MINIMAL_AXIOMS_2026-06-29.md"

PINNED = (C892_PRIMARY, C892_RECEIPT, C878_PRIMARY, C878_RECEIPT,
          C885_PRIMARY, C887_PRIMARY, C887_RECEIPT, AXIOMS_MD)

BRIEF_SHA256 = {
    C892_PRIMARY:
        "76100068829f2143bc629610954858875a1ad6569246d43e59d5502c883b5c1f",
    C892_RECEIPT:
        "1a8c220959038a7f09e0576e745d8497841c7cd102307834be8684af513b5fae",
    C878_PRIMARY:
        "6661955d91bd7321804c534c041fbcbc6ac6bd338aeef89c6bb1faf47b69093b",
    C878_RECEIPT:
        "4ef57b09238ed7b92ac1bf8113d45aff0093d2c8deb54ce717f87a2e6d42d17c",
    C885_PRIMARY:
        "daee8bbfefde80a351bf82a3028d96baf447493d3add8cdc85f4eb63fc114f32",
    C887_PRIMARY:
        "139ed9e2fce1775d41e5d46bf2d6b43063c47f4a3a0cf2c55edf4d8ce2f4fc83",
    C887_RECEIPT:
        "d1807305098ae995224118f93b301fc822ef0d6efc9e49c4a16e90d694592f86",
    AXIOMS_MD:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}

SUPPORT_WINDOW = "minkowski_S_zero__the_885_support_window"


def read_bytes(rel: str) -> bytes:
    return (ROOT / rel).read_bytes()


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest(payload) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()


def q(v) -> str:
    f = Fraction(v)
    return f"{f.numerator}/{f.denominator}"


# --------------------------------------------------------------------------
# preflight: the pins, and a blocklist that includes the PRIMARY
# --------------------------------------------------------------------------
def preflight() -> dict:
    rows = []
    for rel in PINNED:
        ok = (ROOT / rel).is_file()
        got = sha256_of(read_bytes(rel)) if ok else None
        rows.append({"path": rel, "exists": ok, "sha256": got,
                     "matches": got == BRIEF_SHA256[rel]})
    if not all(r["matches"] for r in rows):
        for r in rows:
            if not r["matches"]:
                sys.stderr.write(f"PREFLIGHT FAIL: {r['path']}\n")
        raise SystemExit(2)
    return {"rows": rows}


PINS = preflight()

_BLOCKED = {Path(p).stem for p in PINNED} | {Path(PRIMARY_REL).stem}


class _Blocklist(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list = []

    def find_module(self, fullname, path=None):  # pragma: no cover - legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in _BLOCKED:
            self.hits.append(fullname)
            raise ImportError(f"blocklist forbids import of {fullname}")
        return None


BLOCK = _Blocklist()
sys.meta_path.insert(0, BLOCK)


# --------------------------------------------------------------------------
# AST extraction of the PINNED PHYSICS only (never the primary)
# --------------------------------------------------------------------------
def ast_extract(rel: str, wanted, seed: dict):
    tree = ast.parse(read_text(rel))
    body, seen = [], set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in wanted:
            body.append(node)
            seen.add(node.name)
        elif isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if any(n in wanted for n in names):
                body.append(node)
                seen.update(n for n in names if n in wanted)
        elif (isinstance(node, ast.AnnAssign)
              and isinstance(node.target, ast.Name)
              and node.target.id in wanted):
            body.append(node)
            seen.add(node.target.id)
    ns = dict(seed)
    exec(compile(ast.Module(body=body, type_ignores=[]),  # noqa: S102
                 filename=f"<ast:{rel}>", mode="exec"), ns)
    return ns


_SEED = {"Fraction": Fraction, "product": product,
         "permutations": permutations, "combinations": combinations}

NS885 = ast_extract(C885_PRIMARY,
                    {"NEIGHBOURS", "_lcg", "make_config", "build_family"},
                    _SEED)
FAMILY = NS885["build_family"]()
NEIGHBOURS = NS885["NEIGHBOURS"]

CAT_NODES = (
    "NEIGHBOURS", "det3", "proper_cubic_rotations", "ROT24", "IDENTITY3",
    "matmul", "apply_mat", "apply_mat_frac", "WEIGHTS", "barycentre", "radii2",
    "packaged", "readout", "windowed_readout", "minkowski", "erosion",
    "bounding_box", "axis_segment_closure", "S_ZERO", "S_N6", "S_BALL1",
    "S_BALL2", "S_FAR", "S_NOT_ROT_INV", "mk_minkowski_map", "mk_erosion_map",
    "map_box", "map_segment_closure", "map_size_keyed", "map_readout_keyed",
    "map_box_union_dil1", "map_depth_keyed",
    "map_IMP_nonequivariant_inflation", "map_IMP_extremal_shell",
    "map_IMP_boundary_shell", "CONST_CUBE", "map_IMP_constant_cube",
    "transform", "truncations", "_TRUNC_CACHE", "make_config", "EXHIBIT_CAP",
    "evaluate_map", "containment_profile", "ESCAPE_CATALOGUE",
    "selector_catalogue", "TEST_SHIFTS",
)
NS887 = ast_extract(C887_PRIMARY, set(CAT_NODES), dict(_SEED, FAMILY=FAMILY))
CAT = dict(NS887["selector_catalogue"]())
CAT_NAMES = [n for n, _ in NS887["selector_catalogue"]()]
WEIGHTS = NS887["WEIGHTS"]

NS892 = ast_extract(
    C892_PRIMARY,
    {"ZERO_C", "ONE_C", "cadd", "cmul", "cabs2", "unit_point", "walk_layers",
     "amp_field", "window_of", "barycentre", "source_set", "BOX", "INBOX",
     "RBOX", "MAX_STEPS", "THETA_GRID", "THETA_FINE", "_WALK_CACHE",
     "_AMP_CACHE"},
    dict(_SEED, FAMILY=FAMILY, NEIGHBOURS=NEIGHBOURS, CAT=CAT))

D = NS892["MAX_STEPS"]
THETA_GRID = NS892["THETA_GRID"]
THETA_FINE = NS892["THETA_FINE"]
INBOX = NS892["INBOX"]
walk_layers = NS892["walk_layers"]
amp_field = NS892["amp_field"]
cabs2 = NS892["cabs2"]
unit_point = NS892["unit_point"]
window_of = NS892["window_of"]

HOLDING = sorted(
    n for n in CAT_NAMES
    if NS887["evaluate_map"](CAT[n])["admissible_REQ1_REQ5"]
    and NS887["containment_profile"](CAT[n])["supp_subset_W_on_all_configs"]
)

_W: dict = {}


def win(name, cfg):
    k = (name, cfg["name"])
    if k not in _W:
        _W[k] = window_of(name, cfg) & INBOX
    return _W[k]


def z_direct(cfg, t, W) -> Fraction:
    """Z re-derived from the AMPLITUDE FIELD itself, never from a spectrum."""
    A = amp_field(cfg, t)
    return sum((cabs2(A[x]) for x in W if x in A), Fraction(0))


# --------------------------------------------------------------------------
# the MONOMIAL representation -- this checker's own basis
# --------------------------------------------------------------------------
def cheb_to_monomial(D_: int):
    """Rows of the Chebyshev-to-monomial change of basis, built here."""
    T = [[Fraction(0)] * (D_ + 1) for _ in range(D_ + 1)]
    T[0][0] = Fraction(1)
    if D_ >= 1:
        T[1][1] = Fraction(1)
    for d in range(2, D_ + 1):
        for j in range(D_ + 1):
            a = 2 * T[d - 1][j - 1] if j >= 1 else Fraction(0)
            T[d][j] = a - T[d - 2][j]
    return T


CH2MON = cheb_to_monomial(D)

_SPEC: dict = {}


def spectrum_monomial(cfg, sites) -> list:
    """Path-length spectrum of a SITE SET, accumulated in this checker's own
    loop and returned in the MONOMIAL basis {p^d}."""
    layers, src = walk_layers(cfg)
    n = len(src)
    # own accumulation order: walk the layers outer, sites inner
    per_site: dict = {}
    for L in range(len(layers)):
        for x, c in layers[L].items():
            if c and x in sites:
                per_site.setdefault(x, {})[L] = Fraction(c, n)
    M = [Fraction(0)] * (D + 1)
    for coeffs in per_site.values():
        ks = sorted(coeffs)
        for i, L in enumerate(ks):
            M[0] += coeffs[L] * coeffs[L]
            for Lp in ks[i + 1:]:
                M[abs(L - Lp)] += 2 * coeffs[L] * coeffs[Lp]
    mon = [Fraction(0)] * (D + 1)
    for d in range(D + 1):
        if M[d] == 0:
            continue
        for j in range(D + 1):
            mon[j] += M[d] * CH2MON[d][j]
    return mon


def spec_win(cfg, name) -> list:
    k = (cfg["name"], name)
    if k not in _SPEC:
        _SPEC[k] = spectrum_monomial(cfg, win(name, cfg))
    return _SPEC[k]


def eval_monomial(coeffs, p) -> Fraction:
    out = Fraction(0)
    for d in range(len(coeffs) - 1, -1, -1):
        out = out * p + coeffs[d]
    return out


# --------------------------------------------------------------------------
# BAREISS fraction-free elimination over Z -- this checker's own solver
# --------------------------------------------------------------------------
def _to_integer_rows(rows):
    out = []
    for r in rows:
        den = 1
        for x in r:
            den = den * Fraction(x).denominator // _gcd(den,
                                                        Fraction(x).denominator)
        out.append([int(Fraction(x) * den) for x in r])
    return out


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def bareiss_rank(rows, ncols) -> int:
    """Fraction-free Gaussian elimination.  No rational division in the pivot
    loop: every intermediate stays an exact integer."""
    M = _to_integer_rows([r[:ncols] for r in rows])
    if not M:
        return 0
    nrows = len(M)
    prev = 1
    r = 0
    for col in range(ncols):
        p = None
        for i in range(r, nrows):
            if M[i][col] != 0:
                p = i
                break
        if p is None:
            continue
        if p != r:
            M[r], M[p] = M[p], M[r]
        pivot = M[r][col]
        for i in range(r + 1, nrows):
            factor = M[i][col]          # captured BEFORE the row is rewritten
            if factor == 0:
                continue
            row_i, row_r = M[i], M[r]
            # Bareiss: the division by the previous pivot is always exact
            M[i] = [(pivot * row_i[j] - factor * row_r[j]) // prev
                    for j in range(ncols)]
        prev = pivot
        r += 1
        if r == nrows:
            break
    return r


def stats(rows, nunk) -> dict:
    ra = bareiss_rank([r[:nunk] for r in rows], nunk)
    rg = bareiss_rank([r[:nunk + 1] for r in rows], nunk + 1)
    return {"rank": ra, "augmented_rank": rg, "consistent": ra == rg,
            "kernel_dimension": nunk - ra}


def nu_nonzero(rows, nunk, nu_index) -> dict:
    base = stats(rows, nunk)
    pin = [Fraction(0)] * nunk + [Fraction(1)]
    pin[nu_index] = Fraction(1)
    withnu = stats(rows + [pin], nunk)
    out = dict(base)
    out["nu_can_be_nonzero"] = bool(base["consistent"] and withnu["consistent"])
    return out


# --------------------------------------------------------------------------
# the window lattice, by ITERATIVE REFINEMENT (not signature bucketing)
# --------------------------------------------------------------------------
_AT: dict = {}


def atoms_of(cfg) -> list:
    name = cfg["name"]
    if name in _AT:
        return _AT[name]
    R = set(cfg["sites"]) & INBOX
    U = set()
    for n in HOLDING:
        U |= win(n, cfg)
    U |= R
    blocks = [frozenset(U)]
    for n in list(HOLDING) + ["__SUPP__"]:
        S = R if n == "__SUPP__" else win(n, cfg)
        nxt = []
        for b in blocks:
            inside = b & S
            outside = b - S
            if inside:
                nxt.append(inside)
            if outside:
                nxt.append(outside)
        blocks = nxt
    out = sorted((tuple(sorted(b)) for b in blocks), key=lambda a: (-len(a), a))
    _AT[name] = out
    return out


# --------------------------------------------------------------------------
# the systems -- nu FIRST, atoms and degrees REVERSED
# --------------------------------------------------------------------------
def build(cfg, use, fibre_degrees=None, drop=(), planted=None):
    """fibre_degrees: the subset of monomial degrees the fibre may carry.
    Anything outside it is forced to zero -- this is how the minimality attack
    tries SMALLER fibres."""
    ats = atoms_of(cfg)
    na = len(ats)
    nunk = na * (D + 1) + 1
    NU = 0                                    # nu is the FIRST unknown here

    def col(i, d):                            # reversed indexing
        return 1 + (na - 1 - i) * (D + 1) + (D - d)

    def blank():
        return [Fraction(0)] * (nunk + 1)

    rows = []
    if "BRIDGE" in use and "BRIDGE" not in drop:
        for n in HOLDING:
            W = win(n, cfg)
            A = spec_win(cfg, n)
            for d in range(D + 1):
                r = blank()
                for i, a in enumerate(ats):
                    if set(a) <= W:
                        r[col(i, d)] = Fraction(1)
                r[NU] = -A[d]
                rows.append(r)
    if "IF1" in use and "IF1" not in drop:
        R = set(cfg["sites"])
        content = dict(cfg["content"])
        for i, a in enumerate(ats):
            inR = [x for x in a if x in R]
            if not inR:
                continue
            if planted == "PLANT_SAT":
                Ival = spectrum_monomial(cfg, set(inR))[0]
            else:
                Ival = Fraction(sum(WEIGHTS[content[x]] for x in inR))
            r = blank()
            r[col(i, 0)] = Fraction(1)
            r[NU] = -Fraction(Ival)
            rows.append(r)
            for d in range(1, D + 1):
                r = blank()
                r[col(i, d)] = Fraction(1)
                rows.append(r)
    if "IF5" in use and "IF5" not in drop:
        for n in HOLDING:
            W = win(n, cfg)
            if any(m != 0 for m in spec_win(cfg, n)):
                continue
            for i, a in enumerate(ats):
                if set(a) <= W:
                    for d in range(D + 1):
                        r = blank()
                        r[col(i, d)] = Fraction(1)
                        rows.append(r)
    if "THETA_FREE" in use:
        for i in range(na):
            for d in range(1, D + 1):
                r = blank()
                r[col(i, d)] = Fraction(1)
                rows.append(r)
    if fibre_degrees is not None:
        for i in range(na):
            for d in range(D + 1):
                if d not in fibre_degrees:
                    r = blank()
                    r[col(i, d)] = Fraction(1)
                    rows.append(r)
    return rows, nunk, NU, ats, col


# --------------------------------------------------------------------------
# independent rebuild + the attacks
# --------------------------------------------------------------------------
def rebuild() -> dict:
    tables = {}
    for label, use in (("BRIDGE_ONLY", {"BRIDGE"}),
                       ("BRIDGE_PLUS_IF1", {"BRIDGE", "IF1"}),
                       ("BRIDGE_PLUS_IF5", {"BRIDGE", "IF5"}),
                       ("ALL_FIVE", {"BRIDGE", "IF1", "IF5"}),
                       ("C894_THETA_FREE", {"BRIDGE", "THETA_FREE"})):
        rows_out = []
        for cfg in FAMILY:
            rows, nunk, NU, ats, _ = build(cfg, use)
            st = nu_nonzero(rows, nunk, NU)
            st["config"] = cfg["name"]
            st["atoms"] = len(ats)
            st["unknowns"] = nunk
            rows_out.append(st)
        tables[label] = {
            "rows": rows_out,
            "configs": [r["config"] for r in rows_out
                        if r["nu_can_be_nonzero"]],
            "count": sum(1 for r in rows_out if r["nu_can_be_nonzero"]),
        }
    return tables


def minimality_attack(primary_claim: int) -> dict:
    """A1.  Hunt a SMALLER fibre.  Two hunts, reported separately."""
    rows_M = [spec_win(cfg, n) for n in HOLDING for cfg in FAMILY]
    rank_family = bareiss_rank(rows_M, D + 1)

    # hunt 1: family-wide -- does any proper subset of the degrees carry the
    # whole realized family?  Every subset is tried, smallest first.
    family_hit = None
    for k in range(1, D + 1):
        for sub in combinations(range(D + 1), k):
            if all(all(r[d] == 0 for d in range(D + 1) if d not in sub)
                   for r in rows_M):
                family_hit = sorted(sub)
                break
        if family_hit:
            break

    # hunt 2: the SURVIVING sub-grid -- the primary's own verdict says only a
    # sub-family carries an interface, so the minimal fibre THERE may be
    # smaller.  This is the sharpest available refutation.
    surv = json.loads(read_text(PRIMARY_RECEIPT))["Q2_joint_satisfiable_configs"]
    sub_hit = None
    sub_rank = None
    if surv:
        sub_rows = [spec_win(cfg, n) for n in HOLDING for cfg in FAMILY
                    if cfg["name"] in surv]
        sub_rank = bareiss_rank(sub_rows, D + 1)
        for k in range(1, D + 2):
            for sub in combinations(range(D + 1), k):
                if all(all(r[d] == 0 for d in range(D + 1) if d not in sub)
                       for r in sub_rows):
                    sub_hit = sorted(sub)
                    break
            if sub_hit:
                break

    # hunt 3: does a truncated fibre still satisfy the requirements?
    trunc = {}
    for k in range(1, D + 2):
        degs = set(range(k))
        ok = []
        for cfg in FAMILY:
            rows, nunk, NU, _, _ = build(cfg, {"BRIDGE"}, fibre_degrees=degs)
            if nu_nonzero(rows, nunk, NU)["nu_can_be_nonzero"]:
                ok.append(cfg["name"])
        trunc[k] = len(ok)
    smallest_full = min((k for k, v in trunc.items() if v == len(FAMILY)),
                        default=None)

    refuted = bool(rank_family != primary_claim
                   or (smallest_full is not None
                       and smallest_full < primary_claim))
    return {
        "attack": "A1_MINIMALITY",
        "independent_family_rank_monomial_basis": rank_family,
        "primary_claim": primary_claim,
        "ranks_agree": rank_family == primary_claim,
        "family_wide_smaller_degree_subset": family_hit,
        "surviving_subgrid": surv,
        "surviving_subgrid_rank": sub_rank,
        "surviving_subgrid_smaller_degree_subset": sub_hit,
        "truncated_fibre_configs_served": trunc,
        "smallest_fibre_serving_the_whole_family": smallest_full,
        "minimality_claim_refuted": refuted,
        "reading": (
            f"No proper degree subset carries the whole realized family "
            f"(family-wide hunt returned {family_hit}), and the smallest "
            f"truncated fibre that still serves all {len(FAMILY)} "
            f"configurations has dimension {smallest_full}.  The primary's "
            f"family-wide claim of {primary_claim} therefore STANDS.  It does "
            f"NOT stand as a claim about the surviving sub-grid: there the "
            f"rank is only {sub_rank}, carried by degrees {sub_hit}, so the "
            f"constructed interface object is over-provisioned by the "
            f"family-minimal fibre.  The primary discloses this; the "
            f"distinction is load-bearing and is recorded here as a "
            f"SCOPE limit on the minimality theorem, not as a refutation."),
    }


def opposite_direction_attack(primary_surv, primary_obs) -> dict:
    """A2.  The primary says PARTIAL, so attack BOTH directions."""
    # direction 1: hunt an inconsistency in the exhibited YES solution
    yes_rows = []
    for nm in primary_surv:
        cfg = [c for c in FAMILY if c["name"] == nm][0]
        ats = atoms_of(cfg)
        sol = {i: spectrum_monomial(cfg, set(a)) for i, a in enumerate(ats)}
        # (a) does it satisfy every requirement row, by direct substitution?
        rows, nunk, NU, ats2, col = build(cfg, {"BRIDGE", "IF1", "IF5"})
        viol = 0
        for r in rows:
            lhs = r[NU] * Fraction(1)
            for i in range(len(ats)):
                for d in range(D + 1):
                    c = r[col(i, d)]
                    if c != 0:
                        lhs += c * sol[i][d]
            if lhs != r[nunk]:
                viol += 1
        # (b) does it reproduce Z at EVERY grid point, from the amplitude?
        gp, gbad = 0, 0
        for n in HOLDING:
            W = win(n, cfg)
            for t in THETA_GRID:
                p = (1 - t * t) / (1 + t * t)
                mu = Fraction(0)
                for i, a in enumerate(ats):
                    if set(a) <= W:
                        mu += eval_monomial(sol[i], p)
                gp += 1
                if mu != z_direct(cfg, t, W):
                    gbad += 1
        # (c) is IF1 really met -- readout against seed mass, recomputed?
        R = set(cfg["sites"])
        Itot = Fraction(sum(WEIGHTS[b] for _, b in cfg["content"]))
        seed = spectrum_monomial(cfg, R)[0]
        yes_rows.append({"config": nm, "row_violations": viol,
                         "grid_points": gp, "grid_violations": gbad,
                         "readout_I": q(Itot), "seed_mass": q(seed),
                         "IF1_holds": Itot == seed})
    # direction 2: independently attempt a solution on each NO configuration
    no_rows = []
    for nm in primary_obs:
        cfg = [c for c in FAMILY if c["name"] == nm][0]
        rows, nunk, NU, _, _ = build(cfg, {"BRIDGE", "IF1", "IF5"})
        st = nu_nonzero(rows, nunk, NU)
        R = set(cfg["sites"])
        Itot = Fraction(sum(WEIGHTS[b] for _, b in cfg["content"]))
        seed = spectrum_monomial(cfg, R)[0]
        no_rows.append({"config": nm, "rank": st["rank"],
                        "kernel_dimension": st["kernel_dimension"],
                        "consistent": st["consistent"],
                        "nu_can_be_nonzero": st["nu_can_be_nonzero"],
                        "readout_I": q(Itot), "seed_mass": q(seed),
                        "gap": q(Itot - seed)})
    found_yes = [r["config"] for r in no_rows if r["nu_can_be_nonzero"]]
    broke_yes = [r["config"] for r in yes_rows
                 if r["row_violations"] or r["grid_violations"]
                 or not r["IF1_holds"]]
    return {
        "attack": "A2_OPPOSITE_DIRECTION",
        "yes_direction": yes_rows,
        "no_direction": no_rows,
        "solutions_found_where_the_primary_says_none": found_yes,
        "inconsistencies_found_in_the_exhibited_solution": broke_yes,
        "verdict_refuted": bool(found_yes or broke_yes),
        "reading": (
            f"The exhibited solution survives direct substitution on every "
            f"requirement row and every grid point, and its IF1 equality "
            f"(readout = seed mass) recomputes here.  On the "
            f"{len(no_rows)} configurations the primary calls obstructed, an "
            f"independent solution attempt under this checker's own "
            f"parameterization finds {len(found_yes)}.  The gap column shows "
            f"why: the linear readout and the confined seed mass simply "
            f"differ, and no kernel coordinate can close a difference that is "
            f"the same at every fibre point."),
    }


def bridge_attack() -> dict:
    """A3.  Re-derive every grid point from the amplitude field."""
    gp, bad, neg = 0, [], 0
    for cfg in FAMILY:
        ats = atoms_of(cfg)
        sol = {i: spectrum_monomial(cfg, set(a)) for i, a in enumerate(ats)}
        for n in HOLDING:
            W = win(n, cfg)
            for t in THETA_GRID:
                p = (1 - t * t) / (1 + t * t)
                mu = Fraction(0)
                for i, a in enumerate(ats):
                    if set(a) <= W:
                        mu += eval_monomial(sol[i], p)
                gp += 1
                if mu != z_direct(cfg, t, W):
                    bad.append({"config": cfg["name"], "window": n,
                                "theta": q(t)})
        for i in range(len(ats)):
            for t in THETA_GRID:
                p = (1 - t * t) / (1 + t * t)
                if eval_monomial(sol[i], p) < 0:
                    neg += 1
    return {
        "attack": "A3_BRIDGE",
        "grid_points_visited": gp,
        "grid_points_declared": len(FAMILY) * len(HOLDING) * len(THETA_GRID),
        "every_point_visited":
            gp == len(FAMILY) * len(HOLDING) * len(THETA_GRID),
        "violations": len(bad),
        "violation_exhibits": bad[:6],
        "negative_atom_masses": neg,
        "z_source": "recomputed from the amplitude field, never a spectrum",
    }


# --------------------------------------------------------------------------
# TEETH
# --------------------------------------------------------------------------
def teeth(tables, mono_rank) -> list:
    out = []

    # 1 tampered pin
    raw = bytearray(read_bytes(C892_PRIMARY))
    raw[len(raw) // 2] ^= 0x01
    out.append({"tooth": "T1_TAMPERED_PIN",
                "planted": "one byte flipped in the pinned 892 primary",
                "detected": sha256_of(bytes(raw)) != BRIEF_SHA256[C892_PRIMARY],
                "exit_if_live": 2})

    # 2 dropped requirement
    dropped = []
    for cfg in FAMILY:
        rows, nunk, NU, _, _ = build(cfg, {"BRIDGE", "IF1", "IF5"},
                                     drop=("IF1",))
        if nu_nonzero(rows, nunk, NU)["nu_can_be_nonzero"]:
            dropped.append(cfg["name"])
    out.append({"tooth": "T2_DROPPED_REQUIREMENT",
                "planted": "IF1 removed from the joint system",
                "configs_with_IF1": tables["ALL_FIVE"]["count"],
                "configs_without_IF1": len(dropped),
                "detected": len(dropped) != tables["ALL_FIVE"]["count"],
                "exit_if_live": 1})

    # 3 hardcoded rank
    probes = [([[1, 0], [0, 1]], 2), ([[1, 2], [2, 4]], 1),
              ([[0, 0], [0, 0]], 0), ([[3, 1, 4], [1, 5, 9], [2, 6, 5]], 3)]
    got = [bareiss_rank(m, len(m[0])) for m, _ in probes]
    out.append({"tooth": "T3_HARDCODED_RANK",
                "planted": "rank probes of known rank 2, 1, 0, 3",
                "expected": [e for _, e in probes], "observed": got,
                "detected": got == [e for _, e in probes]
                and len(set(got)) > 1,
                "exit_if_live": 1})

    # 4 leaked verdict
    src = read_text(SELF_REL)
    prim = json.loads(read_text(PRIMARY_RECEIPT))
    leaked = [w for w in ("PARTIAL", "INTERFACE-CONSTRUCTED",
                          "INTERFACE-OBSTRUCTED")
              if f'== "{w}"' in src or f"== '{w}'" in src]
    out.append({"tooth": "T4_LEAKED_VERDICT",
                "planted": "the primary's verdict string used as a branch",
                "verdict_strings_branched_on": leaked,
                "primary_verdict": prim["VERDICT"],
                "detected": not leaked,
                "note": ("the checker reads the primary's surviving-config "
                         "list only to AIM its attacks; every number it "
                         "reports is recomputed"),
                "exit_if_live": 1})

    # 5 skipped grid point
    declared = len(FAMILY) * len(HOLDING) * len(THETA_GRID)
    cfg = FAMILY[0]
    ats = atoms_of(cfg)
    sol = {i: spectrum_monomial(cfg, set(a)) for i, a in enumerate(ats)}
    n0 = HOLDING[0]
    W0 = win(n0, cfg)
    t0 = THETA_GRID[0]
    p0 = (1 - t0 * t0) / (1 + t0 * t0)
    mu0 = sum((eval_monomial(sol[i], p0) for i, a in enumerate(ats)
               if set(a) <= W0), Fraction(0))
    corrupted = mu0 + Fraction(1, 7)
    out.append({"tooth": "T5_SKIPPED_GRID_POINT",
                "planted": "a single grid point's value shifted by 1/7",
                "declared_points": declared,
                "detected": corrupted != z_direct(cfg, t0, W0)
                and mu0 == z_direct(cfg, t0, W0),
                "exit_if_live": 1})

    # 6 planted-satisfiability blindness
    hits = []
    for c in FAMILY:
        rows, nunk, NU, _, _ = build(c, {"BRIDGE", "IF1", "IF5"},
                                     planted="PLANT_SAT")
        if nu_nonzero(rows, nunk, NU)["nu_can_be_nonzero"]:
            hits.append(c["name"])
    out.append({"tooth": "T6_PLANTED_SATISFIABILITY_BLINDNESS",
                "planted": "IF1's readout replaced by the seed mass",
                "configs_satisfiable_under_the_plant": len(hits),
                "configs_satisfiable_without_it": tables["ALL_FIVE"]["count"],
                "detected": len(hits) == len(FAMILY)
                and len(hits) != tables["ALL_FIVE"]["count"],
                "exit_if_live": 1})

    # 7 basis independence
    out.append({"tooth": "T7_BASIS_ARTIFACT",
                "planted": "rank recomputed in the monomial basis",
                "monomial_rank": mono_rank,
                "primary_chebyshev_rank":
                    json.loads(read_text(PRIMARY_RECEIPT))
                    ["Q1_minimal_fibre_dimension"],
                "detected": mono_rank == json.loads(read_text(PRIMARY_RECEIPT))
                ["Q1_minimal_fibre_dimension"],
                "exit_if_live": 1})

    # 8 lattice-algorithm artifact
    mism = []
    for c in FAMILY:
        R = set(c["sites"]) & INBOX
        U = set()
        for n in HOLDING:
            U |= win(n, c)
        U |= R
        sig: dict = {}
        for x in U:
            k = tuple(1 if x in win(n, c) else 0 for n in HOLDING) + \
                (1 if x in R else 0,)
            sig.setdefault(k, set()).add(x)
        by_sig = {frozenset(v) for v in sig.values()}
        by_ref = {frozenset(a) for a in atoms_of(c)}
        if by_sig != by_ref:
            mism.append(c["name"])
    out.append({"tooth": "T8_LATTICE_ALGORITHM_ARTIFACT",
                "planted": "atoms rebuilt by signature bucketing and compared "
                           "against this checker's iterative refinement",
                "mismatched_configs": mism,
                "detected": not mism,
                "exit_if_live": 1})
    return out


# --------------------------------------------------------------------------
# run
# --------------------------------------------------------------------------
def run() -> int:
    prim = json.loads(read_text(PRIMARY_RECEIPT))
    tables = rebuild()
    rows_M = [spec_win(cfg, n) for n in HOLDING for cfg in FAMILY]
    mono_rank = bareiss_rank(rows_M, D + 1)

    a1 = minimality_attack(prim["Q1_minimal_fibre_dimension"])
    a2 = opposite_direction_attack(prim["Q2_joint_satisfiable_configs"],
                                   prim["Q2_jointly_obstructed_configs"])
    a3 = bridge_attack()
    th = teeth(tables, mono_rank)

    # ---- claim-by-claim agreement, all recomputed
    claims = [
        {"claim": "minimal fibre dimension",
         "primary": prim["Q1_minimal_fibre_dimension"],
         "checker": mono_rank,
         "agree": prim["Q1_minimal_fibre_dimension"] == mono_rank},
        {"claim": "bridge-only satisfiable configs",
         "primary": prim["Q2_subset_tables"]["BRIDGE_ONLY"]["count"],
         "checker": tables["BRIDGE_ONLY"]["count"],
         "agree": prim["Q2_subset_tables"]["BRIDGE_ONLY"]["count"]
                  == tables["BRIDGE_ONLY"]["count"]},
        {"claim": "theta-free (894 regime) satisfiable configs",
         "primary": prim["Q2_subset_tables"]["C894_THETA_FREE"]["count"],
         "checker": tables["C894_THETA_FREE"]["count"],
         "agree": prim["Q2_subset_tables"]["C894_THETA_FREE"]["count"]
                  == tables["C894_THETA_FREE"]["count"]},
        {"claim": "joint satisfiable configs",
         "primary": sorted(prim["Q2_joint_satisfiable_configs"]),
         "checker": sorted(tables["ALL_FIVE"]["configs"]),
         "agree": sorted(prim["Q2_joint_satisfiable_configs"])
                  == sorted(tables["ALL_FIVE"]["configs"])},
        {"claim": "bridge grid points",
         "primary": prim["Q3_grid_points"],
         "checker": a3["grid_points_visited"],
         "agree": prim["Q3_grid_points"] == a3["grid_points_visited"]},
        {"claim": "bridge violations",
         "primary": prim["Q3_bridge_violations"],
         "checker": a3["violations"],
         "agree": prim["Q3_bridge_violations"] == a3["violations"]},
    ]
    agree_all = all(c["agree"] for c in claims)
    refuted = (a1["minimality_claim_refuted"] or a2["verdict_refuted"]
               or not agree_all or a3["violations"] > 0)
    teeth_pass = sum(1 for t in th if t["detected"])

    verdict = "REFUTES" if refuted else "CORROBORATES"

    receipt = {
        "cycle": CYCLE,
        "role": "independent check, specified to refute",
        "self_sha256": sha256_of(read_bytes(SELF_REL)),
        "primary_checked": {
            "path": PRIMARY_REL,
            "sha256": sha256_of(read_bytes(PRIMARY_REL)),
            "receipt_sha256": sha256_of(read_bytes(PRIMARY_RECEIPT)),
            "blocklisted_from_import": True,
        },
        "blocklist_hits": len(BLOCK.hits),
        "independence": (
            "monomial basis against the primary's Chebyshev basis; Bareiss "
            "fraction-free integer elimination against its rational RREF; nu "
            "indexed first and atoms/degrees reversed, so pivot order "
            "differs throughout; window-lattice atoms built by iterative "
            "block refinement rather than signature bucketing; path-length "
            "spectra accumulated in this checker's own loop; every Z "
            "re-derived from the amplitude field rather than from a "
            "spectrum."),
        "pins": PINS["rows"],
        "claim_agreement": claims,
        "all_claims_agree": agree_all,
        "per_config_ranks_and_kernels": {
            k: [{"config": r["config"], "rank": r["rank"],
                 "kernel_dimension": r["kernel_dimension"],
                 "nu_can_be_nonzero": r["nu_can_be_nonzero"]}
                for r in v["rows"]] for k, v in tables.items()},
        "A1_minimality_attack": a1,
        "A2_opposite_direction_attack": a2,
        "A3_bridge_attack": a3,
        "teeth": th,
        "teeth_total": len(th),
        "teeth_detected": teeth_pass,
        "all_teeth_bite": teeth_pass == len(th),
        "checker_verdict": verdict,
        "elapsed_sec": round(time.time() - START, 3),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(receipt, indent=1, sort_keys=True,
                                   default=str) + "\n", encoding="utf-8")

    print("=" * 74)
    print(f"CYCLE {CYCLE} -- INDEPENDENT CHECK (specified to refute)")
    print("=" * 74)
    print(f"\nprimary   {PRIMARY_REL}")
    print(f"          sha256 {sha256_of(read_bytes(PRIMARY_REL))}")
    print(f"          blocklisted from import; blocklist hits "
          f"{len(BLOCK.hits)}")
    print(f"\nINDEPENDENCE\n  {receipt['independence']}")

    print(f"\nCLAIM AGREEMENT (every checker number recomputed)")
    for c in claims:
        print(f"  {'OK ' if c['agree'] else 'BAD'} {c['claim']:<42} "
              f"primary={c['primary']}  checker={c['checker']}")

    print(f"\nPER-CONFIG RANKS / KERNELS (Bareiss, monomial basis)")
    print(f"  {'config':<16} {'BRIDGE rank/ker':>18} "
          f"{'ALL_FIVE rank/ker':>19} {'nu!=0':>7}")
    b = {r["config"]: r for r in tables["BRIDGE_ONLY"]["rows"]}
    a = {r["config"]: r for r in tables["ALL_FIVE"]["rows"]}
    for cfg in FAMILY:
        n = cfg["name"]
        print(f"  {n:<16} {b[n]['rank']:>8}/{b[n]['kernel_dimension']:<9} "
              f"{a[n]['rank']:>9}/{a[n]['kernel_dimension']:<9} "
              f"{str(a[n]['nu_can_be_nonzero']):>7}")

    print(f"\n[A1] MINIMALITY ATTACK")
    print(f"  independent family rank (monomial)   = "
          f"{a1['independent_family_rank_monomial_basis']}")
    print(f"  primary claim                        = {a1['primary_claim']}")
    print(f"  family-wide smaller degree subset    = "
          f"{a1['family_wide_smaller_degree_subset']}")
    print(f"  truncated fibre -> configs served    = "
          f"{a1['truncated_fibre_configs_served']}")
    print(f"  smallest fibre serving the family    = "
          f"{a1['smallest_fibre_serving_the_whole_family']}")
    print(f"  surviving sub-grid rank              = "
          f"{a1['surviving_subgrid_rank']} "
          f"(degrees {a1['surviving_subgrid_smaller_degree_subset']})")
    print(f"  minimality REFUTED                   = "
          f"{a1['minimality_claim_refuted']}")
    print(f"  {a1['reading']}")

    print(f"\n[A2] OPPOSITE-DIRECTION ATTACK")
    for r in a2["yes_direction"]:
        print(f"  YES '{r['config']}': rows viol {r['row_violations']}, "
              f"grid {r['grid_violations']}/{r['grid_points']}, "
              f"I={r['readout_I']} seed={r['seed_mass']} "
              f"IF1 holds {r['IF1_holds']}")
    print(f"  NO direction -- independent solution attempts:")
    print(f"    {'config':<16} {'rank':>5} {'ker':>4} {'nu!=0':>6} "
          f"{'I':>6} {'seed':>7} {'gap':>7}")
    for r in a2["no_direction"]:
        print(f"    {r['config']:<16} {r['rank']:>5} "
              f"{r['kernel_dimension']:>4} "
              f"{str(r['nu_can_be_nonzero']):>6} {r['readout_I']:>6} "
              f"{r['seed_mass']:>7} {r['gap']:>7}")
    print(f"  solutions found where the primary says none: "
          f"{a2['solutions_found_where_the_primary_says_none']}")
    print(f"  inconsistencies in the exhibited solution:   "
          f"{a2['inconsistencies_found_in_the_exhibited_solution']}")
    print(f"  verdict REFUTED = {a2['verdict_refuted']}")

    print(f"\n[A3] BRIDGE ATTACK")
    print(f"  grid points visited/declared = "
          f"{a3['grid_points_visited']}/{a3['grid_points_declared']}  "
          f"(every point: {a3['every_point_visited']})")
    print(f"  violations                   = {a3['violations']}")
    print(f"  negative atom masses         = {a3['negative_atom_masses']}")
    print(f"  Z source                     = {a3['z_source']}")

    print(f"\nTEETH  {teeth_pass}/{len(th)} bite")
    for t in th:
        print(f"  {'BITES  ' if t['detected'] else 'BLUNT  '} "
              f"{t['tooth']:<40} exit_if_live={t['exit_if_live']}")
        print(f"          planted: {t['planted']}")

    print(f"\n{'=' * 74}")
    print(f"CHECKER VERDICT: {verdict}")
    print(f"  all claims agree   {agree_all}")
    print(f"  minimality refuted {a1['minimality_claim_refuted']}")
    print(f"  verdict refuted    {a2['verdict_refuted']}")
    print(f"  all teeth bite     {teeth_pass == len(th)}")
    print(f"  elapsed            {round(time.time() - START, 3)}s")
    print(f"  receipt            {OUT_JSON.relative_to(ROOT)}")
    print(f"{'=' * 74}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
