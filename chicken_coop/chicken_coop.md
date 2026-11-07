# Chicken Coop

Small hobby flock project (not a production operation): **5 laying hens** to start (eggs only,
no meat plan) in a **mobile tractor, 2.0 × 4.0 m**, wood frame + galvanized hexagonal mesh, raised
house at one end. Location: Loma Verde, Escobar. Current design: **v6** (below; = v5 adapted to what was found while building). Earlier
versions (v0-v4 wheels) are in `chicken_coop_archive.md` (outdated, not a source of truth).

## General recommendations

**Space (5 hens).** Indoor house ~2 m² (≈0.4 m² per bird) and a 3 m × 2 m run (6 m²,
≈1.2 m² per bird). That is on the tight side for a run that stays put, but the coop is a
tractor: moving it to fresh grass every few days is what keeps the ground from being stripped.

**Ventilation.** High vents near the roofline (above roost height) let
ammonia/humidity out without creating a draft on the birds at night —
same "airflow without direct draft" principle as the avocado frost tents.
Don't rely on the door/pop-hole as the only airflow path.

**Nest boxes.** ~1 box per 3–4 hens is enough (they'll pile into favorites
anyway) — so 3 boxes covers 12 hens. Keep boxes darker/more enclosed than
the rest of the coop and lower than the roosts, or hens will roost in the
boxes and foul them overnight.

**Roosts.** Roosting bar space ~20–25 cm per bird, set higher than the
nest boxes, with room below to catch droppings (removable tray or deep
litter) for easy cleaning.

**Predator-proofing.** Pressure is low (gato montés and comadreja around, no fox); the decided
spec (hexagonal mesh, no skirt, window backing, roof battens) is in *Design v3* below. Principles
that hold for any version:
- The nightly lockup of the hens in the solid house (pop-hole closed) is the single
  highest-leverage defense for a small hobby flock.
- Secure latches (carabiner/spring-loaded, not a simple hook): opossums and cats work easy hooks.
- Any opening a paw or head can reach through (louvers, nest-box lids) needs mesh or a latch.
- Cover the run overhead (mesh) against birds of prey and cats.

## Design v6 (current; last updated 2026-10-12)

**What changed from v5 (found while building; photo of the frame on site 2026-10-12):**
- **Frame height H = 1.40 m** (mesh is 1.5 m, not 1.6). Posts are exactly 1.40 m and stand on the
  ground *inside* the rail perimeter; top rails are flush with post tops. The 10 cm of extra mesh laps
  5 cm into the ground and 5 cm folds over the roof mesh.
- **Corner joints on the outside:** the 4 m long rails are outermost (bottom and top); the ~1.9 m end
  rails butt against their inner faces, and each post sits in the inside corner of that L (4.5 cm
  inboard of the rail line). Top long rails stay 3 m (x 1.0-4.0).
- **Run posts only at x = 1.0 / 2.5 / 4.0** (the old x = 1.5 pair is gone; they match the 3 m roof).
  `post_front_0` moved 4.5 cm east (inside the L with the top-mid rail), so the hub is now ~0.91 m
  and the lock pin / handle stop reach 4.5 cm further in (pin 0.24 m, travel 10 cm).
- **Human door moved to the BACK side, x 2.54-3.30** (0.76 m wide x 1.26 m tall), **hinged on
  `post_back_1` (x = 2.5, same x as `post_front_1`, already in place on site)**, latch on an extra post
  at x 3.30-3.37 in the rail line. Top rail is the lintel, bottom rail the 7 cm sill. You duck slightly
  to go in (1.33 m clear under the top rail). The feed/water corner shifted east (cover x 3.45-3.95)
  so the cover hangers do not sit in the door opening.
- **House floor lowered 0.50 -> 0.40 m** (matches the proto house) so the real **1.02 x 1.02 m
  louvered window** fits in the west gable wall (y 0.22-1.24, sill 0, top at 1.42 m, ~2.7 cm under the
  gable edge). Nest boxes shifted to y 1.27-1.91 beside it. Ramp is gentler (~21 deg).
