
""" from a bunch of selected objects select only curves  """


import maya.cmds as cmds

objects = cmds.ls(selection=1, long=1)

if not objects:
    cmds.error("You forgot to select objects in the scene")
    
resultList = []

for obj in objects:
    
    if cmds.nodeType(obj) != "transform":
        continue
        
    child = cmds.listRelatives(obj, children=1)[0]
    typ = cmds.nodeType(child)
    
    print obj, typ
    
    if typ == "mesh":
        resultList.append(obj)
        
if resultList:
    cmds.select(resultList)
else:
    cmds.warning("returnList is empty")