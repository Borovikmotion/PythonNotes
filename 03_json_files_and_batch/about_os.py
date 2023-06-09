
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
    filePath = __file__
    print(filePath)
    root = os.path.dirname(filePath)
    print(root)
    fileList = os.listdir(root)
    print(fileList)
    for i in fileList:
        fullPath  = os.path.join(root, i)
        print(fullPath)
        print(i , os.path.isdir(fullPath))
        print(i , os.path.isfile(fullPath))

        fileExists = os.path.exists(fullPath)
        print(fileExists)



import os
path = "C:/Users/borov/Documents/maya/scripts/myProject/test.py"

print path.split("/")
print path.split("/")[-1]
print path.replace(path.split("/")[-1], "")

print os.path.dirname(path)
print os.path.basename(path)
print os.path.splitext(path)[-1]

print os.path.getsize(path)


path1 = "C:/Users/borov/Documents/maya/scripts/myProject/main.py"
path2 = "C:/Users/borov/Documents/maya/scripts/myProject/lib/hello.py"
print os.path.commonprefix([path, path1, path2])



# get all folders and files in dir
for dirPath, dirNames, filesNames in os.walk(root):
    print dirPath
    print dirNames
    print filesNames
