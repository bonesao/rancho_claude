# Tropical Greenhouse — Project Definition

Goal: a walk-in greenhouse sized to let **mango and pineapple (and other
tropical/subtropical species) survive and thrive** through Buenos Aires
winters, not just limp along under frost cloth. Year-round vegetables inside
are a secondary use of the space, not the design driver.

Site reference photos:
- [`greenhouse mock.png`](greenhouse%20mock.png) — ground-level shot, orange/blue
  lines mark the intended footprint. The existing avocado frost-cloth tent
  (see [avocado.md](avocado.md)) sits inside this footprint and should end up
  enclosed by the greenhouse rather than moved.
- [`satellite.png`](satellite.png) — top-down Google Maps view with the
  property boundary outlined in red, for overall site context.
- [`sattelite_greenhouse.png`](sattelite_greenhouse.png) — same top-down view
  with the approximate greenhouse footprint outlined in green. Useful for
  cross-checking footprint size against the map's 20m scale bar once the
  real tape-measured dimensions are in.

## Target envelope
- Footprint: **6m × 9m** (tentative real-world size, replacing the earlier
  6m × 8m eyeballed-from-photo estimate — still worth a final tape check
  before ordering materials or pouring footings, but this is a firmer number
  than before). **The 9m axis runs north/south**; the 6m axis runs east/west.
  Net change from the earlier estimate is small: the north/south gable walls
  stay 6m as before, the east/west side walls just grow by 1m (8m → 9m).
- Height: approx. **4m**, driven by mango's mature height, not human headroom
- Two structural options to design and visualize in parallel (see below)

## Site read from the photo

The photo was shot facing south, camera standing roughly at the plot's
**north edge**. That fixes the compass layout:
- **North wall** (short, ~6m, nearest camera): open lawn, no overhead
  obstruction, closest to the house/pergola side of the property.
- **South wall** (short, ~6m, far edge): backs onto the tall
  eucalyptus/deciduous trees visible in the photo background.
- **West wall** (long, ~9m, right of frame): faces the existing wood
  pergola/gazebo and playground structure (confirmed freestanding — no
  shared wall, but keep clearance from both).
- **East wall** (long, ~9m, left of frame): faces the green-tarped area and
  hedge.

### Why this matters more than usual: southern-hemisphere solar geometry
This is the one thing to get right before finalizing a structural design,
because it inverts the "obvious" northern-hemisphere greenhouse playbook:

- In the **southern hemisphere, winter sun tracks low across the northern
  sky**. The single highest-value solar surface here is the **north gable
  wall** (short, 6m wall, full ~4m height) — a mostly-vertical surface
  catches low winter sun efficiently, the same way a north-facing window
  wall works in northern-hemisphere passive solar homes. **Maximize
  glazing (polycarbonate or film) on the north wall.**
- The long walls (east/west) run N-S, so their roof slopes face east and
  west, not north/south — neither catches winter sun as directly as a
  north-facing slope would in an ideal (ridge east-west) layout. This site's
  ridge will end up running N-S given the fixed footprint, which is not the
  textbook-optimal greenhouse orientation, but it's what the existing lawn
  shape and surrounding structures allow.
- **West wall = the overheating risk.** Afternoon sun is the most intense
  heat load in this climate, and it lands on the long west wall closest to
  the pergola. This is the natural place to put the manual vent
  panels/louvers (requirement A below) — venting hot afternoon air where
  it accumulates.
- **South wall is the low-value side** (least direct winter sun anyway) —
  and conveniently it's the side already shaded by the tall trees. That's
  a good match rather than a conflict: put the more solid/insulated
  paneling, thermal mass (e.g. water barrels), and the equipment side
  (heater, power run) here rather than on the valuable north face.
  **Confirmed**: the power outlet is on the south wall (same spot the frost
  cloth is visible in the mock-up photo) — this locks in south as the
  equipment/utility wall and the natural door location.
- Tree canopy caveat: those trees look deciduous (bare in the photo) — they
  will leaf out and cast some shade over the south end of the greenhouse in
  summer. Net effect is probably positive (free summer shade on the low-
  value side, bare in winter when you want sun). **Confirmed**: a nearby oak
  does shade the north/east corner somewhat, but not significantly — no
  major branch-overhang concern.

## Structural options — design and visualize both

