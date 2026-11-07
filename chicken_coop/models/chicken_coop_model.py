"""Chicken coop v0 - parametric Blender build (Blender 5.x).

Source of truth: chicken_coop.md "Design v0". Run it inside Blender (via the
MCP socket: `python tools/bl.py run models/chicken_coop_model.py`).
Re-running is safe: it deletes and rebuilds the Coop_* collections.

Axes: X = 4 m length (house at x=0, west), Y = 2 m width (front/window face
at y=0, back at y=W), Z up. Units: metres.
Mesh is schematic (5 cm grid + wireframe modifier), NOT the real 25x50 mm.
"""
import math
import bmesh
import bpy
from mathutils import Vector

# ---------------- PARAMETERS (edit here) ----------------
L, W, H = 4.0, 2.0, 1.6            # run: length, width, height
T, D = 0.045, 0.07                 # pine 2"x3" real section (thin, deep)
HOUSE_L, HOUSE_W = 1.5, 1.2        # raised house footprint
Z0 = 0.5                           # house floor height
PLY = 0.012                        # plywood thickness
WIN_W, WIN_H = 1.0, 0.85           # TODO: measure the real reused window
SILL, LINTEL = 0.05, 0.05
POP_W, POP_H, POP_Y = 0.30, 0.38, 0.25   # pop-hole size / offset from front
RAMP_L, RAMP_W = 1.1, 0.30
DOOR_Y0, DOOR_Y1, DOOR_H = 0.30, 1.00, 1.30   # human door on east end (default)
WHEEL_R, AXLE_X = 0.15, 1.20       # 30 cm pneumatic wheel; hub 30 cm from the arm pivot
PIV_X = 0.90                       # wheel-arm pivot (a = AXLE_X - PIV_X = 0.30 m)
ARM_END_X, LEDGE_X = 1.95, 1.45    # arm tip (foot pad end) / stop-block position
WHEEL_TRAVEL = 0.06                # how far the wheel drops below the frame when locked
WHEEL_LOCKED = False               # True: arms rotated down, stop blocks inserted
RAMP_LIFTED = False                # True: ramp hoisted by the chain (travel pose), foot at RAMP_FOOT_UP
RAMP_FOOT_UP = 0.15                # ramp foot height above ground when hoisted
LEG3_STOWED = False                # True: leg 3 folded up under the house floor (travel pose)
BLK_H = T                          # bearing block under legs 0-2: 45 mm thick, 2 leg-widths long
MESH_STEP = 0.05                   # schematic mesh pitch
OUT_DIR = r"C:\Lucho\rancho\IA\chicken_coop\models"

HX0, HX1 = T, HOUSE_L              # house x range
HY0, HY1 = T, T + HOUSE_W          # house y range
FRONT_TOP = Z0 + SILL + WIN_H + LINTEL
BACK_TOP = H - 0.045               # wall top; roof layers add ~3.5 cm, stays under the mesh roof

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
    b = m.node_tree.nodes["Principled BSDF"]
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
    cutter = box(ob.name + "_cutter", center, size, None, ob.users_collection[0])
    cutter.hide_viewport = True
    cutter.hide_render = True
    m = ob.modifiers.new("cut", "BOOLEAN")
    m.object = cutter
    m.operation = "DIFFERENCE"


def hinge(name, loc, children, c):
    """Empty at the hinge point; children keep their world pose but now rotate
    with it. Rotate the empty (X for the window, Y for the nest lid) to preview opening."""
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
    xs = [v.co.x for v in bm.verts]
    ys = [v.co.y for v in bm.verts]
    sx, sy = w / (max(xs) - min(xs)), h / (max(ys) - min(ys))
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

# --- frame: perimeter rails, posts, roof members ---
xs = [0, HOUSE_L, HOUSE_L + (L - HOUSE_L) / 2, L]
for z0, z1, tag in ((0, D, "bot"), (H - D, H, "top")):
    bounds(f"rail_{tag}_front", 0, L, 0, T, z0, z1, PINE, FR)
    bounds(f"rail_{tag}_back", 0, L, W - T, W, z0, z1, PINE, FR)
    bounds(f"rail_{tag}_west", 0, T, T, W - T, z0, z1, PINE, FR)
    bounds(f"rail_{tag}_east", L - T, L, T, W - T, z0, z1, PINE, FR)
