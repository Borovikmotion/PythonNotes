import maya.cmds as cmds 
import maya.OpenMaya as om


# create 2 spheres and 2 cubes !


S1 = cmds.xform("pSphere1", ws=1, q=1, t=1)
S2 = cmds.xform("pSphere2", ws=1, q=1, t=1)

# Get vector between Sphere1 and Sphere2
S1_pnt = om.MPoint(S1[0], S1[1], S1[2])
S2_pnt = om.MPoint(S2[0], S2[1], S2[2])
vector_S1_S2 = om.MVector(S2[0] - S1[0], S2[1] - S1[1], S2[2] - S1[2])


# Get distance between 2 spheres, and 1% of it
distance = vector_S1_S2.length() # 100%
dist_unit = distance / 100.0 # 1%

# Normalize vector
vector_S1_S2.normalize()


# ---------------- Place in-between

# Calculate cube1 position in between 2 spheres
C1_pos = S1_pnt + vector_S1_S2 * 30 * dist_unit

# set position
cmds.xform("pCube1", t = [C1_pos.x, C1_pos.y, C1_pos.z], ws=1)

# ---------------- Cross product

vec_y = om.MVector(0,1,0)
cross_vector = vector_S1_S2 ^ vec_y

C2_pos = S1_pnt + cross_vector * 100 * dist_unit
cmds.xform("pCube2", t = [C2_pos.x, C2_pos.y, C2_pos.z], ws=1)