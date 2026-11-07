# Chicken Coop: ARCHIVE (outdated)

> **OUTDATED FILE. Kept only as a human archive of earlier designs (v0 / v1 / v2) and of the
> decisions that led to the current one. It is NOT a source of truth for any ongoing project:
> do not use its dimensions, quantities, specs or shopping lists for planning, building or
> buying. The current design, shopping list and status are in `chicken_coop.md`.**

Frozen files (also archival): v1: `models/chicken_coop_model.py`, `models/chicken_coop.blend`,
`models/render_views.py`, `models/renders/` (including the A-vs-B layout comparison previews
`models/renders/preview_*.png` and `models/preview_options.py`). v2: `models/chicken_coop_model_v2.py`,
`models/chicken_coop_v2.blend`, `models/render_views_v2.py`, `models/renders_v2/`.

---

## Design v2 (2026-10-01/02), superseded by v3 (hexagonal mesh)

(Archived: do not use. The current design is in `chicken_coop.md`.) Files:
`models/chicken_coop_model_v2.py` (parametric build script) → `models/chicken_coop_v2.blend`;
`models/render_views_v2.py` → `models/renders_v2/`. After any design change: edit the script,
run it, run the render script (both via `python tools/bl.py run <script>` with Blender open and
the "MCP for Blender" add-on connected, or through the `blender` MCP tools), and delete any
render that stops making sense. Don't leave stale renders around.

**Layout.** Total 4.0 × 2.0 m. The **house is the first 1.0 m, full width**: plywood walls and a
**gable roof** (ridge along the length, ~20°, 15 cm overhang on both eaves and 10 cm at the west
end, ridge at 1.94 m). The mesh run is the remaining **3.0 m (6 m² of bare grass, no floor)**;
mesh roof and east end wall belong to the run. Frame: 2"×3" pine (45×70 mm), 1.6 m tall,
galvanized welded-mesh walls/roof (~24 m² total incl. a 25 cm anti-dig skirt and the
under-house sides).

**Predator pressure:** low (fox/dog), not zero. Moderate spec: nightly pop-hole lockup is the key
defense. Mesh: galvanized welded (not rebar "sima", not chicken wire), 25×50 mm opening (25×25 if
price is close), wire 1.2–1.5 mm, roll width 1.5 m; 0.9 mm is too thin; buy-once option if a fox
ever shows up: 25×25 at 1.4 mm. Mesh on the roof too (hawks/cats), battens over mesh edges, no
gaps under the bottom rail, skirt weighted with bricks/stakes. Latches: spring
carabiners/barrel bolts (no padlocks). Ground anchors stay (wind, not predators).

**House.**
- **West end wall:** reused ~1.0×0.85 m louvered window (placeholder size; measure the real one),
  side-hinged on one edge, swings outward, 12.7 mm mesh backing optional; 2 nest boxes outside
  the wall (lid opens from outside).
- **Floor:** 18 mm plywood on 2×3 **floor joists** on edge between the front and back floor rails
  (2 end joists + 2 intermediate at x≈0.33/0.67 m), joist hangers or metal angles at the rails.
  The joists belong only to the raised house floor; the run has no floor, so the hens keep the
  grass. Rails run under the house as the chassis.
- 2 roosts (~1.8 m, round pole), litter floor; roof is plywood + chapa.
- **Pop-hole** 0.30×0.38 m on the east wall, guillotine door on cord+pulley from outside.
- **Ramp:** 1.1 m / 27° with cleats every 15 cm, hinged at the pop-hole sill, with a foot eye and
  a ~1.4 m chain on a hook under the roof cross-member at x = 2.0 m. Parked: chain unclipped,
  ramp on the ground. Travel: clip the chain to the foot eye, ramp foot 15 cm up (shut the hens
  in first). A hoisted ramp is also a second barrier on the pop-hole at night; the guillotine
  door stays the main defense.
- Feeder/waterer in a rain-covered corner (back-east, chapa cover hung from the roof frame).

**Handle (full width, copied from a video).** Two arms lapped on the two east corner posts, joined
by a 2×3-on-edge bar across the whole 2.0 m at hip height (z 0.86–0.93 m), with a diagonal brace
under each arm; M8 through-bolts, never into mesh. Lets you stand centred, lift with both hands
wide and steer by swinging the tail.

**Human door** on the front long side, x = 2.54–3.30 m (0.76 m wide × 1.45 m tall), hinged on the
x = 2.5 m post (opens outward), latch on an extra post at x = 3.3 m, lintel above. The east end is
plain mesh + a mid post. The front skirt has a gap in front of the door (modeled), or the door
snags on it.