for i, xp in enumerate(xs):
    x0 = min(max(xp - D / 2, 0), L - D)
    bounds(f"post_front_{i}", x0, x0 + D, 0, T, D, H - D, PINE, FR)
    bounds(f"post_back_{i}", x0, x0 + D, W - T, W, D, H - D, PINE, FR)
    if 0 < i < 3:   # roof cross-members (mesh support), skip over the house
        bounds(f"roof_cross_{i}", xp - T / 2, xp + T / 2, T, W - T, H - T, H, PINE, FR)
bounds("roof_long", HOUSE_L, L, W / 2 - T / 2, W / 2 + T / 2, H - T, H, PINE, FR)
bounds("post_west_mid", 0, T, W / 2 - D / 2, W / 2 + D / 2, D, H - D, PINE, FR)
# east end: door posts + lintel
for i, y in enumerate((DOOR_Y0, DOOR_Y1)):
    bounds(f"door_post_{i}", L - T, L, y - T / 2, y + T / 2, D, H - D, PINE, FR)
bounds("door_lintel", L - T, L, DOOR_Y0, DOOR_Y1, DOOR_H, DOOR_H + T, PINE, FR)

# --- mesh sheets (outer faces) ---
e = 0.003
mesh_panel("mesh_front_east", "XZ", ((HOUSE_L + L) / 2, -e, H / 2), L - HOUSE_L, H)
mesh_panel("mesh_front_under_house", "XZ", (HOUSE_L / 2, -e, Z0 / 2), HOUSE_L, Z0)
mesh_panel("mesh_back", "XZ", (L / 2, W + e, H / 2), L, H)
mesh_panel("mesh_east", "YZ", (L + e, W / 2, H / 2), W, H)
mesh_panel("mesh_west_under_house", "YZ", (-e, W / 2, Z0 / 2), W, Z0)
mesh_panel("mesh_west_above", "YZ", (-e, (HY1 + W) / 2, (Z0 + H) / 2), W - HY1, H - Z0)
mesh_panel("mesh_roof", "XY", (L / 2, W / 2, H + e), L, W)
# anti-dig skirt, folded outward
S = 0.25
mesh_panel("skirt_front", "XY", (L / 2, -S / 2, 0.004), L + 2 * S, S)
mesh_panel("skirt_back", "XY", (L / 2, W + S / 2, 0.004), L + 2 * S, S)
mesh_panel("skirt_west", "XY", (-S / 2, W / 2, 0.004), S, W)
mesh_panel("skirt_east", "XY", (L + S / 2, W / 2, 0.004), S, W)

# --- house shell ---
bounds("house_floor", HX0, HX1, HY0, HY1, Z0 - 0.018, Z0, PLYW, SH)
# Legs 0-2 are bolted to the inside face of a bottom rail and stand on a bearing block laid along
# that rail (block on the ground while parked, so the weight does not hang on the bolts).
# Leg 3 (back-east, away from every rail) is a fold-up prop: hinged under the floor, lowered to
# the ground when parked, stowed against the floor when moving.
FLOOR_BOT = Z0 - 0.018
for i, (lx, ly) in enumerate(((HX0, HY0), (HX1 - D, HY0), (HX0, HY1 - D))):
    bounds(f"house_leg_{i}", lx, lx + D, ly, ly + D, BLK_H, FLOOR_BOT, PINE, SH)
    if i == 1:      # front rail: block runs along x, centred on the leg
        bx0 = lx + D / 2 - D
        bounds(f"leg_block_{i}", bx0, bx0 + 2 * D, T, T + D, 0, BLK_H, PINE, FR)
    else:           # west rail: block runs along y, centred on the leg (not into the front rail)
        by0 = max(T, ly + D / 2 - D)
        bounds(f"leg_block_{i}", T, T + D, by0, by0 + 2 * D, 0, BLK_H, PINE, FR)
