a = "pickle"
print dir (a)
print type (a)


# a simple class
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

cook_1 = Cook(name = "Alisa", age=24, level=80)
# print cook_1 

# call a function from a class
cook_1.fry(food="Potato")

cook_2 = Cook(name = "Bob", age=50, level=1)
cook_2.grill(food="Fish")





# same but enhanced
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
