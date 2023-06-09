# about files


a = "hello world 123"
f = open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="w")
# "hello \n world"
# "hello \t world"

# w
# w+
# r
# a

f.write(a)
f.write("\nsurprise mothefucker")
# f.writelines(a,"hello", "world")

f.close()

text = ["a", "b", "c"]
for i in text:
    f.write(i + "\n")
f.close()



f = open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="r")
data = f.read()
print data 
f.close()

data = f.read()
data = data.split("\n")
for i in data:
    print i

f.close()


# proper way to open file

f =  open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="r")

with open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="w") as f:
    f.write("hello")

with open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="r") as f:
    f.read()



# Json 

{
    "name" : "vasya",
    "surname":"pupkin",
    "data" : {
        "x":1,
    }
}

# write json

import maya.cmds as cmds
import json

objects = cmds.listRelatives(cmds.ls(type="mesh"), p = 1 )

result = {}

for i in objects:
    result[i] = "sphere"

json_path = "C:/Users/borov/Desktop/MayaFiles/testData.json"

with open (json_path, "w") as f:
    # json.dump (result, f)
    f.write(json.dumps(result, indent = 4, sort_keys = True))



# read from json 

import maya.cmds as cmds
import json

json_path = "C:/Users/borov/Desktop/MayaFiles/testData.json"

fromFile = {}

with open (json_path, "r") as f:
    fromFile = json.load(f)

for key, value in fromFile.items():
    print key, value
    cmds.polySphere(name = key)



# adjust userPrefs.mel

import maya.cmds as cmds

myName = "VasyaPupkin"

cmds.optionVar(sv=("DeveloperName", myName))

print cmds.optionVar(q="DeveloperName")

cmds.optionVar(remove="DeveloperName")


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





# import module

import sys
packages = ["myProject"] # project list, that we would like to reload
for i in sys.modules.keys()[:]:
    for package in packages:
        if i.startswith(package):
            del(sys.modules[i])



import myProject.main
myProject.main.main()

# MAIN :

import os

def main():
    # print ("hello_world")

    filePath = __file__
    # print filePath

    root = os.path.dirname(filePath)
    # print (root)

    fileList = os.listdir(root)
    # print (fileList)

    for i in fileList:
        fullPath  = os.path.join(root, i)
        # print fullPath

        # print i , os.path.isdir(fullPath)
        # print i , os.path.isfile(fullPath)

        fileExists = os.path.exists(fullPath)
        print (fileExists)



import os

path = "C:/Users/borov/Documents/maya/scripts/myProject/test.py"

# print path.split("/")
# print path.split("/")[-1]
# print path.replace(path.split("/")[-1], "")

# print os.path.dirname(path)
# print os.path.basename(path)
# print os.path.splitext(path)[-1]

# print os.path.getsize(path)


path1 = "C:/Users/borov/Documents/maya/scripts/myProject/main.py"

path2 = "C:/Users/borov/Documents/maya/scripts/myProject/lib/hello.py"

print os.path.commonprefix([path, path1, path2])




# get all folders and files in dir

    for dirPath, dirNames, filesNames in os.walk(root):
        print dirPath
        print dirNames
        print filesNames



