# Irrigation Control — Actuation, Automation & Weather-Driven Decisions

Merged 2026-07-27 from three previously separate threads that were really one
system viewed at different layers:
1. `wifi_valve_control.md` (WiFi tap/valve control prototype)
2. `lora/soil_moisture_irrigation.md` (LoRa soil-moisture-triggered irrigation)
3. The "weather/rain-data-driven watering advisory" backlog idea

## Why merge
These aren't three separate projects, they're three layers stacked on the
same underlying goal:
- **Actuation** — can we turn water on/off remotely at all?
- **Local trigger** — should it turn on *right now*, based on soil moisture
  at that spot?
- **Decision layer** — should we even be watering today, given accumulated
  rain/weather data across the property?

Building the actuator twice (once for a "WiFi prototype", once for the "real"
LoRa version) was duplicated effort, and the weather-advisory idea was
floating in the backlog with no actual consumer. As one staged project, each
layer builds on the previous one's hardware instead of starting over.

## Layered architecture

### Layer 1 — Actuation (the physical on/off)
Goal: phone (or code) can open/close a real tap or valve, no sensing logic yet.

**Two ways to actuate an existing tap:**

**A. Servo/motor retrofit** — grips and turns the existing canilla, plumbing untouched.
- Pros: no cutting into the water line, fully reversible, cheap, works on a
  tap you already trust not to leak.
- Cons: needs a 3D-printed/improvised mechanical coupler; torque/reliability
  depends on tap stiffness; no confirmation water actually flowed, only servo
  position.
- **Only works cleanly on a quarter-turn ball valve** (lever handle, 90°
  open-to-closed). A multi-turn gate valve (screw stem, several rotations)
  needs a geared DC motor/stepper, not a hobby servo — check tap type first.

**B. Integrated electric valve** — splice a 12V solenoid or motorized ball
valve into the line, replacing manual actuation entirely.
- Pros: purpose-built, reliable, easy relay/MOSFET control, well-documented.
- Cons: requires cutting into hose/pipe; less reversible; another
  gasket/fitting = another leak point.
- **A manual bypass valve in parallel is non-negotiable** — when (not if) the
  system fails, you can still water by hand without disassembling anything.

**Recommendation**: start with A (servo retrofit) if the candidate tap is a
quarter-turn ball valve — cheapest, most reversible way to prove "phone → tap
opens" before committing to a permanent integrated valve. Fall back to B
directly if it's a multi-turn gate valve.

**Stack:**

| Layer | Recommendation | Why |
|---|---|---|
| MCU | Reuse one of the 2 **Heltec Wireless Stick** boards already owned | ESP32 — native WiFi, no purchase needed. LoRa radio sits unused for this layer. |
| Firmware | **ESPHome** | Fastest path to a reliable, locally-controlled device (servo/relay components built in); no cloud dependency; avoids hand-rolling WiFi reconnect/OTA/watchdog logic. |
| Control layer | **Home Assistant** if a dashboard + automation is wanted later; otherwise ESPHome's own web server / native API + phone browser is enough for a bare prototype | Don't stand up Home Assistant for one switch — only worth it once devices accumulate (frost alarm, well monitor, this). |
| Actuation electronics | Servo path: any ESPHome-supported hobby servo + its own 5-6V supply (not off the ESP32 regulator). Valve path: relay/MOSFET module with flyback diode. | Standard ESPHome components either way. |
| Power | Mains adapter if the candidate tap is near an outlet | Simpler than solar/battery for a prototype; revisit if far from power. |
| Mechanical (servo path) | 3D-printed bracket clamping servo horn to tap handle, or improvised hose-clamp + arm | Needs a physical fit check against the actual tap before ordering/printing. |

