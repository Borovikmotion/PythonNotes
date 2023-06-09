
import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin


class MyGraphicsScene(QtWidgets.QDialog):
    def __init__(self):
        super(MyGraphicsScene, self).__init__()

        self.setFixedSize(800,800)
        self.setObjectName("MyGraphicsSceneID")
        self.setWindowTitle("My Graphics Scene")

        # main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        # BASIC SETUP
        self.viewport = QtWidgets.QGraphicsView()
        self.main_layout.addWidget(self.viewport)

        self.scene = QtWidgets.QGraphicsScene()

        self.viewport.setScene(self.scene)
        self.viewport.setRenderHint(QtGui.QPainter.Antialiasing)

        self.main_layout.addWidget(self.viewport)


        # DRAW
        self.penWhite = QtGui.QPen(QtCore.Qt.white)
        self.brushRed = QtGui.QBrush(QtCore.Qt.red)
        self.brushBlue = QtGui.QBrush(QtCore.Qt.blue)

        ellipse = self.scene.addEllipse(20,20,200,200, self.penWhite, self.brushRed)
        rectangle = self.scene.addRect(-300, -300, 200, 200, self.penWhite, self.brushBlue)

        ellipse.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        ellipse.setZValue(2)
        rectangle.setZValue(1)


def main():

    if cmds.window("MyGraphicsSceneID", exists=1):
        cmds.deleteUI("MyGraphicsSceneID")
    
    if cmds.windowPref("MyGraphicsSceneID", exists=1):
        cmds.windowPref("MyGraphicsSceneID", remove=1)
    
    global mydlg

    mydlg = MyGraphicsScene()
    mydlg.show()
