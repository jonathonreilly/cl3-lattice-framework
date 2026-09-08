#!/bin/sh
set -eu
[ "$#" = 1 ]
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
/usr/bin/time -lp /usr/local/bin/python3 -OO "$(dirname "$0")/run_profile.py" "$1" 2>"$1.outer-time.txt"
/usr/bin/time -lp /usr/local/bin/python3 -OO "$(dirname "$0")/forecast.py" "$1" >"$1/FORECAST.json" 2>"$1.forecast-time.txt"
