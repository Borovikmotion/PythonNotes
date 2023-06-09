import maya.cmds as cmds

class Rocket (object):
    def __init__(self, bodyRadius=1, bodyParts=1, partHeight=1.0, nozzleCount=1, nozzleHeight=1.0):
        # main
        self.bodyRadius = bodyRadius 
        self.bodyParts = bodyParts
        self.partHeight = partHeight
        self.nozzleCount = nozzleCount 
        self.nozzleHeight = nozzleHeight

        # additional
        self.rocketPartBB = []
        self.bodyPartOffset = 0
        self.nozzleRadius = 0
        self.nozzleXOffset = 0
        self.nozzleZOffset = 0
        self.nozzleBB = []

        # create body, nose cone and nozzle
        if self.bodyParts != 0:
            self.create_body()
            self.create_nose_cone()
        else:
            cmds.error("the rocket should contain at least 1 body part")
        
        if self.nozzleCount !=0:
            self.create_nozzle()
        else:
            cmds.error("the rocket should contain at least 1 nozzle")

    def create_body(self):
        # offset for the first body part 
        self.bodyPartOffset = self.partHeight/2 + self.nozzleHeight

        for i in range(0,self.bodyParts):
            rocketPart = cmds.polyCylinder(r=self.bodyRadius, h=self.partHeight)
            cmds.xform(rocketPart, ws=1, t=[0, self.bodyPartOffset, 0])
            self.rocketPartBB = cmds.xform(rocketPart, q=1, bb=1, ws=1)
            self.bodyPartOffset = self.rocketPartBB[4] + self.partHeight/2
            i+=1 

    def create_nose_cone(self):
        noseCone = cmds.polyCone(r=self.bodyRadius, h=self.partHeight)
        cmds.xform(noseCone, ws=1, t=[0, self.bodyPartOffset, 0])

    def create_nozzle(self):
        # initial nozzle offset:
        self.nozzleXOffset = self.rocketPartBB[0]

        for i in range(0,self.nozzleCount):
            if self.nozzleCount >1:
                self.nozzleRadius = self.bodyRadius/(self.nozzleCount-1)
            else:
                self.nozzleRadius = self.bodyRadius/self.nozzleCount
                self.nozzleXOffset = 0
            
            nozzle = cmds.polyCone(r=self.nozzleRadius, h=self.nozzleHeight)
            cmds.xform(nozzle, ws=1, t=[self.nozzleXOffset, self.nozzleHeight/2, self.nozzleZOffset])
            self.nozzleBB = cmds.xform(nozzle, q=1, bb=1, ws=1)
            self.nozzleXOffset = self.nozzleBB[3] + self.nozzleRadius
            i +=1


class RocketNew (Rocket):
    def __init__(self):
        super(RocketNew, self).__init__(bodyRadius, bodyParts, partHeight, nozzleCount, nozzleHeight)

    def create_stabilizers(self):
        cube = cmds.polyCube()[0]


myRocket = Rocket(bodyParts=3, bodyRadius=1.0, partHeight=3.0, nozzleCount=3, nozzleHeight=1.5)

# myNewRocket = RocketNew(bodyParts=3, bodyRadius=1.0, partHeight=3.0, nozzleCount=3, nozzleHeight=1.5)
