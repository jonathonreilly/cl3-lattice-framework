# Standard-library candidate decoder

Implemented decoder.py using only ast, hashlib, json, math, re, struct, zipfile and pathlib. No NumPy import or coefficient arithmetic occurs in the decoder. load(JSON,prefix) returns the original metadata, matching prefix record and key-indexed rows with ordinary Python float lists in place of NumPy vectors.

The decoder accepts the actual little-endian float64, uint8, uint64 and UTF-32LE hex arrays. It checks six-member ZIP membership without duplicates, bounded uncompressed sizes, NPY version/header syntax and unique keys, C order, exact dtype/shape/payload length, finite floats, canonical hex strings, matching metadata lengths, artifact SHA/byte count/shape, unique DP keys, prefix coverage/identity and the vacuum row. Object arrays are rejected without unpickling.

The independent comparison control decoded all six frozen NPZ artifacts and compared every float bit (including signed zero) and every metadata value against NumPy's allow_pickle=False decoder. All 83 predicates passed in 0.254 seconds, peak 180.422 MiB. Actual malformed shape, object dtype, NaN payload, truncated payload and duplicate ZIP member mutants failed decoding without relying on artifact hash rejection. NPZ hashes are preserved in RESULT.json. No coefficient recurrence, solve or rational certificate was rerun.

This is a strict decoder for this saved schema, not a general NumPy file implementation. Arbitrary NPY formats, endian conventions and shapes intentionally fail. The original postcheck.load source was read to preserve its metadata/row contract; scientific prefix word-count recurrence remains the downstream certificate's responsibility.
