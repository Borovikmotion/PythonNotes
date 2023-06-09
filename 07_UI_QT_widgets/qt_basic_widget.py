import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui

class ObjectWidget(QtWidgets.QWidget):
    def __init__(self, object_path):
        super(ObjectWidget, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(270, 44)
        self.setMaximumHeight(60)
        self.set_background()

        # layout
        self.main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.main_layout)

    def set_background(self, r=50, g=50, b=50):
        #set background
        self.setAutoFillBackground(True)
        self.p = QtGui.QPalette()

        # RGB
        self.p.setColor(self.backgroundRole(), QtGui.QColor(r,g,b))
        self.setPalette(self.p)

        # HSV
        # self.color = QtGui.QColor()
        # self.color.setHsv(146, 60, 100)
        # self.p.setColor(self.backgroundRole(), self.color)
        # self.setPalette(self.p)