import maya.cmds as cmds
import random

""" OTHER STUFF """
# assign material to the object
planet = cmds.polySphere(n = planetName, r = planetRadius)
planetShader = cmds.shadingNode("lambert", n = "lambert"+planetName, asShader=1)
randColorR = random.uniform(0, 1)
randColorG = random.uniform(0, 1)
randColorB = random.uniform(0, 1)
cmds.setAttr(planetShader + ".color", randColorR, randColorG, randColorB, type="double3")
cmds.select(planet)
cmds.hyperShade(assign = planetShader)