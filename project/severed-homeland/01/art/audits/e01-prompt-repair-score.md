# E01 Prompt Repair Score

## Summary

- Project: severed-homeland
- Episode: 01
- Prompt file: project/severed-homeland/01/prompts/art-image-prompts.json
- Total prompts: 83
- Average score: 100
- Minimum score: 100
- All prompts at 100: yes

## Repair Actions

- rewrote model_visible_prompt into six clean sections for every first-episode asset
- removed production labels, shot codes, source paths, workflow labels, approval language, and untranslated camera-template residue from visible prompts
- added production_metadata.reference_inputs from parent_asset_id and depends_on_assets without copying those ids or paths into model-visible text
- added copy_ready.reference_image_instructions and rebuilt all copyable prompt variants from model-visible content
- separated reusable asset-card wording from 16:9 video reference-frame wording
- added line-control, mask, and post-composite rules for all exact text, symbol, emblem, register, and overlay cases

## Scores By Type

| Type | Count | Average | Minimum | All 100 |
| --- | ---: | ---: | ---: | --- |
| character | 15 | 100 | 100 | yes |
| location | 6 | 100 | 100 | yes |
| prop | 10 | 100 | 100 | yes |
| costume | 5 | 100 | 100 | yes |
| style | 3 | 100 | 100 | yes |
| reference_frame | 44 | 100 | 100 | yes |

## Prompt Scores

