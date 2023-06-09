from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setObjectName("MyDragDropWidgetID")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setFixedSize(500, 500)
        self.setWindowTitle("window expample")

        # main layout
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setSpacing(1)
        self.main_layout.setContentsMargins(5,5,5,5)
        self.setLayout(self.main_layout)


def main():

    if cmds.window("MyDragDropWidgetID", exists=1):
        cmds.deleteUI("MyDragDropWidgetID")
    
    if cmds.windowPref("MyDragDropWidgetID", exists=1):
        cmds.windowPref("MyDragDropWidgetID", remove=1)
    
    global myDragDialog

    myDragDialog = MyDialog()
    myDragDialog.show()