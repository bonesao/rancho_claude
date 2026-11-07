# Frost Alarm + Microclimate Logger

LoRa-based remote sensor in the orchard that warns you the evening before a frost night and builds a long-term local temperature/humidity dataset.

## Why this one first
- **Pure sensing, no actuators** — a bug can't flood a bed or kill a tree, only miss a reading. Lowest-stakes way to learn the LoRa + sensor + gateway pipeline end-to-end.
- High value: Loma Verde gets a handful of brutal radiative-frost nights Jun–Aug; knowing the night before lets you act (irrigate just before dawn, cover, frost smoke).
- Builds a permanent microclimate record that's *yours*, not regional.

## Hardware to buy

### Already have
- Heltec Wireless Stick × 2 (one field node, one house gateway)

### Sensors (~USD 15-20 total)
- **BME280** breakout (I2C) — temp + humidity + barometric pressure. Pressure trend and dew point both matter for frost prediction. **Get the genuine 3.3V version**, not the cheaper BMP280 (no humidity).
- **DS18B20 waterproof probe** with 1-2 m cable — for ground/canopy-level temp, which matters more for plants than air temp 1.5 m up.
- 4.7 kΩ resistor for the DS18B20 1-wire pullup.

### Enclosure & mounting (~USD 15-25)
- IP65 plastic junction box, ~10×10×7 cm, for the Heltec + battery.
- **Solar radiation shield** for the BME280 — non-negotiable, direct sun gives bogus readings 10+ °C off. Options:
  - Buy a small Stevenson screen / multi-plate shield (~USD 10).
  - Or 3D-print one (Thingiverse has dozens).
  - Or improvise: stack 4-5 white plastic flowerpot saucers with spacers between them.
- Cable glands (PG7) for waterproof entries into the box.
- Wooden stake or metal post for mounting at ~1.5 m height.

### Power (~USD 10-15)
- 18650 Li-Po cell, 2500-3000 mAh, with holder. The Heltec has built-in charging.
- **5 V / 2 W solar panel** with a barrel/JST connector matching the Heltec's input.
- Optional: CN3791 MPPT module if you want better solar charging than the onboard linear charger.

### LoRa antennas
- **Confirm frequency first** — Argentina uses **AU915 (915 MHz)**. The Heltec board comes in 433/868/915 variants; the antennas must match.
- Replace the stub antennas with proper 915 MHz half-wave dipoles or short whip antennas with a small ground plane. ~USD 5-10 each. The stub antennas work but give you maybe 1/3 the range.

### Misc
- Silicone wire (more flexible than PVC in cold), heat shrink, solder.
- Small buzzer + LED at the gateway if you want a local "WAKE UP, FROST INCOMING" alert at the house.

## Implementation roadmap

### Phase 1 — Bench (1-2 evenings)
1. Solder headers on both Heltec boards if needed.
2. Install Arduino IDE + ESP32 board package + Heltec library (or use PlatformIO).
3. Flash the basic OLED + LoRa "ping-pong" example. Confirm packets fly between the two boards across the room. OLED shows packet count.
4. Walk one board around the property. Note where the link breaks (this informs antenna upgrades).

### Phase 2 — Sensors (1 evening)
5. Wire BME280 to the field node via I2C (SDA/SCL pins).
6. Wire DS18B20 via 1-wire with the 4.7 kΩ pullup.
7. Read both sensors over serial. Sanity-check vs. a known thermometer.

### Phase 3 — Power management (1 evening)
8. Enable ESP32 deep sleep: wake every 5 min, read sensors, transmit, sleep again.
9. Measure idle current draw (should be sub-mA in deep sleep, ~80 mA briefly during TX). Estimate battery life: a 2500 mAh cell at 5-min intervals should last weeks without solar.

### Phase 4 — Outdoor install (half a day)
10. Mount the BME280 in its radiation shield, separate from the main enclosure (the enclosure heats up in sun).
11. Stake the DS18B20 probe at canopy/ground level near a representative fruit tree.
12. Run a wire to the main enclosure (Heltec + battery + solar input).
13. Position solar panel facing north (we're in the southern hemisphere).

### Phase 5 — Gateway + alerts (1-2 evenings)
14. Gateway board: connect to home WiFi, listen for LoRa packets, push them somewhere.
15. Pick a notification path:
    - **Telegram bot** — simplest, free, push notifications to your phone, easy to set up.
    - **Home Assistant** if you want a dashboard and history graphs.
    - **MQTT + free broker** (HiveMQ) if you want to plug into other things later.
16. Alarm logic:
    - **Simple v1**: temp < 3 °C → warning, temp < 1 °C → alarm.
    - **Smarter v2**: after sunset on a clear night (low humidity + stable/rising pressure), if temp is dropping > 1 °C per hour, predict frost by 4 AM. Send "FROST LIKELY TONIGHT" before bedtime.

### Phase 6 — Tune over the season
17. Log everything. After one winter you'll know your microclimate's actual frost threshold vs. forecast.

## Validation questions

Please answer these so I can refine the spec before you order parts:

1. **Tree layout**: are the fruit trees in one cluster, or spread across the 2000 m²? (See [fruit_trees.md](fruit_trees.md) — do you want one sensor for the whole orchard, or are there distinct cold pockets?)
2. **Distance**: roughly how far from the house WiFi router will the orchard node sit?
3. **Existing infrastructure**: do you have a Raspberry Pi or any always-on computer at the house? (Affects gateway architecture — Pi opens up Home Assistant; without one, a Telegram bot running directly on the gateway ESP32 is simpler.)
4. **Alert channel preference**: Telegram, email, audible alarm at the house, all of the above?
5. **LoRa frequency**: what does the board / seller listing say — 433, 868, or 915 MHz? (If 915, perfect for AR. If 433 or 868, still works, just need matching antennas.)
6. **Data ambition**: do you want full historical logging (graphs, microclimate dataset), or just real-time alerts? Affects whether we need a database/Pi or just a Telegram bot.
7. **Workshop**: do you have a soldering iron, multimeter, and a comfortable place to work on small electronics?
8. **Budget ceiling** for this first project?

## Cross-references
- Companion projects sharing the gateway: [well_monitor.md](well_monitor.md), [../irrigation_control.md](../irrigation_control.md) (if it ends up needing LoRa)
- Trees being protected: [fruit_trees.md](fruit_trees.md)
