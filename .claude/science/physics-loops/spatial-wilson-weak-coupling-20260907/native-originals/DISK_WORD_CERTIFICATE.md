# Explicit nonabelian disk word supplement

Gauge-fix three bottom boundary edges and four vertical edges toI, a spanning tree of the spatial cube. Let U be the fourth bottom edge; source loop is U orU^-1. Let top edges in positive x/y orientations be A,B,C,D. The top face is T=A B C^-1 D^-1. The four side faces, up to inversion, are A,B,D and S=U C^-1. Exactly

U=S D^-1 T^-1 A B.

The freegroup cancellation in check.py verifies this without assuming commutativity. Each factor is an actual face holonomy or its inverse in this gauge. Unitariy triangle inequality thus bounds||I−U||F by the five actual face deviations. Gauge conjugation restores the gauge-independent missing-loop norm statement. This is a concrete implementation of the disk step in DERIVATION.md, not a scalar surrogate.

The12support checks also verify the rational count/constants; they do not replace the analytic Haar-volume, concentration or representation proof.
