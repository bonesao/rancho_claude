"""Chicken coop v4 - parametric Blender build (Blender 5.x).

v4 = v3 with the foot-lever wheel arms replaced by L-shaped bell-crank levers: pivot at the house
end corner, horizontal leg carries the wheel (hub near the west end), vertical leg is pushed by
hand toward the run to drop the wheel and raise the house end. v1-v3 are frozen; this script
writes chicken_coop_v4.blend.

v3 = v2 layout (house = first, full-width 1 m section with a gable roof; mesh run = remaining 3 m)
but with HEXAGONAL mesh (code 3264: 3/4", wire N°21 0.81 mm, 1.5 m high, ~485 g/m2) instead of
welded mesh, NO anti-dig skirt, roof battens every ~50 cm against sagging, and a window
backing mesh. v1 and v2 are frozen (chicken_coop_model.py, chicken_coop_model_v2.py and their
.blend files); this script writes chicken_coop_v4.blend.
Re-running is safe: it deletes and rebuilds the Coop_* collections.

Axes: X = 4 m length (house at x=0, west), Y = 2 m width (front at y=0, back at y=W), Z up.
Units: metres. Mesh is schematic (5 cm grid + wireframe modifier), NOT the real 3/4" hexagonal weave.
"""
import math
import bmesh
import bpy
from mathutils import Vector

# ---------------- PARAMETERS (edit here) ----------------
L, W, H = 4.0, 2.0, 1.6            # whole coop: length, width, height of the run frame
T, D = 0.045, 0.07                 # pine 2"x3" real section (thin, deep)
HOUSE_L = 1.0                      # house section length (full width); run = L - HOUSE_L
XF = HOUSE_L                       # x of the house/run boundary
Z0 = 0.5                           # house floor height
PLY = 0.012                        # plywood thickness
FLOOR_T = 0.018                    # plywood floor thickness
WIN_W, WIN_H = 1.0, 0.85           # TODO: measure the real reused window
SILL = 0.05
WIN_Y0 = 0.12                      # window start along the west wall (y)
NEST_Y0, NEST_Y1 = 1.22, 1.92      # nest boxes along the west wall (y)
SLOPE = 0.36                       # gable roof rise/run (~20 deg)
OV, OV_W = 0.15, 0.10              # eave overhang (front/back) / west-end overhang
POP_W, POP_H, POP_Y = 0.30, 0.38, 0.25   # pop-hole size / offset from the front wall
RAMP_L, RAMP_W = 1.1, 0.30
DOOR_X0, DOOR_X1, DOOR_H = 2.54, 3.30, 1.45   # human door on the FRONT long side (hinge on the x=2.5 post)
WHEEL_R = 0.15                     # 30 cm pneumatic wheel
PIV_X, AXLE_X = 0.20, 0.55         # lever pivot / wheel hub (a = AXLE_X - PIV_X = 0.35 m)
# hub at 0.55 m: CG ~1.33 m (285 kg) -> handle lift ~60 kgf, wheels carry ~225 kgf (~110 each);
# pushing each lever (lock height 0.85 m above the pivot) takes ~45 kgf
LEVER_TOP = 1.00                   # top of the vertical (push) leg
LOCK_Z = 0.85                      # height of the lock ledge / wedge block
LEDGE_X1 = 0.13                    # stop ledge end face (wedge block sits between it and the lever)
WHEEL_TRAVEL = 0.06                # how far the wheel drops below the frame when locked
WHEEL_LOCKED = False               # True: levers pushed, wedge blocks inserted
RAMP_LIFTED = False                # True: ramp hoisted by the chain (travel pose)
RAMP_FOOT_UP = 0.15                # ramp foot height above ground when hoisted
JOISTS_X = (0.33, 0.67)            # intermediate floor joists (plus the two end joists)
HOOK_X = 2.0                       # roof cross-member carrying the ramp-chain hook
MESH_STEP = 0.05                   # schematic mesh pitch (real: 3/4" hexagonal)
OUT_DIR = r"C:\Lucho\rancho\IA\chicken_coop\models"

HX0, HX1 = T, XF                   # house interior box: x range
HY0, HY1 = T, W - T                # house y range (full width, inside the frame rails)
EAVE = H                           # eaves flush with the run's top rails
HSPAN = HY1 - HY0
RIDGE = EAVE + (HSPAN / 2) * SLOPE
FLOOR_BOT = Z0 - FLOOR_T