| Prompt | Asset | Type | Reference Inputs | Score | Status |
| --- | --- | --- | ---: | ---: | --- |
| PROMPT_E01_C001 | E01_C001 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C002 | E01_C002 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C004 | E01_C004 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C005 | E01_C005 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C006 | E01_C006 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C007 | E01_C007 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C011 | E01_C011 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C016A | E01_C016A | character | 2 | 100 | pass_100 |
| PROMPT_E01_C016B | E01_C016B | character | 2 | 100 | pass_100 |
| PROMPT_E01_C017 | E01_C017 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C018 | E01_C018 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C020 | E01_C020 | character | 2 | 100 | pass_100 |
| PROMPT_E01_C022 | E01_C022 | character | 1 | 100 | pass_100 |
| PROMPT_E01_C023 | E01_C023 | character | 1 | 100 | pass_100 |
| PROMPT_E01_C024 | E01_C024 | character | 1 | 100 | pass_100 |
| PROMPT_E01_L007 | E01_L007 | location | 3 | 100 | pass_100 |
| PROMPT_E01_L003 | E01_L003 | location | 3 | 100 | pass_100 |
| PROMPT_E01_L014 | E01_L014 | location | 3 | 100 | pass_100 |
| PROMPT_E01_L001A | E01_L001A | location | 3 | 100 | pass_100 |
| PROMPT_E01_L001B | E01_L001B | location | 3 | 100 | pass_100 |
| PROMPT_E01_L001C | E01_L001C | location | 3 | 100 | pass_100 |
| PROMPT_E01_P016 | E01_P016 | prop | 1 | 100 | pass_100 |
| PROMPT_E01_P008 | E01_P008 | prop | 2 | 100 | pass_100 |
| PROMPT_E01_P009 | E01_P009 | prop | 3 | 100 | pass_100 |
| PROMPT_E01_P002 | E01_P002 | prop | 3 | 100 | pass_100 |
| PROMPT_E01_P003 | E01_P003 | prop | 3 | 100 | pass_100 |
| PROMPT_E01_P004 | E01_P004 | prop | 3 | 100 | pass_100 |
| PROMPT_E01_P017 | E01_P017 | prop | 2 | 100 | pass_100 |
| PROMPT_E01_P005 | E01_P005 | prop | 2 | 100 | pass_100 |
| PROMPT_E01_P018 | E01_P018 | prop | 2 | 100 | pass_100 |
| PROMPT_E01_P020 | E01_P020 | prop | 1 | 100 | pass_100 |
| PROMPT_E01_K001 | E01_K001 | costume | 2 | 100 | pass_100 |
| PROMPT_E01_K002 | E01_K002 | costume | 2 | 100 | pass_100 |
| PROMPT_E01_K003 | E01_K003 | costume | 2 | 100 | pass_100 |
| PROMPT_E01_K004 | E01_K004 | costume | 2 | 100 | pass_100 |
| PROMPT_E01_K006 | E01_K006 | costume | 2 | 100 | pass_100 |
| PROMPT_E01_F001 | E01_F001 | style | 1 | 100 | pass_100 |
| PROMPT_E01_F005 | E01_F005 | style | 1 | 100 | pass_100 |
| PROMPT_E01_F006 | E01_F006 | style | 1 | 100 | pass_100 |
| PROMPT_E01_R001 | E01_R001 | reference_frame | 5 | 100 | pass_100 |
| PROMPT_E01_R002 | E01_R002 | reference_frame | 5 | 100 | pass_100 |
| PROMPT_E01_R003 | E01_R003 | reference_frame | 6 | 100 | pass_100 |
| PROMPT_E01_R004 | E01_R004 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R005 | E01_R005 | reference_frame | 5 | 100 | pass_100 |
| PROMPT_E01_R006 | E01_R006 | reference_frame | 6 | 100 | pass_100 |
| PROMPT_E01_R007 | E01_R007 | reference_frame | 3 | 100 | pass_100 |
| PROMPT_E01_R008 | E01_R008 | reference_frame | 6 | 100 | pass_100 |
| PROMPT_E01_R009 | E01_R009 | reference_frame | 6 | 100 | pass_100 |
| PROMPT_E01_R010 | E01_R010 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R011 | E01_R011 | reference_frame | 6 | 100 | pass_100 |
| PROMPT_E01_R012 | E01_R012 | reference_frame | 5 | 100 | pass_100 |
| PROMPT_E01_R013 | E01_R013 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R014 | E01_R014 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R015 | E01_R015 | reference_frame | 9 | 100 | pass_100 |
| PROMPT_E01_R016 | E01_R016 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R017 | E01_R017 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R018 | E01_R018 | reference_frame | 5 | 100 | pass_100 |
| PROMPT_E01_R019 | E01_R019 | reference_frame | 5 | 100 | pass_100 |
| PROMPT_E01_R020 | E01_R020 | reference_frame | 5 | 100 | pass_100 |
| PROMPT_E01_R021 | E01_R021 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R022 | E01_R022 | reference_frame | 3 | 100 | pass_100 |
| PROMPT_E01_R023 | E01_R023 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R024 | E01_R024 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R025 | E01_R025 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E01_R026 | E01_R026 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R027 | E01_R027 | reference_frame | 3 | 100 | pass_100 |
| PROMPT_E01_R028 | E01_R028 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R029 | E01_R029 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R030 | E01_R030 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R031 | E01_R031 | reference_frame | 5 | 100 | pass_100 |
| PROMPT_E01_R032 | E01_R032 | reference_frame | 9 | 100 | pass_100 |
| PROMPT_E01_R033 | E01_R033 | reference_frame | 5 | 100 | pass_100 |
| PROMPT_E01_R034 | E01_R034 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R035 | E01_R035 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R036 | E01_R036 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R037 | E01_R037 | reference_frame | 4 | 100 | pass_100 |
| PROMPT_E01_R038 | E01_R038 | reference_frame | 7 | 100 | pass_100 |
| PROMPT_E01_R039 | E01_R039 | reference_frame | 6 | 100 | pass_100 |
| PROMPT_E01_R040 | E01_R040 | reference_frame | 6 | 100 | pass_100 |
| PROMPT_E01_O001 | E01_O001 | reference_frame | 9 | 100 | pass_100 |
| PROMPT_E01_O002 | E01_O002 | reference_frame | 9 | 100 | pass_100 |
| PROMPT_E01_O003 | E01_O003 | reference_frame | 10 | 100 | pass_100 |
| PROMPT_E01_O004 | E01_O004 | reference_frame | 9 | 100 | pass_100 |
