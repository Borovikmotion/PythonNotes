# _______CREATE SIMPLE WINDOW_______
import maya.cmds as cmds

def createWindow():
    # cleanup old window
    if cmds.window("CusotmWindowName", exists=1):
        cmds.deleteUI("CusotmWindowName")
    # cleanup old data
    if cmds.windowPref("CusotmWindowName", exists=1):
        cmds.windowPref("CusotmWindowName", remove=1)

    # create new window
    cmds.window("CusotmWindowName", title = "my window", width=400, height=300, toolbox=False)

    # show window
    cmds.showWindow("CusotmWindowName")

createWindow()
