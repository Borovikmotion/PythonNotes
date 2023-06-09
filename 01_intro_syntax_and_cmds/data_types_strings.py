""" типы данных  """
print type (x)
a = "1"
print float(a) 

a = None
b = 3
if a == b:
    print a 
else:
    print b 


""" модификация строк """
a = "x"
b = "y"
c = "z"
res = "Variables: {} {} {}".format(a,b,c) 
print res

""" WORK WITH STRINGS """

name = "VasyaPupkin"
print name[0]
print name.lower()
print name.upper()
print name.replace("Pup", "hyup")
print name.split("a")
print name.title()
age = 32
height = 185
print ("Name: {} age {} : height: {} ".format (name,age,height))
