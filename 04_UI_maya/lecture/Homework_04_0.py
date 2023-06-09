import maya.cmds as cmds
import random

objName = "defaultName"
createdObjects = []
objType = "Sphere"
bMoveObj = False
bGroupObj = False
bColorObj = False

#things could be done to the object
def moveObject(obj):
    offset = 3
    # if len(createdObjects) > 1:
    #     lastObject = createdObjects[-1]
    #     offsetValue = cmds.xform(lastObject, q=1, t=1, ws =1)[0] + offset
    # else:
    #     offsetValue = 0
    # if len(createdObjects) > 1:
    # offsetValue = cmds.xform(lastObject, q=1, t=1, ws =1)[0] + offset
    # print (cmds.xform(lastObject, q=1, t=1, ws =1)[0])

    if len(createdObjects) > 1:
        lastObject = createdObjects[-1]
        offsetValue = (len(createdObjects)-1)*offset
    else:
        offsetValue = 0

    cmds.xform(obj, ws=1, r=1, t = [offsetValue,0,0])

def groupObject(obj):
    grp = cmds.group(n = obj + "GRP")
    createdObjects[-1] = grp

def colorObject(obj):
    objShader = cmds.shadingNode("lambert", n = "lambert"+obj[0], asShader=1)
    randColorR = random.uniform(0, 1)
    randColorG = random.uniform(0, 1)
    randColorB = random.uniform(0, 1)
    cmds.setAttr(objShader + ".color", randColorR, randColorG, randColorB, type="double3")
    cmds.select(obj)
    cmds.hyperShade(assign = objShader)

# create object 
def createObject():
    objName = cmds.textField("ObjectNameTextFieldID", q=1, text=1)
    objType = cmds.radioButtonGrp(objTypeRB, q=1, sl=True) 

    if objType == 1:
        obj = cmds.polySphere(n=objName)
    elif objType == 2:
        obj = cmds.polyCube(n=objName)
    elif objType == 3:
        obj = cmds.polyCone(n=objName)

    createdObjects.append(obj)

    # get info from checkboxes
    bMoveObj = cmds.checkBox(moveObjCheckBox, q=1, v=True)
    bGroupObj = cmds.checkBox(grpObjCheckBox, q=1, v=True)
    bColorObj = cmds.checkBox(colorObjCheckBox, q=1, v=True)

    #do something more
    if bColorObj ==1:
        colorObject(obj=obj)

    # move object 
    if bMoveObj == 1:
        moveObject(obj=obj)

    # group object
    if bGroupObj == 1:
        groupObject(obj=obj[0])



# cancel - delete created object 
def deleteLastObject():
    if createdObjects:
        cmds.delete(createdObjects[-1])
        createdObjects.pop()


# UI
windowName = "SimpleObjectsCreatorWindowID"
panelWidth = 400
panelHeight = 100

# cleanup
if cmds.window(windowName, exists=1):
    cmds.deleteUI(windowName)
if cmds.windowPref(windowName, exists=1):
    cmds.windowPref(windowName, remove=1)

# create new
cmds.window(windowName, title = "Simple Objects Creator v 1.0", width=panelWidth, height=panelHeight, toolbox=False)

# text on top
mainLayout = cmds.columnLayout()
objectNameTextField  = cmds.textField("ObjectNameTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Object Name")

# radio buttons
radButtonsLayout = cmds.rowLayout(numberOfColumns=3, parent = mainLayout, width = panelWidth)
objTypeRB = cmds.radioButtonGrp(numberOfRadioButtons=3, labelArray3=['Sphere', 'Cube', 'Cone'])

# other way to create radion buttons
# objTypeRBC = cmds.radioCollection()
# sphereRB = cmds.radioButton(label = "Sphere", parent = radButtonsLayout)
# cubeRB = cmds.radioButton(label = "Cube", parent = radButtonsLayout)
# coneRB = cmds.radioButton(label = "Cone", parent = radButtonsLayout)

# checkboxes
checkBoxLayout = cmds.columnLayout(parent = mainLayout, width = panelWidth)
cmds.columnLayout(adjustableColumn=True)
grpObjCheckBox = cmds.checkBox( label='Put into a group', parent = checkBoxLayout)
moveObjCheckBox = cmds.checkBox( label='Offset', parent = checkBoxLayout)
colorObjCheckBox = cmds.checkBox( label='Random Color', parent = checkBoxLayout)

# main buttons
buttonsLayout = cmds.rowLayout(numberOfColumns=2, parent = mainLayout)
crtButtonName = "CreateOBjectButtonID"
canButtonName ="CancelButtonID"
cmds.button(crtButtonName, w = panelWidth/2, label = "Create", parent = buttonsLayout, command = "createObject()", statusBarMessage = "Create" )
cmds.button(canButtonName, w = panelWidth/2, label = "Undo", parent = buttonsLayout, command = "deleteLastObject()", statusBarMessage = "Undo" )

# show window
cmds.showWindow(windowName)


