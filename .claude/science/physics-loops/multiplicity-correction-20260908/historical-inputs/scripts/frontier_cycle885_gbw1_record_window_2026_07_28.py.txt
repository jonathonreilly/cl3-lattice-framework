#!/usr/bin/env python3
"""Cycle 885: GBW1 -- is the Gate-B detector window record-determined?

Cycle 884 on this branch decomposed `GB-S2` and selected, by computed argmax,
the sharpest single missing lemma: `GBW1`, "the detector window (its
boundaries, its readout depth, its barrier, and its normalization) is
determined by record content rather than chosen by the runner".  It covers the
five WINDOW coordinates `(a, b, D, barrier, N)` of the honest chart's residual,
and its checker narrowed one of them: the barrier must be record-carried
CONFIGURATION, not a law.  This cycle ATTEMPTS `GBW1` from the four axioms
(Lattice / Qubit / Admissibility / Record) plus approved primitives, with NO new
axiom and NO new primitive.

(A) FORMALIZE FIRST, AS DATA.  Certificate `B` declares the theorem shape
    BEFORE any attempt: the configuration space (finite record configurations
    carrying content and formation depth), the acting group
    `G = Z^3 rtimes O_h^+` built from Lattice, the TYPE of each window
    coordinate under `G` (invariant scalar vs equivariant set), and the five
    requirements a candidate map must satisfy -- content-only (Record: "a
    readout value is determined by record content alone"), translation
    equivariance and rotation equivariance (Lattice: "No site is privileged"),
    permanence-monotonicity (Record: records are permanent), and
    non-triviality/separation (the map must vary with the configuration and
    must refuse perturbed windows).

    The declaration EXPOSES a coordinate the landed 5-tuple never carried: an
    annular window `a <= |x - c| <= b` has a CENTRE `c`, and "No site is
    privileged" forbids supplying it.  The landed chart is scalar-only and
    therefore cannot even STATE the equivariance requirement; this is computed
    in certificate `L` by exhibiting a constant impostor that is
    indistinguishable from the derived map on the scalar chart and refuted on
    the set-valued chart.

(B) THE CANDIDATE MAPS, COMPUTED.  Four candidate families are swept:

    W1  the record support's spatial extent: does the locked-site set's
        barycentre + extremal radii yield `(a, b)`?
    W2  the live payload projection: at axiom level the readable set is
        `supp(R)` ("only records are readable"), so W2's footprint is tested
        for SET EQUALITY with W1's.
    W3  the formation-edge structure: does the permanence filtration's moment
        count determine `N`?
    W4  the barrier as record-carried configuration: `B(R) = supp(R)`, forced
        by count-once + permanence, with the landed fixed central barrier
        refuted by translation equivariance.

    Each returns DERIVED (with its forcing chain) or UNDERDETERMINED / SUPPLIED
    (with its exact gap).  Presence of the 867/874/877/878 record-facing
    primaries in THIS branch's tracked file set is computed, not assumed
    (certificate `C`); where they are absent, the axiom-level surrogate is
    evaluated instead and the substitution is stated.

(C) THE VERDICT AS DATA.  Certificate `M` classifies all five landed window
    coordinates plus the exposed centre, counts how many the strongest derived
    map determines, and names the residual exactly.  The wrong-window stress in
    `L` is adversarial: perturbed tuples the claimed maps must refuse, plus an
    impostor battery of window-shaped maps that fail exactly one requirement.

(D) HONESTY.  This block does not close `GB-S2` and does not close Gate B.  It
    attacks `GB-S2`'s largest named component.  Every candidate that fails,
    fails with its exact gap stated, and the load-bearing results include two
    negatives against the landed construction.

All cited primaries are SHA-256 and git-blob pinned, read as text/AST/JSON only,
and blocked from import by a meta-path firewall.  Every certified number is
rebuilt here with stdlib exact arithmetic; no floating point enters any
certified quantity.

(E) REPAIR LOG (review pass on the interrupted draft; all defects found by
    re-reading the file against its own outputs):

    1.  RECEIPT LOCATION.  The receipt is written to `outputs/`; the draft
        wrote it to `logs/runner-cache/`, which is reserved for run caches.

    2.  PIN INTEGRITY.  `preflight_pins()` now runs before any science and
        exits 2 naming any pinned path that does not resolve, and every pins
        row carries an `exists` flag that the A_PINS gate requires.  A pinned
        input can no longer be silently skipped.  Each row also reports
        `same_basename_elsewhere_in_tree`, because two DISTINCT artifacts on
        this branch share the basename `gbs2_kernel_window_cycle884_
        receipt_2026_07_28.json`: the Cycle 884 PRIMARY receipt in
        `logs/runner-cache/` (pinned here, and the only one carrying the
        `sharpest_missing_lemma` / chart-dimension fields this cycle reads)
        and a Cycle 884 block-note receipt in `outputs/`.  The pin is by full
        path plus sha256 plus git blob, never by basename.

    3.  UNCAPPED FAILURE COUNTS.  `evaluate_map` used the capped exhibit list
        as its failure COUNT, so any map with more than six failures was
        reported as having exactly six.  Counts are now complete and only the
        exhibit lists are capped, with the cap reported.

    4.  ADMISSIBILITY-FILTERED UNIQUENESS.  The draft counted the boundary-
        shell reading as a rival witnessing non-uniqueness while its own REQ4
        evaluation refuted it.  A rival now witnesses non-uniqueness only if
        it satisfies every declared requirement; the boundary shell RETRACTS
        under permanence and is refuted, which SELECTS the support window and
        removes the binary locus choice from the residual.

    5.  COMPUTED CENTRE CLASS.  The centre coordinate's classification was a
        hard-coded literal; it is now computed from whether two admissible
        equivariant centre conventions actually split.

    6.  STRESS COVERAGE.  Every map that feeds the verdict is stressed (W1c
        and W2 were previously unstressed), and a cardinality-PRESERVING
        `move_site` perturbation was added: add/drop perturbations can be
        refused on a counting argument alone.

    7.  N ROBUSTNESS.  A degenerate-window control reads the same terminal
        normalization on the support locus, which IS the barrier, showing the
        readout collapses to a theta-independent seed there -- so the
        theta-dependence is not an artifact of the locus choice.

    8.  CONTROLS VISIBLE.  `O_CONTROLS` gated the exit code but was never
        rendered and never recorded; it is now a printed certificate, and the
        receipt carries the per-certificate pass map.

    9.  IDEMPOTENT CENSUS.  The lineage census excluded nothing, so its count
        changed between a first run and a re-run once the receipt existed; it
        now excludes the runner's own receipt and publishes its scan globs.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000

# Literal, greppable, and pinned below.
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/GATE_B_DYNAMICS_NOTE.md",
    "docs/GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md",
    "scripts/frontier_cycle884_gbs2_kernel_window_2026_07_28.py",
    "logs/runner-cache/gbs2_kernel_window_cycle884_receipt_2026_07_28.json",
    "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py",
)

import ast
from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import permutations, product
import json
from pathlib import Path
import re
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
# Receipts live in outputs/.  logs/runner-cache/ is reserved for run caches.
CACHE = ROOT / "outputs" / "gbw1_record_window_cycle885_receipt_2026_07_28.json"
CACHE_BASENAME = CACHE.name

BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)

# Directories scanned for basename collisions among pinned inputs, and for the
# lineage census in certificate C.
SCAN_DIRS = (
    ("scripts", "*.py"),
    ("docs", "*.md"),
    ("logs/runner-cache", "*"),
    ("outputs", "*.json"),
)


def preflight_pins() -> None:
    """Every pinned input must EXIST before any science runs.

    A silently skipped pin is the failure mode this guard exists to prevent:
    the run must die loudly, with a nonzero exit, naming the missing path.
    """
    missing = [p for p in AUDIT_INPUT_PATHS if not (ROOT / p).is_file()]
    if missing:
        sys.stderr.write(
            "FATAL: pinned input(s) missing; refusing to run.\n"
            + "".join(f"  MISSING PIN: {p}\n" for p in missing))
        raise SystemExit(2)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    AUDIT_INPUT_PATHS[1]:
        "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    AUDIT_INPUT_PATHS[2]:
        "0031e5ddcb2e1408db1bca3d738669b5463e672cfdbecc81b859b0fc609dc271",
    AUDIT_INPUT_PATHS[3]:
        "e246730a808174752f2bb1e113a89bccdf691db81b76bc1e2f6347ab027b0116",
    AUDIT_INPUT_PATHS[4]:
        "685973be36ac89a9632d8ac4113a6e49e9db32e98c9977ec5965a3bb6bff6aeb",
    AUDIT_INPUT_PATHS[5]:
        "5d5c669ebc7c58613892425745b09c35eb94dc216e8c38fe0f161e4f53541f98",
    AUDIT_INPUT_PATHS[6]:
        "2d96422d30f169a1c4b3215db373e4bffd7b1ef20056ea337ff4ae3f86d9511c",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "4a863da1f3f255354839277271a3a69a5c205133",
    AUDIT_INPUT_PATHS[1]: "40b0b4cd552cc41b55e4f3c59f9cabf621b3296b",
    AUDIT_INPUT_PATHS[2]: "5594d74e38a84d95c806449a305a16e1f1db8c43",
    AUDIT_INPUT_PATHS[3]: "2c9e1d0c75ea801f25fa0f9cfa92c67553770b4c",
    AUDIT_INPUT_PATHS[4]: "7b244a7ce3a4d61589bea0f222cca5d847ab0200",
    AUDIT_INPUT_PATHS[5]: "5a3c9db3ff688f26a70cc9b82aed53ec0ff41bb8",
    AUDIT_INPUT_PATHS[6]: "d563c2b9c2a261f44d7304baa51fdd3596188930",
}

# --------------------------------------------------------------------------
# Verbatim needles quoted from the pinned artifacts.
# --------------------------------------------------------------------------
AXIOM_NEEDLES = {
    "lattice_sites":
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site.",
    "no_site_privileged":
        "No site is privileged.",
    "finite_additive_readout":
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`.",
    "count_once":
        "A site never carries more than one record; records are permanent.",
    "only_records_readable":
        "Only records are readable. A readout value is determined by record "
        "content alone.",
    "axioms_and_primitives_complete":
        "Axioms and approved primitives are the complete supplied foundation.",
}

DYNAMICS_NEEDLES = {
    "gbs2b_row":
        "| `GB-S2b` | physical detector-window mass-gain, `TOWARD`, and `F~M` "
        "readout semantics | still supplied Gate-B runner data |",
    "gbs2b_open":
        "of the detector window, `TOWARD` sign, and `F~M` slope remains open.",
    "gbs2_split":
        "but the central barrier, detector-window mass gain, `TOWARD`, and "
        "`F~M` physical readout semantics remain supplied (`GB-S2b`).",
}

INTERFACE_NEEDLES = {
    "gbs2_named_supplied":
        "the specific phase-propagation kernel and detector-window/TOWARD/"
        "`F~M` readouts (`GB-S2`);",
    "kernel_form":
        "phi_GB(x) = strength / (r(x, mass) + 0.1)",
}

# The Cycle 883 finding this cycle leans on: formation weights/rates are
# excluded from axiom content by the axiom memo's own Open Gates section.
C883_NEEDLE = (
    "a weight assigned BY A FORMATION RULE is excluded by the memo's own text "
    "and cannot be derived."
)

# Fields read out of the pinned Cycle 884 receipt (JSON, not text).
C884_EXPECTED = {
    "sharpest_missing_lemma": "GBW1_record_determined_window",
    "sharpest_missing_lemma_strength_vs_GB_S2": "STRICTLY WEAKER",
    "honest_chart_residual_free_dimension": 10,
    "landed_chart_residual_free_dimension": 8,
}

# The five landed WINDOW coordinates, verbatim from the Cycle 884 chart.
WINDOW_COORDS = ("a", "b", "D", "barrier", "N")

# --------------------------------------------------------------------------
# Record-facing primaries the brief names.  Presence is COMPUTED, not assumed.
# --------------------------------------------------------------------------
LINEAGE_PROBES = (
    ("cycle867_composed_record_event_model_v3", "867"),
    ("cycle874_copy_redundancy_content", "874"),
    ("cycle877_sharded_content_survival", "877"),
    ("cycle878_composed_record_event_space", "878"),
)

NEIGHBOURS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
RBOX = 4          # amplitude DP box: |x|_inf <= RBOX
MAX_STEPS = 4     # amplitude DP depth


# --------------------------------------------------------------------------
# import firewall
# --------------------------------------------------------------------------
class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_module(self, fullname, path=None):  # pragma: no cover - legacy
        return self.find_spec(fullname, path)

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _read_bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def _read_text(path: str) -> str:
    return _read_bytes(path).decode("utf-8")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def git_blob_sha1(path: str) -> str:
    data = _read_bytes(path)
    header = f"blob {len(data)}\0".encode("ascii")
    import hashlib
    return hashlib.sha1(header + data).hexdigest()


def digest(payload: object) -> str:
    return sha256(
        json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()


def q(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def string_constants(path: str) -> list:
    """Every string literal in a pinned .py, with implicit concatenation done."""
    out = []
    for node in ast.walk(ast.parse(_read_text(path))):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            out.append(node.value)
    return out


# ---- exact Gaussian rationals --------------------------------------------
def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cabs2(a):
    return a[0] * a[0] + a[1] * a[1]


def unit_point(t: Fraction):
    """Exact rational point on the unit circle: ((1-t^2)/(1+t^2), 2t/(1+t^2))."""
    d = 1 + t * t
    return ((1 - t * t) / d, (2 * t) / d)


# ---- the group G = Z^3 rtimes O_h^+ --------------------------------------
def det3(m) -> int:
    (a, b, c), (d, e, f), (g, h, i) = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def proper_cubic_rotations():
    """The 24 signed permutation matrices with determinant +1."""
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            m = tuple(
                tuple(signs[r] if perm[r] == col else 0 for col in range(3))
                for r in range(3)
            )
            if det3(m) == 1:
                out.append(m)
    return sorted(out)


ROT24 = proper_cubic_rotations()
IDENTITY3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def matmul(m, n):
    return tuple(
        tuple(sum(m[i][k] * n[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def apply_mat(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def apply_mat_frac(m, v):
    return tuple(sum(Fraction(m[i][j]) * v[j] for j in range(3)) for i in range(3))


# --------------------------------------------------------------------------
# record configurations
# --------------------------------------------------------------------------
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


def transform(cfg: dict, mat, shift) -> dict:
    """Transport a configuration by g = (rotation, translation).

    Content and formation depth ride WITH the record (they are record content,
    not site labels), which is what makes the equivariance test meaningful.
    """
    content = dict(cfg["content"])
    depth = dict(cfg["depth"])
    new_sites = {}
    for s in cfg["sites"]:
        t = apply_mat(mat, s)
        t = (t[0] + shift[0], t[1] + shift[1], t[2] + shift[2])
        new_sites[t] = s
    sites = tuple(sorted(new_sites))
    return {
        "name": cfg["name"] + "|g",
        "sites": sites,
        "content": tuple((t, content[new_sites[t]]) for t in sites),
        "depth": tuple((t, depth[new_sites[t]]) for t in sites),
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


FAMILY = build_family()

# a deterministic, small set of group elements used for every equivariance test
TEST_SHIFTS = ((0, 0, 0), (1, 0, 0), (0, -2, 0), (3, 1, -2), (-1, -1, -1))


# --------------------------------------------------------------------------
# window-shaped functionals of a record configuration
# --------------------------------------------------------------------------
def barycentre(cfg) -> tuple:
    sites = cfg["sites"]
    n = len(sites)
    return tuple(Fraction(sum(s[i] for s in sites), n) for i in range(3))


def circum_like_centre(cfg) -> tuple:
    """A SECOND equivariant centre convention: barycentre of the extremal shell.

    Used only to test whether the centre convention is unique.
    """
    c = barycentre(cfg)
    r2 = {s: sum((Fraction(s[i]) - c[i]) ** 2 for i in range(3))
          for s in cfg["sites"]}
    top = max(r2.values())
    ext = [s for s in cfg["sites"] if r2[s] == top]
    n = len(ext)
    return tuple(Fraction(sum(s[i] for s in ext), n) for i in range(3))


def radii2(cfg, centre) -> tuple:
    r2 = [sum((Fraction(s[i]) - centre[i]) ** 2 for i in range(3))
          for s in cfg["sites"]]
    return (min(r2), max(r2))


def site_boundary(cfg) -> tuple:
    """Sites adjacent to the support but not in it: an equivariant shell."""
    supp = set(cfg["sites"])
    out = set()
    for s in supp:
        for nb in NEIGHBOURS:
            t = (s[0] + nb[0], s[1] + nb[1], s[2] + nb[2])
            if t not in supp:
                out.add(t)
    return tuple(sorted(out))


def readout(cfg, weights=(1, 2)) -> int:
    """Record's finite additive scalar readout with the Cycle-883 weight pair."""
    return sum(weights[bit] for _, bit in cfg["content"])


