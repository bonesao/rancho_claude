"""Render the standard reference views of the v2 coop into models/renders_v2/.
Run in Blender via: python tools/bl.py run models/render_views_v2.py
Rebuild the model first (chicken_coop_model_v2.py) if the design changed.
Temporarily poses the openable parts (window, nest lid, wheel arms, ramp) and restores them."""
import math
import os
import bpy
from mathutils import Vector

OUT = r"C:\Lucho\rancho\IA\chicken_coop\models\renders_v2"
os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene
for eng in ("BLENDER_EEVEE", "BLENDER_EEVEE_NEXT", "BLENDER_WORKBENCH"):
    try:
        sc.render.engine = eng
        break
    except TypeError:
        pass
sc.render.resolution_x, sc.render.resolution_y = 1600, 900
cam = sc.camera
O = bpy.data.objects
SHELL = bpy.data.collections["Coop_House_Shell"]
RAMP_UP = math.asin((0.5 - 0.15) / 1.1)          # keep in sync with RAMP_FOOT_UP in the model

# name: (camera location, look-at target, pose)
VIEWS = {
    "01_overview_front": ((-3.8, -6.2, 3.4), (2.0, 1.0, 0.8), None),
    "02_overview_back": ((7.5, 7.0, 3.6), (1.8, 1.0, 0.7), None),
    "03_house_west_end": ((-3.2, -2.6, 1.8), (0.0, 1.0, 1.0), None),
    "04_window_and_nest_lid_open": ((-3.2, -2.6, 1.8), (0.0, 1.0, 1.0), "open"),
    "05_roof_from_above": ((-2.0, -2.5, 4.2), (1.0, 1.0, 1.6), None),
    "06_handle_east_end": ((6.6, 1.0, 1.5), (4.0, 1.0, 0.8), None),
    "07_wheel_arm_rest": ((1.6, -2.0, 0.9), (1.4, 0.0, 0.2), None),
    "08_wheel_arm_locked": ((1.6, -2.0, 0.9), (1.4, 0.0, 0.2), "locked"),
    "09_house_floor_structure": ((-2.8, -3.2, 1.9), (0.5, 1.0, 0.45), "no_shell"),
    "10_ramp_parked": ((3.6, -2.2, 1.3), (2.2, 0.5, 0.5), None),
    "11_ramp_hoisted": ((3.6, -2.2, 1.3), (2.2, 0.5, 0.5), "ramp_up"),
    "12_front_door_closed": ((3.4, -3.6, 1.4), (3.0, 0.0, 0.8), None),
    "13_front_door_open": ((3.4, -3.6, 1.4), (3.0, 0.0, 0.8), "door_open"),
}

for name, (loc, tgt, pose) in VIEWS.items():
    undo = []
    if pose == "open":
        for n, axis, deg in (("window_hinge", 2, 70), ("nest_lid_hinge", 1, 50)):
            o = O[n]
            undo.append((o, "rotation_euler", o.rotation_euler.copy()))
            e = o.rotation_euler.copy()
            e[axis] = math.radians(deg)
            o.rotation_euler = e
    if pose == "door_open":
        h = O["door_hinge"]
        undo.append((h, "rotation_euler", h.rotation_euler.copy()))
        h.rotation_euler.z = math.radians(-80)
    if pose == "locked":
        for side in ("front", "back"):
            h, blk = O[f"wheel_arm_hinge_{side}"], O[f"stop_block_{side}"]
            gap = blk.dimensions.z + 0.002
            undo.append((h, "rotation_euler", h.rotation_euler.copy()))
            undo.append((blk, "location", blk.location.copy()))
            h.rotation_euler.y = math.asin(0.06 / 0.30)
            blk.location.z -= 0.07 + gap - 0.001
    if pose == "no_shell":
        undo.append((SHELL, "hide_render", SHELL.hide_render))
        SHELL.hide_render = True
        for o in SHELL.objects:
            undo.append((o, "hide_render", o.hide_render))
            o.hide_render = True
    if pose == "ramp_up":
        h = O["ramp_hinge"]
        undo.append((h, "rotation_euler", h.rotation_euler.copy()))
        h.rotation_euler.y = RAMP_UP
        for n, hide in (("chain_hanging", True), ("carabiner_hanging", True),
                        ("chain_taut", False), ("carabiner_taut", False)):
            o = O[n]
            undo.append((o, "hide_render", o.hide_render))
            undo.append((o, "hide_viewport", o.hide_viewport))
            o.hide_render = o.hide_viewport = hide
    cam.location = loc
    cam.rotation_euler = (Vector(tgt) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    sc.render.filepath = OUT + "\\" + name + ".png"
    for attempt in range(4):        # Blender sometimes fails to save a still intermittently
        try:
            bpy.ops.render.render(write_still=True)
            break
        except RuntimeError:
            if attempt == 3:
                raise
    for o, attr, val in undo:
        setattr(o, attr, val)

cam.location = VIEWS["01_overview_front"][0]
cam.rotation_euler = (Vector(VIEWS["01_overview_front"][1]) - Vector(cam.location)).to_track_quat("-Z", "Y").to_euler()
print("rendered", len(VIEWS), "views to", OUT)
