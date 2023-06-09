# _______ TOOL BAR _________

import maya.cmds as cmds

if cmds.window("MyToolBarID", exists = 1):
    cmds.deleteUI("MyToolBarID")

if cmds.windowPref("MyToolBarID", exists = 1):
    cmds.windowPref("MyToolBarID", remove = True)

if cmds.toolBar("MyToolBarID", exists = 1):
    cmds.deleteUI("MyToolBarID")


contentWindow = cmds.window("MyToolBarID", sizeable = True)
mainLayout = cmds.formLayout("MyToolBarIDLayout", parent=contentWindow)
cmds.toolBar("MyToolBarID", area="bottom", content=contentWindow, allowedArea = ["bottom"])

def run():
    cmds.polySphere()

ff = cmds.rowLayout(numberOfColumns = 10, parent = mainLayout, height = 37)
cmds.iconTextButton(style = "textOnly", w = 50, h = 30, command = run, label = "My Button")
cmds.popupMenu()
cmds.menuItem(label = "createSphere", command = "run()",)
cmds.menuItem(label = "createMoreSphere ", command = "run()",)
cmds.menuItem(label = "chechbox", checkBox = 1, c = "run()")

