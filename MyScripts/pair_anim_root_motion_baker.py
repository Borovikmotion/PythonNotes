import maya.cmds as cmds
import maya.mel as mel
import os
import maya.standalone
import sys
import json
# import math

class ObjectRebaker(object):
    def __init__(self, path, objName, childObjects, animSourceObject, offsetPosX = 0, offsetPosY = 0, offsetPosZ = 0, offsetRotX = 0, offsetRotY = 0, offsetRotZ = 0, moveChilds = False):
        self.path = path
        self.objName = objName
        self.childObjects = childObjects
        self.animSourceObject = animSourceObject
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
        self.childObjects = childObjects
        self.childObjLocators = []
        self.result = []
        self.outputPath = self.path + "/" + "edited"
        self.minT = 0
        self.maxT = 1

        self.main()

    def freezeChildObjects(self):
        for chObj in self.childObjects:
            chObjName = self.nameSpace + chObj
            childLoc = cmds.spaceLocator(n= chObj + "_LOC")
            childCon = cmds.parentConstraint(chObjName, childLoc, mo=0)
            self.childObjLocators.append(childLoc)

            cmds.bakeResults(childLoc, time = (self.minT,self.maxT))
            cmds.delete(childCon)
            childSafeCon = cmds.parentConstraint(childLoc, chObjName, mo=0)

    def unfreezeChildObjects(self):
        for chObj in self.childObjects:
            chObjName = self.nameSpace + chObj
            cmds.bakeResults(chObjName, time = (self.minT,self.maxT))

        for loc in self.childObjLocators:
            cmds.delete(loc)

        self.childObjLocators = []

    def rebakeObjectAnim(self):
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
        cmds.bakeResults(tempLoc, time = (self.minT,self.maxT))
        cmds.delete(con)

        # constraint our object to temporary offset locator and bake animation
        conFinal = cmds.parentConstraint(tempLoc, self.objectCtrl, mo=0)
        cmds.bakeResults(self.objectCtrl, time = (self.minT,self.maxT))
        cmds.delete(conFinal)
        cmds.delete(tempLoc)

    def transferAnimation(self):
        # put a temporary locator at the anim source object 
        tempLoc = cmds.spaceLocator(n="Anim_Temp_LOC")
        tempCon = cmds.parentConstraint(self.animSourceObject, tempLoc, mo=0)
        cmds.bakeResults(tempLoc, time = (self.minT,self.maxT))
        cmds.delete(tempCon)

        #constrain object to our animation source locator
        cmds.currentTime(self.minT, edit=True)
        animPointCon = cmds.pointConstraint(tempLoc, self.objName, mo=0)
        animOrientCon = cmds.orientConstraint(tempLoc, self.objName, mo=1)
        cmds.bakeResults(self.objName, time = (self.minT,self.maxT))
        cmds.delete(tempLoc)

        # euler filter
        try:
            cmds.filterCurve(self.objName + "_rotateX1", self.objName + "_rotateY1", self.objName + "_rotateZ1")
        except:
            print("Euler Filter Error")
            # cmds.filterCurve(self.objName + "_rotateX", self.objName + "_rotateY", self.objName + "_rotateZ")

    def findNameSpace(self):
        testJointFullName = cmds.ls(type="joint")[0]
        if len(testJointFullName.split(":")) == 2:
            self.nameSpace = testJointFullName.split(":")[0] + ":"
        elif len(testJointFullName.split(":")) == 1:
            self.nameSpace = ""
        
        # apply namespace to the object name
        self.objectCtrl = self.nameSpace + self.objName
        self.exportBone = self.nameSpace + "root"
        self.animSourceObject = self.nameSpace + self.animSourceObject
    
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
    
    def write_json(self, jsonData, path, name):
        with open (path + "/" + name + ".json", "w") as f:
            f.write(json.dumps(jsonData, indent = 4, sort_keys = True))

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
        timing = {}
        # do something for each file
        for f in self.files:
            # import fbx
            self.importFBX(importFilePath = f)

            # get timeline and namespace
            self.findNameSpace()
            # self.minT = cmds.playbackOptions(q=1, min=1)
            # self.maxT = cmds.playbackOptions(q=1, max=1)

            self.minT = round(cmds.playbackOptions(q=1, min=1))
            self.maxT = round(cmds.playbackOptions(q=1, max=1))

            # a thing co calculate delta 
            # deltaMin = round(self.minT) - self.minT
            # deltaMax = round(self.maxT) - self.maxT
            f_short = f.split("/")[-1]
            timing[f_short] = " min: " + str(self.minT) + ", " + " max: " + str(self.maxT)
            # timing[f_short] = " min: " + str(deltaMin) + ", " + "max: " + str(deltaMax)

            # do reparent child object, to keep it's transforms
            if self.moveChilds == False and self.childObjects:
                self.freezeChildObjects()

            # get animation from anim source object and apply it to our target object 
            self.transferAnimation()

            # # rebake anim
            # self.rebakeObjectAnim()

            # bake and delete child's locators
            if self.moveChilds == False and self.childObjects:
                self.unfreezeChildObjects()

            # export fbx
            self.exportFBX(currentFilePath = f)

            # # debug save file
            # fileExportName = f.split("/")[-1]
            # outputFile = self.outputPath + "/" + fileExportName
            # cmds.file(rename = outputFile + ".ma") 
            # cmds.file(force=True, type='mayaAscii', s=True)

            # cleanup scene
            # cmds.delete(self.objectCtrl)
            cmds.file(new=1, force=True)

        # close maya
        maya.standalone.uninitialize()
        # print log
        print ("\n\n\nOutput:\n")
        for i in self.result:
            print (i)
        
        # print ("\n\n\nOutput:\n")
        # for key, value in timing:
        #     print (key.split("/")[-1], value)

        self.write_json(jsonData = timing, path ="D:/Work/66_pair_animation_root_motion", name = "timings")

# ENTER YOUR VALUES HERE
rebake1 = ObjectRebaker(path = "D:/Work/66_pair_animation_root_motion/Source_only_needed_fbx", objName = "root", childObjects = ["pelvis", "ik_hand_gun", "ik_foot_root"], animSourceObject = "ik_foot_root", offsetPosX = 0, offsetPosY = 0, offsetPosZ = 0, offsetRotX = 0, offsetRotY = 0, offsetRotZ = 0, moveChilds = False)


