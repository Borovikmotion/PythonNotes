import maya.cmds as cmds
import json
import maya.mel as mel
import os
import maya.standalone
import sys 

# _______ ENTER YOUR VALUES HERE ________

# path
path_to_maya_files = "D:/Scripts/ComparePoses/poses"
path_to_poses = "C:/Poses"
full_path_to_reference_pose = "D:/Scripts/ComparePoses/poses/A_Zmb_Fat_Idle_Agro.ma"

# comparing threshold, should be > 0
position_threshold = 3
rotation_threshold = 3
scale_threshold = 0.01
# _________________________________________

class GetMayaFiles(object):
    def __init__(self, path):
        self.path = path
        self.files = []
        self.getFiles()

    def getFiles(self):
        if not os.path.isdir(self.path):
            raise ValueError("the path does not exist")
        for i in os.listdir(self.path):
            fileName, fileExt = os.path.splitext(i)
            if fileExt == ".ma" or fileExt == ".mb":
                fullPath = self.path + "/" + i
                self.files.append(fullPath)
        if not self.files:
            print ("there are no acceptable files")
            return self.files

class SavePose(object):
    def __init__(self, path, name):
        self.json_path = path
        self.poseName = name
        self.rootJoint = "root"
        self.jsonData = {}
        self.nameSpace = ""
        self.findNameSpace()
        self.main()

    def findNameSpace(self):
        testJointFullName = cmds.ls(type="joint")[0]
        if len(testJointFullName.split(":")) == 2:
            self.nameSpace = testJointFullName.split(":")[0] + ":"
        elif len(testJointFullName.split(":")) == 1:
            self.nameSpace = ""

    # get all joints in rig 
    def getJoints(self, rootJoint):
        children = cmds.listRelatives(rootJoint, children = 1, fullPath = 1, allDescendents = 1)
        joints = []
        for i in children:
            if cmds.nodeType(i) == "joint":
                transform = cmds.listRelatives(i, parent = 1, fullPath = 0)[0]
                joints.append(transform)
        return joints

    def write_json(self, path, name):
        with open (path + "/" + name + ".json", "w") as f:
            f.write(json.dumps(self.jsonData, indent = 4, sort_keys = True))

    def main(self):
        joints = self.getJoints(rootJoint = self.nameSpace + self.rootJoint)
        # get list of keyable channels and add control to a json
        for jnt in joints:
            if len(jnt.split(":")) == 2:
                jntShortName = jnt.split(":")[1]
            elif len(jnt.split(":")) == 1:
                jntShortName = jnt
            self.jsonData[jntShortName] = {}
            channels = cmds.listAttr(jnt, keyable=1)
            # write down the value of a particular channel and add it to a json
            # fix issue with channels type none
            if channels:
                for ch in channels:
                    self.jsonData[jntShortName][ch] = cmds.getAttr(jnt + "." + ch)
            else:
                continue
        self.write_json (path = self.json_path, name = self.poseName)

