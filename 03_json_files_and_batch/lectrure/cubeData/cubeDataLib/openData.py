import maya.cmds as cmds
import json

PATH = 'C:/Users/volod/Desktop'

def openDateToJson(pathToFile = None):

    if not PATH:
        cmds.error('Oh PATH does not exist')

    json_data = None
    with open(pathToFile, 'r') as f:
        json_data = json.load(f)

    for i in json_data:

        cmds.polyCube(name = i)

        tr = json_data[i]['translate']
        rt = json_data[i]['rotate']
        sc = json_data[i]['scale']

        cmds.xform(i, t = tr)
        cmds.xform(i, ro = rt)
        cmds.xform(i, s = sc)


def main():

    cmds.file(new=1, force=1)

    pathToSave = cmds.fileDialog2(fileFilter="*.json", dialogStyle=2, fileMode = 1, caption = "Open Cubes", okCaption = "Load Cubes", startingDirectory = PATH)[0]

    openDateToJson(pathToFile=pathToSave)



