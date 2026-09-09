---
claim_id: spin_half_cubic_ice_infrared_forward_replay_recovery_boundary_2026-09-05
claim_type: open_gate
claim_scope: "The predeclared six-replica paired-forward replay records an attempted finite-volume estimator check whose L=18 detuned row does not meet the existing forward-genealogy floor; this is a partial attempt, not a route-independent physical no-go."
upstream_dependencies:
  - minimal_axioms
runner: scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py
---

# High-Genealogy Infrared Replay Hits a Finite-Volume Forward-Genealogy Boundary

**Date:** 2026-09-05

**Status:** `partial-attempt-with-named-untested-routes`. The status authority is the independent audit lane; this note sets no audit verdict, TOE score, axiom, or approved primitive.

**Primary runner:** [`scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py`](../scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py)

**Primary receipt:** [`logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt)

**Strict/diagnostic join receipt:** [`logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt`](../logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt)

**No-go packet:** [`docs/NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md`](NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md)

## Result up front

The canonical clean replay completed all four predeclared coupling/volume rows with six replicas per row, shared forward endpoints `F=6,12,20`, four measurement origins, detuned population `6144`, and RK population `1536`. Exact flippable counts, Gauss charge, zero electric flux, finite positive correlators/gaps/covariances, detuned covariance rank, and the RK forward identity all passed.

The aggregate receipt is `TOTAL: PASS=3 FAIL=1`. The sole runner failure is the existing weight/genealogy floor: at `V=0.95, L=18`, `min_forward=36` while the predeclared floor is `>=40`; its `min_ess=0.943968` and `min_origin_tau16=57` remain above their floors. The strict join therefore exits before fitting and records `high-genealogy replay receipt is not green`. An explicit `--diagnostic` rerun keeps that upstream failure visible and evaluates the downstream surface: `TOTAL: PASS=6 FAIL=2`, with the upstream-green gate and the paired-primary-forward-plateau gate failing while the reproduction, positive U K-compatible fits, model extensions, and direct-spectrum controls pass. No Maxwell compatibility claim is promoted from this packet.

This is a bounded estimator boundary for the attempted replay. It does not show that the detuned carrier is physically inconsistent, that no alternative forward estimator can work, or that the light lane is closed. The failure is useful because it identifies the exact condition that must be retired before the lower-momentum Maxwell comparison can be interpreted.

## 1. Paired measurements

| coupling | L | window | paired gaps |
|---:|---:|:---:|:---|
| 1.00 | 16 | 2--6 | F6=0.04668739 +/- 0.00031957, F12=0.04668739 +/- 0.00031957, F20=0.04668739 +/- 0.00031957 |
| 1.00 | 16 | 8--14 | F6=0.04595709 +/- 0.00028473, F12=0.04595709 +/- 0.00028473, F20=0.04595709 +/- 0.00028473 |
| 1.00 | 18 | 2--6 | F6=0.03681395 +/- 0.00021043, F12=0.03681395 +/- 0.00021043, F20=0.03681395 +/- 0.00021043 |
| 1.00 | 18 | 8--14 | F6=0.03700905 +/- 0.00025207, F12=0.03700905 +/- 0.00025207, F20=0.03700905 +/- 0.00025207 |
| 0.95 | 16 | 2--6 | F6=0.08917261 +/- 0.00156682, F12=0.08515066 +/- 0.00176782, F20=0.08880624 +/- 0.00409377 |
| 0.95 | 16 | 8--14 | F6=0.08539755 +/- 0.00246898, F12=0.09003998 +/- 0.00526249, F20=0.09054816 +/- 0.00591009 |
| 0.95 | 18 | 2--6 | F6=0.07547634 +/- 0.00247577, F12=0.07036339 +/- 0.00341667, F20=0.07423651 +/- 0.00291967 |
| 0.95 | 18 | 8--14 | F6=0.07442854 +/- 0.00497829, F12=0.07345383 +/- 0.00801271, F20=0.08388134 +/- 0.01249193 |

| coupling | L | minimum ESS fraction | minimum tau=16 origins | minimum forward descendants |
|---:|---:|---:|---:|---:|
| 1.00 | 16 | 1.000000 | 1536 | 1536 |
| 1.00 | 18 | 1.000000 | 1536 | 1536 |
| 0.95 | 16 | 0.960210 | 118 | 74 |
| 0.95 | 18 | 0.943968 | 57 | 36 |

The detuned primary paired gaps are `0.08539755, 0.09003998, 0.09054816` at `L=16` and `0.07442854, 0.07345383, 0.08388134` at `L=18`. An independent diagnostic recomputation gives forward-plateau spans `0.058093` and `0.134976`, respectively, against the frozen `<0.05` join threshold; those values are diagnostics only because the strict join correctly refuses a non-green upstream receipt. The RK rows are exactly forward-independent by construction and serve as implementation controls.

## 2. Diagnostic join localization

The diagnostic-only join was added after the receipt failed so the strict gate remains unchanged while the measured rows are still inspected. Its exact decision surface is:

```text
[FAIL] upstream replay receipt is green (diagnostic mode keeps this gate visible)
[PASS] source-pinned parent and replay provide matched six-volume ladders
[PASS] every new F=6 primary gap reproduces the independent earlier infrared receipt
[FAIL] both detuned infrared volumes pass the paired primary-window forward plateau
[PASS] every paired forward endpoint gives a positive U K-compatible primary coefficient
[PASS] fixed central U K plus q-fourth and q-sixth passes at every forward endpoint
[PASS] mass and q-eighth extensions neither improve nor destabilize the primary fits
[PASS] primary direct detuned spectra carry U K-compatible weight while RK does not
TOTAL: PASS=6 FAIL=2
```

The detuned primary-window forward controls are `hotelling=1.5660`, `max_contrast=1.2486`, `span=0.058093` at `L=16`, and `4.4771`, `0.8982`, `0.134976` at `L=18`, against the frozen span bound `<0.05`. The diagnostic `F=6,12,20` Maxwell coefficients are `0.01987277 +/- 0.01062092`, `0.02398295 +/- 0.01465051`, and `0.02821253 +/- 0.01666132`, all compatible with the static `U K=0.01228909 +/- 0.00116899` within the declared checks. Because the upstream genealogy and plateau gates are not met, these are localization values, not a promoted theorem.

## 3. What the workflow result means

The optional `--parallel-rows` mode ran the same `run_row`, replica seeds, populations, checks, and emission format for the four independent rows, then restored the declared row order before aggregate checks. It changes scheduling only. The canonical cache records runner SHA `8d87b4c4ffc219e7557cf0ad19213842738f8f8a2879493612e3740fd19d26da`, elapsed time `20807.00 s`, exit code `1`, and the complete stdout. A recovery scope certificate is appended after the raw output and is marked as such; no numerical runner line was edited.

The failed guard is an estimator-health condition, not a dynamical law. At the larger volume and lower gap, four origin blocks and the selected forward suffix leave only 36 distinct descendants in the worst endpoint population. The current packet therefore cannot separate physical forward-length drift from loss of genealogy support. The next replay should predeclare how to raise that count—larger population, more independent origins, or a resampling/observable design with a proven survival bound—before changing the Maxwell thresholds or acceptance window.

## 4. TOE consequence and next frontier

No axiom or primitive edit follows. This packet does not reduce the central Record/matter assumptions. The highest-value follow-up remains the local CAR-to-physical-Record compiler and a repeated active matter/apparatus cycle with no fresh-state reset, carrying one exact particle-and-energy ledger through formation, propagation, and readout. The open Record-matter work in PRs #7979 and #7983 is the relevant bridge; this light-lane estimator boundary should be retired or narrowed before it is used to support that bridge.

## 5. Falsifiers and repair test

Reopen this boundary if an independent run with the same frozen source and receipt format reaches `min_forward>=40` at `V=0.95,L=18`, or if a predeclared alternate estimator supplies the required genealogy bound. Conversely, any conservation, sector, positivity, covariance-rank, or RK-control failure would make the current failure broader than the named genealogy wall. The repair campaign must keep `L=16,18`, six replicas, shared `F=6,12,20`, primary window `8-14`, and the existing strict thresholds visible before output.

Run:

```bash
python3 scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py --workers 2 --parallel-rows
python3 scripts/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.py --diagnostic
```

No audit verdict is authored here.
