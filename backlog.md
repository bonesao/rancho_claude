# Backlog / Living Calendar

Cross-project running list — the "what should I focus on this week?" reference.
Unlike `calendario_huerta.md` (vegetable-bed specific), this covers the whole
property: fruit trees, backlog projects, anything not tied to one patch file.
Pull from this on any conversation; add to it as things come up.

---

## Garden to-dos (added 2026-11-11, see [vegetable_patches.md](vegetable_patches.md))

- [ ] Re-seed luffa in the tunnel's luffa section (planned "in the next days")
- [ ] Check the big beet(s) — decide harvest before they go woody
- [ ] Corn + pumpkin re-sown 2026-11-11 in the empty row: label rows, don't weed inside until ~15 cm. Identify corn vs sunflower in the surviving row (~8 plants, 40 cm) and decide on beans for the three-sisters guild
- [ ] Peas: let seed plants dry fully, harvest pods, store labelled for next season
- [ ] Old raised bed: plan deep aeration (autumn/winter 2027) before next sowing
- [ ] ~Nov 18-21: check germination in the new 2×2 m bed, corn/pumpkin lines, amaranth/pumpkin patch, tunnel pumpkin (all sown 2026-11-11); label rows
- [ ] Chard seed: let bolsón 2 stalks dry fully, collect, store labelled
- [ ] No-till potato mulch: check for shoots in 2–3 weeks, top up hay
- [ ] Identify the Turkish beans' habit (bush vs trellis); if trellis, try moving them from the new 2×2 m bed to the mesh tunnel (next ~2 weeks, workload permitting)
- [ ] Berry fence (pea line): next visit, check the ~4 gifted raspberry transplants (15–20 cm when planted) — how many survive/where, and clear wild zarzamora away from them (see [vegetable_patches.md](vegetable_patches.md))
- [ ] Artichoke: ~7 more small heads to harvest as they fill
- [ ] Amaranth re-sow (optional, "maybe soon")
- [ ] Zucchini and 3-sisters pumpkin batch still unsown — good window now (warm soil)

## Current seasonal notes

### Winter (Jun-Aug) — dormant deciduous fruit tree watering

