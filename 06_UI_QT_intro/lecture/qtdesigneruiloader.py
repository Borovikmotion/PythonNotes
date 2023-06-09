import sys
import maya.cmds as cmds
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit
from PySide2.QtCore import QFile, QObject


class Form(QObject):

    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        
        # Read file into ui_file var
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        
        # load UI from ui_file
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        self.window.setObjectName("SomeUniqueName")
        ui_file.close()

        # make sure you have pushButton_4 in UI file
        self.button = self.window.findChild(QPushButton, 'btn_CreateSphere')
        self.button.clicked.connect(self.ok_handler)

        self.window.show()

    def ok_handler(self):
        print "Test 1 2 3"
        


myUI = Form('D:\\Dev\\Qt\\Test_04\\untitled1\\mainwindow.ui')