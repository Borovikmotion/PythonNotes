import maya.cmds as cmds
import json 

json_path = "D:/Scripts/03/poses"
poseName = "Pose4"
jsonData = {}

# get all controls in rig 
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
