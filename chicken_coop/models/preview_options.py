"""Throwaway side-by-side preview of two house layouts (A: full-width house section,
B: narrow house sticking out). Builds in its own scene "PreviewAB" (the real coop scene is not
touched), renders to models/renders/preview_*.png, then removes the scene.
Run: python tools/bl.py run models/preview_options.py"""
import math
import bmesh
import bpy
from mathutils import Vector

OUT = r"C:\Lucho\rancho\IA\chicken_coop\models\renders"
T, D, H, W, L = 0.045, 0.07, 1.6, 2.0, 4.0
PLY, Z0 = 0.012, 0.5
SLOPE = 0.4                      # roof rise/run (~22 deg)
OV = 0.15                        # eave overhang

main_engine = bpy.context.scene.render.engine
old = bpy.data.scenes.get("PreviewAB")
if old:
    bpy.data.scenes.remove(old)
sc = bpy.data.scenes.new("PreviewAB")
sc.render.engine = main_engine
sc.render.resolution_x, sc.render.resolution_y = 1600, 900
sc.view_settings.view_transform = "Standard"
C = sc.collection


def mat(name, rgb, alpha=1.0, metallic=0.0, rough=0.7):
    m = bpy.data.materials.get("PV_" + name) or bpy.data.materials.new("PV_" + name)
    m.use_nodes = True
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = (*rgb, 1.0)
    b.inputs["Alpha"].default_value = alpha
    b.inputs["Metallic"].default_value = metallic
    b.inputs["Roughness"].default_value = rough
    if alpha < 1.0:
        try:
            m.surface_render_method = "BLENDED"
        except Exception:
            pass
    return m


PINE = mat("pine", (0.72, 0.52, 0.30))
PLYW = mat("ply", (0.88, 0.80, 0.62))
ROOF = mat("roof", (0.30, 0.36, 0.42), metallic=0.5, rough=0.4)
MESH = mat("mesh", (0.55, 0.60, 0.65), alpha=0.22)
GLASS = mat("glass", (0.45, 0.65, 0.85), alpha=0.6)
DARK = mat("dark", (0.05, 0.05, 0.05))
RUBBER = mat("rubber", (0.03, 0.03, 0.03), rough=0.9)
GRASS = mat("grass", (0.25, 0.42, 0.16), rough=1.0)
LABEL = mat("label", (0.8, 0.1, 0.1))


def finish(bm, name, material, loc=(0, 0, 0), rot=(0, 0, 0)):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    ob.location = loc
    ob.rotation_euler = [math.radians(r) for r in rot]
    ob.data.materials.append(material)
    C.objects.link(ob)
    return ob


def box(name, center, size, material, rot=(0, 0, 0)):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x *= size[0]
        v.co.y *= size[1]
        v.co.z *= size[2]
    return finish(bm, name, material, center, rot)


def bnd(name, x0, x1, y0, y1, z0, z1, material):
    return box(name, ((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2), (x1 - x0, y1 - y0, z1 - z0), material)


def cyl(name, center, r, depth, axis, material):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=r, radius2=r, depth=depth)
    rot = {"Z": (0, 0, 0), "Y": (90, 0, 0), "X": (0, 90, 0)}[axis]
    return finish(bm, name, material, center, rot)


