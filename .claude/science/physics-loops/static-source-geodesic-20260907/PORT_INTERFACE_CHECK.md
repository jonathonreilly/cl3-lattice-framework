# Port interface check

Live primary JSON uses TOTAL=34; independent helper uses check_count=37. An initial port assertion incorrectly expected TOTAL on both and raised KeyError for the helper. The assertion was corrected to their actual preserved schemas; both unique check counts and strict CLI now pass. No source, helper, fixture or output schema was changed.
