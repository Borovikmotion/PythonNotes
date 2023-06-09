a = "pickle"
print dir (a)
print type (a)

class Cook(object):

    def __init__(self, name="Default", age=0, level=0):
        # print ("cook is ready")
        self.name = name
        self.age = age
        self.level = level
        self.max_level = 80

    def level_up(self):
        if self.level < self.max_level:
            self.level = self.level + 1 

    def fry(self, food = None):
        self.level_up()
        print (food + " has been fried by " + self.name)

    def boil(self, food = None):
        self.level_up()
        print (food + " has beed boiled by " + self.name)

    def grill(self, food = None):
        self.level_up()
        print (food + " has beed grilled by " + self.name)

    # pass


cook_1 = Cook(name = "Alisa", age=24, level=80)
# print cook_1 
cook_1.fry(food="Potato")

cook_2 = Cook(name = "Bob", age=50, level=1)
cook_2.grill(food="Fish")










import maya.cmds as cmds

class Cook(object):

    def __init__(self, name="Default", age=0, level=0):
        # print ("cook is ready")
        self.name = name
        self.age = age
        self.level = level
        self.max_level = 80
        #food
        self.food = None
        self.food_age = 0
        self.food_taste = 0
        self.food_price = 0
        self.food_taste_description = "Default"

    def take_food(self, food=None, food_age=0):
        if food == None:
            cmds.error(self.name + " has no food to cook")
        
        self.food = food
        self.food_age = food_age
        print (self.name + " is ready to cook " + self.food + " with age " + str(self.food_age))

    def calculate_food_value(self):
        self.food_taste = self.level - self.food_age
        if self.food_taste >= 70:
            self.food_price  = "100$"
            self.food_taste_description = "luxury"

        elif self.food_taste < 70 and self.food_taste >= 40:
            self.food_price  = "70$"
            self.food_taste_description = "delicious"
        
        else:
            self.food_price  = "30$"
            self.food_taste_description = "regular"


    def level_up(self):
        if self.level < self.max_level:
            self.level = self.level + 1 

    def serve_food(self):
        self.calculate_food_value()
        print (self.food_taste_description + " " + self.food + ", sir! the price is " + str(self.food_price))
        self.level_up()

    def fry(self, food = None):
        print (self.food + " has been fried by " + self.name)
        self.serve_food()

    def boil(self, food = None):
        print (self.food + " has beed boiled by " + self.name)
        self.serve_food()

    def grill(self, food = None):
        print (self.food + " has beed grilled by " + self.name)
        self.serve_food()

    # pass


cook_1 = Cook(name = "Alisa", age=24, level=80)
# print cook_1 
cook_1.take_food(food="Potato", food_age=3)
cook_1.fry()

cook_2 = Cook(name = "Bob", age=50, level=30)
cook_2.take_food(food="Fish", food_age=1)
cook_2.grill()

for i in range(60):
    cook_2.boil()


# print cook_1.level 
# cook_1.name = "John"








import maya.cmds as cmds

class Human (object):

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
        print ("99")



obj1 = Human()
obj1.print_name()

obj2 = SuperHuman()
obj2.print_surname()
obj2.print_name()

obj3 = MetaHuman()
obj3.print_name()
obj3.print_age()









import maya.cmds as cmds

class Human (object):

    def __init__(self):
        self.x = 1
    def print_name(self):
        print ("Vasya")


class SuperHuman(Human):

    def __init__(self):
        super(SuperHuman, self).__init__()
        self.y = 2
        # super(SuperHuman, self).print_name()

        # or, old way:
        # Human.print_name(self)

    def print_surname(self):
        print ("Pupkin")


class MetaHuman(Human):

    def __init__(self):
        super(MetaHuman, self).__init__()
        self.z = 3
        # super(MetaHuman, self).print_name()

    def print_age(self):
        print ("32")


class Child(SuperHuman, MetaHuman):

    def __init__(self):
        super(Child, self).__init__()
        self.XYZ = 123
    
    def print_status(self):
        print ("trololo")


obj = Child ()
obj.print_name()
obj.print_surname()
obj.print_age()
print obj.x
print obj.y
print obj.z





import maya.cmds as cmds

class A (object):
    def __init__(self):
        self.x = 1

class B (A):
    def __init__(self):
        super(B, self).__init__()
        self.y = 1
        # var x is overrided
        self.x = 13

p = B()

print p.x
print p.y









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
        self.car_body_node = car_body
        self.car_body_name = car_body[0]

        cmds.setAttr(self.car_body_node + ".width", self.width)
        cmds.setAttr(self.car_body_node + ".height", self.heigt)
        cmds.setAttr(self.car_body_node + ".depth", self.length)

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
