"""Render the standard reference views of the v6 coop into models/renders_v6/.
Run in Blender via: python tools/bl.py run models/render_views_v5.py
Rebuild the model first (chicken_coop_model_v6.py) if the design changed.
Temporarily poses the openable parts (window, nest lid, wheel arms, ramp) and restores them."""
import math
import os
import bpy
from mathutils import Vector

OUT = r"C:\Lucho\rancho\IA\chicken_coop\models\renders_v6"
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
RAMP_UP = math.asin((0.4 - 0.15) / 1.1)          # keep in sync with RAMP_FOOT_UP in the model

# name: (camera location, look-at target, pose)
VIEWS = {
    "01_overview_front": ((-3.8, -6.2, 3.4), (2.0, 1.0, 0.8), None),
    "02_overview_back": ((7.5, 7.0, 3.6), (1.8, 1.0, 0.7), None),
    "03_house_west_end": ((-3.2, -2.6, 1.8), (0.0, 1.0, 1.0), None),
    "04_window_and_nest_lid_open": ((-3.2, -2.6, 1.8), (0.0, 1.0, 1.0), "open"),
    "05_roof_from_above": ((-2.0, -2.5, 4.2), (1.0, 1.0, 1.6), None),
    "06_handle_east_end": ((6.6, 1.0, 1.5), (4.0, 1.0, 0.8), None),
    "07_crank_rest_side": ((0.5, -3.2, 0.65), (0.5, 0.0, 0.6), None),
    "08_crank_locked_side": ((0.5, -3.2, 0.65), (0.5, 0.0, 0.6), "locked"),
    "08b_crank_locked_overview": ((-3.8, -6.2, 3.4), (2.0, 1.0, 0.8), "locked"),
    "08c_lock_pin_engaged": ((2.0, -1.2, 1.25), (1.1, 0.0, 0.9), "locked"),
    "08d_lock_pin_retracted": ((2.0, -1.2, 1.25), (1.0, 0.0, 0.9), None),
    "08e_lifted_side": ((0.5, -3.2, 0.65), (0.5, 0.0, 0.6), "lifted"),
    "08f_lifted_overview": ((-3.8, -6.2, 2.4), (2.0, 1.0, 0.8), "lifted"),
    "09_house_floor_structure": ((-2.8, -3.2, 1.9), (0.5, 1.0, 0.45), "no_shell"),
    "09b_shaft_under_house": ((2.6, 1.0, 0.45), (0.7, 1.0, 0.2), None),
    "10_ramp_parked": ((3.6, -2.2, 1.3), (2.2, 0.5, 0.5), None),
    "11_ramp_hoisted": ((3.6, -2.2, 1.3), (2.2, 0.5, 0.5), "ramp_up"),
    "12_back_door_closed": ((3.6, 5.6, 1.4), (2.9, 2.0, 0.7), None),
    "13_back_door_open": ((3.6, 5.6, 1.4), (2.9, 2.0, 0.7), "door_open"),
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
        h.rotation_euler.z = math.radians(80)
    if pose in ("locked", "lifted"):
        h = O["crank_hinge"]
        undo.append((h, "rotation_euler", h.rotation_euler.copy()))
        h.rotation_euler.y = math.radians(100)
        for n in ("lock_pin", "lock_grip"):          # engage the pin into the post
            o = O[n]
            undo.append((o, "location", o.location.copy()))
            o.location.y += 0.10
    if pose == "lifted":
        # the wheels stay on the ground; the whole coop (everything not parented) rises by the crank drop
        DROP = 0.12 * math.cos(math.radians(10))     # keep in sync with CRANK_E / CRANK_OVER in the model
        for cn in ("Coop_Frame", "Coop_Mesh", "Coop_House_Shell", "Coop_House_Interior", "Coop_Extras"):
            for o in bpy.data.collections[cn].objects:
                if o.parent is None:
                    undo.append((o, "location", o.location.copy()))
                    o.location.z += DROP
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
