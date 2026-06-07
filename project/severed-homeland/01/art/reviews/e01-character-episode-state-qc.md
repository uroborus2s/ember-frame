# E01 Character Episode State QC

Date: 2026-06-07
Batch: B01_E01_CHARACTERS
Scope: episode 01 character state assets in `01/assets/characters/`

## Relationship Locks Confirmed

- Shen family core: Shen Weisang, Shen Zhaomian, and Luo Qinghe must read as son, younger sister, and mother. Luo Qinghe protects by stable hands and blocking positions; Shen Weisang reads exits before acting; Shen Zhaomian remains a village child.
- Yan Nanzhi is the concealed escort target. Episode 01 must keep her hidden and pressured by relics, not reveal full ceremonial identity.
- Gu Huaizhang is Yan Nanzhi's southern mentor and political pressure source, not a pure saint.
- Bai Yi is the Qingming institutional pursuer and mirror-opponent to Shen Weisang. Bai Yi, low-level book officials, grain-tax clerks, mixed-blood slave soldiers, and pure insect soldiers must be immediately distinguishable by species, costume, body scale, tool, and job.
- Crowd cards must preserve regional and class differences. Canyangao villagers are hunters, medicine households, mountain people, and post-road descendants; Jinhe family cards must retain grain-belt labor structure.

## Current File State

The 15 canonical PNGs exist under `project/severed-homeland/01/assets/characters/`, but checksum comparison shows they are identical to the latest copied `history/` candidates. They should be treated as first-round candidates copied into canonical for parent QC, not approved final assets.

## Must Redo

| Asset | File | QC Result | Reason |
| --- | --- | --- | --- |
| E01_C001 Shen Weisang | `c001e01.png` | FAIL | Identity drift. Current image uses high messy topknot, ragged gray cloth, and heavy dirt. Master requires short messy black hair, warm brown practical hunter clothes, cleaner youth silhouette, and exit-reading behavior. |
| E01_C002 Yan Nanzhi | `c002e01.png` | FAIL | Identity drift. Current image reads as rough black-cloaked refugee with masculinized shoulders. Master requires pale classical oval female face, concealed royal bearing, mist-purple/cool-gray outer layers, and deep ink-blue inner layer. |
| E01_C006 Luo Qinghe | `c006e01.png` | FAIL | Identity drift. Current image reads as an ordinary tired older villager. Master requires a 37-year-old doctor-mother whose rough cloth cannot hide quiet beauty, and whose eyes/facial structure visibly connect to both Shen children. |
| E01_C007 Bai Yi | `c007e01.png` | FAIL | Species and tier drift. Current image is a human white-robed long-haired official. Master requires upper Qingming insectoid form: nonhuman head, compound eyes, insect-wax high crown, clean cold-white hierarchy, and transparent wing presence. |
| E01_C016A White Book Official | `c016e01.png` | FAIL | Species drift. Current image is a human white-clothed official. Must use low-level insect-clerk template: insect face, compound eyes, cheek shell, mouthpart jawline, no human hair, high account-clerk hat or insect-wax crown, white book board, and wax seal tools. |
| E01_C016B Grain-Tax Clerk | `c016be01.png` | FAIL | Species and role drift. Current image is another human white-clothed official and is not distinct from C016A. Must remain a low-level insect clerk but show grain-tax function through grain tags, bone abacus, grain-storage inspection tools, and tax posture. |
| E01_C017 Mixed-Blood Slave Soldier | `c017e01.png` | FAIL | Hierarchy drift. Current image reads as ordinary human gray guard. Must retain human upright outline plus shaved/insectified scalp, wax patches, small armor plates, black-sun slave marks, ID tags, scent tags, low rat-tail/money-tail braid, and wrist-seizing/cart-escorting duty. |

## Pending Rework

| Asset | File | QC Result | Reason |
| --- | --- | --- | --- |
| E01_C004 Xue Linqiang | `c004e01.png` | PENDING_REWORK | Role is readable, but he is over-aged, too white-haired, too bulky, and too snow-gray. Master is a frost-injured former wall soldier with hard restraint, not a generic snowfield elder. |
| E01_C005 Shen Zhaomian | `c005e01.png` | PENDING_REWORK | Child scale, herb bag, and suspected-child state work. Gray-brown raggedness is too heavy and should be reduced before final approval. |
| E01_C011 Gu Huaizhang | `c011e01.png` | PENDING_REWORK | Mentor role, scroll, and pressure relationship work. Compared with master, old-official gold trim and old-court visual authority are weakened. |

## Usable Pending Parent QC

| Asset | File | QC Result | Notes |
| --- | --- | --- | --- |
| E01_C018 Pure Insect Soldier | `c018e01.png` | USABLE_PENDING_QC | Pure insect body, reverse-joint legs, sealing role, and scale contrast are readable. |
| E01_C020 Northern Siege Silhouette | `c020e01.png` | USABLE_PENDING_QC | Siege pressure, war-beast scale, and northern threat read clearly. |
| E01_C023 Jinhe Requisitioned Family | `c023e01.png` | USABLE_PENDING_QC | Family structure, elderly/children, cart, grain pressure, and winter food anxiety are readable; color remains somewhat earth-monotone. |
| E01_C024A Young Gray-Wall Military Household | `c024ae01.png` | USABLE_PENDING_QC | Young soldier state, broken spear/wall pressure, and wounded-hand details are readable; palette is still gray-heavy. |
| E01_C027 Canyangao Villagers | `c027e01.png` | USABLE_PENDING_QC | Group shows hunters, medicine-household and village age differences; still needs caution against over-unified gray raggedness. |

## Follow-Up Sent To Image Thread

The image-generation thread has been instructed not to reuse the failed copied candidates, and to regenerate:

- First priority: E01_C001, E01_C002, E01_C006, E01_C007.
- Additional hard failures: E01_C016A, E01_C016B, E01_C017.

The pending rework items can remain for the next pass unless the project requires all canonical files to be final-approved in one batch.

## Rework Thread Observations

- E01_C001 temporary rework image was generated in the child thread image cache and reviewed by parent. Direction is acceptable: short messy black hair, warm brown hunter clothes, practical bow and travel kit, and youth silhouette are back on model. It has not yet been written to canonical at the time of this report.
- E01_C002 temporary rework image fixed the major gender, costume, and concealed-royal-state drift, but still fails delivery constraints because it includes readable English title text and a `168cm` label. Parent sent an immediate correction requiring a no-text redraw before canonical write.
