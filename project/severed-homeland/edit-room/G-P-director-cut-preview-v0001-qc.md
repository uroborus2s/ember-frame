# G-P Director Cut Preview v0001 QC

owner: edit-room + director-room
status: director_cut_preview_generated_needs_final_voice_music_video_retake
date: 2026-06-21

## 1. Output

| item | path |
|---|---|
| preview mp4 | `edit-room/.work/asset-versions/G-P-edit-preview/20260621v0001/G-P_director_cut_preview_v0001_1024x576_24fps_narration_music.mp4` |
| mix wav | `edit-room/.work/asset-versions/G-P-edit-preview/20260621v0001/G-P_director_cut_preview_v0001_mix_48k_stereo.wav` |
| music wav | `music-room/.work/asset-versions/G-P-MX-preview/20260621v0001/G-P_cold_open_score_preview_v0001_48k_stereo.wav` |
| contact sheet | `edit-room/.work/asset-versions/G-P-edit-preview/20260621v0001/G-P_director_cut_preview_v0001_contact.png` |
| manifest | `edit-room/.work/asset-versions/G-P-edit-preview/20260621v0001/G-P_director_cut_preview_v0001_manifest.json` |

## 2. Specs

- resolution: 1024x576 preview
- fps: 24
- frames: 744
- duration: 31.000s
- audio: AAC in mp4, 48 kHz stereo mix source
- narration source: Microsoft Huihui Desktop TTS preview, not final voice
- music source: procedural cold drone / bell / gong preview, not final score

## 3. Director QC

Passed for preview review:

- P-01 is no longer black-screen readable failure; grain gate stays closed and visible.
- P-03 no longer uses the rejected 24fps retime acceleration as formal rhythm.
- Five-shot chain now breathes over 31s instead of 13-19s.
- Narration and music are present and mixed under dialogue-safe levels.
- P-05 keeps the no-stranger-front-face strategy and preserves C001 side/back youth silhouette.

Not final:

- Preview is below final 4K target.
- Narration is TTS preview and needs final voice direction / recording or approved TTS voice.
- Music is a preview bed and needs final stem design, cue sheet, and director listening QC.
- Visuals still use composited / timed existing visual sources; next pass should replace them with final 24fps source shots or approved Comfy retakes.
- No formal `director-room/season-01/01/G-P/{P-XX}/P-XX.mp4` is approved yet.

## 4. Next Orders

- Voice-room: replace preview narration with final narrator voice or approved TTS voice lock; keep the current narration text unless screenwriting/director revises it.
- Music-room: split score into stems: low drone, bone bell, wax needle, rain room tone, copper gong.
- Video-production-room: use this preview as timing reference for 24fps final source retakes.
- Edit-room: keep this as rhythm proof, not final edit; next cut waits for final voice/music/video source.
