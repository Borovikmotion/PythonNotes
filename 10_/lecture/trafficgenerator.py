import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import random
import math

class CurvePath(object):

    def __init__(self, origCurve = None):

        self.origCurve = origCurve
        self.origCurveShape = None

        self.curve = None
        self.curveShape = None

        self.buildCurve()


    def getCurve(self, shape = False):
        """
        Returns curveTransform or curveShape
        """

        if not shape:
            return self.curve
        
        return self.curveShape


    def getCVPosTangent(self, cvNum = 0):

        """
        Get curve CV position and tangent vector in World Space
        """

        # OpenMaya Way

        curveSelection = OpenMaya.MSelectionList() # list that contains objects
        curveSelection.add(self.origCurveShape) # put objects in that list

        curveDP = OpenMaya.MDagPath() # create Dag class object
        
        curveSelection.getDagPath(0, curveDP) # get DagPath to our curve
        
        curveFn = OpenMaya.MFnNurbsCurve(curveDP) #Get NurbsCurve FunctionSet
        pnt = OpenMaya.MPoint()       #create Maya 3D Point class
        curveFn.getCV(cvNum, pnt, OpenMaya.MSpace.kWorld) #get CV position in World Space and save to pnt

        #as Python has no such a thing like Pointers - we use MayaAPI native pointer
        paramUtil = OpenMaya.MScriptUtil()  
        paramPtr = paramUtil.asDoublePtr() # type of our pointer - double

        point = curveFn.closestPoint(pnt, paramPtr, 0.0, OpenMaya.MSpace.kWorld) #get closest point position
        curveFn.getParamAtPoint(point, paramPtr, OpenMaya.MSpace.kWorld) #get param at the closest point

        param = paramUtil.getDouble(paramPtr)  #from pointer -> return the actual number
        
        tangent = curveFn.tangent(param, OpenMaya.MSpace.kWorld) # get tangent vector based on param U value

        tangent.normalize()  #normalize tangent

        return [round(pnt.x, 10), round(pnt.y, 10), round(pnt.z, 10)], [round(tangent.x, 10), round(tangent.y,10), round(tangent.z, 10)]

    
    def crossProduct(self, vecA = [0,0,0], vecB = [0,1,0]):

        """
        Find a vector that is perpendicular both to vecA and vecB
        """

        cross = [   vecA[1]*vecB[2] - vecA[2]*vecB[1],
                    vecA[2]*vecB[0] - vecA[0]*vecB[2],
                    vecA[0]*vecB[1] - vecA[1]*vecB[0]]

        # OpenMaya Way
        c = OpenMaya.MVector(cross[0], cross[1], cross[2])
        c.normalize()

        # Math Way
        length = math.sqrt((cross[0]*cross[0]) + (cross[1]*cross[1]) + (cross[2]*cross[2]))
        norm = [cross[0]/length, cross[1]/length, cross[2]/length]

        # return [c.x, c.y, c.z]
        return norm


    def buildCurve(self, group = True, groupPath = "paths"):

        """
        Main build curve method
        """

        #get curve shape 
        self.origCurveShape = cmds.listRelatives(self.origCurve, c=1, f=1)[0]

        #get curve control points
        numberOfCV =  len(cmds.getAttr(self.origCurveShape + ".cv[:]"))

        #new curve point list
        newCurvePoints = []
        dirV = random.choice([-1,1]) #vector offset direction

        # for each CV get World position and Tangents
        for cv in range(0, numberOfCV):

            # get current CV position and tangent
            cvPos, cvTg = self.getCVPosTangent(cvNum = cv)

            #create test spheres
            # sphere = cmds.polySphere(r=0.2, n="crvSph##")
            # cmds.move(cvPos[0], cvPos[1], cvPos[2])

            #get cross product
            crossProductVec = self.crossProduct(vecA = [0,1,0], vecB = cvTg)

            #create offset vector
            # offset = 1 * dirV
            offset = random.uniform(0.1, 30) * dirV
            newCurvePoints.append([cvPos[0] + crossProductVec[0] * offset, cvPos[1] + crossProductVec[1] * offset, cvPos[2] + crossProductVec[2] * offset])

            #create test offset sphere
            # sphere = cmds.polySphere(r=0.1, n="crvCrossSph##")
            # cmds.move(cvPos[0] + crossProductVec[0] * offset, cvPos[1] + crossProductVec[1] * offset, cvPos[2] + crossProductVec[2] * offset)

        #create move curve
        self.curve = cmds.curve(d=3, p = newCurvePoints, n="pathCurve##")

        #reverse a curve
        if dirV == 1:
            cmds.reverseCurve(self.curve, rpo=1, ch=1)

        #put the curve under a group
        if group:
            if not cmds.objExists(groupPath):
                grp = cmds.group(em=1, n = groupPath.split("|")[-1]) #create empty group
                cmds.hide(grp)

            cmds.parent( self.curve, groupPath) 
            self.curve = cmds.ls(self.curve, l=1)

        #get shape path 
        self.curveShape = cmds.listRelatives(self.curve, c = 1, f = 1)


def main(numberOfPaths = 0):

    # GET SELECTIONS

    #get user seelction
    selection = cmds.ls(sl=1, l=1)

    #check first selected object - if it's not a curve -> exit
    selectedCurve = selection[0]
    selectedCurveShape = cmds.listRelatives(selectedCurve, c=1, f=1)[0]
    if not cmds.nodeType(selectedCurveShape) == "nurbsCurve":
        cmds.error("Please make sure first selected object is a NURBS Curve")
        return 

    #get ships
    shipsSelection = selection[1 : ]
    numberOfPaths = len(shipsSelection)

    #create curves 
    for i in range(0, numberOfPaths):

        curveInstance = CurvePath(origCurve = selectedCurve)

        # ANIMATION

        #apply Motion Path to a ship/curveInstance
        cmds.select(curveInstance.getCurve())
        cmds.select(shipsSelection[i], add = 1)
        motionPath = cmds.pathAnimation(    fractionMode =1,
                                            follow = 1,
                                            followAxis = "z",
                                            upAxis = "y",
                                            worldUpType = "vector",
                                            worldUpVector = [0, 1, 0],
                                            inverseUp = 0, 
                                            inverseFront = 1,
                                            bank = 0,
                                            startTimeU = cmds.playbackOptions(q=1, minTime = 1),
                                            endTimeU = cmds.playbackOptions(q=1, maxTime = 1))
        
        # ANIMATION ADJUSTMENT

        # make motion path animation - linear
        startTime = cmds.playbackOptions(query = True, minTime = True)
        endTime = cmds.playbackOptions(query = True, maxTime = True)

        cmds.selectKey(motionPath, time = (startTime, endTime), attribute = "uValue", keyframe = True)
        cmds.keyTangent(inTangentType = "linear", outTangentType = "linear")

        #shift time keys to a certain position
        time_length = endTime - startTime
        time_offset = random.randint(0, time_length)
        cmds.keyframe(motionPath + ".uValue", e=1, r=1, o="over", tc = -1 * time_offset)

        #set cycle
        cmds.setInfinity(poi = "cycle")



    #select curve
    cmds.select(selectedCurve)



main(numberOfPaths = 4)