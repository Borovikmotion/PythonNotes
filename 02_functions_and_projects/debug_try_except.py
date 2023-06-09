""" DEBUG """

print d["pSphere1"]

def scaleSphere(name, x, y, z):
    if x==0:
        print "x=0"
        x=1
    elif y==0:
        print "y=0"
        y=1
    elif z==0:
        print "z=0"
        z=1
    cmds.xform(name, a=1, s =[x,y,z])

# or raise an error with cmds or python method
def scaleSphere(name, x, y, z):
    if x==0 or y==0 or z==0:
        # print "dont use zero"
        # return 
        # raise AttributeError ("dont use zero")
        cmds.error("dont use zero")
    cmds.xform(name, a=1, s =[x,y,z])

scaleSphere("pSphere1", 1, 0, 3)


""" TRY EXCEPT """
# finnaly - a block of code which will be run anyway after try or exeption
def div(a,b):
    try:
        c = a/b
    except Exception as e:
        print e
        print "dont use zero"
        c = None
    finally:
        print "finally"
    return c

result =  div (4,0)

if result:
    print "yes"
else:
    print "no"