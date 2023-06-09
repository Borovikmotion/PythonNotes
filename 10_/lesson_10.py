# shift vertexes along the normal 

import maya.OpenMaya as om #1.0 
import maya.cmds as cmds
import random

sphereName = cmds.ls(sl=1, l=1)[0]

# types of objects: mObject, MDagPath
selectionList = om.MSelectionList()
selectionList.add(sphereName)

mDagPath = om.MDagPath()
selectionList.getDagPath(0, mDagPath)
# print (mDagPath.fullPathName())

vertexIterator = om.MItMeshVertex(mDagPath)

while not vertexIterator.isDone():
    vertexNormal = om.MVector()
    vertexIterator.getNormal(vertexNormal, om.MSpace.kWorld) #kObject
    vertexNormal.normalize()
    # print (vertexNormal.x, vertexNormal.y, vertexNormal.z)

    pos = vertexIterator.position(om.MSpace.kWorld) #return mPoint

    newPos = pos + vertexNormal*random.uniform(-0.5, 0.5)

    vertexIterator.setPosition(newPos, om.MSpace.kWorld)

    vertexIterator.next()



# pluguis
# examples in the documantation 
# sinus movement
# scripted/sineNode.py



# maya api gould  - book about plugins


# sin = math.sin(x)