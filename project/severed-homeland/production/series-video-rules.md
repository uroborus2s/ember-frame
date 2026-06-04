# Severed Homeland Series Video Rules

## Format

- Aspect ratio: `9:16` vertical short drama.
- Frame rate: `24 fps` unless a downstream workflow explicitly overrides it.
- Default clip length: 3-8 seconds per generated video segment; longer dialogue beats must be split by reaction, prop, or transition shots.
- Visual style: hyper-realistic cinematic low-magic Eastern epic; tactile ancient materials; grounded body mechanics.

## Motion Rules

- Every action must preserve real body weight, real speed, natural breathing, contact reaction, and readable motion paths.
- Avoid floaty slow motion, stiff posing, plastic CGI, impossible acrobatics, or magic solutions that replace scripted judgment.
- Exact spoken words do not belong in video prompts; use subtitle and audio plans for dialogue.

## Continuity Rules

- Preserve character bodies, wounds, wardrobe, props, faction hierarchy, geography, and screen direction.
- Gold-red light belongs to old relay, sun-moon marks, alliance fragments, and route traces.
- Insect-wax white, bone white, white register, and black sun marks belong to Qingming/Suming institutional pressure.
- Northern people and beasts must show migration, injury, mutual reliance, and survival pressure; never render them as a mindless horde.

## Quality Floor

- Character identity must be stable before motion beauty.
- Props carrying story information must be readable in the first second of the shot.
- Fire, smoke, steam, snow, collapse, and siege shots must use local cause-and-effect rather than full-screen spectacle.

## Render Feedback Format

Each render note should identify `episode_id`, `shot_id`, `status`, failure type, visible issue, smallest recommended prompt change, and whether the fix is `needs_prompt_tuning`, `needs_asset_fix`, `needs_regenerate`, or `needs_config`.

## AI Audio And Post

- Dialogue, voiceover, SFX, and music are planned by line/cue, not one audio file per shot.
- Short filenames should be used for final audio exports, such as `audio/dialogue/d001.wav`, `audio/sfx/sfx001.wav`, and `audio/music/mx001.wav`.
- Subtitles must come from `script/final-script.md` and post-production files, not from video prompt text.
