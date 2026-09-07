The coordinator's first preparation attempt checked the diagnostic's declared
fixture before the loop had copied that later inventory entry, so read_bytes
raised FileNotFoundError. No scientific runner, graph build or integration gate
had run. The preparation script now verifies input closure after copying the
complete inventory. Its partial new files must exactly match reviewed blobs
before resumption; current-main files remain protected. This was a coordinator
ordering error, not a source finding or a failed science check.