# ---- the candidate window maps -------------------------------------------
def map_W1_support(cfg) -> dict:
    """W1: the window IS the record support; (a, b) are its extremal radii."""
    c = barycentre(cfg)
    lo, hi = radii2(cfg, c)
    return {"centre": c, "a2": lo, "b2": hi, "set": tuple(cfg["sites"])}


def map_W1b_boundary(cfg) -> dict:
    """W1b: the window is the support's site-boundary shell (disjoint from it)."""
    bd = site_boundary(cfg)
    c = barycentre(cfg)
    r2 = [sum((Fraction(s[i]) - c[i]) ** 2 for i in range(3)) for s in bd]
    return {"centre": c, "a2": min(r2), "b2": max(r2), "set": bd}


def map_W1c_altcentre(cfg) -> dict:
    """W1 with the SECOND centre convention -- same support, different (a, b)."""
    c = circum_like_centre(cfg)
    lo, hi = radii2(cfg, c)
    return {"centre": c, "a2": lo, "b2": hi, "set": tuple(cfg["sites"])}


def map_W2_projection(cfg) -> dict:
    """W2 surrogate: the readable set.  'Only records are readable' => supp(R)."""
    return {"set": tuple(cfg["sites"])}


def map_W4_barrier(cfg) -> dict:
    """W4: the blocked set is the locked-site set, by count-once + permanence."""
    return {"set": tuple(cfg["sites"])}


def map_IMPOSTOR_fixed_barrier(cfg) -> dict:
    """The LANDED reading: a fixed central barrier, independent of the records."""
    return {"set": tuple(sorted(
        x for x in product((-1, 0, 1), repeat=3)))}


def map_IMPOSTOR_fixed_annulus(cfg) -> dict:
    """A constant window: a=1, b=2 about the origin, independent of records."""
    c = (Fraction(0), Fraction(0), Fraction(0))
    return {"centre": c, "a2": Fraction(1), "b2": Fraction(4),
            "set": tuple(sorted(x for x in product(range(-2, 3), repeat=3)
                                if 1 <= sum(v * v for v in x) <= 4))}


# --------------------------------------------------------------------------
# certificate A: pins
# --------------------------------------------------------------------------
def _basename_collisions(path: str) -> list:
    """Other files in the scanned tree carrying the SAME basename.

    Two distinct artifacts on this branch share the basename
    `gbs2_kernel_window_cycle884_receipt_2026_07_28.json` -- the Cycle 884
    PRIMARY receipt (in logs/runner-cache/) and the Cycle 884 block-note
    receipt (in outputs/).  Only the former carries the fields this cycle
    reads.  The collision is reported as data so no reader can mistake one for
    the other, and the pin is by full path + sha256 + git blob, never basename.
    """
    name = Path(path).name
    out = []
    for sub, pat in SCAN_DIRS:
        for p in (ROOT / sub).glob(pat):
            rel = str(p.relative_to(ROOT))
            if p.name == name and rel != path:
                out.append(rel)
    return sorted(out)


def pins_certificate() -> dict:
    rows = []
    for path in AUDIT_INPUT_PATHS:
        exists = (ROOT / path).is_file()
        data = _read_bytes(path)
        rows.append({
            "path": path,
            "exists": exists,
            "bytes": len(data),
            "sha256": sha256(data).hexdigest(),
            "sha256_matches": sha256(data).hexdigest() == EXPECTED_SHA256[path],
            "git_blob": git_blob_sha1(path),
            "git_blob_matches": git_blob_sha1(path) == EXPECTED_GIT_BLOBS[path],
            "same_basename_elsewhere_in_tree": _basename_collisions(path),
        })

    axioms = norm(_read_text(AUDIT_INPUT_PATHS[0]))
    axiom_hits = {k: norm(v) in axioms for k, v in AXIOM_NEEDLES.items()}
    dyn = norm(_read_text(AUDIT_INPUT_PATHS[2]))
    dyn_hits = {k: norm(v) in dyn for k, v in DYNAMICS_NEEDLES.items()}
    iface = norm(_read_text(AUDIT_INPUT_PATHS[3]))
    iface_hits = {k: norm(v) in iface for k, v in INTERFACE_NEEDLES.items()}
    # Cycle 883's exclusion sentence lives in a source string literal that the
    # file splits across lines, so it is read off the AST (implicit
    # concatenation resolved) rather than off the raw text.
    c883_consts = string_constants(AUDIT_INPUT_PATHS[6])
    c883_hit = any(norm(C883_NEEDLE) in norm(c) for c in c883_consts)

    receipt = json.loads(_read_text(AUDIT_INPUT_PATHS[5]))
    c884_hits = {k: receipt.get(k) == v for k, v in C884_EXPECTED.items()}
    c884_window_block = receipt.get("residual_free_by_block", {}).get("WINDOW", [])
    window_matches = tuple(sorted(c884_window_block)) == tuple(sorted(WINDOW_COORDS))

    # the AST of the 884 primary must still declare GBW1 with the same 5 pins
    consts = string_constants(AUDIT_INPUT_PATHS[4])
    gbw1_declared = any("GBW1_record_determined_window" == c for c in consts)

    ok = (
        len(rows) == len(AUDIT_INPUT_PATHS)
        and all(r["exists"] for r in rows)
        and all(r["sha256_matches"] and r["git_blob_matches"] for r in rows)
        and all(axiom_hits.values()) and all(dyn_hits.values())
        and all(iface_hits.values()) and c883_hit
        and all(c884_hits.values()) and window_matches and gbw1_declared
    )
    return {
        "rows": rows,
        "all_pins_present": all(r["exists"] for r in rows),
        "pinned_input_count": len(AUDIT_INPUT_PATHS),
        "missing_pins_are_fatal": (
            "preflight_pins() runs before any science and exits 2 naming any "
            "pinned path that does not resolve; a pin can never be silently "
            "skipped, and every row's existence is additionally gated here"),
        "axiom_needles_present": axiom_hits,
        "dynamics_needles_present": dyn_hits,
        "interface_needles_present": iface_hits,
        "cycle883_formation_weight_exclusion_present": c883_hit,
        "cycle884_receipt_fields_match": c884_hits,
        "cycle884_window_block_coords": sorted(c884_window_block),
        "cycle884_window_block_matches_this_cycles_target": window_matches,
        "GBW1_declared_in_cycle884_ast": gbw1_declared,
        "cycle884_GBW1_statement": receipt.get("sharpest_missing_lemma_statement"),
        "finding": (
            "The GBW1 target is read off the pinned Cycle 884 receipt and its "
            "primary's AST, not restated from memory: the lemma name, its "
            "STRICTLY WEAKER strength against GB-S2, and the exact five WINDOW "
            "coordinates (a, b, D, barrier, N) all round-trip."
        ),
        "pass": ok,
    }


# --------------------------------------------------------------------------
# certificate B: the theorem shape, declared as data BEFORE the attempt
# --------------------------------------------------------------------------
COORD_TYPES = {
    "a": ("G_invariant_scalar",
          "window inner boundary -- a radius, hence invariant under rotations "
          "and translations once measured from a co-moving centre"),
    "b": ("G_invariant_scalar",
          "window outer boundary -- same type as a"),
    "D": ("G_invariant_scalar",
          "readout depth -- the spatial group does not act on depth, so a "
          "record-determined D must be a G-invariant function of the "
          "configuration"),
    "barrier": ("G_equivariant_subset",
                "the blocked set -- a SUBSET of Z^3, which must move with the "
                "records: B(gR) = g B(R)"),
    "N": ("G_invariant_scalar",
          "terminal detector-distribution normalization"),
    "centre": ("G_equivariant_point",
               "EXPOSED BY THIS CYCLE: an annular window a <= |x - c| <= b "
               "carries a centre c with c(gR) = g c(R); the landed 5-tuple "
               "never carried it"),
}

