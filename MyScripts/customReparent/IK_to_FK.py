import maya.cmds as cmds

# get timeline
minT = cmds.playbackOptions(q=1, min=1)
maxT = cmds.playbackOptions(q=1, max=1)
currentT = cmds.currentTime(q=1)

# get selected object name
selectedObjFullName = cmds.ls(sl=1, l=0)

if selectedObjFullName:
    if len(selectedObjFullName[0].split(":")) == 2:
        selectedObjName = selectedObjFullName[0].split(":")[-1]
        nameSpace = selectedObjFullName[0].split(":")[0] + ":"
    elif len(selectedObjFullName[0].split(":")) == 1:
        selectedObjName = selectedObjFullName[0].split(":")[-1]
        nameSpace = ""
else:
    cmds.error("Please select IK control")

# define what body part is it
if selectedObjName == "IKArm_L":
    ikSwitcher = nameSpace + "FKIKArm_L"
    startJoint = nameSpace + "upperarm_l"
    midJoint = nameSpace + "lowerarm_l"
    endJoint = nameSpace + "hand_l"
    startFK = nameSpace + "FKShoulder_L"
    midFK = nameSpace + "FKElbow_L"
    endFK = nameSpace + "FKWrist_L"

elif selectedObjName == "IKArm_R":
    ikSwitcher = nameSpace + "FKIKArm_R"
    startJoint = nameSpace + "upperarm_r"
    midJoint = nameSpace + "lowerarm_r"
    endJoint = nameSpace + "hand_r"
    startFK = nameSpace + "FKShoulder_R"
    midFK = nameSpace + "FKElbow_R"
    endFK = nameSpace + "FKWrist_R"

elif selectedObjName == "IKLeg_L":
    ikSwitcher = nameSpace + "FKIKLeg_L"
    startJoint = nameSpace + "thigh_l"
    midJoint = nameSpace + "calf_l"
    endJoint = nameSpace + "foot_l"
    startFK = nameSpace + "FKHip_L"
    midFK = nameSpace + "FKKnee_L"
    endFK = nameSpace + "FKAnkle_L"

elif selectedObjName == "IKLeg_R":
    ikSwitcher = nameSpace + "FKIKLeg_R"
    startJoint = nameSpace + "thigh_r"
    midJoint = nameSpace + "calf_r"
    endJoint = nameSpace + "foot_r"
    startFK = nameSpace + "FKHip_R"
    midFK = nameSpace + "FKKnee_R"
    endFK = nameSpace + "FKAnkle_R"

else:
    # print selectedObjName
    cmds.error("Something wrong is selected, please select IK control")

# bake joints to locators:
startLocIK = cmds.spaceLocator(n="start_IK_LOC")
midLocIK = cmds.spaceLocator(n="mid_IK_LOC")
endLocIK = cmds.spaceLocator(n="end_IK_LOC")

startConIK = cmds.parentConstraint(startJoint, startLocIK, mo=0)
midConIK = cmds.parentConstraint(midJoint, midLocIK, mo=0)
endConIK = cmds.parentConstraint(endJoint, endLocIK, mo=0)

cmds.bakeResults(startLocIK, midLocIK, endLocIK, time = (minT,maxT))
cmds.delete(startConIK, midConIK, endConIK)

# switch to FK
cmds.setAttr(ikSwitcher+".FKIKBlend", 0) 

# create FK joints locators
startLocFK = cmds.spaceLocator(n="start_FK_LOC")
midLocFK = cmds.spaceLocator(n="mid_FK_LOC")
endLocFK = cmds.spaceLocator(n="end_FK_LOC")

tempStartCon = cmds.parentConstraint(startJoint, startLocFK, mo=0)
tempMidCon = cmds.parentConstraint(midJoint, midLocFK, mo=0)
tempEndCon = cmds.parentConstraint(endJoint, endLocFK, mo=0)
cmds.delete(tempStartCon, tempMidCon, tempEndCon)

startConFK = cmds.parentConstraint(startLocFK, startFK, mo=1)
midConFK = cmds.parentConstraint(midLocFK, midFK, mo=1)
endConFK = cmds.parentConstraint(endLocFK, endFK, mo=1)

# match IK and FK locators
ikFkStartCon = cmds.parentConstraint(startLocIK, startLocFK, mo=0)
ikFkMidCon = cmds.parentConstraint(midLocIK, midLocFK, mo=0)
ikFkEndCon = cmds.parentConstraint(endLocIK, endLocFK, mo=0)

# bake FK controls
cmds.bakeResults(startFK, midFK, endFK, time = (minT,maxT))
cmds.delete(startLocIK, midLocIK, endLocIK, startLocFK, midLocFK, endLocFK)

# euler filter (doesnt work for now because of weird channels names)
# startFKCrv = startFK.split(":")[-1]
# midFKCrv = midFK.split(":")[-1]
# endFKCrv = endFK.split(":")[-1]

# cmds.filterCurve(startFKCrv + "_rotateX", startFKCrv + "_rotateY", startFKCrv + "_rotateZ")
# cmds.filterCurve(midFKCrv + "_rotateX", midFKCrv + "_rotateY", midFKCrv + "_rotateZ")
# cmds.filterCurve(endFKCrv + "_rotateX", endFKCrv + "_rotateY", endFKCrv + "_rotateZ")

# cmds.selectKey (clear) ;
# FKElbow_L.rotateY
# FKElbow_L_rotateX

cmds.currentTime(currentT)
