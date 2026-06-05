# B01 Core Character Partial QC Report

- Project: `project/severed-homeland`
- Batch: `B01_CORE_CHARACTERS`
- Scope: `PROMPT_C001`-`PROMPT_C005`, `PROMPT_C009`-`PROMPT_C011`; `PROMPT_C008` blocked for retry
- Status: `partial_complete_qc_passed_c008_blocked_retry_needed`
- Date: 2026-06-05

## Final Files

| Asset | Prompt | Final file | Status |
| --- | --- | --- | --- |
| C001 | PROMPT_C001 | `assets/characters/c001m.png` | generated, QC passed, pending art review |
| C002 | PROMPT_C002 | `assets/characters/c002m.png` | generated, QC passed, pending art review |
| C003 | PROMPT_C003 | `assets/characters/c003m.png` | generated, QC passed, pending art review |
| C004 | PROMPT_C004 | `assets/characters/c004m.png` | generated, QC passed, pending art review |
| C005 | PROMPT_C005 | `assets/characters/c005m.png` | generated, QC passed, pending art review |
| C009 | PROMPT_C009 | `assets/characters/c009m.png` | generated, QC passed, pending art review |
| C010 | PROMPT_C010 | `assets/characters/c010m.png` | generated, QC passed, pending art review |
| C011 | PROMPT_C011 | `assets/characters/c011m.png` | generated, QC passed, pending art review |

## Blocked For Retry

| Asset | Prompt | Planned file | Status | Reason |
| --- | --- | --- | --- | --- |
| C008 | PROMPT_C008 | `assets/characters/c008m.png` | blocked, not written to canonical output | 厉螳需要重新生成：虫脸本体，40% 拟人度；高级虫族必须有鞋/靴式足具；匕刃在主手臂外侧作为臂铠刃，主手臂仍有可批阅和拿取物品的手。当前图片服务限流前未产出合格候选。 |

## Art Review Corrections

### C001 Identity Lock

C001 was regenerated after user feedback with this hard reference:

`legacy/pre-remake-2026-06-04/assets/characters/character_shen_weisang_multi_state_board.png`

The accepted C001 image locks Shen Weisang's face shape and hairstyle to the provided board: narrow youthful long face, tightened cheek and jaw structure without sharp adult V-shape, sharp sword-like brows, deep black wary eyes, short messy black hair, broken uneven forehead bangs, close face-framing side locks, and cool restrained hunter expression.

The final C001 file was normalized by padding the generated canvas horizontally before upsampling, so the face and hair proportions were not squeezed or stretched.

### C003 Costume Correction

C003 was regenerated after user feedback that the human costumes were reading as beggar/rag styling and that Lu Qingli and Xue Linqiang were too similar in color. The accepted C003 card now uses maintained wall-foot street-functional clothing: cool gray-blue cropped jacket, terracotta inner layer, muted teal/green-gray bindings, compact pockets, narrow knife, ceramic charm, wooden pass, and subtle ear/neck scale traces. This separates her from C004's heavy old imperial armor.

### C004 Armor Correction

C004 required multiple rejections before acceptance:

| History file | Reason retained |
| --- | --- |
| `assets/characters/history/c004m.v001.png` | Rejected: complete old-wall kit but lacked old Zhaoming imperial inheritance, Mingguang-plus-chainmail structure, and enough unrecoverable war wear. |
| `assets/characters/history/c004m.v002.png` | Rejected: improved imperial inheritance and clean weathered face, but still missed the required Tang Mingguang armor plus chainmail emphasis and irreparable battle-damage inheritance. |

The accepted C004 card locks:

- Old human Zhaoming Empire hereditary armor, not ordinary Grey Wall kit.
- Important armor positions using Tang Mingguang chest/heart-guard forms plus chainmail at neck, sleeve, armpit, side-gap, and plate-edge layers.
- War-worn inheritance: cuts, dents, oxidation, worn gilding, missing inlay fragments, replaced cords, repaired hinges, and damage that maintenance cannot fully restore.
- Zhaoming sun-moon astrolabe crest as only an almost illegible three-quarter remnant on a side/close-up armor plate, not a clear full-body badge.
- Clean weather-beaten face: wind, frost, old scars, stubble, and fatigue, not mud, soot, or unwashed grime.

### C005 Costume Correction

C005 was regenerated after user feedback to avoid ragged refugee styling. The accepted card separates two maintained child states: village clothing with light warm-gray short ru jacket, herb-green apron, herb pouch, scorched dark-red hair tie and intact old shoes; Qingming institutional state with clean white child robe and child-scale insect-wax identifier ring.

### C009 Human Clothing Correction