l3x, l3y = HX1 - D, HY1 - D
piv_z = FLOOR_BOT - D / 2                      # pivot bolt through the leg, near its top
for k, (c0, c1) in enumerate(((l3y - 0.02, l3y), (l3y + D, l3y + D + 0.02))):
    bounds(f"leg3_cheek_{k}", l3x - 0.01, l3x + D + 0.01, c0, c1, piv_z - 0.04, FLOOR_BOT, PINE, SH)
leg3_parts = [
    bounds("house_leg_3", l3x, l3x + D, l3y, l3y + D, 0.02, FLOOR_BOT, PINE, SH),
    bounds("leg3_foot_pad", l3x + D / 2 - 0.08, l3x + D / 2 + 0.08, l3y + D / 2 - 0.08,
           l3y + D / 2 + 0.08, 0, 0.02, PLYW, SH),
    cyl("leg3_pivot_bolt", (l3x + D / 2, l3y + D / 2, piv_z), 0.005, D + 0.06, "Y", STEEL, SH, seg=8),
]
# rotate Y POSITIVE (90 deg) to fold the foot toward the west, flat under the floor
leg3_hinge = hinge("leg3_hinge", (l3x + D / 2, l3y + D / 2, piv_z), leg3_parts, SH)
if LEG3_STOWED:
    leg3_hinge.rotation_euler.y = math.radians(90)
bounds("house_back", HX0, HX1, HY1 - PLY, HY1, Z0, BACK_TOP, PLYW, SH)
side = [(HY0, Z0), (HY1, Z0), (HY1, BACK_TOP), (HY0, FRONT_TOP)]
prism_yz("house_west", side, HX0, HX0 + PLY, PLYW, SH)
east = prism_yz("house_east", side, HX1 - PLY, HX1, PLYW, SH)
pop_yc = HY0 + POP_Y + POP_W / 2
cut(east, (HX1 - PLY / 2, pop_yc, Z0 + 0.04 + POP_H / 2), (0.2, POP_W, POP_H))
# front wall: strips + sill + lintel around the window
wc = (HX0 + HX1) / 2
wx0, wx1 = wc - WIN_W / 2, wc + WIN_W / 2
fy0, fy1 = HY0, HY0 + PLY
bounds("front_strip_w", HX0, wx0, fy0, fy1, Z0, FRONT_TOP, PLYW, SH)
bounds("front_strip_e", wx1, HX1, fy0, fy1, Z0, FRONT_TOP, PLYW, SH)
bounds("front_sill", wx0, wx1, fy0, fy1, Z0, Z0 + SILL, PLYW, SH)
bounds("front_lintel", wx0, wx1, fy0, fy1, FRONT_TOP - LINTEL, FRONT_TOP, PLYW, SH)
# louvered window (closed)
wz0, wz1 = Z0 + SILL, Z0 + SILL + WIN_H
fw = 0.04
win_parts = [
    bounds("win_frame_l", wx0, wx0 + fw, fy0 - 0.02, fy0 + 0.02, wz0, wz1, PINE, SH),
    bounds("win_frame_r", wx1 - fw, wx1, fy0 - 0.02, fy0 + 0.02, wz0, wz1, PINE, SH),
    bounds("win_frame_t", wx0, wx1, fy0 - 0.02, fy0 + 0.02, wz1 - fw, wz1, PINE, SH),
    bounds("win_frame_b", wx0, wx1, fy0 - 0.02, fy0 + 0.02, wz0, wz0 + fw, PINE, SH),
]
n_sl = 8
for i in range(n_sl):
    zc = wz0 + fw + (WIN_H - 2 * fw) * (i + 0.5) / n_sl
    win_parts.append(box(f"louver_{i}", (wc, fy0, zc), (WIN_W - 2 * fw, 0.012, 0.13), GLASS, SH, rot=(35, 0, 0)))
