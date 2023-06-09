import maya.cmds as cmds
import json

PATH = 'C:/Users/volod/Desktop'

def saveDateToJson(pathToFile = None):

    if not PATH:
        cmds.error('Oh PATH does not exist')

    cubes = cmds.listRelatives(cmds.ls(type = 'mesh'), p=1, f=1)

    data = {}

    for i in cubes:

        xfrm = {}

        t = cmds.xform(i, q=1, t=1) # [1234, 435, 45]
        r = cmds.xform(i, q=1, ro=1)
        s = cmds.xform(i, q=1, s=1)

        xfrm['translate'] = t
        xfrm['rotate'] = r
        xfrm['scale'] = s


        data[i] = xfrm

    with open(pathToFile, 'w') as outfile:
        json.dump(data, outfile, indent=4) 



def main():
    pathToSave = cmds.fileDialog2(fileFilter="*.json", dialogStyle=2, caption = "Save Cube Data", startingDirectory = PATH)[0]

    saveDateToJson(pathToFile=pathToSave)



