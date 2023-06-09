#basic stuff

def decorator(function):
    def wrapper():
        print ("before")
        function()
        print ("after")
    return wrapper 

def do_something():
    print ("hello world")

# a = decorator(do_something)
# a()

@decorator
def do_something():
    print ("hello world")

@decorator
def do_other_thing():
    print("hello mars")

do_something()
do_other_thing()

print(do_something)
print(do_other_thing)


#call fuction without creating objects from class
@staicmethod
def do_something():
    print ("hello world")

#
@classmethod
def do_something():
    print ("hello world")



# ---- two or more decorators ------

def decorator(function):
    def wrapper():
        print ("before")
        function()
        print ("after")
    return wrapper 


def AddLetter(function):
    def wrapper():
        print ("A")
        function()
        print ("B")
    return wrapper

@AddLetter
@decorator
def do_something():
    print ("hello world")

do_something()


#------ decorators with arguments -------

def divide(divider):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return result/float(divider)
        return wrapper 
    return decorator

@divide(2)
def add(x,y):
    return x+y

print (add(5,6))


@log
@mail()
