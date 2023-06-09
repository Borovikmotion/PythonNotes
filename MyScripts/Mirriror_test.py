import maya.cmds as cmds

minT = cmds.playbackOptions(q=1, min=1)
maxT = cmds.playbackOptions(q=1, max=1)


allJoints = cmds.ls(sl=1)
jointLocators = []
index_L = "L"
index_R = "R"

# get namespace
selectedObjFullName = cmds.ls(sl=1, l=0)[0]
if selectedObjFullName:
    if len(selectedObjFullName[0].split(":")) == 2:
        selectedObjName = selectedObjFullName[0].split(":")[-1]
        nameSpace = selectedObjFullName[0].split(":")[0] + ":"
    elif len(selectedObjFullName[0].split(":")) == 1:
        selectedObjName = selectedObjFullName[0].split(":")[-1]
        nameSpace = ""

# get list of objects
# allJoints = cmds.ls(type="joint")

# for all objects - create locators and bake animation
for joint in allJoints:
    jointLoc = cmds.spaceLocator(n= joint + "_LOC")[0]
    jointCon = cmds.parentConstraint(joint, jointLoc, mo=0)
    jointLocators.append(jointLoc)
    cmds.bakeResults(jointLoc, time = (minT,maxT))
    cmds.delete(jointCon)

grp = cmds.group(empty = 1)

# for all created locators 
for jLoc in jointLocators:

    # ctreate aim forward and upward locators
    aimLocF = cmds.spaceLocator(n= jLoc + "_AIM_F")
    aimLocUP = cmds.spaceLocator(n= jLoc + "_AIM_UP")
    cmds.parent(aimLocF, jLoc)
    cmds.parent(aimLocUP, jLoc)
    cmds.xform(aimLocF, t = [10,0,0], ro = [0,0,0])
    cmds.xform(aimLocUP, t = [0,10,0], ro = [0,0,0])
    cmds.parent(aimLocF, w=1)
    cmds.parent(aimLocUP, w=1)
    conF = cmds.parentConstraint(jLoc, aimLocF, mo=1)
    conUP = cmds.parentConstraint(jLoc, aimLocUP, mo=1)
    cmds.bakeResults(aimLocF, time = (minT,maxT))
    cmds.bakeResults(aimLocUP, time = (minT,maxT))
    cmds.delete(conF, conUP)

    # crete final loc without animatiuon 
    finalLoc = cmds.spaceLocator(n= jLoc + "_Final")
    cmds.parent(finalLoc, jLoc)
    cmds.xform(finalLoc, t = [0,0,0], ro = [0,0,0])
    cmds.parent(finalLoc, w=1)

    # parent locators to the mirror group 
    cmds.parent(jLoc, grp)
    cmds.parent(aimLocF, grp)
    cmds.parent(aimLocUP, grp)

    # constraint final locator to a group locator
    pointCon = cmds.pointConstraint(jLoc, finalLoc, mo=0)
    aimCon = cmds.aimConstraint(aimLocF, finalLoc, mo=1, worldUpType = "object", worldUpObject = aimLocUP[0])

rightJoints = []
leftJoints = []
exceptions = []
nonPairJoints = []

for joint in allJoints:
    if joint[-1] == index_R:
        rightJoints.append(joint)
    elif joint[-1] == index_L:
        leftJoints.append(joint)
    elif joint == "l_FullHand" or joint == "l_FullHand_End" or joint == "r_FullHand" or joint == "r_FullHand_End":
        exceptions.append(joint)
    else:
        nonPairJoints.append(joint)


cmds.xform(grp, scale = [-1, 1, 1])

for joint in rightJoints:
    oppositeJointName = joint[:-1] + index_L
    loc = oppositeJointName + "_LOC" + "_Final"
    if oppositeJointName:
        translateChannelsStatus = cmds.getAttr(joint + ".translateX", keyable=1)
        rotateChannelsStatus = cmds.getAttr(joint + ".rotateX", keyable=1) 
        if translateChannelsStatus:
            cmds.pointConstraint(loc, joint, mo=0)
        if rotateChannelsStatus:
            cmds.orientConstraint(loc, joint, offset=[180,180,0])

for joint in leftJoints:
    oppositeJointName = joint[:-1] + index_R
    loc = oppositeJointName + "_LOC" + "_Final"
    if oppositeJointName:
        translateChannelsStatus = cmds.getAttr(joint + ".translateX", keyable=1)
        rotateChannelsStatus = cmds.getAttr(joint + ".rotateX", keyable=1)
        if translateChannelsStatus:
            cmds.pointConstraint(loc, joint, mo=0)
        if rotateChannelsStatus:
            cmds.orientConstraint(loc, joint, offset=[180,180,0])

for joint in nonPairJoints:
    loc = joint + "_LOC" + "_Final"
    translateChannelsStatus = cmds.getAttr(joint + ".translateX", keyable=1)
    rotateChannelsStatus = cmds.getAttr(joint + ".rotateX", keyable=1)
    if translateChannelsStatus and rotateChannelsStatus:
        # cmds.parentConstraint(loc, joint, mo=0)
        cmds.pointConstraint(loc, joint, mo=0)
        cmds.orientConstraint(loc, joint, offset=[180,180,0])