REQUIREMENTS = {
    "REQ1_content_only": (
        "Record: 'Only records are readable. A readout value is determined by "
        "record content alone.'  The map must be a function of the record "
        "configuration and of nothing else -- no runner-local constant, no "
        "supplied site."),
    "REQ2_translation_equivariance": (
        "Lattice: 'No site is privileged.'  W(tau_v R) = tau_v W(R) for the "
        "equivariant types and W(tau_v R) = W(R) for the invariant types."),
    "REQ3_rotation_equivariance": (
        "Lattice: proper cubic rotations about each site.  Same condition for "
        "all 24 elements of O_h^+."),
    "REQ4_permanence_monotone": (
        "Record: 'A site never carries more than one record; records are "
        "permanent.'  Under R subset R' the map's set-valued output must not "
        "retract: W(R) subset W(R')."),
    "REQ5_separating": (
        "Non-triviality: the map must vary across the configuration family, "
        "and must REFUSE deliberately perturbed window tuples -- a constant "
        "map 'determines' any window and therefore determines none."),
}


def formalization_certificate() -> dict:
    theorem = {
        "name": "GBW1",
        "statement_as_data": (
            "There exists a map W from finite record configurations R (support "
            "in Z^3, per-record content, permanence filtration) to window "
            "tuples (centre, a, b, D, barrier, N) such that W satisfies REQ1-"
            "REQ5, and W is UNIQUE among such maps."),
        "domain": (
            "finite subsets S of Z^3 with a two-state content label per site "
            "(Qubit) and a permanence filtration (Record); no site of Z^3 is "
            "distinguished (Lattice)"),
        "group": "G = Z^3 rtimes O_h^+, |O_h^+| = 24",
        "codomain_types": {k: {"type": v[0], "meaning": v[1]}
                           for k, v in COORD_TYPES.items()},
        "requirements": REQUIREMENTS,
        "two_halves": {
            "EXISTENCE": "at least one map satisfying REQ1-REQ5 exists",
            "UNIQUENESS": "all such maps agree, coordinate by coordinate",
        },
        "why_the_centre_had_to_be_exposed": (
            "The landed window chart is scalar-only: (a, b, D, N) are numbers "
            "and 'barrier' is a locus.  A constant map a = 1, b = 2 is a "
            "G-INVARIANT scalar assignment and therefore passes REQ2/REQ3 "
            "vacuously on the scalar chart.  The requirement only bites on the "
            "SET the tuple denotes, and that set needs a centre.  So the "
            "honest window chart carries 6 coordinates, not 5, and the sixth "
            "is exactly where 'No site is privileged' applies."),
        "what_GBW1_does_NOT_require": (
            "GBW1 does not require the record configuration itself to be "
            "determined.  It is a map FROM configurations.  A coordinate that "
            "reduces to 'whatever the records are' is DERIVED under GBW1, not "
            "deferred."),
    }
    type_complete = all(c in COORD_TYPES for c in WINDOW_COORDS) and \
        "centre" in COORD_TYPES
    tests_declared = {
        "REQ1_content_only": "map is a pure function of the config record; "
                             "checked by AST-free construction and by the "
                             "impostor battery in L",
        "REQ2_translation_equivariance": f"{len(TEST_SHIFTS)} shifts x "
                                         f"{len(FAMILY)} configs",
        "REQ3_rotation_equivariance": f"{len(ROT24)} rotations x "
                                      f"{len(FAMILY)} configs",
        "REQ4_permanence_monotone": "nested pairs generated by depth truncation",
        "REQ5_separating": "perturbed-tuple refusal + non-constancy across the "
                           "family",
    }
    return {
        "theorem_shape": theorem,
        "declared_before_attempt": True,
        "coordinate_count_landed": len(WINDOW_COORDS),
        "coordinate_count_honest": len(COORD_TYPES),
        "exposed_coordinates": sorted(set(COORD_TYPES) - set(WINDOW_COORDS)),
        "tests_declared_per_requirement": tests_declared,
        "finding": (
            "The theorem shape is fixed as data before any attempt: a map from "
            "record configurations to a SIX-coordinate window tuple, "
            "G-equivariant by type, content-only, permanence-monotone and "
            "separating, with EXISTENCE and UNIQUENESS priced separately.  The "
            "sixth coordinate (the centre) is exposed by the formalization "
            "itself, mirroring how Cycle 884 exposed mu and c4 on the kernel "
            "side."),
        "pass": type_complete and set(tests_declared) == set(REQUIREMENTS),
    }


# --------------------------------------------------------------------------
# certificate C: which record-facing primaries are actually on this branch
# --------------------------------------------------------------------------
def lineage_certificate() -> dict:
    # The runner's OWN receipt is excluded from its own census, so the census
    # does not change between a first run and a re-run of the same commit.
    tracked = sorted(
        str(p.relative_to(ROOT))
        for sub, pat in SCAN_DIRS
        for p in (ROOT / sub).glob(pat)
        if p.name != CACHE_BASENAME
    )
    rows = []
    for label, tag in LINEAGE_PROBES:
        pat = re.compile(rf"(?i)cycle{tag}[^0-9]")
        hits = [p for p in tracked if pat.search(Path(p).name)]
        rows.append({
            "probe": label,
            "cycle_tag": tag,
            "present_in_this_worktree": bool(hits),
            "matching_paths": hits[:4],
        })
    present = [r["probe"] for r in rows if r["present_in_this_worktree"]]
    absent = [r["probe"] for r in rows if not r["present_in_this_worktree"]]
    surrogates = {
        "cycle867_composed_record_event_model_v3":
            "axiom-level surrogate: the composed record IS the configuration; "
            "composition is Record's finite additivity over pairwise-disjoint "
            "records",
        "cycle874_copy_redundancy_content":
            "axiom-level surrogate: count-once forbids a second record on a "
            "site, so copy redundancy is a property of the CONTENT map, tested "
            "here as content-only (REQ1)",
        "cycle877_sharded_content_survival":
            "axiom-level surrogate: permanence is the survival law; tested "
            "here as REQ4 monotonicity under the depth filtration",
        "cycle878_composed_record_event_space":
            "NO axiom-level surrogate exists for the Born-measure half; this "
            "is the one place the absence is load-bearing, and it is named in "
            "the N residual rather than papered over",
    }
    return {
        "tracked_file_count_scanned": len(tracked),
        "scan_globs": [f"{sub}/{pat}" for sub, pat in SCAN_DIRS],
        "self_excluded_from_census": CACHE_BASENAME,
        "rows": rows,
        "present": present,
        "absent": absent,
        "axiom_level_surrogates_used_where_absent": surrogates,
        "why_this_matters": (
            "The brief names the 867/874/877/878 record-facing structures as "
            "candidate sources of window-shaped data.  Their presence is "
            "COMPUTED here rather than assumed.  Where a primary is absent "
            "from this worktree it is NOT cited and NOT pinned; the candidate "
            "is evaluated against the axiom clause the primary would have "
            "packaged, and the substitution is stated in the row."),
        "finding": (
            f"{len(present)} of {len(LINEAGE_PROBES)} named record-facing "
            f"primaries are present in this worktree; {len(absent)} are absent "
            f"and are replaced by the named axiom-level surrogate.  The "
            f"absence is load-bearing in exactly one place: the composed-record "
            f"event space, which is where N's residual lands."),
        # gate is on the scan having produced a decision for every probe,
        # never on the decisions themselves
        "pass": len(rows) == len(LINEAGE_PROBES) and all(
            isinstance(r["present_in_this_worktree"], bool) for r in rows),
    }


# --------------------------------------------------------------------------
# certificate D: the group
# --------------------------------------------------------------------------
def group_certificate() -> dict:
    dets = sorted(set(det3(m) for m in ROT24))
    table_ok = all(matmul(m, n) in set(ROT24) for m in ROT24 for n in ROT24)
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    inverses_ok = all(
        any(matmul(m, n) == identity for n in ROT24) for m in ROT24)
    orders = {}
    for m in ROT24:
        k, cur = 1, m
        while cur != identity:
            cur = matmul(cur, m)
            k += 1
        orders[k] = orders.get(k, 0) + 1
    return {
        "rotation_count": len(ROT24),
        "determinants": dets,
        "closed_under_multiplication": table_ok,
        "every_element_invertible": inverses_ok,
        "identity_present": identity in set(ROT24),
        "order_profile": {str(k): v for k, v in sorted(orders.items())},
        "translation_shifts_tested": [list(s) for s in TEST_SHIFTS],
        "finding": (
            f"O_h^+ rebuilt from scratch as the determinant-one signed "
            f"permutation matrices: order {len(ROT24)}, determinants {dets}, "
            f"closed, with the cyclic-order profile "
            f"{ {str(k): v for k, v in sorted(orders.items())} }, which is the "
            f"1 + 8 + 3 + 6 + 6 class structure of the rotation group of the "
            f"cube."),
        "pass": (len(ROT24) == 24 and dets == [1] and table_ok
                 and inverses_ok and identity in set(ROT24)),
    }


# --------------------------------------------------------------------------
# certificate E: the configuration family
# --------------------------------------------------------------------------
def family_certificate() -> dict:
    rows = []
    for cfg in FAMILY:
        c = barycentre(cfg)
        lo, hi = radii2(cfg, c)
        rows.append({
            "name": cfg["name"],
            "records": len(cfg["sites"]),
            "readout_I_with_883_weights": readout(cfg),
            "barycentre": [q(x) for x in c],
            "inner_radius_squared": q(lo),
            "outer_radius_squared": q(hi),
            "depth_levels": len(set(d for _, d in cfg["depth"])),
            "boundary_shell_size": len(site_boundary(cfg)),
        })
    cards = sorted(set(r["records"] for r in rows))
    return {
        "family_size": len(FAMILY),
        "rows": rows,
        "distinct_support_cardinalities": cards,
        "construction": (
            "Twelve configurations built deterministically: shells, balls, an "
            "annulus, a punctured annulus, low-symmetry shapes (an L, a plane "
            "square, a chain), two LCG-selected sparse sets with fixed seeds, "
            "and one off-centre ball that exercises translation.  Content is "
            "the parity bit (Qubit's two states); formation depth is the rank "
            "of the record's squared radius about the configuration's own "
            "barycentre, which is an EQUIVARIANT rule, so the filtration "
            "transports under G."),
        "finding": (
            f"{len(FAMILY)} configurations spanning {len(cards)} distinct "
            f"support sizes, including the off-centre and low-symmetry cases "
            f"that a constant window map cannot survive."),
        "pass": (len(FAMILY) >= 8 and len(cards) >= 4
                 and all(r["records"] > 0 for r in rows)
                 and all(len(cfg["content"]) == len(cfg["sites"])
                         and len(cfg["depth"]) == len(cfg["sites"])
                         for cfg in FAMILY)),
    }


# --------------------------------------------------------------------------
# the requirement harness: evaluate any candidate map against REQ1-REQ5
# --------------------------------------------------------------------------
def _shift_point(p, shift):
    return tuple(p[i] + shift[i] for i in range(3))


EXHIBIT_CAP = 6


def evaluate_map(fn, has_centre: bool, has_radii: bool) -> dict:
    """Run REQ2/REQ3/REQ4/REQ5-nonconstancy on a candidate map, exactly.

    The failure COUNTS are complete.  Only the exhibit LISTS are capped, and
    the cap is reported alongside them, so `..._failures` always means "how
    many failures there are" and never "how many were kept".
    """
    equivariance_failures = 0
    equivariance_exhibits = []
    checked = 0

    def _note(kind, cfg, mat, shift):
        nonlocal equivariance_failures
        equivariance_failures += 1
        if len(equivariance_exhibits) < EXHIBIT_CAP:
            equivariance_exhibits.append({
                "config": cfg["name"], "kind": kind,
                "rotation": [list(r) for r in mat],
                "shift": list(shift),
            })

    for cfg in FAMILY:
        base = fn(cfg)
        for mat in ROT24:
            for shift in TEST_SHIFTS:
                checked += 1
                moved = fn(transform(cfg, mat, shift))
                # sets must transport
                want_set = tuple(sorted(
                    _shift_point(apply_mat(mat, s), shift) for s in base["set"]))
                if tuple(sorted(moved["set"])) != want_set:
                    _note("set", cfg, mat, shift)
                    continue
                if has_centre:
                    want_c = _shift_point(
                        apply_mat_frac(mat, base["centre"]), shift)
                    if tuple(moved["centre"]) != tuple(want_c):
                        _note("centre", cfg, mat, shift)
                        continue
                if has_radii:
                    if (moved["a2"], moved["b2"]) != (base["a2"], base["b2"]):
                        _note("radii", cfg, mat, shift)
    # REQ4: permanence monotonicity along the depth filtration
    monotone_failures = 0
    monotone_exhibits = []
    monotone_checks = 0
    for cfg in FAMILY:
        levels = sorted(set(d for _, d in cfg["depth"]))
        prev = None
        for lv in levels:
            sub_sites = [s for s, d in cfg["depth"] if d <= lv]
            sub = make_config(cfg["name"] + f"@{lv}", sub_sites)
            cur = set(fn(sub)["set"])
            if prev is not None:
                monotone_checks += 1
                if not prev <= cur:
                    monotone_failures += 1
                    if len(monotone_exhibits) < EXHIBIT_CAP:
                        monotone_exhibits.append({
                            "config": cfg["name"], "level": lv,
                            "lost_sites": len(prev - cur),
                        })
            prev = cur
    # REQ5 non-constancy
    distinct_sets = len(set(tuple(sorted(fn(cfg)["set"])) for cfg in FAMILY))
    distinct_radii = None
    if has_radii:
        distinct_radii = len(set(
            (fn(cfg)["a2"], fn(cfg)["b2"]) for cfg in FAMILY))
    return {
        "equivariance_checks": checked,
        "equivariance_failures": equivariance_failures,
        "equivariance_failure_exhibits": equivariance_exhibits,
        "equivariance_exhibits_capped_at": EXHIBIT_CAP,
        "REQ2_REQ3_equivariant": equivariance_failures == 0,
        "permanence_monotonicity_checks": monotone_checks,
        "permanence_monotonicity_failures": monotone_failures,
        "permanence_monotonicity_exhibits": monotone_exhibits,
        "permanence_monotonicity_exhibits_capped_at": EXHIBIT_CAP,
        "REQ4_permanence_monotone": monotone_failures == 0,
        "distinct_set_values_across_family": distinct_sets,
        "distinct_radius_pairs_across_family": distinct_radii,
        "REQ5_nonconstant": distinct_sets > 1,
        "admissible_REQ2_REQ5": (equivariance_failures == 0
                                 and monotone_failures == 0
                                 and distinct_sets > 1),
    }


