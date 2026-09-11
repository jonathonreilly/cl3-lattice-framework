# Released 7753 helper extraction map

The live helper is a reviewed extraction, not a restoration of the historical closure. Exact historical source bodies are stored in `original/historical_helper_sources.gzip_base64.json` at original head `4e9931a970ded94f769553da9e6d77770d612f64`.

| live construction | historical implementation | extraction decision |
|---|---|---|
| sparse multiply/add/scale/dagger/clean/dense | Block 165 lines 419-466 | copied as finite exact utilities |
| fixed cover, local Hodge, antiperiodic quotient, quotient connection | Block 165 `Fixture`, lines 481-631 | narrowed to the fixed `12 x 4` fixture and selected self edge |
| `ssubs`, region pin, carrier substitution | Block 166 lines 468-527 | copied without unrelated pairing/discriminator code |
| Hermitian part | Block 170 line 483 | copied |
| symbolic pinned quotient matrix | Block 170 `Bench`, lines 594-627 | narrowed to fields consumed by Block 212; reflections and pairings omitted |
| x-graded volume/field and exact inverse | Block 171 lines 467-516 | copied for the one tested mode |
| `Site` compatibility surface | Block 171 lines 554-590 | narrowed; unused holonomy dials omitted |
| `Env` W2/W9 profiles | Block 171 lines 593-690 | narrowed to the two families Block 212 calls |
| `EX`, `ET`, `shift_lifts()` | historical and current Block 105 | imported from the current Block 105 file and SHA-256 pinned |
| healing weights | historical Block 145 chain | omitted: for selected edge `(0,0)->(0,0)`, the weight difference is exactly zero |

The helper does not expose historical reflection laws, observable bases, holonomy dials, other chart edges, parent authority gates, parent theorem conclusions, action interpretations, or physical probability/conditional laws.
