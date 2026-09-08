# External review harness incidents

The first author-map verification passed the artifact/map/source/anchor stages and then looked for old corrected sources under `intermediate/scripts/`; those bodies are actually preserved under `first-cache-freeze/source/scripts/`. The failed script and traceback are retained as `verify_author_missing_snapshot_path.py/.log`. Only this external lookup was corrected. The second verification passed. No science execution or candidate edit occurred.

Two bounded display probes used an inappropriate assumed metadata shape/name: slicing the dictionary `FINAL_SOURCE_INVENTORY.json` produced `KeyError: slice(None, 1, None)`; probing original-review `RECEIPT.json` produced FileNotFoundError because that packet is named `FINAL_RECEIPT.json`. Correct schema/path discovery followed. The actual original receipt and all 74 hash-bound artifacts were then verified. These were read-only metadata display errors and not scientific or execution failures.

Root's separately preserved composition probes had Path-versus-serialized-string errors, described in its `COMPOSITION_PREPARATION_RECOVERY.json`. The final independent integration check uses actual absolute note paths and canonical IDs. Root source/caches never changed during those probe repairs. This review performed no global graph write or gate.
