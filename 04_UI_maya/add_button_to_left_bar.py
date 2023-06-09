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
