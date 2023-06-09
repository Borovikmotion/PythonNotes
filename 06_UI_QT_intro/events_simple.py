# SIMPLE WINDOW, but MORE
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui
# from PySide2.QtWidgets import QHBoxLayout

class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()

        # EVENTS
    def enterEvent(self, event):
        print("enter")
        super(MyWindow, self).enterEvent(event)

    def leaveEvent(self, event):
        print("leave")
        super(MyWindow, self).leaveEvent(event)

    def mousePressEvent(self, event):
        print("press")
        super(MyWindow, self).mousePressEvent(event)

if cmds.window("MyTestUI", q=1, exists=True):
    cmds.deleteUI("MyTestUI")

if cmds.windowPref("MyTestUI", exists=True):
    cmds.windowPref("MyTestUI", remove=1)

a = MyWindow()
a.show()