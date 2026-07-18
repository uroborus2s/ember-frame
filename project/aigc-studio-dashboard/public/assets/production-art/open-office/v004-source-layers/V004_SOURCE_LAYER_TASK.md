# V004 Source-Layer Production Task

Status: active production pass

Goal: rebuild the open-office 2.5D scene from source layers, not by placing obvious stickers on the old plate.

Required outputs:

- `open_office_v004_interior_base.png`: clean interior base, same open-office art direction, no exterior trees baked into the room.
- `open_office_v004_window_mask.png`: white-only transparent window area where the tree animation is allowed to appear.
- `open_office_v004_window_foreground.png`: window frame, glass highlights, reflections, and interior foreground detail that must sit above the tree animation.
- `tree_source_v004.png`: separate exterior tree canopy source plate for animation.
- `tree_frames/00.png` through `tree_frames/47.png`: loopable subtle wind frames, masked to windows only.
- `open_office_scene_v004.json`: runtime manifest with navmesh, anchors, staff, QC routes, control desk, mask and layer references.
- Frontend manifest target: `open_office_scene_v004.json`.

ImageGen edit prompt for the interior source plate:

```text
Use case: precise-object-edit
Asset type: production 2.5D game background source layer
Input image: reference and edit target. Preserve the exact open office composition, perspective, camera angle, desk layout, seated staff positions, desk props, lighting direction, walls, floor, and overall warm realistic 2.5D office style.
Primary request: create a clean source-layer version of this open-office game background for runtime animation compositing. Replace only the exterior view visible through the large upper windows with clean warm translucent frosted glass and pale daylight glow. Remove all visible outdoor trees, leaves, branches, and foliage from the window glass. The interior plants that are physically inside the room must remain.
Composition/framing: same wide isometric 2.5D composition, same 1536x900 aspect, no crop changes.
Lighting/mood: warm cinematic office sunlight, realistic reflections, polished production game background.
Constraints: no UI, no labels, no text, no watermark. Do not add new walls or block the walking aisles. Do not move people, desks, computers, windows, chairs, plants, doors, or control desk. Do not paint trees inside the room. The window area must be clean enough for a separate animated tree layer to be composited behind it.
Avoid: pasted characters, floating people, ghosting, smears, extra limbs, distorted desks, duplicate monitors, outdoor foliage baked into the interior plate.
```

ImageGen prompt for the exterior tree source plate:

```text
Use case: game asset texture
Asset type: exterior tree canopy animation source plate
Primary request: a wide realistic sunlit tree canopy seen outside an office window, soft background depth, warm daylight, subtle leaf clusters and branches, designed as a separate animation layer behind glass.
Composition/framing: wide horizontal image, continuous foliage coverage, no buildings, no sky gaps that form hard silhouettes, no room interior.
Lighting/mood: warm afternoon sunlight matching a premium 2.5D office background.
Constraints: no window frames, no interior walls, no people, no UI, no text, no watermark.
Avoid: horror ghosting, double exposure, high contrast flicker, huge close leaves, painterly smear.
```
