import maya.cmds as cmds
import random
import math

minT = cmds.playbackOptions(q=1, min =1)
maxT = cmds.playbackOptions(q=1, max =1)


def createPlanet(planetName, planetRadiusMin, planetRadiusMax, moonsCountMin, moonsCountMax, moonRadiusMin, moonRadiusMax, distanseBtwMoons = 0, colorDeviation = 0.1, rotationMultiplier = 4):
    # create main planet
    planetRadius = random.uniform(planetRadiusMin, planetRadiusMax)
    planet = cmds.polySphere(n = planetName, r = planetRadius)
    distance = planetRadius
    planetGrp = cmds.group(empty=1,n=planetName+"Grp")
    cmds.parent(planet,planetGrp)

    # color the planet 
    planetShader = cmds.shadingNode("lambert", n = "lambert"+planetName, asShader=1)
    randColorR = random.uniform(0, 1)
    randColorG = random.uniform(0, 1)
    randColorB = random.uniform(0, 1)
    cmds.setAttr(planetShader + ".color", randColorR, randColorG, randColorB, type="double3")
    cmds.select(planet)
    cmds.hyperShade(assign = planetShader)

    # random moon count
    moonsCount = random.randint(moonsCountMin, moonsCountMax)

    for i in range(moonsCount):
        
        # create moon
        moonRadius = random.uniform(moonRadiusMin, moonRadiusMax)
        moon = cmds.polySphere(n=planet[0]+ "_moon_" + str(i), r=moonRadius)
        distance = distance + moonRadius + distanseBtwMoons
        cmds.xform(moon, r= 1, t = [distance,0,0])
        distance = distance + moonRadius

        # color moon
        moonShader = cmds.shadingNode("lambert", n = "lambert"+moon[0], asShader=1)
        moonColorR = randColorR + random.uniform(colorDeviation*-1, colorDeviation)
        moonColorG = randColorG + random.uniform(colorDeviation*-1, colorDeviation)
        moonColorB = randColorB + random.uniform(colorDeviation*-1, colorDeviation)
        cmds.setAttr(moonShader + ".color", moonColorR, moonColorG, moonColorB, type="double3")
        cmds.select(moon)
        cmds.hyperShade(assign = moonShader)

        # create Yaw animation control
        rotationGrp = cmds.group(empty=1,n=moon[0]+"YawGroup"+ str(i))
        cmds.parent(moon,rotationGrp)

        # create offset control
        randPitch = random.uniform(-45,45)
        randYaw = random.uniform(0, 360)
        offsetGrp = cmds.group(empty=1,n=moon[0]+"OffsetGroup"+ str(i))
        cmds.parent(rotationGrp,offsetGrp)
        cmds.xform(offsetGrp,r= 1, ro=[0,randYaw,randPitch])

        # parent moon to planet master control
        cmds.parent(offsetGrp,planetGrp)

        # calculate rotation speed
        rotationCount = round(math.sqrt(moonsCount/(1 + i)))*rotationMultiplier
        if rotationCount < 1:
            rotationCount = 1

        # animate yaw control
        cmds.setKeyframe(rotationGrp + ".rotateY", time=minT, v=0, ott= "linear")
        cmds.setKeyframe(rotationGrp + ".rotateY", time=maxT, v=360*rotationCount, itt= "linear")
    
        # set planet distance 
        planetSystemRadius = distance
        planetControlGrp = planetGrp
    
    return planetSystemRadius

def createSolarSystem(starName, starRadiusMin, starRadiusMax, planetCountMin, planetCountMax,):

    # create star
    starRadius = random.uniform(starRadiusMin, starRadiusMax)

    star = cmds.polySphere(n = starName, r = starRadius)
    sDistance = starRadius
    starGrp = cmds.group(empty=1,n=starName+"Grp")
    cmds.parent(star,starGrp)

    # color the star
    starShader = cmds.shadingNode("lambert", n = "lambert"+starName, asShader=1)
    sRandColorR = random.uniform(0.7, 1)
    sRandColorG = random.uniform(0.7, 1)
    sRandColorB = random.uniform(0.7, 1)
    cmds.setAttr(starShader + ".color", sRandColorR, sRandColorG, sRandColorB, type="double3")
    cmds.select(star)
    cmds.hyperShade(assign = starShader)

    # get planet count
    planetCount = random.randint(planetCountMin, planetCountMax)
    planetDistance = 0

    for i in range(planetCount):
        planetName = "Earth"+str(i)

        planetSystemRadius = createPlanet(planetName = planetName, planetRadiusMin = 4, planetRadiusMax = 7, moonsCountMin = 5, moonsCountMax = 15, moonRadiusMin = 0.1, moonRadiusMax = 1.1, )

        planetGrp = planetName + "Grp"

        if i == 0:
            planetDistance = planetDistance + starRadius + planetSystemRadius
        else :
            planetDistance = planetDistance + planetSystemRadius

        # move planet grp away from sun
        cmds.xform(planetGrp,r= 1, t = [planetDistance,0,0])
        planetDistance = planetDistance + planetSystemRadius

        # create Yaw animation control
        planetRotationGrp = cmds.group(empty=1,n=planetGrp+"YawGroup"+ str(i))
        cmds.parent(planetGrp,planetRotationGrp)

        # create offset control
        randPitch = random.uniform(-45,45)
        randYaw = random.uniform(0, 360)
        planetOffsetGrp = cmds.group(empty=1,n=planetName+"OffsetGroup"+ str(i))
        cmds.parent(planetRotationGrp,planetOffsetGrp)
        cmds.xform(planetOffsetGrp,r= 1, ro=[0,randYaw,randPitch])

        # # # calculate rotation speed
        rotationCount = round(math.sqrt(planetCount/(1 + i)))
        if rotationCount < 1:
            rotationCount = 1

        # # # animate yaw control
        cmds.setKeyframe(planetRotationGrp + ".rotateY", time=minT, v=0, ott= "linear")
        cmds.setKeyframe(planetRotationGrp + ".rotateY", time=maxT, v=360*rotationCount, itt= "linear")

        cmds.parent(planetOffsetGrp,starGrp)

createSolarSystem(starName = "Sun", starRadiusMin = 20, starRadiusMax = 30, planetCountMin = 5, planetCountMax =8,)




# createPlanet(planetName = "Earth", planetRadiusMin = 4, planetRadiusMax = 7, moonsCountMin = 5, moonsCountMax = 15, moonRadiusMin = 0.3, moonRadiusMax = 1.5)