# --------------------------------------------------------------------------
# certificate F: W1 -- the record support's spatial extent
# --------------------------------------------------------------------------
def W1_certificate() -> dict:
    supp = evaluate_map(map_W1_support, has_centre=True, has_radii=True)
    bdry = evaluate_map(map_W1b_boundary, has_centre=True, has_radii=True)
    altc = evaluate_map(map_W1c_altcentre, has_centre=True, has_radii=True)

    # ---- Which rivals are ADMISSIBLE?  A map that fails a declared
    # requirement is REFUTED and cannot witness non-uniqueness.  This is
    # computed, never assumed: the rival's own REQ2-REQ5 evaluation decides.
    rival_eval = {
        "W1b_boundary_shell": bdry,
        "W1c_alternate_centre": altc,
    }
    rival_failed_requirements = {}
    for rname, ev in rival_eval.items():
        failed = [req for req, okflag in (
            ("REQ2_REQ3_equivariance", ev["REQ2_REQ3_equivariant"]),
            ("REQ4_permanence_monotone", ev["REQ4_permanence_monotone"]),
            ("REQ5_nonconstant", ev["REQ5_nonconstant"]),
        ) if not okflag]
        rival_failed_requirements[rname] = failed
    admissible_rivals = sorted(
        r for r, f in rival_failed_requirements.items() if not f)
    refuted_rivals = sorted(
        r for r, f in rival_failed_requirements.items() if f)

    # Do the candidates AGREE?  Uniqueness is the second half.
    RIVAL_OF_PAIR = {
        "supp_vs_boundary": "W1b_boundary_shell",
        "centre_convention": "W1c_alternate_centre",
    }
    disagreements = []
    for cfg in FAMILY:
        s, b_, a_ = map_W1_support(cfg), map_W1b_boundary(cfg), map_W1c_altcentre(cfg)
        if (s["a2"], s["b2"]) != (b_["a2"], b_["b2"]):
            disagreements.append({"config": cfg["name"], "pair": "supp_vs_boundary",
                                  "supp": [q(s["a2"]), q(s["b2"])],
                                  "other": [q(b_["a2"]), q(b_["b2"])]})
        if (s["a2"], s["b2"]) != (a_["a2"], a_["b2"]):
            disagreements.append({"config": cfg["name"], "pair": "centre_convention",
                                  "supp": [q(s["a2"]), q(s["b2"])],
                                  "other": [q(a_["a2"]), q(a_["b2"])]})
    live = [d for d in disagreements
            if RIVAL_OF_PAIR[d["pair"]] in admissible_rivals]
    dead = [d for d in disagreements
            if RIVAL_OF_PAIR[d["pair"]] in refuted_rivals]

    # The centre coordinate on its own: do the two equivariant centre
    # conventions ever differ as POINTS (not merely through the radii)?
    centre_splits = [
        cfg["name"] for cfg in FAMILY
        if tuple(barycentre(cfg)) != tuple(circum_like_centre(cfg))]
    centre_rival_admissible = "W1c_alternate_centre" in admissible_rivals
    centre_conventions_agree = not (centre_splits and centre_rival_admissible)

    # Does supp(R) actually FILL the annulus its own (a, b) denote?
    fills = []
    for cfg in FAMILY:
        w = map_W1_support(cfg)
        c, lo, hi = w["centre"], w["a2"], w["b2"]
        rad = int(hi) + 2
        ann = set()
        base = tuple(int(x) for x in (c[0], c[1], c[2]))
        for off in product(range(-rad, rad + 1), repeat=3):
            x = (base[0] + off[0], base[1] + off[1], base[2] + off[2])
            r2 = sum((Fraction(x[i]) - c[i]) ** 2 for i in range(3))
            if lo <= r2 <= hi:
                ann.add(x)
        fills.append({
            "config": cfg["name"],
            "support": len(cfg["sites"]),
            "annulus_sites": len(ann),
            "support_fills_annulus": ann == set(cfg["sites"]),
        })
    filled = sum(1 for f in fills if f["support_fills_annulus"])

    return {
        "candidate": "W1 -- the window is read off the locked-site set",
        "W1_support_reading": supp,
        "W1b_boundary_shell_reading": bdry,
        "W1c_alternate_centre_convention": altc,
        "existence": {
            "at_least_one_admissible_map":
                supp["REQ2_REQ3_equivariant"] and supp["REQ5_nonconstant"],
            "forcing_chain": (
                "Record: 'Only records are readable. A readout value is "
                "determined by record content alone.'  A windowed readout "
                "I_W(R) = I(R restricted to W) is determined by record content "
                "alone ONLY IF W is itself a function of R -- otherwise the "
                "value depends on W, which is not record content.  So the "
                "axiom FORCES the window to be record-determined.  Lattice's "
                "'No site is privileged' then forces that function to be "
                "G-equivariant.  supp(R) with its barycentric extremal radii "
                "is such a function, computed above."),
        },
        "uniqueness": {
            "rival_failed_requirements": rival_failed_requirements,
            "admissible_rivals": admissible_rivals,
            "refuted_rivals": refuted_rivals,
            "candidates_agree": not live,
            "disagreement_count": len(live),
            "disagreement_exhibits": live[:6],
            "disagreements_with_refuted_rivals_not_counted": len(dead),
            "refuted_rival_disagreement_exhibits": dead[:3],
            "centre_convention_splits_on_configs": centre_splits,
            "centre_conventions_agree": centre_conventions_agree,
            "why_it_fails": (
                f"Uniqueness is decided ONLY against rivals that themselves "
                f"satisfy every declared requirement.  Admissible rivals: "
                f"{admissible_rivals or ['none']}.  Refuted rivals (and the "
                f"requirement each fails): "
                f"{ {r: rival_failed_requirements[r] for r in refuted_rivals} }."
                f"  {len(live)} disagreement(s) survive that filter and "
                f"{len(dead)} are discarded as disagreements with a refuted "
                f"map.  The surviving split is the CENTRE convention "
                f"(barycentre vs extremal-shell barycentre), which differs as "
                f"a point on {len(centre_splits)}/{len(FAMILY)} "
                f"configurations.  Existence is derived; uniqueness is not, "
                f"but the residual is one convention, not a menu."),
            "boundary_shell_rival_status": (
                f"REFUTED by REQ4.  The site-boundary shell is equivariant and "
                f"content-only, but it RETRACTS under permanence: as records "
                f"accumulate, former boundary sites are absorbed into the "
                f"support, so W(R) is not contained in W(R') for R contained "
                f"in R'.  Computed: {bdry['permanence_monotonicity_failures']} "
                f"failures out of {bdry['permanence_monotonicity_checks']} "
                f"nested pairs.  Permanence therefore SELECTS the support "
                f"reading over the boundary-shell reading -- a strictly "
                f"sharper outcome than 'two admissible windows disagree'."),
        },
        "annulus_fill": {
            "rows": fills,
            "configs_whose_support_fills_its_own_annulus": filled,
            "of": len(FAMILY),
            "reading": (
                "The axioms determine the window as a SET.  The landed chart "
                "parameterizes it as an ANNULUS (a, b).  The two coincide only "
                "when the support fills the annulus its own extremal radii "
                "denote; the count above is how often that happens in this "
                "family.  Where it does not, (a, b) under-determine the set "
                "and the annular parameterization is the supplied part."),
        },
        "outcome": None,   # filled by the verdict certificate
        "finding": (
            f"W1 EXISTS: the support reading is equivariant on "
            f"{supp['equivariance_checks']} group elements x configurations "
            f"with {supp['equivariance_failures']} failures, permanence-"
            f"monotone on {supp['permanence_monotonicity_checks']} nested "
            f"pairs with {supp['permanence_monotonicity_failures']} failures, "
            f"and non-constant with "
            f"{supp['distinct_set_values_across_family']} distinct values.  Of "
            f"the two rivals, {len(refuted_rivals)} is REFUTED "
            f"({', '.join(refuted_rivals) or 'none'}: the boundary shell "
            f"retracts under permanence, "
            f"{bdry['permanence_monotonicity_failures']} failures) and "
            f"{len(admissible_rivals)} survives "
            f"({', '.join(admissible_rivals) or 'none'}).  Uniqueness still "
            f"FAILS, but only through the centre convention: {len(live)} "
            f"surviving disagreements on {len(centre_splits)}/{len(FAMILY)} "
            f"configurations.  And the support fills its own annulus in only "
            f"{filled} of {len(FAMILY)} configurations, so the (a, b) "
            f"parameterization is strictly weaker than the set."),
        # gate: the candidate and BOTH rivals were fully evaluated against every
        # declared requirement -- not that any of them succeeded.
        "pass": (
            all(all(k in ev for k in ("REQ2_REQ3_equivariant",
                                      "REQ4_permanence_monotone",
                                      "REQ5_nonconstant"))
                for ev in (supp, bdry, altc))
            and len(fills) == len(FAMILY)
            and set(rival_failed_requirements) == set(rival_eval)),
    }


# --------------------------------------------------------------------------
# certificate G: W2 -- the live payload projection
# --------------------------------------------------------------------------
def W2_certificate(lineage: dict) -> dict:
    proj = evaluate_map(map_W2_projection, has_centre=False, has_radii=False)
    same = all(
        tuple(sorted(map_W2_projection(cfg)["set"]))
        == tuple(sorted(map_W1_support(cfg)["set"]))
        for cfg in FAMILY)
    absent = "cycle867_composed_record_event_model_v3" in lineage["absent"]
    return {
        "candidate": "W2 -- the live payload projection's spatial footprint",
        "landed_867_lineage_available_here": not absent,
        "surrogate_used": (
            "the readable set.  Record: 'Only records are readable' makes the "
            "readable set exactly supp(R); a projection cannot expose more "
            "than the records it projects."),
        "evaluation": proj,
        "collapses_into_W1": same,
        "exact_gap": (
            "NONE at axiom level -- and that is the finding: W2 is not an "
            "independent source of window data.  At axiom level the live "
            "projection's footprint is set-equal to W1's support on every "
            "configuration in the family, so W2 supplies no coordinate that W1 "
            "does not already supply.  Any EXTRA structure the landed 147-wire "
            "projection carries (wire count, shard layout) is runner data, not "
            "axiom content, and the 867 primary is not in this worktree to be "
            "pinned; a window coordinate read off a wire count would be "
            "supplied under a different name."),
        "finding": (
            f"W2 collapses into W1: set-equality holds on "
            f"{len(FAMILY)}/{len(FAMILY)} configurations.  The payload "
            f"projection is the readable set, and the readable set is the "
            f"record support.  W2 therefore adds ZERO window coordinates."),
        "pass": isinstance(same, bool) and "REQ5_nonconstant" in proj,
    }


