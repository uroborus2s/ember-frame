# SC002 Same-Ground Height Scale Redo QC Report

Date: 2026-06-11
Scope: `E01_R005`-`E01_R009`, plus `E01_C017` supporting character-state card.
Status: superseded by user visual QC rejection. Do not start final video production, ComfyUI binding, or prompt refresh from this candidate set. Current effective audit: `01/art/audits/sc002-character-identity-height-scale-user-rejection-2026-06-11.md`.

## Repair Targets

- C016B must inherit the global C016 insect official: bone-white face shell, dark compound eyes, thin feelers, wax-white tall accountant hat, white robe, 190-210cm body scale.
- C017 must remain a mixed slave soldier: humanoid skeleton, five hardened fingers, no pure-insect claws, one very thin low money-tail braid at the back.
- C018 must remain a pure insect soldier: 200-230cm, visibly taller than humans and slave soldiers, armed with spear or hook-sickle, route-blocking only.
- Height pressure must be shown on the same ground plane. No table, platform, stairs, grain sacks, or other height-boosting object may create the scale difference.

## Canonical Outputs

| Asset | Canonical file | Source history | QC status |
| --- | --- | --- | --- |
| `E01_R005` | `01/assets/reference-frames/r005e01.png` | `01/assets/reference-frames/history/r005e01.same-ground-height-source-20260611.png` | candidate pass, pending user visual QC |
| `E01_R006` | `01/assets/reference-frames/r006e01.png` | `01/assets/reference-frames/history/r006e01.same-ground-height-source-20260611.png` | candidate pass, pending user visual QC |
| `E01_R007` | `01/assets/reference-frames/r007e01.png` | `01/assets/reference-frames/history/r007e01.same-ground-c016-white-hat-source-20260611.png` | candidate pass with minor text risk, pending user visual QC |
| `E01_R008` | `01/assets/reference-frames/r008e01.png` | `01/assets/reference-frames/history/r008e01.same-ground-height-source-20260611.png` | candidate pass, pending user visual QC |
| `E01_R009` | `01/assets/reference-frames/r009e01.png` | `01/assets/reference-frames/history/r009e01.same-ground-height-source-20260611.png` | candidate pass, pending user visual QC |

All five canonical files are 3840x2160 PNG, no alpha.

## Human QC Notes

- `R005`: C016 reads as the global insect official with white accountant hat and bone-white shell; C018 is taller and armed; villagers remain lower on the same muddy lane.
- `R006`: C017 grips the adult arm/sleeve area instead of ankle; the hand reads as five hardened fingers; C018 remains armed in the same-ground background.
- `R007`: C016 was regenerated after a rejected black-hat candidate. Current canonical restores white wax hat, insect face shell, C017 upper-arm grip, and armed C018 background pressure. Residual risk: one environment cloth sign contains readable Chinese and should not be inherited into final video text layers.
- `R008`: FLF2V first frame preserves the household threshold, loaded grain, C017 action, and armed C018 route pressure.
- `R009`: FLF2V last frame preserves empty threshold, ancestral box, handprint, wheel ruts, and distant route-blocking pressure.

## Decision

The SC002 still-image asset package is internally acceptable as a candidate handoff after the same-ground height-scale redo. It is not final-approved. The next required gate is user visual QC on `r005e01.png` through `r009e01.png`.
