import maya.cmds as cmds

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
