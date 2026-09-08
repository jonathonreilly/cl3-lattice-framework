# Fixed matched detuned L4 source-response run

All21 frozen cells completed in430.862seconds charged wall time, below900; peak child RSS239.312MiB. No replacements, extra seeds or source changes. Three groups contain8 independent paired seven-source vectors each.168 source-replica records and their40-point windows are not168 independent ratio replicas.

|group|population|burn|harmonic|moment ± paired delta SE|10% precision|independent finite-forward references|
|---|---|---|---|---|---|---|
|0|512|160|1|0.766141296 ± 0.004119623|True|F24: 0.749717373 ± 0.003622410, compatible=True; F12: 0.759424486 ± 0.006531699, compatible=True|
|0|512|160|2|1.443081089 ± 0.020613631|True|F24: 1.461035952 ± 0.018795610, compatible=True; F12: 1.443163694 ± 0.007728083, compatible=True|
|1|1024|160|1|0.746697395 ± 0.006397556|True|F24: 0.761192798 ± 0.002634142, compatible=True; F12: 0.753262485 ± 0.002942287, compatible=True|
|1|1024|160|2|1.422587620 ± 0.010089170|True|F24: 1.435299772 ± 0.012742881, compatible=True; F12: 1.431484119 ± 0.007356782, compatible=True|
|2|1024|320|1|0.765249954 ± 0.004116351|True|F24: 0.753379980 ± 0.002624355, compatible=True; F12: 0.751732164 ± 0.004311844, compatible=True|
|2|1024|320|2|1.418653990 ± 0.007226993|True|F24: 1.448942218 ± 0.006368122, compatible=True; F12: 1.444097977 ± 0.011771814, compatible=True|

All six precision checks, twelve method comparisons, four group sensitivities and six half-window comparisons pass their declared nominal thresholds. This does not make the observed differences negligible: group2 harmonic2 differs from F24 by about3.14 combined SE, below the frozen4SE threshold. No threshold was changed.

Every method comparison combines uncertainty from independent runs, including the literal F24 and F12 raw reference records. Neither reference is an exact pure target. Full seven-energy covariance, shared-numerator two-harmonic ratio covariance, all replica B/T values, negative counts and noisy secants remain in ANALYSIS.json. Invalid pooled T is not rescued. Population and burn comparisons use independent seed groups; half-window comparisons retain within-replica pairing.

Source-step .02 remains fixed and no detuned source-step sensitivity was measured. Passing a nominal comparison would not bound source bias, population bias or mixing; failing one remains a failure, not a reason to retune. No pole, photon or larger-volume conclusion follows. The earlier RK gate supplies a separate finite calibration, not a detuned ground oracle.

The original600second forecast failure and prospective900second resource amendment are preserved. Actual runtime does not retrospectively change the compute contract. Production sources are bound in PRODUCTION_FREEZE.json and every cell; all source and reference hashes are checked by the analyzer. No automatic next stage is authorized.

## All group sensitivities

[
  {
    "kind": "population",
    "harmonic": 1,
    "valid": true,
    "difference": 0.019443900602912345,
    "SE": 0.007609206294489997,
    "nominal_4SE_compatible": true
  },
  {
    "kind": "population",
    "harmonic": 2,
    "valid": true,
    "difference": 0.02049346884575365,
    "SE": 0.02295023192098131,
    "nominal_4SE_compatible": true
  },
  {
    "kind": "burn",
    "harmonic": 1,
    "valid": true,
    "difference": -0.01855255885298901,
    "SE": 0.0076074352237191275,
    "nominal_4SE_compatible": true
  },
  {
    "kind": "burn",
    "harmonic": 2,
    "valid": true,
    "difference": 0.003933629953933204,
    "SE": 0.012410510522291989,
    "nominal_4SE_compatible": true
  }
]

## Half-window and sign diagnostics

{
  "0": [
    {
      "harmonic": 1,
      "window": {
        "valid": true,
        "difference": -0.017463027895317063,
        "SE": 0.015080611878879357,
        "nominal_4SE_compatible": true
      },
      "negative_B": 0,
      "nonpositive_T": 0,
      "reversed_secants": 1
    },
    {
      "harmonic": 2,
      "window": {
        "valid": true,
        "difference": 0.015942372102444313,
        "SE": 0.04133901974459529,
        "nominal_4SE_compatible": true
      },
      "negative_B": 0,
      "nonpositive_T": 0,
      "reversed_secants": 5
    }
  ],
  "1": [
    {
      "harmonic": 1,
      "window": {
        "valid": true,
        "difference": -0.008086244673982002,
        "SE": 0.011762946233224433,
        "nominal_4SE_compatible": true
      },
      "negative_B": 0,
      "nonpositive_T": 0,
      "reversed_secants": 2
    },
    {
      "harmonic": 2,
      "window": {
        "valid": true,
        "difference": 0.03143323285762989,
        "SE": 0.017101587335992544,
        "nominal_4SE_compatible": true
      },
      "negative_B": 0,
      "nonpositive_T": 0,
      "reversed_secants": 2
    }
  ],
  "2": [
    {
      "harmonic": 1,
      "window": {
        "valid": true,
        "difference": -0.0012679963460964228,
        "SE": 0.011297855071675543,
        "nominal_4SE_compatible": true
      },
      "negative_B": 0,
      "nonpositive_T": 0,
      "reversed_secants": 5
    },
    {
      "harmonic": 2,
      "window": {
        "valid": true,
        "difference": 0.03930677948413108,
        "SE": 0.023657935601041763,
        "nominal_4SE_compatible": true
      },
      "negative_B": 0,
      "nonpositive_T": 0,
      "reversed_secants": 5
    }
  ]
}
