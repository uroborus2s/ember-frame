# B01 Core Character Partial QC Report

- Project: `project/severed-homeland`
- Batch: `B01_CORE_CHARACTERS`
- Scope: `PROMPT_C001` through `PROMPT_C007`
- Status: `partial_complete_qc_passed`
- Date: 2026-06-05

## Final Files

| Asset | Prompt | Final file | Status |
| --- | --- | --- | --- |
| C001 | PROMPT_C001 | `assets/characters/c001m.png` | generated, QC passed, pending art review |
| C002 | PROMPT_C002 | `assets/characters/c002m.png` | generated, QC passed, pending art review |
| C003 | PROMPT_C003 | `assets/characters/c003m.png` | generated, format QC passed, pending art review |
| C004 | PROMPT_C004 | `assets/characters/c004m.png` | generated, format QC passed, pending art review |
| C005 | PROMPT_C005 | `assets/characters/c005m.png` | generated, format QC passed, pending art review |
| C006 | PROMPT_C006 | `assets/characters/c006m.png` | generated, format QC passed, pending art review |
| C007 | PROMPT_C007 | `assets/characters/c007m.png` | generated, format QC passed, pending art review |

## C001 Identity Lock

C001 was regenerated after user feedback with this hard reference:

`legacy/pre-remake-2026-06-04/assets/characters/character_shen_weisang_multi_state_board.png`

The accepted C001 image locks Shen Weisang's face shape and hairstyle to the provided board: narrow youthful long face, tightened cheek and jaw structure without sharp adult V-shape, sharp sword-like brows, deep black wary eyes, short messy black hair, broken uneven forehead bangs, close face-framing side locks, and cool restrained hunter expression.

The final C001 file was normalized by padding the generated canvas horizontally before upsampling, so the face and hair proportions were not squeezed or stretched.

## Output Contract QC

| Check | Result |
| --- | --- |
| Exact canonical path | pass for C001-C007 |
| Short basename <= 20 chars | pass for C001-C007 |
| PNG format | pass for C001-C007 |
| 2160x3840 minimum resolution | pass for C001-C007 |
| Opaque / no alpha | pass for C001-C007 |
| 9:16 vertical card format | pass for C001-C007 |
| Neutral master character card, not video frame | pass for C001-C007 |
| No readable text, labels, UI, watermark, modern logo | pending visual art review |
| Retained intermediates under project `history/` only | pass; retained candidates are under `assets/characters/history/` |

## Notes

- C001 source image: `/Users/uroborus/.codex/generated_images/019e9776-a0cf-79f0-8415-864271b9ebe5/ig_00072e2f8a194a6a016a22b1e31d048196bf6e3762843ba951.png`
- C002 source image: `/Users/uroborus/.codex/generated_images/019e9776-a0cf-79f0-8415-864271b9ebe5/ig_00072e2f8a194a6a016a22afa8c6e08196903d8d8c2c630820.png`
- C001 final SHA-256: `c91b18535aeafb342a8a30cdf01fb3b66a1a85e891e80c796625ad30e3f7f4b0`
- C002 final SHA-256: `f645200c6a1e50321ff8d84799c9579f42cb4d7bf6d2a806ef9467878b529258`
- C003 final SHA-256: `a93bf6f1fbda53f93880613fbe26a8840315b3aa47cc4c43e6f14f6257921f0a`
- C004 final SHA-256: `b6cb1106c9622a382411f12fefb33ec2c4b1f36fbce670f29da8ed94b2fbd23e`
- C005 final SHA-256: `4258e7f9e43b626d3e37fab21ffe8d73742e21b41f65fbc503d695b03c715e15`
- C006 final SHA-256: `02a2f681faadc742639669e1cdf20cff67a49399deb5075c09948208793034ad`
- C007 final SHA-256: `effa2eb82e6f0e21abef9732858e26b1202c265a378f2ac9161cd11bfc28bdf7`
- Retained history files: `assets/characters/history/c001m.v001.png`, `assets/characters/history/c004m.v001.png`, `assets/characters/history/c006m.v001.png`, `assets/characters/history/c006m.v002.png`, `assets/characters/history/c007m.v001.png`, `assets/characters/history/c007m.v002.png`, `assets/characters/history/c007m.v003.png`
- Remaining B01 assets were not generated in this pass: C008, C009, C010, C011, C022, C023, C024, C025, C026.
