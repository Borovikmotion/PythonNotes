""" C:\Program Files\Autodesk\Maya2020\Python\lib\site-packages\maya\OpenMaya.pyc """


""" CMDS """
s = cmds.polySphere()
print s[1]

Sph = cmds.polySphere()
Grp = cmds.group(em=1)
cmds.parent(Sph[0], Grp)

# Query 
Sph = cmds.polySphere()
print cmds.polySphere(Sph[0], q=1, r=1)

# Edit
cmds.polySphere(Sph[0], e=1, r=5)
