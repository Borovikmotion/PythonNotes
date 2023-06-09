
""" CHECKBOX """

# layouts
mainLayout = cmds.columnLayout()
checkBoxLayout = cmds.columnLayout(parent = mainLayout, width = panelWidth)
cmds.columnLayout(adjustableColumn=True)

# checkbox
myCheckBox = cmds.checkBox( label='Put into a group', parent = checkBoxLayout)

# result of checkbox
bCheckBoxData = cmds.checkBox(myCheckBox, q=1, v=True)