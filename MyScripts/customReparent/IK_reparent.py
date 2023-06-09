import maya.cmds as cmds

def setLocSizeColor(loc, size=10, color=17):
    name = loc[0]
    cmds.setAttr(name+"Shape.localScaleX", size)
    cmds.setAttr(name+"Shape.localScaleY", size)
    cmds.setAttr(name+"Shape.localScaleZ", size)
    cmds.setAttr(name+"Shape.overrideEnabled", 1)
    cmds.setAttr(name+"Shape.overrideColor", color)


# get timeline
minT = cmds.playbackOptions(q=1, min =1)
maxT = cmds.playbackOptions(q=1, max =1)

# get selected objects
selectedObjects = cmds.ls(sl=1, l =1)

if len(selectedObjects)==3:
    startJoint = selectedObjects[0]
    midJoint = selectedObjects[1]
    endJoint = selectedObjects[2]
else:
    cmds.error("Plese select 3 joints - hip, shin and foot")

# constraint end joint to a locator 
footLoc = cmds.spaceLocator(n="IK_LOC")
con = cmds.parentConstraint(endJoint, footLoc, mo=0)

# calculate point in the middle between hip and foot 
startJointPos = cmds.xform(startJoint, t=1, ws=1, q=1)
endJointPos = cmds.xform(endJoint, t=1, ws=1, q=1)
startLocPosX = startJointPos[0] - (startJointPos[0] - endJointPos[0])*0.5
startLocPosY = startJointPos[1] - (startJointPos[1] - endJointPos[1])*0.5
startLocPosZ = startJointPos[2] - (startJointPos[2] - endJointPos[2])*0.5
startLocPos = [startLocPosX,startLocPosY,startLocPosZ]

# tempStLoc = cmds.spaceLocator(n="tempSt_LOC")
# cmds.xform(tempStLoc, t = startLocPos)

# get knee point and extrapolate poleVector
midLocPos = cmds.xform(midJoint, t=1, ws=1, q=1)
endLocPosX = startLocPos[0] - (startLocPos[0] - midLocPos[0])*3
endLocPosY = startLocPos[1] - (startLocPos[1] - midLocPos[1])*3
endLocPosZ = startLocPos[2] - (startLocPos[2] - midLocPos[2])*3
endLocPos = [endLocPosX, endLocPosY, endLocPosZ]

tempEndLoc = cmds.spaceLocator(n="tempEnd_LOC")
cmds.xform(tempEndLoc, t = endLocPos)
tmpCon = cmds.parentConstraint(startJoint, tempEndLoc, mo=1)

# pole vector loc
poleVectorLoc = cmds.spaceLocator(n="PoleVector_LOC")
cmds.xform(poleVectorLoc, t = endLocPos)
tmpCon = cmds.parentConstraint(startJoint, tempEndLoc, mo=1)
pvCon = cmds.pointConstraint(tempEndLoc, poleVectorLoc, mo=0)

# cmds.parent(poleVectorLoc, footLoc)

# bake animation on foot and polevector loc
cmds.bakeResults(footLoc, poleVectorLoc, time = (minT,maxT))
cmds.delete(con,tmpCon,pvCon,tempEndLoc)

# # create ik handle
ikHandle = cmds.ikHandle(n=startJoint+"IK", sj=startJoint, ee=endJoint)
cmds.parent(ikHandle[0], footLoc)
cmds.orientConstraint(footLoc, endJoint, mo=0)
cmds.poleVectorConstraint(poleVectorLoc, ikHandle[0])

# make locators bigger and different color 
setLocSizeColor(footLoc)
setLocSizeColor(poleVectorLoc, size = 5, color = 9)

# select ik control
cmds.select(footLoc)
