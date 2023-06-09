from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds
from DragAndDropSample.WidgetField import WidgetField

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setObjectName("MyDragDropWidgetID")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setFixedSize(500, 500)
        self.setWindowTitle("Drag&Drop sample")

        # main layout
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setSpacing(1)
        self.main_layout.setContentsMargins(5,5,5,5)
        self.setLayout(self.main_layout)

        #add widget fields
        self.obj1 = WidgetField()
        self.obj1.add_test_buttons()
        self.main_layout.addWidget(self.obj1)

        self.obj2 = WidgetField()
        self.main_layout.addWidget(self.obj2)
        

def main():

    if cmds.window("MyDragDropWidgetID", exists=1):
        cmds.deleteUI("MyDragDropWidgetID")
    
    if cmds.windowPref("MyDragDropWidgetID", exists=1):
        cmds.windowPref("MyDragDropWidgetID", remove=1)
    
    global myDragDialog

    myDragDialog = MyDialog()
    myDragDialog.show()