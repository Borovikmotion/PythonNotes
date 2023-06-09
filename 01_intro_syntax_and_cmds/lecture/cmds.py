"""
MAYA Documentation 

https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=__CommandsPython_index_html

"""
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



""" MANIPULATE OBJECTS """
# delete object
cmds.delete(loc)

#parenting
cmds.parent(child_object, parent_object)

# basic transforms, select object or specify the name of the object you wanna transform
cmds.move(10, 0, 0, 'pSphere1', a=1)

# a relative shift in a position
cmds.move(offset[0], offset[1], offset[2], loc, r=1, os=1)
# rotatyion and scale
cmds.rotate()
cmds.scale()

# a very powerful command to get or to apply any transfroms of the objects, including matrixes and cool stuff
cmds.xform()

#get translation, modify, re-apply
locPosStart = cmds.xform(tempLoc, t=1, ws=1, q=1)
locPosX = locPosStart[0] + offsetX
locPosY = locPosStart[1] + offsetY
locPosZ = locPosStart[2] + offsetZ 
locFinalPos = [locPosX,locPosY,locPosZ]
cmds.xform(tempLoc, t=locFinalPos)

# rotate
cmds.xform(grp, ro = [0,45,0], r=1)

# set attribute - directly override any attribute of any objects
loc = cmds.spaceLocator()[0]
cmds.setAttr(loc + ".translateX", 10)
cmds.setAttr(loc + ".rotateY", 45)

# color objects by overriding properties
cmds.setAttr(endLoc[0] +".overrideEnabled", 1)
cmds.setAttr(endLoc[0] +".overrideColor", 17)

# freeze transfromations
cmds.makeIdentity(loc, apply = 1, t =1, s =1, r =1, n = 0, pn = 1)


""" CONSTRAINTS """
# parent, point, orient constraints without offset 
pCon = cmds.parentConstraint(source, target, mo=0)
cmds.pointConstraint(source, target, mo=0)
cmds.orientConstraint(source, target, mo=0)

# aim constraint
# source = end locator, target = our object
cmds.aimConstraint(source, target, worldUpType = "object", worldUpObject = upLoc[0], mo=1)


""" KEYFRAMES AND BAKE """
# get the beginning and end of the timeline
minT = cmds.playbackOptions(q=1, min =1)
maxT = cmds.playbackOptions(q=1, max =1)

# set keyframe on the property
cmds.setKeyframe(loc[0] + ".translateX", time=minT, v=-10)
cmds.setKeyframe("Group.translateX", time=10, v=10)
cmds.setKeyframe(planetRotationGrp + ".rotateY", time=maxT, v=360*rotationCount, itt= "linear")

# bake animation
cmds.bakeResults(objects, time = (minT,maxT))
cmds.bakeSimulation(objects, time = (minT,maxT)) #or this, but it's considered as an obsolete command

# shift all keyframes at the timeline, timeshift
time_shift = 10 # number of frames to shift
cmds.select(animated_object)
cmds.keyframe(edit=True,relative=True,timeChange=time_shift,time=(minT,maxT))


""" OTHER STUFF """
# assign material to the object
planet = cmds.polySphere(n = planetName, r = planetRadius)
planetShader = cmds.shadingNode("lambert", n = "lambert"+planetName, asShader=1)
randColorR = random.uniform(0, 1)
randColorG = random.uniform(0, 1)
randColorB = random.uniform(0, 1)
cmds.setAttr(planetShader + ".color", randColorR, randColorG, randColorB, type="double3")
cmds.select(planet)
cmds.hyperShade(assign = planetShader)