### Layer 2 — Local trigger (soil-moisture automation)
Goal: the valve from Layer 1 opens/closes on its own based on soil moisture,
not a person tapping a button. This is the **first project with an
actuator running unattended** — get it bulletproof on one low-stakes zone
before scaling. The goal here is not water savings (there's well water) but
**labor reduction + consistency**, especially during travel.

**Connectivity choice**: reuse Layer 1's WiFi if the zone is within normal
home WiFi range (no gateway needed). Fall back to LoRa (original plan) only
if the target zone is genuinely out of WiFi range — then it needs the
gateway setup shared with [frost_alarm.md](lora/frost_alarm.md) /
[well_monitor.md](lora/well_monitor.md).

**Sensors (~USD 10-15):**
- **Capacitive soil moisture sensor v2.0** × 2-3 per zone. **NOT resistive**
  — resistive probes corrode within months, worse in this pH ~8 soil
  (alkaline conditions accelerate electrochemical corrosion; see
  [soil_ph.md (memory)](../../Users/lucia/.claude/projects/C--Lucho-rancho-IA/memory/soil_ph.md)).
  - Multiple sensors per zone catches local variation (sun pocket vs. shade)
    and gives redundancy if one fails.
  - Pick versions with a **conformal-coated or epoxy-sealed PCB** — bare-trace
    clones fail outdoors within a season.

**Plumbing add-ons (~USD 10-20):**
- Hose adapters / barbed fittings to splice the solenoid (path B) into the
  existing line, if not already done in Layer 1.
- Teflon tape, hose clamps.
- Optional: **YF-S201 flow meter** inline after the valve — confirms water
  actually flowed when it opened (catches blocked lines, closed upstream
  valve, dead pump).

**Roadmap:**

0. **Pick the zone** — smallest, lowest-stakes bed (salad/herb, not a prized
   patch or a fruit tree). See [vegetable_patches.md](vegetable_patches.md).
1. **Sensor calibration** — record raw ADC value in open air (driest), a
   glass of water (wettest), and two reference soil samples (bone-dry,
   saturated). Map to 0-100%. Cheap sensors vary ±10% between units —
   calibrate each individually.
2. **Valve bench test** — wire relay/MOSFET to a GPIO pin, click the valve
   open/closed from code, listen for the "thunk". Loop over a bucket: open →
   water flows, close → stops within seconds, no drip. Cycle 50 times, check
   fittings for leaks.
3. **Field install** — bury sensors at 15-20cm depth (root zone), spaced
   across the bed, avoiding direct mulch contact (reads artificially wet).
   Splice in the valve with the manual bypass in parallel. Mount electronics
   in an IP65 enclosure on a stake ≥30cm off the ground, away from spray.
4. **"Training wheels" mode (1-2 weeks)** — do not let it water
   automatically yet. Field node sends readings to the gateway/WiFi;
   gateway sends a Telegram message: "Bed 1 at 28%, recommend watering.
   Reply YES to water for 5 min." Build trust in sensor readings vs.
   eyes/fingers before automating.
5. **Autonomous with safeguards (ongoing)** — move to: if avg moisture < X%
   AND last watering > Y hours ago, open valve for Z minutes. **Mandatory
   safety logic** before leaving unattended:
   - Max total watering time per 24h (hard cap — sensor failure can't flood
     the bed).
   - Min interval between waterings (prevents oscillation from an erratic
     sensor).
   - Watchdog: valve "open" for > N minutes → force close.
   - Flow sensor confirmation (if installed): valve opened but no flow →
     alarm.
   - Gateway loses contact with field node for > 1 hour → alarm.
   - Run 2-3 weeks fully monitored before trusting it unattended.
6. **Scale** — once one zone runs reliably, replicate. One Heltec can drive
   multiple valves and read multiple sensor clusters per *area*, not per bed.

### Layer 3 — Decision layer (weather-data-driven advisory)
Goal: reason over **actual accumulated local weather data** (rainfall, temp,
dry-stretch length) instead of generic seasonal heuristics ("water 2-3x/week
in summer", "check by feel"). Would eventually cover fruit trees, mushroom
logs, avocado tents, vegetable patches — anywhere watering calls currently
rely on rules of thumb, not just the automated zone(s) from Layer 2.

This layer only becomes worth building once Layer 2 has real sensor data to
correlate weather against — otherwise it's advisory with nothing to
validate itself against. Sequence it last.

- **Advisory-only first**: a weekly "water / hold off" call surfaced during
  check-ins, not valve automation — property-wide rather than one bed.
- **Later**, if it proves reliable, it could feed thresholds into Layer 2's
  autonomous logic (e.g. suppress a scheduled watering because rain is
  forecast) rather than staying purely advisory.
- To scope when picked up: data source (manual rain-gauge log vs. weather
  API pull persisted to disk vs. the sensors already in Layer 2/LoRa track),
  file format/location for accumulated data, how the suggestion surfaces
  during weekly check-ins.
- Raised 2026-06-06, restated 2026-07-04 after a concrete case (winter
  watering call for durazno/ciruela) showed the gap between generic advice
  and what accumulated rain data could actually tell us.

## Recommended build order
1. **Layer 1 prototype** on one tap — fastest path to "something working",
   no LoRa gateway or baseline questions required. Proves phone → valve.
2. **Layer 2** on the same hardware/zone — add moisture sensor(s), run
   "training wheels" mode, then automate with safeguards.
3. **Add LoRa radio + gateway** only if a later zone is genuinely outside
   WiFi range (property-wide rollout) — reuses the gateway work planned for
   [frost_alarm.md](lora/frost_alarm.md) / [well_monitor.md](lora/well_monitor.md).
4. **Layer 3** once Layer 2 has a season of real data to reason over.

## Validation questions (deduped)
1. **Which tap/zone** is the guinea pig, and what's planted there now /
   is it low-stakes to get wrong for a few weeks? (See
   [vegetable_patches.md](vegetable_patches.md).)
2. **Tap type**: quarter-turn ball valve (lever handle) or multi-turn gate
   valve (screw stem)? Decides whether the servo path (A) is viable.
3. **Current watering method** at that zone: hose by hand, drip line, soaker
   hose, sprinkler? (Affects how the valve splices in.)
4. **Water source**: directly off the pump (on-demand pressure), pressure
   tank, or gravity/header tank? (Affects valve choice.)
5. **Approximate pressure** at that point, if known (or "feels weak / normal
   / strong").
6. **Power nearby**: mains outlet within reach, or fully off-grid?
7. **WiFi signal** at that spot — usable, weak, none? (Determines whether
   Layer 2 can skip LoRa entirely for this zone.)
8. **Mechanical access**: can a bracket clamp onto the handle without
   damaging the tap or blocking a fitting/meter next to it? (Servo path
   only.)
9. **Soil type at that bed**: sandy, loam, clay, mixed? (Determines
   moisture thresholds and dry-down speed — Layer 2.)
10. **Risk appetite**: comfortable moving to autonomous after a couple weeks
    of training-wheels, or prefer "alert me, I'll decide" indefinitely?
11. **Travel pattern**: how long are the longest unsupervised absences this
    would need to cover?

## Open design questions to revisit
- Whether "partial open" (metered flow, not just on/off) is wanted for
  Layer 1, or on/off is enough. Partial-open needs positional feedback
  (potentiometer servo or geared motor with encoder) — a bigger step.
- Whether to add rainfall lockout (don't water if it rained / is forecast to
  rain) to Layer 2 before Layer 3 exists — easy if a BME280 is already on
  site (frost alarm) or the gateway pulls a weather API directly.
- Whether the gateway/controller should expose a simple "water now for
  10 min" web/Telegram command for manual override, independent of the
  automated logic.

## Cross-references
- LoRa initiative (shares gateway/hardware family if Layer 2 needs LoRa):
  [lora/frost_alarm.md](lora/frost_alarm.md), [lora/well_monitor.md](lora/well_monitor.md),
  [lora/lora_pending_questions.md](lora/lora_pending_questions.md)
- Candidate zones: [vegetable_patches.md](vegetable_patches.md)
- Soil chemistry context: [soil_ph.md (memory)](../../Users/lucia/.claude/projects/C--Lucho-rancho-IA/memory/soil_ph.md)
