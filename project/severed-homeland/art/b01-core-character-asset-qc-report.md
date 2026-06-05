# B01 Core Character Partial QC Report

- Project: `project/severed-homeland`
- Batch: `B01_CORE_CHARACTERS`
- Scope: `PROMPT_C001`, `PROMPT_C002`
- Status: `partial_complete_qc_passed`
- Date: 2026-06-05

## Final Files

| Asset | Prompt | Final file | Status |
| --- | --- | --- | --- |
| C001 | PROMPT_C001 | `assets/characters/c001m.png` | generated, QC passed, pending art review |
| C002 | PROMPT_C002 | `assets/characters/c002m.png` | generated, QC passed, pending art review |

## C001 Identity Lock

C001 was regenerated after user feedback with this hard reference:

`legacy/pre-remake-2026-06-04/assets/characters/character_shen_weisang_multi_state_board.png`

The accepted C001 image locks Shen Weisang's face shape and hairstyle to the provided board: narrow youthful long face, tightened cheek and jaw structure without sharp adult V-shape, sharp sword-like brows, deep black wary eyes, short messy black hair, broken uneven forehead bangs, close face-framing side locks, and cool restrained hunter expression.

The final C001 file was normalized by padding the generated canvas horizontally before upsampling, so the face and hair proportions were not squeezed or stretched.

## Output Contract QC

| Check | C001 | C002 |
| --- | --- | --- |
| Exact canonical path | pass | pass |
| Short basename <= 20 chars | pass | pass |
| PNG format | pass | pass |
| 2160x3840 minimum resolution | pass | pass |
| Opaque / no alpha | pass | pass |
| 9:16 vertical card format | pass | pass |
| Neutral master character card, not video frame | pass | pass |
| No readable text, labels, UI, watermark, modern logo | pass | pass |
| Retained intermediates under project `history/` only | pass; no retained project intermediates | pass; no retained project intermediates |

## Notes

- C001 source image: `/Users/uroborus/.codex/generated_images/019e9776-a0cf-79f0-8415-864271b9ebe5/ig_00072e2f8a194a6a016a22b1e31d048196bf6e3762843ba951.png`
- C002 source image: `/Users/uroborus/.codex/generated_images/019e9776-a0cf-79f0-8415-864271b9ebe5/ig_00072e2f8a194a6a016a22afa8c6e08196903d8d8c2c630820.png`
- C001 final SHA-256: `c91b18535aeafb342a8a30cdf01fb3b66a1a85e891e80c796625ad30e3f7f4b0`
- C002 final SHA-256: `f645200c6a1e50321ff8d84799c9579f42cb4d7bf6d2a806ef9467878b529258`
- Remaining B01 assets were not generated in this pass: C003, C004, C005, C006, C007, C008, C009, C010, C011, C022, C023.

