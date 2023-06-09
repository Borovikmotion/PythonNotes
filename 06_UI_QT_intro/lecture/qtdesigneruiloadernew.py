import sys
import maya.cmds as cmds
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QObject


class Form(QObject):

    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        
        # Read file into ui_file var
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        
        # load UI from ui_file
        loader = QUiLoader()
        self.myDialog = loader.load(ui_file)
        ui_file.close()
        
        # YOU need to connect signals HERE:
        self.myDialog.button_OK.clicked.connect(self.on_button_OK_clicked)
        self.myDialog.button_Apply.clicked.connect(self.on_button_Apply_clicked)
        self.myDialog.button_Cancel.clicked.connect(self.myDialog.close)
        self.myDialog.show()


    def on_button_OK_clicked(self):
        
        self.on_button_Apply_clicked()
        self.myDialog.close()
        
        
    def on_button_Apply_clicked(self):
        if self.myDialog.rbutton_Sphere.isChecked():
            cmds.polySphere()
        elif self.myDialog.rbutton_Cube.isChecked():
            cmds.polyCube()
        elif self.myDialog.rbutton_Cone.isChecked():
            cmds.polyCone()
        

myUI = Form('D:/Dev/Qt/Test_03/dfvgdfg/mainwindow.ui')