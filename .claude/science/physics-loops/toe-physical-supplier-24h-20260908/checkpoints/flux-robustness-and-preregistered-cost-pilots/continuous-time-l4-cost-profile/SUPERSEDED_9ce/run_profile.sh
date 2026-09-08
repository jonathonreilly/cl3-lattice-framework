#!/bin/sh
set -eu
[ "$#" = 1 ]
/usr/bin/time -lp /usr/local/bin/python3 -OO "$(dirname "$0")/run_profile.py" "$1" 2>"$1.outer-time.txt"
