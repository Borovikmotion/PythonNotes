import maya.cmds as cmds
import re


pattern = re.compile(".*(ctrl)+.*[0-9]*")

def control_curve(list_of_objects):
    for i in list_of_objects:
        child_node = cmds.listRelatives(i, f=1)
        if cmds.nodeType(child_node) == "nurbsCurve":
            if pattern.match(i):
                yield i
        
selected_objects = cmds.ls(sl=1)

for i in control_curve(selected_objects):
    print i