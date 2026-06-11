# Episode 12 Targeted Asset QC Report

## SC002-SH003 Asset

- Asset: `R12_SC002_SH003`
- Shot: `SC002-SH003`
- File: `12/assets/reference-frames/sc002-sh003.png`
- Source: projectless `imagegen-task`
- Thread: `019eb190-a8fe-7471-9a9c-e7b6b02e6266`
- SHA-256: `6568c20294e4262d24109ebd7dc6c97441710fb1c9325aa678b978f9d1fc1760`
- Status: `passed_with_limitations_2026-06-10`

## SC002-SH003 Visual QC

- File format: PNG.
- Canvas: 16:9.
- Dimensions: 3840x2160.
- Background policy: video frame, alpha forbidden.
- Foreground: alliance fragment, blood-record strip, moon-white jade shard, red thread, insect-wax needle, cracked black stone, and snow mud are readable.
- Midground: Shen Weisang handing the short knife to Lu Qingli is readable, and Lu Qingli's reaction remains present without stealing the foreground focus.
- Background: broken tower half-height exit, falling stone, cold snow wind, and pressure silhouettes are present with reduced detail.
- Continuity: inherits `L011`, `P007`, `P002`, `P004`, `C001`, `C002`, `C003`, `C007`, `C010`.
- Negative checks: no visible UI, watermark, modern prop, subtitle, or clearly readable generated text was observed in parent visual review.

## SC002-SH003 Notes

- Local master reference images were not attached to the isolated imagegen-task; inheritance was prompt-guided and parent-reviewed.
- Source image was 1672x941; canonical output was upsampled to 3840x2160 for the reference-frame contract.
- Any exact multi-clan marks or sun-moon emblems still require line control, mask, or post-composite if later shots need precision.

## SC002-SH003 History

- `12/assets/reference-frames/history/sc002-sh003.v001.png`: main-thread fallback candidate, not canonical.
- `12/assets/reference-frames/history/sc002-sh003.v002.png`: accepted isolated imagegen-task source before upsampling.

## Asset

- Asset: `E12_R024`
- Shot: `SC003-SH002`
- File: `12/assets/reference-frames/r024e12.png`
- Source: built-in `imagegen-task`
- Source group: `019eb18b-167e-78a3-90ed-806a0b95a82a`
- SHA-256: `5825b8cdc6a984f57e608a95db80a81dfc6b43e48a585cab2b4eb71b25b84ba1`

## Visual QC

Passed:

- The half-height collapsed exit is immediately readable.
- Shen Weisang is the main subject and is low against the compressed opening.
- Foreground, midground, and background are separated.
- The escape group remains visible without overtaking the subject.
- Distant Bai Yi pressure reads as a white insect-official silhouette.
- The frame uses video-frame context, not a transparent or isolated card background.

Cautions:

- Actual file resolution is `1672x941`, below the target `3840x2160` reference-frame contract.
- The blood-record/alliance fragment area uses abstract generated marks. Treat them as non-final texture only; any close-up or precise symbol/text beat still requires line control, redraw, or post-composite.

## Contract Status

`generated_candidate_internal_qc_passed_pending_4k_contract`

The image is usable as a composition and continuity candidate for `SC003-SH002`, but final video handoff should regenerate or upscale to `3840x2160` or higher and re-run QC.

## SC002-SH001 Assets

- Asset: `E12_R001`
- Shot: `SC002-SH001`
- File: `12/assets/reference-frames/r001e12.png`
- Source: prompt-only `imagegen-task`
- Source group: `019eb187-1383-77a1-9b5e-1a1274101db8`
- SHA-256: `a04f1b6589e26dd96e963a6c5015cd17d68f17f99e751957a58252d9f8aa86a2`
- Status: `internal_qc_passed_with_notes`

- Asset: `E12_R002`
- Shot: `SC002-SH001`
- File: `12/assets/reference-frames/r002e12.png`
- Source: prompt-only `imagegen-task`
- Source group: `019eb187-1383-77a1-9b5e-1a1274101db8`
- SHA-256: `b88855b01fae4d4d384d8c2a5b76a0cf2b3ebe1617cb3be21da832791f163992`
- Status: `internal_qc_passed_sc002_sh001_corrected`

## SC002-SH001 Visual QC

Passed:

- Both canonical files are PNG, RGB, alpha forbidden, `3840x2160`.
- `E12_R001` reads as the eye-level establishing start of the slow push: black stone stair geometry, half-height exit, Lu Qingli, Shen Weisang, Yan Nanzhi, Lu Mi, Bai Yi and the alliance fragment are readable.
- `E12_R002` has been redone after review: it now reads as the slow-push endpoint of the same establishing wide shot, with Lu Qingli loosening her own trapped outer garment and Shen Weisang still separate near the center axis. It no longer depicts the `SC002-SH002` rescue exchange.
- Foreground, midground and background are separated in both images.
- Both images use video-frame context, not transparent or isolated card backgrounds.
- No visible UI, watermark, subtitle, modern prop, or clearly readable generated text was observed in parent visual review.

Cautions:

- Source imagegen candidates were `1672x941`; canonical files were upscaled to `3840x2160` for the reference-frame contract.
- Local master reference images were not attached to the isolated imagegen-task; inheritance was prompt-guided and parent-reviewed.
- Exact multi-clan marks, sun-moon emblems, blood-record details, or readable prop inscriptions still require line control, mask, redraw, or post-composite if later shots need precision.
- The first unsafe wording attempt was blocked by image safety; final reusable prompts use non-graphic wording such as `red-brown weathering`, `small utility tool`, and `old record bundle`.
- The corrected `E12_R002` prompt additionally forbids foreground paper, writing, glyphs, object exchange, character contact, and medium close-up rescue framing.

## SC002-SH001 History

- `12/assets/reference-frames/history/r001e12.v001-imagegen-source-20260610.png`: original `1672x941` imagegen source for `E12_R001`.
- `12/assets/reference-frames/history/r002e12.v001-imagegen-source-20260610.png`: original `1672x941` imagegen source for `E12_R002`.
- `12/assets/reference-frames/history/r002e12.v002-before-sc002-sh001-wide-redo-20260610.png`: superseded 4K tail-frame image that drifted toward `SC002-SH002`.
- `12/assets/reference-frames/history/r002e12.v003-imagegen-source-wide-redo-20260610.png`: corrected `1672x941` imagegen source for the current `E12_R002`.
