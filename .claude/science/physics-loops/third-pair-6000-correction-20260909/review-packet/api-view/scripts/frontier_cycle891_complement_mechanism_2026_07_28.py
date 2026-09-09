#!/usr/bin/env python3
"""Cycle-891 bank/edge identity algebra and the cyclic k-run alignment law
(self-contained).

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
runner consumed Cycle-879/881/889 artifacts that are not landed on
origin/main and are absent from this tree (its own preflight hard-failed
here), and described its derive/holdout split as "SEALED" although the seal
was an in-process digest computed at runtime from the final rule source in
the same reviewed file -- an execution-order guard, not a cryptographically
sealed or blind holdout.  Per the review findings:

- the input closure is now EMPTY: the unlanded corpus lineage is provenance
  context only, and the recorded holdout story (B=6/7 predictions, the
  P=32 carrier miss, the incidence tables) is stipulated history that
  certifies nothing here;
- the retained claims are the reviewer-verified bounded cores, recomputed
  from scratch in this file:

L1  BANK/EDGE IDENTITY ALGEBRA (exact, exhaustive over B = 3..8 and all
    valid e): N = 8B - 5;  DELTA = 8B - 13 - 8e;  N - DELTA = 8(e + 1);
    b = B - 2 - e;  entry gap 8(B - 1 - b) = 8(e + 1) = N - DELTA.

L2  THE CYCLIC K-RUN ALIGNMENT LAW (exact, randomized against a literal
    ground truth): for a cyclic word of length N with dirty residue set W
    and period P, the longest run of positions i with
    dirt(i) == dirt(i + P) equals (max cyclic gap of W symdiff (W - P))
    - 1, with the empty and single-element edge cases handled (all-good
    -> N; one mismatch -> N - 1).  A perturbation control (the same
    formula with -2) must break.

Fail-closed: every certificate binds `pass` to the predicate it names.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000

from hashlib import sha256
import json
from pathlib import Path
import random
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def l1_identities() -> dict:
    rows, ok = [], True
    for B in range(3, 9):
        N = 8 * B - 5
        for e in range(0, B - 1):
            delta = 8 * B - 13 - 8 * e
            b = B - 2 - e
            entry_gap = 8 * (B - 1 - b)
            good = (N - delta == 8 * (e + 1)
                    and entry_gap == 8 * (e + 1)
                    and entry_gap == N - delta
                    and 0 <= b <= B - 2
                    and delta >= 3)
            ok &= good
            rows.append({"B": B, "N": N, "e": e, "delta": delta, "b": b,
                         "entry_gap": entry_gap, "identities_hold": good})
    check("L1_BANK_EDGE_IDENTITIES", ok,
          f"rows={len(rows)} all_identities_hold={ok} "
          f"(exhaustive over B=3..8, e=0..B-2)")
    return {"rows": rows, "all_hold": ok}


def literal_longest_good_run(N: int, W: set[int], P: int) -> int:
    good = [((i in W) == (((i + P) % N) in W)) for i in range(N)]
    if all(good):
        return N
    # longest cyclic run of consecutive True
    doubled = good + good
    best = run = 0
    for g in doubled:
        run = run + 1 if g else 0
        best = max(best, run)
    return min(best, N)


def law_longest_good_run(N: int, W: set[int], P: int) -> int:
    shifted = {(w - P) % N for w in W}
    M = sorted(W ^ shifted)
    if not M:
        return N
    if len(M) == 1:
        return N - 1
    gaps = [b - a for a, b in zip(M, M[1:])]
    gaps.append(N - M[-1] + M[0])
    return max(gaps) - 1


def l2_krun_law(rng: random.Random) -> dict:
    cells, mismatches = 0, 0
    control_breaks = 0
    control_cells = 0
    for _ in range(3000):
        N = rng.randint(6, 40)
        density = rng.random()
        W = {i for i in range(N) if rng.random() < density}
        P = rng.randint(1, N - 1)
        truth = literal_longest_good_run(N, W, P)
        law = law_longest_good_run(N, W, P)
        cells += 1
        if truth != law:
            mismatches += 1
        # perturbation control: the -2 variant must break whenever the
        # mismatch set is non-empty and non-degenerate
        shifted = {(w - P) % N for w in W}
        if len(W ^ shifted) >= 2:
            control_cells += 1
            if law - 1 != truth:
                control_breaks += 1
    edge_all_good = literal_longest_good_run(12, set(), 5) == 12 \
        and law_longest_good_run(12, set(), 5) == 12
    # parity fact: W and (W - P) have equal cardinality, so the mismatch
    # set W symdiff (W - P) always has EVEN size -- the |M| = 1 branch of
    # the law is defensively present but unreachable.  Verify the parity
    # on a fresh randomized sweep.
    parity_ok = True
    for _ in range(500):
        N = rng.randint(6, 40)
        W = {i for i in range(N) if rng.random() < rng.random()}
        P = rng.randint(1, N - 1)
        shifted = {(w - P) % N for w in W}
        if len(W ^ shifted) % 2 != 0:
            parity_ok = False
    ok = (cells == 3000 and mismatches == 0 and edge_all_good
          and control_cells > 0 and control_breaks == control_cells
          and parity_ok)
    check("L2_KRUN_ALIGNMENT_LAW", ok,
          f"random_cells={cells} mismatches={mismatches} "
          f"all_good_edge_case={edge_all_good} mismatch_set_always_even="
          f"{parity_ok} "
          f"perturbation_control_breaks={control_breaks}/{control_cells}")
    return {"random_cells": cells, "mismatches": mismatches,
            "control_breaks": control_breaks,
            "control_cells": control_cells}


def run_all(seed: int) -> dict:
    rng = random.Random(seed)
    a = l1_identities()
    b = l2_krun_law(rng)
    return {"l1": {"all_hold": a["all_hold"], "rows": len(a["rows"])},
            "l2": b,
            "science_digest": digest([a["rows"], b])}


def main() -> int:
    t0 = monotonic()
    first = run_all(891)
    saved = list(CERTS)
    CERTS.clear()
    second = run_all(891)
    CERTS.clear()
    CERTS.extend(saved)
    det = first["science_digest"] == second["science_digest"]
    check("L3_DETERMINISM", det, f"double_run_digest_equal={det}")
    elapsed = monotonic() - t0
    check("L4_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 891 -- BANK/EDGE IDENTITY ALGEBRA AND THE CYCLIC K-RUN LAW")
    w("=" * 78)
    w("")
    w("SCOPE: self-contained.  The unlanded Cycle-879/881/889 corpus lineage")
    w("is provenance context only.  The historical derive/holdout story is")
    w("recorded history: its runtime digest was an in-process execution-order")
    w("guard, not a cryptographically sealed or blind holdout, and none of")
    w("its predictions are certified by this package.")
    w("")
    w("CLAIMS_JSON: " + compact({
        "identity_rows": first["l1"]["rows"],
        "identities_all_hold": first["l1"]["all_hold"],
        "krun_cells": first["l2"]["random_cells"],
        "krun_mismatches": first["l2"]["mismatches"],
        "control_breaks": first["l2"]["control_breaks"],
        "control_cells": first["l2"]["control_cells"],
        "science_digest": first["science_digest"],
    }))
    w("")
    w("-- CERTIFICATES --------------------------------------------------------")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<28} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    w(f"VERDICT: {'PASS' if nfail == 0 else 'FAIL'}")
    text = "\n".join(out)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 891,
        "claim_type": "bounded_theorem",
        "headline": ("bank/edge identity algebra (N = 8B - 5, "
                     "DELTA = 8B - 13 - 8e, N - DELTA = entry gap = "
                     "8(e + 1); exhaustive over B = 3..8) and the cyclic "
                     "k-run alignment law verified against a literal ground "
                     "truth with a breaking perturbation control.  The "
                     "historical holdout story is recorded, uncertified "
                     "history with an in-process order guard, not a sealed "
                     "blind holdout"),
        "stipulated_scope_inputs": {
            "bank_range": "B = 3..8, e = 0..B-2 (declared sweep)",
            "krun_cell_family": "random cyclic words, N = 6..40 (declared)",
        },
        "provenance_context_non_load_bearing": (
            "the Cycle-879/881/889 corpus artifacts are unlanded and absent "
            "from this tree; the recorded transport anatomy, incidence "
            "tables, co-occurrence counts, B=6/7 predictions and the P=32 "
            "carrier miss are recorded history from that uncertified "
            "computation and certify nothing here"),
        "results": first,
        "certificates": {n: {"pass": ok, "detail": d} for n, ok, d in CERTS},
        "all_certificates_pass": nfail == 0,
        "review_loop": {
            "iteration": 1,
            "disposition": "FIX_THEN_PROCEED",
            "reviewer": "Sol",
            "date": "2026-08-08",
            "fix": ("self-contained rewrite: unlanded closure removed; "
                    "'sealed holdout' language replaced by in-process order "
                    "guard; bounded identity/law cores recomputed from "
                    "scratch with fail-closed certificates"),
        },
        "science_digest": first["science_digest"],
    }
    (ROOT / "outputs" /
     "complement_mechanism_cycle891_receipt_2026_07_28.json").write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
