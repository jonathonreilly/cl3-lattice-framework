#!/usr/bin/env python3
"""Independent finite check of the corrected Cycle-930 station/detector result.

The checker never imports or executes the primary. It pins the primary source
and fresh cache, reads only the compact CLAIMS_JSON interface, then recomputes
station shifts by direct modular enumeration, detector outcomes by literal bit
lists, complete periodic-run translations by interval maps, and the widening
witness by an explicit ordered-start test.

The check covers the corrected finite constructions only. It does not execute
or validate the historical controller corpus or confer a physical meaning on
station ordinals, tick indices, masks, or detector readings.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 30
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py",
    "logs/runner-cache/frontier_cycle930_third_pair_rc3_2026_07_28.txt",
)

from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE = AUDIT_INPUT_PATHS
RECEIPT_REL = "outputs/third_pair_rc3_independent_check_cycle930_receipt_2026_07_28.json"

# Replaced by a pin-only edit after the frozen primary's single bounded run.
EXPECTED_SHA256 = {
    PRIMARY_PATH: "7c87b96a8b0367d36258f3a275856fbcc2a17533900c2d6ec7bf446c12aea2c5",
    PRIMARY_CACHE: "5af28199dffa2a1e1b6cbcb689d5e37c11fd9cedacf4e0e1524accaa12fb3385",
}
CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    CERTS.append((name, bool(ok), detail))
    print(f"{'PASS' if ok else 'FAIL'} {name} :: {detail}")
    return bool(ok)


def file_sha256(relative: str) -> str | None:
    path = ROOT / relative
    return sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def parse_claims(cache_body: bytes) -> dict[str, object] | None:
    for line in cache_body.decode("utf-8", errors="replace").splitlines():
        if line.startswith("CLAIMS_JSON: "):
            value = json.loads(line[len("CLAIMS_JSON: "):])
            return value if isinstance(value, dict) else None
    return None


def independent_station_result() -> dict[str, object]:
    expected_general = {
        ("f(b-1)", "r(b)"),
        ("hf(b)", "r(b-1)"),
        ("f(b)", "hr(b-1)"),
    }
    disagreements: list[dict[str, object]] = []
    cells = 0
    odd_exceptions = 0
    even_exceptions = 0
    for bank_count in range(3, 25):
        for bank in range(1, bank_count - 1):
            cells += 1
            modulus = 8 * bank_count - 5
            period = 8 * (bank_count - 1 - bank)
            rows = {
                "hf(b-1)": 5 * bank - 3,
                "f(b-1)": 5 * bank - 1,
                "hf(b)": 5 * bank + 2,
                "f(b)": 5 * bank + 4,
                "r(b)": 8 * bank_count - 9 - 3 * bank,
                "hr(b)": 8 * bank_count - 7 - 3 * bank,
                "r(b-1)": 8 * bank_count - 6 - 3 * bank,
                "hr(b-1)": 8 * bank_count - 4 - 3 * bank,
            }
            order = tuple(rows)
            values = list(rows.values())
            gaps = [
                (values[(index + 1) % 8] - values[index]) % modulus
                for index in range(8)
            ]
            expected_gaps = [2, 3, 2, 8 * (bank_count - bank) - 13,
                             2, 1, 2, 8 * bank - 4]
            mappings = {
                (source, target)
                for source, x in rows.items()
                for target, y in rows.items()
                if (x + period) % modulus == y
            }
            expected = set(expected_general)
            if bank == (bank_count - 1) // 2:
                if bank_count % 2:
                    expected.add(("r(b-1)", "f(b-1)"))
                    odd_exceptions += 1
                else:
                    expected.add(("r(b)", "f(b)"))
                    even_exceptions += 1
            terminals = (rows["r(b)"], rows["hr(b-1)"], rows["r(b-1)"])
            firsts = (rows["f(b-1)"], rows["f(b)"], rows["hf(b)"])
            rowset = set(values)
            predicates = {
                "ordered": values == sorted(set(values)),
                "gaps": gaps == expected_gaps,
                "variable_bounds": gaps[3] >= 3 and gaps[7] >= 4,
                "sole_unit_gap": gaps.count(1) == 1 and gaps[5] == 1,
                "shift_mappings": mappings == expected,
                "terminal_predecessors":
                    tuple((value - 1) % modulus in rowset for value in terminals)
                    == (False, False, True),
                "first_predecessors":
                    not any((value - 1) % modulus in rowset for value in firsts),
                "unreachable_value":
                    rows["hr(b)"] - period == 5 * bank + 1
                    and rows["hr(b)"] - period not in rowset,
            }
            if not all(predicates.values()):
                disagreements.append({
                    "B": bank_count,
                    "b": bank,
                    "failed": [name for name, ok in predicates.items() if not ok],
                    "mappings": [list(pair) for pair in sorted(mappings)],
                })
    return {
        "cells": cells,
        "disagreements": disagreements,
        "odd_exception_cells": odd_exceptions,
        "even_exception_cells": even_exceptions,
    }


def literal_detector(mask: int, length: int, period: int,
                     min_events: int = 8, repeats: int = 2) -> dict[str, object]:
    bits = [bool((mask >> tick) & 1) for tick in range(length)]
    clean_ticks = [tick for tick, clean in enumerate(bits) if clean]
    if not clean_ticks:
        return {"accepted": False, "reason": "empty"}
    if len(clean_ticks) < min_events:
        return {"accepted": False, "reason": "fewer_than_minimum_clean_ticks"}
    last_clean = clean_ticks[-1]
    required = repeats * period
    if required > last_clean:
        return {"accepted": False, "reason": "last_clean_too_early",
                "last_clean": last_clean}
    if any(bits[tick] != bits[tick + period]
           for tick in range(last_clean - required, last_clean - period + 1)):
        return {"accepted": False, "reason": "last_clean_tail_not_period_exact",
                "last_clean": last_clean}
    mismatches = [
        tick for tick in range(last_clean - period + 1)
        if bits[tick] != bits[tick + period]
    ]
    transient = (max(mismatches) + 1) if mismatches else 0
    if last_clean - transient < required:
        return {"accepted": False, "reason": "period_exact_suffix_too_short",
                "last_clean": last_clean, "transient": transient}
    stable_ticks = [tick for tick in clean_ticks if tick >= transient]
    if len(stable_ticks) < min_events:
        return {"accepted": False, "reason": "too_few_stable_clean_ticks",
                "last_clean": last_clean, "transient": transient,
                "events": len(stable_ticks)}
    residues = {tick % period for tick in stable_ticks}
    if len(residues) == period:
        return {"accepted": False, "reason": "all_residues_clean",
                "last_clean": last_clean, "transient": transient,
                "events": len(stable_ticks), "residue_count": len(residues)}
    return {"accepted": True, "reason": "accepted",
            "last_clean": last_clean, "transient": transient,
            "events": len(stable_ticks), "residue_count": len(residues)}


def whole_stretch_tail(mask: int, length: int, period: int) -> bool:
    bits = [bool((mask >> tick) & 1) for tick in range(length)]
    low = length - 1 - 2 * period
    return low >= 0 and all(
        bits[tick] == bits[tick + period]
        for tick in range(low, length - period)
    )


def mask_from_dirty(length: int, dirty: set[int]) -> int:
    return sum(1 << tick for tick in range(length) if tick not in dirty)


def intervals_of_dirty(mask: int, length: int) -> list[tuple[int, int]]:
    intervals: list[tuple[int, int]] = []
    start: int | None = None
    for tick in range(length + 1):
        dirty = tick < length and not bool((mask >> tick) & 1)
        if dirty and start is None:
            start = tick
        elif not dirty and start is not None:
            intervals.append((start, tick - 1))
            start = None
    return intervals


def independent_detector_result() -> dict[str, object]:
    endpoint = sum(1 << tick for tick in range(0, 15, 2))
    insufficient = mask_from_dirty(18, {2, 6, 16})
    unequal = mask_from_dirty(
        40,
        {2, 7, 8} | {tick for tick in range(15, 40) if tick % 5 == 0},
    )
    return {
        "endpoint": {
            "decision": literal_detector(endpoint, 18, 2),
            "whole_stretch_tail_exact": whole_stretch_tail(endpoint, 18, 2),
        },
        "equal_width_insufficient": {
            "widths": [end - start + 1
                       for start, end in intervals_of_dirty(insufficient, 18)[:2]],
            "decision": literal_detector(insufficient, 18, 4),
        },
        "unequal_width_accepted": {
            "widths": [end - start + 1
                       for start, end in intervals_of_dirty(unequal, 40)[:2]],
            "decision": literal_detector(unequal, 40, 5),
        },
    }


def independent_periodic_width_result() -> dict[str, object]:
    translations = 0
    failures: list[dict[str, int]] = []
    for period in range(2, 9):
        for word in range(1 << period):
            length = 5 * period
            mask = sum(
                1 << tick
                for tick in range(length)
                if (word >> (tick % period)) & 1
            )
            runs = intervals_of_dirty(mask, length)
            widths = {start: end - start + 1 for start, end in runs}
            for start, end in runs:
                if start < period or end + period >= length:
                    continue
                translations += 1
                if widths.get(start + period) != end - start + 1:
                    failures.append({"period": period, "word": word,
                                     "start": start})
    return {"translations": translations, "failures": failures}


def independent_widening_result() -> dict[str, object]:
    period = 8
    target = (18, 26)

    def views(starts: tuple[int, ...]) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
        position = {value: index for index, value in enumerate(starts)}
        widened = {
            (start, start + period)
            for start in starts if start + period in position
        }
        strict = {
            pair for pair in widened
            if position[pair[1]] == position[pair[0]] + 1
        }
        return widened, strict

    extended_wide, extended_strict = views((18, 26))
    separated_wide, separated_strict = views((18, 22, 26))
    return {
        "historical_extension_target_wide": target in extended_wide,
        "historical_extension_target_strict": target in extended_strict,
        "separated_target_wide": target in separated_wide,
        "separated_target_strict": target in separated_strict,
        "separated_is_wide_only":
            target in separated_wide and target not in separated_strict,
        "station_fixture": {
            "B": 5, "b": 3, "N": 35, "P": 8,
            "run_start_pair": list(target),
            "token_zero_station_pair": [17, 25],
        },
    }


def main() -> int:
    started = monotonic()
    input_bytes = {
        relative: (ROOT / relative).read_bytes()
        if (ROOT / relative).is_file() else b""
        for relative in AUDIT_INPUT_PATHS
    }
    actual_pins = {
        relative: sha256(body).hexdigest() if body else None
        for relative, body in input_bytes.items()
    }
    pins_ok = all(actual_pins[path] == EXPECTED_SHA256[path]
                  for path in AUDIT_INPUT_PATHS)
    check("PINNED_PRIMARY_AND_CACHE", pins_ok,
          "; ".join(f"{path}:{'MATCH' if actual_pins[path] == EXPECTED_SHA256[path] else 'MISMATCH'}"
                    for path in AUDIT_INPUT_PATHS))

    claims = parse_claims(input_bytes[PRIMARY_CACHE])
    cache_text = input_bytes[PRIMARY_CACHE].decode("utf-8", errors="replace")
    interface_ok = isinstance(claims, dict) and "TOTAL: PASS=11 FAIL=0" in cache_text
    check("PRIMARY_CLAIMS_INTERFACE", interface_ok,
          f"claims_dict={isinstance(claims, dict)} primary_total_present={'TOTAL: PASS=11 FAIL=0' in cache_text}")
    if not isinstance(claims, dict):
        claims = {}

    station = independent_station_result()
    check("MODULAR_STATION_ENUMERATION",
          station["cells"] == 253 and not station["disagreements"],
          f"cells={station['cells']} disagreements={len(station['disagreements'])} "
          f"odd_exceptions={station['odd_exception_cells']} even_exceptions={station['even_exception_cells']}")

    detector = independent_detector_result()
    endpoint_ok = (
        detector["endpoint"]["decision"].get("accepted") is True
        and detector["endpoint"]["decision"].get("transient") == 0
        and detector["endpoint"]["decision"].get("events") == 8
        and detector["endpoint"]["decision"].get("residue_count") == 1
        and detector["endpoint"]["whole_stretch_tail_exact"] is False
    )
    check("LITERAL_ENDPOINT_DISTINCTION", endpoint_ok,
          "last-clean detector accepts; whole-stretch terminal feature rejects")
    width_ok = (
        detector["equal_width_insufficient"]["widths"] == [1, 1]
        and not detector["equal_width_insufficient"]["decision"].get("accepted")
        and detector["unequal_width_accepted"]["widths"] == [1, 2]
        and detector["unequal_width_accepted"]["decision"].get("accepted") is True
    )
    check("WIDTH_COUNTEREXAMPLES", width_ok,
          "synthetic detector-domain witnesses give [1,1] rejected and [1,2] accepted")

    periodic = independent_periodic_width_result()
    check("PERIODIC_RUN_TRANSLATIONS",
          periodic["translations"] > 0 and not periodic["failures"],
          f"translations={periodic['translations']} failures={len(periodic['failures'])}")

    widening = independent_widening_result()
    check("WIDENING_ONLY_CONTROL",
          widening["historical_extension_target_wide"]
          and widening["historical_extension_target_strict"]
          and widening["separated_is_wide_only"],
          "extension=true/true; separated intervening start=true/false")

    primary_agreement = (
        claims.get("claim_type") == "bounded_theorem"
        and claims.get("station_cells_checked") == station["cells"]
        and claims.get("station_disagreements") == 0
        and claims.get("endpoint_witness", {}).get("detector", {}).get("accepted") is True
        and claims.get("endpoint_witness", {}).get("whole_stretch_tail_exact") is False
        and claims.get("equal_width_insufficient", {}).get("selected_pair_widths") == [1, 1]
        and claims.get("equal_width_unnecessary", {}).get("selected_pair_widths") == [1, 2]
        and claims.get("widening", {}).get("corrected_t1_plus_4_separated_run", {}).get("wide_only") is True
        and claims.get("claim_boundary", {}).get("historical_RC3_closed") is False
    )
    check("PRIMARY_SELECTED_CLAIMS_AGREE", primary_agreement,
          "selected finite values and open-boundary fields match independent routes")

    elapsed = monotonic() - started
    check("RUNTIME_BOUND", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.6f} budget_s={AUDIT_TIMEOUT_SEC}")

    all_pass = all(ok for _name, ok, _detail in CERTS)
    receipt = {
        "schema": "third-pair-cycle930-corrected-independent-check-receipt-v1",
        "authority": "none",
        "audit": "unset",
        "claim_type": "bounded_theorem",
        "cycle": 930,
        "verdict": ("CURRENT_FINITE_CLAIMS_MATCH_INDEPENDENT_ROUTES"
                    if all_pass else "CURRENT_FINITE_CLAIMS_REFUTED_OR_UNBOUND"),
        "all_certificates_pass": all_pass,
        "certificates": {
            name: {"pass": ok, "detail": detail}
            for name, ok, detail in CERTS
        },
        "independent_results": {
            "station": station,
            "detector": detector,
            "periodic_run_width": periodic,
            "widening": widening,
        },
        "declared_inputs": list(AUDIT_INPUT_PATHS),
        "input_sha256": actual_pins,
        "historical_campaign_replayed": False,
        "physical_interpretation_checked": False,
        "formal_audit": False,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "files": {
            "scripts/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py":
                sha256(Path(__file__).read_bytes()).hexdigest()
        },
    }
    out = ROOT / RECEIPT_REL
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"RECEIPT: {RECEIPT_REL}")
    passed = sum(ok for _name, ok, _detail in CERTS)
    failed = len(CERTS) - passed
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
