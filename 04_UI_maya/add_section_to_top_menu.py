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

