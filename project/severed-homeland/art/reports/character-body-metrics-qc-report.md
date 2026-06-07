# Character Body Metrics QC Report

- Project: `project/severed-homeland`
- Scope: all character master cards `C001` through `C026`
- Date: 2026-06-07
- Reviewer: art-room body metrics pass
- Status: `body_metrics_qc_complete_corrections_required`

## Review Method

Authoritative baseline:

- `bible/continuity.md:44`: character height, weight, build, posture, scars, and morphology in `bible/characters.md` are continuity fields and must not be changed casually.
- `bible/characters.md`: named character and faction/body-scale baseline.
- `01/continuity/visual-continuity-bible.json`: episode visual continuity for early human/Suming hierarchy references.
- `assets/asset-index.json`: current `body_metrics`, `identity_lock.height_body_type`, and design summaries.
- `assets/characters/c001m.png` through `assets/characters/c026m.png`: visual card review via contact sheet plus targeted full-card checks.

This report only audits body scale, build, and weight consistency. It does not change images or index files.

## Executive Summary

The character card set is not uniformly broken. Most human named characters and group crowd templates are visually usable, and the newest C004/C008 fixes are visible. The main risk is that several `asset-index.json` body metrics no longer match the Bible, so future Director Room prompt refreshes may inherit wrong body scales even when the current image looks acceptable.

Highest priority conflicts:

| Priority | Asset | Problem |
| --- | --- | --- |
| P0 | C016 | Current index says `170-185cm`, but Bible says Suming基层虫吏 must not be below `190cm`; this breaks the whole官吏/奴兵/虫兵 height hierarchy. |
| P0 | C018 | Current index says `185-205cm`, but Bible says pure insect foot soldiers are `200-230cm`; lower bound is too human. |
| P0 | C019 | Current index says `205-225cm`, but Bible says heavy insect soldiers are `220-260cm`; it collapses the tier gap with C018. |
| P0 | C020 | Current index says Northern siege troops are `175-340cm`, missing the `145-165cm` snow-badger diggers and all subtype weight bands. |
| Resolved | C008 | User confirmed the latest `220cm / 150kg` elite insect-general version is canon; `bible/characters.md` has been updated accordingly. No redraw required for body metrics. |
| Resolved | C010 | Metadata and prompt updated to Bible-compatible `169cm / 52kg`, preserving 鹿弥 as a light寻灾源派萨满 rather than generic攻城鹿族祭兵. No redraw required. |
| Resolved | C012 | Regenerated on 2026-06-07 as corrected `202-210cm / 140-155kg` elite white-bear guard. New canonical passed visual and file QC. |
| Resolved | C014 | Metadata and prompt updated to `218-228cm / 210-260kg`; existing image already reads sufficiently heavy, so no redraw required. |
| Resolved | C021 | Metadata and prompt updated with per-beast size ranges for mammoth, rhino, turtle, yak, python, wyvern, thunder lizard, and frost wolf. No redraw required. |

## Per-Asset Findings

### Named Human And Core Characters

| Asset | Current body metrics | Bible / continuity baseline | Visual judgment | QC result | Required action |
| --- | --- | --- | --- | --- | --- |
| C001 沈维桑 | `173cm`, `61kg`, lean hunter | Bible: `175cm`, `64kg`; episode continuity also `175cm` | Visual reads as a slim late-teen hunter. The approved face/body reference is stable, but metadata is 2cm/3kg below Bible. | Minor mismatch | Either align index to `175cm / 64kg`, or explicitly update Bible if the approved legacy reference is now canon at `173cm / 61kg`. No redraw needed. |
| C002 晏南枝 | `168cm`, `50kg`, slim and upright | Bible: `168cm`, `50kg` | Visual reads as tall, straight, restrained流亡皇室 silhouette. | Pass | No body-scale action. |
| C003 陆青砾 | `156cm`, `44kg`, narrow agile frame | Bible: `157cm`, `43kg` | Visual reads small, quick, wall-foot混裔. Difference is within practical art tolerance. | Pass with tolerance | No action unless strict metadata normalization is desired. |
| C004 薛临墙 | `182cm`, `82kg`, broad but hunger-pressed | Bible: `181cm`, `82kg` | Visual now shows wide old wall-master body, round chest mirror/heart guard, damaged heart-guard pit, and nearly illegible Zhaoming remnant. | Pass | No body-scale action. Keep護心鏡 and broken visual effects locked. |
| C005 沈照眠 | `130cm`, `27kg`, child build | Bible: `132cm`, `26kg`; episode continuity `132cm` | Visual reads as a fragile child in both village and Qingming states. | Pass with tolerance | Optional metadata normalization to `132cm / 26kg`; no redraw. |
| C006 罗青禾 | `163cm`, `54kg`, stable compact strength | Bible: `163cm`, `54kg` | Visual reads as not tall but steady, with worker-mother strength. | Pass | No action. |
| C007 白翳 | `205cm`, `78kg`, extremely tall and thin | Bible: `205cm`, `78kg` | Visual reads as high, clean, thin Qingming official pressure, not muscle mass. | Pass | No body-scale action. |
| C009 孟归藏 | `170cm`, `55kg`, dry scholar build | Bible: `172cm`, `60kg` | Visual reads as thin old-scholar/archivist. Metadata makes him slightly too small and underweight. | Minor mismatch | Align index to `172cm / 60kg` unless a new canon decision intentionally makes him more wasted. No redraw needed. |
| C011 顾怀章 | `180cm`, `65kg`, old thin court posture | Bible: `176cm`, `65kg`; episode continuity `176cm` | Visual reads as a southern old noble with formal posture. Height field is 4cm too tall. | Minor mismatch | Align index to `176cm / 65kg`; no redraw needed. |
| C022 沈季衡 | `178cm`, `67kg`, lean travel-worn surveyor | Bible: `178cm`, `67kg` | Visual reads as a weathered middle-aged route surveyor, not an old hermit. | Pass | No action. |