COLLS = ["Coop_Frame", "Coop_Mesh", "Coop_House_Shell", "Coop_House_Interior",
         "Coop_Extras", "Coop_Env"]


# ---------------- helpers ----------------
def coll(name):
    c = bpy.data.collections.get(name)
    if c is None:
        c = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(c)
    return c


def clear():
    for n in COLLS:
        c = bpy.data.collections.get(n)
        if c:
            for o in list(c.objects):
                bpy.data.objects.remove(o, do_unlink=True)
    for n in ("Cube", "Light"):
        o = bpy.data.objects.get(n)
        if o:
            bpy.data.objects.remove(o, do_unlink=True)


def mat(name, rgb, metallic=0.0, rough=0.6, alpha=1.0):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = (*rgb, 1.0)
    b.inputs["Metallic"].default_value = metallic
    b.inputs["Roughness"].default_value = rough
    b.inputs["Alpha"].default_value = alpha
    if alpha < 1.0:
        try:
            m.surface_render_method = 'BLENDED'
        except Exception:
            m.blend_method = 'BLEND'
    return m


PINE = mat("Pine", (0.72, 0.52, 0.30), rough=0.7)
PLYW = mat("Plywood", (0.80, 0.66, 0.45), rough=0.7)
GALV = mat("GalvMesh", (0.65, 0.67, 0.70), metallic=0.9, rough=0.35)
CHAPA = mat("Chapa", (0.35, 0.42, 0.48), metallic=0.6, rough=0.4)
GLASS = mat("WindowSlats", (0.55, 0.70, 0.80), rough=0.3, alpha=0.6)
RUBBER = mat("Rubber", (0.03, 0.03, 0.03), rough=0.9)
STEEL = mat("Steel", (0.30, 0.30, 0.32), metallic=1.0, rough=0.4)
LITTER = mat("Litter", (0.78, 0.65, 0.35), rough=1.0)
GRASS = mat("Grass", (0.22, 0.38, 0.14), rough=1.0)
BLUE = mat("Waterer", (0.15, 0.35, 0.75), rough=0.4)
RED = mat("Feeder", (0.70, 0.18, 0.12), rough=0.5)


def _finish(bm, name, material, c, loc=(0, 0, 0), rot=(0, 0, 0), parent=None):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    ob.location = loc
    ob.rotation_euler = [math.radians(r) for r in rot]
    if material:
        ob.data.materials.append(material)
    c.objects.link(ob)
    if parent:
        ob.parent = parent
    return ob


def box(name, center, size, material, c, rot=(0, 0, 0), parent=None):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x *= size[0]
        v.co.y *= size[1]
        v.co.z *= size[2]
    return _finish(bm, name, material, c, center, rot, parent)


def bounds(name, x0, x1, y0, y1, z0, z1, material, c):
    return box(name, ((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2),
               (x1 - x0, y1 - y0, z1 - z0), material, c)


def cyl(name, center, r, depth, axis, material, c, seg=24):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=seg, radius1=r,
                          radius2=r, depth=depth)
    rot = {"Z": (0, 0, 0), "Y": (90, 0, 0), "X": (0, 90, 0)}[axis]
    return _finish(bm, name, material, c, center, rot)


