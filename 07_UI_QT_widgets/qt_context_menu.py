# ------------------------- CUSTOM MENU -------------------------------
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui

class MyButton(QtWidgets.QWidget):

    itClicked = QtCore.Signal()

    def __init__(self, text = ""):
        super(MyButton, self).__init__()
        self.text = text
        self.state = True

        # CONTEXT MENU 
        # self.popMenu = None
        # self.create_context_menu() # or use it like a separate function 
        self.popMenu = QtWidgets.QMenu(self)

        self.popMenuAdd = QtWidgets.QAction('Add object', self)
        self.popMenuAdd.setCheckable(True)
        self.popMenu.addAction(self.popMenuAdd)
        self.popMenuAdd.triggered.connect(self.testA)

        self.popMenu.addSeparator()

        self.popMenuDel = QtWidgets.QAction('Delete object', self)
        self.popMenu.addAction(self.popMenuDel)
        self.popMenuDel.triggered.connect(self.testB)

        # attributes
        self.setMouseTracking(True)  
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.onContextMenu)
        #---------------------------

        # UI
        self.setMinimumSize(100, 20)
        self.setMaximumHeight(40)

        # colors
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(80,80,80))
        self.setPalette(self.p)

        # layot
        self.main_layout = QtWidgets.QHBoxLayout()
        self.setContentsMargins(5,5,5,5)
        self.setLayout(self.main_layout)

        # label
        self.label_ = QtWidgets.QLabel(self.text)
        self.main_layout.addWidget(self.label_)

    def mouseReleaseEvent(self, event):
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(90,90,90))
        self.setPalette(self.p)

        if self.state == True:
            self.itClicked.emit()
    
    def enterEvent(self, event):
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(90,90,90))
        self.setPalette(self.p)
    
    def leaveEvent(self, event):
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(80,80,80))
        self.setPalette(self.p)
    
    def mousePressEvent(self, event):
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(100,100,100))
        self.setPalette(self.p)

        if event.buttons() == QtCore.Qt.LeftButton:
            print ("left")
            self.state = True
        elif event.buttons() == QtCore.Qt.RightButton:
            print ("Right")
            self.state = False

            # CONTEXT MENU 
            # self.popMenu.exec_(self.mapToGlobal(event.pos()))

    # def create_context_menu(self):
    #     self.popMenu = QtWidgets.QMenu(self)

    #     self.popMenuAdd = QtWidgets.QAction('Add object', self)
    #     self.popMenu.addAction(self.popMenuAdd)
    #     self.popMenuAdd.triggered.connect(self.testA)

    #     self.popMenuDel = QtWidgets.QAction('Delete object', self)
    #     self.popMenu.addAction(self.popMenuDel)
    #     self.popMenuDel.triggered.connect(self.testB)

    def onContextMenu(self, point):
        self.popMenu.exec_(self.mapToGlobal(point))

    def testA(self):
        print ("test A")

    def testB(self):
        print ("test B")

class MyParentDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(MyParentDialog, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setFixedSize(300,300)
        self.setObjectName("MyUniqueUI_ID")
        self.setWindowTitle("Parent")

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        # custom button
        self.myButton = MyButton("My custom button")
        self.myButton.itClicked.connect(self.on_my_btn_clicked)

        #compose main layout
        self.mainLayout.addWidget(self.myButton)

    def on_my_btn_clicked(self):
        print ("my button clicked")

def main():
    #window
    if cmds.window("MyCustomUI_Id", exists=1):
        cmds.deleteUI("MyCustomUI_Id")
    if cmds.windowPref("MyCustomUI_Id", exists=1):
        cmds.windowPref("MyCustomUI_Id", remove=1)

    global myUI
    myUI = MyParentDialog()
    myUI.show()

if __name__ == "__main__":
    main()



# drag drop events 
# q mouse events
# position 