### Suming / Qingming / Insect Hierarchy

| Asset | Current body metrics | Bible / continuity baseline | Visual judgment | QC result | Required action |
| --- | --- | --- | --- | --- | --- |
| C008 厉螳 | `220cm`, `150kg`, heavy insect general | Bible updated on 2026-06-07 to `220cm / 150kg`, high-ranking heavy combat insect commander, integrated insect face, enclosed segmented boots. | Visual passes recent user requirements: noticeably taller than human, integrated insect head rather than mask, enclosed segmented boots, and about half humanoid command readability. | Resolved / pass | No redraw required for body metrics. Future prompt refresh should inherit the updated Bible baseline rather than the older `218cm / 118kg` narrow-blade version. |
| C016 肃明基层虫吏 | `170-185cm`, slim/medium official | Bible: must be insect, not below `190cm`, common `190-210cm`; episode continuity also `190-210cm` | Visual face, white official robe, shoes, ledger/seal/abacus are correct. The metric field is wrong and weakens hierarchy. | P0 fail in metadata | Change body metrics to `190-210cm`, "tall elongated official, slim but above human height." Add scale refs against 170cm human and lower slave soldier. Redraw only if a future scale panel shows under-190 body. |
| C017 混血奴兵 | `168-180cm`, medium thin | Bible: `170-200cm`, mixed human-insect slave soldier | Visual reads as hybrid清污军户 with human expression and insectized scalp/skin; height panel does not fully protect the 200cm upper bound. | P1 metadata mismatch | Change body metrics to `170-200cm`, with most common examples around human-to-tall-human scale. No redraw required unless later scenes need the tallest slave tier. |
| C018 普通纯虫族小兵 | `185-205cm`, light-mid hard shell | Bible: pure insect foot soldiers `200-230cm`; episode continuity `200-230cm` | Visual reads as taller than human and strongly insectoid. The image can work, but index lower bound is too human. | P0 metadata fail | Change body metrics to `200-230cm`; emphasize low, forward, strong body and clear height above C017. Image likely reusable after index correction. |
| C019 中阶重甲虫士兵 | `205-225cm`, `130-180kg` | Bible: heavy insect soldiers `220-260cm`, wider than C018, lower than high heavy generals | Visual reads as a heavy shield-wall insect soldier and looks usable. Metadata makes the tier too short and too close to C018. | P0 metadata fail | Change body metrics to `220-260cm`, broad heavy armor, clearly wider than C018. Image likely reusable; add or verify explicit scale reference in future derivative. |

### Northern Named And Functional Characters

| Asset | Current body metrics | Bible baseline | Visual judgment | QC result | Required action |
| --- | --- | --- | --- | --- | --- |
| C010 鹿弥 | Updated to `169cm`, `52kg`, light寻灾源派 deer shaman | Bible: `169cm`, `52kg`; named尋灾源派 young shaman, not generic siege ritual troop | Existing visual can remain because the issue was metadata/prompt drift rather than confirmed body failure. | Resolved / metadata only | Completed on 2026-06-07: index and prompt corrected; no redraw required. |
| C012 赫连雪岱 | Updated to `202-210cm`, `140-155kg`, elite white-bear guard | Bible: `202-210cm`, `125-155kg`, bigger than human heavy guard but not low-grade giant-beast build | Regenerated canonical now reads tall, broad and protective, but no longer C014-style shield-worker mass. | Resolved / regenerated | Completed on 2026-06-07: canonical replaced, prompt reviewed, file QC passed. See `art/reports/c012-body-metrics-regeneration-qc-2026-06-07.md`. |
| C013 乌岚 | `185cm`, `72kg`, long-legged black-wolf scout | Bible: `182-190cm`, `68-82kg` | Visual reads lean, fast, low-forward wolf scout. | Pass | No action. |
| C014 拓跋砚熊 | Updated to `218-228cm`, `210-260kg` | Bible: `218-228cm`, `210-260kg`, ordinary human heavy soldier two-to-three times visual weight | Existing visual already reads massive and heavy enough for the Bible role. | Resolved / metadata only | Completed on 2026-06-07: index and prompt corrected; no redraw required. |
| C015 青翎鸦见 | `182cm`, `60kg` | Bible: `172-182cm`, `52-64kg` | Visual reads light-boned, narrow, crow-scout. Height is at upper bound but acceptable. | Pass | No action. |

