import maya.cmds as cmds
import random


def assignNewShader(obj = None, attribute = "color", color = [100,100,100], colorVariation = False, randomColor = False):

    objShape = cmds.listRelatives(obj, c=1, f=1)[0]

    shader = cmds.shadingNode("lambert", n = "planetShader", asShader=1)

    R = 0
    G = 0
    B = 0

    if randomColor:
        R = random.randint(50, 255)
        G = random.randint(50, 255)
        B = random.randint(50, 255) 

    elif colorVariation:
        R = random.randint(color[0] - 50, color[0] + 50)
        G = random.randint(color[1] - 50, color[1] + 50)
        B = random.randint(color[2] - 50, color[2] + 50)
    else:
        R = color[0]
        G = color[1]
        B = color[2]

    cmds.setAttr(shader + "." + attribute, R/255.0, G/255.0, B/255.0, type = "double3")

    cmds.select(objShape)

    cmds.hyperShade(assign = shader)

    cmds.select(d = 1)

    return [R,G,B]
    

def animate(rotationGrp = None):

    if not rotationGrp:
        cmds.error("please define rotation group")
        return

    animationCycles = random.randint(1,5)

    startTime = cmds.playbackOptions(q=1, minTime = 1)
    endtime = cmds.playbackOptions(q=1, maxTime=1)
    
    cmds.cutKey(rotationGrp, time = (startTime, endtime), attribute = "rotateY")

    cmds.setKeyframe(rotationGrp, time = startTime, attribute = "rotateY", value = 0)
    cmds.setKeyframe(rotationGrp, time = endtime, attribute = "rotateY", value = 360 * animationCycles)

    cmds.selectKey(rotationGrp, time = (startTime, endtime), attribute = "rotateY", keyframe = True)
    cmds.keyTangent(inTangentType = "linear", outTangentType = "linear")


def createMoon(moonName = "test", radius = 1, moonColor = None, offsetDistance = 0):
    
    moonGeo = cmds.polySphere(name = moonName, radius = radius)[0]

    grp_moon = cmds.group(empty=1, name = moonName + "_moon")
    grp_orbitPlane = cmds.group(empty=1, name = moonName + "_orbitPlane", p=grp_moon)
    grp_rotation = cmds.group(empty=1, name = moonName + "_rotation", p=grp_orbitPlane)
    grp_rotationOffset = cmds.group(empty=1, name = moonName + "_rotationOffset", p=grp_rotation)
    grp_position = cmds.group(empty=1, name = moonName + "_position", p=grp_rotationOffset)

    cmds.parent(moonGeo, grp_position)
    
    moonGeo_FullPath = cmds.ls(moonGeo, l=1)[0] 

    cmds.move(offsetDistance, 0, 0, grp_position)

    rotateZ = random.uniform(-20,20)
    cmds.rotate(0,0, rotateZ, grp_orbitPlane)

    rotateY = random.uniform(0,360)
    cmds.rotate(0, rotateY, 0, grp_rotationOffset)


    animate(rotationGrp = grp_rotation)


    assignNewShader(obj = moonGeo_FullPath, color = moonColor, colorVariation=True)


    return grp_moon

    


def createPlanet(planetName = "Earth"):


    moons = random.randint(3,17)
    
    planetRadius = random.uniform(1,3)  
    planetGeo = cmds.polySphere(n = planetName, r = planetRadius)[0]


    grp_planet = cmds.group(empty=1, name = planetName + "_planet")
    grp_geo = cmds.group(empty=1, name = planetName + "_geo", parent = grp_planet)

    cmds.parent(planetGeo, grp_geo)

    planetGeo_FullPath = cmds.ls(planetGeo, l=1)[0] 

    color = assignNewShader(obj = planetGeo_FullPath, color = [255,255,255], randomColor=True)


    moonDistance = planetRadius

    for i in range(moons):  

        moonRadius = random.uniform(0.1, 0.6)
        moonOffset = moonDistance + moonRadius + 1

        moonDistance = moonOffset + moonRadius

        moon = createMoon(moonName="{}_{}".format(planetName, i), offsetDistance=moonOffset, radius= moonRadius, moonColor=color)

        cmds.parent(moon, grp_planet)




def run():
    

    if cmds.ls("*_planet"):
        cmds.delete(cmds.ls("*_planet"))


    createPlanet()


