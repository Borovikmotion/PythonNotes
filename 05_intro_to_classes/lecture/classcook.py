class Cook(object):

    def __init__(self, cookName = None, cookAge = None, cookLevel = 0):
        # here we initialize the whole class for a specific object

        #cook personal data
        self.name = cookName
        self.age = cookAge
        self.level = cookLevel

        #we don't know food parameters, but we are going to calculate them
        self.food = None
        self.foodAge = None
        self.foodTaste = 0
        self.foodPrice = 0
        self.foodTasteDescription = ""

    def takeFood(self, food = None, foodAge = 1):

        #Reads food info and saves that info to class variables

        if food == None:
            print ("ERROR: I didn't get any food")

        self.food = food
        self.foodAge = foodAge

    def calculateFoodValue(self):

        #Calculates food taste and price

        self.foodTaste = self.level - self.foodAge

        if self.foodTaste > 70:
            self.foodPrice = "100$"
            self.foodTasteDescription = "Luxury"

        elif self.foodTaste < 70 and self.foodTaste > 40:
            self.foodPrice = "70$"
            self.foodTasteDescription = "Delicious"

        else:
            self.foodPrice = "30$"
            self.foodTasteDescription = "Regular"

    def serveFood(self):

        #final method

        self.calculateFoodValue()
        print (self.foodTasteDescription + " " + self.food + ", sir! The price is " + self.foodPrice)

    def fry(self):
        print (self.food + " has been fried")
        self.serveFood()

    def boil(self):
        print (self.food + " has been boiled")
        self.serveFood()

    def grill(self):
        print (self.food + " has been grilled")
        self.serveFood()


cook_1 = Cook(cookName = "Bob", cookAge = "45", cookLevel = 80) #create class object
cook_1.takeFood(food = "chiken", foodAge = 20) #execute class method
cook_1.grill() #execute another class method

"""
prints:
    chiken has been grilled
    Delicious chiken, sir! The price is 70$
"""

cook_1 = Cook(cookName = "Bill", cookAge = "25", cookLevel = 40) #create class object
cook_1.takeFood(food = "fish", foodAge = 8) #execute class method
cook_1.boil() #execute another class method

"""
prints:
    fish has been boiled
    Regular fish, sir! The price is 30$
"""