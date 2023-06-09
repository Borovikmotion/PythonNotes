# FREEZE CURVES
import maya.cmds as cmds
import maya.standalone
import sys
import os
from argparse import ArgumentParser

def main():
    # path = "D:/Scripts/03/Spheres_and_curves"
    # objectType = "nurbsCurve"

    parser = ArgumentParser(description="Options")
    parser.add_argument('-p', '--path', type = str, required = True, help = "Path to the files")
    parser.add_argument('-nt', '--nodeType', type = str, default = "nurbsCurve", help = "type of files")
    args = parser.parse_args()

    # replace widows slash to python
    path = args.path.replace("\\", "/")
    objectType = args.nodeType

    # check if the path exists
    if not os.path.isdir(path):
        raise ValueError("the path does not exist")


    # get maya files 
    mayaFiles = []

    for i in os.listdir(path):
        # get file name and extension 
        filename, fileExt = os.path.splitext(i)
        if fileExt == ".mb" or fileExt == ".ma":
            fullpath = path + "/" + i
            # fullpath = os.path.join(path, i)
            mayaFiles.append(fullpath)

    if not mayaFiles:
        print ("there are no maya files")
        return


    # open maya 
    maya.standalone.initialize(name="python")

    result = {}

    # do something for each maya file 
    for mf in mayaFiles:
        # open file
        cmds.file(mf, open = True)

        # find curves
        listOfCurves = cmds.ls(type = objectType)
        listOFCurvesTr = cmds.listRelatives(listOfCurves, p = 1)

        if not listOfCurves:
            continue

        fileShortName = mf.split("/")[-1]
        result[fileShortName] = []

        for i in listOFCurvesTr:
            
            # move object to zero
            # cmds.makeIdentity(i, t =1, s =1, r =1)
            # freeze transf
            cmds.makeIdentity(i, apply = 1, t =1, s =1, r =1, n = 0, pn = 1)

            result[fileShortName].append(i)

        # save file
        cmds.file(save = True)

    # close maya
    maya.standalone.uninitialize()

    print "\n\n\nOutput:\n"
    for key, value in result.items():
        print "\n" + key
        if value:
            for i in value:
                print "\t" + i
        else:
            print "\t" + "no curves in the file"



if __name__ == "__main__":
    main()