def prism_yz(name, pts, x0, x1, material, c):
    """Polygon in (y, z) extruded along x from x0 to x1."""
    bm = bmesh.new()
    f = bm.faces.new([bm.verts.new((x0, y, z)) for y, z in pts])
    ext = bmesh.ops.extrude_face_region(bm, geom=[f])
    vs = [g for g in ext["geom"] if isinstance(g, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, vec=(x1 - x0, 0, 0), verts=vs)
    bmesh.ops.recalc_face_normals(bm, faces=list(bm.faces))
    return _finish(bm, name, material, c)


def cut(ob, center, size):
    """Boolean-subtract a hidden box (modifier left live, so it stays editable)."""
    cutter = box(ob.name + "_cutter" + str(len(ob.modifiers)), center, size, None,
                 ob.users_collection[0])
    cutter.hide_viewport = True
    cutter.hide_render = True
    m = ob.modifiers.new("cut", "BOOLEAN")
    m.object = cutter
    m.operation = "DIFFERENCE"


def hinge(name, loc, children, c):
    """Empty at the hinge point; children keep their world pose but now rotate with it."""
    from mathutils import Matrix
    h = bpy.data.objects.new(name, None)
    h.empty_display_type = "ARROWS"
    h.empty_display_size = 0.12
    h.location = loc
    c.objects.link(h)
    for ch in children:
        ch.parent = h
        ch.matrix_parent_inverse = Matrix.Translation(-Vector(loc))
    return h


def mesh_panel(name, plane, center, w, h):
    """Schematic welded-mesh sheet: grid + wireframe modifier.
    plane: 'XZ' (front/back wall), 'YZ' (end wall), 'XY' (roof/skirt)."""
    nx, ny = max(1, round(w / MESH_STEP)), max(1, round(h / MESH_STEP))
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=nx, y_segments=ny, size=1.0)
    xs_ = [v.co.x for v in bm.verts]
    ys_ = [v.co.y for v in bm.verts]
    sx, sy = w / (max(xs_) - min(xs_)), h / (max(ys_) - min(ys_))
    for v in bm.verts:
        v.co.x *= sx
        v.co.y *= sy
    rot = {"XZ": (90, 0, 0), "YZ": (90, 0, 90), "XY": (0, 0, 0)}[plane]
    ob = _finish(bm, name, GALV, coll("Coop_Mesh"), center, rot)
    wf = ob.modifiers.new("wire", "WIREFRAME")
    wf.thickness = 0.002
    wf.offset = 0.0
    return ob


# ---------------- build ----------------
clear()
FR, MS, SH, IN, EX, EN = (coll(n) for n in COLLS)
RUN_L = L - XF

# --- frame: chassis rails along the whole length, run rails/posts/roof members ---
for yo_, tag in ((0, "front"), (W - T, "back")):
    bounds(f"rail_bot_{tag}", 0, L, yo_, yo_ + T, 0, D, PINE, FR)
    bounds(f"rail_top_{tag}", XF, L, yo_, yo_ + T, H - D, H, PINE, FR)
bounds("rail_bot_west", 0, T, T, W - T, 0, D, PINE, FR)
bounds("rail_bot_mid", XF - T, XF, T, W - T, 0, D, PINE, FR)       # under the house east wall
bounds("rail_bot_east", L - T, L, T, W - T, 0, D, PINE, FR)
bounds("rail_top_east", L - T, L, T, W - T, H - D, H, PINE, FR)
bounds("rail_top_mid", XF, XF + T, T, W - T, H - D, H, PINE, FR)   # run's west top rail
# run posts (the one at x=1.5 also takes the wheel-arm stop ledge)
for i, xp in enumerate((XF, 1.5, 2.5, L)):
    x0 = min(max(xp - D / 2, XF), L - D)
    bounds(f"post_front_{i}", x0, x0 + D, 0, T, D, H - D, PINE, FR)
    bounds(f"post_back_{i}", x0, x0 + D, W - T, W, D, H - D, PINE, FR)
for i, xp in enumerate((HOOK_X, 3.0)):
    bounds(f"roof_cross_{i}", xp - T / 2, xp + T / 2, T, W - T, H - T, H, PINE, FR)
bounds("roof_long", XF, L, W / 2 - T / 2, W / 2 + T / 2, H - T, H, PINE, FR)
# house corner posts (ground to eave); walls and floor hang off these
for tag, yo_ in (("front", 0), ("back", W - T)):
    for x0 in (0, XF - D):
        bounds(f"house_post_{tag}_{round(x0, 2)}", x0, x0 + D, yo_, yo_ + T, D, H, PINE, FR)
# front door: extra post on the latch side + lintel (the x=2.5 post is the hinge side)
bounds("door_post", DOOR_X1, DOOR_X1 + D, 0, T, D, H - D, PINE, FR)
bounds("door_lintel", DOOR_X0, DOOR_X1, 0, T, DOOR_H, DOOR_H + T, PINE, FR)
# east end: mid post (mesh support; the full-width handle bolts to the corner posts)
bounds("east_mid_post", L - T, L, W / 2 - T / 2, W / 2 + T / 2, D, H - D, PINE, FR)

