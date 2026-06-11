# Episode 03 Asset Prep Plan - Targeted SC003-SH001

## Summary

- Scope: targeted art-room generation for `SC003-SH001` only.
- Planned assets: 1 reference frame.
- Output directory: `03/assets/reference-frames/`.
- This pass does not generate full Episode 03 character, location, prop, costume, or style card batches.

## Creation Order

| Order | Asset | Type | Phase | Depends On | Blocks | Output |
| ---: | --- | --- | --- | --- | --- | --- |
| 21 | E03_R021 | reference_frame | shot_reference_frames | C001, C002, C006, C017, L001, P001, F002, F003 | SC003-SH001 director prompt refresh | `03/assets/reference-frames/r021e03.png` |

## Asset Contract

`E03_R021` is a video-generation reference frame, not a neutral asset card.

Output format:

```json
{
  "deliverable_kind": "video_generation_reference_frame",
  "file_format": "png",
  "minimum_resolution": "4096x2304",
  "background_policy": "video_frame",
  "alpha_policy": "forbidden",
  "canvas_aspect_ratio": "16:9",
  "required_views": [
    "single cinematic frame matching project delivery ratio",
    "clear camera distance and camera angle",
    "screen direction and action state locked for SC003-SH001",
    "lighting, weather/time, and fire-smoke state visible in-frame"
  ],
  "composition_layers": {
    "foreground": "herb-ash-covered carved mark, old white stone edge, half relay token or hand beat",
    "midground": "Shen Weisang and Yan Nanzhi running to the far side of the ruined old well",
    "background": "ruined old-well mouth, well frame, low hidden-door seam, controlled fire-smoke pressure, distant slave soldier"
  },
  "qc_checks": [
    "16:9 canvas",
    "foreground, midground, and background are visibly separated",
    "no transparent or isolated card background",
    "camera distance, angle, lighting, time of day, screen direction, and action state are readable",
    "Shen Weisang and Yan Nanzhi remain readable without becoming close-up beauty portraits",
    "Luo Qinghe appears only through inherited herb-ash mark evidence, not as a present living figure",
    "distant repeated forms stay grouped and non-granular",
    "no watermarks, modern UI, random text, or wrong faction symbols"
  ]
}
```

## Dependency Notes

- `C001` locks Shen Weisang's hunter silhouette, left-shoulder injury, grey-brown and herb-green costume, bow, route pack, and half-token continuity.
- `C002` locks Yan Nanzhi's fugitive robe, red-thread hair, upright ritual posture, and restrained noble silhouette.
- `C006` contributes Luo Qinghe's herb and old-relay trace logic only; she should not appear alive in the present frame.
- `C017` locks the slave soldier as a hybrid institutional pursuer, distinct from pure insect soldiers and officials.
- `L001` locks Canyangao old-well geography and fire-aftermath material.
- `P001` locks the half sun-moon relay token as a worn, partial route key, not a magic weapon.
