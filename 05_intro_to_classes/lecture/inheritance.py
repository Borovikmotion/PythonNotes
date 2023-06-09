import maya.cmds as cmds

class Car(object):
    
    def __init__(self, width = 1, length = 1, height = 1, radius = 1):
        
        self.width = width
        self.length = length
        self.height = height
        self.radius = radius
        
        
        self.createBody()
        self.createWheels()
        
    def createBody(self):
        
        carBody = cmds.polyCube(n= "body")
        
        self.carBodyNode = carBody[1]
        self.carBodyName = carBody[0]
        
        cmds.setAttr(self.carBodyNode + ".width", self.width)     
        cmds.setAttr(self.carBodyNode + ".height", self.height)   
        cmds.setAttr(self.carBodyNode + ".depth", self.length)   
        
        cmds.xform(self.carBodyName, t = [0,3,0], r=1)
        
    def createWheels(self):
        
        self.carBB = cmds.xform(self.carBodyName, q=1, bb=1, ws=1)
        
        # create wheel A
        
        wheel_1 = cmds.polySphere(n = "wheel1", radius = self.radius)[0]
        cmds.xform(wheel_1, ws=1, t = [self.carBB[0], self.carBB[1],self.carBB[2]])
        
        wheel_2 = cmds.polySphere(n = "wheel2", radius = self.radius)[0]
        cmds.xform(wheel_2, ws=1, t = [self.carBB[3], self.carBB[1],self.carBB[2]])
        
        wheel_3 = cmds.polySphere(n = "wheel3", radius = self.radius)[0]
        cmds.xform(wheel_3, ws=1, t = [self.carBB[0], self.carBB[1],self.carBB[5]])
        
        wheel_4 = cmds.polySphere(n = "wheel4", radius = self.radius)[0]
        cmds.xform(wheel_4, ws=1, t = [self.carBB[3], self.carBB[1],self.carBB[5]])
        

class SuperCar(Car):
    
    def __init__(self, width = 0, length = 0, height = 0, radius =  0):
        
        super(SuperCar, self).__init__(width = width, length = length, height = height, radius =  radius)
        
        self.createSuperCube()
        
        
    def createSuperCube(self):
        
        
        cube = cmds.polyCube()[0]
        
        bb = cmds.xform(cube, q=1, bb=1, ws=1)
        bb_centerPointY = (bb[4] - bb[1])/2
        
        # self.carBB
        platformTop = self.carBB[4]
        
        offset = platformTop + bb_centerPointY
        
        cmds.xform(cube, t = [0, offset, 0], r=1)
        
        
        
        

    
myCar = SuperCar(width = 1, length = 3, height = 0.2, radius =  0.2)