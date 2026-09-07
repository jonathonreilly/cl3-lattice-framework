#!/usr/bin/env python3
"""Conditional Cartesian plaquette-source checks; no repository science imports.

The root-major bit construction and full spectral response sum were authored
by the field scout before reading the independent axis-major/bordered-solve
checker. This packaged runner adds source-rephasing and flux-endpoint checks.
No large-volume Monte Carlo or thermodynamic limit is performed.
"""
from __future__ import annotations

import argparse
import json
from collections import deque
from itertools import combinations, product
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh

AUDIT_INPUT_PATHS = ()
AUDIT_TIMEOUT_SEC = 120
AXES = tuple(combinations(range(3), 2))
BOUNDARY = np.array([1, 1, -1, -1], dtype=np.int64)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, condition: bool, label: str) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def parity(root) -> int:
    return (-1) ** sum(root)


def geometry(length: int):
    roots = tuple(product(range(length), repeat=3))
    links = tuple((root, axis) for root in roots for axis in range(3))
    index = {link: position for position, link in enumerate(links)}
    faces = []
    for orientation, (a, b) in enumerate(AXES):
        for root in roots:
            ra, rb = list(root), list(root)
            ra[a] = (ra[a] + 1) % length
            rb[b] = (rb[b] + 1) % length
            boundary_links = ((root, a), (tuple(ra), b), (tuple(rb), a), (root, b))
            ids = tuple(index[link] for link in boundary_links)
            faces.append((root, orientation, ids, sum(1 << i for i in ids)))
    return links, faces


def component():
    links, faces = geometry(2)

    def moves(state):
        for face, (_, _, ids, mask) in enumerate(faces):
            bits = [(state >> i) & 1 for i in ids]
            if bits[0] == bits[2] and bits[1] == bits[3] and bits[0] != bits[1]:
                yield state ^ mask, face, 2 * bits[0] - 1

    start = sum(1 << i for i, (root, axis) in enumerate(links) if root[axis] % 2)
    states, index, queue, arcs = [start], {start: 0}, deque([start]), []
    while queue:
        state = queue.popleft()
        for destination, face, sign in moves(state):
            if destination not in index:
                index[destination] = len(states)
                states.append(destination)
                queue.append(destination)
            arcs.append((index[state], index[destination], face, sign))
    return links, faces, states, np.asarray(arcs, dtype=np.int64)


def local_algebra(length: int) -> tuple[int, int]:
    links, faces = geometry(length)
    cases, failures = 0, 0
    for root, _, ids, _ in faces:
        for sign in (-1, 1):
            actual = np.array([parity(links[i][0]) for i in ids]) * [-sign, sign, -sign, sign]
            expected = -parity(root) * sign * BOUNDARY
            failures += not np.array_equal(actual, expected)
            cases += 1
    return cases, int(failures)


