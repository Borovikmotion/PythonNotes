import maya.cmds as cmds
import maya.mel as mel

class Rule(object):
    def __init__(self):
        self.rule_name = "Object History"
        self.rule_description = "All objects should not have any history"
        self.output = [] # if output is not empty - rule has not been passed
    
    def check(self):
        self.output = []
        inputStd = ["joint", "tweak", "skinCluster", "mesh", "dispLayer"]
        shapeArray = cmds.ls(type='mesh', dag=1, l=True)
        if shapeArray:
            polyArray = list(set(cmds.listRelatives(shapeArray, p=1, type="transform", f=True)))
            for obj in polyArray:
                tmpListOfinputs = cmds.listHistory(obj, lf=1, il=1,) # list of objects which have inputs
                for i in tmpListOfinputs:
                    i_type = cmds.nodeType(i)
                    if i_type not in inputStd:
                        self.output.append(obj)
                        break
        return self.output


    def fix(self):
        if self.output:
            for i in self.output:
                cmds.select(i)
                mel.eval("doBakeNonDefHistory(1, {\"prePost\"});")
                #deleting polyBlindData node
                tmpListOfinputs = cmds.listHistory(i, lf=1, il=1)
                for j in tmpListOfinputs:
                    j_type = cmds.nodeType(j)
                    if j_type == "polyBlindData":
                        try:
                            cmds.delete(j)
                        except:
                            pass
        output = self.check()
        return output