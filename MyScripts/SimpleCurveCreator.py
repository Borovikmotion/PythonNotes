import maya.cmds as cmds

selection = cmds.ls(sl=1)

for item in selection:
    # print item
    grp = cmds.group(n=item + "_GRP")
    crv = cmds.circle(n=item)
    cmds.parent(crv, grp)
    con = cmds.parentConstraint(item, grp, mo=0)
    cmds.delete(con)



# circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;
# select -r nurbsCircle2.cv[0:7] ;
# scale -r -p 0cm 0cm 0cm 6.324876 6.324876 6.324876 ;