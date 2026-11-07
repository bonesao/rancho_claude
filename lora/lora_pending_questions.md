# LoRa IoT Initiative — Pending Baseline Questions

**Status as of 2026-05-30**: Three project specs drafted, shopping lists and roadmaps in place. Blocked on the answers below before ordering hardware or refining specs further.

**How to use this file**: fill in answers under each question (rough is fine). When done, the next session will consolidate them into shared memory, prune redundant questions out of the three project files, and decide which build to start first.

## Confirmed so far
- **Hardware owned**: 2 × Heltec Wireless Stick (ESP32 + LoRa + 0.49" OLED + Li-Po).
- **LoRa frequency variant**: 915 MHz / US-AU915 band (label said 865-928 MHz, which is the HF band). Compatible with Argentina. Firmware will be configured for 915 MHz.
- **Sourcing of boards**: bought in China (no further provenance).

## Project specs awaiting refinement
- [frost_alarm.md](frost_alarm.md) — orchard sensor + frost prediction (recommended first build, pure sensing)
- [well_monitor.md](well_monitor.md) — well water level + pump current

Note: the soil-moisture irrigation actuator project moved out of this LoRa
track and merged with the WiFi valve prototype — see
[../irrigation_control.md](../irrigation_control.md) (Layer 2). It only
comes back to needing LoRa/this gateway if a target zone is outside WiFi
range.

---

## Cross-project questions (answer here)

### Property & link planning
**Q1. Rough distances** from the house WiFi router to: orchard, well head, candidate vegetable beds. Pacing is fine.
> *Answer:*

**Q2. Line of sight** on those paths — open ground, or through trees / buildings / sheds?
> *Answer:*

**Q3. WiFi coverage map** — where on the property does your WiFi reach with usable signal? (Constrains where the gateway can live.)
> *Answer:*

### Gateway & notifications
**Q4. Always-on computer at the house?** Options:
- None → gateway is a Heltec on USB, sends alerts directly via Telegram. Simplest.
- Raspberry Pi / Pi Zero 2 → Home Assistant or Node-RED, real dashboards + history.
- Old laptop / NUC → same as Pi, more power than needed.

> *Answer:*

**Q5. Preferred alert channel(s)** — Telegram bot, email, audible buzzer at house, dashboard, combination?
> *Answer:*

### Workshop & skill
**Q6. Electronics gear already on hand** — soldering iron, multimeter, breadboard, jumper wires, USB-C cable for the Heltec, helping hands, etc.?
> *Answer:*

**Q7. ESP32 / Arduino prior experience** — never, hobby-level, comfortable?
> *Answer:*

**Q8. Existing smart-home / MQTT / Home Assistant setup** even if abandoned?
> *Answer:*

### Logistics
**Q9. Electronics sourcing in AR** — MercadoLibre, AliExpress shipping, travel/family-brings-it? Determines lead times.
> *Answer:*

**Q10. Timing & sequencing** — batch-order all three projects in one go, or build-one-then-decide? Rough timeline for first deployment (this weekend? this winter?).
> *Answer:*

### Small but worth settling once
**Q11. Timestamp convention** for logs — local AR time, or UTC?
> *Answer:*

**Q12. Budget ceiling** for the IoT track overall (ballpark, keeps me from over-speccing)?
> *Answer:*

---

## After these are answered
The next session should:
1. Consolidate confirmed shared decisions into a single shared-baseline memory note.
2. Remove the now-answered questions from the three project files (they currently each repeat some of the above in their own validation sections).
3. Recommend which project to start first based on the answers (default: frost alarm, but may shift).
4. Produce a finalized shopping list ready to order.
