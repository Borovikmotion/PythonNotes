
# _____LAYOUTS_______

import maya.cmds as cmds


def createWindow():
    UIName = "MyWindowName"

    # cleanup old window
    if cmds.window(UIName , exists=1):
        cmds.deleteUI(UIName )
    # cleanup old data
    if cmds.windowPref(UIName , exists=1):
        cmds.windowPref(UIName , remove=1)

    # create new window
    wnd = cmds.window(UIName , title = "my test window", width=400, height=300, toolbox=False)

    # COLUMN LAYOUT
    # myLayout = cmds.columnLayout(adjustableColumn = 1, rowSpacing = 5)

    # # ROW LAYOUT
    # myLayout = cmds.rowLayout(numberOfColumns =3, cw3=[100,100,50], ct3 = ['both','left','left'], co3 = [0,10,0], cal = (1, 'right'))
    # adjustableColumn3 = 1
    # left, right, both 
    # left right center

    # # FORM LAYOUT
    myLayout = cmds.formLayout(w = 300, h = 200, numberOfDivisions = 100)

    # BUTTONS & text
    # cmds.text(parent = myLayout, label = "hohoho")
    b1 = cmds.button(w = 50, label = "OK", parent = myLayout)
    b2 = cmds.button(w = 50, label = "Apply", parent = myLayout)
    b3 = cmds.button(w = 50, label = "Cancel", parent = myLayout)

    # # move UI elements
    cmds.formLayout(myLayout, e =1, attachForm = [(b1, 'left', 100), (b1, 'top', 50), (b2, 'left', 50), (b2, 'top', 100), ])
    # move element relatively to other object
    cmds.formLayout(myLayout, e =1, attachControl = [(b3, 'left', 0, b1), (b3, 'top', 0, b1) ])
    # make element follow the window by left or right borders
    cmds.formLayout(myLayout, e =1, attachPosition = [(b1, 'left', 0, 50),(b1, 'right', 0, 100)])

    # EXAMPLE HOW TO MAKE ADJUSTABLE WINDOW with form layout
    cmds.formLayout(myLayout, e =1, attachForm = [(b1, 'left', 2), (b1, 'top', 50) ])
    cmds.formLayout(myLayout, e =1, attachForm = [(b3, 'right', 2), (b3, 'top', 50) ])
    cmds.formLayout(myLayout, e =1, attachForm = [(b2, 'top', 50)])
    cmds.formLayout(myLayout, e =1, attachPosition = [(b1, 'right', 0, 33)])
    cmds.formLayout(myLayout, e =1, attachPosition = [(b3, 'left', 0, 66)])
    cmds.formLayout(myLayout, e =1, attachControl = [ (b2, 'left', 2, b1), (b2, 'right', 2, b3) ])

    # show window
    cmds.showWindow(UIName)


createWindow()
