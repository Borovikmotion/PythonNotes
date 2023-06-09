import maya.cmds as cmds
import json
import maya.mel as mel
import os
import maya.standalone
import sys

path = "D:/Work/66_pair_animation_root_motion"
refName = "timings"
currentName = "timings_01"




class CompareJson(object):
    def __init__(self, path, refName, currentName):
        self.json_path = path
        self.poseRefName = refName
        self.poseCurrentName = currentName
        self.jsonRefData = {}
        self.jsonCurrentData = {}
        self.jsonCompareData = {}
        self.nameSpace = ""
        self.result = []

        self.main()

    # read json
    def read_json(self, path, name):
        with open (path + "/" + name + ".json", "r") as f:
            jsonData  = json.load(f)
        return jsonData

    def main(self):
        self.jsonRefData = self.read_json(path = self.json_path, name = self.poseRefName)
        self.jsonCurrentData = self.read_json(path = self.json_path, name = self.poseCurrentName)

        animationFiles = []
        for i in self.jsonRefData.keys():
            animationFiles.append(i)

        for f in animationFiles:
            recorded = self.jsonRefData[f]
            current = self.jsonCurrentData[f]
            for key in recorded.keys():
                delta = abs(recorded[key] - current[key])
                self.result.append(delta)


firtstFramePose = ComparePoses(path = path_to_poses, refName = refPoseShortName, currentName = fileShortName + "_first_frame")


result[fileShortName + "_first_frame"] = firtstFramePose.result