# side-hinged (opens like a door, parallel to the ground): origin on the vertical hinge edge.
# WIN_HINGE_SIDE = "west" -> rotate Z NEGATIVE to swing out; "east" -> rotate Z POSITIVE.
WIN_HINGE_SIDE = "west"
hx = wx0 if WIN_HINGE_SIDE == "west" else wx1
hinge("window_hinge", (hx, fy0, (wz0 + wz1) / 2), win_parts, SH)
# roof: plywood + chapa, shed slope toward the front
th = math.degrees(math.atan2(BACK_TOP - FRONT_TOP, HOUSE_W))
# footprint = house walls exactly (no overhang: it would clip the frame posts/rails);
# stack tops out ~2 cm under the run's mesh roof
rm = (FRONT_TOP + BACK_TOP) / 2
rc = ((HX0 + HX1) / 2, (HY0 + HY1) / 2, rm + 0.0075)
rl = HOUSE_W / math.cos(math.radians(th))
box("house_roof_ply", rc, (HX1 - HX0, rl, 0.015), PLYW, SH, rot=(th, 0, 0))
box("house_roof_chapa", (rc[0], rc[1], rm + 0.02), (HX1 - HX0, rl, 0.01),
    CHAPA, SH, rot=(th, 0, 0))

# --- house interior ---
bounds("litter", HX0 + PLY, HX1 - PLY, HY0 + PLY, HY1 - PLY, Z0, Z0 + 0.03, LITTER, IN)
for i, (rx, rz) in enumerate(((0.65, Z0 + 0.50), (1.05, Z0 + 0.62))):
    cyl(f"roost_{i}", (rx, (HY0 + HY1) / 2, rz), 0.02, HOUSE_W - 0.1, "Y", PINE, IN)

# --- nest boxes (outside the west wall, lids open from outside) ---
nz0, nz1, nx0 = Z0 + 0.05, Z0 + 0.35, -0.35
bounds("nest_floor", nx0, 0, 0.20, 0.95, nz0, nz0 + PLY, PLYW, EX)
bounds("nest_back", nx0, nx0 + PLY, 0.20, 0.95, nz0, nz1, PLYW, EX)
for i, y in enumerate((0.20, 0.575, 0.95 - PLY)):
    bounds(f"nest_div_{i}", nx0, 0, y, y + PLY, nz0, nz1, PLYW, EX)
lid = box("nest_lid", (nx0 / 2, 0.575, nz1 + 0.02), (0.42, 0.80, 0.015), PLYW, EX, rot=(0, -12, 0))
# hinged on the house-side (high) edge: rotate Y POSITIVE to lift the outer edge
hinge("nest_lid_hinge", (0.0, 0.575, nz1 + 0.02 + 0.036), [lid], EX)

# --- ramp (empty parent, tilted; cleats every 15 cm) ---
# Hinged at the pop-hole sill. Parked: foot on the ground. Travel: hoisted by a chain from a hook
# under the roof (rotate `ramp_hinge` about Y toward ramp_up_deg to preview; swap the chains).
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
# foot eye on the ramp (child of the hinge) + chain with a carabiner, hook on the roof cross-member
foot_eye_local = (RAMP_L - 0.03, 0, 0.012)
box("ramp_foot_eye", foot_eye_local, (0.03, 0.03, 0.02), STEEL, EX, parent=ramp)
HOOK = Vector((HOUSE_L + (L - HOUSE_L) / 2, pop_yc, H - T - 0.02))   # under roof_cross_2
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


# chain hangs free when parked (carabiner at the bottom), taut to the ramp foot when hoisted
chain_hang = [rod("chain_hanging", HOOK, HOOK - Vector((0, 0, CHAIN_LEN)), 0.004, STEEL, EX),
              box("carabiner_hanging", (HOOK.x, HOOK.y, HOOK.z - CHAIN_LEN), (0.02, 0.012, 0.05), STEEL, EX)]
chain_taut = [rod("chain_taut", HOOK, foot_up, 0.004, STEEL, EX),
              box("carabiner_taut", foot_up, (0.02, 0.012, 0.05), STEEL, EX)]
for o in (chain_taut if not RAMP_LIFTED else chain_hang):
    o.hide_viewport = o.hide_render = True

