import maya.cmds as cmds

from PySide2 import QtWidgets, QtGui, QtCore


class MyWindow( QtWidgets.QDialog ):
    
    def __init__(self):
        
        super(MyWindow, self).__init__()
        
        self.setObjectName("MyUniqueWindow")
        
        self.setFixedSize(300, 200)
        
        self.mainLayout = QtWidgets.QVBoxLayout()
        
        self.setLayout(self.mainLayout)
        
        self.button1 = QtWidgets.QPushButton("Hello")
        self.button1.clicked.connect(self.printHello)
        
        self.button2 = QtWidgets.QPushButton("Hello2")
        self.button3 = QtWidgets.QPushButton("Hello3")
        
        self.mainLayout.addWidget( self.button1)
        self.mainLayout.addWidget( self.button2)
        self.mainLayout.addWidget( self.button3)
        
        
    def printHello(self):
        
        print "hello"
        
        
        

if cmds.window("MyUniqueWindow", exists = 1):
    cmds.deleteUI("MyUniqueWindow")

if cmds.windowPref("MyUniqueWindow", exists = 1):
    cmds.windowPref("MyUniqueWindow", remove = 1)
    
    
a  = MyWindow()
a.show()