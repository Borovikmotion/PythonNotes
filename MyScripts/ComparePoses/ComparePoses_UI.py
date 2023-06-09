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
        self.useSelection = cmds.checkBox(useSelectionCheckBox, q=1, v=True)
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
        if self.useSelection == False:
            joints = self.getJoints(rootJoint = self.nameSpace + self.rootJoint)
        else:
            joints = self.getJoints(rootJoint = cmds.ls(sl=1))
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
    def __init__(self, path, refName, currentName):
        self.json_path = path
        self.poseRefName = refName
        self.poseCurrentName = currentName
        self.rootJoint = "root"
        self.jsonRefData = {}
        self.jsonCurrentData = {}
        self.jsonCompareData = {}
        self.nameSpace = ""
        self.result = ["Success! Poses Have Matched!"]

        self.positionThreshold = float(cmds.textField("ThresholdPositionTextFieldID", q=1, text=1))
        self.rotationThreshold = float(cmds.textField("ThresholdRotationTextFieldID", q=1, text=1))
        self.scaleThreshold = float(cmds.textField("ThresholdScaleTextFieldID", q=1, text=1))
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

# _______ UI ________
windowName = "ComparePosesWindowID"
panelWidth = 550
panelHeight = 320

# cleanup
if cmds.window(windowName, exists=1):
    cmds.deleteUI(windowName)
if cmds.windowPref(windowName, exists=1):
    cmds.windowPref(windowName, remove=1)

# create new
cmds.window(windowName, title = "Compare Poses v 1.0", width=panelWidth, height=panelHeight, toolbox=False)

# text on top
mainLayout = cmds.columnLayout()
# cmds.textField("ReferencePoseCommentTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Here you need to enter a full path to the reference pose, with necessarily '/' this slash", ed =0)
# ReferencePoseTextField  = cmds.textField("ReferencePoseTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Reference Pose Full Path", it = "C:/perforce/zombie_art/Characters/Creatures/Zmb_Fat_01/animation/source/Movement_Agro/Movement/A_Zmb_Fat_Idle_Agro.ma")

# ref pose
cmds.textField("PosesPathCommentTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Any directory, will be used to save poses .json files and LOG", ed=0)
PosesPathTextField  = cmds.textField("PosesPathTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Json Path", it = "C:\Poses")

cmds.textField("ReferencePoseCommentTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Name of a reference pose", ed=0)
ReferencePoseTextField  = cmds.textField("ReferencePoseTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Reference Pose Name", it = "A_Zmb_Fat_Idle_Agro")
cmds.button("saveReferencePoseButtonName", w = panelWidth, label = "Save Reference Pose", parent = mainLayout, command = "SaveReferencePose()", statusBarMessage = "Save" )

# threshold
cmds.textField("ThresholdCommentTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Values of acceptible delta for position (centimeters), rotation (degress), and scale. Should be > 0", ed=0)
ThresholdPositionTextField  = cmds.textField("ThresholdPositionTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Threshold Position", it = "3")
ThresholdRotationTextField  = cmds.textField("ThresholdRotationTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Threshold Rotation", it = "3")
ThresholdScaleTextField  = cmds.textField("ThresholdScaleTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Threshold Scale", it = "0.01")

# current pose
cmds.textField("CurrentPoseCommentTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Name of a current pose", ed =0)
currentFileFullName = cmds.file(sn =1, q=1)
currentPosePlaseholderName = currentFileFullName.split("/")[-1].split(".")[0]

ReferencePoseTextField  = cmds.textField("CurrentPoseTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Current Pose Name", it = currentPosePlaseholderName)

useSelectionCheckBox = cmds.checkBox( label='Use Selected Root Joint', parent = mainLayout)

# main buttons
buttonsLayout = cmds.rowLayout(numberOfColumns=2, parent = mainLayout)
compareButtonName = "compareOBjectButtonID"
cmds.button(compareButtonName, w = panelWidth, label = "Compare Poses", parent = buttonsLayout, command = "comparePosesCommand()", statusBarMessage = "Compare" )

# result text
ResultCommentTextField  = cmds.textField("ResultCommentTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "TResult", it = "The result of compare will be shown here", ed=0)
ResultTextField  = cmds.textField("ResultTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Result")
ResultDetailsTextField  = cmds.textField("ResultDeatailsTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Result Details")

# show window
cmds.showWindow(windowName)


# ______ Main Functions ________
def SaveReferencePose():
    # save current pose
    posesPath = cmds.textField("PosesPathTextFieldID", q=1, text=1)
    if not os.path.isdir(posesPath):
        os.mkdir(posesPath)
    
    refFileShortName = cmds.textField("ReferencePoseTextFieldID", q=1, text=1)
    refPose = SavePose(path = posesPath, name = refFileShortName)

def comparePosesCommand():
    result = {}
    posesPath = cmds.textField("PosesPathTextFieldID", q=1, text=1)
    if not os.path.isdir(posesPath):
        os.mkdir(posesPath)

    fileShortName = cmds.textField("CurrentPoseTextFieldID", q=1, text=1)
    currentPose = SavePose(path = posesPath, name = fileShortName)

    # compare current and ref pose
    refFileShortName = cmds.textField("ReferencePoseTextFieldID", q=1, text=1) 
    ComparedCurrentPose = ComparePoses(path = posesPath, refName = refFileShortName, currentName = fileShortName)
    result[fileShortName] = ComparedCurrentPose.result

    # save log
    with open (posesPath + "/" + "LOG" + ".json", "w") as f:
        f.write(json.dumps(result, indent = 4, sort_keys = True))

    textResult = str(result[fileShortName][0])
    if textResult[0] != "S":
        textResult = textResult + " Open Log for full details"
    cmds.textField("ResultTextFieldID", tx = textResult, e=1)

    textResultDetails = ""
    result[fileShortName].pop(0)
    for i in result[fileShortName]:
            textResultDetails = textResultDetails + i + "; "
            # print (i) 

    cmds.textField("ResultDeatailsTextFieldID", tx = textResultDetails, e=1)