C009 was regenerated after user feedback that human characters must not all become beggars in identical torn gray clothing. The accepted C009 card keeps Meng Guizang exhausted and smoke-scarred while preserving an old-scholar professional silhouette: structured ash-gray outer robe, indigo inner robe, leather book harness, ochre paper bindings, teal ties, copper clips, bone page markers, and intact archive tools.

### C011 Southern Noble Correction

C011 was regenerated after user feedback that Gu Huaizhang is a southern old-imperial human noble, not a plain gray scholar or refugee. The accepted card restores old-empire silk finery: vermilion silk outer robe, royal-blue silk inner layer, old-gold brocade borders, muted jade lining, refined court tailoring, and red-thread scroll bundle.

## Output Contract QC

| Check | C001-C005 | C009-C011 |
| --- | --- | --- |
| Exact canonical path | pass | pass |
| Short basename <= 20 chars | pass | pass |
| PNG format | pass | pass |
| 2160x3840 minimum resolution | pass | pass |
| Opaque / no alpha | pass | pass |
| 9:16 vertical card format | pass | pass |
| Neutral master character card, not video frame | pass | pass |
| No readable text, labels, UI, watermark, modern logo | pass | pending final art review |
| Retained intermediates under project `history/` only | pass; C004 has two retained rejected files | pass; no retained project intermediates |

## Notes

- C001 source image: `/Users/uroborus/.codex/generated_images/019e9776-a0cf-79f0-8415-864271b9ebe5/ig_00072e2f8a194a6a016a22b1e31d048196bf6e3762843ba951.png`
- C002 source image: `/Users/uroborus/.codex/generated_images/019e9776-a0cf-79f0-8415-864271b9ebe5/ig_00072e2f8a194a6a016a22afa8c6e08196903d8d8c2c630820.png`
- C003 source image: `/Users/uroborus/.codex/generated_images/019e97c3-7cda-7f82-9651-979097917b0a/ig_07becb44ea6fbed1016a22c70546bc8197aa50f4229571387c.png`
- C004 source image: `/Users/uroborus/.codex/generated_images/019e97c3-7cda-7f82-9651-979097917b0a/ig_07becb44ea6fbed1016a22e5594d2481978f02c3d12e22e806.png`
- C005 source image: `/Users/uroborus/.codex/generated_images/019e97c3-7cda-7f82-9651-979097917b0a/ig_07becb44ea6fbed1016a22cad2ee308197873806cc949aab8d.png`
- C009 source image: `/Users/uroborus/.codex/generated_images/019e97cd-3447-7613-83a3-80cefad15700/ig_0ca495dfa15dd983016a22ea6b33608195a0da2a11715c023a.png`
- C010 source image: `/Users/uroborus/.codex/generated_images/019e97cd-3447-7613-83a3-80cefad15700/ig_0ca495dfa15dd983016a22c61ad1e881958428a6397623cd38.png`
- C011 source image: `/Users/uroborus/.codex/generated_images/019e97cd-3447-7613-83a3-80cefad15700/ig_0ca495dfa15dd983016a22d2c77ee88195b981e80c0bd4d936.png`
- C001 final SHA-256: `c91b18535aeafb342a8a30cdf01fb3b66a1a85e891e80c796625ad30e3f7f4b0`
- C002 final SHA-256: `f645200c6a1e50321ff8d84799c9579f42cb4d7bf6d2a806ef9467878b529258`
- C003 final SHA-256: `a93bf6f1fbda53f93880613fbe26a8840315b3aa47cc4c43e6f14f6257921f0a`
- C004 final SHA-256: `a3ed5cc1599d256201f5632de2c67fd5d4a41108943abb5c6c2b76eb8ee926d9`
- C005 final SHA-256: `4258e7f9e43b626d3e37fab21ffe8d73742e21b41f65fbc503d695b03c715e15`
- C009 final SHA-256: `e825d314d5f9428beb9a6a9ba1c8f12ede4df8a4b2af016a8e2b4afd4ac3769b`
- C010 final SHA-256: `c8809ec87a0f70c6939877c96522a92f178fb2659f128bc6304c0693a5965892`
- C011 final SHA-256: `8849b07d861900af146513ec2cb70d56ef42817e032254978f52b9b5f2bda078`
- C004 rejected history SHA-256:
  - `assets/characters/history/c004m.v001.png`: `c0bcca45005e3c15197d0f01349a658404a1d2873c8068d86ec1ad76487bdb51`
  - `assets/characters/history/c004m.v002.png`: `b6cb1106c9622a382411f12fefb33ec2c4b1f36fbce670f29da8ed94b2fbd23e`

Remaining B01 assets not generated or not QC-passed in this pass: C008, C023, C024, C025, C026.
