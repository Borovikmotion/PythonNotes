""" BUTTONS """

# fucntions to run
obj = []
def createObject():
    obj = cmds.polySphere()

def deleteObject():
    cmds.delete(obj)


panelWidth = 400

# layouts
mainLayout = cmds.columnLayout()
cmds.columnLayout(adjustableColumn=True)
buttonsLayout = cmds.rowLayout(numberOfColumns=2, parent = mainLayout)

# BUTTONS
crtButtonName = "CreateOBjectButtonID"
canButtonName ="CancelButtonID"

cmds.button(crtButtonName, w = panelWidth/2, label = "Create", parent = buttonsLayout, command = "createObject()", statusBarMessage = "Create" )
cmds.button(canButtonName, w = panelWidth/2, label = "Undo", parent = buttonsLayout, command = "deleteObject()", statusBarMessage = "Undo" )


