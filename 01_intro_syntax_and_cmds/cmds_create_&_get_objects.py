import maya.cmds as cmds

""" CREATE OBJECTS """
#create locator
loc = cmds.spaceLocator()

#create group
offsetGrp = cmds.group(empty=1, n="OffsetGroup")

# poly objects
sphere = cmds.polySphere()
cube = cmds.polyCube(sx=10, sy=15, sz=5, h=20)
cone = cmds.polyCone(n='myCone', sx=5, sy=5, sz=5)

#curves
#nurbs circle, you can specify the direction (normal x y z vector), center position, ect
cmds.circle()
cmds.circle(nr=(0, 0, 1), c=(0, 0, 0))

# will create a curve with degree=1 (linear) through certain points a, b, c, d
a = [-1,1,0]
b = [1,1,0]
c = [1,-1,0]
d  = [-1,-1,0]
crv = cmds.curve(p=[(a[0], a[1], a[2]), (b[0], b[1], b[2]), (c[0], c[1], c[2]), (d[0], d[1], d[2]), (a[0], a[1], a[2])], n="my_square_curve", d = 1, ws=1)
# or this will also work
crv = cmds.curve(p=[(a), (b), (c), (d), (a)], n="my_square_curve", d = 1, ws=1)

# nurbs surface (tube)
crv = cmds.curve(p=[(a), (b)], d = 1, ws=1)
profile = cmds.circle(c =[a[0], a[1], a[2]], r = 0.5, nr = [1,0,0])
cmds.extrude(profile[0], crv, et=1)



""" GET OBJECTS """
#get selected objects names in short format
selected_objects = cmds.ls(sl=1, l=0)
# list all objects
cmds.ls()
# List all shapes in the dag.
cmds.ls(shapes=True)
# and many other applications

# when you need to find all child objects or just children or parent
all_child_objects = cmds.listRelatives('pSphere1', ad=1)
all_parent_objects = cmds.listRelatives('pSphere8', ap=1)

# for figuring out the type of the node
if cmds.nodeType(childObj) == "nurbsCurve":
    controls.append(i)
