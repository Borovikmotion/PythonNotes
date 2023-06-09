import maya.OpenMaya as om
import maya.cmds as cmds

OBJ_A = "locator1"
OBJ_B = "locator2"
OBJ_C = "locator3"


def axisToVector(obj = None, vec=om.MVector(1,0,0)):
    '''
    Get X axis World Vector
    '''

    if not obj:
        return

    selList = om.MSelectionList()
    om.MGlobal.getSelectionListByName(obj, selList)
    mDag = om.MDagPath()
    selList.getDagPath(0, mDag)

    fnTr = om.MFnTransform(mDag)

    quaternion = om.MQuaternion()
    fnTr.getRotation(quaternion, om.MSpace.kWorld)

    mat = quaternion.asMatrix()

    vec = (vec * mat).normal()

    return vec


def Up2Vec(objToRotate = None, vector = None):

    if not vector or not objToRotate:
        return

    selList = om.MSelectionList()
    selList.add(objToRotate)

    mdag = om.MDagPath()

    selList.getDagPath(0, mdag)

    fnT = om.MFnTransform(mdag)

    #Quaternion contans rotation angle between two vectors
    #If we rotate object by this quaternion
    # - object's Up vector (Y Axis) will match second vector
    quaternion = om.MQuaternion(om.MVector(0,1,0), vector)
    fnT.setRotation(om.MEulerRotation(0,0,0))
    fnT.rotateBy(quaternion)


def Vec2Vec(objToRotate = None, sideVector = None, aimVector=None):

    quaternion = om.MQuaternion(sideVector, aimVector)

    selList = om.MSelectionList()
    selList.add(objToRotate)
    mdag = om.MDagPath()
    selList.getDagPath(0, mdag)

    fnT = om.MFnTransform(mdag)
    fnT.rotateBy(quaternion)


def main():

    # Do initial rotation - Match YAxis with vector
    OBJ_A_Pos = cmds.xform(OBJ_A, q=1, ws=1, t=1)
    OBJ_B_Pos = cmds.xform(OBJ_B, q=1, ws=1, t=1)
    AB_Vector = om.MVector(OBJ_B_Pos[0] - OBJ_A_Pos[0], OBJ_B_Pos[1] - OBJ_A_Pos[1], OBJ_B_Pos[2] - OBJ_A_Pos[2])
    Up2Vec(objToRotate = OBJ_A, vector = AB_Vector)

    # Rotate object's axis to mach another vector
    OBJ_C_Pos = cmds.xform(OBJ_C, q=1, ws=1, t=1)
    AX_vector = axisToVector(obj = OBJ_A)

    AC_Vector = om.MVector(OBJ_C_Pos[0] - OBJ_A_Pos[0], OBJ_C_Pos[1] - OBJ_A_Pos[1], OBJ_C_Pos[2] - OBJ_A_Pos[2])
    AC_Vector = AC_Vector.normal()

    Vec2Vec(OBJ_A, AX_vector, AC_Vector)


main()