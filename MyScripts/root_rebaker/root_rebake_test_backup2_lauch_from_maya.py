import maya.cmds as cmds
import maya.mel as mel
import os

# fileName = "A_Zmb_Fat_Shield_Vault_OnLow.fbx"
# fbxFullPath = path + "/" + fbxFile
# fileShortName = fbxFile.split(".")[0]
# outputFile = path + "/" + "edited" + "/" + fileShortName + ".fbx"

# files path
path = "D:/Scripts/03/testVault"

# enter object name and offsets you want to apply
objectCtrl = "SK_Zmb_Fat_Rig_01:root"
childObj = "SK_Zmb_Fat_Rig_01:pelvis"
offsetPosX = 100
offsetPosY = 0
offsetPosZ = 100
offsetRotX = 0
offsetRotY = 0
offsetRotZ = 0
moveChilds = False

def rebakeObjectAnim():
    minT = cmds.playbackOptions(q=1, min=1)
    maxT = cmds.playbackOptions(q=1, max=1)

    # put a temporary locator right at object we need to rebake 
    tempLoc = cmds.spaceLocator(n="temp_LOC")
    tempCon = cmds.parentConstraint(objectCtrl, tempLoc, mo=0)
    cmds.delete(tempCon)

    # add offsets to the position of the locator
    locPosStart = cmds.xform(tempLoc, t=1, ws=1, q=1)
    locPosX = locPosStart[0] + offsetPosX
    locPosY = locPosStart[1] + offsetPosY
    locPosZ = locPosStart[2] + offsetPosZ
    locFinalPos = [locPosX,locPosY,locPosZ]
    cmds.xform(tempLoc, t=locFinalPos)

    # constraint temporary locator to our object and bake animation
    con = cmds.parentConstraint(objectCtrl, tempLoc, mo=1)
    cmds.bakeResults(tempLoc, time = (minT,maxT))
    cmds.delete(con)

    if moveChilds == False:
        # do reparent to child object, to keep it's transforms
        childLoc = cmds.spaceLocator(n="child_LOC")
        childCon = cmds.parentConstraint(childObj, childLoc, mo=0)
        cmds.bakeResults(childLoc, time = (minT,maxT))
        cmds.delete(childCon)
        childSafeCon = cmds.parentConstraint(childLoc, childObj, mo=0)

        # constraint our object to temporary locator without offset and bake animation
        conFinal = cmds.parentConstraint(tempLoc, objectCtrl, mo=0)
        cmds.bakeResults(objectCtrl, childObj, time = (minT,maxT))
        cmds.delete(conFinal)
        cmds.delete(tempLoc)
        cmds.delete(childSafeCon)
        cmds.delete(childLoc)

    else:
        # constraint our object to temporary locator without offset and bake animation
        conFinal = cmds.parentConstraint(tempLoc, objectCtrl, mo=0)
        cmds.bakeResults(objectCtrl, time = (minT,maxT))
        cmds.delete(conFinal)
        cmds.delete(tempLoc)

def main():

    # get list of acceptible files
    files = []
    if not os.path.isdir(path):
        raise ValueError("the path does not exist")

    for i in os.listdir(path):
        fileName, fileExt = os.path.splitext(i)
        if fileExt == ".mb" or fileExt == ".ma" or fileExt == ".fbx":
            fullPath = path + "/" + i
            files.append(fullPath)
    if not files:
        print ("there are no acceptable files")
        return

    # create output folder
    outputPath = path + "/" + "edited"
    os.mkdir(outputPath)

    # do something for each file
    for f in files:
        # import
        mel.eval('FBXImport -file "{0}"'.format(fullPath))

        # adjust transforms
        rebakeObjectAnim()

        # export fbx
        fileName = f.split("/")[-1]
        outputFile = outputPath + "/" + fileName
        cmds.select(objectCtrl)
        mel.eval('FBXExport -f "{0}" -s'.format(outputFile))

        # cleanup scene
        cmds.delete(objectCtrl)

main()