### Option A: Wood frame + plastic film (MVP)
Build first, cheap, fast, replaceable — proves out orientation, vent design,
and whether this location actually works before committing real money.
- **Frame**: locally-sourced eucalyptus posts (you already have this on the
  property) as the primary structural members, set in concrete footings —
  not just driven into soil, given the 4m height and open-pampas wind
  exposure with no windbreak on the north side.
- **Covering**: UV-stabilized greenhouse film, ideally the scrim-reinforced
  ("diamond") type over generic poly — costs somewhat more but resists tear
  and wind flap significantly better, matters more at 4m than at typical
  2m tunnel height.
- **Lifespan**: film needs replacing every ~3-5 years; frame should outlast
  several film cycles if footings are solid.
- **Known weak points**: single-layer film has poor insulation (loses heat
  fast on frost nights — the main thing you're building this for), and
  wind load capacity at 4m is the main structural risk to size the bracing
  for (diagonal bracing / knee braces at each post, not just square frames).

#### Addressing the insulation weak point (2026-08-02)
Three options, not mutually exclusive — a staged approach rather than a
single choice:

1. **IR-retention film instead of generic poly — do this regardless.**
   Argentine suppliers (e.g. agropol.com.ar) sell "Termoagro"/tricapa
   greenhouse film with additives that retain long-wave infrared, directly
   fighting the radiative heat loss that makes frost nights the worst case.
   Same install as generic film, no new equipment, modestly higher cost.
   Strict upgrade with no real downside.
2. **Manta térmica — manual interior thermal curtain, recommended as the
   actual frost-night defense.** A retractable agricultural thermal blanket
   (widely sold on MercadoLibre AR — Cerroplast, SIL, BERPLAST) deployed
   over the frame/crop at dusk and pulled back in the morning. No permanent
   daytime light penalty (only up at night), fits the manual-operation ethos
   already set by the venting requirement, and cheap enough to buy and test
   now on the *existing* frost-cloth tent, before the greenhouse frame even
   exists. Consistent with the "backup layer, not single point of failure"
   principle already used for the heater/frost-cloth combo below.
3. **Double-layer inflated film — hold in reserve as the upgrade if 1+2
   aren't enough.** The standard commercial fix: two film layers with a
   small continuous-duty blower keeping an air gap pressurized between them.
   A genuine two-for-one — the air gap adds real insulation *and* the taut
   inflated skin resists wind flap/tear better than a single loose sheet,
   addressing both Option A weak points at once. Fits the power-on-site
   requirement (blower draw is low, similar order to the circulation fan
   already planned), but adds a piece of equipment that must keep running
   continuously, plus a fussier airtight install (inflation valve, sealing
   both layers to the frame). More committing than 1+2, so worth trying
   those first.

Suggested sequencing: do #1 unconditionally, pair with #2 for this winter's
MVP, and only build #3 if frost survival still isn't good enough with the
first two in place.

### Option B: Metal frame + polycarbonate panels (target end-state)
- **Frame**: galvanized steel or aluminum tube/channel — much better
  wind/load capacity at 4m than wood, longer service life, but needs either
  a welded kit or bolted galvanized greenhouse framing system.
- **Covering**: twin-wall or triple-wall polycarbonate — meaningfully better
  insulation than single film (matters directly for winter heating cost and
  frost survival margin), and diffuses light evenly (reduces leaf-scorch hot
  spots vs. clear glazing) — a real benefit for mango.
- **Cost/complexity**: substantially higher material cost, and precision
  fabrication/fastening work that's harder to DIY casually than the wood+film
  version.

### Suggested path
Build A first. **Design A's footing layout and bay spacing to match what B
would need** (same post/column spacing, same footing positions) — so the
concrete work isn't wasted when you eventually swap the frame and film for
steel and polycarbonate. Worth pinning down B's likely bay spacing before
pouring A's footings, even if B itself is years out.

*("Bay spacing" = the gap between structural posts/columns along the wall —
e.g. a post every 3m along the 9m east/west walls gives 3 "bays"; the 6m
north/south gable walls would fit 2 bays at the same spacing. It sets how
many footings you dig and where. Wood posts can
usually space wider than a thin steel frame needs, so if A's posts are
spaced for wood-post strength alone, some of A's footings may sit in the
wrong place for B's tighter steel spacing — deciding B's spacing first
avoids that mismatch.)*

## Bay spacing — decided (2026-08-03)

**3m uniform spacing** for both Option A and Option B, chosen over the only
other grid that divides evenly into both 6m and 9m (1.5m):

- **3 bays along each 9m side wall** (posts at 0/3/6/9m), **2 bays along
  each 6m gable wall** (posts at 0/3/6m) — **10 perimeter posts total**.
  1.5m spacing would double that to 20 posts/footings, which is overkill
  for a hobby-scale structure absent a specific engineering reason to go
  tighter.
- Matches the loose 3m example already used when this doc first explained
  what "bay spacing" means (see Option B section above) — now confirmed
  rather than illustrative.
- **Door placement resolves itself**: the south gable wall (door +
  equipment wall, confirmed) lands exactly 2 bays at 3m — one bay for the
  door, the other for the heater/power run/equipment. No post obstructing
  the doorway.
- **Reversible if undersized**: only Option A's footings get poured now;
  Option B is years out. Going tighter later means adding a post between
  each existing one, not redoing the layout — so starting at the standard
  spacing rather than over-building for an unconfirmed wind case is the
  right default.
- **Roof span follow-on**: the 6m gap between paired posts (the roof beam
  span) needs its own support, not just the wall-post grid. Two measures
  work together: **knee braces at every post-to-beam junction** (diagonal,
  same bracing principle as Option A's post bracing, applied at the roof
  level too — stiffens against racking *and* shortens the beam's
  unsupported span at each end) plus a **king post / collar tie at
  mid-span** to carry the remainder. Both needed, not either/or.

## Below-grade perimeter insulation
A real, well-established technique worth building in from the start — known
as perimeter/skirt foundation insulation, a simplified version of what cold
climates call a frost-protected shallow foundation (near-universal in
Chinese-style solar greenhouses).

- **Why**: sun-warmed soil under the greenhouse footprint acts as thermal
  mass overnight — but only if that heat doesn't conduct sideways into the
  colder soil just outside the structure. This matters here beyond the
  usual air-temperature argument: it protects the **root zone** directly,
  which a heater alone doesn't — cold root-zone soil can stunt/kill
  tropical roots even if the air above it is kept warm.
- **Construction**: trench around the **entire perimeter** (lateral heat
  loss happens on every side, not just one wall), ~40-60cm deep. Line the
  outward-facing side with rigid closed-cell foam board (XPS —
  "poliestireno extruido"; avoid plain EPS beadboard, it soaks up
  groundwater and loses effectiveness). Optional horizontal "wing" — another
  board laid flat, extending 40-60cm outward from the base of the vertical
  board, sloped for drainage — adds lateral protection without digging
  deeper. Backfill with final grade sloped away from the wall.
- **Offset outward from the structural post footings — don't run the trench
  along the same line as the posts.** Concrete conducts heat far better
  than soil or foam; a footing sitting exactly on the insulation line acts
  as a thermal bridge, carrying interior soil heat straight out to the cold
  exterior soil at every post, bypassing the insulation. Instead, keep posts
  where the wall needs them (the trench is buried/invisible, so it doesn't
  need to align with the visible wall plane), and dig the trench so its
  vertical board sits ~20-40cm outboard of each footing's outer edge —
  enough clearance that the footing sits fully inside the insulated
  boundary rather than straddling it. This makes the insulated footprint
  slightly larger than the building footprint, which is a bonus (same idea
  as the "wing" oversizing above), not a downside. Depth doesn't need to
  match either — footings will likely go deeper than 40-60cm for
  wind-uplift anchorage; the insulation only needs to wrap the near-surface
  band where seasonal heat exchange actually happens.
- **No frost-depth engineering needed** — Escobar's climate has no real
  ground-freeze issue, so unlike cold-climate FPSF tables, we're not
  chasing frost-heave protection, just thermal containment. 40-60cm is a
  reasonable practical target here, not an underbuild.
- **Do it at MVP stage, not just at the Option B upgrade** — same
  continuity logic as the footing/bay-spacing note above: it's buried,
  one-time effort, and redoing it later means re-digging the whole
  perimeter.
- **Correction to an earlier note**: water-barrel thermal mass belongs on
  the **north wall** (sun-facing, charges up during the day), not the south
  wall as originally suggested — south stays the equipment/insulated wall,
  it's just not where solar thermal mass should sit.
- **Material: loose-fill perlite ("perlita expandida"), decided.** Mined
  mineral, not organic but not a petrochemical foam either — chosen over
  XPS on sourcing grounds: sold by the bag locally (e.g. 200L bags via
  Orlandi SA), a dedicated distributor (Perlinor), and widely listed on
  MercadoLibre. Contain it in a geotextile fabric sock in the trench so
  soil doesn't migrate in and clog the air pockets that make it work.
  (Cork board and cellular foam glass gravel were considered — both
  effectively import/special-order items with no confirmed Argentine
  distributor as of 2026-07-26 — and straw/wood chips/hempcrete were ruled
  out outright, since they rot in constant below-grade moisture regardless
  of ideology.)
- Whatever the fill, **drainage matters as much as the material itself** —
  a gravel/French-drain layer under and around it keeps it dry, since any
  insulator loses much of its value wet.

## Hard requirement A: manual venting
Southern-hemisphere Cfa summers will cook a sealed structure this size —
this is non-negotiable, not a nice-to-have. Likely approach:
- A **ridge vent** running along the roof peak (hinged flap panels, opened
  by a hand crank, push-pole, or pulley/rope from ground level) — hot air
  exits at the highest point, working with the stack effect.
- **Louvered or roll-up panels on the west wall** (the overheating side, see
  above) as the low-level make-up air intake, or roll-up sides in the wood/
  film MVP (simplest DIY manual vent for that version).
- Non-electric passive auto-vent openers (wax-cylinder actuators, no power
  needed, self-open past a temperature threshold) exist as a middle ground
  between "fully manual" and "powered fan" — worth a look as a later
  add-on even though manual control is the baseline requirement.

## Hard requirement B: power available on-site
A nearby outlet opens up:
- **Frost-night heating**: thermostatically-controlled electric heater
  (oil-column or greenhouse-rated fan heater), sized to the ~215m³ interior
  volume (6m × 9m × 4m, up slightly from the earlier ~190m³ estimate).
  Keep the existing frost-cloth-tent approach around the most
  tender young plants as a **backup layer inside the greenhouse** — heater
  failure or a power cut on the coldest night shouldn't be a single point
  of failure, consistent with how the avocado tents are already run (see
  [avocado.md](avocado.md)).
- **Circulation fan**: keeps heat even and air moving — matters for a humid
  tropical greenhouse where stagnant air invites fungal issues, especially
  around pineapple's preferred high humidity.
- **Thermostatic exhaust fan** as a powered supplement to the manual vents
  for hot days when nobody's around to open them — supplement, not
  replacement, per requirement A.

## Supplemental UV lighting & efficient winter heating (question raised 2026-08-06)

**UV lamps for mango/banana — not necessary.** Plants grow on PAR light
(400–700nm, visible spectrum), not UV — UV lamps are mainly a
reptile-terrarium thing (vitamin D synthesis), not a plant requirement.
Mango and banana have no UV dependency for fruiting or health. Buenos
Aires' latitude (-34°) doesn't have extreme winter day-length either
(roughly comparable to Los Angeles), so the north-wall glazing already
planned (see [southern-hemisphere solar geometry](#why-this-matters-more-than-usual-southern-hemisphere-solar-geometry)
above) should deliver enough visible light on its own. If growth ever looks
light-starved once the structure exists (leggy growth, pale leaves), the
fix is more/clearer glazing or a full-spectrum **PAR grow light** — not a
UV lamp specifically. Revisit only if that symptom actually shows up.

**Winter heating that isn't expensive to run:** no heater is "free" —
running cost is watts × hours × how much heat the structure loses, so the
real lever is minimizing losses first (below-grade perimeter insulation,
manta térmica, IR-retention film — all already planned above) so the
heater only has to cover the last few degrees on the coldest nights, not
carry the whole load.
- **"Eco sol"-style radiant/infrared panels**: a reasonable option, not a
  magic low-consumption trick — radiant panels heat objects/mass directly
  rather than the air, which suits a somewhat-leaky structure well (less
  energy wasted heating air that then escapes through gaps), but
  watt-for-watt they draw the same power as any other resistive heater.
  Fine as the frost-night heater already planned in
  [Hard requirement B](#hard-requirement-b-power-available-on-site), as
  long as it's genuinely **thermostatically controlled** so it only fires
  when temperature actually drops near frost, not running continuously.
- **Cheaper-to-run alternatives worth comparing once wattage numbers exist:**
  - **Soil/root-zone heating cables** buried under the tropical beds — heats
    where frost damage actually happens (roots), typically far lower
    wattage than an air heater for equivalent frost protection.
  - **Compost-pile heating** (hot compost or a small Jean Pain-style mound)
    near the equipment wall — no electricity at all, though it's
    upkeep-heavy and better treated as an opportunistic supplement than the
    primary plan.
  - Whatever heater is chosen, a simple **frost-thermostat** (only switches
    on below ~2–3°C) matters more for running cost than the heater
    technology itself — this is already the plan (Hard requirement B calls
    for "thermostatically-controlled"), just flagging it as the main lever.

No wattage numbers exist yet to give a real cost estimate — revisit once
interior volume/insulation level are locked in and an actual heater is
being priced.

## Heat-loss estimate & solar thermal mass sizing (2026-08-31)

First-pass numbers to size the insulation stack and a water-mass "thermal
battery" against the 6×9×4m envelope, using the mitigation stack already
above (IR-retention film + manta térmica).

### Envelope heat-loss order of magnitude
Envelope area (walls + roof, floor excluded — handled separately by
below-grade perimeter insulation): perimeter 30m × 4m = 120m² walls, plus
~60-65m² gable roof ≈ **~185m² total**. Loss = U × A × ΔT, worst case
ΔT=10K (target +5°C inside vs. a -5°C hard-frost night):

| Envelope state | U (W/m²K) | Steady-state loss | Over a 10h night |
|---|---|---|---|
| Single poly film, MVP as-is | ~6.0 | 11.1 kW | 111 kWh |
| + IR-retention film | ~5.0 | 9.3 kW | 93 kWh |
| + manta térmica deployed at night | ~3.0 effective | **5.5 kW** | 55 kWh |
| Option B twin-wall polycarbonate (no manta needed) | ~3.5 | 6.5 kW | 65 kWh |

Bare single-layer film at 4m is genuinely leaky (11kW hole on a hard-frost
night) — the IR film + manta térmica stack isn't a nice-to-have, it's what
brings the load down to something a thermal battery or a modest heater can
plausibly cover (roughly halves it).

### Solar thermal battery sizing (water totes)
A 1000L IBC tote, painted black, charged from ~15°C to ~35°C by a sunny
winter day (ΔT=20K), stores **~23 kWh** (1000kg × 4.186 kJ/kgK × 20K).
Against 55kWh/night (mitigated envelope, hard-frost case), full non-electric
coverage of the worst case needs 2-3 totes under optimistic charging —
realistically:
- **Typical mild frost night** (ΔT≈7K, ~39kWh loss): 2 totes (2000L,
  ~46kWh) plausibly covers it fully on solar thermal mass alone.
- **Rare hard-freeze night** (ΔT≈10-12K, 55-65kWh): thermal mass alone is
  marginal without 4+ totes, which starts competing with the north wall's
  primary job as the winter-sun glazing surface.

**Recommendation: 4-6 IBC totes (4000-6000L) stacked low at the north wall
base** (see the [corrected thermal-mass placement note](#below-grade-perimeter-insulation)
above) — low enough not to shade the glazing above them. Gives ~90-140kWh
of buffer for most real frost nights; the thermostatically-controlled
heater (Hard requirement B) remains the backup layer for outlier cold
snaps, same "backup, not single point of failure" pattern already used for
heater+frost-cloth.

### Overnight cooldown model — and why fan placement matters
The above tote sizing assumes stored heat reaches the air freely, which
isn't automatic. A two-node lumped model (air node + water node, each
losing/gaining heat to the other and to outside) shows the air temp at any
moment is a blend of water temp and outside temp, weighted by two
conductances: **UA_env** (envelope, air-to-outside — ~555 W/K in the
mitigated case above) and **UA_wa** (water-to-air, via convection off the
tote surfaces — depends heavily on whether air is actually moving across
them). Because the air's own thermal mass is tiny, it settles almost
instantly to whichever blend that gives; the water mass itself barely
cools over one night (its own time constant is 28-48h), so the bottleneck
is entirely how fast the totes can hand heat to the air, not whether
enough water is present.

Modeled with 5×1000L totes (~22m² exposed surface), water charged to 30°C
at dusk, outside stepping down to -3°C and holding (worst-case, ignores it
falling further toward dawn):

| Hour | Air temp — natural convection only (h≈7 W/m²K) | Air temp — fan-assisted convection (h≈15 W/m²K) |
|---|---|---|
| 0 (dusk) | 4.2°C | 9.3°C |
| 2 | 3.9°C | 8.5°C |
| 4 | 3.6°C | 7.7°C |
| 6 | 3.3°C | 6.9°C |
| 8 | 3.1°C | 6.3°C |
| 10 (dawn) | 2.8°C | 5.6°C |
| 12 | 2.6°C | 5.0°C |

Doubling the water-to-air coupling (natural vs. fan-assisted convection)
swings the outcome from **"hovers 2.6-4.2°C, borderline for banana/
pineapple all night"** to **"comfortably 5-9°C, real margin."** The
circulation fan already planned for humidity/fungal control (Hard
requirement B) is doing double duty here — but only if it's actually aimed
to move air across/near the tote bank, not just general room mixing.
**Design detail to carry forward: position the tote bank in the
circulation fan's discharge path when laying out the north wall**, not off
to the side where the fan doesn't reach it.

*Caveats: order-of-magnitude planning model, not a substitute for
instrumenting the real structure once built. Outside temp treated as an
instant step-down held flat rather than continuing to fall toward dawn
(real coldest-point-before-sunrise would eat into this margin further); no
allowance for imperfect daytime charging (a cloudy day lowers the starting
tote temp); floor/soil coupling ignored (handled separately by below-grade
perimeter insulation, above).*

## Open questions / next steps
- **Confirm the 6m × 9m footprint with a final tape measurement** — this is
  a firmer number than the earlier photo-eyeballed 6×8m, but not yet
  surveyed/staked on the ground.
- **Species/height reality check** (separate follow-up doc): mango left
  unpruned outgrows a 4m ceiling — likely needs a dwarf/grafted cultivar or
  committed annual pruning. Worth a dedicated planting-plan doc once the
  structure itself is settled, rather than folding species selection into
  this architecture doc.
- Door placement — south wall (confirmed alongside the power outlet), and
  now further confirmed to land in one of the two 3m bays created by the
  bay-spacing decision above.
- **Door width vs. mobile chicken coop (raised 2026-08-06):** revisit
  whether the south-wall door can be sized wide enough to wheel a mobile
  chicken den/tractor inside on winter nights, using the greenhouse as
  extra frost protection for the chickens. Needs the coop's actual
  footprint/wheel width once that project exists — no chicken-coop doc yet
  to cross-reference. Depends on final door detailing within the door bay
  (one of the two 3m south-gable bays), not just the bay width itself.

## Visualization plan (2026-08-02)
Superseded the earlier AI-image-gen mockup idea (drafting a prompt for
ChatGPT/DALL-E/Gemini/Midjourney against `greenhouse mock.png`) in favor of
an actual CAD-based approach — more precise, and reusable as the spec
changes rather than a one-off image. Three paths were considered:

1. **OpenSCAD parametric script (chosen as source of truth)** — free,
   code-based CAD; write the structure as text with the real dimensions as
   named variables, get an instant rotatable 3D preview, export PNG/STL/DXF.
   Easiest to keep in sync since updating the spec is a variable edit, not a
   redraw.
2. **DXF → FreeCAD/Onshape** — most "legitimate CAD" path (real parametric
   solids, useful if this ever needs to go to a contractor), but the 3D
   extrusion step is manual GUI work in the external tool, not something
   scriptable end-to-end. Held in reserve, not pursued now.
3. **Three.js web viewer** — interactive, no-install, shareable Artifact;
   best for presentation/sanity-checking (e.g. overlaying a sun-angle check
   for the north-gable solar argument), but not a real construction
   reference on its own.

**Sequencing decided**: build the OpenSCAD script first (dimensions, posts,
bay spacing, roof, vents), do a **manual visual review of the rendered
PNGs** to sanity-check the schematic before committing to a footing layout
— specifically confirming the diagonal bracing / knee braces at each post
(see Option A's known weak points above) look structurally right — then
eventually build the three.js viewer (Path 3) once the schematic is
settled.

## Cross-references
- [avocado.md](avocado.md) — existing frost-cloth-tent approach for the
  avocado that will end up inside this structure
- [backlog.md](backlog.md) — living backlog, add build tasks here once the
  design is locked
