"""Focused independent operands for the exact-domain and tensor-order repairs."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import numpy as np
import law_tournament_6266_6275_model as model

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/SIGNED_RECORD_FINITE_REFINEMENT_AND_CONDITIONAL_SOURCE_6266_BOUNDED_THEOREM_NOTE_2026-09-09.md', 'docs/RECORD_LAW_EXACT_DOMAIN_AND_CHANNEL_BRIDGE_6275_BOUNDED_THEOREM_NOTE_2026-09-09.md', 'scripts/law_tournament_6266_6275_model.py', 'scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py', 'scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py', '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md', '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md', 'docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md', 'docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
INPUT_SHA256 = {'docs/SIGNED_RECORD_FINITE_REFINEMENT_AND_CONDITIONAL_SOURCE_6266_BOUNDED_THEOREM_NOTE_2026-09-09.md': '4923f614fe704b87f54d1549f3f77900ced51d47cb3f2350bb012347741b4aa0', 'docs/RECORD_LAW_EXACT_DOMAIN_AND_CHANNEL_BRIDGE_6275_BOUNDED_THEOREM_NOTE_2026-09-09.md': 'ccf6f8215c5f82898a31d0972d878a7f00ddecef0724fe50ca713ba492242006', 'scripts/law_tournament_6266_6275_model.py': '3e5f858d6e0c37bdb57798fca398883330017b17c26498208a357939d8233077', 'scripts/admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_2026_08_12.py': '6952a8bf9badcf0a546a024b365d8238376305014ad6755f06db6bfa45fee848', 'scripts/admissibility_strict_nearest_neighbor_state_dependent_record_born_history_single_front_2026_08_12.py': '9e8dafb2f8916340e2131814340518cc64c42d418f78605845c782cef551916a', '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md': '70c0cbe91e079e20111875b26589556dd21c197ade4638512ecd5070bb3e073e', '.claude/science/physics-loops/backlog-dk-os-6377-correction-20260908/provenance/docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md': 'aec5700bca3f148c67ff27948e045afaa0ca861d7b29ae16608e890c08b89235', 'docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md': 'b6b4e25cbdc3b87e5ee8db841b7378e8ea900dee09cf02c993ebb0b823dd4fb4', 'docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md': '1851b00670be98cf4a5f22536ee1f95fd73c7066f5693d4209f43aa439b89ae2', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}
ROOT = Path(__file__).resolve().parents[1]


def input_guard():
    for path, expected in INPUT_SHA256.items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest() != expected:
            raise RuntimeError('input identity mismatch: '+path)


def baseline_domain_acceptance(candidate):
    return model.density4(candidate)


def main():
    input_guard(); results = []
    def check(label, ok, detail):
        results.append(bool(ok));print(('PASS ' if ok else 'FAIL ')+label+': '+detail)
    epsilon = F(1,10**13)
    # Reviewer counterexamples differ in actual exact matrix operands.
    bad_psd = model.diagonal((1+epsilon,0,-epsilon,0))
    bad_trace = model.diagonal((1+epsilon,0,0,0))
    clean = model.diagonal((1,0,0,0))
    check('exact-boundary', baseline_domain_acceptance(clean)
          and not baseline_domain_acceptance(bad_psd) and not baseline_domain_acceptance(bad_trace),
          'rank-one boundary accepted; actual negative eigenweight and excess trace rejected exactly')
    # All diagonal entries are positive; a non-leading principal minor is negative.
    off = [list(row) for row in model.diagonal((F(1,4),)*4)]
    off[1][3] = off[3][1] = model.b63.z(F(1,3))
    malformed = [list(row) for row in clean];malformed[0][1] = model.ONE
    floating = [list(row) for row in clean];floating[0][0] = model.b63.ExactComplex(1.0,0)
    check('nonleading-minor-and-type', not baseline_domain_acceptance(off)
          and not baseline_domain_acceptance(malformed) and not baseline_domain_acceptance(floating),
          'nonleading 2x2 determinant -7/144, non-Hermitian and float operands refused')
    # Exact complex rank-one density, with zeros in effects allowed.
    c = model.b63.ExactComplex
    pure = [[model.Z for _ in range(4)] for _ in range(4)]
    pure[0][0]=pure[3][3]=model.b63.z(F(1,2));pure[0][3]=c(0,-F(1,2));pure[3][0]=c(0,F(1,2))
    check('complex-rank-one', baseline_domain_acceptance(pure)
          and sum(model.weights(pure,model.R0),F(0)) == 1,
          'exact imaginary coherence and singular PSD boundary retained')
    # Independent sparse column interpretation for all canonical input units.
    w = model.dilation()
    columns = ({0:1}, {2:1}, {1:np.sqrt(.5),5:np.sqrt(5/14),29:np.sqrt(1/7)},
               {3:np.sqrt(1/7),27:np.sqrt(2/35),15:np.sqrt(4/5)})
    reference = np.zeros_like(w)
    for col, entries in enumerate(columns):
        for row,value in entries.items():reference[row,col]=value
    check('explicit-permuted-columns', np.max(np.abs(w-reference)) < 1e-14
          and np.max(np.abs(w.conj().T@w-np.eye(4))) < 1e-14,
          'a=2P+M canonical columns independently reconstructed; isometry')
    clean_residual=model.channel_residual();broken_residual=model.channel_residual(bridge=False)
    check('changed-basis-operand', clean_residual < 1e-12 and not broken_residual < 1e-12,
          f'same 16-unit/5-branch plus coarse comparator: bridge {clean_residual:.3g}, omitted bridge {broken_residual:.3g}')
    print(f'TOTAL: PASS={sum(results)} FAIL={len(results)-sum(results)}')
    return int(not all(results))


if __name__ == '__main__':
    raise SystemExit(main())