def trace_derivative_four(h, b, c) -> int:
    """H'=i B and H''=C. Exact integer product-rule trace derivative."""
    h2 = h @ h
    value = 4 * int((c @ h2 @ h).diagonal().sum())
    value -= 4 * int((b @ b @ h2 + b @ h @ b @ h + b @ h2 @ b).diagonal().sum())
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Optional structured receipt path")
    args = parser.parse_args()
    checks = Checks()
    links, faces, states, arcs = component()
    size, volume = len(states), 8
    rows, columns, face_ids, signs = arcs.T
    counts = np.bincount(rows, minlength=size)
    target = np.array([faces[f][1] == 0 for f in face_ids], dtype=np.int64)
    epsilon = np.array([parity(faces[f][0]) for f in face_ids], dtype=np.int64)
    sources = {"occupation_sign": signs * target, "cartesian_curl": epsilon * signs * target}
    electric = np.array([[parity(root) * (((state >> i) & 1) - .5)
                          for i, (root, _) in enumerate(links)] for state in states])
    checks.check(size == 864 and len(arcs) == 6912, "independent bit orbit: 864 states and 6912 directed moves")
    defect = 0
    for row, column, face, sign in arcs:
        root, _, ids, _ = faces[face]
        expected = -parity(root) * sign * BOUNDARY
        defect = max(defect, int(np.max(abs(electric[column, list(ids)] - electric[row, list(ids)] - expected))))
    checks.check(defect == 0, "electric update equals -epsilon*s*oriented boundary on every move")
    local = {str(length): dict(zip(("cases", "failures"), local_algebra(length))) for length in (2, 4, 6, 3)}
    checks.check(all(local[str(length)]["failures"] == 0 for length in (2, 4, 6)), "even-periodic local identities at every root and both occupation signs")
    checks.check(local["3"]["failures"] > 0, "odd-periodic negative control detects the bipartite seam failure")

    def matrix_source(v, face_source):
        phases = epsilon * signs * np.asarray(face_source)[face_ids]
        off = sparse.coo_matrix((-np.exp(1j * phases), (rows, columns)), shape=(size, size)).tocsr()
        return off + sparse.diags(v * counts, dtype=float)

    def matrix(v, theta, source):
        off = sparse.coo_matrix((-np.exp(1j * theta * sources[source]), (rows, columns)), shape=(size, size)).tocsr()
        return off + sparse.diags(v * counts, dtype=float)

    # Arbitrary rational-coefficient sources and link phases, not only a
    # single field direction or a zero-source rephasing.
    link_a = (np.arange(len(links)) % 7 - 3) / 17
    source_b = (np.arange(len(faces)) % 11 - 5) / 19
    curl_a = np.array([np.dot(link_a[list(ids)], BOUNDARY) for _, _, ids, _ in faces])
    diagonal = sparse.diags(np.exp(1j * (electric @ link_a)))
    conjugation = float(sparse.linalg.norm(matrix_source(.95, source_b + curl_a)
                        - diagonal @ matrix_source(.95, source_b) @ diagonal.conj().T))
    checks.check(conjugation < 1e-11, "arbitrary-source link-rephasing identity H[b+curl(a)]=D H[b] D* at L2")
    pure_curl = float(sparse.linalg.norm(matrix_source(.95, curl_a)
                        - diagonal @ matrix(.95, 0, "cartesian_curl") @ diagonal.conj().T))
    checks.check(pure_curl < 1e-11, "exact-curl source is a basis rotation of zero source")

    theta_quantum = 2 * np.pi / 2**2
    flux_a = np.zeros(len(links))
    for i, (root, axis) in enumerate(links):
        if axis == 1:
            flux_a[i] = theta_quantum * root[0]
        if axis == 0 and root[0] == 1:
            flux_a[i] = -theta_quantum * 2 * root[1]
    flux_rotation = sparse.diags(np.exp(1j * (electric @ flux_a)))
    full_flux_residual = float(sparse.linalg.norm(matrix(.95, theta_quantum, "cartesian_curl")
                         - flux_rotation @ matrix(.95, 0, "cartesian_curl") @ flux_rotation.conj().T))
    checks.check(full_flux_residual < 1e-11, "full uniform-source flux quantum is unitarily equivalent to zero at L2")
    endpoint_local = {}
    for length in (2, 4, 6):
        ls, fs = geometry(length)
        theta = 2 * np.pi / length**2
        a = np.array([theta * root[0] if axis == 1 else
                      -theta * length * root[1] if axis == 0 and root[0] == length - 1 else 0.
                      for root, axis in ls])
        curl = np.array([np.dot(a[list(ids)], BOUNDARY) for _, _, ids, _ in fs])
        uniform = np.array([theta if orientation == 0 else 0. for _, orientation, _, _ in fs])
        endpoint_local[str(length)] = float(np.max(abs(np.exp(1j * curl) - np.exp(1j * uniform))))
    checks.check(max(endpoint_local.values()) < 1e-11, "full-flux seam construction at every plaquette of L2/L4/L6")

    # The local proof does not need a torus: negative-coordinate roots and
    # both choices of ordered axes cover the unwrapped/open local convention.
    unwrapped_cases, unwrapped_failures = 0, 0
    for root in product(range(-2, 3), repeat=3):
        for a, b in product(range(3), repeat=2):
            if a == b:
                continue
            ra, rb = list(root), list(root)
            ra[a] += 1
            rb[b] += 1
            for sign in (-1, 1):
                actual = np.array([parity(root), parity(ra), parity(rb), parity(root)]) * [-sign, sign, -sign, sign]
                unwrapped_failures += not np.array_equal(actual, -parity(root)*sign*BOUNDARY)
                unwrapped_cases += 1
    checks.check(unwrapped_failures == 0, "unwrapped local update and reversed ordered-axis conventions, including negative roots")

    trace_data, response_data = {}, []
    h_integer = matrix(1., 0, "cartesian_curl").real.astype(np.int64)
    for name, source in sources.items():
        b = sparse.coo_matrix((-source, (rows, columns)), shape=(size, size)).tocsr()
        c = sparse.coo_matrix((source * source, (rows, columns)), shape=(size, size)).tocsr()
        trace_data[name] = trace_derivative_four(h_integer, b, c)
        test = matrix(.95, .37, name)
        checks.check(sparse.linalg.norm(test-test.conj().T) == 0, f"{name}: Hermitian at real source")
    checks.check(trace_data == {"occupation_sign": 0, "cartesian_curl": -38912},
                 "exact trace-H4 derivatives distinguish source families (independent Laurent-polynomial cross-check)")
    # Dense spectral sum uses all excited eigenvectors. The separate checker
    # obtains the response from a bordered sparse solve instead.
    for v in (1., .95, .90):
        h = matrix(v, 0, "cartesian_curl").real.toarray()
        eigenvalues, eigenvectors = eigh(h)
        psi = eigenvectors[:, 0]
        gaps = eigenvalues[1:] - eigenvalues[0]
        for name, source in sources.items():
            h1 = sparse.coo_matrix((-1j * source, (rows, columns)), shape=(size, size)).tocsr()
            h2 = sparse.coo_matrix((source * source, (rows, columns)), shape=(size, size)).tocsr()
            amplitudes = eigenvectors[:, 1:].conj().T @ (h1 @ psi)
            bare = float(np.vdot(psi, h2 @ psi).real / volume)
            relaxation = float(2 * np.sum(abs(amplitudes)**2 / gaps) / volume)
            curvature = bare - relaxation
            finite_differences = []
            for theta in (.02, .01):
                energy = eigsh(matrix(v, theta, name), k=1, which="SA", tol=1e-12,
                               v0=np.linspace(1, 2, size), return_eigenvectors=False)[0]
                finite_differences.append(float(2 * (energy-eigenvalues[0]) / (theta**2 * volume)))
            errors = [abs(value-curvature) for value in finite_differences]
            ratio = errors[0] / errors[1]
            checks.check(curvature > 0 and 3.9 < ratio < 4.1,
                         f"V={v:.2f}, {name}: positive finite curvature; independent finite differences converge quadratically")
            row = dict(V=v, source=name, curvature=curvature, bare=bare, relaxation=relaxation,
                       finite_differences_theta_002_001=finite_differences,
                       ground_residual=float(np.linalg.norm(h @ psi-eigenvalues[0]*psi)),
                       smallest_component_gap=float(gaps[0]))
            response_data.append(row)
            print(f"RESPONSE V={v:.2f} source={name} curvature={curvature:.12f} bare={bare:.12f} relaxation={relaxation:.12f}")
    checks.check(all(row["ground_residual"] < 1e-11 and row["smallest_component_gap"] > 0 for row in response_data),
                 "ground-state residuals and finite component gaps justify the response calculation")
    result = dict(states=size, directed_moves=len(arcs), electric_update_defect=defect,
                  local_algebra=local, unwrapped_cases=unwrapped_cases, unwrapped_failures=int(unwrapped_failures),
                  arbitrary_source_conjugation_residual=conjugation,
                  pure_curl_conjugation_residual=pure_curl, full_flux_conjugation_residual=full_flux_residual,
                  full_flux_local_phase_residuals=endpoint_local, trace_H4_second_derivatives=trace_data,
                  curvatures=response_data, passed=checks.passed, failed=checks.failed)
    if args.json:
        args.json.write_text(json.dumps(result, indent=2)+"\n")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
