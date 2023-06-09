import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from view import View
from scene import Scene



class MyGraphicsScene(QtWidgets.QDialog):
    def __init__(self):
        super(MyGraphicsScene, self).__init__()

        self.setFixedSize(800,800)
        self.setObjectName("MyGraphicsSceneID")
        self.setWindowTitle("My Graphics Scene")

        # main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.main_layout)

        # BASIC SETUP
        self.viewport = View()
        self.main_layout.addWidget(self.viewport)

        self.scene = Scene()

        self.viewport.setScene(self.scene)

        self.main_layout.addWidget(self.viewport)


        #selection signal
        self.scene.selectionChanged.connect(self.on_change_selection)
    
    def on_change_selection(self):
        self.scene.define_selection()


def main():

    if cmds.window("MyGraphicsSceneID", exists=1):
        cmds.deleteUI("MyGraphicsSceneID")
    
    if cmds.windowPref("MyGraphicsSceneID", exists=1):
        cmds.windowPref("MyGraphicsSceneID", remove=1)
    
    global mydlg

    mydlg = MyGraphicsScene()
    mydlg.show()
