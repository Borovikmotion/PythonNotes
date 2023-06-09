import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin


class MyCheckBox(QtWidgets.QCheckBox):

    def __init__(self):
        super(MyCheckBox, self).__init__()

        self.background_color = "#777" 
        self.circle_color = "#eee"
        self.active_color = "#6db9ff"

        width = 40 #40
        height = 20 #20
        self.setFixedSize(width, height)

    def hitButton(self, pos):
        return self.contentsRect().contains(pos)

    def paintEvent(self, event):
        # --- DRAWING FUNCTIONS
        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.Antialiasing)

        # Pen
        # brush = QtGui.QBrush(QtGui.QColor(255,255,255,255))
        # pen = QtGui.QPen(brush, 5, QtCore.Qt.DashDotLine)
        p.setPen(QtCore.Qt.NoPen)

        # brush = QtGui.QBrush(QtGui.QColor(102, 212, 242, 255))
        # p.setBrush(brush)
        # p.drawEllipse(5,5, 80,80)

        if not self.isChecked():
            # ------------- Background
            p.setBrush(QtGui.QColor(self.background_color))
            p.drawRoundedRect(0,0, self.width(), self.height(), self.height()/2, self.height()/2)
            # ------------- Circle
            p.setBrush(QtGui.QColor(self.circle_color))
            p.drawEllipse(2,2, 16, 16)
        else:
            # ------------- Background
            p.setBrush(QtGui.QColor(self.background_color))
            p.drawRoundedRect(0,0, self.width(), self.height(), self.height()/2, self.height()/2)
            # ------------- Circle
            p.setBrush(QtGui.QColor(self.active_color))
            p.drawEllipse(self.width() - 18, 2, 16, 16)

        p.end()



class MyDialog(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()

        self.setFixedSize(400,400)
        self.setObjectName("MySuperDialogID")
        self.setWindowTitle("Custom Widget Example")

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.main_layout)

        # button
        self.btn = MyCheckBox()
        self.btn.toggled.connect(self.debug)
        self.main_layout.addWidget(self.btn)

        self.btn1 = MyCheckBox()
        self.btn1.toggled.connect(self.debug)
        self.main_layout.addWidget(self.btn1)

    def debug(self, state):
        print state


def main():
    
    
    if cmds.window("MySuperDialogID", exists=1):
        cmds.deleteUI("MySuperDialogID")

    if cmds.windowPref("MySuperDialogID", exists=1):
        cmds.windowPref("MySuperDialogID", remove=1)

    mydlg = MyDialog()
    mydlg.show()


