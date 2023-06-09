import maya.cmds as cmds
import json 

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


refPose = SavePose(path = "D:/Scripts/ComparePoses", name = "A_Zmb_Fat_Idle_Agro")