# --- mesh sheets (outer faces) ---
e = 0.003
mesh_panel("mesh_front_run", "XZ", ((XF + L) / 2, -e, H / 2), RUN_L, H)
mesh_panel("mesh_back_run", "XZ", ((XF + L) / 2, W + e, H / 2), RUN_L, H)
mesh_panel("mesh_east", "YZ", (L + e, W / 2, H / 2), W, H)
mesh_panel("mesh_roof", "XY", ((XF + L) / 2, W / 2, H + e), RUN_L, W)
# under the raised house: sides closed, run side open (shade for the hens)
mesh_panel("mesh_front_under_house", "XZ", (XF / 2, -e, Z0 / 2), XF, Z0)
mesh_panel("mesh_back_under_house", "XZ", (XF / 2, W + e, Z0 / 2), XF, Z0)
mesh_panel("mesh_west_under_house", "YZ", (-e, W / 2, Z0 / 2), W, Z0)
# (no anti-dig skirt in v3: threat is gato montes / comadreja, not diggers, and the coop is a tractor)

# roof battens (1"x1") on top of the mesh roof, ~50 cm grid, so the hexagonal mesh does not sag
for k, bx in enumerate((1.5, 2.5, 3.5)):
    bounds(f"roof_batten_x{k}", bx - 0.0125, bx + 0.0125, T, W - T, H + 0.003, H + 0.028, PINE, FR)
for k, by in enumerate((0.5, 1.5)):
    bounds(f"roof_batten_y{k}", XF, L, by - 0.0125, by + 0.0125, H + 0.003, H + 0.028, PINE, FR)

# --- house floor: end joists + intermediate joists on edge, plywood on top ---
for k, jx in enumerate((HX0 / 2,) + JOISTS_X + (XF - T / 2,)):
    jw = T
    bounds(f"floor_joist_{k}", jx - jw / 2, jx + jw / 2, T, W - T, FLOOR_BOT - D, FLOOR_BOT, PINE, FR)
bounds("house_floor", HX0, HX1, HY0, HY1, FLOOR_BOT, Z0, PLYW, SH)

# --- house shell ---
bounds("house_front", HX0, HX1, HY0, HY0 + PLY, Z0, EAVE, PLYW, SH)
bounds("house_back", HX0, HX1, HY1 - PLY, HY1, Z0, EAVE, PLYW, SH)
gpts = [(HY0, Z0), (HY1, Z0), (HY1, EAVE), (W / 2, RIDGE), (HY0, EAVE)]
west = prism_yz("house_west", gpts, HX0, HX0 + PLY, PLYW, SH)
east = prism_yz("house_east", gpts, HX1 - PLY, HX1, PLYW, SH)
pop_yc = HY0 + POP_Y + POP_W / 2
cut(east, (HX1 - PLY / 2, pop_yc, Z0 + 0.04 + POP_H / 2), (0.2, POP_W, POP_H))
# window cut in the west wall
wy0, wy1 = WIN_Y0, WIN_Y0 + WIN_W
wz0, wz1 = Z0 + SILL, Z0 + SILL + WIN_H
xw = HX0 + PLY / 2
cut(west, (xw, (wy0 + wy1) / 2, (wz0 + wz1) / 2), (0.2, WIN_W, WIN_H))
# louvered window (closed): frame + slats, side-hinged on the low-y edge, swings outward (-x)
fw = 0.04
win_parts = [
    bounds("win_frame_a", xw - 0.02, xw + 0.02, wy0, wy0 + fw, wz0, wz1, PINE, SH),
    bounds("win_frame_b", xw - 0.02, xw + 0.02, wy1 - fw, wy1, wz0, wz1, PINE, SH),
    bounds("win_frame_t", xw - 0.02, xw + 0.02, wy0, wy1, wz1 - fw, wz1, PINE, SH),
    bounds("win_frame_bot", xw - 0.02, xw + 0.02, wy0, wy1, wz0, wz0 + fw, PINE, SH),
]
n_sl = 8
for i in range(n_sl):
    zc = wz0 + fw + (WIN_H - 2 * fw) * (i + 0.5) / n_sl
    win_parts.append(box(f"louver_{i}", (xw, (wy0 + wy1) / 2, zc), (0.012, WIN_W - 2 * fw, 0.13), GLASS, SH,
                         rot=(0, 35, 0)))
