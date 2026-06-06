# B02 Northern And Faction Template Partial QC Report

- Project: `project/severed-homeland`
- Batch: `B02_NORTHERN_AND_FACTION_TEMPLATES`
- Scope: `PROMPT_C012` through `PROMPT_C020`; C021 remains pending separate dispatch/review
- Status: `partial_complete_qc_passed_c016_generated_remaining_pending_dispatch`
- Date: 2026-06-06

## Final Files

| Asset | Prompt | Final file | Status |
| --- | --- | --- | --- |
| C012 | PROMPT_C012 | `assets/characters/c012m.png` | generated, format QC passed, pending art review |
| C013 | PROMPT_C013 | `assets/characters/c013m.png` | generated, format QC passed, pending art review |
| C014 | PROMPT_C014 | `assets/characters/c014m.png` | generated, format QC passed, pending art review |
| C015 | PROMPT_C015 | `assets/characters/c015m.png` | generated, format QC passed, pending art review |
| C016 | PROMPT_C016 | `assets/characters/c016m.png` | generated, format QC passed, pending art review |
| C017 | PROMPT_C017 | `assets/characters/c017m.png` | generated, format QC passed, pending art review |
| C018 | PROMPT_C018 | `assets/characters/c018m.png` | generated, format QC passed, pending art review |
| C019 | PROMPT_C019 | `assets/characters/c019m.png` | generated, format QC passed, pending art review |
| C020 | PROMPT_C020 | `assets/characters/c020m.png` | generated, format QC passed, pending art review |

## Blocked For Retry

No C016 retry block remains after the 2026-06-06 regeneration. Remaining B02 assets not generated or not QC-passed in this pass: C021.

## Art Review Corrections

### C016 Insect-Official Correction

C016 was regenerated after the latest insect-official feedback. The accepted card keeps the official as a natural symmetric insect-face being with about 50% anthropomorphic readability, not a human county clerk, a human face with a shell, or a side-growth collage. The face uses compound-eye texture, cheek carapace, mandible lines, neck membrane, and fine chitin seams as the main structure.

The accepted card also locks the bureaucratic uniform rules: white insect-wax official robe dominates the design, scarlet/cinnabar cords and knots mark authority, cyan/blue-green edging separates collar and sleeves, and the feet use enclosed white official shoes/boots rather than bare claws. The pressure comes from ledger, seal box, account tag, and bone abacus rather than combat mass.

## Output Contract QC

| Check | Result |
| --- | --- |
| Exact canonical path | pass for C012-C020 |
| Short basename <= 20 chars | pass for C012-C020 |
| PNG format | pass for C012-C020 |
| 2160x3840 minimum resolution | pass for C012-C020 |
| Opaque / no alpha | pass for C012-C020 |
| 9:16 vertical card format | pass for C012-C020 |
| Neutral master character card, not video frame | pass for C012-C020 |
| No readable text, labels, UI, watermark, modern logo | pending visual art review |
| Retained intermediates under project `history/` only | pass; retained candidates are under `assets/characters/history/` |

## Notes

- C012 final SHA-256: `95d2f290298ffd46fddb7e3ddc6ae43204b65dabb17e8f3950bf8c997b4eb813`
- C013 final SHA-256: `9cefe481e41eac94a7af5c23bd5eb3dd06ed48240a00e48a0a1e51e09d1fdbf8`
- C014 final SHA-256: `3dd48959f7db0394e2e3fe64771d72818945a1dfaa2d680369e7cb2299fb69f5`
- C015 final SHA-256: `55cada165116df22f9175d934dd2dd8c731def4f3571a3d70464f71cf65c9fd5`
- C016 source image: `/Users/uroborus/.codex/generated_images/019e97cd-3447-7613-83a3-80cefad15700/ig_04e84ef91b261af9016a231948669c8193ae5346576073759d.png`
- C016 final SHA-256: `ece09e5eaaeb57813cc0f85c627dcda859bee511255efd2d34af047b476cba57`
- C017 final SHA-256: `0b5b5b93ff3509c8763f722a6467c3ad0d87218d26c9939dd2ebdebfb57ad341`
- C018 final SHA-256: `a42e4ac3255ef4fe79a09ccd2134e6071255a9a6938f6c2e2c85c309b2751e49`
- C019 final SHA-256: `dce3bd7e54dfaa986ae63e064c81cab6036c80821f74bd502b2ec6b089c2b9b3`
- C020 final SHA-256: `1c6738f8ba9b6f43080d1d5108bd23913faf045f1a7d87a0bcad57ace302a0d3`
- C016 rejected history SHA-256: `assets/characters/history/c016m.v001.png`: `df42fab4027535f10ac79f11cc474bc2e85522431a44d7301922d4efa3cb6680`
- Retained history files: `assets/characters/history/c016m.v001.png`, `assets/characters/history/c017m.v001.png`, `assets/characters/history/c017m.v002.png`, `assets/characters/history/c018m.v001.png`, `assets/characters/history/c019m.v001.png`
- Remaining B02 assets not generated or not QC-passed in this pass: C021.
