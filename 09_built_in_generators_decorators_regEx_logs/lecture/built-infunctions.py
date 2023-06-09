a = lambda x: x*x
b = lambda x: x*x*x
print a(6)
print b(3)

# ---------------------------------------------
x = lambda a,b: a * b
print x(3,4)

# ---------------------------------------------
def myfunc(n):
    return lambda a: a * n
double = myfunc(2)
print double(3)

# ---------------------------------------------
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtWidgets, QtGui, QtCore
class QDialogDebug(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    def __init__(self):
        super(QDialogDebug, self).__init__()
        self.setFixedSize(500,500)
        self.setObjectName("MyDebugDialogID")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)
        self.buttonOK = QtWidgets.QPushButton('Test')
        self.main_layout.addWidget(self.buttonOK)
        self.buttonAGA = QtWidgets.QPushButton('Test')
        self.main_layout.addWidget(self.buttonAGA)
        self.buttonOK.clicked.connect(lambda: self.print_it(do_print=False))
        self.buttonAGA.clicked.connect(lambda: self.print_it(do_print=True))
    def print_it(self, do_print=False):
        if do_print:
            print "YES"
        else:
            print "NO PRINT" 
def main():
    if cmds.window("MyDebugDialogID", exists=1):
        cmds.deleteUI("MyDebugDialogID")
    if cmds.windowPref("MyDebugDialogID", exists=1):
        cmds.windowPref("MyDebugDialogID", remove=1)
    myUI = QDialogDebug()
    myUI.show()
if __name__ == "__main__":
    main()

# ---------------------------------------------
def power2(n):
    return n**2
a = [1,2,3,4,5,6]
a_pow2 = map(power2, a)
print a_pow2

# ---------------------------------------------
import maya.cmds as cmds
def zero_transform(n):
    cmds.makeIdentity(n, apply=1, t=1, r=1, s=1, n=0, pn=1)
    cmds.rename(n, n+"_ZT")
curves = cmds.ls(sl=1)
curves_ZT = map(zero_transform, curves)

# ---------------------------------------------
a = ["one", "two", "three"]
b = ["orange", "green", "blue"]
c = ["apple", "pineapple", "mellow"]
def foo(af, bf, cf):
  return "{} {} {}".format(af, bf, cf)
x = map(foo, a, b, c)
print x

# ---------------------------------------------
a = [1,2,3,4,5,6]
a_pow2 = map(lambda x: x*x, a)
print a_pow2

# ---------------------------------------------
a = [1,2,3,4,5,6]
p2 = lambda x: x*x
a_pow2 = map(p2, a)

# ---------------------------------------------
a = [1,-2,3,-4,5,-6]
new_list = filter(lambda x: x < 0, a)
print new_list

# ---------------------------------------------
a = [1,-2,3,-4,5,-6]
def filt(x):
    if x < 0:
        return x
new_list = filter(filt, a)
print new_list
    
# ---------------------------------------------
a = [1234, 456, 23, None]
if any(a):
    print "YES"
print all(a)

# ---------------------------------------------
from functools import reduce
def foo(x,y):
  print ("{} * {} = {}".format(x, y, x*y))
  return x*y
a = [1,2,3,4,5]
b = reduce(foo, a)
print b

# ---------------------------------------------
a = [1,3,5]
b = ["a", "b", "c"]
print zip(a,b)