# E02 Prompt Repair Score

## Summary

- Project: severed-homeland
- Episode: 02
- Prompt file: project/severed-homeland/02/prompts/art-image-prompts.json
- Initial audit: art-room prompt file and supporting art assets were missing before repair.
- Total prompts: 70
- Average score: 100
- Minimum score: 100
- All prompts at 100: yes

## Repair Actions

- created missing episode art asset index, manifest, design JSON files, style continuity bible, thread plan, and art-image prompt package
- generated production_metadata.reference_inputs from global parents, episode dependencies, costumes, props, locations, and style assets
- kept production ids, source paths, usage, workflow labels, and shot codes out of model-visible prompt text
- rebuilt all prompts with six model-visible sections and copy_ready reference image instructions
- separated reusable 1:1/3:2 asset-card prompts from project-ratio vertical reference-frame prompts
- added line-control, mask, and post-composite rules for exact text, symbols, registers, emblems, seals, blood records, jade marks, and relay tokens

## Scores By Type

| Type | Count | Average | Minimum | All 100 |
| --- | ---: | ---: | ---: | --- |
| style | 3 | 100 | 100 | yes |
| character | 8 | 100 | 100 | yes |
| location | 5 | 100 | 100 | yes |
| prop | 9 | 100 | 100 | yes |
| costume | 5 | 100 | 100 | yes |
| reference_frame | 40 | 100 | 100 | yes |

## Prompt Scores

