""" C:\Program Files\Autodesk\Maya2020\Python\lib\site-packages\maya\OpenMaya.pyc """

""" как запустить мел скрипт через питон """
import maya.cmds as cmds
import maya.mel
maya.mel.eval("polySphere -r 1 -n MyS")


""" типы данных  """
print type (x)
a = "1"
print float(a) 

a = None
b = 3
if a == b:
    print a 
else:
    print b 


""" модификация строк """
a = "x"
b = "y"
c = "z"
res = "Variables: {} {} {}".format(a,b,c) 
print res




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




""" Списки  """
a=["x", "y" ]
a.append ("z")

print a[2]

""" списки внутри списков """
a=["x", "y" ]
a.append("z")
a.append([1,2,3])
print a[3][2]

a.insert(0,"z")
a.remove("y")

a = [4,1,7,0,5]
a.sort()
print a




""" Cловари """
a = {"axX":0, "axY":1, "axZ":2}
print a["axY"]

a = {"X":0, "Y":1, "Z":2}
a["Z"] = 365




""" IF ELSE  """
a = 2
if a==3 and a>0:
    print "yes"
else:
    print "no"

> < >= <= != 
and or 
(...or...) and 
(...or...) and: if True and True 


""" if not ==  """
a = 2
if a==3:
    print "3"
elif a==4:
    print "4"
elif a==10:
    print "10"
else:
    print "no"







""" пройтись по списку в цикле """
a = ["x", "y", "z"]

for element in a:
    print element 

a = ["a", "b", "c"]

for index, value in enumerate(a):
    print index, value





""" Выделение  """
objects = cmds.ls(selection=1, long=1)
if not objects:
    #raise ValueError ('nothing is selected')
    cmds.error ('nothing is selected')
resultList = []


for obj in objects:
    if cmds.nodeType(obj) != 'transform':
        continue
    child = cmds.listRelatives(obj, children = 1)[0]
    type = cmds.nodeType(child)
    if type == "nurbsCurve":
        resultList.append(obj)
print resultList
if resultList:
    cmds.select(resultList)
else: 
    cmds.warning('empty') 




cmds.currentTime()
cmds.setAttr(Sphere[0] + ".translateX", -10)
xform()

maya select object callback 

def abc(x,y,z):
    pass


import time
print time






























