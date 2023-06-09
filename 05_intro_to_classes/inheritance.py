""" INHERITANCE """

class A(object):
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.y = 1
        # var x is overrided
        self.x = 13

p = B()

print p.x
print p.y




# simple examples
import maya.cmds as cmds

class Human(object):
    def __init__(self):
        self.x = 1
    def print_name(self):
        print ("Vasya")


class SuperHuman(Human):
    def __init__(self):
        self.y = 2
    def print_surname(self):
        print ("Pupkin")


class MetaHuman(Human):
    def __init__(self):
        self.z = 3
    def print_age(self):
        print ("32")

obj1 = Human()
obj1.print_name()

obj2 = SuperHuman()
obj2.print_surname()
obj2.print_name()

obj3 = MetaHuman()
obj3.print_name()
obj3.print_age()


class Child(SuperHuman, MetaHuman):
    def __init__(self):
        super(Child, self).__init__()
        self.XYZ = 123
    def print_status(self):
        print ("trololo")


obj = Child()
obj.print_name()
obj.print_surname()
obj.print_age()
print obj.x
print obj.y
print obj.z




# more complicated example
import maya.cmds as cmds

class Car (object):
    def __init__(self, width=1, length=1, heigt=1, radius=1):
        self.width = width 
        self.length = length 
        self.heigt = heigt
        self.radius = radius 

        self.create_body()
        self.create_wheels()

    def create_body(self):

        if cmds.objExists("Body"):
            cmds.delete("Body")

        car_body = cmds.polyCube()
        self.car_body_node = car_body[1]
        self.car_body_name = car_body[0]

        cmds.setAttr(self.carBodyNode + ".width", self.width)     
        cmds.setAttr(self.carBodyNode + ".height", self.height)   
        cmds.setAttr(self.carBodyNode + ".depth", self.length) 

        cmds.xform(self.car_body_name, t=[0,self.radius/2,0], r=1)
        # cmds.xform(self.car_body_name, t=[0,5,0], r=1)

    def create_wheels(self):
        self.BB = cmds.xform(self.car_body_name, q=1, bb=1, ws=1)
        # print (self.car_BB)
        w1 = cmds.polySphere(n="wheel1", radius = self.radius)[0]
        cmds.xform(w1, ws=1, t=[self.BB[0], self.BB[1], self.BB[2]])

        w2 = cmds.polySphere(n="wheel2", radius = self.radius)[0]
        cmds.xform(w2, ws=1, t=[self.BB[3], self.BB[1], self.BB[2]])

        w3 = cmds.polySphere(n="wheel3", radius = self.radius)[0]
        cmds.xform(w3, ws=1, t=[self.BB[0], self.BB[1], self.BB[5]])

        w4 = cmds.polySphere(n="wheel4", radius = self.radius)[0]
        cmds.xform(w4, ws=1, t=[self.BB[3], self.BB[1], self.BB[5]])


class SuperCar(Car):
    def __init__(self, width=1, length=1, heigt=1, radius=1):
        super(SuperCar, self).__init__(width, length, heigt, radius)
        self.create_another_cube()

    def create_another_cube(self):
        cube = cmds.polyCube()[0]
        bb = cmds.xform(cube, q=1, bb=1, ws=1)
        bb_centerPointY = (bb[4] - bb[1])/2
        top = bb[4]
        # offset = top + bb_centerPointY 
        offset = top
        cmds.xform(cube, t = [0, offset, 0], r=1)


myCar = SuperCar(width=1, length=3, heigt=0.2, radius=0.2)
