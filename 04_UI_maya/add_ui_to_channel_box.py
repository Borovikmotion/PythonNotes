# ________ ADD SOMETHJING TO MAYA UI (CHANNELBOX)_________
import maya.cmds as cmds

UIName = "MyWindowName"

def myLayout():
    cmds.columnLayout()
    cmds.button()
    cmds.button()
    cmds.button()

# cleanup old window
if cmds.workspaceControl(UIName, exists=1):
    cmds.deleteUI(UIName, control=1)
    cmds.workspaceControlState(UIName, remove=1)

cmds.workspaceControl(UIName, label = "MyProject", r=1, tabToControl = ["AttributeEditor", -1], initialWidth = 400, minimumWidth = True, widthProperty = "preferred", uiScript = "myLayout()")