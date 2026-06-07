# Episode 02 Asset Prep Plan

## Summary

- Total assets: 63
- style: 0 (inherits series masters F001, F005, F006; no standalone episode style board generation)
- character: 8
- location: 1
- prop: 9
- costume: 5
- reference_frame: 40

## Inheritance Cleanup

- E02 style references now inherit `F001`, `F005`, and `F006` directly from `assets/style/`; `E02_F001`, `E02_F005`, and `E02_F006` are not generated as separate image assets.
- The five duplicate L001 scene cards were merged into `E02_L001`, a single episode scene geography lock at `02/assets/locations/l001e02.png`.
- Reference frames use the single `E02_L001` lock plus local action state, preventing repeated generation of mutually divergent residual village geography.

## Creation Order

| Order | Asset | Type | Depends On | Output |
| ---: | --- | --- | --- | --- |
| 1 | E02_C002 | character | F001, F005, C002, K002, E02_P002A, E02_P002B, E02_P001 | 02/assets/characters/c002e02.png |
| 2 | E02_C006 | character | F001, F005, C006, K006, E02_P004A | 02/assets/characters/c006e02.png |
| 3 | E02_C005 | character | F001, F005, C005, K003, E02_P005 | 02/assets/characters/c005e02.png |
| 4 | E02_C017 | character | F001, F005, C017, K004, E02_P008 | 02/assets/characters/c017e02.png |
| 5 | E02_C001 | character | F001, F005, C001, K001, E02_P001, E02_P005 | 02/assets/characters/c001e02.png |
| 6 | E02_C007 | character | F001, F005, C007, K004, E02_P003, E02_P004A | 02/assets/characters/c007e02.png |
| 7 | E02_C016 | character | F001, F005, C016, K004, E02_P003, E02_P004B | 02/assets/characters/c016e02.png |
| 8 | E02_C018 | character | F001, F005, C018, K004, E02_P004B | 02/assets/characters/c018e02.png |
| 9 | E02_L001 | location | F001, F005, L001 | 02/assets/locations/l001e02.png |
| 10 | E02_P002A | prop | F001, F005, P002, F006 | 02/assets/props/p002ae02.png |
| 11 | E02_P008 | prop | F001, F005, P008 | 02/assets/props/p008e02.png |
| 12 | E02_P003 | prop | F001, F005, P003, F006 | 02/assets/props/p003e02.png |
| 13 | E02_P004A | prop | F001, F005, P004, F006 | 02/assets/props/p004ae02.png |
| 14 | E02_P004B | prop | F001, F005, P004, F006 | 02/assets/props/p004be02.png |
| 15 | E02_P002B | prop | F001, F005, P002, F006 | 02/assets/props/p002be02.png |
| 16 | E02_P004C | prop | F001, F005, P004, F006 | 02/assets/props/p004ce02.png |
| 17 | E02_P005 | prop | F001, F005, P005 | 02/assets/props/p005e02.png |
| 18 | E02_P001 | prop | F001, F005, P001, F006 | 02/assets/props/p001e02.png |
| 19 | E02_K001 | costume | F001, F005, K001 | 02/assets/costumes/k001e02.png |
| 20 | E02_K002 | costume | F001, F005, K002 | 02/assets/costumes/k002e02.png |
| 21 | E02_K003 | costume | F001, F005, K003 | 02/assets/costumes/k003e02.png |
| 22 | E02_K004 | costume | F001, F005, K004 | 02/assets/costumes/k004e02.png |
| 23 | E02_K006 | costume | F001, F005, K006 | 02/assets/costumes/k006e02.png |
| 24 | E02_R001 | reference_frame | F001, F005, F006, E02_L001, E02_C002, E02_C006, E02_C005, E02_C017, E02_P002A, E02_P008 | 02/assets/reference-frames/r001e02.png |
| 25 | E02_R002 | reference_frame | F001, F005, F006, E02_L001, E02_C002, E02_C006, E02_C005, E02_C017, E02_P002A, E02_P008 | 02/assets/reference-frames/r002e02.png |
| 26 | E02_R003 | reference_frame | F001, F005, F006, E02_L001, E02_C002, E02_C006, E02_C005, E02_C017, E02_P002A, E02_P008 | 02/assets/reference-frames/r003e02.png |
| 27 | E02_R004 | reference_frame | F001, F005, F006, E02_L001, E02_C002, E02_C006, E02_C005, E02_C017, E02_P002A, E02_P008 | 02/assets/reference-frames/r004e02.png |
| 28 | E02_R005 | reference_frame | F001, F005, F006, E02_L001, E02_C002, E02_C006, E02_C005, E02_C017, E02_P002A, E02_P008 | 02/assets/reference-frames/r005e02.png |
| 29 | E02_R006 | reference_frame | F001, F005, F006, E02_L001, E02_C002, E02_C006, E02_C005, E02_C017, E02_P002A, E02_P008 | 02/assets/reference-frames/r006e02.png |
| 30 | E02_R007 | reference_frame | F001, F005, F006, E02_L001, E02_C002, E02_C006, E02_C005, E02_C017, E02_P002A, E02_P008 | 02/assets/reference-frames/r007e02.png |
| 31 | E02_R008 | reference_frame | F001, F005, F006, E02_L001, E02_C002, E02_C006, E02_C005, E02_C017, E02_P002A, E02_P008 | 02/assets/reference-frames/r008e02.png |
| 32 | E02_R009 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C005, E02_C007, E02_C016, E02_C017, E02_C018, E02_P003, E02_P004A, E02_P008, E02_P004B | 02/assets/reference-frames/r009e02.png |
| 33 | E02_R010 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C005, E02_C007, E02_C016, E02_C017, E02_C018, E02_P003, E02_P004A, E02_P008, E02_P004B | 02/assets/reference-frames/r010e02.png |
| 34 | E02_R011 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C005, E02_C007, E02_C016, E02_C017, E02_C018, E02_P003, E02_P004A, E02_P008, E02_P004B | 02/assets/reference-frames/r011e02.png |
| 35 | E02_R012 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C005, E02_C007, E02_C016, E02_C017, E02_C018, E02_P003, E02_P004A, E02_P008, E02_P004B | 02/assets/reference-frames/r012e02.png |
| 36 | E02_R013 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C005, E02_C007, E02_C016, E02_C017, E02_C018, E02_P003, E02_P004A, E02_P008, E02_P004B | 02/assets/reference-frames/r013e02.png |
| 37 | E02_R014 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C005, E02_C007, E02_C016, E02_C017, E02_C018, E02_P003, E02_P004A, E02_P008, E02_P004B | 02/assets/reference-frames/r014e02.png |
| 38 | E02_R015 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C005, E02_C007, E02_C016, E02_C017, E02_C018, E02_P003, E02_P004A, E02_P008, E02_P004B | 02/assets/reference-frames/r015e02.png |
| 39 | E02_R016 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C005, E02_C007, E02_C016, E02_C017, E02_C018, E02_P003, E02_P004A, E02_P008, E02_P004B | 02/assets/reference-frames/r016e02.png |
| 40 | E02_R017 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_P002B | 02/assets/reference-frames/r017e02.png |
| 41 | E02_R018 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_P002B | 02/assets/reference-frames/r018e02.png |
| 42 | E02_R019 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_P002B | 02/assets/reference-frames/r019e02.png |
| 43 | E02_R020 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_P002B | 02/assets/reference-frames/r020e02.png |
| 44 | E02_R021 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_P002B | 02/assets/reference-frames/r021e02.png |
| 45 | E02_R022 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_P002B | 02/assets/reference-frames/r022e02.png |
| 46 | E02_R023 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_P002B | 02/assets/reference-frames/r023e02.png |
| 47 | E02_R024 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_P002B | 02/assets/reference-frames/r024e02.png |
| 48 | E02_R025 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C005, E02_P003, E02_P008, E02_P005 | 02/assets/reference-frames/r025e02.png |
| 49 | E02_R026 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C005, E02_P003, E02_P008, E02_P005 | 02/assets/reference-frames/r026e02.png |
| 50 | E02_R027 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C005, E02_P003, E02_P008, E02_P005 | 02/assets/reference-frames/r027e02.png |
| 51 | E02_R028 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C005, E02_P003, E02_P008, E02_P005 | 02/assets/reference-frames/r028e02.png |
| 52 | E02_R029 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C005, E02_P003, E02_P008, E02_P005 | 02/assets/reference-frames/r029e02.png |
| 53 | E02_R030 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C005, E02_P003, E02_P008, E02_P005 | 02/assets/reference-frames/r030e02.png |
| 54 | E02_R031 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C005, E02_P003, E02_P008, E02_P005 | 02/assets/reference-frames/r031e02.png |
| 55 | E02_R032 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C005, E02_P003, E02_P008, E02_P005 | 02/assets/reference-frames/r032e02.png |
| 56 | E02_R033 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C007, E02_P002A, E02_P002B, E02_P001, E02_P003, E02_P008 | 02/assets/reference-frames/r033e02.png |
| 57 | E02_R034 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C007, E02_P002A, E02_P002B, E02_P001, E02_P003, E02_P008 | 02/assets/reference-frames/r034e02.png |
| 58 | E02_R035 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C007, E02_P002A, E02_P002B, E02_P001, E02_P003, E02_P008 | 02/assets/reference-frames/r035e02.png |
| 59 | E02_R036 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C007, E02_P002A, E02_P002B, E02_P001, E02_P003, E02_P008 | 02/assets/reference-frames/r036e02.png |
| 60 | E02_R037 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C007, E02_P002A, E02_P002B, E02_P001, E02_P003, E02_P008 | 02/assets/reference-frames/r037e02.png |
| 61 | E02_R038 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C007, E02_P002A, E02_P002B, E02_P001, E02_P003, E02_P008 | 02/assets/reference-frames/r038e02.png |
| 62 | E02_R039 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C007, E02_P002A, E02_P002B, E02_P001, E02_P003, E02_P008 | 02/assets/reference-frames/r039e02.png |
| 63 | E02_R040 | reference_frame | F001, F005, F006, E02_L001, E02_C001, E02_C002, E02_C006, E02_C007, E02_P002A, E02_P002B, E02_P001, E02_P003, E02_P008 | 02/assets/reference-frames/r040e02.png |
