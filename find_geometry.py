import maya.cmds as cmds

sel = cmds.ls(sl=1)

objects = cmds.listRelatives(sel, ad=1)

for obj in objects:
    obj_type = cmds.nodeType(obj)
    if obj_type == "mesh":
        cmds.parent(obj, w=1)