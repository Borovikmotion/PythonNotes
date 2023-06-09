import math
import maya.cmds as cmds
tor_transform = "pTorus1"
tor = "polyTorus1"
tor_rad = cmds.getAttr(tor + ".radius")
tor_section_rad = cmds.getAttr(tor + ".sectionRadius")
segments = cmds.getAttr(tor + ".subdivisionsAxis")
tor_coord = cmds.xform(tor_transform, q=1, t=1)



radius = tor_rad + tor_section_rad
segments = segments
segment_deg = 360.0 / segments
segment_rad = segment_deg * 0.01745327778

for i in range(segments):
    angle = i * segment_rad
    
    y = math.cos(angle) * radius
    z = math.sin(angle) * radius
    
    loc = cmds.spaceLocator()
    
    cmds.xform(loc, t=[tor_coord[0], y+tor_coord[1], z+tor_coord[2]])