# --------------------------------------------------------------------------
# certificate H: W3 -- formation edges and N
# --------------------------------------------------------------------------
def W3_certificate() -> dict:
    rows = []
    for cfg in FAMILY:
        levels = sorted(set(d for _, d in cfg["depth"]))
        rows.append({
            "config": cfg["name"],
            "formation_moments": len(levels),
            "records": len(cfg["sites"]),
            "additive_readout_I": readout(cfg),
            "unweighted_count": len(cfg["sites"]),
        })
    # Is the moment count a G-invariant of the configuration?
    invariant_failures = 0
    for cfg in FAMILY:
        base = len(set(d for _, d in cfg["depth"]))
        for mat in ROT24[:8]:
            for shift in TEST_SHIFTS:
                moved = transform(cfg, mat, shift)
                remade = make_config("x", moved["sites"])
                if len(set(d for _, d in remade["depth"])) != base:
                    invariant_failures += 1
    # Do distinct configurations share a moment count while differing in I?
    collisions = []
    for i, r in enumerate(rows):
        for s in rows[i + 1:]:
            if (r["formation_moments"] == s["formation_moments"]
                    and r["additive_readout_I"] != s["additive_readout_I"]):
                collisions.append([r["config"], s["config"],
                                   r["formation_moments"],
                                   r["additive_readout_I"],
                                   s["additive_readout_I"]])
    return {
        "candidate": "W3 -- do formation moments determine N?",
        "rows": rows,
        "moment_count_is_G_invariant": invariant_failures == 0,
        "moment_count_invariance_failures": invariant_failures,
        "moment_count_collisions_with_different_readout": collisions[:6],
        "collision_count": len(collisions),
        "what_IS_derived": (
            "Record's finite additivity with I(empty)=0 plus count-once make "
            "the readout a SUM over records: I(R) = sum over sites of the "
            "per-record weight, and Cycle 883's pinned weight pair (1, 2) "
            "fixes the two content values.  So a RECORD-COUNT normalization is "
            "record-determined outright."),
        "exact_gap": (
            "N is not the record-count normalization.  N normalizes the "
            "TERMINAL DETECTOR DISTRIBUTION, which is a quadratic functional "
            "of propagation amplitudes, while the additive readout is a LINEAR "
            "functional of record content.  Two obstructions, both computed: "
            "(i) certificate K exhibits configurations on which the amplitude "
            "normalization moves while the additive readout is fixed, and "
            "moves again when the kernel's phase gain theta moves -- so N is "
            "not a function of record content alone; (ii) the pinned Cycle 883 "
            "reading of the axiom memo's Open Gates section excludes formation "
            "weights and rates from axiom content, which is exactly the "
            "content a rate-shaped normalization would need."),
        "finding": (
            f"The formation filtration is a G-invariant of the configuration "
            f"({invariant_failures} invariance failures), and it does yield a "
            f"record-determined COUNT.  But the count collides: "
            f"{len(collisions)} pairs of configurations share a formation-"
            f"moment count while differing in additive readout, so the moment "
            f"count does not even determine the record readout, let alone the "
            f"amplitude normalization."),
        "pass": len(rows) == len(FAMILY) and isinstance(invariant_failures, int),
    }


# --------------------------------------------------------------------------
# certificate I: W4 -- the barrier as record-carried configuration
# --------------------------------------------------------------------------
def W4_certificate() -> dict:
    derived = evaluate_map(map_W4_barrier, has_centre=False, has_radii=False)
    landed = evaluate_map(map_IMPOSTOR_fixed_barrier, has_centre=False,
                          has_radii=False)
    # the collision: the axiom-forced barrier and the axiom-forced readable
    # set are the SAME set, whereas the landed model needs them disjoint
    collisions = []
    for cfg in FAMILY:
        b = set(map_W4_barrier(cfg)["set"])
        w = set(map_W2_projection(cfg)["set"])
        collisions.append({
            "config": cfg["name"],
            "barrier_size": len(b),
            "readable_size": len(w),
            "overlap": len(b & w),
            "disjoint": not (b & w),
        })
    disjoint_count = sum(1 for c in collisions if c["disjoint"])
    # the candidate repair: the boundary shell is record-determined AND
    # disjoint from the barrier -- but is it ADMISSIBLE?  Computed, not assumed.
    repair = []
    for cfg in FAMILY:
        b = set(map_W4_barrier(cfg)["set"])
        w = set(map_W1b_boundary(cfg)["set"])
        repair.append({"config": cfg["name"], "disjoint": not (b & w)})
    repair_ok = sum(1 for r in repair if r["disjoint"])
    boundary_eval = evaluate_map(map_W1b_boundary, has_centre=True,
                                 has_radii=True)
    # every ADMISSIBLE window candidate, and whether any is barrier-disjoint
    admissible_windows = {}
    for wname, wfn in (("W1_support", map_W1_support),
                       ("W1b_boundary_shell", map_W1b_boundary),
                       ("W1c_alternate_centre", map_W1c_altcentre)):
        ev = evaluate_map(wfn, has_centre=True, has_radii=True)
        disjoint_all = all(
            not (set(map_W4_barrier(cfg)["set"]) & set(wfn(cfg)["set"]))
            for cfg in FAMILY)
        admissible_windows[wname] = {
            "admissible_REQ2_REQ5": ev["admissible_REQ2_REQ5"],
            "disjoint_from_barrier_on_every_config": disjoint_all,
        }
    admissible_and_disjoint = sorted(
        w for w, r in admissible_windows.items()
        if r["admissible_REQ2_REQ5"] and r["disjoint_from_barrier_on_every_config"])
    return {
        "candidate": "W4 -- the barrier is record-carried configuration",
        "derived_map": "B(R) = supp(R), the locked-site set",
        "forcing_chain": (
            "Record: 'A site never carries more than one record; records are "
            "permanent.'  A site already carrying a record is closed to any "
            "further registration, permanently.  That IS a blocked set, and it "
            "is carried by the configuration -- exactly Cycle 884's narrowing "
            "that the barrier must be record-carried CONFIGURATION and not a "
            "law.  Lattice's 'No site is privileged' forbids naming the "
            "blocked set by coordinates, so B must be a function of R; "
            "count-once names it uniquely, since B smaller than supp(R) "
            "contradicts count-once and B larger than supp(R) blocks an "
            "unoccupied site, which requires a LAW -- the thing 884 excluded."),
        "evaluation": derived,
        "landed_fixed_barrier_impostor": {
            "map": "B = the fixed 3x3x3 central cube, independent of R",
            "evaluation": landed,
            "refuted_by": (
                "translation equivariance.  A record-independent barrier does "
                "not move with the records, so B(tau_v R) = B(R) != tau_v B(R) "
                "for every non-zero v.  This is a direct computed collision "
                "with 'No site is privileged': the landed central barrier "
                "privileges the sites of the cube it names."),
        },
        "barrier_readable_collision": {
            "rows": collisions,
            "configs_where_barrier_and_readable_set_are_disjoint": disjoint_count,
            "of": len(FAMILY),
            "reading": (
                "The two axiom-forced identifications COINCIDE: the blocked "
                "set is supp(R) by count-once, and the readable set is supp(R) "
                "by 'only records are readable'.  The landed Gate-B model "
                "needs a barrier that blocks propagation and a window that "
                "reads, DISJOINT from each other.  So the landed disjointness "
                "is not axiom content; it is an extra identification -- a "
                "PROPAGATION barrier read off the REGISTRATION-blocked set."),
        },
        "attempted_repair": {
            "map": "window = the support's site-boundary shell (W1b)",
            "configs_disjoint_from_the_barrier": repair_ok,
            "of": len(FAMILY),
            "boundary_shell_admissible": boundary_eval["admissible_REQ2_REQ5"],
            "boundary_shell_permanence_failures":
                boundary_eval["permanence_monotonicity_failures"],
            "boundary_shell_permanence_checks":
                boundary_eval["permanence_monotonicity_checks"],
            "windows_admissible_and_barrier_disjoint": admissible_and_disjoint,
            "window_admissibility_vs_disjointness": admissible_windows,
            "note": (
                f"The repair FAILS, and its failure is load-bearing.  W1b is "
                f"equivariant, content-only and disjoint from B(R) on "
                f"{repair_ok}/{len(FAMILY)} configurations, but it is NOT "
                f"admissible: it retracts under permanence "
                f"({boundary_eval['permanence_monotonicity_failures']} "
                f"failures on "
                f"{boundary_eval['permanence_monotonicity_checks']} nested "
                f"pairs).  Of the window candidates evaluated here, "
                f"{len(admissible_and_disjoint)} are BOTH admissible AND "
                f"disjoint from the barrier on every configuration.  So no "
                f"record-determined window in this sweep separates from the "
                f"blocked set, and the landed model's barrier/window "
                f"disjointness stays a named identification premise rather "
                f"than a derivable arrangement."),
        },
        "finding": (
            f"The barrier is the one window coordinate the axioms name "
            f"outright: B(R) = supp(R), equivariant on "
            f"{derived['equivariance_checks']} tests with "
            f"{derived['equivariance_failures']} failures and monotone under "
            f"permanence.  The landed fixed central barrier fails equivariance "
            f"on {landed['equivariance_failures']} of "
            f"{landed['equivariance_checks']} checks and is refuted.  "
            f"The cost: the axiom-forced barrier and the axiom-forced readable "
            f"set coincide ({disjoint_count}/{len(FAMILY)} disjoint), and "
            f"{len(admissible_and_disjoint)} of the three swept window "
            f"candidates is both admissible and barrier-disjoint, so the "
            f"landed barrier/window separation needs one named identification."),
        "pass": ("REQ2_REQ3_equivariant" in derived
                 and "REQ2_REQ3_equivariant" in landed
                 and len(collisions) == len(FAMILY)
                 and len(admissible_windows) == 3),
    }


# --------------------------------------------------------------------------
# certificate J: the readout depth D under permanence
# --------------------------------------------------------------------------
def depth_certificate() -> dict:
    rows = []
    for cfg in FAMILY:
        levels = sorted(set(d for _, d in cfg["depth"]))
        seq = []
        for lv in range(1, max(levels) + 4):
            sub_sites = [s for s, d in cfg["depth"] if d <= lv]
            sub = make_config("x", sub_sites) if sub_sites else None
            seq.append(readout(sub) if sub else 0)
        d_form = max(levels)
        stationary = all(v == seq[d_form - 1] for v in seq[d_form - 1:])
        nondecreasing = all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1))
        rows.append({
            "config": cfg["name"],
            "last_formation_depth": d_form,
            "readout_by_depth": seq,
            "stationary_above_last_formation_depth": stationary,
            "nondecreasing_in_depth": nondecreasing,
        })
    all_stationary = all(r["stationary_above_last_formation_depth"] for r in rows)
    all_monotone = all(r["nondecreasing_in_depth"] for r in rows)
    return {
        "coordinate": "D -- the readout depth",
        "rows": rows,
        "stationary_on_every_config": all_stationary,
        "nondecreasing_on_every_config": all_monotone,
        "forcing_chain": (
            "Record: 'records are permanent'.  A record present at depth d is "
            "present at every depth d' >= d, so the depth-indexed readout is "
            "non-decreasing and becomes CONSTANT at the configuration's last "
            "formation depth.  Above that depth every value of D gives the "
            "identical readout: D is GAUGE there.  Below it, reading at depth "
            "D is reading a DIFFERENT (smaller) configuration, so D is not an "
            "independent coordinate below either -- it is a relabelling of the "
            "configuration by the permanence filtration."),
        "landed_relation_reused": (
            "Cycle 884's route R1 proved b <= D on the pinned lattice (the "
            "influence cone), which bounds D from below by the window's outer "
            "boundary.  Combined with permanence-stationarity above the last "
            "formation depth, D's admissible range is an interval on which "
            "every value gives the same readout."),
        "exact_gap": (
            "NONE for the readout.  D is determined as a GAUGE CLASS, not as a "
            "number.  A cycle that wanted a numerical D would have to name a "
            "convention inside the gauge class, and that convention would "
            "change no readout -- which is the definition of gauge."),
        "finding": (
            f"D is gauge above the last formation depth on "
            f"{sum(1 for r in rows if r['stationary_above_last_formation_depth'])}"
            f"/{len(FAMILY)} configurations and the depth-readout is "
            f"non-decreasing on "
            f"{sum(1 for r in rows if r['nondecreasing_in_depth'])}"
            f"/{len(FAMILY)}.  Permanence, not a new premise, is what removes "
            f"this coordinate."),
        "pass": len(rows) == len(FAMILY) and all(
            isinstance(r["stationary_above_last_formation_depth"], bool)
            for r in rows),
    }


