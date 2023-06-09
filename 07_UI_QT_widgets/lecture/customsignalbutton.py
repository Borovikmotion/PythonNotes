from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds


class HAHAHA(object):
    def __init__(self):
        self.x = 1
        self.y = 2



class MyButton(QtWidgets.QWidget):

    itClicked = QtCore.Signal(HAHAHA)

    def __init__(self, text=""):
        super(MyButton, self).__init__()
        self.text = text

        self.setMinimumSize(100,36)
        self.setMaximumHeight(36)

        # set widget property
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(80,80,80))
        self.setPalette(self.p)

        # layout
        self.main_layout = QtWidgets.QHBoxLayout()
        self.setContentsMargins(5,0,5,0)
        self.setLayout(self.main_layout)

        # label
        self.label = QtWidgets.QLabel(self.text)
        self.main_layout.addWidget(self.label)


    def mouseReleaseEvent(self, event):
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(90,90,90))
        self.setPalette(self.p)

        inst = HAHAHA()

        inst.x = 10
        inst.y = 13

        self.itClicked.emit(inst)


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


    
class MyCheckBox(QtWidgets.QCheckBox):
    def __init__(self, *args, **kwargs):
        super(MyCheckBox, self).__init__(*args, **kwargs)


    def mouseReleaseEvent(self, event):
        print "release"

        super(MyCheckBox, self).mouseReleaseEvent(event)

    def mousePressEvent(self, event):
        print "Pressed"

        super(MyCheckBox, self).mousePressEvent(event)





class MyParentDialog(QtWidgets.QDialog):

    def __init__(self, parent = None):

        super(MyParentDialog, self).__init__()

        self.setFixedSize(300,300)
        self.setObjectName("MyUniqueUI_ID")
        self.setWindowTitle("Parent")

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)


        #simple text field
        self.textField = QtWidgets.QLineEdit()

        self.mybtn = MyButton("My Happy Button")
        self.mybtn.itClicked.connect(self.on_mybtn_clicked)

        self.mych = MyCheckBox("HAHAHAH")

        #button
        self.button = QtWidgets.QPushButton("Run Another Window")
        self.button.clicked.connect(self.on_button_clicked)

        #compose main layout
        self.mainLayout.addWidget(self.textField)
        self.mainLayout.addWidget(self.mybtn)
        self.mainLayout.addWidget(self.mych)
        self.mainLayout.addWidget(self.button)


    def on_button_clicked(self):
        print "button Clicked"

    def on_mybtn_clicked(self, name):
        print "My Button Clicked", name.x, name.y




    



def main():
    
    
    if cmds.window("MyUniqueUI_ID", exists = 1):
        cmds.deleteUI("MyUniqueUI_ID")

    if cmds.windowPref("MyUniqueUI_ID", exists = 1):
        cmds.windowPref("MyUniqueUI_ID", remove = 1)

    global myCustomSignalExampleParentWindow

    myCustomSignalExampleParentWindow = MyParentDialog()
    myCustomSignalExampleParentWindow.show()


main()