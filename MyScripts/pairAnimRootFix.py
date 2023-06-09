import maya.cmds as cmds
minT = cmds.playbackOptions(q=1, min=1)
maxT = cmds.playbackOptions(q=1, max=1)

selectionFull = cmds.ls(sl=1)

def main():
    selection = selectionFull[0]
    loc = cmds.spaceLocator()
    tempCon = cmds.parentConstraint(selection, loc, mo=0)
    cmds.bakeResults(loc, time = (minT, maxT))
    cmds.delete(tempCon)
    con = cmds.parentConstraint(loc, selection, mo=1)

    root_grp = cmds.group(empty=1, n= "scene_root_GRP")
    cmds.parent(loc, root_grp)

    cmds.currentTime(minT)

    offset_grp = cmds.group(empty=1, n= "offset_GRP")
    tempCon2 = cmds.parentConstraint(selection, offset_grp, mo=0)
    cmds.delete(tempCon2)

    cmds.parent(root_grp, offset_grp)
    cmds.xform(offset_grp, a = True, t = [0,0,0], ro = [-90,0,0] )
    cmds.bakeResults(selection, time = (minT, maxT))
    cmds.delete(offset_grp)

if selectionFull:
    main()
else:
    cmds.error("please select root joint")