# rotate Z POSITIVE to swing the window out (hinge on the y-low edge)
hinge("window_hinge", (xw - 0.02, wy0, (wz0 + wz1) / 2), win_parts, SH)
# window backing mesh (fixed, inside the opening): the louver gaps are the night weak point
mesh_panel("window_backing", "YZ", (HX0 + PLY + 0.004, (wy0 + wy1) / 2, (wz0 + wz1) / 2), WIN_W, WIN_H)
# gable roof (ridge along x): plywood + chapa, overhang on both eaves and the west end
th = math.degrees(math.atan(SLOPE))
run = HSPAN / 2 + OV
ln = run / math.cos(math.radians(th))
zc = (RIDGE + (EAVE - OV * SLOPE)) / 2 + 0.0075
rx0, rx1 = -OV_W, XF
for s, nm in ((-1, "front"), (1, "back")):
    yc_ = W / 2 + s * (run / 2 - (HSPAN / 2 - HSPAN / 2))  # slab centre between ridge and eave tip
    yc_ = W / 2 + s * (run / 2)
    box(f"house_roof_ply_{nm}", ((rx0 + rx1) / 2, yc_, zc), (rx1 - rx0, ln, 0.015), PLYW, SH,
        rot=(-s * th, 0, 0))
    box(f"house_roof_chapa_{nm}", ((rx0 + rx1) / 2, yc_, zc + 0.0125), (rx1 - rx0, ln, 0.01), CHAPA, SH,
        rot=(-s * th, 0, 0))

# --- house interior ---
bounds("litter", HX0 + PLY, HX1 - PLY, HY0 + PLY, HY1 - PLY, Z0, Z0 + 0.03, LITTER, IN)
for i, (rx, rz) in enumerate(((0.40, Z0 + 0.50), (0.70, Z0 + 0.62))):
    cyl(f"roost_{i}", (rx, W / 2, rz), 0.02, HSPAN - 0.1, "Y", PINE, IN)

# --- nest boxes (outside the west wall, lids open from outside) ---
nz0, nz1, nx0 = Z0 + 0.05, Z0 + 0.35, -0.35
bounds("nest_floor", nx0, 0, NEST_Y0, NEST_Y1, nz0, nz0 + PLY, PLYW, EX)
bounds("nest_back", nx0, nx0 + PLY, NEST_Y0, NEST_Y1, nz0, nz1, PLYW, EX)
for i, y in enumerate((NEST_Y0, (NEST_Y0 + NEST_Y1) / 2 - PLY / 2, NEST_Y1 - PLY)):
    bounds(f"nest_div_{i}", nx0, 0, y, y + PLY, nz0, nz1, PLYW, EX)
nym = (NEST_Y0 + NEST_Y1) / 2
lid = box("nest_lid", (nx0 / 2, nym, nz1 + 0.02), (0.42, NEST_Y1 - NEST_Y0 + 0.04, 0.015), PLYW, EX,
          rot=(0, -12, 0))
# hinged on the house-side (high) edge: rotate Y POSITIVE to lift the outer edge
hinge("nest_lid_hinge", (0.0, nym, nz1 + 0.02 + 0.036), [lid], EX)

# --- ramp (hinged at the pop-hole sill; hoisted by a chain to a roof hook for travel) ---
ramp_deg = math.degrees(math.asin(Z0 / RAMP_L))
ramp_up_deg = math.degrees(math.asin((Z0 - RAMP_FOOT_UP) / RAMP_L))
ramp = bpy.data.objects.new("ramp_hinge", None)
ramp.empty_display_type = "ARROWS"
ramp.empty_display_size = 0.12
ramp.location = (HX1, pop_yc, Z0)
ramp.rotation_euler = (0, math.radians(ramp_up_deg if RAMP_LIFTED else ramp_deg), 0)
EX.objects.link(ramp)
box("ramp_board", (RAMP_L / 2, 0, -0.01), (RAMP_L, RAMP_W, 0.02), PLYW, EX, parent=ramp)
for i in range(1, int(RAMP_L / 0.15)):
    box(f"ramp_cleat_{i}", (i * 0.15, 0, 0.008), (0.02, RAMP_W, 0.016), PINE, EX, parent=ramp)
