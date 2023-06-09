import maya.cmds as cmds
import json
import maya.mel as mel
import os
import maya.standalone
import sys 

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
            jntShortName = jnt.split(":")[1]
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
    def __init__(self, path, refName, currentName):
        self.json_path = path
        self.poseRefName = refName
        self.poseCurrentName = currentName
        self.rootJoint = "root"
        self.jsonRefData = {}
        self.jsonCurrentData = {}
        self.jsonCompareData = {}
        self.nameSpace = ""
        self.result = [True]

        self.positionThreshold = 3
        self.rotationThreshold = 6
        self.scaleThreshold = 0.001
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
                                self.result[0] = False
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
                                self.result[0] = False
                                log = jnt + " " + ch + " " + str(abs(rec - cur)) + ' Mismatch'
                                # self.result.append(str(jnt, ch, abs(recordedChannels[ch] - currentChannels[ch]), 'Mismatch'))
                                self.result.append(log)
                        
                        elif ch[0] == "s":
                            matchingDelta = abs(recordedChannels[ch] - currentChannels[ch])/self.scaleThreshold
                            if matchingDelta > 1:
                                self.result[0] = False
                                log = jnt + " " + ch + " " + str(abs(recordedChannels[ch] - currentChannels[ch])) + ' Mismatch'
                                # self.result.append(str(jnt, ch, abs(recordedChannels[ch] - currentChannels[ch]), 'Mismatch'))
                                self.result.append(log)


# UI
windowName = "ComparePosesWindowID"
panelWidth = 800
panelHeight = 400

# cleanup
if cmds.window(windowName, exists=1):
    cmds.deleteUI(windowName)
if cmds.windowPref(windowName, exists=1):
    cmds.windowPref(windowName, remove=1)

# create new
cmds.window(windowName, title = "Compare Poses v 1.0", width=panelWidth, height=panelHeight, toolbox=False)

# text on top
mainLayout = cmds.columnLayout()
cmds.textField("ReferencePoseCommentTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Here you need to enter a full path to the reference pose, with necessarily '/' this slash", ed =0)
ReferencePoseTextField  = cmds.textField("ReferencePoseTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Reference Pose Full Path", it = "C:/perforce/zombie_art/Characters/Creatures/Zmb_Fat_01/animation/source/Movement_Agro/Movement/A_Zmb_Fat_Idle_Agro.ma")

cmds.textField("PosesPathCommentTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Any directory, will be used to save poses .json files and LOG", ed =0)
PosesPathTextField  = cmds.textField("PosesPathTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Json Path", it = "C:/Users/borov/Desktop/Poses")

cmds.textField("ThresholdCommentTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "These are values of acceptible delta for position, rotation, and scale", ed =0)

ThresholdPositionTextField  = cmds.textField("ThresholdPositionTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Threshold Position", it = "3")
ThresholdRotationTextField  = cmds.textField("ThresholdRotatiuonFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Threshold Rotation", it = "5")
ThresholdScaleTextField  = cmds.textField("ThresholdScaleFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Threshold Scale", it = "0.01")

# main buttons
buttonsLayout = cmds.rowLayout(numberOfColumns=2, parent = mainLayout)
compareButtonName = "compareOBjectButtonID"

# canButtonName ="CancelButtonID"

cmds.button(compareButtonName, w = panelWidth, label = "Compare Poses", parent = buttonsLayout, command = "main()", statusBarMessage = "Compare" )

# show window
cmds.showWindow(windowName)



def main():
    result = {}
    posesPath = cmds.textField("PosesPathTextFieldID", q=1, text=1)

    # save current pose
    fileShortName = "CurrentPose"
    currentPose = SavePose(path = posesPath, name = "CurrentPose")

    # # open maya 
    # maya.standalone.initialize(name="python")

    # ref pose
    refPath = cmds.textField("ReferencePoseTextFieldID", q=1, text=1)
    refFileShortName = (refPath.split("/")[-1]).split(".")[0]

    # save ref pose
    cmds.file(refPath, open = True)
    refPose = SavePose(path = posesPath, name = refFileShortName)

    # compare current and ref pose 
    ComparedCurrentPose = ComparePoses(path = posesPath, refName = refFileShortName, currentName = fileShortName)
    result[fileShortName] = ComparedCurrentPose.result

    # # close maya
    # maya.standalone.uninitialize()
    # # print (mayaFiles.files)

    # save log
    with open (posesPath + "/" + "LOG" + ".json", "w") as f:
        f.write(json.dumps(result, indent = 4, sort_keys = True))

















# _____BATCH_COMPARE_____
# result = {}
# mayaFiles = GetMayaFiles(path = "D:/Scripts/ComparePoses/poses")

# # open maya 
# maya.standalone.initialize(name="python")
# # cmds.file("D:/Scripts/ComparePoses/poses/A_Zmb_Fat_Idle_Agro.ma", open = True)
# # refPose = SavePose(path = "D:/Scripts/ComparePoses/poses", name = "A_Zmb_Fat_Idle_Agro")

# for mf in mayaFiles.files:
#     fileShortName = (mf.split("/")[-1]).split(".")[0]
#     # cmds.file(mf, open = True)
#     # SavePose(path = "D:/Scripts/ComparePoses/poses", name = fileShortName)
#     CurrentPose = ComparePoses(path = "D:/Scripts/ComparePoses/poses", refName = "A_Zmb_Fat_Idle_Agro", currentName = fileShortName)
#     result[fileShortName] = CurrentPose.result

# # close maya
# maya.standalone.uninitialize()
# # print (mayaFiles.files)

# print ("\n\n\nOutput:\n")
# for key, value in result.items():
#     print ("\n" + str(key) + ': ')
#     for i in value:
#         print (str(i))

# with open ("D:/Scripts/ComparePoses/poses" + "/" + "LOG" + ".json", "w") as f:
#     f.write(json.dumps(result, indent = 4, sort_keys = True))



# # currentPose = SavePose(path = "D:/Scripts/ComparePoses", name = "A_Zmb_Fat_Turn_Agro_L45")
# # currentPose = SavePose(path = "D:/Scripts/ComparePoses", name = "CurrentPose")
# # ComparePoses(path = "D:/Scripts/ComparePoses", refName = "A_Zmb_Fat_Idle_Agro", currentName = "CurrentPose")
