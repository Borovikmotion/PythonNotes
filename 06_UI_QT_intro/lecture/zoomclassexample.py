import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore


    

class MyDialog(QtWidgets.QDialog):
    
    def __init__(self):
        
        super(MyDialog, self).__init__()
        
        self.setObjectName("MyBlahBlahBlah")
        self.setWindowTitle("My Dialog Window")
        self.setMinimumSize(300,200)
        self.setMaximumSize(500,500)
        self.setToolTip("Hello HoHoHo")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        
        # layout 
        
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment( QtCore.Qt.AlignTop )
        self.mainLayout.setContentsMargins(5,5,5,5)
        
        self.setLayout( self.mainLayout)
        
        # horizontal layout
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setSpacing(2)
        
        self.mainLayout.addLayout( self.buttonsLayout )
        
        self.btn1 = QtWidgets.QPushButton("Create")
        self.btn1.clicked.connect(self.createPressed)

        self.btn2 = QtWidgets.QPushButton("Apply")
        self.btn2.clicked.connect(self.applyPressed)
        
        self.btn3 = QtWidgets.QPushButton("Close")
        self.btn3.clicked.connect(self.close)
        
        self.buttonsLayout.addWidget(self.btn1)
        self.buttonsLayout.addWidget(self.btn2)
        self.buttonsLayout.addWidget(self.btn3)
        
        # extra widgets
        
        
        self.radLayout = QtWidgets.QHBoxLayout()
        
        self.rbtn1 = QtWidgets.QRadioButton("Sphere")
        self.rbtn1.setChecked(True)
        
        self.rbtn2 = QtWidgets.QRadioButton("Cone")
        self.rbtn3 = QtWidgets.QRadioButton("Cube")
        
        self.radLayout.addWidget(self.rbtn1)
        self.radLayout.addWidget(self.rbtn2)
        self.radLayout.addWidget(self.rbtn3)
        
        self.mainLayout.addLayout( self.radLayout )
        
        
    def createPressed(self):
        
        self.applyPressed()
            
        self.close()
        
        
    def applyPressed(self):
        
        if self.rbtn1.isChecked():
            cmds.polySphere()
        elif self.rbtn2.isChecked():
            cmds.polyCone()
        else:
            cmds.polyCube()
            
            
    def enterEvent(self, event):
        
        self.setCursor(QtCore.Qt.WaitCursor)
        
        self.rbtn2.setChecked(1)
        
        return QtWidgets.QWidget.enterEvent(self, event)
        
        
    def leaveEvent(self, event):
        
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.rbtn1.setChecked(1)
        
        
        return QtWidgets.QWidget.enterEvent(self, event)
        
        
    def mousePressEvent(self, event):
        
        print "Mouse was pressed"
        
        return QtWidgets.QWidget.mousePressEvent(self, event)
        




if cmds.window('MyBlahBlahBlah', q=1, exists=1):
    cmds.deleteUI('MyBlahBlahBlah')

# проверить если Maya хранит в себе настройки отображения нашего UI
if cmds.windowPref('MyBlahBlahBlah', exists = 1):
    cmds.windowPref('MyBlahBlahBlah', remove = 1)
    
    
MyWnd = MyDialog()
MyWnd.show()    


        
        