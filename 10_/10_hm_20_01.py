import maya.api.OpenMaya as om # OpenMaya 2.0
import maya.cmds as cmds

#get object and dag path 
objectName = cmds.ls(sl=1, l=1)[0]
selectionList = om.MSelectionList()
selectionList.add(objectName)
object_mDagPath = selectionList.getDagPath(0)

# grp = cmds.ls(sl=1, l=1)[1]
# sel_list2 = om.MSelectionList()
# sel_list2.add(grp)
# grp_mObject = sel_list2.getComponent(0)[1]

edge_iterator = om.MItMeshEdge(object_mDagPath)

while not edge_iterator.isDone():

    # get index 
    # print(edge_iterator.index())

    # returns number of vertex in the mesh, but it's not really necessary because we can get coordinates directly
    # vertex_1 = edge_iterator.vertexId(0)
    # vertex_2 = edge_iterator.vertexId(1)

    vertex_1_pos = edge_iterator.point(0, om.MSpace.kWorld)
    vertex_2_pos = edge_iterator.point(1, om.MSpace.kWorld)

    # # trying to create a curve throug open naya, fuck that shit, absolutely fucking disgusting api
    # array = om.MPointArray()
    # array.append(vertex_1_pos)
    # array.append(vertex_2_pos)
    # double_thing = om.MDoubleArray()
    # edge_curve = om.MFnNurbsCurve()
    # edge_curve.create(array, double_thing, 1, om.MFnNurbsCurve.kOpen, False, False, grp_mObject)

    # create curve
    crv = cmds.curve(p=[(vertex_1_pos[0], vertex_1_pos[1], vertex_1_pos[2]), (vertex_2_pos[0], vertex_2_pos[1], vertex_2_pos[2])], n="crv_", d = 1, ws=1)

    #get direction
    direction = [vertex_1_pos[0]-vertex_2_pos[0], vertex_1_pos[1]-vertex_2_pos[1],vertex_1_pos[2]-vertex_2_pos[2]]
    # or calculate tangent
    direction2 = cmds.pointOnCurve(crv, p=0, nt =1)
    #or do the same through vector in om 
    direction3 = om.MVector(vertex_1_pos[0]-vertex_2_pos[0], vertex_1_pos[1]-vertex_2_pos[1],vertex_1_pos[2]-vertex_2_pos[2])
    direction3.normalize

    #create circle
    profile = cmds.circle(c =[vertex_1_pos[0], vertex_1_pos[1], vertex_1_pos[2]], r = 0.5, nr = direction3)

    # extrude
    cmds.extrude(profile[0], crv, et=1)


    edge_iterator.next()
