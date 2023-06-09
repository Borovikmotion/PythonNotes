# _________ CUSTOM BUTTON & CUSTOM SIGNAL ________________
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui

class MyButton(QtWidgets.QWidget):

    itClicked = QtCore.Signal(str, str, QtCore.QPoint)

    def __init__(self, text = ""):
        super(MyButton, self).__init__()
        self.text = text
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
        # mousePosition = event.pos()
        # x = mousePosition.x()
        # y = mousePosition.y()
        # self.itClicked.emit("Vasya", "Pupkin", x, y)

        mousePosition = event.pos()
        self.itClicked.emit("Vasya", "Pupkin", mousePosition)
    
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

        #simple text field
        self.textField = QtWidgets.QLineEdit()

        # #checkbox
        self.checkbox = QtWidgets.QCheckBox("MyCheckbox")
        self.checkbox.toggled.connect(self.on_checkbox_toggled)

        #button
        self.button = QtWidgets.QPushButton("Regular Button")
        self.button.clicked.connect(self.on_button_clicked)

        # custom button
        self.myButton = MyButton("CUSTOM BUTTON")
        self.myButton.itClicked.connect(self.on_my_btn_clicked)

        #compose main layout
        self.mainLayout.addWidget(self.textField)
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addWidget(self.checkbox)
        self.mainLayout.addWidget(self.myButton)

    def on_button_clicked(self):
        print("Button Pressed")
        checkbox_state = self.checkbox.isChecked()
    
    def on_checkbox_toggled(self, state):
        print("haha", state)

    def enterEvent(self, event):
        print ("entered")
    
    def mousePressEvent(self, event):
        print ("press")
        print (event.pos())

    # def on_my_btn_clicked(self, name, name2, x, y):
    #     print ("my button clicked", name, name2, x, y)

    def on_my_btn_clicked(self, name, name2, data ):
        print ("my button clicked", name, name2, data)

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