# BASIC WINDOW
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui

class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_UI()

    def setup_UI(self):
        self.setWindowTitle("My Custom Window")
        self.setMinimumSize(480, 360)
        self.setMaximumSize(1920, 1080)
        self.resize(480, 360)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.main_layout)


if cmds.window("MyTestUI", q=1, exists=True):
    cmds.deleteUI("MyTestUI")

if cmds.windowPref("MyTestUI", exists=True):
    cmds.windowPref("MyTestUI", remove=1)


a = MyWindow()
a.show()
