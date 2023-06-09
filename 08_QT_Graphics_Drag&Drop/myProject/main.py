import os

def main():
    # print ("hello_world")

    filePath = __file__
    # print filePath

    root = os.path.dirname(filePath)
    # print (root)

    # fileList = os.listdir(root)
    # # print (fileList)

    # for i in fileList:
    #     fullPath  = os.path.join(root, i)
    #     # print fullPath

    #     # print i , os.path.isdir(fullPath)
    #     # print i , os.path.isfile(fullPath)

    #     fileExists = os.path.exists(fullPath)
    #     print (fileExists)

    # os.walk(root)

    for dirPath, dirNames, filesNames in os.walk(root):
        print dirPath
        print dirNames
        print filesNames

        