**Materials:** see *Lista de compras v2* below (computed from the model's cut list).
Prices not yet checked.

### Reference images, v2 (`models/renders_v2/`, frozen)

| File | Shows |
|------|-------|
| `01_overview_front.png` | whole coop from the front-west: house section, gable roof, run |
| `02_overview_back.png` | from the back-east: door, handle, feed corner, ramp, house at the far end |
| `03_house_west_end.png` | west end wall: window, nest boxes, roof overhang |
| `04_window_and_nest_lid_open.png` | window swung open, nest lid lifted |
| `05_roof_from_above.png` | gable roof over the house, mesh roof over the run |
| `06_handle_east_end.png` | full-width lift handle at the east end, seen from behind |
| `07_wheel_arm_rest.png` | foot-lever wheel at rest |
| `08_wheel_arm_locked.png` | wheel arm stepped down, stop block inserted |
| `09_house_floor_structure.png` | house shell hidden: floor, roosts, posts, nest box |
| `10_ramp_parked.png` / `11_ramp_hoisted.png` | ramp down vs. hoisted by the chain |
| `12_front_door_closed.png` / `13_front_door_open.png` | human door on the front side, closed vs. swung open |

**Open:** real window measurement, skirt handling when moving (front skirt already has a
gap at the door), wheel-arm prototype, price pass, and attaching the floor joists to the
rails (joist hangers or metal angles).

## Lista de compras v2 (diseño actual, 2026-10-02)

Calculada a partir de la lista de cortes del modelo `chicken_coop_model_v2.py` (con manija de
ancho completo y puerta en el frente), con ~15 % extra por desperdicio. Cantidades aproximadas,
redondeadas hacia arriba (van a sobrar cosas). Precios sin verificar. Largos de madera: preguntar
qué largos tiene la maderera (3 m vs 4 m) y adaptar.

### Viaje 1: estructura y malla (lo mínimo para empezar)

| Ítem | Cant. | Notas |
|------|-------|-------|
| Pino 2"x3" (45x70), **impregnado/tratado** si hay | ~65 m: 17 de 4 m | Largueros (4 m), postes, travesaños, vigas del piso de la casilla, poste de la puerta y barra de la manija (2 m). Lo modelado suma ~56 m. Con tirantes de 4 m se desperdicia menos; vigas y postes salen de a 2 por tirante. Tratado porque apoya en suelo húmedo |
| Pino 2"x2" (45x45) | ~12 m: 3 de 4 m | Travesaños del techo del corral, poste central del extremo este, dintel de la puerta, riostras de la manija. Si no hay 2"x2", usar 2"x3" (pesa un poco más) |
| Pino 2"x4" (45x95) | 1 de ~2,5–3 m | Brazos de las ruedas (2 de ~1,15 m). Elegir derecho y sin nudos |
| Listones 1"x1" o 1"x2" | ~45 m (listones de la malla) + ~6 m (puerta humana del frente) | "Sándwich" de la malla: va grampeada y tapada con listón por todo el borde. Cantidad estimada, no sale del modelo |
| Malla electrosoldada galvanizada 25x50 mm, alambre 1,2–1,5 mm, rollo de 1,5 m de ancho | ~18 m de rollo (~26 m², incluye 10 % de solape) | Modelo: ~24 m² (frentes, techo y extremo este del corral, lados bajo la casilla y faldón de 25 cm). 25x25 solo si el precio es parecido. No gallinero (tejido hexagonal), no alambre de 0,9 mm |
| Tornillos para madera 4,5–5 x 70–80 mm | ~1 caja (200–300) | Armado de la estructura |
| Grampas galvanizadas 1" | ~1 kg | Primero se grampea la malla, después van los listones |
| Tornillos 3,5 x 30–40 mm | ~1 caja | Listones |
| Escuadras / ángulos metálicos con tornillos | ~16 | Uniones poste-larguero, que cargan todo el peso al levantar |
| Soportes para vigas ("joist hanger") o escuadras | ~8 | 4 vigas del piso de la casilla x 2 extremos |

### Viaje 2: casilla, manija y ruedas

| Ítem | Cant. | Notas |
|------|-------|-------|
| Terciado exterior (fenólico/marino si da el presupuesto) | 5 placas de 2,44 x 1,22: 4 de 12 mm + 1 de 18 mm | 12 mm: paredes (frente, fondo, 2 hastiales), techo a dos aguas, nidos, rampa. 18 mm: piso de la casilla (~1,8 m²; sobra buena parte). El techo también puede ir en 12 mm (el modelo usa 15 mm) |
| Chapa para techo | 2 (una de ~2,5 m para los 2 faldones de ~1,1 x 1,2 m, más una chica o retazo) | Faldones de la casilla con alero y cobertizo del comedero (~1 x 1 m) |
| Ruedas neumáticas ~30 cm con eje/buje | 2 | Verificar el diámetro del agujero para el perno del eje |
| Bulones M8 con tuerca y arandela, ~100–120 mm | ~12 | Brazos y riostras de la manija, pasantes (no tornillos para madera) |
| Bulones M10 con tuerca y arandela | ~4 | Pivotes de los brazos de rueda y eje |
| Bisagras | ~10 | Ventana (2), tapas de nidos (2), puerta humana del frente (3, es de 1,45 m), rampa (2) |
| Cierres: mosquetones con resorte o pasadores | ~5 | Sin candados |
| Anclajes al suelo (por el viento) | 4 | |
| Lámina de vinilo para piso | ~2 m² | Piso de la casilla (~1,9 x 0,95 m, cama) |
| Comedero + bebedero | 1 de cada | Cualquier tamaño para 5 gallinas |
| Roldana chica + cuerda | 1 | Puerta guillotina de la gallinera |
| Cadena liviana ~1,5 m + mosquetón + 2 armellas/ganchos | 1 | Rampa: sube con la cadena al gancho del techo para mover la estructura (cadena modelada ≈ 1,36 m) |
| Palo redondo 35–40 mm (o cabo grueso) | ~4 m | 2 posaderos de ~1,8 m |
| Malla 12,7 mm para respaldo de ventana (opcional) | ~1 m² | Conviene si las tablillas son finas |

La ventana reusada (~1,0 x 0,85 m) ya la tenés: el marco que se ve en el modelo es solo de
referencia, no hay que comprarlo.

### Extras útiles
- Preservante o aceite para madera (cortes y travesaños inferiores).
- Mechas para madera (agujeros guía, evitan rajar el pino de 45 mm) y una mecha larga para los bulones M8.
- 4 ladrillos o estacas para sostener el faldón (gratis si ya tenés).

### Si hoy solo podés comprar ALGO
Comprar el **pino 2"x3" y los tornillos**. La estructura es lo primero que se arma, no depende de ninguna decisión abierta y los sobrantes se reutilizan. La malla puede esperar a tener el marco armado y confirmadas las medidas de los vanos.

## Weight & handle (structural check, v2)

Estimated from the 3D model (pine 500 kg/m³, plywood 600, mesh ~0.75 kg/m², chapa ~4 kg/m²):
**~286 kg total** (pine 113, plywood 106, mesh 18, roofing 14, hardware 25, hens 10); balance
point x ≈ 1.32 m from the west end. Rough; wet pine runs heavier. Typical 5-hen tractors weigh
50–80 kg, so this one is a big build.
- Lift force at the handle (x ≈ 4.26 m) depends on the wheel-hub position: hub at 1.00 m →
  ~28 kgf; **hub at 1.10 m → ~20 kgf (comfortable; adopted)**, wheels carry ~267 kgf; hub at
  1.20 m → ~11 kgf. Keep the hub west of the balance point by ≥ 0.2 m or the coop tips onto
  the house end.
- Handle failure risk is the connection, not the wood: arms tie into the corner posts, never the
  mesh; M8 through-bolts with washers (not wood screws). Post-to-rail joints carry the whole
  weight when lifting: use metal angle plates or bolts there too. The 2 m bar is 2×3 on edge
  (a round pole of the same span would flex too much).
- Weight-saving options considered, **not adopted** (revisit if it feels too heavy): 9 mm
  plywood for roof and walls, 45×45 instead of 45×70 members.

## Foot-lever wheels (v2)

Idea from a video: each wheel sits on a pivoting arm; step on the arm to lower the wheel (house
end rises), slide a wood block into the gap to lock it. At rest the wheel sits flush with the
frame bottom, unloaded; no latch needed. Dimensions in the model: 30 cm pneumatic wheels, 2×4 arm
on edge (45×95) pivoting on a wheel post at x = 0.80 m, hub at x = 1.10 m (a = 0.30), foot pad
at ~1.63–1.93 m (b ≈ 0.98, lever gain ~3.3), wheel travel 6 cm, block ~14 cm tall jamming under
a ledge bolted to the post at x = 1.50.
- **Don't copy the video's geometry literally:** there the foot presses *between* pivot and
  wheel (force multiplied against you). For a ~286 kg coop that would need ~200+ kgf per foot.
  With the pedal beyond the wheel, expect ~40 kgf per foot (each wheel carries ~133 kgf).
- The arm needs real structure at the house end: a floor rail under the house edge (front/back)
  and a wheel post between it and the bottom rail; pivot bolt M10 through the post. The block
  takes ~57 kgf when locked; stop it from kicking out (screw/cord).
- Procedure: step one side, insert block, repeat the other side, then lift the handle end and
  roll. Wheels drop ~6 cm, so the skirt must be lifted or unstaked before moving.
- Unverified in real life: wood-block lock stiffness and arm bending were only checked with hand
  calcs; build a one-side prototype first.

## 3D model (Blender), v2 files

- Build script: `models/chicken_coop_model_v2.py` (parametric; dimensions are variables at the top,
  idempotent: rebuilds the `Coop_*` collections and saves `models/chicken_coop_v2.blend`).
  Renders: `models/render_views_v2.py` → `models/renders_v2/` (see the table above).
- Run: `python tools/bl.py run <script>` with Blender open and "MCP for Blender" connected
  (N-panel → Connect to Claude); or use the `blender` MCP tools in a session started after it
  was connected. Setup notes are in memory (`blender_workflow`).
- Openable parts (select the empties, rotate in the viewport):
  `window_hinge`: vertical edge, Z positive = swings out.
  `nest_lid_hinge`: wall edge, Y positive = lid lifts.
  `door_hinge`: human door, Z negative = swings out.
  `ramp_hinge`: Y toward ~18.6° = ramp hoisted (swap `chain_hanging` for `chain_taut`), 27° = parked;
  or set `RAMP_LIFTED = True` and rebuild.
  `wheel_arm_hinge_front/back`: pivot, Y positive (~11.5°) = wheel down. `stop_block_*` are
  separate objects (parked on the ledge); or set `WHEEL_LOCKED = True` and rebuild.
- Collections to hide parts: `Coop_House_Shell` (walls/roof, to see roosts, litter and joists),
  `Coop_Mesh`, `Coop_Frame`, `Coop_Extras`.
- Schematic only: mesh drawn at a 5 cm pitch (real is 25×50 mm), window is a placeholder size,
  and the wheel drop is not reflected in the ground contact (frame is not raised in the render).

---

## Original framing (2026-09-11, v0)

Small hobby flock project — not a production operation. Target: ~8–12 laying
hens (eggs only, no meat plan), housed in a coop + run footprint of roughly
4×6 m. Location: Loma Verde, Escobar. Still comparing coop models/designs
online as of 2026-09-11.

**Space.** For 8–12 hens, rule-of-thumb space budgets:
- Enclosed coop (sleeping/nesting, night lockup): ~0.3–0.4 m² per bird →
  roughly 3–5 m² of *indoor* coop is enough. That leaves most of the 4×6 m
  (24 m²) footprint as run.
- Run (daytime outdoor space, if not free-ranging): ~1–2 m² per bird if
  they're run-confined most of the day; less matters if they free-range
  part of the day within a fenced perimeter.
- With a 24 m² total footprint this comfortably covers 8–12 hens even on
  the more generous end of these ratios.

---

## What changed from v1 to v2 (2026-10-01 / 02)

**What changed vs v1 (option "A", chosen after a side-by-side comparison with a narrow
house sticking out of the end, option "B"):**
- Total stays 4.0 × 2.0 m. The **house is the first 1.0 m, full width**, with its own plywood
  walls and a **gable roof** (ridge along the length, ~20°, overhang 15 cm on both eaves and 10 cm
  at the west end; ridge at 1.94 m). The mesh run is the remaining **3.0 m (6 m² of bare grass)**;
  the mesh roof and end wall now start at the house. This also fixes v1's rain-down-the-window
  problem (real overhang). Mesh needed drops to ~24 m² (v1: ~28).
- **Window and nest boxes are on the west end wall:** reused ~1.0×0.85 m louvered window,
  side-hinged on one edge, swings outward; 2 nest boxes outside (lid from outside) beside it.
- **House floor:** plywood (18 mm) on **floor joists**: 2×3 on edge between the front and back floor
  rails (2 end joists + 2 intermediate at x≈0.33/0.67 m). The joists belong only to the raised
  house floor; the run has no floor, so the hens keep the grass. Rails run under the house
  as the chassis, so v1's separate house legs, bearing blocks and fold-up leg are no longer needed.
- **Handle: full width (copied from a video, 2026-10-02).** Two arms lapped on the two east
  corner posts, joined by a 2×3-on-edge bar across the whole 2.0 m, hip height (z 0.86–0.93 m),
  with a diagonal brace under each arm; M8 through-bolts, never into mesh. Lets you stand centred,
  lift with both hands wide and steer by swinging the tail. Lift force unchanged (~20 kgf).
- **Human door on the front long side (2026-10-02),** x = 2.54–3.30 m, 0.76 m wide × 1.45 m
  tall, hinged on the x = 2.5 m post (opens outward), latch on a new post at x = 3.3 m, lintel
  above. The east end is now plain mesh + a mid post. Leave a gap in the front skirt in
  front of the door (modeled), or the door snags on it.
- Ramp (hinged at the pop-hole sill) and the chain/hook hoist carry over from v1; hook under
  the roof cross-member at x = 2.0 m, chain ≈ 1.36 m.
- **Wheels moved:** arm pivot x = 0.80, hub x = 1.10 (v1: 0.90 / 1.20); stop ledge moved to the
  post at x = 1.50. Foot pad ≈ 1.63–1.93 m. Foot force per step ≈ 40 kgf, same as v1.
- **Weight (from the model, same densities as v1): ≈ 286 kg** (v1: 245). Pine 113, plywood 106,
  mesh 18, roofing 14, hardware 25, hens 10 → bigger plywood house. Center of gravity x ≈ 1.33 m
  from the west end. With the hub at 1.10 m: **handle lift ≈ 20 kgf**, wheels carry ≈ 267 kgf
  (both). Keep the hub west of the CG by ≥ 0.2 m or the coop tips onto the house end.
  Weight-saving options (not adopted): 9 mm plywood roof/walls, 45×45 members.

---

## Design v1 (2026-10-01) — superseded by v2, kept for history

Supersedes the 2026-09-29 v0 draft (and the earlier 8–12 hen / 4×6 m fixed framing). A 3D model
of this design exists (`models/renders/`).

### Reference images (latest 3D renders — view these first)

All in `models/renders/` (rendered from `models/chicken_coop.blend`; mesh is schematic, see
the 3D model section):

| File | Shows |
|------|-------|
| `01_overview_front.png` | whole coop from the front (window side), house + wheel arm + ramp |
| `02_overview_back.png` | whole coop from the back/east: door, handle, feed corner, ramp |
| `03_house_front_close.png` | house front: louvered window, nest boxes, wheel arm |
| `04_window_and_nest_lid_open.png` | window swung open (side hinge), nest lid lifted |
| `05_roof_from_above.png` | house roof inside the frame, mesh roof over everything |
| `06_handle_east_end.png` | lift handle: posts, arms, braces, bar |
| `07_wheel_arm_rest.png` | foot-lever wheel at rest (wheel flush with frame bottom) |
| `08_wheel_arm_locked.png` | wheel arm stepped down, stop block inserted |
| `09_house_legs_parked.png` | house legs seen from the back-east: bearing blocks, leg 3 down on its pad |
| `10_house_legs_stowed.png` | same view, leg 3 folded flat under the floor (travel pose) |
| `11_ramp_parked.png` | ramp on the ground, chain hanging free from the roof hook |
| `12_ramp_hoisted.png` | ramp hoisted (foot 15 cm up), chain taut to the roof hook |

**Keeping them current:** after any design change, edit `models/chicken_coop_model.py`, run it,
then run `models/render_views.py` (both via `python tools/bl.py run <script>` with Blender open
and the "MCP for Blender" add-on connected, or through the `blender` MCP tools). Files keep fixed
names so they get overwritten; if a view stops making sense, delete it and remove it from this
table and from `VIEWS` in `render_views.py`. Don't leave stale renders around.

### Concept

2.0×4.0 m × 1.6 m tall frame of 2"×3" pine (45×70 mm), galvanized welded-mesh walls and roof
(mesh roof covers the whole 2×4 m, including over the house), raised house (1.5×1.2 m, floor at
0.5 m) at the west end, ramp to the ground, foot-lever wheels on the house end and a lift
handle on the east end (light end). Estimated ~245 kg total.

**Top view (2.0 × 4.0 m):**

```
                       4.0 m
       ├────────────────────────────────────────┤
       ┌────────────────────────────────────────┐  BACK (mesh)
       │                                  ▒▒▒▒▒▒│ ─┐
       │                                  ▒feed▒│  │
       │        RUN  (bare ground,        ▒water▒│  │ 2.0 m
       │        mesh walls + mesh roof)   ▒▒▒▒▒▒ D  │  ▒ = rain-cover (chapa)
       │  ┌──────────────┐                       │  │  D = human door, 0.7 m
  NB ┌─┤  │    HOUSE     │ ramp               ═══╡  │  ═ = lift handle (east end)
  NB │ │  │  1.5 × 1.2   │╲═════╗                │  │
     └─┤  │ (raised 0.5) │      ╚═ (to ground)   │  │
       └──┴──────────────┴───────────────────────┘ ─┘
      ◎ wheel arms (x≈0.9–1.95 m)  FRONT: window (side-hinged) faces out

  NB = 2 nest boxes on the west end wall, outside the mesh, lids open from outside
```

**Side view:**

```
        NB    HOUSE (window on the front face)
      ┌────┐┌───────────┐  ← shed roof (5°), top ≈ 1.6 m
      │eggs││ roost ×2  ├╲
      └────┘│  litter   │ ╲ ramp (~1.1 m, 27°, cleats)
   ─────────┴───────────┴──╲──────────────────  ← mesh roof over the run
      0.5 m clear   ◎       ╲      feeder/waterer
   ──────────  wheel arm     ╲___ ground
                       skirt ═══► 20–25 cm mesh apron folded outward
```

**Predator pressure:** low (fox/dog), but not zero. Moderate spec: nightly
pop-hole lockup is the key defense; everything else is proportionate.

**Mesh spec:** galvanized welded (not rebar "sima", not chicken wire), 25×50 mm
opening (25×25 if price is close), wire 1.2–1.5 mm, roll width 1.5 m. 0.9 mm
is too thin. Buy-once option if a fox ever shows up: 25×25 at 1.4 mm.
~20 m of roll (~30 m²) incl. roof and a 20–25 cm outward skirt (weighted with
bricks/stakes). Mesh on roof (hawks/cats), battens over mesh edges, no gaps
under bottom rail. Window 12.7 mm backing optional (keep if slats are thin).
Latches: spring carabiners/barrel bolts (no padlocks). Ground anchors stay
(wind, not predators).

**House (as modeled):**
- Reused ~1×1 m louvered window as the front wall (modeled 1.0×0.85 m placeholder), now
  **side-hinged on the west edge** (opens like a door, swings outward), 12.7 mm mesh backing
  inside, latch.
- Walls 12 mm plywood; shed roof (plywood + chapa) fits *inside* the frame with no overhang —
  an overhang clipped the posts/rails. Consequence: rain runs down the window face; consider a
  drip lip or small front gutter.
- 2 nest boxes on the west end wall, outside the mesh, one lid hinged at the wall edge (lifts
  outward). 2 roosts (2×1.1 m), litter floor.
- Pop-hole 0.30×0.38 m on the east wall, guillotine door on cord+pulley from outside, ramp
  1.1 m / 27° with cleats every 15 cm.
- **Ramp (hinged, 2026-10-01):** hinged at the pop-hole sill; foot eye + chain (~1.4 m) hanging
  from a hook under the roof cross-member at x=2.75. Parked: chain unclipped, ramp on the
  ground. Travel: clip the chain to the foot eye, ramp foot 15 cm up. Shut the hens in first.
  Secondary benefit: a hoisted ramp is a second barrier on the pop-hole at night (the guillotine
  door stays the main defense).
- **House supports (2026-10-01):** legs 0–2 (west-front, east-front, west-back) are bolted to the
  inside face of a bottom rail and stand on a **bearing block** (2×3 laid flat, 45 mm thick,
  2 leg-widths = 14 cm long) lying along that rail on the ground, so the parked weight goes
  block → ground, not into the bolts. **Leg 3** (back-east, touches no rail) is a fold-up prop:
  pivot bolt between two cheek plates under the floor, 16×16 cm plywood foot pad; lowered when
  parked, folded west flat against the floor when moving (needs a strap/pin to hold it up).
  Legs 0–2 carry load through their bolts to the rails while rolling. Not modeled yet: floor
  joists. The 18 mm plywood floor currently has no framing under the back half of the house.
- Human door: east end, 0.7 m wide (y 0.3–1.0 m), 1.3 m tall — default; the lift-up roof
  panel alternative is still open.
- Feeder/waterer in a rain-covered corner (back-east, chapa cover hung from the roof frame).

**Materials (approx):** ~100 m pine 2"×3" (frame, handle and wheel posts, floor rails),
~2.5 m of 2"×4" for the two wheel arms, ~40 m 1"×1" battens (mesh sandwich), 4 sheets 9–12 mm
exterior plywood, ~3 roofing sheets, 2 pneumatic ~30 cm wheels with stub-axle bolts, M8/M10
through-bolts with washers (handle, pivots, ledges), metal angle plates, 4 ground anchors
(wind), ~10 hinges, ~5 carabiner/bolt latches, vinyl floor sheet, feeder/waterer.
Prices not yet checked.

**Still open:** real window measurement, human access (end door vs. lift-up roof panel),
placement (grass vs. bare soil), roof drip solution, how to handle the skirt when moving, wheel
arm prototype. Next session: Mercado Libre price pass on mesh, wood, plywood, wheels.

---

## Lista de compras v1 (original 2026-10-01, conservada tal cual)

Cantidades aproximadas, redondeadas hacia arriba (van a sobrar cosas). Precios sin verificar.
Largos de madera: preguntar qué largos tiene la maderera (3 m vs 4 m) y adaptar.
Corresponde al diseño v1 (casilla de 1,5 x 1,2 m dentro del marco de 2 x 4 m). **Reemplazada por
la lista v2 de `chicken_coop.md`**; se guarda solo como referencia histórica.

### Viaje 1: estructura y malla (lo mínimo para empezar)

| Ítem | Cant. | Notas |
|------|-------|-------|
| Pino 2"x3" (45x70), **impregnado/tratado** si hay | ~100 m en total (ej. 25 de 4 m o 34 de 3 m) | Estructura, postes, manija, travesaños de piso. Los largueros miden 4,0 m: con tirantes de 4 m+ se desperdicia menos. Tratado porque apoya en suelo húmedo |
| Pino 2"x4" (45x95) | ~3 m (dos de 1,5 m o uno de 3 m) | Brazos de las ruedas. Elegir derechos y sin nudos |
| Pino 1"x1" (listones) | ~40 m | "Sándwich" de la malla (malla entre estructura y listón) |
| Malla electrosoldada galvanizada 25x50 mm, alambre 1,2–1,5 mm, rollo de 1,5 m de ancho | ~20 m de rollo (~30 m²) | Paredes, techo y faldón. 25x25 solo si el precio es parecido. No gallinero (tejido hexagonal), no alambre de 0,9 mm |
| Tornillos para madera 4,5–5 x 70–80 mm | ~1 caja (200–300) | Armado de la estructura |
| Grampas galvanizadas 1" | ~1 kg | Primero se grampea la malla, después van los listones |
| Tornillos 3,5 x 30–40 mm | ~1 caja | Listones |
| Escuadras / ángulos metálicos con tornillos | ~16 | Uniones poste-larguero, que cargan todo el peso al levantar |

### Viaje 2: casilla, manija y ruedas

| Ítem | Cant. | Notas |
|------|-------|-------|
| Placa de terciado exterior 12 mm (fenólico/marino si da el presupuesto) | 4 | Paredes, piso y nidos de la casilla |
| Chapa para techo | ~3 | Techo de la casilla (dentro del marco) y cobertizo del comedero |
| Ruedas neumáticas ~30 cm con eje/buje | 2 | Verificar el diámetro del agujero para el perno del eje |
| Bulones M8 con tuerca y arandela, ~100–120 mm | ~12 | Brazos y riostras de la manija, pasantes (no tornillos para madera) |
| Bulones M10 con tuerca y arandela | ~4 | Pivotes de los brazos de rueda y eje |
| Bisagras | ~10 | Ventana, tapas de nidos, puerta, paneles |
| Cierres: mosquetones con resorte o pasadores | ~5 | Sin candados |
| Anclajes al suelo (por el viento) | 4 | |
| Lámina de vinilo para piso | ~1,5 x 1,2 m | Piso de la casilla (cama) |
| Comedero + bebedero | 1 de cada | Cualquier tamaño para 5 gallinas |
| Roldana chica + cuerda | 1 | Puerta guillotina de la gallinera |
| Cadena liviana ~1,5 m + mosquetón + 2 armellas/ganchos | 1 | Rampa: sube con la cadena al gancho del techo para mover la estructura |
| Bisagras extra (incluidas en las ~10 de arriba, sumar 2 más) | +2 | Rampa articulada en la gallinera; pata plegable (pata 3) con perno pasante M10 (sumar al conteo de M10) |
| Tacos de apoyo (pino 2"x3" tirado, ~14 cm c/u) | 3 (alcanza con ~0,5 m) | Debajo de las patas de la casilla, sobre los travesaños inferiores |
| Malla 12,7 mm para respaldo de ventana (opcional) | ~1 m² | Conviene si las tablillas son finas |

### Extras útiles
- Preservante o aceite para madera (cortes y travesaños inferiores).
- Mechas para madera (agujeros guía, evitan rajar el pino de 45 mm) y una mecha larga para los bulones M8.
- 4 ladrillos o estacas para sostener el faldón (gratis si ya tenés).

### Si hoy solo podés comprar ALGO
Comprar el **pino 2"x3" y los tornillos**. La estructura es lo primero que se arma, no depende de ninguna decisión abierta y los sobrantes se reutilizan. La malla puede esperar a tener el marco armado y confirmadas las medidas de los vanos.

---

## Structure notes as written for v1 (weight, handle, wheels, Blender model)

The numbers below belong to v1 (245 kg, two mid-wall handle posts, hub at 1.20 m, v1 file
names). Current values are in `chicken_coop.md`.

### Weight & handle (structural check, 2026-10-01)

Estimated from the 3D model (pine 500 kg/m³, plywood 600, mesh ~0.75 kg/m²): **~245 kg
total**, balance point ~1.5 m from the house end (pine ~97, plywood 80, mesh 21, roofing 12,
hardware 25, hens 10). Rough; wet pine runs heavier. Typical 5-hen tractors weigh 50–80 kg,
so this one is a big build.
- Lift force at the handle (x=4.2 m) depends on axle position: 0.8 m → ~48 kgf static
  (≈90+ with jerks: too much for one person); **1.2 m → ~22 kgf (comfortable; adopted)**.
- Handle failure risk is the connection, not the wood: arms must tie into real members, never
  the mesh. Modeled: 2 extra full-height posts in the east wall (y=1.2, 1.8), lapped arms +
  diagonal braces, M8 through-bolts with washers (not wood screws). Post-to-rail joints carry
  the whole weight when lifting: use metal angle plates or bolts there too.
- Weight-saving options considered, **not adopted** (revisit if it feels too heavy):
  45×45 rails/posts instead of 45×70 (~−30 kg), 9 mm plywood (~−20 kg → ~175 kg total),
  smaller run (2×3 m).

### Foot-lever wheels (2026-10-01, replaces the fixed axle)

Idea from a video: each wheel sits on a pivoting arm; step on the arm to lower the wheel
(house end rises), slide a wood block into the gap to lock it. At rest the wheel sits flush
with the frame bottom, unloaded; no latch needed. Dimensions in the model: 30 cm pneumatic
wheels, 2x4 arm on edge (45x95) pivoting on a wheel post at x=0.9 m, hub at x=1.2 m
(a = 0.30), foot pad at ~1.65–1.95 m (b ≈ 0.8 → lever gain ~2.7), wheel travel 6 cm,
block ~11 cm tall jamming under a ledge bolted to the post at x=1.45.
- **Don't copy the video's geometry literally:** there the foot presses *between* pivot and
  wheel (force multiplied against you). For a ~245 kg coop that would need ~200 kgf per foot.
  With the pedal beyond the wheel, expect ~40 kgf per foot (each wheel carries ~105 kgf).
- The arm needs the house end of the frame to be real structure: floor rail under the house
  edge (front/back) and a wheel post between it and the bottom rail; pivot bolt M10 through
  the post. Block takes ~55 kgf when locked; stop it from kicking out (screw/cord).
- Procedure: step one side, insert block, repeat the other side, then lift the handle end
  and roll. Wheels drop ~6 cm, so the apron/skirt must be lifted or unstaked before moving.
- Unverified in real life: wood-block lock stiffness and arm bending were only checked with
  hand calcs; build a one-side prototype first.

### 3D model (Blender), v1 files

- Build script: `models/chicken_coop_model.py` (parametric; dimensions are variables at the
  top, idempotent: rebuilds the `Coop_*` collections). Saved scene: `models/chicken_coop.blend`.
  Renders: `models/render_views.py` → `models/renders/` (see Reference images above).
- Run: `python tools/bl.py run <script>` with Blender open and "MCP for Blender" connected
  (N-panel → Connect to Claude); or use the `blender` MCP tools in a session started after it
  was connected. Setup notes are in memory (`blender_workflow`).
- Openable parts (select the empties, rotate in the viewport):
  `window_hinge` — vertical west edge; Z negative = swings out (`WIN_HINGE_SIDE` flips the side).
  `nest_lid_hinge` — wall edge; Y positive = lid lifts.
  `wheel_arm_hinge_front/back` — pivot; Y positive (~11.5°) = wheel down. `stop_block_*` are
  separate objects (parked on the ledge); or set `WHEEL_LOCKED = True` and rebuild.
- Collections to hide parts: `Coop_House_Shell` (walls/roof, to see roosts and litter),
  `Coop_Mesh`, `Coop_Frame`, `Coop_Extras`.
- Schematic only: mesh drawn at a 5 cm pitch (real is 25×50 mm), window is a placeholder size,
  and the wheel drop is not reflected in the ground contact (frame is not raised in the render).

---

## v1-era log rows

| Date | Event |
|------|-------|
| 2026-10-01 (later) | Added hinged ramp + hoist chain/roof hook, bearing blocks under house legs 0–2, fold-up leg 3; 4 new renders (09–12). Open: floor joists, strap for the stowed leg. |
| 2026-10-01 | Blender MCP set up; 3D model built and iterated (`models/`, renders in `models/renders/`). Design v1: side-hinged window, openable nest lid, mesh roof over whole run, house roof inside the frame (no overhang), full-structure lift handle, axle moved to 1.2 m, foot-lever wheel arms with stop block replacing the fixed axle. Weight estimated ~245 kg, ~22 kgf at the handle. Open: window size, door placement, drip edge, skirt when moving, wheel-arm prototype. |

## v3 foot-lever wheels (superseded by v4 bell-crank levers, 2026-10-08)

Each wheel sat on a straight 2×4 arm pivoting on a wheel post at x = 0.80 m, hub at x = 1.10 m
(a = 0.30), foot pad at ~1.63–1.93 m (lever gain ~3.3, ~40 kgf per foot), wheel travel 6 cm, wood
block jammed under a ledge on the x = 1.50 post. Handle lift was ~20 kgf. Kept for history only.

## v4 bell-crank lever wheels (superseded by v5 cranked axle, 2026-10-08)

**Why v4 (main reason, user's words):** lifting the structure at the handle would have a limit because the tail of the outer structure would touch the floor, especially on slightly uneven terrain. Meaning: lifting the east handle pivots the coop about the wheel axle, so the part of the house end *behind* the wheels swings down toward the ground. Fix = wheels as close to the end as possible (small overhang behind them) **and** raise the house end with the wheels first (wheel drop), then lift the handle. Cost: heavier east handle lift (see below).

Design from the user's sketch (2026-10-08): one rigid **L-shaped lever per side** (2×4 on edge)
pivoting at the house end corner on a wheel post (x = 0.20 m). The horizontal leg runs toward the
run and carries the 30 cm wheel (hub x = 0.55 m, a = 0.35 m); the vertical leg rises to z = 1.0 m
with a grip. **Push the top of the vertical leg toward the run:** the wheel drops 6 cm (lever
turns ~9.9°) and the house end rises. Lock by dropping a wood wedge (~14 cm gap) between a stop
ledge bolted to the corner post (lock height z = 0.85) and the lever. At rest the wheel is flush
with the frame bottom, unloaded.
- Forces (hand calcs): wheel load ~110 kgf per side while the east end sits on the ground →
  **~45 kgf push per lever** at the lock height (gain 0.85/0.35 ≈ 2.4). The wedge takes the
  same load when locked: screw/cord it so it cannot kick out. Pivot bolt M10 through the post.
- Trade-off: moving the hub west makes the **east handle lift ~60 kgf** (v3: ~20). Compromise
  at hub ≈ 0.8 m (~44 kgf). Alternative if too heavy: small fixed wheels at the east end.
- Procedure: push/lock one side, then the other, lift the handle end and roll.
- Clearance checked in the model: ledge on the long side does not touch the window (hinged at
  the west wall, swings outward) or the nest boxes (back side, y 1.22–1.92).
- Unverified in real life: lever bending and wedge stiffness are hand calcs; prototype one side.
- The v3 foot-pedal version is in `chicken_coop_archive.md`.

## v5 branch (brainstorm, 2026-10-08, NOT adopted; v4 stays the current design)

Idea from the user: one mechanism for both wheels instead of one lever per side. Lift/pump it, lock
it in the uplifted state, then walk to the east handle bars and lift/pull as before (nothing drags).
Built as `models/chicken_coop_model_v5.py` → `chicken_coop_v5.blend`, renders in `models/renders_v5/`
(`07/08_crank_*` show parked vs. locked; `08c/08d_lock_pin_*` the pin; `09b_shaft_under_house.png`).
- **Mechanism built (option 2: cranked axle + deadlift handle):** a 32 mm steel shaft crosses under
  the house in sleeves through a post at each side; crank plates at each end carry the wheel stub axle
  120 mm off the shaft; a 0.93 m 2×3 handle clamps on the front shaft end, opposite the crank. Pull the
  handle up ~100° (starts low, ends ~vertical): both wheels drop ~12 cm and the crank goes 10°
  over-centre, so the coop weight presses the handle against a stop block. All mesh is kept (shaft
  passes through a ~3 cm hole in the under-house mesh).
- **Lock pin (user's idea, 2026-10-08):** the grip is a separate 12 mm steel pin with a wood knob,
  NOT joined to the handle. It slides along y through a hole in the handle's top end into a hole
  drilled 3.5 cm deep in the house east-front corner post (`house_post_front_0.93`, at ~1.0 m high).
  Positive lock, like a sliding door bolt: pull the knob out ~6 cm to release (tip stays captive in
  the handle). The over-centre stop takes the load; the pin is the backup against bounces. Hub x is
  derived so the pin lines up with the hole in the locked pose (`GRIP_D`, `CRANK_OVER`, `LOCK_POST_CX`).
  Parked: pin retracted. Alternative post for the hole: `post_front_0` (x 1.0–1.07) → hub ~0.86 m.
- **Numbers (hand calcs, hub 0.79 m):** wheels carry ~237 kgf; pull at the grip ~33 kgf; east
  bars ~44 kgf (v4 at hub 0.55: ~60); overhang behind the wheels drops ~7 cm for a 30 cm lift of the
  east bars, covered by the ~12 cm wheel drop. Torque on the shaft ~30 kgf·m, hand calc only.
- **Why the wheel "drops":** the wheel axle sits on the crank, 12 cm off the shaft; the shaft is fixed
  to the frame. Turning the shaft swings the hub from level with the shaft to 12 cm below it. The wheel
  is already on the ground, so the frame (shaft) rises 12 cm instead. Renders show this: `08e/08f`
  (coop lifted, wheel on the ground), `08g_parked_vs_lifted.png` (side by side).
- **Detail renders** (`renders_v5/detail/`, mechanism isolated, `*_labeled.png` have labels):
  `D1/D4` wheel parked/locked, `D2/D3` crank plate with the tire hidden, `D5/D6` whole shaft across the
  width, `D7` handle + pin + stop block at the post. Scripts: `models/render_detail_v5.py`,
  `tools/label_detail_v5.py`.
- **Open / alternatives considered:** platform-on-crank variant (stand on a short arm, ~44 kgf, sweeps
  25–30 cm) not built; swing-arm pedal not built (wheel drop of 12 cm would need a very deep step).
  Needs welding (or bought parts) for the cranks/stub axles; a latch to keep the parked handle from
  flopping; a stop block through-bolted into the frame.
