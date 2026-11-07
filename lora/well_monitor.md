# Well + Pump Monitor

LoRa node at the well head that tracks water level and pump activity. Catches: pump running dry, hidden plumbing leaks (excessive cycling), seasonal aquifer drop.

## Why this matters
The well is the single piece of critical infrastructure on the homestead with **zero observability** today. A failed pump or unnoticed leak could go for days before you spot it. Even the *baseline data* (normal cycling pattern, normal static water level) is valuable — you can't recognize abnormal until you know normal.

## Hardware to buy

### Already have
- Heltec Wireless Stick × 2. **Note**: if you also build [frost_alarm.md](frost_alarm.md), the gateway can be shared — one Heltec at the house listens to many field nodes. So you may not actually need both for both projects.

### Water level sensor (~USD 10-15)
- **JSN-SR04T** waterproof ultrasonic sensor (the SR04 variant with a sealed transducer on a cable). Measures distance from sensor down to water surface. Useful range ~25 cm to ~4 m.
  - The bare sensor + a separate transducer-on-cable version is best — electronics stay dry, only the transducer head sits in the well casing.
- Alternative (more accurate but harder to install): submersible pressure transducer at the bottom of the well. Skip unless you really need centimeter precision.

### Pump current sensor (~USD 5-10)
- **SCT-013-030** split-core current transformer (CT clamp), 30 A range. Non-invasive — just clips around the pump's hot wire, no rewiring or breaking the circuit. **Much safer than ACS712 for an inline measurement on a 220 V pump.**
- Burden resistor + voltage divider circuit if you get the bare-output CT. Or buy the "voltage output" version with built-in burden — plugs straight into an ESP32 analog pin.

### Enclosure & wiring (~USD 15-20)
- IP65 plastic box near the well head, ~12×12×8 cm.
- Cable glands for the ultrasonic cable and the CT clamp wire.
- Mounting bracket for the ultrasonic transducer at the top of the well casing, pointing straight down at the water.

### Power
- **Strongly prefer mains-powered** here — there's grid at the pump anyway, and continuous logging is more useful than battery-conserving sleep cycles. A simple 5 V USB wall adapter into the Heltec's micro-USB. No battery hassle, no solar panel.
- If the well head is far from any outlet and you don't want to run cable: 18650 + small solar panel, same setup as [frost_alarm.md](frost_alarm.md).

### LoRa antenna
- Same upgrade as the frost alarm: matching-frequency dipole or whip, especially if the well is on the far side of the property.

## Implementation roadmap

### Phase 1 — Survey (30 minutes, no electronics yet)
1. Measure the well:
   - Casing inner diameter.
   - Depth from top of casing to current water surface (drop a weighted string).
   - Depth from top of casing to bottom (same method).
   - Note the static level (pump off, settled) vs. recovery level after heavy pumping.
2. Identify the pump:
   - Submersible (inside the well) or jet/surface pump (at ground level)?
   - Power rating (HP / W) — should be on a nameplate.
   - Single circuit, or shared? Where's the on/off switch?
3. Find the pressure tank if one exists. Note its size.

### Phase 2 — Bench (1-2 evenings)
4. Wire the JSN-SR04T to the field Heltec. Test in a bucket of water — confirm distance readings are stable to ±1 cm.
5. Wire the SCT-013 around an extension cord powering a known load (kettle, hair dryer). Calibrate the ADC reading → amps → watts. Do this **before** going anywhere near the pump.
6. Combine: read both sensors, transmit a packet every 30 seconds.

### Phase 3 — Install at well (half a day)
7. Mount the ultrasonic transducer at the top of the well casing, aimed straight down. Mount the electronics enclosure nearby in a dry, shaded spot.
8. Clip the CT around the pump's hot wire (not both wires — just the live conductor). No electrical work needed if the wiring is already accessible.
9. Power up. Verify the field node transmits and the gateway receives.

### Phase 4 — Calibration (a few days)
10. Tape-measure the actual water depth a few times, compare against the ultrasonic reading. Apply offset/scale correction in software.
11. Watch the pump current trace during normal use. Note: idle current, running current, startup spike.

### Phase 5 — Alarms (1 evening)
Once you have a week of baseline data:
- **Pump running > N minutes continuously** → dry-well risk, alarm.
- **Pump cycling > N times/hour** → likely plumbing leak somewhere downstream.
- **Water level dropping > X cm/day** with no proportional pump use → aquifer issue.
- **Pump trying to start but no current draw** → tripped breaker / failure.

### Phase 6 — Long-term log
Plot water level vs. season. After a year you'll know your aquifer's normal swing and what "dry summer" actually looks like on this property.

## Validation questions

1. **Well type**: drilled (narrow casing, deep), bored (wider, ~30-60 cm), or hand-dug (large diameter, shallow)?
2. **Approximate depth** to water and to bottom? Even a rough number helps choose the right ultrasonic sensor (the JSN-SR04T tops out around 4-5 m; deeper wells need a pressure sensor).
3. **Pump type**: submersible inside the well, or jet pump at the surface? Power rating?
4. **Pressure tank**: yes/no? Approximate size? (Affects how often the pump cycles for a given household demand.)
5. **Distance from well to house WiFi router**? Is there line-of-sight, or are there trees/buildings in between?
6. **Power at the well head**: is there a working outlet, or only the pump's dedicated circuit?
7. **Pump wiring access**: is the hot wire to the pump exposed and clamp-accessible anywhere (e.g. in the breaker box, at a junction box, at the pump switch), or fully enclosed in conduit?
8. **What's the worst failure you've had with the well historically?** Tells me what to prioritize alerting on.
9. **Do you also want flow measurement** (litres pumped) — useful but adds a more expensive sensor and inline plumbing?

## Cross-references
- Sibling project sharing hardware/gateway: [frost_alarm.md](frost_alarm.md)
- Downstream consumer of well water: [../irrigation_control.md](../irrigation_control.md)