foot_eye_local = (RAMP_L - 0.03, 0, 0.012)
box("ramp_foot_eye", foot_eye_local, (0.03, 0.03, 0.02), STEEL, EX, parent=ramp)
HOOK = Vector((HOOK_X, pop_yc, H - T - 0.02))                       # under roof_cross_0
cyl("roof_hook", (HOOK.x, HOOK.y, HOOK.z + 0.02), 0.006, 0.04, "Z", STEEL, EX, seg=8)
th_up = math.radians(ramp_up_deg)
foot_up = Vector((HX1 + foot_eye_local[0] * math.cos(th_up) + foot_eye_local[2] * math.sin(th_up),
                  pop_yc,
                  Z0 - foot_eye_local[0] * math.sin(th_up) + foot_eye_local[2] * math.cos(th_up)))
CHAIN_LEN = (HOOK - foot_up).length


def rod(name, p0, p1, r, material, c):
    d = p1 - p0
    ob = box(name, (p0 + p1) / 2, (2 * r, 2 * r, d.length), material, c)
    ob.rotation_euler = d.to_track_quat("Z", "Y").to_euler()
    return ob


chain_hang = [rod("chain_hanging", HOOK, HOOK - Vector((0, 0, CHAIN_LEN)), 0.004, STEEL, EX),
              box("carabiner_hanging", (HOOK.x, HOOK.y, HOOK.z - CHAIN_LEN), (0.02, 0.012, 0.05), STEEL, EX)]
chain_taut = [rod("chain_taut", HOOK, foot_up, 0.004, STEEL, EX),
              box("carabiner_taut", foot_up, (0.02, 0.012, 0.05), STEEL, EX)]
for o in (chain_taut if not RAMP_LIFTED else chain_hang):
    o.hide_viewport = o.hide_render = True

# --- bell-crank lever wheels (house end) ---
# One rigid L-lever per side (2x4 on edge, vertical leg + horizontal leg) pivoting on a wheel post
# under the floor rail. The horizontal leg carries the wheel; at rest the wheel sits flush with the
# frame bottom, unloaded. Push the top of the vertical leg toward the run: the wheel drops and the
# house end rises by WHEEL_TRAVEL; drop the wedge block between the stop ledge and the lever to lock.
# Preview by rotating the wheel_arm_hinge_* empties about Y (+ = wheel down), or WHEEL_LOCKED = True.
ARM_H = 0.095                                   # 2x4 on edge: 45 thick x 95 wide
mid_z0, mid_z1 = FLOOR_BOT - D, FLOOR_BOT      # house-floor rail (under the floor edge)
a_len = AXLE_X - PIV_X
phi = math.degrees(math.asin(WHEEL_TRAVEL / a_len))
h_lock = LOCK_Z - WHEEL_R                       # lock height above the pivot
gap0 = (PIV_X - ARM_H / 2) - LEDGE_X1           # rest gap between ledge end and lever back face
gap = gap0 + ARM_H / 2 * (1 - math.cos(math.radians(phi))) + h_lock * math.sin(math.radians(phi))
for side in ("front", "back"):
    front = side == "front"
    yo = (lambda u: -u) if front else (lambda u: W + u)     # y at distance u outboard of frame
    fy = (0, T) if front else (W - T, W)
    bounds(f"house_floor_rail_{side}", 0, XF, fy[0], fy[1], mid_z0, mid_z1, PINE, FR)
    bounds(f"wheel_post_{side}", PIV_X - D / 2, PIV_X + D / 2, fy[0], fy[1], D, mid_z0, PINE, FR)
    ay0, ay1 = sorted((yo(0.003), yo(0.003 + T)))
    yc = (ay0 + ay1) / 2
    u0, u1 = -T, 0.003 + T + 0.012
    cyl(f"pivot_bolt_{side}", (PIV_X, yo((u0 + u1) / 2), WHEEL_R), 0.006, u1 - u0, "Y", STEEL, EX, seg=8)
    cyl(f"pivot_washer_{side}", (PIV_X, yo(u1), WHEEL_R), 0.018, 0.004, "Y", STEEL, EX, seg=12)
    # stop ledge bolted to the corner post, at lock height
    ledge_top = LOCK_Z + 0.04
    ly0, ly1 = (ay0, 0) if front else (W, ay1)      # ledge reaches back to the frame face
    bounds(f"lever_ledge_{side}", 0, LEDGE_X1, ly0, ly1, LOCK_Z - 0.10, ledge_top, PINE, EX)
    parts = [
        # horizontal leg (pivot corner to past the hub) and vertical push leg, one rigid L
        bounds(f"lever_leg_h_{side}", PIV_X - ARM_H / 2, AXLE_X + 0.07, ay0, ay1,
               WHEEL_R - ARM_H / 2, WHEEL_R + ARM_H / 2, PINE, EX),
        bounds(f"lever_leg_v_{side}", PIV_X - ARM_H / 2, PIV_X + ARM_H / 2, ay0, ay1,
               WHEEL_R - ARM_H / 2, LEVER_TOP, PINE, EX),
        cyl(f"lever_grip_{side}", (PIV_X, yo(0.003 + T + 0.06), LEVER_TOP - 0.02), 0.016, 0.16, "Y", PINE, EX, seg=12),
    ]
    uw = 0.003 + T + 0.01 + 0.0375                 # wheel centre, outboard of the lever
    parts += [
        cyl(f"tire_{side}", (AXLE_X, yo(uw), WHEEL_R), WHEEL_R, 0.075, "Y", RUBBER, EX, seg=32),
        cyl(f"rim_{side}", (AXLE_X, yo(uw), WHEEL_R), 0.09, 0.08, "Y", STEEL, EX, seg=24),
        cyl(f"stub_axle_{side}", (AXLE_X, yo(0.0965), WHEEL_R), 0.008, 0.187, "Y", STEEL, EX, seg=8),
        cyl(f"axle_washer_{side}", (AXLE_X, yo(0.1675), WHEEL_R), 0.025, 0.003, "Y", STEEL, EX, seg=12),
        cyl(f"axle_nut_{side}", (AXLE_X, yo(0.178), WHEEL_R), 0.015, 0.016, "Y", STEEL, EX, seg=6),
    ]
    h = hinge(f"wheel_arm_hinge_{side}", (PIV_X, yc, WHEEL_R), parts, EX)
    blk_w = gap - 0.002
    # parked on top of the ledge; locked = dropped into the gap between ledge end and lever
    blk_x = LEDGE_X1 + blk_w / 2 if not WHEEL_LOCKED else LEDGE_X1 + gap / 2
    blk_z = ledge_top + 0.07 if not WHEEL_LOCKED else LOCK_Z
    if WHEEL_LOCKED:
        h.rotation_euler.y = math.radians(phi)
    box(f"stop_block_{side}", (blk_x, yc, blk_z), (blk_w, T, 0.14), PINE, EX)
