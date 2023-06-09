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