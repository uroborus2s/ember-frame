# B02 Northern And Faction Template Partial QC Report

- Project: `project/severed-homeland`
- Batch: `B02_NORTHERN_AND_FACTION_TEMPLATES`
- Scope: `PROMPT_C017` through `PROMPT_C020`
- Status: `partial_complete_qc_passed`
- Date: 2026-06-05

## Final Files

| Asset | Prompt | Final file | Status |
| --- | --- | --- | --- |
| C017 | PROMPT_C017 | `assets/characters/c017m.png` | generated, format QC passed, pending art review |
| C018 | PROMPT_C018 | `assets/characters/c018m.png` | generated, format QC passed, pending art review |
| C019 | PROMPT_C019 | `assets/characters/c019m.png` | generated, format QC passed, pending art review |
| C020 | PROMPT_C020 | `assets/characters/c020m.png` | generated, format QC passed, pending art review |

## Output Contract QC

| Check | Result |
| --- | --- |
| Exact canonical path | pass for C017-C020 |
| Short basename <= 20 chars | pass for C017-C020 |
| PNG format | pass for C017-C020 |
| 2160x3840 minimum resolution | pass for C017-C020 |
| Opaque / no alpha | pass for C017-C020 |
| 9:16 vertical card format | pass for C017-C020 |
| Neutral master character card, not video frame | pass for C017-C020 |
| No readable text, labels, UI, watermark, modern logo | pending visual art review |
| Retained intermediates under project `history/` only | pass; retained candidates are under `assets/characters/history/` |

## Notes

- C017 final SHA-256: `0b5b5b93ff3509c8763f722a6467c3ad0d87218d26c9939dd2ebdebfb57ad341`
- C018 final SHA-256: `a42e4ac3255ef4fe79a09ccd2134e6071255a9a6938f6c2e2c85c309b2751e49`
- C019 final SHA-256: `dce3bd7e54dfaa986ae63e064c81cab6036c80821f74bd502b2ec6b089c2b9b3`
- C020 final SHA-256: `1c6738f8ba9b6f43080d1d5108bd23913faf045f1a7d87a0bcad57ace302a0d3`
- Retained history files: `assets/characters/history/c017m.v001.png`, `assets/characters/history/c017m.v002.png`, `assets/characters/history/c018m.v001.png`, `assets/characters/history/c019m.v001.png`
- Remaining B02 assets were not generated in this pass: C012, C013, C014, C015, C016, C021.
