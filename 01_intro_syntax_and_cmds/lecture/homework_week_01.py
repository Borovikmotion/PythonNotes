import maya.cmds as cmds

minT = cmds.playbackOptions(q=1, min =1)
maxT = cmds.playbackOptions(q=1, max =1)

loc = cmds.spaceLocator()
cmds.setKeyframe(loc[0] + ".translateX", time=minT, v=-10)
cmds.setKeyframe(loc[0] + ".translateX", time=maxT, v=10)

count = 0
objects = []

while count < 10:
    s = cmds.polySphere()
    cmds.setAttr(s[0] + ".translateZ", count*2 )
    cmds.parentConstraint(loc, s, mo=1)
    count += 1
    objects.append(s[0])


for obj in objects:
    cmds.bakeResults(obj, time = (minT,maxT))

cmds.bakeResults(objects, time = (minT,maxT))