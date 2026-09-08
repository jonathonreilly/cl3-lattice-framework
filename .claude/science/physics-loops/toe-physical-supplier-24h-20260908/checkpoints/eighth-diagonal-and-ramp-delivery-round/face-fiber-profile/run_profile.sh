#!/bin/sh
# Root must separately authorize this one prospective fixture before invocation.
set -eu
if [ "$#" -ne 1 ]; then echo 'usage: run_profile.sh ABSOLUTE_FRESH_OUTPUT' >&2; exit 2; fi
out=$1
case "$out" in /*) ;; *) echo 'absolute output required' >&2; exit 2;; esac
if [ -e "$out" ] || [ -e "$out.outer-time.txt" ]; then echo 'fresh outputs required' >&2; exit 2; fi
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
set -C
/usr/bin/time -lp /usr/local/bin/python3 -OO "$here/run_profile.py" --out "$out" 2> "$out.outer-time.txt"
# No fixture rerun here. Root runs finalize_outer.py as separate bookkeeping.
