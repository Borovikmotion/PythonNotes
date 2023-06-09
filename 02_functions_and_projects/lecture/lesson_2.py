""" FUNCTIONS """

import maya.cmds as cmds

def create_object(objName, grpName, objType = "sphere"):
    if objType == "sphere":
        obj = cmds.polySphere(n=objName)[0]
    elif objType == "cube":
        obj = cmds.polyCube(n=objName)[0]
    grp = cmds.group(empty=1,n=grpName)
    cmds.parent(obj,grp)
    return grp 

# create_object("helloSphere", "helloGroup")
# create_object("hiSphere", "hiGroup")
# create_object("yoSphere", "yoGroup")
# create_object("yocube", "yoCube", objType = "cube")

def moveUp(objectName, distance):
    if distance < 0:
        cmds.error("please use distance more than zero") 
    cmds.xform(objectName, worldSpace=1, r=1, translation=[0, distance,0])

def main():
    mygroup = create_object("cube", "cubeGRP", objType = "cube")
    moveUp(mygroup, 3)

main()



""" WORK WITH STRINGS """

name = "VasyaPupkin"
print name[0]
print name.lower()
print name.upper()
print name.replace("Pup", "hyup")
print name.split("a")
print name.title()
age = 32
height = 185
print ("Name: {} age {} : height: {} ".format (name,age,height))




""" WORK WITH LISTS """
# basic operations like merge lists, delete enelements, add elemtns
a = ['x', 'y', 'z']
b = ['a', 'b', 'c']

a.append("RRR")
a = a + b 
a.extend(b)
a.insert(1,'RRR')
a.remove('z')
a.pop()
print(a)
print(a.index('x'))
print(len (a))
print(a.count('x'))
a.sort()
a.sort(reverse=True)


# maya selection
# get list of selected objects, if translate Y < 0 then morrir it relatively to XZ plane
selection = cmds.ls(sl=1, l =1)
print (selection)
result = []

for obj in selection:
    # print obj 
    tr = cmds.xform(obj, q=1, t =1)
    ro = cmds.xform(obj, q=1, ro =1)
    sc = cmds.xform(obj, q=1, r=1, s =1)
    if tr[1] < 0:
        result.append(obj)
# print result

if len(result):
    for obj in result:
        tr = cmds.xform(obj, q=1, t =1)
        new_tr = [0,tr[1]*-1, 0]
        cmds.xform(obj, r=1, t = new_tr)
    print obj 

# same code, but optimized
for obj in selection:
    tr = cmds.xform(obj, q=1, t =1)
    if tr[1] < 0:
        new_tr = [0,tr[1]*-1, 0]
        cmds.xform(obj, r=1, t = new_tr)


""" ABOUT DICTIONARES  """

a = {"pSphere1":1, "pSphere2":2,"pSphere3":3,"pSphere4":{"x":1},"pSphere5":5 }

# get element
print a ["pSphere4"] ["x"]

# how to itterate a dictionary
for i in a:
    print i 
    print a[i]

for i in a.keys():
    print i

for i in a.values():
    print i 

for k, v in a.items():
    print k, v

# how to modify a dictionary
# add many elements
b = {'x':1, 'y':2, 'z':3}
a.update(b)
print a

#modify element
b["haha"]=123

# delete element
b.pop("y")
print b



""" CLASSES """
class A:
    def __init__(self):
        self.a=1
        self.b=2

x = A()
y = A()

print x, y 

d = {"pSphere1":x, "pSphere2":y}




""" DEBUG """

print d["pSphere1"]

def scaleSphere(name, x, y, z):
    if x==0:
        print "x=0"
        x=1
    elif y==0:
        print "y=0"
        y=1
    elif z==0:
        print "z=0"
        z=1
    cmds.xform(name, a=1, s =[x,y,z])

# or raise an error with cmds or python method
def scaleSphere(name, x, y, z):
    if x==0 or y==0 or z==0:
        # print "dont use zero"
        # return 
        # raise AttributeError ("dont use zero")
        cmds.error("dont use zero")
    cmds.xform(name, a=1, s =[x,y,z])

scaleSphere("pSphere1", 1, 0, 3)


""" TRY EXCEPT """
# finnaly - a block of code which will be run anyway after try or exeption
def div(a,b):
    try:
        c = a/b
    except Exception as e:
        print e
        print "dont use zero"
        c = None
    finally:
        print "finally"
    return c

result =  div (4,0)

if result:
    print "yes"
else:
    print "no"



""" additional example with SPHERES """

# create a bunch of sprehers in one line
def generateSpheres(minCount,maxCount,minR,maxR):
    distance = 0
    count = random.randint(minCount,maxCount)

    for i in range(count):
        newR = random.uniform(minR, maxR) 
        sph = cmds.polySphere(r = newR)[0]
        rad = cmds.polySphere(sph, q=1, r=1)
        if i > 0:
            distance = distance + rad
        cmds.xform(sph, translation = [distance,0,0])
        distance = distance + rad 
generateSpheres(4,20,1,20)

# create a bunch of sprehers in one line, but use bounding box to find out the borders of the object
def generateSpheres(minCount,maxCount,minR,maxR):
    distance = 0
    count = random.randint(minCount,maxCount)
    for i in range(count):
        rad = random.uniform(minR, maxR) 
        obj = cmds.polySphere(r = rad)[0]
        bBox = cmds.xform(obj, q=1, bb=1)
        if i > 0:
            distance = distance + bBox[3]
        cmds.xform(obj,t=[distance+bBox[3], 0,0])
        distance = distance + bBox[3]
generateSpheres(4,20,1,20)





# this PC - documents - maya
# maya.env
PYTHONPATH = ""
# to google - maya file path variables

import myScript
myScript.main()