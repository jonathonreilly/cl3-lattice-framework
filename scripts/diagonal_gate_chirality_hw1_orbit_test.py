#!/usr/bin/env python3
"""Three-label Gamma anticommutation in explicitly distinct domains.
The simultaneous equivariance identity holds for real and complex matrices.
The real-symmetric zero-diagonal slice is zero. A complex Hermitian pure-hop
counterexample is checked explicitly. Physical chirality is not identified.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.linalg import null_space

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs" / "DIAGONAL_GATE_CHIRALITY_HW1_ORBIT_TEST_NOTE_2026-06-04.md"


AUDIT_INPUT_PATHS = ('docs/DIAGONAL_GATE_CHIRALITY_HW1_ORBIT_TEST_NOTE_2026-06-04.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md')
INPUT_SHA256 = {'docs/DIAGONAL_GATE_CHIRALITY_HW1_ORBIT_TEST_NOTE_2026-06-04.md': '122370d871e55fc4a83a3976e5540c23b62dcd922011d088283f4479d80c4cda', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md': '246d2896378034c89fc472a61cb9dbcdec59a733bb4ee8e6a1a6b80b2e73b3ab'}


def require_inputs():
    """Fail before science if the current publication/premise bytes have drifted."""
    import hashlib
    for relative in AUDIT_INPUT_PATHS:
        path = REPO_ROOT / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != INPUT_SHA256[relative]:
            print(f"INPUT_MISMATCH {relative}")
            return False
    return True

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def close(a, b, atol=1e-9):
    return np.allclose(a, b, atol=atol)


R = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)  # cyclic shift
J = np.ones((3, 3), dtype=float)
I3 = np.eye(3, dtype=float)
GAMMA = (2.0 / 3.0) * J - I3  # Γ_χ


def anticomm(M):
    return M @ GAMMA + GAMMA @ M


def comm(M, N):
    return M @ N - N @ M


def solution_dim_and_basis(basis_mats):
    """dim and representatives of {sum c_k B_k : {M,Γ}=0} within span(basis)."""
    cols = [anticomm(B).ravel() for B in basis_mats]
    Mmap = np.array(cols).T  # image columns
    ns = null_space(Mmap, rcond=1e-9)
    reps = []
    for j in range(ns.shape[1]):
        M = sum(ns[k, j] * basis_mats[k] for k in range(len(basis_mats)))
        reps.append(M)
    return ns.shape[1], reps


def complex_pure_hop():
    u = np.array([1, 1, 1], dtype=complex)
    v = np.array([1, -1, 0], dtype=complex)
    return 1j * (np.outer(u, v) - np.outer(v, u))


def complex_counterexample_ok(H):
    return (np.isfinite(H).all() and not close(H, 0) and close(H, H.conj().T)
            and close(np.diag(H), 0) and close(anticomm(H), 0)
            and not close(comm(H, R), 0))


def main() -> int:
    if not require_inputs():
        return 2
    print("=" * 72)
    print("GATE-CHIRALITY: face-diagonal coupling on the abstract hw=1 label orbit")
    print("=" * 72)

    # ---- R and Γ_χ basics --------------------------------------------------
    record("R is the cyclic 3-shift with R^3 = I", close(np.linalg.matrix_power(R, 3), I3))
    record("Γ_χ = (2/3)J − I", close(GAMMA, (2 / 3) * J - I3))
    record("Γ_χ = (-1/3)I + (2/3)(R + R^2) is a circulant",
           close(GAMMA, (-1 / 3) * I3 + (2 / 3) * (R + R @ R)))
    record("Γ_χ^2 = I", close(GAMMA @ GAMMA, I3))
    record("Γ_χ eigenvalues are {+1, -1, -1}", sorted(np.round(np.linalg.eigvalsh(GAMMA), 6)) == [-1.0, -1.0, 1.0])
    record("trace Γ_χ = -1", abs(np.trace(GAMMA) + 1) < 1e-9)
    record("[Γ_χ, R] = 0 (Γ_χ commutes with the C_3 shift)", close(comm(GAMMA, R), np.zeros((3, 3))))

    # ---- hw=1 label geometry -----------------------------------------
    hw1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    dists = [sum(x != y for x, y in zip(a, b)) for a, b in combinations(hw1, 2)]
    record("hw=1 labels are pairwise face-diagonal (Hamming distance 2)", dists == [2, 2, 2])
    record("C_3 shift R cycles the three labels (single orbit)",
           close(R @ np.array([1, 0, 0]), np.array([0, 1, 0])))

    # ---- symmetric-matrix bases -------------------------------------------
    def sym_basis():
        b = []
        for i in range(3):
            E = np.zeros((3, 3)); E[i, i] = 1; b.append(E)
        for i, j in combinations(range(3), 2):
            E = np.zeros((3, 3)); E[i, j] = 1; E[j, i] = 1; b.append(E)
        return b

    SYM = sym_basis()                                   # 6-dim Sym(R^3)
    SYM_CIRC = [I3, R + R @ R]                           # symmetric circulants (comm(R)∩Sym), 2-dim
    OFFDIAG = SYM[3:]                                    # zero-diagonal symmetric (pure face-diagonal hops), 3-dim

    record("Sym(R^3) basis has dimension 6", len(SYM) == 6)
    record("symmetric circulants {I, R+R^2} span comm(R)∩Sym (dim 2)",
           all(close(comm(M, R), np.zeros((3, 3))) for M in SYM_CIRC))

    # ---- reproduce the finite identity -------------------------------------
    d_circ, _ = solution_dim_and_basis(SYM_CIRC)
    record("finite real-symmetric intersection reproduced: comm(R)∩anticomm(Γ_χ)∩Sym = {0}", d_circ == 0, f"dim={d_circ}")

    # ---- the full chiral family -------------------------------------------
    d_full, reps_full = solution_dim_and_basis(SYM)
    record("full chiral family anticomm(Γ_χ)∩Sym has dimension 2 (chiral operators exist)",
           d_full == 2, f"dim={d_full}")
    # every chiral operator breaks C_3:
    breaks = all(not close(comm(M, R), np.zeros((3, 3))) for M in reps_full)
    record("computed nonzero real-symmetric basis representatives break C_3-equivariance", breaks)

    # ---- C_3-symmetric face-diagonal coupling is NOT chiral ----------------
    M_sym = R + R @ R   # equal weight on all three (single-orbit) face-diagonals = J - I
    record("equal-weight face-diagonal coupling M_sym = R+R^2 = J−I is a circulant",
           close(comm(M_sym, R), np.zeros((3, 3))))
    record("equal-weight (C_3-symmetric) face-diagonal coupling is NOT chiral ({M_sym,Γ_χ} ≠ 0)",
           not close(anticomm(M_sym), np.zeros((3, 3))))

    # ---- pure face-diagonal (zero-diagonal) chiral slice -------------------
    d_off, reps_off = solution_dim_and_basis(OFFDIAG)
    record("D2: real symmetric zero-diagonal anticommuting slice has required dimension 0",
           d_off == 0, f"dim={d_off}")
    record("D2: the real pure-hop anticommutator map has full column rank 3",
           np.linalg.matrix_rank(np.array([anticomm(B).ravel() for B in OFFDIAG]).T, tol=1e-9) == 3)

    H_complex = complex_pure_hop()
    record("D2: nonzero complex Hermitian zero-diagonal hop anticommutes with Gamma and breaks C3",
           complex_counterexample_ok(H_complex), f"H={H_complex.tolist()}")

    # the equal-weight direction is never chiral
    record("the C_3-symmetric equal-weight direction (1,1,1) on the three face-diagonals is never chiral",
           not close(anticomm(SYM[3] + SYM[4] + SYM[5]), np.zeros((3, 3))))

    # ---- escape hatch (II): qubit-factor grading is a DIFFERENT object -----
    # gate asks for Γ_χ on the label R^3 factor; a qubit-factor grading lives elsewhere.
    Gamma_gen = np.kron(GAMMA, np.eye(2))           # the gate's grading, on the label factor
    sigma_z = np.array([[1, 0], [0, -1]], dtype=float)
    gamma_qubit = np.kron(np.eye(3), sigma_z)       # a grading on the qubit factor
    record("escape (II): qubit-factor grading I_3⊗σ_z differs from the gate's Γ_χ⊗I_2",
           not close(Gamma_gen, gamma_qubit))
    record("escape (II): the two gradings commute (live on different tensor factors)",
           close(comm(Gamma_gen, gamma_qubit), np.zeros((6, 6))))
    # a label-trivial qubit operator I_3⊗σ_x anticommutes with the qubit grading but is
    # NOT what GATE-CHIRALITY asks (Γ_χ on the label factor). It is the previous
    # finite identity §4 "separate factor" route, which is OPEN and a different construction.
    sigma_x = np.array([[0, 1], [1, 0]], dtype=float)
    qmass = np.kron(np.eye(3), sigma_x)
    record("escape (II) is a different (open) construction, not Γ_χ on the label factor",
           close(qmass @ gamma_qubit + gamma_qubit @ qmass, np.zeros((6, 6)))
           and not close(qmass @ Gamma_gen + Gamma_gen @ qmass, np.zeros((6, 6))))

    # ---- verdict-supporting statement -------------------------------------
    record("the tested simultaneous real equivariance/anticommutation slice remains zero",
           d_circ == 0 and close(GAMMA @ GAMMA, I3))

    # ---- source-note firewalls --------------------------------------------
    if NOTE.exists():
        text = " ".join(NOTE.read_text(encoding="utf-8").split())
        for phrase in [
            "does not change axioms",
            "real symmetric",
            "Complex Hermitian counterexample",
            "Physical chirality",
        ]:
            record(f"publication text check: {phrase!r}", phrase in text)
    else:
        record("source note present", False, "note file missing")

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"TOTAL: {PASS} passed, {FAIL} failed")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
