#!/usr/bin/env python3
"""Standalone affected-fault checks; no old controller or primary is replayed.

This checker imports definitions only. The four publications explicitly link
this standalone evidence; B38's automatic helper closure is its actual B37
import. These checks do not certify physical realization or an audit grade.
"""
from __future__ import annotations
import contextlib
import hashlib
import io
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import admissibility_gaussian_fair_record_affinity_haar_factor_fresh_port_reset_2026_09_01 as B36
import admissibility_block36_specific_nn_active_cut_record_front_corrected_2026_09_09 as B37
import admissibility_random_axis_m2_matter_repeat_selector_local_compiler_corrected_2026_09_09 as B38

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md', 'docs/ADMISSIBILITY_GAUSSIAN_FAIR_RECORD_MIDPOINT_AFFINITY_HAAR_EDGE_FACTOR_FRESH_PORT_RESET_BOUNDED_THEOREM_NOTE_2026-09-01.md', 'docs/ADMISSIBILITY_BLOCK36_SPECIFIC_NN_ACTIVE_CUT_RECORD_FRONT_BOUNDED_THEOREM_NOTE_2026-09-01.md', 'docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md', 'scripts/admissibility_gaussian_fair_record_affinity_haar_factor_fresh_port_reset_2026_09_01.py', 'scripts/admissibility_block36_specific_nn_active_cut_record_front_corrected_2026_09_09.py', 'scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_corrected_2026_09_09.py')
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
DIRECT_HASHES = {'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md': 'bd4e310f4e9d5f07b2e3f11ad1dc94b2541c12b80a38051584e1d778724a64e7', 'docs/ADMISSIBILITY_GAUSSIAN_FAIR_RECORD_MIDPOINT_AFFINITY_HAAR_EDGE_FACTOR_FRESH_PORT_RESET_BOUNDED_THEOREM_NOTE_2026-09-01.md': '5e945edf9aef50bef597b037aa8dac01b5a9c9a6a6a6fbbfc54978cdd908a9d5', 'docs/ADMISSIBILITY_BLOCK36_SPECIFIC_NN_ACTIVE_CUT_RECORD_FRONT_BOUNDED_THEOREM_NOTE_2026-09-01.md': '22859693cb1a6e192a3cb50d3d0965c7ee8672520be6f59ec491857df153427f', 'docs/ADMISSIBILITY_RANDOM_AXIS_M2_MATTER_REPEAT_SELECTOR_LOCAL_COMPILER_BOUNDED_THEOREM_NOTE_2026-09-01.md': 'c2ff01d9799b707ffd2209b10e5475087ce7996393583d36b313229d8fcf1f6c', 'scripts/admissibility_gaussian_fair_record_affinity_haar_factor_fresh_port_reset_2026_09_01.py': 'b4bd75f059a974c8853c59adc5ea597c9fafeddbe8b245a310f406ead22eb9c9', 'scripts/admissibility_block36_specific_nn_active_cut_record_front_corrected_2026_09_09.py': 'b117ee1f23b40df38a98cff5278d06ee6d72a42b708d5a09540a37db1f15e2f3', 'scripts/admissibility_random_axis_m2_matter_repeat_selector_local_compiler_corrected_2026_09_09.py': '15fa61584696daa13bb2ab29cf09ed175ecda504d1b444ddce7fdff76f57963e'}


def current_inputs_ok() -> bool:
    return all((ROOT / path).is_file() and hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
               for path, expected in DIRECT_HASHES.items())


def guard_current_inputs() -> None:
    if not current_inputs_ok():
        raise RuntimeError("current source/premise input missing or changed")
    print(f"INPUT_BOUND: {len(DIRECT_HASHES)} actual current inputs")




def main() -> int:
    guard_current_inputs()
    checks = B36.Checks()
    original = B36.cylinder_mixture
    for slot, rows in (("preparation", B36.PREPARATION_ROWS), ("test", B36.TEST_ROWS)):
        clean = original(rows)
        swapped = replace(clean, fine=tuple((1-bit, label, weight) for bit, label, weight in clean.fine))
        corrupt_coarse = replace(clean, coarse=(clean.coarse[0] + F(1, 8), clean.coarse[1] - F(1, 8)))
        checks.check("fine_coarse_" + slot, "clean branch law accepted; actual bit labels and coarse weights changed independently",
                     B36.valid_cylinder_mixture(clean, rows)
                     and not B36.valid_cylinder_mixture(swapped, rows)
                     and not B36.valid_cylinder_mixture(corrupt_coarse, rows))
    # The full existing gate must reject the exact original review fault,
    # not merely an independently invented check against its data.
    baseline = B36.Checks()
    with contextlib.redirect_stdout(io.StringIO()):
        B36.gate_record_first_cylinders(baseline)
    def swap_test(rows, *, forged=False):
        result = original(rows, forged=forged)
        if rows == B36.TEST_ROWS:
            return replace(result, fine=tuple((1-bit, label, weight) for bit, label, weight in result.fine))
        return result
    B36.cylinder_mixture = swap_test
    try:
        fault = B36.Checks()
        with contextlib.redirect_stdout(io.StringIO()):
            B36.gate_record_first_cylinders(fault)
    finally:
        B36.cylinder_mixture = original
    checks.check("test_slot_fault_existing_gate", f"clean={baseline.results}; actual test-label swap={fault.results}",
                 baseline.results == {"record_first_fine_cylinder_average": True}
                 and fault.results == {"record_first_fine_cylinder_average": False})
    # Alter the actual payload projection called by the local table. The
    # same current predicate sees a clean baseline then an archive-dependent map.
    baseline_cut = B37.payload_projection_certificate(B37.RuleConfig())
    close = B37.close_payload
    B37.close_payload = lambda vector, config: vector
    try:
        fault_cut = B37.payload_projection_certificate(B37.RuleConfig())
    finally:
        B37.close_payload = close
    checks.check("actual_close_projection_fault", f"clean={baseline_cut}; payload-copying close={fault_cut}", baseline_cut and not fault_cut)
    fresh = B37.explicit_bit_process("fresh", 3)
    frozen = B37.explicit_bit_process("frozen", 3)
    parity = B37.explicit_bit_process("even_parity", 3)
    product = lambda law: law == fresh
    checks.check("explicit_alternative_laws", "fresh accepted, frozen/parity differ as actual finite distributions; not generator-mutation claims",
                 product(fresh) and not product(frozen) and not product(parity)
                 and parity[(0, 0, 0)] == F(1, 4) and fresh[(0, 0, 0)] == F(1, 8))
    cases = []
    for lam, kap in ((F(1),F(1)),(F(-1),F(-1)),(F(1,2),F(1)),(F(1),F(1,2))):
        mismatch = B38.binary_probability(B38.post_state(B38.E_Z, 1, kap), B38.E_Z, -1, lam)
        cases.append((lam, kap, mismatch, mismatch == 0))
    checks.check("actual_second_read_repeat_condition", repr(cases),
                 [row[2] for row in cases] == [0, 0, F(1,4), F(1,4)]
                 and [row[3] for row in cases] == [True, True, False, False])
    carrier = B37.encode_protocol("H_RND", B37.IDENTITY_FRAME, B37.DEFAULT_RND)
    rotation = next(r for r in B37.ROTATIONS if r != B37.IDENTITY_ROTATION)
    rotated = B37.rotate_carrier(rotation, carrier)
    traces = (2*carrier.coefficients[0], 2*rotated.coefficients[0])
    checks.check("encoded_action_scope", f"actual code traces={traces}; this action is not full-matrix unitary conjugation", traces == (50, 4))
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
