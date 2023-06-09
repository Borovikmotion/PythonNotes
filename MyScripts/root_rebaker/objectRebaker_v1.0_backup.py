import maya.cmds as cmds
import maya.mel as mel
import os
import maya.standalone
import sys


class ObjectRebaker(object):
    def __init__(self, path, objName, childObjName, offsetPosX = 0, offsetPosY = 0, offsetPosZ = 0, offsetRotX = 0, offsetRotY = 0, offsetRotZ = 0, moveChilds = False):
        self.path = path
        self.objName = objName
        self.childObjName = childObjName
        self.offsetPosX = offsetPosX
        self.offsetPosY = offsetPosY
        self.offsetPosZ = offsetPosZ
        self.offsetRotX = offsetRotX
        self.offsetRotY = offsetRotY
        self.offsetRotZ = offsetRotZ
        self.moveChilds = moveChilds

        self.nameSpace = ""
        self.exportBone = self.nameSpace + "root"
        self.files = []
        self.objectCtrl = objName
        self.childObj = childObjName
        self.result = []
        self.outputPath = self.path + "/" + "edited"

        self.main()

    def rebakeObjectAnim(self):
        minT = cmds.playbackOptions(q=1, min=1)
        maxT = cmds.playbackOptions(q=1, max=1)

        if self.moveChilds == False:
            # do reparent child object, to keep it's transforms
            childLoc = cmds.spaceLocator(n="child_LOC")
            childCon = cmds.parentConstraint(self.childObj, childLoc, mo=0)
            cmds.bakeResults(childLoc, time = (minT,maxT))
            cmds.delete(childCon)
            childSafeCon = cmds.parentConstraint(childLoc, self.childObj, mo=0)

        # put a temporary locator right at object we need to rebake 
        tempLoc = cmds.spaceLocator(n="temp_LOC")
        tempCon = cmds.parentConstraint(self.objectCtrl, tempLoc, mo=0)
        cmds.delete(tempCon)

        # add offsets to the position of the locator
        locPosStart = cmds.xform(tempLoc, t=1, ws=1, q=1)
        locPosX = locPosStart[0] + self.offsetPosX
        locPosY = locPosStart[1] + self.offsetPosY
        locPosZ = locPosStart[2] + self.offsetPosZ
        locFinalPos = [locPosX,locPosY,locPosZ]
        cmds.xform(tempLoc, t=locFinalPos)

        # add rotation offsets
        locRotStart = cmds.xform(tempLoc, ro=1, ws=1, q=1)
        locRotX = locRotStart[0] + self.offsetRotX
        locRotY = locRotStart[1] + self.offsetRotY
        locRotZ = locRotStart[2] + self.offsetRotZ
        locFinalRot = [locRotX,locRotY,locRotZ]
        cmds.xform(tempLoc, ro=locFinalRot)

        # constraint temporary locator to our object and bake animation
        con = cmds.parentConstraint(self.objectCtrl, tempLoc, mo=1)
        cmds.bakeResults(tempLoc, time = (minT,maxT))
        cmds.delete(con)


        # constraint our object to temporary offset locator and bake animation
        conFinal = cmds.parentConstraint(tempLoc, self.objectCtrl, mo=0)
        cmds.bakeResults(self.objectCtrl, time = (minT,maxT))
        cmds.delete(conFinal)
        cmds.delete(tempLoc)

        if self.moveChilds == False:
            # bake and delete child's locators
            cmds.bakeResults(self.childObj, time = (minT,maxT))
            cmds.delete(childSafeCon)
            cmds.delete(childLoc)

    def findNameSpace(self):
        testJointFullName = cmds.ls(type="joint")[0]
        if len(testJointFullName.split(":")) == 2:
            self.nameSpace = testJointFullName.split(":")[0] + ":"
        elif len(testJointFullName.split(":")) == 1:
            self.nameSpace = ""
        
        # apply namespace to the object name
        self.objectCtrl = self.nameSpace + self.objName
        self.childObj = self.nameSpace + self.childObjName
        self.exportBone = self.nameSpace + "root"
    
    def getFiles(self):
        if not os.path.isdir(self.path):
            raise ValueError("the path does not exist")
        
        for i in os.listdir(self.path):
            fileName, fileExt = os.path.splitext(i)
            if fileExt == ".fbx":
                fullPath = self.path + "/" + i
                self.files.append(fullPath)
            elif fileExt == ".FBX":
                fullPath = self.path + "/" + fileName + ".fbx"
                self.files.append(fullPath)
        if not self.files:
            print ("there are no acceptable files")
            return

    def importFBX(self, importFilePath):
        mel.eval('FBXImport -file "{0}"'.format(importFilePath))

    def exportFBX(self, currentFilePath):
        fileExportName = currentFilePath.split("/")[-1]
        outputFile = self.outputPath + "/" + fileExportName
        cmds.select(self.exportBone)
        mel.eval('FBXExport -f "{0}" -s'.format(outputFile))
        self.result.append(outputFile)

    def main(self):
        # get list of acceptible files
        self.getFiles()
        
        # create output folder
        if not os.path.exists(self.outputPath):
            os.mkdir(self.outputPath)
        else:
            print("edited folder is already there")

        # open maya 
        maya.standalone.initialize(name="python")
        mel.eval("loadPlugin fbxmaya")

        # do something for each file
        for f in self.files:
            # import fbx
            self.importFBX(importFilePath = f)

            # rebake anim
            self.findNameSpace()
            self.rebakeObjectAnim()

            # export fbx
            self.exportFBX(currentFilePath = f)

            # cleanup scene
            # cmds.delete(self.objectCtrl)
            cmds.file(new=1, force=True)

        # close maya
        maya.standalone.uninitialize()
        # print log
        print ("\n\n\nOutput:\n")
        for i in self.result:
            print (i)


# ENTER YOUR VALUES HERE
rebake1 = ObjectRebaker(path = "D:/Scripts/03/testVault", objName = "root", childObjName = "pelvis", offsetPosX = 150, offsetPosY = 0, offsetPosZ = 0, offsetRotX = 0, offsetRotY = 0, offsetRotZ = 0, moveChilds = False)