Durazno, ciruela, cerezo, pelón (and manzana/pera once they drop leaves) go
fully dormant and leafless in winter — **this is normal**, not a stress signal
(unlike palta, which is evergreen and shouldn't be dropping leaves).

- Dormancy = minimal water demand (no transpiration). **Overwatering risk
  (root rot in cold+wet soil) is higher than underwatering risk** during
  this window — err toward watering less, not more.
- Exception: a genuinely prolonged dry stretch (3-4+ weeks, negligible rain)
  can still stress roots, especially on younger trees.
- **Moisture check with mulch + manure layer at the dripline**: don't judge
  by the mulch or the manure layer itself — both hold moisture far longer
  than the mineral soil underneath and will read "damp" long after the
  actual root-zone soil has dried out. Pull mulch aside, dig past the
  manure layer into the mineral soil a few inches down, and judge from there.
- Winter is also a good window for structural pruning while trees are
  leafless/dormant.

### Oct 2026 — plant 2nd avocado batch (4 baby paltas) into ground

**Progress 2026-11-04:** 2 planted ~Oct 21, 3rd planted week of Nov 2. 4th still
to plant (confirm). Check shade cover on the new ones before the heat arrives.

4 younger avocados currently potted on the house porch, not yet in soil (see
[avocado.md](avocado.md) "Second batch" section, logged 2026-08-31). Recommended
sequence:
1. **Now → Sept**: harden off gradually (more outdoor/sun exposure) while still
   potted; build each tree's shade-cloth structure ahead of transplant.
2. **October 2026**: target planting window — after frost risk clears but
   before summer heat, avoiding the Jan/Feb timing that likely stressed the
   first batch.
3. **At planting**: confirm drainage (no pooling) before committing, given the
   first batch's overwatering/root-rot scare.
4. **~May 2027**: build anti-frost tents (frost cloth + thermal-battery
   buckets) ahead of these trees' first winter in the ground.
- Hold off any liquid feed (banana tea, compost leachate, etc.) on this batch
  until each tree is confirmed stable post-transplant.

### Late Aug / spring — orange tree micronutrient correction

Both mature naranja trees have trended toward smaller/more acidic/less sweet
fruit over the years (see [fruit_trees.md](fruit_trees.md), noted 2026-07-27).
Working hypothesis: never-fertilized trees + high soil pH (~pH 8, see
[[soil_ph]]) causing Fe/Zn/Mn lockout.

- **Late Aug (pre bud-break):** soil-side correction — chelated Fe/Zn/Mn
  granules or elemental sulfur at the dripline.
- **Sep-Oct (spring flush, post-bloom):** foliar chelated micronutrient spray
  on new leaves.
- **Dec-Jan (fruit sizing):** second foliar round — this is the window that
  most directly affects sweetness of the fruit that hangs through next winter.
- Also: watch spring leaves for asymmetric blotchy mottling (would point to
  citrus greening/HLB instead of a nutrient issue — reassess if seen).

---

## Open backlog items (small projects to scope)

### Irrigation control (merged, 2026-07-27)
The WiFi tap/valve prototype and the LoRa soil-moisture irrigation project
were merged into one staged project — actuation → automation →
weather-driven decisions — since they were the same underlying goal at
different layers. Full detail (including the weather/rain-data-driven
watering advisory idea, now Layer 3) lives in
[irrigation_control.md](irrigation_control.md), not here, since it's
substantial enough to need its own file.

### Vino de mora (2026-11-07) — season is NOW
Mulberry (black-ripening + white) in season Oct–Dec. Guide in [vino_de_mora.md](vino_de_mora.md).
- [ ] Start harvesting every few days and freezing (negra / roja oscura / blanca in separate bags)
- [ ] Buy minimal kit before fermenting: densímetro, metabisulfito, pectinasa, levadura, damajuana + airlock
- [ ] Decide batch size (5 L control vs. 5 L white+black) once yield is known

### Mobile PWA viewer for working .md files (2026-08-12, plan-ahead only — not active)
Idea: a simple PWA that imports/renders the various working `.md` files
(fruit_trees.md, backlog.md, avocado.md, greenhouse.md, etc.) as
"what you see is what you get" pages, hosted on AWS, so it's checkable from
the phone while out working the terrain instead of walking back inside to
look something up.
- Not to be scoped or built yet — just holding the idea so it isn't lost.
- Known tradeoff already flagged by the user: any future edit to a working
  file needs a matching PWA content update + redeploy/push to actually show
  up on the phone. Plan to pair this with an automated reminder (rather than
  relying on remembering to sync manually) once the PWA is actually built.

### Chicken coop — design phase (2026-09-11, updated 2026-09-29)
Mobile tractor, 5 hens to start, ~2×4 m, eggs only. Design v0 and material
list in [chicken_coop.md](chicken_coop/chicken_coop.md). Predator pressure is low but not
zero: moderate spec (welded mesh, nightly pop-hole lockup, small skirt).
Next: measure the reused window, decide human access (end door vs. lift-up
roof), choose placement, then a Mercado Libre price pass before buying.

### Buy pest traps — durazno/membrillo (2026-08-19)
Neither owned yet. Both needed before committing to any recurring
preventive spray (jabón potásico + neem) on durazno through bloom — see
[fruit_trees.md](fruit_trees.md) for full reasoning.
- **Grafolita pheromone trap** — durazno (amber gum at shoot tips last
  season, leading suspect).
- **Fruit-fly trap** (yellow sticky + attractant, or DIY vinegar trap) —
  durazno (co-suspect) and membrillo (rotten/malformed fruit last season,
  no shoot-tip gum, so grafolita less likely there — see fruit_trees.md).

### Greenhouse schematic → 3D visualization (2026-08-02)
Decided against AI-image-gen mockups in favor of an actual CAD-based
approach, staged:
1. **Build an OpenSCAD parametric script** encoding the current spec (6m ×
   9m × 4m, N-S orientation, bay spacing) as the source of truth for the
   structure.
2. **Manually review the rendered PNGs** to sanity-check the schematic
   visually — e.g. confirm the diagonal bracing/knee braces at each post
   (see Option A weak points in [greenhouse.md](greenhouse.md)) look right
   before committing to a footing layout.
3. **Eventually build a three.js web viewer** (interactive, no install) for
   a more shareable/presentable visualization once the schematic is settled.
Full path comparison and rationale in [greenhouse.md](greenhouse.md).

---

### Limón — pulgones (aphids) on new shoots (2026-10-08)
Black aphids on a tender shoot tip with curled leaves, near flower buds. Details and reasoning in [fruit_trees.md](fruit_trees.md).
- [ ] This week: prune/bag the worst curled tip, hand-wipe the rest, water-jet shoots every 2-3 days
- [ ] Check trunk for ants; add sticky barrier if present
- [ ] Re-check in ~1 week (also naranja/mandarina/quinotos); if spreading → jabón potásico at dusk, not on open flowers
- [ ] No nitrogen/manure/seaweed on the lemon this spring
- 2026-11-04: outbreak spread to many branches → applied jabón potásico + neem on lemon (+ mandarina preventive, durazno/ciruelo leftovers). 
- [ ] Repeat soap/neem on lemon ~Nov 9-11 at dusk, off open flowers; check ants on trunk
- [ ] Durazno: cut open a few aborted/shriveled fruitlets (larva = grafolita, rot = monilia, clean = normal drop); clear fallen fruit. Reminder: pest traps still unbought (see above)

### Mulch ring + flower removal — young apple (2026-10-08)
Red Delicious (planted 2026-08): pinch off the pink-bud flower clusters now (keep leaves), and clear turf in a ~1 m ring around the trunk and mulch it (wood chips or straw, kept off the trunk). Cherry: same ring if it lacks one. Reasoning in [fruit_trees.md](fruit_trees.md).
- Later (July, dormancy): pick a central leader on the apple.

## How to use this file
When asked "what should I focus on this week / this month?", check this
file's current seasonal notes plus `calendario_huerta.md`'s month-by-month
section, and the pending-questions files for any active LoRa workstream.
