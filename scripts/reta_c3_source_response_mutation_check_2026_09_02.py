#!/usr/bin/env python3
"""Three actual source-operand controls, sharing primary predicates.

A clean focused baseline is required. Only a failure at the target predicate
with the other two predicates passing earns attribution. No unrelated child
failure, forced Boolean, or historical forty-case quota is counted.
"""
from __future__ import annotations
import hashlib
import sys
import types
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PRIMARY = 'scripts/reta_c3_source_response_spectral_identity_2026_09_02.py'
AUDIT_TIMEOUT_SEC = 150
AUDIT_INPUT_PATHS = ('scripts/reta_c3_source_response_spectral_identity_2026_09_02.py',
 'docs/AC_RETA_C3_SOURCE_RESPONSE_SPECTRAL_IDENTITY_TYPE_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md',
 'archive/notes/docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md',
 'archive/notes/docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md',
 'archive/notes/docs/ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md',
 'docs/KOIDE_A1_O13_CHEEGER_SIMONS_RZ_NO_GO_NOTE_2026-04-24.md',
 'docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md',
 'scripts/frontier_koide_a1_cheeger_simons_rz_probe.py')
INPUT_SHA256 = {'scripts/reta_c3_source_response_spectral_identity_2026_09_02.py': '2b9f946d685f46fbd9f23e5e50e20b89731fd6f964daedf5f584721be20bf293',
 'docs/AC_RETA_C3_SOURCE_RESPONSE_SPECTRAL_IDENTITY_TYPE_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md': '8bb07f6e65a9e146d94504798bbb01175429ee78fac971588600fb417cb86530',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md': '4d742bcc68a1e7cdb154b366e671f576e9b719b3206445b97666c812a790e58c',
 'archive/notes/docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md': '08c15bdc0c2fc2ccd750ca2752260ae02ec2521a70bc0307103c42058a63ed09',
 'archive/notes/docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md': '83f4ab11435b7f5224c1013768dc56c28dfb56f0ab3fdd5811f9b06251dde665',
 'archive/notes/docs/ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md': '29d97d9abf35e870e7fbff2ad81810deef89dbb9ea6d92fcf7ba147ea5796d69',
 'docs/KOIDE_A1_O13_CHEEGER_SIMONS_RZ_NO_GO_NOTE_2026-04-24.md': '793175beb13915457722519668524d50b20cee4cadce6646bfaae4ccd3148744',
 'docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md': '88ad09bf68eeba52d1978e3ee46d3bb902c60145b929985db4518f72e2b6500a',
 'scripts/frontier_koide_a1_cheeger_simons_rz_probe.py': '93043e5dc4346a512c72ca86bc4865babb5af58385f10f8863f09bfe45339d64'}

CASES = (
    ("Fourier normalization", "projector / 3", "projector / 2"),
    ("log derivative distinguished", "sp.diff(sp.log(determinant), source)", "sp.diff(determinant, source)"),
    ("Hodge order on x", "second = exterior_derivative(hodge_star(form))", "second = hodge_star(exterior_derivative(form))"),
)


def require_inputs(root=ROOT):
    for rel, expected in INPUT_SHA256.items():
        path = root / rel
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f"missing or changed declared input: {rel}")


def evaluate(source, name):
    module = types.ModuleType(name)
    module.__file__ = str(ROOT / PRIMARY)
    sys.modules[name] = module
    try:
        exec(compile(source, module.__file__, "exec"), module.__dict__)
        return module.focused_checks()
    finally:
        del sys.modules[name]


def attributable(baseline, changed, target):
    return (bool(baseline) and all(baseline.values()) and target in baseline
            and set(changed) == set(baseline) and not changed[target]
            and all(value for key, value in changed.items() if key != target))


def main():
    try:
        require_inputs()
        source = (ROOT / PRIMARY).read_text()
        baseline = evaluate(source, "c3_clean")
        if not baseline or not all(baseline.values()):
            print(f"CLEAN_BASELINE_FAILED {baseline}")
            return 1
        print(f"CLEAN_BASELINE {baseline}")
        passed = 1
        for index, (target, old, new) in enumerate(CASES):
            if source.count(old) != 1:
                raise ValueError(f"source operand is not unique: {old}")
            changed_source = source.replace(old, new, 1)
            changed = evaluate(changed_source, f"c3_changed_{index}")
            ok = attributable(baseline, changed, target)
            print(f"{'PASS' if ok else 'FAIL'} {target}: {changed}; source_sha256={hashlib.sha256(changed_source.encode()).hexdigest()}")
            passed += int(ok)
        print(f"TOTAL: PASS={passed} FAIL={4-passed}")
        return 0 if passed == 4 else 1
    except Exception as exc:
        print(f"CONTROL_ERROR: {type(exc).__name__}: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
