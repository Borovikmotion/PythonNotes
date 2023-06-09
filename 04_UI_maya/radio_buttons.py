#layout
mainLayout = cmds.columnLayout()


# radio buttons
radButtonsLayout = cmds.rowLayout(numberOfColumns=3, parent = mainLayout, width = panelWidth)
objTypeRB = cmds.radioButtonGrp(numberOfRadioButtons=3, labelArray3=['Sphere', 'Cube', 'Cone'])

# other way to create radion buttons
# objTypeRBC = cmds.radioCollection()
# sphereRB = cmds.radioButton(label = "Sphere", parent = radButtonsLayout)
# cubeRB = cmds.radioButton(label = "Cube", parent = radButtonsLayout)
# coneRB = cmds.radioButton(label = "Cone", parent = radButtonsLayout)

# get data
bResult = cmds.radioButtonGrp(objTypeRB, q=1, sl=True) 
