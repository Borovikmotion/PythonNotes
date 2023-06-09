# example 1

util = maya.OpenMaya.MScriptUtil()
util.createFromDouble(0.0, 0.0, 0.0)
ptr = util.asDoublePtr() # create an actual pointer

# command that uses pointers
matrix.getShear(ptr, maya.OpenMaya.MSpace.kObject)

shearX = util.getDoubleArrayItem(ptr, 0)
shearY = util.getDoubleArrayItem(ptr, 1)
shearZ = util.getDoubleArrayItem(ptr, 2)



# example 2

util = OpenMaya.MScriptUtil()
util.createFromInt(0)
ptr = xutil.asUintPtr() # unsigned int pointer

# command that uses pointers
someFn.someMethod(ptr)

x = util.getUint(ptr)



# example 3

meshFn = maya.OpenMaya.MFnMesh(node)

u_util = maya.OpenMaya.MScriptUtil()
u_util.createFromDouble(0.0)
u_ptr = u_util.asFloatPtr()

v_util = maya.OpenMaya.MScriptUtil()
v_util.createFromDouble(0.0)
v_ptr = v_util.asFloatPtr()

meshFn.getUV(0, u_ptr, v_ptr)

u = u_util.getFloat(u_ptr)
v = v_util.getFloat(v_ptr))