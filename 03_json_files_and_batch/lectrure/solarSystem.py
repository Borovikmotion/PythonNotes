import maya.cmds as cmds
import random


def setSpacePosition(plane = None, rotationOffset = None, offset = None, pos = None, spreadAngle = 10):

    """
    Defines initial moon position and plane of rotation
    """

    #move moon to the distance
    cmds.move(offset, 0, 0, pos)  # +X direction

    #rotate moon plane to a random degree
    rotZ = random.uniform(-1 * spreadAngle, spreadAngle)
    cmds.rotate(0,0,rotZ,plane)

    # rotate moon around its planet
    rotY = random.uniform(0,360)
    cmds.rotate(0,rotY,0,rotationOffset)



def animate(rotator = None, animationCycles = 20, rotationDirection = None, axisGroup = None, axisRotationCycles=20):
    
    """
    Adds animation keys to a planet or a moon ( + animation of a planet around the planet's axis)
    """

    #get timeline Start frame and End frame
    startTime = cmds.playbackOptions(query = True, minTime = True)
    endTime = cmds.playbackOptions(query = True, maxTime = True)

    #defines should a moon to be rotated CV or CCV
    if not rotationDirection:
        rotationDirection = random.choice([-1,1])

    cmds.cutKey(rotator, time = (startTime, endTime), attribute = "rotateY")
    cmds.setKeyframe(rotator, time = startTime, attribute = "rotateY", value = 0)
    cmds.setKeyframe(rotator, time = endTime, attribute = "rotateY", value = 360 * animationCycles * rotationDirection)
    cmds.selectKey(rotator, time = (startTime, endTime), attribute = "rotateY", keyframe = True)
    cmds.keyTangent(inTangentType = "linear", outTangentType = "linear")

    if axisGroup:
        #rotate body around its own axis (for planets)
        cmds.cutKey(axisGroup, time = (startTime, endTime), attribute = "rotateY")
        cmds.setKeyframe(axisGroup, time = startTime, attribute = "rotateY", value = 0)
        cmds.setKeyframe(axisGroup, time = endTime, attribute = "rotateY", value = 360 * axisRotationCycles)
        cmds.selectKey(axisGroup, time = (startTime, endTime), attribute = "rotateY", keyframe = True)
        cmds.keyTangent(inTangentType = "linear", outTangentType = "linear")



def newShader(obj = None, channel = "color", color = [100,100,100], colorVariation = False, randomColor = False):

    """
    Assignes a new shader to a geo
    """

    #if we passed in a transform node - get its mesh
    if not cmds.nodeType(obj) == "mesh":
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

    cmds.setAttr(shader + "." + channel, R/255.0, G/255.0, B/255.0, type="double3")
    cmds.select(objShape)
    cmds.hyperShade(assign = shader)
    cmds.select(d=1)

    return [R,G,B]    



def createMoon(moonName = "io", offsetDistance = 0, radius = 0.5, planetColor = None):
    """
    Creates a moon
    """

    #create moon geo
    moonGeo = cmds.polySphere(n = moonName, r = radius)
    moonGeo = moonGeo[0]

    #create moon hierarchy
    grp_moon = cmds.group(em=1, n = moonName + "_moon")
    grp_plane = cmds.group(em=1, n = moonName + "_plane", p = grp_moon)
    grp_rotation = cmds.group(em=1, n = moonName + "_rotation", p = grp_plane)
    grp_rotationOffset = cmds.group(em=1, n = moonName + "_rotationOffset", p = grp_rotation)
    grp_pos = cmds.group(em=1, n = moonName + "_position", p = grp_rotationOffset)

    #put the moon under the hierarchy
    cmds.parent(moonGeo, grp_pos)
    moontGeoPath = cmds.ls(moonGeo, l=1)[0]

    # Place the moon in space
    setSpacePosition(plane = grp_plane, rotationOffset = grp_rotationOffset, offset = offsetDistance, pos = grp_pos)

    #animate moons around the planet
    animate(rotator = grp_rotation, animationCycles=10)

    if planetColor:
        newShader(obj = moontGeoPath,  color=planetColor,  colorVariation=True)

    return grp_moon



