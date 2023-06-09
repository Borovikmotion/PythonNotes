import maya.cmds as cmds
import json 

json_path = "D:/Scripts/ComparePoses"
poseName = "A_Zmb_Fat_Idle_Agro"
jsonData = {}


def findNameSpace(self):
    testJointFullName = cmds.ls(type="joint")[0]
    if len(testJointFullName.split(":")) == 2:
        self.nameSpace = testJointFullName.split(":")[0] + ":"
    elif len(testJointFullName.split(":")) == 1:
        self.nameSpace = ""
    # apply namespace to the object name
    self.objectCtrl = self.nameSpace + self.objName
    self.exportBone = self.nameSpace + "root"



# get all joints in rig 
def getControls(rootJoint = "root"):
    children = cmds.listRelatives(rootJoint, children = 1, fullPath = 1, allDescendents = 1)
    controls = []
    for i in children:
        if cmds.nodeType(i) == "joint":
            transform = cmds.listRelatives(i, parent = 1, fullPath =1)[0]
            controls.append(transform)
    return controls

def write_json(path, name):
    with open (path + "/" + name + ".json", "w") as f:
        f.write(json.dumps(jsonData, indent = 4, sort_keys = True))



def main():
    controls = getControls()
    # get list of keyable channels and add control to a json
    for ctrl in controls:
        jsonData[ctrl] = {}
        channels = cmds.listAttr(ctrl, keyable=1)
        # write down the value of a particular channel and add it to a json
        # fix issue with channels type none
        if channels:
            for ch in channels:
                jsonData[ctrl][ch] = cmds.getAttr(ctrl + "." + ch)
        else:
            continue

    write_json (path = json_path, name = poseName)

main ()

