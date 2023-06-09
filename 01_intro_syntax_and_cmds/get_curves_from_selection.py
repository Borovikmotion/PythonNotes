""" Выделение  """
objects = cmds.ls(selection=1, long=1)
if not objects:
    #raise ValueError ('nothing is selected')
    cmds.error ('nothing is selected')
resultList = []


for obj in objects:
    if cmds.nodeType(obj) != 'transform':
        continue
    child = cmds.listRelatives(obj, children = 1)[0]
    type = cmds.nodeType(child)
    if type == "nurbsCurve":
        resultList.append(obj)
print resultList
if resultList:
    cmds.select(resultList)
else: 
    cmds.warning('empty') 