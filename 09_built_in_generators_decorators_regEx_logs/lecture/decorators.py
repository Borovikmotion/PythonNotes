def decorator(function):
    def wrapper():
        print "Before"
        function()
        print "After"
    return wrapper

@decorator
def doIt():
    print "Earth"

doIt()
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def decorator(function):
    def wrapper():
        print "Before"
        function()
        print "After"
    return wrapper
    
def AddLetter(function):
    def wrapper():
        print "A"
        function()
        print "B"
    return wrapper

@AddLetter
@decorator
def doIt():
    print "Earth"

doIt()
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
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

print add(3, 22)