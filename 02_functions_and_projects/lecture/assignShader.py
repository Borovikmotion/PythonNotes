# create shader node
shader = cmds.shadingNode("lambert", n = "lambertRed", asShader=1)

# set color attribute - now shader has "red" color
# color must be in range 0..1, i.e. White = 1, Black = 0
cmds.setAttr(shader + ".color", 1, 0.2, 0.2, type="double3")

# select obejct and assign shader to it
cmds.select("pCube1")
cmds.hyperShade(assign = shader)