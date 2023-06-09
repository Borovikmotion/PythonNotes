import maya.cmds as cmds
import maya.mel as mel

path = "D:/Scripts/03/testVault"
fbxFile = "A_Zmb_Fat_Shield_Vault_OnLow.fbx"
fbxFullPath = path + "/" + fbxFile 
fileShortName = fbxFile.split(".")[0]
outputFile = path + "/" + fileShortName + "_edited_" + ".fbx"

print outputFile
objectCtrl = "SK_Zmb_Fat_Rig_01:root"
offsetPosX = 100
offsetPosY = 0
offsetPosZ = 100

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

    # constraint our object to temporary locator without offset and bake animation
    conFinal = cmds.parentConstraint(tempLoc, objectCtrl, mo=0)
    cmds.bakeResults(objectCtrl, time = (minT,maxT))
    cmds.delete(conFinal)
    cmds.delete(tempLoc)

def main():
    mel.eval('FBXImport -file "{0}"'.format(fbxFullPath))
    # cmds.file(fbxFullPath, i=True, type = "Fbx", rpr=True)
    rebakeObjectAnim()
    cmds.select(objectCtrl)
    mel.eval('FBXExport -f "{0}" -s'.format(outputFile))

main()





