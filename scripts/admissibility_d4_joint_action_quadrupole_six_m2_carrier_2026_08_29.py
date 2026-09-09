#!/usr/bin/env python3
"""Bounded current conditional Eta spin-2 evidence; no historical child campaigns."""
from pathlib import Path
import hashlib
import sys
import eta_spin2_finite_checks_2026_09_09 as evidence
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_D4_COMMON_SPIN2_SOURCE_MODULE_SIX_BIT_CAPACITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md', 'docs/ADMISSIBILITY_D4_FROZEN_H2_COMMON_ACTION_SOURCE_IMAGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md', 'docs/ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md', 'docs/ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/eta_spin2_affine_model_2026_09_09.py', 'scripts/eta_spin2_finite_checks_2026_09_09.py', 'scripts/eta_spin2_joint_model_2026_09_09.py', 'scripts/eta_spin2_native_model_2026_09_09.py', 'scripts/eta_spin2_nondisturbance_model_2026_09_09.py', 'scripts/eta_spin2_quadrupole_model_2026_09_09.py')
EXPECTED_INPUT_SHA256 = {'docs/ADMISSIBILITY_D4_COMMON_SPIN2_SOURCE_MODULE_SIX_BIT_CAPACITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md': '67d0c341356666478aab775a09fb9ab9a2fde6c8e85129ee79bb2002a754b178', 'docs/ADMISSIBILITY_D4_FROZEN_H2_COMMON_ACTION_SOURCE_IMAGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md': 'ef0cabbfb54afa7b4ccb451a5d3a1c36582045633564766a2120b8a50c027704', 'docs/ADMISSIBILITY_D4_JOINT_ACTION_QUADRUPOLE_SIX_M2_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md': '9742b03898fa22e8f9d78ca0592ae2c4e3ef0dd0334e3009924d373f6331f31e', 'docs/ADMISSIBILITY_D4_QUANTUM_DIRECTION_CORNER_COMMON_SOURCE_OWNER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md': '1c8fff9bad1b8c672b0211b17e7452fa664df6885926c16c8b6f0221171e7d4c', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/eta_spin2_affine_model_2026_09_09.py': '0789cfa7c64d91a7fcc1ecd22bf98f61f97edcb942e7692f3106c9f948a351d4', 'scripts/eta_spin2_finite_checks_2026_09_09.py': '448eedc3cfc5804caa91e2928f1e8003e9303d4167414f1f148158faae33b135', 'scripts/eta_spin2_joint_model_2026_09_09.py': 'f6d0bfb9462d02230dc339d933f5fdf248d0a0c0cfa8f56a3fbc2500a6e00542', 'scripts/eta_spin2_native_model_2026_09_09.py': '3753f33054d72c2724b4ac6ff6473acff44741f42f7a941eeec101bc78818a10', 'scripts/eta_spin2_nondisturbance_model_2026_09_09.py': '106766acd78ddbfe0cfb239370b6f82a27e142adb8877e8376a98f66c768c96c', 'scripts/eta_spin2_quadrupole_model_2026_09_09.py': '51d0bb9794c5993bc3c955fd1b7ba4d8bede0ec3b2a79e756c50373fcffcd44f'}

def main():
    for path,wanted in EXPECTED_INPUT_SHA256.items():
        actual=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
        if actual!=wanted:
            print(f'FAIL: current input mismatch {path}',flush=True)
            return 1
    rows=evidence.checks(10)
    for name,ok,data in rows:
        print(('PASS' if ok else 'FAIL')+': '+name+' | '+data,flush=True)
    passed=sum(ok for _,ok,_ in rows);failed=len(rows)-passed
    print(f'TOTAL: {passed} passed, {failed} failed',flush=True)
    print('per_element: exact finite matrix, coefficient or probability predicates named above were executed.')
    print('per_site: supplied six-neighbor condition identities only; no generated physical-site update executed.')
    print('per_mode: checked and not executed — no universal momentum or dynamical mode campaign is claimed.')
    print('per_block: finite conditional source, carrier or channel scope is exactly the named predicates above.')
    print('lattice_wide: checked and not executed — no whole-stencil dynamics, infinite history or physical selection is claimed.')
    return 0 if rows and failed==0 else 1

if __name__=='__main__':
    sys.exit(main())