- **House walls: machimbre** (modeled as 12 mm, a colour change only); floor stays plywood. The house
  is expected to grow (new section, new roof) from the proto already built: not modeled yet.
- Ridge drops to ~1.73 m; house interior ~9 cm narrower (walls inside the posts).

*(The v5 text below is kept and still holds except for the points above. v5 files are frozen:
`chicken_coop_model_v5.py`, `chicken_coop_v5.blend`, `renders_v5/`.)*

## Design v5 (superseded by v6 on the points above)

**Look at `models/renders_v6/` before discussing the coop** (table below). Files:
`chicken_coop/models/chicken_coop_model_v6.py` (parametric build script) → `chicken_coop/models/chicken_coop_v6.blend` (all paths in this file are relative to the `chicken_coop/` folder unless they start with `chicken_coop/` or `tools/bl.py`);
`models/render_views_v6.py` → `models/renders_v6/` (mechanism close-ups `renders_v5/detail/` are still the v5 ones: geometry unchanged except hub x, no re-render yet; v3-v5 are frozen: `chicken_coop_model_v*.py`, `renders_v*/`). After any design change: edit the script,
run it, run the render script (both via `python tools/bl.py run chicken_coop/<path to script>` with Blender open and
the "MCP for Blender" add-on connected, or through the `blender` MCP tools), and delete any
render that stops making sense. Don't leave stale renders around.

**Layout.** Total 4.0 × 2.0 m. The **house is the first 1.0 m, full width**: plywood walls and a
**gable roof** (ridge along the length, ~20°, 15 cm overhang on both eaves and 10 cm at the west
end, ridge at 1.94 m). The mesh run is the remaining **3.0 m (6 m² of bare grass, no floor)**;
mesh roof and east end wall belong to the run. Frame: 2"×3" pine (45×70 mm), 1.4 m tall (v6),
galvanized **hexagonal** mesh walls/roof (~21.7 m² total: run, roof, under-house sides and the
window backing). **No anti-dig skirt.**

