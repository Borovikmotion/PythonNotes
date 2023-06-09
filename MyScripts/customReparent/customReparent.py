import maya.cmds as cmds
minT = cmds.playbackOptions(q=1, min =1)
maxT = cmds.playbackOptions(q=1, max =1)

SelectedObjects = cmds.ls(sl=1, l =1)
obj = SelectedObjects[0]
loc = SelectedObjects[1]

con = cmds.parentConstraint(obj,loc,mo=True)
cmds.bakeResults(loc, time = (minT,maxT))
cmds.delete(con)

cmds.parentConstraint(loc,obj,mo=True)



