
""" CONSTRAINTS """
# parent, point, orient constraints without offset 
pCon = cmds.parentConstraint(source, target, mo=0)
cmds.pointConstraint(source, target, mo=0)
cmds.orientConstraint(source, target, mo=0)

# aim constraint
# source = end locator, target = our object
cmds.aimConstraint(source, target, worldUpType = "object", worldUpObject = upLoc[0], mo=1)
