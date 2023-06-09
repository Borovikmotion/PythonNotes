import maya.cmds as cmds
import maya.mel as mel
import os
import maya.standalone
import sys


# ENTER A PATH TO YOUR FBX FILES HERE:
path_to_fbx_files = "D:/Work/68_Human_Stealth_Kills/fbx_export"

class ObjectRebaker(object):
    def __init__(self, path, objName):
        self.path = path
        self.objName = objName

        self.nameSpace = ""
        self.exportBone = self.nameSpace + "root"
        self.files = []
        self.objectCtrl = objName
        self.childObjects = childObjects
        self.childObjLocators = []
        self.result = []
        self.outputPath = self.path + "/" + "edited"
        self.minT = 0
        self.maxT = 1

        self.main()

    def findNameSpace(self):
        testJointFullName = cmds.ls(type="joint")[0]
        if len(testJointFullName.split(":")) == 2:
            self.nameSpace = testJointFullName.split(":")[0] + ":"
        elif len(testJointFullName.split(":")) == 1:
            self.nameSpace = ""
        
        # apply namespace to the object name
        self.objectCtrl = self.nameSpace + self.objName
        self.exportBone = self.nameSpace + "root"
    
    def getFiles(self):
        if not os.path.isdir(self.path):
            raise ValueError("the path does not exist")
        
        for i in os.listdir(self.path):
            fileName, fileExt = os.path.splitext(i)
            if fileExt == ".fbx":
                fullPath = self.path + "/" + i
                self.files.append(fullPath)
            elif fileExt == ".FBX" or fileExt == ".Fbx" or fileExt == ".fBx" or fileExt == ".fbX" or fileExt == ".FBx" or fileExt == ".fBX" or fileExt == ".FbX":
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
        # check if one of childs objects names matches main object name 
        if self.moveChilds == False and self.childObjects:
            for chObj in self.childObjects:
                if chObj == self.objName:
                    raise ValueError("one of the child objects name matches parent object name")

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

            # get timeline and namespace
            self.minT = round(cmds.playbackOptions(q=1, min=1))
            self.maxT = round(cmds.playbackOptions(q=1, max=1))
            self.findNameSpace()

            # do something with each FBX HERE

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


rebake1 = ObjectRebaker(path = path_to_fbx_files, objName = "root")


