#!/usr/bin/env python3
"""Bounded consistency diagnostic on six inert, exact historical receipts.

No production imports, execution, downloads, data evaluation or new sampling.
A successful run validates this diagnostic, not the failed historical physics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re

for _thread_env in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[_thread_env] = '1'
import numpy as np

AUDIT_INPUT_PATHS = (
    'docs/SPIN_HALF_CUBIC_ICE_SOURCE_RECEIPT_DIAGNOSTIC_NOTE_2026-09-07.md',
    'docs/SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07.md',
    'data/field/spin_half_cubic_ice_historical_receipts_2026_09_07.json',
)
AUDIT_TIMEOUT_SEC = 120
FIXTURE_SHA256 = 'd2af311b8fd4f1b5bef0f026f3b0e7fdda26faee95f49a1ab0f0f9124293c665'
SOURCE_FAMILIES = {
    'projector': 'electric_flux_projector', 'charge': 'electric_charge_response',
    'magnetic': 'checkerboard_cartesian_response',
    'late_time': 'transverse_electric_spectrum', 'infrared': 'transverse_electric_spectrum',
    'replay': 'transverse_electric_spectrum',
}
HEADER_KEYS = ('runner', 'runner_sha256', 'input_fingerprint_sha256', 'timeout_sec',
               'exit_code', 'elapsed_sec', 'status')
NUMBER = r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
CONTRAST = np.array([[-1., 1., 0.], [-1., 0., 1.]])


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'duplicate JSON key: ' + key)
        result[key] = value
    return result


def finite_number(text):
    require(re.fullmatch(NUMBER, text) is not None, 'malformed or nonfinite number')
    value = float(text)
    require(math.isfinite(value), 'nonfinite number')
    return value


def canonical_envelope(payload, record):
    """One ordered header and stdout/stderr envelope; no success-substring search."""
    lines = payload.splitlines()
    require(len(lines) >= 10 and lines[0] == '===== runner cache v1 =====', 'canonical header missing')
    for marker in ('===== runner cache v1 =====', '----- stdout -----', '----- stderr -----'):
        require(lines.count(marker) == 1, 'duplicate or absent envelope marker')
    require(lines[8] == '----- stdout -----', 'malformed ordered header')
    header = {}
    for key, line in zip(HEADER_KEYS, lines[1:8]):
        require(line.startswith(key + ': '), 'malformed ordered header key')
        header[key] = line[len(key) + 2:]
    for line in lines[9:]:
        require(not any(line.startswith(k + ':') for k in HEADER_KEYS),
                'appended or duplicated header token')
    split = lines.index('----- stderr -----')
    require(split > 8, 'invalid envelope order')
    stdout = lines[9:split]
    totals = [line for line in lines if line.startswith('TOTAL:')]
    require(len(totals) == 1 and totals[0] in stdout, 'duplicate or absent stdout total')
    total = re.fullmatch(r'TOTAL: PASS=(\d+) FAIL=(\d+)', totals[0])
    require(total is not None, 'malformed total')
    passed, failed = map(int, total.groups())
    require(sum(line.startswith('[PASS] ') for line in stdout) == passed and
            sum(line.startswith('[FAIL] ') for line in stdout) == failed, 'total/check count mismatch')
    require(header['status'] in ('ok', 'nonzero_exit'), 'unsupported historical status')
    require(header['exit_code'] == ('0' if header['status'] == 'ok' else '1'), 'status/exit mismatch')
    require((failed == 0) == (header['status'] == 'ok'), 'status/total mismatch')
    require(finite_number(header['elapsed_sec']) >= 0 and
            finite_number(header['timeout_sec']) > 0, 'invalid historical timing')
    require(header['runner'] == record['producer']['path'] and
            header['runner_sha256'] == record['producer']['sha256'], 'producer identity mismatch')
    require(header['input_fingerprint_sha256'] == record['historical_header_input_fingerprint_sha256'],
            'historical input identity mismatch')
    # Post-total recovery scope annotations are preserved by the exact payload
    # hash below; they cannot replace the unique status or total above.
    return {'header': header, 'stdout': stdout, 'passed': passed, 'failed': failed,
            'elapsed_exceeds_declared_timeout': float(header['elapsed_sec']) > float(header['timeout_sec'])}


def parse_paired_row(line, protocol):
    match = re.fullmatch(r'PAIRED_ROW V=(1\.00|0\.95) L=(16|18) window=(2-6|8-14) gaps=(\S+) cov=(\S+)', line)
    require(match is not None, 'malformed paired row')
    v, length, window, gap_text, cov_text = match.groups()
    triples = []
    for text in gap_text.split(','):
        item = re.fullmatch(r'(\d+):(' + NUMBER + r')\+/-(' + NUMBER + ')', text)
        require(item is not None, 'malformed gap endpoint')
        endpoint, gap, error = item.groups()
        triples.append((int(endpoint), finite_number(gap), finite_number(error)))
    require([x[0] for x in triples] == protocol['forward_lengths'], 'duplicate, missing or reordered endpoint')
    gaps = np.array([x[1] for x in triples]); errors = np.array([x[2] for x in triples])
    require(np.all(gaps > 0) and np.all(errors > 0), 'nonpositive gap/error')
    entries = [finite_number(x) for x in cov_text.split(',')]
    require(len(entries) == 9, 'covariance requires nine entries')
    covariance = np.array(entries).reshape(3, 3)
    tolerance = protocol['covariance_absolute_tolerance'] + protocol['covariance_relative_tolerance'] * np.max(abs(covariance))
    require(np.max(abs(covariance - covariance.T)) <= tolerance, 'asymmetric covariance')
    require(np.linalg.eigvalsh(covariance).min() >= -tolerance, 'non-PSD covariance')
    require(np.all(np.diag(covariance) > 0), 'nonpositive covariance diagonal')
    require(np.max(abs(np.sqrt(np.diag(covariance)) - errors)) <=
            protocol['gap_error_printing_absolute_tolerance'], 'printed error/covariance mismatch')
    difference = CONTRAST @ gaps
    contrast_covariance = CONTRAST @ covariance @ CONTRAST.T
    if v == '1.00':
        require(np.max(abs(gaps - gaps[0])) == 0 and
                np.max(abs(covariance - covariance[0, 0])) <= tolerance, 'RK identity mismatch')
        # The exact common-mode identity has zero contrast covariance. No inverse.
        hotelling, student, rk_identity = None, None, True
    else:
        require(np.linalg.eigvalsh(contrast_covariance).min() > 4 * tolerance,
                'singular detuned contrast covariance')
        hotelling = float(difference @ np.linalg.solve(contrast_covariance, difference))
        student = float(np.max(abs(difference) / np.sqrt(np.diag(contrast_covariance))))
        rk_identity = False
    span = float((gaps.max() - gaps.min()) / gaps.mean())
    return {'V': float(v), 'L': int(length), 'window': window, 'gaps': gaps.tolist(),
            'errors': errors.tolist(), 'covariance': covariance.tolist(),
            'contrasts': difference.tolist(), 'contrast_covariance': contrast_covariance.tolist(),
            'hotelling_diagnostic': hotelling, 'student_diagnostic': student,
            'relative_span': span, 'rk_identity': rk_identity,
            'significance_cutoffs_pass': rk_identity or (hotelling < protocol['hotelling_strict'] and student < protocol['student_strict']),
            'span_cutoff_pass': span < protocol['relative_span_strict']}


def replay_rows(stdout, protocol):
    rows, health, replicas = {}, {}, set()
    for line in stdout:
        if line.startswith('PAIRED_ROW'):
            row = parse_paired_row(line, protocol)
            key = (row['V'], row['L'], row['window'])
            require(key not in rows, 'duplicate paired row')
            rows[key] = row
        elif line.startswith('ROW_HEALTH'):
            m = re.fullmatch(r'ROW_HEALTH V=(1\.00|0\.95) L=(16|18) min_ess=(' + NUMBER + r') min_origin_tau16=(\d+) min_forward=(\d+)', line)
            require(m is not None, 'malformed health row')
            v, length, ess, origin, forward = m.groups(); key = (float(v), int(length))
            require(key not in health, 'duplicate health row')
            health[key] = {'V': key[0], 'L': key[1], 'min_ess': finite_number(ess),
                           'min_origin_count': int(origin), 'min_forward_count': int(forward)}
        elif line.startswith('REPLICA_DONE'):
            m = re.fullmatch(r'REPLICA_DONE V=(1\.00|0\.95) L=(16|18) replica=([1-6])/6', line)
            require(m is not None, 'malformed replica endpoint')
            v, length, replica = m.groups(); key = (float(v), int(length), int(replica))
            require(key not in replicas, 'duplicate replica endpoint')
            replicas.add(key)
    keys = {(v, length) for v in protocol['couplings'] for length in protocol['lengths']}
    require(set(health) == keys, 'incomplete health rows')
    require(set(rows) == {(*key, f'{a}-{b}') for key in keys for a, b in protocol['windows']}, 'incomplete paired rows')
    require(replicas == {(*key, replica) for key in keys for replica in range(1, protocol['replicas'] + 1)}, 'incomplete replica endpoints')
    certificates = [s for s in stdout if s.startswith('CERTIFICATE:')]
    require(certificates == ['CERTIFICATE: lower_momenta=L16,L18 replicas=6 detuned_population=6144 rk_population=1536 paired_forward_lengths=6,12,20 measurement_origins=4 primary_window=8-14 finite_volume=True thermodynamic_limit=False'], 'certificate identity mismatch')
    return list(rows.values()), list(health.values())


def source_guard(actual_family, required_family):
    return actual_family == required_family


def statistical_guard(rows, health, producer_ok, protocol):
    primary = [r for r in rows if r['V'] == .95 and r['window'] == '8-14']
    require(len(primary) == 2 and {r['L'] for r in primary} == {16, 18}, 'incomplete primary rows')
    genealogy = all(h['min_ess'] > protocol['min_ess_strict'] and
                    h['min_origin_count'] >= protocol['min_origin_count'] and
                    h['min_forward_count'] >= protocol['min_forward_count'] for h in health)
    span = all(r['span_cutoff_pass'] for r in primary)
    significance = all(r['significance_cutoffs_pass'] for r in primary)
    return {'historical_producer_ok': producer_ok, 'genealogy_pass': genealogy,
            'primary_span_pass': span, 'primary_significance_cutoffs_pass': significance,
            'eligible_under_fixed_protocol': producer_ok and genealogy and span and significance,
            'coverage': 'predeclared diagnostic cutoffs; no calibrated confidence coverage asserted'}


def validate_fixture(data):
    records = data['records']
    require(data['schema'] == 'spin-half-ice-historical-receipts-v1', 'fixture schema mismatch')
    require(len(records) == 6 and {r['id'] for r in records} == set(SOURCE_FAMILIES), 'record identity set mismatch')
    envelopes = {}
    for record in records:
        require(record['source_family'] == SOURCE_FAMILIES[record['id']], 'source family identity mismatch')
        envelope = canonical_envelope(record['payload'], record)
        envelopes[record['id']] = envelope
    replay = envelopes['replay']
    rows, health = replay_rows(replay['stdout'], data['protocol'])
    for record in records:
        body = record['payload'].encode('utf-8')
        require(len(body) == record['capture']['bytes'] and sha256(body) == record['capture']['sha256'], 'historical payload identity mismatch')
    return envelopes, rows, health


def load_fixture(path):
    raw = path.read_bytes()
    data = json.loads(raw, object_pairs_hook=unique_object,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError('nonfinite JSON constant')))
    # Structural/covariance checks run before the final immutable fixture pin,
    # so actual adverse files exercise those guards, not only a checksum fence.
    result = validate_fixture(data)
    require(sha256(raw) == FIXTURE_SHA256, 'frozen fixture identity mismatch')
    return data, result


def historical_benchmark(envelopes):
    charge = [line for line in envelopes['charge']['stdout'] if line.startswith('AXIAL_FIT V=0.95 ')]
    magnetic = [line for line in envelopes['magnetic']['stdout'] if line.startswith('SUMMARY V=0.95 ')]
    require(len(charge) == len(magnetic) == 1, 'benchmark row identity mismatch')
    u = re.search(r'U_charge=(' + NUMBER + r')\+/-(' + NUMBER + r').*U_flux=(' + NUMBER + ')', charge[0])
    k = re.search(r'K=(' + NUMBER + r')\+/-(' + NUMBER + ')', magnetic[0])
    require(u is not None and k is not None, 'malformed benchmark estimator')
    u_charge, charge_error, u_flux = map(finite_number, u.groups())
    k_value, k_error = map(finite_number, k.groups())
    return {'U_flux': u_flux, 'U_charge': u_charge, 'borrowed_U_charge_error': charge_error,
            'checkerboard_K': k_value, 'checkerboard_K_error': k_error,
            'historical_product': u_flux * k_value,
            'historical_hybrid_error': math.hypot(u_flux * k_error, k_value * charge_error),
            'U_flux_uncertainty_supplied': False, 'hybrid_uncertainty_resolved': False,
            'scope': 'historical arithmetic only; neither uniform-source UK nor a physical prediction'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path, help='Optional structured diagnostic output')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    before = {p: sha256((root / p).read_bytes()) for p in AUDIT_INPUT_PATHS}
    data, (envelopes, rows, health) = load_fixture(root / AUDIT_INPUT_PATHS[2])
    statistical = statistical_guard(rows, health, envelopes['replay']['header']['status'] == 'ok', data['protocol'])
    matched = source_guard(SOURCE_FAMILIES['magnetic'], data['required_physical_source_family'])
    benchmark = historical_benchmark(envelopes)
    # This diagnostic deliberately cannot mint a physical certificate from
    # historical checks, even on a hypothetical all-green statistical fixture.
    result = {'diagnostic_consistency_pass': True, 'physical_certificate': False,
              'source_match': matched, 'statistics': statistical,
              'historical_benchmark': benchmark, 'paired_rows': rows, 'health': health,
              'historical_statuses': {key: {k: value[k] for k in ('header', 'passed', 'failed', 'elapsed_exceeds_declared_timeout')}
                                      for key, value in envelopes.items()},
              'bound_inputs_sha256': before,
              'input_provenance': {r['id']: {'snapshot_inputs_match_historical_header': r['snapshot_inputs_match_historical_header'],
                                            'scope': r['input_scope']} for r in data['records']}}
    checks = [
        (not matched, 'checkerboard historical response fails uniform source guard'),
        (not statistical['historical_producer_ok'], 'historical replay exit remains failed'),
        (not statistical['genealogy_pass'], 'fixed genealogy floor still fails'),
        (not statistical['primary_span_pass'], 'both primary spans are tested against fixed 0.05'),
        (statistical['primary_significance_cutoffs_pass'], 'paired significance diagnostics pass without a coverage assertion'),
        (not statistical['eligible_under_fixed_protocol'], 'statistical guard independently rejects unchanged replay'),
        (sum(r['rk_identity'] for r in rows) == 4, 'four singular RK common-mode controls require no inverse'),
        (all(not r['span_cutoff_pass'] for r in rows if r['V'] == .95 and r['window'] == '8-14'), 'both detuned primary spans exceed 0.05'),
        (not benchmark['hybrid_uncertainty_resolved'], 'electric uncertainty remains an unresolved hybrid'),
        (abs(benchmark['historical_product'] - .012289089918) < 1e-16, 'preserved historical benchmark central arithmetic'),
        (abs(benchmark['historical_hybrid_error'] - .0011689942811097837) < 1e-16, 'preserved historical hybrid arithmetic'),
        (not result['physical_certificate'], 'diagnostic success grants no physical certificate'),
    ]
    for ok, label in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    after = {p: sha256((root / p).read_bytes()) for p in AUDIT_INPUT_PATHS}
    require(before == after, 'declared input changed during diagnostic')
    result['checks_passed'] = sum(bool(ok) for ok, _ in checks)
    result['checks_failed'] = len(checks) - result['checks_passed']
    print(json.dumps(result, sort_keys=True, indent=2, allow_nan=False))
    if args.json:
        args.json.write_text(json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + '\n')
    print(f"TOTAL: PASS={result['checks_passed']} FAIL={result['checks_failed']}")
    return int(result['checks_failed'] != 0)


if __name__ == '__main__':
    raise SystemExit(main())