def gable_wall(name, pts, x0, x1, material):
    """Polygon in (y, z) extruded along x."""
    bm = bmesh.new()
    f = bm.faces.new([bm.verts.new((x0, y, z)) for y, z in pts])
    ext = bmesh.ops.extrude_face_region(bm, geom=[f])
    vs = [g for g in ext["geom"] if isinstance(g, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, vec=(x1 - x0, 0, 0), verts=vs)
    bmesh.ops.recalc_face_normals(bm, faces=list(bm.faces))
    return finish(bm, name, material)


def run_frame(tag, xa, xb, oy, west_wall):
    """Pine frame + translucent mesh for the run between x=xa and x=xb."""
    for z0, z1, t in ((0, D, "bot"), (H - D, H, "top")):
        bnd(f"{tag}_rail_{t}_f", xa, xb, oy, oy + T, z0, z1, PINE)
        bnd(f"{tag}_rail_{t}_b", xa, xb, oy + W - T, oy + W, z0, z1, PINE)
        bnd(f"{tag}_rail_{t}_e", xb - T, xb, oy + T, oy + W - T, z0, z1, PINE)
        bnd(f"{tag}_rail_{t}_w", xa, xa + T, oy + T, oy + W - T, z0, z1, PINE)
    for x in (xa, (xa + xb) / 2, xb):
        x0 = min(max(x - D / 2, xa), xb - D)
        for yy in (oy, oy + W - T):
            bnd(f"{tag}_post", x0, x0 + D, yy, yy + T, D, H - D, PINE)
    bnd(f"{tag}_cross", (xa + xb) / 2 - T / 2, (xa + xb) / 2 + T / 2, oy + T, oy + W - T, H - T, H, PINE)
    e = 0.004
    box(f"{tag}_m_front", ((xa + xb) / 2, oy - e, H / 2), (xb - xa, e, H), MESH)
    box(f"{tag}_m_back", ((xa + xb) / 2, oy + W + e, H / 2), (xb - xa, e, H), MESH)
    box(f"{tag}_m_east", (xb + e, oy + W / 2, H / 2), (e, W, H), MESH)
    box(f"{tag}_m_roof", ((xa + xb) / 2, oy + W / 2, H + e), (xb - xa, W, e), MESH)
    if west_wall:
        box(f"{tag}_m_west", (xa - e, oy + W / 2, H / 2), (e, W, H), MESH)
    # handle at the east end
    for y in (oy + 1.2, oy + 1.8):
        bnd(f"{tag}_handle_arm", xb, xb + 0.28, y - T / 2, y + T / 2, 0.86, 0.93, PINE)
    cyl(f"{tag}_handle_bar", (xb + 0.26, oy + 1.5, 0.895), 0.025, 0.7, "Y", PINE)


def house(tag, x0, x1, y0, y1, eave, oy, window_on):
    """Plywood box on a floor at Z0 with a gable roof (ridge along x), window, nest boxes, ramp."""
    w = y1 - y0
    ym = (y0 + y1) / 2
    ridge = eave + (w / 2) * SLOPE
    bnd(f"{tag}_floor", x0, x1, y0, y1, Z0 - 0.018, Z0, PLYW)
    bnd(f"{tag}_wall_f", x0, x1, y0, y0 + PLY, Z0, eave, PLYW)
    bnd(f"{tag}_wall_b", x0, x1, y1 - PLY, y1, Z0, eave, PLYW)
    pts = [(y0, Z0), (y1, Z0), (y1, eave), (ym, ridge), (y0, eave)]
    gable_wall(f"{tag}_gable_w", pts, x0, x0 + PLY, PLYW)
    gable_wall(f"{tag}_gable_e", pts, x1 - PLY, x1, PLYW)
    # roof slabs (front slope descends toward -y)
    run = w / 2 + OV
    th = math.degrees(math.atan(SLOPE))
    ln = run / math.cos(math.radians(th))
    zc = (ridge + (eave - OV * SLOPE)) / 2 + 0.02
    for s, name in ((-1, "f"), (1, "b")):
        box(f"{tag}_roof_{name}", ((x0 + x1) / 2, ym + s * run / 2, zc), (x1 - x0 + 0.1, ln, 0.02), ROOF,
            rot=(-s * th, 0, 0))
    # window (reused louvered 1.0 x 0.85)
    if window_on == "west":
        box(f"{tag}_window", (x0 - 0.01, y0 + 0.15 + 0.5, Z0 + 0.05 + 0.425), (0.02, 1.0, 0.85), GLASS)
        nest_y = (y0 + 1.25, y0 + 1.95)
    else:
        xc = (x0 + x1) / 2
        box(f"{tag}_window", (xc, y0 - 0.01, Z0 + 0.05 + 0.425), (1.0, 0.02, 0.85), GLASS)
        nest_y = (y0 + 0.2, y0 + 0.95)
    nx0 = x0 - 0.35
    bnd(f"{tag}_nest", nx0, x0, nest_y[0], nest_y[1], Z0 + 0.05, Z0 + 0.35, PLYW)
    box(f"{tag}_nest_lid", (nx0 / 2 + x0 / 2, (nest_y[0] + nest_y[1]) / 2, Z0 + 0.38),
        (0.42, nest_y[1] - nest_y[0] + 0.04, 0.02), PLYW, rot=(0, -12, 0))
    # pop-hole + ramp on the east wall
    py = y0 + 0.45
    box(f"{tag}_pophole", (x1, py, Z0 + 0.04 + 0.19), (0.02, 0.30, 0.38), DARK)
    a = math.degrees(math.asin(Z0 / 1.1))
    box(f"{tag}_ramp", (x1 + 0.55 * math.cos(math.radians(a)), py, Z0 - 0.55 * math.sin(math.radians(a))),
        (1.1, 0.30, 0.02), PLYW, rot=(0, a, 0))


def wheels(tag, xa, oy):
    for y in (oy - 0.09, oy + W + 0.09):
        cyl(f"{tag}_wheel", (xa, y, 0.15), 0.15, 0.075, "Y", RUBBER)


def label(txt, loc):
    cu = bpy.data.curves.new("lbl" + txt, "FONT")
    cu.body = txt
    cu.size = 1.0
    cu.extrude = 0.03
    ob = bpy.data.objects.new("lbl" + txt, cu)
    ob.location = loc
    ob.data.materials.append(LABEL)
    C.objects.link(ob)


# ---------------- Option A: house = full-width first section, run 3.0 m ----------------
oyA = 0.0
HA = 1.0
run_frame("A", HA, L, oyA, west_wall=False)
# frame rails continue under the house (chassis + floor edge), corner posts
for yy in (oyA, oyA + W - T):
    bnd("A_chassis_bot", 0, HA, yy, yy + T, 0, D, PINE)
    bnd("A_chassis_floor", 0, HA, yy, yy + T, Z0 - 0.018 - D, Z0 - 0.018, PINE)
    for x in (0, HA - D):
        bnd("A_house_post", x, x + D, yy, yy + T, D, Z0 - 0.018 - D, PINE)
bnd("A_chassis_bot_w", 0, T, oyA + T, oyA + W - T, 0, D, PINE)
house("A", 0.0, HA, oyA, oyA + W, 1.45, oyA, "west")
for nm, (xx0, xx1, yy0, yy1) in {"f": (0, HA, oyA - 0.004, oyA), "b": (0, HA, oyA + W, oyA + W + 0.004)}.items():
    bnd("A_under_" + nm, xx0, xx1, yy0, yy1, 0, Z0, MESH)
bnd("A_under_w", -0.004, 0, oyA, oyA + W, 0, Z0, MESH)
wheels("A", 1.2, oyA)
label("A", (-1.8, oyA + 0.6, 0.0))

# ---------------- Option B: narrow house (1.5 x 1.2) in front of a 2.5 m run ----------------
oyB = 4.0
HB = 1.5
run_frame("B", HB, L, oyB, west_wall=True)
hy0, hy1 = oyB + 0.4, oyB + 1.6
house("B", 0.0, HB, hy0, hy1, 1.40, oyB, "front")
# ground-level ladder chassis carrying the wheels + legs standing on the cross rails
for yy in (oyB, oyB + W - T):
    bnd("B_skid", 0, HB, yy, yy + T, 0, D, PINE)
for xx in (0.0, HB - D):
    bnd("B_chassis_cross", xx, xx + D, oyB, oyB + W, 0, T, PINE)
    for yy in (hy0, hy1 - D):
        bnd("B_leg", xx, xx + D, yy, yy + D, T, Z0 - 0.018, PINE)
wheels("B", 1.4, oyB)
label("B", (-1.8, oyB + 0.6, 0.0))

# ---------------- environment ----------------
bnd("ground", -6, 12, -4, 10, -0.02, 0.0, GRASS)
sun = bpy.data.objects.new("PV_Sun", bpy.data.lights.new("PV_Sun", "SUN"))
sun.data.energy = 3.5
sun.rotation_euler = [math.radians(a) for a in (50, 0, 35)]
C.objects.link(sun)
world = bpy.data.worlds.new("PV_World")
world.use_nodes = True
bg = next(n for n in world.node_tree.nodes if n.type == "BACKGROUND")
bg.inputs["Color"].default_value = (0.62, 0.76, 0.92, 1.0)
sc.world = world
cam = bpy.data.objects.new("PV_Cam", bpy.data.cameras.new("PV_Cam"))
C.objects.link(cam)
sc.camera = cam


def shoot(name, loc, tgt, lens=35, roll=0.0):
    cam.location = loc
    cam.data.lens = lens
    e = (Vector(tgt) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    e.rotate_axis("Z", math.radians(roll))
    cam.rotation_euler = e
    sc.render.filepath = OUT + "\\" + name + ".png"
    bpy.ops.render.render(write_still=True, scene=sc.name)


shoot("preview_1_west_end", (-8.5, 3.0, 3.4), (1.5, 3.0, 0.8), lens=32)
shoot("preview_2_top", (1.8, 3.0, 11.0), (1.8, 3.0, 0.0), lens=32, roll=90)
shoot("preview_3_east_end", (10.5, 3.0, 3.2), (1.5, 3.0, 0.8), lens=32)
shoot("preview_4_front_oblique", (-5.0, -5.5, 3.6), (1.8, 3.0, 0.8), lens=30)

bpy.data.scenes.remove(sc)
print("previews rendered")
