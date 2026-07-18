# Open Office v003 Layered Animation Task

Goal: replace the failed window-tree overlay with a real layered game background.

Required layers:

- `open_office_v003_interior_base.png`: current fixed-staff office with dynamic window areas neutralized.
- `open_office_v003_window_mask.png`: exact playable render mask for exterior animation, only glass areas.
- `open_office_v003_window_foreground.png`: window/frame edge foreground drawn above tree animation.
- `tree_source_v003.png`: imagegen source texture for exterior foliage.
- `tree_frames/00.png` to `tree_frames/47.png`: full-canvas transparent loop frames.
- `open_office_v003_preview.png`: composited still for QC.

Rules:

- No tree pixels over wall art, desks, bookshelves, indoor wall, or UI.
- Tree animation must be behind foreground glass/frame edges.
- Existing v001 window tree animation stays disabled.
- If the current base cannot support a larger clean mask, keep the mask conservative rather than faking a big window animation.

Prompt used for `tree_source_v003.png`:

Use case: stylized-concept
Asset type: exterior tree texture for masked 2.5D game window animation
Primary request: generate a soft sunlit exterior tree canopy texture for large office windows, designed to be animated behind window masks.
Scene/backdrop: dense leafy trees outside a premium office, warm daylight, layered foliage depth, no interior objects.
Subject: small natural leaves, branches, soft sun patches, subtle atmospheric depth.
Style/medium: polished realistic 2.5D game art texture, not photoreal stock, compatible with warm AIGC office scene.
Composition/framing: wide landscape, foliage fills the frame, no window frames, no walls, no furniture.
Lighting/mood: warm morning light, soft highlights, low contrast enough to sit behind glass.
Constraints: no people, no animals, no text, no watermark, no building interior, no giant high-contrast branches dominating the frame.
Avoid: flat green texture, obvious repeating pattern, harsh foreground cutout, dark forest, cartoon style.
