
""" Списки  """
a=["x", "y" ]
a.append ("z")

print a[2]

""" списки внутри списков """
a=["x", "y" ]
a.append("z")
a.append([1,2,3])
print a[3][2]

a.insert(0,"z")
a.remove("y")

a = [4,1,7,0,5]
a.sort()
print a


""" WORK WITH LISTS """
# basic operations like merge lists, delete enelements, add elemtns
a = ['x', 'y', 'z']
b = ['a', 'b', 'c']

a.append("RRR")
a = a + b 
a.extend(b)
a.insert(1,'RRR')
a.remove('z')
a.pop()
print(a)
print(a.index('x'))
print(len (a))
print(a.count('x'))
a.sort()
a.sort(reverse=True)



""" пройтись по списку в цикле """
a = ["x", "y", "z"]

for element in a:
    print element 

a = ["a", "b", "c"]

for index, value in enumerate(a):
    print index, value



# maya selection
# get list of selected objects, if translate Y < 0 then morrir it relatively to XZ plane
selection = cmds.ls(sl=1, l =1)
print (selection)
result = []

for obj in selection:
    # print obj 
    tr = cmds.xform(obj, q=1, t =1)
    ro = cmds.xform(obj, q=1, ro =1)
    sc = cmds.xform(obj, q=1, r=1, s =1)
    if tr[1] < 0:
        result.append(obj)
# print result

if len(result):
    for obj in result:
        tr = cmds.xform(obj, q=1, t =1)
        new_tr = [0,tr[1]*-1, 0]
        cmds.xform(obj, r=1, t = new_tr)
    print obj 

# same code, but optimized
for obj in selection:
    tr = cmds.xform(obj, q=1, t =1)
    if tr[1] < 0:
        new_tr = [0,tr[1]*-1, 0]
        cmds.xform(obj, r=1, t = new_tr)