# Handle (full width, like the video): one lapped arm on each EAST CORNER post (inboard side) with a
# diagonal brace, joined by a 2x3-on-edge bar across the whole width; through-bolted (M8), never
# on mesh. Standing centred behind it you lift with both hands wide and steer by swinging the tail.
ARM_LEN, ARM_Z0, ARM_Z1, BRACE_Z = 0.28, 0.86, 0.93, 0.40
for i, (py, ay) in enumerate(((T / 2, 1.5 * T), (W - T / 2, W - 1.5 * T))):
    bounds(f"handle_arm_{i}", L - T, L + ARM_LEN, ay - T / 2, ay + T / 2, ARM_Z0, ARM_Z1, PINE, EX)
    x_lo, x_hi, z_lo, z_hi = L - T / 2, L + ARM_LEN - 0.02, BRACE_Z, ARM_Z0
    blen = math.hypot(x_hi - x_lo, z_hi - z_lo)
    bang = math.degrees(math.atan2(z_hi - z_lo, x_hi - x_lo))
    box(f"handle_brace_{i}", ((x_lo + x_hi) / 2, ay, (z_lo + z_hi) / 2), (blen, T, T), PINE, EX,
        rot=(0, -bang, 0))
    for j, (bx, bz) in enumerate(((L - T / 2, ARM_Z0 + 0.018), (L - T / 2, ARM_Z1 - 0.018))):
        cyl(f"handle_bolt_{i}_{j}", (bx, (py + ay) / 2, bz), 0.004, 2 * T + 0.02, "Y", STEEL, EX, seg=8)
bounds("handle_bar", L + ARM_LEN - T, L + ARM_LEN, 0, W, ARM_Z0, ARM_Z1, PINE, EX)

