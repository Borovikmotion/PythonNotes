import maya.cmds as cmds
import json 

json_path = "D:/Scripts/03/poses"
poseName = "Pose3"
jsonData = {}


# read json
def read_json(path, name):
    with open (path + "/" + name + ".json", "r") as f:
        jsonData  = json.load(f)
    return jsonData

# get selected controls
def getControls(rig = "zoma_base_rig"):

    selectedObjects = cmds.ls(sl=1, l = 0)
    if selectedObjects:
        controls = []
        for i in selectedObjects:
            controls.append(i)
            jsonData[i] = {}

    else:
        cmds.error("please select controls")

    return controls


def main():

    jsonData = read_json(path = json_path, name = poseName)
    controls = getControls()

    # apply data from json to selected controls
    for ctrl in controls:

        recordedChannels = jsonData[ctrl]

        for rCh in recordedChannels:
            cmds.setAttr(ctrl + "." + rCh, recordedChannels[rCh])

main()
