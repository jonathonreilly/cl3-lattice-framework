# Immutable diff preservation

The original unified-diff bytes contain space-only context lines rejected by staged whitespace checking. Their exact bytes are base64-preserved in ALL_LABEL_CLARIFICATION_ORIGINAL.diff.base64, SHA256 2de214a9a1b04ae67b05fa4c7eb1e3d0d5b6aa1c928690fef8969217888075b7. The neighboring .diff is a whitespace-trimmed readable view, not a byte-identical patch. Mathematical source and proof files are untouched.
