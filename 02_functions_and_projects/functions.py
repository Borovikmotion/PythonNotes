""" FUNCTIONS """

import maya.cmds as cmds

def create_object(objName, grpName, objType = "sphere"):
    if objType == "sphere":
        obj = cmds.polySphere(n=objName)[0]
    elif objType == "cube":
        obj = cmds.polyCube(n=objName)[0]
    grp = cmds.group(empty=1,n=grpName)
    cmds.parent(obj,grp)
    return grp 

# create_object("helloSphere", "helloGroup")
# create_object("hiSphere", "hiGroup")
# create_object("yoSphere", "yoGroup")
# create_object("yocube", "yoCube", objType = "cube")

def moveUp(objectName, distance):
    if distance < 0:
        cmds.error("please use distance more than zero") 
    cmds.xform(objectName, worldSpace=1, r=1, translation=[0, distance,0])

def main():
    mygroup = create_object("cube", "cubeGRP", objType = "cube")
    moveUp(mygroup, 3)

main()
