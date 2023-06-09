# columnLayout, rawLayout, formLayout, frameLayout 

command = "createSphere()"

cmds.setParent( {layoutName} )

showWindow( "windowName" )
cmds.window("windowName", exists = 1)
cmds.deleteUI("windowName")

cmds.windowPref("windowName", remove = 1)

cmds.optionVar()
cmds.optionVar( iv=('runMyToolbarOnMayaLaunch', 1))
doRun = cmds.optionVar(q='runMyToolbarOnMayaLaunch')


# mockflow site 

# layouts
# columnLayout
# rowLayout
# formLayout


# _______CREATE SIMPLE WINDOW_______
import maya.cmds as cmds

def createWindow():

    # cleanup old window
    if cmds.window("ASchoolExampleWindowName", exists=1):
        cmds.deleteUI("ASchoolExampleWindowName")

    # cleanup old data
    if cmds.windowPref("ASchoolExampleWindowName", exists=1):
        cmds.windowPref("ASchoolExampleWindowName", remove=1)

    # create new window
    cmds.window("ASchoolExampleWindowName", title = "my window", width=400, height=300, toolbox=False)

    # layouts
    myLayout = cmds.columnLayout()
    # print (myLayout)

    # show some text
    myTextField  = cmds.textField("SomeIDTextField", parent = myLayout, width = 200, placeholderText = "SphereName")


    def createSphere():
        print ("creating a sphere")
        SphName = cmds.textField("SomeIDTextField", q=1, text=1)
        cmds.polySphere(n=SphName)

    # create button
    cmds.button("myButtonID", label = "create sphere", parent = myLayout, command = "createSphere()", statusBarMessage = "Hello" )

    # show window
    cmds.showWindow("ASchoolExampleWindowName")


createWindow()






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

    # # COLUMN LAYOUT
    # myLayout = cmds.columnLayout(adjustableColumn = 1, rowSpacing = 5)
    # cmds.button(w = 50, label = "OK", parent = myLayout)
    # cmds.button(w = 50, label = "Apply", parent = myLayout)
    # cmds.button(w = 50, label = "Cancel", parent = myLayout)


    # # ROW LAYOUT 1
    # myLayout = cmds.rowLayout(numberOfColumns =3, cw3=[100,100,50], ct3 = ['both','left','left'], co3 = [0,10,0], cal = (1, 'right'))
    # # left, right, both 
    # # left right center
    # # adjustableColumn3 = 1
    # cmds.text(parent = myLayout, label = "hohoho")
    # # cmds.button(w = 50, label = "OK", parent = myLayout)
    # cmds.button(w = 50, label = "Apply", parent = myLayout)
    # cmds.button(w = 50, label = "Cancel", parent = myLayout)


    # FORM LAYOUT
    myLayout = cmds.formLayout(w = 300, h = 200, numberOfDivisions = 100)

    b1 = cmds.button(w = 50, label = "OK", parent = myLayout)
    b2 = cmds.button(w = 50, label = "Apply", parent = myLayout)
    b3 = cmds.button(w = 50, label = "Cancel", parent = myLayout)

    # # move objects 
    # cmds.formLayout(myLayout, e =1, attachForm = [(b1, 'left', 100), (b1, 'top', 50), (b2, 'left', 50), (b2, 'top', 100), ])

    # # move object relatively to other object
    # cmds.formLayout(myLayout, e =1, attachControl = [(b3, 'left', 0, b1), (b3, 'top', 0, b1) ])

    # # make object follow the window by left or right borders
    # cmds.formLayout(myLayout, e =1, attachPosition = [(b1, 'left', 0, 50),(b1, 'right', 0, 100)])


    # EXAMPLE HOW TO MAKE ADJUSTABLE WINDOW
    cmds.formLayout(myLayout, e =1, attachForm = [(b1, 'left', 2), (b1, 'top', 50) ])
    cmds.formLayout(myLayout, e =1, attachForm = [(b3, 'right', 2), (b3, 'top', 50) ])
    cmds.formLayout(myLayout, e =1, attachForm = [(b2, 'top', 50)])

    cmds.formLayout(myLayout, e =1, attachPosition = [(b1, 'right', 0, 33)])
    cmds.formLayout(myLayout, e =1, attachPosition = [(b3, 'left', 0, 66)])

    cmds.formLayout(myLayout, e =1, attachControl = [ (b2, 'left', 2, b1), (b2, 'right', 2, b3) ])


    # show window
    cmds.showWindow(UIName)


createWindow()






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






# _______ ADD CUSTOM MENU_______

import maya.cmds as cmds
import maya.mel as mel 

UIName = "MyWindowName"

mainWindow = mel.eval('global string $gMainWindow; $a = $gMainWindow;')
# print mainWindow

if cmds.menu(UIName, exists = True):
    cmds.deleteUI(UIName)

newMenu = cmds.menu(UIName, l="Animation Shol Menu", tearOff = 1, p = mainWindow)

def createSphere():
    cmds.polySphere()

item = cmds.menuItem("ItemName", c = "createSphere()", p = newMenu)





# ______ ADD OBJECTS TO LEFT BAR__________
import maya.cmds as cmds
import maya.mel as mel 

UIName = "MyWindowName"

toolbox  = mel.eval('global string $gToolBox; $a = $gToolBox;')
# print toolbox

def createSphere():
    cmds.polySphere()

# if cmds.window('myTestLayout1', exists = True):
    # cmds.deleteUI('myTestLayout1')
    # ?????

cmds.gridLayout("mytestLayout3", numberOfColumns =1, width = 36, cellWidthHeight = [36, 36], parent = toolbox)

cmds.button(label = "Sph", c = "createSphere()")

cmds.popupMenu()
cmds.menuItem(l="one", c = "createSphere()")
cmds.menuItem(l="two", c = "createSphere()")
cmds.menuItem(l="three", c = "createSphere()")

# find out the name of standard tools
print cmds.flowLayout(toolbox, q=1, childArray =1)



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




