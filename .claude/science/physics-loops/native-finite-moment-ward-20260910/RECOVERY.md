# Exact recovery

Stack base8078:4600d22d47052040aabe090148ec82cb9a1828f5. Preregistration82:b2a67aea7d4122961aac12c443ba0c320350a8e2 precedes the accepted ALLQ and omega5 outputs. Those outputs are now durably included in checkpoint83, exact remote commit6871442099da4c984dd5f9707ffb2082e3696242, snapshot accepted-b378-omega5-allq-degree20-witness-preregistration. Degree10 and earlier proof imports are recovered from earlier snapshots present at that same commit.

RECOVERY_MAP.json maps every copied import to an exact repository path at that commit and its SHA256. Each mapped blob was read with git show and verified against the copied import hash. The copied parent remote receipt authenticates checkpoint83's remote tree and all9698files. Earlier snapshot manifests establish the earlier paths; no subsequently produced degree20/witness outcome is claimed by this packet.

This is direct copied-import recovery. Transitive runtime input dictionaries retain their original absolute paths and hashes; it does not claim every platform interpreter/library byte is remotely archived, nor duplicate large catalogs or supply a new scientific replay. Recover with git show COMMIT:PATH and verify SHA256; platform runtime recreation is a separate requirement.