| Prompt | Asset | Type | Reference Inputs | Score | Status |
| --- | --- | --- | ---: | ---: | --- |
| PROMPT_E02_F001 | E02_F001 | style | 1 | 100 | pass_100 |
| PROMPT_E02_F005 | E02_F005 | style | 1 | 100 | pass_100 |
| PROMPT_E02_F006 | E02_F006 | style | 1 | 100 | pass_100 |
| PROMPT_E02_C002 | E02_C002 | character | 7 | 100 | pass_100 |
| PROMPT_E02_C006 | E02_C006 | character | 5 | 100 | pass_100 |
| PROMPT_E02_C005 | E02_C005 | character | 5 | 100 | pass_100 |
| PROMPT_E02_C017 | E02_C017 | character | 5 | 100 | pass_100 |
| PROMPT_E02_C001 | E02_C001 | character | 6 | 100 | pass_100 |
| PROMPT_E02_C007 | E02_C007 | character | 6 | 100 | pass_100 |
| PROMPT_E02_C016 | E02_C016 | character | 6 | 100 | pass_100 |
| PROMPT_E02_C018 | E02_C018 | character | 5 | 100 | pass_100 |
| PROMPT_E02_L001A | E02_L001A | location | 3 | 100 | pass_100 |
| PROMPT_E02_L001B | E02_L001B | location | 3 | 100 | pass_100 |
| PROMPT_E02_L001C | E02_L001C | location | 3 | 100 | pass_100 |
| PROMPT_E02_L001D | E02_L001D | location | 3 | 100 | pass_100 |
| PROMPT_E02_L001E | E02_L001E | location | 3 | 100 | pass_100 |
| PROMPT_E02_P002A | E02_P002A | prop | 4 | 100 | pass_100 |
| PROMPT_E02_P008 | E02_P008 | prop | 3 | 100 | pass_100 |
| PROMPT_E02_P003 | E02_P003 | prop | 4 | 100 | pass_100 |
| PROMPT_E02_P004A | E02_P004A | prop | 4 | 100 | pass_100 |
| PROMPT_E02_P004B | E02_P004B | prop | 4 | 100 | pass_100 |
| PROMPT_E02_P002B | E02_P002B | prop | 4 | 100 | pass_100 |
| PROMPT_E02_P004C | E02_P004C | prop | 4 | 100 | pass_100 |
| PROMPT_E02_P005 | E02_P005 | prop | 3 | 100 | pass_100 |
| PROMPT_E02_P001 | E02_P001 | prop | 4 | 100 | pass_100 |
| PROMPT_E02_K001 | E02_K001 | costume | 3 | 100 | pass_100 |
| PROMPT_E02_K002 | E02_K002 | costume | 3 | 100 | pass_100 |
| PROMPT_E02_K003 | E02_K003 | costume | 3 | 100 | pass_100 |
| PROMPT_E02_K004 | E02_K004 | costume | 3 | 100 | pass_100 |
| PROMPT_E02_K006 | E02_K006 | costume | 3 | 100 | pass_100 |
| PROMPT_E02_R001 | E02_R001 | reference_frame | 10 | 100 | pass_100 |
| PROMPT_E02_R002 | E02_R002 | reference_frame | 10 | 100 | pass_100 |
| PROMPT_E02_R003 | E02_R003 | reference_frame | 10 | 100 | pass_100 |
| PROMPT_E02_R004 | E02_R004 | reference_frame | 10 | 100 | pass_100 |
| PROMPT_E02_R005 | E02_R005 | reference_frame | 10 | 100 | pass_100 |
| PROMPT_E02_R006 | E02_R006 | reference_frame | 10 | 100 | pass_100 |
| PROMPT_E02_R007 | E02_R007 | reference_frame | 10 | 100 | pass_100 |
| PROMPT_E02_R008 | E02_R008 | reference_frame | 10 | 100 | pass_100 |
| PROMPT_E02_R009 | E02_R009 | reference_frame | 14 | 100 | pass_100 |
| PROMPT_E02_R010 | E02_R010 | reference_frame | 14 | 100 | pass_100 |
| PROMPT_E02_R011 | E02_R011 | reference_frame | 14 | 100 | pass_100 |
| PROMPT_E02_R012 | E02_R012 | reference_frame | 14 | 100 | pass_100 |
| PROMPT_E02_R013 | E02_R013 | reference_frame | 14 | 100 | pass_100 |
| PROMPT_E02_R014 | E02_R014 | reference_frame | 14 | 100 | pass_100 |
| PROMPT_E02_R015 | E02_R015 | reference_frame | 14 | 100 | pass_100 |
| PROMPT_E02_R016 | E02_R016 | reference_frame | 14 | 100 | pass_100 |
| PROMPT_E02_R017 | E02_R017 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E02_R018 | E02_R018 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E02_R019 | E02_R019 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E02_R020 | E02_R020 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E02_R021 | E02_R021 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E02_R022 | E02_R022 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E02_R023 | E02_R023 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E02_R024 | E02_R024 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E02_R025 | E02_R025 | reference_frame | 11 | 100 | pass_100 |
| PROMPT_E02_R026 | E02_R026 | reference_frame | 11 | 100 | pass_100 |
| PROMPT_E02_R027 | E02_R027 | reference_frame | 11 | 100 | pass_100 |
| PROMPT_E02_R028 | E02_R028 | reference_frame | 11 | 100 | pass_100 |
| PROMPT_E02_R029 | E02_R029 | reference_frame | 11 | 100 | pass_100 |
| PROMPT_E02_R030 | E02_R030 | reference_frame | 11 | 100 | pass_100 |
| PROMPT_E02_R031 | E02_R031 | reference_frame | 11 | 100 | pass_100 |
| PROMPT_E02_R032 | E02_R032 | reference_frame | 11 | 100 | pass_100 |
| PROMPT_E02_R033 | E02_R033 | reference_frame | 13 | 100 | pass_100 |
| PROMPT_E02_R034 | E02_R034 | reference_frame | 13 | 100 | pass_100 |
| PROMPT_E02_R035 | E02_R035 | reference_frame | 13 | 100 | pass_100 |
| PROMPT_E02_R036 | E02_R036 | reference_frame | 13 | 100 | pass_100 |
| PROMPT_E02_R037 | E02_R037 | reference_frame | 13 | 100 | pass_100 |
| PROMPT_E02_R038 | E02_R038 | reference_frame | 13 | 100 | pass_100 |
| PROMPT_E02_R039 | E02_R039 | reference_frame | 13 | 100 | pass_100 |
| PROMPT_E02_R040 | E02_R040 | reference_frame | 13 | 100 | pass_100 |
