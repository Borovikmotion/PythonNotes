"""
how to run this in cmd - specify path to mayapy.exe, then path to the script, then --path variable (path to maya files)

"C:\Program Files\Autodesk\Maya2019\bin\mayapy.exe" C:\Users\borov\Documents\maya\scripts\examples\03_json_and_files\batch_mode.py -p "C:\testMayaScenes"


"""

import maya.cmds as cmds
import maya.standalone
import os
from argparse import ArgumentParser


def main():
    # specify path_to_maya_files in the command line through the argparser, or put the info directly here
    # path = "D:/Scripts/03/Spheres_and_curves"
    parser = ArgumentParser(description="Options")
    parser.add_argument('-p', '--path', type = str, required = True, help = "Path to the files")
    args = parser.parse_args()

    # -----------------------------------------------------
    # replace widows slash to python
    PATH = args.path.replace("\\", "/")
    # check if the path exists
    if not os.path.isdir(PATH):
        raise ValueError("the path does not exist")

    # get maya files 
    mayaFiles = []

    for i in os.listdir(PATH):
        # get file name and extension 
        filename, fileExt = os.path.splitext(i)
        if fileExt == ".mb" or fileExt == ".ma":
            fullpath = os.path.join(path, i)
            mayaFiles.append(fullpath)

    if not mayaFiles:
        print ("there are no maya files")
        return

    # -----------------------------------------------------
    # open maya 
    maya.standalone.initialize(name="python")
    result = {}

    # for each maya file 
    for mf in mayaFiles:
        # open file
        cmds.file(mf, open = True, force=True)


        # do something 


        # save filename into log
        fileShortName = mf.split("/")[-1]
        result[fileShortName].append(i)

        # save file
        # cmds.file(save=True)
        # cmds.file(new=1, force=True)

    # close maya
    maya.standalone.uninitialize()

    # print log
    print "\n\n\nOutput:\n"
    for key, value in result.items():
        print "\n" + key
        if value:
            for i in value:
                print "\t" + i
        else:
            print "\t" + "nothing happened"


if __name__ == "__main__":
    main()