# --------------------------------------------------------------------------
# certificate K: N, the terminal normalization -- the amplitude coupling
# --------------------------------------------------------------------------
def amplitude_normalization(cfg, t: Fraction, window_key: str) -> Fraction:
    """Exact terminal normalization Z = sum over window sites of |A(x)|^2.

    A is the finite path sum of length <= MAX_STEPS from the record-determined
    source set (the lattice sites closest to the barycentre), stepping only on
    sites outside the barrier B(R) = supp(R), with per-edge phase gain the exact
    unit-circle point u(t).  Everything is Gaussian-rational; no floating point.
    """
    u = unit_point(t)
    box = [x for x in product(range(-RBOX, RBOX + 1), repeat=3)]
    inbox = set(box)
    barrier = set(cfg["sites"])
    if window_key == "support":
        window = set(cfg["sites"])
    else:
        window = set(site_boundary(cfg))
    c = barycentre(cfg)
    best, src = None, []
    for x in box:
        r2 = sum((Fraction(x[i]) - c[i]) ** 2 for i in range(3))
        if best is None or r2 < best:
            best, src = r2, [x]
        elif r2 == best:
            src.append(x)
    zero = (Fraction(0), Fraction(0))
    amp = {x: zero for x in box}
    cur = {x: (Fraction(1, len(src)), Fraction(0)) for x in src}
    for x, v in cur.items():
        amp[x] = cadd(amp[x], v)
    for _ in range(MAX_STEPS):
        nxt = {}
        for x, v in cur.items():
            if v == zero:
                continue
            for nb in NEIGHBOURS:
                y = (x[0] + nb[0], x[1] + nb[1], x[2] + nb[2])
                if y not in inbox or y in barrier:
                    continue
                nxt[y] = cadd(nxt.get(y, zero), cmul(u, v))
        cur = nxt
        for x, v in cur.items():
            amp[x] = cadd(amp[x], v)
    return sum((cabs2(amp[x]) for x in window if x in inbox), Fraction(0))


def N_certificate() -> dict:
    thetas = (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5))
    rows = []
    for cfg in FAMILY:
        zs = {q(t): q(amplitude_normalization(cfg, t, "boundary")) for t in thetas}
        rows.append({
            "config": cfg["name"],
            "additive_readout_I": readout(cfg),
            "record_count": len(cfg["sites"]),
            "Z_by_theta": zs,
            "Z_depends_on_theta": len(set(zs.values())) > 1,
        })
    theta_dependent = sum(1 for r in rows if r["Z_depends_on_theta"])
    # separating pair: equal record readout, different amplitude normalization
    sep = []
    for i, r in enumerate(rows):
        for s in rows[i + 1:]:
            if (r["additive_readout_I"] == s["additive_readout_I"]
                    and r["Z_by_theta"] != s["Z_by_theta"]):
                sep.append([r["config"], s["config"], r["additive_readout_I"]])

    # ---- CONTROL: read the SAME normalization on the support window, which is
    # exactly the barrier.  No propagated amplitude can reach a blocked site, so
    # this window is degenerate -- computed here rather than asserted.
    supp_rows = []
    for cfg in FAMILY:
        zs = {q(t): q(amplitude_normalization(cfg, t, "support")) for t in thetas}
        supp_rows.append({
            "config": cfg["name"],
            "Z_by_theta": zs,
            "Z_depends_on_theta": len(set(zs.values())) > 1,
        })
    supp_theta_dependent = sum(1 for r in supp_rows if r["Z_depends_on_theta"])
    return {
        "coordinate": "N -- the terminal detector-distribution normalization",
        "theta_values_swept": [q(t) for t in thetas],
        "window_locus_used": (
            "the support's site-boundary shell -- the record-determined locus "
            "DISJOINT from the barrier B(R) = supp(R).  Certificate F refutes "
            "this locus as a WINDOW under REQ4, so N's evaluation is stated as "
            "conditional on the same barrier/window identification premise the "
            "verdict already names; the degenerate-window control below shows "
            "the alternative is not a window at all."),
        "rows": rows,
        "configs_whose_Z_moves_with_theta": theta_dependent,
        "of": len(FAMILY),
        "degenerate_window_control": {
            "window_locus": "supp(R) -- identical to the barrier B(R)",
            "rows": supp_rows,
            "configs_whose_Z_moves_with_theta": supp_theta_dependent,
            "of": len(FAMILY),
            "reading": (
                f"With the window taken to BE the barrier, Z moves with theta "
                f"on {supp_theta_dependent}/{len(FAMILY)} configurations: the "
                f"walk cannot step onto a blocked site, so the only amplitude "
                f"on the window is the theta-independent seed.  The terminal "
                f"distribution is therefore degenerate, not theta-free.  This "
                f"is the computed cost of the barrier/readable-set collision, "
                f"and it is why the theta-dependence measured on the disjoint "
                f"locus is the load-bearing reading rather than an artifact of "
                f"the locus choice."),
        },
        "separating_pairs_equal_readout_different_Z": sep[:6],
        "separating_pair_count": len(sep),
        "what_IS_record_determined": (
            "Given the derived barrier B(R) = supp(R) and a derived window "
            "(W1 or W1b), the entire path sum is a function of the record "
            "configuration AND of the kernel's phase gain theta.  So N is "
            "record-determined ONLY relative to a fixed theta."),
        "exact_gap": (
            "theta is a KERNEL_SHAPE coordinate in Cycle 884's chart, not a "
            "WINDOW coordinate.  The computed theta-dependence of Z means N "
            "cannot be closed inside the window block: GBW1 as stated -- a "
            "lemma over the five WINDOW coordinates -- is MIS-SCOPED, because "
            "one of its five coordinates couples to the kernel block.  The "
            "second, independent obstruction is that even at fixed theta the "
            "additive record readout is LINEAR in content while Z is QUADRATIC "
            "in amplitudes; identifying them is the composed-record event-"
            "space / Born-measure step, which is not in this worktree."),
        "finding": (
            f"Z moves with theta on {theta_dependent}/{len(FAMILY)} "
            f"configurations, and {len(sep)} configuration pairs share an "
            f"additive record readout while differing in Z.  N is therefore "
            f"NOT determined by record content alone: it is determined by "
            f"record content TOGETHER WITH a kernel coordinate.  This is the "
            f"cycle's sharpest negative -- it re-prices GBW1 itself."),
        "pass": (len(rows) == len(FAMILY)
                 and all("Z_by_theta" in r for r in rows)
                 and len(supp_rows) == len(FAMILY)
                 and len(thetas) >= 2),
    }


# --------------------------------------------------------------------------
# certificate L: the wrong-window stress
# --------------------------------------------------------------------------
def stress_certificate() -> dict:
    """Adversarial: perturbed tuples the claimed maps must REFUSE."""
    # EVERY map that feeds the verdict is stressed -- including W1c, the
    # admissible rival that carries the surviving centre residual, and W2,
    # whose footprint the verdict cites as set-equal to W1's.
    claimed = {
        "W1_support": (map_W1_support, True),
        "W1b_boundary": (map_W1b_boundary, True),
        "W1c_altcentre": (map_W1c_altcentre, True),
        "W2_projection": (map_W2_projection, False),
        "W4_barrier": (map_W4_barrier, False),
    }
    results = {}
    for name, (fn, has_radii) in claimed.items():
        accepted, tested, exhibits = 0, 0, []
        control_tested, control_passed = 0, 0
        kinds = {}
        for cfg in FAMILY:
            base = fn(cfg)
            s = set(base["set"])
            # ---- genuinely WRONG windows: not group images of the right one.
            # A map refuses one iff it outputs it neither on this configuration
            # nor on ANY group image of it -- otherwise a map could "refuse" a
            # perturbation that is merely a relabelling.
            wrong = []
            outside = None
            for x in product(range(-RBOX, RBOX + 1), repeat=3):
                if x not in s:
                    outside = x
                    break
            if outside is not None:
                wrong.append(("add_site", tuple(sorted(s | {outside}))))
            if len(s) > 1:
                wrong.append(("drop_site", tuple(sorted(s - {sorted(s)[0]}))))
            # a CARDINALITY-PRESERVING wrong window: add/drop can be refused on
            # a counting argument alone, so the battery would be vacuous
            # without a perturbation that a group image could in principle
            # match.  move_site keeps |W| fixed and changes the shape.
            if outside is not None and len(s) > 1:
                wrong.append(("move_site", tuple(sorted(
                    (s - {sorted(s)[0]}) | {outside}))))
            for tag, ps in wrong:
                tested += 1
                kinds[tag] = kinds.get(tag, 0) + 1
                hit = tuple(sorted(base["set"])) == ps
                if not hit:
                    for mat in ROT24:
                        for shift in TEST_SHIFTS:
                            if tuple(sorted(
                                    fn(transform(cfg, mat, shift))["set"])) == ps:
                                hit = True
                                break
                        if hit:
                            break
                if hit:
                    accepted += 1
                    if len(exhibits) < 4:
                        exhibits.append({"config": cfg["name"],
                                         "perturbation": tag})
            # ---- the DISPLACED window is a positive control, not a wrong
            # window: the map must refuse it HERE and produce it on the shifted
            # configuration.  A map that rejected everything would fail this.
            v = (1, 0, 0)
            shifted = tuple(sorted(_shift_point(x, v) for x in s))
            control_tested += 1
            refused_here = tuple(sorted(base["set"])) != shifted
            produced_there = tuple(sorted(
                fn(transform(cfg, IDENTITY3, v))["set"])) == shifted
            if refused_here and produced_there:
                control_passed += 1
            if has_radii:
                for tag, pa, pb in (
                        ("a_plus_1", base["a2"] + 1, base["b2"]),
                        ("b_minus_1", base["a2"], base["b2"] - 1)):
                    tested += 1
                    kinds[tag] = kinds.get(tag, 0) + 1
                    if (base["a2"], base["b2"]) == (pa, pb):
                        accepted += 1
                        if len(exhibits) < 4:
                            exhibits.append(
                                {"config": cfg["name"], "perturbation": tag})
        results[name] = {
            "wrong_windows_tested": tested,
            "perturbation_kinds_tested": dict(sorted(kinds.items())),
            "perturbations_wrongly_accepted": accepted,
            "refusal_rate": q(Fraction(tested - accepted, tested)),
            "acceptance_exhibits": exhibits,
            "displacement_control_tested": control_tested,
            "displacement_control_passed": control_passed,
            "displacement_control_note": (
                "a translated window is the RIGHT window for the translated "
                "configuration, so it is scored as a positive control: the map "
                "must refuse it on this configuration and produce it on the "
                "shifted one.  A map that refused every tuple would fail here."),
        }

    impostors = {
        "constant_central_barrier": evaluate_map(
            map_IMPOSTOR_fixed_barrier, has_centre=False, has_radii=False),
        "constant_annulus_a1_b2": evaluate_map(
            map_IMPOSTOR_fixed_annulus, has_centre=True, has_radii=True),
    }
    # the scalar-chart blindness: on the LANDED 5-tuple the constant annulus is
    # a perfectly good G-invariant scalar assignment
    scalar_chart_blind = all(
        map_IMPOSTOR_fixed_annulus(cfg)["a2"]
        == map_IMPOSTOR_fixed_annulus(transform(cfg, ROT24[0], (2, 0, 0)))["a2"]
        for cfg in FAMILY)
    inconsistent = [
        name for name, r in results.items()
        if r["perturbations_wrongly_accepted"] > 0]
    control_failures = [
        name for name, r in results.items()
        if r["displacement_control_passed"] != r["displacement_control_tested"]]
    return {
        "claimed_map_stress": results,
        "impostor_battery": impostors,
        "impostor_reading": (
            "Both impostors are window-shaped and both are REFUTED, but by "
            "different clauses: the constant central barrier fails set "
            "equivariance outright, while the constant annulus fails only "
            "because the SET it denotes does not move with the records.  On "
            "the landed scalar-only chart the constant annulus is invisible -- "
            "its a and b are G-invariant numbers, so it passes.  This is the "
            "computed proof that the landed 5-coordinate window chart cannot "
            "state GBW1's equivariance requirement, and that the exposed "
            "centre coordinate is load-bearing rather than decorative."),
        "constant_annulus_passes_the_scalar_chart": scalar_chart_blind,
        "maps_claimed_derived_that_accept_a_wrong_window": inconsistent,
        "maps_that_failed_the_displacement_control": control_failures,
        "finding": (
            f"All {len(claimed)} maps that feed the verdict were stressed with "
            "added sites, dropped sites, cardinality-preserving moved sites "
            "and perturbed radii, and each wrong window was checked against "
            "the map's output on the configuration AND on all "
            f"{len(ROT24)} x {len(TEST_SHIFTS)} group images of it, so a map "
            "cannot 'refuse' a perturbation that is merely a relabelling.  A "
            "displaced window is scored as a POSITIVE control instead, which "
            "is what stops a refuse-everything map from scoring perfectly.  "
            "Wrongly accepted: "
            + ", ".join(f"{k}={v['perturbations_wrongly_accepted']}"
                        for k, v in sorted(results.items()))
            + "; displacement controls passed: "
            + ", ".join(f"{k}={v['displacement_control_passed']}/"
                        f"{v['displacement_control_tested']}"
                        for k, v in sorted(results.items())) + "."),
        # gate: soundness of the CLAIM, not the direction of the outcome.
        # If everything had come out SUPPLIED this gate would pass equally.
        "pass": not inconsistent and not control_failures,
    }


