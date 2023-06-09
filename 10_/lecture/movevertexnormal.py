import maya.OpenMaya as OpenMaya 
import maya.cmds as cmds
import random

selectedMesh = cmds.ls(sl=1,l=1)[0] 

selectionList = OpenMaya.MSelectionList()
selectionList.add(selectedMesh)

mDagPath = OpenMaya.MDagPath()
selectionList.getDagPath(0, mDagPath) 

vertexIterator = OpenMaya.MItMeshVertex(mDagPath)

while not vertexIterator.isDone():

    vectorNormal = OpenMaya.MVector()

    vertexIterator.getNormal(vectorNormal , OpenMaya.MSpace.kWorld)

    vectorNormal.normalize()

    currentPosition = vertexIterator.position(OpenMaya.MSpace.kWorld)

    newPosition = currentPosition + vectorNormal * random.uniform(-0.5, 0.5)

    vertexIterator.setPosition(newPosition, OpenMaya.MSpace.kWorld)

    vertexIterator.next()