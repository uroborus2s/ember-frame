# Episode 01 Inheritance And Path Repair

## Status

- B01 character outputs are rejected and require retry with hard series master identity references.
- B02 location outputs are rejected and require retry with hard series master location references.
- B05 reference frames and B06 shot overrides are blocked until B01 and B02 pass inheritance QC.
- Episode state card paths now route under `01/assets/<type>/`; root `assets/` remains for whole-series reusable assets.

## Corrected Rule

Character episode state cards may only change wardrobe, dirt, wounds, props, emotion, and action state. Face, body, age impression, hairstyle, silhouette, and movement habits must match the series master card with no visible deviation.

Location episode scene cards may only change camera distance, angle, weather, time, damage, staging, and local props. Geography, entrances, exits, landmark positions, materials, and spatial structure must match the series master scene card with no visible deviation.

## File Movement

Moved 33 episode image files out of root episode-contaminated locations.

## Rejected Batches

- `B01_E01_CHARACTERS`: identity drift risk/current outputs rejected.
- `B02_E01_LOCATIONS`: location inheritance drift risk/current outputs rejected.
