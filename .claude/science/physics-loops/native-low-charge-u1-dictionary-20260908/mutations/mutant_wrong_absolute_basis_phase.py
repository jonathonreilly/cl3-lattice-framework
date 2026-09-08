"""Portable original finite controls, with optimization-safe predicates."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md', 'docs/THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md')
import argparse,time,signal,resource,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
_started=time.monotonic()
if __name__ == '__main__':
    signal.alarm(AUDIT_TIMEOUT_SEC)
    _parser=argparse.ArgumentParser();_parser.add_argument('--json',action='store_true');_parser.parse_args()
_predicates=0
def require(value,message):
    global _predicates
    _predicates+=1
    if not value:raise RuntimeError(message)
import pathlib, json
count = 0
old_failures = 0
for m in range(1, 9):
    for subset in range(1 << m):
        I = [i for i in range(m) if subset >> i & 1]
        b = (1 << m) - 1
        sign = 1
        for i in reversed(I):
            sign *= (-1) ** (b & (1 << i) - 1).bit_count()
            b ^= 1 << i
        require(not (b != (1 << m) - 1 ^ subset or sign != (-1) ** (sum(I)-len(I)*(len(I)-1)//2)), 'original guard line 7')
        old_failures += sign != (-1) ** (sum(I) - len(I) * (len(I) - 1) // 2)
        count += 1
require(not not old_failures, 'original guard line 9')
out = {'absolute_basis_columns': count, 'old_identity_failures': old_failures, 'correct_s0': '(-1)^sumI', 'tested_map_optional_block_phase': '(-1)^[D(D-1)/2]', 'PASS': True}

_elapsed=time.monotonic()-_started
_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
require(_elapsed<180 and 0<_rss<384,'portable resources')
out['executed_predicates']=_predicates
out['portable_seconds']=_elapsed
out['portable_rss_mib']=_rss
print(json.dumps(out,indent=2,allow_nan=False))
