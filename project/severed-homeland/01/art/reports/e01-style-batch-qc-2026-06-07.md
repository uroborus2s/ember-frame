# E01 Style Batch QC Report

Date: 2026-06-07

## Result

B04_E01_STYLE is complete and passed coordinator QC. The style dependency for downstream episode-state assets is now satisfied.

## Final Files

| Asset | File | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| E01_F001 | assets/style/f001e01.png | 2048x2048 | 99e124cbf60f42132b0007a9c058478fee6ecf53e1a63110b7f2265acbe1b233 |
| E01_F005 | assets/style/f005e01.png | 3840x2160 | a5f8980e8189956ec6e325372d65ac77d80aebe22c1bfde80602ffc9c52ee993 |
| E01_F006 | assets/style/f006e01.png | 2048x2048 | f7eec8728e538e60af4436ff28dc8f2f1e33486835250606dc6fa84a9f7a80b9 |

## History Files

- assets/style/history/f001e01.v001.png
- assets/style/history/f001e01.v002.png
- assets/style/history/f005e01.v001.png
- assets/style/history/f006e01.v001.png

## QC Notes

- E01_F001: content passed after rejecting the first text-labeled candidate; final board has no readable text and is normalized to 2048x2048.
- E01_F005: passed as a 16:9 landscape composition and local-causality board; final file is normalized to 3840x2160.
- E01_F006: passed as a low-magic and precision-symbol boundary board; final file is 2048x2048.
- No final style image contains readable generated text, UI, watermark, random glyphs, or random insignia.
- Red crosses appear only in prohibited-direction examples.

## Thread Notes

- Primary B04 thread: 019ea079-574d-7751-a1f1-750001408fd5.
- F005 single-asset thread: 019ea082-f0a3-7dd0-9900-79b77cc86b51.
- F006 first single-asset thread stalled without output: 019ea082-fbd3-73e0-a679-c44776699bfe.
- F006 retry thread: 019ea087-b53d-70f1-89a3-417b3af9d23b.
