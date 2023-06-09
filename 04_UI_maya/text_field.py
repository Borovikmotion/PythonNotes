
""" TEXT FIELD """

# layout
mainLayout = cmds.columnLayout()

objName = cmds.textField("ObjectNameTextFieldID", q=1, text=1)

# text field
objectNameTextField  = cmds.textField("ObjectNameTextFieldID", parent = mainLayout, width = panelWidth, placeholderText = "Object Name")