# --- human door (front long side, closed): battens + latch, hinged on the x=2.5 post ---
dy1, dy0 = -2 * e, -2 * e - 0.02
# true diagonal brace: bottom corner on the hinge side up to the top corner on the latch side
_dx0, _dx1 = DOOR_X0 + 0.04, DOOR_X1 - 0.04
_dz0, _dz1 = D + 0.04, DOOR_H - 0.04
_dang = math.degrees(math.atan2(_dz1 - _dz0, _dx1 - _dx0))
DOOR_DIAG = box("door_batten_diag", ((_dx0 + _dx1) / 2, (dy0 + dy1) / 2, (_dz0 + _dz1) / 2),
                (math.hypot(_dx1 - _dx0, _dz1 - _dz0), dy1 - dy0, 0.04), PINE, EX,
                rot=(0, -_dang, 0))
door_parts = [
    bounds("door_batten_l", DOOR_X0, DOOR_X0 + 0.04, dy0, dy1, D, DOOR_H, PINE, EX),
    bounds("door_batten_r", DOOR_X1 - 0.04, DOOR_X1, dy0, dy1, D, DOOR_H, PINE, EX),
    bounds("door_batten_t", DOOR_X0, DOOR_X1, dy0, dy1, DOOR_H - 0.04, DOOR_H, PINE, EX),
    bounds("door_batten_b", DOOR_X0, DOOR_X1, dy0, dy1, D, D + 0.04, PINE, EX),
    DOOR_DIAG,
    bounds("door_latch", DOOR_X1 - 0.12, DOOR_X1 - 0.04, dy0 - 0.03, dy0, 0.80, 0.84, STEEL, EX),
]
# rotate Z NEGATIVE to swing the door outward (hinge on the x=2.5 post side)
hinge("door_hinge", (DOOR_X0, dy0, DOOR_H / 2), door_parts, EX)

# --- rain-covered feed/water corner (back-east) ---
cx0, cx1, cy0, cy1 = 3.10, 3.95, 1.00, 1.95
cz, tilt = 1.25, -6.0
box("rain_cover", ((cx0 + cx1) / 2, (cy0 + cy1) / 2, cz), (cx1 - cx0 + 0.1, cy1 - cy0 + 0.1, 0.01),
    CHAPA, EX, rot=(tilt, 0, 0))
for i, (hx, hy) in enumerate(((cx0, cy0), (cx1, cy0), (cx0, cy1), (cx1, cy1))):
    bounds(f"cover_hanger_{i}", hx - 0.01, hx + 0.01, hy - 0.01, hy + 0.01, cz, H, PINE, EX)
cyl("waterer", (3.40, 1.50, 0.14), 0.10, 0.28, "Z", BLUE, EX)
cyl("feeder", (3.70, 1.50, 0.18), 0.13, 0.36, "Z", RED, EX)

# --- environment: ground, sun, camera ---
g = bounds("ground", -6, 9, -5, 7, -0.02, 0.0, GRASS, EN)
sun = bpy.data.objects.get("CoopSun")
if sun is None:
    sun = bpy.data.objects.new("CoopSun", bpy.data.lights.new("CoopSun", "SUN"))
    EN.objects.link(sun)
sun.data.energy = 3.5
sun.rotation_euler = [math.radians(a) for a in (50, 0, 35)]
world = bpy.context.scene.world or bpy.data.worlds.new("World")
bpy.context.scene.world = world
world.use_nodes = True
bg = next((n for n in world.node_tree.nodes if n.type == "BACKGROUND"), None)
if bg:
    bg.inputs["Color"].default_value = (0.62, 0.76, 0.92, 1.0)
    bg.inputs["Strength"].default_value = 1.0

cam = bpy.data.objects.get("Camera")
if cam is None:
    cam = bpy.data.objects.new("Camera", bpy.data.cameras.new("Camera"))
    EN.objects.link(cam)
cam.location = (-3.8, -6.2, 3.4)
cam.rotation_euler = (Vector((2.0, 1.0, 0.8)) - cam.location).to_track_quat("-Z", "Y").to_euler()
cam.data.lens = 35
bpy.context.scene.camera = cam
bpy.context.scene.view_settings.view_transform = "Standard"
bpy.ops.wm.save_as_mainfile(filepath=OUT_DIR + r"\chicken_coop_v4.blend")

print("coop v4 built:", len([o for c in COLLS for o in bpy.data.collections[c].objects]), "objects;",
      "ramp angle %.1f deg, roof slope %.1f deg, ridge %.2f m, chain %.2f m, lever phi %.1f deg, lock gap %.3f m" % (ramp_deg, th, RIDGE, CHAIN_LEN, phi, gap))
