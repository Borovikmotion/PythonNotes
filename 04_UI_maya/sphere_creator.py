# _______CREATE SIMPLE WINDOW_______
import maya.cmds as cmds

def createSphere():
    # a command to run by a button
    SphName = cmds.textField("SomeIDTextField", q=1, text=1)
    cmds.polySphere(n=SphName)

def createWindow():
    # cleanup old window
    if cmds.window("CusotmWindowName", exists=1):
        cmds.deleteUI("CusotmWindowName")
    # cleanup old data
    if cmds.windowPref("CusotmWindowName", exists=1):
        cmds.windowPref("CusotmWindowName", remove=1)

    # create new window
    cmds.window("CusotmWindowName", title = "my window", width=400, height=300, toolbox=False)

    # layouts
    myLayout = cmds.columnLayout()
    # show some text
    myTextField  = cmds.textField("SomeIDTextField", parent = myLayout, width = 200, placeholderText = "SphereName")
    # create button
    cmds.button("myButtonID", label = "create sphere", parent = myLayout, command = "createSphere()", statusBarMessage = "Hello" )

    # show window
    cmds.showWindow("CusotmWindowName")

createWindow()