# --- foot-lever wheels (house end) ---
# One pivoting 2x4 arm per side, hinged on a wheel post. At rest the wheel sits flush with the
# frame bottom, unloaded. Step on the pad: wheel goes down, the house end rises by WHEEL_TRAVEL;
# slide the stop block into the gap between arm and ledge to lock. Preview by rotating the
# wheel_arm_hinge_* empties about Y (+ = wheel down), or set WHEEL_LOCKED = True.
# Pedal is farther from the pivot than the wheel (lever gain b/a ~2.7) - the opposite of a
# pedal between pivot and wheel, which would double the foot force for a 230 kg coop.
ARM_H = 0.095                                   # 2x4 on edge: 45 thick x 95 tall
mid_z0, mid_z1 = Z0 - 0.018 - D, Z0 - 0.018     # house-floor rail (under the floor edge)
a_len = AXLE_X - PIV_X
phi = math.degrees(math.asin(WHEEL_TRAVEL / a_len))
d_blk = LEDGE_X - PIV_X
gap = ARM_H / 2 * (1 - math.cos(math.radians(phi))) + d_blk * math.sin(math.radians(phi))
arm_top, ledge_top = WHEEL_R + ARM_H / 2, WHEEL_R + ARM_H / 2 + D
for side in ("front", "back"):
    front = side == "front"
    yo = (lambda u: -u) if front else (lambda u: W + u)     # y at distance u outboard of frame
    fy = (0, T) if front else (W - T, W)
    bounds(f"house_floor_rail_{side}", 0, HOUSE_L, fy[0], fy[1], mid_z0, mid_z1, PINE, FR)
    bounds(f"wheel_post_{side}", PIV_X - D / 2, PIV_X + D / 2, fy[0], fy[1], D, mid_z0, PINE, FR)
    ay0, ay1 = sorted((yo(0.003), yo(0.003 + T)))
    yc = (ay0 + ay1) / 2
    # fixed: pivot bolt (through post + arm) and the ledge the block jams against
    u0, u1 = -T, 0.003 + T + 0.012
    cyl(f"pivot_bolt_{side}", (PIV_X, yo((u0 + u1) / 2), WHEEL_R), 0.006, u1 - u0, "Y", STEEL, EX, seg=8)
    cyl(f"pivot_washer_{side}", (PIV_X, yo(u1), WHEEL_R), 0.018, 0.004, "Y", STEEL, EX, seg=12)
    bounds(f"arm_ledge_{side}", LEDGE_X - 0.10, LEDGE_X + 0.10, ay0, ay1, arm_top, ledge_top, PINE, EX)
    # rotating assembly
    parts = [
        bounds(f"wheel_arm_{side}", PIV_X - 0.15, ARM_END_X, ay0, ay1, WHEEL_R - ARM_H / 2, arm_top, PINE, EX),
        bounds(f"foot_pad_{side}", ARM_END_X - 0.32, ARM_END_X - 0.02, yc - 0.06, yc + 0.06,
               arm_top, arm_top + 0.015, PLYW, EX),
    ]
    uw = 0.003 + T + 0.01 + 0.0375                 # wheel centre, outboard of the arm
    parts += [
        cyl(f"tire_{side}", (AXLE_X, yo(uw), WHEEL_R), WHEEL_R, 0.075, "Y", RUBBER, EX, seg=32),
        cyl(f"rim_{side}", (AXLE_X, yo(uw), WHEEL_R), 0.09, 0.08, "Y", STEEL, EX, seg=24),
        cyl(f"stub_axle_{side}", (AXLE_X, yo(0.0965), WHEEL_R), 0.008, 0.187, "Y", STEEL, EX, seg=8),
        cyl(f"axle_washer_{side}", (AXLE_X, yo(0.1675), WHEEL_R), 0.025, 0.003, "Y", STEEL, EX, seg=12),
        cyl(f"axle_nut_{side}", (AXLE_X, yo(0.178), WHEEL_R), 0.015, 0.016, "Y", STEEL, EX, seg=6),
    ]
    h = hinge(f"wheel_arm_hinge_{side}", (PIV_X, yc, WHEEL_R), parts, EX)
    blk_h = gap - 0.002
    blk_z = (arm_top - gap + arm_top) / 2 if WHEEL_LOCKED else ledge_top + blk_h / 2
    if WHEEL_LOCKED:
        h.rotation_euler.y = math.radians(phi)
        blk_z = arm_top - gap / 2
    box(f"stop_block_{side}", (LEDGE_X, yc, blk_z), (0.10, T, blk_h), PINE, EX)