### Northern Group And Beast Relationship Templates

| Asset | Current body metrics | Bible baseline | Visual judgment | QC result | Required action |
| --- | --- | --- | --- | --- | --- |
| C020 北境攻城兵种群像 | `175-340cm`, no subtype weights | Bible includes black-tooth axemen `225-245cm / 160-220kg`; ox shield troops `205-230cm / 180-260kg`; white-mane wolf riders `185-205cm / 80-115kg`; snow-badger diggers `145-165cm / 90-130kg`; trolls `280-340cm / 350-600kg`; bird climbers `175-195cm / 55-80kg`; deer ritual troops `175-210cm / 60-120kg`; lion cavalry `205-225cm / 130-180kg` | Visual shows multiple Northern combat types and scale variety, but the current index misses the shortest snow-badger tier and all weight bands. | P0 group metrics incomplete | Replace the single broad height field with subtype body metrics. If image detail review confirms snow-badger diggers are not visibly short and barrel-bodied, schedule targeted redraw/patch. |
| C021 北境共生兽关系 | Updated with per-beast dimensions and weights | Bible gives exact ranges: mammoth shoulder `380-450cm`, `6-9t`; rhino shoulder `260-320cm`, `3-5t`; turtle shell `180-240cm` high and `400-600cm` wide, `8-14t`; yak shoulder `180-220cm`, `900-1300kg`; ice python length `8-14m`; wyvern length `300-400cm`, wingspan `600-900cm`; thunder lizard length `400-600cm`; frost wolf shoulder `90-120cm`, `80-130kg` | Existing relation card is strong:兽 and handler interaction is readable. | Resolved / metadata only | Completed on 2026-06-07: index and prompt now carry exact scale ranges; no redraw required. |

### Human Crowd Templates

| Asset | Current body metrics | Baseline | Visual judgment | QC result | Required action |
| --- | --- | --- | --- | --- | --- |
| C023 人族逃难流民群像 | children `110-140cm`, youth `145-165cm`, adults `155-175cm`, stooped elders | Bible requires human crowd diversity and not making all humans default ragged refugees. Asset plan says C023 is extreme refugee state, not ordinary people. | Visual shows age, gender, load-bearing, exhaustion, and migration pressure. | Pass | No body-scale action. Keep "extreme refugee state only" warning. |
| C024 边墙普通军户群像 | youth `140-165cm`, adults `160-185cm`, elders/disabled stooped | Bible requires wall households from young carriers to old soldiers, not a line of same soldiers. | Visual shows mixed military household sizes and duties. | Pass | No action. |
| C025 普通人族平民群像 | children `105-145cm`, youth `145-165cm`, adults `155-180cm`, elders stooped | Bible requires production-life, regional, class, and age diversity. | Visual reads as ordinary poor working civilians, not refugees or soldiers. | Pass | No action. |
| C026 墙下集市无籍者与粮牌黑市群像 | children `115-145cm`, youth `145-170cm`, adults `155-185cm`, some hybrids taller but not above slave-soldier pressure | Baseline requires wall-foot market order,无籍者,混裔,black-market hierarchy, and distinction from ordinary people/refugees/military households. | Visual shows market underclass scale and mixed ages. Because C017 slave-soldier range should be `170-200cm`, C026's "not above slave-soldier pressure" remains sensible but should refer to corrected C017 range. | Pass with dependency note | No image action. After C017 correction, update wording if needed: taller hybrids can approach but not exceed the oppressive read of `170-200cm` slave soldiers. |

## Correction Plan

1. Metadata-only high priority:
   - C016: `190-210cm`, tall elongated official, above human scale.
   - C017: `170-200cm`, human-hybrid slave soldier range.
   - C018: `200-230cm`, pure insect foot soldier.
   - C019: `220-260cm`, heavy insect shield-wall tier.
   - C020: replace broad range with subtype height and weight bands.

2. Canon-decision required before redraw:
   - C001: decide whether approved legacy card body remains 173cm/61kg or Bible/episode 175cm/64kg is restored.

3. Potential visual redraw or targeted correction:
   - C020: if snow-badger digger subtype is not visibly below human height and barrel-bodied, redraw or add a focused subtype card.

## Pass List

No body-scale action required for: C002, C003, C004, C005, C006, C007, C013, C015, C022, C023, C024, C025.

Pass with minor metadata normalization: C001, C009, C011, C026.

Requires correction before Director Room prompt refresh: C016, C017, C018, C019, C020.
