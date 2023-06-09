lambda: print ("hello world")

lambda arg1=0, arg2=5344: bla bla 

# ---------- lambda 
# lambda is like a function

a = lambda x: x*x
b = lambda x: x*x*x
print a(6)
print b(6)


x = lambda a, b: a*b
print (x(3,4))

# ----------

def myFunc(n):
    return lambda a: a*n

double = myFunc(2)
triple = myFunc(3)

print (double(3), triple(5))


# ----------

# use lambda in QT, call function with a different values 
# so different buttons can call the same function, but with different args

    self.button.clicked.connect(lambda: self.my_funct(a=5, b=6, c=7))
def my_funct(self, a=0, b=1, c=2):
    print (a+b+c)

# emit a signal without creating a special function for it 
my_signal = QtCore.Signal()
    self.button.clicked.connect(lambda: self.mySignal.emit())


#---------- map 

# map, allows to do something with each element of a list

def power2(n):
    return n**2
# print (power2(5))

a = [1,2,3,4,5]
a_pow2 = map(power2, a)

print (a_pow2)


#-----
#freeze transformations for curves
import maya.cmds as cmds

def zero_transform(n):
    cmds.makeIdentity(n, apply=1, t=1, r=1, s=1, n=0, pn=1)
    cmds.rename(n, n+"_ZT")

curves = cmds.ls(sl=1)
curves_ZT = map(zero_transform, curves)

#-----

a = ["one", "two", "three"]
b = ["orange", "green", "blue"]
c = ["apple", "pineapple", "mellow"]

def foo(af, bf, cf):
    return "{} {} {}".format(af, bf, cf)

x = map(foo, a, b, c)
print (x)

# -------
# map + lambda
a = [1,2,3,4,5,6]

a_pow2 = map(lambda x: x*x, a)
print (a_pow2)


#------ filter 
# deletes some elements from a list

a = [1,-2,3,-4,5,-6]

new_list = filter(lambda x: x>0, a)
print (new_list)

# or

a = [1,-2,3,-4,5,-6]

def filt(x):
    if x > 0:
        return x

new_list = filter(filt, a)
print (new_list)

#------

# if any of elements (at least one element) is true 
a = [True, False, True, False, False, True]
print (any(a))

# if all elements are okay, not None and not zero, not false 
a = [1,2,3,4, None]

print (all(a))

#--------- reduce 
# apply some function to a element of a list, then the result of it apply to the next element of that list 

from functools import reduce

def foo(x,y):
    print ("{} * {} = {} ".format(x,y, x*y))
    return x*y

a = [x for x in range(1, 11)]
b = reduce(foo, a)

print b


# ------ what to google - python buit in functions

a = [1,3,5]
b = ["a", "b", "c"]

print (zip(a,b))


# w3schools.com/python 
# realpython.com


