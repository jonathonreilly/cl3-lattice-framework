# Fixed propagated L8 diagnostic study

All128 fixed segment jobs completed, representing48 independent chains, not128 replicas. Production wall time 4938.904908s; charged total 4946.131711s. Maximum job 61.499193s; maximum RSS 59.328125MiB.

Frozen analyzer status: `fails_diagnostics`. This is a finite diagnostic classification, not stationarity, ground-state convergence, a gap certificate or photon evidence.

| Arm | harmonic | D ± SE | R ± SE | residual ± SE | signed VarH ± SE |
|---|---|---|---|---|---|
|[12, 2048, 32]|1|0.254714038 ± 0.0068677|0.257090287 ± 0.0072572|0.00237625 ± 0.001813|0.0018367 ± 0.002321|
|[12, 2048, 32]|2|0.747029601 ± 0.01548|0.750897861 ± 0.015439|0.00386826 ± 0.001425|0.0018367 ± 0.002321|

|[36, 2048, 8]|1|0.243893255 ± 0.0058618|0.241514334 ± 0.0062961|-0.00237892 ± 0.001141|0.00116108 ± 0.0007841|
|[36, 2048, 8]|2|0.739206329 ± 0.016844|0.736657903 ± 0.016596|-0.00254843 ± 0.001073|0.00116108 ± 0.0007841|

|[36, 2048, 32]|1|0.255335701 ± 0.0081424|0.255595275 ± 0.0080934|0.000259574 ± 0.001497|-0.000540844 ± 0.0009764|
|[36, 2048, 32]|2|0.730239974 ± 0.012659|0.731001557 ± 0.012894|0.000761582 ± 0.001127|-0.000540844 ± 0.0009764|


Original-tag ranges per arm: [(0, 0.0, 0.0), (1, 0.0, 0.4487253824869792), (2, 0.0, 0.3281566478587963)]

Within-L8 comparison flags: 0 / 12. Unflagged differences are not equivalence or equilibration.

## Prespecified matched-size contrasts

L8h2 and L4h1 both use q=pi/2. A/B compares tau12 and C/D tau36, each burn32n; L4 RK512 versus L8 RK2048 remains a supplied initialization difference. Differences below are L8 minus L4, with independent-chain combined SE. They are not pass gates.

{'L8_arm': 0, 'L4_arm': 1, 'quantity': 'D', 'valid': True, 'difference': 0.006449352945801956, 'SE': 0.016627037257049386, 'scope': 'size contrast; not a pass gate'}
{'L8_arm': 0, 'L4_arm': 1, 'quantity': 'R', 'valid': True, 'difference': 0.010643457389107547, 'SE': 0.016660209126475176, 'scope': 'size contrast; not a pass gate'}
{'L8_arm': 0, 'L4_arm': 1, 'quantity': 'correction', 'valid': True, 'difference': 0.004194104443305591, 'SE': 0.0014845396053823636, 'scope': 'size contrast; not a pass gate'}
{'L8_arm': 2, 'L4_arm': 3, 'quantity': 'D', 'valid': True, 'difference': -0.022323952960818683, 'SE': 0.014249837083748131, 'scope': 'size contrast; not a pass gate'}
{'L8_arm': 2, 'L4_arm': 3, 'quantity': 'R', 'valid': True, 'difference': -0.02207760203572462, 'SE': 0.01451843448128881, 'scope': 'size contrast; not a pass gate'}
{'L8_arm': 2, 'L4_arm': 3, 'quantity': 'correction', 'valid': True, 'difference': 0.0002463509250940632, 'SE': 0.0011635144588071553, 'scope': 'size contrast; not a pass gate'}

The endpoint identities target the stationary finite product-G measure and its finite projected vector. Nonstationary sampled ratios do not become exact Rayleigh quotients by using those formulas. R is referenced to Epsi, not the ground energy. Signed negative variance estimates remain unmodified and any nonnegative bound plugin is not a confidence bound. Initial-tag loss tests one specific memory mechanism only.

The 16 within-chain batches and immutable checkpoint segments are diagnostic records, not independent replicates. Full chain vectors, cross-harmonic influences and covariance are preserved in ANALYSIS.json; all segment states and receipt ancestry remain available. No retries, replacements or adaptive arms were part of the authorization.
