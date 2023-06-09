# adjust userPrefs.mel
import maya.cmds as cmds
myName = "VasyaPupkin"
cmds.optionVar(sv=("DeveloperName", myName))
print cmds.optionVar(q="DeveloperName")
cmds.optionVar(remove="DeveloperName")