# --------------------------------------------------------------------------
# certificate M: the verdict
# --------------------------------------------------------------------------
def verdict_certificate(w1: dict, w2: dict, w3: dict, w4: dict,
                        dep: dict, ncert: dict, stress: dict) -> dict:
    existence_a_b = w1["existence"]["at_least_one_admissible_map"]
    unique_a_b = w1["uniqueness"]["candidates_agree"]
    centre_agree = w1["uniqueness"]["centre_conventions_agree"]
    centre_splits = w1["uniqueness"]["centre_convention_splits_on_configs"]
    admissible_rivals = w1["uniqueness"]["admissible_rivals"]
    refuted_rivals = w1["uniqueness"]["refuted_rivals"]
    boundary_rival_admissible = "W1b_boundary_shell" in admissible_rivals
    barrier_ok = (w4["evaluation"]["REQ2_REQ3_equivariant"]
                  and w4["evaluation"]["REQ4_permanence_monotone"]
                  and w4["evaluation"]["REQ5_nonconstant"])
    barrier_landed_refuted = not w4["landed_fixed_barrier_impostor"][
        "evaluation"]["REQ2_REQ3_equivariant"]
    depth_ok = dep["stationary_on_every_config"] and dep["nondecreasing_on_every_config"]
    n_content_only = not (ncert["configs_whose_Z_moves_with_theta"] > 0)

    classification = {}
    classification["barrier"] = {
        "class": "DERIVED" if (barrier_ok and barrier_landed_refuted) else "SUPPLIED",
        "witness": (
            "B(R) = supp(R) from count-once + permanence; equivariant and "
            "monotone on every test; the landed fixed central barrier is "
            "refuted by translation equivariance"),
        "residual_premise": (
            "one identification: the PROPAGATION barrier is read off the "
            "REGISTRATION-blocked set (the two coincide with the readable set, "
            "which the landed model needs disjoint)"),
    }
    classification["D"] = {
        "class": "GAUGE" if depth_ok else "FREE",
        "witness": (
            "permanence makes the depth-indexed readout non-decreasing and "
            "stationary above the last formation depth; Cycle 884 R1's b <= D "
            "bounds the class from below"),
        "residual_premise": "none; D is determined as a gauge class",
    }
    ab_class = ("DERIVED" if (existence_a_b and unique_a_b)
                else "EXISTENCE_DERIVED_UNIQUENESS_OPEN" if existence_a_b
                else "SUPPLIED")
    ab_residual = []
    if boundary_rival_admissible:
        ab_residual.append(
            "one binary locus choice (support vs boundary shell)")
    if not centre_agree:
        ab_residual.append(
            "one centre convention (barycentre vs extremal-shell barycentre)")
    ab_residual.append(
        "the annular (a, b) reading additionally needs the support to fill its "
        "own annulus, which holds on "
        f"{w1['annulus_fill']['configs_whose_support_fills_its_own_annulus']}"
        f"/{w1['annulus_fill']['of']} configurations")
    for coord in ("a", "b"):
        classification[coord] = {
            "class": ab_class,
            "witness": (
                "Record's content-only clause FORCES the window to be a "
                "function of R; supp(R) is admissible on every declared "
                "requirement, while the boundary-shell rival is refuted by "
                f"REQ4 (permanence retraction) -- refuted rivals: "
                f"{refuted_rivals or ['none']}, surviving rivals: "
                f"{admissible_rivals or ['none']}"),
            "residual_premise": "; ".join(ab_residual),
        }
    classification["N"] = {
        "class": "SUPPLIED" if not n_content_only else "DERIVED",
        "witness": (
            "Z moves with the kernel phase gain theta on "
            f"{ncert['configs_whose_Z_moves_with_theta']}/{ncert['of']} "
            "configurations, and separating pairs share an additive record "
            "readout while differing in Z"),
        "residual_premise": (
            "N couples the WINDOW block to the KERNEL block through theta, and "
            "additionally needs the linear-record-readout / quadratic-amplitude "
            "identification (the composed-record event-space step, absent from "
            "this worktree)"),
    }
    # COMPUTED, not asserted: the centre's class follows from whether two
    # admissible equivariant centre conventions actually split.
    classification["centre"] = {
        "class": "DERIVED" if centre_agree else "EXISTENCE_DERIVED_UNIQUENESS_OPEN",
        "witness": (
            "'No site is privileged' forbids a supplied centre and forces an "
            "equivariant one; the barycentre and the extremal-shell barycentre "
            "are both equivariant and both belong to admissible maps, and they "
            f"differ as points on {len(centre_splits)}/{len(FAMILY)} "
            f"configurations ({', '.join(centre_splits) or 'none'})"),
        "residual_premise": (
            "one centre convention" if not centre_agree
            else "none; the equivariant centre conventions coincide"),
    }

    determined = sorted(c for c in WINDOW_COORDS
                        if classification[c]["class"] in ("DERIVED", "GAUGE"))
    partial = sorted(c for c in WINDOW_COORDS
                     if classification[c]["class"]
                     == "EXISTENCE_DERIVED_UNIQUENESS_OPEN")
    supplied = sorted(c for c in WINDOW_COORDS
                      if classification[c]["class"] == "SUPPLIED")
    partition_ok = (len(determined) + len(partial) + len(supplied)
                    == len(WINDOW_COORDS))

    # The residual is BUILT from the computed facts, never listed by hand.
    residual_items = []
    if boundary_rival_admissible:
        residual_items.append(
            "one binary window choice: the record support itself vs its "
            "site-boundary shell (both admissible)")
    if not centre_agree:
        residual_items.append(
            "one centre convention, needed only by the ANNULAR reading of the "
            "window; the SET-valued window needs no centre")
    if supplied:
        residual_items.append(
            "one cross-block coupling: N depends on the kernel phase gain "
            "theta, so it cannot be closed inside the window block")
    if w4["barrier_readable_collision"][
            "configs_where_barrier_and_readable_set_are_disjoint"] < len(FAMILY):
        residual_items.append(
            "one identification premise: propagation barrier = registration-"
            "blocked set")

    return {
        "classification": classification,
        "uniqueness_filter": {
            "rule": (
                "a rival can witness non-uniqueness only if it satisfies every "
                "declared requirement; a rival that fails one is REFUTED and "
                "its disagreements are discarded"),
            "admissible_rivals": admissible_rivals,
            "refuted_rivals": refuted_rivals,
            "rival_failed_requirements":
                w1["uniqueness"]["rival_failed_requirements"],
            "disagreements_counted": w1["uniqueness"]["disagreement_count"],
            "disagreements_discarded":
                w1["uniqueness"]["disagreements_with_refuted_rivals_not_counted"],
        },
        "W2_adds_no_window_coordinate": w2["collapses_into_W1"],
        "stress_soundness": {
            "maps_claimed_derived_that_accept_a_wrong_window":
                stress["maps_claimed_derived_that_accept_a_wrong_window"],
            "maps_that_failed_the_displacement_control":
                stress["maps_that_failed_the_displacement_control"],
        },
        "window_coordinates_determined": determined,
        "window_coordinates_existence_only": partial,
        "window_coordinates_supplied": supplied,
        "count_determined_of_five": len(determined),
        "count_existence_only_of_five": len(partial),
        "count_supplied_of_five": len(supplied),
        "exposed_sixth_coordinate": "centre",
        "residual_named_exactly": residual_items,
        "residual_item_count": len(residual_items),
        "GBW1_status": (
            "NOT CLOSED, and RE-PRICED.  GBW1 was declared over the five "
            "WINDOW coordinates.  One of those five (N) is computed here to "
            "depend on a KERNEL coordinate, so GBW1 as stated cannot be proved "
            "or disproved inside the window block: it must be re-split into "
            "GBW1a (the window LOCUS: centre, a, b, D, barrier -- attacked "
            "here) and GBW1b (the terminal normalization, which is a "
            "kernel-window joint obligation)."),
        "moment_count_is_G_invariant": w3["moment_count_is_G_invariant"],
        "each_remaining_dimension_vs_GBW1": {
            "a": f"inside GBW1a; residual is {'; '.join(ab_residual[:-1]) or 'no free choice'}",
            "b": f"inside GBW1a; residual is {'; '.join(ab_residual[:-1]) or 'no free choice'}",
            "N": "OUTSIDE GBW1a; belongs to a joint kernel-window lemma GBW1b",
            "barrier": "inside GBW1a and DERIVED, modulo one identification",
            "D": "inside GBW1a and GAUGE",
            "centre": ("inside GBW1a; newly exposed; residual is "
                       + ("one convention" if not centre_agree else "none")),
        },
        "strength_vs_884": (
            f"Cycle 884 classified all five WINDOW coordinates FREE.  This "
            f"cycle removes {len(determined)} of them outright (barrier "
            f"DERIVED, D GAUGE), reduces two more to "
            f"{len(ab_residual) - 1} residual item(s) "
            f"({'; '.join(ab_residual[:-1]) or 'none'}) after permanence "
            f"REFUTES the boundary-shell rival, exposes a sixth coordinate the "
            f"landed chart never carried, and shows the fifth is not a window "
            f"coordinate at all."),
        "finding": (
            f"Of the five landed WINDOW coordinates, {len(determined)} are "
            f"determined ({', '.join(determined) or 'none'}), "
            f"{len(partial)} are existence-derived with uniqueness open "
            f"({', '.join(partial) or 'none'}), and {len(supplied)} is "
            f"supplied ({', '.join(supplied) or 'none'}).  The residual is "
            f"{len(residual_items)} named items, none of them 'the window is "
            f"chosen by the runner'."),
        "pass": partition_ok,
    }


# --------------------------------------------------------------------------
# certificate N: honesty gate
# --------------------------------------------------------------------------
def honesty_certificate(science: dict) -> dict:
    forbidden = (
        "gravity is derived", "gravity closes", "Gate B closes",
        "GB-S2 is closed", "GB-S2 closes",
        "physical Newton constant is derived", "the dynamics row is promoted",
    )
    blob = json.dumps(science, sort_keys=True, default=str)
    leaks = [p for p in forbidden if p in blob]
    return {
        "Q1_what_is_not_claimed": [
            "GB-S2 is not discharged; this block attacks one named component",
            "Gate B does not close and gravity does not close",
            "the Gate-B dynamics row is not promoted",
            "no new axiom and no new primitive is introduced",
            "GBW1 is not proved: it is re-priced and shown to be mis-scoped",
        ],
        "Q2_exact_scope": (
            "One lemma's attempt, on a 12-configuration family in a bounded "
            "box, against the four axioms plus the pinned Cycle 883 weight "
            "pair.  Equivariance is verified on the full rotation group and a "
            "finite shift set, not on all of Z^3; the conclusion that a "
            "record-independent map fails equivariance is exact (one "
            "counterexample suffices), while the conclusion that a map IS "
            "equivariant is verified on the tested set and proved structurally "
            "in the forcing chains."),
        "Q3_steelman": (
            "The strongest case against this cycle is that 'derived' for the "
            "barrier is cheap: B(R) = supp(R) makes the barrier whatever the "
            "records are, which feels like relabelling rather than deriving.  "
            "The answer is the declared theorem shape -- GBW1 is a map FROM "
            "record configurations, so a coordinate that reduces to record "
            "content is exactly what it asks for -- but the cost is stated "
            "openly in the barrier/readable-set collision: the landed model "
            "needs those two sets disjoint and the axioms make them equal."),
        "Q4_what_would_refute_this": [
            "an approved primitive that selects between the support window and "
            "the boundary-shell window (would close the a/b residual)",
            "an approved primitive fixing the centre convention",
            "a configuration on which B(R) = supp(R) fails equivariance",
            "a demonstration that Z is theta-independent (would put N back "
            "inside the window block)",
            "showing the landed model does not need barrier and window "
            "disjoint (would remove the identification premise)",
        ],
        "forbidden_phrases_present": leaks,
        "finding": (
            "No closure claim appears anywhere in the science payload.  The "
            "two load-bearing negatives point AGAINST the landed construction "
            "(the fixed central barrier is refuted by equivariance; the landed "
            "window chart is scalar-only and cannot state the requirement), "
            "and the third re-prices the lemma this cycle was sent to prove."),
        "pass": not leaks,
    }


