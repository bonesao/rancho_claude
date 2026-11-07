"""Close-up renders of the v5 wheel mechanism (shaft, crank plate, wheel, handle, pin) with everything
else hidden, into models/renders_v5/detail/. Also writes labels.json (screen positions of key parts,
0..1 from top-left) for label_detail_v5.py. Run: python tools/bl.py run models/render_detail_v5.py
Temporarily poses the crank (parked / locked) and restores it."""
import json
import math
import os
import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

OUT = r"C:\Lucho\rancho\IA\chicken_coop\models\renders_v5\detail"
os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene
sc.render.resolution_x, sc.render.resolution_y = 1600, 1000
cam = sc.camera
O = bpy.data.objects
KEEP = ("axle_shaft", "crank_plate", "stub_axle", "tire", "rim", "axle_washer", "axle_nut", "shaft_collar",
        "shaft_post", "deadlift_handle", "lock_pin", "lock_grip", "handle_stop", "house_floor_rail",
        "rail_bot_", "house_post_", "ground")
CRANK_E, CRANK_OVER, SHAFT_Z = 0.12, 10.0, 0.15      # keep in sync with the model
DROP = CRANK_E * math.cos(math.radians(CRANK_OVER))
HINGE = O["crank_hinge"]
HINGE_LOC0 = HINGE.location.copy()
SX = HINGE_LOC0.x                                     # shaft x
# label -> object name (static/rotating object origin) or a point (x, y, z) in the PARKED frame that
# rotates with the crank hinge
ANCHORS = {
    "shaft (32 mm bar)": (SX, -0.06, SHAFT_Z),
    "shaft collar": (SX, -0.006, SHAFT_Z),
    "crank plate": (SX + CRANK_E * 0.55, -0.014, SHAFT_Z),
    "wheel axle (12 cm off the shaft)": (SX + CRANK_E, -0.16, SHAFT_Z),
    "wheel": "rim_front",
    "post with sleeve": "shaft_post_front",
    "handle": "deadlift_handle",
    "lock pin + grip": "lock_grip",
    "stop block": "handle_stop",
}
# name: (cam loc, target, pose, tires hidden, {label: (dx, dy) text offset in px})
VIEWS = {
    "D1_closeup_parked_wheel": ((1.3, -0.9, 0.45), (0.85, -0.05, 0.17), "parked", False, {
        "wheel": (180, 150), "post with sleeve": (-360, -120), "handle": (-330, 200)}),
    "D2_closeup_parked_crank": ((1.3, -0.9, 0.45), (0.85, -0.05, 0.17), "parked", True, {
        "shaft (32 mm bar)": (-400, 110), "crank plate": (-80, -230),
        "wheel axle (12 cm off the shaft)": (120, 190), "post with sleeve": (-380, -170)}),
    "D3_closeup_locked_crank": ((1.3, -0.9, 0.45), (0.85, -0.05, 0.17), "locked", True, {
        "shaft (32 mm bar)": (-400, 110), "crank plate": (170, -60),
        "wheel axle (12 cm off the shaft)": (120, 190), "post with sleeve": (-380, -170)}),
    "D4_closeup_locked_wheel": ((1.3, -0.9, 0.45), (0.85, -0.05, 0.17), "locked", False, {
        "wheel": (200, 160), "handle": (-380, -120)}),
    "D5_whole_mechanism_parked": ((-1.7, -2.0, 1.4), (0.8, 1.0, 0.2), "parked", False, {}),
    "D6_whole_mechanism_locked": ((-1.7, -2.0, 1.4), (0.8, 1.0, 0.2), "locked", False, {}),
    "D7_handle_pin_post_locked": ((1.65, -1.3, 1.2), (1.03, 0.0, 0.9), "locked", False, {
        "lock pin + grip": (-300, -150), "handle": (-380, 120), "stop block": (200, 160)}),
}
labels_out = {}
for name, (loc, tgt, pose, notires, labs) in VIEWS.items():
    undo = []
    for o in bpy.data.objects:
        if o.type in ("LIGHT", "CAMERA", "EMPTY"):
            continue
        keep = o.name.startswith(KEEP) and not o.hide_render
        if notires and o.name.startswith(("tire", "rim")):
            keep = False
        if not keep:
            undo.append((o, "hide_render", o.hide_render))
            o.hide_render = True
    if pose == "locked":
        undo.append((HINGE, "rotation_euler", HINGE.rotation_euler.copy()))
        HINGE.rotation_euler.y = math.radians(90 + CRANK_OVER)
        for n in ("lock_pin", "lock_grip"):
            o = O[n]
            undo.append((o, "location", o.location.copy()))
            o.location.y += 0.06
        for o in bpy.data.objects:                     # wheels stay on the ground: the coop rises
            if o.parent is None and o.users_collection and o.users_collection[0].name != "Coop_Env" and o.type != "CAMERA":
                undo.append((o, "location", o.location.copy()))
                o.location.z += DROP
    bpy.context.view_layer.update()
    cam.location = loc
    cam.rotation_euler = (Vector(tgt) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    bpy.context.view_layer.update()
    pts = {}
    for lab in labs:
        a_ = ANCHORS[lab]
        w = None
        if isinstance(a_, str):
            w = O[a_].matrix_world.translation
        else:
            # hinge matrix = T(loc) R; parked-frame point p -> loc + R (p - hinge rest location)
            rest = Vector((SX, HINGE_LOC0.y, SHAFT_Z))
            w = HINGE.matrix_world @ (Vector(a_) - rest)
        p = world_to_camera_view(sc, cam, w)
        pts[lab] = [p.x, 1 - p.y, labs[lab][0], labs[lab][1]]
    labels_out[name] = pts
    sc.render.filepath = OUT + "\\" + name + ".png"
    for attempt in range(4):
        try:
            bpy.ops.render.render(write_still=True)
            break
        except RuntimeError:
            if attempt == 3:
                raise
    for o, attr, val in undo:
        setattr(o, attr, val)
cam.location = (-3.8, -6.2, 3.4)
cam.rotation_euler = (Vector((2.0, 1.0, 0.8)) - cam.location).to_track_quat("-Z", "Y").to_euler()
json.dump(labels_out, open(OUT + "\labels.json", "w"), indent=1)
print("rendered", len(VIEWS), "detail views to", OUT)
