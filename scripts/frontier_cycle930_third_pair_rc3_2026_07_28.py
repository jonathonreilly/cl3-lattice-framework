#!/usr/bin/env python3
"""Finite station and detector facts salvaged from historical Cycle 930.

The runner is self-contained. It proves exact affine facts for the supplied
un-padded eight-row station family, checks the originally stated B=3..24
finite grid, distinguishes a detector ending at the last clean tick from a
feature ending at the supplied stretch boundary, and tests a genuine
widening-only run-start witness.

It does not execute the historical controller, reproduce its census, identify
station ordinals with physical time or Record, explain a historical zero count,
classify all arithmetic selectors, or close the historical RC-3 question.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 30
STDOUT_LIMIT_BYTES = 150_000

from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
RECEIPT_REL = "outputs/third_pair_rc3_cycle930_receipt_2026_07_28.json"
CERTS: list[tuple[str, bool, str]] = []

ROW_ORDER = (
    "hf(b-1)", "f(b-1)", "hf(b)", "f(b)",
    "r(b)", "hr(b)", "r(b-1)", "hr(b-1)",
)
PAIR_ORDER = ("swap_swap", "swap_handoff", "handoff_swap")


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def check(name: str, ok: bool, detail: str) -> bool:
    CERTS.append((name, bool(ok), detail))
    print(f"{'PASS' if ok else 'FAIL'} {name} :: {detail}")
    return bool(ok)


def station_rows(bank_count: int, bank: int) -> dict[str, int]:
    """The supplied affine station family on its exact integer domain."""
    if bank_count < 3 or not 1 <= bank <= bank_count - 2:
        raise ValueError("requires B>=3 and 1<=b<=B-2")
    return {
        "hf(b-1)": 5 * bank - 3,
        "f(b-1)": 5 * bank - 1,
        "hf(b)": 5 * bank + 2,
        "f(b)": 5 * bank + 4,
        "r(b)": 8 * bank_count - 9 - 3 * bank,
        "hr(b)": 8 * bank_count - 7 - 3 * bank,
        "r(b-1)": 8 * bank_count - 6 - 3 * bank,
        "hr(b-1)": 8 * bank_count - 4 - 3 * bank,
    }


def station_cell(bank_count: int, bank: int) -> dict[str, object]:
    rows = station_rows(bank_count, bank)
    modulus = 8 * bank_count - 5
    period = 8 * (bank_count - 1 - bank)
    ordered = [rows[name] for name in ROW_ORDER]
    gaps = [
        (ordered[(index + 1) % len(ordered)] - ordered[index]) % modulus
        for index in range(len(ordered))
    ]
    pairs = {
        "swap_swap": (rows["f(b-1)"], rows["r(b)"]),
        "swap_handoff": (rows["f(b)"], rows["hr(b-1)"]),
        "handoff_swap": (rows["hf(b)"], rows["r(b-1)"]),
    }
    value_to_name = {value: name for name, value in rows.items()}
    shift_fixed = tuple(
        name for name in ROW_ORDER
        if (rows[name] + period) % modulus in value_to_name
    )
    expected_extra = (
        ("r(b-1)",) if bank_count % 2 else ("r(b)",)
    ) if bank == (bank_count - 1) // 2 else ()
    return {
        "B": bank_count,
        "b": bank,
        "N": modulus,
        "P": period,
        "rows": rows,
        "ordered_values": ordered,
        "gaps": gaps,
        "expected_gaps": [
            2, 3, 2, 8 * (bank_count - bank) - 13,
            2, 1, 2, 8 * bank - 4,
        ],
        "pairs": {name: list(pair) for name, pair in pairs.items()},
        "all_pairs_span_P": all(end - start == period
                                  for start, end in pairs.values()),
        "unit_gap_lower_and_upper": ["hr(b)", "r(b-1)"],
        "sole_unit_gap": gaps.count(1) == 1 and gaps[5] == 1,
        "pair_terminal_has_row_predecessor": {
            name: ((end - 1) % modulus in value_to_name)
            for name, (_start, end) in pairs.items()
        },
        "pair_first_has_row_predecessor": {
            name: ((start - 1) % modulus in value_to_name)
            for name, (start, _end) in pairs.items()
        },
        "P_shift_fixed_rows": list(shift_fixed),
        "expected_extra_P_shift_fixed_rows": list(expected_extra),
        "extra_P_shift_fixed_rows": sorted(
            set(shift_fixed) - {"f(b-1)", "hf(b)", "f(b)"}
        ),
        "hr_b_minus_P": rows["hr(b)"] - period,
        "hr_b_minus_P_expected": 5 * bank + 1,
        "hr_b_has_no_P_preimage": (rows["hr(b)"] - period) not in value_to_name,
    }


# An affine expression is a tuple (coefficient of B, coefficient of b, constant).
AFFINE_ROWS = {
    "hf(b-1)": (0, 5, -3),
    "f(b-1)": (0, 5, -1),
    "hf(b)": (0, 5, 2),
    "f(b)": (0, 5, 4),
    "r(b)": (8, -3, -9),
    "hr(b)": (8, -3, -7),
    "r(b-1)": (8, -3, -6),
    "hr(b-1)": (8, -3, -4),
}
AFFINE_P = (8, -8, -8)
AFFINE_N = (8, 0, -5)


def affine_sub(*terms: tuple[int, tuple[int, int, int]]) -> tuple[int, int, int]:
    return tuple(sum(sign * expression[i] for sign, expression in terms)
                 for i in range(3))


def affine_shift_analysis() -> dict[str, object]:
    """Solve x+P=y modulo N across all 64 ordered row pairs.

    Since every row lies in [0,N) and 0<P<N, only y-x-P=0 and y-x-P=-N
    are possible. The non-wrap equations give three identities; every other
    equation is a nonzero constant or puts B-b below its domain. In the wrap
    equations, integrality and the domain leave constants 8 and 16, giving
    exactly the odd/even exceptions.
    """
    general: list[list[str]] = []
    nonwrap_outside: list[dict[str, object]] = []
    wrap_viable: list[dict[str, object]] = []
    wrap_excluded: list[dict[str, object]] = []
    unexpected: list[dict[str, object]] = []
    for source, x in AFFINE_ROWS.items():
        for target, y in AFFINE_ROWS.items():
            for wrap in (False, True):
                # y-x-P is 0 without wrap and -N with wrap.
                expression = affine_sub((1, y), (-1, x), (-1, AFFINE_P),
                                        (1, AFFINE_N) if wrap else (0, AFFINE_N))
                row = {"source": source, "target": target,
                       "equation_coefficients": list(expression),
                       "wrap": wrap}
                if expression == (0, 0, 0):
                    general.append([source, target])
                elif not wrap and expression[0:2] in ((-8, 8), (-16, 16)):
                    scale = -expression[0]
                    constant = expression[2]
                    if constant < 2 * scale or constant % scale:
                        row["exclusion"] = (
                            f"equation requires B-b={constant}/{scale}; "
                            "the domain has integer B-b>=2"
                        )
                        nonwrap_outside.append(row)
                    else:
                        unexpected.append(row)
                elif not wrap and expression[0:2] == (0, 0):
                    row["exclusion"] = "nonzero constant equation"
                    nonwrap_outside.append(row)
                elif wrap and expression[0:2] == (-8, 16):
                    constant = expression[2]
                    if constant == 8:
                        row["only_integer_solution"] = "B odd, b=(B-1)/2"
                        wrap_viable.append(row)
                    elif constant == 16:
                        row["only_integer_solution"] = "B even, b=(B-2)/2"
                        wrap_viable.append(row)
                    elif constant % 8:
                        row["exclusion"] = (
                            "constant is neither 0 nor 8 modulo 16 for the "
                            "required parity of B"
                        )
                        wrap_excluded.append(row)
                    else:
                        unexpected.append(row)
                elif wrap and expression[0:2] == (0, 8):
                    numerator = -expression[2]
                    if numerator < 8 or numerator % 8:
                        row["exclusion"] = (
                            f"equation requires b={numerator}/8, "
                            "which is noninteger or below 1"
                        )
                        wrap_excluded.append(row)
                    else:
                        unexpected.append(row)
                elif wrap and expression[0:2] == (8, 0):
                    numerator = -expression[2]
                    if numerator < 24 or numerator % 8:
                        row["exclusion"] = (
                            f"equation requires B={numerator}/8, "
                            "which is noninteger or below 3"
                        )
                        wrap_excluded.append(row)
                    else:
                        unexpected.append(row)
                else:
                    unexpected.append(row)
    expected_general = {
        ("f(b-1)", "r(b)"),
        ("hf(b)", "r(b-1)"),
        ("f(b)", "hr(b-1)"),
    }
    expected_wrap = {
        ("r(b-1)", "f(b-1)", 8),
        ("r(b)", "f(b)", 16),
    }
    got_wrap = {
        (row["source"], row["target"], row["equation_coefficients"][2])
        for row in wrap_viable
    }
    return {
        "general_pairs": general,
        "expected_general_pairs": [list(pair) for pair in sorted(expected_general)],
        "general_pairs_exact": {tuple(pair) for pair in general} == expected_general,
        "nonwrap_outside_count": len(nonwrap_outside),
        "nonwrap_outside": nonwrap_outside,
        "wrap_viable": wrap_viable,
        "wrap_viable_exact": got_wrap == expected_wrap,
        "wrap_excluded_count": len(wrap_excluded),
        "unexpected_equations": unexpected,
        "range_argument": "0<=x,y<N and 0<P<N leave only y-x-P in {0,-N}",
    }


def station_result() -> dict[str, object]:
    analysis = affine_shift_analysis()
    bad: list[dict[str, object]] = []
    cells: list[dict[str, object]] = []
    for bank_count in range(3, 25):
        for bank in range(1, bank_count - 1):
            row = station_cell(bank_count, bank)
            expected_fixed = {"f(b-1)", "hf(b)", "f(b)"} | set(
                row["expected_extra_P_shift_fixed_rows"]
            )
            predicates = {
                "strict_row_order": row["ordered_values"] == sorted(set(row["ordered_values"])),
                "cyclic_gap_formula": row["gaps"] == row["expected_gaps"],
                "variable_gap_bounds": row["gaps"][3] >= 3 and row["gaps"][7] >= 4,
                "sole_unit_gap": row["sole_unit_gap"],
                "three_pairs_span_P": row["all_pairs_span_P"],
                "only_third_terminal_has_row_predecessor":
                    row["pair_terminal_has_row_predecessor"] == {
                        "swap_swap": False,
                        "swap_handoff": False,
                        "handoff_swap": True,
                    },
                "no_pair_first_has_row_predecessor":
                    not any(row["pair_first_has_row_predecessor"].values()),
                "shift_fixed_rows": set(row["P_shift_fixed_rows"]) == expected_fixed,
                "hr_b_minus_P": row["hr_b_minus_P"] == row["hr_b_minus_P_expected"],
                "hr_b_has_no_P_preimage": row["hr_b_has_no_P_preimage"],
            }
            if not all(predicates.values()):
                bad.append({"B": bank_count, "b": bank,
                            "failed": [name for name, ok in predicates.items() if not ok]})
            cells.append({"B": bank_count, "b": bank,
                          "extra": row["extra_P_shift_fixed_rows"]})
    return {
        "quantified_domain": "integers B>=3 and 1<=b<=B-2",
        "cyclic_gap_formula": ["2", "3", "2", "8(B-b)-13", "2", "1", "2", "8b-4"],
        "variable_gap_lower_bounds": [3, 4],
        "affine_shift_analysis": analysis,
        "bounded_regression_domain": "3<=B<=24",
        "cells_checked": len(cells),
        "disagreements": bad,
        "examples": [station_cell(5, 2), station_cell(6, 2), station_cell(7, 3)],
    }


def detector_decision(mask: int, period: int, min_events: int = 8,
                      min_repeats: int = 2) -> dict[str, object]:
    """Historical detector convention: the endpoint is the last clean tick."""
    if mask == 0:
        return {"accepted": False, "reason": "empty"}
    if mask.bit_count() < min_events:
        return {"accepted": False, "reason": "fewer_than_minimum_clean_ticks"}
    last_clean = mask.bit_length() - 1
    required = min_repeats * period
    if required > last_clean:
        return {"accepted": False, "reason": "last_clean_too_early",
                "last_clean": last_clean}
    low = last_clean - required
    window = (mask >> low) & ((1 << (required + 1)) - 1)
    if (window ^ (window >> period)) & ((1 << (period + 1)) - 1):
        return {"accepted": False, "reason": "last_clean_tail_not_period_exact",
                "last_clean": last_clean}
    span = last_clean - period
    broken = (mask ^ (mask >> period)) & ((1 << (span + 1)) - 1)
    transient = broken.bit_length()
    if last_clean - transient < required:
        return {"accepted": False, "reason": "period_exact_suffix_too_short",
                "last_clean": last_clean, "transient": transient}
    stable = (mask >> transient) & ((1 << (last_clean - transient + 1)) - 1)
    events = stable.bit_count()
    if events < min_events:
        return {"accepted": False, "reason": "too_few_stable_clean_ticks",
                "last_clean": last_clean, "transient": transient, "events": events}
    residues = {
        tick % period
        for tick in range(transient, last_clean + 1)
        if (mask >> tick) & 1
    }
    if len(residues) == period:
        return {"accepted": False, "reason": "all_residues_clean",
                "last_clean": last_clean, "transient": transient,
                "events": events, "residue_count": len(residues)}
    return {"accepted": True, "reason": "accepted",
            "last_clean": last_clean, "transient": transient,
            "events": events, "residue_count": len(residues)}


def whole_stretch_tail_exact(mask: int, length: int, period: int,
                             repeats: int = 2) -> bool:
    """Different feature: test the terminal window ending at length-1."""
    if length <= 0 or period <= 0 or repeats * period >= length:
        return False
    low = length - 1 - repeats * period
    return all(
        ((mask >> tick) & 1) == ((mask >> (tick + period)) & 1)
        for tick in range(low, length - period)
    )


def mask_with_dirty_ticks(length: int, dirty: set[int]) -> int:
    return sum(1 << tick for tick in range(length) if tick not in dirty)


def dirty_runs(mask: int, length: int) -> list[tuple[int, int]]:
    runs: list[tuple[int, int]] = []
    tick = 0
    while tick < length:
        if (mask >> tick) & 1:
            tick += 1
            continue
        end = tick
        while end + 1 < length and not ((mask >> (end + 1)) & 1):
            end += 1
        runs.append((tick, end))
        tick = end + 1
    return runs


def detector_result() -> dict[str, object]:
    endpoint_length = 18
    endpoint_period = 2
    endpoint_mask = sum(1 << tick for tick in range(0, 15, 2))
    endpoint_decision = detector_decision(endpoint_mask, endpoint_period)
    whole_tail = whole_stretch_tail_exact(
        endpoint_mask, endpoint_length, endpoint_period
    )

    insufficient_mask = mask_with_dirty_ticks(18, {2, 6, 16})
    insufficient_runs = dirty_runs(insufficient_mask, 18)
    insufficient_decision = detector_decision(insufficient_mask, 4)

    unnecessary_dirty = {2, 7, 8} | {tick for tick in range(15, 40) if tick % 5 == 0}
    unnecessary_mask = mask_with_dirty_ticks(40, unnecessary_dirty)
    unnecessary_runs = dirty_runs(unnecessary_mask, 40)
    unnecessary_decision = detector_decision(unnecessary_mask, 5)

    return {
        "endpoint_conventions": {
            "detector": "last clean tick mask.bit_length()-1",
            "historical_score_feature": "end of supplied stretch length-1",
        },
        "endpoint_witness": {
            "length": endpoint_length,
            "period": endpoint_period,
            "clean_ticks": list(range(0, 15, 2)),
            "detector": endpoint_decision,
            "whole_stretch_tail_exact": whole_tail,
            "distinguishing_bits": {"tick_14": 1, "tick_16": 0},
        },
        "equal_width_not_sufficient_for_this_detector": {
            "length": 18,
            "period": 4,
            "dirty_runs": [list(run) for run in insufficient_runs],
            "selected_pair_widths": [
                insufficient_runs[0][1] - insufficient_runs[0][0] + 1,
                insufficient_runs[1][1] - insufficient_runs[1][0] + 1,
            ],
            "decision": insufficient_decision,
        },
        "equal_width_not_necessary_for_this_detector": {
            "length": 40,
            "period": 5,
            "dirty_runs": [list(run) for run in unnecessary_runs],
            "selected_pair_widths": [
                unnecessary_runs[0][1] - unnecessary_runs[0][0] + 1,
                unnecessary_runs[1][1] - unnecessary_runs[1][0] + 1,
            ],
            "decision": unnecessary_decision,
            "scope": "synthetic detector-domain witness; no bank, controller, or physical realization is claimed",
        },
    }


def complete_periodic_run_width_result() -> dict[str, object]:
    checked = 0
    failures: list[dict[str, int]] = []
    for period in range(2, 9):
        for word in range(1 << period):
            length = 5 * period
            mask = sum(
                1 << tick
                for tick in range(length)
                if (word >> (tick % period)) & 1
            )
            runs = dirty_runs(mask, length)
            by_start = {start: (start, end) for start, end in runs}
            for start, end in runs:
                if start < period or end + period >= length:
                    continue
                checked += 1
                image = by_start.get(start + period)
                if image is None or image[1] - image[0] != end - start:
                    failures.append({"period": period, "word": word, "start": start})
    # Slice global ticks 1..11 from a 5-periodic word dirty on residues 0,1,2.
    clipped_dirty = {
        local
        for local, global_tick in enumerate(range(1, 12))
        if global_tick % 5 in (0, 1, 2)
    }
    clipped_mask = mask_with_dirty_ticks(11, clipped_dirty)
    clipped_widths = [end - start + 1 for start, end in dirty_runs(clipped_mask, 11)]
    return {
        "statement": "translation by P preserves every complete maximal run whose run and translated image lie in the supplied P-periodic region",
        "finite_regression_periods": "2..8, all binary base words, five repeats",
        "complete_run_translations_checked": checked,
        "failures": failures,
        "clipped_boundary_example": {
            "global_slice": "ticks 1..11 of period 5, dirty residues {0,1,2}",
            "visible_run_widths": clipped_widths,
            "unequal_widths_are_boundary_clipping": clipped_widths == [2, 3, 2],
        },
    }


def pair_views(starts: list[int], period: int) -> dict[str, object]:
    index = {start: position for position, start in enumerate(starts)}
    widened: list[list[int]] = []
    consecutive: list[list[int]] = []
    for position, start in enumerate(starts):
        target = start + period
        if target not in index:
            continue
        pair = [start, target]
        widened.append(pair)
        if index[target] == position + 1:
            consecutive.append(pair)
    return {"starts": starts, "widened_pairs": widened,
            "consecutive_pairs": consecutive}


def widening_result() -> dict[str, object]:
    period = 8
    base_dirty = set(range(18, 21)) | set(range(26, 29))
    original_mask = mask_with_dirty_ticks(32, base_dirty | {21})
    corrected_mask = mask_with_dirty_ticks(32, base_dirty | {22})
    original_starts = [start for start, _end in dirty_runs(original_mask, 32)]
    corrected_starts = [start for start, _end in dirty_runs(corrected_mask, 32)]
    original = pair_views(original_starts, period)
    corrected = pair_views(corrected_starts, period)
    target = [18, 26]
    original_wide = target in original["widened_pairs"]
    original_strict = target in original["consecutive_pairs"]
    corrected_wide = target in corrected["widened_pairs"]
    corrected_strict = target in corrected["consecutive_pairs"]
    return {
        "fixture": {
            "B": 5, "b": 3, "N": 35, "P": period,
            "target_pair_run_starts": target,
            "target_pair_stations_for_token_at_zero": [17, 25],
        },
        "historical_t1_plus_3_extension": {
            **original,
            "target_widened": original_wide,
            "target_consecutive": original_strict,
        },
        "corrected_t1_plus_4_separated_run": {
            **corrected,
            "target_widened": corrected_wide,
            "target_consecutive": corrected_strict,
            "wide_only": corrected_wide and not corrected_strict,
        },
        "strict_substitution_rejected": corrected_wide and not corrected_strict,
    }


def science_result() -> dict[str, object]:
    return {
        "claim_type": "bounded_theorem",
        "station": station_result(),
        "detector": detector_result(),
        "periodic_run_width": complete_periodic_run_width_result(),
        "widening": widening_result(),
        "claim_boundary": {
            "historical_controller_campaign_replayed": False,
            "historical_counts_are_current_evidence": False,
            "station_ordinal_is_physical_time": "not supplied",
            "clean_mask_is_a_Record_readout": "not supplied",
            "unit_gap_causes_zero_episodes": "not established",
            "globally_best_arithmetic_or_width_selector": "not classified",
            "B8_and_B9_blind_holdouts": False,
            "B_greater_or_equal_10_controller_corpus": "not built",
            "historical_RC3_closed": False,
            "formal_audit": False,
            "TOE_closure": False,
        },
    }


def main() -> int:
    started = monotonic()
    result = science_result()
    station = result["station"]
    detector = result["detector"]
    periodic = result["periodic_run_width"]
    widening = result["widening"]

    check("AFFINE_SHIFT_SOLUTION",
          station["affine_shift_analysis"]["general_pairs_exact"]
          and station["affine_shift_analysis"]["wrap_viable_exact"]
          and not station["affine_shift_analysis"]["unexpected_equations"],
          "three general P-shifts and exactly the odd/even reverse-row exceptions")
    check("STATION_GRID_REGRESSION",
          station["cells_checked"] == 253 and not station["disagreements"],
          f"cells={station['cells_checked']} disagreements={len(station['disagreements'])}")
    check("ROW_GAP_AND_PAIR_STRUCTURE",
          all(example["sole_unit_gap"] and example["all_pairs_span_P"]
              for example in station["examples"]),
          "eight-row ordering, sole unit gap, and three P-separated pairs")
    endpoint = detector["endpoint_witness"]
    check("LAST_CLEAN_DETECTOR_WITNESS",
          endpoint["detector"]["accepted"]
          and endpoint["detector"]["transient"] == 0
          and endpoint["detector"]["events"] == 8
          and endpoint["detector"]["residue_count"] == 1,
          "length=18 period=2 accepted through last clean tick 14")
    check("ENDPOINT_CONVENTIONS_DIFFER",
          not endpoint["whole_stretch_tail_exact"],
          "whole-stretch endpoint 17 fails because clean(14) != clean(16)")
    insufficient = detector["equal_width_not_sufficient_for_this_detector"]
    check("EQUAL_WIDTH_NOT_SUFFICIENT",
          insufficient["selected_pair_widths"] == [1, 1]
          and not insufficient["decision"]["accepted"],
          f"equal widths [1,1], decision={insufficient['decision']['reason']}")
    unnecessary = detector["equal_width_not_necessary_for_this_detector"]
    check("EQUAL_WIDTH_NOT_NECESSARY",
          unnecessary["selected_pair_widths"] == [1, 2]
          and unnecessary["decision"]["accepted"],
          "synthetic detector-domain pair widths [1,2] with accepted period 5")
    check("COMPLETE_PERIODIC_RUN_WIDTHS",
          periodic["complete_run_translations_checked"] > 0
          and not periodic["failures"]
          and periodic["clipped_boundary_example"]["unequal_widths_are_boundary_clipping"],
          f"translations={periodic['complete_run_translations_checked']} clipped=[2,3,2]")
    corrected = widening["corrected_t1_plus_4_separated_run"]
    historical = widening["historical_t1_plus_3_extension"]
    check("GENUINE_WIDENING_ONLY_TOOTH",
          historical["target_widened"] and historical["target_consecutive"]
          and corrected["wide_only"] and widening["strict_substitution_rejected"],
          "t1+3 is wide/strict true/true; separated t1+4 is true/false")
    second = science_result()
    check("DETERMINISTIC_SCIENCE_PAYLOAD", digest(result) == digest(second),
          "complete finite payload recomputed in-process")
    elapsed = monotonic() - started
    check("RUNTIME_BOUND", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.6f} budget_s={AUDIT_TIMEOUT_SEC}")

    all_pass = all(ok for _name, ok, _detail in CERTS)
    receipt = {
        "schema": "third-pair-cycle930-corrected-primary-receipt-v1",
        "authority": "none",
        "audit": "unset",
        "claim_type": "bounded_theorem",
        "cycle": 930,
        "headline": "Exact affine station structure and finite detector-domain distinctions for the supplied Cycle-930 formulas.",
        "all_certificates_pass": all_pass,
        "certificates": {
            name: {"pass": ok, "detail": detail}
            for name, ok, detail in CERTS
        },
        "results": result,
        "science_digest": digest(result),
        "historical_campaign_replayed": False,
        "external_scientific_inputs": [],
        "package_local_integrity_reads": [
            "scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py"
        ],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "formal_audit": False,
        "files": {
            "scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py":
                sha256(Path(__file__).read_bytes()).hexdigest()
        },
    }
    out = ROOT / RECEIPT_REL
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("CLAIMS_JSON: " + compact({
        "claim_type": result["claim_type"],
        "station_cells_checked": station["cells_checked"],
        "station_disagreements": len(station["disagreements"]),
        "general_shift_pairs": station["affine_shift_analysis"]["general_pairs"],
        "endpoint_witness": endpoint,
        "equal_width_insufficient": insufficient,
        "equal_width_unnecessary": unnecessary,
        "periodic_translation_checks": periodic["complete_run_translations_checked"],
        "widening": widening,
        "claim_boundary": result["claim_boundary"],
        "science_digest": receipt["science_digest"],
    }))
    print(f"RECEIPT: {RECEIPT_REL}")
    passed = sum(ok for _name, ok, _detail in CERTS)
    failed = len(CERTS) - passed
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