class ComparePoses(object):
    def __init__(self, path, refName, currentName, posThr, rotThr, scThr):
        self.json_path = path
        self.poseRefName = refName
        self.poseCurrentName = currentName
        self.rootJoint = "root"
        self.jsonRefData = {}
        self.jsonCurrentData = {}
        self.jsonCompareData = {}
        self.nameSpace = ""
        self.result = ["Success! Poses Have Matched!"]

        self.positionThreshold = posThr
        self.rotationThreshold = rotThr
        self.scaleThreshold = scThr
        # self.findNameSpace()
        self.main()

    # read json
    def read_json(self, path, name):
        with open (path + "/" + name + ".json", "r") as f:
            jsonData  = json.load(f)
        return jsonData

    def main(self):
        self.jsonRefData = self.read_json(path = self.json_path, name = self.poseRefName)
        self.jsonCurrentData = self.read_json(path = self.json_path, name = self.poseCurrentName)

        joints = []
        for i in self.jsonRefData.keys():
            joints.append(i)

        for jnt in joints:
            if jnt != "root":
                recordedChannels = self.jsonRefData[jnt]
                currentChannels = self.jsonCurrentData[jnt]
                
                for ch in recordedChannels.keys():
                    if type(recordedChannels[ch]) == float:
                        if ch[0] == "t":
                            matchingDelta = abs(recordedChannels[ch] - currentChannels[ch])/self.positionThreshold
                            if matchingDelta > 1:
                                self.result[0] = "Mismatch Detected: "
                                log = jnt + " " + ch + " " + str(abs(recordedChannels[ch] - currentChannels[ch])) + ' Mismatch'
                                # self.result.append(str(jnt, ch, abs(recordedChannels[ch] - currentChannels[ch]), 'Mismatch'))
                                self.result.append(log)
                        
                        elif ch[0] == "r":
                            if recordedChannels[ch]>360:
                                rec = recordedChannels[ch] - round((recordedChannels[ch]/360))*360
                            elif recordedChannels[ch]<360:
                                rec = recordedChannels[ch] - round((recordedChannels[ch]/360))*360
                            else: rec = recordedChannels[ch]
                            if currentChannels[ch]>360:
                                cur = currentChannels[ch] - round((currentChannels[ch]/360))*360
                            elif currentChannels[ch]<360:
                                cur = currentChannels[ch] - round((currentChannels[ch]/360))*360
                            else: cur = currentChannels[ch]
                            matchingDelta = abs(rec - cur)/self.rotationThreshold
                            if matchingDelta > 1:
                                self.result[0] = "Mismatch Detected: "
                                log = jnt + " " + ch + " " + str(abs(rec - cur)) + ' Mismatch'
                                # self.result.append(str(jnt, ch, abs(recordedChannels[ch] - currentChannels[ch]), 'Mismatch'))
                                self.result.append(log)
                        
                        elif ch[0] == "s":
                            matchingDelta = abs(recordedChannels[ch] - currentChannels[ch])/self.scaleThreshold
                            if matchingDelta > 1:
                                self.result[0] = "Mismatch Detected: "
                                log = jnt + " " + ch + " " + str(abs(recordedChannels[ch] - currentChannels[ch])) + ' Mismatch'
                                # self.result.append(str(jnt, ch, abs(recordedChannels[ch] - currentChannels[ch]), 'Mismatch'))
                                self.result.append(log)


result = {}
# get maya files
mayaFiles = GetMayaFiles(path = path_to_maya_files)

# check dir
if not os.path.isdir(path_to_poses):
    os.mkdir(path_to_poses)

# open maya 
maya.standalone.initialize(name="python")

# open ref file and save ref pose 
cmds.file(full_path_to_reference_pose, open = True)
refPoseShortName = full_path_to_reference_pose.split("/")[-1].split(".")[0]
refPose = SavePose(path = path_to_poses, name = refPoseShortName)

# compare
for mf in mayaFiles.files:
    fileShortName = (mf.split("/")[-1]).split(".")[0]
    cmds.file(mf, open = True, force = True)
    minT = cmds.playbackOptions(q=1, min=1)
    maxT = cmds.playbackOptions(q=1, max=1)

    cmds.currentTime(minT, edit=True)
    SavePose(path = path_to_poses, name = fileShortName + "_first_frame")
    firtstFramePose = ComparePoses(path = path_to_poses, refName = refPoseShortName, currentName = fileShortName + "_first_frame", posThr = position_threshold, rotThr = rotation_threshold, scThr = scale_threshold)
    result[fileShortName + "_first_frame"] = firtstFramePose.result

    cmds.currentTime(maxT, edit=True)
    SavePose(path = path_to_poses, name = fileShortName + "_last_frame")
    lastFramePose = ComparePoses(path = path_to_poses, refName = refPoseShortName, currentName = fileShortName + "_last_frame", posThr = position_threshold, rotThr = rotation_threshold, scThr = scale_threshold)
    result[fileShortName + "_last_frame"] = lastFramePose.result

# close maya
maya.standalone.uninitialize()
# print (mayaFiles.files)

print ("\n\n\nOutput:\n")
for key, value in result.items():
    print ("\n" + str(key) + ': ')
    for i in value:
        print (str(i))

with open (path_to_poses + "/" + "LOG" + ".json", "w") as f:
    f.write(json.dumps(result, indent = 4, sort_keys = True))