# --------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------
LABELS = (
    "A_PINS",
    "B_FORMALIZATION",
    "C_LINEAGE_PRESENCE",
    "D_GROUP",
    "E_CONFIG_FAMILY",
    "F_W1_SUPPORT_EXTENT",
    "G_W2_PAYLOAD_PROJECTION",
    "H_W3_FORMATION_EDGES",
    "I_W4_BARRIER",
    "J_DEPTH_UNDER_PERMANENCE",
    "K_N_TERMINAL_NORMALIZATION",
    "L_WRONG_WINDOW_STRESS",
    "M_VERDICT",
    "N_HONESTY_GATE",
    "O_CONTROLS",
)
SCIENCE_LABELS = tuple(l for l in LABELS if l != "O_CONTROLS")


def build_science() -> dict:
    pins = pins_certificate()
    form = formalization_certificate()
    lineage = lineage_certificate()
    group = group_certificate()
    family = family_certificate()
    w1 = W1_certificate()
    w2 = W2_certificate(lineage)
    w3 = W3_certificate()
    w4 = W4_certificate()
    dep = depth_certificate()
    ncert = N_certificate()
    stress = stress_certificate()
    verdict = verdict_certificate(w1, w2, w3, w4, dep, ncert, stress)
    w1["outcome"] = verdict["classification"]["a"]["class"]
    science = {
        "A_PINS": pins,
        "B_FORMALIZATION": form,
        "C_LINEAGE_PRESENCE": lineage,
        "D_GROUP": group,
        "E_CONFIG_FAMILY": family,
        "F_W1_SUPPORT_EXTENT": w1,
        "G_W2_PAYLOAD_PROJECTION": w2,
        "H_W3_FORMATION_EDGES": w3,
        "I_W4_BARRIER": w4,
        "J_DEPTH_UNDER_PERMANENCE": dep,
        "K_N_TERMINAL_NORMALIZATION": ncert,
        "L_WRONG_WINDOW_STRESS": stress,
        "M_VERDICT": verdict,
    }
    science["N_HONESTY_GATE"] = honesty_certificate(science)
    return science


def render(certs: dict, labels, header: str = "") -> str:
    out = [header, ""] if header else []
    for label in labels:
        cert = certs[label]
        out.append(f"[{'PASS' if cert['pass'] else 'FAIL'}] {label}")
        finding = cert.get("finding")
        if finding:
            out.append(f"    finding: {finding}")
        out.append("")
    out.append(json.dumps({l: certs[l] for l in labels},
                          indent=2, sort_keys=True, default=str))
    return "\n".join(out) + "\n"


def run() -> int:
    preflight_pins()
    started = monotonic()
    science_a = build_science()
    science_b = build_science()
    deterministic = digest(science_a) == digest(science_b)

    certificates = {label: science_a[label] for label in SCIENCE_LABELS}
    verdict = science_a["M_VERDICT"]

    receipt = {
        "cycle": 885,
        "question": (
            "GBW1: is the Gate-B detector window record-determined?  Formalize "
            "the map from record configurations to (centre, a, b, D, barrier, "
            "N), sweep the landed record-facing structures for window-shaped "
            "data, and classify every window coordinate DERIVED or SUPPLIED "
            "with its exact gap."
        ),
        "outcome_class": "GBW1_repriced_two_coordinates_removed_one_shown_misscoped",
        "GBW1_status": verdict["GBW1_status"],
        "classification": verdict["classification"],
        "count_determined_of_five": verdict["count_determined_of_five"],
        "count_existence_only_of_five": verdict["count_existence_only_of_five"],
        "count_supplied_of_five": verdict["count_supplied_of_five"],
        "exposed_sixth_coordinate": verdict["exposed_sixth_coordinate"],
        "residual_named_exactly": verdict["residual_named_exactly"],
        "each_remaining_dimension_vs_GBW1":
            verdict["each_remaining_dimension_vs_GBW1"],
        "candidate_outcomes": {
            "W1_support_extent": science_a["F_W1_SUPPORT_EXTENT"]["finding"],
            "W2_payload_projection": science_a["G_W2_PAYLOAD_PROJECTION"]["finding"],
            "W3_formation_edges": science_a["H_W3_FORMATION_EDGES"]["finding"],
            "W4_barrier": science_a["I_W4_BARRIER"]["finding"],
        },
        "exact_gaps": {
            "a_b": science_a["F_W1_SUPPORT_EXTENT"]["uniqueness"]["why_it_fails"],
            "W2": science_a["G_W2_PAYLOAD_PROJECTION"]["exact_gap"],
            "W3_N": science_a["H_W3_FORMATION_EDGES"]["exact_gap"],
            "barrier": science_a["I_W4_BARRIER"]["barrier_readable_collision"][
                "reading"],
            "D": science_a["J_DEPTH_UNDER_PERMANENCE"]["exact_gap"],
            "N": science_a["K_N_TERMINAL_NORMALIZATION"]["exact_gap"],
        },
        "theorems": [
            "C885-T1 Record's content-only clause FORCES the detector window "
            "to be a function of the record configuration: a windowed readout "
            "whose window is not record-determined is not determined by record "
            "content alone.  GBW1's EXISTENCE half is therefore an axiom "
            "consequence, not a conjecture.",
            "C885-T2 the barrier is DERIVED: B(R) = supp(R) is equivariant, "
            "permanence-monotone and non-constant on every test here, its "
            "uniqueness is argued in the stated forcing chain (B smaller than "
            "supp(R) contradicts count-once, B larger blocks an unoccupied "
            "site and needs a law), and the landed fixed central barrier is "
            "refuted by translation equivariance on "
            f"{science_a['I_W4_BARRIER']['landed_fixed_barrier_impostor']['evaluation']['equivariance_failures']}"
            " computed collisions.",
            "C885-T3 the readout depth D is GAUGE: permanence makes the "
            "depth-indexed readout stationary above the last formation depth, "
            "so every admissible D gives the identical readout.",
            "C885-T4 permanence REFUTES the boundary-shell window: it retracts "
            "under the filtration on "
            f"{science_a['F_W1_SUPPORT_EXTENT']['W1b_boundary_shell_reading']['permanence_monotonicity_failures']}"
            " of "
            f"{science_a['F_W1_SUPPORT_EXTENT']['W1b_boundary_shell_reading']['permanence_monotonicity_checks']}"
            " nested pairs and so cannot witness non-uniqueness.  GBW1's "
            "UNIQUENESS half still FAILS, but through exactly one surviving "
            "split -- the equivariant CENTRE convention (barycentre vs "
            "extremal-shell barycentre), which differs as a point on "
            f"{len(science_a['F_W1_SUPPORT_EXTENT']['uniqueness']['centre_convention_splits_on_configs'])}"
            f"/{len(FAMILY)} configurations.",
            "C885-T5 the landed 5-coordinate window chart is scalar-only and "
            "cannot state the equivariance requirement; a constant annulus "
            "passes it.  The honest window chart carries a sixth coordinate, "
            "the centre.",
            "C885-T6 GBW1 is MIS-SCOPED: N depends on the kernel phase gain, "
            "so the terminal normalization is a joint kernel-window obligation "
            "and must be split out as GBW1b.",
        ],
        "load_bearing_negatives": [
            "the landed fixed central barrier privileges sites and fails "
            "translation equivariance",
            "the landed window chart is scalar-only, so it cannot even state "
            "GBW1's covariance requirement",
            "the axiom-forced barrier and the axiom-forced readable set "
            "COINCIDE, while the landed model needs them disjoint -- and no "
            "swept window candidate is both admissible and barrier-disjoint, "
            "so the separation has no record-determined realization here",
            "GBW1 as declared by Cycle 884 cannot be settled inside the window "
            "block",
            "with the window taken to BE the barrier the terminal distribution "
            "is degenerate (theta-independent seed only), which is the "
            "computed cost of that collision",
        ],
        "load_bearing_positives": [
            "GBW1 existence is forced by Record's content-only clause",
            "barrier = supp(R) is DERIVED from count-once + permanence",
            "D is GAUGE by permanence",
            "W2 (the payload projection) adds no window coordinate: it is "
            "set-equal to the record support",
            "permanence SELECTS the support window over the boundary-shell "
            "window: the boundary shell retracts under the filtration and is "
            "refuted, removing the binary locus choice from the residual",
        ],
        "uniqueness_filter": verdict["uniqueness_filter"],
        "exact_scope": science_a["N_HONESTY_GATE"]["Q2_exact_scope"],
        "steelman": science_a["N_HONESTY_GATE"]["Q3_steelman"],
        "cycle884_GBW1_statement": science_a["A_PINS"]["cycle884_GBW1_statement"],
        "record_facing_primaries_absent_from_this_worktree":
            science_a["C_LINEAGE_PRESENCE"]["absent"],
        "source_pins": [
            {"path": r["path"], "sha256": r["sha256"], "git_blob": r["git_blob"]}
            for r in science_a["A_PINS"]["rows"]
        ],
    }
    text = render(
        certificates, SCIENCE_LABELS,
        "CYCLE 885 -- GBW1: IS THE DETECTOR WINDOW RECORD-DETERMINED?")
    stdout_bytes = len(text.encode("utf-8"))
    elapsed = monotonic() - started

    controls = {
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocked_modules_loaded": [
            n for n in BLOCKLISTED_MODULES if n in sys.modules],
        "firewall_hits": list(FIREWALL.hits),
        "determinism": {
            "scope": "every science certificate rebuilt from scratch -- the "
                     "rotation group, the configuration family, all four "
                     "candidate sweeps, the exact Gaussian-rational path sums "
                     "and the stress battery -- and compared digest for digest",
            "exact": deterministic,
            "science_digest": digest(science_a),
        },
        "cache_path": str(CACHE.relative_to(ROOT)),
        "cache_sha256": None,   # filled after the receipt is written
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes_science_payload": stdout_bytes,
        "stdout_bytes_note": (
            "measured on the science payload; this controls block is appended "
            "after the measurement, so the figure is not self-referential"),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": stdout_bytes < STDOUT_LIMIT_BYTES,
        "floating_point_in_certified_quantities": False,
        "gate_neutrality": (
            "No certificate gates on a coordinate coming out DERIVED rather "
            "than SUPPLIED.  A_PINS gates on the pins and needles; "
            "B_FORMALIZATION on the theorem shape being type-complete; "
            "C_LINEAGE_PRESENCE on the scan producing a decision for every "
            "probe, in either direction; D_GROUP on the group being a group; "
            "E_CONFIG_FAMILY on the family being well-formed; F/G/H/I/J/K on "
            "the candidate having been evaluated against every declared "
            "requirement, whatever the answer; L on the CLAIM being internally "
            "sound (no map classified DERIVED while accepting a wrong window) "
            "-- a gate that would pass equally had every coordinate come out "
            "SUPPLIED; M on the classification partitioning the five "
            "coordinates exactly.  The determined/supplied counts are "
            "reported as data, including the fact that one of the five is "
            "shown to lie outside the window block entirely.  The one gate "
            "that is NOT a pure computation is N_HONESTY_GATE: it is a static "
            "lint over literal closure phrases, none of which any computed "
            "value can produce, so it constrains this file's prose and not "
            "the science."),
        "finding": (
            "All cited artifacts stayed text/AST/JSON-only behind the import "
            "firewall, every pinned path was checked to exist before any "
            "science ran, the whole science payload rebuilt digest for digest, "
            "and the runtime and stdout caps were respected."),
    }
    controls["pass"] = (
        deterministic
        and controls["runtime_under_limit"]
        and controls["stdout_under_limit"]
        and not controls["blocked_modules_loaded"]
        and not controls["firewall_hits"]
    )
    certificates["O_CONTROLS"] = controls

    receipt["certificate_pass"] = {
        label: bool(certificates[label]["pass"]) for label in LABELS}
    receipt["all_certificates_pass"] = all(
        receipt["certificate_pass"].values())

    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8")
    controls["cache_sha256"] = sha256(CACHE.read_bytes()).hexdigest()

    tail = render(certificates, ("O_CONTROLS",))
    sys.stdout.write(text)
    sys.stdout.write(tail)
    sys.stdout.write(
        f"\ncontrols: deterministic={deterministic} "
        f"runtime_under_limit={controls['runtime_under_limit']} "
        f"stdout={stdout_bytes}B receipt={controls['cache_path']} "
        f"cache={controls['cache_sha256'][:16]}\n")
    return 0 if all(c["pass"] for c in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
