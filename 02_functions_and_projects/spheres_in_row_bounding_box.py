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