**Predator pressure:** low. Real threats around: gato montés (Geoffroy's cat) and comadreja
(opossum); both nocturnal; no fox. Not a dog-proof coop: loose dogs would tear this mesh. The key
defense is the nightly lockup of the hens in the solid plywood house (pop-hole closed, simple
latches on the pop-hole and nest-box lids are enough but they must be secure, since opossums
open easy hooks).
**Mesh (decided 2026-10-02): galvanized hexagonal, supplier code 3264**: ¾" (19 mm) opening,
wire N°21 (0.81 mm), roll 1.5 m high, ~485 g/m² (22 kg per 30 m roll), bought **by the meter**
(~16 m; Provetec, provetec.com.ar). Chosen over welded 50×50 (1.9 mm) and 25×25 (1.6 mm) on
price; the small holes keep paws and heads out. Weak points to design around: thin wire and
thin zinc, tears at the fasteners, sags over spans.
- Mesh is held by a batten "sandwich" (mesh between frame and 1"×1" batten, screwed every 15-20 cm) along all edges and mid-span on the walls; short staples only tack the mesh flat while screwing (staple gun can't take 1" staples).
- Roof: 1"×1" battens on top of the mesh on a ~50 cm grid (modeled) so it cannot sag.
- Window: fixed backing mesh inside the opening (modeled; use two layers). The louver gaps are
  the night weak point.
- No gaps under the bottom rail. Latches: spring carabiners/barrel bolts (no padlocks).
  Ground anchors stay (wind, not predators).
- If loose dogs ever show up: upgrade the lower 60 cm of the run walls to welded mesh.

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

**Human door (v6):** on the BACK long side, x = 2.54–3.30 m (0.76 m wide × 1.26 m tall), hinged on
`post_back_1` (x = 2.5, opens outward), latch on a post at x 3.30–3.37, top rail as lintel. The east
end is plain mesh + a mid post. (v5 had it on the front, x 2.54–3.30, 1.45 m tall.)

*Door build (listones 1"x2", ~6 m = 2 verticals 1.45 m + 2 horizontals ~0.76 m + diagonal ~1.6 m):*
1. Lay the frame flat and square; one screw per joint pair, 3.5 x 50 mm, pilot hole first (1"x2"
   splits near the ends). A plywood or metal corner plate at each corner adds a lot of rigidity.
2. **Diagonal brace from the bottom corner on the hinge side up to the top corner on the latch
   side**: it keeps the latch end from sagging. Screw it at both ends.
3. Lay mesh over the frame, tack with short staples, then screw a 1"x1" batten over the mesh around
   the perimeter (same sandwich as the walls).
4. 2-3 hinges on the x = 2.5 m post, spring latch on the x = 3.3 m post.
The model's door diagonal was a vertical placeholder bar until 2026-10-05; now a true diagonal.

**Materials:** see *Lista de compras v3* below (computed from the model's cut list).
Prices not yet checked.

### Reference images, v6 (`models/renders_v6/`; same names as v5 except `12/13_back_door_*`)

| File | Shows |
|------|-------|
| `01_overview_front.png` | whole coop from the front-west: house section, gable roof, run |
| `02_overview_back.png` | from the back-east: door, handle, feed corner, ramp, house at the far end |
| `03_house_west_end.png` | west end wall: window, nest boxes, roof overhang |
| `04_window_and_nest_lid_open.png` | window swung open, nest lid lifted |
| `05_roof_from_above.png` | gable roof over the house, mesh roof with its batten grid over the run |
| `06_handle_east_end.png` | full-width lift handle at the east end, seen from behind |
| `07_crank_rest_side.png` / `08_crank_locked_side.png` | wheel mechanism parked vs. handle pulled up and pinned (side view) |
| `08b_crank_locked_overview.png` | whole coop, mechanism locked (frame not raised) |
| `08c_lock_pin_engaged.png` / `08d_lock_pin_retracted.png` | lock pin into `post_front_0` vs. retracted |
| `08e_lifted_side.png` / `08f_lifted_overview.png` | locked pose with the coop raised 12 cm, wheels on the ground |
| `08g_parked_vs_lifted.png` | parked and lifted side by side, labeled |
| `09_house_floor_structure.png` | house shell hidden: floor, roosts, posts, nest box |
| `09b_shaft_under_house.png` | the shaft crossing under the house floor |
| `10_ramp_parked.png` / `11_ramp_hoisted.png` | ramp down vs. hoisted by the chain |
| `12_back_door_closed.png` / `13_back_door_open.png` | human door on the back side, closed vs. swung open |
| (`renders_v5/detail/D1..D7`) | v5 mechanism close-ups, still valid for the geometry (hub moved 4.5 cm) |

**Open:** crank/shaft prototype (hub is now ~0.91 m), price pass, attaching the floor joists to the
rails (joist hangers or metal angles), how the house will grow beyond the proto, and the shopping list
below still needs a v6 pass (posts 10 instead of 11, door ~1.26 m with one extra post instead of two, mesh cuts about the same ~16 m).

## Lista de compras v3 (diseño actual, 2026-10-02)

Calculada a partir de la lista de cortes del modelo `chicken_coop_model_v3.py` (malla hexagonal,
sin faldón, manija de ancho completo y puerta en el frente), con ~15 % extra por desperdicio. Cantidades aproximadas,
redondeadas hacia arriba (van a sobrar cosas). Precios sin verificar. Largos de madera: preguntar
qué largos tiene la maderera (3 m vs 4 m) y adaptar.

### Viaje 1: estructura y malla (lo mínimo para empezar)

| Ítem | Cant. | Notas |
|------|-------|-------|
| Pino 2"x3" (45x70), **impregnado/tratado** si hay | ~65 m: 17 de 4 m | Largueros (4 m), postes, travesaños, vigas del piso de la casilla, poste de la puerta, barra de la manija (2 m) y palanca de las ruedas (~1 m, sale de la misma cuenta). Lo modelado suma ~56 m. Con tirantes de 4 m se desperdicia menos; vigas y postes salen de a 2 por tirante. Tratado porque apoya en suelo húmedo |
| Pino 2"x2" (45x45) | ~12 m: 3 de 4 m | Travesaños del techo del corral, poste central del extremo este, dintel de la puerta, riostras de la manija. Si no hay 2"x2", usar 2"x3" (pesa un poco más) |
| Listones 1"x1" (25x25) | ~12 m (techo, sale del modelo) + ~40 m (bordes y tramos de las paredes, estimado) | Techo: grilla de listones cada ~50 cm sobre la malla para que no se combe. Paredes: la malla va grampeada y tapada con listón por todo el borde |
| Listones 1"x2" | ~6 m | Puerta humana del frente |
| **Malla hexagonal galvanizada, código 3264**: 3/4", alambre N°21 (0,81 mm), alto 1,50 m, se vende por metro | **~16 m** (comprar por metro, no el rollo de 30 m) | Modelo: 21,7 m². Cortes: frente 3 m + fondo 3 m + este 2 m + techo 4 m (2 tiras de 2 m) + lados bajo la casilla ~1,5 m + respaldo de ventana 2 m (doble capa) = ~15,5 m, más ~0,5 m de margen. Sin faldón |
| Tornillos para madera 4,5–5 x 70–80 mm | ~1 caja (200–300) | Armado de la estructura |
| Grampas galvanizadas **cortas (las que acepte tu engrampadora, 10–14 mm)** | ~1 caja chica (~0,5 kg) | Solo para **sujetar provisoriamente** la malla tensa mientras se atornilla el listón (cada ~30 cm); no sostienen nada por sí solas. Las de 1" no entran en tu engrampadora |
| Tornillos 3,5 x **50–60 mm**, galvanizados/zincados | ~2 cajas (~300–400) | Listones 1"x1" sobre la malla, uno cada 15–20 cm (~52 m de listón). Largo = 25 mm de listón + 25–30 mm dentro del pino. Los de 30–40 mm quedaban cortos. Agujero guía cerca de los extremos del listón |
| Escuadras / ángulos metálicos con tornillos | ~16 | Uniones poste-larguero, que cargan todo el peso al levantar |
| Soportes para vigas ("joist hanger") o escuadras | ~8 | 4 vigas del piso de la casilla x 2 extremos |

### Viaje 2: casilla, manija y ruedas

| Ítem | Cant. | Notas |
|------|-------|-------|
| Terciado exterior (fenólico/marino si da el presupuesto) | 5 placas de 2,44 x 1,22: 4 de 12 mm + 1 de 18 mm | 12 mm: paredes (frente, fondo, 2 hastiales), techo a dos aguas, nidos, rampa. 18 mm: piso de la casilla (~1,8 m²; sobra buena parte). El techo también puede ir en 12 mm (el modelo usa 15 mm) |
| Chapa para techo | 2 (una de ~2,5 m para los 2 faldones de ~1,1 x 1,2 m, más una chica o retazo) | Faldones de la casilla con alero y cobertizo del comedero (~1 x 1 m) |
| Ruedas neumáticas ~30 cm con eje/buje | 2 | Verificar el diámetro del agujero para el perno del eje |
| Bulones M8 con tuerca y arandela, ~100–120 mm | ~12 | Brazos y riostras de la manija, y cartelas de las palancas, pasantes (no tornillos para madera) |
| Barra de acero lisa Ø32 mm (o caño de pared gruesa) | 1 de ~2,15 m | Eje transversal bajo la casilla (gira dentro de los postes). Torsión ~30 kgf·m según cuentas a mano: confirmar el material con el herrero |
| Planchuela de acero 40×8 mm | 2 de ~0,2 m | Bielas (manivelas) soldadas a cada punta del eje; el eje de la rueda va a 12 cm del eje |
| Varilla/bulón de acero Ø16 mm con tuerca y arandela | 2 de ~0,2 m | Eje de cada rueda, soldado a la biela |
| Collares con prisionero Ø32 (o soldar topes) + casquillos/caños para el agujero en los postes | 4 + 2 | Que el eje no se corra y gire sin trabarse |
| Varilla de acero Ø12 mm ~0,2 m + perilla de madera (el "grip") | 1 | Traba deslizante: pasa por el agujero de la manija y entra 3,5 cm en `post_front_0` |
| Bulones M10 con tuerca y arandela | ~4 | Postes del eje, taco de tope (contra `post_front_0`) y fijación de la manija al eje |
| Bisagras | ~10 | Ventana (2), tapas de nidos (2), puerta humana del frente (3, es de 1,45 m), rampa (2) |
| Cierres: mosquetones con resorte o pasadores | ~5 | Sin candados |
| Anclajes al suelo (por el viento) | 4 | |
| Lámina de vinilo para piso | ~2 m² | Piso de la casilla (~1,9 x 0,95 m, cama) |
| Comedero + bebedero | 1 de cada | Cualquier tamaño para 5 gallinas |
| Roldana chica + cuerda | 1 | Puerta guillotina de la gallinera |
| Cadena liviana ~1,5 m + mosquetón + 2 armellas/ganchos | 1 | Rampa: sube con la cadena al gancho del techo para mover la estructura (cadena modelada ≈ 1,36 m) |
| Palo redondo 35–40 mm (o cabo grueso) | ~4 m | 2 posaderos de ~1,8 m |

La ventana reusada (~1,0 x 0,85 m) ya la tenés: el marco que se ve en el modelo es solo de
referencia, no hay que comprarlo.

### Madera: pino vs. saligna (2026-10-02)
Saligna (eucalipto) se evalúa como alternativa más barata al pino; el usuario la ve en general
intercambiable (diferencias no críticas). No cambia el diseño, pero:
- **Peso:** ~600-700 kg/m³ vs ~450-500 del pino → madera ~150 kg en vez de ~117; total ~315 kg
  (vs 283), ~20 kgf en la manija (vs 18), ~150 kgf por rueda (verificar la carga nominal de las
  ruedas), ~37 kgf en la manija de las ruedas. Estimaciones; si se vende verde pesa mucho más.
- **Preguntar a la maderera:** ¿estacionada/secada?, ¿sección real (¿45x70?)?, ¿hay largos de
  4 m?, ¿impregnada y con qué?
- **Trabajo:** se raja en los extremos y es dura: agujero guía siempre, tornillos a ≥3 cm del
  extremo, herrajes galvanizados o inoxidables (taninos).
- **Mezcla posible:** saligna en largueros, pie de postes y brazos; pino en travesaños del techo,
  dintel, listones y puerta (ahorra peso, sobre todo en el extremo este).
- Tratada/impregnada para todo lo que toca el suelo; lo demás puede ir sin tratar.

### Extras útiles
- Preservante o aceite para madera (cortes y travesaños inferiores).
- Mechas para madera (agujeros guía, evitan rajar el pino de 45 mm) y una mecha larga para los bulones M8.

### Si hoy solo podés comprar ALGO
Comprar el **pino 2"x3" y los tornillos**. La estructura es lo primero que se arma, no depende de ninguna decisión abierta y los sobrantes se reutilizan. La malla puede esperar a tener el marco armado, pero ya está decidida: código 3264, ~16 m por metro.

## Weight & handle (structural check, v5)

Estimated from the 3D model (pine 500 kg/m³, plywood 600, hexagonal mesh 0.485 kg/m², chapa ~4
kg/m²): **~283 kg total** (pine 117, plywood 106, mesh 10.5, roofing 14, hardware 25, hens 10);
balance point x ≈ 1.30 m from the west end. Rough; wet pine runs heavier. Typical 5-hen tractors
weigh 50–80 kg, so this one is a big build.
- Lift force at the handle (x ≈ 4.26 m) depends on the wheel-hub position: hub at 1.00 m →
  ~26 kgf; **hub at 1.10 m → ~18 kgf (v3)**, wheels carry ~264 kgf; hub at
  1.20 m → ~9 kgf. **v5 put the hub at 0.86 m → ~39 kgf at the east handle; v6 (hub 0.91 m) → ~36 kgf, ~34 kgf pull at the grip, wheels carry ~246 kgf** (v5: wheels carry ~243 kgf; v4 at
  0.55 m was ~60 kgf). Hub x is derived in the script (`HUB_X`). Keep the hub west of the balance point by ≥ 0.2 m or the coop tips onto
  the house end.
- Handle failure risk is the connection, not the wood: arms tie into the corner posts, never the
  mesh; M8 through-bolts with washers (not wood screws). Post-to-rail joints carry the whole
  weight when lifting: use metal angle plates or bolts there too. The 2 m bar is 2×3 on edge
  (a round pole of the same span would flex too much).
- Weight-saving options considered, **not adopted** (revisit if it feels too heavy): 9 mm
  plywood for roof and walls, 45×45 instead of 45×70 members.

## Cranked-axle wheels (v5, current)

**Why (user's words):** lifting the structure at the handle would have a limit because the tail of the outer structure would touch the floor, especially on slightly uneven terrain. Meaning: lifting the east handle pivots the coop about the wheel axle, so the part of the house end *behind* the wheels swings down toward the ground. Fix: wheels near the end **and** raise the house end with the wheels first (12 cm wheel drop), then lift the handle. (v3 foot pedals and v4 L-levers are in `chicken_coop_archive.md`.)

**Sequence:** pull the deadlift handle up → both wheels drop together and lock → walk to the east
handle bars and lift/pull as before (nothing drags on the ground).
- **Mechanism:** a 32 mm steel shaft crosses under the house in sleeves through a post at each side
  (between the bottom rail and the floor rail). A crank plate at each end carries the wheel stub axle
  120 mm off the shaft. A 0.93 m 2×3 handle clamps on the front shaft end, opposite the crank (parked:
  points west, ~15 cm off the ground). Pulling it up ~100° swings the cranks down; the crank goes 10°
  over-centre, so the coop weight presses the handle against a stop block bolted to `post_front_0`.
  All under-house mesh is kept (the shaft passes through a ~3 cm hole).
- **Why the wheel "drops":** the wheel axle is off-centre on the crank and the shaft is fixed to the
  frame. Turning the shaft moves the hub from level with the shaft to 12 cm below it. The wheel is
  already on the ground, so the **frame rises 12 cm** instead (see `08e/08f/08g`).
- **Lock pin (user's idea):** the grip is a separate 12 mm steel pin with a wood knob, NOT joined to
  the handle. It slides along y through a hole near the handle's top end into a hole drilled 3.5 cm
  deep in **`post_front_0`** (x 1.0–1.07, runs floor to roof, at ~1.0 m high). Positive lock like a
  door bolt; pull the knob out ~6 cm to release (the tip stays captive in the handle). The over-centre
  stop takes the load, the pin guards against bounces. Parked: pin retracted. Hub x is derived so the
  pin lines up with the hole (`GRIP_D`, `CRANK_OVER`, `LOCK_POST_CX`).
- **Numbers (hand calcs, hub 0.86 m):** wheels carry ~243 kgf; pull at the grip ~33 kgf; east bars
  ~39 kgf (v4: ~60); the overhang behind the wheels drops ~8 cm for a 30 cm lift at the east bars,
  covered by the ~12 cm wheel drop; shaft torque ~30 kgf·m. Lock margin: over-centre 10° ≈ 1.7 cm of
  offset; the pin is the backup. Releasing: push the handle back past vertical (~5 kgf), then lower it
  **under control** (the full coop weight comes onto the crank; letting go drops the house end 12 cm).
- **Welding:** user can get the shaft/crank/stub-axle welding done.
- **Open:** latch/hook so the parked handle does not flop; real shaft material and sleeve/bearing
  choice (ask the herrero); prototype one wheel assembly first; stop block and pin hole alignment on the
  real post; a platform-on-crank variant was considered and not built.

## 3D model (Blender)

- Build script: `models/chicken_coop_model_v6.py` (parametric; dimensions are variables at the top,
  idempotent: rebuilds the `Coop_*` collections and saves `models/chicken_coop_v6.blend`).
  Renders: `models/render_views_v6.py` → `models/renders_v6/` (see the table above).
- Run: `python tools/bl.py run chicken_coop/<path to script>` with Blender open and "MCP for Blender" connected
  (N-panel → Connect to Claude); or use the `blender` MCP tools in a session started after it
  was connected. Setup notes are in memory (`blender_workflow`).
- Openable parts (select the empties, rotate in the viewport):
  `window_hinge`: vertical edge, Z positive = swings out.
  `nest_lid_hinge`: wall edge, Y positive = lid lifts.
  `door_hinge`: human door (back side), Z positive = swings out.
  `ramp_hinge`: Y toward ~18.6° = ramp hoisted (swap `chain_hanging` for `chain_taut`), 27° = parked;
  or set `RAMP_LIFTED = True` and rebuild.
  `crank_hinge`: shaft axis, Y positive (~100°) = handle pulled up, wheels down (the whole coop then
  rises 12 cm; the render script does that for `08e/08f`). `lock_pin` + `lock_grip` slide +0.10 m in y
  to engage the post; or set `WHEEL_LOCKED = True` and rebuild.
  `window_backing` is the fixed mesh inside the window opening (hidden when the window is closed).
- Collections to hide parts: `Coop_House_Shell` (walls/roof, to see roosts, litter and joists),
  `Coop_Mesh`, `Coop_Frame`, `Coop_Extras`.
- Schematic only: mesh drawn at a 5 cm pitch (real is ¾" hexagonal), window is a placeholder size,
  and the .blend keeps the coop at ground level (the "lifted" pose exists only in the render script).

## Nutrition & health

Living Q&A section — add to this as questions come up rather than
front-loading everything now.

**Bedding: reusing alfalfa (archery target) bales for nest boxes.**
Alfalfa is a fine, even preferred, nest-box material — softer than straw,
cushions eggs well, safe if hens peck at it (it's just feed-grade legume
hay). Since these bales lived outside as archery targets, check before use:
- **Mold/must** — alfalfa molds faster than straw (holds moisture, more
  nutrient-dense). Damp, grey/black-speckled, or sour-smelling material
  should be discarded — moldy bedding risks aspergillosis (fungal lung
  infection), a serious risk, not a minor one.
- **Arrow debris** — check for broken nocks/field points/fletching
  fragments worked into the bale (foot-injury/ingestion risk).
- **Compaction** — target bales are pressed much denser than loose bedding;
  break up and fluff before use.
- **Change cadence** — swap nest bedding more often than straw/shavings
  would need, since it breaks down and moistens faster, especially once
  warm/humid.
If the outer layer looks weathered, peel it off and use only the drier
interior.

**Wood ash for chicken health.** Real use is external-parasite control via
the dust bath, not nutrition — don't feed it. Mechanism is the same as
diatomaceous earth: fine alkaline ash coats mites/lice and strips the waxy
cuticle, killing by desiccation. Mix into the dust-bath sand/dirt (~1 part
ash to 3–4 parts dirt), never used pure. Only fully cooled, fully
combusted clean-wood ash — no treated lumber/painted wood/trash mixed in,
no smoldering embers. Keep dry and covered: wet ash turns caustic (mild
lye) and can burn feet/skin, and loose ash dust indoors is a respiratory
irritant — fine as a contained dust-bath ingredient, not as loose coop
litter. Doesn't touch internal parasites (worms) — different problem.
Worth deciding a dry/shaded dust-bath spot once the run layout is settled.

## Log

| Date | Event |
|------|-------|
| 2026-09-11 | Project file started. Target ~8–12 hens, eggs only, 4×6 m coop+run footprint. Still comparing designs online; no build started yet. |
| 2026-09-29 | Direction chosen: mobile tractor, 5 hens to start, 2×4 m, wood frame + welded mesh, raised house with reused window and external nest boxes. Predator pressure confirmed low → moderate mesh/latch spec. |
| 2026-10-01 | Blender model built and iterated through design v1 (details archived in `chicken_coop_archive.md`). |
| 2026-10-01 (v2) | Compared layouts A (full-width house as first 1 m section) vs B (narrow house sticking out) with massing previews; chose A. v2 built (`chicken_coop_model_v2.py`, `renders_v2/`): gable roof with overhang, window + nests on the west wall, floor joists, run 3 m, wheels moved to hub 1.10 m. |
| 2026-10-02 (v3) | Switched to hexagonal mesh (code 3264: ¾", 0.81 mm, 1.5 m high, by the meter, ~16 m) for price; v3 files built; no skirt, roof batten grid, window backing mesh. ~283 kg, ~18 kgf at the handle. v2 moved to `chicken_coop_archive.md`. |
| 2026-10-02 | Wood discussion: saligna considered instead of pine for price; no design change needed (~+30 kg, ~20 kgf at handle). User will check prices/lengths/dryness with the maderera. |
| 2026-10-02 | Shopping list v2 generated from the model's cut list. v2 updated in place: full-width handle on the east corner posts, human door moved to the front long side (x 2.54–3.30), front skirt gap at the door. ~286 kg, ~20 kgf at the handle. v0/v1 material moved to `chicken_coop_archive.md`. |
| 2026-10-08 (v4) | User sketched a new wheel mechanism: L-shaped bell-crank levers with the pivot at the house end corner, wheel hub at x = 0.55 m (was 1.10 m), pushed by hand instead of by foot. v4 built (`chicken_coop_model_v4.py`, `renders_v4/`); v3 frozen. Cost: ~60 kgf lift at the east handle (was ~20); ~45 kgf push per lever. User OK with building at 0.55 m. Main reason: when lifting the east handle the part of the house end behind the wheels swings down and would touch the ground, especially on uneven terrain. |
| 2026-10-08 (v5) | Brainstormed and **adopted v5**: single cranked axle + deadlift handle for both wheels, 12 cm drop, over-centre stop + separate sliding lock pin into `post_front_0` (user chose that post: it runs floor to roof). Hub derived ~0.86 m, ~33 kgf handle pull, ~39 kgf east lift. User can get the welding done. v4 (L-levers) frozen and archived. |
| 2026-10-12 (v6) | Built so far: bottom/top rail frame + posts + proto house inside the perimeter (chickens arrive soon). v6 adopted: H = 1.40 (mesh 1.5), posts on the ground inside the rail L, run posts at 1.0/2.5/4.0, door to the back centred on x = 2.5 (1.26 m tall), house floor 0.40 m, real window 1.02x1.02 in the west gable, machimbre walls. v5 frozen. Hub 0.91 m, ~36 kgf east lift (hand calcs not re-derived for the lower CG). |
| 2026-10-12 (v6 edit) | Second row of posts already set on site, so the back door now hinges on `post_back_1` (x 2.5) and spans x 2.54-3.30 instead of being centred; feed corner moved east. Edited in place (still v6). |
| 2026-10-12 | Door parked: for the MVP (chickens arriving) the back door will be a hack: mesh stapled to a wooden post, tied in place with external wire. The real door (design above) comes after the MVP is done. |
