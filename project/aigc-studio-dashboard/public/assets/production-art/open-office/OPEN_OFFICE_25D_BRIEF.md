# Open Office 2.5D Production Brief

## Direction

Retire the current multi-room office image as a production gameplay scene. Keep it only as a style reference.

Build a new single-room open office level for 2.5D web gameplay:

- One large open office room, fixed isometric 2.5D camera.
- Target image size: 1536x900.
- Warm premium AIGC studio style: wood desks, grey stone floor, sunlit windows, plants, wall art, soft shadows, monitor glow.
- No internal wall maze, no glass corridors through the middle, no tall foreground partition blocking the main route.
- Decorations live on the perimeter and on desks: plants, windows, shelves, paintings, cabinets, screens.
- Desk rows are single-sided: chairs only on one side of each row, not both sides.
- A separate control desk is required for the main controller role.

## Gameplay Layout

The scene must be designed for navigation first:

- A clear main aisle from lower/front entrance to upper/back office area.
- At least one clear horizontal cross aisle between desk rows.
- 3 or 4 long single-sided workstation rows.
- 20 seated work positions in v002: four single-sided rows, five seats per row.
- Moving characters stay mostly in aisles and open floor.
- Fixed seated staff are baked into the fixed-staff scene plate, not patched as floating DOM overlays.
- Interactive seat/stand can be added later only for selected seats with dedicated anchored sprite frames and local occluders.
- The main controller role starts at the separate control desk and is the only role allowed to walk to workstations to assign tasks or control process handoff.
- Two QC inspector roles continuously patrol through the aisles beside the desk rows, simulating review/checking work.
- Normal fixed staff do not move; they sit and work at their own stations.

## Layer Outputs

Required production layers:

- `open_office_empty_base_v002.png`: clean office, no people.
- `open_office_fixed_staff_v002.png`: same office with seated working staff baked into chairs.
- `open_office_foreground_occlusion_v002.png`: only foreground occluding desk lips/chair backs/plants if needed.
- `open_office_walkable_mask_v002.png`: white walkable floor, black blocked furniture/perimeter.
- `open_office_depth_map_v002.png`: grayscale depth order helper.
- `open_office_scene_v002.json`: coordinates, nav graph, collisions, triggers, seat anchors, z rules.

## Scene Rules

- Seats must face monitors correctly.
- Chair backs and desk front lips are the only regular near-character occluders.
- Single-sided desk rows must have all chairs on the aisle side, leaving a predictable clear lane behind the chairs.
- Avoid people on walls, glass, monitor screens, or desk tops unless intentionally baked into the correct chair.
- Keep walkable routes visually obvious: floor must be visible around the main aisle.
- Do not put tall plants, server racks, glass walls, or heavy shadows across the main aisle.
- People must be different silhouettes/clothes; roughly half male and half female in the fixed-staff layer.

## Empty Base Prompt

Use case: stylized-concept
Asset type: production 2.5D web game scene base
Primary request: Generate a new open-plan AIGC studio office clean plate, not an edit of the old maze-like multi-room layout, while preserving the warm high-end realistic 2.5D office style of the reference scene.
Scene/backdrop: one large open office room with perimeter windows, wall art, shelves, plants, cabinets, and subtle monitor glow.
Subject: 3 or 4 long single-sided workstation rows with chairs on only one side, monitors, keyboards, desk lamps, papers, and small office props, plus one separate command/control desk for the main controller.
Style/medium: polished realistic 2.5D isometric game background, detailed bitmap concept art.
Composition/framing: 1536x900 wide composition, fixed isometric camera, clear central aisle from lower/front entrance to upper/back office area, clear cross aisles between rows, visible patrol lanes beside the single-sided desk rows.
Lighting/mood: warm sunlight, soft shadows, premium studio atmosphere, readable floor paths.
Constraints: no people, no UI, no labels, no text, no watermark, no internal wall maze, no glass corridor crossing the main route, no large foreground wall blocking the aisle, no recording booth taking a large area, no chairs on both sides of the same desk row.
Avoid: complex multi-room partitions, double-sided bench seating, tiny closed rooms, blocked aisles, floating objects, impossible chair placement, dark blurry corners.

## Fixed Staff Prompt

Use case: precise-object-edit
Asset type: production fixed-staff 2.5D scene plate
Primary request: Add seated office workers into the existing open-office clean plate. Each person must be truly seated in a chair, facing the computer monitor at their workstation, with correct perspective, scale, shadows, and contact with the chair.
Subject: 20 different seated office workers, roughly half male and half female, different hair/clothes/silhouettes, subtle working poses with hands near keyboard/tablet/mouse. Leave the separate control desk available for the main controller role unless a dedicated seated controller plate is requested.
Constraints: preserve the office layout exactly; add people only into valid single-sided desk chairs; no standing people; no people floating on walls, glass, floor, or monitor screens; no duplicated identical figures; no UI, labels, text, or watermark.
Avoid: pasted cutout look, wrong-facing seated people, hanging on chair backs, sitting on desks, oversized heads, missing legs where visible, mismatched lighting.
