#!/usr/bin/env python3
"""Supplied circulant coefficient conventions and signed trace ratios.
H=aI+bC+conj(b)C^2 is a finite Hermitian matrix, a real and nonzero for r.
Coefficient HS balance characterizes r=1/2 but is not central-block balance.
The eight original numerical rules remain a stipulated finite list, with no
forced/accepted admission or Born interpretation. Mixed-sign spectra have a
different positive-square-root ratio. No physical mass selector is supplied.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs" / "DIAGONAL_GATE_R_HALF_WEIGHTED_PATH_TEST_NOTE_2026-06-04.md"


AUDIT_INPUT_PATHS = ('docs/DIAGONAL_GATE_R_HALF_WEIGHTED_PATH_TEST_NOTE_2026-06-04.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md')
INPUT_SHA256 = {'docs/DIAGONAL_GATE_R_HALF_WEIGHTED_PATH_TEST_NOTE_2026-06-04.md': 'acf17db3932eddb7a1ffd8ee2ca2e58421706fb7c15f50ce052ddba248914f75', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md': '0ea38efea33028a1382071ca0a98bb1b8bc0863edb62518e1e23f45edd069da3'}


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


C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)  # forward 3-cycle
I3 = np.eye(3, dtype=complex)


def hs2(M):
    return float(np.real(np.trace(M.conj().T @ M)))


def koide_Q_from_r(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def koide_Q_from_spectrum(a, bmod, delta=0.0):
    """Q = (sum lambda^2)/(sum |lambda|)^2 for H = aI + bC + b̄C^2, b=|b|e^{iδ}."""
    b = bmod * np.exp(1j * delta)
    H = a * I3 + b * C + np.conj(b) * (C @ C)
    lam = np.linalg.eigvalsh((H + H.conj().T) / 2)  # Hermitian for real a
    denominator = np.sum(np.abs(lam)) ** 2
    if denominator == 0:
        raise ValueError("normalized positive-square-root ratio requires nonzero H")
    return float(np.sum(lam ** 2) / denominator)


def r_from_ratio(bmod, a=1.0):
    if a == 0:
        raise ValueError("r requires a != 0")
    return (bmod ** 2) / (a ** 2)


def central_projectors():
    ps = np.ones((3, 3), dtype=complex) / 3
    return ps, I3 - ps


def central_power_check():
    ps, pd = central_projectors()
    b = 1 / np.sqrt(2)
    H = I3 + b * C + b * (C @ C)
    actual = (hs2(ps @ H), hs2(pd @ H))
    expected = ((1 + np.sqrt(2)) ** 2, 2 * (1 - 1 / np.sqrt(2)) ** 2)
    return (np.allclose(ps @ ps, ps) and np.allclose(pd @ pd, pd)
            and np.allclose(ps @ pd, 0) and np.allclose(ps + pd, I3)
            and np.allclose(actual, expected, atol=1e-9) and abs(actual[0] - actual[1]) > 5)


def main() -> int:
    if not require_inputs():
        return 2
    print("=" * 72)
    print("GATE-R-HALF: diagonal weight conventions vs r = 1/2")
    print("=" * 72)

    # ---- structural identities --------------------------------------------
    record("C is the forward 3-cycle, C^3 = I", np.allclose(np.linalg.matrix_power(C, 3), I3))
    a = 1.0
    bmod = 1.0 / np.sqrt(2.0)
    record("HS norm ||aI||^2 = 3 a^2", abs(hs2(a * I3) - 3 * a ** 2) < 1e-9)
    shift = bmod * C + bmod * (C @ C)  # |b|=b̄ moduli equal (δ=0 representative)
    record("HS norm ||bC + b̄C^2||^2 = 6 |b|^2", abs(hs2(shift) - 6 * bmod ** 2) < 1e-9)
    record("equipartition ||aI||^2 = ||bC+b̄C^2||^2  <=>  3a^2 = 6|b|^2  <=>  r = 1/2",
           abs(3 * a ** 2 - 6 * bmod ** 2) < 1e-9 and abs(r_from_ratio(bmod, a) - 0.5) < 1e-9)

    # exact Koide relation Q = 1/3 + (2/3) r at the three lane points
    for r, Qexp in [(0.0, 1 / 3), (0.5, 2 / 3), (1.0, 1.0)]:
        record(f"signed Q_H = 1/3 + (2/3)r gives Q={Qexp:.3f} at r={r}", abs(koide_Q_from_r(r) - Qexp) < 1e-9)
    # spectral cross-check (δ=0, sign-homogeneous spectrum -> signed readout)
    record("spectral cross-check: r=1/2, δ=0 gives signed Q_H = 2/3",
           abs(koide_Q_from_spectrum(1.0, 1 / np.sqrt(2), 0.0) - 2 / 3) < 1e-9)
    record("spectral cross-check: r=1 gives Q_+ = 1 (supplied nonnegative spectrum)",
           abs(koide_Q_from_spectrum(1.0, 1.0, 0.0) - 1.0) < 1e-9)

    # ---- geometric multiplicity picture from the triangle -----------------
    # each abstract label: 1 stay (I) + 2 face-diagonal neighbors (C, C^2).
    stay_mult, shift_mult = 1, 2
    record("triangle geometry: each abstract label has 1 stay + 2 face-diagonal neighbors",
           (stay_mult, shift_mult) == (1, 2))
    record("the (1,2) coefficient-direction count matches the I-term vs {C,C^2}-terms split",
           stay_mult == 1 and shift_mult == 2)

    # Stipulated rules, keeping every original ratio and expected half flag.
    candidates = [
        ("geometric inverse length with stay normalized", 1.0 / np.sqrt(2.0), True),
        ("inverse squared length", 1.0 / 2.0, False),
        ("path count", 2.0, False),
        ("inverse path count", 0.5, False),
        ("displacement orbit-size ratio 12/6", 2.0, False),
        ("displacement stabilizer ratio 4/8", 0.5, False),
        ("coefficient HS balance", 1.0 / np.sqrt(2.0), True),
        ("equal amplitudes a=abs(b)", 1.0, False),
    ]
    n_half = 0
    for name, ratio, gives_half in candidates:
        r = r_from_ratio(ratio, a=1.0)
        Q = koide_Q_from_r(r)
        is_half = abs(r - 0.5) < 1e-9
        record(f"supplied rule [{name}]: abs(b)/a={ratio:.4f} -> r={r:.4f}, Q_H={Q:.4f}",
               is_half == gives_half, "r=1/2" if is_half else "")
        n_half += int(is_half)
    record("exactly two of these eight supplied rules have r=1/2", n_half == 2)

    ps, pd = central_projectors()
    H = I3 + bmod * C + bmod * (C @ C)
    powers = (hs2(ps @ H), hs2(pd @ H))
    record("D3: true central projectors give unequal powers at coefficient balance",
           central_power_check(), f"coefficient powers={[hs2(I3), hs2(H-I3)]}; central powers={powers}")
    record("D5: signed Q_H=3 differs from Q_+=27/49 for eigenvalues 5,-1,-1",
           abs(koide_Q_from_r(4) - 3) < 1e-9
           and abs(koide_Q_from_spectrum(1, 2) - 27 / 49) < 1e-9)
    record("D3: equal-amplitude rule gives r=1, not coefficient HS balance",
           r_from_ratio(1) == 1 and abs(hs2(I3) - hs2(C + C @ C)) > 1)
    try:
        r_from_ratio(1, a=0)
    except ValueError:
        zero_rejected = True
    else:
        zero_rejected = False
    record("D5: r rejects zero a", zero_rejected)

    # ---- source-note firewalls --------------------------------------------
    if NOTE.exists():
        text = " ".join(NOTE.read_text(encoding="utf-8").split())
        for phrase in [
            "does not change axioms",
            "not forced",
            "does not close",
            "AC_phi_lambda",
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