# Handle: two full-height posts in the east wall (joined to top and bottom rails), each with
# a lapped arm + diagonal brace on its inboard side, through-bolted (M8) - the arm is never
# attached to mesh. Brace turns the pull into axial load instead of prying on the screws.
HANDLE_Y = (1.20, 1.80)
ARM_LEN, ARM_Z0, ARM_Z1, BRACE_Z = 0.28, 0.86, 0.93, 0.40
for i, py in enumerate(HANDLE_Y):
    bounds(f"handle_post_{i}", L - T, L, py - T / 2, py + T / 2, D, H - D, PINE, FR)
    ay = py + T if i == 0 else py - T   # arm lapped on the inboard side of its post
    bounds(f"handle_arm_{i}", L - T, L + ARM_LEN, ay - T / 2, ay + T / 2, ARM_Z0, ARM_Z1, PINE, EX)
    x_lo, x_hi, z_lo, z_hi = L - T / 2, L + ARM_LEN - 0.02, BRACE_Z, ARM_Z0
    blen = math.hypot(x_hi - x_lo, z_hi - z_lo)
    bang = math.degrees(math.atan2(z_hi - z_lo, x_hi - x_lo))
    box(f"handle_brace_{i}", ((x_lo + x_hi) / 2, ay, (z_lo + z_hi) / 2), (blen, T, T), PINE, EX,
        rot=(0, -bang, 0))
    for j, (bx, bz) in enumerate(((L - T / 2, ARM_Z0 + 0.018), (L - T / 2, ARM_Z1 - 0.018))):
        cyl(f"handle_bolt_{i}_{j}", (bx, (py + ay) / 2, bz), 0.004, 2 * T + 0.02, "Y", STEEL, EX, seg=8)
ay0, ay1 = HANDLE_Y[0] + T, HANDLE_Y[1] - T
cyl("handle_bar", (L + ARM_LEN - 0.02, (ay0 + ay1) / 2, (ARM_Z0 + ARM_Z1) / 2),
    0.025, ay1 - ay0 + T, "Y", PINE, EX)

# --- human door (east end, closed): battens + latch + hinges ---
dx = L + 2 * e
bounds("door_batten_l", dx, dx + 0.02, DOOR_Y0, DOOR_Y0 + 0.04, D, DOOR_H, PINE, EX)
bounds("door_batten_r", dx, dx + 0.02, DOOR_Y1 - 0.04, DOOR_Y1, D, DOOR_H, PINE, EX)
bounds("door_batten_t", dx, dx + 0.02, DOOR_Y0, DOOR_Y1, DOOR_H - 0.04, DOOR_H, PINE, EX)
bounds("door_batten_b", dx, dx + 0.02, DOOR_Y0, DOOR_Y1, D, D + 0.04, PINE, EX)
bounds("door_batten_diag", dx, dx + 0.02, DOOR_Y0 + 0.30, DOOR_Y0 + 0.34, D, DOOR_H, PINE, EX)
bounds("door_latch", dx + 0.02, dx + 0.05, DOOR_Y1 - 0.12, DOOR_Y1 - 0.04, 0.80, 0.84, STEEL, EX)

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
bg = world.node_tree.nodes.get("Background")
if bg:
    bg.inputs["Color"].default_value = (0.62, 0.76, 0.92, 1.0)
    bg.inputs["Strength"].default_value = 1.0

cam = bpy.data.objects.get("Camera")
if cam is None:
    cam = bpy.data.objects.new("Camera", bpy.data.cameras.new("Camera"))
    EN.objects.link(cam)
from mathutils import Vector
cam.location = (-3.8, -6.2, 3.4)
cam.rotation_euler = (Vector((2.0, 1.0, 0.8)) - cam.location).to_track_quat("-Z", "Y").to_euler()
cam.data.lens = 35
bpy.context.scene.camera = cam
bpy.context.scene.view_settings.view_transform = "Standard"
bpy.ops.wm.save_as_mainfile(filepath=OUT_DIR + r"\chicken_coop.blend")

print("coop built:", len([o for c in COLLS for o in bpy.data.collections[c].objects]), "objects;",
      "ramp angle %.1f deg, roof slope %.1f deg, front top %.2f m" % (ramp_deg, th, FRONT_TOP))
