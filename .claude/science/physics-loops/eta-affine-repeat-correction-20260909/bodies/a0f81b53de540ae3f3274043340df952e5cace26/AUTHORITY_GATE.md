# Block 35 authority gate

1. Pin canonical main, the current minimal-axiom blob, PR #7814's head, and its
   sole evidence blob before execution.
2. Fail closed if the public PR acquires additional evidence during the run;
   rescan and classify the new material rather than pretending the preregistered
   census remains current.
3. Treat `minimal_axioms.current_path` as the premise authority. Canonical
   main's registry note reflects the 2026-08-13 removal of scalar Record
   additivity; the older registry copy inherited by this stacked branch may not
   be substituted for that pinned object or edited here.
4. Open/blocked/closed PRs and unaudited theorem notes are conditional prior art,
   never retained authority.
5. No audit data, ledger, axiom, primitive registry, or TOE score file may be
   edited in this campaign.
