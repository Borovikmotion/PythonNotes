""" ABOUT DICTIONARES  """
a = {"axX":0, "axY":1, "axZ":2}
print a["axY"]

a = {"X":0, "Y":1, "Z":2}
a["Z"] = 365



a = {"pSphere1":1, "pSphere2":2,"pSphere3":3,"pSphere4":{"x":1},"pSphere5":5 }

# get element
print a ["pSphere4"] ["x"]

# how to itterate a dictionary
for i in a:
    print i 
    print a[i]

for i in a.keys():
    print i

for i in a.values():
    print i 

for k, v in a.items():
    print k, v

# how to modify a dictionary
# add many elements
b = {'x':1, 'y':2, 'z':3}
a.update(b)
print a

#modify element
b["haha"]=123

# delete element
b.pop("y")
print b