def createPlanet(planetName = "mars", moons = 3, offsetDistance = 0):
    """
    Creates a planet
    """

    # create planet geo
    planetRadius = random.uniform(1,3)
    planetGeo = cmds.polySphere(n=planetName, r = planetRadius)
    planetGeo = planetGeo[0] # get transform node

    # create planet hierarchy
    grp_planet = cmds.group(em=1, n = planetName + "_planet")
    grp_plane = cmds.group(em=1, n = planetName + "_plane", p = grp_planet)
    grp_rotation = cmds.group(em=1, n = planetName + "_rotation", p = grp_plane)
    grp_rotationOffset = cmds.group(em=1, n = planetName + "_rotationOffset", p = grp_rotation)
    grp_pos = cmds.group(em=1, n = planetName + "_position", p = grp_rotationOffset)

    #parent planet geo to grp_pos
    cmds.parent(planetGeo, grp_pos)
    planetGeoPath = cmds.ls(planetGeo, l=1)[0]

    #assign planet shader
    color = newShader(obj = planetGeoPath,  color=[255,255,255],  randomColor = True)

    #generate initial information
    moonDistance = planetRadius
    planetDistance = offsetDistance

    # create moons
    for i in range(0,moons): 

        moonRadius = random.uniform(0.1, 0.6)
        moonOffset = moonDistance + 1 + moonRadius
        moonDistance = moonOffset + moonRadius # update the moon distance

        planetDistance += moonDistance #increase the planet distance
        moon = createMoon(moonName= planetName + str(i), offsetDistance = moonOffset, radius=moonRadius, planetColor = color)
        
        cmds.parentConstraint(grp_pos, moon, maintainOffset = 1, skipRotate=["x", "y", "z"])

        cmds.parent(moon, grp_planet)

     # Place the planet in space
    setSpacePosition(plane = grp_plane, rotationOffset = grp_rotationOffset, offset = offsetDistance, pos = grp_pos)

    # animate planet
    animate(rotator = grp_rotation, animationCycles=1, rotationDirection=1, axisGroup = grp_pos)

    return planetDistance, grp_planet



def createStarSystem(minPlanets = 1, maxPlanets = 1, maxPlanetMoons = 0, starName = "test", starRadius = 10):

    """
    Creates a star with planets and moons
    """

    #Create a star geo
    starGeo = cmds.polySphere(n=starName, r = starRadius) 
    starGeo = starGeo[0] 

    #create star hierarchy
    grp_starSystem = cmds.group(em=1, n = starName + "_system")
    grp_star = cmds.group(em=1, n = starName + "_star", p = grp_starSystem)

    #parent star under the star group
    cmds.parent(starGeo, grp_star)
    starGeo = cmds.ls(starGeo, l=1)[0]

    #generate some initial information
    distance = starRadius
    planets = random.randint(minPlanets, maxPlanets)

    for i in range(1, planets):

        #generate number of moons for the planet
        numberOfMoons = random.randint(1, maxPlanetMoons)

        #how far the planet should be from the star
        offset = 20 + distance

        #generate number of moons
        numberOfMoons = random.randint(0, maxPlanetMoons)

        #create planet with moons
        distance, planet = createPlanet(moons = numberOfMoons, planetName="mars" + str(i), offsetDistance = offset)

        #put the planet_group under a star hierarchy
        cmds.parent(planet,  grp_starSystem)


    #assign shader to the star
    newShader(obj = starGeo, channel="ambientColor", color=[255,255,255])


def main():

    #clear the scene
    if cmds.ls("*system*"):
        cmds.delete(cmds.ls("*system*"))

    if cmds.ls("*planetShader*"):
        cmds.delete(cmds.ls("*planetShader*"))

    #create a solar system
    createStarSystem(minPlanets = 3, maxPlanets = 9, maxPlanetMoons = 5, starName = "sun", starRadius = 10)

    #deselect everything at the end
    cmds.select(d= 1)

  

main()
