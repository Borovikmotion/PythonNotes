def positiveNumbers(lst):
    for i in lst:
        if i > 0:
            yield i

a = [1,2,3,-4,-5,6, 7, -8, -2, 2,-1]

# for i in a:
#     if i > 0:
#         print(i)

for i in positiveNumbers(a):
    print(i)



# ------------- 
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

#save result is a separate list
a = [i for i in control_curve(selected_objects)]
print (a)

# or 
# a = control_curve(selected_objects)
# print (a.next())
# print (a.next())

#how to generate a list 
a = [i for i in range(0,10)]
print a 